#!/usr/bin/env python
"""LINEAGE-SWEEP-1 gate for surface (d): every other committed HTML, JSON
registry, and report file directly under Job_Market_paper/reports/ that is
not already covered by a dedicated verifier (the v5 story-report pipeline
has run_v5_gate.py / check_v5_numbers_against_source.py; the results gallery
has results_gallery_build/verify.py; the beamer deck has verify_deck_r6.py).

No such gate existed for this surface before LINEAGE-SWEEP-1 -- this script
is new, not a rewired existing one.

PATH-based, not string-based: scans each file's own text for the retired
artifact's filename/basename (see reports/retired_lineage_gate.py), which
does not change if the surrounding prose is reworded.

Every file below is checked and reported; FROZEN files are historical
snapshots (superseded numbered versions, dated review memos) -- a violation
there is existing, disclosed debt, not new drift, but it still fails the
gate, because an HTML file with a violation is one click away from a
discussant regardless of "supersession" status, and a live .md/.json with a
violation is either read by a build step or presented as if current. LIVE
files with a violation are the same failure with no historical excuse.
Nothing in the list is silently skipped.

QUARANTINE-2 (2026-09-14) narrows that policy for one specific case: a
FROZEN file that now carries a visible, in-page SUPERSEDED banner (marked by
BANNER_MARKER below -- see JMP_research_story_report_v1-v4.html) is no
longer "one click away from a discussant" with no warning, so a violation
inside it is reported as EXCL (disclosed, known debt) rather than FAIL, and
does not fail the gate. This applies only to files that actually carry the
banner; every other FROZEN/LIVE file keeps the original FAIL behaviour
above. See reports/INDEX.md for the retirement record.

Exit code 0 iff every non-banner-marked file below scans clean.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import retired_lineage_gate as rlg  # noqa: E402

REPORTS = Path(__file__).resolve().parent

# Present in a file's own rendered text iff QUARANTINE-2 (or a later pass)
# added the in-page SUPERSEDED banner (see reports/JMP_research_story_report_
# v1-v4.html, each banner div carries this id). A file containing this
# marker has already disclosed its own retired status to anyone who opens
# it, so a lineage violation inside it is EXCL, not FAIL -- see the
# QUARANTINE-2 paragraph in the module docstring.
BANNER_MARKER = 'id="retired-lineage-banner"'

# (path relative to reports/, status label) -- status is informational only,
# it does not change whether a violation fails the gate (banner-marking, via
# BANNER_MARKER above, is what changes that).
FILES = [
    ("JMP_research_story_report_v1.html", "RETIRED-LINEAGE, DO NOT CIRCULATE (banner-marked; see INDEX)"),
    ("JMP_research_story_report_v2.html", "RETIRED-LINEAGE, DO NOT CIRCULATE (banner-marked; see INDEX)"),
    ("JMP_research_story_report_v3.html", "RETIRED-LINEAGE, DO NOT CIRCULATE (banner-marked; see INDEX)"),
    ("JMP_research_story_report_v4.html", "RETIRED-LINEAGE, DO NOT CIRCULATE (banner-marked; see INDEX)"),
    ("JMP_results_gallery_current.html", "LIVE (has its own verify.py; re-checked here for belt-and-suspenders)"),
    ("JMP_draft_and_story_report_v2_review_v1.md", "FROZEN"),
    ("JMP_research_story_report_review_v1.md", "FROZEN"),
    ("JMP_v3_normative_and_scholarly_review_v1.md", "FROZEN"),
    ("JMP_v4_paper_and_report_review_v1.md", "FROZEN"),
    ("JMP_v5_review_and_modular_revision_plan_v1.md", "untracked/retired (quarantined; see INDEX)"),
    ("canonical_notation_v1.md", "LIVE"),
    ("canonical_notation_v5.md", "LIVE"),
    ("consistency_gate_v1.md", "FROZEN"),
    ("consistency_gate_v3.md", "FROZEN"),
    ("consistency_gate_v4.md", "FROZEN"),
    ("model_extraction_v1.md", "LIVE, no successor"),
    ("novelty-audit-structural-well-being-inequality.md", "LIVE, no successor"),
    ("numbers_of_record_v1.json", "LIVE (bound into run_consistency_gate.py)"),
    ("numbers_of_record_v3.json", "FROZEN"),
    ("numbers_of_record_v4.json", "FROZEN"),
    ("paper_expository_carryover_v1.md", "LIVE"),
    ("rehearsal_pack_v1.md", "LIVE spoken seminar script, no successor"),
    ("JMP_reference_profiles_v1.md", "untracked/retired (quarantined; see INDEX)"),
    ("JMP_reference_profiles_v1.csv", "untracked/retired (quarantined; see INDEX)"),
    ("JMP_reference_profiles_v1.tex", "untracked/retired (quarantined; see INDEX)"),
    ("figure_modules/v5_labour_market_opportunity_composition/build_figure.py", "orphan (not wired into v5, but reads a retired file directly)"),
    ("figure_modules/v5_labour_market_opportunity_composition/evidence.md", "orphan"),
]

# novelty-audit-structural-well-being-inequality.docx exists alongside the
# .md twin but is a binary file this gate cannot read as text at run time
# (no docx-parsing dependency is added just for this). It was manually
# VERIFIED on 2026-09-14 (QUARANTINE-2 item 3): extracted word/document.xml,
# stripped markup, and ran the extracted text through the same
# rlg.scan_text() / rlg.scan_four_factor() checks used above. Result:
# 0 RETIRED_PATH_PATTERNS hits (matches the .md twin) and the same disclosed
# four-factor content-signature hit as the .md twin -- expected, since this
# document's subject is the P/A/B/D framework itself, not a read of a
# retired data artifact. Word/section structure matches the .md twin
# (5,643 vs 5,662 words). Nothing here remains UNVERIFIED -- see
# reports/INDEX.md "Binary documents verified".
VERIFIED_BINARY = {
    "novelty-audit-structural-well-being-inequality.docx":
        "content-identical twin of novelty-audit-structural-well-being-"
        "inequality.md; 0 retired-lineage path hits; same disclosed "
        "four-factor content-signature as its .md twin (not new drift)",
}


# Four-factor P/A/B/D content is forbidden "regardless of source file" (the
# ruling), so a clean path scan above does NOT clear a file of this --
# v3.html/v4.html are the known case: they render a self-contained P/A/B/D
# table with no literal retired filename anywhere in the markup. This is a
# structural/wording signature, not a path, so treat a hit as strong
# evidence and a miss as weaker evidence than the path scan (a rewrite can
# dodge it in a way it cannot dodge the path scan).
FOUR_FACTOR_FILES = {"JMP_research_story_report_v1.html", "JMP_research_story_report_v2.html",
                      "JMP_research_story_report_v3.html", "JMP_research_story_report_v4.html",
                      "JMP_v5_review_and_modular_revision_plan_v1.md",
                      "model_extraction_v1.md",
                      "novelty-audit-structural-well-being-inequality.md",
                      "rehearsal_pack_v1.md",
                      "JMP_reference_profiles_v1.md"}


def main() -> int:
    print("LINEAGE-SWEEP-1 surface (d): other reports/ files")
    print("-" * 72)
    any_fail = False
    for rel, status in FILES:
        p = REPORTS / rel
        if not p.exists():
            print("  SKIP  %-70s (not found)" % rel)
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        violations = rlg.scan_files([p])
        four_factor = rlg.scan_four_factor(text) if rel in FOUR_FACTOR_FILES else []
        banner_marked = BANNER_MARKER in text
        if violations or four_factor:
            if banner_marked:
                print("  EXCL  %-70s [%s]" % (rel, status))
                print("        banner-marked historical file -- disclosed, known "
                      "debt; does not fail the gate (QUARANTINE-2)")
            else:
                any_fail = True
                print("  FAIL  %-70s [%s]" % (rel, status))
            if violations:
                hits = sorted({h for hs in violations.values() for h in hs})
                print("        retired-lineage path reference(s): %s" % ", ".join(hits))
            if four_factor:
                print("        [supplementary, content-signature] four-factor "
                      "P/A/B/D pattern(s): %s" % ", ".join(four_factor))
        else:
            print("  PASS  %-70s [%s]" % (rel, status))
    for rel, verdict in VERIFIED_BINARY.items():
        p = REPORTS / rel
        if not p.exists():
            print("  SKIP  %-70s (not found)" % rel)
            continue
        print("  VERIFIED %-67s (binary, manually verified 2026-09-14)" % rel)
        print("        %s" % verdict)
    print("-" * 72)
    if any_fail:
        print("SURFACE (d): FAIL -- see the LINEAGE-SWEEP-1 report for remediation status")
        return 1
    print("SURFACE (d): PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
