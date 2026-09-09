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

JMP = Path(__file__).resolve().parent.parent
PDF = JMP / 'manuscript/JMP_working_paper_for_seminar_v5.pdf'
S12 = JMP.parent / 'MNL/experiments/JMP_SEMINAR_SPRINT/runs/s12_welfare_record'
S11 = JMP.parent / 'MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record'


def rows(path: Path):
    with path.open(encoding='utf-8') as f:
        return list(csv.DictReader(f))


def main() -> int:
    text = ' '.join(p.get_text() for p in pymupdf.open(PDF))
    text = ' '.join(text.split())

    six = rows(S12 / 's12_six_index_attributions_v1.csv')

    def cell(sample, ref, basis, index):
        for r in six:
            if (r['sample'] == sample and r['reference'] == ref
                    and r['basis'] == basis and r['index'] == index):
                return r
        raise SystemExit('missing row %r' % ((sample, ref, basis, index),))

    checks = []
    for tag, sample, ref in [('singles', 'singles', 'singles_female'),
                             ('couples', 'couples', 'household-own')]:
        r = cell(sample, ref, 'raw', 'gini')
        base = float(r['I00'])
        for comp, col in [('P', 'C_P'), ('A', 'C_A'), ('B', 'C_B'),
                          ('AB', 'C_AB'), ('D', 'C_D')]:
            checks.append(('%s share %s' % (tag, comp),
                           '%.2f' % (100.0 * float(r[col]) / base)))
        checks.append(('%s baseline Gini' % tag, '%.6f' % base))
        for st in ['I10', 'I01']:
            checks.append(('%s %s' % (tag, st), '%.6f' % float(r[st])))

    # the two-group one-factor effects, recomputed here
    for tag, sample, ref in [('singles', 'singles', 'singles_female'),
                             ('couples', 'couples', 'household-own')]:
        r = cell(sample, ref, 'raw', 'gini')
        i00, i10, i01 = float(r['I00']), float(r['I10']), float(r['I01'])
        checks.append(('%s one-factor E' % tag,
                       '%.1f' % (100.0 * (i00 - i01) / i00)))
        checks.append(('%s one-factor P magnitude' % tag,
                       '%.1f' % abs(100.0 * (i00 - i10) / i00)))

    # the estimated consumption weights and their standard errors
    for tag, f in [('singles', 's11_singles_parameter_table_v1.csv'),
                   ('couples', 's11_couples_parameter_table_v1.csv')]:
        for r in rows(S11 / f):
            if r['param'] == 'beta_c':
                checks.append(('%s beta_c' % tag, '%.4f' % float(r['estimate'])))
                checks.append(('%s beta_c s.e.' % tag,
                               '%.4f' % float(r['se_robust_CR1'])))

    # the couples budget-channel split
    for r in rows(S12 / 's12_couples_nested_D_attributions_v1.csv'):
        if r['basis'] == 'raw' and r['index'] == 'gini':
            b = float(r['I00'])
            checks.append(('couples resources share',
                           '%.2f' % (100.0 * float(r['C_nonlabour']) / b)))
            checks.append(('couples composition share',
                           '%.2f' % (100.0 * float(r['C_composition']) / b)))

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
    return 0


if __name__ == '__main__':
    sys.exit(main())
