"""Full-economics, reader-facing sections for the V9 research-story report.

V9 keeps the seven-part reading sequence and the single collapsed technical
appendix introduced in V8.  It restores the economic model, derivations and
identification discussion from the last full-content report, and adds the
certified ex-ante opportunity-prospect results as a distinct perspective.
"""
from __future__ import annotations

import re

import v5_sections as v5
import v8_sections as v8


TITLE = (
    "Unequal Job Opportunities and Well-Being Inequality: "
    "A Latent-Jobs Structural Decomposition"
)

ABSTRACT = r"""In a preliminary restricted structural decomposition of the
attained-bundle money metric, equalising systematic utility heterogeneity,
coarse geographic and temporal access, and systematic wage opportunities—while
holding household resources, needs and composition fixed—reduces the Gini by
{{n:d2_deltaI_pct_singles_eq|.1f}}–{{n:d2_deltaI_pct_couples_uneq|.1f}}%
relative to its baseline level across household types and reporting scales. In
the corresponding ex-ante perspective, the access and earning-opportunity
channels together account for {{n:wea_opportunity_min_pct|.1f}}–{{n:wea_opportunity_max_pct|.1f}}%
of baseline inequality, depending on household type and scale. The channel
ordering diverges: earning opportunities dominate under the attained-bundle
measure, whereas access is about three times earning opportunities for
single-adult households under the ex-ante measure. These figures do not
estimate the total share of well-being inequality caused by unequal job
opportunities."""

PRELIM_NOTE = (
    "Discussion draft. The attained-bundle decomposition remains preliminary "
    "and subject to ongoing numerical validation of the counterfactual "
    "integration. The separate ex-ante calculation has passed its numerical "
    "certification checks. Both are restricted structural accounting exercises, "
    "not causal decompositions, and neither welfare perspective is designated "
    "as primary."
)


def reader_voice(text: str) -> str:
    """Remove implementation vocabulary while leaving economics and maths intact."""
    replacements = (
        ("Mapping-F", "attained-bundle"),
        ("DECOMP-2", "preliminary structural decomposition"),
        ("POSFIT-v3b", "predictive-fit diagnostics"),
        ("POSFIT v3b", "predictive-fit diagnostics"),
        ("S11/S10", "preferred specification"),
        ("S11", "preferred specification"),
        ("S12", "large predictive integration sample"),
        ("criterion-A", "accepted estimation sample"),
        ("proposal panel", "numerical integration sample"),
        ("exact-H", "reference-integral"),
        ("H-F", "full-reference convention"),
        ("H-D", "positive-consumption reference sensitivity"),
        ("H-X", "restricted-household sensitivity"),
        ("NN pricing state", "non-employment price"),
        ("NN state", "non-employment price"),
        ("dwt-weighted", "household-weighted"),
        ("dwt", "household weights"),
        ("worktree", "working copy"),
        ("registry", "record"),
        ("adjudication", "assessment"),
        ("Gate 0", "initial check"),
        ("G1-G9", "the nine release checks"),
        ("MECHANICAL_STOCHASTIC_CONDITIONING",
         "the mechanical implication of conditioning under stochastic choice"),
    )
    for old, new in replacements:
        text = re.sub(
            r"(?<![A-Za-z0-9])" + re.escape(old) + r"(?![A-Za-z0-9])",
            lambda _: new,
            text,
            flags=re.I,
        )
    text = re.sub(r"(?<![A-Za-z0-9])anchor node(?![A-Za-z0-9])",
                  "included observed job", text, flags=re.I)
    text = re.sub(r"(?<![A-Za-z0-9])anchor(?![A-Za-z0-9])",
                  "included observed job", text, flags=re.I)
    text = re.sub(r"(?<![A-Za-z0-9])node-level(?![A-Za-z0-9])",
                  "job-specific", text, flags=re.I)
    text = re.sub(r"(?<![A-Za-z0-9])node(?![A-Za-z0-9])",
                  "integration point", text, flags=re.I)
    text = re.sub(r"(?<![A-Za-z0-9])gate(?![A-Za-z0-9])",
                  "standard", text, flags=re.I)
    text = re.sub(r"(?<![A-Za-z0-9])mission(?![A-Za-z0-9])",
                  "research task", text, flags=re.I)
    text = re.sub(r"(?<![A-Za-z0-9])ruling(?![A-Za-z0-9])",
                  "decision", text, flags=re.I)
    return text


_intro_open = v5.INTRO.split("**The normative reference.**", 1)[0]
_literature = v5.INTRO.split("**Relation to existing work.**", 1)[1].split(
    "**Roadmap.**", 1
)[0]
_literature = _literature.replace(
    "Their references fix a wage or an unearned-income intercept and maximize "
    "over a deterministic budget set. Ours fixes consumption across the "
    "alternatives of an estimated opportunity distribution and integrates. "
    "That is a different reference and, as Section 6 records, the ordering is "
    "sensitive to it.",
    "Their references fix a wage or an unearned-income intercept and maximize "
    "over a deterministic budget set. Here the attained-bundle perspective "
    "uses the universally available non-employment state, while the ex-ante "
    "perspective fixes consumption across the alternatives of an estimated job "
    "prospect and integrates. The two references answer different questions, "
    "which is why both are reported without designating either as primary.",
)
_literature = _literature.replace(
    "an opportunity-sensitive money-metric welfare level built on the own-set "
    "equal-consumption principle",
    "two money-metric perspectives built on explicit indifference conditions",
)
_literature = re.sub(
    r" Within this bounded decomposition exercise, earning-opportunity "
    r"heterogeneity has a larger Shapley contribution than the model's coarse "
    r"geographic/temporal access channel\.",
    "",
    _literature,
)

WHY_INCOME_MIXES = reader_voice(_intro_open) + r"""
The paper therefore keeps two welfare questions separate. The attained-bundle
perspective asks what the job a household actually obtained is worth. The
ex-ante perspective asks what the household's entire job prospect is worth
before a particular job is realised. Both are money metrics derived from an
indifference condition, but they need not rank channels in the same way. That
difference is economically useful: one perspective describes the value of the
realised outcome, while the other makes reachability part of welfare directly.

The empirical strategy joins a random-utility model to a random-opportunity
model. Jobs are packages of employment, occupation, weekly hours and hourly
wages; couples choose two packages under a shared household budget. Every
package is priced through the French tax-benefit system. The model then
separates systematic variation in the value of consumption and leisure from
systematic variation in employment access, hours, occupations and wage offers,
subject to explicit maintained assumptions.

The main accounting exercise equalises three pathways: systematic utility
heterogeneity, coarse geographic and temporal access, and systematic wage
opportunities. Household resources, needs and composition remain fixed, so the
exercise is deliberately restricted. Interactions are assigned with an exact
Shapley allocation, separately for each welfare perspective and separately for
single-adult and couple households.

The headline result is not a single percentage. The two measures disagree
about which opportunity channel dominates. Earning opportunities dominate when
welfare values the realised job. When welfare values the whole prospect,
access is about three times earning opportunities for single-adult households.
The reason is structural: reachability enters the ex-ante prospect directly,
whereas the attained-bundle measure sees only the realised job, for which wages
drive consumption.

## Relation to existing work

""" + reader_voice(_literature) + r"""
The contribution is therefore the conjunction of four elements: household-
specific latent job opportunities, a tax-benefit-consistent budget for every
work arrangement, explicit money-metric comparisons, and a complete
interaction-aware accounting across the declared pathways. The divergence
between the two welfare perspectives is a result of that conjunction, not a
choice of a preferred metric.
"""


LATENT_JOBS = reader_voice(v5.DATA + "\n\n" + v5.MODEL).replace(
    "Section 4", "Section 3"
).replace(
    r"where $\mathcal B(z;\theta)=(z^{\theta}-1)/\theta$ with "
    r"$\mathcal B(z;0)=\log z$",
    r"where $\mathcal B(z;\theta)=(z^{\theta}-1)/\theta$ with "
    r"$\mathcal B(z;0)=\log z$ is the Box-Cox leisure transform. "
    r"The coefficient $\beta_{\ell}^{g}(\mathbf x_i)$ is the household-specific "
    r"weight on leisure, $\theta_{\ell}^{g}$ governs its curvature, and "
    r"$\beta_c$ is the weight on log consumption",
)


MONEY_METRIC = r"""
The attained-bundle money metric asks what the household's realised job is
worth. Let $j_i^{\mathrm{obs}}$ denote the observed job package and let $o$
denote the universally available non-employment state. The deterministic
utility index from Section 2 can be written

$$
u_i(C,j)=L_i(j)+\beta_c\log(C/\lambda_c),
$$

where $L_i(j)$ is the complete non-consumption part of utility. For a couple it
contains both spouses' leisure terms. The equivalent consumption
$M_i^{\mathrm{att}}$ is defined by the indifference condition

$$
u_i\!\left(M_i^{\mathrm{att}},o\right)
=u_i\!\left(C_i^{\mathrm{obs}},j_i^{\mathrm{obs}}\right).
$$

Substituting the utility index makes the derivation visible:

$$
L_i(o)+\beta_c\log\!\left(\frac{M_i^{\mathrm{att}}}{\lambda_c}\right)
=L_i(j_i^{\mathrm{obs}})+\beta_c\log\!\left(\frac{C_i^{\mathrm{obs}}}{\lambda_c}\right),
$$

$$
\log M_i^{\mathrm{att}}
=\log C_i^{\mathrm{obs}}
+\frac{L_i(j_i^{\mathrm{obs}})-L_i(o)}{\beta_c},
$$

and hence

$$
\boxed{
M_i^{\mathrm{att}}
=C_i^{\mathrm{obs}}
\exp\!\left\{
\frac{L_i(j_i^{\mathrm{obs}})-L_i(o)}{\beta_c}
\right\}.}
$$

The argument solved for is consumption, so the measure is already in euros;
there is no separate conversion of a utility index into money. The normaliser
$\lambda_c$ disappears from the closed form. The estimated consumption weight
$\beta_c$ controls how a non-consumption advantage or disadvantage translates
into a proportional consumption adjustment. A larger $\beta_c$ makes the same
leisure difference a smaller proportional adjustment.

In the estimated domain, the non-employment state maximises the non-consumption
index for every household. This is an empirical property of the specification,
verified for both samples, not a general theorem. Non-workers therefore have
$M_i^{\mathrm{att}}=C_i^{\mathrm{obs}}$. Workers trade consumption against less
leisure, so their attained-bundle value reflects both what the job pays after
taxes and transfers and the leisure it costs.

The distinction between direct and indirect opportunity effects matters.
Unrealised jobs do not enter this formula. Opportunities matter because they
shape which job becomes $j_i^{\mathrm{obs}}$; once that job is fixed, its wage
affects priced consumption directly. This is why earning opportunities can
dominate the attained-bundle decomposition even when access is important in
the choice model.

For household-size comparisons, the paper also reports
$M_i^{\mathrm{att}}/m_i$, where $m_i$ is the modified-OECD equivalence scale.
Equivalisation is a normative reporting convention, not an estimated
parameter. Single-adult and couple distributions remain separate throughout;
their welfare levels are never pooled or compared with one another.
"""


DECOMPOSITION_ECONOMICS = r"""
The decomposition asks how inequality changes when selected systematic
differences are replaced by common reference profiles. Write the household's
structural inputs as

$$
x_i=(x_i^P,x_i^A,x_i^B,d_i),
$$

where $x_i^P$ carries the observed characteristics that shift systematic
utility, $x_i^A$ carries coarse geographic and temporal access shifters,
$x_i^B$ carries the observed characteristics that shift the wage-offer
location, and $d_i$ contains household resources, needs and composition.
The three equalisation operators are

$$
\begin{aligned}
T_Px_i&=(\bar x^P,x_i^A,x_i^B,d_i),\\
T_Ax_i&=(x_i^P,\bar x^A,x_i^B,d_i),\\
T_Bx_i&=(x_i^P,x_i^A,\bar x^B,d_i).
\end{aligned}
$$

$T_P$ equalises age profiles and the child-related utility shifter while
retaining the sex- and household-type-specific coefficient blocks. The child
term is a reduced-form behavioural and time-constraint shifter, so calling this
pathway "preferences" is shorthand rather than a claim that it contains pure
taste alone. $T_A$ equalises region, urban or rural location, and survey year
where they enter employment access. It does not equalise personal occupation
access, the hours density or every job attribute. $T_B$ equalises the education-
and experience-related arguments of the wage-offer location. It does not remove
the common wage dispersion, realised wage luck or selection. Every operator
changes a pathway and leaves estimated coefficients fixed; it does not replace
every occurrence of the corresponding raw characteristic.

For a coalition $S\subseteq\{P,A,B\}$, $T_S$ applies exactly the substitutions
named by $S$ simultaneously. Let $p\in\{\mathrm{att},\mathrm{EA}\}$ index the
attained-bundle and ex-ante welfare perspectives. With $\mathcal G$ denoting
the household-weighted Gini,

$$
I_S^p=\mathcal G\!\left(\left\{M_i^p(T_Sx_i)\right\}_{i=1}^N\right),
\qquad
v^p(S)=I_\varnothing^p-I_S^p.
$$

Thus, $v^p(S)$ is the inequality removed by equalising the pathways in $S$
under perspective $p$. Household resources, needs and composition remain
$d_i$ in every coalition, so $I_{\{P,A,B\}}^p$ generally remains positive. The
exercise does not label that residual as preferences or opportunities.

One-at-a-time comparisons are insufficient because the pathways interact.
For each $k\in\{P,A,B\}$, the exact Shapley contribution is

$$
\phi_k^p
=\sum_{S\subseteq\{P,A,B\}\setminus\{k\}}
\frac{|S|!\,(3-|S|-1)!}{3!}
\left[v^p(S\cup\{k\})-v^p(S)\right].
$$

Equivalently, it is the average marginal contribution of pathway $k$ over all
$3!=6$ orders in which the three equalisation steps can be introduced. The
allocation closes by construction and is checked numerically:

$$
\phi_P^p+\phi_A^p+\phi_B^p
=I_\varnothing^p-I_{\{P,A,B\}}^p
\equiv\Delta I^p.
$$

Contributions are signed and are not rescaled to sum to one hundred. A share
of $\Delta I^p$ describes the allocation of the movable component; a share of
$I_\varnothing^p$ describes its size relative to baseline inequality. Those
denominators answer different questions and are kept separate.

Exactly the same operators and allocation rule are applied to both welfare
perspectives. This common accounting structure makes the channel-ordering
comparison meaningful while preserving the distinction between what the two
welfare objects value. Neither perspective is declared primary; choosing
between them is a separate substantive decision.
"""


_behaviour = v5.RESULTS.split("## Fit", 1)[0]
_behaviour = _behaviour.replace("Section 4", "Section 3")

CURRENT_RESULTS = reader_voice(_behaviour) + r"""
## Predictive fit

The fit evidence is a population prediction, obtained by integrating the
estimated choice model over the opportunity distribution and the taste shocks.
It is not the probability of choosing from the finite set used in estimation
and it is not an in-sample fitted choice. The comparison therefore tests the
model away from the realised choices used to estimate it.

{{figure:fitband}}

The preferred specification reproduces participation and occupation margins
closely in aggregate, while its hours fit is uneven. Across all reported
population moments, the corrected mean absolute deviation is
{{n:mae_singles|.4f}} for single adults and {{n:mae_couples|.4f}} for couples.
The correction is not an across-the-board improvement: the single-adult value
rises slightly while the couple value falls.

For the extensive margin, numerical precision is sufficient to report an
accuracy of {{n:single_women_accuracy_pct|.1f}}% for single women, against a
model-simulated range of {{n:single_women_band_lo_pct|.1f}}%–{{n:single_women_band_hi_pct|.1f}}%,
and {{n:coupled_women_accuracy_pct|.1f}}% for coupled women, against
{{n:coupled_women_band_lo_pct|.1f}}%–{{n:coupled_women_band_hi_pct|.1f}}%.
The corresponding statistics for single men and coupled men are WITHHELD
because numerical integration error remains too large relative to sampling
variation.

The common hours mismatch is underprediction of the observed 37-hour mass
point. The observed-minus-predicted gaps are
{{n:gap37_single_women|.1f}} percentage points for single women,
{{n:gap37_coupled_men|.1f}} for coupled men,
{{n:gap37_single_men|.1f}} for single men and
{{n:gap37_coupled_women|.1f}} for coupled women. This is a finding about the
observed concentration at exactly 37 hours, not the model's neighbouring
full-time range.

{{figure:fit}}

{{table:fitsingles}}

{{table:fitcouples}}

The richer common-opportunity benchmarks fit less well on the same households
and the same sampled alternatives. The deterioration is concentrated in the
margins governed by the opportunity distribution, especially occupations.
That comparison supports the empirical relevance of opportunity heterogeneity,
but a better maximised criterion does not by itself prove that the mechanism is
identified.

## Attained-bundle well-being

{{table:welfare_reader}}

On the equivalised basis, the Gini of the attained-bundle money metric is
{{n:w1f_eq_gini_singles|.4f}} for single-adult households and
{{n:w1f_eq_gini_couples|.4f}} for couples, compared with
{{n:ceq_gini_singles|.4f}} and {{n:ceq_gini_couples|.4f}} for disposable
consumption in the same samples. These are within-sample dispersion
comparisons, not welfare-loss estimates.

## Attained-bundle decomposition

Equalising systematic utility heterogeneity, coarse geographic and temporal
access, and systematic wage opportunities—while holding household resources,
needs and composition fixed—reduces the Gini by
{{n:d2_deltaI_pct_singles_eq|.1f}}–{{n:d2_deltaI_pct_couples_uneq|.1f}}%
relative to its baseline level across household types and reporting scales.
Within this restricted exercise, the earning-opportunity channel is larger
than the coarse access channel throughout. The preference contribution changes
sign with equivalisation, so no directional claim is made about it.

{{table:decomposition_reader}}

An allocated contribution averages a pathway's marginal effect over all
coalition orders; it is not the one-factor reduction. The full allocation is
shown because interactions matter. Every coalition Gini and contribution is
closely reproduced by an independent simulation. The allocation closes to
numerical precision. These checks validate the calculation for the stated game;
they do not validate its maintained behavioural assumptions or turn it into a
causal decomposition.

## Ex-ante well-being and decomposition

The ex-ante perspective values the household's whole job prospect. Its
certified distribution and Shapley accounting are:

{{table:wea_results}}

The access and earning-opportunity contributions together account for
{{n:wea_opportunity_min_pct|.1f}}–{{n:wea_opportunity_max_pct|.1f}}% of
baseline ex-ante inequality, depending on household type and scale. For
single-adult households, access is {{n:wea_singles_access_earn_ratio_uneq|.1f}}
times the earning-opportunity contribution before equivalisation and
{{n:wea_singles_access_earn_ratio_eq|.1f}} times after it—about three times on
either basis. For couples, earning opportunities remain larger than access.

Equivalisation is materially consequential for couples. It moves the ex-ante
access-plus-earnings share from {{n:wea_couples_opportunity_uneq_pct|.1f}}% to
{{n:wea_couples_opportunity_eq_pct|.1f}}% of baseline inequality and turns the
preference contribution negative. The scale convention therefore changes the
substantive attribution, and no directional claim about preferences is made.

## The two welfare perspectives side by side

{{table:perspective_comparison}}

The measures disagree about which channel dominates. Under the attained-bundle
measure, earning opportunities dominate for both household types at both
scales. Under the ex-ante measure, access dominates earning opportunities by
about three to one for single-adult households; earnings still dominate for
couples. The economic reason is direct. The ex-ante measure values the whole
prospect, so reachability enters welfare directly. The attained-bundle measure
sees only the realised job, where wages drive disposable consumption. Neither
measure is designated primary here.

Earlier circulated figures near 90% described all non-preference
circumstances, including household resources and composition, rather than job
opportunities alone. They are not comparable with the restricted
access-and-earnings figures reported here and are not current results.

All percentages in this section belong to restricted three-pathway accounting
exercises. They do not estimate the total share of well-being inequality caused
by unequal job opportunities. The attained-bundle counterfactual remains
preliminary; the ex-ante computation has passed the separate numerical checks
reported in the appendix, but it remains conditional on the same structural
model and equalisation conventions.
"""


PRELIMINARY_LIMITS = r"""
These decomposition estimates are preliminary and subject to ongoing numerical
validation of the counterfactual integration. That caveat applies especially
to the attained-bundle counterfactual, which carries realised alternatives
through a finite integration sample. The ex-ante numerical calculation has
passed its declared checks, including an independent implementation, but
certification of a calculation is not certification of the model's maintained
economic assumptions.

## Scale and household comparison

Equivalisation is a normative convention and is materially consequential here.
For couples, dividing by the modified-OECD scale moves the ex-ante access-plus-
earnings share from {{n:wea_couples_opportunity_uneq_pct|.1f}}% to
{{n:wea_couples_opportunity_eq_pct|.1f}}% of baseline inequality and changes
the preference contribution from {{n:wea_couples_pref_uneq|.5f}} Gini points to
{{n:wea_couples_pref_eq|.5f}}. The latter is negative. A negative Shapley term
means that, averaged over coalition orders, equalising that pathway raises
rather than lowers inequality. It does not establish that preference
heterogeneity is equalising in a causal or welfare-theoretic sense. Because the
sign and magnitude depend on scale, no directional claim about preferences is
made.

The two household types are separate estimated populations. Their means,
medians and Ginis describe within-population distributions; welfare levels are
not compared across single-adult and couple households. Reporting both raw and
equivalised results exposes the role of the scale convention instead of hiding
it behind one preferred presentation.

## Scope of the equalisation exercise

The access pathway is coarse. It contains region, urban or rural location and
survey year where those variables enter employment access. It does not contain
personal occupation access, the concentration of offers at particular hours,
or every feature of a feasible job. The earning-opportunity pathway equalises
systematic wage-offer locations, not the common dispersion of wages, realised
wage luck or selection. Household resources, needs and composition are fixed
throughout and receive no allocated share. The resulting percentages therefore
are neither a complete decomposition of well-being inequality nor estimates of
the causal effect of geography, education or occupation.

The Shapley allocation is exact for the declared three-pathway game. Exact
closure shows that interactions have been allocated consistently; it says
nothing about whether the pathways are normatively exhaustive. Likewise, the
independent numerical reproduction rules out many implementation mistakes but
does not remove parameter uncertainty. The reported repeat-run comparisons are
simulation checks, not confidence intervals. Estimation uncertainty has not
been propagated through either decomposition.

## Numerical and predictive boundaries

The attained-bundle exercise uses an integration sample that represents the
lower part of the modelled hours range sparsely, while a separate assessment
finds substantial model-implied mass there. Its direct effect on the
attained-bundle attribution has not been fully quantified. Coverage below ten
hours therefore remains an explicit limitation of that exercise.

The predictive evidence has a separate boundary. Women's extensive-accuracy
statistics are reportable, but the corresponding statistic for each group of
men is withheld because numerical integration error is too large relative to
sampling variation. The underprediction at exactly 37 hours is retained as its
own finding rather than absorbed into a wider full-time interval. Aggregate fit
does not eliminate these group- and margin-specific discrepancies.

## Maintained econometric assumptions

The separation of preferences from opportunities relies on the functional
form and exclusion restrictions in Section 2. Smooth leisure preferences,
piecewise hours opportunities, excluded local-labour-market shifters and
conditional independence of wages and hours are maintained assumptions. The
regional variation does not create causal identification, and the model does
not establish that omitted personal access dimensions are orthogonal to the
included ones.

Two observation-rule questions also remain open. The estimation sample screens
on observed hours and wages for workers, so it is selected on outcomes of the
process being modelled. In addition, the sampled-choice probability conditions
on a labelled collection of alternatives. Existing diagnostics are consistent
with the assumed sampling law but do not prove it. Finally, the weekly time
endowment is maintained rather than estimated, and the model is not invariant
to changing it. These issues qualify structural interpretation without
altering the arithmetic of the reported calculations.
"""


EX_ANTE = r"""
The ex-ante money metric asks what a household's whole job prospect is worth,
before one job is realised. Let $\Omega_i$ be the household's job domain,
$g_i(j)$ its structural opportunity density with respect to base measure
$\nu$, $L_i(j)$ the non-consumption utility index and $C_i(j)$ priced
consumption. Under the type-I extreme-value normalisation, the actual prospect
is represented by

$$
J_i
=\int_{\Omega_i}
\exp\{L_i(j)\}
\left(\frac{C_i(j)}{\lambda_c}\right)^{\beta_c}
g_i(j)\,d\nu(j).
$$

Now keep the same opportunity prospect and preferences, but give every job the
same consumption $m$. The non-consumption and opportunity part of that
reference is

$$
H_i
=\int_{\Omega_i}\exp\{L_i(j)\}g_i(j)\,d\nu(j),
$$

so the reference prospect has value

$$
J_i^{\mathrm{ref}}(m)
=\left(\frac{m}{\lambda_c}\right)^{\beta_c}H_i.
$$

The ex-ante money metric $M_i^{\mathrm{EA}}$ solves the indifference condition

$$
J_i^{\mathrm{ref}}\!\left(M_i^{\mathrm{EA}}\right)=J_i.
$$

Taking logs and inverting gives

$$
\log H_i+\beta_c\log\!\left(\frac{M_i^{\mathrm{EA}}}{\lambda_c}\right)
=\log J_i,
$$

$$
\boxed{
M_i^{\mathrm{EA}}
=\lambda_c\exp\!\left\{
\frac{\log J_i-\log H_i}{\beta_c}
\right\}.}
$$

This ratio is invariant to a common rescaling of the opportunity intensity:
the same scale multiplies $J_i$ and $H_i$ and cancels. What does not cancel is
the composition of the prospect across jobs with different consumption and
non-consumption values. Access therefore matters directly by changing which
jobs receive weight in the prospect. Earning opportunities matter through the
consumption generated by the wage distribution. The appendix records the
integration design, tax-benefit pricing volume, reference-domain convention,
numerical checks and sensitivity calculations; those are implementation facts,
whereas the definition and inversion above are the economic object.

The attained-bundle and ex-ante measures answer different questions. The first
values the realised job against non-employment and contains no average over
jobs not taken. The second values the entire stochastic prospect and therefore
depends directly on reachability. This difference explains the empirical
channel reversal for single-adult households: access is about three times
earning opportunities ex ante, while earning opportunities dominate in the
attained-bundle accounting. It is not a contradiction and it is not resolved
by calling one measure primary. The choice between perspectives belongs to the
paper's substantive welfare argument and remains for the principal investigator.
"""


WEA_TECHNICAL_RECORD = r"""
## Certified ex-ante calculation

This record contains implementation and verification material that is excluded
from the reader-facing audit. The numerical authority is
`MNL_wea/docs/wea_sprint_1/stage4/stage4_certification_and_results_v1.json`,
with the economist-facing summary in
`MNL_wea/docs/wea_sprint_1/WEA_SPRINT_1_result_memo_v1.md`. The welfare branch
commit is `ff7c2d51`.

### Integration design

The design was chosen before inspecting any consumption integral, welfare
level, Gini or Shapley value. Two fixed independent seed streams were used.
The smallest defensive design passing the pre-specified H-accuracy rules in
all eight coalitions was 6,400 draws for singles and 76,800 for couples.
Occupation was marginalised in the target and proposal because priced
consumption depends on employment, hours and wages rather than the occupation
label itself. The final household samples contain 1,540 singles and 2,223
couples.

### Pricing volume

The calculation priced 351,024,407 new EUROMOD states: 8,573,928 and 8,574,032
for the two singles streams, and 166,937,889 and 166,938,558 for the two couples
streams. Price-replication controls had a maximum discrepancy of EUR 0.00.
Every generated market row joined exactly one priced value; there were no
missing, extra or duplicate joins and no failed or retried production tasks.

### Reference-domain convention

The reported reference is H-F. States with non-positive consumption contribute
zero to J through the $C\to0^+$ limit but remain in H and receive the common
reference consumption. There is no one-euro floor, observed-consumption
substitution or silent household deletion. H-D drops non-positive-consumption
states from both integrals. H-X excludes households whose non-employment
consumption is non-positive. The latter excludes 73 singles and 60 couples and
is disclosed only as a sensitivity.

### Certification gates

|Gate|Check|Singles|Couples|
|---|---|---:|---:|
|C1|Exact H on the priced set|PASS|PASS|
|C2|Effective sample size for J and H|PASS|PASS|
|C3|Largest sampled market-node share|PASS|PASS|
|C4|Wage-tail bound and high-earnings diagnostic|PASS|PASS|
|C5|Two-seed household, Gini and Shapley stability|PASS|PASS|
|C6|Constant-consumption identity|PASS|PASS|
|C7|One-state identity|PASS|PASS|
|C8|Common intensity-rescaling invariance|PASS|PASS|
|C9|Flat-reference inversion|PASS|PASS|
|C10|Finite positive welfare for every released household|PASS|PASS|
|C11|Exact Shapley adding-up|PASS|PASS|
|C12|Independent reimplementation|PASS|PASS|

C3 was amended before any population calculation to exclude the exactly
integrated non-employment atom from a diagnostic intended to detect sampled-
market weight concentration. The originally registered atom-inclusive
statistic is retained in the source record. The first large pricing launch
exhausted memory and was discarded; no partial output from it enters the
results.

### Sensitivities

Under stream B, the access-plus-earnings shares of baseline ex-ante inequality
are 14.8%, 20.3%, 21.2% and 7.8% for singles raw, singles equivalised, couples
raw and couples equivalised. Under H-D they are 15.3%, 20.6%, 21.3% and 8.0%.
Under H-X they are 15.5%, 21.3%, 22.6% and 8.5%. Access remains larger than
earnings for singles and earnings remains larger than access for couples in
every sensitivity.
"""


_v8_provenance = next(
    section["body"] for section in v8.SECTIONS if section["key"] == "provenance"
)
PROVENANCE = _v8_provenance + "\n\n" + WEA_TECHNICAL_RECORD


SECTIONS = [
    {"key": "why",
     "title": "Why income inequality mixes preferences and opportunities",
     "body": WHY_INCOME_MIXES},
    {"key": "model",
     "title": "How the latent-jobs model separates preferences from opportunities",
     "body": LATENT_JOBS},
    {"key": "money",
     "title": "How attained bundles become money-metric well-being",
     "body": MONEY_METRIC},
    {"key": "decomposition",
     "title": "How the preliminary counterfactual decomposition works",
     "body": DECOMPOSITION_ECONOMICS},
    {"key": "results", "title": "What the current results say",
     "body": CURRENT_RESULTS},
    {"key": "limits", "title": "What remains preliminary",
     "body": PRELIMINARY_LIMITS},
    {"key": "exante",
     "title": "How the ex-ante perspective values the whole job prospect",
     "body": EX_ANTE},
    {"key": "provenance", "title": "Appendix. Technical record and provenance",
     "body": PROVENANCE, "appendix": True, "collapse": True, "paper": False},
]


QA = []
