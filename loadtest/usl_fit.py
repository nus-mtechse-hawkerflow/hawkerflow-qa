"""Fit the Universal Scalability Law to a stepped k6 run and estimate headroom.

Reads the per-step sub-metrics that hawkerflow.js exports (successful browse and
checkout requests, tagged step:<rps>) and the plateau schedule it logs, then for
each plateau computes:

    X  achieved throughput  = successful requests / plateau seconds
    R  mean response time   (successful requests)
    N  concurrency          = X * R   (Little's law: requests in flight)

and fits  C(n) = n / (1 + sigma (n - 1) + kappa n (n - 1))  to the relative
capacity C = X / X0 at relative load n = N / N0 (base = lowest plateau).
sigma is contention (queueing on shared resources), kappa is coherency
(crosstalk); with kappa > 0 throughput peaks at n* = sqrt((1 - sigma) / kappa).

Outputs (in --out): usl.md (per-step table, fit, headroom) and usl.png.

Caveat: k6 drives an open model (arrival rate), and the USL is defined for
concurrency. Little's law gives the concurrency each plateau actually ran at;
plateaus where the platform kept up show near-linear scaling, so the fit is
only informative once some step pushes the system towards saturation.

Usage:
    python usl_fit.py --summary reports/k6-summary.json --k6-log reports/k6-output.txt \\
      --out reports [--workload-rps 40]
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

TEXT = "#0b0b0b"
TEXT_SECONDARY = "#52514e"
GRID = "#e6e5e0"
SURFACE = "#fcfcfb"
MEASURED = "#2a78d6"
FITTED = "#eb6834"

NAMES = ("stalls", "order_enqueue")


def read_plateaus(log: Path) -> dict[int, float]:
    """Total plateau seconds per rate, from the PLATEAUS line hawkerflow.js logs."""
    for line in log.read_text(errors="replace").splitlines():
        m = re.search(r"PLATEAUS: (\[.*?\])(?:\"|\s|$)", line.replace('\\"', '"'))
        if m:
            seconds: dict[int, float] = {}
            for start, end, rps in json.loads(m.group(1)):
                seconds[int(rps)] = seconds.get(int(rps), 0) + (end - start)
            return seconds
    raise SystemExit(f"No PLATEAUS line in {log}: was the run made with the tagged hawkerflow.js?")


def steps(summary: dict, plateau_s: dict[int, float]) -> list[dict]:
    metrics = summary["metrics"]
    rows = []
    for rps, secs in sorted(plateau_s.items()):
        count = 0.0
        weighted_ms = 0.0
        p95 = {}
        for name in NAMES:
            reqs = metrics.get(f"http_reqs{{name:{name},step:{rps},expected_response:true}}", {})
            dur = metrics.get(f"http_req_duration{{name:{name},step:{rps},expected_response:true}}", {})
            n = reqs.get("count", 0)
            count += n
            weighted_ms += n * dur.get("avg", 0)
            p95[name] = dur.get("p(95)")
        if not count:
            continue
        failed = metrics.get(f"http_req_failed{{step:{rps}}}", {}).get("value")
        e2e = metrics.get(f"order_e2e_ms{{step:{rps}}}", {})
        x = count / secs
        r_ms = weighted_ms / count
        rows.append({
            "offered": rps, "x": x, "r_ms": r_ms, "n": x * r_ms / 1000, "failed": failed,
            "p95_stalls": p95["stalls"], "p95_enqueue": p95["order_enqueue"],
            "e2e_avg": e2e.get("avg"), "e2e_p95": e2e.get("p(95)"),
        })
    return rows


def fit(rows: list[dict]) -> dict | None:
    import numpy as np

    pts = sorted((r["n"], r["x"]) for r in rows if r["n"] > 0 and r["x"] > 0)
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
           "r2": 1 - ss_res / ss_tot if ss_tot else 1.0, "max_n": float(n.max())}
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
    ns = [r["n"] for r in rows]
    xs = [r["x"] for r in rows]
    if model:
        top = max(max(ns), model.get("n_star", 0)) * 1.3
        grid = np.linspace(model["n0"], top, 200)
        ax.plot(grid, model["x0"] * model["capacity"](grid / model["n0"]), color=FITTED, linewidth=2,
                label=f"USL fit (σ={model['sigma']:.3f}, κ={model['kappa']:.4f})")
    ax.scatter(ns, xs, color=MEASURED, s=40, zorder=3, label="measured plateau")
    for r in rows:
        ax.annotate(f"{r['offered']} rps offered", (r["n"], r["x"]), xytext=(6, -10),
                    textcoords="offset points", fontsize=8, color=TEXT_SECONDARY)
    ax.set_xlabel("Concurrency N = X·R (requests in flight)", fontsize=9, color=TEXT_SECONDARY)
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
    def ms(v):
        return "–" if v is None else f"{v:,.0f}"

    lines = [
        "# Scalability: per-step results and USL fit", "",
        "Throughput counts successful browse and checkout requests only (order polls and errors excluded).", "",
        "| Offered (req/s) | Achieved X (req/s) | Achieved / offered | Errors (all requests) | Mean R (ms) | Concurrency N | p95 browse (ms) | p95 enqueue (ms) | Order end-to-end p95 (ms) |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        err = "–" if r["failed"] is None else f"{r['failed'] * 100:.1f}%"
        lines.append(f"| {r['offered']} | {r['x']:.1f} | {r['x'] / r['offered'] * 100:.0f}% | {err} | {r['r_ms']:.0f} | "
                     f"{r['n']:.2f} | {ms(r['p95_stalls'])} | {ms(r['p95_enqueue'])} | {ms(r['e2e_p95'])} |")
    lines.append("")

    if not model:
        lines += ["**No USL fit:** needs at least three plateaus with successful requests.", ""]
    else:
        lines += [f"**USL fit:** σ (contention) = {model['sigma']:.3f}, κ (coherency) = {model['kappa']:.4f}, "
                  f"R² = {model['r2']:.3f} (relative to the lowest plateau, X₀ = {model['x0']:.1f} req/s at N₀ = {model['n0']:.2f}).", ""]
        if "x_peak" in model:
            lines.append(f"- Predicted peak: **{model['x_peak']:.0f} req/s** at concurrency N ≈ {model['n_star']:.1f}; "
                         "beyond that, throughput falls (retrograde scaling).")
            peak = model["x_peak"]
        elif "x_ceiling" in model:
            lines.append(f"- No retrograde region in the tested range (κ = 0). Contention alone caps throughput at about "
                         f"**{model['x_ceiling']:.0f} req/s** (asymptote X₀/σ).")
            peak = model["x_ceiling"]
        else:
            lines.append("- Near-linear scaling across the tested range: no contention measured, so no ceiling can be estimated yet. "
                         "Run a higher step to find the knee.")
            peak = None
        if peak:
            lines.append(f"- Headroom over the {workload:.0f} req/s workload model: **{peak / workload:.1f}×**.")
        if model["max_n"] < 2:
            lines.append("- ⚠️ Concurrency varied less than 2× across plateaus, so the fit is weakly constrained.")
        lines.append("")
    if any((r["failed"] or 0) > 0.01 for r in rows):
        lines += ["⚠️ Some plateaus had more than 1% failed requests. If they are `429`s, API Gateway throttling "
                  "(not the services) limited throughput at that step.", ""]
    lines += ["Caveat: k6 offers load at a fixed arrival rate (open model) while the USL is defined for concurrency; "
              "N here is the concurrency each plateau actually ran at (Little's law)."]
    path.write_text("\n".join(lines) + "\n")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--summary", type=Path, required=True, help="k6 --summary-export JSON")
    p.add_argument("--k6-log", type=Path, required=True, help="k6 console output containing the PLATEAUS line")
    p.add_argument("--workload-rps", type=float, default=40, help="workload model to compute headroom against")
    p.add_argument("--title", default="HawkerFlow throughput vs concurrency")
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    rows = steps(json.loads(args.summary.read_text()), read_plateaus(args.k6_log))
    if not rows:
        raise SystemExit("No per-step data in the summary: was the run made with the tagged hawkerflow.js?")
    model = fit(rows)
    report(rows, model, args.workload_rps, args.out / "usl.md")
    plot(rows, model, args.out / "usl.png", args.title)
    print(f"Wrote {args.out}/usl.md, usl.png")


if __name__ == "__main__":
    main()
