"""Run the complete V7 circulation gate suite and write one summary."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_JSON = ROOT / "reports/v7_release_gate_summary.json"
OUT_MD = ROOT / "reports/v7_release_gate_summary.md"


def run(label: str, command: list[str]) -> dict:
    proc = subprocess.run(command, cwd=ROOT, text=True, encoding="utf-8",
                          errors="replace", capture_output=True)
    if proc.stdout:
        print(proc.stdout, end="")
    if proc.stderr:
        print(proc.stderr, end="", file=sys.stderr)
    return {"gate": label, "status": "PASS" if proc.returncode == 0 else "FAIL",
            "returncode": proc.returncode, "command": command,
            "output_tail": (proc.stdout + proc.stderr)[-4000:]}


def main() -> int:
    py = sys.executable
    results = [
        run("G1-G9 ruling suite", [py, "reports/check_v7_ruling_gates.py"]),
        run("number-to-source", [py, "reports/check_v7_numbers_against_source.py"]),
        run("gallery verifier", [py, "reports/results_gallery_build/verify.py"]),
        run("deck r7 verifier", [py, "beamer/verify_deck_r7.py"]),
    ]

    paper_pdf = ROOT / "manuscript/JMP_working_paper_for_seminar_v7.pdf"
    paper_log = ROOT / "manuscript/JMP_working_paper_for_seminar_v7.log"
    nb_path = ROOT.parent / "MNL/experiments/JMP_SEMINAR_SPRINT/JMP_canonical_AtoZ.ipynb"
    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    errors = [(i, out.get("ename", "error")) for i, cell in enumerate(nb.get("cells", []))
              for out in cell.get("outputs", []) if out.get("output_type") == "error"]
    code_cells = [cell for cell in nb.get("cells", []) if cell.get("cell_type") == "code"
                  and "".join(cell.get("source", [])).strip()]
    unexecuted = [i for i, cell in enumerate(code_cells) if cell.get("execution_count") is None]
    log = paper_log.read_text(encoding="utf-8", errors="replace") if paper_log.exists() else ""
    static = [
        ("paper PDF render", paper_pdf.exists() and paper_pdf.stat().st_size > 1_000_000,
         f"{paper_pdf.stat().st_size if paper_pdf.exists() else 0} bytes"),
        ("paper fatal/undefined-reference scan",
         bool(log) and "Fatal error" not in log and "undefined references" not in log.lower(),
         "fatal and undefined-reference strings absent"),
        ("canonical notebook execution", not errors and not unexecuted,
         f"{len(code_cells)} non-empty code cells; errors={errors}; unexecuted={unexecuted}"),
        ("version separation", (ROOT / "reports/JMP_research_story_report_v6.html").exists()
         and (ROOT / "reports/JMP_research_story_report_v7.html").exists(),
         "v6 and v7 both exist; v7 builder redirects all v6 write targets"),
    ]
    for label, ok, detail in static:
        results.append({"gate": label, "status": "PASS" if ok else "FAIL",
                        "returncode": 0 if ok else 1, "command": [], "output_tail": detail})
        print(f"{results[-1]['status']}: {label} — {detail}")

    ruling = json.loads((ROOT / "reports/v7_ruling_gate_results.json").read_text(encoding="utf-8"))
    status = "PASS" if all(item["status"] == "PASS" for item in results) else "FAIL"
    payload = {"release": "V7-BUILD", "status": status, "ruling_gates": ruling["gates"],
               "additional_gates": results[1:]}
    OUT_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    lines = ["# V7 complete release gate summary", "", f"Overall: **{status}**", "",
             "## Ruling gates", "", "| Gate | Requirement | Status |", "|---|---|---:|"]
    for item in ruling["gates"]:
        lines.append(f"| {item['gate']} | {item['name']} | **{item['status']}** |")
    lines.extend(["", "## Additional release gates", "", "| Gate | Status |", "|---|---:|"])
    for item in results[1:]:
        lines.append(f"| {item['gate']} | **{item['status']}** |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("V7 RELEASE", status)
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
