"""Audit banned vocabulary in rendered V8 HTML outside an exact appendix boundary.

This checker deliberately knows nothing about source modules, section numbers, or
``details`` layout.  It requires one explicit begin/end marker in each rendered
file, removes exactly that byte range, then strips non-rendered content and HTML
tags before scanning the resulting reader-visible text.
"""
from __future__ import annotations

import hashlib
import html
import json
import re
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports/JMP_research_story_report_v8.html"
GALLERY = ROOT / "reports/JMP_results_gallery_v8.html"
OUT_JSON = ROOT / "reports/v8_banned_term_audit.json"
OUT_MD = ROOT / "reports/v8_banned_term_audit.md"
NEGATIVE_JSON = ROOT / "reports/v8_banned_term_negative_control.json"
NEGATIVE_MD = ROOT / "reports/v8_banned_term_negative_control.md"

BEGIN_MARKER = "<!-- V8_PROVENANCE_APPENDIX_BEGIN -->"
END_MARKER = "<!-- V8_PROVENANCE_APPENDIX_END -->"

# These are scanned as delimited terms, case-insensitively.  The final two
# entries cover the failures that the earlier 27-term audit did not enumerate.
BANNED = [
    "S10", "S11", "S12", "POSFIT", "v3b", "DECOMP-2", "criterion-A",
    "Gate 0", "anchor", "node", "proposal panel", "exact-H", "H-F",
    "H-D", "H-X", "NN state", "NN pricing state", "SHA", "hash", "dwt",
    "worktree", "registry", "G1-G9", "adjudication", "gate", "mission",
    "ruling", "Mapping-F", "MECHANICAL_STOCHASTIC_CONDITIONING",
]

REPLACEMENTS = [
    ("Mapping-F attained-bundle money metric", "attained-bundle money metric"),
    ("Corrected POSFIT-v3b predictive evidence", "the corrected predictive-fit diagnostics"),
    ("the corrected S11 evaluation", "the corrected evaluation"),
    ("S12-native full employment-hours width", "the full employment-hours range represented in the predictive integration sample"),
    ("H-F domain", "the ex-ante reference keeps the full opportunity environment fixed while equalising consumption across jobs"),
    ("exact-H pre-validation", "additional counterfactual tax-benefit evaluations are required before the ex-ante measure can be reported reliably"),
    ("dwt-weighted", "household-weighted"),
    ("the estimation panel's anchor node", "the household's own observed job, which the simulation always includes"),
    ("MECHANICAL_STOCHASTIC_CONDITIONING", "the pattern is a mechanical consequence of conditioning on realised outcomes under stochastic choice"),
    ("V7 status note", "deleted from the report; the status statement uses the required ongoing-validation wording and names no version"),
]


class BoundaryError(ValueError):
    """The rendered file does not contain one unambiguous appendix boundary."""


def digest_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def remove_exact_appendix(document: str) -> tuple[str, str]:
    """Return content outside and inside the one explicit appendix boundary."""
    begin_count = document.count(BEGIN_MARKER)
    end_count = document.count(END_MARKER)
    if begin_count != 1 or end_count != 1:
        raise BoundaryError(
            f"expected one marker pair, found begin={begin_count}, end={end_count}"
        )
    begin = document.index(BEGIN_MARKER)
    end = document.index(END_MARKER)
    if begin >= end:
        raise BoundaryError("appendix end marker precedes begin marker")
    appendix_end = end + len(END_MARKER)
    return document[:begin] + document[appendix_end:], document[begin:appendix_end]


def rendered_text(fragment: str) -> str:
    """Reduce rendered HTML to visible text, excluding code, CSS, data and tags."""
    fragment = re.sub(r"<script\b[^>]*>.*?</script\s*>", " ", fragment,
                      flags=re.S | re.I)
    fragment = re.sub(r"<style\b[^>]*>.*?</style\s*>", " ", fragment,
                      flags=re.S | re.I)
    fragment = re.sub(r"data:[^\s\"'>]+", " ", fragment, flags=re.I)
    fragment = re.sub(r"<img\b[^>]*>", " ", fragment, flags=re.S | re.I)
    fragment = re.sub(r"<!--.*?-->", " ", fragment, flags=re.S)
    fragment = re.sub(r"<[^>]+>", " ", fragment, flags=re.S)
    return re.sub(r"\s+", " ", html.unescape(fragment)).strip()


def term_pattern(term: str) -> re.Pattern[str]:
    if term == "G1-G9":
        return re.compile(r"(?<![A-Za-z0-9])G[1-9](?![A-Za-z0-9])", re.I)
    return re.compile(
        r"(?<![A-Za-z0-9])" + re.escape(term) + r"(?![A-Za-z0-9])",
        re.I,
    )


def counts(text: str) -> dict[str, int]:
    return {term: len(term_pattern(term).findall(text)) for term in BANNED}


def scan_path(path: Path) -> dict:
    document = path.read_text(encoding="utf-8")
    outside, appendix = remove_exact_appendix(document)
    visible = rendered_text(outside)
    appendix_visible = rendered_text(appendix)
    hits = counts(visible)
    return {
        "path": str(path.relative_to(ROOT)).replace("\\", "/")
        if path.is_relative_to(ROOT) else str(path),
        "marker_begin_count": document.count(BEGIN_MARKER),
        "marker_end_count": document.count(END_MARKER),
        "rendered_character_count": len(visible),
        "appendix_rendered_character_count": len(appendix_visible),
        "outside_appendix_counts": hits,
        "inside_appendix_counts": counts(appendix_visible),
        "outside_appendix_total": sum(hits.values()),
        "status": "PASS" if not any(hits.values()) else "FAIL",
    }


def negative_control(path: Path) -> dict:
    """Inject S11 before the boundary in a temporary rendered copy and scan it."""
    original = path.read_bytes()
    document = original.decode("utf-8")
    # Validate the real file before constructing the control.
    remove_exact_appendix(document)
    injected = document.replace(
        BEGIN_MARKER,
        '<p id="v8-audit-negative-control">S11</p>\n' + BEGIN_MARKER,
        1,
    )
    temporary_path = None
    observed = None
    with tempfile.TemporaryDirectory(prefix="jmp-v8-negative-control-") as tmp:
        temporary_path = Path(tmp) / path.name
        temporary_path.write_text(injected, encoding="utf-8", newline="\n")
        observed = scan_path(temporary_path)
        existed_during_scan = temporary_path.is_file()
    removed = temporary_path is not None and not temporary_path.exists()
    unchanged = digest_bytes(path.read_bytes()) == digest_bytes(original)
    detected = bool(observed and observed["outside_appendix_counts"]["S11"] > 0)
    observed_failure = bool(observed and observed["status"] == "FAIL")
    passed = detected and observed_failure and existed_during_scan and removed and unchanged
    return {
        "status": "PASS" if passed else "FAIL",
        "injected_term": "S11",
        "injection_location": "rendered HTML immediately before the explicit appendix begin marker",
        "expected_audit_result": "FAIL",
        "observed_audit_result": observed["status"] if observed else "NOT RUN",
        "observed_s11_count": observed["outside_appendix_counts"]["S11"] if observed else 0,
        "temporary_file_existed_during_scan": existed_during_scan,
        "temporary_file_removed": removed,
        "original_sha256_unchanged": unchanged,
        "scanner_pipeline": [
            "remove only the exact marked appendix range",
            "strip script elements",
            "strip style elements",
            "strip base64/data URLs and image tags",
            "strip all remaining tags",
            "decode HTML entities",
            "scan rendered text",
        ],
    }


def write_outputs(surfaces: list[dict], control: dict) -> None:
    status = "PASS" if control["status"] == "PASS" and all(
        item["status"] == "PASS" for item in surfaces
    ) else "FAIL"
    payload = {
        "gate": "V8 rendered-text banned-term audit",
        "status": status,
        "appendix_begin_marker": BEGIN_MARKER,
        "appendix_end_marker": END_MARKER,
        "exclusion_rule": "exclude exactly and only the inclusive rendered-HTML marker range",
        "pipeline": control["scanner_pipeline"],
        "negative_control": control,
        "surfaces": surfaces,
        "replacements": [{"before": old, "after": new} for old, new in REPLACEMENTS],
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8", newline="\n")

    lines = [
        "# V8 rendered-text banned-term audit", "",
        f"Overall: **{status}**", "",
        "The checker reads the rendered HTML, excludes exactly the explicit marker range, strips script/style elements, base64/data URLs, image tags and all remaining tags, decodes HTML entities, and scans the resulting visible text.", "",
        "## Explicit appendix boundary", "",
        f"- Begin: `{BEGIN_MARKER}`",
        f"- End: `{END_MARKER}`",
        "- Exclusion: exactly and only the inclusive range between those markers.", "",
        "## Negative control", "",
        f"- Injected `{control['injected_term']}` {control['injection_location']}.",
        f"- Expected audit result: **{control['expected_audit_result']}**.",
        f"- Observed audit result: **{control['observed_audit_result']}** ({control['observed_s11_count']} hit).",
        f"- Temporary injected file removed: **{str(control['temporary_file_removed']).upper()}**; original SHA-256 unchanged: **{str(control['original_sha256_unchanged']).upper()}**.", "",
        "## Rendered-text scan", "",
        "| Surface | Begin markers | End markers | Hits outside appendix | Status |",
        "|---|---:|---:|---:|---:|",
    ]
    for surface in surfaces:
        lines.append(
            f"| `{surface['path']}` | {surface['marker_begin_count']} | "
            f"{surface['marker_end_count']} | {surface['outside_appendix_total']} | "
            f"**{surface['status']}** |"
        )
    lines.extend(["", "## Term counts outside the appendix", "",
                  "| Banned term | Report | Gallery | Status |",
                  "|---|---:|---:|---:|"])
    for term in BANNED:
        report_count = surfaces[0]["outside_appendix_counts"][term]
        gallery_count = surfaces[1]["outside_appendix_counts"][term]
        row_status = "PASS" if report_count == gallery_count == 0 else "FAIL"
        lines.append(
            f"| `{term}` | {report_count} | {gallery_count} | **{row_status}** |"
        )
    lines.extend(["", "## Required before/after replacements", "",
                  "| Before | After |", "|---|---|"])
    for old, new in REPLACEMENTS:
        lines.append(f"| `{old}` | {new} |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")

    NEGATIVE_JSON.write_text(json.dumps(control, indent=2, ensure_ascii=False) + "\n",
                             encoding="utf-8", newline="\n")
    negative_lines = [
        "# V8 banned-term audit negative control", "",
        f"Overall: **{control['status']}**", "",
        f"A temporary rendered copy received `{control['injected_term']}` {control['injection_location']}. The same scanner was expected to return **FAIL** and returned **{control['observed_audit_result']}** with {control['observed_s11_count']} detected hit.", "",
        f"The temporary file was removed: **{str(control['temporary_file_removed']).upper()}**. The original rendered report's SHA-256 remained unchanged: **{str(control['original_sha256_unchanged']).upper()}**.",
    ]
    NEGATIVE_MD.write_text("\n".join(negative_lines) + "\n", encoding="utf-8",
                           newline="\n")


def main() -> int:
    try:
        surfaces = [scan_path(REPORT), scan_path(GALLERY)]
        control = negative_control(REPORT)
    except BoundaryError as exc:
        print(f"RENDERED-LANGUAGE AUDIT FAIL: {exc}")
        return 1
    write_outputs(surfaces, control)
    status = "PASS" if control["status"] == "PASS" and all(
        item["status"] == "PASS" for item in surfaces
    ) else "FAIL"
    total = sum(item["outside_appendix_total"] for item in surfaces)
    print(
        f"RENDERED-LANGUAGE AUDIT {status}: {total} outside-appendix hits; "
        f"negative control observed {control['observed_audit_result']}"
    )
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
