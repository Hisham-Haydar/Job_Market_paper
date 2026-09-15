"""Reader-facing sections for the V12 research-story report (structural edit).

V12 keeps the V11 body and removes the duplicate predecessor document from the
appendix. Analysis that lived only in that document (raw labour-force status,
the full fit comparison, coalition values, robustness, time-endowment
sensitivity, benchmark input caveat) is promoted into Sections 2, 5 and 6. The
appendix is rebuilt from implementation material only. No number changes.
"""
from __future__ import annotations

import v7_sections as v7
import v6_sections as v6
import v10_sections as v10
import v11_sections as v11
import v11_illustration as illustration

TITLE = v11.TITLE
D_STATUS = v11.D_STATUS
PERSPECTIVES_SENTENCE = v11.PERSPECTIVES_SENTENCE
INTERPRETATION_SENTENCE = v11.INTERPRETATION_SENTENCE
ABSTRACT = v11.ABSTRACT
PRELIM_NOTE = v11.PRELIM_NOTE
reader_voice = v11.reader_voice
_replace_once = v11._replace_once


def _between(text: str, start: str, end_marker: str) -> str:
    i = text.index(start)
    j = text.index(end_marker, i) + len(end_marker)
    return text[i:j]


# --------------------------------------------------------------------------- #
# Section 2: promote observed raw labour-force status
# --------------------------------------------------------------------------- #

LES_SECTION = r"""
### Observed raw labour-force status

The structural model has one non-work alternative, so unemployment and
inactivity are the same state inside it. The data distinguish them. The table
recovers each person's raw labour-force status from the person-level survey
file, including for spouses, whose status in the household design file records
only employed or not employed.

{{table:observed_les}}

Most non-working adults in both samples are unemployed rather than inactive,
which is consistent with the sample screens that remove students and pension
recipients. Because the model maps both states to non-employment, nothing in
the estimates or welfare measures distinguishes a household that is searching
from one that is out of the labour force.
"""

LATENT_JOBS = _replace_once(
    v11.LATENT_JOBS,
    "Both spouses' labour-force status is mapped to employment or non-employment; "
    "the model does not distinguish unemployment from inactivity. The appendix "
    "reports the raw status breakdown.",
    LES_SECTION.strip(),
)


# --------------------------------------------------------------------------- #
# Section 5: promote the full fit comparison and attained-bundle analysis
# --------------------------------------------------------------------------- #

_benchmark = reader_voice(_between(
    v7.RESULTS, "The two re-estimated common-opportunity benchmarks are worse by",
    "has been identified."))

RESULTS = v11.RESULTS
RESULTS = _replace_once(
    RESULTS,
    "The complete moment-by-moment tables are in the appendix.",
    r"""The margin-by-margin comparison below reports every population moment. The
sub-ten-hour cell is a coverage limitation of the finite integration sample,
which contains no draw between 5 and 10 hours; the long-hours reporting bin
closes at 70 hours inclusive.

{{table:fitsingles}}

{{table:fitcouples}}

At the level of individual predictions the evidence is group-specific. For all
four groups, the association between predicted probabilities and realised
outcomes is what conditioning on realised outcomes mechanically produces under
stochastic choice. For coupled men and coupled women the remaining dispersion
is evidence of misspecification; for single men and single women numerical
integration error is too large to decide. An earlier claim of excess
predictability across three groups is withdrawn.""",
)
RESULTS = _replace_once(
    RESULTS,
    """The richer common-opportunity benchmarks fit less well on the same households
and the same sampled alternatives. The deterioration is concentrated in the
margins governed by the opportunity distribution, especially occupations.
That comparison supports the empirical relevance of opportunity heterogeneity,
but a better maximised criterion does not by itself prove that the mechanism is
identified.""",
    "{{table:benchmark}}\n\n" + _benchmark,
)
RESULTS = _replace_once(
    RESULTS,
    """consumption in the same samples. These are within-sample dispersion
comparisons, not welfare-loss estimates.""",
    """consumption in the same samples. These are within-sample dispersion
comparisons, not welfare-loss estimates: the gap between the money metric and
observed consumption reflects the leisure a job costs relative to not working,
and no loss index is constructed from it.""",
)
RESULTS = _replace_once(
    RESULTS,
    """An allocated contribution averages a pathway's marginal effect over all
coalition orders; it is not the one-factor reduction.""",
    r"""The coalition values behind the allocation are reported in full. "Change from
actual" is the one-factor effect of each coalition; the Monte Carlo range is the
spread of the Gini level across 1,000 simulation replications, never a
confidence interval.

{{table:pabcoalitionsingles}}

{{table:pabcoalitioncouples}}

Consumption dispersion is large relative to dispersion in log well-being: the
variance of log consumption is roughly
{{n:d2_varshare_logC_couples|.0f}}–{{n:d2_varshare_logC_singles|.0f}}% of the
variance of log well-being, the excess offset by a large negative covariance
between consumption and the value of leisure. Household resources, needs and
composition stay outside the allocation, as do sex-specific parameter
differences and behavioural randomness.

**Robustness.** Every coalition Gini and every Shapley contribution reproduces
closely under an independent second simulation seed, including the sign change
of the preference contribution. The simulation always includes each household's
own observed job, which {{n:d2_anchorshare_singles|.1f}}% of single adults and
{{n:d2_anchorshare_couples|.1f}}% of couples attain under every coalition;
excluding it moves $\Delta I$ by at most {{n:d2_anchormove_pct|.1f}}% (couples,
equivalised), with no sign change in any specification.

An allocated contribution averages a pathway's marginal effect over all
coalition orders; it is not the one-factor reduction.""",
)


# --------------------------------------------------------------------------- #
# Section 6: merge the predecessor limitations
# --------------------------------------------------------------------------- #

LIMITS = v11.LIMITS
LIMITS = _replace_once(
    LIMITS,
    """systematic wage-offer locations, not the common dispersion of wages, realised
wage luck or selection.""",
    """systematic wage-offer locations, not the common dispersion of wages, realised
wage luck or selection. Those location differences shift offered wages by at most
about {{n:diag1_location_log|.2f}} log points, against a common offer spread of
about {{n:diag1_sigma|.2f}} log points, so the operator removes a small part of
earnings dispersion by construction; this is a definitional boundary, not a
measurement error.""",
)
LIMITS = _replace_once(
    LIMITS,
    """own finding rather than absorbed into a wider full-time interval. Aggregate fit
does not eliminate these group- and margin-specific discrepancies.""",
    """own finding rather than absorbed into a wider full-time interval. Aggregate fit
does not eliminate these group- and margin-specific discrepancies.

The common-opportunity benchmarks carried one input defect. The first benchmark's
estimation input used a different width for the residual hours set, which shifts
its log hours density by a constant that cancels from the conditional
likelihood; its estimates, standard errors and criterion comparison are
unchanged, and the second benchmark does not use those rows. Its absolute
opportunity-mass levels were nonetheless mis-scaled, and the benchmark fit
moments reported above are the corrected ones. No downstream use of those
absolute levels was found, but the search was not exhaustive.

Wage elasticities are not reported. A valid gross-wage perturbation requires new
tax-benefit pricing of the affected job alternatives, and the priced support
used here does not contain that counterfactual.""",
)
LIMITS = _replace_once(
    LIMITS,
    """Finally, the weekly time
endowment is maintained rather than estimated, and the model is not invariant
to changing it.""",
    r"""Finally, the weekly time
endowment is maintained rather than estimated, and the model is not invariant
to changing it. Re-estimating the model with an endowment of 75 or 90 hours
instead of 80 rebuilds physical leisure, moves the criterion materially in
opposite directions and changes which single-adult coefficients sit at their
bounds; the couples model has no coefficient at a bound in any of the three.
The 80-hour baseline is a maintained convention.

{{figure:ws4time}}
""",
)


# --------------------------------------------------------------------------- #
# Appendix: implementation only
# --------------------------------------------------------------------------- #

_estimation = v11.IMPLEMENTATION_RECORD.split("## Implementation record: observed labour-force status", 1)[0]
_estimation = _replace_once(_estimation, "## Implementation record: estimation",
                            "## Implementation record: sampled-alternative likelihood and optimiser")
_estimation = _replace_once(_estimation, v11.RESTRICTIONS_PARAGRAPH + "\n\n", "")
_estimation = _replace_once(
    _estimation,
    """This appendix is excluded from the reader-facing language audit. It collects the
implementation detail moved out of the main text in this version, followed by
the certified ex-ante calculation record and the preserved technical record of
earlier versions.""",
    """This appendix contains implementation material only: the estimation device,
parameter code names, simulation and integration design, numerical diagnostics,
the illustration's selection method, pricing and certification records, and
superseded historical status statements. Every economic object and result is in
the main text.""",
)

_adequacy = reader_voice(_between(
    v7.RESULTS, "The corrected POSFIT-v3b numerical-adequacy gate is applied mechanically",
    "not preserved."))

APPENDIX_BODY = _estimation.rstrip() + r"""

## Implementation record: estimated parameter vectors and code names

""" + v11.RESTRICTIONS_PARAGRAPH + r"""

One single-adult coordinate, the female age-square term, is at its box endpoint.
Under the active-set convention its interval is not reported and the interior
curvature is computed after removing it.

{{table:fullsingles}}

{{table:fullcouples}}

## Implementation record: attained-bundle counterfactual simulation

The attained-bundle decomposition reuses the already-priced estimation sample,
with no re-estimation and no new pricing. For each coalition, household-constant
covariates of the equalised pathways are replaced by their household-weighted
sample means; covariates that vary across a household's alternatives are
protected. Each household's attained bundle is then simulated with the
Gumbel-max rule under common random numbers, so realised taste draws are carried
through every coalition, and the attained-bundle money metric and Gini are
recomputed. The executed access substitution covers local unemployment exposure,
region, urbanisation and year.

Each coalition value is the mean over 1,000 replications at fixed estimates; the
reported Monte Carlo range is the spread across replications. An independent
second seed reproduces the allocation. A per-replication share range, which
divides by that replication's own near-zero $\Delta I$, is not informative on its
own and is not shown. The allocation closes to machine precision in every sample
and scale. The simulation sample always includes each household's observed job;
the robustness check that excludes it is reported in Section 5. Neither
counterfactual-attainment route for a final decomposition is executed here.

## Implementation record: predictive-fit numerical precision

""" + _adequacy + r"""

{{figure:nodeconvergence}}

""" + illustration.APPENDIX_BLOCK.strip() + r"""

## Implementation record: data access, software and replication

**Data.** French EU-SILC, accessed through Eurostat's harmonised release, with
2016 survey collection and a 2015 income reference year, transformed into an
input file for EUROMOD [@sutherlandfigari2013] under the French 2015 policy
system. Regional labour-market conditions come from the Eurostat regional
labour-force series. Microdata access is granted under Eurostat's research-access
conditions and the data cannot be redistributed.

**Software.** Python with JAX (0.10.1) for automatic differentiation, and the
EUROMOD connector (0.2.17).

**Replication.** Code and derived, non-confidential intermediate artefacts will
be released in a public replication archive on publication; every step is
reproducible conditional on authorised access to EU-SILC.

"""

_certified = "## Certified ex-ante calculation" + v10.PROVENANCE.split("## Certified ex-ante calculation", 1)[1]
_q26 = next(a for q, a in v7.QA if q == "Is the ex-ante opportunity-prospect metric a result?")

HISTORICAL = r"""
## Historical status statements, superseded before V9

""" + v10.SUPERSEDED_NOTE + r"""

*Superseded before V9.* Earlier versions printed the following paragraph three
times: in their introduction, under the heading "The distinct ex-ante
opportunity-prospect metric", and under the heading "Numerically blocked
opportunity-prospect metric".

> """ + v7.WEA_STATUS + r"""

*Superseded before V9.* Earlier question "Is the ex-ante opportunity-prospect
metric a result?", with its answer:

> """ + _q26 + r"""

*Superseded before V9.* Earlier status sentence of the attained-bundle
decomposition appendix:

> """ + v6.MISSION_WORDING + "\n"

PROVENANCE = APPENDIX_BODY + _certified.rstrip() + "\n\n" + HISTORICAL


SECTIONS = []
for _section in v11.SECTIONS:
    _new = dict(_section)
    _new["body"] = {"model": LATENT_JOBS, "results": RESULTS, "limits": LIMITS,
                    "provenance": PROVENANCE}.get(_section["key"], _section["body"])
    SECTIONS.append(_new)

QA = []
