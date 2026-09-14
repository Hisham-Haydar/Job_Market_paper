"""Reader-language, structure, preservation, and gallery checks for V8."""
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

import check_v8_rendered_language as rendered_audit  # noqa: E402
import v7_sections as v7  # noqa: E402
import v8_sections as v8  # noqa: E402


REPORT = ROOT / "reports/JMP_research_story_report_v8.html"
GALLERY = ROOT / "reports/JMP_results_gallery_v8.html"
SOURCE = BUILD / "story_v8.generated.md"
OUT_JSON = ROOT / "reports/v8_reader_gate_results.json"
OUT_MD = ROOT / "reports/v8_reader_gate_results.md"
MAP_JSON = ROOT / "reports/v8_section_map.json"
MAP_MD = ROOT / "reports/v8_section_map.md"


BANNED = rendered_audit.BANNED


SECTION_MAP = [
    ("Abstract", "Replaced by the authorised magnitude paragraph; the predecessor abstract is deliberately omitted."),
    ("Status note", "Deleted; the report uses the required ongoing-validation language and names no predecessor version."),
    ("Introduction", "Economic motivation moved to main section 1; model, welfare and extension material moved to main sections 2, 3 and 7; full block retained in the provenance appendix."),
    ("Data", "Core sample and institutional facts condensed into main section 2; full tables and screens retained in the provenance appendix."),
    ("A latent-jobs model of household labour supply", "Economic mechanism and maintained restrictions condensed into main section 2; equations and estimation details retained in the provenance appendix."),
    ("Money-metric well-being and structural inequality decomposition", "Attained-bundle economics moved to main section 3 and counterfactual logic to main section 4; technical formulae and domain conventions retained in the provenance appendix."),
    ("Empirical results", "Headline fit, welfare and the full numerical allocation moved to main section 5; detailed coefficient, moment and coalition tables retained in the provenance appendix."),
    ("Sensitivity and limitations", "Economic limitations condensed into main section 6; full diagnostic record retained in the provenance appendix."),
    ("Conclusion", "Substantive conclusions distributed across main sections 5–7; predecessor block retained in the provenance appendix."),
    ("Appendix A. The estimated parameter vectors", "Retained wholesale in the collapsed provenance appendix."),
    ("Appendix B. Inequality indices and the allocation rule", "Retained wholesale in the collapsed provenance appendix."),
    ("Appendix C. Data, software and replication", "Retained wholesale in the collapsed provenance appendix."),
    ("Appendix D. Preliminary restricted-operator decomposition", "Numerical headline and complete allocation table moved to main section 5; technical block retained wholesale in the collapsed provenance appendix."),
    ("The research notebook", "Retained wholesale in the collapsed provenance appendix."),
    ("Scientific history of this result", "Retained wholesale in the collapsed provenance appendix."),
    ("Questions for presentation preparation", "Retained wholesale in the collapsed provenance appendix; no questions follow the appendix."),
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def plain_fragment(text: str) -> str:
    return rendered_audit.rendered_text(text)


def outside_appendix(document: str) -> str:
    outside, _ = rendered_audit.remove_exact_appendix(document)
    return rendered_audit.rendered_text(outside)


def report_main_outside_appendix(document: str) -> str:
    outside, _ = rendered_audit.remove_exact_appendix(document)
    main = re.search(r'<main id="doc">(.*?)</main>', outside, flags=re.S)
    if not main:
        raise ValueError("rendered report main element not found")
    return rendered_audit.rendered_text(main.group(1))


def term_pattern(term: str) -> re.Pattern:
    return rendered_audit.term_pattern(term)


def main() -> int:
    report_html = read(REPORT)
    gallery_html = read(GALLERY)
    source = read(SOURCE)
    report_text = report_main_outside_appendix(report_html)
    gallery_text = outside_appendix(gallery_html)
    report_scan = rendered_audit.scan_path(REPORT)
    gallery_scan = rendered_audit.scan_path(GALLERY)
    control = rendered_audit.negative_control(REPORT)
    failures: list[str] = []
    checks: list[dict[str, str]] = []

    def check(name: str, ok: bool, evidence: str) -> None:
        checks.append({"check": name, "evidence": evidence,
                       "status": "PASS" if ok else "FAIL"})
        if not ok:
            failures.append(name)

    expected_titles = [
        "Why income inequality mixes preferences and opportunities",
        "How the latent-jobs model separates preferences from opportunities",
        "How attained bundles become money-metric well-being",
        "How the preliminary counterfactual decomposition works",
        "What the current results say",
        "What remains preliminary",
        "Why an ex-ante opportunity-prospect extension is useful",
    ]
    positions = [report_text.find(title) for title in expected_titles]
    check("seven-part economics sequence", all(pos >= 0 for pos in positions)
          and positions == sorted(positions), "V8 main-section headings")

    abstract_html = re.search(r'<h2 id="abstract">Abstract</h2>(.*?)(?=<p><em>)',
                              report_html, flags=re.S)
    check("authorised abstract with 1.8–9.9%",
          bool(abstract_html)
          and re.sub(r"\s+", " ", plain_fragment(abstract_html.group(1)))
          == re.sub(r"\s+", " ", v8.ABSTRACT)
          and "1.8–9.9%" in report_text,
          "section A paragraph, verbatim after whitespace normalization")

    exante_source = next(s["body"] for s in v8.SECTIONS if s["key"] == "exante")
    check("one-paragraph ex-ante section", exante_source == v8.EX_ANTE
          and "\n\n" not in exante_source and "%" not in exante_source,
          "section E paragraph; no historical percentage")
    check("J/H formulae and domains confined to provenance",
          not re.search(r"\bJ_i\b|\bH_i\b|\bH-[FDX]\b|exact-H", report_text, re.I),
          "reader-facing report text")

    report_hits = report_scan["outside_appendix_total"]
    gallery_hits = gallery_scan["outside_appendix_total"]
    check("banned implementation vocabulary absent from reader-facing report",
          report_hits == 0, "rendered HTML after exact marked-range exclusion")
    check("banned implementation vocabulary absent from reader-facing gallery",
          gallery_hits == 0, "rendered HTML after exact marked-range exclusion")
    check("rendered-language audit negative control fires",
          control["status"] == "PASS"
          and control["observed_audit_result"] == "FAIL"
          and control["observed_s11_count"] > 0,
          "temporary rendered copy with S11 inserted before the appendix marker")
    check("household-weight terminology installed",
          bool(re.search(r"household(?: weights|-weighted)", report_text, re.I))
          and bool(re.search(r"household(?: weights|-weighted)", gallery_text, re.I)),
          "decomposition method and welfare-table caption")

    details_match = re.search(
        r'<h1 id="8-appendix.*?</h1><details><summary>Show this section</summary>',
        report_html,
        flags=re.S,
    )
    gallery_details = re.search(
        r'<section id="provenance">.*?<details><summary>Show technical provenance</summary>',
        gallery_html,
        flags=re.S,
    )
    check("technical provenance is collapsed on both surfaces",
          bool(details_match) and bool(gallery_details),
          "HTML details elements")
    report_after_marker = report_html.split(rendered_audit.END_MARKER, 1)[1]
    gallery_after_marker = gallery_html.split(rendered_audit.END_MARKER, 1)[1]
    check("explicit provenance appendix is the final main-content region",
          not plain_fragment(report_after_marker.split("</main>", 1)[0])
          and not plain_fragment(gallery_after_marker.split("</main>", 1)[0]),
          f"{rendered_audit.BEGIN_MARKER} … {rendered_audit.END_MARKER}")
    toc = re.search(r'<nav id="toc">(.*?)</nav>', report_html, flags=re.S)
    collapsed_body = re.search(
        r'<details><summary>Show this section</summary>(.*?)</details>',
        report_html,
        flags=re.S,
    )
    hidden_ids = (re.findall(r'<h[12] id="([^"]+)"', collapsed_body.group(1))
                  if collapsed_body else [])
    check("collapsed provenance headings omitted from reader navigation",
          bool(toc) and all(f'href="#{heading_id}"' not in toc.group(1)
                            for heading_id in hidden_ids),
          "report table of contents")

    provenance = next(s["body"] for s in v8.SECTIONS if s["key"] == "provenance")
    preserved = (
        v7.ABSTRACT not in provenance
        and v7.PRELIM_NOTE not in provenance
        and all(section["body"] in provenance for section in v7.SECTIONS)
        and all(question in provenance and answer in provenance for question, answer in v7.QA)
    )
    check("technical blocks retained wholesale and old abstract/status deleted",
          preserved, "direct source-string containment")
    check("no predecessor-version label is rendered",
          not re.search(r"(?<![A-Za-z0-9])V7(?![A-Za-z0-9])",
                        plain_fragment(report_html), flags=re.I),
          "complete rendered report, including the opened appendix")

    results_start = report_text.index("What the current results say")
    limits_start = report_text.index("What remains preliminary")
    results = report_text[results_start:limits_start]
    check("full decomposition allocation remains in main results",
          "Complete Shapley allocation" in results
          and all(token in results for token in ("58.6%", "124.0%", "4.6%", "29.6%")),
          "main section 5 numerical table")
    check("restricted-exercise caveat accompanies decomposition",
          "They do not estimate the total share of well-being inequality caused by unequal job opportunities." in results,
          "main section 5")
    check("corrected predictive-fit disposition retained",
          all(text in results for text in (
              "Coupled men’s extensive accuracy is WITHHELD",
              "observed 37-hour mass point", "3.8", "6.5",
          )), "main section 5")
    check("short-hours limitation retained",
          "represents the lower part of the modelled hours range sparsely" in report_text
          and "substantial model-implied mass" in report_text
          and "below ten hours" in report_text,
          "main section 6")
    ongoing = "preliminary and subject to ongoing numerical validation of the counterfactual integration"
    check("required ongoing-work language", ongoing in report_text
          and "still cleaning the results" not in report_text.lower(),
          "status note and main section 6")

    figure_count = len(re.findall(r"<figure(?:\s|>)", gallery_html))
    caption_count = len(re.findall(r"<figcaption(?:\s|>)", gallery_html))
    standalone = gallery_html.count("<figcaption class=standalone>")
    all_caption_html = " ".join(
        re.findall(r"<(?:figcaption|caption)\b[^>]*>.*?</(?:figcaption|caption)>",
                   report_html + gallery_html, flags=re.S | re.I)
    )
    all_caption_text = plain_fragment(all_caption_html)
    source_caption_text = " ".join(
        line for line in source.splitlines()
        if line.startswith("Table:") or line.startswith("![")
    )
    check("household-weighted wording used in every weight caption",
          not term_pattern("dwt").search(all_caption_text)
          and "weighted using household weights" not in all_caption_text.lower()
          and not term_pattern("dwt").search(source_caption_text)
          and "weighted using household weights" not in source_caption_text.lower(),
          "rendered report, gallery and editable Markdown captions")
    heading_text = " ".join(re.findall(r"<h[1-3][^>]*>(.*?)</h[1-3]>",
                                       gallery_html[:gallery_html.index('<section id="provenance">')],
                                       flags=re.S | re.I))
    check("gallery headings and captions are reader-facing",
          figure_count + standalone == caption_count
          and not any(term_pattern(term).search(plain_fragment(heading_text))
                      for term in BANNED),
          f"{figure_count} figures, {caption_count} captions")

    v7_paths = [
        "reports/JMP_research_story_report_v7.html",
        "reports/research_story_build/story_v7.generated.md",
        "reports/research_story_build/v7_sections.py",
        "reports/research_story_build/v7_render_inputs.py",
        "reports/numbers_of_record_v7.json",
    ]
    diff = subprocess.run(["git", "diff", "--exit-code", "--", *v7_paths],
                          cwd=ROOT, capture_output=True, text=True)
    check("V7 report and editable sources untouched", diff.returncode == 0,
          "git diff over V7 paths")
    check("no unresolved source tokens", "{{" not in source,
          "generated editable Markdown")

    map_payload = {"status": "PASS" if preserved else "FAIL",
                   "mapping": [{"v7_block": src, "v8_destination": dst}
                               for src, dst in SECTION_MAP]}
    MAP_JSON.write_text(json.dumps(map_payload, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8", newline="\n")
    map_lines = [
        "# V7-to-V8 section map", "",
        f"Overall: **{map_payload['status']}**", "",
        "The predecessor abstract and status note are deliberately omitted. Every detailed section and presentation-preparation block is retained verbatim inside the explicitly marked, collapsed technical-provenance appendix; the table records where its economic content now appears in the reader-facing sequence.", "",
        "| V7 block | V8 destination |", "|---|---|",
    ]
    map_lines.extend(f"| {src} | {dst} |" for src, dst in SECTION_MAP)
    MAP_MD.write_text("\n".join(map_lines) + "\n", encoding="utf-8", newline="\n")

    result = {"gate": "V8 reader-facing release", "status": "PASS" if not failures else "FAIL",
              "checks": checks, "failures": failures}
    OUT_JSON.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8",
                        newline="\n")
    lines = ["# V8 reader-facing gate results", "",
             f"Overall: **{result['status']}**", "",
             "| Check | Evidence | Status |", "|---|---|---:|"]
    lines.extend(f"| {row['check']} | {row['evidence']} | **{row['status']}** |"
                 for row in checks)
    if failures:
        lines.extend(["", "## Failures", ""] + [f"- {failure}" for failure in failures])
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"READER GATES {result['status']}: {len(checks)} checks, {len(failures)} failures")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
