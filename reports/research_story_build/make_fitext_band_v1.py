"""Render the POSFIT-v3 observed extensive-accuracy/band figure.

The observed point and simulated band are distinct source columns. The G2
file decides only whether the point may be displayed.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
POSFIT = REPO / "MNL_posfit" / "outputs" / "positive_fit_diagnostics_v3"
OUT = HERE / "assets" / "fitext_band_v1.png"

GROUPS = ["couples_female", "singles_female", "couples_male", "singles_male"]
PRETTY = {
    "couples_female": "coupled women",
    "singles_female": "single women",
    "couples_male": "coupled men",
    "singles_male": "single men",
}


def _rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def build() -> None:
    g2 = {
        row["group"]: row for row in _rows(POSFIT / "g2_adequacy.csv")
        if row["weighting"] == "weighted"
        and row.get("scope", "all") == "all"
        and row["statistic"] == "extensive_accuracy"
    }
    bands = {
        row["group"]: row for row in _rows(POSFIT / "model_simulated_bands.csv")
        if row["weighting"] == "weighted"
        and row["scope"] == "all"
        and row["statistic"] == "extensive_accuracy"
        and row["support"] == "full"
    }

    fig, ax = plt.subplots(figsize=(10.8, 5.3), dpi=160)
    for y, group in enumerate(GROUPS):
        if g2[group]["label"] != "ADEQUATE":
            ax.text(75.5, y, "withheld: quadrature-limited", va="center",
                    color="#555866", fontsize=11.5)
            continue
        row = bands[group]
        observed = 100 * float(row["observed"])
        lo = 100 * float(row["simulated_p025"])
        hi = 100 * float(row["simulated_p975"])
        ax.plot([lo, hi], [y, y], color="#99A7C7", lw=7,
                solid_capstyle="round", zorder=1)
        ax.scatter([observed], [y], color="#1450C8", s=75, zorder=2)
        ax.text(92.8, y, f"{observed:.1f}%  [{lo:.1f}, {hi:.1f}]",
                va="center", ha="left", color="#222533", fontsize=11.5)

    ax.set_yticks(range(len(GROUPS)), [PRETTY[group] for group in GROUPS])
    ax.invert_yaxis()
    ax.set_xlim(75, 100)
    ax.set_xlabel("weighted extensive-margin accuracy (%)")
    ax.grid(axis="x", alpha=.22)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.text(.995, -.22, "point: observed   band: model-simulated 95% interval",
            transform=ax.transAxes, ha="right", color="#555866", fontsize=10)
    fig.tight_layout()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    build()
