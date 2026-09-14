"""Write the V8 surface manifest and human-readable release record."""
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
OUT_JSON = ROOT / "reports/v8_surface_manifest.json"
OUT_MD = ROOT / "docs/results/JMP_REPORT_V8_release_v1.md"

SURFACES = {
    "report HTML": ROOT / "reports/JMP_research_story_report_v8.html",
    "editable resolved Markdown": ROOT / "reports/research_story_build/story_v8.generated.md",
    "editable section source": ROOT / "reports/research_story_build/v8_sections.py",
    "numerical input adapter": ROOT / "reports/research_story_build/v8_render_inputs.py",
    "report builder": ROOT / "reports/research_story_build/build_v8.py",
    "V8 numerical registry": ROOT / "reports/numbers_of_record_v8.json",
    "reader-facing gallery": ROOT / "reports/JMP_results_gallery_v8.html",
    "gallery builder": ROOT / "reports/results_gallery_build/build_v8.py",
    "reader-language checker": ROOT / "reports/check_v8_reader_gates.py",
    "rendered-language checker": ROOT / "reports/check_v8_rendered_language.py",
    "number-to-source checker": ROOT / "reports/check_v8_numbers_against_source.py",
    "offline render checker": ROOT / "reports/research_story_build/check_v8_render.py",
    "release-suite runner": ROOT / "reports/run_v8_release_gates.py",
    "release-manifest writer": ROOT / "reports/write_v8_release_manifest.py",
    "banned-term audit": ROOT / "reports/v8_banned_term_audit.md",
    "banned-term negative control": ROOT / "reports/v8_banned_term_negative_control.md",
    "section map": ROOT / "reports/v8_section_map.md",
    "number-to-source results": ROOT / "reports/v8_number_to_source_results.md",
    "reader gate results": ROOT / "reports/v8_reader_gate_results.md",
    "render gate results": ROOT / "reports/v8_render_gate.json",
    "complete gate summary": ROOT / "reports/v8_release_gate_summary.md",
    "authorisation source": ROOT / "docs/JMP_preseminar_reader_facing_and_WEA_pricing_authorization_v1.md",
}

EVIDENCE = {
    "corrected prediction ranges": WORKSPACE / "MNL_posfit/outputs/positive_fit_diagnostics_v3b/model_simulated_bands.csv",
    "corrected numerical precision": WORKSPACE / "MNL_posfit/outputs/positive_fit_diagnostics_v3b/g2_adequacy.csv",
    "corrected population moments": WORKSPACE / "MNL_posfit/experiments/JMP_SEMINAR_SPRINT/runs/bandfix2_recompute/new_results_v1.json",
    "decomposition record": WORKSPACE / "MNL_decomp/outputs/welfare/preseminar_pab_v1/preseminar_pab_record_v1.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_head(path: Path) -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=path,
                                   text=True).strip()


def main() -> None:
    missing = [str(path) for path in (*SURFACES.values(), *EVIDENCE.values())
               if not path.is_file()]
    if missing:
        raise SystemExit("Missing release inputs:\n" + "\n".join(missing))
    gate = json.loads((ROOT / "reports/v8_release_gate_summary.json").read_text(
        encoding="utf-8"))
    if gate["status"] != "PASS":
        raise SystemExit("V8 release suite has not passed")

    records = [
        {"surface": name,
         "path": str(path.relative_to(WORKSPACE)).replace("\\", "/"),
         "bytes": path.stat().st_size,
         "sha256": digest(path)}
        for name, path in SURFACES.items()
    ]
    evidence = [
        {"source": name,
         "path": str(path.relative_to(WORKSPACE)).replace("\\", "/"),
         "sha256": digest(path)}
        for name, path in EVIDENCE.items()
    ]
    payload = {
        "release": "V8-READER",
        "status": "PASS",
        "job_market_paper_parent_commit": git_head(ROOT),
        "constraints": {
            "numbers_changed": False,
            "reestimation": False,
            "repricing": False,
            "decomposition_rerun": False,
            "ex_ante_result_reported": False,
            "v7_overwritten": False,
        },
        "surfaces": records,
        "evidence": evidence,
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8",
                        newline="\n")

    report_hash = next(row["sha256"] for row in records
                       if row["surface"] == "report HTML")
    lines = [
        "# JMP report V8 reader-facing release record", "",
        "Status: **PASS**", "",
        f"Report HTML SHA-256: `{report_hash}`", "",
        "## Reader-facing changes", "",
        "- The abstract is the authorised magnitude paragraph, including 1.8–9.9%.",
        "- The main report follows the seven-part economic sequence from motivation through the ex-ante extension.",
        "- The full numerical Shapley allocation remains in the main results with the restricted-exercise caveat.",
        "- Corrected predictive evidence is retained: coupled men's extensive accuracy is WITHHELD, the 37-hour mass-point finding remains explicit, and short-hours coverage remains a limitation.",
        "- The ex-ante section is the authorised single paragraph. No historical ex-ante percentage is reported.",
        "- Detailed predecessor sections and the implementation record are preserved in one explicitly marked, collapsed provenance appendix; the predecessor abstract and status note are omitted, and V7 files were not overwritten.", "",
        "## Release records", "",
        "- Banned-term deletion/replacement audit: `reports/v8_banned_term_audit.md`",
        "- Banned-term negative control: `reports/v8_banned_term_negative_control.md`",
        "- V7-to-V8 section map: `reports/v8_section_map.md`",
        "- Complete checks: `reports/v8_release_gate_summary.md`",
        "- Number-to-source checks: `reports/v8_number_to_source_results.md`", "",
        "## Tool, model, effort and dependency ledger", "",
        "| Work item | Tool/model or dependency | Effort and status |",
        "|---|---|---|",
        "| Narrative rebuild | Codex; runtime model identifier is not embedded in repository artifacts | Seven main sections rewritten and reviewed; complete |",
        "| HTML generation | Python, pypandoc/Pandoc, vendored MathJax | Report and gallery built offline; complete |",
        "| Numerical evidence | Accepted V7 registry plus the corrected predictive-fit and decomposition artifacts listed below | Read-only propagation; no value changed |",
        "| Visual inspection | Playwright with local Microsoft Edge | Report and gallery rendered offline at desktop width; complete |",
        "| Validation | Reader-language, number-to-source, render, V7 regression and source-compilation checks | All PASS |",
        "| External services | None | No network data or external model dependency used |", "",
        "## Surfaces and SHA-256", "",
        "| Surface | Path | SHA-256 |", "|---|---|---|",
    ]
    for row in records:
        lines.append(f"| {row['surface']} | `{row['path']}` | `{row['sha256']}` |")
    lines.extend(["", "## Numerical evidence", "",
                  "| Source | Path | SHA-256 |", "|---|---|---|"])
    for row in evidence:
        lines.append(f"| {row['source']} | `{row['path']}` | `{row['sha256']}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"wrote {OUT_JSON} and {OUT_MD} ({len(records)} surfaces)")


if __name__ == "__main__":
    main()
