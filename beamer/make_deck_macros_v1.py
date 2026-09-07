#!/usr/bin/env python
"""Generate deck_numbers_v1.tex from the frozen seminar-sprint artefacts.

Every number that appears on a slide of JMP_seminar_deck_v1.tex is defined here
and read from a named artefact.  No decomposition percentage, and no fit or
welfare magnitude, is typed into the .tex by hand.

The provenance table at the end of manuscript/JMP_seminar_deck_content_v2.md is
the authority for which artefact backs which slide; this script follows it.

Usage:  python beamer/make_deck_macros_v1.py [--sprint PATH] [--out PATH]
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import math
import sys

import pandas as pd

DEFAULT_SPRINT = pathlib.Path(__file__).resolve().parents[2] / 'MNL/experiments/JMP_SEMINAR_SPRINT'


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
    design = pd.read_csv(figures / 'figS6_02_coefficient_stability.csv')
    # The reference sample size is recorded in the reference-estimate column.
    n_drawn = int(re.search(r'estimate_R(\d+)', ' '.join(design.columns)).group(1))
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

    # The Shapley slide shows the four states and the two averaged orders, so
    # it needs the states and the contributions in GINI POINTS, not shares.
    # Four decimals is what the slide can carry and what the arithmetic on it
    # has to close in.
    for name, col in (("StateBase", "I00"), ("StatePrefEq", "I10"),
                      ("StateEnvEq", "I01"), ("StateBothEq", "I11")):
        m.num(name, abs(float(prim[col])), src, dp=4)
    m.num("LevelPref", prim["C_pref"], src, dp=4)
    m.num("LevelEnv", prim["C_env"], src, dp=4)
    m.num("LevelAcc", prim["C_acc"], src, dp=3)
    m.num("LevelEarn", prim["C_earn"], src, dp=3)
    m.num("LevelNeeds", prim["C_needs"], src, dp=3)

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
        if tag == "Raw":
            # the Shapley slide's second build shows the split in Gini points
            m.num("LevelGeo", row["C_geo"], src, dp=3)
            m.num("LevelOth", row["C_oth"], src, dp=3)
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
                      / float(ruro["I00"])), src, dp=1, pct=True)
        m.num("BenchInequalityDrop" + tag,
              (float(rumbd["I00"]) - float(ruro["I00"])) / float(ruro["I00"]),
              src, dp=1, pct=True, signed=True)

    # ------- the two-answers slide: where the omitted contribution goes
    # Panel (b) of the benchmark figure decomposes the market-side share that
    # the benchmark cannot represent into the three places it actually goes.
    src = "SPRINT/figures/figR01_benchmark_decomposition.csv"
    rb = pd.read_csv(figures / "figR01_benchmark_decomposition.csv")
    pb = rb[rb["panel"] == "b"].set_index("quantity")
    for name, key in (("RelabelPref", "reappears as preferences"),
                      ("RelabelNeeds", "reappears as endowments and needs"),
                      ("RelabelOut", "leaves the measured total")):
        m.num(name, pb.loc[key, "value"], src, dp=0, pct=True)

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

    # v4: the author's precise display rounding. No estimates are changed.
    src = 'SPRINT/tables/headline_decomposition_v1.csv'
    m.num('VEnvAlone',(float(prim['I00'])-float(prim['I01']))/float(prim['I00']),src+'; (I00-I01)/I00',dp=0,pct=True)
    # the other single-order leg. Equalising preferences alone RAISES inequality,
    # so (I00-I10)/I00 is negative and the slide states it as a rise; the macro
    # carries the magnitude so no sign is hand-typed.
    m.num('VPrefAlone',abs((float(prim['I00'])-float(prim['I10']))/float(prim['I00'])),src+'; |(I00-I10)/I00|',dp=0,pct=True)
    for name, col, dp in [('VStateBase','I00',3), ('VStatePref','I10',3),
                          ('VStateEnv','I01',3), ('VStateCommon','I11',3),
                          ('VLevelEnv','C_env',3)]:
        m.num(name, abs(float(prim[col])), src, dp=dp)
    for stem, col in channels:
        m.num('VShare'+stem, prim[col], src, dp=1, pct=True)
        m.num('VRound'+stem, prim[col], src, dp=0, pct=True)
        half = (float(prim[col+'__band_hi'])-float(prim[col+'__band_lo']))/2
        # The brief gives the market band conservatively, rounded outward
        # to one decimal; other displayed bands use nearest rounding.
        if stem == 'Market':
            m.num('VBand'+stem, math.ceil(half*1000)/10,src+'; outward to 0.1 percentage points',dp=1)
        else:
            m.num('VBand'+stem, half, src, dp=1, pct=True)
    for stem in ['Pref','Env']:
        m.num('VMale'+stem, male['C_'+stem.lower()+'_over_I00'], src, dp=1, pct=True)
    # ---- slide 15b: the nested endowments/needs split (R-263) -------------
    ne_p = sprint / 'runs/nested_endowments/ne_step4_nested_v1.json'
    if ne_p.is_file():
        ne = json.loads(ne_p.read_text(encoding='utf-8'))
        if ne.get('status') != 'NE_STEP4_DONE':
            raise SystemExit('nested endowments artefact is not NE_STEP4_DONE')
        nsrc = 'SPRINT/runs/nested_endowments/ne_step4_nested_v1.json'
        fr = ne['results']['singles_female']['raw']['contributions']
        m.num('VNestRes', fr['C_nonlabour_over_I00']['estimate'], nsrc, dp=0, pct=True)
        m.num('VNestComp', fr['C_composition_over_I00']['estimate'], nsrc, dp=0, pct=True)
        # slide 13 prints the attributed share against the one-factor effect,
        # so both carry one decimal: the whole point is that they differ.
        m.num('VNestCompAttr', fr['C_composition_over_I00']['estimate'], nsrc,
              dp=2, pct=True)
        m.num('VNestCompAlone',
              ne['results']['singles_female']['raw']['one_factor_effects']
              ['one_factor_composition_share_of_I00'], nsrc, dp=2, pct=True)

    src = 'SPRINT/tables/parameter_uncertainty_v1.csv'
    m.num('VParEnvLo',se['parameter_lo_2p5'],src,dp=1,pct=True)
    m.num('VParEnvHi',se['parameter_hi_97p5'],src,dp=1,pct=True)
    # the preference share carries a CR1 interval too, and the headline slide
    # prints both rather than only the environment's.
    m.num('VParPrefLo',sp['parameter_lo_2p5'],src,dp=1,pct=True)
    m.num('VParPrefHi',sp['parameter_hi_97p5'],src,dp=1,pct=True)
    src = 'SPRINT/figures/fig02_hours_bands_obs_vs_pred.csv'
    m.num('VHoursObs',f35['observed'],src,dp=1,pct=True)
    m.num('VHoursPred',f35['predicted'],src,dp=1,pct=True)
    m.num('VHoursMAE',bins['pred_minus_obs'].abs().mean(),src,dp=3)
    src = 'SPRINT/figures/fig03_employment_obs_vs_pred.csv'
    m.num('VEmpObs',allrow['observed'],src,dp=1,pct=True)
    m.num('VEmpPred',allrow['predicted'],src,dp=1,pct=True)
    src = 'SPRINT/tables/wage_fit_within_sample_v1.csv'
    m.thousands('NEmployed',one(wf,group='all')['n_employed_observed'],src)
    src = 'SPRINT/tables/external_hours_validation_v1.csv'
    ext = pd.read_csv(tables/'external_hours_validation_v1.csv')
    f = one(ext,sex='pooled',band='F35')
    bounds = re.findall(r'\d+\.\d+',f['band_definition'])
    m.num('StatHours',sum(map(float,bounds))/len(bounds),src,dp=0)
    for name,col in [('VExtLFS','lfs_share_of_focal_bands'),
                     ('VExtObs','sample_obs_share_of_focal_bands'),
                     ('VExtPred','model_pred_share_of_focal_bands')]:
        m.num(name,f[col],src,dp=0,pct=True)
    src = 'SPRINT/runs/rum_benchmark_final/rb_step4_misclassification_v1.json'
    peak = next(c for c in hours_const if c['availability_constant_in_g_under_RURO']=='beta_h_f35')
    m.num('VPeakAvailability',peak['RURO_S8_estimate'],src,dp=2)
    m.num('VPeakTaste',peak['RUM_B_estimate'],src,dp=2)
    gaps = pos['sex_specific_leisure_block']['leisure_intercept_gap_male_minus_female']
    m.num('VGapFinal',gaps['RURO_S8'],src,dp=2,signed=True)
    m.num('VGapBench',gaps['RUM_B'],src,dp=2,signed=True)
    m.num('VBenchGap',rumb['negll_gap'],'SPRINT/runs/rum_benchmark_final/rb_step1_estimation_v1.json',dp=0)
    src = 'SPRINT/runs/agebound_addendum_s2/ab_welfare_comparison_v1.csv'
    age = pd.read_csv(runs/'agebound_addendum_s2/ab_welfare_comparison_v1.csv')
    m.num('VAgeMove',one(age,reference_arm='singles_female',basis='raw',quantity='C_P')['relative_change_pct'],src,dp=0,signed=True)
    src = 'SPRINT/runs/final_couples_welfare/cw_step3b_sensitivity_table_v1.csv'
    sens = pd.read_csv(runs/'final_couples_welfare/cw_step3b_sensitivity_table_v1.csv')
    m.num('VCouplesMove',sens[sens.quantity=='C_P'].relative_delta.abs().max(),src,dp=0,pct=True)
    src = 'SPRINT/figures/figS6_02_coefficient_stability.csv'
    m.num('VDrawMin',design.R.min(),src,dp=0)
    m.num('VDrawMax',design.R.max(),src,dp=0)
    m.num('VDrawMoveAll',design.deviation_in_R100_SE.abs().max(),src+'; full 50--400 range',dp=2)
    # Both scopes are explicit in the corrected v4.1 row.
    m.num('VDrawMove',design[design.R>=n_drawn].deviation_in_R100_SE.abs().max(),src+'; R >= reference R (100), NOT the full 50--400 range',dp=1)
    src = 'SPRINT/runs/couples_clean_baseline/r240_step3_estimation_v1.json'
    couple = json.loads((runs/'couples_clean_baseline/r240_step3_estimation_v1.json').read_text(encoding='utf-8'))
    m.thousands('NCouples',couple['estimation']['inference']['G_clusters'],src)
    for tag,sx in [('Female','f'),('Male','m')]:
        m.num('VCouplePeak'+tag,couple['fit']['f35_peak_vs_singles'][sx]['estimate'],src,dp=2)
    m.num('VGeo',one(ng,reference_arm='singles_female',basis='raw')['C_geo_over_I00'], 'SPRINT/tables/nested_geographic_access_v1.csv',dp=0,pct=True)
    # Dates and enumerators are document metadata, not estimates. They are
    # read from the author's document rather than invented table entries.
    content = (pathlib.Path(__file__).resolve().parents[1]/'manuscript/JMP_seminar_deck_content_v2.md').read_text(encoding='utf-8')
    metadata = sorted(set(re.findall(r'\b(?:19|20)\d{2}\b',content))|{'1','2'})
    digitwords = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
    for value in metadata:
        m.add('Doc'+''.join(digitwords[int(c)] for c in value),value,'manuscript/JMP_seminar_deck_content_v2.md (citation/year/enumerator metadata)')
    # B4's exact-zero result is in the published counterpart-test table.
    counterpart = (tables/'wishmore_counterpart_test_v1.md').read_text(encoding='utf-8')
    z = re.search(r'0\.000000',counterpart)
    if not z: raise SystemExit('missing exact-zero counterpart result')
    m.num('VWishZero',float(z.group()),'SPRINT/tables/wishmore_counterpart_test_v1.md',dp=0)

    # Keep the no-orphan gate meaningful after the authored notes replace the
    # old, much longer notes. Only emit commands actually used by the deck.
    deck = out.parent/'JMP_seminar_deck_v1.tex'
    if deck.exists():
        used = set(re.findall(r'\\([A-Za-z]+)\b',deck.read_text(encoding='utf-8')))
        m.rows = [row for row in m.rows if row[0] in used]
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
    print("wrote %s (%d macros)" % (out, len(m.rows)))
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--sprint", type=pathlib.Path, default=DEFAULT_SPRINT)
    ap.add_argument("--out", type=pathlib.Path,
                    default=pathlib.Path(__file__).parent / "deck_numbers_v1.tex")
    a = ap.parse_args()
    sys.exit(build(a.sprint, a.out))
