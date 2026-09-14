"""Negative control for run_v5_gate.py.

A gate that passes is worth nothing unless it fails when it should. This injects
one violation at a time into a COPY of the artifacts, runs the gate against the
copy, and checks that the intended item flips to FAIL.
"""
import re
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

JMP = Path(r'C:\Users\hisham\Repo\Job_Market_paper')
PY = sys.executable

MUTATIONS = [
    # (item number expected to fail, file key, find, replace)
    (1, 'tex', r'estimated}, not fixed at one',
     r'fixed at one at the numeraire beta_c = 1 and so'),
    (2, 'tex', 'g^{E}_{ij}', 'g^{Acc}_{ij}'),
    (5, 'md', 'directly pay-neutral', 'shown to fail Independence of pay'),
    (7, 'tex', 'earning-opportunity heterogeneity has a larger contribution '
     'than the coarse geographic/temporal access channel',
     'coarse geographic/temporal access heterogeneity has a larger '
     'contribution than the earning-opportunity channel'),
    (9, 'tex', 'held fixed', 'left unadjusted'),
    (10, 'tex', 'The estimated model has',
     'The SCALE-1 CERTIFIED estimated model has'),
    (15, 'md', 'We claim no new allocation principle.',
     'This is the first structural labour-supply Shapley decomposition.'),
    (16, 'tex', 'is not a causal analysis', 'is a causal analysis'),
    (18, 'tex', 'reference is directly pay-neutral, and earning opportunities '
     'reach the measure through the attained evaluation.',
     'reference is directly pay-neutral, and earning opportunities reach '
     'the measure through the attained evaluation. Equivalently, '
     '$J_{i,S}=\\int e^{L_{i,S}(j)}(C_{i,S}(j)/\\lambda_c)^{\\beta_c}'
     '\\widehat g_{i,S}(j)\\,d\\nu(j)$ recovers the same amount.'),
]

FILES = {
    'tex': 'manuscript/JMP_working_paper_for_seminar_v5.tex',
    'md': 'reports/research_story_build/story_v5.generated.md',
    'html': 'reports/JMP_research_story_report_v5.html',
}


EXPECTED_ITEMS = 18

# LINEAGE-SWEEP-1 added item 17 (retired-lineage path check); REBUILD-1 left
# one residual hit (s12_welfare_record_report_v1.md, cited for the separate
# W1 pay-neutrality/W3 content, out of REBUILD-1's scope) that made a clean
# copy legitimately show item 17 as failing -- not a control defect. REBUILD-3
# repointed those citations and removed the W3 content that didn't survive
# verification (see build_v5.py's REBUILD-3 comment), closing the residual:
# a clean copy now has zero failures. Kept as an empty set, not deleted, so a
# future residual of the same kind has an established place to be recorded
# rather than silently loosening the "clean copy must have zero fails" check
# below. MEASURE-DEF-1 added item 18 (retired ex-ante J/H welfare
# construction, content-signature check); a clean copy has zero failures on
# it as well.
KNOWN_PRE_EXISTING_FAILURES: set[int] = set()


def run_gate(root: Path):
    """Run the gate and refuse to interpret a crash as a clean result.

    A gate that dies on an import or a missing input prints no item lines, and
    an earlier version of this control read that as "no failures" -- which made
    every mutation look uncaught and, worse, would have made a broken gate look
    like a passing one.
    """
    env = os.environ.copy()
    env['PYTHONIOENCODING'] = 'utf-8'
    r = subprocess.run([PY, str(root / 'reports/run_v5_gate.py')],
                       capture_output=True, text=True, env=env,
                       encoding='utf-8')
    fails, seen = set(), 0
    for line in r.stdout.splitlines():
        m = re.match(r'^(\d+)\s+.*\s(PASS|FAIL)\s*$', line)
        if m:
            seen += 1
            if m.group(2) == 'FAIL':
                fails.add(int(m.group(1)))
    if seen != EXPECTED_ITEMS:
        raise SystemExit(
            'the gate reported %d items, expected %d. It did not run.'
            '\n--- stdout ---\n%s\n--- stderr ---\n%s'
            % (seen, EXPECTED_ITEMS, r.stdout, r.stderr))
    return fails, r.stdout


def main():
    base = Path(tempfile.mkdtemp(prefix='v5gate_'))
    root = base / 'Job_Market_paper'
    shutil.copytree(JMP / 'manuscript', root / 'manuscript',
                    ignore=shutil.ignore_patterns('*.pdf~'))
    (root / 'reports').mkdir(parents=True, exist_ok=True)
    for name in ['run_v5_gate.py', 'retired_lineage_gate.py',
                 'JMP_research_story_report_v5.html',
                 'numbers_of_record_v5.json']:
        shutil.copy2(JMP / 'reports' / name, root / 'reports' / name)
    (root / 'reports/research_story_build').mkdir(parents=True, exist_ok=True)
    shutil.copy2(JMP / 'reports/research_story_build/story_v5.generated.md',
                 root / 'reports/research_story_build/story_v5.generated.md')
    # the gate reads the MNL evidence through JMP.parent
    (base / 'MNL').mkdir(exist_ok=True)
    sprint = JMP.parent / 'MNL/experiments/JMP_SEMINAR_SPRINT/runs'
    for rel in ['v5_evidence/v5_step2_welfare_evidence_v1.json']:
        d = base / 'MNL/experiments/JMP_SEMINAR_SPRINT/runs' / rel
        d.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(sprint / rel, d)
    # item 7/9/17 read the DECOMP-2 preliminary P/A/B decomposition directly
    # (MNL_decomp, preseminar_pab_v1) -- same lineage the gallery build uses.
    decomp2 = JMP.parent / 'MNL_decomp/outputs/welfare/preseminar_pab_v1'
    decomp2_dst = base / 'MNL_decomp/outputs/welfare/preseminar_pab_v1'
    decomp2_dst.mkdir(parents=True, exist_ok=True)
    for rel in (['coalition_values_singles.csv', 'coalition_values_couples.csv',
                 'shapley_PAB_singles.csv', 'shapley_PAB_couples.csv',
                 'log_variance_split_v1.csv', 'anchor_excluded_arm_v1.json']
                + [p.name for p in decomp2.glob('fig_preseminar_pab_*.png')]):
        shutil.copy2(decomp2 / rel, decomp2_dst / rel)

    clean, out = run_gate(root)
    print('clean copy fails:', sorted(clean) or 'none')
    unexpected_clean_fails = clean - KNOWN_PRE_EXISTING_FAILURES
    if clean & KNOWN_PRE_EXISTING_FAILURES:
        print('(item(s) %s are known pre-existing failures -- LINEAGE-SWEEP-1 '
              'debt, not a control defect -- and are excluded from the check '
              'below)' % sorted(clean & KNOWN_PRE_EXISTING_FAILURES))
    if unexpected_clean_fails:
        print(out)
        return 1

    originals = {k: (root / v).read_text(encoding='utf-8')
                 for k, v in FILES.items()}
    rc = 0
    for num, key, find, repl in MUTATIONS:
        path = root / FILES[key]
        txt = originals[key]
        if find not in txt:
            print('SKIP item %-2d  anchor not found: %r' % (num, find[:48]))
            rc = 1
            continue
        path.write_text(txt.replace(find, repl), encoding='utf-8')
        fails, _ = run_gate(root)
        ok = num in fails
        print('%-4s item %-2d  mutation caught by %s'
              % ('OK' if ok else 'MISS', num, sorted(fails) or 'nothing'))
        if not ok:
            rc = 1
        path.write_text(txt, encoding='utf-8')
    shutil.rmtree(base, ignore_errors=True)
    print('\nnegative control:', 'PASS' if rc == 0 else 'FAIL')
    return rc


if __name__ == '__main__':
    raise SystemExit(main())
