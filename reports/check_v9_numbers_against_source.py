"""Trace every new V9 welfare result to the certified ex-ante record."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "reports/research_story_build"
WORKSPACE = ROOT.parent
sys.path.insert(0, str(BUILD))
sys.path.insert(0, str(ROOT / "reports"))

import check_v9_rendered_language as audit  # noqa: E402
import v9_render_inputs as inputs  # noqa: E402
import v9_sections as sections  # noqa: E402


WEA = WORKSPACE / "MNL_wea/docs/wea_sprint_1/stage4/stage4_certification_and_results_v1.json"
MEMO = WORKSPACE / "MNL_wea/docs/wea_sprint_1/WEA_SPRINT_1_result_memo_v1.md"
REPORT = ROOT / "reports/JMP_research_story_report_v9.html"
GALLERY = ROOT / "reports/JMP_results_gallery_v9.html"
REGISTRY = ROOT / "reports/numbers_of_record_v9.json"
OUT_JSON = ROOT / "reports/v9_number_to_source_results.json"
OUT_MD = ROOT / "reports/v9_number_to_source_results.md"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def visible(path: Path) -> str:
    outside, _ = audit.remove_exact_appendix(path.read_text(encoding="utf-8"))
    return audit.rendered_text(outside)


def main() -> int:
    record = json.loads(WEA.read_text(encoding="utf-8"))
    report = visible(REPORT)
    gallery = visible(GALLERY)
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))["entries"]
    failures: list[str] = []
    claims: list[dict[str, str]] = []

    def claim(name: str, ok: bool, source: str) -> None:
        claims.append({"claim": name, "source": source,
                       "status": "PASS" if ok else "FAIL"})
        if not ok:
            failures.append(name)

    all_certified = all(
        all(record["overall"][population].values())
        for population in ("singles", "couples")
    ) and all(record["overall"]["C12_household"].values())
    claim("all certification checks pass", all_certified,
          "certified Stage 4 JSON overall block")

    bodies = [section["body"] for section in sections.SECTIONS
              if section["key"] != "provenance"]
    placeholders = re.findall(r"\{\{n:([^|}]+?)(?:\|([^}]+))?\}\}",
                              "\n".join(bodies))
    missing = sorted({key for key, _ in placeholders if key not in inputs.REG})
    claim("every main scalar placeholder resolves", not missing,
          "V9 number registry")

    expected = {
        ("singles", "unequivalised"): (14.8, "Access > earnings"),
        ("singles", "equivalised"): (20.3, "Access > earnings"),
        ("couples", "unequivalised"): (21.3, "Earnings > access"),
        ("couples", "equivalised"): (7.9, "Earnings > access"),
    }
    tables = inputs.TABLES["wea_results"] + inputs.TABLES["perspective_comparison"]
    for (population, scale), (rounded, ordering) in expected.items():
        row = record["results"][population][scale]
        label = f"{row['A_plus_B_pct_of_baseline_gini']:.1f}%"
        claim(f"{population} {scale} ex-ante result",
              float(f"{row['A_plus_B_pct_of_baseline_gini']:.1f}") == rounded
              and label in tables and ordering in tables
              and label in report and label in gallery,
              f"results.{population}.{scale}")

    attained_expected = (2.4, 1.9, 6.7, 3.5)
    attained_values = []
    for population in ("singles", "couples"):
        for scale in ("unequivalised", "equivalised"):
            attained_values.append(round(
                record["comparison_W1F"][population][scale]
                ["W1F_A_plus_B_pct_of_baseline"], 1
            ))
    claim("attained comparison values come from the same record",
          tuple(attained_values) == attained_expected
          and all(f"{value:.1f}%" in inputs.TABLES["perspective_comparison"]
                  for value in attained_values),
          "comparison_W1F block")

    opportunity = [
        row["A_plus_B_pct_of_baseline_gini"]
        for population in record["results"].values()
        for row in population.values()
    ]
    claim("abstract ex-ante range is the sourced minimum and maximum",
          round(min(opportunity), 1) == 7.9
          and round(max(opportunity), 1) == 21.3
          and "7.9–21.3%" in report,
          "derived over four certified A+B shares")

    s = record["results"]["singles"]
    ratios = [s[scale]["phi"]["A"] / s[scale]["phi"]["B"]
              for scale in ("unequivalised", "equivalised")]
    claim("single-adult access is about three times earnings",
          all(3.0 < ratio < 3.5 for ratio in ratios)
          and all(f"{ratio:.1f}" in report for ratio in ratios),
          "singles phi.A / phi.B")

    c = record["results"]["couples"]
    claim("couples equivalisation and preference sign",
          round(c["unequivalised"]["A_plus_B_pct_of_baseline_gini"], 1) == 21.3
          and round(c["equivalised"]["A_plus_B_pct_of_baseline_gini"], 1) == 7.9
          and c["unequivalised"]["phi"]["P"] > 0
          and c["equivalised"]["phi"]["P"] < 0,
          "couples raw/equivalised certified rows")

    wea_registry = {key: value for key, value in registry.items()
                    if key.startswith("wea_")}
    claim("new registry entries point only to the certified record",
          bool(wea_registry)
          and all("stage4_certification_and_results_v1.json" in item["source"]
                  for item in wea_registry.values()),
          "V9 numerical registry source fields")

    sources = {
        "certified ex-ante result record": {"path": str(WEA.relative_to(WORKSPACE)).replace("\\", "/"),
                                            "sha256": sha(WEA)},
        "certified result memo": {"path": str(MEMO.relative_to(WORKSPACE)).replace("\\", "/"),
                                  "sha256": sha(MEMO)},
        "attained-bundle predecessor registry": {
            "path": "Job_Market_paper/reports/numbers_of_record_v8.json",
            "sha256": sha(ROOT / "reports/numbers_of_record_v8.json"),
        },
    }
    result = {
        "gate": "V9 number-to-source",
        "status": "PASS" if not failures else "FAIL",
        "placeholder_count": len(placeholders),
        "missing_placeholders": missing,
        "claims": claims,
        "sources": sources,
        "failures": failures,
    }
    OUT_JSON.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8", newline="\n")
    lines = ["# V9 number-to-source results", "",
             f"Overall: **{result['status']}**", "",
             "| Check | Source | Status |", "|---|---|---:|"]
    lines.extend(f"| {row['claim']} | `{row['source']}` | **{row['status']}** |"
                 for row in claims)
    lines.extend(["", "## Source hashes", ""])
    for name, item in sources.items():
        lines.append(f"- {name}: `{item['sha256']}` — `{item['path']}`")
    if failures:
        lines.extend(["", "## Failures", ""] + [f"- {item}" for item in failures])
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"V9 NUMBER-TO-SOURCE {result['status']}: {len(claims)} checks, "
          f"{len(failures)} failures")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
