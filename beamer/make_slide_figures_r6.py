#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Render the R6 deck's slide-native panels.

Four panels, each from one authorized source and each carrying no number the
R6 ruling withholds:

  calibration_r6   deciles.csv        calibration CONDITIONED ON PREDICTION
  fitext_r6        hard_classification_metrics.csv observed accuracy,
                   screened by g2_adequacy.csv (G2-ADEQUATE groups only)
  kernelacc_r6     s11_singles_parameter_table_v1.csv   access kernel
  kernelwage_r6    s11_singles_parameter_table_v1.csv   wage-offer kernel

No welfare panel is produced: BASELINE-F-1 commits aggregates only, and a
distribution figure would need household-level values that must stay in the
restricted environment.
"""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
POSFIT = REPO / "MNL_posfit" / "outputs" / "positive_fit_diagnostics_v3"   # MNL_posfit 96693269
S11 = REPO / "MNL" / "experiments" / "JMP_SEMINAR_SPRINT" / "runs" / "s11_welfare_specs_of_record"
OUT = HERE / "figures" / "r6"

DEEPRED = "#96191F"
ACC = "#1450C8"
EARN = "#C87814"
GREY = "#3C3C46"

plt.rcParams.update({
    "font.size": 18, "axes.titlesize": 19, "axes.labelsize": 18,
    "xtick.labelsize": 16, "ytick.labelsize": 16, "legend.fontsize": 16,
    "figure.dpi": 120, "savefig.bbox": "tight", "pdf.fonttype": 42,
})


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def rows(p: Path) -> list[dict]:
    with p.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def finish(fig, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / (name + "_slide.pdf"))
    plt.close(fig)
    print("  wrote figures/r6/%s_slide.pdf" % name)


GROUPS = ["singles_male", "singles_female", "couples_male", "couples_female"]
PRETTY = {"singles_male": "single men", "singles_female": "single women",
          "couples_male": "coupled men", "couples_female": "coupled women"}


def calibration(man: dict) -> None:
    p = POSFIT / "deciles.csv"
    man["deciles.csv"] = sha256(p)
    d = [r for r in rows(p) if r["weighting"] == "weighted"]
    fig, axes = plt.subplots(1, 4, figsize=(19, 5.0), sharex=True, sharey=True)
    for ax, g in zip(axes, GROUPS):
        sub = sorted((r for r in d if r["group"] == g), key=lambda r: int(r["decile"]))
        x = [float(r["mean_predicted_E_hours_work"]) for r in sub]
        y = [float(r["mean_observed_hours"]) for r in sub]
        lo = min(min(x), min(y)) - 2
        hi = max(max(x), max(y)) + 2
        ax.plot([lo, hi], [lo, hi], color=GREY, lw=1.4, ls="--", zorder=1)
        ax.plot(x, y, "o-", color=DEEPRED, lw=2.2, ms=7, zorder=2)
        ax.set_title(PRETTY[g])
        ax.set_xlabel("predicted E[h | work]")
        ax.grid(alpha=0.25, lw=0.6)
    axes[0].set_ylabel("mean observed hours")
    fig.suptitle("")
    finish(fig, "calibration_r6")


def fitext(man: dict) -> None:
    g2_path = POSFIT / "g2_adequacy.csv"
    hard_path = POSFIT / "hard_classification_metrics.csv"
    man["g2_adequacy.csv"] = sha256(g2_path)
    man["hard_classification_metrics.csv"] = sha256(hard_path)
    d = [r for r in rows(g2_path)
         if r["weighting"] == "weighted" and r["statistic"] == "extensive_accuracy"
         and r.get("scope", "all") == "all"]
    by = {r["group"]: r for r in d}
    observed = {r["group"]: float(r["extensive_accuracy"])
                for r in rows(hard_path) if r["weighting"] == "weighted"}
    fig, ax = plt.subplots(figsize=(13, 5.6))
    ys, labels, colors, texts = [], [], [], []
    for g in GROUPS:
        r = by[g]
        labels.append(PRETTY[g])
        if r["label"] == "ADEQUATE":
            ys.append(100.0 * observed[g])
            colors.append(ACC)
            texts.append("%.1f%%" % ys[-1])
        else:
            ys.append(0.0)
            colors.append("#D8D8DC")
            texts.append("withheld: quadrature-limited")
    ax.barh(labels, ys, color=colors, height=0.55)
    for i, (v, t) in enumerate(zip(ys, texts)):
        if v > 0:
            ax.text(v - 2, i, t, va="center", ha="right", color="white", fontsize=17)
        else:
            ax.text(1.5, i, t, va="center", ha="left", color=GREY, fontsize=16)
    ax.set_xlim(0, 100)
    ax.set_xlabel("extensive-margin accuracy (%), G2-adequate groups only")
    ax.invert_yaxis()
    ax.grid(axis="x", alpha=0.25, lw=0.6)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    finish(fig, "fitext_r6")


ACCESS_BLOCK = [
    ("beta_E", "access constant"),
    ("beta_E_gsur", "survey-strata shift"),
    ("beta_E_drgur", "regional unemployment"),
    ("beta_E_drgmd", "regional median income"),
    ("beta_E_drgn2", "region 2"), ("beta_E_drgn3", "region 3"),
    ("beta_E_drgn4", "region 4"), ("beta_E_drgn5", "region 5"),
    ("beta_E_drgn6", "region 6"), ("beta_E_drgn7", "region 7"),
    ("beta_E_drgn8", "region 8"),
]
WAGE_BLOCK = [
    ("beta_w0", "offer location"),
    ("beta_w_educL", "low education"),
    ("beta_w_educH", "high education"),
    ("beta_w_pexp", "experience"),
    ("beta_w_pexp2", "experience squared"),
    ("sigma", "offer dispersion"),
    ("delta_occ_2", "occupation 2"),
    ("delta_occ_3", "occupation 3"),
    ("delta_occ_4", "occupation 4"),
]


def kernel(man: dict, block, name: str, colour: str, xlabel: str) -> None:
    p = S11 / "s11_singles_parameter_table_v1.csv"
    man["s11_singles_parameter_table_v1.csv"] = sha256(p)
    tab = {r["param"]: r for r in rows(p)}
    labels, est, err = [], [], []
    for key, lab in block:
        r = tab[key]
        if not r["se_robust_CR1"]:
            continue
        labels.append(lab)
        est.append(float(r["estimate"]))
        err.append(1.96 * float(r["se_robust_CR1"]))
    fig, ax = plt.subplots(figsize=(13, 0.52 * len(labels) + 2.2))
    y = list(range(len(labels)))
    ax.axvline(0.0, color=GREY, lw=1.2, ls="--")
    ax.errorbar(est, y, xerr=err, fmt="o", color=colour, ecolor=colour,
                elinewidth=2.0, capsize=5, ms=8)
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()
    ax.set_xlabel(xlabel)
    ax.grid(axis="x", alpha=0.25, lw=0.6)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    finish(fig, name)


def main() -> int:
    man: dict = {}
    print("R6 slide figures:")
    calibration(man)
    fitext(man)
    kernel(man, ACCESS_BLOCK, "kernelacc_r6", ACC,
           "S11 singles, log access index; bars are 1.96 x CR1 robust s.e.")
    kernel(man, WAGE_BLOCK, "kernelwage_r6", EARN,
           "S11 singles, log wage-offer density; bars are 1.96 x CR1 robust s.e.")
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "r6_source_manifest.json").write_text(
        json.dumps(man, indent=2, sort_keys=True), encoding="utf-8")
    print("  wrote figures/r6/r6_source_manifest.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
