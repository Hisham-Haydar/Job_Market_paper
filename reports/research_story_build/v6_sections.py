"""REPORT-V6: presentation-only successor; the v5 evidence and prose stay frozen.

Unchanged sections are inherited verbatim. Every decomposition table, figure,
numeric token, signed contribution and denominator is carried into Appendix D.
No numerical ex-ante work is called by this module or its renderer.
"""
import re
import v5_sections as previous
from v5_sections import *  # noqa: F403 -- explicitly frozen predecessor

APPENDIX_TITLE = 'Preliminary restricted-operator decomposition'
MISSION_WORDING = (
    'A preliminary P/A/B decomposition has been computed for the attained-bundle '
    'money metric, holding resources, needs and composition fixed. It is a '
    'restricted counterfactual exercise, not a comprehensive share of inequality '
    'due to all opportunities. A separately defined ex-ante metric is being '
    'reconstructed for comparison; neither historical ex-ante percentages nor '
    'a settled cross-estimand conclusion are reported here.')
DIAGNOSTIC_WORDING = (
    'The earning-opportunity channel equalises wage-offer location only: the '
    'systematic differences associated with education and potential experience, '
    'which shift offer locations by at most about {{n:diag1_location_log|.2f}} '
    'log points. The common offer spread (about {{n:diag1_sigma|.2f}} log points), '
    'wage-draw luck and selection remain in the residual and are quantitatively '
    'larger than the location differences removed by this operator. This is a '
    'definitional boundary of the exercise, not a measurement error. '
    'Equalising locations can change attained wages; it does not equalise the '
    'whole wage distribution. The diagnostic comparison that also compresses '
    'the common spread and selection is a bound, not an additional decomposition '
    'result. Thin effective support for couples leaves individual wage '
    'attainment noisy and remains a numerical limitation.')
EA_STATUS = (
    'A separately defined ex-ante metric is being reconstructed for comparison. '
    'Historical ex-ante percentages are not current results and are not shown. '
    'The verified attained-bundle measure and its observed-bundle results remain '
    'the current welfare evidence; no settled comparison between the two metrics '
    'is available.')
APP_REF = 'Appendix D'

ABSTRACT = previous.ABSTRACT.split(' Attributing the resulting inequality', 1)[0]
ABSTRACT += (' The empirical results describe structural estimates, predictive '
             'diagnostics and observed-bundle welfare and resource inequality. '
             'A computed restricted-operator decomposition is presented in '
             'Appendix D as a preliminary exercise.')
PRELIM_NOTE = ('Discussion draft. Structural estimates, diagnostics and the '
               'verified observed-bundle welfare results are reported in the '
               'main text. The preliminary restricted-operator decomposition '
               'is in Appendix D.')

# Relocate the introductory result and qualifications; keep the variance
# paragraph in the main text as well because resource inequality is retained.
INTRO = previous.INTRO
intro_paras = INTRO.split('\n\n')
intro_moved = []
for i, para in enumerate(intro_paras):
    if para.startswith('The normative half then yields'):
        intro_moved.append(para)
        intro_paras[i] = EA_STATUS
    elif para.startswith('**What we find.**'):
        intro_moved.append(para.replace('**What we find.**', '**Restricted results.**'))
        intro_paras[i] = ('The computed preliminary restricted-operator '
                         'decomposition, including all numerical results and '
                         'their limitations, is reported in Appendix D.')
    elif para.startswith('Two qualifications belong with the headline.'):
        intro_moved.append(para.replace('with the headline', 'with these appendix results'))
        intro_paras[i] = ''
    elif para.startswith('What is new, to our knowledge'):
        intro_paras[i] = para.replace(
            " Within this bounded decomposition exercise, earning-opportunity heterogeneity has a larger Shapley contribution than the model's coarse geographic/temporal access channel.", '')
INTRO = '\n\n'.join(intro_paras)

WELFARE, method = previous.WELFARE.split('## The preliminary structural decomposition', 1)
WELFARE += '\nThe restricted counterfactual operators and allocation rule are set out in Appendix D.\n'
RESULTS, results = previous.RESULTS.split('## The preliminary decomposition', 1)

# Retain the decomposition-specific sensitivity discussion in the appendix;
# all other sensitivity and diagnostic paragraphs remain unchanged.
SENSITIVITY, sensitivity = previous.SENSITIVITY, []
start = SENSITIVITY.index('## Equivalization and the preliminary decomposition')
end = SENSITIVITY.index('## Two open econometric questions')
sensitivity.append(SENSITIVITY[start:end])
SENSITIVITY = SENSITIVITY[:start] + SENSITIVITY[end:]
for prefix in ('**The $A$ channel', '**$\\Delta I$ is bounded',
               "**The preference contribution's sign", "Section 5's decomposition"):
    paras = SENSITIVITY.split('\n\n')
    moved = [p for p in paras if p.startswith(prefix)]
    assert len(moved) == 1, prefix
    sensitivity.extend(moved)
    SENSITIVITY = '\n\n'.join(p for p in paras if not p.startswith(prefix))

CONCLUSION = previous.CONCLUSION.split('\n\nA complete decomposition', 1)[0]
CONCLUSION += ('\n\nThe observed-bundle welfare and resource distributions are '
               'the descriptive welfare results. Appendix D preserves the '
               'computed preliminary restricted-operator decomposition and '
               'states its scope; it does not identify a comprehensive '
               'contribution of unequal opportunities to inequality.\n')

APP_DECOMP = ('\n' + MISSION_WORDING + '\n\n' + DIAGNOSTIC_WORDING
              + '\n\n## Counterfactual operators and simulation rule\n' + method
              + '\n\n## Coalition values and signed allocation\n' + results
              + '\n\n' + '\n\n'.join(sensitivity)
              + '\n\n## Interpretation of the restricted results\n'
              + '\n\n'.join(intro_moved))

# Update only decomposition-specific cross-references, leaving references to
# structural estimates and diagnostics in Sections 4--6 intact.
def appendix_references(text):
    for old, new in (
        ('Section 5\'s decomposition', 'The appendix decomposition'),
        ('the preliminary decomposition of Section 5', 'the preliminary decomposition in Appendix D'),
        ('The preliminary decomposition of Section 5', 'The preliminary decomposition in Appendix D'),
        ('exercise of Section 5', 'exercise in Appendix D'),
        ('decomposition (Section 5)', 'decomposition (Appendix D)'),
        ('Section 5 reports only the bounded', 'Appendix D reports only the bounded'),
        ('Section 5 reports both', 'Appendix D reports both'),
        ('comparison reported in Section 5', 'comparison reported in Appendix D'),
        ('reported in Section 5', 'reported in Appendix D'),
        ('See Section 5.', 'See Appendix D.'),
    ):
        text = text.replace(old, new)
    return text

SECTIONS = []
for section in previous.SECTIONS:
    if section['key'] == 'notebook':
        SECTIONS.append({'key': 'appdecomp', 'title': 'Appendix D. ' + APPENDIX_TITLE,
                         'body': appendix_references(APP_DECOMP), 'appendix': True})
    new = dict(section)
    new['body'] = appendix_references(globals().get(
        {'intro': 'INTRO', 'welfare': 'WELFARE', 'results': 'RESULTS',
         'sensitivity': 'SENSITIVITY', 'conclusion': 'CONCLUSION'}.get(section['key'], ''),
        section['body']))
    SECTIONS.append(new)
QA = [(q, appendix_references(a)) for q, a in previous.QA]
