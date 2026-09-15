"""Build V12 without writing any V11, V10 or V9 path.

V12 is the structural release that removes the duplicate appendix document (see v12_sections.py). The paper TeX/bib outputs that the underlying v6 engine
always produces are not part of this task and are redirected to a scratch
location instead of a new manuscript version, so no manuscript file is
touched.
"""
from __future__ import annotations

from pathlib import Path
import runpy
import re
import sys

import v12_render_inputs
import v12_sections


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PAPER = ROOT / "manuscript"
SCRATCH = Path(
    r"C:\Users\hisham\AppData\Local\Temp\48\claude\c--Users-hisham-Repo"
    r"\7ffcd4f5-580f-46bd-a91d-cb1ea33c1d02\scratchpad"
)
SCRATCH.mkdir(parents=True, exist_ok=True)

redirects = {
    (PAPER / "JMP_working_paper_for_seminar_v6.bib").resolve():
        (SCRATCH / "v12_unused_paper.bib").resolve(),
    (PAPER / "JMP_working_paper_for_seminar_v6.tex").resolve():
        (SCRATCH / "v12_unused_paper.tex").resolve(),
    (HERE / "story_v6.generated.md").resolve():
        (HERE / "story_v12.generated.md").resolve(),
    (ROOT / "reports/JMP_research_story_report_v6.html").resolve():
        (ROOT / "reports/JMP_research_story_report_v12.html").resolve(),
    (ROOT / "reports/numbers_of_record_v6.json").resolve():
        (ROOT / "reports/numbers_of_record_v12.json").resolve(),
}

original_write_text = Path.write_text
BEGIN_MARKER = "<!-- V12_PROVENANCE_APPENDIX_BEGIN -->"
END_MARKER = "<!-- V12_PROVENANCE_APPENDIX_END -->"


def caption_language(document: str) -> str:
    def clean(text: str) -> str:
        text = re.sub(r"weighted using household weights", "household-weighted",
                      text, flags=re.I)
        text = re.sub(r"dwt-weighted", "household-weighted", text, flags=re.I)
        return re.sub(r"(?<![A-Za-z0-9])dwt(?![A-Za-z0-9])",
                      "household weights", text, flags=re.I)

    def clean_element(match: re.Match) -> str:
        return match.group(1) + clean(match.group(2)) + match.group(3)

    document = re.sub(r"(<figcaption\b[^>]*>)(.*?)(</figcaption>)",
                      clean_element, document, flags=re.S | re.I)
    document = re.sub(r"(<caption\b[^>]*>)(.*?)(</caption>)",
                      clean_element, document, flags=re.S | re.I)
    document = re.sub(r'(\balt=")([^"]*)(")', clean_element, document,
                      flags=re.S | re.I)
    return document


def mark_and_move_html_appendix(document: str) -> str:
    pattern = re.compile(
        r'(<h1 id="7-appendix-technical-record-and-provenance">.*?</h1>'
        r'<details><summary>Show this section</summary>.*?</details>)',
        flags=re.S,
    )
    match = pattern.search(document)
    if not match:
        raise RuntimeError("rendered V12 provenance appendix block not found")
    appendix = (
        BEGIN_MARKER
        + '<section id="v12-provenance-appendix" data-audit-exclude="true" '
          'aria-label="Technical record and provenance">'
        + match.group(1)
        + "</section>"
        + END_MARKER
    )
    document = document[:match.start()] + document[match.end():]
    document = re.sub(
        r'<h1 id="questions-for-presentation-preparation">Questions for '
        r'presentation preparation</h1>', "", document, count=1,
    )
    document = re.sub(
        r'<a class="" href="#questions-for-presentation-preparation">.*?</a>',
        "", document, count=1, flags=re.S,
    )
    appendix_link = re.search(
        r'<a class="" href="#7-appendix-technical-record-and-provenance">.*?</a>',
        document, flags=re.S,
    )
    if not appendix_link:
        raise RuntimeError("V12 provenance appendix navigation link not found")
    link = appendix_link.group(0)
    document = document[:appendix_link.start()] + document[appendix_link.end():]
    document = document.replace("</nav>", link + "</nav>", 1)
    if document.count("</main>") != 1:
        raise RuntimeError("cannot place V12 provenance appendix at end of main")
    return document.replace("</main>", appendix + "</main>", 1)


def mark_and_move_markdown_appendix(document: str) -> str:
    cleaned = []
    for line in document.splitlines():
        if line.startswith("Table:") or line.startswith("!["):
            line = re.sub(r"weighted using household weights",
                          "household-weighted", line, flags=re.I)
            line = re.sub(r"dwt-weighted", "household-weighted", line,
                          flags=re.I)
            line = re.sub(r"(?<![A-Za-z0-9])dwt(?![A-Za-z0-9])",
                          "household weights", line, flags=re.I)
        cleaned.append(line)
    document = "\n".join(cleaned) + "\n"
    pattern = re.compile(
        r'(^# 7\. Appendix\. Technical record and provenance\n.*?)'
        r'(?=^# Questions for presentation preparation\n)',
        flags=re.S | re.M,
    )
    match = pattern.search(document)
    if not match:
        raise RuntimeError("editable V12 provenance appendix block not found")
    appendix = match.group(1).rstrip() + "\n"
    document = document[:match.start()] + document[match.end():]
    document = re.sub(r'^# Questions for presentation preparation\n\s*', "",
                      document, count=1, flags=re.M)
    return (document.rstrip() + "\n\n" + BEGIN_MARKER + "\n" + appendix
            + END_MARKER + "\n")


def v12_write_text(path, data, *args, **kwargs):
    target = redirects.get(path.resolve(), path)
    if isinstance(data, str):
        data = data.replace("JMP_working_paper_for_seminar_v6",
                            "JMP_working_paper_for_seminar_v9")
        data = data.replace(
            "REPORT-V6: presentation-only successor; frozen v5 tables, figures "
            "and scalar values.",
            "REPORT-V12: duplicate predecessor document removed from the appendix; "
            "analysis promoted to the body; implementation-only appendix; numbers unchanged.",
        )
        data = data.replace(
            "v6; numerical evidence preserved from v5; diagnostic boundary added",
            "v12; numerical evidence identical to v11; structural edit only",
        )
        if target == redirects[(ROOT / "reports/JMP_research_story_report_v6.html").resolve()]:
            collapsed = re.search(
                r"<details><summary>Show this section</summary>(.*?)</details>",
                data, flags=re.S,
            )
            if collapsed:
                for heading_id in re.findall(r'<h[12] id="([^"]+)"',
                                             collapsed.group(1)):
                    data = re.sub(
                        r'<a class="(?:sub|)" href="#' + re.escape(heading_id)
                        + r'">.*?</a>', "", data, count=1, flags=re.S,
                    )
            data = caption_language(data)
            data = mark_and_move_html_appendix(data)
        elif target == redirects[(HERE / "story_v6.generated.md").resolve()]:
            data = mark_and_move_markdown_appendix(data)
    kwargs.setdefault("newline", "\n")
    return original_write_text(target, data, *args, **kwargs)


sys.modules["v6_sections"] = v12_sections
sys.modules["v6_render_inputs"] = v12_render_inputs
Path.write_text = v12_write_text
try:
    runpy.run_path(str(HERE / "build_v6.py"), run_name="__main__")
finally:
    Path.write_text = original_write_text

for old, new in redirects.items():
    if not new.is_file():
        raise SystemExit("missing V12 build target: " + str(new))
    if old.exists() and old.stat().st_mtime_ns > new.stat().st_mtime_ns:
        raise SystemExit("V11/V6 write escaped redirect: " + str(old))

print("V12 HTML, editable Markdown and numerical registry written "
      "(paper TeX/bib redirected to scratch; not part of this task).")
