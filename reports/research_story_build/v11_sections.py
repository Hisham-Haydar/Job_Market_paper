"""Reader-facing sections for the V11 research-story report (Stage B).

V11 rebuilds the economic derivation on top of the V10 release: an
introduction that states the full logical chain, the structural objects in the
body with their reason, meaning and empirical use, welfare organised as two
perspectives (outcomes versus prospects), the decomposition with household
resources, needs and composition explicitly held fixed, and implementation
detail moved to the technical appendix. No number changes; every scalar is
bound to the V10 registry or to the certified ex-ante record.
"""
from __future__ import annotations

import re

import v5_sections as v5
import v9_sections as v9
import v10_sections as v10
import v11_illustration as illustration


TITLE = v10.TITLE
reader_voice = v9.reader_voice

D_STATUS = (
    "The current decomposition equalises preferences, geographic/temporal job "
    "access and systematic earning opportunities while holding household "
    "resources, needs and composition fixed."
)

PERSPECTIVES_SENTENCE = (
    "The two measures answer different welfare questions. The attained-bundle "
    "measure evaluates the bundle eventually reached against a common "
    "non-employment reference. The ex-ante measure evaluates the household's "
    "entire distribution of potential job outcomes against a reference prospect "
    "that preserves the same opportunity environment while equalising "
    "consumption across jobs."
)

INTERPRETATION_SENTENCE = (
    "The importance assigned to different labour-market inequalities depends on "
    "whether welfare evaluates the realised outcome or the opportunity prospect "
    "itself."
)


def _replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise RuntimeError("expected exactly one occurrence of: " + old[:90])
    return text.replace(old, new, 1)


def _cut_between(text: str, start: str, end: str) -> tuple[str, str]:
    """Remove text[start:end) (start inclusive, end exclusive); return both."""
    i = text.index(start)
    j = text.index(end, i)
    return text[:i] + text[j:], text[i:j]


def _drop_paragraph(text: str, prefix: str) -> tuple[str, str]:
    paragraphs = text.split("\n\n")
    hits = [k for k, p in enumerate(paragraphs) if p.lstrip().startswith(prefix)]
    if len(hits) != 1:
        raise RuntimeError("expected one paragraph starting with: " + prefix)
    removed = paragraphs.pop(hits[0])
    return "\n\n".join(paragraphs), removed


ABSTRACT = r"""Observed income inequality is not welfare inequality: households
differ in what they prefer and in the jobs they can reach, and observed
labour-supply choices mix the two. We estimate a random-utility,
random-opportunity model of job choice on French EU-SILC data priced through
EUROMOD, translate it into money-metric well-being under two perspectives, and
allocate counterfactual changes in the Gini with an exact Shapley rule. The
current decomposition equalises preferences, geographic/temporal job access and
systematic earning opportunities while holding household resources, needs and
composition fixed. When welfare evaluates the bundle a household actually
attains, access and earning opportunities together account for
{{n:att_opportunity_min_pct|.1f}}–{{n:att_opportunity_max_pct|.1f}}% of baseline
inequality and earning opportunities matter more than access. When welfare
evaluates the whole opportunity prospect, they account for
{{n:wea_opportunity_min_pct|.1f}}–{{n:wea_opportunity_max_pct|.1f}}%, and for
single-adult households access becomes about three times as important as earning
opportunities; couples show no such reversal. The importance assigned to
different labour-market inequalities therefore depends on whether welfare
evaluates the realised outcome or the opportunity prospect itself. These are
restricted structural accounting shares: they are not causal estimates and do
not estimate the total share of well-being inequality caused by unequal job
opportunities."""

PRELIM_NOTE = (
    "Discussion draft. The attained-bundle counterfactual integration remains "
    "preliminary; the ex-ante calculation has passed its numerical checks. Both "
    "are restricted structural accounting exercises, not causal decompositions, "
    "and neither welfare perspective is designated as primary."
)


# --------------------------------------------------------------------------- #
# 1. Introduction
# --------------------------------------------------------------------------- #

_literature = v9._literature
_literature = _replace_once(
    _literature,
    "with the factors defined as structural operators inside an estimated "
    "job-choice model: what a household prefers, which jobs it can reach, what "
    "those jobs pay, and what its budget and needs are.",
    "with the factors defined as structural operators inside an estimated "
    "job-choice model: what a household prefers, which jobs it can reach and "
    "what those jobs pay, with its budget, needs and composition held fixed.",
)
_literature = _replace_once(
    _literature,
    ", reported as preliminary and work in progress pending the "
    "counterfactual-attainment estimand of Section 4.",
    ", applied identically to both welfare perspectives.",
)
_literature = _replace_once(
    _literature,
    "The preliminary three-operator exercise of Section 5",
    "The three-operator exercise of Section 4",
)

INTRO = r"""
Two people can work the same hours for the same hourly pay and be very
differently placed. One chose that job from several that were open; the other
took the only offer available. Their incomes are identical and their
circumstances are not. This paper is about what that difference does to the
measurement of well-being inequality.

## The logical chain

**Observed income inequality is not necessarily welfare inequality.**
Households differ in their preferences over consumption and leisure, in the
constraints that shape their budgets and needs, and in the job prospects they
face. Low earnings can describe someone who values leisure and chose short
hours, someone who cannot obtain a well-paid job, or someone whose household
resources make a different arrangement affordable. A distribution of income
records outcomes with these explanations already mixed in.

**Observed labour-supply choices do not identify preferences alone.** A
household is seen in a job because it wanted that job *and* because that job
was available. If part-time work is rare in a local labour market, few people
will be observed working part time even if many would like to. Choice
frequencies therefore reflect the density of opportunities as well as tastes,
and a model that gives everyone the same set of jobs must read every difference
in behaviour as a difference in preferences.

**Therefore four steps are needed, each answering a question the previous one
leaves open.**

1. *A structural labour-supply model that separates preferences from
   opportunities.* Without it there is nothing to attribute: the econometrician
   cannot tell whether a household works little because it prefers to or
   because it cannot find more work. Section 2 sets out that model.
2. *A money-metric welfare mapping.* Estimated utility is not an interpersonal
   welfare index, because preferences differ. Comparing households requires a
   common monetary yardstick with an explicit reference. Section 3 constructs
   two, each answering a different welfare question.
3. *Structural equalisation counterfactuals.* To ask how much inequality is
   associated with a source of heterogeneity, the source is replaced by a
   common reference inside the model, welfare is recomputed and inequality is
   measured again. Section 4 defines those counterfactuals.
4. *An order-independent decomposition.* The sources interact, so the effect
   of equalising one depends on which others have already been equalised. The
   Shapley value averages over every order. Section 4 applies it.

## Why this matters

A distributional analysis based only on realised disposable income can miss
heterogeneity in the labour-market prospects that households face. Two
households with the same income may differ in how many jobs they can reach, in
the hours those jobs offer and in what they pay. Whether that heterogeneity
should count in a welfare comparison, and how much inequality is associated
with it, are empirical and normative questions that an income distribution
cannot answer.

The paper asks whether welfare inequality is associated primarily with
systematic preferences, with geographic and temporal job access, or with
systematic earning opportunities. The answer can identify which margins deserve
explicit attention in later policy analysis. It does not show that an
opportunity policy is more effective or cheaper than redistribution: that
comparison requires a policy experiment and cost estimates that are not part of
this paper.

## What the paper does and finds

The empirical strategy joins a random-utility model to a random-opportunity
model. Jobs are packages of employment, occupation, weekly hours and hourly
wages; couples choose two packages under a shared household budget. Every
package is priced through the French tax-benefit system. The model separates
systematic variation in the value of consumption and leisure from systematic
variation in employment access, hours, occupations and wage offers, subject to
explicit maintained assumptions.

Well-being is then measured from two perspectives. The attained-bundle
perspective (ATT) asks how well off a household is in the bundle it actually
attains. The ex-ante perspective (EA) asks how valuable the distribution of job
prospects it faces is. """ + PERSPECTIVES_SENTENCE + r"""

""" + D_STATUS + r""" Interactions are allocated with an exact Shapley rule,
separately for each welfare perspective and for single-adult and couple
households. A fourth pathway for household resources, needs and composition is
a planned extension, not part of the present results.

The central result is a contrast. Under attained-bundle welfare, earning
opportunities matter more than the coarse access channel, for both household
types and on both reporting scales. Under ex-ante welfare, access becomes much
more important for single-adult households—about three times earning
opportunities. Couples show no such reversal: earning opportunities remain
larger than access. """ + INTERPRETATION_SENTENCE + r""" The contrast is not a
disagreement to be resolved by choosing a winner; it shows what each welfare
question makes visible, and neither perspective is designated primary here.

## Relation to existing work

""" + reader_voice(_literature) + r"""
The contribution is therefore the conjunction of four elements: household-
specific latent job opportunities, a tax-benefit-consistent budget for every
work arrangement, explicit money-metric comparisons under two welfare
perspectives, and a complete interaction-aware accounting across the declared
pathways.

## Roadmap

Section 2 presents the latent-jobs model and a matched-household illustration
of what unequal opportunity means inside it. Section 3 turns choices into
well-being under the two perspectives. Section 4 defines the counterfactual
inequality object and the Shapley allocation. Section 5 reports estimates, fit,
well-being and both decompositions. Section 6 collects what remains
preliminary. Implementation, numerical verification and provenance are in the
appendix.
"""


# --------------------------------------------------------------------------- #
# 2. Model
# --------------------------------------------------------------------------- #

_data = v5.DATA
_data, LES_BLOCK = _cut_between(_data, "{{report-only}}\n### Observed raw labour-force status",
                                "## The household budget")
_data = _replace_once(
    _data,
    "The accounting identity linking original income, benefits, taxes and social "
    "contributions to disposable income holds to machine precision at both the "
    "person and the household-alternative level, before and after the benefit "
    "take-up adjustment. ",
    "",
)
_data = _replace_once(
    _data, "## The household budget",
    "Both spouses' labour-force status is mapped to employment or "
    "non-employment; the model does not distinguish unemployment from "
    "inactivity. The appendix reports the raw status breakdown.\n\n"
    "## The household budget",
)
_data = _data.replace("Section 4", "Section 3")
DATA = reader_voice(_data)

MODEL = r"""
## Jobs as packages

A job is a package $j$: an employment state $e\in\{0,1\}$ and, when employed,
an occupation $k\in\{1,\dots,{{n:n_occ}}\}$, weekly hours
$h\in[{{n:hours_floor}},{{n:hours_cap}}]$ and an hourly wage
$w\in[{{n:wage_lo}},{{n:wage_hi}}]$. The base measure $\nu$ places mass one on
the single non-employment state $o$ and, on the employed part, counting measure
over occupations with Lebesgue measure over hours and wages. A single adult
chooses one package; a couple chooses one pair of packages under a shared
budget. Every package is priced: $C_i(j)$ is the household's monthly disposable
consumption at $j$ after taxes and transfers.

## A. Systematic utility

**Why.** A labour-supply model must say what a household gains from a job
(consumption) and what it gives up (leisure). Welfare comparisons later need
the two to be separable, because consumption is observable in euros while the
value of leisure is not.

**Object.** For a single adult of sex group $g$ the systematic utility of
package $j$ is

$$
v_i(j)=L_i(j)+\beta_c\log\!\left(\frac{C_i(j)}{\lambda_c}\right),
\qquad
L_i(j)=\beta_{\ell}^{g}(\mathbf x_i)\,
\mathcal B\!\left(\tilde\ell_i(j);\theta_{\ell}^{g}\right),
$$

$$
\beta_{\ell}^{g}(\mathbf x_i)=\beta_{\ell 0}^{g}+\beta_{\ell a}^{g}a_i
+\beta_{\ell a^{2}}^{g}a_i^{2}+\mathbb 1\{g=\text{women}\}\,\beta_{\ell k}^{g}k_i .
$$

**Interpretation.** $L_i(j)$ is the complete non-consumption value of the
package: normalised leisure $\tilde\ell_i(j)=({{n:time_endowment}}-h)/{{n:leisure_scale}}$
passed through the Box-Cox transform $\mathcal B(z;\theta)=(z^{\theta}-1)/\theta$,
with $\mathcal B(z;0)=\log z$. The household-specific weight
$\beta_{\ell}^{g}(\mathbf x_i)$ varies with centred age $a_i$ and, for women, with
the number of children $k_i$; $\theta_{\ell}^{g}$ governs curvature. The child
term is a reduced-form behavioural and time-constraint shifter, not pure
taste. $\beta_c$ is the weight on log consumption and is estimated, not fixed.
$\lambda_c$ is a units convention that cancels from every choice probability.
For a couple, $L_i(j)$ is the sum of the two spouses' leisure terms, with no
direct cross-leisure term, and $C_i(j)$ is the household's joint consumption.
The random-utility shock is i.i.d. type-I extreme value with unit scale, so
utility is measured in the natural unit of that scale.

**Empirical use.** $v_i(j)$ is the preference half of the choice law below.
Its split into $L_i$ and $\beta_c\log C_i$ is what later turns a utility
difference into a proportional consumption adjustment in both welfare
measures, and its household-specific coefficients are the preference pathway
$P$ equalised in Section 4.

## B. The choice law with opportunities

**Why.** A standard random-utility model assumes every household chooses from
the same set of jobs. Then any difference in what households do has to be a
difference in what they want. If jobs are not equally available, that reading
attributes scarcity to taste.

**Object.** In the random-utility, random-opportunity model the probability
that household $i$ is observed in package $j$ is

$$
P_i(j)=\frac{\exp\{v_i(j)\}\,g_i(j)}
{\displaystyle\int\exp\{v_i(k)\}\,g_i(k)\,d\nu(k)} .
$$

**Interpretation.** $g_i(j)$ is the household's opportunity density: the
relative intensity with which package $j$ is available to it before any choice
is made. A package is chosen often when it is valued ($v_i$ high) *or* when it
is plentiful ($g_i$ high). Observed choices therefore reflect both systematic
preferences and the density of opportunities. A common-opportunity model is the
special case in which $g_i$ is the same for everyone, so that $P_i(j)$ depends
on $v_i$ alone. Rescaling $g_i$ by a household-specific constant leaves $P_i$
unchanged, which is why only the shape of the opportunity environment, not its
level, is estimated.

**Empirical use.** This law is the likelihood that is estimated. It is also the
central distinction of the paper: because $g_i$ is household-specific, the
model can attribute part of observed behaviour to reachability rather than to
taste, and both welfare perspectives inherit that separation.

## C. The structure of opportunities

**Why.** "Opportunity" is not one object. A household may face few jobs, jobs
concentrated at particular hours, a particular occupational mix, or low offered
wages. These margins have different economic meaning and must be separable to
be equalised one at a time.

**Object.** The opportunity density factorises into four blocks, switched off
on non-employment by $E_i(j)=\mathbb 1\{h>0\}$:

$$
g_i(j)=g^{E}_i\cdot\left(g^{H}_i(h)\cdot g^{\mathrm{Occ}}_i(k)\cdot
g^{W}_i(w\mid k)\right)^{E_i(j)} .
$$

**Interpretation.**
**Access**, $g^{E}_i=\exp\{\beta_E+\beta_s s_i+\sum_{r=2}^{8}\beta_r\,\mathrm{reg}_{ir}+\beta_u u_i+\beta_m m_i\}$,
is the employment mass: it moves with the local group unemployment measure
$s_i$, region and urbanisation, and survey year where it applies.
**Hours**, $g^{H}_i(h)=\exp\{\sum_b \beta_b\mathbb 1\{h\in b\}\}$, elevates five
bands over a residual set of width {{n:hours_reference_width}} hours per week;
the narrow full-time band $[33.5,36.5)$ is a density elevation over an
interval, not an atom at thirty-five hours.
**Occupation**, $g^{\mathrm{Occ}}_i(k)=\exp\{\beta^{\mathrm{occ}}_{k,g}\}$, with
group 1 as reference.
**Wage offer**, $g^{W}_i(w\mid k)$, is log-normal with location
$\mu_i(k)=\beta_{w0}+\beta_{wL}L_i+\beta_{wH}H_i+\beta_{wx}x_i+\beta_{wx^{2}}x_i^{2}+\delta_k$
in education, potential experience and occupation, dispersion $\sigma$, and is
truncated to $[{{n:wage_lo}},{{n:wage_hi}}]$ euros per hour and renormalised on
that support.

In the preferred specification, the dimensions that vary across households are
the access shifters (local unemployment exposure, region, urbanisation and
year), the wage-offer location (education and experience), and the sex- and
household-type-specific hours and occupation blocks. The hours and occupation
blocks do not vary with other household characteristics within a group.

The decomposition pathway $A$ equalises only the access shifters: local
unemployment exposure, region, urbanisation and year. It is the estimated geographic/temporal access channel, not all job
opportunities: personal occupation access, the hours density and every other
feature of a feasible job are left as estimated. The pathway $B$ equalises the
systematic wage-offer location, not the common wage dispersion.

**Empirical use.** The factorisation defines what the equalisation operators of
Section 4 can change. It also determines how opportunities reach welfare: in
the attained-bundle perspective only through the job eventually attained, and
in the ex-ante perspective directly, as weights on the whole prospect.

""" + illustration.REPORT_BLOCK + r"""

## Identification, in words

Choices alone do not separate a taste for leisure from a scarcity of jobs at
that number of hours. Three kinds of restriction do the work. Preferences are
smooth in hours, while the opportunity density is a step function over bands,
so a spike in observed hours at a band is read as availability rather than as
a kink in tastes. Excluded shifters enter availability and not preferences: the
local group unemployment measure and the regional and urbanisation indicators
shift access and appear nowhere in utility. And the wage-offer distribution is
independent of offered hours conditional on occupation, which separates the
wage location from the hours density. These are the restrictions of
@capeau2016 and @dagsvikjia2016, maintained here rather than tested. The
regional variation supports the access block conditional on those
restrictions; it is not a causal design, and no causal effect of geography is
claimed.

## Estimation, in words

Because the set of possible jobs is a continuum, the likelihood is evaluated on
a set of sampled alternatives for each household, every one priced through the
tax-benefit system, with a correction that makes the sample stand in for the
full opportunity environment. The sampling device is computational: it is not
an offer, an availability or an opportunity, and it enters no welfare measure.
Standard errors are cluster-robust on the household. The sampled-set
probability, the proposal design, the optimiser and the curvature diagnostics
are reported in the appendix.
"""

LATENT_JOBS = reader_voice(DATA) + "\n\n" + MODEL


# --------------------------------------------------------------------------- #
# 3. Welfare
# --------------------------------------------------------------------------- #

WELFARE = r"""
Estimated utility is not an interpersonal monetary welfare index. Its units are
those of the taste shock, preferences differ across households, and the same
utility number means different things for different people. To compare
households, each one's situation is translated into euros through an
indifference condition: the consumption level that would leave the household
exactly as well off in an explicitly stated reference situation. The choice of
reference is the welfare question being asked. This section asks two.

""" + PERSPECTIVES_SENTENCE + r"""

## Perspective 1 — ATT: how well off is the household in the bundle it actually attains?

**Why.** Households end up in particular jobs. A natural welfare question
values that realised outcome, consumption and leisure together, in a common
monetary unit.

**Object.** Let $j_i^{\mathrm{obs}}$ be the observed package and $o$ the
non-employment state, which is available to every household. The
attained-bundle money metric $M_i^{\mathrm{att}}$ solves the indifference condition

$$
L_i(o)+\beta_c\log\!\left(\frac{M_i^{\mathrm{att}}}{\lambda_c}\right)
=L_i(j_i^{\mathrm{obs}})+\beta_c\log\!\left(\frac{C_i^{\mathrm{obs}}}{\lambda_c}\right),
$$

so that

$$
\boxed{
M_i^{\mathrm{att}}
=C_i^{\mathrm{obs}}
\exp\!\left\{
\frac{L_i(j_i^{\mathrm{obs}})-L_i(o)}{\beta_c}
\right\}.}
$$

**Interpretation.** $M_i^{\mathrm{att}}$ is the monthly consumption at
non-employment that would be as good as the household's actual job and actual
consumption. The reference is non-employment, which every household can reach.
The measure values the attained bundle: observed consumption, adjusted by the
leisure the job costs relative to not working, converted at the rate
$1/\beta_c$. The normaliser $\lambda_c$ cancels. Opportunity density has no
direct term in this measure conditional on the attained bundle. Opportunities
matter because they shape which job becomes $j_i^{\mathrm{obs}}$ and what it
pays; once that job is fixed, jobs not taken play no role.

The general construction evaluates the attained bundle against the job the
household would most prefer if every job paid the same consumption. On the
current empirical domain that job is non-employment for every household in both
samples, because non-employment maximises the non-consumption index. The
measure therefore coincides with the staying-home equivalent. This is a
verified property of the estimated specification, not a general theorem: with a
different leisure specification or a different reference, the two could
separate. For non-workers, $M_i^{\mathrm{att}}=C_i^{\mathrm{obs}}$; for workers
it lies below observed consumption by the value of the leisure given up.

**Empirical use.** $M_i^{\mathrm{att}}$ is computed for every household from
its own priced consumption, its estimated leisure index and $\beta_c$. Its
distribution and its counterfactual versions under the operators of Section 4
give the attained-bundle decomposition.

## Perspective 2 — EA: how valuable is the distribution of job prospects the household faces?

**Why.** The attained-bundle measure values the outcome reached. A welfare
question about opportunities may also treat the quality of the prospect itself
as welfare-relevant: a household facing many good jobs is, before any job is
realised, in a different position from one facing few, even if both end up in
similar jobs. A second perspective values that prospect directly.

**Object.** Let $\widehat g_i$ be the household's estimated opportunity density
on its job domain $\Omega_i$. The value of the actual prospect is

$$
J_i
=\int_{\Omega_i}
\exp\{L_i(j)\}
\left(\frac{C_i(j)}{\lambda_c}\right)^{\beta_c}
\widehat g_i(j)\,d\nu(j),
$$

and the value of a reference prospect with the same opportunities and the same
preferences, but the same consumption $m$ at every job, is
$(m/\lambda_c)^{\beta_c}H_i$ with

$$
H_i
=\int_{\Omega_i}\exp\{L_i(j)\}\,\widehat g_i(j)\,d\nu(j).
$$

The ex-ante money metric $M_i^{\mathrm{EA}}$ is the common consumption at which
the reference prospect is exactly as valuable as the actual one,
$J_i^{\mathrm{ref}}(M_i^{\mathrm{EA}})=J_i$:

$$
\boxed{
M_i^{\mathrm{EA}}
=\lambda_c\exp\!\left\{
\frac{\log J_i-\log H_i}{\beta_c}
\right\}.}
$$

**Interpretation.** Four things follow.

1. $J_i$ values the household's actual consumption prospects over its whole
   estimated opportunity environment: every job enters, weighted by how
   available it is and how much the household values it.
2. $H_i$ builds the own-opportunity, flat-consumption reference: the same jobs,
   the same availability and the same preferences, with pay differences
   removed.
3. $M_i^{\mathrm{EA}}$ is the constant consumption level that makes that
   reference prospect equivalent to the actual prospect. It is in euros per
   month.
4. Opportunity composition therefore enters welfare directly. A common
   rescaling of $\widehat g_i$ multiplies $J_i$ and $H_i$ alike and cancels;
   what does not cancel is how opportunity weight is spread across jobs with
   different consumption and leisure. Access changes which jobs receive weight;
   earning opportunities change the consumption those jobs deliver.

The integrals have a random-utility reading. Under the maintained type-I
extreme-value shocks and latent-job structure, $\log J_i$ is, up to an additive
constant common to $J_i$ and $H_i$, the expected utility of the best job the
household can reach, averaged over the jobs that happen to be available and
over its taste shocks. The ex-ante measure therefore treats the dispersion of
those shocks as part of what makes a rich prospect valuable. That is a
normative position, not a consequence of estimation: if the shocks are read as
optimisation errors rather than as idiosyncratic tastes, part of the value
attributed to variety would not be welfare. The reference prospect carries the
same shocks and the same opportunity environment, which limits but does not
remove this dependence.

**Empirical use.** $J_i$ and $H_i$ are integrated numerically over each
household's estimated opportunity environment, with every integration point
priced through the tax-benefit system. The resulting $M_i^{\mathrm{EA}}$ and its
counterfactual versions give the ex-ante decomposition. Integration design,
reference-domain convention and numerical checks are in the appendix.

## Outcomes versus prospects

Neither perspective corrects the other. The attained-bundle measure answers a
question about outcomes and the ex-ante measure a question about prospects, and
both are money metrics derived from an explicit indifference condition. Because
opportunities reach them through different routes—through the realised job in
one case and as weights on the whole prospect in the other—the two can
attribute inequality to different labour-market channels. When they do, the
difference is informative about what each welfare question makes visible. The
choice between them is a substantive normative decision and is not made here.

## F. Equivalisation

**Why.** Both money metrics are household-level consumption equivalents.
Inequality comparisons across households of different size and composition
require a convention for resources and needs.

**Object.** For either perspective $p\in\{\mathrm{att},\mathrm{EA}\}$,

$$
M_i^{p,\mathrm{eq}}=\frac{M_i^{p}}{e_i},
$$

where $e_i$ is the modified-OECD equivalence scale of household $i$.

**Interpretation.** $e_i$ is a normative reporting convention, not an
estimated parameter. Every result is reported both on the raw household basis
and equivalised. Single-adult and couple households are separate estimated
populations and their welfare levels are never pooled or compared.

**Empirical use.** The convention is substantively consequential, not a
formatting choice. For couples under the ex-ante perspective, equivalising
moves the access-plus-earnings share of baseline inequality from
{{n:wea_couples_opportunity_uneq_pct|.1f}}% to
{{n:wea_couples_opportunity_eq_pct|.1f}}% and turns the preference contribution
negative. That is why both bases are always shown.
"""


# --------------------------------------------------------------------------- #
# 4. Decomposition
# --------------------------------------------------------------------------- #

DECOMPOSITION = r"""
""" + D_STATUS + r""" Household resources, needs and composition are not
equalised and receive no allocated share, so the three pathways do not exhaust
the sources of welfare inequality.

## G. Counterfactual inequality

**Why.** A well-being distribution alone does not say which sources of
heterogeneity it reflects. To ask how much inequality is associated with a
pathway, the pathway must be removed inside the model and welfare recomputed.

**Object.** Write household $i$'s structural inputs as
$x_i=(x_i^P,x_i^A,x_i^B,d_i)$: the characteristics that shift systematic
utility, the geographic and temporal access shifters, the characteristics that
shift the wage-offer location, and household resources, needs and composition.
The operators

$$
\begin{aligned}
T_Px_i&=(\bar x^P,x_i^A,x_i^B,d_i),\\
T_Ax_i&=(x_i^P,\bar x^A,x_i^B,d_i),\\
T_Bx_i&=(x_i^P,x_i^A,\bar x^B,d_i)
\end{aligned}
$$

replace one pathway by a common reference profile, and $T_S$ applies the
substitutions named by a coalition $S\subseteq\{P,A,B\}$ together. With
$\mathcal G$ the household-weighted Gini,

$$
I^p(S)=\mathcal G\!\left(\left\{M_i^p(T_Sx_i)\right\}_{i=1}^N\right),
\qquad
v^p(S)=I^p(\varnothing)-I^p(S).
$$

**Interpretation.** Each coalition is a structural counterfactual: the named
sources of heterogeneity are equalised, welfare is fully recomputed for every
household under perspective $p$, and inequality is measured again. $T_P$
equalises age profiles and the child-related shifter while keeping sex- and
household-type-specific blocks. $T_A$ equalises local unemployment exposure, region,
urbanisation and year where they enter access—the geographic/temporal channel,
not all job opportunities. $T_B$ equalises the education- and experience-related
wage-offer location, not wage dispersion, wage luck or selection. Estimated
coefficients are never changed, and $d_i$ is the same in every coalition, so
$I^p(\{P,A,B\})$ generally remains positive. $v^p(S)$ is the inequality removed
by equalising the pathways in $S$.

**Empirical use.** $I^p(S)$ is the bridge from the estimated model to the
decomposition: eight coalitions per perspective, household type and scale,
each with complete recomputation of welfare and inequality.

## H. Shapley allocation

**Why.** The pathways interact. The inequality removed by equalising access
depends on whether preferences or earning opportunities have already been
equalised. Reporting one ordering would make the answer depend on an arbitrary
choice.

**Object.** For $k\in\{P,A,B\}$,

$$
\phi_k^p
=\sum_{S\subseteq\{P,A,B\}\setminus\{k\}}
\frac{|S|!\,(3-|S|-1)!}{3!}
\left[v^p(S\cup\{k\})-v^p(S)\right],
\qquad
\phi_P^p+\phi_A^p+\phi_B^p=I^p(\varnothing)-I^p(\{P,A,B\})\equiv\Delta I^p .
$$

**Interpretation.** $\phi_k^p$ is the marginal contribution of pathway $k$
averaged over all $3!=6$ orders in which the three equalisations can be
introduced. The allocation adds up exactly to the movable component
$\Delta I^p$. Contributions are signed: a negative term means that, on average
over orders, equalising that pathway raises inequality. This is the standard
Shapley value from cooperative game theory, applied as in the distributional
decomposition literature; no new allocation principle is claimed.

**Empirical use.** Two denominators are kept apart. A share of $\Delta I^p$
describes how the movable component is allocated. A share of
$I^p(\varnothing)$ describes the size of a contribution relative to baseline
inequality. The headline access-plus-earnings figures are shares of each
perspective's own baseline Gini. The same operators and allocation rule are
applied to both welfare perspectives, which makes their channel orderings
comparable.

## A planned extension: household resources, needs and composition

A fourth pathway $D$, equalising household resources, needs and composition,
is a planned extension and is not part of the present results. If it is added,
$A+B$ remains the labour-market opportunity component, while $A+B+D$ would
describe broader non-preference circumstances. $A+B+D$ would not be an
opportunity share.
"""


# --------------------------------------------------------------------------- #
# 5. Results
# --------------------------------------------------------------------------- #

_behaviour = v5.RESULTS.split("## Fit", 1)[0]
_behaviour = _behaviour.replace("Section 4", "Section 3")
_behaviour, OPTIMISER_PARAGRAPH = _drop_paragraph(_behaviour, "The estimated model has")
_behaviour, RESTRICTIONS_PARAGRAPH = _drop_paragraph(_behaviour, "**Maintained restrictions.**")
_behaviour = _replace_once(
    _behaviour, "## Behavioural estimates\n",
    "## Behavioural estimates\n\nThe preference, opportunity and wage blocks are "
    "estimated separately for single adults and couples. Optimiser paths, "
    "curvature diagnostics and the complete list of maintained parameter "
    "restrictions are in the appendix.\n",
)
_behaviour = _replace_once(
    _behaviour, "{{table:wage}}",
    "{{table:wage}}\n\nSome coefficients are restricted rather than estimated: "
    "consumption enters in exact logs, the male children leisure effect in "
    "couples is zero, and couples have no direct cross-leisure term. The singles "
    "and couples models are estimated separately, so their wage blocks are not "
    "restricted to agree.",
)

_v9_results = v9.CURRENT_RESULTS.split("## Predictive fit", 1)[1]
_fit, _rest = _v9_results.split("## Attained-bundle well-being", 1)
_fit, FIT_TABLES = _cut_between(_fit, "{{table:fitsingles}}",
                                "The richer common-opportunity benchmarks")
_fit = _replace_once(
    _fit, "{{figure:fit}}",
    "{{figure:fit}}\n\nThe complete moment-by-moment tables are in the appendix.",
)
_att, _rest = _rest.split("## Ex-ante well-being and decomposition", 1)
_ea, _rest = _rest.split("## The two welfare perspectives side by side", 1)
_ea = _replace_once(
    _ea,
    "The ex-ante perspective values the household's whole job prospect. Its\n"
    "certified distribution and Shapley accounting are:",
    "The ex-ante perspective values the household's whole job prospect. Its\n"
    "distribution and exact Shapley accounting, which passed the numerical checks\n"
    "reported in the appendix, are:",
)

RESULTS = r"""
> **Main result.** Under attained-bundle welfare, earning opportunities matter
> more than the coarse access channel. Under ex-ante welfare, access becomes
> much more important for single-adult households—about three times earning
> opportunities. Couples show no such reversal. """ + INTERPRETATION_SENTENCE + r"""

""" + reader_voice(_behaviour) + r"""
## Predictive fit
""" + _fit + r"""
## Attained-bundle well-being
""" + _att + r"""
## Ex-ante well-being and decomposition
""" + _ea + r"""
## The central result: outcomes versus prospects

{{table:perspective_comparison}}

The comparison applies the same operators and the same allocation rule to both
welfare perspectives. It is not a pure comparison of welfare definitions: the
attained-bundle counterfactual is integrated on a sample that covers short hours
sparsely, while the ex-ante integrals use a separate certified design
(Section 6).

Three findings stand out.

- **ATT: earning opportunities matter more than access.** When welfare values
  the attained bundle, access and earning opportunities together account for
  {{n:att_opportunity_min_pct|.1f}}–{{n:att_opportunity_max_pct|.1f}}% of
  baseline inequality, and earning opportunities are larger than access for
  both household types on both scales.
- **EA: access becomes much more important for single adults.** When welfare
  values the whole prospect, the combined share is
  {{n:wea_opportunity_min_pct|.1f}}–{{n:wea_opportunity_max_pct|.1f}}%, and for
  single-adult households access is
  {{n:wea_singles_access_earn_ratio_uneq|.1f}} times earning opportunities
  before equivalisation and {{n:wea_singles_access_earn_ratio_eq|.1f}} times
  after it.
- **Couples show no such reversal.** Earning opportunities remain larger than
  access for couples under both perspectives and on both scales.

""" + INTERPRETATION_SENTENCE + r""" The economic mechanism is the route by which
opportunities enter each measure. The attained-bundle measure sees only the
realised job, where the wage drives disposable consumption, so systematic
differences in wage offers dominate. The ex-ante measure weights every job by
its availability, so a household's coarse access environment enters welfare
directly. Why the reversal appears for single adults and not for couples is
not tested here; one reading is that a single adult's participation depends on
one earner's access, whereas a couple's joint budget and second earner leave
earning opportunities in front. The reversal is a finding for single-adult
households only. Neither measure is designated primary here.

Earlier circulated figures near 90% described all non-preference
circumstances, including household resources and composition, rather than job
opportunities alone. They are not comparable with the restricted
access-and-earnings figures reported here and are not current results.

All percentages in this section come from restricted three-pathway accounting
exercises that hold household resources, needs and composition fixed. They do
not estimate the total share of well-being inequality caused by unequal job
opportunities.
"""



# --------------------------------------------------------------------------- #
# 6. Limits
# --------------------------------------------------------------------------- #

LIMITS = v9.PRELIMINARY_LIMITS
LIMITS = _replace_once(
    LIMITS,
    "Household resources, needs and composition are fixed\n"
    "throughout and receive no allocated share. The resulting percentages therefore\n"
    "are neither a complete decomposition of well-being inequality nor estimates of\n"
    "the causal effect of geography, education or occupation.",
    "Household resources, needs and composition are fixed\n"
    "throughout and receive no allocated share; adding them as a fourth pathway is\n"
    "a planned extension. The resulting percentages therefore are neither a\n"
    "complete decomposition of well-being inequality nor estimates of the causal\n"
    "effect of geography, education or occupation.",
)
LIMITS = _replace_once(
    LIMITS,
    "certification of a calculation is not certification of the model's maintained\n"
    "economic assumptions.",
    "certification of a calculation is not certification of the model's maintained\n"
    "economic assumptions. " + v10.CERTIFICATION_SCOPE,
)
LIMITS = LIMITS + r"""
## The welfare comparison

The contrast between the two perspectives is computed with identical operators
and allocation rules, but not with identical numerical integration. The
attained-bundle counterfactual carries realised alternatives through a finite
integration sample that represents short hours sparsely; the ex-ante integrals
use a separate, certified integration design. Part of any numerical difference
between the two decompositions could therefore reflect integration rather than
the welfare definition alone, although the channel orderings are stable across
the reported ex-ante sensitivities.
"""


# --------------------------------------------------------------------------- #
# 7. Appendix
# --------------------------------------------------------------------------- #

IMPLEMENTATION_RECORD = r"""
This appendix is excluded from the reader-facing language audit. It collects the
implementation detail moved out of the main text in this version, followed by
the certified ex-ante calculation record and the preserved technical record of
earlier versions.

## Implementation record: estimation

The choice set is a continuum, so the likelihood is evaluated over sampled
alternatives. For each household we draw $R={{n:n_draws}}$ alternatives from a
proposal density $q_{ij}$ and place the observed package in the set as well,
giving a set $\mathcal C_i$ with $|\mathcal C_i|={{n:n_alt_rows}}$ rows. Write the
sampled-set index

$$
V_{ij}=v_i(j)+\log g_i(j)-\log q_{ij},
\qquad
q_{ij}=q^{E}_{ij}\left(q^{H}_{ij}q^{W}_{ij}q^{\mathrm{Occ}}_{ij}\right)^{E_{ij}} .
$$

The contribution of household $i$ is the conditional probability of its
observed package $y$ within that set,

$$
\Pr\!\left(y\mid\mathcal C_i\right)=
\frac{n_{y}\exp V_{iy}}{\sum_{s\in\mathcal C_i}\exp V_{is}} .
$$

The denominator runs over slots rather than distinct packages, and a package
drawn more than once keeps its multiplicity $n_y$; the observed package carries
the same proposal correction as any other row. The proposal density is a
computational device, fitted out of fold so that a household's own outcome never
enters the proposal used to score it. For couples the proposal draws the joint
participation regime first and then the two spouse packages conditional on it.
Non-positive simulated consumption receives a one-euro floor inside this
likelihood only.

""" + reader_voice(OPTIMISER_PARAGRAPH) + r"""

Optimization uses five starts under two polishing contracts, ten terminal paths
in all. These diagnostics support a stable local solution found from the starts
tested; they are not a proof of global uniqueness.

""" + RESTRICTIONS_PARAGRAPH + r"""

The tax-benefit accounting identity linking original income, benefits, taxes
and social contributions to disposable income holds to machine precision at
both the person and the household-alternative level, before and after the
benefit take-up adjustment.

> **Two distinct leisure-scaling exercises.** **Analytical reparameterisation
> (zero re-estimation):** the exact $\lambda_\ell$ pullback was evaluated at 10,
> 20, 40, 43.0 and 45.623591 hours a week; choice probabilities were bitwise
> equivalent and the pre-refit objective deviation was exactly zero.
> **Independent re-estimation:** the four non-baseline $\lambda_\ell$ values were
> then independently re-estimated under the full multi-start protocol as a
> separate verification of the analytical image.

{{figure:ws4lambda}}

## Implementation record: observed labour-force status

""" + LES_BLOCK.replace("{{report-only}}", "").replace("{{/report-only}}", "").replace(
    "### Observed raw labour-force status\n", "") + r"""

## Implementation record: population-fit moments

""" + FIT_TABLES + r"""

""" + illustration.APPENDIX_BLOCK + r"""
"""

import v6_sections as v6  # noqa: E402

_historical = v10.PROVENANCE
# Two predecessor passages missed by the V10 sweep: an editorial heading that
# precedes its labelled quotation, and the V6 decomposition status sentence.
_historical = _replace_once(
    _historical,
    "**Numerically blocked opportunity-prospect metric.** " + v10.SUPERSEDED_NOTE,
    "**Opportunity-prospect metric: historical status.** " + v10.SUPERSEDED_NOTE
    + " (Historical heading: “Numerically blocked opportunity-prospect metric”.)",
)
_historical = v10._label_superseded(_historical, v6.MISSION_WORDING)
PROVENANCE = IMPLEMENTATION_RECORD + "\n\n" + _historical


SECTIONS = [
    {"key": "why", "title": "Why welfare inequality is not income inequality",
     "body": INTRO},
    {"key": "model",
     "title": "How the latent-jobs model separates preferences from opportunities",
     "body": LATENT_JOBS},
    {"key": "money", "title": "From choices to well-being: outcomes versus prospects",
     "body": WELFARE},
    {"key": "decomposition",
     "title": "From well-being to inequality: counterfactuals and the Shapley allocation",
     "body": DECOMPOSITION},
    {"key": "results", "title": "What the current results say", "body": RESULTS},
    {"key": "limits", "title": "What remains preliminary", "body": LIMITS},
    {"key": "provenance", "title": "Appendix. Technical record and provenance",
     "body": PROVENANCE, "appendix": True, "collapse": True, "paper": False},
]

QA = []
