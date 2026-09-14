"""Build report/paper v7 without writing any v6 path.

The stable renderer remains build_v6.py.  This versioned entry point injects
the v7 sections and corrected inputs, redirects every generated target to a
v7 filename, and updates source-only provenance during the write.
"""
from pathlib import Path
import runpy
import sys

import v7_render_inputs
import v7_sections


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PAPER = ROOT / 'manuscript'

redirects = {
    (PAPER / 'JMP_working_paper_for_seminar_v6.bib').resolve():
        (PAPER / 'JMP_working_paper_for_seminar_v7.bib').resolve(),
    (PAPER / 'JMP_working_paper_for_seminar_v6.tex').resolve():
        (PAPER / 'JMP_working_paper_for_seminar_v7.tex').resolve(),
    (HERE / 'story_v6.generated.md').resolve():
        (HERE / 'story_v7.generated.md').resolve(),
    (ROOT / 'reports/JMP_research_story_report_v6.html').resolve():
        (ROOT / 'reports/JMP_research_story_report_v7.html').resolve(),
    (ROOT / 'reports/numbers_of_record_v6.json').resolve():
        (ROOT / 'reports/numbers_of_record_v7.json').resolve(),
}

original_write_text = Path.write_text


def v7_write_text(path, data, *args, **kwargs):
    target = redirects.get(path.resolve(), path)
    if isinstance(data, str):
        data = data.replace('JMP_working_paper_for_seminar_v6',
                            'JMP_working_paper_for_seminar_v7')
        data = data.replace(
            'Predictive diagnostics: POSFIT v3; repository MNL_posfit; branch '
            'diagnostics/posfit-v3; commit 96693269; artifact run_provenance.json; '
            'SHA-256 BDC3722C325FF8A27BE719AA52A741DF7BEEF9515B4A63554C65E8769EB7F40B.',
            'Predictive diagnostics: POSFIT v3b; repository MNL_posfit; branch '
            'diagnostics/posfit-v3; commit cd7247cf; artifact '
            'outputs/positive_fit_diagnostics_v3b/run_provenance.json; SHA-256 '
            + v7_render_inputs.POSFIT_RUN_SHA256 + '.')
        data = data.replace(
            'REPORT-V6: presentation-only successor; frozen v5 tables, figures '
            'and scalar values.',
            'REPORT-V7: corrected POSFIT-v3b and Band-Fix-2 fit evidence; '
            'DECOMP-2 evidence inherited unchanged after no-dependency verification.')
        data = data.replace(
            'v6; numerical evidence preserved from v5; diagnostic boundary added',
            'v7; corrected POSFIT-v3b and Band-Fix-2 fit; DECOMP-2 restored unchanged')
    return original_write_text(target, data, *args, **kwargs)


sys.modules['v6_sections'] = v7_sections
sys.modules['v6_render_inputs'] = v7_render_inputs
Path.write_text = v7_write_text
try:
    runpy.run_path(str(HERE / 'build_v6.py'), run_name='__main__')
finally:
    Path.write_text = original_write_text

for old in redirects:
    if old.exists() and old.stat().st_mtime_ns > redirects[old].stat().st_mtime_ns:
        raise SystemExit('v6 write escaped redirect: ' + str(old))

print('v7 report, editable Markdown, paper TeX and numerical registry written.')
runpy.run_path(str(HERE / 'sync_paper_fit_v7.py'), run_name='__main__')
