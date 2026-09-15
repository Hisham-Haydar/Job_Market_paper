#!/usr/bin/env python
"""Build the V11 gallery from the released V10 gallery and the V11 report.

V11 reorganises the welfare evidence as two perspectives, adds the
matched-household illustration, replaces the decomposition, central-result and
limitation panels with the V11 report text, and keeps every embedded figure and
table from V10. Displayed numbers are read from the V11 registry, never typed.
"""
from __future__ import annotations

import base64
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "reports/research_story_build"))
import v11_render_inputs as inputs  # noqa: E402
import v11_sections as sections  # noqa: E402

SOURCE = ROOT / "reports/JMP_results_gallery_v10.html"
REPORT = ROOT / "reports/JMP_research_story_report_v11.html"
OUT = ROOT / "reports/JMP_results_gallery_v11.html"
BEGIN_V10 = "<!-- V10_PROVENANCE_APPENDIX_BEGIN -->"
END_V10 = "<!-- V10_PROVENANCE_APPENDIX_END -->"
BEGIN_V11 = "<!-- V11_PROVENANCE_APPENDIX_BEGIN -->"
END_V11 = "<!-- V11_PROVENANCE_APPENDIX_END -->"


def reg(key: str, fmt: str) -> str:
    return format(float(inputs.REG[key]["value"]), fmt)


def report_h1_body(document: str, number: int) -> str:
    match = re.search(
        rf'<h1 id="{number}-[^"]+">.*?</h1>(.*?)(?=<h1 id="|{re.escape(BEGIN_V11)})',
        document, flags=re.S)
    if not match:
        raise RuntimeError(f"missing V11 report section {number}")
    return match.group(1)


def report_h2(document: str, heading_id: str) -> str:
    match = re.search(
        rf'<h2 id="{re.escape(heading_id)}">.*?</h2>(.*?)(?=<h2 id="|<h1 id="|{re.escape(BEGIN_V11)})',
        document, flags=re.S)
    if not match:
        raise RuntimeError(f"missing V11 report subsection {heading_id}")
    return match.group(1)


def replace_section(document: str, section_id: str, title: str, body: str) -> str:
    pattern = re.compile(
        rf'(<section id="{re.escape(section_id)}"><div class="kicker">'
        r'.*?</div><h2>).*?(</h2>)(.*?)(</section>)', flags=re.S)
    document, count = pattern.subn(
        lambda m: m.group(1) + title + m.group(2) + body + m.group(4), document, count=1)
    if count != 1:
        raise RuntimeError(f"missing V10 gallery section {section_id}")
    return document


def section_body(document: str, section_id: str) -> str:
    match = re.search(
        rf'<section id="{re.escape(section_id)}"><div class="kicker">.*?</div><h2>.*?</h2>(.*?)</section>',
        document, flags=re.S)
    if not match:
        raise RuntimeError(f"missing V10 gallery section {section_id}")
    return match.group(1)


def main() -> None:
    document = SOURCE.read_text(encoding="utf-8")
    report = REPORT.read_text(encoding="utf-8")

    welfare_lead = (
        "<p class=lead>" + sections.PERSPECTIVES_SENTENCE + "</p>"
        "<div class=notice><strong>ATT — attained-bundle welfare.</strong> How well off "
        "is the household in the bundle it actually attains?"
        "<code class=formula>M_att_i = C_obs_i * exp{[L_i(j_obs) - L_i(o)] / beta_c}</code>"
        "Opportunities reach this measure through the outcome eventually attained. "
        "On the current empirical domain it coincides with the staying-home equivalent.</div>"
        "<div class=notice><strong>EA — ex-ante opportunity-prospect welfare.</strong> How "
        "valuable is the distribution of job prospects the household faces?"
        "<code class=formula>J_i = &int; exp{L_i(j)} (C_i(j)/lambda_c)^beta_c g_i(j) dnu(j);  "
        "H_i = &int; exp{L_i(j)} g_i(j) dnu(j);  "
        "M_EA_i = lambda_c exp{[log J_i - log H_i] / beta_c}</code>"
        "It values the whole estimated opportunity prospect against a reference with the "
        "same opportunities and equal consumption across jobs.</div>"
        "<p>Neither perspective corrects the other, and neither is designated primary. "
        "The panels below show the attained-bundle distribution; the ex-ante distribution "
        "is reported with the decompositions.</p>"
    )
    welfare_old = section_body(document, "welfare")
    welfare_old = re.sub(r'^<div class=notice><strong>Attained-bundle money metric\.</strong>.*?</p>\s*<p>.*?</p>',
                         "", welfare_old, count=1, flags=re.S)
    document = replace_section(document, "welfare",
                               "From choices to well-being: outcomes versus prospects",
                               welfare_lead + welfare_old)

    figure = inputs.MATCHED_FIG
    caption = re.search(r"!\[(.*?)\]\(", inputs.CAPTIONS["matched"], flags=re.S).group(1)
    matched_html = (
        "<h3>Two matched households</h3>"
        "<p>Two employed single men who share occupation group, hours band and observed-wage "
        "quintile and have nearly identical estimated leisure profiles face different "
        f"opportunity environments. Household A's employment mass is {reg('mh_access_ratio', '.1f')} "
        "times household B's; B's wage-offer location is "
        f"{reg('mh_wage_gap', '.1f')} log points higher, so B's wage-offer distribution "
        "first-order stochastically dominates A's while A faces more offers paying at least any "
        "given wage over essentially all offer mass. Hours and occupation opportunities are "
        "identical by construction. Neither household is better placed on every margin. "
        "The pair is a stated-rule teaching example, not causal and not representative.</p>"
        '<figure class=""><img alt="Matched-household opportunity illustration" src="data:image/png;base64,'
        + base64.b64encode(figure.read_bytes()).decode()
        + f'"><figcaption>{caption}</figcaption></figure>'
    )
    document = replace_section(document, "opportunities",
                               "What the estimated opportunity distributions look like",
                               section_body(document, "opportunities") + matched_html)

    decomposition = (
        "<p class=lead>" + sections.D_STATUS + " Household resources, needs and composition "
        "receive no allocated share; adding them is a planned extension.</p>"
        "<h3>Attained-bundle perspective (ATT)</h3>"
        + report_h2(report, "attained-bundle-decomposition")
        + "<h3>Ex-ante perspective (EA)</h3>"
        + report_h2(report, "ex-ante-well-being-and-decomposition")
    )
    document = replace_section(document, "decomposition", "What the two decompositions say",
                               decomposition)

    central = report_h2(report, "the-central-result-outcomes-versus-prospects")
    document = replace_section(
        document, "exante",
        "The central result: the welfare question changes which labour-market inequality matters",
        central
        + "<p>For couples, equivalisation moves the ex-ante access-plus-earnings share from "
        f"{reg('wea_couples_opportunity_uneq_pct', '.1f')}% to "
        f"{reg('wea_couples_opportunity_eq_pct', '.1f')}% of baseline inequality and turns the "
        "preference contribution negative. The scale convention is materially consequential, "
        "so no directional preference claim is made.</p>")

    document = replace_section(document, "limitations", "What remains preliminary",
                               report_h1_body(report, 6))

    nav_titles = {
        "welfare": "From choices to well-being: outcomes versus prospects",
        "decomposition": "What the two decompositions say",
        "limitations": "What remains preliminary",
        "exante": "The central result: outcomes versus prospects",
    }
    for sid, title in nav_titles.items():
        document, count = re.subn(
            rf'(<a href="#{sid}"><span>\d+</span>).*?(</a>)',
            lambda m: m.group(1) + title + m.group(2), document, count=1)
        if count != 1:
            raise RuntimeError(f"missing gallery navigation link {sid}")
    document = re.sub(r"<title>.*?</title>",
                      "<title>" + sections.TITLE + " · Results gallery</title>",
                      document, count=1, flags=re.S)
    document = document.replace("Reader-facing evidence · V10", "Reader-facing evidence · V11")
    document = document.replace(BEGIN_V10, BEGIN_V11).replace(END_V10, END_V11)
    if document.count(BEGIN_V11) != 1 or document.count(END_V11) != 1:
        raise RuntimeError("V11 gallery must contain exactly one appendix marker pair")
    standalone = document.count("<figcaption class=standalone>")
    if document.count("<figure") + standalone != document.count("<figcaption"):
        raise RuntimeError("a gallery figure is missing its caption")
    OUT.write_text(document, encoding="utf-8", newline="\n")
    print(f"wrote {OUT} ({OUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
