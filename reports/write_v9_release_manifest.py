"""Write the V9-WEA surface manifest and human-readable release record."""
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
WEA_ROOT = WORKSPACE / "MNL_wea"
OUT_JSON = ROOT / "reports/v9_surface_manifest.json"
OUT_MD = ROOT / "docs/results/JMP_REPORT_V9_release_v1.md"

SURFACES = {
    "report HTML": ROOT / "reports/JMP_research_story_report_v9.html",
    "editable resolved Markdown": ROOT / "reports/research_story_build/story_v9.generated.md",
    "editable section source": ROOT / "reports/research_story_build/v9_sections.py",
    "numerical input adapter": ROOT / "reports/research_story_build/v9_render_inputs.py",
    "report builder": ROOT / "reports/research_story_build/build_v9.py",
    "V9 numerical registry": ROOT / "reports/numbers_of_record_v9.json",
    "reader-facing gallery": ROOT / "reports/JMP_results_gallery_v9.html",
    "gallery builder": ROOT / "reports/results_gallery_build/build_v9.py",
    "deck source": ROOT / "beamer/JMP_seminar_deck_r9.tex",
    "rehearsal deck source": ROOT / "beamer/JMP_seminar_deck_r9_rehearsal.tex",
    "deck numerical macros": ROOT / "beamer/deck_numbers_r9.tex",
    "deck macro generator": ROOT / "beamer/make_deck_numbers_r9.py",
    "deck preparation script": ROOT / "beamer/prepare_deck_v9.py",
    "deck builder": ROOT / "beamer/build_deck_r9.py",
    "deck verifier": ROOT / "beamer/verify_deck_r9.py",
    "presentation PDF": ROOT / "beamer/build/JMP_seminar_deck_r9.pdf",
    "rehearsal PDF": ROOT / "beamer/build/JMP_seminar_deck_r9_rehearsal.pdf",
    "presentation rendered text": ROOT / "beamer/build/JMP_seminar_deck_r9_text.txt",
    "rehearsal rendered text": ROOT / "beamer/build/JMP_seminar_deck_r9_rehearsal_text.txt",
    "rehearsal script": ROOT / "reports/rehearsal_pack_v9.md",
    "rehearsal-script builder": ROOT / "beamer/build_rehearsal_script_v9.py",
    "executed canonical notebook": WEA_ROOT / "experiments/JMP_SEMINAR_SPRINT/JMP_canonical_AtoZ.ipynb",
    "notebook updater": WEA_ROOT / "experiments/JMP_SEMINAR_SPRINT/refresh_canonical_notebook_v9.py",
    "notebook verifier": WEA_ROOT / "experiments/JMP_SEMINAR_SPRINT/verify_canonical_notebook_v9.py",
    "reader and economics checker": ROOT / "reports/check_v9_reader_gates.py",
    "rendered-language checker": ROOT / "reports/check_v9_rendered_language.py",
    "number-to-source checker": ROOT / "reports/check_v9_numbers_against_source.py",
    "cross-surface checker": ROOT / "reports/check_v9_synced_surfaces.py",
    "offline render checker": ROOT / "reports/research_story_build/check_v9_render.py",
    "release-suite runner": ROOT / "reports/run_v9_release_gates.py",
    "release-manifest writer": ROOT / "reports/write_v9_release_manifest.py",
    "banned-term audit": ROOT / "reports/v9_banned_term_audit.md",
    "banned-term negative control": ROOT / "reports/v9_banned_term_negative_control.md",
    "number-to-source results": ROOT / "reports/v9_number_to_source_results.md",
    "reader gate results": ROOT / "reports/v9_reader_gate_results.md",
    "render gate results": ROOT / "reports/v9_render_gate.json",
    "complete gate summary": ROOT / "reports/v9_release_gate_summary.md",
}

EVIDENCE = {
    "certified ex-ante result record": WEA_ROOT / "docs/wea_sprint_1/stage4/stage4_certification_and_results_v1.json",
    "certified ex-ante result memo": WEA_ROOT / "docs/wea_sprint_1/WEA_SPRINT_1_result_memo_v1.md",
    "attained-bundle decomposition record": WORKSPACE / "MNL_decomp/outputs/welfare/preseminar_pab_v1/preseminar_pab_record_v1.json",
    "corrected prediction ranges": WORKSPACE / "MNL_posfit/outputs/positive_fit_diagnostics_v3b/model_simulated_bands.csv",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_head(path: Path) -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=path, text=True).strip()


def git_ref(path: Path, ref: str) -> str:
    return subprocess.check_output(["git", "rev-parse", ref], cwd=path, text=True).strip()


def file_commit(path: Path, relative_file: str) -> str:
    return subprocess.check_output(
        ["git", "log", "-1", "--format=%H", "--", relative_file],
        cwd=path,
        text=True,
    ).strip()


def main() -> None:
    missing = [str(path) for path in (*SURFACES.values(), *EVIDENCE.values()) if not path.is_file()]
    if missing:
        raise SystemExit("Missing release inputs:\n" + "\n".join(missing))
    gate = json.loads((ROOT / "reports/v9_release_gate_summary.json").read_text(encoding="utf-8"))
    if gate["status"] != "PASS":
        raise SystemExit("V9-WEA release suite has not passed")

    records = [
        {
            "surface": name,
            "path": str(path.relative_to(WORKSPACE)).replace("\\", "/"),
            "bytes": path.stat().st_size,
            "sha256": digest(path),
        }
        for name, path in SURFACES.items()
    ]
    evidence = [
        {
            "source": name,
            "path": str(path.relative_to(WORKSPACE)).replace("\\", "/"),
            "sha256": digest(path),
        }
        for name, path in EVIDENCE.items()
    ]
    payload = {
        "release": "V9-WEA",
        "status": "PASS",
        "job_market_paper_parent_commit": git_head(ROOT),
        "welfare_certification_commit": file_commit(
            WEA_ROOT,
            "docs/wea_sprint_1/stage4/stage4_certification_and_results_v1.json",
        ),
        "welfare_notebook_commit": git_head(WEA_ROOT),
        "welfare_published_commit": git_ref(WEA_ROOT, "origin/welfare/wea-sprint-1"),
        "constraints": {
            "attained_bundle_numbers_changed": False,
            "certified_ex_ante_results_added": True,
            "reestimation": False,
            "repricing": False,
            "v8_overwritten": False,
            "neither_welfare_perspective_designated_primary": True,
        },
        "surfaces": records,
        "evidence": evidence,
    }
    OUT_JSON.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    report_hash = next(row["sha256"] for row in records if row["surface"] == "report HTML")
    lines = [
        "# JMP report V9-WEA release record",
        "",
        "Status: **PASS**",
        "",
        f"Report HTML SHA-256: `{report_hash}`",
        "",
        "## Reader-facing release",
        "",
        "- Exact title: *Unequal Job Opportunities and Well-Being Inequality: A Latent-Jobs Structural Decomposition*.",
        "- The main text restores the utility model, opportunity density, estimation criterion, maintained separation assumptions, both welfare derivations, and the structural operators.",
        "- The attained-bundle perspective values the realised job; the ex-ante perspective values the whole job prospect. Neither is designated primary.",
        "- Earning opportunities dominate attained-bundle accounting. For single-adult households, access is about three times earnings in ex-ante accounting.",
        "- Ex-ante access plus earnings is 7.9-21.3% of its own baseline Gini. For couples, equivalisation moves the share from 21.3% to 7.9% and turns the preference contribution negative; no directional preference claim is made.",
        "- Earlier figures near 90% covered all non-preference circumstances, including household resources and composition, and are not comparable with the current restricted results.",
        "- The implementation, certification and provenance record remains within the single collapsed appendix. V8 was not overwritten.",
        "- The welfare branch was published as a focused snapshot because an unrelated oversized blob in its local ancestral history cannot pass GitHub's file-size limit; the certified result and notebook contents are unchanged apart from line-ending normalization in the published snapshot.",
        "",
        "## Verification records",
        "",
        "- Banned-term rendered-text scan: `reports/v9_banned_term_audit.md`",
        "- Banned-term negative control: `reports/v9_banned_term_negative_control.md`",
        "- Number-to-source checks: `reports/v9_number_to_source_results.md`",
        "- Reader/economics checks: `reports/v9_reader_gate_results.md`",
        "- Complete release suite: `reports/v9_release_gate_summary.md`",
        "",
        "## Tool and dependency ledger",
        "",
        "| Work item | Tool or dependency | Status |",
        "|---|---|---|",
        "| Narrative and equations | Python section source and Pandoc/MathJax rendering | Complete |",
        "| Certified ex-ante evidence | Stage-4 result record and memo | Read-only propagation; all declared checks passed |",
        "| Decks | LaTeX build plus rendered-text verification | Main and rehearsal PDFs built without box warnings |",
        "| Notebook | Executed canonical notebook with source-linked comparison table | No error outputs; synchronized |",
        "| Visual inspection | Offline browser and PDF rendering | Report, gallery and comparison slide inspected |",
        "| Validation | Language, negative control, number lineage, rendering, synchronization and V8 regression | All PASS |",
        "",
        "## Surfaces and SHA-256",
        "",
        "| Surface | Path | SHA-256 |",
        "|---|---|---|",
    ]
    for row in records:
        lines.append(f"| {row['surface']} | `{row['path']}` | `{row['sha256']}` |")
    lines.extend(["", "## Numerical evidence", "", "| Source | Path | SHA-256 |", "|---|---|---|"])
    for row in evidence:
        lines.append(f"| {row['source']} | `{row['path']}` | `{row['sha256']}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"wrote {OUT_JSON} and {OUT_MD} ({len(records)} surfaces)")


if __name__ == "__main__":
    main()
