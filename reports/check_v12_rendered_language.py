"""Run the unchanged V8 banned-term audit, with its negative control, on V12."""
from __future__ import annotations

import json
from pathlib import Path

import check_v8_rendered_language as base


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports/JMP_research_story_report_v12.html"
GALLERY = ROOT / "reports/JMP_results_gallery_v12.html"
OUT_JSON = ROOT / "reports/v12_banned_term_audit.json"
OUT_MD = ROOT / "reports/v12_banned_term_audit.md"
NEGATIVE_JSON = ROOT / "reports/v12_banned_term_negative_control.json"
NEGATIVE_MD = ROOT / "reports/v12_banned_term_negative_control.md"
BEGIN_MARKER = "<!-- V12_PROVENANCE_APPENDIX_BEGIN -->"
END_MARKER = "<!-- V12_PROVENANCE_APPENDIX_END -->"


def _configure() -> None:
    base.ROOT = ROOT
    base.REPORT = REPORT
    base.GALLERY = GALLERY
    base.OUT_JSON = OUT_JSON
    base.OUT_MD = OUT_MD
    base.NEGATIVE_JSON = NEGATIVE_JSON
    base.NEGATIVE_MD = NEGATIVE_MD
    base.BEGIN_MARKER = BEGIN_MARKER
    base.END_MARKER = END_MARKER


def remove_exact_appendix(document: str):
    _configure()
    return base.remove_exact_appendix(document)


def rendered_text(fragment: str) -> str:
    return base.rendered_text(fragment)


def scan_path(path: Path) -> dict:
    _configure()
    return base.scan_path(path)


def negative_control(path: Path) -> dict:
    _configure()
    return base.negative_control(path)


def main() -> int:
    _configure()
    result = base.main()
    for path in (OUT_MD, NEGATIVE_MD):
        text = path.read_text(encoding="utf-8").replace("V8", "V12")
        path.write_text(text, encoding="utf-8", newline="\n")
    payload = json.loads(OUT_JSON.read_text(encoding="utf-8"))
    payload["gate"] = "V12 rendered-text banned-term audit"
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8", newline="\n")
    return result


if __name__ == "__main__":
    raise SystemExit(main())
