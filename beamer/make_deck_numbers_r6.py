#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generate every numeral the R6 seminar deck is allowed to state.

R6 (JMP_W1_fork_ruling_v1.md Appendix A) and the BASELINE-F-1 ruling
(JMP_W1_BASELINE_F1_authorization_and_Cobs_ruling_v1.md) bound what may be
shown.  This script reads ONLY the three authorized sources:

  S11  MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/
       s11_{singles,couples}_parameter_table_v1.csv  -- model of record
  FIT  MNL_posfit/outputs/positive_fit_diagnostics_v3/  -- observed fit,
       simulated bands and G2 gate (MNL_posfit commit 96693269)
  W1F  MNL/outputs/welfare/baseline_f1_v1/                             -- E1 baseline
  D2   MNL_decomp/outputs/welfare/preseminar_pab_v1/                   -- DECOMP-2

and writes deck_numbers_r6.tex plus build/r6_number_provenance.json.

It refuses to emit a fit statistic whose G2 label is not ADEQUATE, and it
refuses to emit any W1-EA quantity: no source here contains one.
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]                       # C:\Users\hisham\Repo
MNL = REPO / "MNL"
# FINAL-GATE-1 accepts POSFIT v3 as the sole positive-fit package.  In
# particular, displayed accuracy is the parsed *observed* statistic from
# hard_classification_metrics.csv; node_bootstrap_mean is a numerical-
# integration diagnostic and must never be relabelled as observed accuracy.
POSFIT = REPO / "MNL_posfit" / "outputs" / "positive_fit_diagnostics_v3"
POSFIT_COMMIT = "96693269"
S11 = MNL / "experiments" / "JMP_SEMINAR_SPRINT" / "runs" / "s11_welfare_specs_of_record"
W1F = MNL / "outputs" / "welfare" / "baseline_f1_v1"
W1FEQ = MNL / "outputs" / "welfare" / "baseline_f1_equivalised_v1"
DECOMP2 = REPO / "MNL_decomp" / "outputs" / "welfare" / "preseminar_pab_v1"
DECK_SRC = HERE / "JMP_seminar_deck_r6.tex"

OUT_TEX = HERE / "deck_numbers_r6.tex"
OUT_JSON = HERE / "build" / "r6_number_provenance.json"

# Fit statistics the deck may state.  R6 build brief: extensive accuracy only,
# and only where the G2 quadrature gate labels it ADEQUATE.
ALLOWED_FIT_STATISTIC = "extensive_accuracy"
EXPECTED_ADEQUATE_GROUPS = {"couples_female", "couples_male", "singles_female"}
EXPECTED_LIMITED_GROUPS = {"singles_male"}

# --------------------------------------------------------------------------
# Equivalence-scale authority (DECK-3).  The scale is RATIFIED; the guard no
# longer keys on the artifact's provisional label.  It asserts instead that
# (i) the ratifying ruling is recorded here verbatim, (ii) the deck source
# cites it and the scale-review memo by name, and (iii) the artifacts use the
# scale the ruling ratifies.  The artifact status string is accepted whether
# it still reads provisional (the committed JSONs predate the ruling) or has
# been relabelled as ratified.
# --------------------------------------------------------------------------
SCALE_RULING_ID = 'Deputy ruling "SCALE CLOSED; CHILD-SHIFTER FRAMING", s1'
SCALE_RULING_CITE = "SCALE CLOSED; CHILD-SHIFTER FRAMING"
SCALE_RULING_QUOTE = (
    "Modified-OECD is ratified as the primary equivalence scale for current "
    "JMP distributional reporting. The provisional economics-review status "
    "is closed.")
SCALE_MEMO = "JMP_SCALE_REVIEW_1_equivalence_scale_economics_v1.md"
RATIFIED_SCALE_NAME = "modified_OECD"
ACCEPTED_SCALE_STATUSES = {"PROVISIONAL_PENDING_ECONOMICS_REVIEW",
                           "RATIFIED", "RATIFIED_PRIMARY"}


def check_scale_status(statuses: set[str], names: set[str]) -> None:
    """Refuse unless every artifact uses the ratified scale under an accepted
    status label (provisional pre-ruling label, or a ratified label)."""
    if not SCALE_RULING_QUOTE.startswith("Modified-OECD is ratified"):
        raise SystemExit("REFUSED: scale ruling quote missing or altered")
    if names != {RATIFIED_SCALE_NAME}:
        raise SystemExit(
            "REFUSED: equivalised artifacts use scale %s; %s ratifies only %s"
            % (sorted(names), SCALE_RULING_ID, RATIFIED_SCALE_NAME))
    bad = {s for s in statuses
           if s not in ACCEPTED_SCALE_STATUSES and not s.startswith("RATIFIED")}
    if bad or not statuses:
        raise SystemExit(
            "REFUSED: unrecognised equivalence-scale status %s (accepted: %s "
            "or any RATIFIED* label)" % (sorted(bad), sorted(ACCEPTED_SCALE_STATUSES)))


def check_scale_citation(src: str) -> None:
    """Refuse unless the source-only provenance block carries both citations."""
    match = re.search(
        r"% BEGIN READER-VOICE PROVENANCE(.*?)% END READER-VOICE PROVENANCE",
        src,
        re.S,
    )
    if match is None:
        raise SystemExit("REFUSED: reader-voice provenance block is missing")
    flat = re.sub(r"\s+", " ", match.group(1).replace("\\_", "_"))
    missing = [s for s in (SCALE_RULING_CITE, SCALE_MEMO) if s not in flat]
    if missing:
        raise SystemExit(
            "REFUSED: deck provenance does not cite %s (missing: %s); the "
            "equivalised numbers may not be emitted without the ratifying "
            "source record" % (SCALE_RULING_ID, missing))


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def rows(p: Path) -> list[dict]:
    with p.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


# --------------------------------------------------------------------------
# number formatting: the deck's display precision, fixed here, never on a slide
# --------------------------------------------------------------------------
def eur(x: float) -> str:
    """Household EUR/month, unequivalised: nearest euro, thin-space thousands."""
    return "{:,}".format(int(round(x))).replace(",", r"\,")


def gini(x: float) -> str:
    return "%.3f" % x


def gini6(x: float) -> str:
    """Six decimals: the precision the E3-EQ equivalised memo reports the
    headline equivalised Ginis at (docs/results/
    JMP_BASELINE_F1_equivalised_reporting_v1.md, commit 4c4e07e)."""
    return "%.6f" % x


def pct1(x: float) -> str:
    return "%.1f" % (100.0 * x)


def num(x: float, d: int) -> str:
    return ("%." + str(d) + "f") % x


def count(n: int) -> str:
    return "{:,}".format(int(n)).replace(",", r"\,")


def main() -> int:
    prov: dict = {"sources": {}, "macros": {}, "refusals": []}
    tex: list[str] = [
        "% deck_numbers_r6.tex -- GENERATED by make_deck_numbers_r6.py.",
        "% Do not edit by hand.  Every numeral on an R6 slide comes from here.",
        "% Sources: S11 parameter tables (model of record);",
        "%          positive_fit_diagnostics_v3, MNL_posfit 96693269 (observed values; G2-ADEQUATE only);",
        "%          welfare/baseline_f1_v1 (BASELINE-F-1, commit 6048c9f, verified b5550af).",
        "%          preseminar_pab_v1 (DECOMP-2, MNL_decomp b52761b4).",
        "% Vintage status: every positive-fit macro is POSFIT v3 (96693269).",
        "%          FitExt* binds to hard_classification_metrics.csv observed values;",
        "%          FitExtRatio* binds separately to the G2 numerical-adequacy ratios.",
        "",
    ]

    def mac(name: str, value: str, source: str, raw=None) -> None:
        tex.append(r"\newcommand{\%s}{%s}" % (name, value))
        prov["macros"][name] = {"rendered": value, "source": source, "raw": raw}

    # ---------------------------------------------------------------- W1-F
    agg_path = W1F / "baseline_f1_full_sample_aggregates_v1.json"
    agg = json.loads(agg_path.read_text(encoding="utf-8"))
    prov["sources"]["baseline_f1_full_sample_aggregates_v1.json"] = {
        "path": str(agg_path), "sha256": sha256(agg_path),
        "executed_commit": agg["executed_commit"],
        "recorded_commit": "6048c9f7", "verified_commit": "b5550af5",
        "units": agg["units"], "weight": agg["weight"], "pooled_row": agg["pooled_row"],
        "C_obs_benchmark": agg["C_obs_benchmark"],
    }
    if agg["pooled_row"]:
        raise SystemExit("REFUSED: aggregates carry a pooled row; R6 forbids a pooled figure")
    if agg["C_obs_benchmark"] != "NOT PRODUCED":
        prov["refusals"].append(
            "C_obs benchmark present in source but E3 is not authorised; not emitted")

    tex.append("% --- BASELINE-F-1 (E1): household EUR/month, unequivalised, dwt-weighted ---")
    for grp, tag in (("singles", "Sing"), ("couples", "Coup")):
        s = agg["samples"][grp]
        src = "baseline_f1_full_sample_aggregates_v1.json samples.%s" % grp
        mac("WF" + tag + "N", count(s["unweighted_n"]), src, s["unweighted_n"])
        mac("WF" + tag + "Mean", eur(s["dwt_weighted_mean"]), src, s["dwt_weighted_mean"])
        mac("WF" + tag + "Median", eur(s["dwt_weighted_median"]), src, s["dwt_weighted_median"])
        mac("WF" + tag + "Gini", gini(s["dwt_weighted_gini"]), src, s["dwt_weighted_gini"])
        mac("WF" + tag + "Workers", count(s["worker_count"]), src, s["worker_count"])
        mac("WF" + tag + "Nonworkers", count(s["nonworker_count"]), src, s["nonworker_count"])
        c = agg["checks"][grp]
        mac("WF" + tag + "Cone", "%g" % c["C1"]["max_abs_W_minus_C_obs"],
            src.replace("samples", "checks") + " C1", c["C1"]["max_abs_W_minus_C_obs"])
        mac("WF" + tag + "Ctwo", count(c["C2"]["invalid_ratio_count"]),
            src.replace("samples", "checks") + " C2", c["C2"]["invalid_ratio_count"])
        mac("WF" + tag + "Cfive", "%.1e" % c["C5"]["max_abs_utility_difference"],
            src.replace("samples", "checks") + " C5",
            c["C5"]["max_abs_utility_difference"])
    tex.append("")

    # ------------------------------------------------------------- DECOMP-2
    # The final economics/claim review authorises only the bounded headline
    # range and the variance-language range on the deck.  Both are derived
    # from the executed coalition/variance files, never typed into the slide.
    d2_pcts = []
    for sample in ("singles", "couples"):
        p = DECOMP2 / ("coalition_values_%s.csv" % sample)
        rr = rows(p)
        prov["sources"][p.name] = {"path": str(p), "sha256": sha256(p)}
        for scale in ("unequivalised", "equivalised"):
            base = next(float(r["I_S_gini"]) for r in rr
                        if r["scale"] == scale and r["coalition"] == "EMPTY")
            equal = next(float(r["I_S_gini"]) for r in rr
                         if r["scale"] == scale and r["coalition"] == "PAB")
            d2_pcts.append(100.0 * (base - equal) / base)
    var_path = DECOMP2 / "log_variance_split_v1.csv"
    var_rows = rows(var_path)
    prov["sources"][var_path.name] = {
        "path": str(var_path), "sha256": sha256(var_path)}
    var_pcts = [100.0 * float(r["share_var_log_C"]) for r in var_rows]
    mac("DTwoMinPct", num(min(d2_pcts), 1),
        "coalition_values_{singles,couples}.csv minimum Delta-I share of baseline",
        min(d2_pcts))
    mac("DTwoMaxPct", num(max(d2_pcts), 1),
        "coalition_values_{singles,couples}.csv maximum Delta-I share of baseline",
        max(d2_pcts))
    mac("DTwoVarMinPct", num(min(var_pcts), 0),
        "log_variance_split_v1.csv minimum Var(log C)/Var(log W)",
        min(var_pcts))
    mac("DTwoVarMaxPct", num(max(var_pcts), 0),
        "log_variance_split_v1.csv maximum Var(log C)/Var(log W)",
        max(var_pcts))
    tex.append("")

    # ------------------------------------------------------------ W1-F (E3-EQ)
    # Equivalised reporting is PRIMARY per the Deputy/PI ruling item B.  Pure
    # re-reporting of the already-verified BASELINE-F-1 W_F/C_obs values under
    # the modified-OECD household scale; no new welfare construction.  Source:
    # docs/results/JMP_BASELINE_F1_equivalised_reporting_v1.md (commit
    # 4c4e07e), over the verified construction (MNL 6048c9f, verified
    # b5550af).  The modified-OECD scale is RATIFIED (SCALE_RULING_ID above);
    # the committed JSONs still carry the pre-ruling provisional label, which
    # check_scale_status accepts alongside a ratified label.
    check_scale_citation(DECK_SRC.read_text(encoding="utf-8"))
    prov["scale_authority"] = {"ruling": SCALE_RULING_ID, "quote": SCALE_RULING_QUOTE,
                               "memo": SCALE_MEMO,
                               "memo_in_tree": False,
                               "ratified_scale": RATIFIED_SCALE_NAME}
    scale_status_seen: set[str] = set()
    scale_name_seen: set[str] = set()
    for grp, tag in (("singles", "Sing"), ("couples", "Coup")):
        p = W1FEQ / (grp + "_equivalised_reporting_v1.json")
        eq = json.loads(p.read_text(encoding="utf-8"))
        prov["sources"][p.name] = {
            "path": str(p), "sha256": sha256(p),
            "memo": "docs/results/JMP_BASELINE_F1_equivalised_reporting_v1.md",
            "memo_commit": "4c4e07e", "scale_status": eq["equivalised"]["scale_status"],
            "scale_name": eq["equivalised"]["scale_name"]}
        scale_status_seen.add(eq["equivalised"]["scale_status"])
        scale_name_seen.add(eq["equivalised"]["scale_name"])
        for obj, otag in (("C_eq", "CEq"), ("W_F_eq", "WEq")):
            v = eq["equivalised"][obj]
            src = "%s equivalised.%s" % (p.name, obj)
            mac("WF" + tag + otag + "Gini", gini6(v["dwt_weighted_gini"]), src,
                v["dwt_weighted_gini"])
            mac("WF" + tag + otag + "Mean", eur(v["dwt_weighted_mean"]), src,
                v["dwt_weighted_mean"])
            mac("WF" + tag + otag + "Median", eur(v["dwt_weighted_median"]), src,
                v["dwt_weighted_median"])
    check_scale_status(scale_status_seen, scale_name_seen)
    tex.append("")

    # ------------------------------------------------------------- fit / G2
    g2_path = POSFIT / "g2_adequacy.csv"
    g2 = rows(g2_path)
    prov["sources"]["g2_adequacy.csv"] = {"path": str(g2_path), "sha256": sha256(g2_path)}

    hc_path = POSFIT / "hard_classification_metrics.csv"
    hc = rows(hc_path)
    prov["sources"]["hard_classification_metrics.csv"] = {
        "path": str(hc_path), "sha256": sha256(hc_path)}

    tex.append("% --- positive fit: ONLY G2-ADEQUATE statistics (weighted, the binding rule) ---")
    tag_of = {"singles_male": "SM", "singles_female": "SF",
              "couples_male": "CM", "couples_female": "CF"}
    adequate_groups: list[str] = []
    limited_groups: list[str] = []
    for r in g2:
        if (r["weighting"] != "weighted" or r["statistic"] != ALLOWED_FIT_STATISTIC
                or r.get("scope", "all") != "all"):
            continue
        grp = r["group"]
        if r["label"] != "ADEQUATE":
            limited_groups.append(grp)
            prov["refusals"].append(
                "%s %s is %s (ratio %s); not emitted"
                % (grp, ALLOWED_FIT_STATISTIC, r["label"], r["adequacy_ratio_mcse_to_sampling_sd"]))
            continue
        adequate_groups.append(grp)
        observed_row = next(
            q for q in hc
            if q["group"] == grp and q["weighting"] == "weighted"
        )
        v = float(observed_row[ALLOWED_FIT_STATISTIC])
        mac("FitExt" + tag_of[grp], pct1(v),
            "hard_classification_metrics.csv %s/weighted/%s observed; "
            "g2_adequacy.csv label ADEQUATE" % (grp, ALLOWED_FIT_STATISTIC), v)
        mac("FitExtRatio" + tag_of[grp], num(float(r["adequacy_ratio_mcse_to_sampling_sd"]), 2),
            "g2_adequacy.csv %s/weighted/%s adequacy ratio" % (grp, ALLOWED_FIT_STATISTIC),
            float(r["adequacy_ratio_mcse_to_sampling_sd"]))
    mac("FitAdequateCount", str(len(adequate_groups)), "g2_adequacy.csv count of ADEQUATE groups")
    mac("FitLimitedCount", str(len(limited_groups)), "g2_adequacy.csv count of limited groups")
    # The fit-verdict slide names these groups by hand rather than stating a
    # bare count (DECK-NUMBERS-1: "a bare count reads as a headline even when
    # disclaimed; named groups cannot").  Refuse silently-stale prose if a
    # future v3 re-run changes which groups clear the gate.
    if set(adequate_groups) != EXPECTED_ADEQUATE_GROUPS or set(limited_groups) != EXPECTED_LIMITED_GROUPS:
        raise SystemExit(
            "REFUSED: G2-ADEQUATE group membership changed (adequate=%s "
            "limited=%s); the fit-verdict slide names these groups by hand "
            "in %s -- update that wording before regenerating"
            % (sorted(adequate_groups), sorted(limited_groups), DECK_SRC.name))
    tex.append("")

    def ratio(g2_rows: list[dict], group: str, weighting: str) -> float:
        for r in g2_rows:
            if (r["group"] == group and r["weighting"] == weighting
                    and r["statistic"] == ALLOWED_FIT_STATISTIC
                    and r.get("scope", "all") == "all"):
                return float(r["adequacy_ratio_mcse_to_sampling_sd"])
        raise SystemExit("REFUSED: no %s/%s/%s row in %s"
                         % (group, weighting, ALLOWED_FIT_STATISTIC, g2_path))

    cm_weighted_v3 = ratio(g2, "couples_male", "weighted")
    cm_unweighted_v3 = ratio(g2, "couples_male", "unweighted")
    tex.append("% --- fit-verdict slide note: POSFIT v3 ---")
    mac("FitExtRatioCMWeightedVThree", num(cm_weighted_v3, 3),
        "g2_adequacy.csv (v3) couples_male/weighted/extensive_accuracy adequacy ratio",
        cm_weighted_v3)
    mac("FitExtRatioCMUnweightedVThree", num(cm_unweighted_v3, 3),
        "g2_adequacy.csv (v3) couples_male/unweighted/extensive_accuracy adequacy ratio",
        cm_unweighted_v3)
    mac("PosfitVThreeCommit", POSFIT_COMMIT,
        "MNL_posfit commit carrying positive_fit_diagnostics_v3 (diagnostics/posfit-v3 branch)")
    tex.append("")

    provp = POSFIT / "run_provenance.json"
    pf = json.loads(provp.read_text(encoding="utf-8"))
    prov["sources"]["run_provenance.json"] = {
        "path": str(provp), "sha256": sha256(provp), "posfit_commit": POSFIT_COMMIT}
    tex.append("% --- S11 objectives reproduced by the diagnostics evaluator (POSFIT v3) ---")
    mac("ObjSingles", num(pf["objectives"]["singles"], 3),
        "v3 run_provenance.json objectives.singles", pf["objectives"]["singles"])
    mac("ObjCouples", num(pf["objectives"]["couples"], 3),
        "v3 run_provenance.json objectives.couples", pf["objectives"]["couples"])
    # Two DIFFERENT node counts, never conflated (DECK-3):
    #  FitNodes   = the diagnostic panel's common quadrature nodes per household
    #               (v2b S12 support), used by the G2 node bootstrap;
    #  FrameDraws = the estimation frame's drawn alternatives per household
    #               (criterion-A R100 panel that S11 was estimated on), as
    #               recorded by v2b support_record_v2.csv.
    support_match = re.search(r"([\d,]+) already-priced common nodes", pf["predictive_support"])
    if not support_match:
        raise SystemExit("REFUSED: cannot parse v3 predictive_support node count")
    fit_nodes = int(support_match.group(1).replace(",", ""))
    mac("FitNodes", count(fit_nodes),
        "v3 run_provenance.json predictive_support", fit_nodes)
    s11_record_path = S11 / "s11_welfare_specs_of_record_v1.json"
    s11_record = json.loads(s11_record_path.read_text(encoding="utf-8"))
    prov["sources"][s11_record_path.name] = {
        "path": str(s11_record_path), "sha256": sha256(s11_record_path)}
    alternatives = {int(v["n_alternatives"]) for v in s11_record["results"].values()}
    if alternatives != {101}:
        raise SystemExit("REFUSED: S11 alternatives per household changed: %s" % alternatives)
    mac("FrameDraws", str(alternatives.pop() - 1),
        "s11_welfare_specs_of_record_v1.json results.*.n_alternatives minus observed alternative")
    mac("FitSims", str(pf["c5_simulation"]["draws"]),
        "v3 run_provenance.json c5_simulation.draws (fixed-theta outcome vectors)")
    mac("EvaluatorCommit", pf["evaluator_commit"][:7],
        "v3 run_provenance.json evaluator_commit")
    mac("PosfitCommit", POSFIT_COMMIT, "MNL_posfit commit carrying positive_fit_diagnostics_v3")
    tex.append("")

    # -------------------------------------------------------- S11 estimates
    tex.append("% --- S11 model of record: estimated opportunity kernel ---")
    for grp, tag, fn in (("singles", "Sing", "s11_singles_parameter_table_v1.csv"),
                         ("couples", "Coup", "s11_couples_parameter_table_v1.csv")):
        p = S11 / fn
        prov["sources"][fn] = {"path": str(p), "sha256": sha256(p)}
        tab = {r["param"]: r for r in rows(p)}
        active = [r for r in tab.values() if r["pinned"] == "False"]
        mac("S%sParams" % tag, str(len(tab)), "%s row count" % fn, len(tab))
        mac("S%sActive" % tag, str(len(active)), "%s non-pinned rows" % fn, len(active))
        if grp == "singles":
            for nm, label in (("beta_E", "AccessConst"), ("beta_E_gsur", "AccessSur"),
                              ("beta_h_f35", "HoursFThirtyFive"), ("beta_c", "BetaC"),
                              ("sigma", "WageSigma"), ("beta_w_educH", "WageEducH"),
                              ("beta_w_pexp", "WagePexp")):
                r = tab[nm]
                mac("SEleven" + label, num(float(r["estimate"]), 3),
                    "%s %s estimate" % (fn, nm), float(r["estimate"]))
                if r["se_robust_CR1"]:
                    mac("SEleven" + label + "Z", num(float(r["z_robust"]), 1),
                        "%s %s z_robust" % (fn, nm), float(r["z_robust"]))
    tex.append("")

    # ------------------------------------------------------- sample framing
    tex.append("% --- estimation frames (S11 corrected criterion-A) ---")
    mac("FrameSingles", count(agg["samples"]["singles"]["unweighted_n"]),
        "baseline_f1 samples.singles.unweighted_n")
    mac("FrameCouples", count(agg["samples"]["couples"]["unweighted_n"]),
        "baseline_f1 samples.couples.unweighted_n")
    tex.append("")

    # REPORT-V6: read the two diagnostic magnitudes from the supplied memo.
    diag_path = HERE.parent / "docs/Decomposition_diag_1.txt"
    diag_text = diag_path.read_text(encoding="utf-8")
    prov["sources"][diag_path.name] = {
        "path": str(diag_path), "sha256": sha256(diag_path)}
    tex.append("% --- wage-offer location diagnostic (appendix only) ---")
    for macro, pattern in (
        ("OfferLocationLog", r"at most about (0\.10) log points"),
        ("OfferSpreadLog", r"sigma ≈ (0\.37)"),
    ):
        match = re.search(pattern, diag_text)
        if not match:
            raise SystemExit("Diagnostic source missing: " + macro)
        value = float(match[1])
        mac(macro, format(value, ".2f"),
            "Decomposition_diag_1.txt section 5 Verdict; log points", value)

    OUT_JSON.parent.mkdir(exist_ok=True)
    OUT_TEX.write_text("\n".join(tex) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(prov, indent=2, sort_keys=True), encoding="utf-8")
    print("wrote %s (%d macros)" % (OUT_TEX.name, len(prov["macros"])))
    print("G2-ADEQUATE extensive accuracy: %s" % (", ".join(adequate_groups) or "none"))
    print("withheld as quadrature-limited: %s" % (", ".join(limited_groups) or "none"))
    for r in prov["refusals"]:
        print("  refused: %s" % r)
    return 0


# ==========================================================================
# DECK-V16: the same number source, repointed at the V15 number registry.
#
#   python make_deck_numbers_r6.py --v16
#
# writes deck_numbers_v16.tex and build/v16_number_provenance.json.  The R6
# path above is untouched and remains the default.  V16 reads ONE source,
# reports/numbers_of_record_v15.json -- the registry behind
# JMP_research_story_report_v15.html and JMP_results_gallery_v15.html -- and
# only formats registry values: no arithmetic, no rerun, no second source.
# Every macro records its registry key, the raw registry value and the format
# used, so the verifier can re-derive each rendered string from the registry.
# ==========================================================================
V15_REGISTRY = HERE.parent / "reports" / "numbers_of_record_v15.json"
V16_OUT_TEX = HERE / "deck_numbers_v16.tex"
V16_OUT_JSON = HERE / "build" / "v16_number_provenance.json"

# macro name -> (registry key, format spec).  "," in a spec is Python's
# thousands separator, rendered as a plain comma exactly as the V15 report does.
V16_MACROS = {
    # data and samples
    "VCollectionYear": ("collection_year", "d"),
    "VIncomeYear": ("income_year", "d"),
    "VNSingles": ("n_singles", ",d"),
    "VNCouples": ("n_couples", ",d"),
    # real-world inequality: consumption versus attained-bundle money metric
    "VCEqGiniSingles": ("ceq_gini_singles", ".4f"),
    "VAttEqGiniSingles": ("w1f_eq_gini_singles", ".4f"),
    "VCEqGiniCouples": ("ceq_gini_couples", ".4f"),
    "VAttEqGiniCouples": ("w1f_eq_gini_couples", ".4f"),
    # do opportunities matter for behaviour: common-opportunity benchmarks
    "VKFreeSingles": ("kfree_singles", "d"),
    "VKFreeRumA": ("kfree_ruma", "d"),
    "VKFreeRumB": ("kfree_rumb", "d"),
    "VRumGap": ("rum_gap", ".2f"),
    "VMaeSingles": ("mae_singles", ".4f"),
    "VMaeRumA": ("mae_ruma", ".4f"),
    "VMaeRumB": ("mae_rumb", ".4f"),
    # matched-household illustration
    "VMatchedAccessRatio": ("mh_access_ratio", ".1f"),
    "VMatchedWageGap": ("mh_wage_gap", ".1f"),
    "VMatchedEmpShareA": ("mh_employment_share_a", ".2f"),
    "VMatchedEmpShareB": ("mh_employment_share_b", ".2f"),
    # ex-ante (EA) perspective: access + earnings as % of own baseline Gini
    "VEAOppMin": ("wea_opportunity_min_pct", ".1f"),
    "VEAOppMax": ("wea_opportunity_max_pct", ".1f"),
    "VEASingOppRaw": ("wea_singles_uneq_opportunity_pct", ".1f"),
    "VEASingOppEq": ("wea_singles_eq_opportunity_pct", ".1f"),
    "VEACoupOppRaw": ("wea_couples_uneq_opportunity_pct", ".1f"),
    "VEACoupOppEq": ("wea_couples_eq_opportunity_pct", ".1f"),
    "VEASingRatioRaw": ("wea_singles_access_earn_ratio_uneq", ".1f"),
    "VEASingRatioEq": ("wea_singles_access_earn_ratio_eq", ".1f"),
    "VEASingPhiARaw": ("wea_singles_uneq_phi_a", ".5f"),
    "VEASingPhiBRaw": ("wea_singles_uneq_phi_b", ".5f"),
    "VEASingPhiAEq": ("wea_singles_eq_phi_a", ".5f"),
    "VEASingPhiBEq": ("wea_singles_eq_phi_b", ".5f"),
    "VEACoupPhiARaw": ("wea_couples_uneq_phi_a", ".5f"),
    "VEACoupPhiBRaw": ("wea_couples_uneq_phi_b", ".5f"),
    "VEACoupPhiAEq": ("wea_couples_eq_phi_a", ".5f"),
    "VEACoupPhiBEq": ("wea_couples_eq_phi_b", ".5f"),
    "VEACoupPrefRaw": ("wea_couples_pref_uneq", ".5f"),
    "VEACoupPrefEq": ("wea_couples_pref_eq", ".5f"),
    # attained-bundle (ATT) benchmark
    "VAttOppMin": ("att_opportunity_min_pct", ".1f"),
    "VAttOppMax": ("att_opportunity_max_pct", ".1f"),
    "VAttSingOppRaw": ("att_singles_uneq_opportunity_pct", ".1f"),
    "VAttSingOppEq": ("att_singles_eq_opportunity_pct", ".1f"),
    "VAttCoupOppRaw": ("att_couples_uneq_opportunity_pct", ".1f"),
    "VAttCoupOppEq": ("att_couples_eq_opportunity_pct", ".1f"),
    "VAttSingPhiARaw": ("d2_giniA_singles_uneq", ".4f"),
    "VAttSingPhiBRaw": ("d2_giniB_singles_uneq", ".4f"),
    "VAttSingPhiAEq": ("d2_giniA_singles_eq", ".4f"),
    "VAttSingPhiBEq": ("d2_giniB_singles_eq", ".4f"),
    "VAttCoupPhiARaw": ("d2_giniA_couples_uneq", ".4f"),
    "VAttCoupPhiBRaw": ("d2_giniB_couples_uneq", ".4f"),
    "VAttCoupPhiAEq": ("d2_giniA_couples_eq", ".4f"),
    "VAttCoupPhiBEq": ("d2_giniB_couples_eq", ".4f"),
}


def v16_render(value, spec: str) -> str:
    """Format one registry value; a minus sign becomes LaTeX math minus."""
    text = format(value, spec)
    return text.replace("-", "$-$") if text.startswith("-") else text


def main_v16() -> int:
    registry = json.loads(V15_REGISTRY.read_text(encoding="utf-8"))
    entries = registry["entries"]
    if "v15" not in str(registry.get("presentation_version", "")):
        raise SystemExit("REFUSED: %s is not the V15 registry" % V15_REGISTRY.name)
    prov: dict = {"registry": str(V15_REGISTRY), "registry_sha256": sha256(V15_REGISTRY),
                  "presentation_version": registry["presentation_version"],
                  "macros": {}}
    tex = [
        "% deck_numbers_v16.tex -- GENERATED by make_deck_numbers_r6.py --v16.",
        "% Do not edit by hand.  Every numeral on a V16 slide comes from here, and",
        "% every value here is one entry of reports/numbers_of_record_v15.json,",
        "% formatted only (no arithmetic).",
        "",
    ]
    for name, (key, spec) in V16_MACROS.items():
        if key not in entries:
            raise SystemExit("REFUSED: registry key %r missing from V15 registry" % key)
        raw = entries[key]["value"]
        if isinstance(raw, str):
            raise SystemExit("REFUSED: registry key %r is not numeric" % key)
        rendered = v16_render(raw, spec)
        tex.append(r"\newcommand{\%s}{%s}" % (name, rendered))
        prov["macros"][name] = {"key": key, "raw": raw, "format": spec,
                                "rendered": rendered,
                                "units": entries[key].get("units"),
                                "status": entries[key].get("status")}
    V16_OUT_JSON.parent.mkdir(exist_ok=True)
    V16_OUT_TEX.write_text("\n".join(tex) + "\n", encoding="utf-8", newline="\n")
    V16_OUT_JSON.write_text(json.dumps(prov, indent=2, sort_keys=True), encoding="utf-8",
                            newline="\n")
    print("wrote %s (%d macros from %s)" % (V16_OUT_TEX.name, len(prov["macros"]),
                                           V15_REGISTRY.name))
    return 0


if __name__ == "__main__":
    import sys
    raise SystemExit(main_v16() if "--v16" in sys.argv[1:] else main())
