"""Build V12 surfaces, run the complete release suite, and write one summary.

V12 is a structural edit of the report and gallery. The deck, rehearsal script and
notebook are unchanged from V11 and are verified as regressions, including their
synchronisation with the V12 report and gallery.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WEA_ROOT = ROOT.parent / "MNL_wea"
OUT_JSON = ROOT / "reports/v12_release_gate_summary.json"
OUT_MD = ROOT / "reports/v12_release_gate_summary.md"


def run(label: str, command: list[str], cwd: Path = ROOT) -> dict:
    proc = subprocess.run(command, cwd=cwd, text=True, encoding="utf-8", errors="replace",
                          capture_output=True)
    encoding = sys.stdout.encoding or "utf-8"
    for stream, target in ((proc.stdout, sys.stdout), (proc.stderr, sys.stderr)):
        if stream:
            print(stream.encode(encoding, errors="replace").decode(encoding), end="", file=target)
    return {"gate": label, "status": "PASS" if proc.returncode == 0 else "FAIL",
            "returncode": proc.returncode, "command": command,
            "output_tail": (proc.stdout + proc.stderr)[-4000:]}


def main() -> int:
    py = sys.executable
    sprint = "experiments/JMP_SEMINAR_SPRINT/"
    results = [
        run("report build", [py, "reports/research_story_build/build_v12.py"]),
        run("gallery build", [py, "reports/results_gallery_build/build_v12.py"]),
        run("rendered-text language and negative control", [py, "reports/check_v12_rendered_language.py"]),
        run("Stage A ex-ante status and negative control", [py, "reports/check_v12_stage_a_status.py"]),
        run("body/appendix section-title uniqueness and negative control", [py, "reports/check_v12_section_titles.py"]),
        run("reader structure and economic derivation", [py, "reports/check_v12_reader_gates.py"]),
        run("number-to-source", [py, "reports/check_v12_numbers_against_source.py"]),
        run("offline HTML render", [py, "reports/research_story_build/check_v12_render.py"]),
        run("cross-surface synchronisation", [py, "reports/check_v12_synced_surfaces.py"]),
        run("deck verification (R11, unchanged)", [py, "beamer/verify_deck_r11.py"]),
        run("executed notebook verification (V11, unchanged)", [py, sprint + "verify_canonical_notebook_v11.py"], WEA_ROOT),
        run("Python source compilation", [py, "-m", "py_compile",
            "reports/research_story_build/build_v12.py", "reports/research_story_build/v12_sections.py",
            "reports/research_story_build/v12_render_inputs.py", "reports/results_gallery_build/build_v12.py",
            "reports/check_v12_rendered_language.py", "reports/check_v12_stage_a_status.py",
            "reports/check_v12_section_titles.py", "reports/check_v12_reader_gates.py",
            "reports/check_v12_numbers_against_source.py", "reports/check_v12_synced_surfaces.py",
            "reports/research_story_build/check_v12_render.py", "reports/write_v12_release_manifest.py"]),
        run("V9, V10 and V11 byte-preservation", ["git", "diff", "--exit-code", "--",
            "reports/JMP_research_story_report_v9.html", "reports/JMP_results_gallery_v9.html",
            "reports/JMP_research_story_report_v10.html", "reports/JMP_results_gallery_v10.html",
            "reports/JMP_research_story_report_v11.html", "reports/JMP_results_gallery_v11.html",
            "reports/numbers_of_record_v11.json", "reports/research_story_build/v11_sections.py",
            "reports/research_story_build/story_v11.generated.md", "reports/v11_matched_households.json",
            "manuscript/figures/v11/fig_matched_households_v11.png", "beamer/JMP_seminar_deck_r11.tex"]),
    ]
    status = "PASS" if all(item["status"] == "PASS" for item in results) else "FAIL"
    OUT_JSON.write_text(json.dumps({"release": "V12", "status": status, "gates": results},
                                   indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    lines = ["# V12 complete release gate summary", "", f"Overall: **{status}**", "",
             "| Gate | Status | Evidence |", "|---|---:|---|"]
    for item in results:
        tail = item["output_tail"].strip().splitlines()
        detail = (tail[-1] if tail else "completed").replace("|", "\\|")
        lines.append(f"| {item['gate']} | **{item['status']}** | {detail} |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print("V12 RELEASE", status)
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
