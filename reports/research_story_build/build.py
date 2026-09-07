# -*- coding: utf-8 -*-
"""Build reports/JMP_research_story_report_v1.html in the Job_Market_paper repo."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import common
import shell
import sec_a
import sec_b
import sec_c
import sec_d
from common import FigureBank, n, box

OUT = common.JMP / "reports/JMP_research_story_report_v1.html"

TOC = [
    ("The paper", [
        ("s1", "1", "Executive overview"),
        ("s2", "2", "The original economic problem"),
        ("s3", "3", "Data"),
        ("s4", "4", "What a latent job is"),
        ("s5", "5", "Proposal sampling and the correction"),
        ("s6", "6", "The structural model, complete"),
    ]),
    ("The estimates", [
        ("s7", "7", "The estimated model, coefficient by coefficient"),
        ("s8", "8", "How this specification was reached"),
        ("s9", "9", "Does the model fit?"),
        ("s10", "10", "External validation"),
        ("s11", "11", "Couples"),
        ("s12", "12", "Children"),
    ]),
    ("The welfare results", [
        ("s13", "13", "The welfare measure"),
        ("s14", "14", "Building the decomposition"),
        ("s15", "15", "Headline results"),
        ("s16", "16", "Endowments and needs"),
        ("s17", "17", "Geographic access"),
        ("s18", "18", "The common-opportunity benchmark"),
    ]),
    ("Limits and use", [
        ("s19", "19", "Robustness and uncertainty"),
        ("s20", "20", "What this paper does not identify"),
        ("s21", "21", "Reproduction: the hands-on guide"),
        ("s22", "22", "Seminar question bank"),
        ("s23", "23", "Self-check: every numeral to its key"),
    ]),
]


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
    W.append('<h1>Opportunities, preferences, and the anatomy of welfare '
             "inequality</h1>")
    W.append('<p class="sub">A research and presentation manual for the job market '
             "paper &mdash; the model, the estimates, the decomposition, and the "
             "answers to the questions it invites.</p>")
    W.append('<p class="sub">Single-adult and couple households, France. Every numeral '
             "on this page is rendered from an embedded data block; hover any of them "
             "for its key, its definition and the artefact it came from.</p>")
    W.append(box("key", "The paper in five lines", (
        "<ul>"
        "<li><b>Question.</b> How much of welfare inequality is preference, and how "
        "much is the environment people face?</li>"
        "<li><b>Method.</b> Estimate the opportunity distribution and preferences "
        "jointly, with the tax-benefit system solved exactly at every alternative; then "
        "decompose an opportunity-sensitive money-metric welfare measure by Shapley "
        "attribution.</li>"
        "<li><b>Headline.</b> Preferences " + n("C_pref_female_raw_share", "pct", 1)
        + ", the non-preference environment " + n("C_env_female_raw_share", "pct", 1)
        + " &mdash; of which endowments and needs "
        + n("C_needs_female_raw_share", "pct", 1) + ", earning opportunities "
        + n("C_earn_female_raw_share", "pct", 1) + ", job access "
        + n("C_acc_female_raw_share", "pct", 1) + ", almost all of it geographic.</li>"
        "<li><b>Benchmark.</b> Removing opportunity heterogeneity reverses the sign of "
        "the estimated sex difference in leisure valuation and cuts measured inequality "
        "by " + n("rum_inequality_drop_raw", "pctabs", 1) + " &mdash; but it does "
        "<em>not</em> raise the preference share.</li>"
        "<li><b>Main caveat.</b> The preference contribution is reference-sensitive; "
        "the dominance of the environment is not.</li>"
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

    html = shell.page(
        title="JMP research story report",
        toc_html=toc_html(),
        body_html="".join(body),
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
