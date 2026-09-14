"""Run the complete current release gate set and record actual return codes.

The v1/v2 historical consistency runner remains tied to its own retired model;
run_v5_gate.py is the maintained 18-item current-model runner, repointed to v6.
"""
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
GATES = [
    'reports/run_v5_gate.py',
    'reports/run_v5_gate_negative_control.py',
    'reports/check_v5_numbers_against_source.py',
    'reports/check_v5_pdf_layout.py',
    'reports/check_v6_render.py',
    'beamer/verify_deck_r6.py',
    'reports/results_gallery_build/verify.py',
    'reports/check_reports_dir_lineage.py',
    'reports/run_final_claim_wording_gate.py',
    'reports/check_report_v6_framing.py',
    'reports/run_final_claim_evidence_gate.py',
]
env = os.environ.copy()
env['PYTHONIOENCODING'] = 'utf-8'
results = []
for script in GATES:
    print('Running ' + script, flush=True)
    run = subprocess.run([sys.executable, str(ROOT / script)], cwd=ROOT,
                         env=env, capture_output=True, text=True, encoding='utf-8')
    status = 'PASS' if run.returncode == 0 else 'FAIL'
    print(status + ': ' + script, flush=True)
    if run.returncode:
        print(run.stdout[-4500:] + run.stderr[-2000:], flush=True)
    results.append({'gate': script, 'status': status, 'returncode': run.returncode,
                    'stdout': run.stdout, 'stderr': run.stderr})
report = ROOT / 'reports/JMP_research_story_report_v6.html'
payload = {'status': 'PASS' if all(r['returncode'] == 0 for r in results) else 'FAIL',
           'completed_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
           'v6_path': str(report.relative_to(ROOT)).replace('\\', '/'),
           'v6_sha256': hashlib.sha256(report.read_bytes()).hexdigest(),
           'gates': results}
(ROOT / 'reports/report_v6_gate_results.json').write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')
lines = ['# Report v6 release gates', '', '**' + payload['status'] + '**', '',
         'Report: `' + payload['v6_path'] + '`', '',
         'SHA-256: `' + payload['v6_sha256'] + '`', '',
         '| Gate | Result |', '|---|---|']
lines += ['| `' + r['gate'] + '` | ' + r['status'] + ' |' for r in results]
lines += ['', 'The number-to-source gate reads all six current surfaces, including the untouched gallery and canonical notebook. '
          'The historical v1/v2 consistency runner is superseded for the current model by the maintained 18-item runner, '
          'as documented in canonical_notation_v5.md; its incompatible beta_c=1 and historical hours-density clauses are not reintroduced.', '']
(ROOT / 'reports/report_v6_gate_results.md').write_text('\n'.join(lines), encoding='utf-8')
print('REPORT-V6: ' + payload['status'], flush=True)
raise SystemExit(0 if payload['status'] == 'PASS' else 1)
