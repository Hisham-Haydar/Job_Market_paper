#!/usr/bin/env python
"""Generate deck_numbers_v1.tex from the frozen seminar-sprint artefacts.

Every number that appears on a slide of JMP_seminar_deck_v1.tex is defined here
and read from a named artefact.  No decomposition percentage, and no fit or
welfare magnitude, is typed into the .tex by hand.

The provenance table at the end of manuscript/JMP_seminar_deck_content_v1.md is
the authority for which artefact backs which slide; this script follows it.

Usage:  python beamer/make_deck_macros_v1.py [--sprint PATH] [--out PATH]
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys

import pandas as pd

DEFAULT_SPRINT = pathlib.Path(
    r"C:\Users\hisham\Repo\MNL\experiments\JMP_SEMINAR_SPRINT"
)


class Macros:
    """Collects \\newcommand definitions, refusing silent redefinition."""

    def __init__(self):
        self.rows = []
        self.seen = set()

    def add(self, name, value, source):
        # TeX control-sequence names are letters only: \FooB2 would parse as
        # \FooB followed by the character 2, silently splitting the macro.
        if not name.isalpha():
            raise SystemExit("macro name must be letters only: " + name)
        if name in self.seen:
            raise SystemExit("duplicate macro: " + name)
        self.seen.add(name)
        self.rows.append((name, str(value), source))

    def num(self, name, value, source, dp=2, pct=False, signed=False):
        v = float(value) * (100.0 if pct else 1.0)
        fmt = "{:+." + str(dp) + "f}" if signed else "{:." + str(dp) + "f}"
        self.add(name, fmt.format(v), source)

    def thousands(self, name, value, source):
        self.add(name, "{:,}".format(int(round(float(value)))).replace(",", "{,}"),
                 source)

    def render(self, header):
        out = [header, ""]
        last = None
        for name, value, source in self.rows:
            if source != last:
                out.append("")
                out.append("% ---- " + source)
                last = source
            out.append("\\newcommand{\\" + name + "}{" + value + "}")
        out.append("")
        out.append("% " + str(len(self.rows)) + " macros emitted.")
        out.append("\\endinput")
        return "\n".join(out) + "\n"


def one(df, **eq):
    """Select the unique row matching all equality constraints."""
    sub = df
    for col, val in eq.items():
        sub = sub[sub[col] == val]
    if len(sub) != 1:
        raise SystemExit("expected 1 row for %r, got %d" % (eq, len(sub)))
    return sub.iloc[0]


def build(sprint, out):
    tables = sprint / "tables"
    figures = sprint / "figures"
    runs = sprint / "runs"
    m = Macros()

    # ------------------------------------------------ slide 6: the sample
    src = "sample: fig03_employment_obs_vs_pred.csv + the sampled-set design"
    emp = pd.read_csv(figures / "fig03_employment_obs_vs_pred.csv")
    n_hh = int(one(emp, group="all")["households"])
    n_drawn = 100                      # drawn latent jobs per household
    n_alt = n_drawn + 1                # + the observed job, inserted deterministically
    m.thousands("NHouseholds", n_hh, src)
    m.add("NAlternatives", n_alt, src)
    m.add("NDrawnJobs", n_drawn, src)
    m.thousands("NPricedRows", n_hh * n_alt, src)

    # ------------------------------- slides 10-11: within-sample fit
    src = "SPRINT/figures/fig02_hours_bands_obs_vs_pred.csv"
    hb = pd.read_csv(figures / "fig02_hours_bands_obs_vs_pred.csv")
    bins = hb[hb["band"] != "[33.5,36.5) peak"]        # 12 bins; last row is a repeat
    f35 = one(hb, band="F35 ref (33.5-36.5)")
    m.num("HoursStatObs", f35["observed"], src, dp=4)
    m.num("HoursStatPred", f35["predicted"], src, dp=4)
    m.num("HoursStatObsPct", f35["observed"], src, dp=2, pct=True)
    m.num("HoursStatPredPct", f35["predicted"], src, dp=2, pct=True)
    m.num("HoursMAE", bins["pred_minus_obs"].abs().mean(), src, dp=4)
    m.add("HoursNBins", len(bins), src)
    m.num("HoursBandShortfall", one(hb, band="40.5-44.5")["pred_minus_obs"],
          src, dp=3, signed=True)

    src = "SPRINT/figures/fig03_employment_obs_vs_pred.csv"
    allrow = one(emp, group="all")
    m.num("EmpObs", allrow["observed"], src, dp=4)
    m.num("EmpPred", allrow["predicted"], src, dp=4)

    src = "SPRINT/figures/fig04_occupation_obs_vs_pred.csv"
    occ = pd.read_csv(figures / "fig04_occupation_obs_vs_pred.csv")
    m.num("OccMaxDev", occ["pred_minus_obs"].abs().max(), src, dp=4)
    m.add("OccNCategories", len(occ), src)

    src = "SPRINT/tables/wage_fit_within_sample_v1.csv"
    wf = pd.read_csv(tables / "wage_fit_within_sample_v1.csv")
    m.num("WageMedFitMen", one(wf, group="male")["median_fit_eur_h"], src, dp=2)
    m.num("WageMedFitWomen", one(wf, group="female")["median_fit_eur_h"], src, dp=2)
    m.num("WageMedFitAll", one(wf, group="all")["median_fit_eur_h"], src, dp=2)

    # ---------------------------------- slide 13: external hours validation
    src = "SPRINT/figures/figX1_external_hours_lfs_validation.csv"
    xh = pd.read_csv(figures / "figX1_external_hours_lfs_validation.csv")
    # panel (b) is the one validation panel: three sources on the statutory band
    for tag, source_label in (("LFS", "external benchmark"),
                              ("Obs", "observed sample"),
                              ("Pred", "model-implied")):
        m.num("ExtStatBand" + tag,
              one(xh, panel="b", sex="pooled", band="F35", source=source_label)["value"],
              src, dp=1, pct=True)
    for tag, sx in (("Women", "female"), ("Men", "male")):
        m.num("ExtStatBandLFS" + tag,
              one(xh, panel="b", sex=sx, band="F35",
                  source="external benchmark")["value"],
              src, dp=1, pct=True)
    # panel (a): the descriptive wish-more gradient, pooled, employed
    pa = xh[(xh["panel"] == "a") & (xh["sex"] == "pooled")]
    # NOTE: macro names must be letters only -- TeX would split \ExtWishFthirtyfive
    # after the first digit, so spell the band out.
    m.num("ExtWishStatBand", one(pa, band="F35")["wish_more_share_code2_YES"],
          src, dp=1, pct=True)
    m.num("ExtWishLongHours", one(pa, band="LH")["wish_more_share_code2_YES"],
          src, dp=1, pct=True)

    # ------------------------------------------ slide 14: the matched pair
    src = "SPRINT/runs/figE1_matched_households/e1_matched_households_v1.json"
    e1 = json.loads((runs / "figE1_matched_households"
                     / "e1_matched_households_v1.json").read_text(encoding="utf-8"))
    rank = e1["rankings"]["employed"]
    pair = e1["pairs"]["employed::forward"]
    h1, h2 = pair["household_1"], pair["household_2"]
    m.thousands("EOneNPairs", rank["n_pairs"], src)
    m.num("EOneSeparation", pair["separation_vs_admissible_median"], src, dp=2)
    m.num("EOneOmegaA", h1["omega_leisure_weight"], src, dp=2)
    m.num("EOneOmegaB", h2["omega_leisure_weight"], src, dp=2)
    m.num("EOnePiA", h1["pi_participation"], src, dp=3)
    m.num("EOnePiB", h2["pi_participation"], src, dp=3)
    m.add("EOneHours", "{:.0f}".format(h1["observed_hours"]), src)

    # ------------------ slides 15-16: the headline decomposition (exact table)
    src = "SPRINT/tables/headline_decomposition_v1.csv"
    hd = pd.read_csv(tables / "headline_decomposition_v1.csv")
    prim = one(hd, model="S8", reference_arm="singles_female", basis="raw")
    male = one(hd, model="S8", reference_arm="singles_male_structural_zero", basis="raw")
    eqv = one(hd, model="S8", reference_arm="singles_female", basis="equivalized")
    eqvmale = one(hd, model="S8", reference_arm="singles_male_structural_zero",
                  basis="equivalized")

    m.num("IBaseline", prim["I00"], src, dp=6)
    m.num("IBaselineShort", prim["I00"], src, dp=3)
    m.num("IPrefOnly", prim["I10"], src, dp=6)
    m.num("IEnvOnly", prim["I01"], src, dp=6)
    m.num("IEnvOnlyShort", prim["I01"], src, dp=3)
    m.num("IBothCommon", abs(float(prim["I11"])), src, dp=6)

    channels = [("Pref", "C_pref_over_I00"), ("Env", "C_env_over_I00"),
                ("Acc", "C_acc_over_I00"), ("Earn", "C_earn_over_I00"),
                ("Needs", "C_needs_over_I00"),
                ("Market", "C_acc_plus_C_earn_over_I00")]
    for stem, col in channels:
        m.num("Share" + stem, prim[col], src, dp=2, pct=True)
        half = (float(prim[col + "__band_hi"]) - float(prim[col + "__band_lo"])) / 2.0
        m.num("Band" + stem, half, src, dp=2, pct=True)
        m.num("Share" + stem + "Eqv", eqv[col], src, dp=2, pct=True)
    m.num("SharePrefMaleRef", male["C_pref_over_I00"], src, dp=2, pct=True)
    m.num("ShareMarketMaleRef", male["C_acc_plus_C_earn_over_I00"], src, dp=2, pct=True)
    m.num("SharePrefEqvMaleRef", eqvmale["C_pref_over_I00"], src, dp=2, pct=True)
    m.num("SharePrefEnvLo", hd["C_pref_over_I00"].min(), src, dp=1, pct=True)
    m.num("SharePrefEnvHi", hd["C_pref_over_I00"].max(), src, dp=1, pct=True)

    # Rounded forms for the slide HEADLINES.  A headline carries one number and
    # it is spoken, so it is quoted to the nearest point; the exact value and
    # its band stay in the speaker notes and on the figure.  Only the channels
    # a headline actually names get one -- an unused macro is an orphan the
    # verifier rejects.
    for stem in ("Pref", "Env", "Needs", "Market"):
        col = dict(channels)[stem]
        m.num("Rnd" + stem, prim[col], src, dp=0, pct=True)
    m.num("RndPrefMaleRef", male["C_pref_over_I00"], src, dp=0, pct=True)

    # ------------------------------ slide 15, second click: the two intervals
    src = "SPRINT/tables/parameter_uncertainty_v1.csv"
    pu = pd.read_csv(tables / "parameter_uncertainty_v1.csv")
    sp = one(pu, model="S8", reference_arm="singles_female", basis="raw",
             quantity="s_pref")
    se = one(pu, model="S8", reference_arm="singles_female", basis="raw",
             quantity="s_env")
    m.num("ParPrefLo", sp["parameter_lo_2p5"], src, dp=2, pct=True)
    m.num("ParPrefHi", sp["parameter_hi_97p5"], src, dp=2, pct=True)
    m.num("ParEnvLo", se["parameter_lo_2p5"], src, dp=2, pct=True)
    m.num("ParEnvHi", se["parameter_hi_97p5"], src, dp=2, pct=True)
    shares = pu[pu["is_share"] == True]
    m.add("ParWidenLo", "{:.0f}".format(shares["parameter_over_rqmc_width"].min()), src)
    m.add("ParWidenHi", "{:.0f}".format(shares["parameter_over_rqmc_width"].max()), src)
    m.add("ParKInterior", int(sp["K"]), src)

    gsh = pu[pu["quantity"] == "C_geo_share_of_C_acc"]
    if len(gsh):
        g = gsh[gsh["basis"] == "raw"].iloc[0]
        m.num("ParGeoShareLo", g["parameter_lo_2p5"], src, dp=0, pct=True)
        m.num("ParGeoShareHi", g["parameter_hi_97p5"], src, dp=0, pct=True)

    # ------------------------------------------- slide 17: inside job access
    src = "SPRINT/tables/nested_geographic_access_v1.csv"
    ng = pd.read_csv(tables / "nested_geographic_access_v1.csv")
    for tag, basis in (("Raw", "raw"), ("Eqv", "equivalized")):
        row = one(ng, model="S8", basis=basis, reference_arm="singles_female")
        m.num("ShareGeo" + tag, row["C_geo_over_I00"], src, dp=2, pct=True)
        m.num("BandGeo" + tag, row["C_geo_over_I00__E_T"], src, dp=2, pct=True)
        m.num("ShareAccNested" + tag, row["C_acc_over_I00"], src, dp=2, pct=True)
        m.num("GeoShareOfAcc" + tag, row["C_geo_share_of_C_acc"], src, dp=2, pct=True)
        m.num("BandGeoShareOfAcc" + tag, row["C_geo_share_of_C_acc__E_T"],
              src, dp=2, pct=True)
        if tag == "Raw":          # only the raw share reaches a headline
            m.num("RndGeoShareOfAcc" + tag, row["C_geo_share_of_C_acc"],
                  src, dp=0, pct=True)

    # ---------------------- slide 17, second click: 24 regional environments
    src = "SPRINT/figures/figG02_regional_access_environments.csv"
    rg = pd.read_csv(figures / "figG02_regional_access_environments.csv")
    m.add("NRegionalEnvs", int(rg.groupby("profile").size().max()), src)
    for tag, prof in (("A", "household_1"), ("B", "household_2")):
        g = rg[rg["profile"] == prof]
        m.num("RegMass" + tag + "Lo", g["employment_opportunity_mass"].min(), src, dp=3)
        m.num("RegMass" + tag + "Hi", g["employment_opportunity_mass"].max(), src, dp=3)
        m.thousands("RegWelf" + tag + "Lo", g["W1_eur_per_month"].min(), src)
        m.thousands("RegWelf" + tag + "Hi", g["W1_eur_per_month"].max(), src)

    # -------------------------------------------- slide 18: the sex subgroup
    src = "SPRINT/tables/subgroup_decomposition_v1.csv"
    sg = pd.read_csv(tables / "subgroup_decomposition_v1.csv")
    sex = sg[sg["dimension"] == "sex"]

    def sub(group, quantity, arm="singles_female", basis="raw"):
        return one(sex, group=group, quantity=quantity,
                   reference_arm=arm, basis=basis)

    for tag, grp in (("Men", "men"), ("Women", "women")):
        acc = sub(grp, "C_acc_over_I00")
        m.num("SubAcc" + tag, acc["estimate"], src, dp=2, pct=True)
        m.num("SubAcc" + tag + "MaleRef",
              sub(grp, "C_acc_over_I00", arm="singles_male_structural_zero")["estimate"],
              src, dp=2, pct=True)
        m.num("SubAcc" + tag + "Eqv",
              sub(grp, "C_acc_over_I00", basis="equivalized")["estimate"],
              src, dp=2, pct=True)
        m.num("SubGeo" + tag, sub(grp, "C_geo_over_I00")["estimate"],
              src, dp=2, pct=True)
        m.num("RndSubAcc" + tag, acc["estimate"], src, dp=0, pct=True)
    m.num("SubPrefMenFemRef", sub("men", "s_pref")["estimate"],
          src, dp=2, pct=True, signed=True)
    m.num("SubPrefMenMaleRef",
          sub("men", "s_pref", arm="singles_male_structural_zero")["estimate"],
          src, dp=2, pct=True, signed=True)

    # ------------------------------- slide 19: the common-choice-set benchmark
    src = "SPRINT/runs/rum_benchmark_final/rb_step1_estimation_v1.json"
    rb1 = json.loads((runs / "rum_benchmark_final"
                      / "rb_step1_estimation_v1.json").read_text(encoding="utf-8"))
    nest = rb1["step6_nesting"]
    comp = nest["comparator"]
    m.num("PrefNegLL", comp["negll"], src, dp=2)
    m.add("PrefNFree", int(comp["n_free"]), src)
    rumb = nest["variants"].get("RUM_B") or list(nest["variants"].values())[-1]
    m.num("BenchNegLL", rumb["negll"], src, dp=2)
    m.num("BenchGapNats", rumb["negll_gap"], src, dp=1)
    m.num("BenchLR", rumb["LR_statistic_2x_negll_gap"], src, dp=1)
    m.add("BenchDF", int(rumb["df"]), src)

    src = "SPRINT/runs/rum_benchmark_final/rb_step2_fit_comparison_v1.csv"
    fc = pd.read_csv(runs / "rum_benchmark_final" / "rb_step2_fit_comparison_v1.csv")
    fc.to_csv(out.parent / "_fit_comparison_echo.csv", index=False)  # audit echo

    src = "SPRINT/runs/rum_benchmark_final/rb_step4_misclassification_v1.json"
    rb4 = json.loads((runs / "rum_benchmark_final"
                      / "rb_step4_misclassification_v1.json").read_text(encoding="utf-8"))
    pos = rb4["positive_side_misclassification"]
    hours_const = [c for c in pos["relocated_constants"]
                   if c["availability_constant_in_g_under_RURO"].startswith("beta_h_")]
    m.num("BenchConstMAD",
          sum(abs(c["difference"]) for c in hours_const) / len(hours_const),
          src, dp=3)
    m.add("BenchNConstants", len(hours_const), src)

    src = "SPRINT/tables/rum_benchmark_decomposition_v1.csv"
    rd = pd.read_csv(tables / "rum_benchmark_decomposition_v1.csv")
    for tag, basis in (("Raw", "raw"), ("Eqv", "equivalized")):
        sel = rd[(rd["basis"] == basis) & (rd["reference_arm"] == "singles_female")]
        ruro = sel[sel["model"] == "RURO"].iloc[0]
        rumbd = sel[sel["model"] != "RURO"].iloc[0]
        if tag == "Raw":
            m.num("BenchSharePrefRURO", ruro["C_pref_over_I00"], src, dp=1, pct=True)
            m.num("BenchSharePrefRUMB", rumbd["C_pref_over_I00"], src, dp=1, pct=True)
            m.num("RndBenchDropRaw",
                  abs((float(rumbd["I00"]) - float(ruro["I00"]))
                      / float(ruro["I00"])), src, dp=0, pct=True)
        m.num("BenchInequalityDrop" + tag,
              (float(rumbd["I00"]) - float(ruro["I00"])) / float(ruro["I00"]),
              src, dp=1, pct=True, signed=True)

    # ------------------------------------------ B1: estimated coefficients
    src = "SPRINT/figures/fig08_coefficients_by_block.csv"
    cb = pd.read_csv(figures / "fig08_coefficients_by_block.csv")
    m.add("NEstimatedParams", len(cb), src)

    # --------------------------------------- B4: the wish-more counterpart
    src = "SPRINT/tables/wishmore_counterpart_test_v1.csv"
    wm = pd.read_csv(tables / "wishmore_counterpart_test_v1.csv")
    pooled = wm[(wm["sex"] == "pooled") & (wm["is_priced_band"] == True)]
    w = pooled["weighted_share_of_workers"].astype(float)
    m.num("WishModel",
          float((pooled["model_underemployed_share"].astype(float) * w).sum() / w.sum()),
          src, dp=1, pct=True)
    # the external aggregate is the run record's own five-focal-band share, not a
    # model-weighted re-average: WISHMORE code 2 is the "wishes more" branch
    # (the export's delivered code 1 is No -- the label is inverted at source).
    src = "SPRINT/runs/external_hours_lfs/xh1_table_record_v1.json"
    xh1 = json.loads((runs / "external_hours_lfs"
                      / "xh1_table_record_v1.json").read_text(encoding="utf-8"))
    m.num("WishLFS",
          xh1["wishmore_verdict"]["what_the_reversed_map_implies"][
              "implied_share_wishing_more_over_the_five_focal_bands"],
          src, dp=1, pct=True)

    header = "\n".join([
        "% deck_numbers_v1.tex --- GENERATED FILE.  DO NOT EDIT BY HAND.",
        "%",
        "% Produced by beamer/make_deck_macros_v1.py from the frozen seminar-sprint",
        "% artefacts of the estimation repository:",
        "%   " + str(sprint),
        "%",
        "% Every number on every slide of JMP_seminar_deck_v1.tex is defined here and",
        "% read from a named artefact.  No decomposition percentage is typed by hand.",
        "% Regenerate with:  python beamer/make_deck_macros_v1.py",
    ])
    out.write_text(m.render(header), encoding="utf-8")
    (out.parent / "_fit_comparison_echo.csv").unlink(missing_ok=True)
    print("wrote %s (%d macros)" % (out, len(m.rows)))
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--sprint", type=pathlib.Path, default=DEFAULT_SPRINT)
    ap.add_argument("--out", type=pathlib.Path,
                    default=pathlib.Path(__file__).parent / "deck_numbers_v1.tex")
    a = ap.parse_args()
    sys.exit(build(a.sprint, a.out))
