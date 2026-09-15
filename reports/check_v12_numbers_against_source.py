"""Trace every V11 welfare and illustration number to its source record."""
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

import check_v12_rendered_language as audit  # noqa: E402
import v12_render_inputs as inputs  # noqa: E402
import v12_sections as sections  # noqa: E402


WEA = WORKSPACE / "MNL_wea/docs/wea_sprint_1/stage4/stage4_certification_and_results_v1.json"
MEMO = WORKSPACE / "MNL_wea/docs/wea_sprint_1/WEA_SPRINT_1_result_memo_v1.md"
MATCHED = ROOT / "reports/v11_matched_households.json"
REPORT = ROOT / "reports/JMP_research_story_report_v12.html"
GALLERY = ROOT / "reports/JMP_results_gallery_v12.html"
REGISTRY = ROOT / "reports/numbers_of_record_v12.json"
REGISTRY_V10 = ROOT / "reports/numbers_of_record_v11.json"
OUT_JSON = ROOT / "reports/v12_number_to_source_results.json"
OUT_MD = ROOT / "reports/v12_number_to_source_results.md"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def visible(path: Path) -> str:
    outside, _ = audit.remove_exact_appendix(path.read_text(encoding="utf-8"))
    return audit.rendered_text(outside)


def main() -> int:
    record = json.loads(WEA.read_text(encoding="utf-8"))
    matched = json.loads(MATCHED.read_text(encoding="utf-8"))
    report, gallery = visible(REPORT), visible(GALLERY)
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))["entries"]
    registry_v10 = json.loads(REGISTRY_V10.read_text(encoding="utf-8"))["entries"]
    claims: list[dict[str, str]] = []
    failures: list[str] = []

    def claim(name: str, ok: bool, source: str) -> None:
        claims.append({"claim": name, "source": source, "status": "PASS" if ok else "FAIL"})
        if not ok:
            failures.append(name)

    claim("all certification checks pass",
          all(all(record["overall"][p].values()) for p in ("singles", "couples"))
          and all(record["overall"]["C12_household"].values()), "certified record overall block")

    carried = {k: v for k, v in registry_v10.items()}
    changed = [k for k, v in carried.items() if registry.get(k) != v]
    claim("every V11 registry value unchanged in V12", not changed,
          "numbers_of_record_v11.json vs v12 (" + (", ".join(changed) or "no differences") + ")")
    new_keys = sorted(set(registry) - set(carried))
    claim("V12 adds no registry key",
          not new_keys, ", ".join(new_keys))

    bodies = "\n".join(s["body"] for s in sections.SECTIONS) + sections.ABSTRACT
    placeholders = re.findall(r"\{\{n:([^|}]+?)(?:\|([^}]+))?\}\}", bodies)
    missing = sorted({k for k, _ in placeholders if k not in inputs.REG})
    claim("every scalar placeholder resolves", not missing, "V12 registry")

    expected = {("singles", "unequivalised"): (14.8, "Access > earnings"),
                ("singles", "equivalised"): (20.3, "Access > earnings"),
                ("couples", "unequivalised"): (21.3, "Earnings > access"),
                ("couples", "equivalised"): (7.9, "Earnings > access")}
    tables = inputs.TABLES["wea_results"] + inputs.TABLES["perspective_comparison"]
    for (population, scale), (rounded, ordering) in expected.items():
        row = record["results"][population][scale]
        label = f"{row['A_plus_B_pct_of_baseline_gini']:.1f}%"
        claim(f"{population} {scale} ex-ante result",
              round(row["A_plus_B_pct_of_baseline_gini"], 1) == rounded
              and label in tables and ordering in tables and label in report and label in gallery,
              f"results.{population}.{scale}")

    att = [record["comparison_W1F"][p][s]["W1F_A_plus_B_pct_of_baseline"]
           for p in ("singles", "couples") for s in ("unequivalised", "equivalised")]
    claim("attained comparison values from the certified record",
          [round(v, 1) for v in att] == [2.4, 1.9, 6.7, 3.5]
          and all(f"{v:.1f}%" in inputs.TABLES["perspective_comparison"] for v in att),
          "comparison_W1F block")
    claim("attained A+B range is the sourced minimum and maximum",
          f"{min(att):.1f}–{max(att):.1f}%" in report
          and registry["att_opportunity_min_pct"]["value"] == min(att)
          and registry["att_opportunity_max_pct"]["value"] == max(att),
          "derived over four comparison_W1F shares")
    ea = [row["A_plus_B_pct_of_baseline_gini"] for pop in record["results"].values() for row in pop.values()]
    claim("ex-ante A+B range is the sourced minimum and maximum",
          f"{min(ea):.1f}–{max(ea):.1f}%" in report, "derived over four certified shares")
    s = record["results"]["singles"]
    ratios = [s[k]["phi"]["A"] / s[k]["phi"]["B"] for k in ("unequivalised", "equivalised")]
    claim("single-adult access about three times earnings",
          all(3.0 < r < 3.5 for r in ratios) and all(f"{r:.1f}" in report for r in ratios), "singles phi.A/phi.B")
    c = record["results"]["couples"]
    claim("couples: no reversal, equivalisation and preference sign",
          not c["unequivalised"]["B_gt_A"] is False and c["unequivalised"]["B_gt_A"] and c["equivalised"]["B_gt_A"]
          and all(record["comparison_W1F"]["couples"][k]["W1F_B_gt_A"] for k in ("unequivalised", "equivalised"))
          and c["unequivalised"]["phi"]["P"] > 0 > c["equivalised"]["phi"]["P"]
          and "21.3%" in gallery and "7.9%" in gallery, "couples rows")
    claim("singles reversal: ATT earnings > access, EA access > earnings",
          all(record["comparison_W1F"]["singles"][k]["W1F_B_gt_A"] for k in ("unequivalised", "equivalised"))
          and not any(s[k]["B_gt_A"] for k in ("unequivalised", "equivalised")), "singles rows")

    for key, entry in registry.items():
        if not key.startswith("mh_"):
            continue
        field = entry["source"].split("::", 1)[1]
        value = matched
        for part in field.split("."):
            value = value[part]
        claim(f"illustration {key} equals its record", value == entry["value"], entry["source"])
    claim("illustration numbers displayed as sourced",
          all(t in report for t in (f"{matched['access_mass_ratio_A_over_B']:.1f} times",
                                    f"{matched['wage_location_gap_B_minus_A_logpoints']:.1f} log points",
                                    f"{matched['opportunity_employment_share_A']:.2f}",
                                    f"{matched['opportunity_employment_share_B']:.2f}"))
          and f"{matched['access_mass_ratio_A_over_B']:.1f}" in gallery, "v11_matched_households.json")
    claim("illustration dominance statements match the record",
          matched["wage_offer_FOSD_B_over_A"] and not matched["wage_offer_FOSD_A_over_B"]
          and matched["hours_density_distance"] == 0.0 and matched["occupation_mass_distance"] == 0.0,
          "v11_matched_households.json")
    identifier_like = [k for k in json.dumps(matched).lower().split('"')
                       if k in ("source_idhh", "idhh", "idperson", "row", "region", "gsur", "dwt", "age")]
    claim("illustration record carries no identifier or record value", not identifier_like,
          ", ".join(identifier_like) or "none")

    memo = MEMO.read_text(encoding="utf-8")
    claim("pricing count 351,024,407 matches the result memo and report appendix",
          "**351,024,407**" in memo and "351,024,407" in REPORT.read_text(encoding="utf-8"), "result memo table")

    sources = {name: {"path": str(path.relative_to(WORKSPACE)).replace("\\", "/"), "sha256": sha(path)}
               for name, path in (("certified ex-ante result record", WEA), ("certified result memo", MEMO),
                                  ("matched-household record", MATCHED), ("V12 registry", REGISTRY_V10))}
    result = {"gate": "V12 number-to-source", "status": "PASS" if not failures else "FAIL",
              "placeholder_count": len(placeholders), "claims": claims, "sources": sources, "failures": failures}
    OUT_JSON.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    lines = ["# V12 number-to-source results", "", f"Overall: **{result['status']}**", "",
             "| Check | Source | Status |", "|---|---|---:|"]
    lines.extend(f"| {r['claim']} | `{r['source']}` | **{r['status']}** |" for r in claims)
    lines.extend(["", "## Source hashes", ""])
    lines.extend(f"- {n}: `{i['sha256']}` — `{i['path']}`" for n, i in sources.items())
    if failures:
        lines.extend(["", "## Failures", ""] + [f"- {x}" for x in failures])
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"V12 NUMBER-TO-SOURCE {result['status']}: {len(claims)} checks, {len(failures)} failures")
    for x in failures:
        print("  FAIL:", x)
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
