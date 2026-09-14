#!/usr/bin/env python
"""Build a versioned reader-facing gallery from the frozen V7 gallery.

The predecessor gallery supplies the already-embedded figures and numerical
tables.  V8 changes the sequence, headings, and captions, and keeps the former
implementation-facing diagnostic panels in one collapsed provenance appendix.
No numerical input is recomputed or reformatted.
"""
from __future__ import annotations

import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "reports/JMP_results_gallery_current.html"
REPORT = ROOT / "reports/JMP_research_story_report_v8.html"
OUT = ROOT / "reports/JMP_results_gallery_v8.html"
BEGIN_MARKER = "<!-- V8_PROVENANCE_APPENDIX_BEGIN -->"
END_MARKER = "<!-- V8_PROVENANCE_APPENDIX_END -->"


def section(document: str, section_id: str) -> str:
    match = re.search(
        rf'<section id="{re.escape(section_id)}">(.*?)</section>',
        document,
        flags=re.S,
    )
    if not match:
        raise RuntimeError(f"missing source-gallery section: {section_id}")
    body = match.group(1)
    body = re.sub(r'^<div class=kicker>.*?</div><h2>.*?</h2>', '', body, count=1,
                  flags=re.S)
    return body


def report_section(document: str, number: int) -> str:
    match = re.search(
        rf'<h1 id="{number}-[^"]+">.*?</h1>(.*?)(?=<h1 id="{number + 1}-|'
        r'<!-- V8_PROVENANCE_APPENDIX_BEGIN -->)',
        document,
        flags=re.S,
    )
    if not match:
        raise RuntimeError(f"missing report section: {number}")
    return match.group(1)


def reader_language(text: str) -> str:
    images = []

    def stash_image(match):
        images.append(match.group(0))
        return f"@@V8_IMAGE_{len(images) - 1}@@"

    text = re.sub(r"<img[^>]*>", stash_image, text, flags=re.S | re.I)
    replacements = (
        ("Accepted Mapping-F construction", "Attained-bundle money metric"),
        ("Mapping-F", "attained-bundle"),
        ("POSFIT node-convergence v3b", "the numerical-convergence diagnostics"),
        ("POSFIT v3b", "the predictive-fit diagnostics"),
        ("DECOMP-2", "the preliminary structural decomposition"),
        ("S11/S10", "the preferred specification"),
        ("S12", "the large predictive integration sample"),
        ("S11", "the preferred specification"),
        ("criterion-A", "the estimation-sample"),
        ("dwt-weighted", "household-weighted"),
        ("dwt", "household weights"),
        ("node-level", "job-specific"),
        ("proposal panel", "numerical integration sample"),
        ("adjudication", "assessment"),
        ("adequacy gate", "numerical-precision standard"),
        (" gate", " standard"),
    )
    for old, new in replacements:
        text = re.sub(re.escape(old), new, text, flags=re.I)
    text = text.replace("W1_F_i", "M_i")
    text = text.replace("W1_F", "the attained-bundle money metric")
    for index, image_tag in enumerate(images):
        text = text.replace(f"@@V8_IMAGE_{index}@@", image_tag)
    return text


def main() -> None:
    source = SOURCE.read_text(encoding="utf-8")
    report = REPORT.read_text(encoding="utf-8")
    style = re.search(r"<style>(.*?)</style>", source, flags=re.S).group(1)
    style += (
        "details{margin:24px 0;padding:18px;background:#f1f2ef;"
        "border:1px solid var(--line);border-radius:8px}"
        "summary{cursor:pointer;font-weight:700}"
        ".tw{overflow:auto;max-width:100%;-webkit-overflow-scrolling:touch}"
    )

    main_sections = [
        ("samples", "Who is studied",
         reader_language(section(source, "samples"))),
        ("observed", "What households do",
         reader_language(section(source, "observed"))),
        ("model", "How preferences and opportunities enter the model",
         reader_language(section(source, "model"))),
        ("fit", "How the model predicts observed behaviour",
         reader_language(section(source, "fit"))),
        ("opportunities", "What the estimated opportunity distributions look like",
         reader_language(section(source, "opportunities"))),
        ("welfare", "How attained bundles become money-metric well-being",
         reader_language(section(source, "welfare"))),
    ]

    current_results = report_section(report, 5)
    behaviour = re.search(
        r'<h2 id="behaviour-and-predictive-fit">(.*?)(?=<h2 id="attained-bundle-well-being">)',
        current_results,
        flags=re.S,
    )
    welfare_results = re.search(
        r'<h2 id="attained-bundle-well-being">(.*?)(?=<h2 id="preliminary-structural-decomposition">)',
        current_results,
        flags=re.S,
    )
    if not behaviour or not welfare_results:
        raise RuntimeError("missing reader-facing fit or welfare subsection")
    main_sections[3] = (
        main_sections[3][0], main_sections[3][1],
        reader_language("<h3>Headline findings</h3>" + behaviour.group(1)
                        + main_sections[3][2]),
    )
    main_sections[5] = (
        main_sections[5][0], main_sections[5][1],
        reader_language(main_sections[5][2]
                        + "<h3>Distributional results</h3>"
                        + welfare_results.group(1)),
    )
    decomposition = re.search(
        r'<h2 id="preliminary-structural-decomposition">(.*)',
        current_results,
        flags=re.S,
    )
    if not decomposition:
        raise RuntimeError("missing reader-facing decomposition subsection")
    decomp_body = "<h3>Numerical results</h3>" + decomposition.group(1)
    main_sections.append((
        "decomposition",
        "What the preliminary decomposition says",
        reader_language(decomp_body),
    ))
    main_sections.append((
        "limitations",
        "What remains preliminary",
        reader_language(report_section(report, 6)),
    ))
    main_sections.append((
        "exante",
        "Why an ex-ante opportunity-prospect extension is useful",
        reader_language(report_section(report, 7)),
    ))

    technical = "".join(
        f'<h3>{html.escape(title)}</h3>{section(source, section_id)}'
        for section_id, title in (
            ("final-diagnostics", "Predictive-fit calculation record"),
            ("decomposition", "Counterfactual-decomposition calculation record"),
            ("robustness", "Robustness and implementation record"),
        )
    )
    provenance = (
        '<p class="lead">The earlier implementation-facing panels are preserved '
        'here so every displayed value and its source context remain available.</p>'
        '<details><summary>Show technical provenance</summary>'
        + technical
        + "</details>"
    )
    all_sections = main_sections + [(
        "provenance", "Technical provenance", provenance,
    )]

    nav = "".join(
        f'<a href="#{sid}"><span>{number:02d}</span>{html.escape(title)}</a>'
        for number, (sid, title, _) in enumerate(all_sections, 1)
    )
    body_parts = []
    for number, (sid, title, content) in enumerate(all_sections, 1):
        rendered_section = (
            f'<section id="{sid}"><div class="kicker">{number:02d} / evidence</div>'
            f'<h2>{html.escape(title)}</h2>{content}</section>'
        )
        if sid == "provenance":
            rendered_section = BEGIN_MARKER + rendered_section + END_MARKER
        body_parts.append(rendered_section)
    body = "".join(body_parts)
    document = (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>Reader-facing results gallery</title><style>' + style + "</style>"
        '</head><body><nav class="sidebar"><div class="brand">Results gallery'
        '<small>Reader-facing evidence · V8</small></div>' + nav + "</nav><main>"
        '<header class="hero"><div class="eyebrow">Economic evidence</div>'
        '<h1>From job opportunities to well-being inequality</h1>'
        '<p>Observed behaviour, the estimated model, attained-bundle well-being '
        'and the preliminary counterfactual decomposition for single-adult and '
        'couple households.</p></header>' + body + "</main></body></html>"
    )
    document = re.sub(r"[ \t]+(?=\n)", "", document)
    # Clean caption and fallback-alt text without touching embedded base64 data.
    def clean_caption(match: re.Match) -> str:
        visible = re.sub(r"weighted using household weights",
                         "household-weighted", match.group(2), flags=re.I)
        visible = re.sub(r"dwt-weighted", "household-weighted", visible,
                         flags=re.I)
        visible = re.sub(r"(?<![A-Za-z0-9])dwt(?![A-Za-z0-9])",
                         "household weights", visible, flags=re.I)
        return match.group(1) + visible + match.group(3)

    document = re.sub(r"(<figcaption\b[^>]*>)(.*?)(</figcaption>)",
                      clean_caption, document, flags=re.S | re.I)
    document = re.sub(r"(<caption\b[^>]*>)(.*?)(</caption>)",
                      clean_caption, document, flags=re.S | re.I)
    document = re.sub(r'(\balt=")([^"]*)(")', clean_caption, document,
                      flags=re.S | re.I)
    standalone_captions = document.count("<figcaption class=standalone>")
    if document.count("<figure") + standalone_captions != document.count("<figcaption"):
        raise RuntimeError("a gallery figure is missing its caption")
    OUT.write_text(document, encoding="utf-8", newline="\n")
    print(f"wrote {OUT} ({OUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
