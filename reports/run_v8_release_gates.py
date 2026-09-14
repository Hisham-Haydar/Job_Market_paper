"""Run the complete V8 reader-facing release suite and write one summary."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_JSON = ROOT / "reports/v8_release_gate_summary.json"
OUT_MD = ROOT / "reports/v8_release_gate_summary.md"


def run(label: str, command: list[str], cwd: Path = ROOT) -> dict:
    proc = subprocess.run(command, cwd=cwd, text=True, encoding="utf-8",
                          errors="replace", capture_output=True)
    if proc.stdout:
        print(proc.stdout, end="")
    if proc.stderr:
        print(proc.stderr, end="", file=sys.stderr)
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
        run("rendered-text language and negative control",
            [py, "reports/check_v8_rendered_language.py"]),
        run("reader-language and structure", [py, "reports/check_v8_reader_gates.py"]),
        run("number-to-source", [py, "reports/check_v8_numbers_against_source.py"]),
        run("offline HTML render", [py, "check_v8_render.py"],
            ROOT / "reports/research_story_build"),
        run("V7 decision-suite regression", [py, "reports/check_v7_ruling_gates.py"]),
        run("V7 number-lineage regression", [py, "reports/check_v7_numbers_against_source.py"]),
        run("preserved gallery regression", [py, "reports/results_gallery_build/verify.py"]),
        run("Python source compilation", [py, "-m", "py_compile",
            "reports/research_story_build/build_v8.py",
            "reports/research_story_build/v8_sections.py",
            "reports/research_story_build/v8_render_inputs.py",
            "reports/results_gallery_build/build_v8.py",
            "reports/check_v8_rendered_language.py",
            "reports/check_v8_reader_gates.py",
            "reports/check_v8_numbers_against_source.py"]),
    ]

    static = [
        ("V7/V8 version separation",
         (ROOT / "reports/JMP_research_story_report_v7.html").is_file()
         and (ROOT / "reports/JMP_research_story_report_v8.html").is_file(),
         "both versioned report files exist"),
        ("editable source present",
         (ROOT / "reports/research_story_build/v8_sections.py").is_file()
         and (ROOT / "reports/research_story_build/story_v8.generated.md").is_file(),
         "section source and generated Markdown exist"),
        ("reader-facing gallery present",
         (ROOT / "reports/JMP_results_gallery_v8.html").is_file(),
         "versioned V8 gallery exists"),
    ]
    for label, ok, detail in static:
        results.append({"gate": label, "status": "PASS" if ok else "FAIL",
                        "returncode": 0 if ok else 1, "command": [],
                        "output_tail": detail})
        print(f'{"PASS" if ok else "FAIL"}: {label} — {detail}')

    status = "PASS" if all(item["status"] == "PASS" for item in results) else "FAIL"
    payload = {"release": "V8-READER", "status": status, "gates": results}
    OUT_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8",
                        newline="\n")
    lines = [
        "# V8 complete release gate summary", "",
        f"Overall: **{status}**", "",
        "| Gate | Status | Evidence |", "|---|---:|---|",
    ]
    for item in results:
        detail = item["output_tail"].strip().splitlines()[-1] if item["output_tail"].strip() else "completed"
        lines.append(f"| {item['gate']} | **{item['status']}** | {detail} |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print("V8 RELEASE", status)
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
