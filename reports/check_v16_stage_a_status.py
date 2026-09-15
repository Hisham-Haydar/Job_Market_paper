"""Stage A status gate for V12, with a negative control that must fire.

Every present-tense claim that the ex-ante metric is blocked, not computed,
definition-only or has no result must sit inside a passage labelled
"Superseded before V9". The check reads the full rendered text of the report and
gallery (appendix included) and fails on any unlabelled occurrence.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "reports"))
import check_v16_rendered_language as audit  # noqa: E402

REPORT = ROOT / "reports/JMP_research_story_report_v16.html"
GALLERY = ROOT / "reports/JMP_results_gallery_v15.html"
OUT_JSON = ROOT / "reports/v16_stage_a_status_results.json"
LABEL = "Superseded before V9"
WINDOW = 2500
STALE = re.compile(
    r"definition-only|numerically blocked|has no numerical result|"
    r"no numerical result is reported|no number for that metric is reported|"
    r"currently block numerical implementation|ex-ante[^.]{0,80}\b(?:is|remains) "
    r"(?:blocked|unavailable|not computed|not yet computed)|"
    r"ex-ante metric is being reconstructed",
    flags=re.I,
)


def unlabelled(text: str) -> list[str]:
    misses = []
    for match in STALE.finditer(text):
        preceding = text[max(0, match.start() - WINDOW):match.start()]
        if LABEL not in preceding:
            misses.append(text[max(0, match.start() - 120):match.end() + 60])
    return misses


def scan(document: str) -> dict:
    text = audit.rendered_text(document)
    hits = len(STALE.findall(text))
    misses = unlabelled(text)
    return {"stale_occurrences": hits, "labels": text.count(LABEL),
            "unlabelled": misses, "status": "PASS" if not misses else "FAIL"}


def main() -> int:
    report_doc = REPORT.read_text(encoding="utf-8")
    gallery_doc = GALLERY.read_text(encoding="utf-8")
    report = scan(report_doc)
    gallery = scan(gallery_doc)
    injected = report_doc.replace(
        audit.BEGIN_MARKER,
        "<p>The ex-ante metric is definition-only and numerically blocked.</p>"
        + audit.BEGIN_MARKER, 1)
    control = scan(injected)
    control_ok = control["status"] == "FAIL" and len(control["unlabelled"]) >= 1
    status = ("PASS" if report["status"] == gallery["status"] == "PASS" and control_ok
              else "FAIL")
    payload = {"gate": "V16 Stage A ex-ante status", "status": status,
               "report": report, "gallery": gallery,
               "negative_control": {"injected": "unlabelled blocked-status sentence "
                                                "before the appendix marker",
                                    "expected": "FAIL", "observed": control["status"],
                                    "unlabelled_found": len(control["unlabelled"]),
                                    "status": "PASS" if control_ok else "FAIL"}}
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8", newline="\n")
    print(f"V16 STAGE A STATUS {status}: report {report['stale_occurrences']} stale / "
          f"{len(report['unlabelled'])} unlabelled; gallery {gallery['stale_occurrences']} / "
          f"{len(gallery['unlabelled'])}; negative control observed {control['status']}")
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
