"""Build V11 surfaces, run the complete release suite, and write one summary."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
WEA_ROOT = WORKSPACE / "MNL_wea"
OUT_JSON = ROOT / "reports/v11_release_gate_summary.json"
OUT_MD = ROOT / "reports/v11_release_gate_summary.md"


def run(label: str, command: list[str], cwd: Path = ROOT) -> dict:
    proc = subprocess.run(command, cwd=cwd, text=True, encoding="utf-8", errors="replace",
                          capture_output=True)
    encoding = sys.stdout.encoding or "utf-8"
    if proc.stdout:
        print(proc.stdout.encode(encoding, errors="replace").decode(encoding), end="")
    if proc.stderr:
        print(proc.stderr.encode(encoding, errors="replace").decode(encoding), end="", file=sys.stderr)
    return {"gate": label, "status": "PASS" if proc.returncode == 0 else "FAIL",
            "returncode": proc.returncode, "command": command,
            "output_tail": (proc.stdout + proc.stderr)[-4000:]}


def main() -> int:
    py = sys.executable
    sprint = "experiments/JMP_SEMINAR_SPRINT/"
    results = [
        run("matched-household illustration", [py, "reports/research_story_build/make_v11_matched_households.py"]),
        run("report build", [py, "reports/research_story_build/build_v11.py"]),
        run("gallery build", [py, "reports/results_gallery_build/build_v11.py"]),
        run("deck build and verification", [py, "beamer/build_deck_r11.py"]),
        run("rehearsal-script build", [py, "beamer/build_rehearsal_script_v11.py"]),
        run("notebook surface refresh", [py, sprint + "refresh_canonical_notebook_v11.py"], WEA_ROOT),
        run("executed notebook verification", [py, sprint + "verify_canonical_notebook_v11.py"], WEA_ROOT),
        run("rendered-text language and negative control", [py, "reports/check_v11_rendered_language.py"]),
        run("Stage A ex-ante status and negative control", [py, "reports/check_v11_stage_a_status.py"]),
        run("reader structure and economic derivation", [py, "reports/check_v11_reader_gates.py"]),
        run("number-to-source", [py, "reports/check_v11_numbers_against_source.py"]),
        run("offline HTML render", [py, "reports/research_story_build/check_v11_render.py"]),
        run("cross-surface synchronisation", [py, "reports/check_v11_synced_surfaces.py"]),
        run("deck verification", [py, "beamer/verify_deck_r11.py"]),
        run("Python source compilation", [py, "-m", "py_compile",
            "reports/research_story_build/build_v11.py", "reports/research_story_build/v11_sections.py",
            "reports/research_story_build/v11_render_inputs.py", "reports/research_story_build/v11_illustration.py",
            "reports/research_story_build/make_v11_matched_households.py",
            "reports/results_gallery_build/build_v11.py", "reports/check_v11_rendered_language.py",
            "reports/check_v11_stage_a_status.py", "reports/check_v11_reader_gates.py",
            "reports/check_v11_numbers_against_source.py", "reports/check_v11_synced_surfaces.py",
            "reports/research_story_build/check_v11_render.py", "reports/write_v11_release_manifest.py",
            "beamer/make_deck_numbers_r11.py", "beamer/prepare_deck_v11.py", "beamer/build_deck_r11.py",
            "beamer/verify_deck_r11.py", "beamer/build_rehearsal_script_v11.py",
            str(WEA_ROOT / sprint / "refresh_canonical_notebook_v11.py"),
            str(WEA_ROOT / sprint / "verify_canonical_notebook_v11.py")]),
        run("V9 and V10 byte-preservation", ["git", "diff", "--exit-code", "--",
            "reports/JMP_research_story_report_v9.html", "reports/JMP_results_gallery_v9.html",
            "reports/numbers_of_record_v9.json", "reports/research_story_build/v9_sections.py",
            "reports/research_story_build/story_v9.generated.md", "beamer/JMP_seminar_deck_r9.tex",
            "reports/JMP_research_story_report_v10.html", "reports/JMP_results_gallery_v10.html",
            "reports/numbers_of_record_v10.json", "reports/research_story_build/v10_sections.py",
            "reports/research_story_build/story_v10.generated.md"]),
    ]
    status = "PASS" if all(item["status"] == "PASS" for item in results) else "FAIL"
    OUT_JSON.write_text(json.dumps({"release": "V11", "status": status, "gates": results},
                                   indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    lines = ["# V11 complete release gate summary", "", f"Overall: **{status}**", "",
             "| Gate | Status | Evidence |", "|---|---:|---|"]
    for item in results:
        tail = item["output_tail"].strip().splitlines()
        detail = (tail[-1] if tail else "completed").replace("|", "\\|")
        lines.append(f"| {item['gate']} | **{item['status']}** | {detail} |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print("V11 RELEASE", status)
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
