"""Write the V11 surface manifest (paths, sizes, SHA-256) after the suite passes."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
WEA_ROOT = WORKSPACE / "MNL_wea"
OUT_JSON = ROOT / "reports/v11_surface_manifest.json"
B = "reports/research_story_build/"

SURFACES = {
    "report HTML": ROOT / "reports/JMP_research_story_report_v11.html",
    "reader-facing gallery": ROOT / "reports/JMP_results_gallery_v11.html",
    "editable resolved Markdown": ROOT / (B + "story_v11.generated.md"),
    "editable section source": ROOT / (B + "v11_sections.py"),
    "illustration text source": ROOT / (B + "v11_illustration.py"),
    "numerical input adapter": ROOT / (B + "v11_render_inputs.py"),
    "report builder": ROOT / (B + "build_v11.py"),
    "gallery builder": ROOT / "reports/results_gallery_build/build_v11.py",
    "matched-household generator": ROOT / (B + "make_v11_matched_households.py"),
    "matched-household record": ROOT / "reports/v11_matched_households.json",
    "matched-household figure": ROOT / "manuscript/figures/v11/fig_matched_households_v11.png",
    "V11 numerical registry": ROOT / "reports/numbers_of_record_v11.json",
    "deck source": ROOT / "beamer/JMP_seminar_deck_r11.tex",
    "deck numerical macros": ROOT / "beamer/deck_numbers_r11.tex",
    "presentation PDF": ROOT / "beamer/build/JMP_seminar_deck_r11.pdf",
    "rehearsal PDF": ROOT / "beamer/build/JMP_seminar_deck_r11_rehearsal.pdf",
    "rehearsal script": ROOT / "reports/rehearsal_pack_v11.md",
    "executed canonical notebook": WEA_ROOT / "experiments/JMP_SEMINAR_SPRINT/JMP_canonical_AtoZ.ipynb",
    "complete gate summary": ROOT / "reports/v11_release_gate_summary.md",
}


def main() -> None:
    gate = json.loads((ROOT / "reports/v11_release_gate_summary.json").read_text(encoding="utf-8"))
    if gate["status"] != "PASS":
        raise SystemExit("V11 release suite has not passed")
    missing = [str(p) for p in SURFACES.values() if not p.is_file()]
    if missing:
        raise SystemExit("Missing release inputs:\n" + "\n".join(missing))
    rows = [{"surface": name, "path": str(path.relative_to(WORKSPACE)).replace("\\", "/"),
             "bytes": path.stat().st_size, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
            for name, path in SURFACES.items()]
    payload = {"release": "V11", "status": "PASS",
               "constraints": {"reestimation": False, "repricing": False, "welfare_recomputed": False,
                               "decomposition_recomputed": False, "certified_values_changed": False,
                               "v9_overwritten": False, "v10_overwritten": False,
                               "neither_welfare_perspective_designated_primary": True},
               "surfaces": rows}
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print(f"wrote {OUT_JSON} ({len(rows)} surfaces)")


if __name__ == "__main__":
    main()
