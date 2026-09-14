"""Editable reader-facing source for the V8 research-story report.

The seven main sections follow the economic sequence specified for V8.  The
complete V7 record is preserved, without numerical alteration, inside one
collapsed technical-provenance appendix.
"""
import v7_sections as v7


TITLE = "Unequal Job Opportunities and Well-Being Inequality"

ABSTRACT = """In a preliminary restricted structural decomposition of the attained-bundle
money metric, equalising systematic utility heterogeneity, coarse geographic
and temporal access, and systematic wage opportunities—while holding
household resources, needs and composition fixed—reduces the Gini by
1.8–9.9% relative to its baseline level across household types and reporting
scales. Within this restricted exercise, the earning-opportunity channel is
larger than the coarse access channel throughout. These figures do not
estimate the total share of well-being inequality caused by unequal job
opportunities."""

PRELIM_NOTE = (
    "Discussion draft. These decomposition estimates are preliminary and "
    "subject to ongoing numerical validation of the counterfactual integration."
)


WHY_INCOME_MIXES = r"""
Income inequality records differences in outcomes, but it does not say why
those differences arose. Two people can work the same hours at the same wage
and nevertheless face very different circumstances: one may have chosen from
several suitable jobs, while the other accepted the only job available. Their
incomes coincide, but the freedom behind those incomes does not.

The ambiguity also runs in the other direction. Low earnings may reflect a
preference for leisure, scarce access to suitable hours or occupations, weak
wage offers, or household resources that make fewer hours affordable. Those
explanations are observationally entangled and have different implications for
how inequality should be interpreted. A distribution of income therefore mixes
preferences with opportunities before the analysis begins.

The paper addresses both sides of that problem. First, it uses a structural
model to distinguish systematic differences in how households value
consumption and leisure from systematic differences in the jobs they can reach.
Second, it converts each household's attained consumption-and-leisure bundle
into a common monetary unit. This makes it possible to ask how the inequality
of attained well-being changes when selected dimensions of preferences and
opportunities are equalised.
"""


LATENT_JOBS = r"""
A latent job is an employment state together with an occupation, weekly hours
and an hourly wage. Households choose among such packages rather than choosing
hours in isolation. Couples choose both partners' packages under a shared
household budget. Each package is priced through the French tax-benefit system,
so changes in work arrangements affect disposable income through the actual
schedule of taxes and transfers.

The application uses French EU-SILC collected in
{{n:collection_year|.0f}}, whose incomes refer to {{n:income_year|.0f}}, and
the French {{n:policy_year|.0f}} tax-benefit system. The estimation samples
contain {{n:n_singles|,.0f}} single-adult households and
{{n:n_couples|,.0f}} couples. The two household types are estimated separately.

The preferred specification gives every potential job two conceptually
distinct components. Utility describes how consumption and leisure are valued.
The opportunity distribution describes how strongly employment, hours,
occupations and wage offers are represented before a choice is made. Choices
reflect both components, so the separation is not automatic.

The model obtains that separation from maintained restrictions. Preferences
vary smoothly with leisure, whereas hours opportunities may be concentrated in
particular ranges. Local unemployment, region and urbanisation shift access to
employment but are excluded from preferences. Conditional on occupation, the
wage-offer distribution is assumed independent of offered hours. Under these
functional-form and exclusion restrictions, observed choices can inform the
systematic preference and opportunity components separately. This is a
structural interpretation, not a causal design.

The predictive-fit diagnostics then integrate the estimated choice model over
the opportunity distribution and taste shocks. They are population predictions,
not fitted choices from the alternatives used during estimation. A large
predictive integration sample is used to assess both fit and the numerical
precision of the reported diagnostics.
"""


MONEY_METRIC = r"""
The attained-bundle money metric asks how much consumption at home would leave
a household as well off as it is at the consumption-and-leisure bundle it
actually attained. Home is universally available and, in the estimated domain,
maximises the non-consumption part of utility for every household. The monetary
equivalent is therefore

$$
M_i=C_i^{\mathrm{attained}}
\exp\!\left\{\frac{L_i(\mathrm{attained})-L_i(\mathrm{home})}{\beta_c}\right\},
$$

where $C_i^{\mathrm{attained}}$ is disposable consumption, $L_i$ is the
systematic value of leisure and other non-consumption attributes, and
$\beta_c$ is the estimated weight on log consumption. The expression is already
in euros: it is the consumption level that solves an indifference comparison,
not an index subsequently converted into money.

Opportunities affect this measure through the bundle the household attains.
Jobs not taken are not averaged directly into the attained-bundle measure. A
non-worker's money metric therefore equals observed consumption, while a
worker's valuation also reflects the leisure difference between the attained
job and home.

Results are reported separately for single-adult and couple households, both
before and after applying the modified-OECD equivalence scale. Equivalisation is
a normative reporting choice. The two estimated populations are never pooled,
and their welfare levels are not compared with one another.
"""


DECOMPOSITION_ECONOMICS = r"""
The preliminary counterfactual decomposition asks what happens to the
distribution of attained-bundle well-being when three modelled dimensions are
equalised. The first is systematic preference heterogeneity, represented by the
observed characteristics that shift the utility of leisure. The second is
coarse geographic and temporal access, represented by region, urban or rural
location, and year. The third is systematic wage opportunities, represented by
the observed characteristics that shift wage offers.

For each combination of equalised dimensions, the model predicts the job bundle
each household attains, converts that bundle into the money metric, and computes
the Gini of the resulting distribution using household weights. The exercise
holds household resources, needs and composition fixed. It also leaves personal
occupation access, the concentration of hours opportunities, idiosyncratic wage
dispersion and behavioural randomness outside the equalisation.

Because the dimensions can interact, their contributions cannot be read from
three one-at-a-time comparisons. The Shapley allocation averages each
dimension's marginal contribution over the possible orders of equalisation.
The contributions consequently add to the total change between baseline
inequality and inequality after all three dimensions have been equalised. In
the table below that total change is denoted $\Delta I$. This is an accounting
of a deliberately restricted counterfactual exercise, not an estimate of the
total causal contribution of unequal job opportunities.
"""


CURRENT_RESULTS = r"""
## Behaviour and predictive fit

The preferred specification reproduces participation and occupation margins
closely in aggregate, while its hours fit is uneven. Across all reported
population moments, the corrected mean absolute deviation is
{{n:mae_singles|.4f}} for single adults and {{n:mae_couples|.4f}} for couples.
The correction is not an across-the-board improvement: the single-adult value
rises slightly while the couple value falls.

For the extensive margin, the predictive-fit diagnostics are sufficiently
precise to report an accuracy of {{n:single_women_accuracy_pct|.1f}}% for single
women, against a model-simulated range of
{{n:single_women_band_lo_pct|.1f}}%–{{n:single_women_band_hi_pct|.1f}}%, and
{{n:coupled_women_accuracy_pct|.1f}}% for coupled women, against
{{n:coupled_women_band_lo_pct|.1f}}%–{{n:coupled_women_band_hi_pct|.1f}}%.
Single men's and coupled men's extensive-accuracy statistics are WITHHELD
because numerical integration error remains too large relative to sampling
variation. Coupled men's extensive accuracy is WITHHELD.

The common hours mismatch is underprediction of the observed 37-hour mass
point. The observed-minus-predicted gaps are
{{n:gap37_single_women|.1f}} percentage points for single women,
{{n:gap37_coupled_men|.1f}} for coupled men,
{{n:gap37_single_men|.1f}} for single men and
{{n:gap37_coupled_women|.1f}} for coupled women. This finding concerns the
observed 37-hour concentration, not the model's neighbouring full-time range.

## Attained-bundle well-being

{{table:welfare_reader}}

On the equivalised basis, the Gini of the attained-bundle money metric is
{{n:w1f_eq_gini_singles|.4f}} for single-adult households and
{{n:w1f_eq_gini_couples|.4f}} for couples, compared with
{{n:ceq_gini_singles|.4f}} and {{n:ceq_gini_couples|.4f}} for disposable
consumption in the same samples. These are within-sample dispersion
comparisons, not welfare-loss estimates.

## Preliminary structural decomposition

Equalising systematic utility heterogeneity, coarse geographic and temporal
access, and systematic wage opportunities—while holding household resources,
needs and composition fixed—reduces the Gini by
{{n:d2_deltaI_pct_singles_eq|.1f}}–{{n:d2_deltaI_pct_couples_uneq|.1f}}%
relative to its baseline level across household types and reporting scales.
Within this restricted exercise, the earning-opportunity channel is larger than
the coarse access channel throughout. The preference contribution changes sign
with equivalisation, so no directional claim is made about it.

{{table:decomposition_reader}}

The percentages and allocated shares in this table belong to the restricted
exercise just described. They do not estimate the total share of well-being
inequality caused by unequal job opportunities. The contributions reproduce
closely in an independent simulation run; that comparison is a check on
simulation variation, not a confidence interval for parameter uncertainty.
"""


PRELIMINARY_LIMITS = r"""
These decomposition estimates are preliminary and subject to ongoing numerical
validation of the counterfactual integration.

The main limitation is support at short hours. The currently priced estimation
sample represents the lower part of the modelled hours range sparsely, while a
separate integration assessment finds substantial model-implied mass there.
The consequences for the attained-bundle decomposition have not yet been fully
quantified. The quantitative decomposition should therefore be read as a
preliminary structural accounting exercise; additional numerical robustness
checks are in progress.

The exercise is also deliberately partial. Household resources, needs and
composition remain fixed; the access comparison covers only coarse geographic
and temporal variation; and systematic wage opportunities change wage-offer
locations without removing idiosyncratic wage dispersion or selection. The
reported simulation variation does not propagate parameter uncertainty. These
restrictions explain why the reported Gini reduction is not a complete
decomposition of well-being inequality and why it carries no causal
interpretation.

The predictive evidence has a separate numerical boundary. Women's extensive
accuracy is reportable, but the corresponding statistic for each group of men
is withheld. The 37-hour mass-point mismatch is retained explicitly rather than
being absorbed into a broader hours category. Coverage below ten hours remains
a limitation of the finite predictive integration sample.
"""


EX_ANTE = """We are also developing a complementary ex-ante measure that values the
quality of the household’s entire job-opportunity prospect rather than only
the bundle eventually attained. It asks for the constant consumption level
that would make the household indifferent between its actual stochastic job
prospect and a reference prospect with the same opportunities but equal
consumption across jobs. Unlike the attained-bundle measure, this object is
directly sensitive to the estimated opportunity distribution. Its numerical
implementation requires additional counterfactual tax-benefit evaluations
to obtain adequate coverage of the hours distribution, so the corresponding
inequality decomposition is still preliminary and is not reported here."""


def _v7_record():
    blocks = [
        "## V7 abstract\n\n" + v7.ABSTRACT,
        "## V7 status note\n\n" + v7.PRELIM_NOTE,
    ]
    for section in v7.SECTIONS:
        blocks.append("## V7 block: " + section["title"] + "\n\n" + section["body"])
    qa = ["## V7 presentation-preparation questions"]
    for number, (question, answer) in enumerate(v7.QA, 1):
        qa.append("### %d. %s\n\n%s" % (number, question, answer))
    blocks.append("\n\n".join(qa))
    return """
This collapsed appendix preserves the complete predecessor text and its
implementation-level provenance. It is not part of the reader-facing argument.
Its purpose is to keep every technical definition, numerical table, diagnostic
qualification and historical note available without interrupting the economic
sequence of the report.

""" + "\n\n".join(blocks) + "\n"


SECTIONS = [
    {"key": "why", "title": "Why income inequality mixes preferences and opportunities",
     "body": WHY_INCOME_MIXES},
    {"key": "model", "title": "How the latent-jobs model separates preferences from opportunities",
     "body": LATENT_JOBS},
    {"key": "money", "title": "How attained bundles become money-metric well-being",
     "body": MONEY_METRIC},
    {"key": "decomposition", "title": "How the preliminary counterfactual decomposition works",
     "body": DECOMPOSITION_ECONOMICS},
    {"key": "results", "title": "What the current results say",
     "body": CURRENT_RESULTS},
    {"key": "limits", "title": "What remains preliminary",
     "body": PRELIMINARY_LIMITS},
    {"key": "exante", "title": "Why an ex-ante opportunity-prospect extension is useful",
     "body": EX_ANTE},
    {"key": "provenance", "title": "Appendix. Technical record and provenance",
     "body": _v7_record(), "appendix": True, "collapse": True, "paper": False},
]


QA = [
    ("What is the paper's central distinction?",
     "Observed income combines what households prefer with the jobs and wages they can reach; the structural model separates those components under maintained restrictions."),
    ("What does the current money metric value?",
     "It values the bundle actually attained by the consumption level at home that would make the household indifferent to that bundle."),
    ("How should the decomposition be read?",
     "As a preliminary restricted structural accounting exercise, not as the total causal share of inequality due to unequal job opportunities."),
]
