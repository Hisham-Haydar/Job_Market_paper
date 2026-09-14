"""Build the reader-facing V8 report without writing a V7 path.

The stable V6 renderer is reused with V8 sections and a read-only adapter over
the accepted V7 evidence.  Generated targets are redirected to V8 filenames.
"""
from pathlib import Path
import runpy
import re
import sys

import v8_render_inputs
import v8_sections


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PAPER = ROOT / "manuscript"

redirects = {
    (PAPER / "JMP_working_paper_for_seminar_v6.bib").resolve():
        (PAPER / "JMP_working_paper_for_seminar_v8.bib").resolve(),
    (PAPER / "JMP_working_paper_for_seminar_v6.tex").resolve():
        (PAPER / "JMP_working_paper_for_seminar_v8.tex").resolve(),
    (HERE / "story_v6.generated.md").resolve():
        (HERE / "story_v8.generated.md").resolve(),
    (ROOT / "reports/JMP_research_story_report_v6.html").resolve():
        (ROOT / "reports/JMP_research_story_report_v8.html").resolve(),
    (ROOT / "reports/numbers_of_record_v6.json").resolve():
        (ROOT / "reports/numbers_of_record_v8.json").resolve(),
}

original_write_text = Path.write_text
BEGIN_MARKER = "<!-- V8_PROVENANCE_APPENDIX_BEGIN -->"
END_MARKER = "<!-- V8_PROVENANCE_APPENDIX_END -->"


def caption_language(document: str) -> str:
    """Install reader-facing weight language in every visible caption/alt."""
    def clean(text: str) -> str:
        text = re.sub(r"weighted using household weights", "household-weighted",
                      text, flags=re.I)
        text = re.sub(r"dwt-weighted", "household-weighted", text, flags=re.I)
        return re.sub(r"(?<![A-Za-z0-9])dwt(?![A-Za-z0-9])",
                      "household weights", text, flags=re.I)

    def clean_element(match: re.Match) -> str:
        return match.group(1) + clean(match.group(2)) + match.group(3)

    document = re.sub(
        r"(<figcaption\b[^>]*>)(.*?)(</figcaption>)",
        clean_element,
        document,
        flags=re.S | re.I,
    )
    document = re.sub(
        r"(<caption\b[^>]*>)(.*?)(</caption>)",
        clean_element,
        document,
        flags=re.S | re.I,
    )
    document = re.sub(
        r'(\balt=")([^"]*)(")', clean_element, document, flags=re.S | re.I
    )
    return document


def mark_and_move_html_appendix(document: str) -> str:
    """Move the collapsed appendix to the end of main and mark its exact range."""
    pattern = re.compile(
        r'(<h1 id="8-appendix-technical-record-and-provenance">.*?</h1>'
        r'<details><summary>Show this section</summary>.*?</details>)',
        flags=re.S,
    )
    match = pattern.search(document)
    if not match:
        raise RuntimeError("rendered provenance appendix block not found")
    appendix = (
        BEGIN_MARKER
        + '<section id="v8-provenance-appendix" data-audit-exclude="true" '
          'aria-label="Technical record and provenance">'
        + match.group(1)
        + "</section>"
        + END_MARKER
    )
    document = document[:match.start()] + document[match.end():]
    # QA is intentionally empty in V8; remove the renderer's unconditional shell.
    document = re.sub(
        r'<h1 id="questions-for-presentation-preparation">Questions for '
        r'presentation preparation</h1>',
        "",
        document,
        count=1,
    )
    document = re.sub(
        r'<a class="" href="#questions-for-presentation-preparation">.*?</a>',
        "",
        document,
        count=1,
        flags=re.S,
    )
    appendix_link = re.search(
        r'<a class="" href="#8-appendix-technical-record-and-provenance">.*?</a>',
        document,
        flags=re.S,
    )
    if not appendix_link:
        raise RuntimeError("provenance appendix navigation link not found")
    link = appendix_link.group(0)
    document = document[:appendix_link.start()] + document[appendix_link.end():]
    document = document.replace("</nav>", link + "</nav>", 1)
    if document.count("</main>") != 1:
        raise RuntimeError("cannot place provenance appendix at end of main")
    return document.replace("</main>", appendix + "</main>", 1)


def mark_and_move_markdown_appendix(document: str) -> str:
    """Make the editable Markdown mirror the rendered appendix placement."""
    cleaned_lines = []
    for line in document.splitlines():
        if line.startswith("Table:") or line.startswith("!["):
            line = re.sub(r"weighted using household weights",
                          "household-weighted", line, flags=re.I)
            line = re.sub(r"dwt-weighted", "household-weighted", line,
                          flags=re.I)
            line = re.sub(r"(?<![A-Za-z0-9])dwt(?![A-Za-z0-9])",
                          "household weights", line, flags=re.I)
        cleaned_lines.append(line)
    document = "\n".join(cleaned_lines) + "\n"
    pattern = re.compile(
        r'(^# 8\. Appendix\. Technical record and provenance\n.*?)(?=^# Questions '
        r'for presentation preparation\n)',
        flags=re.S | re.M,
    )
    match = pattern.search(document)
    if not match:
        raise RuntimeError("editable provenance appendix block not found")
    appendix_lines = []
    for line in match.group(1).rstrip().splitlines():
        appendix_lines.append(line)
    appendix = "\n".join(appendix_lines) + "\n"
    document = document[:match.start()] + document[match.end():]
    document = re.sub(
        r'^# Questions for presentation preparation\n\s*', "", document,
        count=1, flags=re.M,
    )
    return (
        document.rstrip()
        + "\n\n" + BEGIN_MARKER + "\n"
        + appendix
        + END_MARKER + "\n"
    )


def v8_write_text(path, data, *args, **kwargs):
    target = redirects.get(path.resolve(), path)
    if isinstance(data, str):
        data = data.replace(
            "JMP_working_paper_for_seminar_v6",
            "JMP_working_paper_for_seminar_v8",
        )
        data = data.replace(
            "REPORT-V6: presentation-only successor; frozen v5 tables, figures "
            "and scalar values.",
            "REPORT-V8: reader-facing narrative; corrected V7 numerical evidence "
            "preserved without alteration.",
        )
        data = data.replace(
            "v6; numerical evidence preserved from v5; diagnostic boundary added",
            "v8; reader-facing narrative; corrected V7 evidence preserved",
        )
        if target == redirects[(ROOT / "reports/JMP_research_story_report_v6.html").resolve()]:
            collapsed = re.search(
                r"<details><summary>Show this section</summary>(.*?)</details>",
                data,
                flags=re.S,
            )
            if collapsed:
                for heading_id in re.findall(r'<h[12] id="([^"]+)"', collapsed.group(1)):
                    data = re.sub(
                        r'<a class="(?:sub|)" href="#' + re.escape(heading_id)
                        + r'">.*?</a>',
                        "",
                        data,
                        count=1,
                        flags=re.S,
                    )
            data = caption_language(data)
            data = mark_and_move_html_appendix(data)
        elif target == redirects[(HERE / "story_v6.generated.md").resolve()]:
            data = mark_and_move_markdown_appendix(data)
    kwargs.setdefault("newline", "\n")
    return original_write_text(target, data, *args, **kwargs)


sys.modules["v6_sections"] = v8_sections
sys.modules["v6_render_inputs"] = v8_render_inputs
Path.write_text = v8_write_text
try:
    runpy.run_path(str(HERE / "build_v6.py"), run_name="__main__")
finally:
    Path.write_text = original_write_text

for old, new in redirects.items():
    if not new.is_file():
        raise SystemExit("missing V8 build target: " + str(new))
    if old.exists() and old.stat().st_mtime_ns > new.stat().st_mtime_ns:
        raise SystemExit("V6 write escaped redirect: " + str(old))

print("V8 HTML, editable Markdown, section source and numerical registry written.")
