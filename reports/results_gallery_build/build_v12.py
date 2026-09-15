#!/usr/bin/env python
"""Build the V12 gallery from the V11 gallery and the V12 report (structural edit).

- Body panels that mirror the report (decomposition, central result, limitations)
  are refreshed from the V12 report.
- The variance-accounting table moves from the appendix into the decomposition
  panel; its stale column label is replaced.
- The appendix keeps implementation diagnostics only: predictive-fit matrices and
  calibration, integration convergence, and the leisure-normalisation exercise.
  The time-endowment block moves to the body through the report's Section 6. The
  duplicated decomposition record, its figures (whose images embed an outdated
  access definition and internal labels), the robustness and limitation boxes
  and the wage-elasticity note are removed; the superseded ex-ante status box is
  kept as a labelled historical statement.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "reports/results_gallery_build"))
import build_v11 as base  # noqa: E402

SOURCE = ROOT / "reports/JMP_results_gallery_v11.html"
REPORT = ROOT / "reports/JMP_research_story_report_v12.html"
OUT = ROOT / "reports/JMP_results_gallery_v12.html"
BEGIN_V11, END_V11 = base.BEGIN_V11, base.END_V11
BEGIN_V12 = "<!-- V12_PROVENANCE_APPENDIX_BEGIN -->"
END_V12 = "<!-- V12_PROVENANCE_APPENDIX_END -->"
base.BEGIN_V11 = BEGIN_V12  # report section extraction stops at the V12 marker


def cut(document: str, start: str, end: str) -> tuple[str, str]:
    if document.count(start) != 1:
        raise RuntimeError("gallery anchor not unique: " + start[:60])
    i = document.index(start)
    j = document.index(end, i)
    return document[:i] + document[j:], document[i:j]


def main() -> None:
    document = SOURCE.read_text(encoding="utf-8")
    report = REPORT.read_text(encoding="utf-8")

    # Appendix: remove the time-endowment block (now in the body).
    document, _ = cut(document, "<h4>Time endowment T: independent re-estimation at 75 and 90</h4>",
                      '<p class="small">Accepted source: WS4 branch')
    document, _ = cut(document, "<br><strong>Time-endowment sensitivity",
                      "</div><h4><code>lambda_l</code>")
    document = document.replace("<h3>Leisure normalisation and time-endowment sensitivity</h3>",
                                "<h3>Leisure normalisation: analytic image and independent re-estimation</h3>", 1)

    # Appendix: remove the duplicated decomposition record, keep the variance table.
    document, record = cut(document, "<h3>Counterfactual-decomposition calculation record</h3>",
                           '<article class=warn><h3>Distinct ex-ante metric</h3>')
    variance = record[record.index("<h3>Variance accounting within the bounded game</h3>"):
                      record.index("<h3>Robustness and implementation record</h3>")]
    variance = variance.replace("<h3>Variance accounting within the bounded game</h3>",
                                "<h3>Variance accounting</h3>").replace("W1_F", "M_att")
    document = document.replace(
        '<article class=warn><h3>Distinct ex-ante metric</h3>',
        '<h3>Historical status statement, superseded before V9</h3><div class=verdicts>'
        '<article class=warn><h3>Distinct ex-ante metric</h3>', 1)
    document, _ = cut(document, '<article class=warn><h3>Wage elasticities</h3>', "</article></div>")
    document = document.replace("</article></div></article></div>", "</article></div>", 1) \
        if "</article></div></article></div>" in document else document
    document = re.sub(r"(<article class=warn><h3>Distinct ex-ante metric</h3>.*?</article>)\s*</article></div>",
                      r"\1</div>", document, count=1, flags=re.S)
    document = document.replace(
        '<p class="lead">The earlier implementation-facing panels are preserved here so every '
        'displayed value and its source context remain available.</p>',
        '<p class="lead">Implementation diagnostics only: predictive-fit matrices and calibration, '
        'integration convergence and the leisure-normalisation exercise. Every result is in the '
        'panels above.</p>', 1)

    # Body panels refreshed from the V12 report.
    decomposition = (
        "<p class=lead>" + base.sections.D_STATUS + " Household resources, needs and composition "
        "receive no allocated share; adding them is a planned extension.</p>"
        "<h3>Attained-bundle perspective (ATT)</h3>"
        + base.report_h2(report, "attained-bundle-decomposition")
        + variance
        + "<h3>Ex-ante perspective (EA)</h3>"
        + base.report_h2(report, "ex-ante-well-being-and-decomposition")
    )
    document = base.replace_section(document, "decomposition", "What the two decompositions say",
                                    decomposition)
    central_old = base.section_body(document, "exante")
    tail = central_old[central_old.rindex("<p>For couples, equivalisation moves"):]
    document = base.replace_section(
        document, "exante",
        "The central result: the welfare question changes which labour-market inequality matters",
        base.report_h2(report, "the-central-result-outcomes-versus-prospects") + tail)
    document = base.replace_section(document, "limitations", "What remains preliminary",
                                    base.report_h1_body(report, 6))

    document = document.replace("Reader-facing evidence · V11", "Reader-facing evidence · V12")
    document = document.replace(BEGIN_V11, BEGIN_V12).replace(END_V11, END_V12)
    if document.count(BEGIN_V12) != 1 or document.count(END_V12) != 1:
        raise RuntimeError("V12 gallery must contain exactly one appendix marker pair")
    if document.count("<details") != document.count("</details>"):
        raise RuntimeError("unbalanced details elements")
    appendix = document[document.index(BEGIN_V12):document.index(END_V12)]
    for gone in ("Counterfactual-decomposition calculation record", "Wage elasticities",
                 "Short-hours support", "Benchmark input defect", "Time endowment T"):
        if gone in appendix:
            raise RuntimeError("removed appendix block survived: " + gone)
    standalone = document.count("<figcaption class=standalone>")
    if document.count("<figure") + standalone != document.count("<figcaption"):
        raise RuntimeError("a gallery figure is missing its caption")
    OUT.write_text(document, encoding="utf-8", newline="\n")
    print(f"wrote {OUT} ({OUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
