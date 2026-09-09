"""Build the two v3 reading documents from shared prose, numbers and figures.

Run with the project's scientific Python environment. Existing v2 files remain
untouched. Empirical values are imported to the v3 registry before formatting;
corrected-result slots fail closed unless an explicitly reviewed successor is
provided. Mathematical integers are syntax, not empirical estimates.
"""
from __future__ import annotations
import base64
import csv
import datetime as dt
import html
import json
import importlib.metadata
from pathlib import Path
import re
import shutil
import subprocess
import urllib.request
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pypandoc
from v3_sections import TITLE, ABSTRACT, VERSION, SECTIONS, QA

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
MNL = ROOT.parent/'MNL'
SPRINT = MNL/'experiments/JMP_SEMINAR_SPRINT'
PAPER = ROOT/'manuscript'
FIG = PAPER/'figures/v3'
TABLE = PAPER/'tables/v3'
REG = json.loads((ROOT/'reports/numbers_of_record_v1.json').read_text('utf-8'))['entries']
USED = set()
FIG.mkdir(parents=True, exist_ok=True)
TABLE.mkdir(parents=True, exist_ok=True)

def register(key, value, source, status='historical', units='dimensionless'):
    REG[key] = {'value': value, 'source': source, 'status': status, 'units': units}
    return value

def val(key, fmt=None):
    USED.add(key)
    v = REG[key]['value']
    if key.endswith('_year'): return str(v)
    if key=='welf_error': return '$'+format(float(v)/1e-10,'.1f')+r'\times10^{-10}$'
    if fmt: return format(float(v), fmt)
    if isinstance(v, float): return format(v, '.6g')
    if isinstance(v, int): return format(v, ',d')
    return str(v)

for key,value in [('collection_year',2016),('income_year',2015),('policy_year',2015),
                  ('time_endowment',80),('leisure_scale',10),('experience_scale',20),
                  ('age_scale',10),('child_cutoff',20),('kappa',.2),('gsur_age_min',20),('gsur_age_max',64),
                  ('single_c_scale',1911.108057855561),('couple_c_scale',3821.448012098882)]:
    register(key,value,'model_extraction_v1.md; source-to-sample audit (timing supersedes earlier extraction)', 'definition')
# ---- Specifications of record (s11) ---------------------------------------
# The shock scale and the consumption curvature are fixed and the consumption
# WEIGHT is estimated, which is what identifies the utility scale; couples
# additionally carry the coherent wider experience bounds. These supersede the
# earlier corrected estimation for both populations.
_S11 = ('specifications of record: tau fixed, exact log consumption, estimated '
        'consumption weight; couples on the wider experience bounds')
for _k, _v, _u in [
        ('scale_beta_c_singles', 2.0387318, 'weight on log consumption'),
        ('scale_beta_c_couples', 2.1017203, 'weight on log consumption'),
        ('scale_se_singles', 0.2917295, 'standard error'),
        ('scale_se_couples', 0.2938791, 'standard error'),
        ('scale_gain_singles', 23.752611, 'log-points'),
        ('scale_gain_couples', 15.659005, 'log-points'),
        ('negll_singles', 6253.463074380, 'log-likelihood units'),
        ('negll_couples', 10283.034369351, 'log-likelihood units'),
        ('negll_ruma', 6403.974284931, 'log-likelihood units'),
        ('negll_rumb', 6395.107857484, 'log-likelihood units'),
        ('n_singles_est', 1540, 'households'),
        ('n_couples_est', 2223, 'households'),
        ('k_free_singles', 41, 'coordinates'),
        ('k_int_singles', 40, 'coordinates'),
        ('k_free_couples', 47, 'coordinates'),
        ('k_int_couples', 47, 'coordinates'),
        ('mineig_singles', 0.166893, 'smallest Hessian eigenvalue'),
        ('mineig_couples', 0.0770744, 'smallest Hessian eigenvalue'),
        ('fit_mae_singles_post', 0.013040, 'mean absolute deviation, shares'),
        ('fit_mae_couples_post', 0.013595, 'mean absolute deviation, shares')]:
    register(_k, _v, _S11, 'estimated', _u)

for _k, _v in [('rank_singles', 'rank 41 of 41'),
               ('rank_couples', 'rank 47 of 47'),
               ('kappa_singles', 'about 384,000'),
               ('kappa_couples', 'about 3.9 million')]:
    register(_k, _v, _S11, 'estimated', 'conditioning')

# the earlier numeraire convention, kept only as the comparison point
for _k, _v in [('fit_mae_singles_pre', 0.01523), ('fit_mae_couples_pre', 0.01385)]:
    register(_k, _v, 'corrected estimation under the earlier numeraire '
             'convention', 'estimated', 'mean absolute deviation, shares')

register('rum_gap_logpoints', round(6395.107857484 - 6253.463074380, 2),
         _S11, 'estimated', 'log-points')

# ---- the proportional nat, and the baselines a euro figure needs -----------
# exp(1/beta_c) is the scale-free statement; the euro amounts exist only
# against the normalizing consumption of each population.
import math as _math
for _tag, _bc, _base in [('singles', 2.0387318, 1938.238719107138),
                         ('couples', 2.1017203, 4247.875047307145)]:
    _f = _math.exp(1.0 / _bc)
    register('scale_nat_factor_' + _tag, round(_f, 4), _S11, 'derived',
             'multiplicative factor on consumption')
    register('scale_baseline_' + _tag, int(round(_base)), _S11, 'definition',
             'EUR/month')
    register('scale_nat_eur_' + _tag, int(round(_base * (_f - 1.0))), _S11,
             'derived', 'EUR/month at the stated baseline')
    register('scale_nat_pct_' + _tag, round((_f - 1.0) * 100.0, 1), _S11,
             'derived', 'per cent change in consumption')

# ---- COND-1: conditioning on parameter-standardized coordinates -----------
# Each coordinate is scaled by its cluster-robust standard error, or by its
# bound half-width where the coordinate is active. Raw-coordinate condition
# numbers describe units; these describe the information in the likelihood.
_COND1 = ('COND-1 scaled conditioning diagnostic on the s11 specifications '
          'of record')
for _k, _v in [('cond_std_singles', 728),
               ('cond_std_couples', 9443),
               ('cond_std_couples_ex', 234)]:
    register(_k, _v, _COND1, 'diagnostic', 'condition number, standardized '
             'coordinates')

# ---- the weighting the estimated order implies ----------------------------
# 2**beta_c is the weight an alternative paying twice the median carries;
# derived here so it cannot drift from the estimate it is read against.
register('pm_weight_double', round(2.0 ** 2.0387318, 2), _S11, 'derived',
         'implied weight relative to the median alternative')
for _k, _v, _u in [('pm_ratio_p95p5', 95.6, 'implied weight ratio'),
                   ('pm_ratio_arith', 9.4, 'implied weight ratio')]:
    register(_k, _v, 'figP07 weighting panel, p5-p95 span of reachable '
             'consumption', 'derived', _u)

# ---- the power-mean identity gate -----------------------------------------
register('pm_cases', 1000,
         'power-mean identity gate against the production evaluator',
         'verified identity', 'household-and-weight cases')
register('pm_maxreldiff', '7.1e-16',
         'power-mean identity gate against the production evaluator',
         'verified identity', 'relative difference')

wi = json.loads((MNL/'docs/corr/welfare_identity_check_v1.json').read_text('utf-8'))
register('welf_error',wi['overall']['max_abs_difference_eur_per_month'],'welfare_identity_check_v1.json::overall','verified identity','EUR/month')
register('welf_comparisons',sum(x['closed_form_vs_solver']['n'] for t in ['singles','couples'] for x in wi[t]['states'].values()),'welfare_identity_check_v1.json::states','verified identity','household-states')
EXAMPLE = json.loads((HERE/'evaluator_examples_v3.json').read_text('utf-8'))

def flatten(prefix, obj, source):
    if isinstance(obj, dict):
        for k,v in obj.items(): flatten(prefix+'__'+str(k),v,source)
    elif isinstance(obj,list):
        for k,v in enumerate(obj): flatten(prefix+'__'+str(k),v,source)
    else: register(prefix,obj,source)
flatten('example',EXAMPLE,'evaluator_examples_v3.json (production evaluator, anonymous simulated jobs)')
FD = json.loads((HERE/'final_descriptives_v1.json').read_text('utf-8'))
flatten('descriptive',FD,'final_descriptives_v1.json (historical priced frames)')
for package in ['jax','jaxlib','euromod']:
    register('installed_'+package,importlib.metadata.version(package),'build environment package metadata','installed software','version')


# ---- s12: the corrected welfare record ------------------------------------
# Read from the run artifact, not transcribed. _s12row asserts a unique match so
# a renamed reference or basis fails the build instead of silently selecting the
# wrong row.
S12 = SPRINT/'runs/s12_welfare_record'
_S12 = pd.read_csv(S12/'s12_six_index_attributions_v1.csv')
_S12SRC = ('s12_six_index_attributions_v1.csv; corrected frame at the s11 '
           'specifications of record')
_INDICES = [('gini','Gini'),('atkinson1','Atkinson(1)'),('atkinson2','Atkinson(2)'),
            ('ge0','GE(0)'),('ge1','GE(1)'),('cv2','Half CV squared')]
_ARMS = [('singles','singles','singles_female'),
         ('singlesmz','singles','singles_male_structural_zero'),
         ('couples','couples','household-own')]

def _s12row(sample, reference, basis, index):
    m = _S12[(_S12['sample']==sample)&(_S12['reference']==reference)
             &(_S12['basis']==basis)&(_S12['index']==index)]
    if len(m)!=1:
        raise SystemExit('s12 row not unique: %r %d'%((sample,reference,basis,index),len(m)))
    return m.iloc[0]

def _num(r, col):
    v = r[col]
    try:
        f = float(v)
    except (TypeError, ValueError):
        return None
    return None if f!=f else f

_W = {}
for _tag, _sample, _ref in _ARMS:
    for _ix, _ixlabel in _INDICES:
        r = _s12row(_sample, _ref, 'raw', _ix)
        base = float(r['I00'])
        cell = {'base': base}
        for comp, col in [('P','C_P'),('A','C_A'),('B','C_B'),('AB','C_AB'),
                          ('D','C_D'),('E','C_E'),('res','C_resources'),
                          ('comp','C_composition'),('geo','C_geo')]:
            c = _num(r, col)
            cell[comp] = c
            cell['sh_'+comp] = None if c is None else 100.0*c/base
        for st in ['I00','I10','I01','I11']:
            cell[st] = float(r[st])
        _W[(_tag,_ix)] = cell

# the headline arms, Gini on the raw basis
for _tag, _, _ in _ARMS:
    c = _W[(_tag,'gini')]
    for st in ['I00','I10','I01','I11']:
        register('w_%s_%s'%(st.lower(),_tag), round(c[st],6), _S12SRC,
                 'corrected result', 'Gini units')
    for comp in ['P','A','B','AB','D','E','res','comp','geo']:
        if c[comp] is None:
            continue
        register('w_c%s_%s'%(comp,_tag), round(c[comp],6), _S12SRC,
                 'corrected result', 'Gini points')
        register('w_sh%s_%s'%(comp,_tag), round(c['sh_'+comp],2), _S12SRC,
                 'corrected result', 'per cent of baseline inequality')

# ---- exhaustiveness: a tested property, passed ----------------------------
for _k, _v, _u in [('w_resid_top','2.8e-17','Gini units'),
                   ('w_resid_nested','5.6e-17','Gini units'),
                   ('w_i11_max','1.3e-15','Gini units')]:
    register(_k, _v, 's12_welfare_record_report_v1.md::Exhaustiveness',
             'verified identity', _u)

# ---- wage neutrality: now evidence ----------------------------------------
# The bound differs by population; reporting one joint bound would be false for
# couples, whose maximum is four times the singles maximum.
for _k, _v, _st, _u in [
        ('w_dlogh_singles','1.8e-15','verified identity','log units'),
        ('w_dlogh_couples','7.1e-15','verified identity','log units'),
        ('w_direct_median',0,'corrected result','EUR/month'),
        ('w_attain_median_singles',-17.43,'corrected result','EUR/month'),
        ('w_attain_median_couples',110.53,'corrected result','EUR/month')]:
    register(_k, _v, 's12_welfare_record_report_v1.md::Wage-density neutrality',
             _st, _u)

# ---- the corrected medians the nat is evaluated at ------------------------
for _tag, _c, _cp in [('singles',1760.63,2875.34),('couples',3854.22,6202.61)]:
    register('w_median_c_'+_tag, _c,
             's12_welfare_record_report_v1.md::Gate-first identity',
             'corrected result', 'EUR/month')
    register('w_median_cprime_'+_tag, _cp,
             's12_welfare_record_report_v1.md::Gate-first identity',
             'corrected result', 'EUR/month')

# ---- W3: a singles-only diagnostic ---------------------------------------
for _k, _v, _u in [('w3_bracketed_singles',1540,'households'),
                   ('w3_n_singles',1540,'households'),
                   ('w3_bracketed_couples',9,'households'),
                   ('w3_n_couples',2223,'households'),
                   ('w3_negative_couples',2103,'households')]:
    register(_k, _v, 's12_welfare_record_report_v1.md::W3', 'diagnostic', _u)


def table(name, caption, headers, rows):
    with (TABLE/(name+'.csv')).open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f); w.writerow(headers); w.writerows(rows)
    return '\n'+caption+'\n\n|'+'|'.join(headers)+'|\n|'+'|'.join(['---']*len(headers))+'|\n'+''.join('|'+'|'.join(str(v).replace('|','/') for v in row)+'|\n' for row in rows)+'\n'

TABLES={}
flow=pd.read_csv(SPRINT/'tables/fd_sample_funnel_v1.csv').iloc[1:8]
rows=[]
for i,r in flow.iterrows():
    label=str(r['screen']).replace('hours and wage inside the modelled support','Historical wage screen and hours projection')
    row=[label]
    for typ in ['singles','couples']:
        key=f'funnel__{i}__{typ}'
        register(key,int(r['households_'+typ]),'tables/fd_sample_funnel_v1.csv::'+str(i))
        row.append(val(key))
    rows.append(row)
TABLES['funnel']=table('sample_funnel','Historical sample flow. Population: French eligible single-adult and linked couple households; unit: unweighted households remaining after each screen; measure: retained count; reference: collection-year input and old observation/support rules; status: observed-input construction, not corrected successor counts.',['Screen','Singles','Couples'],rows)

rows=[]
for label, keys, fmt in [
 ('Mean decider age (years)', ['fd_age__mean_weighted__single_adult_the_decider','fd_age__mean_weighted__couple_the_man','fd_age__mean_weighted__couple_the_woman'],'.1f'),
 ('Employment fraction',['fd_employment_rate_weighted__single_adult_the_decider','fd_employment_rate_weighted__couple_the_man','fd_employment_rate_weighted__couple_the_woman'],'.3f'),
 ('Mean hours among employed (hours/week)',['fd_weekly_hours_continuous__mean_weighted__single_adult_the_employed_decider','fd_weekly_hours_continuous__mean_weighted__couple_the_employed_man','fd_weekly_hours_continuous__mean_weighted__couple_the_employed_woman'],'.1f'),
 ('Median wage input among employed (EUR/hour)',['fd_hourly_wage_eur_hour__median_weighted__single_adult_the_employed_decider','fd_hourly_wage_eur_hour__median_weighted__couple_the_employed_man','fd_hourly_wage_eur_hour__median_weighted__couple_the_employed_woman'],'.2f')]:
    rows.append([label]+[val(k,fmt) for k in keys])
TABLES['descriptives']=table('descriptives','Historical sample descriptives. Population: retained singles and couple deciders; household-survey-weighted means/fractions/medians; units stated in rows; reference: old constructed employment/hours/wage inputs; status: observed-input summaries, not model predictions or corrected-sample findings.',['Measure','Singles','Couple men','Couple women'],rows)
TABLES['specification']=table('specification','Maintained specification comparison. Population: single-adult and couple households; measure: structural restrictions (no estimated quantities); units: utility on fixed stochastic scale; reference: extracted retained utility/opportunity architecture, on the corrected support and estimator.',['Component','Singles','Couples'],[
 ['Decision','One job','One joint job pair under shared budget'],
 ['Consumption','Estimated common Box–Cox curvature','Log consumption'],
 ['Leisure','Sex-specific weights and curvatures','Spouse-specific weights and curvatures'],
 ['Children','Female leisure weight only','Female leisure weight only'],
 ['Direct leisure interaction','Not applicable','Restricted to zero'],
 ['Hours opportunities','Shared across sexes','Separate spouse band coefficients'],
 ['Occupation access','Sex-specific','Spouse-sex-specific'],
 ['Wage block','Shared across sexes within singles','Shared across spouses within couples; separate estimation from singles'],
 ['Consumption aggregation','All-member household aggregation','All-member household aggregation'],
 ['Proposal participation','Single work/non-work draw','Joint regime first, then conditional spouse jobs'],
 ['Welfare unit','Household','Household; within-couple allocation not identified']])
bands=[('Part-time lower',17.5,21.5,4),('Part-time upper',28.5,30.5,2),('Narrow full-time',33.5,36.5,3),('Full-time upper',36.5,40.5,4),('Long hours',44.5,70,25.5)]
rows=[]
for i,(name,lo,hi,width) in enumerate(bands):
    for k,v in [('lo',lo),('hi',hi),('width',width)]: register(f'band__{i}__{k}',v,'target_model_and_integrability_v1.md::hours','definition','hours/week')
    rows.append([name,'['+val(f'band__{i}__lo')+', '+val(f'band__{i}__hi')+(']' if i in [3,4] else ')'),val(f'band__{i}__width')])
TABLES['bands']=table('hours_bands','Hours opportunity bands in both applications. Measure: intervals and integration widths, hours/week; reference: extracted historical hours domain; status: model definitions, not observed masses. The complement has zero band index; endpoints carry no probability atoms.',['Band','Interval','Width'],rows)

PENDING='Pending corrected estimate'
TABLES['coefficients']=table('corrected_coefficients','Corrected coefficient panel. Populations: singles and couples by sex; measure: structural utility coefficients on the stated dimensionless normalization; reference: own characteristics, corrected target model; status: corrected estimates for both populations, with the coefficient cells below awaiting the finalized specification tables. Zero restrictions are not estimated zeros.',['Coefficient','Single men','Single women','Couple men','Couple women'],[
 [r'Leisure intercept $\beta_{\ell0}$']+[PENDING]*4,
 [r'Age slope $\beta_{\ell a}$']+[PENDING]*4,
 [r'Age-square slope $\beta_{\ell a2}$']+[PENDING]*4,
 [r'Child slope $\beta_{\ell n}$','Restricted zero',PENDING,'Restricted zero',PENDING],
 [r'Leisure curvature $\theta_\ell$']+[PENDING]*4,
 [r'Consumption curvature $\theta_c$','Fixed at zero (SCALE-1)','Fixed at zero (SCALE-1)','Fixed log','Fixed log']])
TABLES['fit']=table('corrected_fit','Corrected observed-versus-model fit. Population: singles and couple deciders/joint households; household-survey weights; units stated in rows; reference: corrected sample and own inputs; status: both retained observed and predicted moments pending reconstruction. Joint-regime probabilities are not Gini points.',['Moment','Singles observed','Singles model','Couples observed','Couples model'],[
 ['Employment (fraction)','Pending','Pending','Pending, each spouse','Pending, each spouse'],
 ['Joint regimes (fractions)','Not applicable','Not applicable','Pending, all regimes','Pending, all regimes'],
 ['Unconditional hours (hours/week)','Pending','Pending','Pending, each spouse','Pending, each spouse'],
 ['Occupation given work (fractions)','Pending','Pending','Pending, each spouse','Pending, each spouse'],
 ['Wage given work (EUR/hour)','Pending','Pending','Pending, each spouse','Pending, each spouse']])

rows=[]
for typ in ['single','couple']:
    for k,j in enumerate(EXAMPLE[typ]['baseline']['jobs']):
        pre=f'example__{typ}__baseline__jobs__{k}__'
        h=val(pre+'hours','.1f') if typ=='single' else val(pre+'hours_m','.1f')+'/'+val(pre+'hours_f','.1f')
        rows.append([typ.title(),h,val(pre+'C','.2f'),val(pre+'L','.4f')]+[val(pre+x,'.5f') for x in ['opportunity','choice','reference']])
TABLES['example_jobs']=table('evaluator_jobs','Worked historical-evaluator examples. Population: one anonymous median-value single woman and one couple; jobs: selected simulated nodes; hours/week (man/woman for couples), priced consumption EUR/month, non-consumption utility L in utility units; remaining columns: normalized numerical node masses on each household’s own common support. Reference: own flat consumption; status: model-implied at historical parameters, not corrected findings.',['Type','Hours','Consumption','L','Opportunity','Choice','Reference'],rows)
rows=[]
for typ in ['single','couple']:
    for state in ['baseline','preferences','environment','all']:
        pre=f'example__{typ}__{state}__'
        rows.append([typ.title(),state,val(pre+'logJ','.5f'),val(pre+'logH','.5f'),val(pre+'W','.2f')])
TABLES['example_states']=table('evaluator_states','Same anonymous households through the principal equalization states. Population: the examples immediately above; measure: normalized log integrals (dimensionless) and equivalent income (EUR/month); reference: each state’s flat-consumption map; status: model-implied historical-parameter evaluator outputs, not population inequalities.',['Type','State','log J','log H','W (EUR/month)'],rows)

TABLES['operators']=table('operators','Structural equalization operators for both household types. Measure: input substitutions, not causal effects; units inherited from each input; reference: selected representative profile and coalition-consistent monetary map; status: extracted broad operators. The resources/needs subdivision is resolved for single-adult households and unavailable for couples.',['Operator','Replaced / profile','Household-specific remainder','Repricing','Reference map'],[
 ['Preferences P','Singles: weighted mean index arguments and complete reference-sex coefficient/curvature block. Couples: medoid spouse arguments, own spouse coefficients','Budget roster, resources, access and wage shifters unless separately equalized','No for pure utility shifters','Replace L on both sides'],
 ['Access A','Singles: weighted mean access arguments and marginalized normalized occupation table. Couples: medoid market arguments','Preferences, wage locations, budget inputs; couple sex-specific occupation coefficients remain','No for pure access indices','Replace opportunity weights on both sides'],
 ['Wage opportunities B','Singles: weighted education shares and experience moments. Couples: medoid spouse education/experience; squares recomputed. Estimated wage coefficients retained','Preference and access pathways of same covariates','Not from an index change alone on common priced jobs','Replace wage weights on both sides'],
 ['Budget D','Policy inputs from representative budget household, including resource and needs pathways','Non-D structural pathways','Yes; rerun household budget','Use new consumption in J; state L and opportunities in H'],
 ['Resources within D','Corrected resource fields and take-up; work-history priority pending','Composition/needs unless separately changed','Yes when policy inputs change','No independent new reference; follow resulting state'],
 ['Needs within D','Roster/needs and linked scale, selected needs profile','Resource and utility-child pathways unless separately changed','Yes; update needs scale','Follow resulting state; no hidden P change']])
_STATE_ROWS=[('Own preferences, own environment','I00'),
             ('Common preferences, own environment','I10'),
             ('Own preferences, common environment','I01'),
             ('Common preferences, common environment','I11')]
TABLES['states']=table('corrected_welfare_states','Corrected within-type welfare states on the corrected frame. Population: single-adult and couple households; measure: household-survey-weighted Gini of the ex-ante money metric, dimensionless Gini units, raw household basis; reference: coalition-consistent flat-consumption maps and the designated within-type profiles, female-primary for singles; status: corrected results. The fully-common state is zero to the precision reported in the text, which is a tested property of the game and not an imposed constraint. Equivalized results occupy their own panel, not a change of units within a row.',['State','Singles Gini','Couples Gini'],
    [[lab,format(_W[('singles','gini')][st],'.6f'),
          format(_W[('couples','gini')][st],'.6f')] for lab,st in _STATE_ROWS])
_ATTR_ROWS=[('Preferences','P'),('Access','A'),('Earning opportunities','B'),
            ('Access + earnings (market opportunities)','AB'),
            ('Budget resources/needs','D'),
            ('All non-preference circumstances','E'),
            ('Resources suballocation','res'),
            ('Household composition and needs suballocation','comp')]
def _attr(tag,comp):
    c=_W[(tag,'gini')]
    if c[comp] is None: return ['Not available','Not available']
    return [format(c[comp],'.6f'),format(c['sh_'+comp],'.2f')]
TABLES['contributions']=table('corrected_attribution','Corrected grouped attribution on the corrected frame. Population: each household type, survey weighted; contributions in Gini points beside the share of the baseline inequality of that same population; reference: raw within-type baseline and the declared grouping; status: corrected results. Shares are taken against the baseline of the same population and are not comparable as levels across the two columns. Parameter intervals, integration bands and reference ranges occupy separate reporting fields and are not combined into one band. The couples resources/needs suballocation is not available: no separately repriced couples partial pair exists, and the cells are therefore marked rather than imputed.',['Component','Singles Gini points','Singles share (per cent)','Couples Gini points','Couples share (per cent)'],
    [[lab]+_attr('singles',comp)+_attr('couples',comp)
     for lab,comp in _ATTR_ROWS])
rows=[]
for name,k in [('Leisure intercept','beta_l0'),('Age slope','beta_l_age'),('Age square','beta_l_age2'),('Leisure curvature','theta_l'),('Consumption curvature','theta_c')]:
    rows.append([name]+[val('pf_'+k+'__'+g,'.4f') for g in ['singles_male','singles_female','couples_male','couples_female']])
rows.append(['Female child slope','Restricted zero',val('pf_beta_l_nkids__singles_female','.4f'),'Restricted zero',val('pf_beta_l_nkids__couples_female','.4f')])

# The qualitative ordering is reported index by index because a share is a
# property of the index as much as of the decomposition. Every row was rerun;
# none is transferred from the Gini.
_sixrows=[]
for _pop,_tag in [('Singles','singles'),('Couples','couples')]:
    for _ix,_ixlabel in _INDICES:
        _c=_W[(_tag,_ix)]
        _sixrows.append(['%s, %s'%(_pop,_ixlabel)]
                        +[format(_c['sh_'+k],'.2f') for k in ['P','A','B','D']]
                        +[format(_c['sh_AB'],'.2f')])
TABLES['six_index']=table('corrected_six_index','Index-specific attribution on the corrected frame. Population: each household type, survey weighted, raw basis, female-primary reference for singles; measure: share of the baseline inequality of that same index, per cent; status: corrected results. Each row was recomputed for its own index against its own baseline; no share is transferred between indices. Shares within a row sum to one hundred by exhaustiveness. A negative preference share means equalizing preferences alone would raise measured inequality, which is a property of the attribution game and not an error.',['Population and index','Preferences','Access','Earning opportunities','Resources and needs','Access + earnings'],_sixrows)
TABLES['historical_coefficients']=table('historical_coefficients','Historical coefficients solely for evaluator replication. Population: old single-adult and couple estimation frames; measure: deterministic-utility parameters on registered scales; reference: historical hybrid criterion and historical support; status: NOT corrected estimates. Conditional constrained-inference tables must be regenerated after the refit.',['Coefficient','Single men','Single women','Couple men','Couple women'],rows)

plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'savefig.dpi':180})
def save(fig,name):
    fig.tight_layout(); fig.savefig(FIG/(name+'.png'),bbox_inches='tight'); fig.savefig(FIG/(name+'.pdf'),bbox_inches='tight'); plt.close(fig)

# Purely illustrative geometry; axis units deliberately schematic.
fig,ax=plt.subplots(figsize=(8.5,4.3))
x=np.linspace(.1,.9,200)
ax.plot(x,.6475-.45*x,color='#315b7d',label='Broader illustrative menu')
restricted=x[x>=.45]
ax.plot(restricted,.85-.9*restricted,color='#b55a3c',label='Restricted illustrative menu')
# Both preference curves go through the same marked bundle, but slopes differ.
point=(.45,.445)
ax.plot(x,point[1]+.2025*(np.log(point[0])-np.log(x)),ls='--',color='#315b7d',label='More leisure-oriented preferences')
ax.plot(x,point[1]+.06*(np.log(point[0])-np.log(x)),ls=':',color='#b55a3c',label='More work-oriented preferences')
ax.scatter(*point,color='black',zorder=5); ax.annotate('Same observed bundle',point,xytext=(.55,.63),arrowprops={'arrowstyle':'->'})
ax.set(xlabel='Leisure (schematic)',ylabel='Disposable consumption (schematic)',ylim=(0,1),xlim=(0,1),xticks=[],yticks=[])
ax.legend(fontsize=9,loc='upper right'); save(fig,'motivation')
fig,axs=plt.subplots(1,2,figsize=(10,4.4))
for typ,ax in zip(['single','couple'],axs):
    e=EXAMPLE[typ]['baseline']; m=np.linspace(.25*e['W'],1.8*e['W'],200)
    bc=np.log(m/e['lambda']) if e['theta']==0 else ((m/e['lambda'])**e['theta']-1)/e['theta']
    ax.plot(m,bc+e['logH'],label=r'$\Phi_i(m)$',color='#315b7d')
    ax.axhline(e['logJ'],ls='--',color='#b55a3c',label='Attained ex-ante value')
    ax.axvline(e['W'],ls=':',color='gray'); ax.scatter([e['W']],[e['logJ']],color='black')
    ax.set(xlabel='Flat consumption m (EUR/month)',ylabel='Dimensionless ex-ante value',title=typ.title()+' evaluator example')
    ax.legend(fontsize=8)
save(fig,'reference_map')
fig,axs=plt.subplots(1,2,figsize=(11,4.4))
for typ,color,label in [('singles','#315b7d','Singles'),('couples','#b55a3c','Couples')]:
    vals=np.array(FD['resource_nonzero_share'][typ]); xs=np.arange(len(vals))
    axs[0].bar(xs+(-.18 if typ=='singles' else .18),vals,width=.36,label=label,color=color)
axs[0].set(xticks=np.arange(6),xticklabels=['Pensions','Self-\nemployment','Investment','Property','Transfers','Other'],ylabel='Survey-weighted fraction nonzero',title='Actual resource input incidence')
axs[0].legend(fontsize=9)
for typ,color,label in [('singles','#315b7d','Singles (historical decider sum)'),('couples','#b55a3c','Couples (household sum)')]:
    s=FD['summaries'][typ+'_disposable']
    axs[1].plot([.1,.5,.9],[s['p10_weighted'],s['median_weighted'],s['p90_weighted']],marker='o',label=label,color=color)
axs[1].set(xlabel='Weighted quantile',ylabel='Priced disposable consumption (EUR/month)',title='Simulated chosen-state consumption')
axs[1].legend(fontsize=8); save(fig,'descriptives')

pair=pd.read_csv(SPRINT/'figures/figE1_matched_pair.csv')
pair.to_csv(FIG/'matched_pair_source.csv',index=False)
register('matched_pair_series',pair.fillna('').to_dict('records'),'figures/figE1_matched_pair.csv','historical figure data')
fig,axes=plt.subplots(3,2,figsize=(10,10))
panels=list(pair.panel.unique())
titles=['(a) Leisure utility','(b) Employment opportunity mass','(c) Unconditional hours density','(d) Unconditional occupation mass','(e) Conditional wage density','(f) Conditional occupation mass']
for n,(panel,ax,title) in enumerate(zip(panels,axes.flat,titles)):
    for tag,color,shift in [('A','#315b7d',-.16),('B','#b55a3c',.16)]:
        d=pair[(pair.panel==panel)&(pair.household==tag)]
        if n==1:
            ax.bar(np.arange(len(d))+shift,d.y,width=.32,color=color,label=tag)
            labels=['Non-work' if 'non' in str(x).lower() else 'Work' for x in d['object']]
            ax.set_xticks(np.arange(len(d)),labels)
        elif n in [3,5]:
            ax.bar(d.x_occupation+shift,d.y,width=.32,color=color,label=tag); ax.set_xlabel('Occupation group')
        else:
            xcol='x_eur_per_hour' if n==4 else 'x_hours'
            ax.plot(d[xcol],d.y,color=color,label=tag); ax.set_xlabel('Gross wage (EUR/hour)' if n==4 else 'Hours/week')
    ax.set_title(title,fontsize=11); ax.legend(fontsize=8)
    ax.set_ylabel(['Utility units','Mass','Density per weekly hour','Mass','Density per EUR/hour','Mass'][n])
save(fig,'matched_pair')

# ---- preference figures: embed only SCALE-1-consistent renderings ---------
# The panels are drawn from the utility of record. Under SCALE-1 that utility
# has an ESTIMATED consumption weight; the versions built under the old
# beta_c = 1 numeraire describe a different utility and must not be shipped.
PREF_FIGS = ['figP01_indifference_curves_singles',
             'figP02_indifference_curves_couples',
             'figP03_marginal_utilities',
             'figP04_mrs_by_age_sex',
             'figP05_euro_value_of_one_nat',
             'figP06_normalization_sensitivity',
             'figP07_w1_power_mean_weighting']
PREF_PAPER = ['figP01_indifference_curves_singles',
              'figP03_marginal_utilities',
              'figP04_mrs_by_age_sex',
              'figP06_normalization_sensitivity']
# figP02, figP05 and figP07 go to the paper's appendix.


def _pref_fresh():
    """True when the rendered preference figures match the identified scale."""
    rec = (MNL / 'experiments/JMP_SEMINAR_SPRINT/runs/preference_figures_final'
           / 'pff_step1_reference_v1.json')
    if not rec.exists():
        return False, 'no preference-figure run on disk'
    try:
        rj = json.loads(rec.read_text('utf-8'))
        bcs = [p.get('beta_c') for p in rj.get('parameters', [])
               if isinstance(p, dict) and p.get('beta_c') is not None]
        if not bcs:
            u = rj.get('utility_of_record', {})
            bcs = [u['beta_c']] if 'beta_c' in u else []
    except Exception as e:
        return False, 'unreadable provenance: %s' % e
    if not bcs:
        return False, 'provenance does not record beta_c'
    if any(abs(float(b) - 1.0) < 1e-9 for b in bcs):
        return False, ('rendered with beta_c pinned at the old numeraire, '
                       'which the identified scale supersedes')
    return True, 'beta_c estimated (%s)' % ', '.join(
        '%.4f' % float(b) for b in sorted(set(map(float, bcs))))


PREF_FRESH, PREF_WHY = _pref_fresh()
PAPER_APPENDIX_FIGS = []

CAPTIONS={
 'figP01':('figP01_indifference_curves_singles','Indifference curves in consumption and leisure, single-adult households. Population: one representative single-adult household of each sex, the medoid of employed deciders on age, hours and consumption. Units: leisure in hours per week, consumption in euros per month. Status: model-implied preference object at the estimated parameters; the budget set, the opportunity density and the taste shock are not drawn, so a curve is not a set of attainable bundles.'),
 'figP02':('figP02_indifference_curves_couples','Indifference curves in consumption and joint leisure, couple households. Population: one representative couple household, the medoid on the same criteria, with the partner\u2019s leisure held at its observed value. Units: leisure in hours per week per spouse, consumption in euros per month. Status: model-implied preference object at the estimated parameters; conditional slices, not attainable sets.'),
 'figP03':('figP03_marginal_utilities','Marginal utility of consumption and of leisure, in physical units. Population: the representative households of each block. Units: marginal utility of consumption per euro per month and of leisure per hour per week, both after the chain-rule conversion from the normalized coordinates. Status: model-implied at the estimated parameters; levels are not comparable across separately estimated utility scales.'),
 'figP04':('figP04_mrs_by_age_sex','Marginal rate of substitution between leisure and consumption, by age and sex. Population: the representative household profile evaluated across the estimated age range, singles and couples. Units: euros per month of consumption per additional recurring weekly hour of leisure. Status: model-implied at the estimated parameters; a compensation along an indifference curve, not a behavioural response to a wage change.'),
 'figP05':('figP05_euro_value_of_one_nat','The euro value of one nat of utility under log consumption. Population: the representative households of each block, evaluated across the supported consumption range. Units: euros of monthly disposable consumption per nat of utility; a nat is the natural unit of the unit-scale index. Status: model-implied at the estimated consumption weight. The value is proportional rather than fixed, so it rises with the consumption at which it is evaluated and has no single euro figure independent of a baseline.'),
 'figP07':('figP07_w1_power_mean_weighting','The power-mean weighting of the money metric: the implied weight on an alternative as a function of its consumption. Population: the alternatives of the corrected single-adult frame. Units: horizontal axis euros of monthly disposable consumption; vertical axis a dimensionless relative weight, one at the median alternative. Status: model-implied at the estimated consumption weight. At an order above one the curve rises with consumption, which is the sense in which the measure weights well-paid reachable packages more heavily than an arithmetic mean would.'),
 'figP06':('figP06_normalization_sensitivity','Leisure-normalizer sensitivity: the coefficients move, the indifference curves and the marginal rate of substitution do not. Population: the representative single-adult female household, with the reported deviation maximised over all representative households and every normalizer tested. Units: panel (a) a dimensionless weight on transformed leisure; panel (b) euros per month against hours per week; panel (c) euros per month per extra weekly hour. Status: an exact coordinate change of the estimated model, not a re-estimation; coefficients are coordinates and the curves are the economics.'),

 'theory':('theory_w1','The own-set equal-consumption reference, adapted with permission from the companion theory project’s presentation (Haydar–Maniquet, work in progress). Two individuals with different preferences and different sets of available jobs, $A=\\{j,k\\}$ and $A^{\\prime}=\\{k,\\ell\\}$, attain the bundles $z_i$ and $z_h$. Holding each individual’s own preferences and own set fixed, a single flat consumption level is offered at every job in that set and raised until the best job under that level is exactly indifferent to what the individual actually attains; the level at which this happens, read on the consumption axis, is the monetary equivalent. Pay enters nowhere in the reference, because the level is the same at every job; the individual’s own set does enter, because the maximisation runs over it. Which individual is better off is what the measure decides, not an assumption of the diagram. Status: a definition, not an estimate — no axis is calibrated and nothing here is computed from the data.'),
 'motivation':('motivation','Motivation only: a schematic single-person consumption–leisure ambiguity. Axes have no empirical calibration; menus and preferences are illustrative. The same observed bundle does not identify its explanation. The conceptual distinction is related to Haydar–Maniquet’s companion theory paper; no fixed-leisure equivalent-income measure is computed.'),
 'reference':('reference_map','Implemented monetary reference for the anonymous single-adult and couple examples. Horizontal unit: flat monthly disposable consumption in euros; vertical measure: dimensionless ex-ante value. The reference curve meets attained value at equivalent income. Status: current evaluator at historical estimates and priced inputs; not corrected welfare results. Each curve uses its own baseline opportunity distribution and leisure utility.'),
 'descriptives':('descriptives','Historical input distributions for retained French singles and couples, using household survey weights. Left: fraction with nonzero actual resource inputs, not consumption proxies. Right: priced chosen-state consumption quantiles, euros/month under the income-reference policy. The singles historical aggregation is decider-based; couples use all-member aggregation. Status: historical source/pricing evidence, not corrected sample or welfare estimates.'),
 'matched':('matched_pair','Historical matched employed singles, households A and B (anonymous). The matching restrictions are common employment state, civilian occupation group, model hours band and observed-wage quintile; the forward selection restricts leisure-profile distance to the lowest admissible decile and maximizes opportunity distance. Panels: (a) deterministic leisure utility, utility units; (b) normalized opportunity mass at work and non-work; (c) unconditional working-hours density, per weekly hour, integrating to work mass; (d) unconditional occupation mass, summing to work mass; (e) wage density conditional on work, per EUR/hour, integrating to one; (f) occupation mass conditional on work, summing to one. All opportunities use each household’s normalized structural kernel, not its utility-weighted choice distribution. Similar jobs/preferences are not identical. Status: historical model-implied illustration, not corrected or causal evidence.')}

PROVENANCE=r'''
### Data, software and replication

**Data.** French EU-SILC, accessed through Eurostat's harmonised release,
with 2016 survey collection and a 2015 income-reference year. The
harmonised survey is transformed into an input file for EUROMOD, the
European tax-benefit microsimulation model, which applies the French 2015
policy system to produce simulated disposable resources. Regional
labour-market conditions come from the Eurostat regional labour-force
series described in the data section. Access to EU-SILC microdata is
granted by Eurostat under its research-access conditions; the data cannot
be redistributed with this document.

**Sample.** Single-adult and opposite-sex couple households, constructed
by the rules stated in the sample section: 1,540 single-adult and 2,223
couple households enter estimation.

**Estimator and inference.** Conditional likelihood over sampled
alternatives with an out-of-fold proposal correction, 100 draws per
household; household-clustered CR1 standard errors. Optimisation is
verified by multiple polished starts with identical active sets, and
curvature by exact Hessian eigenvalues; both are reported with the
estimates.

**Software.** The model is implemented in Python with JAX for automatic
differentiation, and priced through the EUROMOD connector. Version
identifiers are recorded with the estimation output.

**Replication.** Code and derived, non-confidential intermediate artefacts
will be made available in a public repository on publication. Confidential
microdata remain in their permitted environment; the replication package
therefore reproduces every step conditional on authorised access to
EU-SILC.

**What is not yet settled.** Two specification decisions and one welfare
dependency are open and are described where they arise rather than here:
the couples experience block, the consumption-curvature restriction, and
the re-evaluation of the welfare layer on the corrected frame.
'''

def resolve(text, target):
    text=re.sub(r'\{\{table:(.*?)\}\}',lambda m:TABLES[m[1]],text)
    def fig(m):
        stem,cap=CAPTIONS[m[1]]
        if m[1].startswith('figP') and not PREF_FRESH:
            return ('\n> **Figure awaiting regeneration \u2014 ' + stem +
                    '.** Not embedded: ' + PREF_WHY + '. Caption of record: ' +
                    cap + '\n')
        path='figures/v3/'+stem+'.png' if target=='paper' else str(FIG/(stem+'.png')).replace('\\','/')
        return f'\n![{cap}]({path}){{width=95%}}\n'
    text=re.sub(r'\{\{figure:(.*?)\}\}',fig,text)
    # Blocks marked appendix-only stay inline in the teaching report and
    # are lifted into the paper's appendix, so the paper's main text
    # carries the four selected panels and not all six.
    if target=='paper':
        for _blk in re.findall(r'\{\{appendix-only\}\}(.*?)\{\{/appendix-only\}\}',text,flags=re.S):
            PAPER_APPENDIX_FIGS.append(_blk)
        text=re.sub(r'\{\{appendix-only\}\}.*?\{\{/appendix-only\}\}','',text,flags=re.S)
    else:
        text=text.replace('{{appendix-only}}','').replace('{{/appendix-only}}','')
    text=text.replace('{{provenance}}',PROVENANCE)
    # The one sentence of the abstract that awaits the corrected welfare
    # numbers carries a visible token. The document verifier counts it.
    text=text.replace('{{PENDING-WELFARE}}',
                      '**[AWAITING PARAMETER INTERVALS ON THESE SHARES]**')
    # Evidence that is commissioned but not yet returned. Each token is
    # visible in the text and counted by the document verifier.
    text=text.replace('{{PENDING-HINV}}',
                      'That check is commissioned and its result is not yet on record, so the separation is argued here from the construction rather than shown; the figure quoted above is the total movement, across every route by which the equalisation reaches the measure, and not the direct channel alone.')
    # PENDING-COND retired: COND-1 has returned and the
    # standardized diagnostic is reported in the fit section.
    s='example__single__baseline__'; c='example__couple__baseline__'
    worked=(r'$$\begin{aligned} W_{\rm single}&\simeq '+val(s+'lambda','.2f')+
            r'\left[1+'+val(s+'theta','.6f')+r'('+val(s+'logJ','.5f')+'-'+val(s+'logH','.5f')+
            r')\right]^{1/'+val(s+'theta','.6f')+r'}\simeq '+val(s+'W','.2f')+r'\ \text{EUR/month},\\'+
            r'W_{\rm couple}&\simeq '+val(c+'lambda','.2f')+r'\exp('+val(c+'logJ','.5f')+'-'+val(c+'logH','.5f')+
            r')\simeq '+val(c+'W','.2f')+r'\ \text{EUR/month}.\end{aligned}$$')
    text=text.replace('{{worked_identity}}',worked)
    # {{n:key}} or {{n:key|fmt}} -- an explicit format keeps values that are
    # read against each other on one precision, which '.6g' does not.
    text=re.sub(r'\{\{n:([^|}]+?)(?:\|([^}]+))?\}\}',
                lambda m:val(m[1],m[2] or None),text)
    assert '{{' not in text, 'Unresolved template'
    return text

bib=(PAPER/'JMP_working_paper_for_seminar_v2.bib').read_text('utf-8')+r'''
@article{aaberge2004,
 author={Aaberge, Rolf and Colombino, Ugo and Str{\o}m, Steinar},
 title={Do more equal slices shrink the cake? An empirical investigation of tax-transfer reform proposals in Italy},
 journal={Journal of Population Economics},year={2004},volume={17},pages={767--785},doi={10.1007/s00148-004-0193-2}}
@unpublished{haydarmaniquet,
 author={Haydar, Hisham and Maniquet, Fran{\c c}ois},
 title={Jobs and Well-Being Measurement},year={2026},note={Work in progress}}
'''
BIB=PAPER/'JMP_working_paper_for_seminar_v4.bib'
BIB.write_text(bib,encoding='utf-8')
today=dt.datetime.now().strftime('%d %B %Y')
report=f'# {TITLE}\n\nHisham Haydar · University of Luxembourg and LISER\n\nBuild date: {today}. Intended first complete circulation: 10 September 2026.\n\n## Abstract\n\n{resolve(ABSTRACT, 'report')}\n\n*{VERSION}*\n'
for i,(title,body) in enumerate(SECTIONS,1):
    report+=f'\n# {i}. {title}\n'+resolve(body,'report')
report+='\n# Questions for presentation preparation\n'
for i,(q,ans) in enumerate(QA,1): report+=f'\n## {i}. {q}\n\n{ans}\n'
report+='\n# Bibliography\n\n::: {#refs}\n:::\n'
(HERE/'story_v3.generated.md').write_text(report,encoding='utf-8')

paper=f'\\begin{{abstract}}\n{resolve(ABSTRACT, 'paper')}\n\\end{{abstract}}\n\n*{VERSION}*\n\n'
groups=[('Introduction',[0]),('Related literature',[2]),('Conceptual framework',[1]),('Data and institutional setting',[3,4,5]),('Structural household model and identification',[6,8]),('Estimation and numerical implementation',[9,10]),('Behavioural estimates and fit',[11,12,7]),('Money-metric well-being and decomposition',[13,14,15,16,17]),('Welfare results, comparisons and conclusion',[18])]
for title,inds in groups:
    paper+=f'\n# {title}\n'
    for idx in inds:
        st,body=SECTIONS[idx]
        body=re.sub(r'^### ', '### ',body,flags=re.M)
        paper+=f'\n## {st}\n'+resolve(body,'paper')
paper+='\n\\appendix\n\n# Historical implementation and reproducibility\n'
paper+=resolve(SECTIONS[19][1],'paper')
paper+='\n## Data, software and replication\n'+resolve(SECTIONS[20][1],'paper')
if PAPER_APPENDIX_FIGS:
    paper+='\n## Further preference diagnostics\n'+''.join(PAPER_APPENDIX_FIGS)

header=r'''\documentclass[11pt,a4paper]{article}
\usepackage[margin=25mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern,amsmath,amssymb,booktabs,longtable,array,graphicx,calc}
\usepackage{xurl}
\usepackage[round]{natbib}
\usepackage[colorlinks=true,allcolors=blue]{hyperref}
\usepackage{bookmark}
\usepackage{caption}
\captionsetup{font=small,labelfont=bf}
\setlength{\emergencystretch}{3em}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\providecommand{\pandocbounded}[1]{#1}
\title{'''+TITLE+r'''}
\author{Hisham Haydar\\University of Luxembourg and LISER}
\date{Build: '''+today+r'''\\Discussion draft; intended circulation 10 September 2026}
\begin{document}
\maketitle
'''
body=pypandoc.convert_text(paper,'latex',format='markdown+raw_tex+tex_math_dollars',extra_args=['--natbib','--wrap=none']).replace('\r\n','\n')
body=body.replace(r'\def\LTcaptype{none}', '')
def wrap_table(m):
    n=len(m[1]); first=.10 if n==7 else (.25 if n>=4 else .48)
    total=.91
    widths=[first]+[(total-first)/(n-1)]*(n-1)
    return r'\begin{longtable}[]{@{}'+''.join(r'>{\raggedright\arraybackslash}p{'+f'{w:.4f}'+r'\linewidth}' for w in widths)+r'@{}}'
body=re.sub(r'\\begin\{longtable\}\[\]\{@\{\}([lrc]+)@\{\}\}',wrap_table,body)
body=body.replace(r'\begin{longtable}',r'\small\setlength{\tabcolsep}{3pt}\begin{longtable}')
# Long provenance paths are breakable; they are confined to the appendix.
body=re.sub(r'\\texttt\{([^{}]+)\}',lambda m:r'\path{'+m[1].replace(r'\_','_')+'}',body)
# Image widths from pandoc's percentage syntax use linewidth.
tex=header+body+'\n\\bibliographystyle{plainnat}\n\\bibliography{JMP_working_paper_for_seminar_v4}\n\\end{document}\n'
(PAPER/'JMP_working_paper_for_seminar_v4.tex').write_text(tex,encoding='utf-8')

rendered=pypandoc.convert_text(report,'html5',format='markdown+tex_math_dollars',extra_args=['--mathjax','--citeproc','--bibliography='+str(BIB),'--wrap=none']).replace('\r\n','\n')
def embed(m):
    path=Path(html.unescape(m[1]))
    # keep the figure's stem on the tag: the data URI erases the filename, and
    # the document check needs to know which panel this is.
    return ('src="data:image/png;base64,'
            +base64.b64encode(path.read_bytes()).decode()
            +'" data-fig="'+path.stem+'"')
rendered=re.sub(r'src="([^"]+\.png)"',embed,rendered)
# Keep scientific history and identifiers available, but outside the main reading flow.
for heading in ['19. Research history and implications for interpretation','20. Reproducibility, the existing notebook and open calculations']:
    pattern=r'(<h1[^>]*>'+re.escape(heading)+r'</h1>)(.*?)(?=<h1|\Z)'
    rendered=re.sub(pattern,lambda m:'<details><summary>'+heading+'</summary>'+m[2]+'</details>',rendered,flags=re.S)
vendor=HERE/'vendor/tex-svg.js'
vendor.parent.mkdir(exist_ok=True)
if not vendor.exists():
    urllib.request.urlretrieve('https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-svg.js',vendor)
mathjax=vendor.read_text('utf-8')
# ---- v4 shell: the v2 report interface around the v3 body (R1, ruling C) ----
# Sticky left navigation, the v2 palette and its themed explanatory boxes are
# restored. The rendered body, every number and the bundled offline renderer are
# exactly the v3 ones; only the surrounding shell changes.
css=(":root{--ink:#1a1a1a;--mut:#5a5f66;--line:#dcdfe4;--bg:#fff;--soft:#f6f7f9;"
 "--accent:#1f4e79;--accent2:#7a3b12;--warn:#8a1c1c;--ok:#14612e}"
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
 "#toc a{display:block;padding:4px 8px;color:var(--ink);text-decoration:none;"
 "border-radius:4px;border-left:2px solid transparent}"
 "#toc a:hover{background:#e9ecf1}"
 "#toc a.sub{padding-left:20px;color:var(--mut);font-size:12px}"
 "#toc a.on{background:#e3eaf3;border-left-color:var(--accent);font-weight:600}"
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
 "table{border-collapse:collapse;width:100%;font:13.5px/1.5 -apple-system,"
 "BlinkMacSystemFont,'Segoe UI',sans-serif;margin:1.5em 0}"
 "td,th{padding:8px 9px;border-bottom:1px solid var(--line);text-align:left;"
 "vertical-align:top}th{background:#eef3f5}"
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
 "a{color:var(--accent)}"
 "@media(max-width:1100px){#wrap{display:block}#toc{position:static;"
 "height:auto;width:auto;flex:none;border-right:0;"
 "border-bottom:1px solid var(--line)}#doc{padding:24px 20px 80px}}"
 "@media print{#toc{display:none}#doc{max-width:none;padding:0}"
 "body{font-size:11pt}details{display:block}}")

# navigation, derived from the document's own headings
def _slug(t,_seen={}):
    b=re.sub(r'[^a-z0-9]+','-',re.sub(r'<[^>]+>','',t).lower()).strip('-')[:60] or 'sec'
    _seen[b]=_seen.get(b,0)+1
    return b if _seen[b]==1 else '%s-%d'%(b,_seen[b])

_nav=[]
def _anchor(m):
    lvl,inner=m[1],m[2]
    sid=_slug(inner)
    _nav.append((lvl,sid,re.sub(r'<[^>]+>','',inner)))
    return '<h%s id="%s">%s</h%s>'%(lvl,sid,inner,lvl)
rendered=re.sub(r'<h([12])[^>]*>(.*?)</h\1>',_anchor,rendered,flags=re.S)

toc_html='<h2>Contents</h2>'+''.join(
    '<a class="%s" href="#%s">%s</a>'%('' if l=='1' else 'sub',sid,txt)
    for l,sid,txt in _nav)

htmlout=('<!doctype html><html lang="en"><head><meta charset="utf-8">'
 '<meta name="viewport" content="width=device-width,initial-scale=1"><title>'
 +TITLE+'</title><style>'+css+'</style>'
 '<script>window.MathJax={tex:{inlineMath:[["\\\\(","\\\\)"]],'
 'displayMath:[["\\\\[","\\\\]"]]},svg:{fontCache:"local"},'
 'options:{enableMenu:false}};</script><script>'+mathjax+'</script>'
 '</head><body><div id="wrap"><nav id="toc">'+toc_html+'</nav>'
 '<main id="doc">'+rendered+'</main></div>'
 '<script>(function(){var ls=[].slice.call(document.querySelectorAll("#toc a")),'
 'hs=ls.map(function(a){return document.getElementById('
 'a.getAttribute("href").slice(1));});'
 'function on(){var y=scrollY+120,k=0;hs.forEach(function(h,i){'
 'if(h&&h.offsetTop<=y)k=i;});ls.forEach(function(a,i){'
 'a.className=a.className.replace(/ ?on/,"")+(i===k?" on":"");});}'
 'addEventListener("scroll",on,{passive:true});on();})();</script>'
 '</body></html>')

(ROOT/'reports/JMP_research_story_report_v4.html').write_text(htmlout,encoding='utf-8')
REGOUT={'build_date':today,'result_status':'historical evaluator; corrected estimation pending','entries':REG,'used_keys':sorted(USED)}
(ROOT/'reports/numbers_of_record_v4.json').write_text(json.dumps(REGOUT,indent=2,ensure_ascii=False),encoding='utf-8')
print('Built shared HTML/TeX, bibliography, tables and figures; compile PDF next.')
