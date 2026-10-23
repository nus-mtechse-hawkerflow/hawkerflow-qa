"""Slide-sized figures (16:9, 1920x1080, large text) for the scalability presentation.

    python evidence/figures/make_slide_figures.py      (from the hawkerflow-qa repo root; needs matplotlib)

Writes into evidence/figures/slides/:
    s2_run0_gateway_cap.png        run 0: requests reaching the services flatten at the gateway limit
    s3_run1_scaling.png            run 1: requests and tasks per service rising with the load
    s4_order_backlog_run1_vs_run2.png  order queue backlog and order tasks, run 1 vs run 2 (HA)
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
OUT = HERE / "slides"
LOADTEST = HERE.parent / "loadtest"
RUNS = {
    "run0": next(LOADTEST.glob("*run39062818294")) / "loadtest-step-2" / "metrics.csv",
    "run1": next(LOADTEST.glob("*run39115915961")) / "loadtest-step-3" / "metrics.csv",
    "run2": next(LOADTEST.glob("*run39974647663")) / "loadtest-step-4" / "metrics.csv",
}
STEPS = {  # held plateaus, minutes after k6 starts
    "run0": [(1, 6, 25), (7, 12, 50), (13, 18, 100), (19, 24, 200)],
    "run1": [(1, 8, 25), (9, 16, 50), (17, 24, 100), (25, 32, 200)],
    "run2": [(1, 8, 25), (9, 16, 50), (17, 24, 100), (25, 32, 200)],
}
LEAD_IN_MIN = 2

# Same validated categorical colours as the report figures; the earlier run is drawn in
# a muted grey as the baseline, the later run in blue, both directly labelled.
ORDER, HAWKER, BASELINE = "#2a78d6", "#eb6834", "#a9a8a3"
TEXT, TEXT_2, GRID, SURFACE, BAND = "#0b0b0b", "#52514e", "#e6e5e0", "#ffffff", "#f2f1ec"
FS = {"title": 30, "label": 18, "tick": 16, "note": 17, "band": 16}


def load(path: Path) -> dict:
    data: dict = defaultdict(lambda: defaultdict(lambda: ([], [])))
    rows = list(csv.DictReader(path.open()))
    t0 = min(dt.datetime.fromisoformat(r["timestamp"]) for r in rows) + dt.timedelta(minutes=LEAD_IN_MIN)
    for r in rows:
        xs, ys = data[r["panel"]][r["series"]]
        xs.append((dt.datetime.fromisoformat(r["timestamp"]) - t0).total_seconds() / 60)
        ys.append(float(r["value"]))
    return data


def new(rows: int = 1):
    fig, axes = plt.subplots(rows, 1, figsize=(12.8, 7.2), sharex=True)
    fig.patch.set_facecolor(SURFACE)
    return fig, ([axes] if rows == 1 else list(axes))


def style(ax, ylabel: str, steps, xmax: float, band_labels: bool) -> None:
    ax.set_facecolor(SURFACE)
    for a, b, rps in steps:
        ax.axvspan(a, b, color=BAND, zorder=0, linewidth=0)
        if band_labels:
            ax.text((a + b) / 2, 1.02, f"{rps} req/s", transform=ax.get_xaxis_transform(),
                    ha="center", va="bottom", fontsize=FS["band"], color=TEXT_2)
    ax.set_ylabel(ylabel, fontsize=FS["label"], color=TEXT_2)
    ax.grid(axis="y", color=GRID, linewidth=1)
    ax.tick_params(colors=TEXT_2, labelsize=FS["tick"], length=0)
    for spine in ("top", "right", "left"):
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color(GRID)
    ax.set_xlim(-LEAD_IN_MIN, xmax)
    ax.set_ylim(bottom=0)


def label_end(ax, x, y, text, dy=0):
    ax.annotate(text, (x, y), xytext=(8, dy), textcoords="offset points", fontsize=FS["note"],
                color=TEXT_2, va="center", annotation_clip=False)


def finish(fig, path: Path, title: str, xlabel_ax) -> None:
    xlabel_ax.set_xlabel("minutes since load started   (shaded: held load steps)", fontsize=FS["label"], color=TEXT_2)
    fig.suptitle(title, x=0.02, ha="left", fontsize=FS["title"], color=TEXT, fontweight="bold")
    fig.tight_layout(rect=(0, 0, 0.9, 0.93))
    fig.savefig(path, dpi=150, facecolor=SURFACE)
    plt.close(fig)


def s2(run0) -> None:
    fig, (ax,) = new(1)
    xs, ys = run0["alb_requests"]["all"]
    ax.plot(xs, [y / 60 for y in ys], color=ORDER, linewidth=3.5)
    style(ax, "requests reaching the services / s", STEPS["run0"], 27, band_labels=True)
    ax.set_ylim(0, 215)
    for a, b, rps in STEPS["run0"]:
        ax.hlines(rps, a, b, colors=TEXT_2, linewidth=1.5, linestyles=(0, (5, 4)))
    ax.text(-1.5, 195, "dashed: load offered by k6\nsolid: load reaching the services", fontsize=FS["note"], color=TEXT_2, va="top")
    ax.annotate("flat at ~37 req/s:\nthe API Gateway limit\nrejects the rest", xy=(15.5, 37), xytext=(13.5, 135),
                fontsize=FS["note"], color=TEXT_2, arrowprops={"arrowstyle": "-", "color": TEXT_2, "linewidth": 1.2})
    finish(fig, OUT / "s2_run0_gateway_cap.png", "Run 0: the API Gateway limit capped the whole API", ax)


def s3(run1) -> None:
    fig, (ax,) = new(1)
    for name, colour in (("order", ORDER), ("hawker", HAWKER)):
        xs, ys = run1["tasks"][name]
        ax.step(xs, ys, where="post", color=colour, linewidth=4)
        label_end(ax, xs[-1], ys[-1], f"{name}: {ys[-1]:.0f} tasks")
    style(ax, "running tasks", STEPS["run1"], 35, band_labels=True)
    ax.set_ylim(0, 5.8)
    ax.yaxis.get_major_locator().set_params(integer=True)
    finish(fig, OUT / "s3_run1_scaling.png", "Run 1: tasks scale out automatically as load rises", ax)


def s4(run1, run2) -> None:
    fig, axes = new(2)
    for key, data, colour, text in (("run1", run1, BASELINE, "run 1 (before HA)"), ("run2", run2, ORDER, "run 2 (HA)")):
        xs, ys = data["sqs_visible"]["all"]
        axes[0].plot(xs, ys, color=colour, linewidth=3.5)
        peak = max(range(len(ys)), key=ys.__getitem__)
        axes[0].annotate(f"{text}: peak {ys[peak]:.0f}", (xs[peak], ys[peak]),
                         xytext=(26.5, 980 if key == "run2" else 700), textcoords="data", fontsize=FS["note"],
                         color=TEXT_2, va="center", arrowprops={"arrowstyle": "-", "color": TEXT_2, "linewidth": 1})
        xs, ys = data["tasks"]["order"]
        axes[1].step(xs, ys, where="post", color=colour, linewidth=3.5)
        start = ys[0]
        axes[1].text(-1.5, start + (0.35 if key == "run2" else -0.55),
                     f"{text}: starts with {start:.0f}", fontsize=FS["note"], color=TEXT_2)
    style(axes[0], "orders waiting\nin queue", STEPS["run2"], 35, band_labels=True)
    axes[0].set_ylim(0, 1200)
    style(axes[1], "order tasks", STEPS["run2"], 35, band_labels=False)
    axes[1].set_ylim(0, 5.8)
    axes[1].yaxis.get_major_locator().set_params(integer=True)
    finish(fig, OUT / "s4_order_backlog_run1_vs_run2.png",
           "At 100 req/s, orders queue until order scales out", axes[1])


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    runs = {k: load(v) for k, v in RUNS.items()}
    s2(runs["run0"])
    s3(runs["run1"])
    s4(runs["run1"], runs["run2"])
    print(f"Wrote {sorted(p.name for p in OUT.glob('*.png'))}")
