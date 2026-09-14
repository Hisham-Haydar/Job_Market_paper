"""Build the v5 paper and the v5 research report from one source of prose,
numbers, tables and figures.

v5 is a source-reconciled rewrite, not a patch layer over v4.  Every empirical
token resolves against an accepted artifact: the S11 specifications of record,
the verified Mapping-F baseline, POSFIT v3, the sensitivity packages, or
DECOMP-2. A token with no source
fails the build; it is never filled with a predecessor value.

Run with the project's scientific Python environment:

    <venv>/python build_v5.py
"""
from __future__ import annotations
import base64
import csv
import datetime as dt
import html
import importlib.metadata
import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402
import pypandoc  # noqa: E402

from v5_sections import TITLE, ABSTRACT, PRELIM_NOTE, SECTIONS, QA  # noqa: E402
from make_fitext_band_v1 import build as build_fitext_band  # noqa: E402

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
MNL = ROOT.parent / 'MNL'
SPRINT = MNL / 'experiments/JMP_SEMINAR_SPRINT'
sys.path.insert(0, str(SPRINT))
import final_diagnostics_surface_v1 as final_surface  # noqa: E402

S11 = SPRINT / 'runs/s11_welfare_specs_of_record'
V5 = SPRINT / 'runs/v5_evidence'
MFIG = SPRINT / 'figures'
PAPER = ROOT / 'manuscript'
FIG = PAPER / 'figures/v5'
TABLE = PAPER / 'tables/v5'
FIG.mkdir(parents=True, exist_ok=True)
TABLE.mkdir(parents=True, exist_ok=True)

REG: dict = {}
USED: set = set()
today = dt.datetime.now().strftime('%d %B %Y')


def register(key, value, source, status='estimated', units='dimensionless'):
    REG[key] = {'value': value, 'source': source, 'status': status,
                'units': units}
    return value


def val(key, fmt=None):
    USED.add(key)
    if key not in REG:
        raise SystemExit('unregistered number: %r' % key)
    v = REG[key]['value']
    if key.endswith('_year'):
        return str(v)          # a year is not a quantity: no thousands group
    if fmt:
        return format(float(v), fmt)
    if isinstance(v, float):
        return format(v, '.6g')
    if isinstance(v, int):
        return format(v, ',d')
    return str(v)


# =========================================================================== #
# 1.  DEFINITIONS -- fixed by the model, not estimated
# =========================================================================== #
_DEF = 'model definition, bound to the executed specification'
for _k, _v, _u in [
        ('collection_year', 2016, 'EU-SILC collection year'),
        ('income_year', 2015, 'income reference year'),
        ('policy_year', 2015, 'EUROMOD policy system'),
        ('time_endowment', 80, 'hours/week'),
        ('leisure_scale', 10, 'hours/week'),
        ('hours_floor', 5, 'hours/week'),
        ('hours_cap', 70, 'hours/week'),
        ('wage_lo', 2, 'EUR/hour'),
        ('wage_hi', 590, 'EUR/hour'),
        ('experience_scale', 20, 'years'),
        ('age_scale', 10, 'years'),
        ('child_cutoff', 20, 'years of age'),
        ('gsur_scale', 10, 'multiplier on the unemployment fraction'),
        ('n_draws', 100, 'sampled alternatives per household'),
        ('n_nodes', 2048, 'common integration nodes per household'),
        ('n_alt_rows', 101, 'rows per household in the criterion'),
        ('n_occ', 4, 'occupation groups'),
        ('hours_reference_width', 26.5, 'hours/week'),
        ('cr1_draws', 100, 'parameter draws'),
        ('n_scrambles', 8, 'RQMC scrambles')]:
    register(_k, _v, _DEF, 'definition', _u)

# lambda_c: ONE constant of record per population, taken from the estimation
# frame the specification was estimated on.  See the reconciliation below.
_EVID = json.loads((V5 / 'v5_step2_welfare_evidence_v1.json').read_text('utf-8'))
_LAM = _EVID['lambda_c_reconciliation']
for _t in ['singles', 'couples']:
    register('lambda_c_' + _t,
             _LAM['constants_in_circulation']['estimation_frame_c_scale'][_t],
             'v5_step2_welfare_evidence_v1.json::lambda_c_reconciliation',
             'definition', 'EUR/month')
    register('lambda_c_welfare_panel_' + _t,
             _LAM['constants_in_circulation']['welfare_panel_c_scale'][_t],
             'v5_step2_welfare_evidence_v1.json::lambda_c_reconciliation',
             'definition', 'EUR/month')
register('lambda_c_maxdev',
         max(c['max_relative_deviation_from_power_mean']
             for c in _LAM['numerical_check']),
         'v5_step2_welfare_evidence_v1.json::lambda_c_reconciliation',
         'verified identity', 'relative difference')

# =========================================================================== #
# 2.  THE SPECIFICATIONS OF RECORD (S11)
# =========================================================================== #
_S11REC = json.loads((S11 / 's11_welfare_specs_of_record_v1.json').read_text('utf-8'))
_S11SRC = ('s11_welfare_specs_of_record_v1.json; specifications of record, '
           'tau = 1, theta_c = 0, beta_c estimated')
PAR = {'singles': pd.read_csv(S11 / 's11_singles_parameter_table_v1.csv'),
       'couples': pd.read_csv(S11 / 's11_couples_parameter_table_v1.csv'),
       'ruma': pd.read_csv(S11 / 's11_rum_a_parameter_table_v1.csv'),
       'rumb': pd.read_csv(S11 / 's11_rum_b_parameter_table_v1.csv')}
MOM = pd.read_csv(S11 / 's11_criterion_b_population_moments_v1.csv')


def par(tag, name, col='estimate'):
    m = PAR[tag][PAR[tag]['param'] == name]
    if len(m) != 1:
        raise SystemExit('parameter not unique: %s %s' % (tag, name))
    return m.iloc[0][col]


for _t, _model, _n, _neg, _gain, _free, _int in [
        ('singles', 'SINGLES', 1540, 6253.463074380, 23.752611, 41, 40),
        ('couples', 'COUPLES', 2223, 10283.034369351, 15.659005, 47, 47)]:
    _mae = _S11REC['results'][_model]['criterion_b_population_fit'][
        'mean_absolute_error']
    register('n_' + _t, _n, _S11SRC, 'sample', 'households')
    register('negll_' + _t, _neg, _S11SRC, 'estimated', 'log-likelihood units')
    register('gain_' + _t, _gain, _S11SRC, 'estimated', 'log-points')
    register('kfree_' + _t, _free, _S11SRC, 'estimated', 'free coordinates')
    register('kint_' + _t, _int, _S11SRC, 'estimated', 'interior coordinates')
    register('mae_' + _t, _mae, _S11SRC, 'estimated',
             'mean absolute deviation over the population moments')
    register('beta_c_' + _t, float(par(_t, 'beta_c')), _S11SRC, 'estimated',
             'weight on log consumption')
    register('beta_c_se_' + _t, float(par(_t, 'beta_c', 'se_robust_CR1')),
             _S11SRC, 'estimated', 'cluster-robust standard error')
    register('sigma_' + _t, float(par(_t, 'sigma')), _S11SRC, 'estimated',
             'log-wage dispersion')
register('negll_ruma', 6403.974284931, _S11SRC, 'estimated',
         'log-likelihood units')
register('negll_rumb', 6395.107857484, _S11SRC, 'estimated',
         'log-likelihood units')
register('rum_gap', round(6395.107857484 - 6253.463074380, 2), _S11SRC,
         'estimated', 'log-points')
register('mae_ruma', _S11REC['results']['RUM-A']['criterion_b_population_fit'][
             'mean_absolute_error'], _S11SRC, 'estimated',
         'mean absolute deviation over the population moments')
register('mae_rumb', _S11REC['results']['RUM-B']['criterion_b_population_fit'][
             'mean_absolute_error'], _S11SRC, 'estimated',
         'mean absolute deviation over the population moments')
register('kfree_rumb', 16, _S11SRC, 'estimated', 'free coordinates')
register('kfree_ruma', 10, _S11SRC, 'estimated', 'free coordinates')
for _t, _v in [('singles', 0.166893), ('couples', 0.0770744)]:
    register('mineig_' + _t, _v, _S11SRC, 'diagnostic',
             'smallest Hessian eigenvalue on the interior block')
for _t, _v in [('singles', '1.1e-10'), ('couples', '1.3e-09')]:
    register('spread_' + _t, _v, _S11SRC, 'diagnostic',
             'negLL spread over ten terminal paths')

# the proportional nat: exp(1/beta_c), stated as a factor, never as one euro sum
import math as _math  # noqa: E402
for _t in ['singles', 'couples']:
    _f = _math.exp(1.0 / REG['beta_c_' + _t]['value'])
    register('nat_factor_' + _t, round(_f, 4), _S11SRC, 'derived',
             'multiplicative factor on consumption')
    register('nat_pct_' + _t, round(100.0 * (_f - 1.0), 1), _S11SRC, 'derived',
             'per cent increase in consumption')
# MEASURE-DEF-1: pm_weight_double ("an alternative paying twice the median
# contributes N times as much") described a contribution to the retired
# ex-ante power-moment welfare functional; removed together with that
# functional's prose, not carried forward under the accepted W1_F measure,
# which has no such power-moment contribution at all.

# =========================================================================== #
# 3.  THE PRELIMINARY P/A/B DECOMPOSITION (DECOMP-2)
# =========================================================================== #
# Retired under DECOMP-PRESEMINAR-1: the four-factor P/A/B/D decomposition
# previously loaded here from s12_six_index_attributions_v1.csv,
# s12_s11_cr1_headline_shares_v1.csv and s12_couples_nested_D_attributions_v1.*
# (headline_decomposition_v1.csv / ss8_step1_states_v1.json /
# cw_step3_states_v1.json / gn_step2_nested_v1.json are the earlier retired
# generation of the same lineage; this file never read those directly).
# Superseded by DECOMP-2's bounded, preliminary three-factor P/A/B exercise,
# same lineage and same loader pattern already used by
# reports/results_gallery_build/build.py: MNL_decomp worktree, branch
# welfare/preseminar-pab, commit b52761b4. Deliberately NOT sourced from any
# of the four retired files above.
DECOMP2 = ROOT.parent / 'MNL_decomp' / 'outputs/welfare/preseminar_pab_v1'
_D2SRC = ('MNL_decomp preseminar_pab_v1 (welfare/preseminar-pab, b52761b4); '
          'preliminary three-factor P/A/B decomposition, not the final '
          'decomposition architecture')
D2_COAL = {s: pd.read_csv(DECOMP2 / ('coalition_values_%s.csv' % s))
           for s in ('singles', 'couples')}
D2_SHAP = {s: pd.read_csv(DECOMP2 / ('shapley_PAB_%s.csv' % s))
           for s in ('singles', 'couples')}
D2_VAR = pd.read_csv(DECOMP2 / 'log_variance_split_v1.csv')
D2_ANCHOR = json.loads((DECOMP2 / 'anchor_excluded_arm_v1.json')
                       .read_text('utf-8'))
D2_SCALE = {'uneq': 'unequivalised', 'eq': 'equivalised'}
D2_COAL_LABEL = {'EMPTY': 'Actual (no equalization)', 'P': 'P', 'A': 'A',
                 'B': 'B', 'PA': 'P + A', 'PB': 'P + B', 'AB': 'A + B',
                 'PAB': 'P + A + B'}


def d2_coalition_row(sample, scale_key, coalition):
    scale = D2_SCALE[scale_key]
    m = D2_COAL[sample][(D2_COAL[sample]['scale'] == scale)
                        & (D2_COAL[sample]['coalition'] == coalition)]
    if len(m) != 1:
        raise SystemExit('DECOMP-2 coalition row not unique: %r'
                         % ((sample, scale, coalition),))
    return m.iloc[0]


def d2_shapley_row(sample, scale_key, factor):
    scale = D2_SCALE[scale_key]
    m = D2_SHAP[sample][(D2_SHAP[sample]['scale'] == scale)
                        & (D2_SHAP[sample]['factor'] == factor)]
    if len(m) != 1:
        raise SystemExit('DECOMP-2 shapley row not unique: %r'
                         % ((sample, scale, factor),))
    return m.iloc[0]


for _s in ('singles', 'couples'):
    for _sk in ('uneq', 'eq'):
        _empty = d2_coalition_row(_s, _sk, 'EMPTY')
        _pab = d2_coalition_row(_s, _sk, 'PAB')
        _base = float(_empty['I_S_gini'])
        # I(actual) - I(P,A,B equalized): positive, since equalizing reduces
        # inequality. NOTE: this is the OPPOSITE sign convention from the
        # coalition CSV's own "change_from_actual" column (I(coalition) -
        # I(actual), negative for a reduction) -- both are correct in their
        # own file, this line matches the paper's own stated definition,
        # Delta I = I(empty) - I({P,A,B}).
        _delta = _base - float(_pab['I_S_gini'])
        register('d2_baseline_%s_%s' % (_s, _sk), round(_base, 6), _D2SRC,
                 'result', 'Gini units, baseline coalition (actual)')
        register('d2_deltaI_%s_%s' % (_s, _sk), round(_delta, 6), _D2SRC,
                 'result', 'Gini points, I(actual) minus I(P,A,B equalized)')
        register('d2_deltaI_pct_%s_%s' % (_s, _sk),
                 round(100.0 * _delta / _base, 1), _D2SRC, 'result',
                 'per cent of baseline Gini')
        for _f in ('P', 'A', 'B'):
            _row = d2_shapley_row(_s, _sk, _f)
            register('d2_gini%s_%s_%s' % (_f, _s, _sk),
                     round(float(_row['gini_point_contribution']), 6), _D2SRC,
                     'result', 'Gini points, exact Shapley contribution')
            if _f != 'P':
                register('d2_share%s_%s_%s' % (_f, _s, _sk),
                         round(100.0 * float(_row['share_of_delta_I']), 1),
                         _D2SRC, 'result', 'per cent of Delta_I')
    # variance decomposition is reported once per sample, on the actual
    # (EMPTY) coalition -- the fixed-resources share of dispersion in the
    # REPORTED distribution, not in the counterfactual-equalized one.
    _ve = D2_VAR[(D2_VAR['sample'] == _s) & (D2_VAR['coalition'] == 'EMPTY')].iloc[0]
    register('d2_varshare_logC_%s' % _s,
             round(100.0 * float(_ve['share_var_log_C']), 0), _D2SRC,
             'diagnostic', 'per cent of the variance of log W1_F')

# Robustness: the anchor node the estimation panel inserts deterministically
# in every coalition. Report the worst-case (largest absolute) relative move
# in Delta_I across the four sample x scale cells, and which cell it is --
# same selection rule as reports/results_gallery_build/build.py's
# d2_anchor_line().
_moves = [(s, sk, D2_ANCHOR[s][D2_SCALE[sk]]['delta_I_relative_move'])
          for s in ('singles', 'couples') for sk in ('uneq', 'eq')]
_worst = max(_moves, key=lambda t: abs(t[2]))
register('d2_anchormove_pct', round(abs(_worst[2]) * 100.0, 1), _D2SRC,
         'diagnostic', 'per cent, largest absolute relative move in Delta_I')
register('d2_anchormove_cell', '%s, %s' % (_worst[0], D2_SCALE[_worst[1]]),
         _D2SRC, 'diagnostic', 'sample and scale of the largest move')
for _s in ('singles', 'couples'):
    _share = float(d2_coalition_row(_s, 'uneq', 'EMPTY')
                   ['share_attaining_the_observed_node'])
    register('d2_anchorshare_%s' % _s, round(100.0 * _share, 1), _D2SRC,
             'diagnostic', 'per cent of households attaining the observed '
             'node under the actual coalition')

# MEASURE-DEF-1: the "welfare levels" registration block that stood here
# (wl_* from v5_welfare_distributions_v1.csv, inc_gini_* from
# lorenz_observed_income) fed the report-only "ex-ante measure's levels"
# subsection and figures (welfdist, lorenz) in RESULTS. That subsection
# reported the retired ex-ante inclusive-value construction's own levels,
# a different object from the verified Mapping-F W1_F baseline (below) --
# removed under MEASURE-DEF-1 rather than relabelled, since it produced a
# reported number from a construction Deputy ruling R2 retired. Nothing
# else read WD/ARM/SAMP or these keys; removed together, not left orphaned.

# =========================================================================== #
# REBUILD-2: the verified Mapping-F W1_F construction (BASELINE-F-1 / E3-EQ).
# Unequivalised aggregates: MNL commit 6048c9f7, independently verified
# b5550af5 (baseline_f1_verification_v1.md). Equivalised reporting: memo
# 4c4e07e (this repo). Same lineage the r6 deck's own baseline slides use
# (make_deck_numbers_r6.py) -- deliberately the same source, not a new one.
_BF1 = MNL / 'outputs/welfare/baseline_f1_v1/baseline_f1_full_sample_aggregates_v1.json'
_BF1SRC = ('baseline_f1_full_sample_aggregates_v1.json (MNL 6048c9f7, '
           'verified b5550af5)')
_bf1 = json.loads(_BF1.read_text('utf-8'))
for _tag in ['singles', 'couples']:
    s = _bf1['samples'][_tag]
    register('w1f_n_' + _tag, int(s['unweighted_n']), _BF1SRC, 'result', 'households')
    register('w1f_workers_' + _tag, int(s['worker_count']), _BF1SRC, 'result', 'households')
    register('w1f_nonworkers_' + _tag, int(s['nonworker_count']), _BF1SRC, 'result', 'households')
    register('w1f_mean_' + _tag, round(float(s['dwt_weighted_mean']), 0), _BF1SRC,
             'result', 'EUR/month, unequivalised')
    register('w1f_median_' + _tag, round(float(s['dwt_weighted_median']), 0), _BF1SRC,
             'result', 'EUR/month, unequivalised')
    register('w1f_gini_' + _tag, round(float(s['dwt_weighted_gini']), 4), _BF1SRC,
             'result', 'Gini units, unequivalised')

_BF1EQSRC = ('{sample}_equivalised_reporting_v1.json '
             '(JMP_BASELINE_F1_equivalised_reporting_v1.md, commit 4c4e07e; '
             'MNL 6048c9f7)')
for _tag in ['singles', 'couples']:
    _eq = json.loads((MNL / ('outputs/welfare/baseline_f1_equivalised_v1/'
                             '%s_equivalised_reporting_v1.json' % _tag))
                     .read_text('utf-8'))['equivalised']
    _src = _BF1EQSRC.format(sample=_tag)
    for _obj, _pfx in [('C_eq', 'ceq'), ('W_F_eq', 'w1f_eq')]:
        register('%s_mean_%s' % (_pfx, _tag),
                 round(float(_eq[_obj]['dwt_weighted_mean']), 0), _src,
                 'result', 'EUR/month, equivalised')
        register('%s_median_%s' % (_pfx, _tag),
                 round(float(_eq[_obj]['dwt_weighted_median']), 0), _src,
                 'result', 'EUR/month, equivalised')
        register('%s_gini_%s' % (_pfx, _tag),
                 round(float(_eq[_obj]['dwt_weighted_gini']), 4), _src,
                 'result', 'Gini units, equivalised')

# REBUILD-2 limitations: the single-men fit gap, recomputed here from the
# same S11 criterion-B moments table the fit tables above already use, not
# a new source.
_MOMSRC = 's11_criterion_b_population_moments_v1.csv'
_sm = MOM[(MOM['model'] == 'SINGLES') & (MOM['sex'] == 'male')]
_sm_emp = _sm[_sm['moment'] == 'employment'].iloc[0]
_sm_ft = _sm[_sm['moment'] == 'hours::ft'].iloc[0]
register('singlesmale_emp_gap_pp',
         round(100.0 * abs(float(_sm_emp['observed']) - float(_sm_emp['predicted'])), 1),
         _MOMSRC, 'diagnostic', 'percentage points, S11 model of record')
register('singlesmale_hours_gap_pp',
         round(100.0 * abs(float(_sm_ft['observed']) - float(_sm_ft['predicted'])), 1),
         _MOMSRC, 'diagnostic', 'percentage points, S11 model of record')

# neutrality, bridge -- unrelated to the P/A/B decomposition above.
# REBUILD-3: closes the LINEAGE-SWEEP-1/REBUILD-1 item-17 residual. The
# "Wage-density neutrality" numerics (dlogh_*, direct_median, attain_median_*)
# and the W3 relative-index diagnostic below both cited
# s12_welfare_record_report_v1.md, a retired-lineage artifact. Repointed
# against the accepted sources named in REBUILD-3 (JMP_W1_fork_ruling_v1.md
# R1, JMP_measure_map_v1.md, baseline_f1_verification_v1.md):
#   - the pay-neutrality claim SURVIVES, more strongly than stated before --
#     R1: "the opportunity density g, the numerical proposal q, the
#     behavioural shocks epsilon, and the intensity kappa" do not enter the
#     accepted W1-F reference at all, an exact property of the construction,
#     not a numerical residual. The dlogh_*/direct_median numbers were a
#     redundant numerical check of an already-exact algebraic fact (H has no
#     wage argument by construction; see v5_sections.py's WELFARE section)
#     and are dropped as no longer needed, not because the claim failed.
#   - attain_median_* is dropped: it quantified an earning-opportunity
#     counterfactual under the retired S12 P/A/B/D simulation. No accepted
#     source computes this magnitude; Section 4 now states the (still true)
#     qualitative channel without a number.
#   - the W3 relative-index diagnostic (below) does NOT survive: MEASURE-MAP-1R
#     classifies W3 as "DIFFERENT OBJECT... REUSABLE FOR LITERAL: no" and its
#     R4 final statement lists it under "no current ruling requires". Removed
#     from v5_sections.py's SENSITIVITY section entirely, not recited.
# MEASURE-DEF-1: the W1/W4 bridge block that stood here (gint_med_*,
# w41_*, delta_med_* from s12_w4_premise_audit_v1.json) defined W1 itself
# via the retired ex-ante J/H integrals ("beta_c*log(W1/lambda_c) = log J -
# log H"), reusing the paper's own "W1" symbol for a different, retired
# object. Removed together with the SENSITIVITY and appendix prose that
# read it; the pay-neutrality finding those sections separately supported
# survives on its own, stronger footing (Section 4, Deputy ruling R1) and
# needed no bridge to state.

for _p in ['jax', 'jaxlib', 'euromod']:
    try:
        register('installed_' + _p, importlib.metadata.version(_p),
                 'build environment package metadata', 'software', 'version')
    except importlib.metadata.PackageNotFoundError:
        register('installed_' + _p, 'not recorded in this environment',
                 'build environment package metadata', 'software', 'version')


# =========================================================================== #
# 4.  TABLES
# =========================================================================== #
def table(name, caption, headers, rows):
    with (TABLE / (name + '.csv')).open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(headers)
        w.writerows(rows)
    return ('\n' + caption + '\n\n|' + '|'.join(headers) + '|\n|'
            + '|'.join(['---'] * len(headers)) + '|\n'
            + ''.join('|' + '|'.join(str(v).replace('|', '/') for v in row)
                      + '|\n' for row in rows) + '\n')


TABLES: dict = {}

# ---- T1: the final funnel ------------------------------------------------- #
_flow = pd.read_csv(SPRINT / 'runs/final_descriptives/fd_funnel_v1.csv')
_tail = pd.read_csv(V5 / 'v5_funnel_tail_v1.csv')
_rows = []
for _, r in _flow.iloc[:8].iterrows():
    _rows.append([str(r['screen']).replace(
        'hours and wage inside the modelled support',
        'observed hours and wage inside the calibrated support'),
        format(int(r['households_singles']), ',d'),
        format(int(r['households_couples']), ',d')])
for _, r in _tail.iloc[:2].iterrows():
    _rows.append([str(r['screen']), format(int(r['households_singles']), ',d'),
                  format(int(r['households_couples']), ',d')])
_rows.append(['**Estimation sample**', '**1,540**', '**2,223**'])
TABLES['funnel'] = table(
    'v5_funnel',
    'Table: Sample construction. Unweighted households remaining after each '
    'screen, from the France 2016 EUROMOD input file to the two estimation '
    'samples. Rows are sequential; the counts are read from the frame records '
    'and are not reconstructed by subtraction.',
    ['Screen', 'Single-adult', 'Couple'], _rows)

# ---- T2: descriptives on the estimation frame ----------------------------- #
_CONT = pd.read_csv(V5 / 'v5_descriptives_continuous_v1.csv')
_CAT = pd.read_csv(V5 / 'v5_descriptives_categorical_v1.csv')


def _cont(unit, var, stat):
    m = _CONT[(_CONT['unit'] == unit) & (_CONT['variable'] == var)]
    if len(m) != 1:
        raise SystemExit('descriptive not unique: %r' % ((unit, var),))
    return float(m.iloc[0][stat])


_UNITS = [('the decider', 'the man', 'the woman'),
          ('the employed decider', 'the employed man', 'the employed woman')]
_rows = []
for label, var, which, fmt in [
        ('Age (years)', 'age', 0, '.1f'),
        ('Children under 20', 'children under 20', 0, '.2f'),
        ('Usual weekly hours, employed', 'weekly hours (continuous)', 1, '.1f'),
        ('Delivered hourly wage, employed (EUR/hour)',
         'hourly wage (EUR/hour)', 1, '.2f')]:
    cells = []
    for u in _UNITS[which]:
        try:
            cells.append(format(_cont(u, var, 'mean_weighted'), fmt))
        except SystemExit:
            cells.append('--')
    _rows.append([label] + cells)


def _cat(htype, dim, cat):
    m = _CAT[(_CAT['household_type'] == htype) & (_CAT['dimension'] == dim)
             & (_CAT['category'].astype(str) == cat)]
    return float(m.iloc[0]['share_weighted']) if len(m) == 1 else None


_rows.append(['Households (unweighted)', '1,540', '2,223', ''])
TABLES['descriptives'] = table(
    'v5_descriptives',
    'Table: Descriptive means on the estimation samples. Weighted by the '
    'household cross-sectional weight; one row per household, with '
    'spouse-specific variables carried on the household row. Hours and wages '
    'are conditional on employment. These are observed inputs, not model '
    'predictions.',
    ['Measure', 'Single-adult decider', 'Couple man', 'Couple woman'], _rows)

# ---- T2b: observed raw LES (LES-FIX, corrected for couples) --------------- #
# The couples design frame's own les_m/les_f columns are a derived
# employed/not-employed {3,7} recode that erases raw code 5 (Unemployed);
# raw LES is recovered by joining idperson_m/idperson_f back to the raw
# FR 2016 source. See MNL/docs/corr/JMP_observed_activity_LES_v2_audit.md.
_LES = pd.read_csv(MNL / 'outputs/obs_activity_v2/JMP_observed_activity_LES_v2.csv')
_LES_GROUP_ORDER = ['single_men', 'single_women', 'couple_men', 'couple_women']
_LES_GROUP_LABEL = {'single_men': 'Single men', 'single_women': 'Single women',
                     'couple_men': 'Men in couples', 'couple_women': 'Women in couples'}
_rows = []
_lesA = _LES[_LES['figure'] == 'A']
for g in _LES_GROUP_ORDER:
    gdf = _lesA[_lesA['group'] == g].set_index('les_code')
    n_total = int(gdf['n_group_total_unweighted'].iloc[0])
    cells = []
    for code in (3, 5, 7):
        r = gdf.loc[code]
        cells.append('%.1f%% (n=%d)' % (100 * r['weighted_share'], int(r['n_unweighted'])))
    _rows.append([_LES_GROUP_LABEL[g]] + cells + [format(n_total, ',d')])
TABLES['observed_les'] = table(
    'v5_observed_les',
    'Table: Observed raw labour-force status (LES), weighted shares with '
    'unweighted counts in parentheses, by sex and household type, on the '
    'final estimation samples. For couples this uses raw '
    'LES recovered by joining idperson_m/idperson_f to the raw FR 2016 '
    'source, not the design frame’s own les_m/les_f columns, which are a '
    'derived employed/not-employed recode that omits raw code 5 '
    '(Unemployed) entirely. **The structural model does not distinguish '
    'unemployment from inactivity: both LES 5 and LES 7 map to the single '
    'nonwork alternative.** This table is a descriptive correction to how '
    'the observed data is displayed, not a change to the model or the '
    'estimation sample.',
    ['Group', 'Employee (LES 3)', 'Unemployed (LES 5)', 'Inactive (LES 7)', 'N'],
    _rows)

# ---- T3: occupation mapping ----------------------------------------------- #
TABLES['occmap'] = table(
    'v5_occupation_map',
    'Table: The four occupation groups. ISCO-08 major groups are aggregated '
    'into four modelled groups; group 1 is the omitted reference in the '
    'estimated occupation block. This is a research aggregation adopted for '
    'this paper, not an ILO classification. ISCO 0, the armed forces, has no '
    'modelled alternative and is a sample screen; that is unsupported '
    'occupation, not missing occupation.',
    ['Model group', 'ISCO-08 major groups', 'Description'],
    [['1 (reference)', '6--9',
      'Skilled agricultural, craft, plant and machine operators, and '
      'elementary occupations'],
     ['2', '5', 'Service and sales workers'],
     ['3', '4', 'Clerical support workers'],
     ['4', '1--3', 'Managers, professionals, technicians and associate '
      'professionals']])

# ---- T4: couples participation regimes ------------------------------------ #
_REG = pd.read_csv(V5 / 'v5_couples_regimes_v1.csv')
TABLES['regimes'] = table(
    'v5_couples_regimes',
    'Table: Observed joint participation regimes among the 2,223 estimated '
    'couple households. These are joint regimes, not two spouse marginals.',
    ['Regime', 'Meaning', 'Weighted share', 'Mean hours, man',
     'Mean hours, woman'],
    [[str(r['regime']), str(r['meaning']),
      format(float(r['share_weighted']), '.4f'),
      format(float(r['mean_hours_man_weighted']), '.1f'),
      format(float(r['mean_hours_woman_weighted']), '.1f')]
     for _, r in _REG.iterrows() if str(r['regime']) != 'TOTAL'])

# ---- T5-T7: coefficients by economic block -------------------------------- #
GREEK = {
    'beta_l0': r'$\beta_{\ell 0}$', 'beta_l_age': r'$\beta_{\ell a}$',
    'beta_l_age2': r'$\beta_{\ell a^2}$', 'beta_l_nkids': r'$\beta_{\ell n}$',
    'theta_l': r'$\theta_\ell$'}


def _cell(tag, name, digits=4):
    m = PAR[tag][PAR[tag]['param'] == name]
    if len(m) != 1:
        return '--'
    r = m.iloc[0]
    if bool(r['pinned']):
        return format(float(r['estimate']), '.%df' % digits) + ' (restricted)'
    if bool(r['active_bound']):
        return format(float(r['estimate']), '.%df' % digits) + ' (at bound)'
    se = r['se_robust_CR1']
    if pd.isna(se):
        return format(float(r['estimate']), '.%df' % digits)
    return (format(float(r['estimate']), '.%df' % digits) + ' ('
            + format(float(se), '.%df' % digits) + ')')


PREF_ROWS = [
    (r'Leisure weight, intercept ' + GREEK['beta_l0'],
     'beta_l0_sm', 'beta_l0_sf', 'beta_l0_m', 'beta_l0_f'),
    (r'Leisure weight, age ' + GREEK['beta_l_age'],
     'beta_l_age_sm', 'beta_l_age_sf', 'beta_l_age_m', 'beta_l_age_f'),
    (r'Leisure weight, age squared ' + GREEK['beta_l_age2'],
     'beta_l_age2_sm', 'beta_l_age2_sf', 'beta_l_age2_m', 'beta_l_age2_f'),
    (r'Leisure weight, children ' + GREEK['beta_l_nkids'],
     None, 'beta_l_nkids_sf', None, 'beta_l_nkids_f'),
    (r'Leisure curvature ' + GREEK['theta_l'],
     'theta_l_sm', 'theta_l_sf', 'theta_l_m', 'theta_l_f')]
_rows = []
for lab, sm, sf, cm, cf in PREF_ROWS:
    _rows.append([lab,
                  '&mdash;' if sm is None else _cell('singles', sm),
                  _cell('singles', sf),
                  '&mdash;' if cm is None else _cell('couples', cm),
                  _cell('couples', cf)])
_rows.append([r'Consumption weight $\beta_c$',
              _cell('singles', 'beta_c'), _cell('singles', 'beta_c'),
              _cell('couples', 'beta_c'), _cell('couples', 'beta_c')])
TABLES['pref'] = table(
    'v5_coefficients_preferences',
    'Table: The preference block. Cluster-robust standard errors in '
    'parentheses, clustered on the household. "At bound" '
    'marks an estimate at a box endpoint, whose interval is reported under the '
    'active-set convention in the appendix. The consumption weight is common '
    'within a population and enters as $\\beta_c\\log(C/\\lambda_c)$.',
    ['Coefficient', 'Single men', 'Single women', 'Couple men',
     'Couple women'], _rows)

ACC_ROWS = [
    (r'Employment constant $\beta_E$', 'beta_E', 'beta_E_m', 'beta_E_f'),
    (r'Group unemployment rate $\beta_{E,gsur}$', 'beta_E_gsur',
     'beta_E_gsur', 'beta_E_gsur'),
    (r'Densely populated $\beta_{E,u}$', 'beta_E_drgur', 'beta_E_drgur',
     'beta_E_drgur'),
    (r'Intermediate density $\beta_{E,m}$', 'beta_E_drgmd', 'beta_E_drgmd',
     'beta_E_drgmd')]
_rows = []
for lab, s, cm, cf in ACC_ROWS:
    if lab.startswith(r'Employment constant'):
        _rows.append([lab, _cell('singles', s), _cell('couples', cm),
                      _cell('couples', cf)])
    else:
        _rows.append([lab, _cell('singles', s), _cell('couples', cm),
                      'shared with the man'])
for k in range(2, 9):
    _rows.append([r'Region %d $\beta_{E,%d}$' % (k, k),
                  _cell('singles', 'beta_E_drgn%d' % k),
                  _cell('couples', 'beta_E_drgn%d' % k),
                  'shared with the man'])
HRS = [('Part-time lower, [17.5, 21.5)', 'pt1'),
       ('Part-time upper, [28.5, 30.5)', 'pt2'),
       ('Narrow full-time, [33.5, 36.5)', 'f35'),
       ('Full-time upper, [36.5, 40.5]', 'ft'),
       ('Long hours, [44.5, 70]', 'lh')]
for lab, k in HRS:
    _rows.append([r'Hours band: ' + lab,
                  _cell('singles', 'beta_h_' + k),
                  _cell('couples', 'beta_h_%s_m' % k),
                  _cell('couples', 'beta_h_%s_f' % k)])
for k in range(2, 5):
    _rows.append([r'Occupation %d $\xi_%d$' % (k, k),
                  _cell('singles', 'beta_occ_%d_f' % k),
                  _cell('couples', 'beta_occ_%d_m' % k),
                  _cell('couples', 'beta_occ_%d_f' % k)])
TABLES['access'] = table(
    'v5_coefficients_access',
    'Table: The opportunity block: employment access, the hours density and '
    'occupation access. Cluster-robust standard errors in parentheses. The '
    'employment index multiplies the working indicator; the omitted references '
    'are region 1, thinly populated areas, the residual hours set of total '
    'width 26.5 hours per week, and occupation group 1. The singles occupation '
    'column reports the female coordinates; the male coordinates are in the '
    'appendix table. Hours coefficients are common across the two singles sex '
    'groups and spouse-specific for couples.',
    ['Coefficient', 'Singles', 'Couple men', 'Couple women'], _rows)

WAGE_ROWS = [(r'Intercept $\beta_{w0}$', 'beta_w0'),
             (r'Low education $\beta_{wL}$', 'beta_w_educL'),
             (r'High education $\beta_{wH}$', 'beta_w_educH'),
             (r'Potential experience $\beta_{wx}$', 'beta_w_pexp'),
             (r'Experience squared $\beta_{wx^2}$', 'beta_w_pexp2'),
             (r'Occupation 2 $\delta_2$', 'delta_occ_2'),
             (r'Occupation 3 $\delta_3$', 'delta_occ_3'),
             (r'Occupation 4 $\delta_4$', 'delta_occ_4'),
             (r'Log-wage dispersion $\sigma$', 'sigma')]
_rows = [[lab, _cell('singles', p), _cell('couples', p)]
         for lab, p in WAGE_ROWS]
_rows.append([r'Consumption weight $\beta_c$', _cell('singles', 'beta_c'),
              _cell('couples', 'beta_c')])
TABLES['wage'] = table(
    'v5_coefficients_wage',
    'Table: The wage block and the consumption weight. The offered log wage '
    'is normal with mean $\\mu_i(k)$ and dispersion $\\sigma$, truncated to '
    '[2, 590] EUR/hour and renormalized on that support. Experience enters in '
    'units of twenty years. Slopes and $\\sigma$ are common across the two '
    'singles sex groups and across spouses within couples; the singles and '
    'couples models are estimated separately, so the two columns are not '
    'restricted to agree.',
    ['Coefficient', 'Singles', 'Couples'], _rows)

# ---- appendix: the complete parameter vectors ----------------------------- #
for _tag, _key in [('singles', 'fullsingles'), ('couples', 'fullcouples')]:
    _rows = []
    for _, r in PAR[_tag].iterrows():
        if bool(r['pinned']):
            continue
        status = 'at bound' if bool(r['active_bound']) else 'estimated'
        se = ('--' if pd.isna(r['se_robust_CR1'])
              else format(float(r['se_robust_CR1']), '.6g'))
        z = ('--' if pd.isna(r['z_robust'])
             else format(float(r['z_robust']), '.3f'))
        _rows.append([r'\path{%s}' % r['param'],
                      format(float(r['estimate']), '.6g'), se, z,
                      '[%g, %g]' % (r['lower_bound'], r['upper_bound']),
                      status])
    TABLES[_key] = table(
        'v5_full_coefficients_' + _tag,
        'Table: The %s estimated coordinates. Standard errors are '
        'cluster-robust on the household; boundary-active estimates are marked '
        'at bound. Maintained restrictions are stated once in the accompanying note.'
        % _tag,
        ['Coordinate', 'Estimate', 'CR1 s.e.', 'z', 'Box', 'Status'], _rows)

# ---- T8/T9: fit by margin ------------------------------------------------- #
MOMLAB = {'employment': 'Employment', 'mean_log_wage': 'Mean log wage'}


def _momlab(m):
    if m in MOMLAB:
        return MOMLAB[m]
    if m.startswith('hours::'):
        k = m.split('::')[1]
        return 'Hours: ' + {'zero': 'non-employment', 'pt1': '[17.5, 21.5)',
                            'pt2': '[28.5, 30.5)', 'f35': '[33.5, 36.5)',
                            'ft': '[36.5, 40.5]', 'lh': '[44.5, 70]',
                            'h_0_10': '[5, 10)', 'h_10_17_5': '[10, 17.5)',
                            'h_21_5_28_5': '[21.5, 28.5)',
                            'h_30_5_33_5': '[30.5, 33.5)',
                            'h_40_5_44_5': '(40.5, 44.5)'}.get(k, k)
    if m.startswith('occupation::'):
        return 'Occupation group ' + m.split('::')[1]
    if m.startswith('quadrant::'):
        return 'Joint regime ' + {'NN': 'neither works', 'MO': 'man only',
                                  'WO': 'woman only',
                                  'BB': 'both work'}[m.split('::')[1]]
    return m


for _tag, _model in [('singles', 'SINGLES'), ('couples', 'COUPLES')]:
    d = MOM[MOM['model'] == _model]
    _rows = []
    for sex in ['household', 'male', 'female']:
        s = d[d['sex'] == sex]
        for _, r in s.iterrows():
            _rows.append([{'household': 'Household', 'male': 'Man',
                           'female': 'Woman'}[sex], _momlab(r['moment']),
                          format(float(r['observed']), '.4f'),
                          format(float(r['predicted']), '.4f'),
                          format(float(r['absolute_error']), '.4f'),
                          str(r['denominator'])])
    TABLES['fit' + _tag] = table(
        'v5_fit_' + _tag,
        'Table: Observed against model population shares, %s. The model column '
        'is a population prediction computed by direct integration over the '
        'estimated opportunity distribution and the taste shocks; it is not a '
        'sampled-menu choice probability and not an in-sample fitted value. '
        'The denominator column states the population each share is taken '
        'over.' % _tag,
        ['Unit', 'Moment', 'Observed', 'Model', 'Absolute deviation',
         'Denominator'], _rows)

# ---- T9b: the verified own-set equal-consumption baseline, equivalised ---- #
_rows = []
for tag, pop in [('singles', 'Single-adult'), ('couples', 'Couple')]:
    _rows.append([
        pop, format(REG['w1f_n_' + tag]['value'], ',d'),
        format(REG['w1f_workers_' + tag]['value'], ',d'),
        format(REG['w1f_nonworkers_' + tag]['value'], ',d'),
        format(REG['ceq_mean_' + tag]['value'], ',.0f'),
        format(REG['ceq_median_' + tag]['value'], ',.0f'),
        format(REG['ceq_gini_' + tag]['value'], '.4f'),
        format(REG['w1f_eq_mean_' + tag]['value'], ',.0f'),
        format(REG['w1f_eq_median_' + tag]['value'], ',.0f'),
        format(REG['w1f_eq_gini_' + tag]['value'], '.4f')])
TABLES['baselinef1'] = table(
    'v5_baseline_f1',
    'Table: The verified own-set equal-consumption $W^1_F$ construction, modified-OECD '
    'equivalised, against equivalised disposable consumption in the same '
    'sample. Household EUR/month, dwt-weighted. The sample aggregates are '
    'reproduced to machine precision, confirmed by an independent '
    'reimplementation. Reported separately by population; no '
    'pooled figure and no cross-population level comparison.',
    ['Population', 'N', 'Workers', 'Non-workers', '$C^{eq}$ mean',
     '$C^{eq}$ median', '$C^{eq}$ Gini', '$W^1_F{}^{eq}$ mean',
     '$W^1_F{}^{eq}$ median', '$W^1_F{}^{eq}$ Gini'], _rows)

# MEASURE-DEF-1: T10 ("welfare levels", TABLES['levels']) reported the
# retired ex-ante measure's own levels against priced disposable income,
# fed by the wl_*/inc_gini_* registrations removed above. Removed together
# with the report-only "ex-ante measure's levels" subsection that used it;
# T9b below (TABLES['baselinef1']) is the accepted W1_F equivalent.

# ---- T11: the eight P/A/B coalitions, per sample --------------------------- #
def _d2_coalition_table(sample, label):
    _rows = []
    for scale_key in ('uneq', 'eq'):
        scale = D2_SCALE[scale_key]
        for coalition in ('EMPTY', 'P', 'A', 'B', 'PA', 'PB', 'AB', 'PAB'):
            r = d2_coalition_row(sample, scale_key, coalition)
            _rows.append([scale, D2_COAL_LABEL[coalition],
                          format(float(r['I_S_gini']), '.4f'),
                          format(float(r['change_from_actual']), '+.4f'),
                          format(float(r['mc_min']), '.4f') + '–'
                          + format(float(r['mc_max']), '.4f')])
    return table(
        'v5_pab_coalition_%s' % sample,
        'Table: %s, the eight P/A/B coalitions. Weighted Gini of money-metric '
        'well-being, dwt-weighted, simulated on the estimated model’s '
        'already-priced estimation panel with no re-estimation and no new '
        'pricing. "Change from actual" is the one-factor effect of that '
        'coalition. The Monte Carlo range is the spread of the Gini level '
        'across 1,000 simulation replications, never a confidence interval.'
        % label,
        ['Scale', 'Coalition', 'I(S), Gini', 'Change from actual',
         'MC range (min–max)'], _rows)


TABLES['pabcoalitionsingles'] = _d2_coalition_table('singles', 'Single adults')
TABLES['pabcoalitioncouples'] = _d2_coalition_table('couples', 'Couples')

# ---- T12: the exact three-player Shapley allocation ------------------------ #
_rows = []
for _s, _pop in [('singles', 'Single-adult'), ('couples', 'Couple')]:
    for _sk in ('uneq', 'eq'):
        _scale = D2_SCALE[_sk]
        for _f, _lab in [('P', 'Preferences (systematic utility '
                          'heterogeneity)'),
                         ('A', 'Local access shifters '
                               '(region, urban/rural, year)'),
                         ('B', 'Earning opportunities')]:
            row = d2_shapley_row(_s, _sk, _f)
            cell = [_pop, _scale, _f, _lab,
                    format(float(row['gini_point_contribution']), '+.4f')]
            if _f == 'P':
                cell.append('—')  # no directional claim -- see prose
            else:
                cell.append(format(float(row['share_of_delta_I']) * 100,
                                   '.1f') + '%')
            cell.append(format(float(row['second_seed_gini_point']), '+.4f'))
            _rows.append(cell)
        _di = d2_shapley_row(_s, _sk, 'Delta_I')
        _rows.append([_pop, _scale, r'$\Delta I$', 'I(actual) $-$ I(P,A,B '
                      'equalized)', format(float(_di['gini_point_contribution']),
                                           '+.4f'), '100.0%',
                      format(float(_di['second_seed_gini_point']), '+.4f')])
TABLES['pabshapley'] = table(
    'v5_pab_shapley',
    'Table: The exact three-player Shapley allocation of $\\Delta I$ across '
    'P, A and B. Gini-point contribution beside the share of $\\Delta I$ '
    '(not of baseline inequality), and an independent second-seed '
    'reproduction. No directional claim is made about P: its sign changes '
    'between unequivalised and equivalised reporting in both samples, so '
    'its share of $\\Delta I$ is not stated. A Monte Carlo per-replication '
    'share range, which divides by that replication’s own near-zero '
    '$\\Delta I$ and is not informative on its own, is reported in the '
    'technical gallery, not here.',
    ['Population', 'Scale', 'Factor', 'Label', 'Gini-point contribution',
     'Share of $\\Delta I$', 'Second-seed Gini-point'], _rows)

# ---- T14: the benchmark comparison ---------------------------------------- #
TABLES['benchmark'] = table(
    'v5_benchmark',
    'Table: The estimated model against two re-estimated common-opportunity '
    'benchmarks, on the same 1,540 single-adult households, the same sampled '
    'alternatives and the same criterion. A better maximized criterion does '
    'not by itself establish that a mechanism has been identified; the '
    'margin-by-margin comparison in the fit table and figure is the substantive '
    'evidence.',
    ['Specification', 'Free coordinates', 'Criterion', 'Difference',
     'Population fit'],
    [['Latent jobs with household-specific opportunities',
      val('kfree_singles'), val('negll_singles', '.3f'), '--',
      val('mae_singles', '.4f')],
     ['Benchmark A: common opportunity distribution, preferences re-estimated',
      val('kfree_ruma'), val('negll_ruma', '.3f'),
      format(6403.974284931 - 6253.463074380, '+.2f'), val('mae_ruma', '.4f')],
     ['Benchmark B: common opportunity shape, employment and hours moved into '
      'utility and re-estimated',
      val('kfree_rumb'), val('negll_rumb', '.3f'),
      format(6395.107857484 - 6253.463074380, '+.2f'), val('mae_rumb', '.4f')]])

# ---- T15: the operators of the preliminary decomposition ------------------- #
TABLES['operators'] = table(
    'v5_operators',
    'Table: The three structural equalization operators of the preliminary '
    'decomposition (Section 5). Each operator replaces the arguments of one '
    'structural pathway with a common reference profile and leaves the '
    'estimated coefficients in place; it does not equalize every occurrence '
    'of a raw characteristic. Operators are applied as one simultaneous '
    'substitution map, not as an ordered product. Household resources, needs '
    'and composition are held fixed throughout this exercise -- not a fourth '
    'operator here -- pending the counterfactual-attainment estimand the '
    'paper’s final decomposition architecture requires.',
    ['Operator', 'What is replaced', 'What is retained'],
    [[r'$T_P$ preferences (systematic utility heterogeneity)',
      'Singles: the arguments of the leisure weight and the complete '
      'reference-sex leisure block. Couples: the medoid spouse arguments, with '
      'own spouse coefficients retained',
      'Access and wage pathways of the same characteristics'],
     [r'$T_A$ local geographic/temporal access shifters',
      'Region, urban/rural and year arguments of the employment index',
      'Preferences, wage location, group unemployment, hours-band access, '
      'personal occupation access and node-level alternative characteristics'],
     [r'$T_B$ earning opportunities',
      'The arguments of the offered-wage location: education shares and '
      'experience moments, with squares recomputed rather than averaged',
      'The estimated wage coefficients and dispersion; the preference and '
      'access pathways of the same characteristics']])

# ---- T16: index definitions ----------------------------------------------- #
TABLES['indices'] = table(
    'v5_indices',
    'Table: The six inequality indices, defined on a weighted distribution of '
    'strictly positive levels with mean $\\mu$. Multiplying an index by a '
    'positive constant scales its level and its contributions but not its '
    'shares, so GE(2) and the squared coefficient of variation are the same '
    'game. Atkinson(1) and GE(0) rank any positive distribution identically '
    'because $A(1)=1-e^{-GE(0)}$; their shares can nevertheless differ, '
    'because a nonlinear transformation does not commute with averaging '
    'marginal contributions over coalition orders.',
    ['Index', 'Definition'],
    [['Gini', r'$\frac{1}{2\mu}\,\mathbb{E}\lvert W-\tilde W\rvert$, for '
      r'$W,\tilde W$ independent draws from the distribution'],
     ['Atkinson(1)', r'$1-\exp\!\big(\mathbb{E}\log W\big)/\mu$'],
     ['Atkinson(2)', r'$1-\big(\mathbb{E}[W^{-1}]\big)^{-1}/\mu$'],
     ['GE(0)', r'$\mathbb{E}\log(\mu/W)$'],
     ['GE(1)', r'$\mathbb{E}\big[(W/\mu)\log(W/\mu)\big]$'],
     [r'GE(2) $=CV^2/2$', r'$\tfrac{1}{2}\mathbb{E}\big[(W/\mu)^2-1\big]$']])

# MEASURE-DEF-1: T17 (TABLES['bridge']) reported the W1/W4 bridge, defined
# through the retired ex-ante J/H integrals via `_BR`. Removed together with
# `_BR` and the SENSITIVITY/appendix prose that read it.

# ---- T18: the lambda_c reconciliation ------------------------------------- #
TABLES['lambda'] = table(
    'v5_lambda_c',
    'Table: The consumption normalizer. Three constants were in circulation. '
    'Under exact log consumption the normalizer enters utility as the '
    'alternative-invariant term $-\\beta_c\\log\\lambda_c$, so it cancels from '
    'every choice probability; it does not enter the $W^1_F$ welfare '
    'measure at all. The paper reports the estimation-frame constant '
    'throughout, for the choice-probability role it actually plays.',
    ['Panel', 'Single-adult (EUR/month)', 'Couple (EUR/month)', 'Role'],
    [['Estimation frame, 101 sampled alternatives per household',
      format(REG['lambda_c_singles']['value'], ',.6f'),
      format(REG['lambda_c_couples']['value'], ',.6f'),
      'Constant of record'],
     ['Welfare panel, 2,048 common integration nodes',
      format(REG['lambda_c_welfare_panel_singles']['value'], ',.6f'),
      format(REG['lambda_c_welfare_panel_couples']['value'], ',.6f'),
      'Recomputed over its own rows; inert'],
     ['Predecessor frames, before the sample correction', '1,911.108058',
      '3,821.448012', 'Superseded']])


# =========================================================================== #
# 5.  FIGURES
# =========================================================================== #
CAPTIONS = {}


def mfig(key, stem, caption, src=None):
    """Register a figure rendered by the MNL figure runs."""
    source = MFIG / ((stem + '_paper.png') if src is None else src)
    dest = FIG / (stem + '.png')
    dest.write_bytes(source.read_bytes())
    CAPTIONS[key] = (stem, caption)


def lfig(key, stem, caption):
    """Register a figure already living in the manuscript figure tree."""
    src = PAPER / 'figures/v3' / (stem + '.png')
    (FIG / (stem + '.png')).write_bytes(src.read_bytes())
    CAPTIONS[key] = (stem, caption)


def dfig(key, stem, caption):
    """Register a figure from the DECOMP-2 preliminary-decomposition run
    (MNL_decomp, preseminar_pab_v1) -- same source directory as
    reports/results_gallery_build/build.py's d2fig()."""
    (FIG / (stem + '.png')).write_bytes((DECOMP2 / (stem + '.png')).read_bytes())
    CAPTIONS[key] = (stem, caption)


def xfig(key, stem, caption):
    """Register a figure already rendered to this build's own assets/
    directory (REBUILD-2: a static PNG conversion of an existing, gated
    figure asset -- see reports/research_story_build/assets/README, and
    beamer/figures/r6/fitext_r6_slide.pdf for the source the deck itself
    builds this from via make_slide_figures_r6.py)."""
    src = HERE / 'assets' / (stem + '.png')
    (FIG / (stem + '.png')).write_bytes(src.read_bytes())
    CAPTIONS[key] = (stem, caption)


def acceptedfig(key, stem, caption, data):
    """Register a reader rendering or accepted committed PNG without analysis."""
    (FIG / (stem + '.png')).write_bytes(data)
    CAPTIONS[key] = (stem, caption)


lfig('theory', 'theory_w1',
     r'**Own-set equal-consumption equivalents.** The theoretical W1 construction '
     r'from the companion theory paper. Individuals with preferences '
     r'$R_i,R_h$ and ability sets $A=\{j,k\}$ and $A^{\prime}=\{k,\ell\}$ '
     r'attain $z_i$ and $z_h$. For each individual, a common consumption level '
     r'is assigned to every job in their own set; the level at which the '
     r'preferred reference job becomes indifferent to the attained bundle is '
     r'the money metric. Adapted from Haydar and Maniquet (2026), work in '
     r'progress. This is the deterministic construction; the estimated measure '
     r'is its ex-ante extension, defined in Section 4.')
mfig('datapanel', 'figV08_data_panel',
     'Weighted distributions on the estimation samples: age, usual weekly '
     'hours among employed deciders, education, and the delivered hourly wage '
     'input. Observed inputs, not model predictions.')
mfig('resources', 'figV09_resources_panel',
     'Weighted distributions on the estimation samples: simulated disposable '
     'income at the observed job, children under twenty, the incidence of '
     'non-labour budget inputs by family, and urbanisation. Panel (a) is a '
     'tax-benefit output evaluated at the observed choice; panel (c) reports '
     'inputs to that calculation. The two are never added, and stocks are '
     'never summed with monthly flows.')
build_fitext_band()
xfig('fitband', 'fitext_band_v1',
     'Weighted extensive-margin accuracy against the model’s own '
     'simulated 95 per cent band (500 outcome vectors at the fitted '
     'estimates), restricted to groups whose statistic clears the pre-registered '
     'numerical-adequacy gate; single men do not clear it and are withheld. '
     'Observed and band values: coupled women 89.8% [88.7, 91.6]; single '
     'women 85.5% [80.8, 86.6]; coupled men 92.3% [89.2, 92.1]. '
     'Source: individual-level predictive diagnostics.')
acceptedfig(
    'nodeconvergence',
    'fig_posfit_predictive_integration_node_convergence_v1',
    'predictive/integration-node convergence. Weighted predicted participation '
    'over the fixed-seed integration-node subsets; the shaded area is '
    'the numerical 10--90 per cent envelope, and observed participation is the '
    'horizontal reference line.',
    final_surface.node_figure_png(),
)
acceptedfig(
    'ws4lambda',
    'ws4_sectionC_lambda_v1',
    'Leisure-normalisation evidence. Analytical reparameterisation '
    '(zero re-estimation) is distinguished from the subsequent independent '
    're-estimation of the four non-baseline normalisers.',
    final_surface.git_blob(
        final_surface.MNL_REPO, final_surface.WS4_REV,
        f'{final_surface.WS4_OUT}/ws4_sectionC_lambda_v1.png',
    ),
)
acceptedfig(
    'ws4time',
    'ws4_sectionC_T_v1',
    'Time-endowment sensitivity evidence. T=75 and T=90 are independent '
    're-estimations; T=80 is the baseline used as-is and was not '
    're-estimated.',
    final_surface.git_blob(
        final_surface.MNL_REPO, final_surface.WS4_REV,
        f'{final_surface.WS4_OUT}/ws4_sectionC_T_v1.png',
    ),
)
mfig('fit', 'figV06_fit_by_margin',
     'Observed against model population shares, margin by margin, for both '
     'estimated specifications. Model shares are population predictions '
     'computed by direct integration over the estimated opportunity '
     'distribution, not sampled-menu choice probabilities.')
# MEASURE-DEF-1: the 'lorenz'/'welfdist' figures (figV01/figV02) plotted the
# retired ex-ante measure's own distribution, against WD/ARM/SAMP, removed
# above with the report-only subsection that embedded them.
dfig('pabarch', 'fig_preseminar_pab_architecture_v1',
     'The eight P/A/B counterfactual coalitions, built from the estimated '
     'model by equalising household-constant covariates within a block. '
     'Node-level alternative characteristics are preserved in every '
     'coalition; only household-constant covariates are equalised. '
     'Preliminary, model-based.')
dfig('pabdecompsingles', 'fig_preseminar_pab_decomposition_singles_v1',
     'Single-adult estimation sample: coalition Gini levels and the exact '
     'Shapley allocation of $\\Delta I$ across P, A and B, with the sign '
     'instability of P annotated. Modified-OECD-equivalised $W^1_F$; Monte '
     'Carlo ranges over 1,000 replications, not confidence intervals. '
     'Preliminary, model-based.')
dfig('pabdecompcouples', 'fig_preseminar_pab_decomposition_couples_v1',
     'Couple estimation sample: coalition Gini levels and the exact Shapley '
     'allocation of $\\Delta I$ across P, A and B, with the sign instability '
     'of P annotated. Modified-OECD-equivalised $W^1_F$; Monte Carlo ranges '
     'over 1,000 replications, not confidence intervals. Preliminary, '
     'model-based.')
# MEASURE-DEF-1: the 'powermean' figure (figV07_power_mean) illustrated the
# retired ex-ante functional's power-moment contribution and marginal
# effect; removed with the WELFARE prose that embedded it -- the accepted
# W1_F closed form has no power-moment contribution to illustrate.
for _k, _stem, _cap in [
    ('prefsingles', 'figP01_indifference_curves_singles',
     'Indifference curves in consumption and leisure, single-adult '
     'households, at one representative household of each sex. The budget '
     'set, the opportunity density and the taste shock are not drawn, so a '
     'curve is not a set of attainable bundles. The consumption axis is '
     'logarithmic; under log consumption every finite utility target is '
     'attainable at a finite positive consumption, which may lie outside the '
     'plotted range.'),
    ('prefcouples', 'figP02_indifference_curves_couples',
     'Indifference curves in consumption and each spouse\u2019s leisure, '
     'couple households, with the partner\u2019s leisure held at its observed '
     'value. Conditional slices of a joint object, not attainable sets.'),
    ('marginal', 'figP03_marginal_utilities',
     'Marginal utility of consumption and of leisure in physical units, after '
     'the chain-rule conversion from the normalized coordinates. Levels are '
     'not comparable across separately estimated utility scales.'),
    ('mrs', 'figP04_mrs_by_age_sex',
     'Marginal rate of substitution between leisure and consumption, by age '
     'and sex, in euros per month per additional recurring weekly hour of '
     'leisure. A compensation along an indifference curve, not a behavioural '
     'response to a wage change.'),
    ('nat', 'figP05_euro_value_of_one_nat',
     'The euro value of one nat of utility under log consumption. The value '
     'is proportional rather than fixed: it rises with the consumption at '
     'which it is evaluated and has no single euro figure independent of a '
     'baseline.'),
    ('normalization', 'figP06_normalization_sensitivity',
     'Leisure-normalizer sensitivity. Under a change of normalizer the '
     'coefficients move by more than an order of magnitude while the '
     'indifference curves and the marginal rate of substitution coincide '
     'exactly. This is a coordinate change of the estimated model, not a '
     're-estimation, and it does not bear on whether a bound binds: '
     'reparameterization multiplies a coefficient and its box endpoint by the '
     'same factor.')]:
    lfig(_k, _stem, _cap)
# The matched-household illustration is deliberately NOT registered: it is
# rendered at the superseded consumption numeraire and would be a second
# generation of the model inside a document whose point is that there is one.


# =========================================================================== #
# 6.  RESOLUTION
# =========================================================================== #
PAPER_APPENDIX = []


def resolve(text, target):
    text = re.sub(r'\{\{table:(.*?)\}\}', lambda m: TABLES[m[1]], text)

    def fig(m):
        stem, cap = CAPTIONS[m[1]]
        path = ('figures/v5/' + stem + '.png' if target == 'paper'
                else str(FIG / (stem + '.png')).replace('\\', '/'))
        return '\n![%s](%s){width=95%%}\n' % (cap, path)
    text = re.sub(r'\{\{figure:(.*?)\}\}', fig, text)

    def strip(tag, keep):
        nonlocal text
        if keep:
            text = text.replace('{{%s}}' % tag, '').replace('{{/%s}}' % tag, '')
        else:
            text = re.sub(r'\{\{%s\}\}.*?\{\{/%s\}\}' % (tag, tag), '', text,
                          flags=re.S)
    strip('report-only', target == 'report')
    strip('paper-only', target == 'paper')
    text = re.sub(r'\{\{n:([^|}]+?)(?:\|([^}]+))?\}\}',
                  lambda m: val(m[1], m[2] or None), text)
    if '{{' in text:
        raise SystemExit('unresolved template near: %r'
                         % text[max(0, text.index('{{') - 90):
                                text.index('{{') + 90])
    return text


# =========================================================================== #
# 7.  BIBLIOGRAPHY
# =========================================================================== #
BIBEXTRA = r'''
@article{muehlhan2023,
 author={M{\"u}hlhan, Jannek},
 title={The German job miracle and its impact on income inequality: a decomposition study},
 journal={International Journal of Microsimulation},year={2023},volume={16},number={1},
 pages={28--64},doi={10.34196/ijm.00274}}
@techreport{creedyherault2011,
 author={Creedy, John and H{\'e}rault, Nicolas},
 title={Decomposing inequality and social welfare changes: the use of alternative welfare metrics},
 institution={Melbourne Institute of Applied Economic and Social Research},
 type={Working Paper},number={8/11},year={2011}}
@article{bargain2012,
 author={Bargain, Olivier},
 title={Back to the future: decomposition analysis of distributive policies using behavioural simulations},
 journal={International Tax and Public Finance},year={2012},volume={19},pages={708--731},
 doi={10.1007/s10797-011-9203-y}}
@article{jessen2019,
 author={Jessen, Robin},
 title={Why has income inequality in {G}ermany increased from 2002 to 2011? A behavioral microsimulation decomposition},
 journal={Review of Income and Wealth},year={2019},volume={65},number={3},pages={540--560},
 doi={10.1111/roiw.12397}}
@techreport{jiathoresen2021,
 author={Jia, Zhiyang and Thoresen, Thor O.},
 title={Welfare effects of tax policy change when there are choice restrictions on labour supply},
 institution={Statistics Norway, Research Department},type={Discussion Paper},
 number={959},year={2021}}
@incollection{owen1977,
 author={Owen, Guillermo},
 title={Values of games with a priori unions},
 booktitle={Mathematical Economics and Game Theory},editor={Henn, Rudolf and Moeschlin, Otto},
 publisher={Springer},address={Berlin},year={1977},pages={76--88},
 doi={10.1007/978-3-642-45494-3_7}}
@article{shorrocks1982,
 author={Shorrocks, Anthony F.},
 title={Inequality decomposition by factor components},
 journal={Econometrica},year={1982},volume={50},number={1},pages={193--211},
 doi={10.2307/1912537}}
@article{sastretrannoy2002,
 author={Sastre, Mercedes and Trannoy, Alain},
 title={Shapley inequality decomposition by factor components: some methodological issues},
 journal={Journal of Economics},year={2002},volume={77},number={S1},pages={51--89},
 doi={10.1007/BF03052500}}
@article{fleurbaeymaniquet2006,
 author={Fleurbaey, Marc and Maniquet, Fran{\c c}ois},
 title={Fair income tax},journal={The Review of Economic Studies},year={2006},
 volume={73},number={1},pages={55--83}}
@article{fleurbaeymaniquet2017,
 author={Fleurbaey, Marc and Maniquet, Fran{\c c}ois},
 title={Fairness and well-being measurement},journal={Mathematical Social Sciences},
 year={2017},volume={90},pages={119--126},doi={10.1016/j.mathsocsci.2017.02.005}}
@article{fleurbaeymaniquet2018,
 author={Fleurbaey, Marc and Maniquet, Fran{\c c}ois},
 title={Optimal income taxation theory and principles of fairness},
 journal={Journal of Economic Literature},year={2018},volume={56},number={3},
 pages={1029--1079},doi={10.1257/jel.20171238}}
@article{fleurbaeymaniquet2018ijet,
 author={Fleurbaey, Marc and Maniquet, Fran{\c c}ois},
 title={Inequality-averse well-being measurement},
 journal={International Journal of Economic Theory},year={2018},volume={14},number={1},
 pages={35--50},doi={10.1111/ijet.12140}}
@article{aaberge2018,
 author={Aaberge, Rolf and Colombino, Ugo},
 title={Structural labour supply models and microsimulation},
 journal={International Journal of Microsimulation},year={2018},volume={11},number={1},
 pages={162--197}}
@article{aaberge2004,
 author={Aaberge, Rolf and Colombino, Ugo and Str{\o}m, Steinar},
 title={Do more equal slices shrink the cake? An empirical investigation of tax-transfer reform proposals in {I}taly},
 journal={Journal of Population Economics},year={2004},volume={17},pages={767--785},
 doi={10.1007/s00148-004-0193-2}}
@techreport{capeau2021,
 author={Cap{\'e}au, Bart and De Sadeleer, Liebrecht and Maes, Sebastiaan and Decoster, Andr{\'e}},
 title={Nonparametric welfare analysis for discrete choice: levels and differences of individual and social welfare},
 institution={CESifo},type={Working Paper},number={9071},year={2021}}
@unpublished{haydarmaniquet,
 author={Haydar, Hisham and Maniquet, Fran{\c c}ois},
 title={Jobs and Well-Being Measurement},year={2026},note={Work in progress}}
'''
bib = (PAPER / 'JMP_working_paper_for_seminar_v2.bib').read_text('utf-8') + BIBEXTRA
BIB = PAPER / 'JMP_working_paper_for_seminar_v5.bib'
BIB.write_text(bib, encoding='utf-8')

# READER-VOICE-1: keep machine provenance in each generated surface without
# exposing internal workflow vocabulary to readers.  The paper receives TeX
# comments and the story report receives an HTML comment; both copies are
# deliberately identical so citation gates can inspect either block.
READER_VOICE_PROVENANCE = [
    'BEGIN READER-VOICE PROVENANCE',
    'Source-only provenance; excluded from rendered reader text.',
    ('Specifications: S11; artifact '
     's11_welfare_specs_of_record_v1.json; SHA-256 '
     '5FDC88502493CE540B088880EECF049BC268392FF3E8790FFE78A16AA6DDC884.'),
    ('Welfare definition: Mapping F; artifact JMP_W1_fork_ruling_v1.md; '
     'SHA-256 7F5D26857D8A96174A9924848F65A02611944273D7775FDC52DC82364A818C05.'),
    ('Welfare authorization: BASELINE-F-1 and E1; artifact '
     'JMP_W1_BASELINE_F1_authorization_and_Cobs_ruling_v1.md; SHA-256 '
     '54DFD886E41D0A89C1056CBEA5FA51E0A1294D3CA0813F938802BDC3DBD9EE0E.'),
    ('Welfare aggregates: artifact baseline_f1_verification_v1.md; MNL commit '
     '6048c9f7; independent verification b5550af5; SHA-256 '
     'DA7BADF639F3D502D47B301558453D76501C9C44033ECE3F17BDE350BFD5E55F.'),
    ('Equivalised reporting: E3-EQ; artifact '
     'JMP_BASELINE_F1_equivalised_reporting_v1.md; commit 4c4e07e; SHA-256 '
     'DACD34B593D0E676AC802779960DBB4F4BDC32A462C26F8852D56C9D4C95A669.'),
    ('Predictive diagnostics: POSFIT v3; repository MNL_posfit; branch '
     'diagnostics/posfit-v3; commit 96693269; artifact run_provenance.json; '
     'SHA-256 BDC3722C325FF8A27BE719AA52A741DF7BEEF9515B4A63554C65E8769EB7F40B.'),
    ('Bounded decomposition: DECOMP-2; repository MNL_decomp; branch '
     'welfare/preseminar-pab; commit b52761b4; artifact '
     'preseminar_pab_record_v1.json; SHA-256 '
     'BCBE4B6FC742DAA39535D5C3EB03BDA0641055A9F5E851B4F53F62FA3E612011.'),
    ('Leisure scaling: WS4; commit 5a8e6bba; artifacts '
     'ws4_sectionC_lambda_v1.png and ws4_sectionC_T_v1.png.'),
    'END READER-VOICE PROVENANCE',
]

# =========================================================================== #
# 8.  ASSEMBLY
# =========================================================================== #
report = ('# ' + TITLE + '\n\nHisham Haydar \u00b7 University of Luxembourg '
          'and LISER\n\nBuild date: ' + today + '.\n\n## Abstract\n\n'
          + resolve(ABSTRACT, 'report') + '\n\n*' + PRELIM_NOTE + '*\n')
paper = ('\\begin{abstract}\n' + resolve(ABSTRACT, 'paper')
         + '\n\\end{abstract}\n\n*' + PRELIM_NOTE + '*\n\n')

_n = 0
for sec in SECTIONS:
    if sec.get('report', True):
        _n += 1
        report += '\n# %d. %s\n' % (_n, sec['title'])
        report += resolve(sec['body'], 'report')

_started_appendix = False
for sec in SECTIONS:
    if not sec.get('paper', True):
        continue
    if sec.get('appendix') and not _started_appendix:
        paper += '\n\\appendix\n'
        _started_appendix = True
    paper += '\n# %s\n' % sec['title']
    paper += resolve(sec['body'], 'paper')

report += '\n# Questions for presentation preparation\n'
for i, (q, a) in enumerate(QA, 1):
    report += '\n## %d. %s\n\n%s\n' % (i, q, resolve(a, 'report'))
report += '\n# Bibliography\n\n::: {#refs}\n:::\n'
(HERE / 'story_v5.generated.md').write_text(report, encoding='utf-8')

header = (r'''\documentclass[11pt,a4paper]{article}
\usepackage[margin=25mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern,amsmath,amssymb,booktabs,longtable,array,graphicx,calc}
\usepackage{ragged2e}
\usepackage{needspace}
\usepackage{float}
\raggedbottom
% Float discipline. The panel figures are about 0.43\textheight each, so the
% default allowance of several top floats lets two of them plus a long-captioned
% table exceed the page and produce an overfull vbox in the output routine.
\setcounter{topnumber}{1}
\setcounter{bottomnumber}{1}
\setcounter{totalnumber}{2}
\renewcommand{\topfraction}{0.6}
\renewcommand{\bottomfraction}{0.4}
\renewcommand{\textfraction}{0.12}
\renewcommand{\floatpagefraction}{0.7}
\usepackage{xurl}
\usepackage[round]{natbib}
\usepackage[colorlinks=true,allcolors=blue]{hyperref}
\usepackage{bookmark}
\usepackage{caption}
\captionsetup{font=small,labelfont=bf}
\setlength{\emergencystretch}{3em}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\providecommand{\pandocbounded}[1]{#1}
\title{''' + TITLE + r'''}
\author{Hisham Haydar\\University of Luxembourg and LISER}
\date{Build: ''' + today + r'''\\Discussion draft}
\begin{document}
\maketitle
''')
body = pypandoc.convert_text(
    paper, 'latex', format='markdown+raw_tex+tex_math_dollars',
    extra_args=['--natbib', '--wrap=none']).replace('\r\n', '\n')
body = body.replace(r'\def\LTcaptype{none}', '')
# Figures are pinned where they are written rather than floated. longtable
# mis-accounts the remaining page height when a float shares the page, which
# clipped the last rows of a table and, on one page, a whole paragraph. With
# every figure placed in sequence the page breaking is correct, and \raggedbottom
# absorbs the slack.
body = body.replace(r'\begin{figure}', r'\begin{figure}[H]')


def wrap_table(m):
    n = len(m[1])
    first = .155 if n == 7 else (.25 if n >= 4 else .42)
    # Leave room for 2*tabcolsep per column. A residual 0.12154pt overfull
    # survives on wide tables regardless of these widths: it is pandoc's
    # longtable rule geometry, is 0.04 mm, and check_v5_pdf_layout.py
    # confirms no ink crosses the margin.
    total = .98 - .014 * n
    widths = [first] + [(total - first) / (n - 1)] * (n - 1)
    return (r'\begin{longtable}[]{@{}'
            # \RaggedRight, not \raggedright: the latter carries infinite
            # glue shrinkage, and longtable splitting a page inside such a cell
            # produces an overfull vbox that runs past the bottom margin.
            + ''.join(r'>{\RaggedRight\arraybackslash}p{' + f'{w:.4f}'
                      + r'\linewidth}' for w in widths) + r'@{}}')


body = re.sub(r'\\begin\{longtable\}\[\]\{@\{\}([lrc]+)@\{\}\}', wrap_table, body)
# \Needspace forces the page to break BEFORE a table when too little room is
# left: pandoc's longtable keeps its caption and header together in one
# unbreakable chunk, and starting that chunk near the foot of a page is what
# produced the overfull vbox that ran past the bottom margin.
body = body.replace(
    r'\begin{longtable}',
    r'\Needspace*{12\baselineskip}\small\setlength{\tabcolsep}{3pt}'
    r'\begin{longtable}')
_tex_provenance = '\n'.join('% ' + line for line in READER_VOICE_PROVENANCE)
tex = (header + body + '\n\\bibliographystyle{plainnat}\n'
       '\\bibliography{JMP_working_paper_for_seminar_v5}\n'
       + _tex_provenance + '\n\\end{document}\n')
(PAPER / 'JMP_working_paper_for_seminar_v5.tex').write_text(tex, encoding='utf-8')

# ---- the HTML report ------------------------------------------------------ #
rendered = pypandoc.convert_text(
    report, 'html5', format='markdown+tex_math_dollars',
    extra_args=['--mathjax', '--citeproc', '--bibliography=' + str(BIB),
                '--wrap=none']).replace('\r\n', '\n')


def embed(m):
    p = Path(html.unescape(m[1]))
    return ('src="data:image/png;base64,'
            + base64.b64encode(p.read_bytes()).decode()
            + '" data-fig="' + p.stem + '"')


rendered = re.sub(r'src="([^"]+\.png)"', embed, rendered)
# tables scroll inside their own container rather than overflowing the viewport
rendered = re.sub(r'<table', '<div class="tw"><table', rendered)
rendered = re.sub(r'</table>', '</table></div>', rendered)
# Scientific history and the notebook description stay available but outside the
# main reading flow. The heading is KEPT so the section still has an anchor and
# a table-of-contents entry; only its body collapses.
for _h in [s['title'] for s in SECTIONS if s.get('collapse')]:
    _pat = (r'(<h1[^>]*>[\d.\s]*' + re.escape(_h) + r'</h1>)(.*?)(?=<h1|\Z)')
    rendered = re.sub(
        _pat, lambda m: (m[1] + '<details><summary>Show this section</summary>'
                         + m[2] + '</details>'), rendered, flags=re.S)

vendor = HERE / 'vendor/tex-svg.js'
vendor.parent.mkdir(exist_ok=True)
if not vendor.exists():
    urllib.request.urlretrieve(
        'https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-svg.js', vendor)
mathjax = vendor.read_text('utf-8')

css = (":root{--ink:#1a1a1a;--mut:#5a5f66;--line:#dcdfe4;--bg:#fff;"
       "--soft:#f6f7f9;--accent:#1f4e79;--accent2:#7a3b12}"
       "*{box-sizing:border-box}"
       "body{margin:0;background:var(--bg);color:var(--ink);"
       "font:17px/1.62 Georgia,'Iowan Old Style','Times New Roman',serif}"
       "#wrap{display:flex;align-items:flex-start;max-width:1500px;margin:0 auto}"
       "#toc{position:sticky;top:0;flex:0 0 306px;height:100vh;overflow-y:auto;"
       "padding:22px 16px 60px 20px;border-right:1px solid var(--line);"
       "background:var(--soft);font-family:-apple-system,BlinkMacSystemFont,"
       "'Segoe UI',Roboto,sans-serif;font-size:13px;line-height:1.45}"
       "#toc h2{font-size:11px;letter-spacing:.14em;text-transform:uppercase;"
       "color:var(--mut);margin:0 0 12px;font-weight:700;border:0;padding:0}"
       "#toc a{display:block;padding:4px 8px;color:var(--ink);"
       "text-decoration:none;border-radius:4px;border-left:2px solid transparent}"
       "#toc a:hover{background:#e9ecf1}"
       "#toc a.sub{padding-left:20px;color:var(--mut);font-size:12px}"
       "#toc a.on{background:#e3eaf3;border-left-color:var(--accent);"
       "font-weight:600}"
       "#doc{flex:1 1 auto;min-width:0;padding:34px 52px 140px;max-width:1020px}"
       "h1{font-size:27px;line-height:1.24;margin:2.2em 0 .35em;padding-top:.4em;"
       "border-top:2px solid var(--ink);letter-spacing:-.01em}"
       "h1:first-of-type{margin-top:.2em;border-top:0}"
       "h2{font-size:20px;margin:1.7em 0 .4em;color:var(--accent);line-height:1.3}"
       "h3{font-size:16.5px;margin:1.4em 0 .3em;font-family:-apple-system,"
       "BlinkMacSystemFont,'Segoe UI',sans-serif}"
       "p{margin:.62em 0}ul,ol{margin:.55em 0 .55em 0;padding-left:1.35em}"
       "li{margin:.28em 0}"
       "figure{margin:2em 0}img{max-width:100%;height:auto}"
       "figcaption{font:14px/1.55 -apple-system,BlinkMacSystemFont,'Segoe UI',"
       "sans-serif;color:var(--mut);margin-top:.5em}"
       ".tw{overflow-x:auto;margin:1.5em 0;-webkit-overflow-scrolling:touch}"
       "table{border-collapse:collapse;width:100%;min-width:520px;"
       "font:13.5px/1.5 -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}"
       "td,th{padding:8px 9px;border-bottom:1px solid var(--line);"
       "text-align:left;vertical-align:top}th{background:#eef3f5}"
       ".math.display{display:block;overflow-x:auto;margin:1.6em 0}"
       "code{overflow-wrap:anywhere;font-size:.85em;background:var(--soft);"
       "padding:1px 4px;border-radius:3px}"
       "blockquote{margin:1.1em 0;padding:13px 17px;border:1px solid #c9d8e8;"
       "border-left:3px solid var(--accent);border-radius:6px;background:#eef3f8}"
       "blockquote p{margin:.3em 0}"
       "details{margin:2em 0;padding:16px 18px;background:var(--soft);"
       "border:1px solid var(--line);border-radius:6px}"
       "summary{font-weight:700;cursor:pointer;font-family:-apple-system,"
       "BlinkMacSystemFont,'Segoe UI',sans-serif}"
       "#refs div{margin:.7em 0;padding-left:1.6em;text-indent:-1.6em}"
       "a{color:var(--accent)}"
       "@media(max-width:1100px){#wrap{display:block}#toc{position:static;"
       "height:auto;width:auto;flex:none;border-right:0;"
       "border-bottom:1px solid var(--line)}#doc{padding:24px 20px 80px}}"
       "@media print{#toc{display:none}#doc{max-width:none;padding:0}"
       "body{font-size:11pt}details{display:block}}")

_nav = []
_seen: dict = {}


def _slug(t):
    b = re.sub(r'[^a-z0-9]+', '-', re.sub(r'<[^>]+>', '', t).lower()).strip('-')[:60] or 'sec'
    _seen[b] = _seen.get(b, 0) + 1
    return b if _seen[b] == 1 else '%s-%d' % (b, _seen[b])


def _anchor(m):
    lvl, inner = m[1], m[2]
    sid = _slug(inner)
    _nav.append((lvl, sid, re.sub(r'<[^>]+>', '', inner)))
    return '<h%s id="%s">%s</h%s>' % (lvl, sid, inner, lvl)


rendered = re.sub(r'<h([12])[^>]*>(.*?)</h\1>', _anchor, rendered, flags=re.S)
toc_html = '<h2>Contents</h2>' + ''.join(
    '<a class="%s" href="#%s">%s</a>' % ('' if l == '1' else 'sub', sid, txt)
    for l, sid, txt in _nav)

_html_provenance = ('<!--\n' + '\n'.join(READER_VOICE_PROVENANCE)
                    + '\n-->')
htmlout = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
           '<meta name="viewport" content="width=device-width,initial-scale=1">'
           '<title>' + TITLE + '</title><style>' + css + '</style>'
           '<script>window.MathJax={tex:{inlineMath:[["\\\\(","\\\\)"]],'
           'displayMath:[["\\\\[","\\\\]"]]},svg:{fontCache:"local"},'
           'options:{enableMenu:false}};</script><script>' + mathjax
           + '</script></head><body><div id="wrap"><nav id="toc">' + toc_html
           + '</nav><main id="doc">' + rendered + '</main></div>'
           '<script>(function(){var ls=[].slice.call('
           'document.querySelectorAll("#toc a")),'
           'hs=ls.map(function(a){return document.getElementById('
           'a.getAttribute("href").slice(1));});'
           'function on(){var y=scrollY+120,k=0;hs.forEach(function(h,i){'
           'if(h&&h.offsetTop<=y)k=i;});ls.forEach(function(a,i){'
           'a.className=a.className.replace(/ ?on/,"")+(i===k?" on":"");});}'
           'addEventListener("scroll",on,{passive:true});on();})();</script>'
           + _html_provenance +
           '</body></html>')
(ROOT / 'reports/JMP_research_story_report_v5.html').write_text(
    htmlout, encoding='utf-8')

_existing_register = json.loads((ROOT / 'reports/numbers_of_record_v5.json').read_text('utf-8'))
# The discussion notebook consumes these registered, reader-facing tables.
# Preserve them when the story builder refreshes its own scalar register.  The
# one-time fallback repairs an older story-only register from the committed
# baseline; subsequent builds preserve the live copy.
if ('discussion_tables' not in _existing_register
        or 'n_predecessor_singles' not in _existing_register.get('entries', {})):
    _baseline = subprocess.check_output(
        ['git', '-C', str(ROOT), 'show', 'HEAD:reports/numbers_of_record_v5.json'],
        text=True, encoding='utf-8')
    _existing_register = json.loads(_baseline)

_gallery_keys = {
    'registered_for', 'sample_funnel', 'descriptives', 'observed_margins',
    'occupation', 'coefficients', 'fit', 'wage_quantile_fit',
    'opportunity_examples',
}
_current_gallery = _existing_register.get('gallery') or {}
_current_gallery = {k: v for k, v in _current_gallery.items()
                    if k in _gallery_keys}

REGOUT = {'build_date': today,
          'model_of_record': 'S11 specifications of record: tau = 1, '
                             'theta_c = 0, beta_c estimated; accepted literal '
                             'Mapping-F baseline on the 1,540 / 2,223 frames',
          # 'entries' is REG alone, not merged with the predecessor file's
          # entries: merging silently carried forward orphaned keys from
          # retired sources (w_i00_singles, cr1_lo_*, resid_top, ...) even
          # after this script stopped registering them, which is exactly
          # the "filled with a predecessor value" this module's own
          # docstring says never happens. REG is a complete, fresh
          # registration from this run (verified: every {{n:...}} token the
          # resolve() pass needs is already satisfied from REG alone, or
          # the build raises "unregistered number" and does not reach here).
          'entries': dict(REG), 'used_keys': sorted(USED),
          'unused_keys': sorted(set(REG) - USED),
          # Preserve only the fields consumed by the rebuilt current gallery.
          # In particular, never carry the retired I00/I10/I01/I11 examples
          # back into its registry when this shared builder is rerun.
          'gallery': _current_gallery,
          'discussion_tables': _existing_register['discussion_tables']}
(ROOT / 'reports/numbers_of_record_v5.json').write_text(
    json.dumps(REGOUT, indent=2, ensure_ascii=False), encoding='utf-8')
print('v5: %d registered numbers, %d used; paper and report written.'
      % (len(REG), len(USED)))
