# -*- coding: utf-8 -*-
"""Build reports/JMP_research_story_report_v2.html in the Job_Market_paper repo."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import common
import shell
import sec_a
import sec_b
import sec_c
import sec_d
from common import FigureBank, n, box, lit
OUT = common.JMP / "reports/JMP_research_story_report_v2.html"

# Reading order required by Goal-1 R-277.  The section modules retain their
# historical source boundaries; the release build assembles them into the
# economic sequence below and remaps section cross-references simultaneously.
SECTION_ORDER = [1, 2, 3, 4, 6, 11, 12, 5, 7, 9, 13, 14,
                 15, 16, 17, 18, 10, 19, 20, 8, 21, 22, 23, 24]
NEW_SECTION = {old: new for new, old in enumerate(SECTION_ORDER, start=1)}
TOC = [
    ("Question, data and model", [
        ("s1", "1", "Executive overview"),
        ("s2", "2", "The original economic problem"),
        ("s3", "3", "Data"),
        ("s4", "4", "What a latent job is"),
        ("s5", "5", "The structural model, complete"),
        ("s6", "6", "Couples"),
        ("s7", "7", "Children"),
    ]),
    ("Estimation and fit", [
        ("s8", "8", "Proposal sampling and the correction"),
        ("s9", "9", "The estimated model, coefficient by coefficient"),
        ("s10", "10", "Does the model fit?"),
    ]),
    ("Welfare, inequality and evidence", [
        ("s11", "11", "The welfare measure"),
        ("s12", "12", "Building the decomposition"),
        ("s13", "13", "Headline results"),
        ("s14", "14", "Endowments and needs"),
        ("s15", "15", "Geographic access"),
        ("s16", "16", "The common-opportunity benchmark"),
        ("s17", "17", "External validation"),
        ("s18", "18", "Robustness and uncertainty"),
    ]),
    ("Limits and use", [
        ("s19", "19", "What this paper does not identify"),
        ("s20", "20", "How this specification was reached"),
        ("s21", "21", "Reproduction: the hands-on guide"),
        ("s22", "22", "Seminar question bank"),
        ("s23", "23", "Self-check: every numeral to its key"),
        ("s24", "24", "Glossary"),
    ]),
]


def reading_order(body_html: str) -> str:
    """Reorder complete h2 sections and keep their references internally valid."""
    starts = list(re.finditer(r'<h2 id="s(\d+)" class="exempt">', body_html))
    if len(starts) != len(SECTION_ORDER):
        raise RuntimeError("expected %d numbered sections, found %d" %
                           (len(SECTION_ORDER), len(starts)))
    preamble = body_html[:starts[0].start()]
    blocks = {}
    for pos, match in enumerate(starts):
        end = starts[pos + 1].start() if pos + 1 < len(starts) else len(body_html)
        blocks[int(match.group(1))] = body_html[match.start():end]

    ordered = []
    for old in SECTION_ORDER:
        new = NEW_SECTION[old]
        block = blocks[old]
        block = re.sub(
            r'(<h2 id=")s%d(" class="exempt">)%d\.' % (old, old),
            lambda match: "%ss%d%s%d." %
            (match.group(1), new, match.group(2), new), block, count=1)
        ordered.append(block)
    assembled = preamble + "".join(ordered)

    # Remap prose references such as “section 19.2” and “sections 13–17” in
    # one callback, avoiding cascaded replacements.
    ref = re.compile(
        r'([Ss]ections?(?:&nbsp;|\s)+)'
        r'(\d+(?:\.\d+)?(?:(?:&nbsp;|\s)*(?:&ndash;|–|-|and|,)(?:&nbsp;|\s)*'
        r'\d+(?:\.\d+)?)*)')

    def remap_ref(match):
        def one(number):
            whole, dot, tail = number.group(0).partition(".")
            mapped = str(NEW_SECTION.get(int(whole), int(whole)))
            return mapped + (dot + tail if dot else "")
        return match.group(1) + re.sub(r'\d+(?:\.\d+)?', one, match.group(2))

    return ref.sub(remap_ref, assembled)


def toc_html() -> str:
    out = ["<h2>Contents</h2>"]
    for grp, items in TOC:
        out.append('<div class="grp">%s</div>' % grp)
        for sid, num, title in items:
            out.append('<a href="#%s" data-sec="%s"><span class="tnum">%s</span>%s</a>'
                       % (sid, sid, num, title))
    return "".join(out)


def front_matter() -> str:
    W = []
    W.append('<h1>Job Opportunities, Preferences, and Well-Being Inequality: '
             "A RURO Analysis of French Singles and Couples</h1>")
    W.append('<p class="sub">First complete discussion draft &mdash; ' +
             lit("10 September 2026", "delivery date") +
             ". The model, evidence, welfare construction and the questions it "
             "invites.</p>")
    W.append('<p class="sub">Single-adult and couple households, France. Every numeral '
             "on this page is rendered from an embedded data block; hover any of them "
             "for its key, its definition and the data file it was read from.</p>")
    W.append(box("warn", "Result status - read before any estimate", (
        "<p><b>Verified facts</b> in this report include the source-to-sample "
        "reconciliation, the executed historical formulas, and the current "
        "chosen-row-free common welfare support. <b>Every displayed behavioural "
        "or welfare estimate is a current-implementation estimate under the "
        "sampled-alternatives criterion presently implemented, not a corrected "
        "bounded-support estimate.</b></p>"
        "<p>The estimator, the structural wage support, all affected parameters, "
        "predictions, welfare results and decomposition results are under correction. "
        "The initial support candidate is a renormalised bounded wage density; the "
        "corrected fit does not yet exist. The four corrected resource-field "
        "classifications also make the earlier nested resource/composition percentages "
        "historical only. The current welfare integrator itself is unaffected by the "
        "chosen-row problem: its common support contains no observed row, so the "
        "chosen-row contribution is exactly zero (<code>WINT-1</code>).</p>"
        "<p>Sources: <code>MNL/docs/corr/target_model_and_integrability_v1.md</code>; "
        "<code>MNL/docs/jmp_methodology/JMP_sampled_alternatives_criterion_audit_v1.md</code>, "
        "as corrected by the welfare mission; and "
        "<code>MNL/docs/corr/fr2016_source_to_estimation_sample_audit_v1.md</code>.</p>")))
    W.append(box("key", "The paper in five lines", (
        "<ul>"
        "<li><b>Question.</b> How much inequality in money-metric well-being is "
        "associated with unequal access to jobs and unequal earning opportunities, "
        "rather than heterogeneous preferences, after separately accounting for "
        "non-labour resources and household composition?</li>"
        "<li><b>Method.</b> Specify one structural population model, estimate it under "
        "the sampling law, integrate that same model on common numerical support, and "
        "attribute inequality with a grouped Shapley rule.</li>"
        "<li><b>Available evidence.</b> The current-implementation estimates suggest "
        "that non-preference circumstances matter, but the corrected magnitudes and "
        "their ordering cannot yet be stated.</li>"
        "<li><b>Correction now running.</b> Re-estimation must combine a justified "
        "sampled-alternatives estimator, bounded and renormalised wage support, "
        "all-member singles resources, and the corrected resource classification.</li>"
        "<li><b>Interpretive limit.</b> Attribution is descriptive and reference-sensitive; "
        "it is neither causal identification nor a moral-responsibility verdict.</li>"
        "</ul>")))
    W.append('<hr class="soft">')
    return "".join(W)


def main() -> int:
    nor = common.load_nor()
    aux = common.build_aux()
    F = FigureBank()

    body = [front_matter()]
    for mod in (sec_a, sec_b, sec_c, sec_d):
        body.extend(mod.sections(F))

    body_html = reading_order("".join(body))
    body_html = re.sub(
        r"<table>(?!<caption>)",
        '<table><caption class="credit"><b>Metadata.</b> Population: identified by the section and row labels. Units: identified by column headings. Measure, reference and observed/model/illustrative status: identified in the table heading and adjacent status statement.</caption>',
        body_html,
    )
    html = shell.page(
        title="JMP research story report",
        toc_html=toc_html(),
        body_html=body_html,
        nor_json=json.dumps(nor, ensure_ascii=False, separators=(",", ":")),
        aux_json=json.dumps(aux, ensure_ascii=False, separators=(",", ":")),
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8")

    print("wrote %s" % OUT)
    print("  size          %.2f MB" % (len(html.encode("utf-8")) / 1024 / 1024))
    print("  figures       %d embedded (%.2f MB of PNG before base64)"
          % (len(F.used), F.bytes / 1024 / 1024))
    print("  NOR entries   %d" % len(nor["entries"]))
    print("  AUX groups    %s" % ", ".join(k for k in aux if not k.startswith("_")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
