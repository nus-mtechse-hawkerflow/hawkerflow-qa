"""Report figures for the scalability section, from the committed load-test evidence.

    python evidence/figures/make_figures.py      (from the hawkerflow-qa repo root; needs matplotlib)

Writes into evidence/figures/:
    fig1_run0_vs_run1.png   requests through the load balancer and tasks, run 0 vs run 1
    fig2_order_bottleneck.png  run 1: order tasks, CPU and queue backlog over the steps
"""

from __future__ import annotations

import csv
import datetime as dt
from collections import defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

HERE = Path(__file__).resolve().parent
LOADTEST = HERE.parent / "loadtest"
RUN0 = next(LOADTEST.glob("*run39062818294")) / "loadtest-step-2" / "metrics.csv"
RUN1 = next(LOADTEST.glob("*run39115915961")) / "loadtest-step-3" / "metrics.csv"

# Validated categorical order (dataviz validator: all checks pass on #fcfcfb).
COLOURS = {"order": "#2a78d6", "hawker": "#eb6834"}
SINGLE = "#2a78d6"
TEXT, TEXT_2, GRID, SURFACE, BAND = "#0b0b0b", "#52514e", "#e6e5e0", "#fcfcfb", "#f0efea"
LEAD_IN_MIN = 2  # collect_metrics windows start 2 minutes before k6

# Step plateaus in minutes after k6 starts: (start, end, offered req/s)
STEPS = {
    "run0": [(1, 6, 25), (7, 12, 50), (13, 18, 100), (19, 24, 200)],   # HOLD 5m
    "run1": [(1, 8, 25), (9, 16, 50), (17, 24, 100), (25, 32, 200)],   # HOLD 7m
}


def load(path: Path) -> dict:
    data: dict = defaultdict(lambda: defaultdict(lambda: ([], [])))
    rows = list(csv.DictReader(path.open()))
    t0 = min(dt.datetime.fromisoformat(r["timestamp"]) for r in rows) + dt.timedelta(minutes=LEAD_IN_MIN)
    for r in rows:
        xs, ys = data[r["panel"]][r["series"]]
        xs.append((dt.datetime.fromisoformat(r["timestamp"]) - t0).total_seconds() / 60)
        ys.append(float(r["value"]))
    return data


def style(ax, ylabel: str) -> None:
    ax.set_facecolor(SURFACE)
    ax.set_ylabel(ylabel, fontsize=8, color=TEXT_2)
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    ax.tick_params(colors=TEXT_2, labelsize=8, length=0)
    for spine in ("top", "right", "left"):
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color(GRID)
    ax.set_ylim(bottom=0)


def bands(ax, steps, label: bool) -> None:
    for a, b, rps in steps:
        ax.axvspan(a, b, color=BAND, zorder=0, linewidth=0)
        if label:
            ax.text((a + b) / 2, 1.02, f"{rps} req/s", transform=ax.get_xaxis_transform(),
                    ha="center", va="bottom", fontsize=7.5, color=TEXT_2)


def tasks(ax, data) -> None:
    for name in ("order", "hawker"):
        xs, ys = data["tasks"][name]
        ax.step(xs, ys, where="post", color=COLOURS[name], linewidth=2, label=name)
        ax.annotate(f"{name} {ys[-1]:.0f}", (xs[-1], ys[-1]), xytext=(4, 6 if name == "order" else -10),
                    textcoords="offset points", fontsize=8, color=TEXT_2, annotation_clip=False)
    ax.yaxis.get_major_locator().set_params(integer=True)


def fig1(run0, run1) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(11, 6))
    fig.patch.set_facecolor(SURFACE)
    for col, (key, data, title) in enumerate([
        ("run0", run0, "Run 0: API Gateway limit 50 req/s"),
        ("run1", run1, "Run 1: limit 500 req/s, max tasks order 5 / hawker 3"),
    ]):
        top, bottom = axes[0][col], axes[1][col]
        xs, ys = data["alb_requests"]["all"]
        top.plot(xs, ys, color=SINGLE, linewidth=2)
        style(top, "requests / min" if col == 0 else "")
        bands(top, STEPS[key], label=True)
        top.set_title(title, loc="left", fontsize=10, color=TEXT, fontweight="bold", pad=16)
        tasks(bottom, data)
        style(bottom, "running tasks" if col == 0 else "")
        bands(bottom, STEPS[key], label=False)
        bottom.set_xlabel("minutes since load started (shaded: held steps)", fontsize=8, color=TEXT_2)
        for ax in (top, bottom):
            ax.set_xlim(-LEAD_IN_MIN, STEPS[key][-1][1] + 3)
    req_max = max(max(d["alb_requests"]["all"][1]) for d in (run0, run1)) * 1.08
    task_max = max(max(ys) for d in (run0, run1) for _, ys in d["tasks"].values()) + 0.6
    for col in (0, 1):
        axes[0][col].set_ylim(0, req_max)
        axes[1][col].set_ylim(0, task_max)
    axes[0][0].annotate("flat at ~2,200/min:\nthe gateway rejects the rest", xy=(15, 2300), xytext=(9, 9500),
                        fontsize=8, color=TEXT_2, arrowprops={"arrowstyle": "-", "color": TEXT_2, "linewidth": 0.8})
    axes[1][0].legend(loc="upper left", fontsize=8, frameon=False, labelcolor=TEXT_2)
    fig.suptitle("Requests reaching the services, and tasks per service", x=0.01, ha="left",
                 fontsize=12, color=TEXT, fontweight="bold")
    fig.tight_layout(rect=(0, 0, 0.95, 0.95))
    fig.savefig(HERE / "fig1_run0_vs_run1.png", dpi=150, facecolor=SURFACE)
    plt.close(fig)


def fig2(run1) -> None:
    fig, axes = plt.subplots(3, 1, figsize=(9, 6.2), sharex=True)
    fig.patch.set_facecolor(SURFACE)
    xs, ys = run1["tasks"]["order"]
    axes[0].step(xs, ys, where="post", color=COLOURS["order"], linewidth=2)
    style(axes[0], "order tasks")
    axes[0].yaxis.get_major_locator().set_params(integer=True)
    xs, ys = run1["ecs_cpu"]["order"]
    axes[1].plot(xs, ys, color=COLOURS["order"], linewidth=2)
    axes[1].axhline(60, color=TEXT_2, linewidth=0.8, linestyle=(0, (4, 3)))
    axes[1].text(0, 62, "scaling target 60%", fontsize=7.5, color=TEXT_2)
    style(axes[1], "order CPU (%)")
    xs, ys = run1["sqs_visible"]["all"]
    axes[2].plot(xs, ys, color=COLOURS["order"], linewidth=2)
    style(axes[2], "orders waiting in queue")
    for i, ax in enumerate(axes):
        bands(ax, STEPS["run1"], label=(i == 0))
        ax.set_xlim(-LEAD_IN_MIN, 35)
    axes[2].annotate("CPU at 100% on 2 tasks → backlog peaks at 738\n(oldest 72 s); drains once order reaches 4–5 tasks",
                     xy=(23, 730), xytext=(26.5, 450), fontsize=8, color=TEXT_2,
                     arrowprops={"arrowstyle": "-", "color": TEXT_2, "linewidth": 0.8})
    axes[2].set_xlabel("minutes since load started (shaded: held steps)", fontsize=8, color=TEXT_2)
    fig.suptitle("Run 1: order scaled too slowly at 100 req/s, then caught up", x=0.01, ha="left",
                 fontsize=12, color=TEXT, fontweight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(HERE / "fig2_order_bottleneck.png", dpi=150, facecolor=SURFACE)
    plt.close(fig)


if __name__ == "__main__":
    r0, r1 = load(RUN0), load(RUN1)
    fig1(r0, r1)
    fig2(r1)
    print(f"Wrote {HERE / 'fig1_run0_vs_run1.png'}, {HERE / 'fig2_order_bottleneck.png'}")
