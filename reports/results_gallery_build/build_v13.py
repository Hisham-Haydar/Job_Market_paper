#!/usr/bin/env python
"""Build the V13 gallery from the V12 gallery and the V13 report (figures release).

The decomposition panel gains the architecture diagram and the regenerated
attained-bundle and ex-ante Shapley figures; the central-result panel gains the
two-perspective figure. Everything else is copied from V12.
"""
from __future__ import annotations

import base64
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "reports/results_gallery_build"))
import build_v11 as base  # noqa: E402

sys.path.insert(0, str(ROOT / "reports/research_story_build"))
import v13_render_inputs as inputs  # noqa: E402

SOURCE = ROOT / "reports/JMP_results_gallery_v12.html"
REPORT = ROOT / "reports/JMP_research_story_report_v13.html"
OUT = ROOT / "reports/JMP_results_gallery_v13.html"
BEGIN_V12 = "<!-- V12_PROVENANCE_APPENDIX_BEGIN -->"
END_V12 = "<!-- V12_PROVENANCE_APPENDIX_END -->"
BEGIN_V13 = "<!-- V13_PROVENANCE_APPENDIX_BEGIN -->"
END_V13 = "<!-- V13_PROVENANCE_APPENDIX_END -->"
base.BEGIN_V11 = BEGIN_V13


def figure_html(key: str) -> str:
    caption, path = re.search(r"!\[(.*?)\]\((.*?)\)", inputs.CAPTIONS[key], flags=re.S).groups()
    data = base64.b64encode(Path(path).read_bytes()).decode()
    return (f'<figure class=""><img alt="{caption.split(".")[0]}" src="data:image/png;base64,{data}">'
            f"<figcaption>{caption}</figcaption></figure>")


def main() -> None:
    document = SOURCE.read_text(encoding="utf-8")
    report = REPORT.read_text(encoding="utf-8")

    old_decomposition = base.section_body(document, "decomposition")
    variance = old_decomposition[old_decomposition.index("<h3>Variance accounting</h3>"):
                                 old_decomposition.index("<h3>Ex-ante perspective (EA)</h3>")]
    decomposition = (
        "<p class=lead>" + base.sections.D_STATUS + " Household resources, needs and composition "
        "receive no allocated share; adding them is a planned extension.</p>"
        + figure_html("v13architecture")
        + "<h3>Attained-bundle perspective (ATT)</h3>"
        + base.report_h2(report, "attained-bundle-decomposition")
        + variance
        + "<h3>Ex-ante perspective (EA)</h3>"
        + base.report_h2(report, "ex-ante-well-being-and-decomposition")
    )
    document = base.replace_section(document, "decomposition", "What the two decompositions say", decomposition)

    old_central = base.section_body(document, "exante")
    tail = old_central[old_central.rindex("<p>For couples, equivalisation moves"):]
    document = base.replace_section(
        document, "exante",
        "The central result: the welfare question changes which labour-market inequality matters",
        base.report_h2(report, "the-central-result-outcomes-versus-prospects") + tail)
    document = base.replace_section(document, "limitations", "What remains preliminary",
                                    base.report_h1_body(report, 6))

    document = document.replace("Reader-facing evidence · V12", "Reader-facing evidence · V13")
    document = document.replace(BEGIN_V12, BEGIN_V13).replace(END_V12, END_V13)
    if document.count(BEGIN_V13) != 1 or document.count(END_V13) != 1:
        raise RuntimeError("V13 gallery must contain exactly one appendix marker pair")
    if document.count("<figure") + document.count("<figcaption class=standalone>") != document.count("<figcaption"):
        raise RuntimeError("a gallery figure is missing its caption")
    OUT.write_text(document, encoding="utf-8", newline="\n")
    print(f"wrote {OUT} ({OUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
