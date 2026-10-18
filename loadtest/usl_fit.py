"""Per-step results of a stepped k6 run, and a Universal Scalability Law fit for headroom.

Reads the per-step sub-metrics hawkerflow.js exports (tagged step:<rps>), the plateau
schedule and scenario start it logs, and (optionally) the CloudWatch metrics.csv from
collect_metrics.py. For each plateau it reports:

    achieved X      successful browse + checkout requests per second (useful work)
    orders/s        orders created, counted against the step the checkout started in
    gateway calls/s every request k6 sent, polls included and whatever the status
    429s            requests rejected by a rate limit (API Gateway throttling)
    R               mean SERVER response time: the load balancer's TargetResponseTime
                    average over the plateau (k6's own latency is mostly network between
                    the GitHub runner and the stack, ~220 ms in run 0)
    N = X * R       concurrency inside the system (Little's law)

and fits  C(n) = n / (1 + sigma (n - 1) + kappa n (n - 1))  to relative capacity
C = X / X0 at relative load n = N / N0 (base = lowest plateau). sigma is contention
(waiting on shared resources); kappa is coherency (crosstalk), which makes throughput
peak at n* = sqrt((1 - sigma) / kappa) and fall beyond it.

Only unthrottled plateaus are fitted: a plateau with any 429 measures the gateway,
not the services, so it is excluded (and the reason stated). Fewer than three usable
plateaus means no fit.

Caveat: k6 drives an open model (arrival rate) while the USL is defined for
concurrency. Plateaus where the platform keeps up show near-linear scaling; the fit
only becomes informative once a step pushes the system towards saturation.

Usage:
    python usl_fit.py --summary reports/k6-summary.json --k6-log reports/k6-output.txt \\
      [--metrics reports/metrics.csv] --out reports [--workload-rps 40]
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
from pathlib import Path

TEXT = "#0b0b0b"
TEXT_SECONDARY = "#52514e"
GRID = "#e6e5e0"
SURFACE = "#fcfcfb"
MEASURED = "#2a78d6"
EXCLUDED = "#a9a8a3"
FITTED = "#eb6834"

NAMES = ("stalls", "order_enqueue")


def read_log(log: Path) -> tuple[list[tuple[float, float, int]], dt.datetime | None]:
    """Plateaus [(start_s, end_s, rps)] and scenario start, from hawkerflow.js's log lines."""
    text = log.read_text(errors="replace").replace('\\"', '"')
    m = re.search(r"PLATEAUS: (\[.*?\])(?:\"|\s|$)", text, re.M)
    if not m:
        raise SystemExit(f"No PLATEAUS line in {log}: was the run made with the tagged hawkerflow.js?")
    plateaus = [(float(a), float(b), int(r)) for a, b, r in json.loads(m.group(1))]
    s = re.search(r"SCENARIO_START: (\S+?Z)", text)
    start = dt.datetime.fromisoformat(s.group(1).replace("Z", "+00:00")) if s else None
    return plateaus, start


def server_latency_ms(metrics_csv: Path | None, start: dt.datetime | None,
                      plateaus: list[tuple[float, float, int]]) -> dict[int, float]:
    """Mean ALB TargetResponseTime (ms) per plateau rate, from collect_metrics.py's CSV."""
    if not (metrics_csv and metrics_csv.exists() and start):
        return {}
    points = []
    with metrics_csv.open() as f:
        for row in csv.DictReader(f):
            if row["panel"] == "alb_avg":
                points.append((dt.datetime.fromisoformat(row["timestamp"]), float(row["value"])))
    out: dict[int, list[float]] = {}
    for a, b, rps in plateaus:
        # CloudWatch stamps a 1-minute datapoint with its start: keep minutes wholly inside.
        lo, hi = start + dt.timedelta(seconds=a), start + dt.timedelta(seconds=b)
        vals = [v for t, v in points if lo <= t and t + dt.timedelta(minutes=1) <= hi]
        out.setdefault(rps, []).extend(vals)
    return {rps: sum(v) / len(v) * 1000 for rps, v in out.items() if v}


def steps(summary: dict, plateaus, server_ms: dict[int, float]) -> list[dict]:
    metrics = summary["metrics"]
    seconds: dict[int, float] = {}
    for a, b, rps in plateaus:
        seconds[rps] = seconds.get(rps, 0) + (b - a)

    def val(key, field):
        return metrics.get(key, {}).get(field)

    rows = []
    for rps, secs in sorted(seconds.items()):
        count, weighted_ms, p95 = 0.0, 0.0, {}
        for name in NAMES:
            n = val(f"http_reqs{{name:{name},step:{rps},expected_response:true}}", "count") or 0
            count += n
            weighted_ms += n * (val(f"http_req_duration{{name:{name},step:{rps},expected_response:true}}", "avg") or 0)
            p95[name] = val(f"http_req_duration{{name:{name},step:{rps},expected_response:true}}", "p(95)")
        if not count:
            continue
        x = count / secs
        throttled = val(f"throttled_429{{step:{rps}}}", "count")
        failed = val(f"http_req_failed{{step:{rps}}}", "value")
        client_ms = weighted_ms / count
        r_ms, r_source = (server_ms[rps], "server") if rps in server_ms else (client_ms, "client")
        rows.append({
            "offered": rps, "x": x, "failed": failed,
            "orders_s": (val(f"orders_created{{step:{rps}}}", "count") or 0) / secs if f"orders_created{{step:{rps}}}" in metrics else None,
            "gateway_s": (val(f"http_reqs{{step:{rps}}}", "count") or 0) / secs if f"http_reqs{{step:{rps}}}" in metrics else None,
            "throttled": throttled,
            "r_ms": r_ms, "r_source": r_source, "client_ms": client_ms, "n": x * r_ms / 1000,
            "p95_stalls": p95["stalls"], "p95_enqueue": p95["order_enqueue"],
            "e2e_p95": val(f"order_e2e_ms{{step:{rps}}}", "p(95)"),
        })
    for r in rows:
        if r["throttled"] is not None:
            r["excluded"] = "429s at the gateway" if r["throttled"] > 0 else None
        else:  # older runs without the throttle counter: treat heavy failures as throttling
            r["excluded"] = "over 1% failed requests (likely gateway 429s)" if (r["failed"] or 0) > 0.01 else None
    return rows


def fit(rows: list[dict]) -> dict | None:
    import numpy as np

    pts = sorted((r["n"], r["x"]) for r in rows if not r["excluded"] and r["n"] > 0 and r["x"] > 0)
    if len(pts) < 3:
        return None
    n0, x0 = pts[0]
    n = np.array([p[0] / n0 for p in pts])
    c = np.array([p[1] / x0 for p in pts])
    xv, yv = n[1:] - 1, n[1:] / c[1:] - 1          # y = sigma x + kappa x (x + 1)
    a, b = np.linalg.lstsq(np.column_stack([xv, xv * (xv + 1)]), yv, rcond=None)[0]
    sigma, kappa = float(a), float(b)
    if kappa < 0:                                   # no retrograde region: Amdahl only
        kappa = 0.0
        sigma = float(xv @ yv / (xv @ xv)) if xv @ xv else 0.0
    sigma = min(max(sigma, 0.0), 1.0)

    def capacity(m):
        return m / (1 + sigma * (m - 1) + kappa * m * (m - 1))

    pred = capacity(n)
    ss_res = float(((c - pred) ** 2).sum())
    ss_tot = float(((c - c.mean()) ** 2).sum())
    out = {"sigma": sigma, "kappa": kappa, "n0": n0, "x0": x0, "capacity": capacity,
           "r2": 1 - ss_res / ss_tot if ss_tot else 1.0, "spread": float(n.max()), "points": len(pts)}
    if kappa > 0:
        n_star = ((1 - sigma) / kappa) ** 0.5
        out.update(n_star=n_star * n0, x_peak=x0 * capacity(n_star))
    elif sigma > 0:
        out.update(x_ceiling=x0 / sigma)            # asymptote of n / (1 + sigma (n - 1))
    return out


def plot(rows: list[dict], model: dict | None, path: Path, title: str) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    fig, ax = plt.subplots(figsize=(8, 4.5))
    fig.patch.set_facecolor(SURFACE)
    ax.set_facecolor(SURFACE)
    if model:
        top = max(max(r["n"] for r in rows), model.get("n_star", 0)) * 1.3
        grid = np.linspace(model["n0"], top, 200)
        ax.plot(grid, model["x0"] * model["capacity"](grid / model["n0"]), color=FITTED, linewidth=2,
                label=f"USL fit (σ={model['sigma']:.3f}, κ={model['kappa']:.4f})")
    used = [r for r in rows if not r["excluded"]]
    dropped = [r for r in rows if r["excluded"]]
    ax.scatter([r["n"] for r in used], [r["x"] for r in used], color=MEASURED, s=40, zorder=3, label="measured plateau")
    if dropped:
        ax.scatter([r["n"] for r in dropped], [r["x"] for r in dropped], color=EXCLUDED, s=40, zorder=3,
                   label="excluded (throttled)")
    for r in rows:
        ax.annotate(f"{r['offered']} rps offered", (r["n"], r["x"]), xytext=(6, -10),
                    textcoords="offset points", fontsize=8, color=TEXT_SECONDARY)
    source = "server" if all(r["r_source"] == "server" for r in rows) else "client (no server data)"
    ax.set_xlabel(f"Concurrency N = X·R  (R = {source} response time)", fontsize=9, color=TEXT_SECONDARY)
    ax.set_ylabel("Successful requests / s", fontsize=9, color=TEXT_SECONDARY)
    ax.set_title(title, loc="left", fontsize=11, color=TEXT, fontweight="bold")
    ax.set_xlim(left=0)
    ax.set_ylim(bottom=0)
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    ax.tick_params(colors=TEXT_SECONDARY, labelsize=8, length=0)
    for spine in ("top", "right", "left"):
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color(GRID)
    ax.legend(loc="lower right", fontsize=8, frameon=False, labelcolor=TEXT_SECONDARY)
    fig.tight_layout()
    fig.savefig(path, dpi=150, facecolor=SURFACE)
    plt.close(fig)


def report(rows: list[dict], model: dict | None, workload: float, path: Path) -> None:
    def num(v, fmt="{:,.0f}"):
        return "–" if v is None else fmt.format(v)

    lines = [
        "# Scalability: per-step results and USL fit", "",
        "Achieved X counts successful browse and checkout requests (useful work). Gateway calls include "
        "order polls and every status. R is the load balancer's mean response time (server side) unless marked client.", "",
        "| Offered (req/s) | Achieved X (req/s) | Orders/s | Gateway calls/s | 429s | Errors (all) | R (ms) | N | p95 browse (ms) | p95 enqueue (ms) | Order end-to-end p95 (ms) | In fit |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        err = "–" if r["failed"] is None else f"{r['failed'] * 100:.1f}%"
        r_txt = f"{r['r_ms']:.0f}" + ("" if r["r_source"] == "server" else " (client)")
        lines.append(
            f"| {r['offered']} | {r['x']:.1f} | {num(r['orders_s'], '{:.1f}')} | {num(r['gateway_s'], '{:.1f}')} | "
            f"{num(r['throttled'])} | {err} | {r_txt} | {r['n']:.2f} | {num(r['p95_stalls'])} | {num(r['p95_enqueue'])} | "
            f"{num(r['e2e_p95'])} | {'no: ' + r['excluded'] if r['excluded'] else 'yes'} |")
    lines.append("")

    if any(r["r_source"] == "client" for r in rows):
        lines += ["⚠️ No server-side latency for some plateaus (no `--metrics`, no `SCENARIO_START` in the k6 log, or no "
                  "load balancer datapoints), so their R is k6's client latency, which is mostly network. N is overstated.", ""]

    if not model:
        lines += ["**No USL fit:** needs at least three unthrottled plateaus with successful requests.", ""]
    else:
        lines += [f"**USL fit** on {model['points']} plateaus: σ (contention) = {model['sigma']:.3f}, "
                  f"κ (coherency) = {model['kappa']:.4f}, R² = {model['r2']:.3f} "
                  f"(relative to X₀ = {model['x0']:.1f} req/s at N₀ = {model['n0']:.2f}).", ""]
        if "x_peak" in model:
            lines.append(f"- Predicted peak: **{model['x_peak']:.0f} req/s** at concurrency N ≈ {model['n_star']:.1f}; "
                         "beyond that, throughput falls (retrograde scaling).")
            peak = model["x_peak"]
        elif "x_ceiling" in model:
            lines.append(f"- No retrograde region in the tested range (κ = 0). Contention alone caps throughput at about "
                         f"**{model['x_ceiling']:.0f} req/s** (asymptote X₀/σ).")
            peak = model["x_ceiling"]
        else:
            lines.append("- Near-linear scaling across the tested range: no contention measured, so no ceiling can be "
                         "estimated. Headroom is at least the highest achieved rate.")
            peak = None
        best = max(r["x"] for r in rows if not r["excluded"])
        if peak:
            lines.append(f"- Headroom over the {workload:.0f} req/s workload model: **{peak / workload:.1f}×** "
                         f"(highest measured: {best:.0f} req/s = {best / workload:.1f}×).")
        else:
            lines.append(f"- Headroom over the {workload:.0f} req/s workload model: **≥ {best / workload:.1f}×** "
                         f"(highest measured: {best:.0f} req/s).")
        if model["spread"] < 2:
            lines.append("- ⚠️ Concurrency varied less than 2× across the fitted plateaus, so the fit is weakly constrained.")
        lines.append("")
    lines += ["Caveat: k6 offers load at a fixed arrival rate (open model) while the USL is defined for concurrency; "
              "N is the concurrency each plateau actually ran at (Little's law)."]
    path.write_text("\n".join(lines) + "\n")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--summary", type=Path, required=True, help="k6 --summary-export JSON")
    p.add_argument("--k6-log", type=Path, required=True, help="k6 console output (PLATEAUS, SCENARIO_START lines)")
    p.add_argument("--metrics", type=Path, help="metrics.csv from collect_metrics.py, for server-side latency")
    p.add_argument("--workload-rps", type=float, default=40, help="workload model to compute headroom against")
    p.add_argument("--title", default="HawkerFlow throughput vs concurrency")
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    plateaus, start = read_log(args.k6_log)
    rows = steps(json.loads(args.summary.read_text()), plateaus, server_latency_ms(args.metrics, start, plateaus))
    if not rows:
        raise SystemExit("No per-step data in the summary: was the run made with the tagged hawkerflow.js?")
    model = fit(rows)
    report(rows, model, args.workload_rps, args.out / "usl.md")
    plot(rows, model, args.out / "usl.png", args.title)
    print(f"Wrote {args.out}/usl.md, usl.png")


if __name__ == "__main__":
    main()
