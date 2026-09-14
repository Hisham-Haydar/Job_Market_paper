#!/usr/bin/env python
"""The v5 consistency gate.

Two things this is and is not.

IT IS the verifier for the v5 artifact pair. It carries forward every content
rule of `consistency_gate_spec_v1.md` that still applies to the S11
specifications of record, adds the rules of `canonical_notation_v5.md`, and adds
the SINGLE CURRENT MODEL check the v5 instruction requires.

IT IS NOT a replacement for `run_consistency_gate.py`. That runner is bound to
the v1/v2 artifact family: it parses a markdown paper that v5 does not produce,
an HTML section structure v5 does not use, and a registry key space
(`numbers_of_record_v1.json`) that v5 replaced. It also enforces two clauses of
its own specification that the current model contradicts -- `beta_c == 1` and
the F35 peak parameterisation -- so running it against v5 would fail the paper
for describing the model it estimates. It remains in the tree, unchanged, and
guards its own artifacts. `canonical_notation_v5.md` records exactly which of
its clauses are superseded and which are carried forward here.

Artifacts checked
    P   manuscript/JMP_working_paper_for_seminar_v5.tex
    H   reports/JMP_research_story_report_v5.html   (text layer)
    M   reports/research_story_build/story_v5.generated.md
    R   reports/numbers_of_record_v5.json

Exit code 0 if every item passes, 1 otherwise.
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Dict, List, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent))
import retired_lineage_gate as rlg  # noqa: E402

JMP = Path(__file__).resolve().parent.parent
PAPER = JMP / 'manuscript/JMP_working_paper_for_seminar_v5.tex'
HTML = JMP / 'reports/JMP_research_story_report_v5.html'
MD = JMP / 'reports/research_story_build/story_v5.generated.md'
REG = JMP / 'reports/numbers_of_record_v5.json'


# --------------------------------------------------------------------------- #
# artifact text layers
# --------------------------------------------------------------------------- #
class Text(HTMLParser):
    SKIP = {'script', 'style'}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth = 0
        self.buf: List[str] = []

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.depth += 1

    def handle_endtag(self, tag):
        if tag in self.SKIP and self.depth:
            self.depth -= 1

    def handle_data(self, d):
        if not self.depth:
            self.buf.append(d)


def html_text(path: Path) -> str:
    p = Text()
    p.feed(path.read_text(encoding='utf-8'))
    return ' '.join(p.buf)


def norm(s: str) -> str:
    s = unicodedata.normalize('NFKC', s)
    s = re.sub(r'\\(?:mathrm|mathbb|text|emph|textbf|mathcal)\{([^{}]*)\}',
               r'\1', s)
    s = re.sub(r'[*`$\\]', '', s)
    return re.sub(r'\s+', ' ', s).strip().lower()


PAPER_RAW = PAPER.read_text(encoding='utf-8')
HTML_RAW = HTML.read_text(encoding='utf-8')
MD_RAW = MD.read_text(encoding='utf-8')
HTML_TXT = html_text(HTML)
REGJ = json.loads(REG.read_text(encoding='utf-8'))

ART: Dict[str, str] = {'P': PAPER_RAW, 'H': HTML_TXT, 'M': MD_RAW}
NORM: Dict[str, str] = {k: norm(v) for k, v in ART.items()}
NAMES = {'P': 'paper v5 (LaTeX)', 'H': 'report v5 (rendered text)',
         'M': 'report v5 (markdown source)'}


# --------------------------------------------------------------------------- #
@dataclass
class Item:
    num: int
    title: str
    verdict: str = 'PASS'
    detail: List[str] = field(default_factory=list)

    def fail(self, msg: str) -> None:
        self.verdict = 'FAIL'
        self.detail.append(msg)

    def note(self, msg: str) -> None:
        self.detail.append(msg)


ITEMS: List[Item] = []


def item(num: int, title: str) -> Item:
    it = Item(num, title)
    ITEMS.append(it)
    return it


def forbid(it: Item, needle: str, arts: str = 'PHM',
           permitted: Tuple[str, ...] = (), case: bool = False) -> None:
    """Fail if `needle` occurs outside its permitted surrounding contexts.

    `case=True` searches the raw text and is case-sensitive: the specification
    flags upper-case STATUS TOKENS and internal run labels, and exempts the
    ordinary English words that share their letters ("described as pending in
    earlier drafts" is prose, not a status stamp).
    """
    for a in arts:
        hay = ART[a] if case else NORM[a]
        n = needle if case else norm(needle)
        start = 0
        while True:
            k = hay.find(n, start)
            if k < 0:
                break
            window = hay[max(0, k - 300): k + 300]
            wnorm = window if case else window
            if not any((p if case else norm(p)) in wnorm for p in permitted):
                it.fail('%s: %r at offset %d' % (NAMES[a], needle, k))
                break
            start = k + len(n)


# --------------------------------------------------------------------------- #
# 1.  SINGLE CURRENT MODEL  (the new v5 requirement)
# --------------------------------------------------------------------------- #
def _history_spans(raw: str, art: str) -> List[Tuple[int, int]]:
    """Character spans of the history section, in the normalised text.

    EVERY occurrence of the heading is used, not the first: the report's table
    of contents repeats it, and taking only the first occurrence would place the
    permitted span over the navigation rather than over the section.
    """
    hay = NORM[art]
    spans = []
    for m in re.finditer(re.escape(norm('scientific history of this result')),
                         hay):
        end = hay.find('bibliography', m.end())
        spans.append((m.start(), end if end > m.start() else len(hay)))
    return spans


it = item(1, 'SINGLE CURRENT MODEL: one specification, everywhere')
# 1a. the superseded consumption conventions may appear only inside history
SUPERSEDED = [
    ('beta_c = 1', [r'beta_c\s*=\s*1(?![0-9.])', r'\\beta_c\s*=\s*1(?![0-9.])',
                    r'\\beta_c\\equiv\s*1', r'beta_c\\equiv 1']),
    ('theta_c = 0.168', [r'0\.168']),
]
# A COUNTERFACTUAL mention is not an assertion of the model: the paper must be
# able to say that the measure would be an arithmetic mean only AT beta_c = 1,
# and to draw that comparison line on a figure. What is forbidden is asserting
# the superseded convention as the specification in force.
COUNTERFACTUAL = ('only at', 'would be', 'comparison at', 'linear comparison',
                  'flat comparison', 'is arithmetic only', 'against the linear',
                  'against the flat')
for label, pats in SUPERSEDED:
    for a in 'PHM':
        hay = NORM[a]
        spans = _history_spans(ART[a], a)
        for pat in pats:
            for m in re.finditer(pat, hay):
                if any(lo <= m.start() <= hi for lo, hi in spans):
                    continue
                w = hay[max(0, m.start() - 200): m.start() + 200]
                if any(c in w for c in COUNTERFACTUAL):
                    continue
                it.fail('%s: superseded convention %s asserted outside the '
                        'history section, at offset %d: %r'
                        % (NAMES[a], label, m.start(),
                           hay[max(0, m.start() - 70):m.start() + 70]))
    if it.verdict == 'PASS':
        it.note('%s: absent outside history in all three artifacts' % label)

# 1b. the current conventions are stated positively
for need in ['theta_c', 'beta_c']:
    for a in 'PHM':
        if norm(need) not in NORM[a]:
            it.fail('%s: does not state %s at all' % (NAMES[a], need))
for a in 'PHM':
    if 'estimated' not in NORM[a] or 'consumption weight' not in NORM[a]:
        it.fail('%s: does not state that the consumption weight is estimated'
                % NAMES[a])
# 1c. the registry declares the model of record
if 'beta_c estimated' not in REGJ.get('model_of_record', ''):
    it.fail('registry: model_of_record does not name the estimated '
            'consumption weight')
# 1d. exactly one value of beta_c per population reaches the text
for a in 'PHM':
    seen_bc = set(re.findall(r'2\.0387\d*', NORM[a])) | set(
        re.findall(r'2\.1017\d*', NORM[a]))
    if not seen_bc:
        it.fail('%s: neither estimated consumption weight appears' % NAMES[a])
it.note('current model: tau = 1, theta_c = 0 exactly, beta_c estimated')


# --------------------------------------------------------------------------- #
# 2.  NOTATION  (spec v1 s1.2, s1.3; canon v5)
# --------------------------------------------------------------------------- #
it = item(2, 'Notation: forbidden symbol variants and the four-factor rule')
for bad in ['g^{Acc}', 'g^Acc', 'gAcc', 'log_gAcc', 'g^{market}', 'g^market',
            'g^{Market}', 'omega_ig', 'working_ij', 'age_i', 'nkids_i']:
    forbid(it, bad)
if '\u03c9_ig' in PAPER_RAW or '\u03c9_ig' in HTML_TXT:
    it.fail('omega_ig in its unicode spelling')
# the four-factor product, with all four canonical names and no fifth factor
for a in 'PM':
    hay = ART[a]
    ok = all(s in hay for s in ['g^{E}', 'g^{H}', 'g^{\\mathrm{Occ}}', 'g^{W}'])
    if not ok:
        it.fail('%s: the opportunity density is not stated with all four '
                'canonical factor names' % NAMES[a])
    else:
        it.note('%s: four-factor product stated with the canonical names'
                % NAMES[a])
# the proposal is never called an economic object
for phrase in ['proposal opportunity', 'proposal offer', 'proposal density is '
               'an opportunity']:
    forbid(it, phrase)


# --------------------------------------------------------------------------- #
# 3.  THE FIVE-BAND RULE  (canon v5, replacing spec v1 s1.4)
# --------------------------------------------------------------------------- #
it = item(3, 'The hours density: five bands over one residual reference')
for a in 'PM':
    hay = NORM[a]
    if 'five bands' not in hay:
        it.fail('%s: does not state the five-band structure' % NAMES[a])
    if '26.5' not in hay:
        it.fail('%s: does not state the residual reference width' % NAMES[a])
    if 'not an atom at thirty-five hours' not in hay and \
       'not an atom at 35 hours' not in hay:
        it.fail('%s: does not deny the 35-hour atom reading' % NAMES[a])
# the superseded parameterisation must not reappear
forbid(it, 'beta_F35 = 0')
forbid(it, '35-hour band is the reference')


# --------------------------------------------------------------------------- #
# 4.  THE W1 STATEMENT  (spec v1 s2)
# --------------------------------------------------------------------------- #
it = item(4, 'The W1 statement: all three clauses, and the accepted closed form')
CLAUSES = [
    ('own preferences retained',
     ['own preferences', "household's own preferences"]),
    ('own opportunity set retained',
     ['own set of reachable jobs', 'own reachable jobs', 'own opportunities',
      'own opportunity distribution']),
    ('consumption equalized across the reference alternatives',
     ['same disposable-consumption level to every job',
      'same flat monthly amount', 'flat consumption', 'equal-consumption']),
]
for a in 'PM':
    for name, alts in CLAUSES:
        if not any(norm(x) in NORM[a] for x in alts):
            it.fail('%s: the W1 statement is missing the clause %r'
                    % (NAMES[a], name))
# MEASURE-DEF-1: the accepted measure is the closed-form Mapping-F
# construction, not a power mean over a reference distribution -- that
# framing belonged to the retired ex-ante functional (see item 18). The
# requirement here is the closed form itself, not a word describing it.
for a in 'PM':
    if 'C_i^{\\mathrm{obs}}' not in ART[a]:
        it.fail('%s: the accepted Mapping-F closed form '
                '(C_i^{obs} exp[...]) is not stated' % NAMES[a])


# --------------------------------------------------------------------------- #
# 5.  PAY NEUTRALITY  (review finding 8)
# --------------------------------------------------------------------------- #
it = item(5, 'Pay neutrality is stated as the property established')
for a in 'PM':
    if 'directly pay-neutral' not in NORM[a]:
        it.fail('%s: the narrow pay-neutrality sentence is missing' % NAMES[a])
    if 'through the attained' not in NORM[a] and \
       'through attainment' not in NORM[a]:
        it.fail('%s: the attainment channel is not named beside it' % NAMES[a])
for bad in ['independence of pay fails', 'does not inherit independence of pay',
            'fails independence of pay']:
    forbid(it, bad)


# --------------------------------------------------------------------------- #
# 6.  SHAPLEY WORDING  (spec v1 s10; review finding 15)
# --------------------------------------------------------------------------- #
it = item(6, 'Shapley wording: attributed to, not removed')
forbid(it, 'removes 93.7')
for bad in ['the inequality removed by equalizing', 'share removes',
            'removed by preferences']:
    forbid(it, bad)
for a in 'PM':
    if 'average of marginal contributions over' not in NORM[a] and \
       'averages marginal contributions over' not in NORM[a]:
        it.fail('%s: does not state that a share averages over coalition '
                'orders' % NAMES[a])
    if 'is not the reduction' not in NORM[a]:
        it.fail('%s: does not distinguish a share from the one-factor effect'
                % NAMES[a])


# --------------------------------------------------------------------------- #
# 7.  THE MULTI-INDEX STATEMENT  (review finding 14)
# --------------------------------------------------------------------------- #
it = item(7, 'The preliminary P/A/B scale statement matches the computed shares '
              '(DECOMP-2)')
_D2DIR = JMP.parent / 'MNL_decomp' / 'outputs/welfare/preseminar_pab_v1'
import csv as _csv7  # noqa: E402
_D2SHAP = {}
for _s in ('singles', 'couples'):
    with (_D2DIR / ('shapley_PAB_%s.csv' % _s)).open(encoding='utf-8') as _f:
        _D2SHAP[_s] = {(row['scale'], row['factor']): row
                       for row in _csv7.DictReader(_f)}
# B (earning opportunities) must exceed A (coarse geographic/temporal access) in
# every sample x scale cell -- recomputed from the source CSVs, not trusted
# from the registry that wrote them.
_bdoma = []
for _s in ('singles', 'couples'):
    for _scale in ('unequivalised', 'equivalised'):
        _a = float(_D2SHAP[_s][(_scale, 'A')]['share_of_delta_I'])
        _b = float(_D2SHAP[_s][(_scale, 'B')]['share_of_delta_I'])
        _bdoma.append((_s, _scale, _b > _a))
        if not _b > _a:
            it.fail('B does not exceed A for %s, %s (recomputed from '
                    'shapley_PAB_%s.csv)' % (_s, _scale, _s))
if all(ok for *_, ok in _bdoma):
    it.note('B (earning opportunities) exceeds A (coarse geographic/temporal '
            'access) in all %d sample x scale cells, recomputed from '
            'DECOMP-2' % len(_bdoma))
# P's sign must actually differ between scales in both samples -- this is
# the basis for the "no directional claim about P" statement.
for _s in ('singles', 'couples'):
    _pu = float(_D2SHAP[_s][('unequivalised', 'P')]['gini_point_contribution'])
    _pe = float(_D2SHAP[_s][('equivalised', 'P')]['gini_point_contribution'])
    if (_pu >= 0) == (_pe >= 0):
        it.fail('%s: P has the same sign at both scales (%.6f, %.6f) -- the '
                '"no directional claim" statement is not grounded' % (_s, _pu, _pe))
for a in 'PM':
    if ('earning-opportunity heterogeneity has a larger contribution than '
            'the coarse geographic/temporal access channel') not in NORM[a]:
        it.fail('%s: does not state the robust B-over-A ordering' % NAMES[a])
    if ('preference contribution is not sign-robust to equivalisation' not in NORM[a]
            and 'no directional claim' not in NORM[a]):
        it.fail('%s: does not disclaim a direction for the preference '
                'contribution' % NAMES[a])
# the retired six-index statement must not resurface
forbid(it, 'under all six indices we report')
forbid(it, 'access exceeds earning opportunities for single adults')


# --------------------------------------------------------------------------- #
# 8.  COVERAGE: the two uncertainties stay apart  (spec v1 s4)
# --------------------------------------------------------------------------- #
it = item(8, 'The two decomposition uncertainty summaries (Monte Carlo range, '
              'second-seed check) are never called a confidence interval')
# The retired four-factor decomposition kept an RQMC integration band and a
# CR1 parameter interval separate; the current preliminary DECOMP-2 exercise
# instead reports a Monte Carlo simulation-replication range and an
# independent second-seed reproduction, with the same guarantee: neither is
# a confidence interval, and they are never merged into one.
for a in 'PM':
    if 'never merged' not in NORM[a] and 'never combined' not in NORM[a]:
        it.fail('%s: does not state that the two uncertainty summaries are '
                'kept apart' % NAMES[a])
    if 'never confidence intervals' not in NORM[a] and \
       'never a confidence interval' not in NORM[a]:
        it.fail('%s: does not state that the Monte Carlo range is not a '
                'confidence interval' % NAMES[a])
for bad in ['combined interval', 'merged interval', 'total uncertainty band']:
    forbid(it, bad)
_gini = [k for k in REGJ['entries'] if k.startswith('d2_gini')]
_seed = [k for k in REGJ['entries']
         if 'second_seed' in k or 'anchormove' in k]
if not _gini:
    it.fail('registry: no DECOMP-2 Gini-point contributions are registered')
else:
    it.note('registry: %d DECOMP-2 Gini-point contributions registered, all '
            'sourced from shapley_PAB_*.csv (Monte Carlo simulation, not a '
            'parameter draw)' % len(_gini))


# --------------------------------------------------------------------------- #
# 9.  NESTED SEMANTICS AND THE COUPLES D CELL  (spec v1 s5)
# --------------------------------------------------------------------------- #
it = item(9, 'DECOMP-2 is bounded: resources, needs and composition are held '
              'fixed; no total-inequality claim')
E0 = REGJ['entries']
for a in 'PM':
    if ('the decomposition is bounded by design because household resources, '
            'needs and composition are held fixed') not in NORM[a]:
        it.fail('%s: does not state that resources, needs and composition '
                'are held fixed using the approved boundedness wording' % NAMES[a])
    if 'means opportunities are unimportant' not in NORM[a] and \
       'not evidence that opportunities are unimportant' not in NORM[a] and \
       'not a finding that job opportunities are unimportant' not in NORM[a] and \
       'not a finding that opportunities are unimportant' not in NORM[a]:
        it.fail('%s: does not deny that the small movable share means '
                'opportunities are unimportant' % NAMES[a])
    if 'nested' in NORM[a] and 'subdivision' in NORM[a] and \
       'resources and household composition' in NORM[a]:
        it.fail('%s: retains language describing a resources/composition '
                'subdivision -- D is held fixed in this exercise, not '
                'decomposed' % NAMES[a])
    if 'delta i is small by construction' in NORM[a] or \
       'δi is small by construction' in NORM[a]:
        it.fail('%s: retains the forbidden small-by-construction claim' % NAMES[a])
for k in ['d2_deltaI_pct_singles_uneq', 'd2_deltaI_pct_singles_eq',
          'd2_deltaI_pct_couples_uneq', 'd2_deltaI_pct_couples_eq',
          'd2_varshare_logC_singles', 'd2_varshare_logC_couples']:
    if k not in E0:
        it.fail('registry: %s is missing, so the "held fixed" claim is not '
                'bound' % k)
# the stated Delta_I range and variance-share range are recomputed directly
# from the source CSVs, not trusted from the registry that wrote them
_d2vals = [float(E0['d2_deltaI_pct_%s_%s' % (s, sk)]['value'])
           for s in ('singles', 'couples') for sk in ('uneq', 'eq')]
_lo, _hi = min(_d2vals), max(_d2vals)
for a in 'PM':
    hay = ART[a]
    if ('%.1f' % _lo) not in hay or ('%.1f' % _hi) not in hay:
        it.fail('%s: the stated ΔI-share range does not match the '
                'registered min/max (%.1f to %.1f per cent)' % (NAMES[a], _lo, _hi))
    else:
        it.note('%s: ΔI-share range %.1f to %.1f per cent matches the '
                'registry' % (NAMES[a], _lo, _hi))


# --------------------------------------------------------------------------- #
# 10. FORBIDDEN TERMS AND MACHINE LABELS  (spec v1 s10; review finding 24)
# --------------------------------------------------------------------------- #
it = item(10, 'No machine labels, status tokens, private paths or slogans')
for bad in ['SCALE-1', 'S8', 'LOC4', 'PROVISIONAL', 'PENDING', 'CERTIFIED',
            'criterion-A', 'criterion-B', 'S10', 'S11', 'S12', 'RUM-A',
            'RUM-B']:
    forbid(it, bad, case=True)
forbid(it, 'beta_ll estimated')
for bad in ['companion project', 'one borrowed principle',
            'the normative half is settled next',
            'a retraction, at its exact scope',
            'the licensed statement is therefore',
            'nothing in this section is now awaiting']:
    forbid(it, bad)
for pat in [r'[A-Za-z]:\\\\Users', r'/c/Users/', r'\\\\Users\\\\hisham',
            r'outputs/corr/']:
    for a in 'PH':
        if re.search(pat, ART[a]):
            it.fail('%s: a private path or internal run label is visible (%s)'
                    % (NAMES[a], pat))
for bad in ['bootstrap']:
    forbid(it, bad, permitted=('not a bootstrap',))


# --------------------------------------------------------------------------- #
# 11. NUMBER BINDING: every reported number resolves to a source
# --------------------------------------------------------------------------- #
it = item(11, 'Every number is bound to a registered source')
E = REGJ['entries']
missing_src = [k for k, v in E.items() if not v.get('source')]
if missing_src:
    it.fail('registry: %d entries carry no source: %s'
            % (len(missing_src), missing_src[:5]))
used = set(REGJ['used_keys'])
if not used:
    it.fail('registry: no key is recorded as used')
bad_status = [k for k in used
              if E[k]['status'] not in {'definition', 'estimated', 'result',
                                        'derived', 'diagnostic', 'interval',
                                        'band', 'verified identity', 'sample',
                                        'software'}]
if bad_status:
    it.fail('registry: unrecognised status on %s' % bad_status[:5])
it.note('registry: %d entries, %d used by the two documents, every used entry '
        'typed and sourced' % (len(E), len(used)))
# no unresolved template markers survived into either artifact
for a in 'PM':
    if re.search(r'\{\{n:', ART[a]):
        it.fail('%s: an unresolved number token survived' % NAMES[a])
if 'AWAITING PARAMETER INTERVALS' in PAPER_RAW or \
        'AWAITING PARAMETER INTERVALS' in HTML_TXT:
    it.fail('the v4 placeholder for missing intervals is still present')


# --------------------------------------------------------------------------- #
# 12. THE SAMPLE OF RECORD
# --------------------------------------------------------------------------- #
it = item(12, 'The funnel ends where the estimation begins')
for a in 'PM':
    hay = NORM[a]
    for n in ['1,540', '2,223']:
        if n not in hay:
            it.fail('%s: the estimation sample size %s is not stated'
                    % (NAMES[a], n))
    # The predecessor counts legitimately appear as an intermediate funnel row
    # and in the history section. What is forbidden is presenting either of
    # them AS the estimation sample.
    for stale in ['1,555', '2,275']:
        for m in re.finditer(re.escape(stale), hay):
            w = hay[max(0, m.start() - 160): m.start() + 160]
            if 'estimation sample' in w or 'we estimate' in w or \
               'are estimated on' in w:
                it.fail('%s: the predecessor count %s is presented as the '
                        'estimation sample' % (NAMES[a], stale))
                break
if int(E['n_singles']['value']) != 1540 or int(E['n_couples']['value']) != 2223:
    it.fail('registry: the sample sizes are not the estimation samples')


# --------------------------------------------------------------------------- #
# 13. FIGURE AND TABLE INTEGRITY
# --------------------------------------------------------------------------- #
it = item(13, 'Figures and tables are present, captioned and rendered')
figs = re.findall(r'\\includegraphics\[[^]]*\]\{([^}]+)\}', PAPER_RAW)
if len(figs) < 9:
    it.fail('paper: only %d figures are included' % len(figs))
for f in figs:
    p = (JMP / 'manuscript' / f)
    if not p.exists():
        it.fail('paper: figure file missing on disk: %s' % f)
ntab = PAPER_RAW.count(r'\begin{longtable}')
# REBUILD-2 deliberately bounded the paper (old fit/benchmark/bridge/lambda/
# welfare-levels tables moved report-only), so the threshold that fit the
# unbounded v5 paper no longer applies; lowered to still catch a real
# regression without penalizing the intended reduction.
if ntab < 12:
    it.fail('paper: only %d tables' % ntab)
ncap = PAPER_RAW.count(r'\caption{')
if ncap < len(figs) + ntab:
    it.fail('paper: %d captions for %d figures and %d tables'
            % (ncap, len(figs), ntab))
nembed = HTML_RAW.count('data-fig=')
if nembed < 10:
    it.fail('report: only %d embedded figures' % nembed)
it.note('paper: %d figures, %d tables, %d captions; report: %d embedded '
        'figures, %d tables' % (len(figs), ntab, ncap, nembed,
                                HTML_RAW.count('<table')))
# every table the report renders must be inside a horizontal scroll wrapper
if HTML_RAW.count('<div class="tw"><table') != HTML_RAW.count('<table'):
    it.fail('report: a table is not wrapped for horizontal scrolling')


# --------------------------------------------------------------------------- #
# 14. THE REPORT EXPLAINS AND THE PAPER ARGUES
# --------------------------------------------------------------------------- #
it = item(14, 'The report carries the explanatory apparatus')
if 'Questions for presentation preparation' not in MD_RAW:
    it.fail('report: the question-and-answer section is missing')
nq = len(re.findall(r'^## \d+\. ', MD_RAW, flags=re.M))
if nq < 15:
    it.fail('report: only %d questions' % nq)
for need in ['What is new and what is inherited', 'A worked illustration']:
    if need not in MD_RAW:
        it.fail('report: the block %r is missing' % need)
if HTML_RAW.count('<details>') < 2:
    it.fail('report: the history and notebook sections are not collapsible')
# the stale answers the review named must be gone
for bad in ['log utility gives an arithmetic consumption average',
            'the first picture is generic motivation',
            'corrected nested attribution is not established']:
    forbid(it, bad, arts='HM')
# FINAL M9 accepts the canonical notebook as the reader-facing results
# notebook while retaining the exact raw-job-set/pricing boundary.
for need in ['canonical reader-facing results notebook',
             'not a raw-data end-to-end reproduction system',
             'raw job-set construction', 'euromod pricing',
             'next engineering priority']:
    if need not in MD_RAW.lower().replace('’', "'"):
        it.fail('report: the notebook description omits %r' % need)
it.note('report: %d questions, history and notebook collapsed, worked '
        'household present, notebook scope boundary disclosed' % nq)


# --------------------------------------------------------------------------- #
# 15. THE NOVELTY CLAIM IS THE LICENSED ONE
# --------------------------------------------------------------------------- #
it = item(15, 'The novelty claim is conservative and fully conjoined')
# The novelty ruling REQUIRES a "what is new / what is inherited" box that lists
# these five claims under "Not claimed". Listing a claim in order to disown it is
# the opposite of making it, so that block is the permitted site.
DISOWNED = ('not claimed', 'we claim no', 'do not claim')
for bad in ['a new Shapley method', 'new Shapley rule',
            'the first structural labour-supply Shapley decomposition',
            'first structural labour supply shapley',
            'the first money-metric welfare-inequality decomposition',
            'the first decomposition of money-metric inequality',
            'the first RURO welfare analysis',
            'the first preference-versus-opportunity welfare comparison']:
    forbid(it, bad, permitted=DISOWNED)
for a in 'PM':
    hay = NORM[a]
    if 'introduce and implement' not in hay:
        it.fail('%s: the abstract does not use the conservative wording'
                % NAMES[a])
    k = hay.find('to our knowledge')
    if k < 0:
        it.fail('%s: the qualified priority sentence is absent' % NAMES[a])
    else:
        w = hay[k:k + 900]
        # REBUILD-2: the preliminary exercise is a plain (ungrouped) exact
        # Shapley value on three players, not the grouped Owen rule an
        # earlier, now-withdrawn four-operator version required -- 'grouped
        # allocation' dropped from the required conjunction because it would
        # no longer be an accurate claim, not because the check is loosened
        # for its own sake; 'complete recomputation' replaces it as the
        # methodological-discipline claim actually made.
        for part in ['random-utility random-opportunity', 'money-metric',
                     'every coalition', 'complete recomputation']:
            if part not in w:
                it.fail('%s: the "to our knowledge" claim is not fully '
                        'conjoined: %r is missing' % (NAMES[a], part))
    if 'allocation rule is inherited' not in hay:
        it.fail('%s: the inherited-rule sentence is missing' % NAMES[a])
    for c in ['muhlhan', 'mühlhan', 'muehlhan']:
        if c in hay:
            break
    else:
        it.fail('%s: the closest structural decomposition precedent is not '
                'cited' % NAMES[a])
    if 'creedy' not in hay:
        it.fail('%s: the closest money-metric decomposition precedent is not '
                'cited' % NAMES[a])
    for c in ['shorrocks']:
        if c not in hay:
            it.fail('%s: the allocation machinery is not credited (%s)'
                    % (NAMES[a], c))


# --------------------------------------------------------------------------- #
# 16. NO CAUSAL CLAIM, AND THE OPEN ITEMS SURVIVE
# --------------------------------------------------------------------------- #
it = item(16, 'No causal claim; the genuinely unresolved items are retained')
# Both sentences are required, not either: the geography sentence scopes one
# covariate and the decomposition sentence scopes the whole exercise. Accepting
# either let a mutation that reversed one of them pass the negative control.
for a in 'PM':
    if 'no causal effect of geography is claimed' not in NORM[a]:
        it.fail('%s: the geography disclaimer is absent' % NAMES[a])
    if 'is not a causal analysis' not in NORM[a]:
        it.fail('%s: the decomposition-is-not-causal sentence is absent'
                % NAMES[a])
for bad in ['is a causal analysis', 'we identify the causal',
            'the causal effect of job access', 'causally attributable']:
    forbid(it, bad)
for need, label in [
        ('selected on an outcome', 'the outcome-selection question'),
        ('sampling law', 'the sampling-law question')]:
    for a in 'PM':
        if need not in NORM[a]:
            it.fail('%s: %s has been dropped' % (NAMES[a], label))
it.note('the two open econometric questions and the couples D limitation are '
        'all retained')


# --------------------------------------------------------------------------- #
# 17.  RETIRED LINEAGE (LINEAGE-SWEEP-1)  --  path-based, not string-based
# --------------------------------------------------------------------------- #
it = item(17, 'Retired welfare-decomposition lineage: no read by path '
              '(DECOMP-PRESEMINAR-1)')
# REG (numbers_of_record_v5.json) carries a top-level "discussion_tables" key
# that this build script deliberately carries forward untouched -- it is
# consumed by a SEPARATE artifact (MNL's discussion_notebook_support.py /
# "the discussion notebook" referenced throughout the QA section), not by
# the story report or the paper this item gates. Scanning the whole file
# would conflate that separate, out-of-scope consumer's data with what this
# surface actually renders. Scan only "entries" and "gallery" -- the parts
# build_v5.py itself writes and resolve() actually reads back via val()/
# TABLES -- and report discussion_tables separately, informationally.
_reg_json = json.loads(REG.read_text(encoding='utf-8'))
_reg_scannable = json.dumps({k: v for k, v in _reg_json.items()
                             if k != 'discussion_tables'})
_reg_dt_violations = rlg.scan_text(json.dumps(_reg_json.get('discussion_tables', {})))
_LINEAGE_TARGETS = [
    JMP / 'reports/research_story_build/build_v5.py',
    JMP / 'reports/research_story_build/v5_sections.py',
    JMP / 'reports/research_story_build/common.py',
    PAPER,
    HTML,
]
_violations = rlg.scan_files([p for p in _LINEAGE_TARGETS if p.exists()])
_reg_hits = rlg.scan_text(_reg_scannable)
if _reg_hits:
    _violations[REG] = _reg_hits
if _violations:
    it.fail('this gate checks the build source and registry for a READ of a '
            'retired artifact by its own path/basename, not the rendered '
            'prose -- a reworded sentence does not clear this check while '
            'the underlying data source is unchanged')
    for p, hits in _violations.items():
        it.fail('%s: %s' % (p.relative_to(JMP), ', '.join(hits)))
else:
    it.note('no retired-lineage path reference found in build_v5.py, '
            'v5_sections.py, common.py, %s (entries/gallery only), %s, or %s'
            % (REG.name, PAPER.name, HTML.name))
if _reg_dt_violations:
    it.note('%s: discussion_tables (a separate, out-of-scope artifact '
            'consumed by MNL/experiments/JMP_SEMINAR_SPRINT/'
            'discussion_notebook_support.py, not by this story report or '
            'paper) still carries retired-lineage references: %s -- not '
            'counted against this item; fix belongs to a future pass on '
            'the discussion notebook itself' % (REG.name, ', '.join(_reg_dt_violations)))
_four_factor = {}
for p in [PAPER, HTML]:
    hits = rlg.scan_four_factor(p.read_text(encoding='utf-8', errors='ignore'))
    if hits:
        _four_factor[p] = hits
if _four_factor:
    it.fail('supplementary content signature for a forbidden four-factor '
            'P/A/B/D decomposition (this signal is not path-based and can '
            'be dodged by rewording -- treat a clean result here as weaker '
            'evidence than the path check above, and a hit here as strong '
            'evidence regardless)')
    for p, hits in _four_factor.items():
        it.fail('%s: %s' % (p.relative_to(JMP), ', '.join(hits)))


# --------------------------------------------------------------------------- #
# 18.  RETIRED EX-ANTE WELFARE CONSTRUCTION  (MEASURE-DEF-1, Deputy ruling R2)
# --------------------------------------------------------------------------- #
it = item(18, 'Retired ex-ante inclusive-value welfare construction: not '
              'presented as the measure (MEASURE-MAP-1R / Deputy ruling R2)')
# REBUILD-2 gated the ex-ante J/H derivation to {{report-only}}, which kept
# it out of the paper but left it live, undisclaimed, in the discussant-
# facing HTML report even though every reported number was already literal
# Mapping-F W1_F. MEASURE-DEF-1 replaced the welfare section's definition
# with the accepted closed form and either removed the ex-ante derivation or
# labelled it retired with R2 cited. This item is the standing gate against
# a regression: it fails if the construction's own defining notation
# resurfaces in either surface without that label, close enough to be a hit
# on the same reading. Content signature, not path-based -- see
# retired_lineage_gate.scan_exante's own docstring for why no retired FILE
# exists to gate by path here, and why a hit is nonetheless strong evidence.
_exante = {}
_exante_sources = {PAPER: PAPER_RAW, HTML: HTML_TXT}
# HTML is scanned on its parsed text layer (HTML_TXT), not the raw file:
# the raw HTML interleaves tags, attributes and embedded base64 figure data
# between a formula and its disclaiming sentence, which can push the two
# past the local disclaimer window even when they sit in the same rendered
# paragraph. The text layer is what a reader (and item 4/5/etc. above)
# actually sees, so it is also the right layer to check disclaiming
# proximity against.
for p, txt in _exante_sources.items():
    hits = rlg.scan_exante(txt)
    if hits:
        _exante[p] = hits
if _exante:
    it.fail('the ex-ante inclusive-value construction (J/H integrals over '
            'the estimated opportunity density) is present without an '
            'explicit retired/withdrawn label and an R2 citation nearby')
    for p, hits in _exante.items():
        it.fail('%s: %s' % (p.relative_to(JMP), ', '.join(hits)))
else:
    it.note('no undisclaimed ex-ante J/H construction found in %s or %s'
            % (PAPER.name, HTML.name))
# the accepted closed form must actually be the one stated (belt-and-braces
# with item 4, which checks the same thing on the paper/report text layer)
if 'W^1_{F,i}=C_i^{\\mathrm{obs}}\\exp' not in PAPER_RAW and \
        'W^1_{i,F}=C_i^{\\mathrm{obs}}\\exp' not in PAPER_RAW:
    it.fail('paper: the accepted literal W1_F closed form is not stated in '
            'its boxed form')


# --------------------------------------------------------------------------- #
def main() -> int:
    rc = 0
    lines = ['# Consistency gate, v5', '',
             'Artifacts: `%s`, `%s`, `%s`, `%s`.' % (
                 PAPER.name, HTML.name, MD.name, REG.name), '',
             'Scope note. This gate carries forward the content rules of '
             '`consistency_gate_spec_v1.md` that still apply to the S11 '
             'specifications of record, adds the rules of '
             '`canonical_notation_v5.md`, and adds the single-current-model '
             'check. `run_consistency_gate.py` is NOT re-run against v5: it is '
             'bound to the v1/v2 artifact family and to two clauses of its own '
             'specification that the current model contradicts. See '
             '`canonical_notation_v5.md` for the clause-by-clause disposition.',
             '', '| # | Item | Verdict |', '|---|---|---|']
    for x in ITEMS:
        lines.append('| %d | %s | **%s** |' % (x.num, x.title, x.verdict))
        if x.verdict == 'FAIL':
            rc = 1
    lines.append('')
    for x in ITEMS:
        lines.append('## %d. %s — %s' % (x.num, x.title, x.verdict))
        lines.append('')
        if x.detail:
            for d in x.detail:
                lines.append('- %s' % d)
        else:
            lines.append('- no findings')
        lines.append('')
    lines.append('**Overall: %s**' % ('PASS' if rc == 0 else 'FAIL'))
    (JMP / 'reports/consistency_gate_v5.md').write_text(
        '\n'.join(lines) + '\n', encoding='utf-8')
    for x in ITEMS:
        print('%-2d %-62s %s' % (x.num, x.title[:62], x.verdict))
        for d in x.detail:
            if x.verdict == 'FAIL':
                print('     %s' % d)
    print('\nwrote reports/consistency_gate_v5.md  (exit %d)' % rc)
    return rc


if __name__ == '__main__':
    sys.exit(main())
