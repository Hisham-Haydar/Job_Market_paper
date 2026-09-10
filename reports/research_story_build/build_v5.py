"""Build the v5 paper and the v5 research report from one source of prose,
numbers, tables and figures.

v5 is a source-reconciled rewrite, not a patch layer over v4.  Every empirical
token resolves against an artifact produced by the S11 specifications of record
(tau = 1, exact log consumption, estimated consumption weight) or the S12
welfare record on the 1,540 / 2,223 estimation frames.  A token with no source
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
import urllib.request
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402
import pypandoc  # noqa: E402

from v5_sections import TITLE, ABSTRACT, PRELIM_NOTE, SECTIONS, QA  # noqa: E402

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
MNL = ROOT.parent / 'MNL'
SPRINT = MNL / 'experiments/JMP_SEMINAR_SPRINT'
S11 = SPRINT / 'runs/s11_welfare_specs_of_record'
S12 = SPRINT / 'runs/s12_welfare_record'
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
register('pm_weight_double',
         round(2.0 ** REG['beta_c_singles']['value'], 2), _S11SRC, 'derived',
         'contribution to the power moment, relative to the median alternative')

# =========================================================================== #
# 3.  THE WELFARE RECORD (S12) AND ITS INTERVALS
# =========================================================================== #
_S12SRC = ('s12_six_index_attributions_v1.csv; corrected welfare record at the '
           'S11 specifications of record')
SIX = pd.read_csv(S12 / 's12_six_index_attributions_v1.csv')
LEV = pd.read_csv(V5 / 'v5_six_index_levels_v1.csv')
OF = pd.read_csv(V5 / 'v5_one_factor_vs_shapley_v1.csv')
WD = pd.read_csv(V5 / 'v5_welfare_distributions_v1.csv')
CR1 = pd.read_csv(S12 / 's12_s11_cr1_headline_shares_v1.csv')
ARM = {'singles': 'singles_female', 'couples': 'household-own',
       'singlesmz': 'singles_male_structural_zero'}
SAMP = {'singles': 'singles', 'singlesmz': 'singles', 'couples': 'couples'}
INDICES = [('gini', 'Gini'), ('atkinson1', 'Atkinson(1)'),
           ('atkinson2', 'Atkinson(2)'), ('ge0', 'GE(0)'), ('ge1', 'GE(1)'),
           ('cv2', r'GE(2) $=CV^2/2$')]
COMPS = [('P', 'Preferences'), ('A', 'Job access'),
         ('B', 'Earning opportunities'),
         ('AB', 'Market opportunities (A + B)'),
         ('D', 'Resources and needs'),
         ('E', 'All non-preference circumstances')]


def sixrow(tag, basis, index):
    m = SIX[(SIX['sample'] == SAMP[tag]) & (SIX['reference'] == ARM[tag])
            & (SIX['basis'] == basis) & (SIX['index'] == index)]
    if len(m) != 1:
        raise SystemExit('s12 row not unique: %r' % ((tag, basis, index),))
    return m.iloc[0]


for _tag in ['singles', 'singlesmz', 'couples']:
    for _ix, _ in INDICES:
        r = sixrow(_tag, 'raw', _ix)
        base = float(r['I00'])
        if _ix == 'gini':
            for st in ['I00', 'I10', 'I01', 'I11']:
                register('w_%s_%s' % (st.lower(), _tag), float(r[st]),
                         _S12SRC, 'result', 'index units')
        for comp, _ in COMPS:
            v = r['C_' + comp]
            if pd.isna(v):
                continue
            register('w_c%s_%s_%s' % (comp, _ix, _tag), float(v), _S12SRC,
                     'result', 'index points')
            register('w_sh%s_%s_%s' % (comp, _ix, _tag),
                     round(100.0 * float(v) / base, 2), _S12SRC, 'result',
                     'per cent of that index baseline')
        register('w_base_%s_%s' % (_ix, _tag), float(base), _S12SRC, 'result',
                 'index level')
# short aliases for the Gini, the headline index
for _tag in ['singles', 'singlesmz', 'couples']:
    for comp, _ in COMPS:
        k = 'w_sh%s_gini_%s' % (comp, _tag)
        if k in REG:
            register('w_sh%s_%s' % (comp, _tag), REG[k]['value'], _S12SRC,
                     'result', 'per cent of the baseline Gini')
            register('w_c%s_%s' % (comp, _tag),
                     REG['w_c%s_gini_%s' % (comp, _tag)]['value'], _S12SRC,
                     'result', 'Gini points')

# one-factor effects, the two-group game
for _tag in ['singles', 'couples']:
    m = OF[(OF['sample'] == SAMP[_tag]) & (OF['reference'] == ARM[_tag])
           & (OF['basis'] == 'raw') & (OF['index'] == 'gini')].iloc[0]
    register('of_P_' + _tag, round(float(m['one_factor_P_pct']), 2),
             'v5_one_factor_vs_shapley_v1.csv', 'result',
             'per cent reduction in the baseline Gini')
    register('of_E_' + _tag, round(float(m['one_factor_E_pct']), 2),
             'v5_one_factor_vs_shapley_v1.csv', 'result',
             'per cent reduction in the baseline Gini')
    register('of_P_rise_' + _tag, abs(round(float(m['one_factor_P_pct']), 1)),
             'v5_one_factor_vs_shapley_v1.csv', 'result',
             'per cent change in the baseline Gini, sign in the text')

# CR1 parameter intervals on the headline shares
for _, r in CR1.iterrows():
    tag = 'singles' if r['sample'] == 'singles' else 'couples'
    if r['basis'] != 'raw':
        continue
    comp = r['share'].replace('share_', '')
    register('cr1_lo_%s_%s' % (comp, tag), round(100.0 * float(r['CR1_p2_5']), 1),
             's12_s11_cr1_headline_shares_v1.csv', 'interval',
             'per cent, 2.5th parameter percentile')
    register('cr1_hi_%s_%s' % (comp, tag), round(100.0 * float(r['CR1_p97_5']), 1),
             's12_s11_cr1_headline_shares_v1.csv', 'interval',
             'per cent, 97.5th parameter percentile')
    register('rq_lo_%s_%s' % (comp, tag), round(100.0 * float(r['RQMC_lo']), 1),
             's12_s11_cr1_headline_shares_v1.csv', 'band',
             'per cent, RQMC integration band')
    register('rq_hi_%s_%s' % (comp, tag), round(100.0 * float(r['RQMC_hi']), 1),
             's12_s11_cr1_headline_shares_v1.csv', 'band',
             'per cent, RQMC integration band')

# ---- the couples subdivision of D, repriced --------------------------------
# This landed after the v5 brief was written, which assumed it did not exist.
# It is a real repricing of two counterfactual panels at the S11 specification,
# not an imputed split, and it carries its own identity gate.
_ND = pd.read_csv(S12 / 's12_couples_nested_D_attributions_v1.csv')
_NDJ = json.loads((S12 / 's12_couples_nested_D_attributions_v1.json')
                  .read_text('utf-8'))
_NDSRC = ('s12_couples_nested_D_attributions_v1.csv; two repriced '
          'counterfactual panels at the S11 specification of record')
if _NDJ['status'] != 'S12_COUPLES_NESTED_D_COMPLETE' or not _NDJ['gates']['PASS']:
    raise SystemExit('the couples nested-D artifact is not a passing complete '
                     'run; v5 must not report a split from it')
for _ix, _ in INDICES:
    r = _ND[(_ND['basis'] == 'raw') & (_ND['index'] == _ix)]
    if len(r) != 1:
        raise SystemExit('couples nested-D row not unique: %s' % _ix)
    r = r.iloc[0]
    for comp, col in [('res', 'C_nonlabour'), ('comp', 'C_composition')]:
        register('nd_c%s_%s' % (comp, _ix), float(r[col]), _NDSRC, 'result',
                 'index points')
        register('nd_sh%s_%s' % (comp, _ix),
                 round(100.0 * float(r[col]) / float(r['I00']), 2), _NDSRC,
                 'result', 'per cent of that index baseline')
    # the share of the CHANNEL, which is what the two cells divide
    tot = float(r['C_needs_total'])
    register('nd_chres_%s' % _ix, round(100.0 * float(r['C_nonlabour']) / tot, 1),
             _NDSRC, 'result', 'per cent of the resources-and-needs channel')
    register('nd_chcomp_%s' % _ix,
             round(100.0 * float(r['C_composition']) / tot, 1), _NDSRC,
             'result', 'per cent of the resources-and-needs channel')
    re_ = _ND[(_ND['basis'] == 'modified_OECD_equivalized')
              & (_ND['index'] == _ix)].iloc[0]
    tote = float(re_['C_needs_total'])
    register('nde_chres_%s' % _ix,
             round(100.0 * float(re_['C_nonlabour']) / tote, 1), _NDSRC,
             'result', 'per cent of the channel, equivalized')
    register('nde_chcomp_%s' % _ix,
             round(100.0 * float(re_['C_composition']) / tote, 1), _NDSRC,
             'result', 'per cent of the channel, equivalized')
for comp in ['res', 'comp']:
    register('nd_c%s' % comp, REG['nd_c%s_gini' % comp]['value'], _NDSRC,
             'result', 'Gini points')
    register('nd_sh%s' % comp, REG['nd_sh%s_gini' % comp]['value'], _NDSRC,
             'result', 'per cent of the baseline Gini')
    register('nd_ch%s' % comp, REG['nd_ch%s_gini' % comp]['value'], _NDSRC,
             'result', 'per cent of the resources-and-needs channel')
    register('nde_ch%s' % comp, REG['nde_ch%s_gini' % comp]['value'], _NDSRC,
             'result', 'per cent of the channel, equivalized')

# ---- the same subdivision for single adults --------------------------------
# The current singles record includes the corrected resources/composition split.
_SD = ('s12_six_index_attributions_v1.csv; corrected singles nested-D '
       'attribution on repriced partial-D panels')
for _ix, _ in INDICES:
    for _bas, _pfx in [('raw', 'sd'), ('equivalized', 'sde')]:
        r = sixrow('singles', _bas, _ix)
        tot = float(r['C_D'])
        for comp, col in [('res', 'C_resources'), ('comp', 'C_composition')]:
            v = float(r[col])
            register('%s_c%s_%s' % (_pfx, comp, _ix), v, _SD, 'diagnostic',
                     'index points')
            register('%s_sh%s_%s' % (_pfx, comp, _ix),
                     round(100.0 * v / float(r['I00']), 2), _SD, 'diagnostic',
                     'per cent of that index baseline')
            register('%s_ch%s_%s' % (_pfx, comp, _ix),
                     round(100.0 * v / tot, 1), _SD, 'diagnostic',
                     'per cent of the resources-and-needs channel')
for comp in ['res', 'comp']:
    for _pfx in ['sd', 'sde']:
        for _kind in ['sh', 'ch']:
            register('%s_%s%s' % (_pfx, _kind, comp),
                     REG['%s_%s%s_gini' % (_pfx, _kind, comp)]['value'], _SD,
                     'diagnostic', 'per cent')

# How robust is each nested statement? Counted, not asserted.
_nd_res_leads = sum(1 for _ix, _ in INDICES
                    if REG['nd_chres_%s' % _ix]['value'] > 50)
_sd_res_leads = sum(1 for _ix, _ in INDICES
                    if REG['sd_chres_%s' % _ix]['value'] > 50)
_sde_res_leads = sum(1 for _ix, _ in INDICES
                     if REG['sde_chres_%s' % _ix]['value'] > 50)
_nde_res_leads = sum(1 for _ix, _ in INDICES
                     if REG['nde_chres_%s' % _ix]['value'] > 50)
_comp_bigger_for_couples = sum(
    1 for _ix, _ in INDICES
    if REG['nd_chcomp_%s' % _ix]['value'] > REG['sd_chcomp_%s' % _ix]['value'])
_equiv_raises_comp = sum(
    1 for _ix, _ in INDICES
    if REG['nde_chcomp_%s' % _ix]['value'] > REG['nd_chcomp_%s' % _ix]['value']
    and REG['sde_chcomp_%s' % _ix]['value'] > REG['sd_chcomp_%s' % _ix]['value'])
for _k, _v, _u in [('nd_res_leads_couples', _nd_res_leads, 'indices of six'),
                   ('nd_res_leads_singles', _sd_res_leads, 'indices of six'),
                   ('nd_res_leads_couples_eq', _nde_res_leads, 'indices of six'),
                   ('nd_res_leads_singles_eq', _sde_res_leads, 'indices of six'),
                   ('nd_comp_bigger_couples', _comp_bigger_for_couples,
                    'indices of six'),
                   ('nd_equiv_raises_comp', _equiv_raises_comp,
                    'indices of six')]:
    register(_k, _v, 'counted over the six index-specific nested attributions',
             'result', _u)
register('nd_resid', '1.4e-17', _NDSRC, 'verified identity', 'index units')
register('nd_vs_cd', '0.0', _NDSRC, 'verified identity', 'index units')
for _k, _v in [('nd_n_res', _NDJ['partition']['resources']),
               ('nd_n_comp', _NDJ['partition']['composition']),
               ('nd_n_geo', _NDJ['partition']['geography'])]:
    register(_k, int(_v), _NDSRC, 'definition', 'budget fields')
_r = _ND[(_ND['basis'] == 'raw') & (_ND['index'] == 'gini')].iloc[0]
register('nd_of_res', round(100.0 * float(_r['one_factor_nonlabour_fall'])
                            / float(_r['I00']), 2), _NDSRC, 'result',
         'per cent reduction in the baseline Gini')
register('nd_of_comp', round(100.0 * float(_r['one_factor_composition_fall'])
                             / float(_r['I00']), 2), _NDSRC, 'result',
         'per cent reduction in the baseline Gini')

# welfare levels
for _tag in ['singles', 'couples']:
    for basis in ['raw', 'equivalized']:
        r = WD[(WD['sample'] == SAMP[_tag]) & (WD['reference'] == ARM[_tag])
               & (WD['basis'] == basis) & (WD['state'] == 'I00')].iloc[0]
        for stat in ['mean_weighted', 'median', 'p10', 'p90']:
            register('wl_%s_%s_%s' % (stat.split('_')[0], basis, _tag),
                     round(float(r[stat]), 0),
                     'v5_welfare_distributions_v1.csv', 'result', 'EUR/month')
        register('wl_gini_%s_%s' % (basis, _tag),
                 round(float(r['gini_weighted']), 6),
                 'v5_welfare_distributions_v1.csv', 'result', 'Gini units')
for _tag in ['singles', 'couples']:
    o = _EVID['lorenz_observed_income']['%s|raw' % SAMP[_tag]]
    register('inc_gini_' + _tag, round(float(o['gini_weighted']), 6),
             'v5_step2_welfare_evidence_v1.json::lorenz_observed_income',
             'result', 'Gini units')

# exhaustiveness, neutrality, W3, bridge
for _k, _v, _u in [('resid_top', '2.8e-17', 'index units'),
                   ('resid_nested', '5.6e-17', 'index units'),
                   ('i11_max', '1.3e-15', 'index units')]:
    register(_k, _v, 's12_welfare_record_report_v1.md::Exhaustiveness',
             'verified identity', _u)
for _k, _v, _s, _u in [
        ('dlogh_singles', '1.8e-15', 'verified identity', 'log units'),
        ('dlogh_couples', '7.1e-15', 'verified identity', 'log units'),
        ('direct_median', 0, 'result', 'EUR/month'),
        ('attain_median_singles', -17.43, 'result', 'EUR/month'),
        ('attain_median_couples', 110.53, 'result', 'EUR/month')]:
    register(_k, _v, 's12_welfare_record_report_v1.md::Wage-density neutrality',
             _s, _u)
_BR = _EVID['w1_w4_bridge']
for _t in ['singles', 'couples']:
    b = _BR[_t]
    register('gint_med_' + _t, round(b['ghat_integral_on_H_domain']['median'], 6),
             's12_w4_premise_audit_v1.json', 'diagnostic',
             'opportunity mass on the H domain')
    register('w41_med_' + _t,
             round(b['unit_mass_corrected_bridge']['W4_over_W1']['median'], 4),
             's12_w4_premise_audit_v1.json', 'result',
             'ratio after unit-mass normalization')
    register('w41_min_' + _t,
             round(b['unit_mass_corrected_bridge']['W4_over_W1']['min'], 4),
             's12_w4_premise_audit_v1.json', 'result', 'ratio')
    register('w41_max_' + _t,
             round(b['unit_mass_corrected_bridge']['W4_over_W1']['max'], 4),
             's12_w4_premise_audit_v1.json', 'result', 'ratio')
    register('delta_med_' + _t,
             round(b['unit_mass_corrected_bridge']['Delta_nats']['median'], 4),
             's12_w4_premise_audit_v1.json', 'result', 'nats')
for _k, _v, _u in [('w3_bracketed_singles', 1540, 'households'),
                   ('w3_bracketed_couples', 9, 'households'),
                   ('w3_negative_couples', 2103, 'households')]:
    register(_k, _v, 's12_welfare_record_report_v1.md::W3', 'diagnostic', _u)

# the exact multi-index counts the review requires
_RK = _EVID['ranking_statements']
for _t in ['singles', 'couples']:
    for _k in ['A_gt_B', 'B_gt_A', 'A_gt_D', 'AB_gt_D', 'D_largest_of_PABD',
               'P_negative', 'P_positive']:
        register('rk_%s_%s' % (_k.lower(), _t), len(_RK[_t][_k]),
                 'v5_step2_welfare_evidence_v1.json::ranking_statements',
                 'result', 'indices out of six')

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

# ---- T10: welfare levels -------------------------------------------------- #
_rows = []
for tag in ['singles', 'couples']:
    for basis in ['raw', 'equivalized']:
        r = WD[(WD['sample'] == SAMP[tag]) & (WD['reference'] == ARM[tag])
               & (WD['basis'] == basis) & (WD['state'] == 'I00')].iloc[0]
        _rows.append([{'singles': 'Single-adult', 'couples': 'Couple'}[tag],
                      {'raw': 'Household', 'equivalized': 'Equivalized'}[basis],
                      format(float(r['mean_weighted']), ',.0f'),
                      format(float(r['p10']), ',.0f'),
                      format(float(r['median']), ',.0f'),
                      format(float(r['p90']), ',.0f'),
                      format(float(r['gini_weighted']), '.4f')])
    _rows.append([{'singles': 'Single-adult', 'couples': 'Couple'}[tag],
                  'Priced disposable income', '--', '--', '--', '--',
                  format(REG['inc_gini_' + tag]['value'], '.4f')])
TABLES['levels'] = table(
    'v5_welfare_levels',
    'Table: The distribution of money-metric well-being, and the priced '
    'disposable income it replaces. Levels are in euros per month of '
    'equivalent flat consumption, weighted. Levels are not comparable between '
    'the two household types: each type carries its own reference '
    'construction, and the Gini of the money metric and the Gini of income are '
    'not two estimates of one quantity.',
    ['Population', 'Basis', 'Mean', 'p10', 'Median', 'p90', 'Gini'], _rows)

# ---- T11: the four states and the one-factor effects ---------------------- #
_rows = []
for lab, st in [('Own preferences, own circumstances', 'I00'),
                ('Common preferences, own circumstances', 'I10'),
                ('Own preferences, common circumstances', 'I01'),
                ('Common preferences, common circumstances', 'I11')]:
    _rows.append([lab, format(REG['w_%s_singles' % st.lower()]['value'], '.6f'),
                  format(REG['w_%s_couples' % st.lower()]['value'], '.6f')])
_rows.append(['*Preferences equalized alone: change in the Gini (per cent)*',
              format(-REG['of_P_singles']['value'], '+.2f'),
              format(-REG['of_P_couples']['value'], '+.2f')])
_rows.append(['*All other circumstances equalized alone: change (per cent)*',
              format(-REG['of_E_singles']['value'], '+.2f'),
              format(-REG['of_E_couples']['value'], '+.2f')])
TABLES['states'] = table(
    'v5_welfare_states',
    'Table: The four coalition states of the two-group game and the '
    'corresponding one-factor effects. Weighted Gini of the money metric on '
    'the raw household basis, with the female-primary reference for '
    'single-adult households. The fully common state is zero to the precision '
    'reported in the text: that is a tested property of the game, not an '
    'imposed constraint. A positive percentage in the last two rows is a rise '
    'in inequality.',
    ['State', 'Single-adult', 'Couple'], _rows)

# ---- T12: the grouped attribution with intervals -------------------------- #
_rows = []
for comp, lab in COMPS:
    row = [lab]
    for tag in ['singles', 'couples']:
        k = 'w_c%s_%s' % (comp, tag)
        if k not in REG:
            row += ['--', '--']
            continue
        row.append(format(REG[k]['value'], '.6f'))
        share = REG['w_sh%s_%s' % (comp, tag)]['value']
        lo = REG.get('cr1_lo_%s_%s' % (comp, tag))
        cell = format(share, '.2f')
        if lo is not None:
            cell += ' [%s, %s]' % (
                format(lo['value'], '.1f'),
                format(REG['cr1_hi_%s_%s' % (comp, tag)]['value'], '.1f'))
        row.append(cell)
    _rows.append(row)
TABLES['attribution'] = table(
    'v5_attribution',
    'Table: Grouped attribution of well-being inequality. Contributions in '
    'Gini points beside the share of the baseline Gini of the same population, '
    'per cent, with the 95 per cent cluster-robust parameter interval in '
    'brackets from 100 draws. Shares are taken against the baseline of the '
    'same population and are not comparable as levels across the two '
    'populations. The parameter interval and the RQMC integration band measure '
    'different things and are never combined; the integration band is reported '
    'separately in the text and in the figure. Resources and needs enter here '
    'as one component of the four-player game; its subdivision into non-labour '
    'resources and household composition is a nested attribution and has its '
    'own table.',
    ['Component', 'Singles: Gini points', 'Singles: share [95 per cent]',
     'Couples: Gini points', 'Couples: share [95 per cent]'], _rows)

# ---- T12b: the subdivision of D for couples ------------------------------- #
_rows = []
for ix, ixlab in INDICES:
    _rows.append([ixlab,
                  format(REG['nd_shres_%s' % ix]['value'], '.2f') + ' / '
                  + format(REG['nd_shcomp_%s' % ix]['value'], '.2f'),
                  format(REG['nd_chres_%s' % ix]['value'], '.1f') + ' / '
                  + format(REG['nd_chcomp_%s' % ix]['value'], '.1f'),
                  format(REG['nde_chres_%s' % ix]['value'], '.1f') + ' / '
                  + format(REG['nde_chcomp_%s' % ix]['value'], '.1f'),
                  format(REG['sd_shres_%s' % ix]['value'], '.2f') + ' / '
                  + format(REG['sd_shcomp_%s' % ix]['value'], '.2f'),
                  format(REG['sd_chres_%s' % ix]['value'], '.1f') + ' / '
                  + format(REG['sd_chcomp_%s' % ix]['value'], '.1f'),
                  format(REG['sde_chres_%s' % ix]['value'], '.1f') + ' / '
                  + format(REG['sde_chcomp_%s' % ix]['value'], '.1f')])
TABLES['nestedD'] = table(
    'v5_nested_d',
    'Table: The subdivision of the resources-and-needs contribution into '
    'non-labour resources and household composition and needs, reported as '
    '"resources / composition" in every cell. Columns two and five are shares '
    'of that population’s baseline inequality; the remaining columns are '
    'shares of the resources-and-needs channel itself, which the two cells '
    'divide. The couple cells come from two counterfactual panels repriced '
    'through the tax-benefit system on the corrected partition of '
    + str(REG['nd_n_res']['value']) + ' resource fields, '
    + str(REG['nd_n_comp']['value']) + ' composition and needs fields and '
    + str(REG['nd_n_geo']['value']) + ' geographic fields, and sum to the joint '
    'contribution to a residual of 1.4e-17 in index units. The single-adult '
    'cells also report the corrected nested attribution. Both populations use '
    'their current repriced partial-D panels; raw and equivalized channel '
    'shares are displayed separately.',
    ['Index', 'Couples: share of baseline', 'Couples: share of channel',
     'Couples: channel, equivalized', 'Singles: share of baseline',
     'Singles: share of channel', 'Singles: channel, equivalized'], _rows)

# ---- T13: six-index levels and shares ------------------------------------- #
_rows = []
for tag, pop in [('singles', 'Single-adult'), ('couples', 'Couple')]:
    for ix, ixlab in INDICES:
        row = [pop + ', ' + ixlab,
               format(REG['w_base_%s_%s' % (ix, tag)]['value'], '.6f')]
        for comp in ['P', 'A', 'B', 'D', 'AB']:
            row.append(format(REG['w_sh%s_%s_%s' % (comp, ix, tag)]['value'],
                              '.2f'))
        _rows.append(row)
TABLES['sixindex'] = table(
    'v5_six_index',
    'Table: Baseline level and attribution shares under six inequality '
    'indices. Every row was recomputed for its own index against its own '
    'baseline; no coalition value or share is transferred between indices. '
    'Shares within a row sum to one hundred by exhaustiveness. A negative '
    'preference share means that equalizing preferences alone would raise that '
    'index, which is a property of this exhaustive two-group game with a '
    'nonnegative index and is explained in the text.',
    ['Population and index', 'Baseline level', 'Preferences (per cent)',
     'Access', 'Earning opportunities', 'Resources and needs',
     'Access + earnings'], _rows)

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

# ---- T15: the operators --------------------------------------------------- #
TABLES['operators'] = table(
    'v5_operators',
    'Table: The four structural equalization operators. Each operator replaces '
    'the arguments of one structural pathway with a common reference profile '
    'and leaves the estimated coefficients in place; it does not equalize every '
    'occurrence of a raw characteristic. Education, for example, enters both '
    'the wage location and the local-market lookup, and only the named pathway '
    'is substituted. Operators are applied as one simultaneous substitution '
    'map, not as an ordered product.',
    ['Operator', 'What is replaced', 'What is retained', 'Repricing'],
    [[r'$T_P$ preferences',
      'Singles: the arguments of the leisure weight and the complete '
      'reference-sex leisure block. Couples: the medoid spouse arguments, with '
      'own spouse coefficients retained',
      'Budget roster, resources, access and wage pathways of the same '
      'characteristics', 'No: pure utility shifters do not change the budget'],
     [r'$T_A$ job access',
      'The arguments of the employment index and the occupation access table',
      'Preferences, wage location, budget inputs; sex-specific occupation '
      'coefficients', 'No: the priced jobs are unchanged'],
     [r'$T_B$ earning opportunities',
      'The arguments of the offered-wage location: education shares and '
      'experience moments, with squares recomputed rather than averaged',
      'The estimated wage coefficients and dispersion; the preference and '
      'access pathways of the same characteristics',
      'No on a common priced node set: the change is in the density over '
      'nodes'],
     [r'$T_D$ resources and needs',
      'The non-labour budget inputs, the household roster and the needs '
      'profile',
      'Every non-budget structural pathway',
      'Yes: the household budget is recomputed through the tax-benefit '
      'system']])

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

# ---- T17: the W1/W4 bridge ------------------------------------------------ #
_rows = []
for tag, pop in [('singles', 'Single-adult'), ('couples', 'Couple')]:
    b = _BR[tag]
    _rows.append([
        pop,
        'yes' if b['home_is_argmax_L']['pass'] else 'no',
        format(b['ghat_integral_on_H_domain']['median'], '.6f'),
        format(b['unit_mass_corrected_bridge']['W4_over_W1']['median'], '.4f'),
        '[%s, %s]' % (
            format(b['unit_mass_corrected_bridge']['W4_over_W1']['min'], '.4f'),
            format(b['unit_mass_corrected_bridge']['W4_over_W1']['max'], '.4f')),
        format(b['unit_mass_corrected_bridge']['Delta_nats']['median'], '.4f'),
        'yes' if b['unit_mass_corrected_bridge']['Delta_nonnegative_everywhere']
        else 'no'])
TABLES['bridge'] = table(
    'v5_bridge',
    'Table: The bridge between the two monetary references, after the premise '
    'audit. The second column reports whether non-work maximizes the '
    'non-consumption index for every household; the third reports the median '
    'mass of the opportunity kernel on the domain the reference integral uses. '
    'That mass is not one, which is the premise that failed and the reason the '
    'earlier signed gaps were scale artefacts. The remaining columns are the '
    'bridge after normalizing the kernel on exactly that domain.',
    ['Population', 'Non-work maximizes $L$', 'Median $\\int\\hat g$',
     'Median $W^4/W^1$', 'Range', 'Median $\\Delta$ (nats)',
     '$\\Delta\\ge 0$ everywhere'], _rows)

# ---- T18: the lambda_c reconciliation ------------------------------------- #
TABLES['lambda'] = table(
    'v5_lambda_c',
    'Table: The consumption normalizer. Three constants were in circulation. '
    'Under exact log consumption the normalizer enters utility as the '
    'alternative-invariant term $-\\beta_c\\log\\lambda_c$, so it cancels from '
    'every choice probability and exactly from the money metric. The paper '
    'reports the estimation-frame constant throughout.',
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
mfig('fit', 'figV06_fit_by_margin',
     'Observed against model population shares, margin by margin, for both '
     'estimated specifications. Model shares are population predictions '
     'computed by direct integration over the estimated opportunity '
     'distribution, not sampled-menu choice probabilities.')
mfig('lorenz', 'figV01_welfare_lorenz',
     'Lorenz curves of money-metric well-being and of the priced disposable '
     'income it replaces, over the same households and the same weights. The '
     'two curves answer different questions about the same households; their '
     'Gini values are not two estimates of one quantity.')
mfig('welfdist', 'figV02_welfare_distributions',
     'The distribution of money-metric well-being, by household type and '
     'basis, with weighted medians marked. Levels are not comparable across '
     'the two panels: each household type carries its own reference '
     'construction.')
mfig('signed', 'figV03_signed_decomposition',
     'The grouped attribution, signed, in per cent of each population\u2019s '
     'own baseline Gini. The black bar is the 95 per cent cluster-robust '
     'parameter interval; the shaded bar is the RQMC integration band. They '
     'measure different things and are never combined.')
mfig('onefactor', 'figV04_one_factor_vs_shapley',
     'Equalizing one group alone against the grouped Shapley share. For '
     'single-adult households, equalizing preferences alone raises the Gini '
     'while the preference share is positive; the share averages marginal '
     'contributions over coalition orders and the one-factor effect does not.')
mfig('sixindex', 'figV05_six_index_shares',
     'Attribution shares under six inequality indices. Each index keeps its '
     'own coalition values and its own allocation. Access exceeds earning '
     'opportunities for single adults under all six and the ordering reverses '
     'for couples under all six; the singles preference share changes sign '
     'outside the Gini.')
mfig('powermean', 'figV07_power_mean',
     'The consumption coefficient as the order of a power mean. Left: the '
     'contribution an alternative makes to the consumption power moment, '
     'relative to the median alternative, against the linear comparison at '
     '$\\beta_c=1$. Right: the marginal effect of that alternative\u2019s '
     'consumption on the resulting equivalent amount, which carries exponent '
     '$\\beta_c-1$, against the flat comparison at $\\beta_c=1$. Neither curve '
     'is a reference probability weight: holding the reference measure fixed, '
     'those weights do not vary with consumption at all.')
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
tex = (header + body + '\n\\bibliographystyle{plainnat}\n'
       '\\bibliography{JMP_working_paper_for_seminar_v5}\n\\end{document}\n')
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

REGOUT = {'build_date': today,
          'model_of_record': 'S11 specifications of record: tau = 1, '
                             'theta_c = 0, beta_c estimated; welfare at S12 on '
                             'the 1,540 / 2,223 estimation frames',
          'entries': {**_existing_register.get('entries', {}), **REG}, 'used_keys': sorted(USED),
          'unused_keys': sorted(set(REG) - USED),
          'gallery': _existing_register.get('gallery'),
          'discussion_tables': _existing_register['discussion_tables']}
(ROOT / 'reports/numbers_of_record_v5.json').write_text(
    json.dumps(REGOUT, indent=2, ensure_ascii=False), encoding='utf-8')
print('v5: %d registered numbers, %d used; paper and report written.'
      % (len(REG), len(USED)))
