"""V7 number-to-source gate.

Expected display values are computed from accepted JSON/CSV artifacts.  The
gate then checks the report, paper, gallery, notebook, deck and rehearsal
surfaces, and emits a claim/source ledger.  It performs no estimation.
"""
from __future__ import annotations

import csv
import hashlib
import html
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
POSFIT_REPO = WORKSPACE / "MNL_posfit"
MNL_REPO = WORKSPACE / "MNL"
PF = POSFIT_REPO / "outputs/positive_fit_diagnostics_v3b"
MOM_PATH = (POSFIT_REPO / "experiments/JMP_SEMINAR_SPRINT/runs/"
            "bandfix2_recompute/new_results_v1.json")
RUM_PATH = POSFIT_REPO / "outputs/band_fix_1/band_fix_3_rum_edge_scope_v1.json"
REG_PATH = ROOT / "reports/numbers_of_record_v7.json"
OUT_JSON = ROOT / "reports/v7_number_to_source_results.json"
OUT_MD = ROOT / "reports/v7_number_to_source_results.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def clean(text: str) -> str:
    text = re.sub(r"data:image/[^;]+;base64,[^\"']+", " ", text)
    text = re.sub(r"<script\b.*?</script>|<style\b.*?</style>", " ", text,
                  flags=re.I | re.S)
    # Require a tag-name starter so mathematical comparisons such as h<10 do
    # not consume everything through the next literal greater-than sign.
    text = re.sub(r"<[!/A-Za-z][^>]{0,1000}>", " ", text)
    text = html.unescape(text)
    text = text.replace("\\%", "%").replace("\\_", "_").replace("--", "–")
    return re.sub(r"\s+", " ", text).strip()


def notebook_text(path: Path) -> str:
    nb = json.loads(read(path))
    chunks: list[str] = []
    for cell in nb.get("cells", []):
        chunks.append("".join(cell.get("source", [])))
        for output in cell.get("outputs", []):
            chunks.append("".join(output.get("text", [])))
            for key, value in output.get("data", {}).items():
                if key.startswith("image/"):
                    continue
                chunks.append("".join(value) if isinstance(value, list) else str(value))
    return clean("\n".join(chunks))


def csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def token(value: float, digits: int) -> str:
    return f"{value:.{digits}f}"


def main() -> int:
    new = json.loads(read(MOM_PATH))
    rum = json.loads(read(RUM_PATH))
    registry = json.loads(read(REG_PATH))
    bands = csv_rows(PF / "model_simulated_bands.csv")
    adequacy = csv_rows(PF / "g2_adequacy.csv")

    bsel = {r["group"]: r for r in bands if r["weighting"] == "weighted"
            and r["scope"] == "all" and r["statistic"] == "extensive_accuracy"
            and r["support"] == "full"}
    asel = {r["group"]: r for r in adequacy if r["weighting"] == "weighted"
            and r["scope"] == "all" and r["statistic"] == "extensive_accuracy"}
    primary_moments = {(r["model"], r["sex"], r["moment"]): r for r in new["moments"]
                       if r["model"] in ("SINGLES", "COUPLES")}

    sources = {
        "POSFIT v3b simulation bands": PF / "model_simulated_bands.csv",
        "POSFIT v3b numerical adequacy": PF / "g2_adequacy.csv",
        "Band-Fix-2 population moments": MOM_PATH,
        "RUM edge-scope audit": RUM_PATH,
        "V7 registered decomposition values": REG_PATH,
    }
    failures: list[str] = []
    claims: list[dict] = []

    def source_check(condition: bool, message: str) -> None:
        if not condition:
            failures.append("SOURCE: " + message)

    # Cross-check the copied V7 registry against its corrected source values.
    for model, key in (("SINGLES", "mae_singles"), ("COUPLES", "mae_couples"),
                       ("RUM-A", "mae_ruma"), ("RUM-B", "mae_rumb")):
        actual = float(new["summaries"][model]["mean_absolute_error"])
        registered = float(registry["entries"][key]["value"])
        source_check(abs(actual - registered) < 1e-15, f"registry {key} differs from Band-Fix-2")
    source_check(float(registry["entries"]["d2_deltaI_pct_singles_eq"]["value"]) == 1.8,
                 "registered lower DECOMP endpoint differs")
    source_check(float(registry["entries"]["d2_deltaI_pct_couples_uneq"]["value"]) == 9.9,
                 "registered upper DECOMP endpoint differs")

    surfaces = {
        "report": clean(read(ROOT / "reports/JMP_research_story_report_v7.html")),
        "report_source": clean(read(ROOT / "reports/research_story_build/story_v7.generated.md")),
        "paper": clean(read(ROOT / "manuscript/JMP_working_paper_for_seminar_v7.tex") + "\n" +
                       read(ROOT / "manuscript/sections/05b_fit.tex")),
        "gallery": clean(read(ROOT / "reports/JMP_results_gallery_current.html")),
        "notebook": notebook_text(MNL_REPO / "experiments/JMP_SEMINAR_SPRINT/JMP_canonical_AtoZ.ipynb"),
        "deck": clean(read(ROOT / "beamer/build/JMP_seminar_deck_r7_text.txt") + "\n" +
                      read(ROOT / "beamer/deck_numbers_r7.tex")),
        "rehearsal": clean(read(ROOT / "reports/rehearsal_pack_v7.md")),
    }

    def claim(name: str, expected: list[str], source: str, on: tuple[str, ...]) -> None:
        row = {"claim": name, "expected_tokens": expected, "source": source,
               "surfaces": {}, "status": "PASS"}
        for surface in on:
            haystack = surfaces[surface].lower()
            missing = [part for part in expected if part.lower() not in haystack]
            ok = not missing
            row["surfaces"][surface] = "PASS" if ok else "FAIL: " + repr(missing)
            if not ok:
                row["status"] = "FAIL"
                failures.append(f"{surface}: {name} missing source-derived token(s) {missing}")
        claims.append(row)

    # Corrected population MAEs, derived rather than hard-coded.
    summary_tokens = {model: token(float(new["summaries"][model]["mean_absolute_error"]), 4)
                      for model in ("SINGLES", "COUPLES", "RUM-A", "RUM-B")}
    claim("primary population-fit MAEs",
          [summary_tokens["SINGLES"], summary_tokens["COUPLES"]],
          "Band-Fix-2 population moments::summaries", tuple(surfaces))
    claim("benchmark population-fit MAEs",
          [summary_tokens["RUM-A"], summary_tokens["RUM-B"]],
          "Band-Fix-2 population moments::summaries",
          ("report", "report_source", "paper", "rehearsal"))

    # The only reportable extensive-accuracy values are the two adequate groups.
    for group, label in (("singles_female", "single women"),
                         ("couples_female", "coupled women")):
        row = bsel[group]
        gate = asel[group]
        pct = [token(100 * float(row[field]), 1)
               for field in ("observed", "simulated_p025", "simulated_p975")]
        raw = [token(float(row[field]), 4)
               for field in ("observed", "simulated_p025", "simulated_p975")]
        ratio = token(float(gate["adequacy_ratio_mcse_to_sampling_sd"]), 3)
        claim(f"{label} reportable accuracy/band (headline units)", pct,
              "POSFIT v3b simulation bands + numerical adequacy",
              ("report", "report_source", "paper"))
        claim(f"{label} reportable accuracy/band (raw shares)", raw,
              "POSFIT v3b simulation bands", ("gallery", "notebook"))
        claim(f"{label} reportable accuracy headline", [pct[0]],
              "POSFIT v3b simulation bands", ("deck", "rehearsal"))
        claim(f"{label} adequacy ratio", [ratio],
              "POSFIT v3b numerical adequacy",
              ("report", "report_source", "paper", "notebook"))

    # Men are traced through ratios/status, while their accuracy display is withheld.
    for group, label in (("singles_male", "single men"), ("couples_male", "coupled men")):
        ratio = token(float(asel[group]["adequacy_ratio_mcse_to_sampling_sd"]), 3)
        claim(f"{label} withheld accuracy adequacy ratio", [ratio, "quadrature-limited"],
              "POSFIT v3b numerical adequacy",
              ("report", "report_source", "paper", "notebook"))
        claim(f"{label} withheld accuracy status", ["WITHHELD", "quadrature-limited"],
              "POSFIT v3b numerical adequacy", ("gallery", "notebook", "deck", "rehearsal"))

    # Four observed-minus-predicted 37-hour gaps from corrected moment cells.
    gaps = []
    for model, sex in (("SINGLES", "male"), ("SINGLES", "female"),
                       ("COUPLES", "male"), ("COUPLES", "female")):
        row = primary_moments[(model, sex, "hours::h_36_5_37_5")]
        gaps.append(token(100 * (float(row["observed"]) - float(row["predicted"])), 1))
    claim("four-group 37-hour observed-minus-predicted gaps", gaps,
          "Band-Fix-2 population moments::hours::h_36_5_37_5",
          ("report", "report_source", "paper", "deck", "rehearsal"))
    mass_cells = []
    for model, sex in (("SINGLES", "male"), ("SINGLES", "female"),
                       ("COUPLES", "male"), ("COUPLES", "female")):
        row = primary_moments[(model, sex, "hours::h_36_5_37_5")]
        mass_cells.extend([token(float(row["observed"]), 4),
                           token(float(row["predicted"]), 4)])
    claim("four-group 37-hour observed/predicted cells", mass_cells,
          "Band-Fix-2 population moments::hours::h_36_5_37_5", ("gallery", "notebook"))

    # Corrected structural FT gaps are required in the detailed fit surfaces.
    ft_cells = []
    for model, sex in (("SINGLES", "male"), ("SINGLES", "female"),
                       ("COUPLES", "male"), ("COUPLES", "female")):
        row = primary_moments[(model, sex, "hours::ft")]
        ft_cells.extend([token(float(row["observed"]), 4),
                         token(float(row["predicted"]), 4)])
    claim("corrected structural FT observed/predicted cells", ft_cells,
          "Band-Fix-2 population moments::hours::ft", ("gallery", "paper"))

    decomp_tokens = [
        token(float(registry["entries"]["d2_deltaI_pct_singles_eq"]["value"]), 1),
        token(float(registry["entries"]["d2_deltaI_pct_couples_uneq"]["value"]), 1),
    ]
    claim("restricted DECOMP-2 Gini-change range", decomp_tokens,
          "V7 registry::d2_deltaI_pct_singles_eq/couples_uneq", tuple(surfaces))

    rum_a = rum["RUM-A"]
    claim("RUM-A input-width limitation",
          [token(float(rum_a["reference_width_as_coded"]), 1),
           token(float(rum_a["reference_width_S11_edges"]), 1),
           token(float(rum_a["log_gbar_offset_difference_min"]), 6)],
          "RUM edge-scope audit::RUM-A", ("report", "report_source", "paper"))

    # Explicit retired-value/lineage safeguards.
    forbidden = {
        "retired single-men near-FT gap": r"(?<!\d)9\.48(?!\d)",
        "retired coupled-women near-FT gap": r"(?<!\d)7\.21(?!\d)",
        "retired singles MAE": r"(?<!\d)0\.0129(?!\d)",
        "retired couples MAE": r"(?<!\d)0\.0136(?!\d)",
        "retired structural PT2 label": r"Part-time upper,?\s*\[28\.5,\s*30\.5\)",
        "retired structural FT label": r"Full-time upper,?\s*\[36\.5,\s*40\.5\]",
    }
    for name, pattern in forbidden.items():
        for surface, text in surfaces.items():
            if re.search(pattern, text, flags=re.I):
                failures.append(f"{surface}: {name} remains ({pattern})")

    result = {
        "gate": "number-to-source",
        "status": "PASS" if not failures else "FAIL",
        "source_artifacts": {name: {"path": str(path.relative_to(WORKSPACE)), "sha256": sha(path)}
                             for name, path in sources.items()},
        "claims": claims,
        "failures": failures,
    }
    OUT_JSON.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    lines = ["# V7 number-to-source gate", "", f"Overall: **{result['status']}**", "",
             "Expected display values are computed from the accepted source artifacts listed below; no estimate is recomputed.", "",
             "| Claim family | Source | Status |", "|---|---|---:|"]
    for row in claims:
        lines.append(f"| {row['claim']} | `{row['source']}` | **{row['status']}** |")
    lines.extend(["", "## Source hashes", ""])
    for name, item in result["source_artifacts"].items():
        lines.append(f"- {name}: `{item['sha256']}` — `{item['path']}`")
    if failures:
        lines.extend(["", "## Failures", ""] + [f"- {item}" for item in failures])
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"NUMBER-TO-SOURCE {result['status']}: {len(claims)} claim families, "
          f"{len(surfaces)} surfaces, {len(failures)} failures")
    for failure in failures:
        print("  -", failure)
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
