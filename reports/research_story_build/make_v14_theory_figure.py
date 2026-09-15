"""Draw the deterministic own-set equal-consumption construction (theory figure).

Regenerated for V14. The previously embedded image (manuscript/figures/v3/theory_w1.png,
a raster adapted from the companion theory project's slides) has no surviving
generator, overlapping labels, and draws two different preference relations,
so it is not reused.

Construction (Measure 1 of the companion theory paper): for an individual with
preferences R, ability set A and attained bundle z = (c, j), assign the same
consumption w to every job in A; the individual's preferred job among those
equal-consumption bundles is the reference job, and w is chosen so that this
reference bundle is indifferent to z. That w is the money metric.

The drawing uses one illustrative preference relation for BOTH individuals,
u(c, j) = log c + a_j, so indifference means equal u. Because the job term is
additive, the preferred job at equal consumption does not depend on w. The
numbers below only place shapes; no axis carries a numeric tick, and the figure
contains no estimated value, household datum or certified number.
"""
from __future__ import annotations

import io
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from PIL import Image  # noqa: E402

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = ROOT / "manuscript/figures/v14/fig_v14_theory_own_set.png"

JOBS = ["j", "k", "ℓ"]
X = {"j": 0.0, "k": 1.0, "ℓ": 2.0}
JOB_VALUE = {"j": 0.0, "k": 0.45, "ℓ": 0.85}   # same preferences for both individuals

PEOPLE = [
    {"name": "Individual 1", "colour": "#b5302a", "set": ["j", "k"], "set_label": "A₁ = {j, k}",
     "job": "j", "c": 2.3},
    {"name": "Individual 2", "colour": "#1f5fa8", "set": ["k", "ℓ"], "set_label": "A₂ = {k, ℓ}",
     "job": "k", "c": 2.0},
]


def utility(c: float, job: str) -> float:
    return math.log(c) + JOB_VALUE[job]


def indifferent_consumption(u: float, job: str) -> float:
    return math.exp(u - JOB_VALUE[job])


def panel(ax, person: dict, letter: str) -> None:
    colour = person["colour"]
    own = person["set"]
    u = utility(person["c"], person["job"])
    reference = max(own, key=lambda job: JOB_VALUE[job])
    w = indifferent_consumption(u, reference)

    for job in JOBS:
        if job not in own:
            ax.axvspan(X[job] - 0.42, X[job] + 0.42, color="#eeeeee", zorder=0)
            ax.text(X[job], 3.0, "not in this\nability set", ha="center", va="top", fontsize=9, color="#777777")
    left, right = X[own[0]] - 0.42, X[own[-1]] + 0.42
    ax.axvspan(left, right, color=colour, alpha=0.06, zorder=0)
    ax.annotate("", xy=(left + 0.05, -0.3), xytext=(right - 0.05, -0.3),
                arrowprops=dict(arrowstyle="-", color=colour, linewidth=2.2), annotation_clip=False)
    ax.text((left + right) / 2, -0.42, "own ability set " + person["set_label"], ha="center", va="top",
            fontsize=10.5, color=colour, weight="bold")

    xs = [X[job] for job in own]
    ys = [indifferent_consumption(u, job) for job in own]
    ax.plot(xs, ys, color=colour, linewidth=1.4, linestyle="--", zorder=2)
    for job, y in zip(own, ys):
        if job != person["job"]:
            ax.scatter([X[job]], [y], s=55, facecolors="white", edgecolors=colour, linewidths=1.6, zorder=3)
    ax.text(sum(xs) / 2 + 0.08, sum(ys) / 2 + 0.12, "bundles indifferent\nto the attained bundle",
            fontsize=9, color=colour, ha="left")

    ax.scatter([X[person["job"]]], [person["c"]], s=120, color=colour, zorder=4)
    ax.annotate("attained bundle z", (X[person["job"]], person["c"]), xytext=(10, 8),
                textcoords="offset points", fontsize=10.5, color=colour, weight="bold")

    ax.hlines(w, left + 0.05, right - 0.05, colors=colour, linewidth=2.6, zorder=3)
    for job in own:
        ax.scatter([X[job]], [w], s=40, color=colour, marker="s", zorder=4)
    ax.text(left + 0.08, w - 0.1, "same consumption w\non every job in the set",
            fontsize=9, color=colour, ha="left", va="top")
    ax.scatter([X[reference]], [w], s=380, facecolors="none", edgecolors="#17252b", linewidths=1.8, zorder=5)
    ax.annotate(f"preferred job at equal\nconsumption ({reference}), indifferent to z",
                (X[reference], w), xytext=(-40, -58), textcoords="offset points", fontsize=9.5,
                color="#17252b", arrowprops=dict(arrowstyle="-", color="#17252b", linewidth=0.8))

    ax.hlines(w, -0.6, left + 0.05, colors=colour, linewidth=1.0, linestyles=":")
    ax.text(-0.56, w + 0.05, "money metric", ha="left", va="bottom", fontsize=10, color=colour, weight="bold")

    ax.set_xlim(-0.6, 2.5)
    ax.set_ylim(0, 3.1)
    ax.set_xticks([X[job] for job in JOBS])
    ax.set_xticklabels(JOBS, fontsize=13)
    ax.set_yticks([])
    ax.text(2.5, -0.1, "jobs", ha="right", va="top", fontsize=11)
    ax.set_ylabel("consumption", fontsize=11)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title(f"({letter}) {person['name']}", fontsize=12.5, color=colour, weight="bold", loc="left")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(1, 2, figsize=(13.5, 6.2), sharey=True)
    for ax, person, letter in zip(axes, PEOPLE, "ab"):
        panel(ax, person, letter)
    fig.suptitle("Own-set equal-consumption equivalents: same preferences, different ability sets",
                 fontsize=13, weight="bold")
    fig.text(0.5, 0.005, "Theoretical illustration of the deterministic construction: no estimated values, "
             "no household data. Both individuals rank jobs at equal consumption as j < k < ℓ.",
             ha="center", fontsize=9.5, color="#444444")
    fig.tight_layout(rect=(0.02, 0.09, 1, 0.95))
    buffer = io.BytesIO()
    fig.savefig(buffer, dpi=170, format="png")
    plt.close(fig)
    Image.open(buffer).convert("RGB").quantize(colors=256, method=Image.Quantize.MEDIANCUT,
                                               dither=Image.Dither.NONE).save(OUT, optimize=True)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
