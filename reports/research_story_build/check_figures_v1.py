#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Document figure check (Goal-1 R-283.2 item 1). FAILS the build when:

  * any of figP01-figP06 is absent from the report; or
  * a caption of record for one of them omits population, units or status; or
  * a preference panel is embedded from a rendering that does not match the
    identified utility scale.

The last clause is the one that matters while SCALE-1 is landing: the panels on
disk were drawn under the old beta_c = 1 numeraire, so embedding them would put
a different utility in front of the reader. Until FIGS-4 regenerates them the
report carries a visible awaiting-regeneration notice and this check fails, by
design and not by accident.

Exit code 0 only if every clause passes.
"""
from __future__ import annotations

import io
import json
import re
import sys
from pathlib import Path

JMP = Path("C:/Users/hisham/Repo/Job_Market_paper")
MNL = Path("C:/Users/hisham/Repo/MNL")
REPORT = JMP / "reports/JMP_research_story_report_v4.html"
PAPER = JMP / "manuscript/JMP_working_paper_for_seminar_v4.tex"
PROV = (MNL / "experiments/JMP_SEMINAR_SPRINT/runs/preference_figures_final"
        / "pff_step1_reference_v1.json")

SIX = ["figP01_indifference_curves_singles",
       "figP02_indifference_curves_couples",
       "figP03_marginal_utilities",
       "figP04_mrs_by_age_sex",
       "figP05_euro_value_of_one_nat",
       "figP06_normalization_sensitivity",
       "figP07_w1_power_mean_weighting"]
PAPER_FOUR = [SIX[0], SIX[2], SIX[3], SIX[5]]
APPENDIX = [SIX[1], SIX[4], SIX[6]]

FAIL: list[str] = []


def main() -> int:
    if not REPORT.exists():
        print("FAIL: report not built")
        return 1
    html = REPORT.read_text(encoding="utf-8", errors="replace")
    tex = PAPER.read_text(encoding="utf-8") if PAPER.exists() else ""

    # ---- 1. all six are present in the report, embedded or explicitly held
    print("1. the six preference panels are present in the report")
    for stem in SIX:
        embedded = ('data-fig="%s"' % stem) in html
        held = ("Figure awaiting regeneration" in html
                and stem in html)
        ok = embedded or held
        print("   %-46s %s" % (stem, "present" if ok else "MISSING"))
        if not ok:
            FAIL.append("%s is absent from the report" % stem)

    # ---- 2. every caption carries population, units and status
    print("2. captions carry population / units / status")
    for stem in SIX:
        i = html.find('data-fig="%s"' % stem)
        if i < 0:
            window = ""
        else:
            a = html.rfind("<figure", 0, i)
            b = html.find("</figure>", i)
            window = html[a if a >= 0 else max(0, i - 4000):
                          (b + 9) if b >= 0 else i + 4000]
        miss = [w for w in ("Population:", "Units:", "Status:")
                if w.lower() not in window.lower()]
        print("   %-46s %s" % (stem, "ok" if not miss else "missing " + ",".join(miss)))
        if miss:
            FAIL.append("%s caption omits %s" % (stem, ", ".join(miss)))

    # ---- 3. the paper carries its four, and not the other two in main text
    print("3. the paper's selection")
    if tex:
        body = tex.split("\\appendix", 1)[0]
        appx = tex.split("\\appendix", 1)[1] if "\\appendix" in tex else ""
        for stem in PAPER_FOUR:
            ok = stem in body or "Figure awaiting regeneration" in body
            print("   main text %-40s %s" % (stem, "present" if ok else "MISSING"))
            if not ok:
                FAIL.append("%s is absent from the paper's main text" % stem)
        for stem in APPENDIX:
            in_body = stem in body
            print("   appendix  %-40s %s"
                  % (stem, "not in main text" if not in_body else "IN MAIN TEXT"))
            if in_body:
                FAIL.append("%s should be in the paper's appendix, not the main "
                            "text" % stem)
    else:
        print("   paper not built; skipped")

    # ---- 4. nothing stale is embedded
    print("4. embedded panels match the identified utility scale")
    scale_ok, why = False, "no provenance record"
    if PROV.exists():
        try:
            rj = json.loads(PROV.read_text("utf-8"))
            bcs = [p.get("beta_c") for p in rj.get("parameters", [])
                   if isinstance(p, dict) and p.get("beta_c") is not None]
            if not bcs:
                why = "provenance does not record beta_c"
            elif any(abs(float(b) - 1.0) < 1e-9 for b in bcs):
                why = ("rendered with beta_c pinned at the old numeraire, "
                       "which the identified scale supersedes")
            else:
                scale_ok = True
                why = "beta_c estimated (%s)" % ", ".join(
                    "%.4f" % float(b) for b in sorted(set(map(float, bcs))))
        except Exception as e:
            why = "unreadable provenance: %s" % e
    print("   provenance: %s" % why)
    embedded_any = any(('data-fig="%s"' % s) in html for s in SIX)
    if embedded_any and not scale_ok:
        FAIL.append("a stale preference panel is embedded (%s)" % why)
    if not scale_ok:
        FAIL.append("preference panels await regeneration on the identified "
                    "scale (%s)" % why)
    print("   embedded: %s" % ("yes" if embedded_any else "no, held for regeneration"))

    print()
    if FAIL:
        print("VERDICT: FAIL (%d)" % len(FAIL))
        for f in FAIL:
            print("  - %s" % f)
        return 1
    print("VERDICT: PASS -- six panels present, captions complete, scale current")
    return 0


if __name__ == "__main__":
    sys.exit(main())
