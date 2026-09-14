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
