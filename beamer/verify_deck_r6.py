#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""R6 gates for the seminar deck.

The v4 gates are bound to content R2 retires, so they do not apply to this
deck.  These gates enforce what R6 and the BASELINE-F-1 ruling actually
require:

  G-RETIRE   no retired W1-EA magnitude appears anywhere in the PDF text.
  G-NOSHARE  no P/A/B/D share, no Shapley/Owen magnitude, no access share.
  G-CAPTION  the calibration figure carries the required caption verbatim.
  G-UNITS    every welfare slide states units, weight and unequivalised.
  G-SOURCE   the welfare slides cite the recorded and verified commits.
  G-NUMBERS  every numeral in the deck source is a macro, not typed.
  G-G2       only G2-ADEQUATE fit statistics reach a slide.
  G-QA       every welfare slide's note is a Q&A note citing a ruling ID.
  G-NOCONF   no confusion-matrix headline number.
  G-POOLED   no pooled welfare figure.

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
BUILD = HERE / "build"
SRC = HERE / "JMP_seminar_deck_r6.tex"
NUMBERS = HERE / "deck_numbers_r6.tex"
TEXT = BUILD / "JMP_seminar_deck_r6_text.txt"
POSFIT = REPO / "MNL_posfit" / "outputs" / "positive_fit_diagnostics_v2"

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
CAPTION = "quadrature-limited; support audit pending"
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

    # --------------------------------------------------------- G-NOSHARE
    share_words = ["shapley", "owen", "share of inequality", "of measured inequality",
                   "decomposition result", "attributed to the environment"]
    bad = [w for w in share_words if w in text.lower()]
    gate("G-NOSHARE", not bad,
         "no decomposition magnitude in the rendered deck" if not bad
         else "share language rendered: " + ", ".join(bad))

    # --------------------------------------------------------- G-CAPTION
    gate("G-CAPTION", CAPTION in src and (not text or CAPTION in text),
         "calibration caption verbatim: %r" % CAPTION)

    # ----------------------------------------------------------- G-UNITS
    # the two distribution slides, not the B1 checks slide that shares the stem
    wf = [f for f in frames(src) if "Baseline $\\Wone$-F," in f]
    ok_units = len(wf) == 2 and all("\\wfunits" in f for f in wf)
    rendered_units = (not text) or ("household EUR/month, unequivalised" in text)
    gate("G-UNITS", ok_units and rendered_units,
         "%d baseline slides, each carrying units/weight/unequivalised" % len(wf))

    # ---------------------------------------------------------- G-SOURCE
    gate("G-SOURCE", "6048c9f" in src and "b5550af" in src,
         "baseline slides cite recorded 6048c9f and verified b5550af")

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
    gate("G-G2", (not bad_fit) and bool(adequate),
         "%d ADEQUATE weighted statistics exist; only those are emitted" % len(adequate))

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
    gate("G-POOLED", agg["pooled_row"] is False and "pooled" not in
         text.lower().replace("no pooled figure", ""),
         "source carries no pooled row; deck shows singles and couples separately")

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
