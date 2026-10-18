"""Pull CloudWatch metrics for a load-test window and chart the scaling behaviour.

This turns a k6 run into report evidence: did ECS add Order tasks when the queue
backed up, how fast, and did latency hold? Outputs (in --out):

    metrics.csv       every datapoint (long format), the table view of the charts
    scaling.png       small multiples on one shared time axis
    summary.md        headline numbers for the report

Usage (needs AWS credentials with cloudwatch:GetMetricData):

    python collect_metrics.py \
      --start 2026-10-15T13:00:00+08:00 --end 2026-10-15T13:35:00+08:00 \
      --cluster hawkerflow-dev \
      --service order=hawkerflow-order --service hawker=hawkerflow-hawker \
      --service customer=hawkerflow-customer --service analytics=hawkerflow-analytics \
      --alb app/hawkerflow-dev-alb/0123456789abcdef \
      --queue order_queue --db hawkerflow-dev \
      --out reports/step-run-1

Re-plot without AWS from an earlier CSV:  python collect_metrics.py --from-csv reports/x/metrics.csv --out reports/x

Running task counts come from Container Insights (ECS/ContainerInsights namespace);
enable containerInsights on the cluster or that panel will be empty.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
from collections import defaultdict
from pathlib import Path

# Fixed categorical order: colour follows the service, never its rank.
SERVICE_COLOURS = {
    "order": "#2a78d6",
    "hawker": "#eb6834",
    "customer": "#1baf7a",
    "analytics": "#eda100",
}
SINGLE_COLOUR = "#2a78d6"
TEXT = "#0b0b0b"
TEXT_SECONDARY = "#52514e"
GRID = "#e6e5e0"
SURFACE = "#fcfcfb"

# (panel key, title, unit) in display order
PANELS = [
    ("tasks", "Running tasks per service", "tasks"),
    ("ecs_cpu", "ECS CPU per service", "% CPU"),
    ("alb_requests", "Requests through the load balancer", "requests / min"),
    ("alb_p95", "Load balancer target response time, p95", "seconds"),
    ("sqs_visible", "Order queue backlog", "messages waiting"),
    ("sqs_age", "Age of oldest queued order", "seconds"),
    ("rds_cpu", "RDS CPU", "% CPU"),
    ("rds_conn", "RDS connections", "connections"),
]


def build_queries(args) -> list[dict]:
    """One GetMetricData query per (panel, series)."""
    queries = []

    def add(panel, series, namespace, metric, dims, stat):
        queries.append(
            {
                "panel": panel,
                "series": series,
                "Id": f"q{len(queries)}",
                "MetricStat": {
                    "Metric": {
                        "Namespace": namespace,
                        "MetricName": metric,
                        "Dimensions": [{"Name": k, "Value": v} for k, v in dims.items()],
                    },
                    "Period": 60,
                    "Stat": stat,
                },
            }
        )

    for label, name in args.service:
        dims = {"ClusterName": args.cluster, "ServiceName": name}
        add("tasks", label, "ECS/ContainerInsights", "RunningTaskCount", dims, "Maximum")
        add("ecs_cpu", label, "AWS/ECS", "CPUUtilization", dims, "Average")

    if args.alb:
        lb = {"LoadBalancer": args.alb}
        add("alb_requests", "all", "AWS/ApplicationELB", "RequestCount", lb, "Sum")
        add("alb_p95", "all", "AWS/ApplicationELB", "TargetResponseTime", lb, "p95")
        # Mean server-side latency (not plotted): usl_fit.py uses it for concurrency N = X * R,
        # because k6's latency is mostly network between the runner and the stack.
        add("alb_avg", "all", "AWS/ApplicationELB", "TargetResponseTime", lb, "Average")

    if args.queue:
        q = {"QueueName": args.queue}
        add("sqs_visible", "all", "AWS/SQS", "ApproximateNumberOfMessagesVisible", q, "Maximum")
        add("sqs_age", "all", "AWS/SQS", "ApproximateAgeOfOldestMessage", q, "Maximum")

    if args.db:
        d = {"DBInstanceIdentifier": args.db}
        add("rds_cpu", "all", "AWS/RDS", "CPUUtilization", d, "Average")
        add("rds_conn", "all", "AWS/RDS", "DatabaseConnections", d, "Maximum")

    return queries


def fetch(args) -> list[dict]:
    import boto3  # imported here so --from-csv works without boto3

    cw = boto3.client("cloudwatch", region_name=args.region)
    queries = build_queries(args)
    meta = {q["Id"]: q for q in queries}
    rows = []

    for i in range(0, len(queries), 400):  # API limit: 500 queries per call
        batch = [{"Id": q["Id"], "MetricStat": q["MetricStat"], "ReturnData": True} for q in queries[i : i + 400]]
        token = None
        while True:
            kwargs = {"MetricDataQueries": batch, "StartTime": args.start, "EndTime": args.end, "ScanBy": "TimestampAscending"}
            if token:
                kwargs["NextToken"] = token
            resp = cw.get_metric_data(**kwargs)
            for result in resp["MetricDataResults"]:
                q = meta[result["Id"]]
                for ts, value in zip(result["Timestamps"], result["Values"]):
                    rows.append({"timestamp": ts.isoformat(), "panel": q["panel"], "series": q["series"], "value": value})
            token = resp.get("NextToken")
            if not token:
                break

    # ALB RequestCount per minute is already a 60-s sum; nothing to convert.
    rows.sort(key=lambda r: (r["panel"], r["series"], r["timestamp"]))
    return rows


def write_csv(rows: list[dict], path: Path) -> None:
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp", "panel", "series", "value"])
        writer.writeheader()
        writer.writerows(rows)


def read_csv(path: Path) -> list[dict]:
    with path.open() as f:
        return [{**r, "value": float(r["value"])} for r in csv.DictReader(f)]


def group(rows: list[dict]) -> dict:
    data: dict = defaultdict(lambda: defaultdict(lambda: ([], [])))
    for r in rows:
        ts = dt.datetime.fromisoformat(r["timestamp"])
        xs, ys = data[r["panel"]][r["series"]]
        xs.append(ts)
        ys.append(r["value"])
    return data


def _label_line_ends(ax, ends: list[tuple], integer: bool, min_gap_px: float = 11) -> None:
    """Direct-label each line at its end with name and value, nudging labels apart
    vertically so series that end on the same value stay readable."""
    if not ends:
        return
    ax.figure.canvas.draw()  # finalise limits so data->pixel transforms are correct
    placed = []
    for name, x, y in sorted(ends, key=lambda e: e[2]):
        px = ax.transData.transform((0, y))[1]
        target = max(px, placed[-1] + min_gap_px) if placed else px
        placed.append(target)
        value = f"{y:.0f}" if integer or abs(y) >= 10 else f"{y:.2g}"
        ax.annotate(
            f"{name} {value}", (x, y), xytext=(6, (target - px) * 72 / ax.figure.dpi),
            textcoords="offset points", color=TEXT_SECONDARY, fontsize=8,
            va="center", ha="left", annotation_clip=False,
        )


def plot(rows: list[dict], path: Path, title: str) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.dates as mdates
    import matplotlib.pyplot as plt

    data = group(rows)
    panels = [p for p in PANELS if p[0] in data]
    if not panels:
        raise SystemExit("No datapoints to plot: check the time window and dimension names.")

    fig, axes = plt.subplots(len(panels), 1, figsize=(11, 2.3 * len(panels)), sharex=True)
    axes = [axes] if len(panels) == 1 else list(axes)
    fig.patch.set_facecolor(SURFACE)

    for ax, (key, panel_title, unit) in zip(axes, panels):
        ax.set_facecolor(SURFACE)
        series = data[key]
        multi = len(series) > 1 or next(iter(series)) != "all"
        ends = []
        for name in [s for s in SERVICE_COLOURS if s in series] + [s for s in series if s not in SERVICE_COLOURS]:
            xs, ys = series[name]
            colour = SERVICE_COLOURS.get(name, SINGLE_COLOUR)
            if key == "tasks":
                ax.step(xs, ys, where="post", color=colour, linewidth=2, label=name)
            else:
                ax.plot(xs, ys, color=colour, linewidth=2, label=name)
            if multi and xs:
                ends.append((name, xs[-1], ys[-1]))
        ax.set_title(panel_title, loc="left", fontsize=10, color=TEXT, fontweight="bold")
        ax.set_ylabel(unit, fontsize=8, color=TEXT_SECONDARY)
        ax.set_ylim(bottom=0)
        _label_line_ends(ax, ends, key == "tasks")
        ax.grid(axis="y", color=GRID, linewidth=0.8)
        ax.tick_params(colors=TEXT_SECONDARY, labelsize=8, length=0)
        for spine in ("top", "right", "left"):
            ax.spines[spine].set_visible(False)
        ax.spines["bottom"].set_color(GRID)
        if multi:
            ax.legend(loc="upper left", fontsize=8, frameon=False, ncol=4, labelcolor=TEXT_SECONDARY)
        if key == "tasks":
            ax.yaxis.get_major_locator().set_params(integer=True)

    axes[-1].xaxis.set_major_formatter(mdates.DateFormatter("%H:%M", tz=dt.timezone(dt.timedelta(hours=8))))
    axes[-1].set_xlabel("Time (SGT)", fontsize=8, color=TEXT_SECONDARY)
    fig.suptitle(title, x=0.01, ha="left", fontsize=12, color=TEXT, fontweight="bold")
    fig.tight_layout(rect=(0, 0, 0.93, 0.98))
    fig.savefig(path, dpi=150, facecolor=SURFACE)
    plt.close(fig)


def summarise(rows: list[dict], path: Path, cpu_target: float = 60) -> None:
    data = group(rows)
    lines = ["# Scaling evidence summary", ""]

    # Load start: first minute the load balancer carried meaningful traffic (the window
    # also includes an idle lead-in, which must not count towards scale-out time).
    load_start = None
    if "alb_requests" in data:
        xs, ys = data["alb_requests"]["all"]
        if ys:
            load_start = next((x for x, y in zip(xs, ys) if y >= 0.1 * max(ys)), None)

    def minutes(a, b):
        return f"{(b - a).total_seconds() / 60:.0f}" if a and b else "–"

    if "tasks" in data:
        lines += [
            f"| Service | Tasks at start | Peak tasks | Load start → first scale-out (min) | CPU > {cpu_target:.0f}% → first scale-out (min) |",
            "|---|---|---|---|---|",
        ]
        for name, (xs, ys) in data["tasks"].items():
            if not ys:
                continue
            start = ys[0]
            first = next((x for x, y in zip(xs, ys) if y > start), None)
            if not first:
                lines.append(f"| {name} | {start:.0f} | {max(ys):.0f} | no scale-out | – |")
                continue
            # The breach that triggered it: first CPU datapoint above target before the scale-out.
            breach = None
            if name in data.get("ecs_cpu", {}):
                cx, cy = data["ecs_cpu"][name]
                breach = next((x for x, y in zip(cx, cy) if y > cpu_target and x <= first), None)
            lines.append(f"| {name} | {start:.0f} | {max(ys):.0f} | {minutes(load_start, first)} | "
                         f"{minutes(breach, first) if breach else '– (not CPU-triggered)'} |")
        lines += ["", "Times are at CloudWatch's 1-minute resolution. A scale-out without a prior CPU breach was "
                  "triggered by another target (hawker: requests per task; order: queue backlog per task).", ""]

    def peak(panel, label, fmt):
        if panel in data:
            values = [v for _, (_, ys) in data[panel].items() for v in ys]
            if values:
                lines.append(f"- {label}: {fmt(max(values))}")

    peak("alb_requests", "Peak requests per minute", lambda v: f"{v:,.0f}")
    peak("alb_p95", "Worst 1-min p95 target response time", lambda v: f"{v * 1000:,.0f} ms")
    peak("sqs_visible", "Peak order-queue backlog", lambda v: f"{v:,.0f} messages")
    peak("sqs_age", "Oldest queued order", lambda v: f"{v:,.0f} s")
    peak("rds_cpu", "Peak RDS CPU", lambda v: f"{v:.0f}%")
    peak("rds_conn", "Peak RDS connections", lambda v: f"{v:.0f}")
    path.write_text("\n".join(lines) + "\n")


def parse_args():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--start", type=dt.datetime.fromisoformat)
    p.add_argument("--end", type=dt.datetime.fromisoformat)
    p.add_argument("--region", default="ap-southeast-1")
    p.add_argument("--cluster")
    p.add_argument(
        "--service", action="append", default=[], metavar="LABEL=ECS_SERVICE_NAME",
        type=lambda s: tuple(s.split("=", 1)), help="repeat per service; label is order|hawker|customer|analytics",
    )
    p.add_argument("--alb", help="ALB dimension value, e.g. app/<name>/<id>")
    p.add_argument("--queue", help="SQS queue name (not URL)")
    p.add_argument("--db", help="RDS DB instance identifier")
    p.add_argument("--title", default="HawkerFlow under load")
    p.add_argument("--cpu-target", type=float, default=60, help="auto-scaling CPU target, for the scale-out timing")
    p.add_argument("--from-csv", type=Path, help="re-plot an earlier metrics.csv without AWS")
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    if not args.from_csv and not (args.start and args.end and args.cluster):
        p.error("--start, --end and --cluster are required unless --from-csv is given")
    return args


def main():
    args = parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    if args.from_csv:
        rows = read_csv(args.from_csv)
    else:
        rows = fetch(args)
        write_csv(rows, args.out / "metrics.csv")
    plot(rows, args.out / "scaling.png", args.title)
    summarise(rows, args.out / "summary.md", args.cpu_target)
    print(f"Wrote {args.out}/scaling.png, summary.md" + ("" if args.from_csv else ", metrics.csv"))


if __name__ == "__main__":
    main()
