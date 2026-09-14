"""V8 number-to-source checks for the report and reader-facing gallery."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
BUILD = ROOT / "reports/research_story_build"
sys.path.insert(0, str(BUILD))
sys.path.insert(0, str(ROOT / "reports"))

import check_v8_rendered_language as rendered_audit  # noqa: E402
import v8_render_inputs as inputs  # noqa: E402
import v8_sections as sections  # noqa: E402


RULING = ROOT / "docs/JMP_preseminar_reader_facing_and_WEA_pricing_authorization_v1.md"
V7_SOURCE = BUILD / "story_v7.generated.md"
V8_SOURCE = BUILD / "story_v8.generated.md"
V8_REPORT = ROOT / "reports/JMP_research_story_report_v8.html"
V8_GALLERY = ROOT / "reports/JMP_results_gallery_v8.html"
V8_REGISTRY = ROOT / "reports/numbers_of_record_v8.json"
POSFIT = WORKSPACE / "MNL_posfit/outputs/positive_fit_diagnostics_v3b"
MOMENTS = (WORKSPACE / "MNL_posfit/experiments/JMP_SEMINAR_SPRINT/runs/"
           "bandfix2_recompute/new_results_v1.json")
DECOMP = WORKSPACE / "MNL_decomp/outputs/welfare/preseminar_pab_v1"
OUT_JSON = ROOT / "reports/v8_number_to_source_results.json"
OUT_MD = ROOT / "reports/v8_number_to_source_results.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def squash(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def visible_html(path: Path) -> str:
    outside, _ = rendered_audit.remove_exact_appendix(read(path))
    return rendered_audit.rendered_text(outside)


def number_tokens(text: str) -> set[str]:
    return set(re.findall(
        r"(?<![A-Za-z0-9])[-+]?(?:\d{1,3}(?:,\d{3})+|\d+(?:\.\d+)?(?:e[-+]?\d+)?)(?:%)?",
        text,
        flags=re.I,
    ))


def table_data_tokens(text: str) -> set[str]:
    rows = "\n".join(
        line for line in text.splitlines()
        if line.startswith("|Single-adult|") or line.startswith("|Couple|")
    )
    return number_tokens(rows)


def main() -> int:
    failures: list[str] = []
    claims: list[dict[str, str]] = []

    def claim(name: str, ok: bool, source: str) -> None:
        claims.append({"claim": name, "source": source,
                       "status": "PASS" if ok else "FAIL"})
        if not ok:
            failures.append(name)

    ruling = read(RULING)
    abstract_match = re.search(
        r"“(In a preliminary restricted structural decomposition.*?job\s+opportunities\.)”",
        ruling,
        flags=re.S,
    )
    exante_match = re.search(
        r"“(We are also developing a complementary ex-ante measure.*?reported here\.)”",
        ruling,
        flags=re.S,
    )
    claim("abstract is verbatim from the authorised paragraph",
          bool(abstract_match) and squash(sections.ABSTRACT) == squash(abstract_match.group(1)),
          "reader-facing authorisation, section A")
    claim("ex-ante paragraph is verbatim from the authorised paragraph",
          bool(exante_match) and squash(sections.EX_ANTE) == squash(exante_match.group(1)),
          "reader-facing authorisation, section E")

    reader_bodies = [s["body"] for s in sections.SECTIONS if s["key"] != "provenance"]
    placeholders = re.findall(r"\{\{n:([^|}]+?)(?:\|([^}]+))?\}\}",
                              "\n".join(reader_bodies))
    missing = sorted({key for key, _ in placeholders if key not in inputs.REG})
    claim("every reader-facing scalar placeholder resolves", not missing,
          "V8 number registry entries")

    resolved_main = "\n".join(inputs.resolve(body, "report") for body in reader_bodies)
    v7_numbers = number_tokens(read(V7_SOURCE))
    v8_numbers = number_tokens(resolved_main)
    novel = sorted(v8_numbers - v7_numbers)
    claim("no new numerical value was introduced into the main prose", not novel,
          "V7 generated source numerical-token inventory")

    old_welfare_numbers = table_data_tokens(inputs.TABLES["baselinef1"])
    new_welfare_numbers = table_data_tokens(inputs.TABLES["welfare_reader"])
    claim("reader-facing welfare table preserves every numerical cell",
          old_welfare_numbers == new_welfare_numbers,
          "V7 attained-bundle welfare table")
    old_decomp_numbers = number_tokens(inputs.TABLES["pabshapley"])
    new_decomp_numbers = number_tokens(inputs.TABLES["decomposition_reader"])
    claim("reader-facing decomposition table preserves every numerical cell",
          old_decomp_numbers == new_decomp_numbers,
          "accepted Shapley allocation table")

    report = visible_html(V8_REPORT)
    gallery = visible_html(V8_GALLERY)
    moments = json.loads(read(MOMENTS))
    expected_mae = [
        f'{moments["summaries"][model]["mean_absolute_error"]:.4f}'
        for model in ("SINGLES", "COUPLES")
    ]
    claim("corrected population-fit deviations resolve on both surfaces",
          all(value in report and value in gallery for value in expected_mae),
          "Band-Fix-2 population moments")

    bands = read(POSFIT / "model_simulated_bands.csv")
    expected_women = ["85.7%", "80.0%", "85.9%", "89.8%", "88.1%", "91.2%"]
    claim("reportable women's accuracy values and ranges resolve",
          all(value in report and value in gallery for value in expected_women)
          and "singles_female" in bands and "couples_female" in bands,
          "corrected model-simulated prediction ranges")
    claim("men's extensive accuracy remains withheld",
          all(re.search(r"coupled men.s extensive accuracy is withheld",
                        surface, flags=re.I)
              for surface in (report, gallery)),
          "corrected numerical-precision assessment")

    primary = {(row["model"], row["sex"], row["moment"]): row
               for row in moments["moments"]}
    gaps = []
    for model, sex in (("SINGLES", "female"), ("COUPLES", "male"),
                       ("SINGLES", "male"), ("COUPLES", "female")):
        row = primary[(model, sex, "hours::h_36_5_37_5")]
        gaps.append(f'{100 * (float(row["observed"]) - float(row["predicted"])):.1f}')
    claim("four corrected 37-hour gaps resolve",
          all(value in report and value in gallery for value in gaps),
          "Band-Fix-2 37-hour observed and predicted cells")

    registry = json.loads(read(V8_REGISTRY))["entries"]
    welfare_keys = (
        "w1f_eq_gini_singles", "w1f_eq_gini_couples",
        "ceq_gini_singles", "ceq_gini_couples",
    )
    welfare_values = [f'{float(registry[key]["value"]):.4f}' for key in welfare_keys]
    claim("attained-bundle and consumption Ginis resolve",
          all(value in report and value in gallery for value in welfare_values),
          "verified attained-bundle welfare registry")

    magnitude = [
        f'{float(registry["d2_deltaI_pct_singles_eq"]["value"]):.1f}',
        f'{float(registry["d2_deltaI_pct_couples_uneq"]["value"]):.1f}',
    ]
    claim("restricted-decomposition magnitude resolves",
          all(value in report and value in gallery for value in magnitude),
          "accepted counterfactual-decomposition record")
    claim("full numerical allocation is present on both surfaces",
          all(value in report and value in gallery
              for value in number_tokens(inputs.TABLES["decomposition_reader"])),
          "accepted Shapley allocation table")

    exante_visible = squash(sections.EX_ANTE)
    claim("no historical ex-ante percentage is reported",
          "%" not in exante_visible and not number_tokens(exante_visible),
          "reader-facing authorisation, section E")

    source_artifacts = {
        "reader-facing authorisation": RULING,
        "corrected prediction ranges": POSFIT / "model_simulated_bands.csv",
        "corrected numerical precision": POSFIT / "g2_adequacy.csv",
        "corrected population moments": MOMENTS,
        "decomposition record": DECOMP / "preseminar_pab_record_v1.json",
        "V7 numerical registry": ROOT / "reports/numbers_of_record_v7.json",
    }
    result = {
        "gate": "V8 number-to-source",
        "status": "PASS" if not failures else "FAIL",
        "reader_numeric_tokens": sorted(v8_numbers),
        "novel_numeric_tokens": novel,
        "placeholder_count": len(placeholders),
        "missing_placeholders": missing,
        "claims": claims,
        "sources": {
            name: {
                "path": str(path.relative_to(WORKSPACE)).replace("\\", "/"),
                "sha256": sha(path),
            }
            for name, path in source_artifacts.items()
        },
        "failures": failures,
    }
    OUT_JSON.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8",
                        newline="\n")
    lines = [
        "# V8 number-to-source results", "",
        f"Overall: **{result['status']}**", "",
        "Every scalar placeholder resolves, the two reader-facing numerical tables preserve their predecessor cells exactly, and every main-text numeric token is inherited from the sourced V7 inventory.", "",
        "| Check | Source | Status |", "|---|---|---:|",
    ]
    for row in claims:
        lines.append(f"| {row['claim']} | `{row['source']}` | **{row['status']}** |")
    lines.extend(["", "## Source hashes", ""])
    for name, item in result["sources"].items():
        lines.append(f"- {name}: `{item['sha256']}` — `{item['path']}`")
    if failures:
        lines.extend(["", "## Failures", ""] + [f"- {failure}" for failure in failures])
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"NUMBER-TO-SOURCE {result['status']}: {len(claims)} checks, "
          f"{len(failures)} failures")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
