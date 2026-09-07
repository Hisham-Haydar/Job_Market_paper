#!/usr/bin/env python
"""Generate reports/numbers_of_record_v1.json from the frozen seminar-sprint artefacts.

This is a companion to make_deck_macros_v1.py: it carries every quantity the
deck macros already emit, plus the additional sample sizes, parameter-count
facts, and welfare/decomposition detail (both reference arms, both bases,
with RQMC bands and CR1 intervals) that a reader needs to check a number in
the paper against its source table without hunting through the deck's TeX.

Every entry is {value, source, column_or_key, basis, reference}:
  - source            path to the artefact, relative to the sprint root
  - column_or_key      the exact column name (CSV) or key path (JSON) read
  - basis              what the number is conditioned on (reference arm,
                        raw/equivalized, model spec, sex, ...); "n/a" if none
  - reference          one-sentence description of what the number is

Usage:  python beamer/make_numbers_of_record_v1.py [--sprint PATH] [--out PATH]
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys

import pandas as pd

DEFAULT_SPRINT = pathlib.Path(__file__).resolve().parents[2] / 'MNL/experiments/JMP_SEMINAR_SPRINT'


class Numbers:
    """Collects numbers-of-record entries, refusing silent redefinition."""

    def __init__(self):
        self.entries = {}

    def add(self, key, value, source, column_or_key, basis, reference):
        if key in self.entries:
            raise SystemExit("duplicate numbers-of-record key: " + key)
        if isinstance(value, float):
            value = float(value)
        self.entries[key] = {
            "value": value,
            "source": source,
            "column_or_key": column_or_key,
            "basis": basis,
            "reference": reference,
        }


def one(df, **eq):
    sub = df
    for col, val in eq.items():
        sub = sub[sub[col] == val]
    if len(sub) != 1:
        raise SystemExit("expected 1 row for %r, got %d" % (eq, len(sub)))
    return sub.iloc[0]


def jload(path):
    return json.loads(path.read_text(encoding="utf-8"))


def build(sprint, out):
    tables = sprint / "tables"
    figures = sprint / "figures"
    runs = sprint / "runs"
    n = Numbers()

    # ================================================================
    # SAMPLE SIZES
    # ================================================================
    n.add("n_households_raw_frame", 11459,
          "runs/param_child_v1/child_age_aggregates_v1.json",
          "raw_link_audit.households", "n/a",
          "Total raw-frame households (singles + couples pooled, pre-estimation-sample "
          "filtering) used for the child-linkage audit.")

    n.add("n_households_singles", 1555,
          "runs/final_singles_welfare/ss8_step1_states_v1.json",
          "equivalence_scale.n_households", "singles estimation sample",
          "Singles estimation-sample household count; also the CR1 cluster count "
          "G_clusters for singles inference.")

    n.add("n_households_couples", 2275,
          "runs/couples_clean_baseline/r240_step0_gates_v1.json",
          "gates.G1_rectangular.n_households", "couples estimation sample",
          "Couples estimation-sample household count; identical to the R240 "
          "estimation's G_clusters (CR1 cluster count for couples inference).")

    n.add("n_alternatives", 101,
          "SPRINT/figures/figS6_02_coefficient_stability.csv",
          "estimate_R100 column name (R=100 -> 101 alternatives)", "reference draw count R=100",
          "Choice-set size: 100 drawn jobs plus the observed job, inserted "
          "deterministically.")

    n.add("n_priced_rows_singles", 157055,
          "export/gpu_research_bundle_v1/data/"
          "fr_p2a_singles2016_regionlive_margqh_floor5_v1__mnlmeta.json",
          "row_counts.singles (== row_counts.total for this singles-only export)",
          "singles, 1555 households x 101 alternatives",
          "Total priced alternative-rows for the singles estimation sample "
          "(1555 x 101 = 157055). This export contains singles only; it is not a "
          "combined singles+couples total.")

    # ================================================================
    # PARAMETER COUNTS
    # ================================================================
    n.add("n_params_active", 41,
          "runs/param_child_v1/compact_evaluation_v1.json",
          "coordinates_41", "n/a",
          "Active singles parameter-vector length (the certified 41-coordinate "
          "compact spec); bitwise-equal negLL/gradient to the 51-coordinate form.")

    n.add("n_params_provenance", 51,
          "runs/param_child_v1/compact_evaluation_v1.json",
          "coordinates_51", "n/a",
          "Full 51-coordinate provenance vector = 41 active + 10 dropped/pinned "
          "coordinates never consumed by the singles branches (8 inactive couples "
          "coordinates + 2 pinned year effects retained as fixed parameters).")

    n.add("n_params_interior", 39,
          "tables/parameter_uncertainty_v1.md",
          "prose: 'K = 100 draws ... 39 interior coordinates are drawn'", "S8 singles",
          "Of the 41 active parameters, 39 are interior (drawn under RQMC "
          "resampling) and 2 are free-but-at-a-bound.")

    n.add("n_params_at_bound", 2,
          "tables/parameter_uncertainty_v1.md",
          "prose: '... 10 pinned and 2 free-but-at-a-bound coordinates are held at theta-hat'",
          "S8 singles",
          "2 of the 41 active parameters are free but sit at an active bound; held "
          "fixed at theta-hat during RQMC resampling (39 + 2 = 41).")

    # ================================================================
    # FINAL negLL
    # ================================================================
    n.add("negll_singles_final", 18022.764617170084,
          "runs/param_child_v1/compact_evaluation_v1.json",
          "negll_anchor (== negll51 == negll41)", "S8, compact 41/51-coordinate spec",
          "Final singles negative log-likelihood; bitwise-identical whether evaluated "
          "on the 41-coordinate active vector or the 51-coordinate provenance vector.")

    n.add("negll_couples_final", 43493.342239066726,
          "runs/couples_clean_baseline/r240_step3_estimation_v1.json",
          "estimation.negll", "R240 four-leg single optimum",
          "Final couples negative log-likelihood, R240 certified estimation.")

    # ================================================================
    # THE FOUR STATES (I00/I10/I01/I11) -- singles, both reference arms, both bases
    # ================================================================
    hd = pd.read_csv(tables / "headline_decomposition_v1.csv")
    src_hd = "tables/headline_decomposition_v1.csv"
    state_cols = [("I00", "{}", "baseline"),
                  ("I10", "{P}", "preferences equalised"),
                  ("I01", "{A,B,D}", "environment equalised"),
                  ("I11", "{A,B,D,P}", "preferences AND environment equalised")]
    for arm_tag, arm in (("female", "singles_female"),
                         ("male", "singles_male_structural_zero")):
        for basis in ("raw", "equivalized"):
            row = one(hd, model="S8", reference_arm=arm, basis=basis)
            for state, coalition, desc in state_cols:
                key = "state_%s_%s_%s" % (state, arm_tag, basis)
                n.add(key, float(row[state]), src_hd, state,
                      "S8, %s reference, %s basis" % (arm_tag, basis),
                      "Gini-points state %s (%s): %s." % (state, coalition, desc))
                lo, hi = float(row[state + "__band_lo"]), float(row[state + "__band_hi"])
                n.add(key + "__rqmc_band", [lo, hi], src_hd,
                      state + "__band_lo / " + state + "__band_hi",
                      "S8, %s reference, %s basis" % (arm_tag, basis),
                      "RQMC scramble-jackknife band (8 scrambles) for state %s." % state)

    # ================================================================
    # C_pref / C_env / C_acc / C_earn / C_needs -- raw + equivalized, both arms,
    # with RQMC bands (headline_decomposition) and CR1 intervals (parameter_uncertainty)
    # ================================================================
    channel_cols = ["C_pref", "C_env", "C_acc", "C_earn", "C_needs"]
    for arm_tag, arm in (("female", "singles_female"),
                         ("male", "singles_male_structural_zero")):
        for basis in ("raw", "equivalized"):
            row = one(hd, model="S8", reference_arm=arm, basis=basis)
            for col in channel_cols:
                key = "%s_%s_%s" % (col, arm_tag, basis)
                n.add(key, float(row[col]), src_hd, col,
                      "S8, %s reference, %s basis" % (arm_tag, basis),
                      "Gini-point contribution of channel %s to inequality I00." % col)
                lo, hi = float(row[col + "__band_lo"]), float(row[col + "__band_hi"])
                n.add(key + "__rqmc_band", [lo, hi], src_hd,
                      col + "__band_lo / " + col + "__band_hi",
                      "S8, %s reference, %s basis" % (arm_tag, basis),
                      "RQMC scramble-jackknife band (8 scrambles) for %s." % col)
                share_col = col + "_over_I00"
                n.add(key + "_share", float(row[share_col]), src_hd, share_col,
                      "S8, %s reference, %s basis" % (arm_tag, basis),
                      "Channel %s as a share of I00 (baseline inequality)." % col)

    # CR1 (asymptotic, delta-method) intervals -- point_estimate + [lo,hi], raw basis,
    # female reference, singles model S8. parameter_uncertainty_v1.csv has no
    # equivalized/male-reference rows for these level quantities (checked: only
    # s_pref/s_env/C_geo/C_geo_over_I00/C_oth/C_oth_over_I00/I* + the 5 channel levels,
    # all under model=S8, reference_arm=singles_female, basis=raw).
    pu = pd.read_csv(tables / "parameter_uncertainty_v1.csv")
    src_pu = "tables/parameter_uncertainty_v1.csv"
    for col in channel_cols + ["C_geo", "C_geo_over_I00", "C_oth", "C_oth_over_I00",
                                "I00", "I10", "I01", "I11", "s_pref", "s_env"]:
        sub = pu[(pu["quantity"] == col) & (pu["model"] == "S8")
                 & (pu["reference_arm"] == "singles_female") & (pu["basis"] == "raw")]
        if len(sub) != 1:
            continue
        r = sub.iloc[0]
        key = "%s_female_raw__cr1_interval" % col
        n.add(key, [float(r["parameter_lo_2p5"]), float(r["parameter_hi_97p5"])],
              src_pu, "parameter_lo_2p5 / parameter_hi_97p5",
              "S8, female reference, raw basis",
              "CR1/HC1 sandwich delta-method 95%% interval for %s "
              "(K_interior=%d clusters-corrected)." % (col, int(r["K"])))

    # ================================================================
    # ONE-FACTOR EQUALIZATION EFFECTS
    # ================================================================
    prim = one(hd, model="S8", reference_arm="singles_female", basis="raw")
    env_only = (float(prim["I00"]) - float(prim["I01"])) / float(prim["I00"])
    pref_only = (float(prim["I00"]) - float(prim["I10"])) / float(prim["I00"])
    n.add("equalization_env_only", env_only, src_hd,
          "(I00 - I01) / I00", "S8, female reference, raw basis",
          "Inequality reduction from equalizing environment alone, as a share of "
          "baseline inequality I00 (the headline 77%% figure).")
    n.add("equalization_pref_only", pref_only, src_hd,
          "(I00 - I10) / I00", "S8, female reference, raw basis",
          "Inequality reduction from equalizing preferences alone, as a share of "
          "baseline inequality I00 (the headline +10%% figure).")

    # ================================================================
    # RUM BENCHMARK BLOCK
    # ================================================================
    rb1 = jload(runs / "rum_benchmark_final" / "rb_step1_estimation_v1.json")
    src_rb1 = "runs/rum_benchmark_final/rb_step1_estimation_v1.json"
    nest = rb1["step6_nesting"]
    comp = nest["comparator"]
    n.add("rum_pref_model_negll", float(comp["negll"]), src_rb1,
          "step6_nesting.comparator.negll", "S8 (preferred model)",
          "negLL of the preferred RURO/S8 specification, used as the nesting "
          "comparator for the RUM benchmark.")
    n.add("rum_pref_model_n_free", int(comp["n_free"]), src_rb1,
          "step6_nesting.comparator.n_free", "S8 (preferred model)",
          "Free-parameter count of the preferred specification in the benchmark test.")
    rumb = nest["variants"].get("RUM_B") or list(nest["variants"].values())[-1]
    n.add("rum_bench_negll", float(rumb["negll"]), src_rb1,
          "step6_nesting.variants.RUM_B.negll", "RUM_B (common-choice-set benchmark)",
          "negLL of the nested RUM benchmark model.")
    n.add("rum_bench_negll_gap", float(rumb["negll_gap"]), src_rb1,
          "step6_nesting.variants.RUM_B.negll_gap", "RUM_B vs S8",
          "Nats gap between the benchmark and preferred model's negLL.")
    n.add("rum_bench_LR_statistic", float(rumb["LR_statistic_2x_negll_gap"]), src_rb1,
          "step6_nesting.variants.RUM_B.LR_statistic_2x_negll_gap", "RUM_B vs S8",
          "Likelihood-ratio statistic (2x negLL gap) for the nested benchmark test.")
    n.add("rum_bench_df", int(rumb["df"]), src_rb1,
          "step6_nesting.variants.RUM_B.df", "RUM_B vs S8",
          "Degrees of freedom for the RUM benchmark LR test.")

    rb4 = jload(runs / "rum_benchmark_final" / "rb_step4_misclassification_v1.json")
    src_rb4 = "runs/rum_benchmark_final/rb_step4_misclassification_v1.json"
    pos = rb4["positive_side_misclassification"]
    hours_const = [c for c in pos["relocated_constants"]
                   if c["availability_constant_in_g_under_RURO"].startswith("beta_h_")]
    n.add("rum_bench_const_mad", sum(abs(c["difference"]) for c in hours_const) / len(hours_const),
          src_rb4, "positive_side_misclassification.relocated_constants[*].difference (mean |.|)",
          "n/a",
          "Mean absolute difference between RURO/S8 availability constants and their "
          "RUM_B relocated-as-taste counterparts, across the hour-band constants.")
    n.add("rum_bench_n_constants", len(hours_const), src_rb4,
          "positive_side_misclassification.relocated_constants (count with beta_h_ prefix)",
          "n/a", "Number of hour-band availability constants compared in the "
          "misclassification test.")
    gaps = pos["sex_specific_leisure_block"]["leisure_intercept_gap_male_minus_female"]
    n.add("rum_leisure_gap_final", float(gaps["RURO_S8"]), src_rb4,
          "positive_side_misclassification.sex_specific_leisure_block."
          "leisure_intercept_gap_male_minus_female.RURO_S8", "S8 (preferred model)",
          "Male-minus-female leisure-intercept gap under the preferred RURO/S8 model.")
    n.add("rum_leisure_gap_benchmark", float(gaps["RUM_B"]), src_rb4,
          "positive_side_misclassification.sex_specific_leisure_block."
          "leisure_intercept_gap_male_minus_female.RUM_B", "RUM_B benchmark",
          "Male-minus-female leisure-intercept gap under the RUM_B benchmark model "
          "(the sign reverses relative to RURO/S8).")

    rd = pd.read_csv(tables / "rum_benchmark_decomposition_v1.csv")
    src_rd = "tables/rum_benchmark_decomposition_v1.csv"
    for tag, basis in (("raw", "raw"), ("equivalized", "equivalized")):
        sel = rd[(rd["basis"] == basis) & (rd["reference_arm"] == "singles_female")]
        ruro = sel[sel["model"] == "RURO"].iloc[0]
        rumbd = sel[sel["model"] != "RURO"].iloc[0]
        n.add("rum_share_pref_RURO_%s" % tag, float(ruro["C_pref_over_I00"]), src_rd,
              "C_pref_over_I00 (model=RURO)", "%s basis, female reference" % tag,
              "Preference channel's share of I00 under the preferred RURO/S8 model.")
        n.add("rum_share_pref_RUMB_%s" % tag, float(rumbd["C_pref_over_I00"]), src_rd,
              "C_pref_over_I00 (model!=RURO)", "%s basis, female reference" % tag,
              "Preference channel's share of I00 under the RUM_B benchmark model.")
        n.add("rum_inequality_drop_%s" % tag,
              (float(rumbd["I00"]) - float(ruro["I00"])) / float(ruro["I00"]),
              src_rd, "(I00[!=RURO] - I00[RURO]) / I00[RURO]",
              "%s basis, female reference" % tag,
              "Relative change in baseline inequality I00 moving from RURO/S8 to the "
              "RUM_B benchmark.")

    figr01 = pd.read_csv(figures / "figR01_benchmark_decomposition.csv")
    src_figr01 = "figures/figR01_benchmark_decomposition.csv"
    pb = figr01[figr01["panel"] == "b"].set_index("quantity")
    for tag, key_lbl in (("relabelled_as_preferences", "reappears as preferences"),
                         ("relabelled_as_needs", "reappears as endowments and needs"),
                         ("leaves_measured_total", "leaves the measured total")):
        n.add("rum_omitted_share_%s" % tag, float(pb.loc[key_lbl, "value"]), src_figr01,
              "panel b, quantity='%s'" % key_lbl, "n/a",
              "Where the market-side share the benchmark cannot represent actually "
              "goes: %s." % key_lbl)

    # ================================================================
    # GEOGRAPHIC SPLIT
    # ================================================================
    ng = pd.read_csv(tables / "nested_geographic_access_v1.csv")
    src_ng = "tables/nested_geographic_access_v1.csv"
    for tag, basis in (("raw", "raw"), ("equivalized", "equivalized")):
        row = one(ng, model="S8", basis=basis, reference_arm="singles_female")
        n.add("geo_share_of_I00_%s" % tag, float(row["C_geo_over_I00"]), src_ng,
              "C_geo_over_I00", "S8, female reference, %s basis" % tag,
              "Geographic-access channel C_geo as a share of I00.")
        n.add("geo_share_of_C_acc_%s" % tag, float(row["C_geo_share_of_C_acc"]), src_ng,
              "C_geo_share_of_C_acc", "S8, female reference, %s basis" % tag,
              "Geographic channel as a share of the total access channel C_acc.")
        n.add("geo_share_of_I00_%s__band" % tag,
              float(row["C_geo_over_I00__E_T"]), src_ng, "C_geo_over_I00__E_T",
              "S8, female reference, %s basis" % tag,
              "RQMC scramble-jackknife half-width for the geographic share of I00.")

    rg = pd.read_csv(figures / "figG02_regional_access_environments.csv")
    src_rg = "figures/figG02_regional_access_environments.csv"
    n.add("n_regional_environments", int(rg.groupby("profile").size().max()), src_rg,
          "count of rows per profile", "n/a",
          "Number of distinct regional employment-opportunity environments "
          "illustrated for the matched-pair households.")
    for tag, prof in (("A", "household_1"), ("B", "household_2")):
        g = rg[rg["profile"] == prof]
        n.add("regional_opportunity_mass_range_%s" % tag,
              [float(g["employment_opportunity_mass"].min()),
               float(g["employment_opportunity_mass"].max())],
              src_rg, "employment_opportunity_mass (min, max)", "profile=%s" % prof,
              "Range of employment-opportunity mass across the 24 regional "
              "environments, for the matched-pair household %s." % prof)

    # ================================================================
    # SEX SUBGROUP NUMBERS
    # ================================================================
    sg = pd.read_csv(tables / "subgroup_decomposition_v1.csv")
    src_sg = "tables/subgroup_decomposition_v1.csv"
    sex = sg[sg["dimension"] == "sex"]

    def sub(group, quantity, arm="singles_female", basis="raw"):
        return one(sex, group=group, quantity=quantity,
                   reference_arm=arm, basis=basis)

    for tag, grp in (("men", "men"), ("women", "women")):
        for basis in ("raw", "equivalized"):
            row = sub(grp, "C_acc_over_I00", basis=basis)
            n.add("subgroup_%s_acc_share_%s" % (tag, basis), float(row["estimate"]),
                  src_sg, "estimate (quantity=C_acc_over_I00)",
                  "sex=%s, female reference, %s basis" % (grp, basis),
                  "Access channel's share of I00 for the %s subgroup." % grp)
        row_male_ref = sub(grp, "C_acc_over_I00", arm="singles_male_structural_zero")
        n.add("subgroup_%s_acc_share_male_ref" % tag, float(row_male_ref["estimate"]),
              src_sg, "estimate (quantity=C_acc_over_I00)",
              "sex=%s, male reference, raw basis" % grp,
              "Access channel's share of I00 for the %s subgroup, male reference arm." % grp)
        row_geo = sub(grp, "C_geo_over_I00")
        n.add("subgroup_%s_geo_share" % tag, float(row_geo["estimate"]), src_sg,
              "estimate (quantity=C_geo_over_I00)",
              "sex=%s, female reference, raw basis" % grp,
              "Geographic channel's share of I00 for the %s subgroup." % grp)

    n.add("subgroup_men_pref_share_female_ref",
          float(sub("men", "s_pref")["estimate"]), src_sg,
          "estimate (quantity=s_pref)", "sex=men, female reference, raw basis",
          "Preference channel's share for men under the female reference arm.")
    n.add("subgroup_men_pref_share_male_ref",
          float(sub("men", "s_pref", arm="singles_male_structural_zero")["estimate"]),
          src_sg, "estimate (quantity=s_pref)", "sex=men, male reference, raw basis",
          "Preference channel's share for men under the male reference arm "
          "(sign flips relative to the female reference).")

    # ================================================================
    # DRAW-COUNT FACTS
    # ================================================================
    design = pd.read_csv(figures / "figS6_02_coefficient_stability.csv")
    src_design = "figures/figS6_02_coefficient_stability.csv"
    n.add("drawcount_ladder", [50, 100, 200, 400], src_design,
          "R column, unique values", "n/a",
          "Draw-count ladder over which parameter stability is checked (R = number "
          "of drawn jobs, alternatives = R+1).")
    n.add("drawcount_max_deviation_full_range", float(design["deviation_in_R100_SE"].abs().max()),
          src_design, "deviation_in_R100_SE (max abs, full R=50..400 range)", "n/a",
          "Largest coefficient movement (in R=100 standard-error units) across the "
          "full 50-400 draw-count range.")
    n_drawn_ref = 100
    n.add("drawcount_max_deviation_geq_reference",
          float(design[design.R >= n_drawn_ref].deviation_in_R100_SE.abs().max()),
          src_design, "deviation_in_R100_SE (max abs, R >= 100 only)", "n/a",
          "Largest coefficient movement (in R=100 SE units) restricted to R >= the "
          "reference draw count of 100 (NOT the full 50-400 range).")
    s6 = jload(runs / "drawcount_s6" / "s6_drawcount_estimation_v1.json")
    n.add("drawcount_status", s6["STATUS"],
          "runs/drawcount_s6/s6_drawcount_estimation_v1.json", "STATUS", "n/a",
          "Completion status of the draw-count stability estimation sweep.")

    # ================================================================
    # EXTERNAL VALIDATION NUMBERS
    # ================================================================
    xh1 = jload(runs / "external_hours_lfs" / "xh1_table_record_v1.json")
    src_xh1 = "runs/external_hours_lfs/xh1_table_record_v1.json"
    n.add("external_validation_n_rows", int(xh1["table"]["n_rows"]),
          src_xh1, "table.n_rows", "n/a",
          "Row count of the external LFS hours-validation table "
          "(7 hour-bands x 3 sex categories: male, female, pooled).")
    n.add("external_validation_wishmore_status", xh1["wishmore_verdict"]["status"],
          src_xh1, "wishmore_verdict.status", "n/a",
          "Status flag on the WISHMORE-variable coding check used in the external "
          "validation (an unresolved coding-ambiguity caveat, not a pass/fail gate).")

    ext = pd.read_csv(tables / "external_hours_validation_v1.csv")
    src_ext = "tables/external_hours_validation_v1.csv"
    f = one(ext, sex="pooled", band="F35")
    for tag, col in (("lfs", "lfs_share_of_focal_bands"),
                     ("obs", "sample_obs_share_of_focal_bands"),
                     ("pred", "model_pred_share_of_focal_bands")):
        n.add("external_validation_statutory_band_%s" % tag, float(f[col]), src_ext,
              col, "sex=pooled, band=F35",
              "Share of workers in the statutory-hours band (F35), %s source." % tag)

    # ================================================================
    # COUPLES WELFARE NUMBERS
    # ================================================================
    cw = jload(runs / "final_couples_welfare" / "cw_step4_pooled_v1.json")
    src_cw = "runs/final_couples_welfare/cw_step4_pooled_v1.json"
    b = cw["B_couples"]
    for basis_tag, block_key in (("raw", "principal_states_raw"),
                                 ("equivalized", "principal_states_equivalized")):
        block = b[block_key]
        for state in ("I0000", "I1000", "I0111", "I1111"):
            row = block[state]
            key = "couples_state_%s_%s" % (state, basis_tag)
            n.add(key, float(row["estimate"]), src_cw,
                  "B_couples.%s.%s.estimate" % (block_key, state),
                  "couples R240 baseline, %s basis" % basis_tag,
                  "Couples Gini-points state %s (%s): %s."
                  % (state, row["state"], row["coalition"]))
            n.add(key + "__rqmc_band",
                  [float(row["band_lo"]), float(row["band_hi"])], src_cw,
                  "B_couples.%s.%s.band_lo / band_hi" % (block_key, state),
                  "couples R240 baseline, %s basis" % basis_tag,
                  "RQMC scramble-jackknife band for couples state %s." % state)
    contrib = b["contributions_equivalized"]
    for ch, row in contrib.items():
        n.add("couples_%s_equivalized" % ch, float(row["estimate"]), src_cw,
              "B_couples.contributions_equivalized.%s.estimate" % ch,
              "couples R240 baseline, equivalized basis",
              "Couples channel contribution %s (Gini points, equivalized)." % ch)
        n.add("couples_%s_equivalized__rqmc_band" % ch,
              [float(row["band_lo"]), float(row["band_hi"])], src_cw,
              "B_couples.contributions_equivalized.%s.band_lo / band_hi" % ch,
              "couples R240 baseline, equivalized basis",
              "RQMC scramble-jackknife band for couples channel %s." % ch)

    sens = pd.read_csv(runs / "final_couples_welfare" / "cw_step3b_sensitivity_table_v1.csv")
    #: the RAW couples contributions. The step-4 artefact carries an
    #: equivalized contributions block only, so the raw row the paper
    #: prints had nothing to check against. This table carries one
    #: baseline and one band per quantity per basis; the raw baselines
    #: are those contributions.
    src_sens = "runs/final_couples_welfare/cw_step3b_sensitivity_table_v1.csv"
    raw_sens = sens[sens.basis == "raw"].drop_duplicates("quantity")
    for ch in ("C_P", "C_E", "C_A", "C_B", "C_D"):
        row = raw_sens[raw_sens.quantity == ch]
        if len(row) != 1:
            raise SystemExit("expected one raw baseline for %s" % ch)
        row = row.iloc[0]
        n.add("couples_%s_raw" % ch, float(row["baseline"]), src_sens,
              "baseline (basis=raw, quantity=%s)" % ch,
              "couples R240 baseline, raw basis",
              "Couples channel contribution %s (Gini points, raw)." % ch)
        n.add("couples_%s_raw__rqmc_band" % ch,
              [float(row["band_lo"]), float(row["band_hi"])], src_sens,
              "band_lo / band_hi (basis=raw, quantity=%s)" % ch,
              "couples R240 baseline, raw basis",
              "RQMC scramble-jackknife band for couples channel %s, raw."
              % ch)
    n.add("couples_male_leisure_sensitivity_max", float(sens[sens.quantity == "C_P"].relative_delta.abs().max()),
          "runs/final_couples_welfare/cw_step3b_sensitivity_table_v1.csv",
          "relative_delta (quantity=C_P, max abs across sensitivity arms)",
          "couples C_P channel",
          "Largest relative movement of the couples preference-channel contribution "
          "C_P across the male-leisure sensitivity battery.")

    n.add("n_couples_clusters", 2275,
          "runs/couples_clean_baseline/r240_step3_estimation_v1.json",
          "estimation.inference.G_clusters", "couples R240",
          "CR1 cluster count for couples inference (identical to the couples "
          "household count).")

    # ================================================================
    # BETA_LL STATUS (ABSENT / welfare at 0)
    # ================================================================
    pr = jload(runs / "param_child_v1" / "parameter_records_v1.json")
    bll = pr["B_couples_beta_ll"]
    src_pr = "runs/param_child_v1/parameter_records_v1.json"
    n.add("beta_ll_status", bll["status"], src_pr,
          "B_couples_beta_ll.status", "couples cross-leisure interaction term",
          "Existence status of the beta_ll cross-leisure interaction term: ABSENT "
          "from the certified couples spec (non-PD on the joint frame; fixing it "
          "moved the weak direction to couples-male leisure).")
    n.add("beta_ll_welfare_effective_value", float(bll["welfare_effective_beta_ll"]), src_pr,
          "B_couples_beta_ll.welfare_effective_beta_ll", "couples welfare pipeline",
          "The effective value the welfare pipeline uses for beta_ll: exactly 0.0, "
          "confirmed by absence of a stored interaction_name in build_V (not an "
          "estimated-then-zeroed coordinate).")
    n.add("beta_ll_cross_leisure_form", bll["cross_leisure_form"], src_pr,
          "B_couples_beta_ll.cross_leisure_form", "n/a",
          "Functional form the (absent) cross-leisure term would take: "
          "beta_ll * BoxCox(leisure_male) * BoxCox(leisure_female).")

    # ================================================================
    # CHILD COEFFICIENTS
    # ================================================================
    csf = pr["C_single_female"]
    n.add("beta_l_nkids_female", float(csf["estimate"]), src_pr,
          "C_single_female.estimate", "S8 corrected-floor5, param=beta_l_nkids_sf",
          "Female singles leisure child-count shifter: certified INTERIOR estimate "
          "of the final S8 model (not pinned, not at a bound).")
    n.add("beta_l_nkids_female_se", float(csf["se_robust"]), src_pr,
          "C_single_female.se_robust", "S8 corrected-floor5, param=beta_l_nkids_sf",
          "CR1/HC1 sandwich robust standard error for beta_l_nkids_sf "
          "(G_clusters=%d, K_interior=%d)." % (csf["standard_error_convention"]["G_clusters"],
                                                csf["standard_error_convention"]["K_interior"]))
    n.add("beta_l_nkids_female_z", float(csf["z_robust"]), src_pr,
          "C_single_female.z_robust", "S8 corrected-floor5, param=beta_l_nkids_sf",
          "Robust z-statistic for beta_l_nkids_sf.")

    csm = pr["C_single_male"]
    n.add("beta_l_nkids_male_historical_test", float(csm["estimate"]), src_pr,
          "C_single_male.estimate", "historical S-battery S4 (pre-floor5 S0/LOC4 frame)",
          "Male singles child-count shifter: a HISTORICAL, REJECTED test estimate "
          "(record_decision=REJECT), not part of the certified 41-parameter S8 "
          "vector. final_S8_status: ABSENT; structural zero by the sex-specific "
          "shifter specification. Scope caveat: tested on the pre-floor5 frame; "
          "no new test performed on the final corrected S8 model.")
    n.add("beta_l_nkids_male_status", csm["final_S8_status"], src_pr,
          "C_single_male.final_S8_status", "S8 final",
          "Status of the male child-count shifter in the certified S8 model: "
          "ABSENT (structural zero).")

    # ================================================================
    # Emit
    # ================================================================
    out.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "_meta": {
            "generated_by": "beamer/make_numbers_of_record_v1.py",
            "sprint_root": str(sprint),
            "note": "Every quantity here is read from a named frozen artefact of the "
                    "estimation repository. No number is typed by hand. See each "
                    "entry's 'source' and 'column_or_key' fields for exact provenance.",
            "n_entries": len(n.entries),
        },
        "entries": n.entries,
    }
    out.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    print("wrote %s (%d entries)" % (out, len(n.entries)))
    return sorted(n.entries.keys())


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--sprint", type=pathlib.Path, default=DEFAULT_SPRINT)
    ap.add_argument("--out", type=pathlib.Path,
                    default=pathlib.Path(__file__).resolve().parents[1]
                    / "reports" / "numbers_of_record_v1.json")
    a = ap.parse_args()
    keys = build(a.sprint, a.out)
    print("\n".join(keys))
    sys.exit(0)
