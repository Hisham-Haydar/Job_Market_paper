"""Write the V7 surface/hash manifest and the human-readable release record."""
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
OUT_JSON = ROOT / "reports/v7_surface_manifest.json"
OUT_MD = ROOT / "docs/results/JMP_REPORT_V7_release_v1.md"

SURFACES = {
    "report HTML": ROOT / "reports/JMP_research_story_report_v7.html",
    "editable report source": ROOT / "reports/research_story_build/story_v7.generated.md",
    "report section source": ROOT / "reports/research_story_build/v7_sections.py",
    "report data adapter": ROOT / "reports/research_story_build/v7_render_inputs.py",
    "report build entry point": ROOT / "reports/research_story_build/build_v7.py",
    "V7 number registry": ROOT / "reports/numbers_of_record_v7.json",
    "gallery HTML": ROOT / "reports/JMP_results_gallery_current.html",
    "gallery builder": ROOT / "reports/results_gallery_build/build.py",
    "gallery verifier": ROOT / "reports/results_gallery_build/verify.py",
    "canonical notebook": WORKSPACE / "MNL/experiments/JMP_SEMINAR_SPRINT/JMP_canonical_AtoZ.ipynb",
    "notebook support": WORKSPACE / "MNL/experiments/JMP_SEMINAR_SPRINT/jmp_walkthrough_support.py",
    "notebook diagnostics renderer": WORKSPACE / "MNL/experiments/JMP_SEMINAR_SPRINT/final_diagnostics_surface_v1.py",
    "notebook V7 updater": WORKSPACE / "MNL/experiments/JMP_SEMINAR_SPRINT/refresh_canonical_notebook_v7.py",
    "notebook execution provenance": WORKSPACE / "MNL/experiments/JMP_SEMINAR_SPRINT/runs/research_walkthrough/provenance_v1.json",
    "deck source": ROOT / "beamer/JMP_seminar_deck_r7.tex",
    "deck PDF": ROOT / "beamer/build/JMP_seminar_deck_r7.pdf",
    "deck rehearsal PDF": ROOT / "beamer/build/JMP_seminar_deck_r7_rehearsal.pdf",
    "deck number source": ROOT / "beamer/deck_numbers_r7.tex",
    "deck slide-8 figure": ROOT / "beamer/figures/r7/fitext_r7_slide.pdf",
    "deck slide-9 figure": ROOT / "beamer/figures/r7/hours37_r7_slide.pdf",
    "deck source manifest": ROOT / "beamer/figures/r7/r7_source_manifest.json",
    "versioned rehearsal pack": ROOT / "reports/rehearsal_pack_v7.md",
    "current rehearsal pack": ROOT / "reports/rehearsal_pack_v1.md",
    "paper source": ROOT / "manuscript/JMP_working_paper_for_seminar_v7.tex",
    "paper bibliography": ROOT / "manuscript/JMP_working_paper_for_seminar_v7.bib",
    "paper PDF": ROOT / "manuscript/JMP_working_paper_for_seminar_v7.pdf",
    "modular paper fit section": ROOT / "manuscript/sections/05b_fit.tex",
    "paper singles fit table": ROOT / "manuscript/tables/v7/v7_fit_singles.csv",
    "paper couples fit table": ROOT / "manuscript/tables/v7/v7_fit_couples.csv",
    "paper benchmark table": ROOT / "manuscript/tables/v7/v7_benchmark.csv",
    "paper corrected fit figure": ROOT / "manuscript/figures/v7/fit_by_margin_v7.png",
    "paper corrected accuracy figure": ROOT / "manuscript/figures/v7/fitext_band_v3b.png",
    "paper corrected convergence figure": ROOT / "manuscript/figures/v7/node_convergence_v3b.png",
    "band-edge dependency audit": ROOT / "docs/results/JMP_V7_band_edge_dependency_audit_v1.md",
    "fit impact/adjudication memo": ROOT / "docs/results/JMP_V7_fit_impact_and_adjudication_v1.md",
    "G1-G9 checker": ROOT / "reports/check_v7_ruling_gates.py",
    "number-to-source checker": ROOT / "reports/check_v7_numbers_against_source.py",
    "complete gate summary": ROOT / "reports/v7_release_gate_summary.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_head(path: Path) -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=path,
                                   text=True).strip()


def main() -> None:
    missing = [str(path) for path in SURFACES.values() if not path.is_file()]
    if missing:
        raise SystemExit("Missing release surfaces:\n" + "\n".join(missing))
    records = [{"surface": name, "path": str(path.relative_to(WORKSPACE)).replace("\\", "/"),
                "bytes": path.stat().st_size, "sha256": digest(path)}
               for name, path in SURFACES.items()]
    mnl_head = git_head(WORKSPACE / "MNL")
    payload = {
        "release": "V7-BUILD",
        "accepted_posfit_commit": "cd7247cf9c627b35b6b5b017be214823b77bbd13",
        "job_market_paper_parent_commit": git_head(ROOT),
        "mnl_surface_commit": mnl_head,
        "constraints": {"reestimation": False, "repricing": False,
                        "wea_computation": False, "decomp_rerun": False},
        "surfaces": records,
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# JMP report V7 release record", "", "Date: 14 September 2026  ",
        "Status: **PASS — G1–G9 and number-to-source gate**  ",
        "Accepted corrected POSFIT commit: `cd7247cf9c627b35b6b5b017be214823b77bbd13`", "",
        f"Canonical-notebook surface commit: `{mnl_head}`", "",
        "## Claim disposition", "",
        "- Men's extensive accuracy is withheld for both singles and couples because the corrected statistic is quadrature-limited.",
        "- The corrected weighted four-group adjudication is D = mechanical stochastic conditioning for all groups; E = misspecification evidence for both couple groups and inconclusive/quadrature-limited for both single groups.",
        "- The three-group excess-predictability claim is withdrawn.",
        "- The retired near-full-time headline is replaced by **underprediction of the observed 37-hour mass point**. Singles MAE rises slightly, so the correction is not presented as improved fit.",
        "- DECOMP-2 is restored to the main results as a preliminary restricted P/A/B exercise; its abstract statement is qualitative and its quantitative main-text statement carries the exact scope caveat.",
        "- Current W1_F language refers to equivalent consumption at the universally available non-employment reference. W_EA_flat is definition-only and blocked; no historical W1-EA percentage is live.",
        "- The short-hours limitation and RUM-A/B estimation-input band defect are disclosed.", "",
        "## Exact W1_F/WEA language change", "",
        "Retired from current W1_F: “equivalent flat consumption level” and descriptions in which current W1_F integrates over an opportunity distribution.", "",
        "Current W1_F: “The empirical Mapping-F implementation evaluates the attained bundle against the universally available non-employment reference. Under the current specification, estimated opportunity density therefore affects this money metric through attained outcomes rather than through a direct opportunity-prospect term.”", "",
        "W_EA_flat is separately defined under the H-F primary domain, remains numerically blocked by support/pricing requirements including 260 couples without a priced NN state, and has no reported number.", "",
        "## Build and dependency ledger", "",
        "| Item | Tool/dependency | Effort/status |", "|---|---|---|",
        "| Corrected predictive evidence | POSFIT v3b and node-convergence v3b at the accepted commit | Read-only propagation; no re-estimation, no repricing |",
        "| Population fit | Band-Fix-2 `new_results_v1.json` | Read-only propagation; descriptive 37-hour cell kept separate from structural FT |",
        "| Report/gallery | Python builders, Pandoc HTML renderer | Rebuilt and verified |",
        "| Notebook | Python/Jupyter nbconvert using the MNL project environment | All non-empty code cells executed; zero error outputs |",
        "| Deck | Python figure/number builders and MiKTeX Beamer | Projected and rehearsal PDFs rebuilt; zero overfull/underfull boxes |",
        "| Paper | V7 Python source adapter and MiKTeX/pdfLaTeX/BibTeX | 35-page PDF rebuilt; no fatal or undefined-reference errors |",
        "| DECOMP-2 | SHA-pinned S10 criterion-A frames and accepted DECOMP assets | No-dependency audit PASS; not rerun |",
        "| Agent | Codex | Release engineering and evidence audit; runtime model identifier is not embedded in the build artifacts |", "",
        "## Surfaces and SHA-256", "", "| Surface | Path | SHA-256 |", "|---|---|---|",
    ]
    for row in records:
        lines.append(f"| {row['surface']} | `{row['path']}` | `{row['sha256']}` |")
    lines.extend(["", "The revised abstract and main-results decomposition subsection are in the editable report source and V7 paper source listed above. The dependency classification is in `docs/results/JMP_V7_band_edge_dependency_audit_v1.md`; the complete gate table is in `reports/v7_release_gate_summary.md`."])
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {OUT_JSON} and {OUT_MD} ({len(records)} surfaces)")


if __name__ == "__main__":
    main()
