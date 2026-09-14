"""Reader-language, structure, preservation, and gallery checks for V8."""
from __future__ import annotations

import html
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "reports/research_story_build"
sys.path.insert(0, str(BUILD))

import v7_sections as v7  # noqa: E402
import v8_sections as v8  # noqa: E402


REPORT = ROOT / "reports/JMP_research_story_report_v8.html"
GALLERY = ROOT / "reports/JMP_results_gallery_v8.html"
SOURCE = BUILD / "story_v8.generated.md"
V7_REPORT = ROOT / "reports/JMP_research_story_report_v7.html"
OUT_JSON = ROOT / "reports/v8_reader_gate_results.json"
OUT_MD = ROOT / "reports/v8_reader_gate_results.md"
AUDIT_JSON = ROOT / "reports/v8_banned_term_audit.json"
AUDIT_MD = ROOT / "reports/v8_banned_term_audit.md"
MAP_JSON = ROOT / "reports/v8_section_map.json"
MAP_MD = ROOT / "reports/v8_section_map.md"


BANNED = [
    ("S10", "the estimation or already-priced sample"),
    ("S11", "the preferred specification"),
    ("S12", "the large predictive integration sample"),
    ("POSFIT", "the predictive-fit diagnostics"),
    ("v3b", "the corrected diagnostics"),
    ("DECOMP-2", "the preliminary structural decomposition"),
    ("criterion-A", "the estimation sample"),
    ("Gate 0", "the relevant economic condition"),
    ("anchor", "the observed-job alternative, where economically relevant"),
    ("node", "integration point or job alternative"),
    ("proposal panel", "the numerical integration sample"),
    ("exact-H", "pre-pricing numerical validation"),
    ("H-F", "the full opportunity environment with equal consumption across jobs"),
    ("H-D", "the estimated-domain sensitivity"),
    ("H-X", "the disclosed sample-restriction sensitivity"),
    ("NN state", "the neither-partner-works alternative"),
    ("NN pricing state", "the priced neither-partner-works alternative"),
    ("SHA", "source provenance in the collapsed appendix"),
    ("hash", "source provenance in the collapsed appendix"),
    ("dwt", "household weights"),
    ("worktree", "source provenance in the collapsed appendix"),
    ("registry", "numerical source record in the collapsed appendix"),
    ("G1-G9", "validation checks"),
    ("adjudication", "diagnostic assessment"),
    ("gate", "numerical-precision standard or validation check"),
    ("mission", "omitted from reader-facing prose"),
    ("ruling", "omitted from reader-facing prose"),
]


SECTION_MAP = [
    ("Abstract", "Replaced by the authorised magnitude paragraph; predecessor retained in the collapsed provenance appendix."),
    ("Status note", "Replaced by the required ongoing-validation language; predecessor retained in the collapsed provenance appendix."),
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
    ("Questions for presentation preparation", "Retained wholesale in the collapsed provenance appendix; replaced by three reader-facing questions after the report."),
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def plain_fragment(text: str) -> str:
    text = re.sub(r"<script.*?</script>|<style.*?</style>", " ", text,
                  flags=re.S | re.I)
    text = re.sub(r"<img[^>]*>", " ", text, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def report_main(document: str, appendix_number: int) -> str:
    start = document.index('<main id="doc">')
    stop = document.index(f'<h1 id="{appendix_number}-appendix', start)
    return plain_fragment(document[start:stop])


def report_reader_text(document: str) -> str:
    start = document.index('<main id="doc">')
    body = document[start:document.index('</main>', start)]
    body = re.sub(
        r'<details><summary>Show this section</summary>.*?</details>',
        ' ',
        body,
        flags=re.S,
    )
    return plain_fragment(body)


def gallery_main(document: str) -> str:
    start = document.index("<main>")
    stop = document.index('<section id="provenance">', start)
    return plain_fragment(document[start:stop])


def term_pattern(term: str) -> re.Pattern:
    if term == "G1-G9":
        return re.compile(r"(?<![A-Za-z0-9])G[1-9](?![A-Za-z0-9])", re.I)
    return re.compile(r"(?<![A-Za-z0-9])" + re.escape(term)
                      + r"(?![A-Za-z0-9])", re.I)


def main() -> int:
    report_html = read(REPORT)
    gallery_html = read(GALLERY)
    source = read(SOURCE)
    report_text = report_main(report_html, 8)
    full_reader_text = report_reader_text(report_html)
    gallery_text = gallery_main(gallery_html)
    v7_text = report_main(read(V7_REPORT), 8)
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

    audit_rows = []
    report_hits = 0
    gallery_hits = 0
    for term, replacement in BANNED:
        pattern = term_pattern(term)
        old_count = len(pattern.findall(v7_text))
        new_report = len(pattern.findall(full_reader_text))
        new_gallery = len(pattern.findall(gallery_text))
        report_hits += new_report
        gallery_hits += new_gallery
        audit_rows.append({
            "term": term,
            "v7_reader_count": old_count,
            "v8_report_reader_count": new_report,
            "v8_gallery_reader_count": new_gallery,
            "replacement": replacement,
            "status": "PASS" if new_report == 0 and new_gallery == 0 else "FAIL",
        })
    check("banned implementation vocabulary absent from reader-facing report",
          report_hits == 0, "term-by-term audit")
    check("banned implementation vocabulary absent from reader-facing gallery",
          gallery_hits == 0, "term-by-term audit")
    check("household-weight terminology installed",
          "household weights" in report_text and "household weights" in gallery_text,
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
        v7.ABSTRACT in provenance
        and v7.PRELIM_NOTE in provenance
        and all(section["body"] in provenance for section in v7.SECTIONS)
        and all(question in provenance and answer in provenance for question, answer in v7.QA)
    )
    check("V7 blocks retained wholesale in provenance source", preserved,
          "direct source-string containment")

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
    heading_text = " ".join(re.findall(r"<h[1-3][^>]*>(.*?)</h[1-3]>",
                                       gallery_html[:gallery_html.index('<section id="provenance">')],
                                       flags=re.S | re.I))
    check("gallery headings and captions are reader-facing",
          figure_count + standalone == caption_count
          and not any(term_pattern(term).search(plain_fragment(heading_text))
                      for term, _ in BANNED),
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

    audit_status = "PASS" if report_hits == 0 and gallery_hits == 0 else "FAIL"
    audit_payload = {"status": audit_status, "terms": audit_rows}
    AUDIT_JSON.write_text(json.dumps(audit_payload, indent=2) + "\n", encoding="utf-8",
                          newline="\n")
    audit_lines = [
        "# V8 banned-term deletion/replacement audit", "",
        f"Overall: **{audit_status}**", "",
        "Counts exclude the collapsed technical-provenance appendices and image data.", "",
        "| Banned term | V7 reader count | V8 report | V8 gallery | Reader-facing replacement | Status |",
        "|---|---:|---:|---:|---|---:|",
    ]
    for row in audit_rows:
        audit_lines.append(
            f"| `{row['term']}` | {row['v7_reader_count']} | "
            f"{row['v8_report_reader_count']} | {row['v8_gallery_reader_count']} | "
            f"{row['replacement']} | **{row['status']}** |"
        )
    AUDIT_MD.write_text("\n".join(audit_lines) + "\n", encoding="utf-8",
                        newline="\n")

    map_payload = {"status": "PASS" if preserved else "FAIL",
                   "mapping": [{"v7_block": src, "v8_destination": dst}
                               for src, dst in SECTION_MAP]}
    MAP_JSON.write_text(json.dumps(map_payload, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8", newline="\n")
    map_lines = [
        "# V7-to-V8 section map", "",
        f"Overall: **{map_payload['status']}**", "",
        "Every predecessor block is retained verbatim in the collapsed technical-provenance appendix; the table records where its economic content now appears in the reader-facing sequence.", "",
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
