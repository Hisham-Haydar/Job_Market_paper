#!/usr/bin/env python
"""Independent check: do the headline numbers in the COMPILED PDF match source?

The build resolves tokens against its own registry, and the gate checks the
registry. Neither proves that what a reader sees in the PDF equals what the
run artifacts contain. This reads the rendered PDF text and compares a set of
headline magnitudes recomputed straight from the S11/S12 CSVs.

Exit code 0 if every expected string is present in the rendered text.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

import pymupdf

sys.path.insert(0, str(Path(__file__).resolve().parent))
import retired_lineage_gate as rlg  # noqa: E402

JMP = Path(__file__).resolve().parent.parent
PDF = JMP / 'manuscript/JMP_working_paper_for_seminar_v5.pdf'
S11 = JMP.parent / 'MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record'
DECOMP2 = JMP.parent / 'MNL_decomp/outputs/welfare/preseminar_pab_v1'


def rows(path: Path):
    with path.open(encoding='utf-8') as f:
        return list(csv.DictReader(f))


def main() -> int:
    # LINEAGE-SWEEP-1: this script's OWN ground truth is two retired
    # welfare-decomposition artifacts (see reports/retired_lineage_gate.py
    # for the definition). A path-based scan of its own source, not of
    # rendered prose, is the only honest way to flag that: rewording the
    # PDF text below would not fix what this checker actually reads.
    self_violations = rlg.scan_files([Path(__file__)])
    lineage_rc = 0
    if self_violations:
        print('RETIRED-LINEAGE SELF-CHECK: FAIL -- this verifier reads a '
              'retired artifact by path as its own ground truth:')
        print(rlg.format_violations(self_violations, JMP))
        print('This verifier needs repointing at the DECOMP-2 / '
              'preseminar_pab_v1 lineage before its PASS/FAIL is '
              'trustworthy; see the LINEAGE-SWEEP-1 report.')
        lineage_rc = 1
    else:
        print('RETIRED-LINEAGE SELF-CHECK: PASS')

    text = ' '.join(p.get_text() for p in pymupdf.open(PDF))
    text = ' '.join(text.split())

    # DECOMP-2: preliminary three-factor P/A/B decomposition (superseding the
    # retired S12 six-index/nested-D lineage this script used to read).
    d2_scale = {'uneq': 'unequivalised', 'eq': 'equivalised'}
    d2_coal = {s: rows(DECOMP2 / ('coalition_values_%s.csv' % s))
               for s in ('singles', 'couples')}
    d2_shap = {s: rows(DECOMP2 / ('shapley_PAB_%s.csv' % s))
               for s in ('singles', 'couples')}

    def coal_row(sample, scale_key, coalition):
        scale = d2_scale[scale_key]
        for r in d2_coal[sample]:
            if r['scale'] == scale and r['coalition'] == coalition:
                return r
        raise SystemExit('missing coalition row %r' % ((sample, scale, coalition),))

    def shap_row(sample, scale_key, factor):
        scale = d2_scale[scale_key]
        for r in d2_shap[sample]:
            if r['scale'] == scale and r['factor'] == factor:
                return r
        raise SystemExit('missing shapley row %r' % ((sample, scale, factor),))

    checks = []
    delta_pcts = []
    for tag in ('singles', 'couples'):
        for sk in ('uneq', 'eq'):
            base = float(coal_row(tag, sk, 'EMPTY')['I_S_gini'])
            pab = float(coal_row(tag, sk, 'PAB')['I_S_gini'])
            delta = base - pab
            pct = 100.0 * delta / base
            delta_pcts.append(pct)
            checks.append(('%s %s baseline Gini' % (tag, sk), '%.4f' % base))
            for factor in ('P', 'A', 'B'):
                g = float(shap_row(tag, sk, factor)['gini_point_contribution'])
                checks.append(('%s %s share %s (Gini points)' % (tag, sk, factor),
                               '%.4f' % g))
    # the abstract/headline state the min and max of that 1.8-9.9 range
    checks.append(('deltaI pct min', '%.1f' % min(delta_pcts)))
    checks.append(('deltaI pct max', '%.1f' % max(delta_pcts)))
    # B dominates A in every cell -- the qualitative ordering the text states
    for tag in ('singles', 'couples'):
        for sk in ('uneq', 'eq'):
            a = float(shap_row(tag, sk, 'A')['share_of_delta_I']) * 100
            b = float(shap_row(tag, sk, 'B')['share_of_delta_I']) * 100
            if not b > a:
                raise SystemExit('B does not exceed A for %s %s: %.2f vs %.2f'
                                 % (tag, sk, b, a))

    # the estimated consumption weights and their standard errors
    for tag, f in [('singles', 's11_singles_parameter_table_v1.csv'),
                   ('couples', 's11_couples_parameter_table_v1.csv')]:
        for r in rows(S11 / f):
            if r['param'] == 'beta_c':
                checks.append(('%s beta_c' % tag, '%.4f' % float(r['estimate'])))
                checks.append(('%s beta_c s.e.' % tag,
                               '%.4f' % float(r['se_robust_CR1'])))

    checks += [('singles sample', '1,540'), ('couples sample', '2,223')]

    bad = [(n, v) for n, v in checks if v not in text]
    print('%s: %d headline magnitudes checked against the run artifacts'
          % (PDF.name, len(checks)))
    if bad:
        for n, v in bad:
            print('  MISSING  %-32s %s' % (n, v))
        print('NUMBERS: FAIL (%d of %d not found in the rendered text)'
              % (len(bad), len(checks)))
        return 1
    print('NUMBERS: PASS, every recomputed magnitude appears in the PDF')
    return lineage_rc


if __name__ == '__main__':
    sys.exit(main())
