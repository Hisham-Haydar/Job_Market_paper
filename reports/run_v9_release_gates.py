"""Build V9 surfaces, run the complete release suite, and write one summary."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
WEA_ROOT = WORKSPACE / "MNL_wea"
OUT_JSON = ROOT / "reports/v9_release_gate_summary.json"
OUT_MD = ROOT / "reports/v9_release_gate_summary.md"


def run(label: str, command: list[str], cwd: Path = ROOT) -> dict:
    proc = subprocess.run(
        command,
        cwd=cwd,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
    )
    if proc.stdout:
        encoding = sys.stdout.encoding or "utf-8"
        print(proc.stdout.encode(encoding, errors="replace").decode(encoding), end="")
    if proc.stderr:
        encoding = sys.stderr.encoding or "utf-8"
        print(
            proc.stderr.encode(encoding, errors="replace").decode(encoding),
            end="",
            file=sys.stderr,
        )
    return {
        "gate": label,
        "status": "PASS" if proc.returncode == 0 else "FAIL",
        "returncode": proc.returncode,
        "command": command,
        "output_tail": (proc.stdout + proc.stderr)[-4000:],
    }


def main() -> int:
    py = sys.executable
    results = [
        run("report build", [py, "reports/research_story_build/build_v9.py"]),
        run("gallery build", [py, "reports/results_gallery_build/build_v9.py"]),
        run("deck build", [py, "beamer/build_deck_r9.py"]),
        run("rehearsal-script build", [py, "beamer/build_rehearsal_script_v9.py"]),
        run(
            "notebook surface refresh",
            [py, "experiments/JMP_SEMINAR_SPRINT/refresh_canonical_notebook_v9.py"],
            WEA_ROOT,
        ),
        run(
            "rendered-text language and negative control",
            [py, "reports/check_v9_rendered_language.py"],
        ),
        run("reader structure and restored economics", [py, "reports/check_v9_reader_gates.py"]),
        run("number-to-source", [py, "reports/check_v9_numbers_against_source.py"]),
        run("offline HTML render", [py, "reports/research_story_build/check_v9_render.py"]),
        run("cross-surface synchronization", [py, "reports/check_v9_synced_surfaces.py"]),
        run("deck verification", [py, "beamer/verify_deck_r9.py"]),
        run(
            "executed notebook verification",
            [py, "experiments/JMP_SEMINAR_SPRINT/verify_canonical_notebook_v9.py"],
            WEA_ROOT,
        ),
        run("V8 complete-suite regression", [py, "reports/run_v8_release_gates.py"]),
        run(
            "Python source compilation",
            [
                py,
                "-m",
                "py_compile",
                "reports/research_story_build/build_v9.py",
                "reports/research_story_build/v9_sections.py",
                "reports/research_story_build/v9_render_inputs.py",
                "reports/results_gallery_build/build_v9.py",
                "reports/check_v9_rendered_language.py",
                "reports/check_v9_reader_gates.py",
                "reports/check_v9_numbers_against_source.py",
                "reports/check_v9_synced_surfaces.py",
                "reports/research_story_build/check_v9_render.py",
                "reports/write_v9_release_manifest.py",
                "beamer/make_deck_numbers_r9.py",
                "beamer/prepare_deck_v9.py",
                "beamer/build_deck_r9.py",
                "beamer/verify_deck_r9.py",
                "beamer/build_rehearsal_script_v9.py",
                str(WEA_ROOT / "experiments/JMP_SEMINAR_SPRINT/refresh_canonical_notebook_v9.py"),
                str(WEA_ROOT / "experiments/JMP_SEMINAR_SPRINT/verify_canonical_notebook_v9.py"),
            ],
        ),
    ]

    v8_paths = [
        "reports/JMP_research_story_report_v8.html",
        "reports/JMP_results_gallery_v8.html",
        "reports/research_story_build/v8_sections.py",
        "reports/research_story_build/v8_render_inputs.py",
        "reports/research_story_build/build_v8.py",
    ]
    v8_diff = run(
        "V8 byte-preservation",
        ["git", "diff", "--exit-code", "--", *v8_paths],
    )
    results.append(v8_diff)

    static = [
        (
            "V8/V9 version separation",
            (ROOT / "reports/JMP_research_story_report_v8.html").is_file()
            and (ROOT / "reports/JMP_research_story_report_v9.html").is_file(),
            "both versioned report files exist",
        ),
        (
            "editable V9 source present",
            (ROOT / "reports/research_story_build/v9_sections.py").is_file()
            and (ROOT / "reports/research_story_build/story_v9.generated.md").is_file(),
            "section source and resolved Markdown exist",
        ),
        (
            "all synchronized surfaces present",
            all(
                path.is_file()
                for path in (
                    ROOT / "reports/JMP_results_gallery_v9.html",
                    ROOT / "beamer/build/JMP_seminar_deck_r9.pdf",
                    ROOT / "beamer/build/JMP_seminar_deck_r9_rehearsal.pdf",
                    ROOT / "reports/rehearsal_pack_v9.md",
                    WEA_ROOT / "experiments/JMP_SEMINAR_SPRINT/JMP_canonical_AtoZ.ipynb",
                )
            ),
            "gallery, deck, rehearsal and notebook exist",
        ),
    ]
    for label, ok, detail in static:
        results.append(
            {
                "gate": label,
                "status": "PASS" if ok else "FAIL",
                "returncode": 0 if ok else 1,
                "command": [],
                "output_tail": detail,
            }
        )
        print(f'{"PASS" if ok else "FAIL"}: {label} - {detail}')

    status = "PASS" if all(item["status"] == "PASS" for item in results) else "FAIL"
    payload = {"release": "V9-WEA", "status": status, "gates": results}
    OUT_JSON.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    lines = [
        "# V9-WEA complete release gate summary",
        "",
        f"Overall: **{status}**",
        "",
        "| Gate | Status | Evidence |",
        "|---|---:|---|",
    ]
    for item in results:
        detail = (
            item["output_tail"].strip().splitlines()[-1]
            if item["output_tail"].strip()
            else "completed"
        )
        detail = detail.replace("|", "\\|")
        lines.append(f"| {item['gate']} | **{item['status']}** | {detail} |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print("V9-WEA RELEASE", status)
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
