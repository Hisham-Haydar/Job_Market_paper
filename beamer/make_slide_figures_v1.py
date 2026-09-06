#!/usr/bin/env python
r"""Slide-native figure variants for the JMP seminar deck (R-260).

Renders `figures/slides/<name>_slide.pdf` from the SAME data CSVs the paper
figures use, under a slide style rather than a paper style:

  * ONE panel per file.  Multi-panel paper figures are split; the deck picks
    per slide the panel that carries that slide's message.
  * 16:9 canvas (13.33 x 7.5 in), so a figure fills a widescreen frame.
  * every text element >= 18 pt at slide scale.
  * NO figure title, NO footnote, NO status or provenance stamp, and NO
    internal label anywhere -- not in the source and not in the PDF text
    layer.  Internal names (C_P, C_A, S8, LOC4, the arm keys) are mapped to
    audience words before they can reach an axis, a legend or a tick.
  * minimal legends; the house colours of the paper figure kit.

Audience vocabulary, and nothing else:
    final model / benchmark
    preferences / job access / earning opportunities /
        household endowments and needs
    female reference / male reference

Usage:  python beamer/make_slide_figures_v1.py [--sprint PATH] [--out PATH]
"""
from __future__ import annotations

import argparse
import pathlib
import sys
import json

import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt                              # noqa: E402
from matplotlib.lines import Line2D                          # noqa: E402
from matplotlib.patches import Patch                         # noqa: E402
import matplotlib.ticker as mticker                          # noqa: E402

DEFAULT_SPRINT = pathlib.Path(__file__).resolve().parents[2] / 'MNL/experiments/JMP_SEMINAR_SPRINT'

# ---------------------------------------------------------------- slide style
# The house palette of the paper figure kit, unchanged, so the slide figures
# and the paper figures are recognisably the same family.
INK, GREY = "#1a1a1a", "#8c8c8c"
ACC = ["#2b3a67", "#3f7d8c", "#c8553d", "#e0a458", "#7a9e7e"]

# One colour per channel, matching the deck preamble's channel colours.
C_PREF = "#c8553d"      # preferences            (deck: chpref)
C_ACC = "#2b3a67"       # job access             (deck: chacc)
C_EARN = "#e0a458"      # earning opportunities  (deck: chearn)
C_NEEDS = "#7a9e7e"     # endowments and needs   (deck: chneeds)
C_ENV = "#3f7d8c"       # the environment        (deck: chenv)

FIGSIZE = (13.333, 7.5)          # 16:9
BASE = 22                        # every text element is >= MIN_PT
MIN_PT = 18

SLIDE_RC = {
    "figure.figsize": FIGSIZE,
    "figure.dpi": 100, "savefig.dpi": 200, "savefig.bbox": "tight",
    "savefig.pad_inches": 0.05,
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans", "Arial", "Helvetica", "sans-serif"],
    "font.size": BASE,
    "axes.titlesize": BASE, "axes.labelsize": BASE,
    "xtick.labelsize": MIN_PT + 1, "ytick.labelsize": MIN_PT + 1,
    "legend.fontsize": MIN_PT + 1,
    "axes.edgecolor": INK, "axes.linewidth": 1.4,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": "#dddddd", "grid.linewidth": 1.0,
    "axes.axisbelow": True, "legend.frameon": False,
    "xtick.color": INK, "ytick.color": INK, "text.color": INK,
    "xtick.major.width": 1.2, "ytick.major.width": 1.2,
    "xtick.major.size": 5, "ytick.major.size": 5,
    "lines.linewidth": 3.0, "lines.markersize": 11,
    "figure.facecolor": "white", "axes.facecolor": "white",
}

# --------------------------------------------------------- audience vocabulary
# Every internal name that could otherwise reach a rendered string.  Anything
# not in here raises, so a new internal label cannot slip onto a slide.
CHANNEL_WORDS = {
    "C_P": "preferences", "C_pref": "preferences", "s_pref": "preferences",
    "C_E": "opportunities\nand budgets",
    "C_env": "opportunities\nand budgets",
    "s_env": "opportunities\nand budgets",
    "C_A": "job access", "C_acc": "job access",
    "C_B": "earning opportunities", "C_earn": "earning opportunities",
    "C_D": "household endowments\nand needs",
    "C_needs": "household endowments\nand needs",
    "C_geo": "geographic access", "C_oth": "remaining access",
    "job access": "job access",
    "earning opportunities": "earning opportunities",
    "endowments and needs": "household endowments\nand needs",
    "preferences": "preferences",
    "JOB ACCESS": "job access",
    "EARNING OPPORTUNITIES": "earning opportunities",
    "ENDOWMENTS AND NEEDS": "household endowments\nand needs",
}
# Short forms for a crowded categorical axis.  Still audience words -- only
# the qualifier is dropped, never the channel's identity.
CHANNEL_SHORT = {
    "preferences": "preferences",
    "opportunities\nand budgets": "opportunities\nand budgets",
    "job access": "job\naccess",
    "earning opportunities": "earning\nopportunities",
    "household endowments\nand needs": "endowments\nand needs",
    "geographic access": "geographic\naccess",
    "remaining access": "remaining\naccess",
}
CHANNEL_COLOUR = {
    "preferences": C_PREF,
    "opportunities\nand budgets": C_ENV,
    "job access": C_ACC,
    "earning opportunities": C_EARN,
    "household endowments\nand needs": C_NEEDS,
    "geographic access": C_ACC,
    "remaining access": GREY,
}
MODEL_WORDS = {
    "RURO": "final model", "S8": "final model",
    "RUM_B": "benchmark", "RUM_A": "benchmark",
    "estimated model (random opportunity)": "final model",
    "common-choice-set benchmark": "benchmark",
}
ARM_WORDS = {
    "singles_female": "female reference",
    "singles_male_structural_zero": "male reference",
}


def words(mapping: dict, key: str) -> str:
    """Map an internal name to its audience wording, or refuse."""
    k = str(key).strip()
    if k not in mapping:
        raise SystemExit(
            "no audience wording for %r -- add it to the vocabulary rather "
            "than letting an internal label reach a slide" % k)
    return mapping[k]


# ------------------------------------------------------------------- plumbing
INDEX: list[dict] = []


def new_ax(xlabel="", ylabel=""):
    fig, ax = plt.subplots(figsize=FIGSIZE)
    if xlabel:
        ax.set_xlabel(xlabel, labelpad=12)
    if ylabel:
        ax.set_ylabel(ylabel, labelpad=12)
    return fig, ax


def save(fig, name: str, out: pathlib.Path, source: str, panel: str) -> None:
    """Write the slide PDF.  No title, no footnote, no stamp is ever added."""
    out.mkdir(parents=True, exist_ok=True)
    path = out / (name + "_slide.pdf")
    fig.savefig(path)
    plt.close(fig)
    INDEX.append(dict(slide_figure=name + "_slide.pdf", source_csv=source,
                      panel=panel))
    print("  %-46s <- %s [%s]" % (path.name, source, panel))


def pct(x):
    return 100.0 * np.asarray(x, dtype=float)


def hbar_with_band(ax, labels, values, lo, hi, colours, xlabel):
    """Horizontal signed bars with an interval, the deck's recurring form."""
    y = np.arange(len(labels))[::-1]
    ax.barh(y, values, height=0.62, color=colours, alpha=0.92,
            edgecolor="white", linewidth=1.6, zorder=3)
    ax.errorbar(values, y, xerr=[values - lo, hi - values], fmt="none",
                ecolor=INK, elinewidth=2.0, capsize=7, capthick=2.0, zorder=4)
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.set_xlabel(xlabel, labelpad=12)
    ax.axvline(0.0, color=INK, lw=1.4, zorder=2)
    ax.grid(axis="y", visible=False)
    return y


# ==================================================================== figures
def f_headline(sprint, out):
    """Preferences against the environment -- the headline, one panel."""
    src = "figW02_headline_decomposition.csv"
    d = pd.read_csv(sprint / "figures" / src)
    d = d[(d["basis"] == "raw") & (d["model"] == "S8")
          & (d["reference_arm"] == "singles_female")]
    order = ["C_E", "C_P"]
    d = d.set_index("quantity").loc[order].reset_index()
    lab = [words(CHANNEL_WORDS, q) for q in d["quantity"]]
    col = [CHANNEL_COLOUR[l] for l in lab]
    base = float(d["estimate"].sum())
    fig, ax = new_ax()
    hbar_with_band(ax, lab, pct(d["estimate"] / base),
                   pct(d["band_lo"] / base), pct(d["band_hi"] / base), col,
                   "share of measured welfare inequality removed  (%)")
    for i, v in enumerate(pct(d["estimate"] / base)):
        ax.annotate("%.0f%%" % v, xy=(v, len(lab) - 1 - i), xytext=(14, 0),
                    textcoords="offset points", va="center",
                    fontsize=BASE + 8, fontweight="bold", color=col[i])
    ax.set_xlim(0, 118)
    save(fig, "headline", out, src, "S8 / female reference / raw")


def f_headline_intervals(sprint, out):
    """The same two shares carrying BOTH intervals, kept on offset rows."""
    src = "figU01_headline_two_intervals.csv"
    d = pd.read_csv(sprint / "figures" / src)
    d = d[(d["panel"] == "C") & (d["quantity"] == "s_env")]
    e = pd.read_csv(sprint / "figures" / src)
    p = e[(e["panel"] == "B") & (e["quantity"] == "s_pref")]
    rows = [("opportunities\nand budgets", d.iloc[0]),
            ("preferences", p.iloc[0])]
    fig, ax = new_ax()
    for k, (lab, r) in enumerate(rows):
        y = len(rows) - 1 - k
        col = CHANNEL_COLOUR[lab]
        ax.plot([pct(r["rqmc_band_lo"]), pct(r["rqmc_band_hi"])],
                [y + 0.13] * 2, color=col, lw=9, solid_capstyle="butt",
                zorder=3)
        ax.plot([pct(r["parameter_lo_2p5"]), pct(r["parameter_hi_97p5"])],
                [y - 0.13] * 2, color=col, lw=9, alpha=0.42,
                solid_capstyle="butt", zorder=3)
        ax.plot([pct(r["point_estimate"])] * 2, [y - 0.26, y + 0.26],
                color=INK, lw=3.0, zorder=5)
    ax.set_yticks([len(rows) - 1 - k for k in range(len(rows))])
    ax.set_yticklabels([lab for lab, _ in rows])
    for tick, (lab, _) in zip(ax.get_yticklabels(), rows):
        tick.set_color(CHANNEL_COLOUR[lab])
        tick.set_fontweight("bold")
    ax.set_ylim(-0.6, len(rows) - 0.4)
    ax.set_xlim(0, 100)
    ax.set_xlabel("share of measured welfare inequality removed  (%)",
                  labelpad=12)
    ax.legend(handles=[
        Line2D([], [], color=GREY, lw=9, label="integration band"),
        Line2D([], [], color=GREY, lw=9, alpha=0.42,
               label="parameter interval")],
        loc="upper center", ncol=2, bbox_to_anchor=(0.5, 1.10))
    ax.grid(axis="y", visible=False)
    save(fig, "headline_intervals", out, src, "panels B and C / raw")


def f_environment(sprint, out):
    """Inside the environment: the three nested channels."""
    src = "figW03_nested_environment.csv"
    d = pd.read_csv(sprint / "figures" / src)
    d = d[(d["basis"] == "raw") & (d["model"] == "S8")
          & (d["reference_arm"] == "singles_female")]
    d = d.set_index("quantity").loc[["C_D", "C_B", "C_A"]].reset_index()
    lab = [words(CHANNEL_WORDS, q) for q in d["quantity"]]
    col = [CHANNEL_COLOUR[l] for l in lab]
    base = 0.13427655615401177  # baseline inequality, the CSV's own I00 scale
    hd = pd.read_csv(sprint / "tables" / "headline_decomposition_v1.csv")
    base = float(hd[(hd["model"] == "S8") & (hd["basis"] == "raw")
                    & (hd["reference_arm"] == "singles_female")]["I00"].iloc[0])
    fig, ax = new_ax()
    hbar_with_band(ax, lab, pct(d["estimate"] / base),
                   pct(d["band_lo"] / base), pct(d["band_hi"] / base), col,
                   "share of measured welfare inequality removed  (%)")
    for i, v in enumerate(pct(d["estimate"] / base)):
        ax.annotate("%.0f%%" % v, xy=(v, len(lab) - 1 - i), xytext=(14, 0),
                    textcoords="offset points", va="center",
                    fontsize=BASE + 6, fontweight="bold", color=col[i])
    ax.set_xlim(0, 74)
    save(fig, "environment", out, src, "S8 / female reference / raw")


def f_geographic(sprint, out):
    """Inside job access: the geographic split (panel B)."""
    src = "figG01_nested_geographic_access.csv"
    d = pd.read_csv(sprint / "figures" / src)
    d = d[(d["panel"] == "B") & (d["basis"] == "raw")
          & (d["reference_arm"] == "singles_female")]
    d = d[d["quantity"].isin(["C_geo", "C_oth"])]
    d = d.set_index("quantity").loc[["C_geo", "C_oth"]].reset_index()
    lab = [words(CHANNEL_WORDS, q) for q in d["quantity"]]
    col = [CHANNEL_COLOUR[l] for l in lab]
    hd = pd.read_csv(sprint / "tables" / "headline_decomposition_v1.csv")
    base = float(hd[(hd["model"] == "S8") & (hd["basis"] == "raw")
                    & (hd["reference_arm"] == "singles_female")]["I00"].iloc[0])
    v = pct(d["gini_points"] / base)
    et = pct(d["E_T"] / base)
    fig, ax = new_ax()
    hbar_with_band(ax, lab, v, v - et, v + et, col,
                   "share of measured welfare inequality removed  (%)")
    for i, x in enumerate(v):
        ax.annotate("%.1f%%" % x, xy=(x, len(lab) - 1 - i), xytext=(14, 0),
                    textcoords="offset points", va="center",
                    fontsize=BASE + 6, fontweight="bold", color=col[i])
    ax.set_xlim(0, 17.5)
    save(fig, "geographic", out, src, "panel B / female reference / raw")


def f_subgroup(sprint, out):
    """Job access within each sex -- the subgroup finding, one panel."""
    src = "figU02_subgroup_decomposition.csv"
    d = pd.read_csv(sprint / "figures" / src)
    d = d[(d["dimension"] == "sex") & (d["quantity"] == "C_acc_over_I00")]
    d = d.set_index("group").loc[["men", "women"]].reset_index()
    fig, ax = new_ax()
    y = np.arange(len(d))[::-1]
    v, et = pct(d["estimate"]), pct(d["E_T"])
    ax.barh(y, v, height=0.5, color=C_ACC, alpha=0.92, edgecolor="white",
            linewidth=1.6, zorder=3)
    ax.errorbar(v, y, xerr=et, fmt="none", ecolor=INK, elinewidth=2.0,
                capsize=7, capthick=2.0, zorder=4)
    ax.set_yticks(y)
    ax.set_yticklabels(list(d["group"]))
    ax.set_xlabel("share of that group's own measured inequality removed\n"
                  "by equalising job access  (%)", labelpad=14,
                  fontsize=MIN_PT + 1)
    ax.grid(axis="y", visible=False)
    for i, x in enumerate(v):
        ax.annotate("%.1f%%" % x, xy=(x, y[i]), xytext=(14, 0),
                    textcoords="offset points", va="center",
                    fontsize=BASE + 8, fontweight="bold", color=C_ACC)
    ax.set_xlim(0, 25)
    save(fig, "subgroup", out, src, "sex / job access share / raw")


def f_benchmark(sprint, out):
    """The final model against the common-choice-set benchmark (panel a)."""
    src = "figR01_benchmark_decomposition.csv"
    d = pd.read_csv(sprint / "figures" / src)
    d = d[(d["panel"] == "a") & (d["model"].isin(["RURO", "RUM_B"]))]
    chans = ["job access", "earning opportunities", "endowments and needs",
             "preferences"]
    fig, ax = new_ax()
    x = np.arange(len(chans))
    w = 0.36
    for k, m in enumerate(["RURO", "RUM_B"]):
        sub = d[d["model"] == m].set_index("quantity").loc[chans]
        base = float(sub["I00"].iloc[0])
        v = pct(sub["value"] / base)
        ax.bar(x + (k - 0.5) * w, v, width=w,
               color=[CHANNEL_COLOUR[words(CHANNEL_WORDS, c)] for c in chans],
               alpha=0.92 if k == 0 else 0.42,
               edgecolor="white", linewidth=1.6,
               hatch=None if k == 0 else "//", zorder=3)
    ax.set_xticks(x)
    ax.set_xticklabels([CHANNEL_SHORT[words(CHANNEL_WORDS, c)]
                        for c in chans], fontsize=MIN_PT)
    ax.set_ylabel("share of that model's own\nmeasured inequality removed  (%)",
                  labelpad=14, fontsize=MIN_PT + 1)
    ax.legend(handles=[
        Patch(facecolor=GREY, alpha=0.92, label=words(MODEL_WORDS, "RURO")),
        Patch(facecolor=GREY, alpha=0.42, hatch="//",
              label=words(MODEL_WORDS, "RUM_B"))],
        loc="upper left", ncol=2)
    ax.grid(axis="x", visible=False)
    ax.set_ylim(0, 108)
    save(fig, "benchmark", out, src, "panel a / final model vs benchmark")


def f_hours(sprint, out):
    """Hours-band shares, observed against model-implied."""
    src = "fig02_hours_bands_obs_vs_pred.csv"
    d = pd.read_csv(sprint / "figures" / src)
    d = d[d["band"] != "[33.5,36.5) peak"].copy()
    d["short"] = [b.split(" (")[0] if " (" in b else b for b in d["band"]]
    fig, ax = new_ax()
    x = np.arange(len(d))
    w = 0.4
    ax.bar(x - w / 2, pct(d["observed"]), width=w, color=INK, alpha=0.82,
           edgecolor="white", linewidth=1.4, zorder=3)
    ax.bar(x + w / 2, pct(d["predicted"]), width=w, color=C_ACC, alpha=0.82,
           edgecolor="white", linewidth=1.4, zorder=3)
    peak = int(np.argmax(d["observed"].values))
    ax.axvspan(peak - 0.5, peak + 0.5, color=C_EARN, alpha=0.16, zorder=1)
    ax.set_xticks(x)
    ax.set_xticklabels(d["short"], rotation=45, ha="right", fontsize=MIN_PT)
    ax.set_ylabel("share of households  (%)", labelpad=12)
    ax.set_xlabel("weekly hours", labelpad=12)
    ax.legend(handles=[Patch(facecolor=INK, alpha=0.82, label="observed"),
                       Patch(facecolor=C_ACC, alpha=0.82,
                             label="model-implied")],
              loc="upper left")
    ax.grid(axis="x", visible=False)
    save(fig, "hours", out, src, "twelve hours bins")


def f_fit(sprint, out):
    """Employment and occupation fit on one panel: observed against implied."""
    emp = pd.read_csv(sprint / "figures" / "fig03_employment_obs_vs_pred.csv")
    occ = pd.read_csv(sprint / "figures" / "fig04_occupation_obs_vs_pred.csv")
    rows = [("employment", float(emp[emp["group"] == "all"]["observed"].iloc[0]),
             float(emp[emp["group"] == "all"]["predicted"].iloc[0]))]
    for _, r in occ.iterrows():
        name = str(r["category"]).replace(" -- reference", "")
        rows.append((name, float(r["observed"]), float(r["predicted"])))
    fig, ax = new_ax()
    y = np.arange(len(rows))[::-1]
    obs = pct([r[1] for r in rows])
    pre = pct([r[2] for r in rows])
    ax.hlines(y, obs, pre, color=GREY, lw=2.4, zorder=2)
    ax.plot(obs, y, "o", color=INK, ms=15, zorder=4, label="observed")
    ax.plot(pre, y, "D", color=C_ACC, ms=12, zorder=4, label="model-implied")
    ax.set_yticks(y)
    ax.set_yticklabels([r[0] for r in rows], fontsize=MIN_PT + 1)
    ax.set_xlabel("share  (%)", labelpad=12)
    ax.legend(loc="lower right")
    ax.grid(axis="y", visible=False)
    save(fig, "fit", out, "fig03_employment + fig04_occupation",
         "employment and the five occupation categories")


def f_external(sprint, out):
    """External validation: the statutory band from three sources (panel b)."""
    src = "figX1_external_hours_lfs_validation.csv"
    d = pd.read_csv(sprint / "figures" / src)
    d = d[(d["panel"] == "b") & (d["band"] == "F35")]
    order = ["external benchmark", "observed sample", "model-implied"]
    sexes = ["pooled", "female", "male"]
    fig, ax = new_ax()
    x = np.arange(len(sexes))
    w = 0.26
    cols = [GREY, INK, C_ACC]
    for k, s in enumerate(order):
        v = [pct(float(d[(d["sex"] == sx) & (d["source"] == s)]["value"].iloc[0]))
             for sx in sexes]
        ax.bar(x + (k - 1) * w, v, width=w, color=cols[k], alpha=0.85,
               edgecolor="white", linewidth=1.4, zorder=3, label=s)
    ax.set_xticks(x)
    ax.set_xticklabels(["all", "women", "men"])
    ax.set_ylabel("share in the statutory 35-hour band  (%)", labelpad=12)
    ax.legend(loc="upper right", ncol=1)
    ax.grid(axis="x", visible=False)
    ax.set_ylim(0, 52)
    save(fig, "external", out, src, "panel b -- the one validation panel")


def f_observed_hours(sprint, out):
    """The requested observed-only panel, from the existing histogram CSV."""
    src = 'fig01_observed_hours_35h_peak.csv'
    d = pd.read_csv(sprint/'figures'/src)
    fig, ax = new_ax('weekly hours', 'share of households  (%)')
    ax.bar(d.hours_lower, pct(d.weighted_share_of_all_households),
           width=d.hours_upper-d.hours_lower, align='edge',
           color=INK, linewidth=0, zorder=3)
    ax.axvspan(33.5,36.5,color=C_EARN,alpha=0.25,zorder=1)
    ax.set_xlim(0,70)
    ax.grid(axis='x',visible=False)
    save(fig,'observed_hours',out,src,'observed hours; statutory band shaded')


def f_headline_references(sprint, out):
    """Signed contributions with integration bands, both reference arms."""
    src='figW02_headline_decomposition.csv'
    d=pd.read_csv(sprint/'figures'/src)
    d=d[(d.basis=='raw') & (d.model=='S8')]
    fig,ax=new_ax('contribution  (Gini points)')
    for k,arm in enumerate(['singles_female','singles_male_structural_zero']):
        sub=d[d.reference_arm==arm].set_index('quantity')
        for y,q,col in [(1,'C_E',C_ENV),(0,'C_P',C_PREF)]:
            r=sub.loc[q];yy=y+(0.15 if k==0 else -0.15)
            ax.barh(yy,r.estimate,height=0.23,color=col,alpha=1 if k==0 else 0.4,
                    hatch=None if k==0 else '//',zorder=3)
            ax.errorbar(r.estimate,yy,xerr=[[r.estimate-r.band_lo],[r.band_hi-r.estimate]],
                        fmt='none',ecolor=INK,capsize=6,lw=2,zorder=4)
    ax.set_yticks([1,0],['non-preference\nenvironment','preferences'])
    ax.axvline(0,color=INK,lw=1)
    ax.set_xlim(-0.003,0.15)
    ax.grid(axis='y',visible=False)
    ax.legend(handles=[Patch(facecolor=GREY,label='female reference'),
                       Patch(facecolor=GREY,alpha=0.4,hatch='//',label='male reference')],
              loc='lower right')
    save(fig,'headline_references',out,src,'raw; signed contributions; both reference conventions')


def f_regional_profiles(sprint, out):
    """Same profile across regional environments; one panel, same source CSV."""
    src='figG02_regional_access_environments.csv'
    d=pd.read_csv(sprint/'figures'/src)
    fig,ax=new_ax('employment opportunity mass','equivalent income  (euros / month)')
    for k,(profile,s) in enumerate(d.groupby('profile',sort=False)):
        ax.scatter(s.employment_opportunity_mass,s.W1_eur_per_month,
                   color=['#c81e28','#1450c8'][k],s=100,zorder=3,
                   label=profile.replace('household_','household '))
    ax.legend(loc='upper left')
    save(fig,'regional_profiles',out,src,'fixed profiles across regional access environments')


def f_matched_pair(sprint, out):
    """The matched pair, on ONE panel: the two things the slide contrasts.

    The message is that the preference profiles coincide while the chance of
    any offer does not, so both are put on the same axis -- two paired bars,
    with the coinciding pair read as one and the diverging pair as two.
    """
    src = "figE1_matched_pair.csv"
    e1 = pd.read_json(
        sprint / "runs" / "figE1_matched_households"
        / "e1_matched_households_v1.json", typ="series")
    pair = e1["pairs"]["employed::forward"]
    h1, h2 = pair["household_1"], pair["household_2"]
    cols = (C_ACC, C_PREF)

    rows = [
        ("how much they\nvalue their time",
         h1["omega_leisure_weight"], h2["omega_leisure_weight"], "%.2f"),
        ("their chance of\nany job offer",
         h1["pi_participation"], h2["pi_participation"], "%.2f"),
    ]
    fig, axes = plt.subplots(1, 2, figsize=FIGSIZE)
    for ax, (lab, v1, v2, fmt) in zip(axes, rows):
        vals = [v1, v2]
        x = np.arange(2)
        ax.bar(x, vals, width=0.56, color=cols, alpha=0.92,
               edgecolor="white", linewidth=2.0, zorder=3)
        for i, v in enumerate(vals):
            ax.annotate(fmt % v, xy=(x[i], v), xytext=(0, 12),
                        textcoords="offset points", ha="center",
                        fontsize=BASE + 6, fontweight="bold", color=cols[i])
        ax.set_xticks(x)
        ax.set_xticklabels(["one", "the other"])
        ax.set_title(lab, fontsize=BASE, pad=16)
        ax.set_ylim(0, max(vals) * 1.34)
        ax.grid(axis="x", visible=False)
        ax.tick_params(labelsize=MIN_PT + 1)
    save(fig, "matched_pair", out, src,
         "leisure weight and employment opportunity mass, the two households")


def f_couples(sprint, out):
    """Singles and couples side by side, equivalized."""
    src = "figC03_singles_vs_couples.csv"
    d = pd.read_csv(sprint / "figures" / src)
    chans = ["C_A", "C_B", "C_D", "C_P"]
    fig, ax = new_ax()
    x = np.arange(len(chans))
    w = 0.36
    for k, t in enumerate(["singles", "couples"]):
        s = d[d["type"] == t].set_index("quantity")
        base = float(d[(d["type"].str.startswith(t))
                       & (d["quantity"] == "I0000")]["value"].iloc[0])
        v = pct([float(s.loc[c, "value"]) / base for c in chans])
        ax.bar(x + (k - 0.5) * w, v, width=w,
               color=[CHANNEL_COLOUR[words(CHANNEL_WORDS, c)] for c in chans],
               alpha=0.92 if k == 0 else 0.42, edgecolor="white",
               linewidth=1.6, hatch=None if k == 0 else "//", zorder=3)
    ax.set_xticks(x)
    ax.set_xticklabels([CHANNEL_SHORT[words(CHANNEL_WORDS, c)]
                        for c in chans], fontsize=MIN_PT)
    ax.set_ylabel("share of measured inequality\nremoved  (%)", labelpad=14,
                  fontsize=MIN_PT + 1)
    ax.legend(handles=[Patch(facecolor=GREY, alpha=0.92, label="singles"),
                       Patch(facecolor=GREY, alpha=0.42, hatch="//",
                             label="couples")], loc="upper left", ncol=2)
    ax.grid(axis="x", visible=False)
    save(fig, "couples", out, src, "equivalized, both household types")


def f_draws(sprint, out):
    """The headline contributions against the draw count."""
    src = "figW05_welfare_vs_R.csv"
    d = pd.read_csv(sprint / "figures" / src)
    d = d[(d["basis"] == "raw") & (d["model"] == "S8")
          & (d["reference_arm"] == "singles_female")
          & (d["quantity"].isin(["C_P", "C_E"]))]
    fig, ax = new_ax()
    for q, lab in (("C_E", "opportunities and budgets"),
                   ("C_P", "preferences")):
        s = d[d["quantity"] == q].sort_values("R")
        col = CHANNEL_COLOUR[words(CHANNEL_WORDS, q)]
        ax.plot(s["R"], s["estimate"], "o-", color=col, lw=3.2, ms=13,
                zorder=3)
        ax.fill_between(s["R"], s["band_lo"], s["band_hi"], color=col,
                        alpha=0.20, zorder=2)
        ax.annotate(lab, xy=(s["R"].iloc[-1], s["estimate"].iloc[-1]),
                    xytext=(14, 0), textcoords="offset points", va="center",
                    color=col, fontweight="bold")
    ax.set_xscale("log")
    ax.set_xticks(sorted(d["R"].unique()))
    ax.get_xaxis().set_major_formatter(mticker.ScalarFormatter())
    ax.set_xlabel("drawn jobs per household", labelpad=12)
    ax.set_ylabel("contribution  (Gini points)", labelpad=12)
    ax.set_xlim(42, 620)
    save(fig, "draws", out, src, "S8 / female reference / raw")


def f_coefficients(sprint, out):
    """The estimated coefficients, one slide per block group (backup B1)."""
    src = "fig08_coefficients_by_block.csv"
    d = pd.read_csv(sprint / "figures" / src)
    blocks = list(dict.fromkeys(d["block"]))
    # three slides: split the blocks into three balanced groups
    groups, cur, size = [], [], 0
    target = int(np.ceil(len(d) / 3))
    for b in blocks:
        n = int((d["block"] == b).sum())
        if cur and size + n > target:
            groups.append(cur)
            cur, size = [], 0
        cur.append(b)
        size += n
    if cur:
        groups.append(cur)
    for gi, grp in enumerate(groups, start=1):
        s = d[d["block"].isin(grp)].reset_index(drop=True)
        fig, ax = new_ax()
        y = np.arange(len(s))[::-1]
        at_bound = s["at_active_bound"].astype(str).str.lower().isin(
            ["true", "1", "yes"])
        colours = [ACC[blocks.index(b) % len(ACC)] for b in s["block"]]
        for i in range(len(s)):
            if at_bound.iloc[i]:
                ax.plot(s["estimate"].iloc[i], y[i], "o", mfc="white",
                        mec=colours[i], mew=2.6, ms=13, zorder=4)
            else:
                ax.errorbar(s["estimate"].iloc[i], y[i],
                            xerr=[[s["estimate"].iloc[i] - s["lo95"].iloc[i]],
                                  [s["hi95"].iloc[i] - s["estimate"].iloc[i]]],
                            fmt="o", color=colours[i], ms=12, elinewidth=2.2,
                            capsize=6, capthick=2.0, zorder=4)
        ax.axvline(0.0, color=INK, lw=1.4, zorder=2)
        ax.set_yticks(y)
        ax.set_yticklabels([str(p) for p in s["param"]], fontsize=MIN_PT)
        ax.set_xlabel("estimate", labelpad=12)
        ax.grid(axis="y", visible=False)
        save(fig, "coefficients_%d" % gi, out, src,
             "blocks: " + ", ".join(grp))


def f_conceptual(sprint, out):
    """The schematic, one panel per file: (A) same tastes, different access;
    (B) same access, different tastes.  Redrawn at slide scale from the
    paper figure's own stylised parameters."""
    sys.path.insert(0, str(sprint / "runs" / "figT1"))
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "figT1", sprint / "runs" / "figT1" / "make_figT1_v1.py")
    t1 = importlib.util.module_from_spec(spec)
    with matplotlib.rc_context(SLIDE_RC):
        spec.loader.exec_module(t1)

    lbar = t1.LBAR
    l = np.linspace(6.0, 80.0, 500)

    def one(cases, name, panel):
        fig, ax = new_ax("leisure", "consumption")
        for job, pref, col in cases:
            h, c = job
            ub = t1.utility(c, lbar - h, **pref)
            for du in (-0.9, 0.0, 0.9):
                ax.plot(l, t1.indifference_c(l, ub + du, **pref), color=col,
                        lw=3.4 if du == 0.0 else 1.8,
                        alpha=1.0 if du == 0.0 else 0.32, zorder=3)
            ax.plot([lbar - h], [c], "o", ms=17, color=col, mec="white",
                    mew=2.4, zorder=6)
            w1 = t1.w1_level(job, pref)
            ax.axhline(w1, color=col, lw=2.2, ls=(0, (1, 1.8)), alpha=0.9,
                       zorder=2)
        ax.set_xlim(6, 84)
        ax.set_ylim(600, 3400)
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        save(fig, name, out, "runs/figT1/make_figT1_v1.py", panel)

    with matplotlib.rc_context(SLIDE_RC):
        one([(t1.JOB_RICH, t1.PREF_SHARED, C_ACC),
             (t1.JOB_THIN, t1.PREF_SHARED, C_PREF)],
            "conceptual_a", "same preferences, different opportunities")
        one([(t1.JOB_FT, t1.PREF_SHARED, C_ACC),
             (t1.JOB_PT, t1.PREF_LEISURE, C_PREF)],
            "conceptual_b", "same opportunities, different preferences")


# R-261 RETIRED three of these from the deck.  The smooth (c, l) schematic
# (f_conceptual) and the matched-pair bar chart (f_matched_pair) are now drawn
# in the companion theory talk's own TikZ grammar, on the deck's conceptual
# slides, so the rendered variants are no longer used.  Their generators are
# KEPT -- the paper still carries the smooth figure -- but they are out of the
# deck's figure set, and the verifier fails on an unused slide figure.
RETIRED = [f_conceptual, f_matched_pair]

FIGURES = [f_hours, f_external, f_environment,
           f_subgroup, f_benchmark, f_couples, f_coefficients]


def build(sprint: pathlib.Path, out: pathlib.Path, missing_only=False) -> int:
    print("rendering slide figures ->", out)
    if missing_only:
        # v4 explicitly reuses existing panels; only these three were absent.
        targets=[(f_observed_hours,'observed_hours'),
                 (f_headline_references,'headline_references'),
                 (f_regional_profiles,'regional_profiles')]
        chosen=[f for f,name in targets if not (out/(name+'_slide.pdf')).exists()]
    else:
        chosen=FIGURES+[f_observed_hours,f_headline_references,f_regional_profiles]
    for fn in chosen:
        with matplotlib.rc_context(SLIDE_RC):
            fn(sprint, out)
    idx = pd.DataFrame(INDEX)
    if missing_only and (out/'slide_figure_index.csv').exists():
        idx=pd.concat([pd.read_csv(out/'slide_figure_index.csv'),idx],ignore_index=True)
        idx=idx.drop_duplicates('slide_figure',keep='last')
        idx=idx[idx.slide_figure.map(lambda name:(out/name).exists())]
    idx.to_csv(out / "slide_figure_index.csv", index=False)
    # record the style actually used, for the deck verifier's font check
    rec = {k: SLIDE_RC[k] for k in
           ("font.size", "axes.labelsize", "axes.titlesize", "xtick.labelsize",
            "ytick.labelsize", "legend.fontsize", "figure.figsize")}
    rec["min_pt"] = MIN_PT
    pd.Series(rec).to_json(out / "slide_style_v1.json")
    print("wrote %d slide figures + the index" % len(idx))
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--sprint", type=pathlib.Path, default=DEFAULT_SPRINT)
    ap.add_argument("--out", type=pathlib.Path,
                    default=pathlib.Path(__file__).parent / "figures" / "slides")
    ap.add_argument('--missing-only',action='store_true')
    a = ap.parse_args()
    sys.exit(build(a.sprint, a.out, a.missing_only))
