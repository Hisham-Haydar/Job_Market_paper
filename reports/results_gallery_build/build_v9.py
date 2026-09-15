#!/usr/bin/env python
"""Build the V9 reader-facing gallery from the released V8 gallery and V9 report."""
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "reports/JMP_results_gallery_v8.html"
REPORT = ROOT / "reports/JMP_research_story_report_v9.html"
OUT = ROOT / "reports/JMP_results_gallery_v9.html"
BEGIN_V8 = "<!-- V8_PROVENANCE_APPENDIX_BEGIN -->"
END_V8 = "<!-- V8_PROVENANCE_APPENDIX_END -->"
BEGIN_V9 = "<!-- V9_PROVENANCE_APPENDIX_BEGIN -->"
END_V9 = "<!-- V9_PROVENANCE_APPENDIX_END -->"


def report_section(document: str, number: int) -> str:
    match = re.search(
        rf'<h1 id="{number}-[^"]+">.*?</h1>(.*?)(?=<h1 id="{number + 1}-|'
        r'<!-- V9_PROVENANCE_APPENDIX_BEGIN -->)',
        document,
        flags=re.S,
    )
    if not match:
        raise RuntimeError(f"missing V9 report section {number}")
    return match.group(1)


def subsection(document: str, heading_id: str, next_id: str | None) -> str:
    end = rf'(?=<h2 id="{re.escape(next_id)}">)' if next_id else r'\Z'
    match = re.search(
        rf'<h2 id="{re.escape(heading_id)}">.*?</h2>(.*?){end}',
        document,
        flags=re.S,
    )
    if not match:
        raise RuntimeError(f"missing V9 report subsection {heading_id}")
    return match.group(1)


def replace_section(document: str, section_id: str, title: str, body: str) -> str:
    pattern = re.compile(
        rf'(<section id="{re.escape(section_id)}"><div class="kicker">'
        r'.*?</div><h2>).*?(</h2>)(.*?)(</section>)',
        flags=re.S,
    )
    document, count = pattern.subn(
        lambda match: match.group(1) + title + match.group(2) + body
        + match.group(4),
        document,
        count=1,
    )
    if count != 1:
        raise RuntimeError(f"missing V8 gallery section {section_id}")
    return document


def main() -> None:
    document = SOURCE.read_text(encoding="utf-8")
    report = REPORT.read_text(encoding="utf-8")
    results = report_section(report, 5)

    attained = subsection(results, "attained-bundle-decomposition",
                          "ex-ante-well-being-and-decomposition")
    exante = subsection(results, "ex-ante-well-being-and-decomposition",
                        "the-two-welfare-perspectives-side-by-side")
    comparison = subsection(results, "the-two-welfare-perspectives-side-by-side", None)
    comparison = comparison.split('<h1 id="6-', 1)[0]

    decomposition_body = (
        "<h3>Attained-bundle perspective</h3>" + attained
        + "<h3>Ex-ante perspective</h3>" + exante
        + "<h3>Side-by-side comparison</h3>" + comparison
    )
    document = replace_section(
        document,
        "decomposition",
        "What the two decompositions say",
        decomposition_body,
    )

    explanation = (
        "<p class=lead>The measures disagree about which opportunity channel "
        "dominates. Under the attained-bundle measure, earning opportunities "
        "dominate. Under the ex-ante measure, access is about three times "
        "earning opportunities for single-adult households.</p>"
        "<p>The ex-ante measure values the whole prospect, so reachability "
        "matters directly. The attained-bundle measure sees only the realised "
        "job, where wages drive disposable consumption. Neither perspective is "
        "designated primary.</p>"
        "<p>For couples, equivalisation moves the ex-ante access-plus-earnings "
        "share from 21.3% to 7.9% of baseline inequality and turns the preference "
        "contribution negative. The scale convention is materially consequential, "
        "so no directional preference claim is made.</p>"
    )
    document = replace_section(
        document,
        "exante",
        "Why the channel ordering changes",
        explanation,
    )

    exact_title = (
        "Unequal Job Opportunities and Well-Being Inequality: "
        "A Latent-Jobs Structural Decomposition"
    )
    document = re.sub(r"<title>.*?</title>",
                      "<title>" + exact_title + " · Results gallery</title>",
                      document, count=1, flags=re.S)
    document = re.sub(r"<h1>From job opportunities to well-being inequality</h1>",
                      "<h1>" + exact_title + "</h1>", document, count=1)
    document = document.replace("Reader-facing evidence · V8",
                                "Reader-facing evidence · V9")
    document = document.replace(BEGIN_V8, BEGIN_V9).replace(END_V8, END_V9)
    if document.count(BEGIN_V9) != 1 or document.count(END_V9) != 1:
        raise RuntimeError("V9 gallery must contain exactly one appendix marker pair")
    OUT.write_text(document, encoding="utf-8", newline="\n")
    print(f"wrote {OUT} ({OUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
