# -*- coding: utf-8 -*-
"""Refresh report descriptives from the frozen final singles/couples rows.

This script is deliberately descriptive: it does not refit either model.  It
reads the corrected floor-five singles frame, the clean-couples frame, the
priced chosen rows, and the frozen France input used by the couples build.
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


HERE = Path(__file__).resolve().parent
FIG = HERE / "figures"
MNL = HERE.parents[2] / "MNL"
SINGLES = (MNL / "outputs/p2a_singles2016/region_live_margqh_floor5_v1/"
           "fr_p2a_singles2016_regionlive_margqh_floor5_v1__singles.parquet")
COUPLES = (MNL / "experiments/JMP_SEMINAR_SPRINT/runs/couples_clean_baseline/"
           "ps1h_couples_frame_floor5_v1.parquet")
COUPLES_ENGINE = (MNL / "experiments/JMP_SEMINAR_SPRINT/runs/couples_clean_baseline/"
                  "ps1h_couples_engine_ready_floor5_v1.parquet")
COUPLES_PRICED = (MNL / "experiments/JMP_SEMINAR_SPRINT/runs/couples_clean_baseline/"
                  "_priced_floor5_switch_with_idorighh.parquet")
SINGLES_SCALE = (MNL / "experiments/JMP_SEMINAR_SPRINT/runs/final_singles_welfare/"
                 "ss9_equivalence_scale_v1.parquet")
RAW = Path(r"C:\Users\hisham\MNL\EUROMOD-STORAGE\Data\FR\FR_2016_a3.txt")

COLORS = {"single": "#2463a9", "men": "#315a76", "women": "#c25b56",
          "couple": "#7b5ba7"}


def weighted_quantile(x, w, q):
    x = np.asarray(x, float)
    w = np.asarray(w, float)
    ok = np.isfinite(x) & np.isfinite(w) & (w > 0)
    x, w = x[ok], w[ok]
    order = np.argsort(x)
    x, w = x[order], w[order]
    return float(np.interp(q, (np.cumsum(w) - .5 * w) / w.sum(), x))


def summary(x, w):
    x = np.asarray(x, float)
    w = np.asarray(w, float)
    ok = np.isfinite(x) & np.isfinite(w) & (w > 0)
    x, w = x[ok], w[ok]
    return {
        "n": int(len(x)),
        "mean_weighted": float(np.average(x, weights=w)),
        "median_weighted": weighted_quantile(x, w, .5),
        "p10_weighted": weighted_quantile(x, w, .1),
        "p90_weighted": weighted_quantile(x, w, .9),
        "min": float(x.min()),
        "max": float(x.max()),
    }


def save(fig, stem):
    fig.tight_layout()
    fig.savefig(FIG / f"{stem}.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def main():
    FIG.mkdir(parents=True, exist_ok=True)
    s = pd.read_parquet(SINGLES)
    s = s.loc[s["is_chosen"].eq(1)].drop_duplicates("idorighh").copy()
    c = pd.read_parquet(COUPLES)
    c = c.loc[c["is_chosen"].eq(1)].drop_duplicates("idorighh").copy()
    ce = pd.read_parquet(COUPLES_ENGINE)
    ce = ce.loc[ce["is_chosen"].eq(1)].drop_duplicates("source_idorighh")
    c = c.merge(ce[["source_idorighh", "consumption", "consumption_raw"]],
                left_on="idorighh", right_on="source_idorighh", how="left")

    # One common funnel ending in the two frozen estimation populations.  The
    # intermediate counts are read from the certified reader export; only its
    # obsolete floor-ten wording is not reused.
    fig, ax = plt.subplots(figsize=(11, 5.8))
    stages = ["Raw households", "Eligible household types", "Age",
              "Education", "Retirement", "Labour state", "Other members",
              "Hours/wage support"]
    flow_csv = (MNL / "outputs/p2a_singles2016/notebook_dev_v3/"
                "results_discussion_table1_1_sample_flow.csv")
    flow = pd.read_csv(flow_csv)
    all_hh = flow["households"].astype(int).tolist()[:len(stages)]
    x = np.arange(len(stages))
    ax.plot(x, all_hh, marker="o", lw=2.5, color="#555555")
    ax.scatter([len(stages)], [len(s)], s=130, color=COLORS["single"], zorder=3)
    ax.scatter([len(stages)], [len(c)], s=130, color=COLORS["couple"], zorder=3)
    ax.plot([len(stages)-1, len(stages)], [all_hh[-1], len(s)], color=COLORS["single"])
    ax.plot([len(stages)-1, len(stages)], [all_hh[-1], len(c)], color=COLORS["couple"])
    ax.set_xticks(list(x) + [len(stages)], stages + ["Final type samples"], rotation=25,
                  ha="right")
    ax.set_ylabel("Households remaining")
    ax.set_title("One construction, two final estimation samples")
    ax.annotate(f"Singles: {len(s):,}", (len(stages), len(s)), xytext=(-90, -24),
                textcoords="offset points", color=COLORS["single"], weight="bold")
    ax.annotate(f"Couples: {len(c):,}", (len(stages), len(c)), xytext=(-90, 12),
                textcoords="offset points", color=COLORS["couple"], weight="bold")
    ax.spines[["top", "right"]].set_visible(False)
    save(fig, "rg_fig1_1_sample_funnel")

    # Continuous observed hours; reporting bins are not structural bands.
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8), sharey=True)
    bins = np.arange(5, 71, 2)
    axes[0].hist(s.loc[s.working.eq(1), "hours"], bins=bins,
                 weights=s.loc[s.working.eq(1), "dwt"], density=True,
                 alpha=.8, color=COLORS["single"])
    axes[0].set_title("Singles: employed deciders")
    cm = c.loc[c.working_m.eq(1)]
    cf = c.loc[c.working_f.eq(1)]
    axes[1].hist(cm.hours_m, bins=bins, weights=cm.dwt, density=True,
                 histtype="step", lw=2.2, color=COLORS["men"], label="Men")
    axes[1].hist(cf.hours_f, bins=bins, weights=cf.dwt, density=True,
                 histtype="step", lw=2.2, color=COLORS["women"], label="Women")
    axes[1].set_title("Couples: employed spouses")
    axes[1].legend(frameon=False)
    for ax in axes:
        ax.axvspan(33.5, 36.5, color="#e7b64b", alpha=.22)
        ax.set_xlabel("Observed weekly hours (continuous)")
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_ylabel("Survey-weighted density")
    fig.suptitle("Observed hours in the corrected floor-five final samples")
    save(fig, "rg_fig2_2_hours_bands")

    # Age and wage are distributions, not a conditional wage-age profile.
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8))
    axes[0].hist(s.dag, bins=np.arange(20, 62, 3), weights=s.dwt, density=True,
                 histtype="step", lw=2.2, color=COLORS["single"], label="Singles")
    axes[0].hist(pd.concat([c.dag_m, c.dag_f]), bins=np.arange(20, 62, 3),
                 weights=pd.concat([c.dwt, c.dwt]), density=True, histtype="step",
                 lw=2.2, color=COLORS["couple"], label="Couple spouses")
    axes[0].set_xlabel("Age (years)")
    axes[0].set_ylabel("Survey-weighted density")
    axes[0].set_title("Age")
    sw = s.loc[s.working.eq(1)]
    cw_m, cw_f = c.loc[c.working_m.eq(1)], c.loc[c.working_f.eq(1)]
    axes[1].hist(sw.wage, bins=np.linspace(2, 60, 35), weights=sw.dwt, density=True,
                 histtype="step", lw=2.2, color=COLORS["single"], label="Singles")
    axes[1].hist(pd.concat([cw_m.wage_m, cw_f.wage_f]), bins=np.linspace(2, 60, 35),
                 weights=pd.concat([cw_m.dwt, cw_f.dwt]), density=True, histtype="step",
                 lw=2.2, color=COLORS["couple"], label="Couple spouses")
    axes[1].set_xlabel("Observed hourly wage (euros/hour)")
    axes[1].set_title("Observed workers' wages")
    axes[1].legend(frameon=False)
    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Final-sample age and observed-worker wage distributions")
    save(fig, "rg_fig2_3_wage_age")

    # Occupation shares, keeping spouses separate.
    fig, ax = plt.subplots(figsize=(10.5, 5.2))
    groups = np.arange(1, 5)
    def shares(df, col, work):
        z = df.loc[df[work].eq(1)]
        den = z.dwt.sum()
        return np.array([z.loc[z[col].eq(k), "dwt"].sum()/den for k in groups])
    vals = [shares(s, "loc4", "working"), shares(c, "loc4_m", "working_m"),
            shares(c, "loc4_f", "working_f")]
    width = .24
    for off, val, lab, col in zip((-width, 0, width), vals,
                                  ("Singles", "Couple men", "Couple women"),
                                  (COLORS["single"], COLORS["men"], COLORS["women"])):
        ax.bar(groups + off, val, width, label=lab, color=col)
    ax.set_xticks(groups)
    ax.set_xlabel("Research aggregation of ISCO-08 major groups")
    ax.set_ylabel("Survey-weighted share among employed")
    ax.set_title("Observed occupations in both final samples")
    ax.legend(frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    save(fig, "rg_fig2_4_occupation_by_sex")

    # Household disposable consumption, raw and modified-OECD equivalized.
    ss = pd.read_parquet(SINGLES_SCALE)[["idhh", "m_oecd"]]
    s = s.merge(ss, on="idhh", how="left")
    cp = pd.read_parquet(COUPLES_PRICED)
    chosen_people = cp.loc[cp.is_chosen.eq(1), ["idorighh", "idperson", "dag"]].drop_duplicates()
    members = chosen_people.groupby("idorighh").dag.agg(
        adults=lambda z: int((z >= 14).sum()), children=lambda z: int((z < 14).sum()))
    members["m_oecd"] = 1 + .5 * (members.adults - 1) + .3 * members.children
    c = c.merge(members[["m_oecd"]], left_on="idorighh", right_index=True, how="left")
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8))
    cap = weighted_quantile(pd.concat([s.consumption, c.consumption]),
                            pd.concat([s.dwt, c.dwt]), .99)
    for ax, equiv, title in zip(axes, (False, True),
                                ("Raw household amount", "Modified-OECD equivalized")):
        sx = s.consumption / (s.m_oecd if equiv else 1)
        cx = c.consumption / (c.m_oecd if equiv else 1)
        ax.hist(sx.clip(upper=cap), bins=40, weights=s.dwt, density=True,
                histtype="step", lw=2.2, color=COLORS["single"], label="Singles")
        ax.hist(cx.clip(upper=cap), bins=40, weights=c.dwt, density=True,
                histtype="step", lw=2.2, color=COLORS["couple"], label="Couples")
        ax.set_title(title)
        ax.set_xlabel("Disposable consumption (real-2016 euros/month)")
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_ylabel("Survey-weighted density (top percentile winsorized for display)")
    axes[1].legend(frameon=False)
    fig.suptitle("Final-sample disposable-consumption distributions by household type")
    save(fig, "rg_fig2_1_income_distributions")

    # Weighted Lorenz curves for the exact same chosen-row consumption object.
    def lorenz(x, w):
        x, w = np.asarray(x, float), np.asarray(w, float)
        ok = np.isfinite(x) & np.isfinite(w) & (w > 0)
        x, w = x[ok], w[ok]
        o = np.argsort(x)
        x, w = x[o], w[o]
        p = np.r_[0, np.cumsum(w) / w.sum()]
        y = np.r_[0, np.cumsum(w * x) / np.sum(w * x)]
        return p, y
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8))
    for ax, equiv, title in zip(axes, (False, True),
                                ("Raw household amount", "Modified-OECD equivalized")):
        for frame, label, color in ((s, "Singles", COLORS["single"]),
                                    (c, "Couples", COLORS["couple"])):
            xval = frame.consumption / (frame.m_oecd if equiv else 1)
            p, y = lorenz(xval, frame.dwt)
            ax.plot(p, y, lw=2.3, label=label, color=color)
        ax.plot([0, 1], [0, 1], ls="--", lw=1, color="#777777")
        ax.set_title(title)
        ax.set_xlabel("Cumulative survey-weighted household share")
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_ylabel("Cumulative disposable-consumption share")
    axes[1].legend(frameon=False)
    fig.suptitle("Final-sample disposable-consumption Lorenz curves")
    save(fig, "rg_fig3_1_lorenz_and_deciles")

    # Actual frozen resource inputs.  Source units are intentionally not guessed.
    resource_vars = ["ypp", "yse", "yiy", "ypr", "ypt", "yot"]
    raw = pd.read_csv(RAW, sep="\t", usecols=["idhh", "dwt"] + resource_vars)
    ids_s, ids_c = set(s.idorighh), set(c.idorighh)
    def resource_nonzero(ids):
        z = raw.loc[raw.idhh.isin(ids)].copy()
        hh = z.groupby("idhh").agg({**{v: "sum" for v in resource_vars}, "dwt": "first"})
        return np.array([np.average(hh[v].ne(0), weights=hh.dwt) for v in resource_vars])
    rs, rc = resource_nonzero(ids_s), resource_nonzero(ids_c)
    fig, ax = plt.subplots(figsize=(10.5, 5.2))
    x = np.arange(len(resource_vars))
    ax.bar(x-.19, rs, .38, label="Singles", color=COLORS["single"])
    ax.bar(x+.19, rc, .38, label="Couples", color=COLORS["couple"])
    ax.set_xticks(x, resource_vars)
    ax.set_ylabel("Survey-weighted share with non-zero recorded input")
    ax.set_title("Actual non-labour resource inputs in the final household samples")
    ax.legend(frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    save(fig, "rg_fig2_5_resource_inputs")

    out = {
        "source": "frozen corrected singles and clean-couples chosen rows",
        "n_singles": len(s), "n_couples": len(c),
        "minimum_employed_hours": {
            "singles": float(s.loc[s.working.eq(1), "hours"].min()),
            "couple_men": float(c.loc[c.working_m.eq(1), "hours_m"].min()),
            "couple_women": float(c.loc[c.working_f.eq(1), "hours_f"].min()),
        },
        "summaries": {
            "singles_age": summary(s.dag, s.dwt),
            "couple_men_age": summary(c.dag_m, c.dwt),
            "couple_women_age": summary(c.dag_f, c.dwt),
            "singles_disposable": summary(s.consumption, s.dwt),
            "couples_disposable": summary(c.consumption, c.dwt),
        },
        "resource_variables_displayed": resource_vars,
        "resource_nonzero_share": {"singles": rs.tolist(), "couples": rc.tolist()},
        "unit_caveat": "Field-level source units/time bases are UNRESOLVED B1.",
    }
    (HERE / "final_descriptives_v1.json").write_text(
        json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("refreshed", len(list(FIG.glob("rg_fig*.png"))), "report figures")


if __name__ == "__main__":
    main()
