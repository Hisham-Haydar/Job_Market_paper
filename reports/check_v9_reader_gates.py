"""Reader-language, economics-restoration and boundary checks for V9."""
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

import check_v9_rendered_language as audit  # noqa: E402
import v5_sections as v5  # noqa: E402
import v9_sections as v9  # noqa: E402


REPORT = ROOT / "reports/JMP_research_story_report_v9.html"
GALLERY = ROOT / "reports/JMP_results_gallery_v9.html"
SOURCE = BUILD / "story_v9.generated.md"
OUT_JSON = ROOT / "reports/v9_reader_gate_results.json"
OUT_MD = ROOT / "reports/v9_reader_gate_results.md"


def plain(fragment: str) -> str:
    return audit.rendered_text(fragment)


def outside(path: Path) -> tuple[str, str, str]:
    document = path.read_text(encoding="utf-8")
    visible, appendix = audit.remove_exact_appendix(document)
    return document, plain(visible), plain(appendix)


def main() -> int:
    report_html, report_text_all, appendix_text = outside(REPORT)
    gallery_html, gallery_text, _ = outside(GALLERY)
    main_match = re.search(r'<main id="doc">(.*?)</main>', report_html, flags=re.S)
    if not main_match:
        raise SystemExit("V9 report main element missing")
    main_without_appendix, _ = audit.remove_exact_appendix(main_match.group(1))
    report_text = plain(main_without_appendix)
    source = SOURCE.read_text(encoding="utf-8")
    source_main = source.split(audit.BEGIN_MARKER, 1)[0]
    source_main_lower = source_main.lower()
    failures: list[str] = []
    checks: list[dict[str, str]] = []

    def check(name: str, ok: bool, evidence: str) -> None:
        checks.append({"check": name, "evidence": evidence,
                       "status": "PASS" if ok else "FAIL"})
        if not ok:
            failures.append(name)

    exact_title = (
        "Unequal Job Opportunities and Well-Being Inequality: "
        "A Latent-Jobs Structural Decomposition"
    )
    check("exact unshortened title",
          report_text.count(exact_title) == 1 and exact_title in gallery_text,
          "report and gallery rendered headings")

    titles = [section["title"] for section in v9.SECTIONS if section["key"] != "provenance"]
    positions = [report_text.find(title) for title in titles]
    check("seven-part reader sequence",
          all(position >= 0 for position in positions)
          and positions == sorted(positions),
          "seven ordered main headings")

    v5_words = sum(len(re.findall(r"\b[\w’'-]+\b", section["body"]))
                   for section in v5.SECTIONS
                   if not section.get("appendix") and section["key"] != "notebook")
    v9_words = len(re.findall(r"\b[\w’'-]+\b", report_text))
    check("main-text length restored",
          v9_words >= int(0.9 * v5_words),
          f"V9 {v9_words:,} words; full-content comparator {v5_words:,} words")

    abstract_match = re.search(r'<h2 id="abstract">Abstract</h2>(.*?)(?=<p><em>)',
                               report_html, flags=re.S)
    check("abstract contains both perspectives and caveat",
          bool(abstract_match)
          and "1.8–9.9%" in plain(abstract_match.group(1))
          and "7.9–21.3%" in plain(abstract_match.group(1))
          and "channel ordering diverges" in plain(abstract_match.group(1)).lower()
          and "do not estimate the total share" in plain(abstract_match.group(1)),
          "rendered abstract")

    # Prose is checked in flattened rendered text. Equations are checked in the
    # exact pre-render main-text stream because the language audit deliberately
    # strips MathJax spans; a mathematical symbol must never become an audit hit.
    economics = {
        "utility and Box-Cox": all(token in source_main_lower for token in (
            "deterministic utility", "box-cox", r"\beta_c\log", "leisure curvature")),
        "four-block opportunity density": all(token in report_text for token in (
            "Access", "Hours", "Occupation", "Wage offer", "opportunity density")),
        "maximised conditional criterion and proposal correction": all(
            token in source_main for token in (
                "conditional probability", r"-\log q_{ij}", "computational device",
                "maximised",
            )),
        "maintained separation assumptions": all(token in source_main_lower for token in (
            "smooth in hours", "step function over bands", "excluded shifters",
            "independent of offered hours", "maintained here rather than tested")),
        "attained indifference and closed form": all(token in source_main for token in (
            r"M_i^{\mathrm{att}}", "indifference condition",
            r"\log M_i^{\mathrm{att}}", r"C_i^{\mathrm{obs}}",
            r"\exp\!\left\{")),
        "operator equations and exact allocation": all(token in source_main for token in (
            r"T_Px_i", r"T_Ax_i", r"T_Bx_i", r"I_S^p", r"\phi_k^p", "3!=6")),
        "ex-ante definition and inversion": all(token in source_main for token in (
            r"J_i", r"H_i", r"J_i^{\mathrm{ref}}", r"M_i^{\mathrm{EA}}",
            r"\log J_i-\log H_i")),
    }
    for name, ok in economics.items():
        check(name, ok, "main-text equations and rendered interpretation")

    results_start = report_text.index("What the current results say")
    limits_start = report_text.index("What remains preliminary")
    results = report_text[results_start:limits_start]
    limits = report_text[limits_start:]
    check("both perspectives reported without a primary",
          all(token in results for token in (
              "The two welfare perspectives side by side",
              "Earnings > access", "Access > earnings",
              "Neither measure is designated primary here")),
          "main results comparison")
    check("channel-ordering divergence stated in economics",
          "ex-ante measure values the whole prospect" in results.lower()
          and "attained-bundle measure sees only the realised job" in results.lower()
          and "wages drive disposable consumption" in results.lower(),
          "main results interpretation")
    check("couples equivalisation flag in results and limitations",
          all(token in results for token in ("21.3%", "7.9%", "turns the preference contribution negative"))
          and all(token in limits for token in ("21.3%", "7.9%", "no directional claim about preferences")),
          "sections 5 and 6")
    check("historical context is scoped and non-current",
          "Earlier circulated figures near 90%" in results
          and "all non-preference circumstances" in results
          and "not current results" in results,
          "one short historical paragraph")
    check("ex-ante is never called Measure 1",
          not re.search(r"(?:ex-ante.{0,80}Measure 1|Measure 1.{0,80}ex-ante)",
                        report_text, flags=re.I | re.S),
          "rendered main text")

    for label, path in (("report", REPORT), ("gallery", GALLERY)):
        scan = audit.scan_path(path)
        check(f"banned terms absent from {label}",
              scan["outside_appendix_total"] == 0,
              "unchanged rendered-text term list")
    control = audit.negative_control(REPORT)
    check("negative control fires",
          control["status"] == "PASS"
          and control["observed_audit_result"] == "FAIL"
          and control["observed_s11_count"] > 0,
          "temporary S11 insertion before appendix boundary")

    check("one final collapsed appendix boundary",
          report_html.count(audit.BEGIN_MARKER) == 1
          and report_html.count(audit.END_MARKER) == 1
          and '<details><summary>Show this section</summary>' in report_html
          and not plain(report_html.split(audit.END_MARKER, 1)[1].split("</main>", 1)[0]),
          "exact marked range at end of report main")
    check("technical ex-ante record is in appendix",
          all(token in appendix_text for token in (
              "Integration design", "Pricing volume", "351,024,407",
              "Reference-domain convention", "Certification gates",
              "Sensitivities", "C12")),
          "collapsed appendix")
    check("gallery is synchronised",
          all(token in gallery_text for token in (
              "What the two decompositions say", "21.3%", "7.9%",
              "about three times", "Neither perspective is designated primary")),
          "reader-facing gallery")

    diff = subprocess.run(
        ["git", "diff", "--exit-code", "--",
         "reports/JMP_research_story_report_v8.html",
         "reports/JMP_results_gallery_v8.html",
         "reports/research_story_build/v8_sections.py",
         "reports/research_story_build/v8_render_inputs.py",
         "reports/research_story_build/build_v8.py"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    check("V8 is untouched", diff.returncode == 0,
          "git diff over V8 report, gallery and source")
    check("no unresolved source tokens", "{{" not in source,
          "generated V9 Markdown")

    result = {
        "gate": "V9 reader-facing economics release",
        "status": "PASS" if not failures else "FAIL",
        "v5_comparator_words": v5_words,
        "v9_main_words": v9_words,
        "checks": checks,
        "failures": failures,
    }
    OUT_JSON.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8", newline="\n")
    lines = ["# V9 reader and economics gate results", "",
             f"Overall: **{result['status']}**", "",
             "| Check | Evidence | Status |", "|---|---|---:|"]
    lines.extend(f"| {row['check']} | {row['evidence']} | **{row['status']}** |"
                 for row in checks)
    if failures:
        lines.extend(["", "## Failures", ""] + [f"- {item}" for item in failures])
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"V9 READER GATES {result['status']}: {len(checks)} checks, "
          f"{len(failures)} failures")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
