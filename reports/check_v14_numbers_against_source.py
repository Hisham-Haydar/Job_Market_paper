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

import check_v14_rendered_language as audit  # noqa: E402
import v14_render_inputs as inputs  # noqa: E402
import v14_sections as sections  # noqa: E402


WEA = WORKSPACE / "MNL_wea/docs/wea_sprint_1/stage4/stage4_certification_and_results_v1.json"
MEMO = WORKSPACE / "MNL_wea/docs/wea_sprint_1/WEA_SPRINT_1_result_memo_v1.md"
MATCHED = ROOT / "reports/v11_matched_households.json"
REPORT = ROOT / "reports/JMP_research_story_report_v14.html"
GALLERY = ROOT / "reports/JMP_results_gallery_v14.html"
REGISTRY = ROOT / "reports/numbers_of_record_v14.json"
REGISTRY_V10 = ROOT / "reports/numbers_of_record_v13.json"
OUT_JSON = ROOT / "reports/v14_number_to_source_results.json"
OUT_MD = ROOT / "reports/v14_number_to_source_results.md"


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
    claim("every V13 registry value unchanged in V14", not changed,
          "numbers_of_record_v13.json vs v14 (" + (", ".join(changed) or "no differences") + ")")
    new_keys = sorted(set(registry) - set(carried))
    claim("V14 adds no registry key",
          not new_keys, ", ".join(new_keys))

    bodies = "\n".join(s["body"] for s in sections.SECTIONS) + sections.ABSTRACT
    placeholders = re.findall(r"\{\{n:([^|}]+?)(?:\|([^}]+))?\}\}", bodies)
    missing = sorted({k for k, _ in placeholders if k not in inputs.REG})
    claim("every scalar placeholder resolves", not missing, "V14 registry")

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

    # ---- V13 figures: every printed number re-derived independently -------------
    import csv as _csv
    from PIL import Image as _Image
    figure_values = json.loads((ROOT / "reports/v13_figure_values.json").read_text(encoding="utf-8"))["values"]
    decomp = WORKSPACE / "MNL_decomp/outputs/welfare/preseminar_pab_v1"

    def csv_rows(name):
        with (decomp / name).open(encoding="utf-8", newline="") as handle:
            return list(_csv.DictReader(handle))

    expected_figure: dict[str, float] = {}
    for pop in ("singles", "couples"):
        shap, coal = csv_rows(f"shapley_PAB_{pop}.csv"), csv_rows(f"coalition_values_{pop}.csv")
        for scale in ("unequivalised", "equivalised"):
            expected_figure[f"att_{pop}_{scale}_baseline_gini"] = float(next(
                r["I_S_gini"] for r in coal if r["scale"] == scale and r["coalition"] == "EMPTY"))
            expected_figure[f"ea_{pop}_{scale}_baseline_gini"] = record["results"][pop][scale]["gini_EMPTY"]
            for f in ("P", "A", "B"):
                expected_figure[f"att_{pop}_{scale}_phi_{f.lower()}"] = float(next(
                    r["gini_point_contribution"] for r in shap if r["scale"] == scale and r["factor"] == f))
                expected_figure[f"ea_{pop}_{scale}_phi_{f.lower()}"] = record["results"][pop][scale]["phi"][f]
            comp, res = record["comparison_W1F"][pop][scale], record["results"][pop][scale]
            for f in ("A", "B"):
                expected_figure[f"central_att_{pop}_{scale}_{f.lower()}_pct_baseline"] = 100 * comp["W1F_phi"][f] / comp["W1F_gini_EMPTY"]
                expected_figure[f"central_ea_{pop}_{scale}_{f.lower()}_pct_baseline"] = 100 * res["phi"][f] / res["gini_EMPTY"]
    claim("every number printed on a V13 figure is listed and nothing extra is printed",
          set(figure_values) == set(expected_figure), f"{len(figure_values)} printed figure values")
    mismatched = [k for k, e in expected_figure.items()
                  if k not in figure_values or abs(figure_values[k]["value"] - e) > 1e-12
                  or figure_values[k]["text"] != format(e, figure_values[k]["format"])]
    claim("figure values equal the certified CSV and JSON sources, including printed text", not mismatched,
          ", ".join(mismatched) or "shapley_PAB_*.csv, coalition_values_*.csv, stage-4 record")
    claim("figure values registered in the V13 registry",
          all(registry.get("fig13_" + k, {}).get("value") == v["value"] for k, v in figure_values.items()),
          "fig13_* registry keys")
    claim("attained-bundle CSV contributions equal the certified comparison record",
          all(abs(expected_figure[f"att_{p}_{s}_phi_{f.lower()}"] - record["comparison_W1F"][p][s]["W1F_phi"][f]) < 1e-12
              for p in ("singles", "couples") for s in ("unequivalised", "equivalised") for f in ("P", "A", "B")),
          "shapley_PAB_*.csv vs comparison_W1F")
    singles_reverse = all(
        (record["comparison_W1F"]["singles"][s]["W1F_phi"]["B"] > record["comparison_W1F"]["singles"][s]["W1F_phi"]["A"])
        and (record["results"]["singles"][s]["phi"]["A"] > record["results"]["singles"][s]["phi"]["B"])
        for s in ("unequivalised", "equivalised"))
    couples_no_reverse = all(
        (record["comparison_W1F"]["couples"][s]["W1F_phi"]["B"] > record["comparison_W1F"]["couples"][s]["W1F_phi"]["A"])
        and (record["results"]["couples"][s]["phi"]["B"] > record["results"]["couples"][s]["phi"]["A"])
        for s in ("unequivalised", "equivalised"))
    claim("central figure verdicts match the record: singles reverse, couples do not",
          singles_reverse and couples_no_reverse, "stage-4 record orderings")
    fig_dir = ROOT / "manuscript/figures/v13"
    new_figs = sorted(fig_dir.glob("fig_v13_*.png"))
    old_hashes = {hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in (WORKSPACE / "MNL_decomp/outputs/welfare/preseminar_pab_v1").glob("*.png")}
    claim("four new figures, palette-encoded, none reusing an old image",
          len(new_figs) == 4 and all(_Image.open(p).mode == "P" for p in new_figs)
          and not ({sha(p) for p in new_figs} & old_hashes), ", ".join(p.name for p in new_figs))
    v11_manifest = json.loads((ROOT / "reports/v11_surface_manifest.json").read_text(encoding="utf-8"))
    matched_pin = next(r["sha256"] for r in v11_manifest["surfaces"] if r["surface"] == "matched-household figure")
    claim("matched-household figure byte-identical to V11",
          sha(ROOT / "manuscript/figures/v11/fig_matched_households_v11.png") == matched_pin, "V11 manifest")

    # ---- V14 theory figure ----------------------------------------------------------
    import base64 as _b64
    theory = ROOT / "manuscript/figures/v14/fig_v14_theory_own_set.png"
    caption_digits = re.findall(r"\d+", inputs.THEORY_CAPTION)
    claim("theory figure carries no estimated or certified number",
          caption_digits == ["2026", "3"] and not any(k.startswith("fig14") for k in registry),
          "caption digits " + ", ".join(caption_digits) + "; generator draws no numeric ticks")
    claim("theory figure regenerated, palette-encoded, not the old stored image",
          _Image.open(theory).mode == "P"
          and sha(theory) not in {sha(p) for p in (ROOT / "manuscript/figures").glob("v*/theory_w1.png")},
          "fig_v14_theory_own_set.png")

    def embedded(path):
        doc = path.read_text(encoding="utf-8")
        return [m for m in re.findall(r"data:image/png;base64,([A-Za-z0-9+/=]+)", doc)]

    v14_theory = _b64.b64encode(theory.read_bytes()).decode()
    for surface in ("research_story_report", "results_gallery"):
        old = sorted(embedded(ROOT / f"reports/JMP_{surface}_v13.html"))
        new = embedded(ROOT / f"reports/JMP_{surface}_v14.html")
        others = sorted(x for x in new if x != v14_theory)
        claim(f"{surface}: every other figure byte-identical to V13",
              others == old and new.count(v14_theory) == 1, f"{len(old)} V13 images, {len(new)} V14 images")

    memo = MEMO.read_text(encoding="utf-8")
    claim("pricing count 351,024,407 matches the result memo and report appendix",
          "**351,024,407**" in memo and "351,024,407" in REPORT.read_text(encoding="utf-8"), "result memo table")

    sources = {name: {"path": str(path.relative_to(WORKSPACE)).replace("\\", "/"), "sha256": sha(path)}
               for name, path in (("certified ex-ante result record", WEA), ("certified result memo", MEMO),
                                  ("matched-household record", MATCHED), ("V13 predecessor registry", REGISTRY_V10))}
    result = {"gate": "V14 number-to-source", "status": "PASS" if not failures else "FAIL",
              "placeholder_count": len(placeholders), "claims": claims, "sources": sources, "failures": failures}
    OUT_JSON.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    lines = ["# V14 number-to-source results", "", f"Overall: **{result['status']}**", "",
             "| Check | Source | Status |", "|---|---|---:|"]
    lines.extend(f"| {r['claim']} | `{r['source']}` | **{r['status']}** |" for r in claims)
    lines.extend(["", "## Source hashes", ""])
    lines.extend(f"- {n}: `{i['sha256']}` — `{i['path']}`" for n, i in sources.items())
    if failures:
        lines.extend(["", "## Failures", ""] + [f"- {x}" for x in failures])
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"V14 NUMBER-TO-SOURCE {result['status']}: {len(claims)} checks, {len(failures)} failures")
    for x in failures:
        print("  FAIL:", x)
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
