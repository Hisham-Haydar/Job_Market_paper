"""Run the established offline browser checks on the V11 report and gallery."""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

import check_v8_render as base


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
base.REPORT = ROOT / "reports/JMP_research_story_report_v11.html"
base.GALLERY = ROOT / "reports/JMP_results_gallery_v11.html"
base.OUT = ROOT / "reports/v11_render_gate.json"
base.SCREEN_REPORT = Path(tempfile.gettempdir()) / "jmp_v11_report_results.png"
base.SCREEN_GALLERY = Path(tempfile.gettempdir()) / "jmp_v11_gallery_opening.png"


def main() -> int:
    result = base.main()
    payload = json.loads(base.OUT.read_text(encoding="utf-8"))
    payload["gate"] = "V11 offline render"
    base.OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8", newline="\n")
    return result


if __name__ == "__main__":
    raise SystemExit(main())
