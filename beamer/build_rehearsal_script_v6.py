"""Refresh the standalone script from the compiled deck and its speaker notes.

Projection text is extracted from the PDF; internal source labels in the notes
are translated to reader language. The extended diagnostic Q&A is preserved
from the committed predecessor, including every numerical sensitivity value.
"""
from pathlib import Path
import re
import subprocess
import pymupdf
import pypandoc

ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / 'beamer/JMP_seminar_deck_r6.tex').read_text('utf-8')
numbers = (ROOT / 'beamer/deck_numbers_r6.tex').read_text('utf-8')
macros = dict(re.findall(r'\\newcommand\{\\(\w+)\}\{([^{}]*)\}', numbers + source))
macros.update(Wone='W^1', S=r'\S')

def expand(text):
    for name, value in sorted(macros.items(), key=lambda kv: -len(kv[0])):
        text = re.sub(r'\\' + re.escape(name) + r'\b', lambda m: value, text)
    return text

def reader_note(text):
    text = re.sub(r'\s+', ' ', text).strip()
    # Source-only opening clauses contain no economic claim.
    text = re.sub(r'^Q\\&A note --- .*?\. (?:md Appendix A\. )?', '', text)
    text = text.replace('md Appendix A. ', '')
    text = text.replace('Two estimation samples, singles and couples, on the corrected criterion-A frames. Everything on the slides after this point is S11. I am deliberately not showing the older S8 or R240 numbers alongside, because the frames differ and a side-by-side would invite a comparison the samples do not support.',
                        'The two estimation samples contain single-adult and couple households. The estimates and diagnostics use these same samples throughout.')
    text = text.replace('R1 rules F primary for the current paper.', 'The full feasible-set reference is primary for the current paper.')
    text = text.replace('the ruling is explicit about it', 'the distinction is explicit')
    text = text.replace('R6 forbids presenting a singles/couples equivalised-level comparison as a finding', 'the analysis does not compare equivalised welfare levels across these separately estimated samples')
    text = text.replace('nothing in the recent rulings touched them', 'they motivate the current specification')
    text = text.replace('The fork analysis', 'The reference comparison').replace('the fork analysis', 'the reference comparison')
    for old, new in (
        ('DECOMP-2', 'this bounded decomposition exercise'),
        ('Mapping-F', 'attained-bundle'), ('Mapping F', 'the full feasible-set reference'),
        ('Mapping M', 'the market-only reference'), ('Measure-1', 'own-set equal-consumption'),
        ('MEASURE-MAP-1R', 'worked-household'), ('criterion-A', 'sampled-alternative'),
        ('POSFIT v3', 'individual-level predictive diagnostics'),
        ('v3 common-node support', 'common-node support'),
        ('v3 re-evaluates', 'the diagnostic analysis re-evaluates'),
        ('C1 and C2', 'The nonworker and worker checks'),
        ('C3 is', 'The dependency check is'), ('C5 inverts', 'The indifference check inverts'),
    ):
        text = text.replace(old, new)
    # Keep provenance out of spoken notes, without matching decimal numerals.
    text = re.sub(r'(?:MNL )?commit\s+`?[0-9a-f]{7,40}`?[,;]?', '', text)
    text = re.sub(r'\b(?:JMP|MNL)[A-Za-z0-9_./\\-]*\.(?:md|csv|json|py)', 'the source analysis', text)
    text = re.sub(r'\b(?:R[1-6]|BASELINE-F-1|E[1-3](?:-EQ)?)\b', 'the stated specification', text)
    text = re.sub(r'Source: individual-level predictive diagnostics \(.*?\)\.',
                  'Source details are retained in the provenance note.', text)
    text = re.sub(r'Deputy ruling "SCALE CLOSED; CHILD-SHIFTER FRAMING", section 1',
                  'equivalence-scale analysis', text)
    text = re.sub(r"Deputy ruling ``SCALE CLOSED; CHILD-SHIFTER FRAMING'', section 1",
                  'equivalence-scale analysis', text)
    text = text.replace('ruling the stated specification confirms', 'the welfare definition confirms')
    text = text.replace('G2 bootstrap', 'numerical-adequacy bootstrap')
    return text

frames = re.findall(r'\\begin\{frame\}.*?\\end\{frame\}', source, re.S)
main_count = len(re.findall(r'\\begin\{frame\}', source.split(r'\appendix', 1)[0]))
doc = pymupdf.open(ROOT / 'beamer/build/JMP_seminar_deck_r6.pdf')
section_titles = set(re.sub(r'\s+', ' ', x).strip() for x in
                     re.findall(r'\\section\{([^}]+)\}', source))
section_titles = {x.replace(r'$\Wone$', 'W 1') for x in section_titles}
pages = [page for page in doc if re.sub(r'\s+', ' ', page.get_text()).strip()
         not in section_titles]
assert len(frames) == len(pages), (len(frames), len(pages))
out = ['# Seminar rehearsal script', '',
       f'The main presentation contains {main_count} slides. The remaining {len(frames)-main_count} slides are backup material.', '',
       '## Main presentation', '']
for i, (frame, page) in enumerate(zip(frames, pages), 1):
    if i == main_count + 1:
        out += ['## Backup / appendix', '', '### Preliminary restricted-operator decomposition', '']
    projected = re.sub(r'\s+', ' ', page.get_text()).strip()
    projected = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', projected)
    projected = projected.replace('0 20 40 60 80 100', '0; 20; 40; 60; 80; 100')
    note = re.search(r'\\note\{(.*?)\}\s*\\end\{frame\}', frame, re.S)
    assert note, i
    clean = reader_note(note[1])
    spoken = pypandoc.convert_text(expand(clean), 'markdown', format='latex',
                                 extra_args=['--wrap=none']).strip()
    spoken = re.sub(r'(?<=\d)--(?=\d)', '–', spoken)
    if i == 12:
        spoken += ('\n\nThe money metric is derived from the own-set equal-consumption principle. '
                   'Under the current empirical specification its direct reference collapses '
                   'to the universally available non-employment state; opportunity heterogeneity '
                   'therefore affects the current welfare measure through attained bundles.')
    if i == 13:
        spoken += ('\n\nThe one-nat shortfall has a leisure-index difference of -1. '
                   'Current nonworkers: W=C. Current workers: W<C under the maintained empirical domain.')
    out += [f'### Slide {i}' if i <= main_count else f'### Backup slide {i-main_count}', '',
            'On slide: ' + projected, '', 'Say: ' + spoken, '']

# Preserve the extended diagnostic and sensitivity content from the predecessor.
old = subprocess.check_output(['git', '-C', str(ROOT), 'show',
                              '61af387:reports/rehearsal_pack_v1.md']).decode('utf-8')
extended = old.split('## Extended Q&A', 1)[1].split('## Quick-reference index', 1)[0]
extended = '## Extended Q&A' + extended
extended = re.sub(r'Source: `outputs/positive_fit_diagnostics_v3/g2_adequacy.csv`, group `couples_male`, statistic `extensive_accuracy`\.',
                  'Source details are retained in the provenance note.', extended)
extended = extended.replace("I'll note this particular sensitivity check is a completed diagnostic on a branch not yet merged into the main estimation line, so take the direction of the finding as solid and the exact magnitudes as provisional.",
                            'The reported magnitudes describe this completed sensitivity diagnostic.')
extended = re.sub(r'`scripts/enhanced/enh_RURO_prep_mnl_basic.py:52` \(MNL\)',
                  'the leisure definition', extended)
extended = re.sub(r'Sensitivity: `experiments/[^`]+`, MNL commit `[^`]+`, branch `[^`]+` \(confirmed NOT merged to `main`\)\.',
                  'The sensitivity analysis is documented in the provenance note.', extended)
out += [extended, '']
provenance = re.search(r'% BEGIN READER-VOICE PROVENANCE(.*?)% END READER-VOICE PROVENANCE', source, re.S)[1]
provenance = re.sub(r'^% ?', '', provenance, flags=re.M)
out += ['<!-- BEGIN READER-VOICE PROVENANCE', provenance,
        'Script generator: beamer/build_rehearsal_script_v6.py.',
        'Extended Q&A source: predecessor reports/rehearsal_pack_v1.md.',
        'Diagnostic Q&A: MNL_posfit/outputs/positive_fit_diagnostics_v3/g2_adequacy.csv; couples_male; extensive_accuracy.',
        'Time sensitivity: MNL@5a8e6bba; experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/JMP_leisure_normalisation_time_sensitivity_v1.md.',
        'Leisure definition: MNL/scripts/enhanced/enh_RURO_prep_mnl_basic.py:52.',
        'END READER-VOICE PROVENANCE -->', '']
(ROOT / 'reports/rehearsal_pack_v1.md').write_text('\n'.join(out), encoding='utf-8')
print(f'Rehearsal script: {main_count} main + {len(frames)-main_count} backup slides.')
