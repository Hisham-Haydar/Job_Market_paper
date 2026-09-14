"""Corrected render inputs for report/paper v7.

Unaffected tables, figures and scalar entries are inherited from v6.  The fit
surfaces are rebuilt from POSFIT-v3b and Band-Fix-2 only.
"""
from copy import deepcopy
from pathlib import Path
import csv
import hashlib
import json
import re
import shutil

import matplotlib.pyplot as plt
import pandas as pd

import v6_render_inputs as frozen

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PAPER = ROOT / 'manuscript'
FIG = PAPER / 'figures/v7'
TABLE = PAPER / 'tables/v7'
FIG.mkdir(parents=True, exist_ok=True)
TABLE.mkdir(parents=True, exist_ok=True)

MNL_POSFIT = ROOT.parent / 'MNL_posfit'
POSFIT = MNL_POSFIT / 'outputs/positive_fit_diagnostics_v3b'
NODE = MNL_POSFIT / 'outputs/posfit_node_convergence_v3b'
BAND_FIX_2 = (MNL_POSFIT / 'experiments/JMP_SEMINAR_SPRINT/runs/'
              'bandfix2_recompute')
NEW_RESULTS = BAND_FIX_2 / 'new_results_v1.json'

REG = deepcopy(frozen.REG)
TABLES = deepcopy(frozen.TABLES)
CAPTIONS = deepcopy(frozen.CAPTIONS)
USED = set()
DIAG_SHA256 = frozen.DIAG_SHA256

# The coefficient estimates are unchanged, but v6 inherited S12-native labels
# for the S11 hours-density coefficients.  Correct only this structural table;
# descriptive reporting bins (including [36.5, 37.5)) remain independent.
TABLES['access'] = (TABLES['access']
    .replace('width 26.5 hours per week', 'width 29.5 hours per week')
    .replace('Part-time lower, [17.5, 21.5)', 'Part-time lower, [18.5, 21.5)')
    .replace('Part-time upper, [28.5, 30.5)', 'Part-time upper, [29.5, 30.5)')
    .replace('Full-time upper, [36.5, 40.5]', 'Full-time upper, [37.5, 40.5]'))


def register(key, value, source, status='corrected result', units='dimensionless'):
    REG[key] = {'value': value, 'source': source, 'status': status, 'units': units}


new = json.loads(NEW_RESULTS.read_text('utf-8'))
summaries = new['summaries']
moments = pd.DataFrame(new['moments'])
mom_source = ('MNL_posfit/experiments/JMP_SEMINAR_SPRINT/runs/'
              'bandfix2_recompute/new_results_v1.json')
register('mae_singles', summaries['SINGLES']['mean_absolute_error'],
         mom_source + '::summaries.SINGLES.mean_absolute_error', units='mean absolute deviation')
register('mae_couples', summaries['COUPLES']['mean_absolute_error'],
         mom_source + '::summaries.COUPLES.mean_absolute_error', units='mean absolute deviation')
register('mae_ruma', summaries['RUM-A']['mean_absolute_error'],
         mom_source + '::summaries.RUM-A.mean_absolute_error', units='mean absolute deviation')
register('mae_rumb', summaries['RUM-B']['mean_absolute_error'],
         mom_source + '::summaries.RUM-B.mean_absolute_error', units='mean absolute deviation')
register('hours_reference_width', 29.5,
         'MNL_posfit/outputs/positive_fit_diagnostics_v3b/run_provenance.json::evaluation_model_band_edges',
         status='S11/S10 definition', units='hours')

sm = moments[(moments.model == 'SINGLES') & (moments.sex == 'male')]
sm37 = sm[sm.moment == 'hours::h_36_5_37_5'].iloc[0]
register('singlesmale_hours_gap_pp',
         100 * (float(sm37.observed) - float(sm37.predicted)),
         mom_source + '::moments[SINGLES,male,hours::h_36_5_37_5]',
         status='corrected diagnostic', units='percentage points')


def table(name, caption, headers, rows):
    with (TABLE / (name + '.csv')).open('w', newline='', encoding='utf-8') as handle:
        writer = csv.writer(handle)
        writer.writerow(headers)
        writer.writerows(rows)
    return ('\n' + caption + '\n\n|' + '|'.join(headers) + '|\n|'
            + '|'.join(['---'] * len(headers)) + '|\n'
            + ''.join('|' + '|'.join(str(value).replace('|', '/') for value in row)
                      + '|\n' for row in rows) + '\n')


MOMLAB = {
    'employment': 'Employment',
    'mean_log_wage': 'Mean log wage',
    'hours::zero': 'Hours: non-employment',
    'hours::h_0_10': 'Hours: [5, 10)',
    'hours::h_10_18_5': 'Hours: [10, 18.5)',
    'hours::pt1': 'Structural PT1: [18.5, 21.5)',
    'hours::h_21_5_29_5': 'Hours: [21.5, 29.5)',
    'hours::pt2': 'Structural PT2: [29.5, 30.5)',
    'hours::h_30_5_33_5': 'Hours: [30.5, 33.5)',
    'hours::f35': 'Hours: [33.5, 36.5)',
    'hours::h_36_5_37_5': 'Observed 37-hour mass point: [36.5, 37.5)',
    'hours::ft': 'Structural FT: [37.5, 40.5]',
    'hours::h_40_5_44_5': 'Hours: (40.5, 44.5)',
    'hours::lh': 'Hours: [44.5, 70]',
}


def moment_label(moment):
    if moment in MOMLAB:
        return MOMLAB[moment]
    if moment.startswith('occupation::'):
        return 'Occupation group ' + moment.split('::')[1]
    if moment.startswith('quadrant::'):
        return 'Joint regime ' + {
            'NN': 'neither works', 'MO': 'man only',
            'WO': 'woman only', 'BB': 'both work'}[moment.split('::')[1]]
    return moment


for tag, model in [('singles', 'SINGLES'), ('couples', 'COUPLES')]:
    rows = []
    data = moments[moments.model == model]
    for sex in ('household', 'male', 'female'):
        for _, row in data[data.sex == sex].iterrows():
            rows.append([
                {'household': 'Household', 'male': 'Man', 'female': 'Woman'}[sex],
                moment_label(row.moment),
                format(float(row.observed), '.4f'),
                format(float(row.predicted), '.4f'),
                format(float(row.absolute_error), '.4f'),
                row.denominator,
            ])
    TABLES['fit' + tag] = table(
        'v7_fit_' + tag,
        'Table: Corrected observed against model population moments, ' + tag + '. '
        'Structural PT1, PT2 and FT rows use the S11/S10 definitions; the other '
        'hours rows are mutually exclusive descriptive residual categories, '
        'including the observed 37-hour mass-point cell. Predictions were fully '
        're-evaluated after rebuilding the structural indicators; no row is a '
        'relabelling of the superseded evaluation.',
        ['Unit', 'Moment', 'Observed', 'Model', 'Absolute deviation', 'Denominator'],
        rows)

TABLES['benchmark'] = table(
    'v7_benchmark',
    'Table: The estimated singles model against two re-estimated common-opportunity '
    'benchmarks. Estimates and maximized criteria are unchanged; criterion-B '
    'population moments are corrected to the S11/S10 structural-band definitions. '
    'The RUM-A estimation-input band defect and its cancellation in the conditional '
    'likelihood are disclosed in the limitations.',
    ['Specification', 'Free coordinates', 'Criterion', 'Difference', 'Population fit'],
    [
        ['Latent jobs with household-specific opportunities', '41', '6253.463', '--',
         format(summaries['SINGLES']['mean_absolute_error'], '.4f')],
        ['Benchmark A: common opportunity distribution, preferences re-estimated',
         '10', '6403.974', '+150.51', format(summaries['RUM-A']['mean_absolute_error'], '.4f')],
        ['Benchmark B: common opportunity shape, employment and hours moved into utility',
         '16', '6395.108', '+141.64', format(summaries['RUM-B']['mean_absolute_error'], '.4f')],
    ])


def md_figure(path, caption):
    return '\n![' + caption + '](' + path.as_posix() + '){width=95%}\n'


def make_fit_band():
    bands = pd.read_csv(POSFIT / 'model_simulated_bands.csv')
    g2 = pd.read_csv(POSFIT / 'g2_adequacy.csv')
    bands = bands[(bands.weighting == 'weighted') & (bands.scope == 'all') &
                  (bands.statistic == 'extensive_accuracy') & (bands.support == 'full')]
    gate = g2[(g2.weighting == 'weighted') & (g2.scope == 'all') &
              (g2.statistic == 'extensive_accuracy')]
    data = bands.merge(gate[['group', 'adequate']], on='group')
    data = data[data.adequate].set_index('group').loc[['singles_female', 'couples_female']]
    labels = ['Single women', 'Coupled women']
    observed = data.observed.to_numpy(float) * 100
    lo = data.simulated_p025.to_numpy(float) * 100
    hi = data.simulated_p975.to_numpy(float) * 100
    fig, ax = plt.subplots(figsize=(7.8, 3.6))
    y = range(len(data))
    ax.hlines(y, lo, hi, color='#5b7794', linewidth=8, alpha=.38,
              label='model-simulated 95% band')
    ax.scatter(observed, y, color='#b44b28', s=72, zorder=3, label='observed accuracy')
    ax.set_yticks(list(y), labels)
    ax.set_xlabel('Weighted extensive-margin accuracy (%)')
    ax.set_title('Reportable accuracy statistics after the corrected adequacy gate')
    ax.grid(axis='x', alpha=.22)
    ax.legend(frameon=False, loc='lower right')
    ax.set_xlim(min(lo) - 2, max(hi) + 2)
    fig.tight_layout()
    out = FIG / 'fitext_band_v3b.png'
    fig.savefig(out, dpi=200, bbox_inches='tight')
    plt.close(fig)
    return out


def make_margin_fit():
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.4), sharex=True, sharey=True)
    for ax, (model, title) in zip(axes, [('SINGLES', 'Single adults'), ('COUPLES', 'Couples')]):
        data = moments[(moments.model == model) &
                       ~moments.moment.isin(['mean_log_wage'])]
        for sex, marker, color in [('household', 's', '#666666'),
                                   ('male', 'o', '#305f8d'),
                                   ('female', '^', '#b44b28')]:
            part = data[data.sex == sex]
            if len(part):
                ax.scatter(part.observed, part.predicted, s=27, marker=marker,
                           color=color, alpha=.8, label=sex.capitalize())
        ax.plot([0, .9], [0, .9], color='black', linewidth=1, alpha=.45)
        ax.set_title(title)
        ax.grid(alpha=.18)
        ax.set_xlabel('Observed share')
    axes[0].set_ylabel('Predicted share')
    axes[1].legend(frameon=False, fontsize=8)
    fig.suptitle('Corrected population moments: observed versus predicted')
    fig.tight_layout()
    out = FIG / 'fit_by_margin_v7.png'
    fig.savefig(out, dpi=200, bbox_inches='tight')
    plt.close(fig)
    return out


fit_band_path = make_fit_band()
fit_path = make_margin_fit()
node_path = FIG / 'node_convergence_v3b.png'
shutil.copyfile(NODE / 'figures/node_convergence.png', node_path)

CAPTIONS['fitband'] = md_figure(
    fit_band_path,
    '**Corrected weighted extensive accuracy.** Only single women and coupled '
    'women clear the preregistered numerical-adequacy gate. The statistics for '
    'single men and coupled men are quadrature-limited and withheld. Source: '
    'POSFIT v3b.')
CAPTIONS['nodeconvergence'] = md_figure(
    node_path,
    '**Corrected predictive/integration-node convergence.** Weighted predicted '
    'participation over fixed-seed node subsets; the shaded area is the numerical '
    '10--90% envelope and observed participation is the horizontal reference. '
    'Source: POSFIT node convergence v3b.')
CAPTIONS['fit'] = md_figure(
    fit_path,
    '**Corrected population fit.** Observed against fully re-evaluated S11 model '
    'shares using S11/S10 structural-band indicators. The observed 37-hour '
    'mass-point cell is a descriptive residual category outside structural FT.')

CAPTIONS['theory'] = CAPTIONS['theory'].replace(
    'the estimated measure is its ex-ante extension, defined in Section 4.',
    'the current empirical Mapping-F measure evaluates the attained bundle '
    'against the non-employment reference state, as defined in Section 4.')


def strip_modes(text, target):
    for tag in ('report-only', 'paper-only'):
        if tag == target + '-only':
            text = text.replace('{{' + tag + '}}', '').replace('{{/' + tag + '}}', '')
        else:
            text = re.sub(r'\{\{' + tag + r'\}\}.*?\{\{/' + tag + r'\}\}',
                          '', text, flags=re.S)
    return text


def val(key, fmt=None):
    USED.add(key)
    value = REG[key]['value']
    if key.endswith('_year'):
        return str(value)
    if fmt:
        return format(float(value), fmt)
    if isinstance(value, float):
        return format(value, '.6g')
    if isinstance(value, int):
        return format(value, ',d')
    return str(value)


def resolve(text, target):
    text = strip_modes(text, target)
    text = re.sub(r'\{\{table:(.*?)\}\}', lambda match: TABLES[match[1]], text)

    def figure(match):
        value = CAPTIONS[match[1]]
        if target == 'paper':
            value = value.replace(FIG.as_posix() + '/', 'figures/v7/')
            value = value.replace(frozen.FIG.as_posix() + '/', 'figures/v5/')
        return value

    text = re.sub(r'\{\{figure:(.*?)\}\}', figure, text)
    text = re.sub(r'\{\{n:([^|}]+?)(?:\|([^}]+))?\}\}',
                  lambda match: val(match[1], match[2]), text)
    if '{{' in text:
        raise SystemExit('Unresolved v7 token')
    return text


POSFIT_RUN_SHA256 = hashlib.sha256((POSFIT / 'run_provenance.json').read_bytes()).hexdigest().upper()
