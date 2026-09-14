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

DECK-3 also repoints G-G2 and G-CAPTION to POSFIT v2b (MNL_posfit a2e80a8):
G-G2 now ties each group's extensive-accuracy row to its v2b label in both
directions; G-CAPTION checks the v2b caption and that "support audit pending"
is gone.

DECK-NUMBERS-1 (Deputy M2 fit-verdict correction) narrowly reopens G-G2's
v2b-only rule: the fit-verdict slide's speaker note cites POSFIT v3
(MNL_posfit 96693269, diagnostics/posfit-v3) by name, sourcing exactly the
two coupled-men extensive-accuracy ratio macros and the v3 commit macro from
it. G-G2 allows ONLY that named g2_adequacy_v3.csv source and ONLY for those
three macros; any other v3 source, or a v3 source for any other macro, still
fails the gate.

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
POSFIT = REPO / "MNL_posfit" / "outputs" / "positive_fit_diagnostics_v2b"   # MNL_posfit a2e80a8

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
# DECK-3: v2b IS the support-coverage audit, so "support audit pending" is
# retired; the caption now states the v2b status.
CAPTION = ("support coverage audited (POSFIT v2b); calibration statistics "
           "partly quadrature-limited; fit verdicts open pending Deputy review")
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


def main() -> int:
    src = SRC.read_text(encoding="utf-8")
    nums = NUMBERS.read_text(encoding="utf-8")
    text = TEXT.read_text(encoding="utf-8", errors="replace") if TEXT.exists() else ""

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

    # --------------------------------------------------------- G-CAPTION
    cap_ok = (CAPTION in flat(src) and (not text or CAPTION in flat(text))
              and RETIRED_CAPTION not in (src + text).lower())
    gate("G-CAPTION", cap_ok,
         "calibration caption verbatim (v2b status): %r; retired %r absent"
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
    gate("G-SOURCE",
         "6048c9f" in src and "b5550af" in src and "4c4e07e" in src,
         "baseline slides cite recorded 6048c9f, verified b5550af, "
         "and the E3-EQ equivalised-reporting memo 4c4e07e")

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
    # DECK-NUMBERS-1: the ONLY authorised v3 source is g2_adequacy_v3.csv,
    # and it may source ONLY the fit-verdict note's two ratio macros plus the
    # v3 commit macro -- everything else MNL_posfit must still be v2b.
    v3_source_key = "g2_adequacy_v3.csv"
    v3_source_prefix = "g2_adequacy.csv (v3)"
    v3_allowed_macros = {"FitExtRatioCMWeightedVThree", "FitExtRatioCMUnweightedVThree"}
    posfit_ok = all(
        "positive_fit_diagnostics_v2b" in v["path"]
        or (k == v3_source_key and "positive_fit_diagnostics_v3" in v["path"])
        for k, v in emitted["sources"].items() if "MNL_posfit" in v.get("path", ""))
    v3_macro_sources = {name for name, meta in emitted["macros"].items()
                        if meta["source"].startswith(v3_source_prefix)}
    v3_scope_ok = v3_macro_sources == v3_allowed_macros
    gate("G-G2", (not bad_fit) and bool(adequate) and not row_bad and posfit_ok
         and v3_scope_ok,
         "%d ADEQUATE weighted statistics exist; only those are emitted; "
         "extensive-accuracy rows match v2b labels %s; all posfit sources are "
         "v2b except the fit-verdict note's g2_adequacy_v3.csv (macros %s)"
         % (len(adequate), ext, sorted(v3_macro_sources))
         if not row_bad and posfit_ok and v3_scope_ok
         else "G2 row mismatch %s / non-v2b posfit source outside the "
              "authorised v3 scope (v3 macros seen: %s)"
              % (row_bad, sorted(v3_macro_sources)))

    # ----------------------------------------------------------- G-SCALE
    # DECK-3: the modified-OECD scale is ratified.  Every equivalised welfare
    # slide must cite the ratifying ruling and the scale-review memo, and no
    # "PROVISIONAL" scale wording may reappear in the source or rendered deck.
    ruling = "SCALE CLOSED; CHILD-SHIFTER FRAMING"
    memo = "JMP_SCALE_REVIEW_1_equivalence_scale_economics_v1.md"
    unesc = src.replace("\\_", "_")
    wfeq_macro = re.search(r"\\newcommand\{\\wfunitseq\}(.*?)\n\n", unesc, re.S)
    macro_cites = bool(wfeq_macro) and ruling in flat(wfeq_macro.group(1)) \
        and memo in flat(wfeq_macro.group(1))
    # pdftotext renders \texttt{\_} as a space, so compare the memo name with
    # underscores normalised to spaces on both sides.
    rendered_cites = (not text) or (
        ruling in flat_text
        and flat(memo.replace("_", " ")) in flat(text.replace("_", " ")))
    nocomment = re.sub(r"(?m)%.*$", "", src)
    prov_hits = sorted(set(m.group(0) for m in re.finditer(
        r"provisional[^.\n]{0,40}|pending\s+(an\s+)?economics\s+review",
        (nocomment + "\n" + text), re.I)))
    scale_ok = macro_cites and ok_eq and rendered_cites and not prov_hits
    gate("G-SCALE", scale_ok,
         "both equivalised slides cite %r and %s; no PROVISIONAL scale wording"
         % (ruling, memo) if scale_ok
         else "scale citation missing (macro=%s rendered=%s) or provisional "
              "wording present: %s" % (macro_cites, rendered_cites, prov_hits))

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
    op_ix = src.find(r"\headlineframe{DECOMP-2 equalises")
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


if __name__ == "__main__":
    sys.exit(main())
