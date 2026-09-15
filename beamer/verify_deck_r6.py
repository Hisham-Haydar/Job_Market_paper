#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""R6 gates for the seminar deck.

The v4 gates are bound to content R2 retires, so they do not apply to this
deck.  These gates enforce what R6 and the BASELINE-F-1 ruling actually
require:

  G-RETIRE   no retired W1-EA magnitude appears anywhere in the PDF text.
  G-DECOMP   the M10 DECOMP-2 wording and immediately-following caveat appear.
  G-CAPTION  the calibration figure carries the required caption verbatim.
  G-UNITS    every welfare slide states units, weight and unequivalised.
  G-SOURCE   the welfare slides cite the recorded and verified commits.
  G-NUMBERS  every numeral in the deck source is a macro, not typed.
  G-G2       only G2-ADEQUATE fit statistics reach a slide.
  G-QA       every welfare slide's note is a Q&A note citing a ruling ID.
  G-NOCONF   no confusion-matrix headline number.
  G-POOLED   no pooled welfare figure.
  G-NOSIDEBYSIDE  no singles/couples equivalised-welfare-level comparison
             in one visual (slide/table/figure) or one sentence; the old
             "near equality" claim never appears (docs deputy item A).
  G-EQPRIMARY  the equivalised welfare slides exist, are primary (section 6),
             and the unequivalised slides are demoted to backup (item B).
  G-CHILDSHIFTER  the child-shifter wording is present verbatim and is never
             called a preference/taste parameter (item C).
  G-PLABEL   the P label is unchanged and A is narrowed to the authorized
              local geographic/temporal shifters (M5).
  G-NOBAN    none of the seminar-freeze out-of-scope tokens appear: W_EA,
             finite-offer welfare, OEC characterisation, SCALE-SENS-1 (item F).
  G-SCALE    (DECK-3) the equivalised slides cite the ratifying Deputy ruling
             "SCALE CLOSED; CHILD-SHIFTER FRAMING" s1 and the scale-review memo
             JMP_SCALE_REVIEW_1_equivalence_scale_economics_v1.md, and no
             "PROVISIONAL" / "pending economics review" wording reappears.
  G-ASSETS   (HAZARD-1) every figure/table asset the compiled deck references
             resolves to a file the R6 generators actually wrote THIS run
             under figures/r6/ (an allowlist, not a denylist of names), and no
             reference anywhere in the deck source touches beamer/_retired_assets
             or a mock_presentation-named tree.

FINAL-GATE-1 repoints G-G2 and G-CAPTION wholly to POSFIT v3. G-G2 binds
displayed accuracy to the observed column in hard_classification_metrics.csv
and uses g2_adequacy.csv only for the numerical-adequacy verdict.

Exit code 0 only if every gate passes.
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]

import sys
sys.path.insert(0, str(HERE.parent / "reports"))
import retired_lineage_gate as rlg  # noqa: E402
BUILD = HERE / "build"
SRC = HERE / "JMP_seminar_deck_r6.tex"
NUMBERS = HERE / "deck_numbers_r6.tex"
TEXT = BUILD / "JMP_seminar_deck_r6_text.txt"
POSFIT = REPO / "MNL_posfit" / "outputs" / "positive_fit_diagnostics_v3"   # MNL_posfit 96693269

# Magnitudes that exist only in the retired W1-EA record (R2).  Sources:
# beamer/check_deck_welfare_current_v1.py and the superseded welfare block of
# manuscript/JMP_seminar_deck_content_v2.md.
RETIRED_TOKENS = {
    "58%": "W1-EA nested endowments-and-needs share",
    "93.7": "W1-EA environment share",
    "94%": "W1-EA Shapley environment share",
    "35.5%": "W1-EA narrow job-opportunity total",
    "45.73": "W1-EA nested non-labour resources share",
    "12.45": "W1-EA nested composition share",
    "0.134": "W1-EA baseline Gini",
    "13.05": "W1-EA geographic access share",
    "19.58": "W1-EA men's job-access share",
    "49.16": "W1-EA corrected-frame access share",
    "55.92": "W1-EA corrected-frame job-opportunity total",
    "34.20": "W1-EA corrected-frame resources-and-needs share",
    "0.193596": "W1-EA corrected-frame baseline Gini",
    "9.88": "W1-EA corrected-frame preference share",
    "8.23": "W1-EA couples access share",
    "35.72": "W1-EA couples earning-opportunity share",
    "51.20": "W1-EA couples resources-and-needs share",
    "4.29": "W1-EA-era couples curvature ratio",
    "power mean": "W1-EA power-mean text",
    "power-mean": "W1-EA power-mean text",
    "figP07": "W1-EA figure figP07",
    "77%": "W1-EA direct counterfactual reduction",
    "6.3%": "W1-EA preference share",
    "6.4%": "W1-EA benchmark preference share",
}

# Seminar-freeze out-of-scope tokens (docs/JMP_seminar_architecture_freeze_
# 2026-09-17_v1.md, item F of the deputy brief).  Added to the existing
# 24-entry RETIRED_TOKENS map above without removing any of its entries;
# "figP07" and "4.29" are already covered by that map.
OUT_OF_SCOPE_TOKENS = {
    "W_EA": "October-only W_EA welfare architecture, banned before then",
    "finite-offer welfare": "finite-offer welfare architecture, October-only",
    "finite-market-set welfare": "finite-market-set welfare, October-only",
    "OEC characterisation": "OEC-CHAR-1 mission, on HOLD until October",
    "OEC-CHAR": "OEC-CHAR-1 mission, on HOLD until October",
    "SCALE-SENS-1": "scale-sensitivity mission, not a seminar deliverable",
}
RETIRED_TOKENS.update(OUT_OF_SCOPE_TOKENS)
# The reader-facing caption states the diagnostic status in plain economics.
CAPTION = ("support coverage audited using individual-level predictive "
           "diagnostics; calibration statistics "
           "partly quadrature-limited; use the explicit group verdicts")
RETIRED_CAPTION = "support audit pending"
WELFARE_FRAMES = ["Haydar--Maniquet", "staying-home equivalent",
                  "Baseline $\\Wone$-F, single adults",
                  "Baseline $\\Wone$-F, couples",
                  "Four operators", "observed", "quantitative welfare decomposition"]

fails: list[str] = []
passes: list[str] = []


def gate(name: str, ok: bool, detail: str) -> None:
    (passes if ok else fails).append("%-10s %s" % (name, detail))


def frames(src: str) -> list[str]:
    return re.findall(r"\\begin\{frame\}(.*?)\\end\{frame\}", src, re.S)


def flat(s: str) -> str:
    """Collapse all whitespace runs (including line wraps) to one space, so
    a verbatim-wording check does not break just because the .tex source or
    the pdftotext -layout extraction happens to wrap a sentence differently
    than the canonical string is typed here."""
    return re.sub(r"\s+", " ", s).strip()


def headline(frame: str) -> str:
    m = re.search(r"\\headlineframe\{(.*?)\}", frame, re.S)
    return flat(m.group(1)) if m else ""


def reader_voice_provenance(src: str) -> str:
    """Return the single source-only provenance block, or an empty string."""
    blocks = re.findall(
        r"% BEGIN READER-VOICE PROVENANCE(.*?)% END READER-VOICE PROVENANCE",
        src,
        re.S,
    )
    return blocks[0] if len(blocks) == 1 else ""


def main() -> int:
    src = SRC.read_text(encoding="utf-8")
    nums = NUMBERS.read_text(encoding="utf-8")
    text = TEXT.read_text(encoding="utf-8", errors="replace") if TEXT.exists() else ""
    provenance = reader_voice_provenance(src)

    # ---------------------------------------------------------- G-RETIRE
    hits = []
    haystack = (src + "\n" + text).lower()
    for tok, why in RETIRED_TOKENS.items():
        # the token list is checked in the deck body and the rendered text,
        # never in this file's own comments
        if tok.lower() in haystack:
            hits.append("%s (%s)" % (tok, why))
    gate("G-RETIRE", not hits,
         "no retired W1-EA magnitude present" if not hits
         else "RETIRED MATERIAL PRESENT: " + "; ".join(hits))

    # ---------------------------------------------------------- G-DECOMP
    # M10 authorises one bounded DECOMP-2 claim and requires its caveat to
    # follow immediately.  The numerical range itself is macro-backed.
    result_frames = [f for f in frames(src)
                     if r"\DTwoMinPct--\DTwoMaxPct\%" in f]
    result = flat(result_frames[0]) if len(result_frames) == 1 else ""
    approved = [
        "In a preliminary three-factor structural exercise that holds "
        "household resources, needs and composition fixed, equalising "
        "systematic utility heterogeneity, coarse geographic/temporal access "
        "heterogeneity and earning opportunities changes money-metric "
        "well-being inequality by",
        "of the baseline Gini, depending on household type and reporting scale.",
        "Within the Shapley allocation of that movable component, "
        "earning-opportunity heterogeneity has a larger contribution than the "
        "coarse geographic/temporal access channel in both samples and both "
        "reporting conventions.",
        "The preference contribution is not sign-robust to equivalisation.",
    ]
    caveat = ("These are preliminary model-based accounting results, not "
              "causal estimates and not the final decomposition of total "
              "well-being inequality.")
    pref_ix = result.find(approved[-1])
    caveat_ix = result.find(caveat)
    note_ix = result.find(r"\note{")
    adjacent = pref_ix != -1 and caveat_ix > pref_ix and \
        (note_ix == -1 or caveat_ix < note_ix)
    gate("G-DECOMP",
         len(result_frames) == 1 and all(s in result for s in approved)
         and adjacent,
         "approved M10 claim present; required caveat follows immediately"
         if len(result_frames) == 1 and all(s in result for s in approved)
         and adjacent else "M10 claim missing, paraphrased, duplicated, or "
                            "detached from its caveat")

    # REPORT-V6 changes the placement, not the accepted numerical evidence.
    main_src, backup_src = src.split(r"\appendix", 1)
    mission = ("A preliminary P/A/B decomposition has been computed for the attained-bundle "
               "money metric, holding resources, needs and composition fixed. It is a "
               "restricted counterfactual exercise, not a comprehensive share of inequality "
               "due to all opportunities. A separately defined ex-ante metric is being "
               "reconstructed for comparison; neither historical ex-ante percentages nor "
               "a settled cross-estimand conclusion are reported here.")
    gate("G-DECOMP-BACKUP",
         r"\DTwoMinPct" not in main_src and r"\DTwoVarMinPct" not in main_src
         and "earning-opportunity heterogeneity has a larger" not in flat(main_src)
         and mission in flat(backup_src)
         and "Preliminary restricted-operator decomposition" in backup_src,
         "computed decomposition and exact scope wording are confined to backup")

    # --------------------------------------------------------- G-CAPTION
    cap_ok = (CAPTION in flat(src) and (not text or CAPTION in flat(text))
              and RETIRED_CAPTION not in (src + text).lower())
    gate("G-CAPTION", cap_ok,
         "plain-language calibration caption verbatim: %r; retired %r absent"
         % (CAPTION, RETIRED_CAPTION))

    # ----------------------------------------------------------- G-UNITS
    # Four distribution slides now: 2 equivalised PRIMARY (\S6, \wfunitseq)
    # and 2 unequivalised BACKUP (appendix, \wfunits) -- not the B3/B4/B5
    # checks/gate/authority slides that share the "Baseline $\Wone$-F" stem.
    wf = [f for f in frames(src) if "Baseline $\\Wone$-F," in headline(f)]
    wf_eq = [f for f in wf if "unequivalised" not in headline(f)]
    wf_uneq = [f for f in wf if "unequivalised" in headline(f)]
    ok_eq = len(wf_eq) == 2 and all("\\wfunitseq" in f for f in wf_eq)
    ok_uneq = len(wf_uneq) == 2 and all("\\wfunits" in f for f in wf_uneq)
    flat_text = flat(text)
    rendered_units = (not text) or (
        "household EUR/month, unequivalised" in flat_text
        and "household-equivalised" in flat_text)
    gate("G-UNITS", ok_eq and ok_uneq and rendered_units,
         "%d equivalised (primary) + %d unequivalised (backup) baseline "
         "slides, each carrying units/weight/scale-status"
         % (len(wf_eq), len(wf_uneq)))

    # ---------------------------------------------------------- G-SOURCE
    source_tokens = (
        "JMP_W1_fork_ruling_v1.md",
        "JMP_W1_BASELINE_F1_authorization_and_Cobs_ruling_v1.md",
        "JMP_BASELINE_F1_equivalised_reporting_v1.md",
        "6048c9f7",
        "b5550af5",
        "4c4e07e",
    )
    gate("G-SOURCE",
         bool(provenance) and all(token in provenance for token in source_tokens),
         "source-only provenance carries the welfare artifacts, recorded "
         "6048c9f7, verified b5550af5, and equivalised-reporting 4c4e07e")

    # --------------------------------------------------------- G-NUMBERS
    body = re.sub(r"(?m)^\s*%.*$", "", src)
    body = body.split(r"\begin{document}", 1)[1]
    body = re.sub(r"\\note\{.*?\n\}", "", body, flags=re.S)      # notes are prose
    typed = set()
    for m in re.finditer(r"(?<![\\A-Za-z0-9=\-])\d+(?:\.\d+)?", body):
        frag = body[max(0, m.start() - 40):m.start()]
        if re.search(r"(RGB|rgb|node distance|inner sep|minimum |xshift|yshift|"
                     r"vskip|hspace|vspace|width|height|sep=|scale|lw|alpha|"
                     r"itemsep|em\}|pt\}|mm|\\rule|\\fontsize|linespread|"
                     r"parskip|\\vskip|opacity|!)\s*[^ ]*$", frag):
            continue
        typed.add(m.group(0))
    # Allowed without a macro: TikZ/list indices, the gate threshold quoted in
    # a caption, the seminar date, and the statutory 35-hour week -- a legal
    # fact named on the model diagram, not an estimate.
    allowed = {"0", "1", "2", "3", "4", "1.96", "0.25"}
    if "17 September" in body:
        allowed.add("17")
    if "35h peak" in body or "35-hour" in body:
        allowed.add("35")
    typed -= allowed
    gate("G-NUMBERS", not typed,
         "no hand-typed quantitative numeral on a slide" if not typed
         else "hand-typed numerals: " + ", ".join(sorted(typed)))

    # -------------------------------------------------------------- G-G2
    with (POSFIT / "g2_adequacy.csv").open(newline="", encoding="utf-8") as fh:
        g2 = list(csv.DictReader(fh))
    adequate = {(r["group"], r["statistic"]) for r in g2
                if r["weighting"] == "weighted" and r["label"] == "ADEQUATE"}
    emitted = json.loads((BUILD / "r6_number_provenance.json").read_text(encoding="utf-8"))
    bad_fit = []
    for name, meta in emitted["macros"].items():
        s = meta["source"]
        if not s.startswith("g2_adequacy.csv"):
            continue
        if "ADEQUATE" not in s and "count of" not in s and "adequacy ratio" not in s:
            bad_fit.append(name)
    # DECK-3: tie the slide's per-group rows to the source labels in both
    # directions -- an ADEQUATE group's macro must be on a slide, and a
    # QUADRATURE-LIMITED group must have no macro at all.
    tag_of = {"singles_male": "SM", "singles_female": "SF",
              "couples_male": "CM", "couples_female": "CF"}
    ext = {r["group"]: r["label"] for r in g2
           if r["weighting"] == "weighted" and r["statistic"] == "extensive_accuracy"
           and r.get("scope", "all") == "all"}
    row_bad = []
    for grp, lab in ext.items():
        mname = "FitExt" + tag_of[grp]
        if lab == "ADEQUATE" and ("\\" + mname + "{}") not in src:
            row_bad.append("%s ADEQUATE but not on slide" % grp)
        if lab != "ADEQUATE" and mname in emitted["macros"]:
            row_bad.append("%s %s but emitted" % (grp, lab))
    hard = list(csv.DictReader((POSFIT / "hard_classification_metrics.csv").open(
        newline="", encoding="utf-8")))
    hard_observed = {r["group"]: float(r["extensive_accuracy"])
                     for r in hard if r["weighting"] == "weighted"}
    value_bad = []
    for grp, lab in ext.items():
        if lab != "ADEQUATE":
            continue
        meta = emitted["macros"]["FitExt" + tag_of[grp]]
        if not meta["source"].startswith("hard_classification_metrics.csv"):
            value_bad.append("%s not observed-source bound" % grp)
        if abs(float(meta["raw"]) - hard_observed[grp]) > 1e-15:
            value_bad.append("%s observed value mismatch" % grp)
    posfit_ok = all(
        "positive_fit_diagnostics_v3" in v["path"]
        for k, v in emitted["sources"].items() if "MNL_posfit" in v.get("path", ""))
    gate("G-G2", (not bad_fit) and bool(adequate) and not row_bad and posfit_ok
         and not value_bad,
         "%d ADEQUATE weighted statistics exist; only those are emitted; "
         "extensive-accuracy rows match v3 labels %s and observed values"
         % (len(adequate), ext)
         if not row_bad and posfit_ok and not value_bad
         else "G2 row/source/value mismatch %s %s or non-v3 positive-fit source"
              % (row_bad, value_bad))

    # ----------------------------------------------------------- G-SCALE
    # DECK-3: the modified-OECD scale is ratified.  Every equivalised welfare
    # slide must state the scale in plain language; the source-only provenance
    # block must carry the ratifying ruling and scale-review memo. No
    # "PROVISIONAL" scale wording may reappear in the visible source or deck.
    ruling = "SCALE CLOSED; CHILD-SHIFTER FRAMING"
    memo = "JMP_SCALE_REVIEW_1_equivalence_scale_economics_v1.md"
    unesc = src.replace("\\_", "_")
    wfeq_macro = re.search(r"\\newcommand\{\\wfunitseq\}(.*?)\n\n", unesc, re.S)
    macro_plain = bool(wfeq_macro) and "modified-OECD scale" in flat(
        wfeq_macro.group(1))
    provenance_cites = bool(provenance) and ruling in provenance \
        and memo in provenance
    rendered_plain = (not text) or "modified-OECD scale" in flat_text
    nocomment = re.sub(r"(?m)%.*$", "", src)
    prov_hits = sorted(set(m.group(0) for m in re.finditer(
        r"provisional[^.\n]{0,40}|pending\s+(an\s+)?economics\s+review",
        (nocomment + "\n" + text), re.I)))
    scale_ok = (macro_plain and provenance_cites and ok_eq and rendered_plain
                and not prov_hits)
    gate("G-SCALE", scale_ok,
         "both equivalised slides state the modified-OECD scale; source-only "
         "provenance cites %r and %s; no PROVISIONAL scale wording"
         % (ruling, memo) if scale_ok
         else "scale statement/citation missing (macro=%s provenance=%s "
              "rendered=%s) or provisional wording present: %s"
              % (macro_plain, provenance_cites, rendered_plain, prov_hits))

    # -------------------------------------------------------------- G-QA
    notes_missing = []
    for f in frames(src):
        if not any(k in f for k in ("\\Wone", "Baseline", "operators", "attainment",
                                    "welfare decomposition")):
            continue
        m = re.search(r"\\note\{(.*?)\n\}", f, re.S)
        if m is None:
            continue
        note = m.group(1)
        if "Q&A note" in note or "Q\\&A note" in note:
            if not re.search(r"\bR[1-6]\b|BASELINE-F-1|\bE[1-3]\b", note):
                notes_missing.append("note without a ruling ID")
    # every welfare-section frame must carry one
    welfare_src = src.split("% ================================================================ 5 W1", 1)[1]
    welfare_src = welfare_src.split("% ================================================================ BACKUP", 1)[0]
    wframes = frames(welfare_src)
    qa = [f for f in wframes if "Q\\&A note" in f or "Q&A note" in f]
    gate("G-QA", len(qa) == len(wframes) and not notes_missing,
         "%d/%d welfare slides carry a Q&A note citing a ruling ID"
         % (len(qa), len(wframes)))

    # ---------------------------------------------------------- G-NOCONF
    # Confusion-matrix vocabulary only.  "sensitivity" and "precision" are not
    # on this list: both carry an ordinary meaning the deck uses (Mapping M is
    # sensitivity only; machine precision), and neither names a cell count.
    conf = [w for w in ("confusion matrix", "confusion matrices",
                        "balanced accuracy", "specificity", "true positive",
                        "false positive", "true negative", "false negative",
                        "recall rate")
            if w in text.lower()]
    gate("G-NOCONF", not conf,
         "no confusion-matrix headline statistic" if not conf
         else "confusion-matrix language rendered: " + ", ".join(conf))

    # ---------------------------------------------------------- G-POOLED
    agg = json.loads((REPO / "MNL/outputs/welfare/baseline_f1_v1/"
                      "baseline_f1_full_sample_aggregates_v1.json")
                     .read_text(encoding="utf-8"))
    pooled_residual = flat_text.lower().replace("no pooled figure", "")
    gate("G-POOLED", agg["pooled_row"] is False and "pooled" not in pooled_residual,
         "source carries no pooled row; deck shows singles and couples separately")

    # ----------------------------------------------------- G-NOSIDEBYSIDE
    # Item A: no singles/couples EQUIVALISED-welfare-LEVEL comparison in one
    # visual or one sentence, and the withdrawn "near equality" claim never
    # reappears.  Frame-level check: no single frame carries both a
    # singles-equivalised macro and a couples-equivalised macro.
    sing_eq_re = re.compile(r"\\WFSing[A-Za-z]*Eq[A-Za-z]*")
    coup_eq_re = re.compile(r"\\WFCoup[A-Za-z]*Eq[A-Za-z]*")
    mixed = [i for i, f in enumerate(frames(src))
             if sing_eq_re.search(f) and coup_eq_re.search(f)]
    # Rendered-text check: the literal equivalised Gini values for singles
    # and for couples must never land in the same paragraph (a blank-line
    # separated block of pdftotext -layout output is the closest proxy for
    # "one visual/one sentence" available on extracted text).
    provfile = BUILD / "r6_number_provenance.json"
    nums = json.loads(provfile.read_text(encoding="utf-8"))["macros"] \
        if provfile.exists() else {}
    sing_vals = [nums[k]["rendered"] for k in nums if re.match(r"WFSing.*Eq.*Gini$", k)]
    coup_vals = [nums[k]["rendered"] for k in nums if re.match(r"WFCoup.*Eq.*Gini$", k)]
    para_hits = []
    if text and sing_vals and coup_vals:
        for para in re.split(r"\n\s*\n", text):
            if any(v in para for v in sing_vals) and any(v in para for v in coup_vals):
                para_hits.append(para[:80])
    near_eq = [p for p in ("near equality", "nearly equal", "near-equality")
               if p in (src + "\n" + text).lower()]
    gate("G-NOSIDEBYSIDE",
         not mixed and not para_hits and not near_eq,
         "no frame or paragraph mixes singles- and couples-equivalised "
         "levels; withdrawn near-equality claim absent"
         if not mixed and not para_hits and not near_eq
         else "VIOLATION: mixed frames=%s paragraphs=%s near-equality=%s"
              % (mixed, para_hits, near_eq))

    # -------------------------------------------------------- G-EQPRIMARY
    # Item B: equivalised results are primary (section 6), unequivalised
    # demoted to a backup appendix slide.
    sec6_ix = src.find(r"\section{Equivalised $\Wone$-F distribution")
    appendix_ix = src.find(r"\appendix")
    backup_eq_frames = [f for f in frames(src)
                        if "Baseline $\\Wone$-F," in headline(f)
                        and "unequivalised" in headline(f)]
    gate("G-EQPRIMARY",
         sec6_ix != -1 and appendix_ix != -1 and sec6_ix < appendix_ix
         and len(backup_eq_frames) == 2
         and all(src.find(f) > appendix_ix for f in backup_eq_frames),
         "equivalised distribution is section 6 (primary, before \\appendix); "
         "%d unequivalised slides demoted into the backup appendix"
         % len(backup_eq_frames))

    # ----------------------------------------------------- G-CHILDSHIFTER
    # Item C: the child-shifter sentence is verbatim, and the shifter is
    # never called a preference/taste parameter outright.
    CHILD_SENTENCE = (
        "Children enter the current structural specification through a "
        "reduced-form female time-constraint shifter. In a unitary "
        "labour-supply model this term may capture both tastes and "
        "childcare/home-production constraints; we therefore do not "
        "interpret it as pure preference heterogeneity.")
    flat_src = flat(src)
    mislabel = re.search(
        r"child[a-z]*\s+(is|as|,)?\s*a\s+(pure\s+)?(preference|taste)\s+parameter",
        flat_src + " " + flat_text, re.I)
    child_ok = flat(CHILD_SENTENCE) in flat_src and mislabel is None
    gate("G-CHILDSHIFTER", child_ok,
         "child-shifter wording verbatim, never called a preference/taste "
         "parameter" if child_ok else "child-shifter wording missing or mislabelled")

    # ---------------------------------------------------------- G-PLABEL
    # M5: retain the P label and restrict A to geographic/temporal shifters.
    PLABEL = "systematic utility heterogeneity (tastes + reduced-form time constraints)"
    ALABEL = ("local geographic/temporal access shifters "
              "(region, urban/rural, year)")
    op_ix = src.find(r"\headlineframe{This bounded decomposition equalises")
    op_table = flat(src[op_ix:op_ix + 2200]) if op_ix != -1 else ""
    plabel_ok = (PLABEL in op_table and ALABEL in op_table
                 and "Personal occupation access, hours-band access" in op_table
                 and "not equalised by $A$" in op_table)
    gate("G-PLABEL",
         plabel_ok,
         "P label retained; A restricted to local geographic/temporal shifters"
         if plabel_ok else "P label or narrowed A-channel wording missing")

    # ---------------------------------------------------------- G-NOBAN
    # Item F: the seminar-freeze out-of-scope tokens, checked explicitly
    # (also covered inside G-RETIRE's merged token map above).
    ban_hits = [tok for tok in OUT_OF_SCOPE_TOKENS if tok.lower() in haystack]
    gate("G-NOBAN", not ban_hits,
         "none of the out-of-scope tokens (W_EA, finite-offer welfare, "
         "OEC characterisation, SCALE-SENS-1) appear" if not ban_hits
         else "OUT-OF-SCOPE TOKENS PRESENT: " + ", ".join(ban_hits))

    # --------------------------------------------------------- G-ASSETS
    # Allowlist = the figure files the R6 generators actually wrote THIS
    # run under figures/r6/ (build_deck_r6.py always runs
    # make_slide_figures_r6.py immediately before latexmk, so this is a
    # live snapshot of the current build, not a hardcoded name list).
    R6_FIGDIR = HERE / "figures" / "r6"
    allowlist = {p.name for p in R6_FIGDIR.glob("*.pdf")} if R6_FIGDIR.is_dir() else set()

    # Every call site that can pull in a figure/table asset: \slidefig{name}
    # (resolves to figures/r6/<name>_slide.pdf), \deckfig{name}{width} and a
    # bare \includegraphics{name} (both resolve to figures/r6/<name>[.pdf]),
    # and \input{<file>} naming a non-driver, non-numbers file (a stray table
    # input would show up here too).
    refs: list[tuple[str, str]] = []
    for m in re.finditer(r"\\slidefig\{([^}]+)\}", src):
        refs.append((m.group(1), m.group(1) + "_slide.pdf"))
    for m in re.finditer(r"\\deckfig\{([^}]+)\}\{[^}]*\}", src):
        name = m.group(1)
        refs.append((name, name if name.endswith(".pdf") else name + ".pdf"))
    for m in re.finditer(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", src):
        name = m.group(1)
        refs.append((name, name if name.endswith(".pdf") else name + ".pdf"))

    unresolved = [(call, fname) for call, fname in refs if fname not in allowlist]

    # No reference anywhere in the deck source (or preamble it pulls in via
    # \input) may touch the quarantine tree or a mock-presentation tree.
    preamble_path = HERE / "jmp_beamer_preamble.tex"
    preamble_src = preamble_path.read_text(encoding="utf-8") if preamble_path.is_file() else ""
    banned_hits = [tok for tok in ("_retired_assets", "mock_presentation", "Presentation_mock")
                   if tok in src or tok in preamble_src or tok in text]

    gate("G-ASSETS",
         bool(allowlist) and not unresolved and not banned_hits,
         "%d figure asset(s) referenced, all resolve to this run's "
         "figures/r6/ output %s; no reference to a retired-assets or "
         "mock-presentation tree"
         % (len(refs), sorted(allowlist))
         if not unresolved and not banned_hits and allowlist
         else "VIOLATION: unresolved asset references %s; banned-tree "
              "mentions %s; allowlist %s"
              % (unresolved, banned_hits, sorted(allowlist)))

    # ------------------------------------------------------- G-LINEAGE
    # LINEAGE-SWEEP-1: path-based, not string-based. G-RETIRE/G-NOSHARE
    # above check RENDERED WORDING (a specific magnitude, a specific share
    # word) -- a rewrite that keeps reading the same retired file but
    # phrases the result differently would clear both. This gate instead
    # scans the number/figure GENERATORS and the deck source for a read of
    # a retired artifact BY PATH.
    _lineage_targets = [SRC, HERE / "make_deck_numbers_r6.py",
                         HERE / "make_slide_figures_r6.py", NUMBERS]
    _lineage_violations = rlg.scan_files([p for p in _lineage_targets if p.exists()])
    gate("G-LINEAGE", not _lineage_violations,
         "no retired-lineage artifact referenced by path in the deck "
         "source or number/figure generators" if not _lineage_violations
         else "RETIRED-LINEAGE PATH READ: " +
              rlg.format_violations(_lineage_violations, REPO))

    print("R6 deck verification")
    print("-" * 68)
    for line in passes:
        print("  PASS  " + line)
    for line in fails:
        print("  FAIL  " + line)
    print("-" * 68)
    print("%d passed, %d failed" % (len(passes), len(fails)))
    return 1 if fails else 0


# ==========================================================================
# DECK-V16 profile:  python verify_deck_r6.py --deck v16
#
# The same verifier, repointed at JMP_seminar_beamer_v16.tex.  The R6 gates
# above are bound to R6 content (backup-confined decomposition wording, POSFIT
# fit labels, W1-F units slides) and are not re-run against V16.  Carried over
# unchanged in substance: the retired-token map (G-RETIRE / G-NOBAN), the
# typed-numeral scan (G-NUMBERS), the asset allowlist (G-ASSETS, now bound to
# the images embedded in the V15 report and gallery), the retired-lineage path
# scan (G-LINEAGE), G-NOCONF, G-POOLED and G-NOSIDEBYSIDE.  Added: G-REGISTRY
# (every numeral on every slide page resolves to a V15-registry entry through
# the macros that frame uses) and the V16 content gates.  Two negative
# controls are run on in-memory copies and must both FAIL their gate.
# ==========================================================================
V16_SRC = HERE / "JMP_seminar_beamer_v16.tex"
V16_NUMBERS = HERE / "deck_numbers_v16.tex"
V16_PROV = BUILD / "v16_number_provenance.json"
V16_PDF = BUILD / "JMP_seminar_beamer_v16.pdf"
V16_TEXT = BUILD / "JMP_seminar_beamer_v16_text.txt"
V16_REH_TEXT = BUILD / "JMP_seminar_beamer_v16_rehearsal_text.txt"
V16_RESULTS = BUILD / "v16_verification.json"
V15_REPORT = HERE.parent / "reports" / "JMP_research_story_report_v15.html"
V15_GALLERY = HERE.parent / "reports" / "JMP_results_gallery_v15.html"

V16_RQ = ("How much inequality in money-metric well-being is associated with unequal "
          "job opportunities rather than heterogeneous preferences, once labour supply "
          "is modelled as choice among latent jobs?")
V16_SUBQ = (
    "Do observed labour-supply choices reflect preferences alone, or also "
    "heterogeneous latent job opportunities?",
    "How do conclusions differ when welfare evaluates the attained bundle versus the "
    "ex-ante opportunity prospect?",
    "In a restricted P/A/B decomposition, how much welfare inequality is associated "
    "with preferences, local access, and earning opportunities?",
)
# Internal labels: the V15 rendered-text banned list, the DECK-V16 brief's list,
# and the measure names the brief forbids.  (pattern, case-sensitive?)
V16_INTERNAL = [
    (r"\bM08\w*", True), (r"\bS(8|9|10|11|12)\b", True), (r"DECOMP", True),
    (r"POSFIT", True), (r"\bgates?\b", False), (r"\bhash(es)?\b", False),
    (r"\bSHA\b", True), (r"\bSRC\b", True), (r"CLEAN", True),
    (r"criterion-A", False), (r"\bv3b\b", False), (r"\banchor\w*", False),
    (r"\bnodes?\b", False), (r"proposal panel", False), (r"exact-H", False),
    (r"\bH-[FDX]\b", True), (r"\bNN (pricing )?state", True), (r"\bdwt\b", False),
    (r"worktree", False), (r"\bregistry\b", False), (r"\bG1-G9\b", True),
    (r"adjudication", False), (r"\bmissions?\b", False), (r"\brulings?\b", False),
    (r"Mapping-F", False), (r"MECHANICAL_STOCHASTIC", True), (r"\bW1-?F\b", True),
    (r"\bW_?EA\b", True), (r"\bRUM-?[AB]\b", True), (r"BASELINE-F", True),
    (r"\bR240\b", True), (r"\bcommit\b", False), (r"\bRURO\b", True),
    (r"\bmeasure\s+(1|one)\b", False), (r"Haydar\s*[-\u2013]+\s*Maniquet", False),
    (r"\bW1\b", True), (r"\\Wone\b", True), (r"W\^\{?1\}?(?!\d)", True),
]
# The V15 theory caption is used verbatim; it names the companion paper, its
# W^1 notation and a year, which the brief explicitly allows.  It is excised
# (after a verbatim check) before the label and measure-name scans.
V16_ANCHORS = [  # the brief's running order, as headline phrases
    ("real-world inequality", "same income"),
    ("literature gap", "Each ingredient exists"),
    ("research question", "Research question"),
    ("latent-jobs model", "The latent-jobs model"),
    ("welfare: EA", "EA, the opportunity-prospect perspective"),
    ("welfare: ATT", "ATT, the attained-bundle benchmark"),
    ("ATT versus EA", "The two measures answer different welfare questions."),
    ("decomposition", "The decomposition equalises three channels"),
    ("results", "Central result:"),
    ("limitations", "What these results are not."),
    ("conclusion", "Conclusion:"),
]
V16_EQUATIONS = {
    "systematic utility": r"v_i(j)=L_i(j)+\beta_c\log",
    "choice law with opportunity density": r"P_i(j)=\frac{\exp\{v_i(j)\}\,g_i(j)}",
    "attained-bundle welfare": r"M^{\mathrm{att}}_i=C^{\mathrm{obs}}_i\exp",
    "ex-ante welfare": r"M^{\mathrm{EA}}_i=\lambda_c\exp",
    "Shapley": r"\phi^p_k=\sum_{S\subseteq\{P,A,B\}\setminus\{k\}}",
}
V16_REQUIRED = {
    "resources/needs/composition held fixed":
        "Household resources, needs and composition are held fixed in the current decomposition.",
    "access = local access, defined":
        "local unemployment exposure, region, urban or rural location, year",
    "access is not total opportunity": "The access channel is local access, not total opportunity.",
    "preliminary": "The decomposition is preliminary",
    "no causal claim": "makes no causal claim",
    "no parameter uncertainty yet": "No parameter uncertainty yet.",
    "preferences not equated with responsibility":
        "it is not equated with what households are responsible for",
    "two different welfare questions": "The two measures answer different welfare questions.",
}


V16_PROFILE = {
    "tag": "V16",
    "src": V16_SRC, "numbers": V16_NUMBERS, "prov": V16_PROV, "pdf": V16_PDF,
    "text": V16_TEXT, "reh_text": V16_REH_TEXT, "results": V16_RESULTS,
    "lineage": [V16_SRC, HERE / "make_deck_numbers_r6.py", V16_NUMBERS,
                HERE / "build_deck_v16.py"],
    "caption": None,                        # None -> the verbatim V15 caption
    "caption_numbers": {"1", "2026", "3"},
    "caption_reh_end": r"defined in\s*Section 3\.",
    "anchors": V16_ANCHORS, "main_range": (16, 18),
    "required": V16_REQUIRED,
    "central_phrases": ["earning opportunities dominate under ATT",
                        "access dominates under EA for single adults",
                        "couples show no reversal"],
    "primary_phrase": "neither is designated primary",
    "extra_labels": [],
    "style": False,
}

# ==========================================================================
# DECK-V17 profile:  python verify_deck_r6.py --deck v17
#
# The same verifier repointed at the style revision.  Every V16 check runs
# with V17's own titles, required statements and shortened caption; added
# are the style check (frame titles <= 6 words; no body paragraph longer than
# three rendered lines), a caveat-placement check, a backup check and the
# conflict / theory-figure placement checks.  Four negative controls.
# ==========================================================================
V17_SRC = HERE / "JMP_seminar_beamer_v17.tex"
V17_CAPTION = (
    "Own-set equal-consumption equivalents: each individual gets a common consumption on "
    "every job in their own ability set; the level at which the preferred job is indifferent "
    "to the attained bundle is their money metric, comparable across individuals. Adapted "
    "from Haydar and Maniquet (2026), work in progress.")
V17_TITLES = [
    "Motivation", "The conflict", "Research question", "Literature and gap", "Job packages",
    "Opportunities: the choice probability", "Data and EUROMOD", "Estimation", "Welfare",
    "Ex-ante prospect welfare", "Attained-bundle welfare",
    "Inequality and Shapley decomposition", "Results: prospects versus attained outcomes",
    "What is not claimed", "Conclusion",
]
V17_PROFILE = {
    "tag": "V17",
    "src": V17_SRC, "numbers": HERE / "deck_numbers_v17.tex",
    "prov": BUILD / "v17_number_provenance.json",
    "pdf": BUILD / "JMP_seminar_beamer_v17.pdf",
    "text": BUILD / "JMP_seminar_beamer_v17_text.txt",
    "reh_text": BUILD / "JMP_seminar_beamer_v17_rehearsal_text.txt",
    "results": BUILD / "v17_verification.json",
    "lineage": [V17_SRC, HERE / "make_deck_numbers_r6.py", HERE / "deck_numbers_v17.tex",
                HERE / "build_deck_v17.py"],
    "caption": V17_CAPTION,
    "caption_numbers": {"2026"},
    "caption_reh_end": r"work in\s*progress\.",
    "anchors": [(t, t) for t in V17_TITLES], "main_range": (15, 16),
    "required": {
        "resources/needs/composition held fixed":
            "Household resources, needs and composition held fixed",
        "access = local access, defined":
            "local unemployment exposure, region, urban or rural location, year",
        "access is local access, not total opportunity": "local access, not total opportunity",
        "preliminary": "Preliminary decomposition",
        "not causal": "Not causal",
        "no parameter uncertainty yet": "No parameter uncertainty yet",
        "preferences not equated with responsibility": "Preferences are not responsibility",
        "prospects versus attained outcomes": "prospects versus attained outcomes",
        "two different welfare questions": "two different welfare questions",
    },
    "central_phrases": ["prospects versus attained outcomes", "no reversal",
                        "single adults: access $>$ earnings", "earnings $>$ access"],
    "primary_phrase": "neither perspective is designated primary",
    "extra_labels": [(r"\b[vV]\d{1,2}\b", True), (r"\bfrozen\b", False),
                     (r"\baccepted\b", False), (r"\bSection\s+\d", False)],
    "style": True,
}


def split_appendix(src: str) -> tuple[str, str]:
    """Split at a real \\appendix command line, never at a mention in a comment."""
    parts = re.split(r"(?m)^[ \t]*\\appendix[ \t]*$", src, maxsplit=1)
    return (parts[0], parts[1]) if len(parts) == 2 else (src, "")


def _title_words(title: str) -> int:
    t = re.sub(r"\$[^$]*\$", " x ", title)
    t = re.sub(r"\\[A-Za-z]+\*?", " ", t).replace("{", " ").replace("}", " ")
    return len([w for w in t.split() if re.search(r"[A-Za-z0-9]", w)])


def frame_titles(src: str) -> list[str]:
    body = src.split(r"\begin{document}", 1)[-1]
    return [flat(m.group(2)) for m in re.finditer(
        r"\\(frametitle|headlineframe)\{((?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*)\}", body)]


_MATH_FONTS = ("CMMI", "CMSY", "CMEX", "MSBM", "CMR")


def paragraph_violations(pdf: Path, skip_pages: set[int], max_lines: int = 3) -> list[str]:
    """Rendered-body paragraphs longer than max_lines.

    A paragraph is a PyMuPDF text block, minus the frame-title band, the
    footline, display-math lines (math fonts dominate, fewer than three prose
    words) and table blocks (any baseline carrying three or more separate text
    runs).  Consecutive baselines more than 2.2 font sizes apart split a block.
    """
    import pymupdf
    out = []
    doc = pymupdf.open(pdf)
    for pno, page in enumerate(doc, 1):
        if pno in skip_pages:
            continue
        height = page.rect.height
        for block in page.get_text("dict")["blocks"]:
            if block.get("type") != 0:
                continue
            lines = []
            cells: dict = {}
            for ln in block["lines"]:
                spans = [s for s in ln["spans"] if s["text"].strip()]
                if spans:
                    y0 = spans[0]["origin"][1]
                    key0 = next((k for k in cells if abs(k - y0) <= 2), y0)
                    size0 = max(s["size"] for s in spans)
                    cells[key0] = cells.get(key0, 0) + 1 + sum(
                        1 for a, b in zip(spans, spans[1:]) if b["bbox"][0] - a["bbox"][2] > 2.5 * size0)
            if any(n >= 3 for n in cells.values()):
                continue                         # a table: some baseline carries three or more cells
            for ln in block["lines"]:
                spans = [s for s in ln["spans"] if s["text"].strip()]
                if not spans:
                    continue
                y = spans[0]["origin"][1]
                if y < 0.11 * height or y > 0.92 * height:
                    continue
                prose = sum(len(re.findall(r"[A-Za-z]{3,}", s["text"])) for s in spans
                            if not s["font"].startswith(_MATH_FONTS) and "SSI" not in s["font"])
                mathy = any(s["font"].startswith(_MATH_FONTS) or "SSI" in s["font"]
                            for s in spans)
                if mathy and prose < 3:
                    continue
                size = max(s["size"] for s in spans)
                runs = 1 + sum(1 for a, b in zip(spans, spans[1:])
                               if b["bbox"][0] - a["bbox"][2] > 2.5 * size)
                lines.append((y, size, " ".join(s["text"] for s in spans), "BX" in spans[0]["font"],
                              runs))
            if not lines:
                continue
            rows: dict = {}
            for y, size, text, bold, runs in lines:
                key = next((k for k in rows if abs(k - y) <= 2), y)
                rows.setdefault(key, []).append((size, text, bold, runs))
            if any(sum(r[3] for r in v) >= 3 for v in rows.values()):
                continue                         # a table row
            ys = sorted(rows)
            para = [ys[0]]
            for prev, cur in zip(ys, ys[1:]):
                size = max(r[0] for r in rows[cur])
                restyled = (abs(size - max(r[0] for r in rows[prev])) > 0.6
                            or rows[cur][0][2] != rows[prev][0][2])
                if cur - prev > 2.2 * size or restyled:
                    para = [cur]
                else:
                    para.append(cur)
                if len(para) > max_lines:
                    first = " ".join(r[1] for r in rows[para[0]])[:60]
                    out.append("page %d: %d+ lines from %r" % (pno, len(para), first))
                    break
    return out


def style_violations(src: str, pdf: Path, max_words: int = 6) -> tuple[list, list]:
    long_titles = ["%r (%d words)" % (t, _title_words(t)) for t in frame_titles(src)
                   if _title_words(t) > max_words]
    fr = frames(src)
    skip = {i for i, f in enumerate(fr, 1) if r"\titlepage" in f}
    return long_titles, paragraph_violations(pdf, skip)


def _norm(s: str) -> str:
    import unicodedata
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("\u2019", "'").replace("\u2013", "--").replace("\u2212", "-")
    s = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1-\2", s)
    return flat(s)


def _strip_comments(s: str) -> str:
    return re.sub(r"(?m)(?<!\\)%.*$", "", s)


def _images_in(html: Path) -> set[str]:
    import base64
    import hashlib
    text = html.read_text(encoding="utf-8")
    return {hashlib.sha256(base64.b64decode(m)).hexdigest()
            for m in re.findall(r"data:image/png;base64,([A-Za-z0-9+/=]+)", text)}


def v16_gates(src: str, pages: list[str], reh_text: str, P: dict | None = None) -> tuple[list, list, dict]:
    P = V16_PROFILE if P is None else P
    T = "G-" + P["tag"]
    import hashlib
    sys.path.insert(0, str(HERE))
    sys.path.insert(0, str(HERE.parent / "reports" / "research_story_build"))
    import make_deck_numbers_r6 as numsrc  # noqa: E402
    import v15_render_inputs as v15  # noqa: E402

    ok_l: list[str] = []
    bad_l: list[str] = []
    detail: dict = {}

    def g(name: str, ok: bool, msg: str) -> None:
        (ok_l if ok else bad_l).append("%-18s %s" % (name, msg))
        detail[name] = {"pass": bool(ok), "detail": msg}

    body = src.split(r"\begin{document}", 1)[1]
    fr = frames(src)
    proj = "\n".join(pages)
    proj_n = _norm(proj)

    # ------------------------------------------------ carried over from R6
    haystack = (src + "\n" + proj + "\n" + reh_text).lower()
    hits = ["%s (%s)" % (t, w) for t, w in RETIRED_TOKENS.items() if t.lower() in haystack]
    g("G-RETIRE", not hits, "no retired magnitude or out-of-scope token in source, "
      "slides or notes" if not hits else "RETIRED MATERIAL PRESENT: " + "; ".join(hits))
    ban = [t for t in OUT_OF_SCOPE_TOKENS if t.lower() in haystack]
    g("G-NOBAN", not ban, "no seminar-freeze out-of-scope token"
      if not ban else "OUT-OF-SCOPE TOKENS PRESENT: " + ", ".join(ban))

    # typed numerals: slides AND notes; dimensions and the verbatim caption removed
    caption_src = v15.THEORY_CAPTION if P["caption"] is None else P["caption"]
    cap_present = flat(caption_src) in flat(body)
    scan = _strip_comments(body)
    if cap_present:
        scan = flat(scan).replace(flat(caption_src), " ")
    scan = re.sub(r"\\renewcommand\{\\arraystretch\}\{[\d.]+\}", "", scan)
    scan = re.sub(r"\d*\.?\d+\s*(em|ex|pt|mm|cm|\\textwidth|\\textheight|\\paperwidth|\\linewidth)",
                  "", scan)
    scan = re.sub(r"\\(includegraphics|graphicspath|input)(\[[^\]]*\])?\{[^}]*\}", "", scan)
    scan = re.sub(r"\\multicolumn\{\d+\}", r"\\multicolumn{}", scan)
    scan = re.sub(r"_\{?0\}?(?![0-9.])", "_", scan)   # a zero subscript names a symbol (I_0), not a value
    for literal in P.get("literals", []):       # an event name on the title slide, not a value
        scan = scan.replace(literal, " ")
    typed = {m.group(0) for m in re.finditer(r"(?<![\\A-Za-z0-9])\d+(?:\.\d+)?", scan)}
    typed -= {"1", "3"}          # the Shapley weight |S|!(3-|S|-1)!/3!
    g("G-NUMBERS", not typed, "no hand-typed numeral on any slide or note "
      "(Shapley-weight integers and the theory-figure caption excepted)"
      if not typed else "hand-typed numerals: " + ", ".join(sorted(typed)))

    # assets: every included image is byte-identical to an image embedded in V15
    v15_imgs = _images_in(V15_REPORT) | _images_in(V15_GALLERY)
    gp = re.search(r"\\graphicspath\{((?:\{[^}]*\})+)\}", src)
    dirs = [HERE / d for d in re.findall(r"\{([^{}]*)\}", gp.group(1))] if gp else []
    refs = re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", body)
    unresolved, not_v15, used = [], [], []
    for name in refs:
        hit = next((d / name for d in dirs if (d / name).is_file()), None)
        if hit is None:
            unresolved.append(name)
            continue
        used.append(hit.name)
        if hashlib.sha256(hit.read_bytes()).hexdigest() not in v15_imgs:
            not_v15.append(name)
    banned_tree = [t for t in ("_retired_assets", "mock_presentation", "Presentation_mock")
                   if t in src]
    g("G-ASSETS", bool(refs) and not unresolved and not not_v15 and not banned_tree,
      "%d figure(s) %s, each byte-identical to an image embedded in the V15 report/gallery"
      % (len(refs), used) if refs and not unresolved and not not_v15 and not banned_tree
      else "VIOLATION: unresolved %s; not a V15 image %s; banned tree %s"
           % (unresolved, not_v15, banned_tree))

    lin = rlg.scan_files([p for p in P["lineage"] if p.exists()])
    g("G-LINEAGE", not lin, "no retired-lineage artifact referenced by path"
      if not lin else "RETIRED-LINEAGE PATH READ: " + rlg.format_violations(lin, REPO))

    conf = [w for w in ("confusion matrix", "balanced accuracy", "specificity",
                        "true positive", "false positive", "recall rate") if w in proj.lower()]
    g("G-NOCONF", not conf, "no confusion-matrix statistic" if not conf
      else "confusion-matrix language: " + ", ".join(conf))
    g("G-POOLED", "pooled" not in proj.lower(), "no pooled figure")

    prov = json.loads(P["prov"].read_text(encoding="utf-8"))["macros"]
    eur = {m for m, v in prov.items() if "EUR" in str(v.get("units"))}
    mixed = [i + 1 for i, f in enumerate(fr)
             if any(("\\" + m) in f and m.endswith(("Singles", "Sing")) for m in eur)
             and any(("\\" + m) in f and m.endswith(("Couples", "Coup")) for m in eur)]
    near = [p for p in ("near equality", "nearly equal") if p in haystack]
    g("G-NOSIDEBYSIDE", not mixed and not near,
      "no frame sets singles and couples euro welfare levels side by side"
      if not mixed and not near else "VIOLATION frames %s near-equality %s" % (mixed, near))

    # ------------------------------------------------ G-REGISTRY
    registry = json.loads(numsrc.V15_REGISTRY.read_text(encoding="utf-8"))["entries"]
    if P.get("rebuild"):
        rebuilt = getattr(numsrc, P["rebuild"])()
        stale = sorted(m for m in set(prov) | set(rebuilt)
                       if rebuilt.get(m, {}).get("rendered") != prov.get(m, {}).get("rendered"))
    else:
        stale = [m for m, v in prov.items()
                 if v["key"] not in registry
                 or numsrc.v16_render(registry[v["key"]]["value"], v["format"]) != v["rendered"]]
    numtex = P["numbers"].read_text(encoding="utf-8")
    tex_macros = dict(re.findall(r"\\newcommand\{\\(\w+)\}\{(.*)\}", numtex))
    drift = [m for m, v in prov.items() if tex_macros.get(m) != v["rendered"]]
    unresolved_nums = []
    if len(pages) != len(fr):
        unresolved_nums.append("page/frame count mismatch %d vs %d" % (len(pages), len(fr)))
    for i, (f, page) in enumerate(zip(fr, pages), 1):
        allowed = set()
        for m in prov:
            if re.search(r"\\%s(?![A-Za-z])" % m, f):
                rendered = prov[m]["rendered"].replace("$-$", "-")
                allowed.add(rendered.lstrip("-"))
                allowed |= {t.lstrip("-").rstrip(",") for t in re.findall(
                    r"(?<![\w.,])-?\d[\d,]*(?:\.\d+)?(?![\w])", rendered)}
        if r"\begin{enumerate}" in f:
            allowed |= {"1", "2", "3"}
        if "3!" in f:
            allowed |= {"1", "3"}
        text = page
        if flat(caption_src) in flat(f):
            allowed |= P["caption_numbers"]     # the theory-figure caption only
        counters = {len(fr), len(frames(split_appendix(src)[0])), len(frames(split_appendix(src)[0])) - 1}
        text = re.sub(r"(?<![\d.])(\d{1,2})\s*/\s*(\d{1,2})(?![\d.])",
                      lambda mm: " " if int(mm.group(2)) in counters else mm.group(0), text)  # footline counter
        allowed |= {dg for dg in ("1", "3") if re.search(r"\$[^$]*(?<![\\A-Za-z0-9.])%s(?![0-9.])[^$]*\$" % dg, f)}
        for m in re.finditer(r"(?<![\w.,])-?\d[\d,]*(?:\.\d+)?(?![\w])", _norm(text)):
            tok = m.group(0).lstrip("-").rstrip(",")
            if tok not in allowed:
                unresolved_nums.append("page %d: %s" % (i, tok))
    g("G-REGISTRY", not stale and not drift and not unresolved_nums,
      "every numeral on all %d slide pages resolves, through the macros its frame uses, to a "
      "V15-registry entry re-read and re-formatted now (%d macros)" % (len(pages), len(prov))
      if not stale and not drift and not unresolved_nums
      else "stale macros %s; tex drift %s; unresolved %s" % (stale, drift, unresolved_nums[:12]))

    # ------------------------------------------------ V16 content gates
    main_fr = frames(split_appendix(src)[0])
    n = len(main_fr)
    lo, hi = P["main_range"]
    positions = [(lab, proj_n.find(_norm(a))) for lab, a in P["anchors"]]
    ordered = all(p >= 0 for _, p in positions) and \
        [p for _, p in positions] == sorted(p for _, p in positions)
    g(T + "-STRUCTURE", lo <= n <= hi and len(pages) == len(fr) and ordered,
      "%d main slides (%d-%d), %d pages match %d frames, running order %s"
      % (n, lo, hi, len(pages), len(fr), " -> ".join(l for l, _ in positions))
      if lo <= n <= hi and len(pages) == len(fr) and ordered
      else "count %d pages %d order %s" % (n, len(pages), positions))

    rq_ok = all(_norm(q) in proj_n for q in (V16_RQ,) + V16_SUBQ)
    g(T + "-RQ", rq_ok, "research question and three subquestions rendered verbatim"
      if rq_ok else "research question or a subquestion not verbatim on a slide")

    eqs = re.findall(r"\\slideeq\{", body)
    other_display = [m.group(0) for m in re.finditer(r"(?<!\\)\\\[|\$\$|\\begin\{(?:equation|align|multline|eqnarray)", body)]
    sig_miss = [k for k, s in V16_EQUATIONS.items() if flat(s) not in flat(body)]
    eq_frames = [f for f in fr if r"\slideeq{" in f]
    notes_ok = all(re.search(r"\\note\{\s*In words:", f) for f in eq_frames)
    g(T + "-EQUATIONS", len(eqs) == 5 and not other_display and not sig_miss and notes_ok,
      "exactly five displayed equations (%s), each frame's note opens with a spoken "
      "interpretation line" % ", ".join(V16_EQUATIONS)
      if len(eqs) == 5 and not other_display and not sig_miss and notes_ok
      else "count %d, other display %s, missing %s, notes %s"
           % (len(eqs), other_display, sig_miss, notes_ok))

    central = [f for f in fr if P.get("central_marker", "fig_v13_central_result.png") in f]
    cf = flat(central[0]) if len(central) == 1 else ""
    central_ok = (len(central) == 1 and "fig_v13_central_result.png" in used
                  and "fig_v13_central_result.png" not in not_v15
                  and all(ph in cf for ph in P["central_phrases"]))
    g(T + "-CENTRAL", central_ok, "one central-result slide reuses the V15 ATT-versus-EA "
      "figure unchanged and states the reversal for single adults, none for couples"
      if central_ok else "central-result slide missing, altered or mis-worded")

    import pymupdf
    reading = _norm(" ".join(pg.get_text() for pg in pymupdf.open(P["pdf"]))).lower() \
        if P["pdf"].exists() else ""
    miss = [k for k, s in P["required"].items()
            if _norm(s).lower() not in proj_n.lower() and _norm(s).lower() not in reading]
    g(T + "-REQUIRED", not miss, "required statements rendered on slides: " + "; ".join(P["required"])
      if not miss else "missing on slides: " + ", ".join(miss))

    notes_all = " ".join(re.findall(r"\\note\{(.*?)\}\s*\\end\{frame\}", body, re.S))
    sentences = re.split(r"(?<=[.;:?])\s+", _norm(proj) + " " + flat(notes_all))
    prim = [s for s in sentences if re.search(r"\b(primary|preferred measure|headline measure|"
                                              r"main measure|main welfare measure)\b", s, re.I)
            and not re.search(r"\b(neither|not|no)\b", s, re.I)]
    ea_rank = re.findall(r"EA[^.]{0,60}\b(is|as) (the )?(primary|preferred|main|headline|better|"
                         r"correct)\b", _norm(proj) + flat(notes_all))
    g(T + "-NOPRIMARY", not prim and not ea_rank and P["primary_phrase"] in proj_n.lower(),
      "EA foregrounded without being called the primary measure; slides say neither is designated primary"
      if not prim and not ea_rank else "primacy wording: %s %s" % (prim[:3], ea_rank))

    cap_ok = cap_present and "Haydar and Maniquet" in flat(caption_src) and \
        (P["caption"] is None or "Section" not in caption_src)
    g(T + "-CAPTION", cap_ok, "theory figure carries its caption verbatim (companion-paper attribution kept)"
      if cap_ok else "theory caption missing or altered")

    lab_src = _strip_comments(body)
    lab_src = re.sub(r"\\(includegraphics|graphicspath|input)(\[[^\]]*\])?\{[^}]*\}", "", lab_src)
    lab_src = flat(lab_src).replace(flat(caption_src), " ")
    lab_proj = _norm(proj)
    cap_render = [p for p in pages if "Own-set equal-consumption equivalents" in p]
    for p in cap_render:   # excise the caption block on its page only
        lab_proj = lab_proj.replace(_norm(p), _norm(p.split("Own-set equal-consumption")[0]))
    lab_reh = _norm(reh_text)
    lab_reh = re.sub(r"Own-set equal-consumption equivalents.*?" + P["caption_reh_end"], " ",
                     lab_reh, flags=re.S)
    lab_hits = []
    for pat, cs in V16_INTERNAL + P["extra_labels"]:
        rx = re.compile(pat, 0 if cs else re.I)
        for where, hay in (("source", lab_src), ("slides", lab_proj), ("notes", lab_reh)):
            m = rx.search(hay)
            if m:
                lab_hits.append("%s in %s" % (m.group(0), where))
    g(T + "-LABELS", not lab_hits, "no internal label or forbidden measure name in source, "
      "slides or notes (%d patterns)" % (len(V16_INTERNAL) + len(P["extra_labels"]))
      if not lab_hits else "INTERNAL LABELS: " + "; ".join(lab_hits))

    if P.get("high_share_context"):
        # a share in [80, 100] is a violation when its line talks about opportunities,
        # unless the line is the unallocated remainder, a total or a fit accuracy
        high = []
        for line in (proj + "\n" + reh_text).splitlines():
            ln = _norm(line).lower()
            for m in re.finditer(r"(\d+(?:\.\d+)?)\s*(%|per ?cent)", ln):
                if (80 <= float(m.group(1)) <= 100
                        and re.search(r"opportunit|access|earning|\bjob", ln)
                        and not re.search(r"not allocated|accuracy|\btotal\b", ln)):
                    high.append(line.strip()[:90])
    else:
        high = [m.group(0) for m in re.finditer(r"(\d+(?:\.\d+)?)\s*(%|\\%|per ?cent)",
                                                _norm(proj + reh_text) + " " + flat(src))
                if 80 <= float(m.group(1)) <= 100]
    words = re.findall(r"\b(eighty|ninety|near(ly)? 90|80\s*(-|--|to)\s*90)\b",
                       (proj + reh_text + src).lower())
    g(T + "-NO8090", not high and not words, "no 80-90% opportunity claim anywhere"
      if not high and not words else "high-share claim: %s %s" % (high, words))

    return ok_l, bad_l, detail


def v17_extra_gates(src: str, pdf: Path, tag: str = "V17",
                    table_macros: tuple = ("VEASingPhiARaw", "VAttSingPhiARaw"),
                    welfare_title: str = "Welfare") -> tuple[list, list, dict]:
    """Style-revision checks that only the V17 profile carries."""
    ok_l: list[str] = []
    bad_l: list[str] = []
    detail: dict = {}

    def g(name: str, ok: bool, msg: str) -> None:
        (ok_l if ok else bad_l).append("%-18s %s" % (name, msg))
        detail[name] = {"pass": bool(ok), "detail": msg}

    long_titles, long_paras = style_violations(src, pdf)
    n_titles = len(frame_titles(src))
    g("G-" + tag + "-STYLE", not long_titles and not long_paras,
      "%d frame titles all <= 6 words; no rendered body paragraph longer than 3 lines"
      % n_titles if not long_titles and not long_paras
      else "long titles %s; long paragraphs %s" % (long_titles, long_paras[:8]))

    main_src, backup_src = split_appendix(src)
    main_fr = frames(main_src)
    limits = [f for f in main_fr if r"\frametitle{What is not claimed}" in f]
    scattered = [i + 1 for i, f in enumerate(main_fr)
                 if f not in limits and re.search(r"\\caveat\{|deepred", re.sub(
                     r"\{\\color\{deepred\}\\rule\{[^}]*\}\{[^}]*\}\}", "",   # a decorative rule is not text
                     re.sub(r"\\note\{.*", "", f, flags=re.S)))]
    g("G-" + tag + "-CAVEATS", len(limits) == 1 and not scattered,
      "caveats on one dedicated slide only; no red caveat text on any other main slide"
      if len(limits) == 1 and not scattered else "caveat text on main frames %s" % scattered)

    conclusion_ix = main_src.find(r"\frametitle{Conclusion}")
    tables_main = [m for m in table_macros if "\\" + m in main_src]
    tables_backup = all("\\" + m in backup_src for m in table_macros)
    g("G-" + tag + "-BACKUP", conclusion_ix != -1 and not tables_main and tables_backup
      and len(frames(backup_src)) >= 2,
      "EA and ATT results tables are backup slides after the conclusion (%d backup slides)"
      % len(frames(backup_src)) if not tables_main and tables_backup
      else "results tables in main deck %s or missing from backup" % tables_main)

    titles = [flat(t) for t in frame_titles(main_src)]
    conflict = next((f for f in main_fr if r"\frametitle{The conflict}" in f), "")
    conflict_ok = (len(titles) > 1 and titles[1] == "The conflict"
                   and titles.index("The conflict") < titles.index("Data and EUROMOD")
                   and all(k in conflict for k in ("Compensation", "Responsibility", r"\nexists",
                                                    r"Fleurbaey \& Maniquet")))
    g("G-" + tag + "-CONFLICT", conflict_ok,
      "compensation-versus-responsibility conflict is slide 3, before the data, with the "
      "impossibility and the Fleurbaey-Maniquet citation"
      if conflict_ok else "conflict slide missing, late or incomplete")

    welfare = next((f for f in main_fr if r"\frametitle{%s}" % welfare_title in f), "")
    theory_ok = "theory_w1.png" in welfare and "theory_w1.png" not in backup_src \
        and "Section" not in welfare.split(r"\note{")[0]
    g("G-" + tag + "-THEORYFIG", theory_ok,
      "theory figure is the main 'Welfare' slide, with a slide caption that drops the section reference"
      if theory_ok else "theory figure not central, or caption still names a section")
    return ok_l, bad_l, detail


# ==========================================================================
# DECK-V18 profile:  python verify_deck_r6.py --deck v18
#
# Every V17 check and control, repointed.  Added: the mixed-denominator check,
# the hyperlink check (source targets and resolved destinations in the compiled
# PDF), the 100%-of-baseline display, the cross-check against the manager's
# verification of the shares, the title slide, the selected-estimates slide,
# no causal language, no elasticity, and the appendix structure.
# ==========================================================================
V18_SRC = HERE / "JMP_seminar_beamer_v18.tex"
V18_TITLES = [
    "Motivation", "The conflict", "Research question", "Literature and gap", "Job packages",
    "Opportunities: the choice probability", "Data and EUROMOD", "Estimation",
    "Selected estimates", "Welfare", "Ex-ante prospect welfare", "Attained-bundle welfare",
    "Inequality and Shapley decomposition", "How much is associated with opportunities?",
    "Which opportunity channel matters?", "Where does baseline inequality go?",
    "What is not claimed", "Conclusion",
]
V18_PROFILE = dict(V17_PROFILE, **{
    "tag": "V18",
    "src": V18_SRC, "numbers": HERE / "deck_numbers_v18.tex",
    "prov": BUILD / "v18_number_provenance.json",
    "pdf": BUILD / "JMP_seminar_beamer_v18.pdf",
    "text": BUILD / "JMP_seminar_beamer_v18_text.txt",
    "reh_text": BUILD / "JMP_seminar_beamer_v18_rehearsal_text.txt",
    "results": BUILD / "v18_verification.json",
    "lineage": [V18_SRC, HERE / "make_deck_numbers_r6.py", HERE / "deck_numbers_v18.tex",
                HERE / "build_deck_v18.py"],
    "anchors": [(t, t) for t in V18_TITLES], "main_range": (17, 19),
    "required": {
        "resources/needs/composition held fixed":
            "Household resources, needs and composition held fixed",
        "access = local access, defined":
            "local unemployment exposure, region, urban or rural location, year",
        "access is local access, not total opportunity": "local access, not total opportunity",
        "preliminary": "Preliminary decomposition",
        "not causal": "Not causal",
        "no parameter uncertainty yet": "No parameter uncertainty yet",
        "preferences not equated with responsibility": "Preferences are not responsibility",
        "prospects versus attained outcomes": "prospects versus attained outcomes",
        "two different welfare questions": "two different welfare questions",
        "neither perspective primary": "Neither perspective is designated primary",
        "A is the local-access channel": "A is the currently estimated local-access channel",
        "2x2 label": "A + B as % of the relevant baseline Gini",
        "100% display denominator label": "shares of baseline Gini",
        "X2: remainder label": "Not allocated by this exercise",
        "X2: sex blocks retained": "retains sex-specific preference and opportunity blocks",
        "X2: luck and spread excluded": "wage-draw luck and the common offer spread",
        "X1: A + B alone": "A + B alone",
    },
    "central_marker": r"\hypertarget{main:howmuch}",
    "central_phrases": ["Ex-ante prospect", "Attained bundle",
                        r"A + B as \% of the relevant baseline Gini",
                        r"\VEASingOppEq", r"\VEACoupOppEq", r"\VAttSingOppEq", r"\VAttCoupOppEq"],
    "rebuild": "build_v18",
    "literals": ["4th-Year PhD Workshop"],
    "high_share_context": True,
    "table_macros": ("VEASingPhiARaw", "VAttFigSingPhiARaw"),
    "v18": True,
})

BASE_RX = re.compile(r"baseline gini|of baseline|% of i ?0|shares? of baseline", re.I)
EXPL_RX = re.compile(r"explained (p/a/b )?(component|change)|shares? of (the )?(currently )?explained", re.I)
GOAL1 = {  # the manager's Goal 1 verification (computed from displayed, rounded inputs)
    "Sing": {"P": 0.14, "A": 15.53, "B": 4.79, "sum": 20.46, "rest": 79.54,
             "sP": 0.7, "sA": 75.9, "sB": 23.4},
    "Coup": {"P": -1.77, "A": 3.74, "B": 4.20, "sum": 6.17, "rest": 93.83,
             "sP": -28.6, "sA": 60.6, "sB": 68.0},
}
RULING_ESTIMATES = {  # the values the V18 ruling quotes for the selected-estimates slide
    "VCoefSingBetaC": "2.0387", "VCoefSingBetaCSE": "0.2917",
    "VCoefCoupBetaC": "2.1017", "VCoefCoupBetaCSE": "0.2939",
    "VCoefSingBetaEGsur": "$-$1.4422", "VCoefSingBetaEGsurSE": "0.2356",
    "VCoefCoupBetaEGsur": "$-$1.1924", "VCoefCoupBetaEGsurSE": "0.1557",
    "VCoefSingBetaWEducH": "0.1491", "VCoefSingBetaWEducHSE": "0.0308",
    "VCoefCoupBetaWEducH": "0.1817", "VCoefCoupBetaWEducHSE": "0.0197",
    "VCoefSingSigma": "0.3815", "VCoefSingSigmaSE": "0.0133",
    "VCoefCoupSigma": "0.3631", "VCoefCoupSigmaSE": "0.0072",
}
TITLE_LINES = ["Unequal Job Opportunities and Well-Being Inequality",
               "A Latent-Jobs Structural Decomposition", "Hisham Haydar",
               "University of Luxembourg & LISER", "4th-Year PhD Workshop",
               "Discussant: Sebastian Dobre"]


def _slide_part(frame: str) -> str:
    return re.sub(r"\\note\{.*", "", frame, flags=re.S)


def denominator_mixes(src: str, pages: list[str]) -> list[str]:
    hits = []
    for i, page in enumerate(pages, 1):
        t = _norm(page)
        if BASE_RX.search(t) and EXPL_RX.search(t):
            hits.append("page %d" % i)
    body = src.split(r"\begin{document}", 1)[-1]
    for i, f in enumerate(frames(body), 1):
        slide = flat(_slide_part(f)).replace(r"\%", "%").replace("$I_0$", "I0")
        if BASE_RX.search(slide) and EXPL_RX.search(slide):
            hits.append("frame %d source" % i)
        note = re.search(r"\\note\{(.*)\}\s*$", f, re.S)
        for sentence in re.split(r"(?<=[.;?!])\s+", flat(note.group(1)) if note else ""):
            if BASE_RX.search(sentence) and EXPL_RX.search(sentence):
                hits.append("frame %d note: %s" % (i, sentence[:70]))
    return hits


def link_problems(src: str, pdf: Path) -> tuple[list, dict]:
    import pymupdf
    body = src.split(r"\begin{document}", 1)[-1]
    targets = set(re.findall(r"\\hypertarget\{([^}]+)\}", body))
    used = re.findall(r"\\(?:hyperlink|golink|maplink|backnav)\{([^}]+)\}", body)
    problems = ["missing target %s" % t for t in sorted(set(used) - targets)]
    main_src, backup_src = split_appendix(src)
    backups = frames(backup_src)
    appmap = [f for f in backups if r"\hypertarget{appmap}" in f]
    others = [f for f in backups if r"\hypertarget{appmap}" not in f]
    no_nav = [re.search(r"\\hypertarget\{([^}]+)\}", f).group(1) for f in others
              if not (r"\backnav{" in f or (r"\beamerreturnbutton{Back}" in f and "{appmap}" in f))]
    problems += ["backup without Back/Appendix map: %s" % t for t in no_nav]
    backup_targets = {re.search(r"\\hypertarget\{([^}]+)\}", f).group(1) for f in others}
    mapped = set(re.findall(r"\\maplink\{([^}]+)\}", appmap[0])) if len(appmap) == 1 else set()
    problems += ["backup not on the appendix map: %s" % t for t in sorted(backup_targets - mapped)]
    if len(appmap) != 1:
        problems.append("appendix map missing")
    stats = {"source_links": len(used), "targets": len(targets), "backups": len(others),
             "main_slides_with_buttons": sum(r"\cornerlinks{" in f for f in frames(main_src))}
    if pdf.exists():
        doc = pymupdf.open(pdf)
        names = doc.resolve_names() if hasattr(doc, "resolve_names") else {}
        internal = broken = 0
        for page in doc:
            for link in page.get_links():
                kind = link.get("kind")
                if kind == pymupdf.LINK_URI:
                    continue
                internal += 1
                ok = False
                if kind == pymupdf.LINK_GOTO:
                    ok = 0 <= link.get("page", -1) < len(doc)
                elif kind == pymupdf.LINK_NAMED:
                    dest = link.get("nameddest") or link.get("name")
                    ok = (0 <= link.get("page", -1) < len(doc)
                          or (dest in names and 0 <= names[dest].get("page", -1) < len(doc)))
                if not ok:
                    broken += 1
        stats.update({"pdf_internal_links": internal, "pdf_broken_links": broken})
        if broken:
            problems.append("%d PDF links do not resolve" % broken)
        if internal < len(used):
            problems.append("PDF has %d internal links for %d in the source" % (internal, len(used)))
    else:
        problems.append("compiled PDF missing")
    return problems, stats


def v18_gates(src: str, pages: list[str], reh: str, P: dict) -> tuple[list, list, dict]:
    import pymupdf
    ok_l: list[str] = []
    bad_l: list[str] = []
    detail: dict = {}

    def g(name: str, ok: bool, msg: str) -> None:
        (ok_l if ok else bad_l).append("%-18s %s" % (name, msg))
        detail[name] = {"pass": bool(ok), "detail": msg}

    prov = json.loads(P["prov"].read_text(encoding="utf-8"))["macros"]
    body = src.split(r"\begin{document}", 1)[-1]
    main_src, backup_src = split_appendix(src)
    main_fr = frames(main_src)

    def frame_with(target: str) -> str:
        return next((f for f in frames(body) if r"\hypertarget{%s}" % target in f), "")

    mixes = denominator_mixes(src, pages)
    g("G-" + P["tag"] + "-DENOMINATORS", not mixes,
      "no slide, frame or note sentence mixes shares of baseline Gini with shares of the explained change"
      if not mixes else "MIXED DENOMINATORS: %s" % mixes[:6])

    problems, stats = link_problems(src, P["pdf"])
    g("G-" + P["tag"] + "-LINKS", not problems,
      "%d source links to %d targets; %d internal links in the PDF, %d unresolved; every backup "
      "has Back and Appendix map; every backup is on the map; %d main slides carry buttons"
      % (stats["source_links"], stats["targets"], stats.get("pdf_internal_links", 0),
         stats.get("pdf_broken_links", 0), stats["main_slides_with_buttons"])
      if not problems else "LINK PROBLEMS: %s" % problems[:8])
    detail["G-" + P["tag"] + "-LINKS"]["stats"] = stats

    hundred = frame_with("main:hundred")
    slide = flat(_slide_part(hundred))
    sums = {}
    arith_ok = True
    for pop in ("Sing", "Coup"):
        num = lambda n: float(prov[n]["rendered"].replace("$-$", "-"))
        rows = [num("VHundred%s%s" % (pop, k)) for k in ("P", "A", "B", "Rest")]
        sums[pop] = rows
        arith_ok &= (round(sum(rows), 6) == 100.0 and prov["VHundred%sTotal" % pop]["rendered"] == "100.0"
                     and prov["VHundred%sAB" % pop]["rendered"] == prov["VEA%sOppEq" % pop]["rendered"]
                     and round(num("VHundred%sExplained" % pop), 6) == round(sum(rows[:3]), 6))
    phrases = P.get("hundred_phrases") or ["Not allocated by this exercise", r"1-(\phi_P+\phi_A+\phi_B)/I_0", "A + B alone",
               "holds household resources, needs and composition fixed", "sex-specific",
               "wage-draw luck and the common offer spread", "shares of baseline Gini",
               r"A $=$ current local-access channel", r"\VHundredCoupP"]
    missing = [ph for ph in phrases if ph not in slide]
    negative = prov["VHundredCoupP"]["raw"] < 0 and "$-$" in prov["VHundredCoupP"]["rendered"]
    table = r"\begin{tabular}" in slide and r"\includegraphics" not in slide
    g("G-" + P["tag"] + "-HUNDRED", arith_ok and not missing and negative and table,
      "rows close to 100.0 for both populations (singles %s, couples %s); A + B rows equal the "
      "headline; couples' negative preference row shown; remainder labelled not allocated, with its "
      "qualification on the slide; couples shown as a table" % (sums["Sing"], sums["Coup"])
      if arith_ok and not missing and negative and table
      else "arithmetic %s missing %s negative %s table %s" % (arith_ok, missing, negative, table))

    diffs = {}
    worst = 0.0
    for pop, ref in GOAL1.items():
        exact = {k: prov["VPctEA%s%sEq" % (pop, k)]["raw"] for k in "PAB"}
        exact["sum"] = exact["P"] + exact["A"] + exact["B"]
        exact["rest"] = 100.0 - exact["sum"]
        for k in "PAB":
            exact["s" + k] = prov["VExpl%s%s" % (pop, k)]["raw"]
        for k, v in ref.items():
            d = abs(exact[k] - v)
            diffs["%s.%s" % (pop, k)] = {"exact": round(exact[k], 4), "goal1": v, "abs_diff": round(d, 4)}
            worst = max(worst, d / (0.1 if k.startswith("s") else 0.02))
    g("G-" + P["tag"] + "-GOAL1", worst <= 1.0,
      "registry-derived shares agree with the Goal 1 verification within rounding of its inputs "
      "(baseline shares within 0.02 pp, explained shares within 0.1)"
      if worst <= 1.0 else "disagreement with Goal 1 verification: %s" % diffs)
    detail["G-" + P["tag"] + "-GOAL1"]["differences"] = diffs

    page1 = _norm(pages[0]) if pages else ""
    title_missing = [ln for ln in TITLE_LINES if _norm(ln) not in page1]
    sparse = len(page1.split()) <= 40
    g("G-" + P["tag"] + "-TITLE", not title_missing and sparse,
      "title slide carries the six ruling lines and nothing else (%d words)" % len(page1.split())
      if not title_missing and sparse else "title lines missing %s or slide not sparse" % title_missing)

    sel = _slide_part(frame_with("main:sel"))
    coef_used = set(re.findall(r"\\(VCoef\w+)", sel))
    est_ok = (coef_used == set(RULING_ESTIMATES)
              and all(prov[m]["rendered"] == v and prov[m]["kind"] == "coef"
                      for m, v in RULING_ESTIMATES.items()))
    g("G-" + P["tag"] + "-ESTIMATES", est_ok,
      "selected-estimates slide shows exactly beta_c, local unemployment exposure, high education "
      "and sigma for both populations, from the V15 gallery, matching the ruling's values"
      if est_ok else "selected estimates differ: used %s" % sorted(coef_used ^ set(RULING_ESTIMATES)))

    reading = " ".join(pg.get_text() for pg in pymupdf.open(P["pdf"])) if P["pdf"].exists() else ""
    notes = " ".join(re.findall(r"\\note\{(.*?)\}\s*\\end\{frame\}", body, re.S))
    causal = [s_ for s_ in re.split(r"(?<=[.;?!])\s+", flat(_norm(reading)) + " " + flat(notes))
              if re.search(r"\bcaus", s_, re.I)
              and not re.search(r"\b(not|no|nor|never|nothing|non|none)\b", s_, re.I)]
    g("G-" + P["tag"] + "-NOCAUSAL", not causal, "every sentence that mentions causality negates it"
      if not causal else "causal language: %s" % causal[:4])

    story = (HERE.parent / "reports/research_story_build/story_v15.generated.md").read_text(encoding="utf-8")
    v15_says = "Wage elasticities are not reported." in story
    elas = re.search(r"elasticit", src + reading + reh, re.I)
    g("G-" + P["tag"] + "-ELASTICITY", v15_says and not elas,
      "V15 states 'Wage elasticities are not reported.'; the deck adds no elasticity"
      if v15_says and not elas else "elasticity content present, or V15 statement not found")

    n_backup = len(frames(backup_src)) - 1
    substantive = len(main_fr) - 1
    lo, hi = P.get("substantive_range", (16, 18))
    g("G-" + P["tag"] + "-APPENDIX", n_backup >= 12 and lo <= substantive <= hi,
      "%d substantive main slides (%d-%d) and %d backup slides beyond the appendix map (>= 12)"
      % (substantive, lo, hi, n_backup) if n_backup >= 12 and lo <= substantive <= hi
      else "main %d backup %d" % (substantive, n_backup))
    return ok_l, bad_l, detail


# ==========================================================================
# DECK-V19 profile:  python verify_deck_r6.py --deck v19
#
# Every V18 check and its seven controls, repointed.  Added: G-V19-BENCHMARKS
# (every literature number on a slide resolves to a corpus citation recorded in
# literature_benchmarks_v19.json and re-verified against the corpus), G-V19-TONE
# (scope stated once; hedges moved, not deleted; one spoken line on the
# attained-bundle calculation), G-V19-DLABEL (the residual is never labelled D)
# and G-V19-CORRECTIONS (review corrections a, b, c, e; d reported, nothing removed).
# ==========================================================================
V19_SRC = HERE / "JMP_seminar_beamer_v19.tex"
LIT_RECORD_V19 = HERE / "literature_benchmarks_v19.json"
V19_TITLES = [
    "Motivation", "The conflict", "Research question", "Inequality of opportunity",
    "From circumstances to job opportunities", "Building blocks", "Job packages",
    "Opportunities: the choice probability", "How are preferences and opportunities separated?",
    "Data and EUROMOD", "Estimation", "Selected estimates",
    "Welfare: attained outcomes versus job prospects", "Ex-ante prospect welfare",
    "Attained-bundle welfare", "Inequality and Shapley decomposition",
    "How much is associated with opportunities?", "Which opportunity channel matters?",
    "Where does baseline inequality go?", "What is not claimed", "Conclusion",
]
V19_PROFILE = dict(V18_PROFILE, **{
    "tag": "V19",
    "src": V19_SRC, "numbers": HERE / "deck_numbers_v19.tex",
    "prov": BUILD / "v19_number_provenance.json",
    "pdf": BUILD / "JMP_seminar_beamer_v19.pdf",
    "text": BUILD / "JMP_seminar_beamer_v19_text.txt",
    "reh_text": BUILD / "JMP_seminar_beamer_v19_rehearsal_text.txt",
    "results": BUILD / "v19_verification.json",
    "lineage": [V19_SRC, HERE / "make_deck_numbers_r6.py", HERE / "deck_numbers_v19.tex",
                HERE / "build_deck_v19.py", LIT_RECORD_V19],
    "anchors": [(t, t) for t in V19_TITLES], "main_range": (20, 22),
    "substantive_range": (19, 21),
    "welfare_title": "Welfare: attained outcomes versus job prospects",
    "required": {
        "resources/needs/composition held fixed":
            "Household resources, needs and composition held fixed",
        "access = local access, defined":
            "local unemployment exposure, region, urban or rural location, year",
        "access is local access, not total opportunity": "local access, not total opportunity",
        "preliminary (scope slide)": "Preliminary decomposition",
        "not causal (scope slide)": "Not causal",
        "no parameter uncertainty yet": "No parameter uncertainty yet",
        "preferences not equated with responsibility": "Preferences are not responsibility",
        "prospects versus attained outcomes": "prospects versus attained outcomes",
        "two different welfare questions": "two different welfare questions",
        "neither perspective primary": "Neither perspective is designated primary",
        "2x2 label": "A + B as % of the relevant baseline Gini",
        "100% display denominator label": "shares of baseline Gini",
        "residual label": "Other / outside current P-A-B decomposition",
        "residual footnote": "Current decomposition equalises P, A and B only.",
        "X1: A + B alone": "A + B alone",
        "backup: sex-specific blocks": "sex-specific",
        "backup: luck and spread": "wage-draw luck and the common offer spread",
        "EOp footer": "Different outcomes, circumstance sets and methods.",
        "EOp bottom line": "An inequality-of-opportunity question with a structural opportunity object.",
        "identification bottom line":
            "These restrictions give different empirical variation to preferences and opportunities.",
        "8b wording": "If availability heterogeneity is omitted, some of its effects can be absorbed by the estimated utility component.",
        "8c contribution": "The contribution is the structural equalisation of estimated preferences, access and earning opportunities followed by recomputation of money-metric welfare inequality.",
        "conclusion next step": "Next: extend the decomposition to household resources and needs.",
        "welfare framing": "attained outcomes versus job prospects",
        "ATT question": "What is the money equivalent of the attained bundle?",
        "EA question": "What constant consumption over the household's own job environment is equivalent to its prospect?",
    },
    "hundred_phrases": ["Other / outside current P-A-B decomposition", r"1-(\phi_P+\phi_A+\phi_B)/I_0",
                        "A + B alone", "Current decomposition equalises P, A and B only.",
                        "shares of baseline Gini", r"\VHundredCoupP"],
    "rebuild": "build_v19",
    "v19": True,
})

HEDGES = [r"\bnot causal\b", r"\bno causal\b", r"\bcausal", r"\bpreliminary\b", r"\bpoint estimates?\b",
          r"\bnot statistically\b", r"\bstatistically established\b", r"\bsubject to\b",
          r"\bcannot claim\b"]
MATURITY = "less numerically mature"
EOP_MACROS = {"VLitItaly", "VLitItalyYear", "VLitBrazilLo", "VLitBrazilHi", "VLitBrazilYear",
              "VLitFrance", "VLitFranceYear"}


def benchmark_problems(src: str, record: dict) -> list[str]:
    sys.path.insert(0, str(HERE))
    import make_deck_numbers_r6 as numsrc  # noqa: E402
    problems = []
    try:
        verified = numsrc.verify_literature(record)
    except SystemExit as exc:
        return ["corpus verification failed: %s" % exc]
    body = src.split(r"\begin{document}", 1)[-1]
    used = set(re.findall(r"\\(VLit[A-Za-z]+)", body))
    problems += ["literature macro without a recorded corpus citation: %s" % m
                 for m in sorted(used - set(verified))]
    for bm in record["benchmarks"]:
        if bm.get("status") != "verified" or not all(bm.get(k) for k in ("country", "outcome", "measure", "paper")):
            problems.append("benchmark %s incomplete or unverified" % bm.get("id"))
        if bm["paper"] not in record["papers"]:
            problems.append("benchmark %s cites an unknown paper" % bm["id"])
    eop = next((f for f in frames(body) if r"\hypertarget{main:eop}" in f), "")
    eop_used = set(re.findall(r"\\(VLit[A-Za-z]+)", re.sub(r"\\note\{.*", "", eop, flags=re.S)))
    if eop_used != EOP_MACROS:
        problems.append("inequality-of-opportunity slide shows %s, expected %s"
                        % (sorted(eop_used), sorted(EOP_MACROS)))
    lit_frames = [i for i, f in enumerate(frames(body), 1)
                  if re.search(r"\\VLit[A-Za-z]+", re.sub(r"\\note\{.*", "", f, flags=re.S))]
    allowed = {i for i, f in enumerate(frames(body), 1)
               if r"\hypertarget{main:eop}" in f or r"\hypertarget{b:eopbench}" in f or r"\hypertarget{b:lit}" in f}
    problems += ["literature numbers on an unexpected slide %d" % i for i in lit_frames if i not in allowed]
    return problems


def v19_gates(src: str, pages: list[str], reh: str, P: dict) -> tuple[list, list, dict]:
    ok_l: list[str] = []
    bad_l: list[str] = []
    detail: dict = {}

    def g(name: str, ok: bool, msg: str) -> None:
        (ok_l if ok else bad_l).append("%-18s %s" % (name, msg))
        detail[name] = {"pass": bool(ok), "detail": msg}

    record = json.loads(LIT_RECORD_V19.read_text(encoding="utf-8"))
    problems = benchmark_problems(src, record)
    n_items = len(record["items"])
    g("G-V19-BENCHMARKS", not problems,
      "%d literature items and %d benchmarks each resolve to a corpus quote on the recorded page; "
      "no literature number on a slide without a recorded citation" % (n_items, len(record["benchmarks"]))
      if not problems else "BENCHMARK PROBLEMS: %s" % problems[:5])

    body = src.split(r"\begin{document}", 1)[-1]
    main_src, backup_src = split_appendix(src)
    main_fr = frames(main_src)
    limits_ix = next(i for i, f in enumerate(main_fr) if r"\hypertarget{main:limits}" in f)
    hedge_hits = []
    for i, page in enumerate(pages[:len(main_fr)]):
        if i == limits_ix:
            continue
        t = _norm(page).lower()
        for h in HEDGES:
            if re.search(h, t):
                hedge_hits.append("slide %d: %s" % (i, h))
    notes = re.findall(r"\\note\{(.*?)\}\s*\\end\{frame\}", body, re.S)
    maturity_notes = sum(flat(n).count(MATURITY) for n in notes)
    maturity_slides = sum(_norm(pg).count(MATURITY) for pg in pages)
    moved = {h: bool(re.search(h, (flat(" ".join(notes)) + " " + _norm(" ".join(pages[len(main_fr):]))).lower()))
             for h in (r"\bnot causal\b", r"\bpreliminary\b", r"\bpoint estimates?\b", r"\bnot statistically\b")}
    tone_ok = not hedge_hits and maturity_notes == 1 and maturity_slides == 0 and all(moved.values())
    g("G-V19-TONE", tone_ok,
      "no hedge on any main slide except the scope slide; hedges kept in notes and backup; the "
      "attained-bundle maturity line spoken exactly once"
      if tone_ok else "hedges %s; maturity in notes %d, on slides %d; moved %s"
                      % (hedge_hits[:6], maturity_notes, maturity_slides, moved))

    d_hits = [i + 1 for i, pg in enumerate(pages) if re.search(r"(?<![\w-])D(?![\w-])", _norm(pg))]
    d_src = re.findall(r"channel D|D channel|fourth channel D|\bD\b(?= operator)", body)
    completes = re.findall(r"complet\w* (the )?decomposition", (flat(" ".join(notes)) + " "
                                                               + _norm(" ".join(pages))).lower())
    hundred_page = next((pg for pg in pages if "Where does baseline inequality go?" in pg), "")
    conclusion = next((pg for pg in pages[:len(main_fr)] if "Conclusion" in pg.split("\n", 3)[0]
                       or "Next: extend the decomposition" in pg), "")
    d_ok = (not d_hits and not d_src and not completes
            and "Other / outside current P-A-B decomposition" in _norm(hundred_page)
            and "Current decomposition equalises P, A and B only." in _norm(hundred_page)
            and "Next: extend the decomposition to household resources and needs." in _norm(conclusion))
    g("G-V19-DLABEL", d_ok,
      "the residual is labelled 'Other / outside current P-A-B decomposition' with its footnote; no "
      "slide labels anything D or implies that adding a channel completes the decomposition"
      if d_ok else "D labels on pages %s, source %s, completion wording %s" % (d_hits, d_src, completes))

    rendered = _norm(" ".join(pages))
    corr = {
        "a density equation": r"g_i(o)=1" in body and r"g^{E}_i\cdot\Big(" not in body,
        "b conventional-model wording": not re.search(
            r"must be a difference in taste|would have to be a difference in taste|every difference in "
            r"behaviour (must|would)|must read every difference", flat(body), re.I)
            and _norm(P["required"]["8b wording"]) in rendered,
        "c contribution wording": not re.search(r"levels? rather than changes|rather than changes|"
                                                r"\\emph\{level\}", body)
            and _norm(P["required"]["8c contribution"]) in rendered,
        "d fit evidence kept pending verification": (r"\hypertarget{b:extensive}" in body
                                                     and r"\hypertarget{b:margins}" in body),
        "e identifiers in parameter tables": all(
            len(re.findall(r"\\VCoef\w+Id\b", next((f for f in frames(body)
                                                     if r"\hypertarget{%s}" % t in f), ""))) >= n
            for t, n in (("b:prefs", 20), ("b:access", 12), ("b:hours", 27), ("b:wage", 9))),
    }
    g("G-V19-CORRECTIONS", all(corr.values()),
      "review corrections applied: " + "; ".join(corr) if all(corr.values())
      else "corrections missing: %s" % [k for k, v in corr.items() if not v])
    return ok_l, bad_l, detail


def main_profile(P: dict) -> int:
    import subprocess
    src = P["src"].read_text(encoding="utf-8")
    pdftotext = Path.home() / "AppData/Local/Programs/MiKTeX/miktex/bin/x64/pdftotext.exe"
    if not P["text"].exists() and P["pdf"].exists():
        subprocess.run([str(pdftotext), "-layout", str(P["pdf"]), str(P["text"])], check=True)
    text = P["text"].read_text(encoding="utf-8", errors="replace")
    pages = text.split("\f")
    if pages and not pages[-1].strip():
        pages = pages[:-1]
    reh = P["reh_text"].read_text(encoding="utf-8", errors="replace") \
        if P["reh_text"].exists() else ""
    T = "G-" + P["tag"]

    ok_l, bad_l, detail = v16_gates(src, pages, reh, P)
    if P["style"]:
        ok2, bad2, det2 = v17_extra_gates(src, P["pdf"], P["tag"],
                                          P.get("table_macros", ("VEASingPhiARaw", "VAttSingPhiARaw")),
                                          P.get("welfare_title", "Welfare"))
        ok_l, bad_l = ok_l + ok2, bad_l + bad2
        detail.update(det2)
    if P.get("v18"):
        ok3, bad3, det3 = v18_gates(src, pages, reh, P)
        ok_l, bad_l = ok_l + ok3, bad_l + bad3
        detail.update(det3)
    if P.get("v19"):
        ok4, bad4, det4 = v19_gates(src, pages, reh, P)
        ok_l, bad_l = ok_l + ok4, bad_l + bad4
        detail.update(det4)

    # ---------------- negative controls: in-memory copies, original files untouched
    controls = {}
    inj = list(pages)
    inj[1] = inj[1] + "\nEstimated under S11.\n"
    _, _, det_tok = v16_gates(src, inj, reh, P)
    controls["NC-LABEL (inject 'S11' on slide 2)"] = {
        "expected": T + "-LABELS FAIL",
        "fired": not det_tok[T + "-LABELS"]["pass"]}
    inj = list(pages)
    inj[1] = inj[1] + "\nA share of 12.34 per cent.\n"
    _, _, det_num = v16_gates(src, inj, reh, P)
    controls["NC-REGISTRY (inject unregistered '12.34' on slide 2)"] = {
        "expected": "G-REGISTRY FAIL",
        "fired": not det_num["G-REGISTRY"]["pass"]}
    if P["style"]:
        long_src = src.replace(r"\frametitle{Motivation}",
                               r"\frametitle{Why income inequality mixes several different mechanisms}", 1)
        titles_bad, _ = style_violations(long_src, P["pdf"])
        controls["NC-STYLE-TITLE (inject a seven-word title on slide 2)"] = {
            "expected": T + "-STYLE FAIL", "fired": bool(titles_bad), "hits": titles_bad}
        v16_titles, paras_bad = style_violations(V16_SRC.read_text(encoding="utf-8"), V16_PDF)
        controls["NC-STYLE-PARAGRAPH (render check on the prose-bodied V16 PDF)"] = {
            "expected": "paragraph check FAIL", "fired": bool(paras_bad),
            "hits": paras_bad[:6], "count": len(paras_bad),
            "v16_long_titles": len(v16_titles)}
    if P.get("v18"):
        target = next(i for i, pg in enumerate(pages) if "Where does baseline inequality go?" in pg)
        inj = list(pages)
        inj[target] = inj[target] + "\nThe access share of explained change is large.\n"
        mixes = denominator_mixes(src, inj)
        controls["NC-DENOMINATORS (inject 'share of explained change' on the 100% slide)"] = {
            "expected": T + "-DENOMINATORS FAIL", "fired": bool(mixes), "hits": mixes[:3]}
        broken_src = src.replace(r"\golink{b:utility}", r"\golink{b:nowhere}", 1)
        problems, _ = link_problems(broken_src, P["pdf"])
        controls["NC-LINKS (point one main-slide button at a missing target)"] = {
            "expected": T + "-LINKS FAIL", "fired": bool(problems), "hits": problems[:3]}
        inj = list(pages)
        inj[1] = inj[1] + "\nJob opportunities account for 85.0% of inequality.\n"
        _, _, det_high = v16_gates(src, inj, reh, P)
        controls["NC-8090 (inject an 85% opportunity claim on slide 2)"] = {
            "expected": T + "-NO8090 FAIL", "fired": not det_high[T + "-NO8090"]["pass"]}

    if P.get("v19"):
        record = json.loads(LIT_RECORD_V19.read_text(encoding="utf-8"))
        tampered = json.loads(json.dumps(record))
        for item in tampered["items"]:
            if item["macro"] == "VLitItaly":
                item["display"] = "21.5"
        bad_record = benchmark_problems(src, tampered)
        controls["NC-BENCHMARK-RECORD (Italy value changed to 21.5 in the record)"] = {
            "expected": "G-V19-BENCHMARKS FAIL", "fired": bool(bad_record), "hits": bad_record[:2]}
        injected = src.replace(r"{\tiny Checchi \& Peragine \VLitItalyYear}",
                               r"{\tiny Checchi \& Peragine \VLitItalyYear} {\huge \VLitSpain\%}", 1)
        bad_slide = benchmark_problems(injected, record)
        controls["NC-BENCHMARK-SLIDE (unrecorded benchmark added to the EOp slide)"] = {
            "expected": "G-V19-BENCHMARKS FAIL", "fired": bool(bad_slide) and injected != src,
            "hits": bad_slide[:2]}

    label = "verify_deck_r6.py --deck " + P["tag"].lower()
    print("%s deck verification (%s)" % (P["tag"], label))
    print("-" * 68)
    for line in ok_l:
        print("  PASS  " + line)
    for line in bad_l:
        print("  FAIL  " + line)
    print("-" * 68)
    for name, c in controls.items():
        print("  %s  %s -> expected %s" % ("FIRED" if c["fired"] else "SILENT", name, c["expected"]))
        if c.get("hits"):
            print("         e.g. %s" % c["hits"][0])
    print("-" * 68)
    fired = all(c["fired"] for c in controls.values())
    print("%d passed, %d failed; %d negative controls %s"
          % (len(ok_l), len(bad_l), len(controls), "all fired" if fired else "DID NOT ALL FIRE"))
    P["results"].write_text(json.dumps({"gates": detail, "negative_controls": controls,
                                        "passed": len(ok_l), "failed": len(bad_l)},
                                       indent=2), encoding="utf-8", newline="\n")
    return 1 if bad_l or not fired else 0


def main_v16() -> int:
    return main_profile(V16_PROFILE)


if __name__ == "__main__":
    if "--deck" in sys.argv[1:]:
        deck = sys.argv[sys.argv.index("--deck") + 1]
        sys.exit(main_profile({"v16": V16_PROFILE, "v17": V17_PROFILE, "v18": V18_PROFILE,
                               "v19": V19_PROFILE}[deck]))
    sys.exit(main())
