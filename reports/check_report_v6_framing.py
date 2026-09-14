"""REPORT-V6 acceptance: demotion, verbatim framing, preservation and provenance."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'reports/research_story_build'))
import v5_sections as old
import v6_sections as new

checks = []
def check(name, ok, detail):
    checks.append({'check': name, 'status': 'PASS' if ok else 'FAIL', 'detail': detail})

def read(rel):
    return (ROOT / rel).read_text('utf-8')

def flat(text):
    return re.sub(r'\s+', ' ', text).strip()

def no_headline(text):
    return not re.search(r'1\.8\s*(?:--?|–)\s*9\.9\s*%|earning-opportunity heterogeneity has a larger|earning opportunities exceed', text, re.I)

md = read('reports/research_story_build/story_v6.generated.md')
html5 = read('reports/JMP_research_story_report_v5.html')
html6 = read('reports/JMP_research_story_report_v6.html')
tex = read('manuscript/JMP_working_paper_for_seminar_v6.tex')
deck = read('beamer/JMP_seminar_deck_r6.tex')
script = re.sub(r'<!--.*?-->', '', read('reports/rehearsal_pack_v1.md'), flags=re.S)
main_md = md.split('# 8. Appendix A.', 1)[0]
main_deck = deck.split(r'\appendix', 1)[0].split(r'\begin{document}', 1)[1]
main_script = script.split('## Backup / appendix', 1)[0]
paper_text = ' '.join(p.get_text() for p in pymupdf.open(ROOT / 'manuscript/JMP_working_paper_for_seminar_v6.pdf'))
deck_text = ' '.join(p.get_text() for p in pymupdf.open(ROOT / 'beamer/build/JMP_seminar_deck_r6.pdf'))
for name, text in [('report', md), ('paper PDF', paper_text), ('deck PDF', deck_text), ('rehearsal', script)]:
    check(name + ': verbatim mission wording', flat(new.MISSION_WORDING) in flat(text), 'All three mission sentences retained verbatim.')
    check(name + ': explicit appendix title', new.APPENDIX_TITLE in flat(text), new.APPENDIX_TITLE)
for name, text in [('report', main_md), ('paper', tex.split(r'\appendix', 1)[0]), ('deck', main_deck), ('rehearsal', main_script)]:
    check(name + ': no headline decomposition result', no_headline(text), 'Range and channel-ranking result are confined to appendix/backup.')
check('deck: every decomposition frame in backup',
      r'\DTwoMinPct' not in main_deck and r'\DTwoVarMinPct' not in main_deck,
      'Three former main frames moved; scope and diagnostic backup frames added.')
check('main text: reconstruction status', new.EA_STATUS in main_md,
      'Historical ex-ante percentages explicitly excluded; current welfare evidence unchanged.')

for name, pattern in [('tables', r'<table\b.*?</table>'), ('embedded figures', r'<img\b[^>]*>')]:
    before = Counter(re.findall(pattern, html5, re.S))
    after = Counter(re.findall(pattern, html6, re.S))
    check('report: all ' + name + ' preserved exactly', before == after,
          f'{sum(before.values())} predecessor {name}; {sum(after.values())} current {name}.')
reg5 = json.loads(read('reports/numbers_of_record_v5.json'))
reg6 = json.loads(read('reports/numbers_of_record_v6.json'))
check('registry: all numerical values and provenance retained',
      all(reg6['entries'].get(k) == v for k, v in reg5['entries'].items()),
      f"All {len(reg5['entries'])} predecessor entries are unchanged; two diagnostic entries added.")
tokens = lambda s: set(re.findall(r'\{\{n:(d2_[^|}]+)', s))
before = tokens(old.ABSTRACT + ''.join(s['body'] for s in old.SECTIONS) + ''.join(a for q, a in old.QA))
after = tokens(new.ABSTRACT + ''.join(s['body'] for s in new.SECTIONS) + ''.join(a for q, a in new.QA))
check('decomposition: every distinct numerical token retained', before <= after,
      f'{len(before)} predecessor decomposition quantities; missing: {sorted(before-after)}.')
for key in ('data', 'model', 'appcoef'):
    old_body = next(s['body'] for s in old.SECTIONS if s['key'] == key)
    new_body = next(s['body'] for s in new.SECTIONS if s['key'] == key)
    check('protected prose: ' + key, old_body == new_body, 'Inherited without changes.')
check('protected prose: behavioural estimates, fit and observed-bundle results',
      new.RESULTS == old.RESULTS.split('## The preliminary decomposition', 1)[0],
      'All results before the former decomposition subsection retained verbatim.')
protected = ['reports/JMP_research_story_report_v5.html',
             'reports/research_story_build/build_v5.py',
             'reports/research_story_build/v5_sections.py',
             'reports/research_story_build/story_v5.generated.md',
             'reports/numbers_of_record_v5.json',
             'manuscript/JMP_working_paper_for_seminar_v5.tex',
             'manuscript/JMP_working_paper_for_seminar_v5.pdf',
             'reports/JMP_results_gallery_current.html']
protected += [str(p.relative_to(ROOT)).replace('\\', '/') for folder in ('manuscript/figures/v5', 'beamer/figures/r6')
              for p in (ROOT / folder).glob('*') if p.is_file()]
changed = []
for rel in protected:
    before_hash = subprocess.check_output(['git', '-C', str(ROOT), 'rev-parse', 'HEAD:' + rel], stderr=subprocess.DEVNULL).decode().strip()
    after_hash = subprocess.check_output(['git', '-C', str(ROOT), 'hash-object', rel]).decode().strip()
    if before_hash != after_hash:
        changed.append(rel)
check('v5 and accepted assets unchanged', not changed, f'{len(protected)} files checked; changed: {changed}.')
diag = read('docs/Decomposition_diag_1.txt')
for key, pattern in [('diag1_location_log', r'at most about (0\.10) log points'),
                     ('diag1_sigma', r'sigma ≈ (0\.37)')]:
    value = float(re.search(pattern, diag)[1])
    check(key + ': parsed diagnostic source', reg6['entries'][key]['value'] == value,
          'docs/Decomposition_diag_1.txt::5. Verdict; no new numerical exercise.')
check('placement negative controls',
      not no_headline(main_md + '\n1.8–9.9%') and
      not no_headline(main_deck + '\nearning opportunities exceed coarse access'),
      'Injecting the range or channel-ranking headline fails the placement rule.')

result = {'status': 'PASS' if all(c['status'] == 'PASS' for c in checks) else 'FAIL',
          'checks': checks, 'v6_sha256': hashlib.sha256((ROOT / 'reports/JMP_research_story_report_v6.html').read_bytes()).hexdigest()}
(ROOT / 'reports/report_v6_framing_gate.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
for c in checks:
    print(c['status'] + ' ' + c['check'] + ': ' + c['detail'])
raise SystemExit(0 if result['status'] == 'PASS' else 1)
