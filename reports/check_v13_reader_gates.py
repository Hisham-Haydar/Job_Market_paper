"""Reader-language, economic-derivation and boundary checks for V12."""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "reports/research_story_build"
sys.path.insert(0, str(BUILD))
sys.path.insert(0, str(ROOT / "reports"))

import check_v13_rendered_language as audit  # noqa: E402
import v13_sections as v11  # noqa: E402


REPORT = ROOT / "reports/JMP_research_story_report_v13.html"
GALLERY = ROOT / "reports/JMP_results_gallery_v13.html"
SOURCE = BUILD / "story_v13.generated.md"
OUT_JSON = ROOT / "reports/v13_reader_gate_results.json"
OUT_MD = ROOT / "reports/v13_reader_gate_results.md"

# Superseded V4-era headline and fit numbers and stale specification labels.
SUPERSEDED_NUMBERS = ("55.92", "49.16", "34.20", "9.88 per cent", "35.72", "51.20",
                      "8.23", "0.01304", "0.013595", "0.01523", "0.01385")
STALE_LABELS = ("S8", "R240", "floor5", "Mapping F", "W1_F", "own-set equal-consumption",
                "Measure 1", "measure one", "Haydar-Maniquet", "Haydar–Maniquet",
                "Haydar and Maniquet")
IMPLEMENTATION_TOKENS = (
    r"|\mathcal C_i|", r"-\log q_{ij}", "n_{y}", "polishing contracts",
    "exact Hessian", "idperson", "theta_c_singles", "beta_E_y2015",
    "out of fold", "bitwise equivalent", "machine precision",
)


def plain(fragment: str) -> str:
    return audit.rendered_text(fragment).replace("’", "'").replace("‘", "'")


def flat(text: str) -> str:
    return " ".join(text.split())


def main() -> int:
    report_html = REPORT.read_text(encoding="utf-8")
    gallery_html = GALLERY.read_text(encoding="utf-8")
    outside, appendix = audit.remove_exact_appendix(report_html)
    main_match = re.search(r'<main id="doc">(.*?)</main>', report_html, flags=re.S)
    main_outside, _ = audit.remove_exact_appendix(main_match.group(1))
    main_body = main_outside.split('<h1 id="bibliography">', 1)[0]
    report_text = plain(main_body)
    appendix_text = plain(appendix)
    gallery_outside, _ = audit.remove_exact_appendix(gallery_html)
    gallery_text = plain(gallery_outside)
    source = SOURCE.read_text(encoding="utf-8")
    source_main = source.split(audit.BEGIN_MARKER, 1)[0].split("# Bibliography", 1)[0]
    source_flat = flat(source_main)
    checks: list[dict[str, str]] = []
    failures: list[str] = []

    def check(name: str, ok: bool, evidence: str) -> None:
        checks.append({"check": name, "evidence": evidence, "status": "PASS" if ok else "FAIL"})
        if not ok:
            failures.append(name)

    title = v11.TITLE
    check("exact unshortened title", report_text.count(title) == 1 and title in gallery_text,
          "report and gallery rendered headings")
    titles = [s["title"] for s in v11.SECTIONS if s["key"] != "provenance"]
    numbered = [f"{k}. {t}" for k, t in enumerate(titles, 1)]
    positions = [report_text.rfind(t) for t in numbered]

    def section(k: int) -> str:
        end = positions[k + 1] if k + 1 < len(positions) else len(report_text)
        return report_text[positions[k]:end]
    check("six-part reader sequence", all(p >= 0 for p in positions) and positions == sorted(positions),
          " / ".join(titles))

    # Introduction chain before methodology.
    intro = section(0)
    check("introduction states the logical chain before methodology", all(t in intro for t in (
        "Observed income inequality is not necessarily welfare inequality",
        "Observed labour-supply choices do not identify preferences alone",
        "A structural labour-supply model that separates preferences from opportunities",
        "A money-metric welfare mapping", "Structural equalisation counterfactuals",
        "An order-independent decomposition")), "section 1")
    check("why it matters, without a cost-effectiveness claim",
          "can miss heterogeneity in the labour-market prospects" in intro
          and "It does not show that an opportunity policy is more effective or cheaper than redistribution" in intro
          and not re.search(r"opportunity polic\w+ (?:beats|outperforms|is more effective than)",
                            report_text + gallery_text, flags=re.I),
          "section 1 and all rendered text")

    # Equations A-H with WHY / OBJECT / INTERPRETATION / EMPIRICAL USE.
    equations = {
        "A systematic utility": (r"v_i(j)=L_i(j)+\beta_c\log", r"\mathcal B"),
        "B choice law": (r"P_i(j)=\frac{\exp\{v_i(j)\}\,g_i(j)}",),
        "C opportunity factorisation": (r"g_i(j)=g^{E}_i\cdot", r"g^{W}_i(w\mid k)"),
        "D attained-bundle metric": (r"M_i^{\mathrm{att}}", r"\frac{L_i(j_i^{\mathrm{obs}})-L_i(o)}{\beta_c}"),
        "E ex-ante J, H and inversion": (r"J_i", r"H_i", r"\log J_i-\log H_i", r"M_i^{\mathrm{EA}}"),
        "F equivalisation": (r"M_i^{p,\mathrm{eq}}=\frac{M_i^{p}}{e_i}",),
        "G counterfactual inequality": (r"I^p(S)=\mathcal G", r"T_Ax_i"),
        "H Shapley allocation": (r"\phi_k^p", r"\frac{|S|!\,(3-|S|-1)!}{3!}", "3!=6"),
    }
    for name, tokens in equations.items():
        check(f"equation {name} in main text", all(t in source_main for t in tokens), "pre-render source")
    rubric_ok = all(source_main.count(label) >= 6 for label in
                    ("**Why.**", "**Object.**", "**Interpretation.**", "**Empirical use.**"))
    check("WHY -> OBJECT -> INTERPRETATION -> EMPIRICAL USE rubric", rubric_ok,
          "each label appears for every lettered block (A-C, D, E, F, G, H)")

    welfare = section(2)
    check("welfare section organised as outcomes versus prospects",
          "From choices to well-being: outcomes versus prospects" in welfare
          and "ATT: how well off is the household in the bundle it actually attains?" in welfare
          and "EA: how valuable is the distribution of job prospects the household faces?" in welfare
          and flat(v11.PERSPECTIVES_SENTENCE) in flat(welfare), "section 3")
    check("ATT: opportunities act through the attained outcome; staying-home coincidence disclosed",
          "Opportunity density has no direct term in this measure conditional on the attained bundle" in welfare
          and "coincides with the staying-home equivalent" in welfare
          and "not a general theorem" in welfare, "section 3")
    check("EA: four-point interpretation, shock reading and normative caveat",
          all(t in welfare for t in ("values the household's actual consumption prospects",
                                     "own-opportunity, flat-consumption reference",
                                     "constant consumption level",
                                     "Opportunity composition therefore enters welfare directly",
                                     "That is a normative position, not a consequence of estimation")),
          "section 3")
    check("neither perspective framed as a fix or failure",
          "Neither perspective corrects the other" in welfare
          and not re.search(r"\b(fix(es)?|remed(y|ies)|repairs?)\b.{0,40}attained-bundle|attained-bundle.{0,40}\bfail",
                            report_text, flags=re.I), "rendered main text")
    check("equivalisation substantively consequential for couples",
          "substantively consequential, not a formatting choice" in welfare, "section 3")
    check("A is geographic/temporal, not all job opportunities",
          "not all job opportunities" in report_text and "not all job opportunities" in welfare + report_text,
          "sections 2 and 4")

    d_status = flat(v11.D_STATUS)
    check("D status sentence in abstract, introduction, decomposition, gallery",
          flat(report_text).count(d_status) >= 3 and d_status in flat(gallery_text),
          "exact reader-facing wording")
    check("D recorded as planned extension; A+B+D never an opportunity share",
          "planned extension" in report_text and "A+B+D" in report_text
          and "would not be an opportunity share" in report_text
          and not re.search(r"A\s*\+\s*B\s*\+\s*D[^.]{0,60}(?<!not be an )opportunity share(?! )", report_text.replace("would not be an opportunity share", "")),
          "section 4")
    check("P/A/B never described as exhausting welfare inequality",
          "do not exhaust the sources of welfare inequality" in report_text
          and not re.search(r"(?<!not )exhaust(?:s|ive)? (?:all|the sources of) (?:welfare|well-being) inequality",
                            report_text.replace("do not exhaust the sources of welfare inequality", ""),
                            flags=re.I), "rendered main text")

    results = section(4)
    interpretation = flat(v11.INTERPRETATION_SENTENCE)
    check("central result prominent: abstract, introduction, results lead and subsection",
          flat(report_text).count(interpretation) >= 3
          and results.lstrip().startswith(numbered[4] + " Main result.")
          and "The central result: outcomes versus prospects" in results, "sections 1 and 5")
    check("reversal stated as a singles finding; couples no reversal",
          "Couples show no such reversal" in results
          and "The reversal is a finding for single-adult households only" in results
          and "Earnings > access" in results and "Access > earnings" in results, "section 5")
    check("comparison not claimed to isolate the welfare definition",
          "It is not a pure comparison of welfare definitions" in results
          and not re.search(r"isolat\w+ (?:only )?the welfare definition", report_text, flags=re.I)
          and "represents short hours sparsely" in report_text, "sections 5 and 6")
    check("baseline-Gini versus explained-change denominators distinguished",
          "A share of \\(\\Delta I^p\\)" in plain(main_body) or "describes how the movable component is allocated" in report_text,
          "section 4")
    check("neither measure primary", "Neither measure is designated primary here" in results, "section 5")

    illustration = report_text[report_text.find("two matched households"):report_text.find("Identification, in words")]
    check("matched-household illustration present and bounded",
          "not a causal comparison and it is not representative" in illustration
          and "first-order stochastically dominates" in illustration
          and "neither environment is better on every margin" in illustration
          and "Identifiers, exact observed values, ages, regions and local labour-market values are withheld" in illustration,
          "section 2")

    body_impl = [t for t in IMPLEMENTATION_TOKENS if t in source_main]
    check("implementation detail moved out of the body", not body_impl, "absent from body: " + ", ".join(IMPLEMENTATION_TOKENS))
    check("implementation detail present in appendix",
          all(t in appendix_text for t in ("sampled-alternative likelihood and optimiser", "polishing contracts",
                                           "estimated parameter vectors and code names",
                                           "attained-bundle counterfactual simulation",
                                           "predictive-fit numerical precision",
                                           "Implementation record: matched-household illustration",
                                           "Integration design", "Pricing volume", "351,024,407",
                                           "Certification gates", "C12")), "collapsed appendix")

    # ---- V12 structural checks ------------------------------------------------
    check("promoted: observed raw labour-force status in Section 2",
          "Observed raw labour-force status" in section(1) and "Unemployed (LES 5)" in section(1)
          and "Observed raw labour-force status" not in appendix_text, "section 2")
    check("promoted: full fit comparison, fit tables and benchmark in Section 5",
          all(t in results for t in ("Corrected observed and predicted population moments, single adults",
                                     "Corrected observed and predicted population moments, couples",
                                     "two re-estimated common-opportunity benchmarks",
                                     "An earlier claim of excess predictability across three groups is withdrawn")),
          "section 5")
    check("promoted: within-sample equivalised comparison and coalition values in Section 5",
          all(t in results for t in ("no loss index is constructed from it",
                                     "Single adults, the eight P/A/B coalitions",
                                     "Couples, the eight P/A/B coalitions", "Robustness.")), "section 5")
    limits_text = section(5)
    headings = re.findall(r"^#{1,3} (.+)$", source, flags=re.M)
    check("limitations merged into Section 6; no second limitations section",
          all(t in limits_text for t in ("endowment of 75 or 90 hours", "Wage elasticities are not reported",
                                         "common-opportunity benchmarks carried one input defect",
                                         "definitional boundary, not a measurement error"))
          and not any(h.strip().lower() in ("limitations", "what is not established",
                                            "two open econometric questions") for h in headings),
          "section 6 and every heading in the source")
    check("inherited predecessor document removed from appendix",
          "Technical record:" not in source and "Technical presentation-preparation questions" not in source
          and "Scientific history" not in source, "generated V13 Markdown")
    body_words = len(re.findall(r"\b[\w'-]+\b", report_text))
    appendix_words = len(re.findall(r"\b[\w'-]+\b", appendix_text))
    check("appendix about a quarter of the body", appendix_words <= 0.35 * body_words,
          f"appendix {appendix_words:,} words / body {body_words:,} words = {appendix_words / body_words:.2f}")
    section4 = section(3)
    check("figure: architecture diagram in Section 4",
          'data-fig="fig_v13_architecture"' in main_body
          and "How the decomposition is built" in section4, "section 4")
    check("figures: attained-bundle and ex-ante Shapley figures in Section 5",
          all(t in results for t in ("Attained-bundle welfare: exact Shapley contribution",
                                     "Ex-ante welfare: exact Shapley contribution")), "section 5")
    central_start = results.find("The central result: outcomes versus prospects")
    check("figure: central two-perspective figure under The central result",
          central_start >= 0 and results.find("The central result. Access and earning-opportunity", central_start) > central_start,
          "section 5, central result")
    check("no old decomposition image embedded",
          "fig_preseminar_pab_" not in report_html and "fig_preseminar_pab_" not in gallery_html, "report and gallery")
    check("figures follow text: only implementation diagnostics in the appendix",
          appendix.count("<img") == 2 and 'data-fig="node_convergence_v3b"' in appendix
          and 'data-fig="ws4_sectionC_lambda_v1"' in appendix
          and 'data-fig="ws4_sectionC_T_v1"' in main_body, "appendix images: integration convergence, leisure normalisation")
    check("defect (a): Shapley table access cell includes local unemployment exposure",
          report_text.count("Local unemployment exposure, region, urban or rural location, and year") == 4
          and "Region, urban or rural location, and year" not in report_text + gallery_text,
          "Section 5 table and gallery")
    check("defect (b): both passages missed by Stage A carried forward under the superseded label",
          all(t in appendix_text for t in ("Numerically blocked opportunity-prospect metric",
                                           "A separately defined ex-ante metric is being reconstructed"))
          and appendix_text.index("Superseded before V9")
          < appendix_text.index("Numerically blocked opportunity-prospect metric"),
          "historical status statements")
    import hashlib
    manifest = json.loads((ROOT / "reports/v11_surface_manifest.json").read_text(encoding="utf-8"))
    pinned = {row["surface"]: row["sha256"] for row in manifest["surfaces"]}
    check("matched-household illustration exactly as built in V11",
          hashlib.sha256((ROOT / "manuscript/figures/v11/fig_matched_households_v11.png").read_bytes()).hexdigest()
          == pinned["matched-household figure"]
          and hashlib.sha256((ROOT / "reports/v11_matched_households.json").read_bytes()).hexdigest()
          == pinned["matched-household record"]
          and "two matched households" in report_text, "V11 manifest hashes")

    stale_numbers = [n for n in SUPERSEDED_NUMBERS if n in report_text or n in gallery_text]
    check("no superseded V4 number in main text or gallery", not stale_numbers, ", ".join(stale_numbers) or "none")
    stale_labels = [label for label in STALE_LABELS
                    if re.search(r"(?<![A-Za-z0-9])" + re.escape(label) + r"(?![A-Za-z0-9])", report_text + " " + gallery_text)]
    check("no stale specification label or Haydar-Maniquet defensive language", not stale_labels,
          ", ".join(stale_labels) or "none")

    for label, path in (("report", REPORT), ("gallery", GALLERY)):
        scan = audit.scan_path(path)
        check(f"banned terms absent from {label}", scan["outside_appendix_total"] == 0, "rendered-text term list")
    control = audit.negative_control(REPORT)
    check("banned-term negative control fires",
          control["status"] == "PASS" and control["observed_audit_result"] == "FAIL", "temporary S11 insertion")

    check("one final collapsed appendix boundary",
          report_html.count(audit.BEGIN_MARKER) == 1 and report_html.count(audit.END_MARKER) == 1
          and '<details><summary>Show this section</summary>' in report_html, "marked range")
    check("Stage A superseded quotations preserved", appendix_text.count("Superseded before V9") >= 4,
          f"{appendix_text.count('Superseded before V9')} labels")
    check("gallery synchronised",
          all(t in gallery_text for t in ("From choices to well-being: outcomes versus prospects",
                                          "Two matched households", "What the two decompositions say",
                                          "The central result", "Couples show no such reversal")),
          "reader-facing gallery")

    diff = subprocess.run(
        ["git", "diff", "--exit-code", "--",
         "reports/JMP_research_story_report_v9.html", "reports/JMP_results_gallery_v9.html",
         "reports/research_story_build/v9_sections.py", "reports/research_story_build/story_v9.generated.md",
         "reports/JMP_research_story_report_v10.html", "reports/JMP_results_gallery_v10.html",
         "reports/research_story_build/v10_sections.py", "reports/research_story_build/story_v10.generated.md",
         "reports/JMP_research_story_report_v11.html", "reports/JMP_results_gallery_v11.html",
         "reports/research_story_build/v11_sections.py", "reports/research_story_build/story_v11.generated.md",
         "reports/JMP_research_story_report_v12.html", "reports/JMP_results_gallery_v12.html",
         "reports/research_story_build/v12_sections.py", "reports/research_story_build/story_v12.generated.md"],
        cwd=ROOT, capture_output=True, text=True)
    check("V9 to V12 untouched", diff.returncode == 0, "git diff over V9-V11 report, gallery and source")
    check("no unresolved source tokens", "{{" not in source, "generated V13 Markdown")

    result = {"gate": "V13 reader-facing structure, figures and economic derivation", "status": "PASS" if not failures else "FAIL",
              "main_words": len(re.findall(r"\b[\w’'-]+\b", report_text)), "checks": checks, "failures": failures}
    OUT_JSON.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    lines = ["# V13 reader, structure, figures and economics gate results", "", f"Overall: **{result['status']}**", "",
             "| Check | Evidence | Status |", "|---|---|---:|"]
    lines.extend(f"| {r['check']} | {r['evidence'].replace('|', '/')} | **{r['status']}** |" for r in checks)
    if failures:
        lines.extend(["", "## Failures", ""] + [f"- {item}" for item in failures])
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"V13 READER GATES {result['status']}: {len(checks)} checks, {len(failures)} failures")
    for item in failures:
        print("  FAIL:", item)
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
