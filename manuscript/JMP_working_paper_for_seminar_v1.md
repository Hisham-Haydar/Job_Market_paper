# Unequal Job Opportunities and the Measurement of Welfare Inequality

### Evidence from a random-utility, random-opportunity model of French single-adult households

**Seminar working paper, version 1.** France 2016 (EU-SILC / SRCV, priced through EUROMOD).

---

## Drafting note

*This note is the only place in the paper where a status tag appears. It is to be
stripped at final. Everything not listed here is on the record of an accepted run
or a ratified ruling.*

*File of record: `JMP/manuscript/JMP_working_paper_for_seminar_v1.md`. That is
the name the R-233 sprint direction gives the seminar drafting target in its
§14, "Paper writing in parallel"; the draft was renamed on to it at the R-245
close-out. There is no other working-paper file and no earlier name is still in
use anywhere.*

This is a **seminar working paper**, not a submission and not a final-publication
claim. It is written to be argued with. Three things follow.

**First, what is provisional.** Every welfare and decomposition magnitude in §7,
§8 and Appendix D carries the label
`FINAL_SINGLES_PROVISIONAL_PENDING_ECONOMICS_REVIEW` (singles) or
`FINAL_COUPLES_PROVISIONAL_PENDING_ECONOMICS_REVIEW` (couples). They are computed,
internally verified, gate-passed and reproducible; they are *provisional pending
one bounded economics review*, which is the review this seminar is part of. The
specific items that review is asked to look at are:

| item | where | what the review is asked |
|---|---|---|
| the equivalence scale as an endowments-and-needs object | §3.5, §7.4 | is the *economics* of a coalition-moving scale right, or is the residual a genuine needs term? |
| the reference-preference range (branch A) | §7.5 | is reporting a range, never an average, the right discipline? |
| the couples male-leisure sensitivity | §8.4 | is a sensitivity-bounded companion the right presentation? |
| the pooled non-exhaustiveness | §8.5 | is a type-specific reference the right object, given that it breaks pooling? |
| couples worse off than singles at every quantile on the modified-OECD scale | §8.5 | an implication of the ratified scale, not a finding this lane can adjudicate |
| the $W^{1}_{\text{ref}}$ ordering flip | Appendix D | a fact about the measure, not about the world — but it should be seen |

**Second, what is a placeholder.** Two lanes were commissioned to close gaps in
this draft. Both have now returned; one is complete, and one is complete except
for a source that does not exist in the accessible data. What came back is in the
text; what did not is marked `[PLACEHOLDER]`, with nothing written in its place.

- **The age-bound diagnostic. Returned complete**, and reported in §5.5. Its
  verdict is to retain the model of record, on a close margin: the widened box is
  clean, but the bound value lies inside both released coefficients' intervals, so
  the bound was binding on a curvature the data do not identify. Its one
  substantive finding is folded into §5.5 and echoed in §7.5 and §8.4.
- **External validation. Returned**, and reported in §9. The 35-hour concentration
  result is complete: the model's hours-opportunity structure is visible in a
  source it never saw. The underemployment axis is **now also complete** — the
  national coding of the labour-force wish-to-work-more variable was resolved
  against the EU-LFS codebook (version of 8 July 2021, $1 =$ No, $2 =$ Yes) at the
  integration pass, and §9.3 reports it as external evidence on hours constraints.
  **Not available at all:** any matched employer–employee source that would
  validate the wage-offer block independently, for which no file exists in the
  accessible restricted-data folder. §9.1 reports the within-sample wage fit and
  fixes the framing that comparison will be read under; it is the paper's one
  remaining placeholder.

**Third, two authorizations are not on disk.** The consolidated Goal-1 rulings
register ends at R-233. The freeze direction this draft is written under
(deputy s12 plus addendum s1, Goal-1 R-244.3) and the interpretation discipline
it quotes in §7.3 are taken from the sprint decision log, which is the surface
of record for the sprint, rather than from the rulings document. Where §7.3
quotes the interpretation discipline it quotes the sprint record's own wording.
This is disclosed rather than smoothed over, on the same convention §3, §4 and
§10 already use for authorizations that post-date the register.

**Fourth, how the paper names things.** The main text, every figure and every
table use economic language only: *final singles model* (or *preferred RURO
model*), *the occupation-conditioned wage specification benchmark*, *observed
sample*, *model-implied*, *job access*, *earning opportunities*, *household
endowments and needs*, *preferences*. Internal specification and run labels appear
nowhere in §1–§11 or on any figure; they are retained in the technical appendices,
where reproducibility needs them, behind the legend at the head of Appendix A.
This note is the one exception, because its subject is the status of the draft
itself, and it is to be stripped at final.

**Standing conventions carried throughout.** Terminology follows the ratified
rule: *job access / feasibility*, *earning capacity / wage-offer technology*,
*preferences*, *endowments / needs*. The term **ability set $A_i$** is reserved
and denotes only the set of jobs a person is capable or eligible to perform.
Monte-Carlo bands are **numerical-integration precision and never sampling
confidence intervals**. No cell of the decomposition is a compensating variation.
The 35-hour coefficient is an *institutionally motivated opportunity peak in the
estimated offer density*, never an estimate of a statutory effect. The order
between the job-access and earning-opportunity channels remains unresolved under
the final model, so no ordering between them is claimed in either direction.

---

## Abstract

Labour-supply models that put every household on a common budget set must book
whatever is left over as taste. This paper separates the two. It estimates a
random-utility, random-opportunity (RURO) model of job choice on 1,555 French
single-adult households from the 2016 EU-SILC, in which a job is a package of
weekly hours, an hourly wage and an occupation, every package is priced through
the EUROMOD tax–benefit system, and a household-specific *opportunity density*
over packages is estimated jointly with Box–Cox preferences in one likelihood.
The preferred specification carries **41 estimated structural parameters**, of
which four factors describe availability — job access, hours, occupation, and an
occupation-conditional log-normal wage-offer technology — and the rest describe
tastes. Welfare is money-metric: each household's equivalent income at a common
reference pay, which compensates for pay and holds the household responsible for
its own opportunity set. The inequality of that measure is then decomposed, by an
Owen value over a coalition structure that puts preferences against the complete
environment, into preferences and a complete environment split into job access,
earning opportunities, and endowments and needs. Two methodological ingredients make the
decomposition exhaustive rather than approximately so: a **coalition-consistent
inversion**, in which the money-metric yardstick moves with the coalition, and a
**coalition-consistent equivalization**, in which the equivalence scale moves
with the channel that equalises household composition. With both in place the
fully common state is numerically zero and the four channels are exhaustive by
measurement rather than by assumption.

The headline result is stated with its guards.

> **Within the currently modelled non-preference environment, budget-side
> endowments and needs are the largest nested contribution under both positive
> models and both reference-preference conventions.** On the final singles
> model with the female reference, equalising the whole non-preference environment
> removes 93.7 per cent of baseline money-metric inequality (±0.6) and equalising
> preferences a further 6.3 per cent (±0.6); inside the environment, endowments
> and needs carry 58.2 per cent (±1.5), earning opportunities 20.6 (±1.6) and job
> access 14.9 (±1.1), so that job access and earning opportunities together — the
> two channels that are about the market rather than the budget — carry 35.5 per
> cent (±0.9). Across all eight rows of the table the environment share runs 89.0
> to 96.7 per cent, the preference share 3.3 to 11.0 per cent with a constant
> sign, the endowments-and-needs share 53.2 to 68.9 per cent, and the nested
> order is endowments and needs above earning opportunities above job access in
> every one.

Four qualifiers travel with that sentence and are not optional: it is structural
and model-conditional; it is not causal; it is provisional pending the bounded
economics review; and it is **not** a statement that job opportunities are
unimportant. A parallel module on 2,275 opposite-sex couples reproduces the same
nested order and the same environment dominance, but its preference contribution
is materially sensitive to the male leisure block, so singles remain the
quantitative headline and couples are reported as a sensitivity-bounded
companion.

**Keywords:** labour supply, job opportunities, random opportunity sets,
equivalent income, welfare inequality, Owen value, EUROMOD.

---

## 1. Introduction

### 1.1 Why preferences and opportunities must be separated

Two single adults hold the same job — the same occupation, the same weekly hours,
the same wage. One of them turned down better offers; the other took the only one
there was. A model that gives them a common budget set and a free choice of hours
cannot tell them apart, and it will book the entire difference between them as a
difference in taste for leisure. That is not a small technical concession. It is
the whole normative question. If the difference is taste, most welfare criteria
say the two are equally well off and neither has a claim on the other. If the
difference is opportunity, they are not equally well off and one of them does.

The problem is sharper than "some people are constrained". Constraints do not
enter labour supply as a single scalar. They enter as at least three distinct
objects, and the three are not substitutes:

- **job access / feasibility** — whether working packages are available at all,
  and at what hours;
- **earning opportunities** — what a package pays, conditional on being reachable;
- **endowments and needs** — non-labour income, household composition, and every
  other household-specific input to the tax–benefit budget.

The first two are about the market. The third is about the budget. They are
routinely bundled, and once bundled the resulting object cannot answer the
question anyone actually asks, which is *which* of them a policy would have to
move.

**Figure T1** makes the identification problem concrete before any estimate is
introduced. Its two panels show, for two households each, five objects: the
indifference map over consumption and leisure; the density of feasible packages
over hours; the occupation-conditional wage-offer densities; the chosen job; and
the attained money-metric welfare level. In panel (A) the two households have the
*same* preferences and different opportunity environments; in panel (B) the
*same* opportunity environment and different preferences. In both panels the
households end up at different observed jobs. Reading the observed job alone will
not tell you which panel you are in. Only a model that carries both objects
explicitly, and separates them in one likelihood, can.

> **Figure T1. Why the observed job does not identify the explanation.**
> Two panels, each showing five objects for two households: preferences, as
> indifference curves in consumption–leisure space; job access, as the density of
> feasible packages over weekly hours, with the statutory week marked; earning
> opportunities, as occupation-conditional wage-offer densities; the chosen job, as
> a marked point; and attained welfare, as the money-metric level $W^1$ — the flat
> consumption that, offered at every job in the household's own set, leaves it
> exactly as well off as it is, drawn as a horizontal line the household's own
> indifference curve through its chosen job reaches at its largest feasible
> leisure. In **(A)** the two households share one indifference map (drawn faintly
> in grey behind them) and face different opportunity environments; in **(B)** they
> face the same environment — the access densities and the wage-offer sets coincide
> — and have different preferences. In both panels they end at different observed
> jobs and different welfare levels. The figure is a **schematic**: it is drawn
> from stylised parameters chosen for legibility, no axis carries a numeral, and
> nothing in it is an estimate. Source: `SPRINT/runs/figT1/make_figT1_v1.py`.

### 1.2 Why RURO rather than a common-choice-set RUM

The natural instinct is to enrich a discrete-choice labour-supply model: add
hours dummies, add fixed costs of work, add part-time penalties. That helps the
fit, and it does not solve the problem, because those terms sit in the *utility*
index. A part-time dummy in $u$ says people dislike part-time work; a part-time
term in the offer density says part-time jobs are scarce. Both produce the same
observed hours distribution, and a specification that only has the first will
attribute scarcity to distaste by construction.

**That claim is checked rather than asserted, and the check qualifies it in a way
worth stating here.** §6.7 fits the common-choice-set benchmark this argument
names, on the same data and the same priced packages. The misattribution to tastes
is real and large **on the behavioural side**: the benchmark recovers the hours
constants in its utility index at essentially the availability values, to a mean
absolute difference of 0.037, and it reverses the sign of the male-minus-female
leisure gap, from $+0.428$ to $-1.991$. But on the **money-metric decomposition**
it does not turn opportunity into taste: the preference share is 6.4 per cent
under the benchmark against 6.3 under the preferred model. What the omission does
there is understate measured inequality — by 24.2 per cent on the raw basis — and
relabel within the environment, moving market-side dispersion to the budget side.
Both halves of that finding are reported, because only one of them is the half the
premise predicts.

The random-utility random-opportunity architecture separates them by putting the
availability object in the likelihood as its own factor. A household's choice
probability over job packages is

$$
P_{ij} \;=\;
\frac{\exp\!\big(u_{ij}(\theta) + \log g_{ij}(\theta)\big)}
{\sum_{j'} \exp\!\big(u_{ij'}(\theta) + \log g_{ij'}(\theta)\big)} ,
$$

with $u$ a utility over the package's consumption and leisure and $g$ an
*opportunity density* over the latent job space. The two are estimated jointly.
Availability terms therefore have somewhere to go other than into tastes, and
that — not the fit — is the reason for the architecture. This paper adds three
things to the standard RURO specification: an **occupation** margin in the
availability object; an occupation-conditional **wage-offer location**, so that
the wage is a property of the job rather than of the person; and the entire
welfare-and-decomposition layer built on top.

Three points of discipline should be stated at the outset, because they govern
how every coefficient below is read.

1. **The opportunity set is an estimated density, not a menu.** Nothing in the
   data records the jobs a household could have had. What the design delivers is
   $g_{ij}$: an availability weight over a continuous latent job space. Every
   welfare object in this paper is a functional of that estimated density and
   inherits its model-conditionality.
2. **The proposal is computation; the offer density is economics.** Alternatives
   are sampled, and the sampled-set likelihood carries McFadden's $-\log q_{ij}$
   correction. The proposal $q$ is a calibrated numerical instrument. It carries
   no parameter of interest, it cancels from the estimand exactly, and no sign or
   magnitude on the proposal side may be read economically. A proposal may be
   richer than its target.
3. **The access margin does not yet separate capability from availability.** The
   present access density may combine personal capability and market
   availability; it does not yet separately identify $A_i$ from $O_i$. This
   sentence travels with the access channel wherever it appears.

### 1.3 The headline, stated plainly

Welfare here is money-metric and, specifically, it is *equivalent income at a
common reference pay*: the flat consumption level that, offered at every job in
the household's own opportunity set, would leave the household exactly as well off
as it actually is. This measure compensates for pay and holds the household
responsible for its own set — it prices what you can get, never what it pays.
The inequality of that measure across households is what gets decomposed.

The decomposition is an Owen value over the coalition structure
$\{\{\mathrm{pref}\},\{\mathrm{acc},\mathrm{earn},\mathrm{needs}\}\}$: an exhaustive two-player game between preferences and the
complete environment, with the environment's three internal channels entering as
a nested grouped layer. The contribution of a channel is the fall in measured
inequality when that channel is equalised across households, valued by the Owen
rule so that the answer does not depend on the order in which channels are
equalised.

On the preferred singles specification, the picture is this.

- **The environment dominates.** Equalising the whole non-preference environment
  removes between **89.0 and 93.7 per cent** of baseline money-metric inequality
  under the two ratified reference-preference conventions and on both the raw and
  the equivalized basis. Across all eight rows of the headline table — which adds
  the benchmark specification — the range is 89.0 to 96.7 per cent. Equalising
  preferences removes the complement, 3.3 to 11.0 per cent, with a sign that does
  not change anywhere.
- **Inside the environment, the two market channels are substantial and the
  budget channel is larger.** On the preferred model with the female reference
  and the raw basis, equalising job access removes **14.9 per cent** (±1.1) of
  baseline inequality and equalising earning opportunities **20.6 per cent**
  (±1.6). Taken together — as one coalition, jackknifed as one quantity — the two
  market channels remove **35.5 per cent** (±0.9). On the coalition-consistent
  equivalized basis the combined market figure is **25.9 per cent** (±0.9).
- **Endowments and needs are the largest single nested contribution.**
  **58.2 per cent** (±1.5) on the preferred model, female reference, raw basis;
  53.2 to 68.9 per cent across the eight rows; and the order endowments and
  needs above earning opportunities above job access holds in
  every one of them.

These are not statements that job opportunities are unimportant. Removing all
between-household variation in job access alone removes about a seventh of
measured money-metric inequality, and removing the two market channels together
removes about a third of it on the raw basis. What the numbers say is that in
*this* population — French single adults with a well-defined labour-supply
decision, under the French 2016 tax–benefit system — the budget side of the
environment carries more of the measured dispersion than the market side does.
That is a fact about a modelled decomposition of a modelled measure on one
country-year, and it is stated as such.

The ordering *between* job access and earning opportunities is deliberately not
claimed. The two channels have distinct point estimates in every row of the
table, but the access channel is precisely the one that does not yet separate
$A_i$ from $O_i$. The design does not identify that ordering, so no ranking is
claimed; the numbers are printed and the ranking is not asserted.

### 1.4 Contributions

**Substantive.** This is, as far as we are aware, the first paper that estimates
a structural latent-opportunity labour-supply model, carries the estimated
opportunity object into a money-metric welfare measure defined on constrained
feasible sets, and decomposes the inequality of that measure into preference and
environment components in an order-independent way — with the environment split
into job access, earning opportunities, and endowments and needs. The pieces
exist separately in three literatures. The integrated object does not.

**Methodological, first: the coalition-consistent inversion.** A money-metric
measure is defined by an indifference between the attained situation and an
optimum over a counterfactual budget. When a decomposition equalises a channel,
the attained side moves. If the *reference* side is held at the baseline — as it
naturally is, because the reference is what makes coalition values comparable —
the two sides move asymmetrically and the fully common state does not close. The
fix is to take both the preference block and the opportunity block *from the
coalition* on both sides of the indifference. This is not a tuning choice; it is
what makes the decomposition exhaustive. Measured: it removes about 95 per cent
of the residual in every arm (§7.1 and Appendix B).

**Methodological, second: the coalition-consistent equivalization.** Equivalized
welfare divides by an equivalence scale, and the scale is a function of household
composition. But household composition is one of the objects the
endowments-and-needs channel equalises. Freezing each household's own scale in
all sixteen coalition states therefore divides a common numerator by a
household-specific number in the fully common state, and reintroduces exactly the
dispersion the operator removed. Measured on this sample, the residual it creates
is **0.071799**, which is — to six decimals — the weighted Gini of $1/m$. Letting
the scale move with the channel restores exhaustiveness exactly. The point
generalises to any decomposition that equalises demographics and reports
equivalized outcomes, and it is not, as far as we know, in the literature.

**Empirical infrastructure.** Every one of the 157,055 job packages in the
estimation frame carries a disposable income that the French 2016 tax–benefit
system actually delivers at that package, computed by EUROMOD rather than by an
approximating budget function. The decomposition's budget channel is a *panel
swap*: node utilities are re-evaluated against the income the system returns for
the node's own wage and hours against a common reference background. That is only
possible because pricing is exact and deterministic.

### 1.5 Roadmap

§2 positions the paper against four neighbouring literatures and against its
closest competitors. §3 sets out the framework: the model, the welfare measure,
the four cells and the decomposition, including the equivalization result. §4
describes the data, the sample, the institutional setting and the EUROMOD layer.
§5 gives the estimator, the identification arguments, the draw-count stability
study, and the three heterogeneity extensions that were tested and rejected —
which are reported here as *identification evidence*, not as failures. §6 gives
the singles estimates and fit. §7 gives the welfare decomposition and is the
paper's core. §8 gives the couples module. §9 is the external-validation
placeholder. §10 states the limitations. §11 concludes. Appendix A carries the
full parameter tables, Appendix B the exhaustiveness saga in one page, Appendix C
the numerical layer, and Appendix D the couples tables. A self-check table binding
every numeral in the paper to a source closes the document.

---

## 2. Literature positioning

The literature is strong on the separate building blocks and weak on their
integration. Four neighbouring bodies of work each supply one ingredient, and no
one of them supplies the object this paper reports.

### 2.1 Four neighbours

**Constrained structural labour supply: RURO and latent jobs.** This literature
gives the behavioural architecture — jobs as packages, opportunity densities,
sampled alternatives, and an explicit warning that choice-set specification
matters for counterfactuals. It is the positive backbone of this paper. Its
canonical statement of the field, including the unresolved tension between common
welfare functions and preference-respecting welfare measures, is Aaberge and
Colombino (2018); the closest empirical antecedent with non-convex tax–benefit
constraints and region-conditioned opportunity heterogeneity is Aaberge, Colombino
and Strøm (1999); and Aaberge, Colombino and Wennemo (2009) is the paper that
shows the opportunity block is the empirically fragile component, with
first-order consequences for policy counterfactuals when the choice set is
poorly represented. Dagsvik et al. (2014) is the conceptual framing — why latent
jobs should be read as opportunities rather than disguised hours dummies — and
Dagsvik and Jia (2016) the identification paper that says how far the
preferences–opportunities separation can be taken with cross-sectional data.

**Empirical welfare analysis under heterogeneous preferences.** This literature
shows that money-metric comparisons move once preferences are allowed to differ,
and it supplies the normative machinery for respecting that heterogeneity rather
than assuming it away. It is close, and it is incomplete for the present purpose,
because it typically lacks an explicit opportunity-set object and therefore risks
booking constrained outcomes as preferences. Bargain et al. (2013) is the clearest
empirical template for the money-metric layer, and it concedes openly that what it
labels preferences may embed unmodelled opportunity constraints.

**Inequality of opportunity and responsibility-sensitive measurement.** This is
where the normative interpretation comes from: some differences should be
compensated, others respected. Most of that literature works with type partitions
or reduced-form circumstances rather than with estimated feasible job sets, and it
does not separate access from earning capacity inside the circumstance set.

**Decomposition methodology.** Shorrocks (2013) supplies the rule that turns a
structural separation into a reportable, order-independent quantitative result,
and the grouped/Owen extension is what makes a *nested* channel layer reportable
in the same way. Shorrocks gives the rule, not the factor definitions. The missing
step was never the formula; it was the economic construction of the factors inside
a structural labour-supply and welfare framework.

### 2.2 The closest welfare precedent, verbatim

The paper's position relative to the closest empirical welfare precedent is on
the record in the following terms, which are reproduced here verbatim:

> "Decoster and Haan (2015) provide a direct empirical precedent for carrying
> structurally estimated consumption–leisure preference heterogeneity into
> preference-respecting money-metric welfare comparisons. In their framework,
> differences in individual constraints are represented primarily by gross
> wages, non-labour income, and the tax-benefit budget, while labour supply is
> evaluated without a household-specific latent distribution of available jobs.
> The present paper adds that missing opportunity object. It distinguishes the
> distribution of accessible employment, hours, and occupation packages from the
> wage distribution conditional on those packages, and carries both objects,
> together with heterogeneous preferences and budget-side endowments, into the
> measurement and decomposition of money-metric well-being inequality."

Four positioning points attach to that paragraph. Decoster and Haan estimate
heterogeneous consumption–leisure preferences and preserve them in money-metric
welfare comparisons; their non-preference environment is represented primarily by
the gross wage, non-labour income and the tax–benefit budget; they do not estimate
household-specific latent job-opportunity distributions; and the present paper
separates job access and feasibility from earning capacity conditional on the job,
and carries both into welfare-inequality decomposition. The reference is
Decoster, André, and Peter Haan. 2015. "Empirical Welfare Analysis with Preference
Heterogeneity." *International Tax and Public Finance* 22(2): 224–251, with the
2013 conference version as the accessible working-paper source. It should not be
confused with Carpantier and Sapata (2016), whose machinery — conditional equality
and egalitarian equivalence on U.S. singles, with partially individualized
preferences recovered from revealed-choice discrepancies — is a different question
on different data.

### 2.3 The closest substantive competitor

Jacquet, Jia and Thoresen (2026) is the closest substantive competitor and the
first objection any reader will raise. It already introduces a
responsibility-sensitive comparison inside a structural job-choice model and
computes a circumstance-only welfare object. The answer to "what is new?" has to
be sharper than "France instead of Norway", and it is threefold. First,
*decomposition is the object here, not a by-product*: the paper reports an
order-independent attribution over an exhaustive set of channels, with
exhaustiveness tested rather than assumed, rather than a two-way welfare contrast.
Second, the dual object is constructed: the state that neutralizes the environment
while keeping preferences ($W^{01}$) exists here alongside the state that
neutralizes preferences while keeping the environment ($W^{10}$), and the Owen
value uses all four combinations rather than one contrast. Third, the environment
is not a single object: it is split into job access, earning opportunities and
endowments-and-needs, which is where the substantive result lives. If those three
differences do not survive visibly into the tables, the paper will read as
derivative, and that is the standard it should be held to.

### 2.4 Capéau et al.'s opportunity measure as the degenerate case

The RURO tradition writes the availability object, in Dagsvik's naming, as an
*opportunity measure* $\theta g(h)$: a scalar job-offer intensity $\theta$ times
an offer distribution over hours. Aaberge, Colombino and Wennemo (2009) estimate
that intensity as a **common scalar** with no covariates, alongside two hours-band
peak parameters. Capéau, Decoster and Dekkers (2016) make the intensity
covariate-dependent, $\log q(x) = \eta_q' x$, on region, education, age, sex and a
type-specific unemployment rate, with a log-normal wage-offer density in education
and potential experience and a piecewise-uniform hours density conditioned on sex
alone; the sampled-alternatives correction they derive is the same McFadden object
carried here. There is **no occupation channel** anywhere in that model, and there
is no welfare object and no decomposition.

The present specification nests theirs in a precise sense. Switch off the
occupation availability weights and the occupation-conditional wage-offer
location, and what remains — a level shift on every working package moved by
a group-specific unemployment rate, geography and urbanisation, times a step
density over hours bands, times a log-normal wage-offer density in education and
experience — is exactly their $\theta \cdot g_2(h) \cdot g_1(w)$ with a richer
conditioning set on the intensity — and it even carries the same
exclusion-restricted shifter they use, a group-specific unemployment rate.
**Capéau et al.'s $\theta$ is the degenerate
case of the access margin used here**: their access object is one number per
covariate cell, ours is that number plus a sex-specific occupation-availability
vector, and the wage location is allowed to shift with the occupation that
availability vector places the household in. That extra structure is not
decoration. It is what makes the split between *job access* and *earning
opportunities* an object at all rather than a partition of a single scalar, and
§6.5 shows that removing it does not make the effect disappear — it relocates it
into education in the wage block and into occupation access, which is the
sharpest evidence in the paper that the two channels are distinguishable at all.

The other side of that comparison is a warning the same literature supplies and
this paper inherits. Capéau et al. state plainly that the induced utility and the
hours-offer density are not separately non-parametrically identified — the hours
peaks could in principle be attributed to preferences instead. That is exactly the
reason the 35-hour coefficient in §6.3 is named an institutionally motivated
opportunity peak and never an estimate of a statutory effect, and the reason the
non-identification sentence travels with the access channel throughout.

### 2.5 The gap, stated precisely

There is still no paper that takes a structurally estimated latent-opportunity
labour-supply model, computes a money-metric welfare object conditional on
constrained feasible sets, and decomposes welfare inequality into preference and
environment components in an order-independent way on a concrete empirical
baseline, with the environment split into access, earning opportunities and the
budget side. That is the gap. This paper fills it on France 2016 single-adult
households and reports what it finds, including where the finding is sensitive to
a normative convention and where the design cannot yet separate two objects it
would like to.

The main vulnerability is the one the identification literature already names: the
preferences–opportunities split is identified more cleanly as a product than as
its factors, and a decomposition of an incompletely identified split risks being
parametric bookkeeping. The response is not denial. It is that the paper is a
disciplined structural decomposition under maintained assumptions stated in the
open; that the two heterogeneity extensions which would most obviously threaten
the split were tested and reported negative with their measured reasons (§5.4);
that the nested channel layer is reported unranked; and that every magnitude
travels with its integration band and its provisional label.
---

## 3. Framework

### 3.1 Terminology

Four terms are used throughout in exactly one sense each, and the discipline is
part of the argument rather than housekeeping.

| term | what it denotes |
|---|---|
| **job access / feasibility** | which job packages are available to the household at all, and at what hours and in what occupations |
| **earning capacity / wage-offer technology** | what a package pays, conditional on the job |
| **preferences** | the consumption–leisure trade-off |
| **endowments / needs** | non-labour income, household composition, and every other household-specific input to the tax–benefit budget mapping |

**The ability set $A_i$ is a reserved term.** It denotes the set of jobs a person
is capable or eligible to perform, and nothing else. It is not used loosely for
the opportunity set, the access density, or the wage distribution.
**Opportunity-set dominance is not productivity**: dominance is a later
comparison relation between opportunity sets or distributions, and it is not the
definition of earning capacity.

The following sentence is carried explicitly wherever the access density is
introduced or an attribution is made to the access channel:

> The present access density may combine personal capability and market
> availability; it does not yet separately identify $A_i$ from $O_i$.

### 3.2 The model

A household does not choose hours off a continuum. It takes or declines *job
packages* that the market puts in front of it, and a package is a triple
$(h, w, k)$ — weekly hours, an hourly wage, an occupation — together with the
disposable income the tax–benefit system delivers at that triple. The
specification carries two distinct objects: a **utility function**, which says
how a household ranks packages it can have, and an **opportunity density**, which
says how available each package is. The likelihood is what separates them, and
reading any coefficient means knowing which of the two it belongs to.

**Utility.** Preferences are Box–Cox over consumption and leisure, with the taste
shifters carried in the leisure weight:

$$
u_{ij} \;=\; \beta_{\ell}^{g}(\mathbf{x}_i)\,
\mathcal{B}\!\left(\tilde{\ell}_{ij};\theta_{\ell}^{g}\right)
\;+\; \beta_{c}\,\mathcal{B}\!\left(\tilde{c}_{ij};\theta_{c}\right),
\qquad
\mathcal{B}(z;\theta)=\frac{z^{\theta}-1}{\theta},
$$

$$
\beta_{\ell}^{g}(\mathbf{x}_i)\;=\;\beta_{\ell 0}^{g}
+\beta_{\ell a}^{g}a_i+\beta_{\ell a^{2}}^{g}a_i^{2}
+\mathbb{1}\{g=\text{women}\}\,\beta_{\ell k}^{g}k_i ,
$$

with $\tilde{\ell}_{ij}=(\bar L-h_{ij})/\lambda_{\ell}$,
$\tilde{c}_{ij}=c_{ij}/\lambda_c$, $a_i$ age centred and scaled by ten, $k_i$ the
number of children, and $\beta_c\equiv 1$ as the scale numeraire. The consumption
curvature $\theta_c$ is shared by the two sexes by construction of the certified
specification; the leisure curvature $\theta_{\ell}^{g}$ is not. The leisure
normaliser is $\lambda_{\ell}=10$ hours.

**The opportunity density.** Availability factorises into four margins, each
equal to one at its own reference, the last three switched off on the
non-employment package ($E_{ij}=\mathbb{1}\{h_{ij}>0\}$):

$$
g_{ij}\;=\;g^{E}_{ij}\cdot g^{H}_{ij}\cdot g^{\mathrm{Occ}}_{ij}\cdot g^{W}_{ij}.
$$

*The access margin* $g^{E}$ is a level shift on every working package, moved by
the group-specific unemployment rate, the region of residence and urbanisation:

$$
\log g^{E}_{ij}=E_{ij}\Bigl[\beta_{E}+\beta_{s}\tilde{s}_i
+\textstyle\sum_{r=2}^{8}\beta_{r}\mathbb{1}\{R_i=r\}
+\beta_{u}U_i+\beta_{m}M_i\Bigr].
$$

*The hours-band factor* $g^{H}$ is a step density over five bands, the statutory
35-hour band being the reference with its coefficient normalised to zero:

$$
\log g^{H}_{ij}=\sum_{b}\beta_{b}\,\mathbb{1}\{h_{ij}\in B_b\},
\qquad \beta_{\mathrm{F35}}\equiv 0 .
$$

The preferred positive specification adds one coefficient on a 35-hour indicator
inside this factor. We label it an **institutionally motivated opportunity peak**:
it is a feature of the estimated offer density at the statutory week, not an
estimate of the causal effect of any statute. The restricted model at that
coefficient equal to zero reproduces the benchmark objective to
$2.9\times10^{-10}$ on the corrected frame, so the addition is a genuine
one-degree-of-freedom restriction rather than a reparameterisation.

*The occupation weights* $g^{\mathrm{Occ}}$ place four occupation categories, the
first omitted, with a separate set of offer weights for men and for women:
$\log g^{\mathrm{Occ}}_{ij}=E_{ij}\sum_{k=2}^{4}\beta^{\mathrm{occ}}_{k,g}
\mathbb{1}\{o_{ij}=k\}$, $\beta^{\mathrm{occ}}_{1,g}\equiv 0$.

*The wage location* $g^{W}$ is an occupation-conditional log-normal offer density
— a Mincer equation carried **inside** the opportunity set, so that it describes
the wage a person could be offered rather than the wage the employed are seen at:

$$
\log g^{W}_{ij}=E_{ij}\Bigl[-\tfrac12\Bigl(\tfrac{\log w_{ij}-\mu_i}{\sigma}\Bigr)^{2}
-\log\sigma-\tfrac12\log 2\pi-\log w_{ij}\Bigr],
\qquad
\mu_i=\beta_{w0}+\beta_{wL}L_i+\beta_{wH}H_i+\beta_{wx}x_i+\beta_{wx^{2}}x_i^{2},
$$

with the preferred specification adding occupation-specific location shifts
$\delta_{\mathrm{occ}}$. These are **location shifts of the offer distribution,
not causal occupational wage premia**, and no sentence in this paper reads them
as the latter.

One convention is not visible in the algebra and governs how the regional and
occupation coefficients are read: the estimator centres those terms within each
household's own choice set, weighting by the proposal density,
$\tilde m_{ij}=m_{ij}-\sum_{j'}q_{ij'}m_{ij'}\big/\sum_{j'}q_{ij'}$, so they are
read against the household's own set rather than a global origin.

### 3.3 The welfare measure

Welfare is money-metric. Each measure asks what consumption level, under a stated
reference object, would leave the household exactly as well off as its own
opportunity situation. A measure solves

$$
W(z,R,A;y)=w \quad\Longleftrightarrow\quad z \;\mathrel{I}\; \max_{R}\{B\},
$$

an indifference between the attained bundle $z$ and the own-preference optimum
over a measure-specific counterfactual budget $B$; the measures differ **only** in
how $B$ is built. The axiomatic basis is the companion theory paper's and is not
reproduced: what that paper establishes, and what we use, is that each member of
the family is characterised by the responsibility/compensation stance its
reference encodes, so that choosing a reference is a normative act made explicit
rather than a technical convenience.

**The carrier measure: $W^1$, equivalent income at a common reference pay.**
$W^1$ builds $B$ from the household's **own** opportunity set $A$ with **pay
ignored**: $z'=(c',j')\in B \iff j'\in A$ and $c'=w$, a flat consumption level $w$
at every job in $A$. The money-metric anchor is that flat level $w$ itself. $W^1$
is therefore the equivalent income at a common reference pay: it compensates for
pay and holds the household responsible for its set — it prices *what you can
get*, never *what it pays*. It is the measure the decomposition is carried on.

**The normative-reference sensitivities: $W^4$ and $W^6$.** $W^4$ takes the
non-employment option as its reference and is a Full Compensation reading; $W^6$
takes the universal job set under an equal-pay profile, and is Full Compensation
with a weak-responsibility component. They are reported as **normative-reference
disclosures**: they show how the valuation moves when the responsibility cut
moves. They are **not** evidence that the $W^1$ result is quantitatively robust,
and no cross-measure quantitative robustness claim is licensed in any form.

One member of the family is not operational on this design and is recorded as a
compatibility finding rather than a result: the best-paid-equivalent measure
requires the maximum pay over the household's actual set, whereas any
implementation here can only form the maximum over its *sampled* nodes. On a
continuous latent support those are not the same object, and the sampled-set
maximum has no basis-invariant target. It is out of the source decomposition and
out of paper-facing welfare inequality.

**The ex-ante common quadrature support — the frozen design.** The nodes are
*integration support*, not a menu, and in the ex-ante construction the observed job
carries no privileged mass in any state. The design goes one step further than
that: **all households are evaluated on a common set of quadrature nodes**, so
that finite integration-support variation cannot appear as welfare inequality.
This is not a common realised economic opportunity set, and households are not
claimed to face a common list of jobs; only the numerical support changed. The
common proposal is the record's own base component with the household index
integrated out,
$\bar q_{\mathrm{base}}(e,k,h,w)=q_E(e)\,q_H(h)\sum_i \omega_i\,q_{\mathrm{Occ},i}(k)\,q_{W,i}(w\mid k)$,
which makes domination — $\bar q \ge \omega_i q_i$ pointwise, hence bounded
importance weights — a *construction property* rather than an argument; the
minimum slack over $3{,}184{,}640$ household $\times$ node comparisons is
$+3.226$ nats. Coverage improved rather than degraded: the median per-household
effective sample size is about a third higher than the household-specific
support's in every arm. The support change moved the fully-observed welfare level
by $-5.53\%$ on the preferred model and $-7.74\%$ on the benchmark; that movement
is a quadrature-support difference and nothing else, it is disclosed, and absolute
levels are not frozen as final.

**The coalition-consistent inversion — the frozen design.** The money metric
solves $R^{S}_{\text{replace}}(w) = V^{S}_{i}$ for $w$. In the earlier
implementation the leisure block and the opportunity block on the *reference* side
were frozen at the baseline coalition while the attained side moved with the
coalition — an asymmetry that put the same object on the two sides of one
indifference at two different coalitions. The correction takes $u$ and the
opportunity index **from the coalition** on both sides, so that the same reference
set $\bar A$ and the same responsibility stance $R$ appear on both sides in every
coalition. Nothing else changes: the same bracketing solve, the same tolerances,
the same normalisation, the same ex-ante support. Every inversion input was
classified to exactly one channel before the correction was run, and no input was
undeterminable. The measured effect is in §7.1 and Appendix B: the correction
removes about 95 per cent of the residual in every arm, and the common quadrature
support removes essentially all of the rest.

### 3.4 The decomposition

**The two-player structure.** The headline architecture is an exhaustive
two-player game — **preferences versus the complete environment** — with the
environment's internal channels entering as a *nested*, grouped layer. In Owen
terms the coalition structure is
$\{\{\mathrm{pref}\},\{\mathrm{acc},\mathrm{earn},\mathrm{needs}\}\}$ over the primitive
players

* $\mathrm{pref}$ — **preferences**: the leisure weight, its age profile, the
  child shifter, and the preference block itself;
* $\mathrm{acc}$ — **job access**: the employment margin, its regional,
  urbanisation and group-unemployment arguments, and occupation availability;
* $\mathrm{earn}$ — **earning opportunities**: the education and experience
  loadings of the offer-wage location, and its occupation-conditional location
  shifts;
* $\mathrm{needs}$ — **endowments and needs**: non-labour income, needs-related
  demographics, and every other household-specific input to the tax–benefit
  budget mapping.

The players are named rather than lettered throughout, in the formal statements
as well as in the prose, so that a channel is always identifiable on sight and
never collides with the measure-side symbols of §3.3.

Two properties of the structure matter for how it is read. First, the two-player
partition sums to 100 per cent by construction, so preferences and environment
exhaust the game *conditional on exhaustiveness holding*. Second, **signed
contributions are legitimate**: a channel may enter with either sign, because
equalising a channel can raise measured inequality as easily as lower it, and no
component is a share of a positive total. Nothing here is a pie chart.

Equalising endowments and needs is a **panel swap, not a reweighting**: node
utilities are re-evaluated against the budget the tax–benefit system returns for
the node's own wage and hours against a common reference background. The residual
of the earlier three-player presentation is not relabelled as the
endowments-and-needs contribution; that contribution is formed from its own Owen
marginals, because the interactions have to be evaluated rather than assumed away.
A variable used on both sides moves only on the side it is used on — the
leisure-weight child term stays with preferences, while the tax-benefit-side child
term moves with endowments and needs.

**The four cells.** The design evaluates four preference/environment states under
one identical welfare definition and reference convention:

| cell | preferences | environment | coalition |
|---|---|---|---|
| $W^{00}$ | own | own | $\{\}$ |
| $W^{10}$ | reference | own | $\{\mathrm{pref}\}$ |
| $W^{01}$ | own | reference | $\{\mathrm{acc},\mathrm{earn},\mathrm{needs}\}$ |
| $W^{11}$ | reference | reference | $\{\mathrm{acc},\mathrm{earn},\mathrm{needs},\mathrm{pref}\}$ |

with $I^{00},I^{10},I^{01},I^{11}$ the corresponding inequality indices. These are
**well-being levels under stated reference conventions**; none is a compensating
variation or a tax-reform welfare change, and no tax reform is required to define
them. No
cell is a compensating variation, none is $CV$, $CV^{\circ}$ or
$CV^{\mathrm{pref}}$, and none may be described in those terms. The four cells are
the *level analogues* of those objects by what each neutralizes — $W^{10}$ answers
to $CV^{\circ}$, $W^{01}$ to $CV^{\mathrm{pref}}$, $W^{00}$ to the
actual-preferences-and-circumstances state a standard $CV$ evaluates across a
reform, and $W^{11}$ has no $CV$-family counterpart — but the analogy is one of
construction only, and the two-player Owen value uses all four combinations and is
not merely the opposite of $CV^{\circ}$. Policy-reform objects are preserved as a
later module and are not executed here.

Once the environment is split, the full state space is the sixteen coalitions of
$\{\mathrm{pref},\mathrm{acc},\mathrm{earn},\mathrm{needs}\}$, and the four principal cells above are the corners of it. The
signed contributions $C_{\mathrm{pref}}, C_{\mathrm{env}}$ and the nested
$C_{\mathrm{acc}}, C_{\mathrm{earn}}, C_{\mathrm{needs}}$ are Owen values on
that game, satisfying $C_{\mathrm{pref}} + C_{\mathrm{env}} = I^{00} - I^{11}$ and $C_{\mathrm{acc}} + C_{\mathrm{earn}} + C_{\mathrm{needs}} = C_{\mathrm{env}}$.

**Exhaustiveness is a tested property, and it now passes.** The construction is
licensed to report shares only if the fully common state $I^{11}$ is negligible,
and the test was pre-stated before any cell was read: $I^{11}$ counts as negligible
only if *both* $|I^{11}|\le 0.00125$ — the certified Gini-scale component-level
precision constant — and $|I^{11}|/I^{00}\le 0.01$. The test is equally explicit
that $I^{11}$ is not to be forced to zero and not renormalised mechanically, and
that a non-negligible $I^{11}$ **halts** the headline.

On the frozen design the test **passes, and in the reported arms it passes at
numerical zero rather than merely inside the tolerance**: $I^{11}$ is
$0.000\mathrm{e}{+}00$ in the female-primary arms and $-2.035\mathrm{e}{-}31$ in
the preferred model's male-reference arm, against an allowance of $0.00125$. The
fully common state returns a constant welfare vector, and both accounting
identities close at machine precision in every arm. That is what licenses the
percentages in §7. It was not always so: an earlier implementation failed the test
on both limbs in every arm, with $I^{1111}/I^{0000}=3.03$ on the preferred model,
and the headline was correctly halted. Appendix B is the one-page account of what
was found and removed between those two states, because the sequence is itself a
methodological result.

### 3.5 Equivalization is an endowments-and-needs object

Equivalized welfare divides each household's $W^1$ by a modified-OECD equivalence
scale $m_i = 1 + 0.5\times(\text{members aged }14+\text{ beyond the first}) +
0.3\times(\text{members under }14)$. On this sample $m \in [1.0, 2.9]$ with mean
$1.163$, and $1{,}127$ of $1{,}555$ households sit at $m=1$, so the equivalization
is not a relabelling.

The natural convention — freeze each household's own $m$ in all sixteen coalition
states — **destroys exhaustiveness**, and the way it does so is exact rather than
approximate. Under that convention $I^{11}$ rises from zero to **0.071799** in
every one of the four arms, 43 per cent of $I^{00}$. The residual is not
mysterious: the weighted Gini of $1/m$ is **0.071799**, the same number to six
decimals. Dividing a common numerator by a household-specific divisor reintroduces
exactly the dispersion of the scale, and no operator in $\{\mathrm{pref},\mathrm{acc},\mathrm{earn},\mathrm{needs}\}$ removes it
under that convention.

The fix is the one the coalition-consistent inversion already legislates: *the
reference side must move with the coalition*. Household composition **is** a
an endowments-and-needs object — one of the four channels of the formal
decomposition above. The
endowments-and-needs operator does not adjust income and leave the family intact;
it replaces the household's whole exogenous budget-side profile with the reference
profile and reprices the opportunity set at it. The frozen reference profile is a
single-person household aged 34, so $m_{\text{medoid}} = 1$, derived
from the reference parquet by the same formula rather than transcribed. Under the
coalition-consistent scale, exhaustiveness is restored exactly:
$I^{11} = 0.000\mathrm{e}{+}00$ and $-2.035\mathrm{e}{-}31$, as in the raw basis.
The own-scale leg is retained as the diagnostic that shows the size of the defect,
never as a headline.

**Why the scale moves: factor consistency, not closure.** Household composition is
part of the endowments-and-needs factor by definition, and the equalisation
operator replaces that exogenous needs profile with the reference profile. Because
the equivalence scale is a deterministic function of household composition, it is
evaluated at the coalition-specific composition whenever the endowments-and-needs
factor is replaced. The scale therefore moves with that coalition **as a
consequence of the definition of the factor, not in order to force the
decomposition to close**. Exact exhaustiveness is a consequence of this
convention. Under the alternative normative object — *equalise resources while
holding each household's own needs fixed* — the equivalence scale would remain
household-specific and the resulting dispersion would be a genuine needs component
requiring a different decomposition. This paper adopts the first object.

That the first object is also the one under which the four channels close exactly
is a *check* on the convention rather than the argument for it: a convention that
were internally inconsistent with the factor definition would be very unlikely to
produce an exactly zero fully common state, and it does not.

### 3.6 The numerical layer, in one paragraph

Three sources of numerical error are handled and reported separately, and none of
them is sampling uncertainty. Alternatives are drawn from a **defensive mixture**
proposal (75 base and 25 defensive draws per unit block, mixture weight
$\lambda=0.25$ exactly) on disjoint address spaces, so no region of the job space
carries a proposal density that can vanish relative to the target. The welfare
functionals are integrals over the estimated opportunity density and are evaluated
on an **Owen-scrambled Sobol basis with eight independent scrambles**, with the
per-household mean over scrambles taken *before* the log and before the
money-metric inversion — the order matters and is the order used throughout. Precision
is reported by a **delete-one-scramble jackknife**,
$SE_{\text{jack}}=\sqrt{\tfrac{7}{8}\sum_r (T_{(-r)}-\bar T)^2}$ and
$E_T = t_{0.975,7}\cdot SE_{\text{jack}}$ with $t_{0.975,7}=2.364624251$; no bias
term is folded in. **These bands are numerical-integration precision, never
sampling confidence intervals.** Sampling uncertainty of the estimated parameter
vector, propagated to the welfare functionals, is **not estimated in this paper**,
and that third row is stated rather than elided. Appendix C carries the
instrument-level detail and the full set of numerical checks.

---

## 4. Data and institutional setting

### 4.1 Data and sample

The estimation data are France 2016 EU-SILC / SRCV household microdata, taken in
the form EUROMOD delivers them: the input file `FR_2016_a3`, covering **11,459
households**. This is authentic survey microdata, not the synthetic HHoT training
database that shares part of the EUROMOD French documentation.

The modelled population is the set of households whose labour-supply decision is
well defined and separable: one or two prime-age adults who are neither retired,
disabled, nor still in education, and with no other household member who is
themselves working or employable. Applying that definition in sequence removes
about 62 per cent of the post-composition baseline, almost all of it at the first
two hurdles.

**Table 4.1 — Sample flow (households).**

| step | households | dropped | share of file total |
|---|---:|---:|---:|
| all households in the France 2016 input file | 11,459 | — | 100.0% |
| one- or two-adult households (composition screen) | 10,003 | 1,456 | 87.3% |
| every adult aged 20–60 | 5,793 | 4,210 | 50.6% |
| no adult still in education | 5,557 | 236 | 48.5% |
| no retirement or disability benefit | 4,973 | 584 | 43.4% |
| labour status in scope | 4,010 | 963 | 35.0% |
| no other employable or earning member | 3,887 | 123 | 33.9% |
| hours and wage within bounds | 3,830 | 57 | 33.4% |
| → single-adult households (modelled) | **1,555** | — | 13.6% |

The composition screen at the second row is a household-classification step, not a
behavioural one, and it is itemised separately: of the 1,456 households it
removes, **930** have three or more adults, **452** have two adults not mutually
linked as partners, **53** are two mutually linked adults of the same sex, and
**21** have no adult aged 20 or over.

Of the 3,830 households that clear the whole funnel, **1,555 are single-adult
households** — the estimation sample of this paper — and **2,275 are opposite-sex
couple households**, which are the parallel module of §8. The 1,555 single-adult
households contain 2,236 persons: a single adult decider plus, in some households,
children. Restricting the primary module to singles is a modelling choice rather
than a data limitation: a single adult's problem is one-dimensional in employment
and hours, while a couple requires a joint decision over two labour supplies and a
joint budget.

The estimation frame pairs each household with 101 job packages — the observed one
and 100 drawn alternatives — giving **$1{,}555 \times 101 = 157{,}055$ priced
rows**. All descriptive shares are weighted by the survey weight `dwt`; counts are
unweighted. The sample represents a population of **4,547,080**.

**Table 4.2 — Composition of the 1,555 single-adult households.**

| dimension | category | households | unweighted share | weighted share |
|---|---|---:|---:|---:|
| sex | female | 841 | 54.1% | 52.1% |
| sex | male | 714 | 45.9% | 47.9% |
| education | low | 232 | 14.9% | 14.5% |
| education | mid | 692 | 44.5% | 43.1% |
| education | high (tertiary) | 631 | 40.6% | 42.4% |
| employment | employed | 1,348 | 86.7% | 87.1% |
| employment | non-employed | 207 | 13.3% | 12.9% |

The sample is majority female and highly educated, and 87 per cent are employed.
The employment rate is high because the eligibility screen removes exactly the
groups with low attachment; it is the right denominator for this model, since the
margin being explained is the labour supply of people who could plausibly be
working.

**The parameter count, stated once.** The parameter vector has **51 coordinates**.
Ten are **pinned** — held, not estimated: the couples leisure block and two year
dummies, all of which carry identically zero gradient on a singles-only sample.
**41 are free and estimated**, and 41 is the $k$ in every information criterion in
this paper. Of those 41, two rest on an active box bound at the optimum and carry
no standard error, leaving **39 interior** coordinates, which is the constant
$K_{\text{interior}}$ used for inference. The paper's phrase "41 estimated
structural parameters" refers to the 41 free coordinates. The ten pinned
non-estimated couples coordinates are never displayed in a singles parameter
table, and the historical 47-coordinate pooled vector appears nowhere.

**The wage variable.** The production data carry **observed** hourly wages for
workers. The delivered variable `yivwg` satisfies the arithmetic identity
`yivwg = yem × (12/yemmy) / (lhw × 52/12)` on **100.0 per cent** of FR_2015 and
FR_2016 persons with observed hours and earnings, in every labour-status and
self-employment category, to machine precision; on the estimation frame the
model's `wage` equals `yivwg` bitwise on all **1,348** working chosen rows. It is
an observed wage, not a prediction. The one exception is small and named: the
**21** workers recorded with zero annual earnings, for whom no observed hourly
wage exists and the delivered value stands.

### 4.2 Institutional setting

France's statutory working week is 35 hours, and the observed hours distribution
piles up on it: a single dominant spike at 35, a second cluster in the high
thirties, and very little mass between the modes (Figure 1). Hours are chosen over
a small number of *bands*, not on a continuum; a specification treating hours as a
smooth choice variable would have to explain the gaps away.

The model's hours-band factor is a categorical density over five bands. Because
only differences between bands are identified, one band's coefficient must be
normalised, and the specification normalises the band containing the statutory
week — precisely because it is the modal band. Every other hours coefficient is
therefore read *relative to a statutory full-time job*. The 35-hour mass is in the
model as the yardstick, not excluded from it.

**Table 4.3 — The hours bands.**

| band | hours range | role in the offer density | workers |
|---|---|---|---:|
| statutory full-time (35 h reference) | 33.5 – 36.5 | reference — coefficient normalised to zero | 389 |
| short part-time | 17.5 – 21.5 | own estimated coefficient | 34 |
| long part-time | 28.5 – 30.5 | own estimated coefficient | 172 |
| above-statutory full time | 36.5 – 40.5 | own estimated coefficient | 436 |
| long hours (overtime) | 44.5 – 70.0 | own estimated coefficient | 296 |

*Worker counts are on the 1,327 employed households with positive recorded
earnings, over a contiguous partition of the hours line that closes the gaps
between the estimated bands.* The band $[36.5, 40.5)$ is **above-statutory full
time** — full-time work in excess of the statutory week, not "full time" as
against the 35-hour spike.

Nothing in this section, and nothing in the specification, is an estimate of the
effect of the statutory week. The 35-hour coefficient the preferred specification
adds is a feature of the estimated offer density at the statutory week — an
institutionally motivated opportunity peak — and the paper does not claim
identification of a statutory effect anywhere.

**Occupation.** Occupation enters as four task groups, collapsed from ISCO-08
one-digit codes.

**Table 4.4 — The occupation key: ISCO-08 major groups to the four task groups.**

| group | task group | ISCO-08 major groups | share of employed (weighted) |
|---:|---|---|---:|
| 1 | routine manual | 6, 7, 8, 9 — skilled agricultural; craft and trades; plant and machine operators; elementary | 27.5% |
| 2 | nonroutine manual | 5 — service and sales workers | 15.4% |
| 3 | routine cognitive | 4 — clerks | 9.4% |
| 4 | nonroutine cognitive | 1, 2, 3 — senior officials and managers; professionals; technicians and associate professionals | 47.6% |

The four categories are a task grouping, **not a skill ranking**. Elementary
occupations (ISCO 9) are collapsed with the skilled manual groups rather than
given their own category, and armed forces (ISCO 0) map to an unknown-occupation
sentinel that no household in this sample carries; non-employed rows carry a
separate no-occupation code. Occupation composition differs sharply by sex — group 1 employs 38
per cent of men against 18 per cent of women, groups 2 and 3 are each roughly
twice as common among women, and group 4 is the largest for both. Because the
offer density is allowed to depend on occupation separately by sex, this
composition is information rather than nuisance.

**The wage-offer summary.** Over the 1,327 employed households with
positive recorded earnings (weighted population 3,892,446), the delivered hourly
wage has a weighted **mean of €15.47** and a weighted **median of €14.05**. Its
range on the estimation frame is €2.06 to €94.76, with weighted p01 €3.14 and p99
€41.72. Wages are log-normal with a long right tail, which is why the wage-offer
block is specified as a log-normal density rather than a deterministic wage.

### 4.3 Geography

The finest household geography in the delivered data is **NUTS-2**: the variable
`drgn2`, **22** metropolitan régions. There is no commune, no département, no
employment zone and no NUTS-3. Cell sizes at NUTS-2 run from 3 to 245 households,
median 53.5, with 5 cells below 30. The two sampling-unit variables in the file
are unlabelled, have no published territorial crosswalk, and are clustering
dimensions, never merge keys. The estimated access block itself keys on the
coarser `drgn1` (ZEAT, 8 zones, cell sizes 122–279), carrying seven region
dummies.

Degree of urbanisation is a three-level coding: `drgur` 832 households, `drgmd`
328, `drgru` 395, with **rural as the reference category** — it is loaded but
carries no coefficient — and two urbanisation dummies against it. `gsur` is the
*continuous* group-specific unemployment rate from a (zone, education, sex)
lookup at opportunity year 2015, scaled by ten and conditional on working: 47 unique
household-level values, range $[0.053183, 0.225]$, mean $0.09451$, constant within
household. It is not a region dummy, has no omitted category, and is reported
separately from the region dummies throughout.

**The missing-region verification.** The EUROMOD French derivation contains a
recode that maps missing region to the capital région, which would contaminate any
Île-de-France comparison. It was checked against the EU-SILC household register
and **it never fired**: the register carries $N = 11{,}459$ households, an exact
match to the EUROMOD household universe; region is observed at NUTS-2 across all
22 codes; the missing-region flag count is $0$ and the weighted missing-region
share $0.0000\%$. The 245 frame households coded as capital-région are all
genuine. One standing disclosure travels with the geography: Corse has three
households, so no Corse-specific statement is possible anywhere in this paper.

### 4.4 EUROMOD, pricing, and take-up

Consumption is not a survey variable in this model; it is priced. **EUROMOD is
deterministic**: given a household, a weekly hours figure and an hourly wage, the
tax–benefit system returns a disposable income by arithmetic, and the same triple
always returns the same euro figure. Nothing in the estimation simulates a
tax–benefit outcome. All of the randomness in the pipeline is in *which* points
get evaluated, never in what a point is worth. That is what makes a counterfactual
job package priceable at all: every one of the 157,055 rows carries a disposable
income the tax–benefit system actually delivers at that package.

The priced object is EUROMOD's `ils_dispy`, adjusted for benefit take-up. Take-up
traits are rebuilt deterministically from the priced observed node —
revealed-first rates, seeded Bernoulli, seed `20162016`, revealed rates 0.548 for
non-workers and 0.265 for workers, realised shares 0.542 and 0.292 — and enter
through the mask
$\texttt{ils\_dispy\_takeup} = \texttt{ils\_dispy} - \texttt{bsa00\_s}\cdot(1-\texttt{take})$.

**The pricing convention on the minimum-income benefit, stated because it governs
every consumption figure in the paper.** The French system's minimum-income
benefit (RSA) is simulated in EUROMOD with a rank-based non-take-up rule that
rations to a *batch-relative* target. **The convention adopted here grants full
entitlement inside the pricing engine and applies take-up afterwards as a
household trait, once, at assembly.** Take-up is a property of the household, not
of the batch it happened to be priced in; granting full entitlement in the engine
and masking once at assembly is the only convention under which a household's
priced budget is a function of that household alone. Operationally the
full-entitlement flag is carried into the engine's input column list, which is
proven bitwise identical to running the pricing system with the non-take-up policy
switched off.

Take-up is the input weakness of the pipeline and is flagged rather than buried:
the rates are estimated on thin cells, and they enter consumption through the
take-up-adjusted disposable income the builder uses.

**The couples pricing correction, in one sentence.** The couples panel used in §8
was re-priced from scratch because the full-entitlement flag was absent from the
couples raw schema and could not reach the engine, so the rank-based rationing
fired and the take-up trait was then applied a second time at assembly — a defect
that made a household's disposable income depend on which other households were in
its batch and on its position in the sort, affecting **1,805 of 2,275 households
(79.3 per cent)** by up to €1,343.52 per month; the singles frame was never
affected, with a within-household identical-input spread of exactly zero across
all 1,555 households, and all couples results in this paper are computed on the
corrected panel, on which that spread is exactly zero on the full frame and
neighbour and position invariance are exact.
---

## 5. Estimation and identification

### 5.1 The sampled-alternatives estimator

The choice set is not enumerable — the latent job space is continuous in the wage
and in hours — so it is sampled. The estimator is a conditional logit over sampled
choice sets,

$$
\hat{\theta}=\arg\max_{\theta}\sum_{i=1}^{N}
\Bigl[V_{i\,j^{*}_i}(\theta)-\log\!\!\sum_{j\in\mathcal{C}_i}\!\exp V_{ij}(\theta)\Bigr],
$$

$$
V_{ij}(\theta)=\underbrace{u_{ij}(\theta)}_{\text{tastes}}
+\underbrace{\log g_{ij}(\theta)}_{\text{availability}}
-\underbrace{\log q_{ij}}_{\text{proposal correction}},
\qquad
q_{ij}=q^{E}_{ij}\bigl(q^{H}_{ij}q^{W}_{ij}q^{\mathrm{Occ}}_{ij}\bigr)^{E_{ij}} .
$$

Each household is given its observed package plus $R = 100$ drawn alternatives, so
$|\mathcal{C}_i| = 101$. The $-\log q_{ij}$ offset is McFadden's
sampling-of-alternatives correction, which makes the sampled-set likelihood
consistent for the parameters of the full choice set.

**Deterministic chosen inclusion.** The observed package is inserted into every
household's choice set with certainty, and the proposal correction on that row is
declared **exactly zero** (`chosen_inclusion: deterministic_unit`), while the
proposal convention on the drawn rows is the **exact marginal** density
(`convention: exact_marginal`). Both declarations are on the specification of
record and are checked rather than assumed. The consequence matters for how fit is
read and is stated in §6.2: the chosen row carries $\log q = 0$ while the 100
drawn rows carry large positive $-\log q$ corrections from continuous densities,
so any *within-set ranking* statistic compares one uncorrected point against a
hundred corrected ones.

**$q$ is computation; $g$ is economics.** The two objects share the words "hours",
"wage" and "occupation" and share nothing else. $q$ is the importance-sampling
proposal the alternatives were *drawn* from: a calibrated numerical instrument,
not estimated, carrying no parameter of interest, and cancelling from the estimand
exactly, because the composite index carries the matching correction. Changing the
proposal can change only the Monte-Carlo efficiency of the estimator. An arm that
"does better" as a proposal is a better *sampler*, never a better *model*. In
particular, **a proposal may be richer than its target**: conditioning the wage
proposal on occupation is a variance-reduction choice and says nothing about
whether wage offers genuinely shift with occupation — only the structural $g^{W}$
block speaks to that, and §6.5 is where it does.

**Inference.** Standard errors are a cluster-robust (CR1/HC1) sandwich on
household-clustered scores with $G=1{,}555$ clusters, the bread taken on the
interior block, and the finite-sample constant
$c=G/(G-K_{\text{interior}})=1.0257255936675462$ at $K_{\text{interior}}=39$.
Coefficients are read against the normal quantile $z_{0.975}=1.959963984540054$
rather than a $t$ quantile, because the sandwich is an asymptotic
normal-approximation object with no exact small-sample $t$ distribution behind it.
Two coordinates rest on active bounds and are dropped from the inference block
entirely, carrying no standard error.

### 5.2 Two exact invariance results

Two identification remarks discipline how the estimates are read, and both are
exact reparameterisation checks rather than robustness exercises.

**Age centring is exact.** Re-centring the age variable and carrying the
admissible set through the exact map returns the same optimum: the objective
agrees with the preferred specification to $1.38\times10^{-10}$ against a
$10^{-8}$ band, and the active set and the near-boundary flagged set are
identical.

**Bound-activity in the leisure block is a normalisation artefact, not a property
of the model.** The leisure normaliser is a unit choice. Re-expressing the
accepted point at $\lambda_{\ell}=40$ by the exact map — no re-estimation — sends
the age-squared coefficients from $+1.0$, at the ceiling of their box in the
$\lambda_{\ell}=10$ unit, to $0.034845$ for men and $0.055555$ for women, strictly
interior. The statement "age-squared is at a bound" is therefore a statement about
the $\lambda_{\ell}=10$ unit, not about the model. Invariance across
$\lambda_{\ell}\in\{10,40,45\}$ holds with the objective bitwise equal, choice
probabilities agreeing to $6.11\times10^{-16}$, marginal rates of substitution to
$5.55\times10^{-16}$ in relative terms, and indifference curves to
$2.17\times10^{-10}$ euros.

### 5.3 Draw-count stability

The estimator is a simulated one, so the first question about any coefficient is
whether it is a property of the model or of the draw count. It is answered by
re-estimating the whole specification at $R \in \{50, 100, 200, 400\}$ on nested
stems, with the certified multi-start, four-leg convergence and CR1 protocol at
every rung, and reading each rung's coefficients against the $R=100$ robust
standard errors.

**Figure 7** plots the optimised objective, the objective per
household and the free-block curvature against $R$. It carries a note on its face
that must be read with it: **the negative log-likelihood is not comparable across
$R$**. The sampled likelihood is a different objective at each draw count and
rises with $R$ by construction; the figure shows the shape, not a model
comparison.

What *is* comparable across $R$ is every coefficient and its robust standard
error, and every share statistic. **Figure 8** plots the key
coordinates — the 35-hour peak, the employment level, occupation access by sex,
the occupation wage-location shifts, the wage dispersion, and a leisure curvature
term — against $R$, normalised by the $R=100$ robust standard error. The result:
between $R=100$ and $R=400$ **no free interior coordinate moves by more than
0.21 of its own robust standard error**, the largest mover being a
male occupation-access coefficient. Between $R=50$ and $R=100$ the largest move is
0.56 of a standard error, which is why $R=50$ is not used. **Figure 9**
 plots predicted participation against $R$: the model matches the
weighted observed participation rate of 0.8708 with predictions of 0.8660, 0.8668,
0.8669 and 0.8665 at the four rungs.

The corresponding question on the welfare side is separate, because the welfare
objects are non-linear functionals of $\hat\theta$ through a money-metric
inversion, and is answered in §7.6 and **Figure 10**.

One disclosure about Figure 8's construction. The preferred singles specification
has one common employment-level coefficient, so the figure shows that coefficient
once; the sex contrast is instead shown through the sex-specific occupation-access
coefficients.
The figure shows the pooled $\beta_E$ in one panel, says so on its face, and gives
the panel that carries the sex contrast to the occupation-access coordinates,
which are the sex-specific job-access coordinates the model actually has.

### 5.4 Three heterogeneity extensions, and what their failure identifies

The choice model carries a job-package Gumbel shock and no household-level
persistent term. Three heterogeneity extensions were specified in advance and
assessed by **synthetic-recovery diagnostics before real-data estimation**, from the accepted
specification's own point, with the expected likelihood-ratio depth computed
exactly under the truth's marginal choice probabilities so that the finding does
not depend on a draw. All three are negative, they fail for **three different
measured reasons**, and under the standing rule that no extension is admitted
none satisfied the stated recovery criterion, so none is included in the preferred
specification, which is retained rather than an extension invented.

These results are reported here as **identification evidence**, not as an
appendix of failures, because between them they establish what a cross-section of
this design can and cannot support.

**HP — a random leisure intercept.** A household-level random term on the leisure
weight loads on the Box–Cox leisure transform, which at the estimated curvature is
nearly flat across a household's own alternatives: its within-household spread is
**0.0732** for men and **0.1270** for women against a Gumbel of scale one. The
expected likelihood-ratio signal against a zero variance is **0.0081** and
**0.1351** at the two non-zero truths, against the **2.706** a boundary test
requires. The expected objective peaks exactly at the truth, so the estimator is
right and the *design* is uninformative. Real-data estimation was not run, by rule.

**HO — a common working-alternative frailty.** A household-level random term on
the working indicator has about four times HP's leverage — loading standard
deviation **0.297**, and an axis likelihood-ratio depth of 1.02 to 13.56 rather
than HP's fraction of a nat. It nevertheless fails, and for a different reason:
because it shifts every working alternative equally, it is exactly a binary mixed
logit on the employment margin with **one observation per household**, and
re-fitting the accepted coordinates under a zero variance absorbs about **95 per
cent** of its signal through the employment intercept. The depth a
likelihood-ratio test actually computes — the *profile* depth, with the remaining
coordinates re-optimised — is **0.0492** and **0.6996**, again against **2.706**.
Real-data estimation was not run, by rule.

**W3 — wage-residual/preference dependence.** A correlation between the
person-level wage residual and a persistent preference component fails in a third
way: the correlation parameter runs to the $\pm 0.99$ endpoint of its box, and the
point estimate of the dependence is near-unbiased but has no usable interval. The
binding constraint is again the loading — the within-set spread of the Box–Cox
leisure transform, 0.073 and 0.127, is the same wall HP hit — and the
likelihood-ratio statistic against the preferred model has **no valid null
reference**, because the null sits on a boundary and the nuisance correlation is
unidentified under it.

**The loading principle.** Three failures, three mechanisms, one lesson worth
stating as a design rule. A persistent household-level term is identified in a
single-cross-section discrete-choice design only if two conditions hold together.
First, **leverage**: the variable the term loads on must have enough *within-household*
spread across the choice set, measured against the scale-one Gumbel, for the term
to change the ranking of a household's own alternatives; HP and W3 fail here, at
0.07–0.13. Second, **a second contrast**: even with leverage, the term must move
something the existing coordinates cannot absorb; HO has the leverage and fails
here, because a term that shifts all working alternatives equally is a shift the
employment intercept can re-fit, and with one choice per household there is no
second margin to pin the two apart. Depth on an *axis* — holding the rest of the
model fixed — is therefore not evidence; only depth on a *profile*, with the rest
re-optimised, is. That distinction is what separates HO's 13.56 from its 0.6996.

None of this establishes that preference or opportunity heterogeneity is absent.
It rejects *those three parameterisations* on *this design*, and it names exactly
what would change the arithmetic: repeated choices per household, which would
supply the second contrast on the employment margin; external moments on
job-offer or access rates or on wage offers, which would pin the persistent terms
from outside the choice likelihood; and desired-hours moments, which would
discipline the hours-band density against a stated target rather than infer both
from realised hours. No such moment enters the objective anywhere in this paper.

### 5.5 The age-bound diagnostic

Two free coordinates — the age-squared terms in the single-male and single-female
leisure weights — rest on an active box bound at $+1.0$ in the $\lambda_\ell = 10$
unit at the optimum, and carry no standard error. §5.2 establishes by exact
reparameterisation that this is a property of the unit and not of the model. The
narrower question the bound leaves open is what it costs — in the estimated age
profile, in the fit, and in the welfare layer — and a diagnostic was run under a
four-limb rule declared before any artefact was read.

**The design.** The admissible box of the four singles quadratic-age coordinates
is widened by a factor of five on half-widths — the linear terms from $\pm 5$ to
$\pm 25$, the quadratic terms from $\pm 1$ to $\pm 5$ — and *nothing else changes*:
no coordinate is added or removed, no pin is moved, no tolerance, seed, start,
contract or draw changes, and the couples block is untouched. Widening the whole
block by one factor keeps the 5:1 linear-to-quadratic half-width ratio,
which is what a quadratic-only widening would break. The box is deliberately not
taken as the pull-back of a unit box at a different leisure normaliser, because
that map is built from the estimated leisure curvatures and a declared admissible
region must not be a function of the parameter it constrains. The widened model is
re-estimated under the same multi-start and four-leg protocol, returns
`SINGLE-OPTIMUM`, and is then carried through the *same* welfare basis, support,
operators, inversion and jackknife as the headline, with only $\hat\theta$ varying.

**Limb A — the widened model is well behaved. Passes.** The active set goes to
**empty** rather than relocating onto the linear age terms, every coordinate is
interior, the free-block Hessian is full rank (41 of 41) and well conditioned
(minimum eigenvalue $+0.439$, condition number $1.19\times10^{5}$, clean tier), and
the near-boundary flagged set stays empty. This matters because an earlier,
quadratic-only widening had failed by relocating the constraint; that failure mode
does not repeat.

| | preferred model | widened box |
|---|---:|---:|
| free coordinates $k$ | 41 | 41 |
| active bounds at the optimum | 2 | **0** |
| interior coordinates | 39 | **41** |
| objective | 18022.7646 | 18022.2124 |
| free-block minimum eigenvalue | $+0.442$ | $+0.439$ |
| hours-grid share MAE | 0.008345 | 0.008269 |

**Limb B — the gain is negligible. Fails, and this is the informative limb.** The
objective improves by **0.552**, so twice the gain is **1.104**; because the two
specifications have the **same free coordinates and the same terms** and differ
only by the admissible region, that number is a bound-relaxation gain and **not** a
chi-square statistic with a degree of freedom, no $p$-value is quoted, and
$\Delta\mathrm{AIC} = \Delta\mathrm{BIC} = -1.104$ exactly because $k$ is identical. The two
released coordinates land at $1.447$ (s.e. 1.036, $z=1.40$, 95 % interval
$[-0.584, 3.477]$) for men and $1.722$ (s.e. 0.895, $z=1.92$, $[-0.032, 3.475]$)
for women — and **the bound value $+1.0$ lies inside both intervals**. The bound
was therefore not hiding an identified curvature; it was binding on a coefficient
the data do not pin down. That is a positive result about the retained
specification rather than a defect of the diagnostic.

**Limb C — the implied age profile is economically sensible. Passes.** The implied
leisure weight is strictly positive across ages 20–64 for both sexes and is
U-shaped with an *interior* minimum inside the observed support — at age 40 for
men (weight 4.55, against 10.31 at 20 and 12.92 at 64) and age 43 for women (4.36,
against 13.30 at 20 and 12.11 at 64). The implied compensation for one more weekly
hour of work is positive at every age for both sexes, with minima of €11.71 and
€28.73. Figures AB1 and AB2 plot both profiles under the two boxes.

**Limb D — something non-negligible moves. Passes, and it is the welfare layer.**
The positive layer barely moves: the hours-grid share error improves by 0.9 per
cent, the predicted employment share by 0.00013, the 35-hour peak from 2.5795 to
2.5692 (about a tenth of its own standard error), and every hours-band share in
the fourth decimal or beyond. The largest movement anywhere in the parameter
vector is 0.72 of a preferred-model robust standard error, on the
children-in-leisure shifter, followed by the two leisure curvatures at $-0.61$ and
$-0.43$. But of the 24 headline welfare quantities compared against their own
jackknife bands, **two leave their band, and both are the preference
contribution**: on the raw basis $C_{\mathrm{pref}}$ moves $+12.8$ per cent under the female
reference and $+5.2$ per cent under the male structural zero. Six of 126
quantities move across all bases; nothing else in the headline does, and no sign
and no ordering changes anywhere.

**The verdict: retain the preferred specification, and the margin is close.** The
widened box fails on the objective limb. The pre-declared rule
required all four limbs for the widened box to become a candidate replacement; it
fails the one asking for a materially better objective. The specification of
record is retained with its two bound-active coordinates.

Two things should be carried out of this diagnostic rather than filed. The first
is that the bound costs nothing the paper reads: it binds on a curvature the data
do not identify, and releasing it moves no coefficient the paper interprets by as
much as one standard error. The second is that **the one place it does register is
the preference contribution on the raw basis**, at about 13 per cent — the same
channel that carries the reference sensitivity of §7.5 and the couples
sensitivity of §8.4. Three independent perturbations of this design — the
reference-preference convention, a box on a preference curvature, and a pinned
refit of the couples male leisure block — all move the same quantity and leave the
environment side and the nested order alone. That is worth saying plainly: **the
preference/environment split is the fragile margin of this decomposition, and the
environment's internal structure is the robust one.**

---

## 6. Results: the singles module

### 6.1 The estimates

The final singles model carries **41 estimated structural parameters**.
**Figure 2** plots all 41 by economic block with CR1 95 per cent
intervals, and the full table with standard errors, $z$ statistics and inference
status is **Appendix A**. Blocks, and what they say:

| block | $n$ | reading |
|---|---:|---|
| singles-male leisure | 4 | intercept, age, age$^2$, curvature |
| singles-female leisure | 5 | as above plus the children-in-leisure shifter |
| consumption curvature | 1 | shared by the two groups by construction |
| hours opportunity | 5 | four band shifters plus the employment level $\beta_E$ |
| the 35-hour peak | 1 | the one coordinate the final model adds to the benchmark |
| market access | 10 | the group-specific unemployment rate, seven region dummies, two urbanisation dummies |
| occupation opportunity | 6 | three availability weights each for men and women |
| wage-offer technology | 6 | intercept, two education loadings, experience and its square, dispersion |
| occupation wage-location | 3 | $\delta_{\mathrm{occ}}$ |

Four features are worth reading off the table directly.

**The leisure curvatures differ sharply by sex and are precisely estimated.**
$\theta_\ell = -1.746$ (s.e. 0.247, $z=-7.07$) for single men and $-1.079$
(s.e. 0.245, $z=-4.40$) for single women. The two intercepts, $4.672$ and $4.244$,
are individually significant at conventional levels but wide (s.e. 2.00 and 1.86),
which is the standard picture for a Box–Cox level term that trades off against its
own curvature. The children-in-leisure shifter for women is $+1.169$ (s.e. 0.608,
$z=1.92$) — positive, as expected, and not precisely estimated. There is **no male
counterpart** to that coefficient in the specification, a structural absence that
turns out to matter a great deal for the welfare layer and is dealt with in §7.5
and Appendix B.

**The consumption curvature is $\theta_c = 0.168$** (s.e. 0.074, $z=2.27$),
comfortably inside the unit interval and well away from both the log limit and
linearity.

**The access block is where the sharpest coefficients are.** The employment level
is $\beta_E = -3.334$ ($z=-9.30$). The group-specific unemployment rate carries
$-1.253$ ($z=-6.32$): a higher unemployment rate for a household's own
region-education-sex group lowers the availability of working packages, which is
the sign the variable is there to test. None of the seven
region dummies has an interval excluding zero once the continuous rate is in, and
neither urbanisation dummy does — geography enters through the rate rather than
through the zone. The occupation-availability
weights, by contrast, are large and precise and differ strongly by sex: for men,
$-1.311$ ($z=-8.86$) on nonroutine manual and $-1.933$ ($z=-9.91$) on routine
cognitive against the routine-manual reference, with the nonroutine-cognitive
weight at $+0.005$ and an interval covering zero; for women, nonroutine cognitive at $+0.717$
($z=7.24$) and routine cognitive at $-0.405$ ($z=-3.07$). That contrast — men
concentrated in and around routine manual, women's availability tilted toward
nonroutine cognitive — is the single strongest piece of sex-specific structure in
the access block, and it is what the model uses to keep occupational sorting out
of the taste block.

**The wage-offer technology is conventional and tightly estimated.**
$\beta_{w0}=2.125$ ($z=41.3$); tertiary education shifts the offer location by
$+0.151$ log points ($z=5.06$) while the low-education loading is $+0.056$ with an
interval covering zero; experience enters at $+0.220$ ($z=2.52$) with a small
negative square whose interval covers zero; dispersion is $\sigma = 0.390$ ($z=29.4$).

### 6.2 Fit

The interpretable fit objects on an importance-sampled choice set are the **share**
statistics, where the predicted share $\sum_j p_{ij}\mathbb{1}[\text{bin}_j]$ is a
self-normalised importance-sampling estimate of the model-implied distribution and
is directly comparable to the observed weighted share. Four such objects are
reported.

| object | observed | predicted | figure |
|---|---:|---:|---|
| employment rate (weighted) | 0.8708 | 0.8668 | Figure 4 |
| the statutory band $[33.5,36.5)$ | 0.2485 | 0.2520 | Figure 1, Figure 3 |
| hours-grid share, mean absolute error over 12 bins | — | 0.0083 | Figure 3 |
| occupation share, largest absolute deviation over 5 categories | — | 0.0070 | Figure 5 |
| offered-wage quintile share, largest absolute deviation | — | 0.0532 | Figure 6 |

Employment is matched to four-tenths of a percentage point and the statutory band
to a third of one. The hours grid is matched to under a percentage point on
average across twelve bins, with two identifiable weak spots: the model
over-predicts the two thinnest short-hours bins (by $+0.011$ and $+0.021$) and
under-predicts the $[40.5,44.5)$ band by $-0.034$. Occupation is matched almost
exactly — the largest deviation across the five categories, including
non-employment, is seven-tenths of a percentage point.

**The one substantial misfit is in the offered-wage distribution, and it is
reported rather than smoothed.** The model over-predicts the bottom wage quintile
by $+0.053$ and under-predicts the second, third and fourth by $-0.026$, $-0.022$
and $-0.019$. This is a known and durable feature of the specification: §6.5
reports an attempt, specified in advance, to repair it with an hours-conditioned wage
location, and the attempt failed.

**Rank, top-$k$ and Brier statistics are absent from this paper by rule, and the
reason is structural rather than presentational.** Under
$V = u + \log g - \log q$ with deterministic chosen inclusion, the chosen row
carries $\log q = 0$ exactly while the 100 drawn rows carry large positive
$-\log q$ corrections from continuous densities, so within-set ranking compares an
uncorrected point against a hundred corrected ones. The resulting statistics are
near-degenerate in level — the chosen-row rank has median 101 of 101 and the
top-1, top-5 and top-10 hit rates are 0.000 for every specification including the
benchmark — and they are not comparable across draw counts. They are comparable
*across specifications on an identical frame*, and nowhere else, which is not a
use this paper makes. The corresponding figure was withdrawn from the paper set;
the files remain on disk.

### 6.3 The 35-hour peak

The single coordinate the preferred specification adds to the benchmark is a
shifter on the statutory-week indicator inside the hours-offer density. Its
estimate is

$$
\hat\beta_{h,\mathrm{F35}} = 2.5795 \quad (\text{s.e. } 0.0983,\ z = 26.24,\
\text{interior}),
$$

and it is the largest single improvement any one coordinate makes to this
specification: the likelihood-ratio statistic against the nested benchmark is
**861.42** on one degree of freedom, $\Delta\mathrm{AIC} = -859.42$ and
$\Delta\mathrm{BIC} = -854.07$. The restriction is genuine — the preferred model at
that coordinate equal to zero reproduces the benchmark's objective on the same
frame to $2.9\times10^{-10}$ — so this is a one-degree-of-freedom nesting and not a
reparameterisation.

**The licensed wording, and it is the only wording used.** This coefficient is an
**institutionally motivated opportunity peak in the estimated offer density at the
statutory week**. It says that the fitted density of *available* job packages has
a large mass point at 35 hours, over and above the band structure. It is **not** an
estimate of the causal effect of the 35-hour statute, no counterfactual removing
the statute is computed anywhere in this paper, and the identification literature's
own warning applies with full force: the induced utility and the hours-offer
density are not separately non-parametrically identified, so the peak *could* in
principle be a taste for the statutory week rather than an availability feature.
What the specification does is put it in the availability object rather than the
taste object, and say so.

The interest of the number is that it is large — a factor of roughly $e^{2.58}
\approx 13$ on the availability weight of the statutory band relative to the
smooth part of the schedule — and that it survives every stability check in §5.3
essentially unchanged.

### 6.4 The occupation wage-location shifts

The three $\delta_{\mathrm{occ}}$ coefficients are the extension that separates
the preferred specification and its benchmark from the certified base:

| shift | estimate | s.e. | $z$ |
|---|---:|---:|---:|
| $\delta_{\mathrm{occ},2}$ (nonroutine manual) | $-0.048$ | 0.041 | $-1.17$ |
| $\delta_{\mathrm{occ},3}$ (routine cognitive) | $+0.047$ | 0.037 | $1.28$ |
| $\delta_{\mathrm{occ},4}$ (nonroutine cognitive) | $+0.274$ | 0.035 | $7.78$ |

**These are location shifts of the wage-offer distribution, not causal
occupational wage premia.** The reading is: conditional on a job in nonroutine
cognitive being available to this household, the log-normal density of what that
job would pay is centred about 0.27 log points higher than in routine manual, at
the same education and experience and the same dispersion. It is a statement about
the offer technology, not about what happens to a person who moves occupation.
Nothing in the design identifies the latter, and the paper does not claim it.

### 6.5 The channel-separation null

Two variants specified in advance test whether the occupation wage-location block is
doing separable work or is a redundant relabelling of things already in the model.
They give opposite answers, and together they are the cleanest structural evidence
in the paper that job access and earning opportunities are distinguishable
channels at all.

**Removing $\delta_{\mathrm{occ}}$ does not remove the effect — it relocates it.**
The variant that drops the occupation wage-location entirely costs 49.9 in
objective, which is unremarkable. What is not unremarkable is where the effect
goes. The tertiary-education loading in the wage block jumps from $0.151$ to
$0.330$ — a move of **6.0 preferred-model standard errors** — and the female
nonroutine-cognitive *access* coefficient jumps from $0.717$ to $0.915$. With no
occupation term in the wage location, education in the earning-opportunity block
and occupation in the job-access block absorb it between them. That is a
channel-separation result: the same underlying variation is being loaded onto two
*different* channels depending on whether the model is given a place to put it,
and the decomposition of §7 is precisely an accounting over those channels. A
specification without $\delta_{\mathrm{occ}}$ would silently move mass from
earning opportunities into job access and into the education loading.

**Adding an hours-conditioned wage location is a null, and it does not repair the
wage misfit.** The mirror variant adds four hours-band shifters to the wage
location. Two of the four are individually significant with opposite signs — the
shortest band lies $+0.190$ above the statutory reference and the longest band
$-0.085$ below it, in log points — and the likelihood improves. But the two
information criteria split: $\Delta\mathrm{AIC} = -10.2$ against
$\Delta\mathrm{BIC} = +11.2$ on households and $+29.7$ on rows. Neither is a
BIC-supported extension. More decisively, it does **not** do the job it was
proposed for. The offered-wage quintile misfit of §6.2 is essentially where it was:
the variant takes 0.0061 off the bottom-quintile over-prediction, a 12.7 per cent
reduction, and gives 0.0020 of it straight back on the second quintile, leaving
the third unchanged to five decimals, so that the wage-quintile share mean
absolute error is *marginally worse* ($0.021761 \to 0.021830$). Five of seven fit
metrics degrade, and the deterioration is concentrated exactly in the two bins the
significant coefficient covers. **Nothing was promoted**: the honest answer to the
question the variant was built to answer is no, and the wage-quintile misfit
remains an open item of the specification.

### 6.6 Specification sensitivity: the preferred model against its benchmark

The benchmark is the occupation-conditioned wage specification without the
statutory-week peak — the final model minus that one coordinate: 40 free coordinates against 41, nested exactly, on the identical frame. On
every positive criterion the preferred model wins decisively — a likelihood-ratio
statistic of 861.42 on one degree of freedom, $\Delta\mathrm{AIC}=-859.4$,
$\Delta\mathrm{BIC}=-854.1$, an hours-grid share error four times smaller
($0.0083$ against $0.0338$), and a statutory-band share of 0.2520 against 0.0546
where the observed value is 0.2485. The benchmark simply cannot put mass at the
statutory week, and that is what it is for: it is the nested reference against
which the one coordinate is measured, not a candidate.

**But the two specifications are not close in the welfare layer, and this is a
finding rather than a nuisance.** The coefficient differences between them are
modest — the leisure curvatures move from $-1.75$ and $-1.08$ to $-2.42$ and
$-2.08$, the access and wage blocks barely move at all — and yet the preference
contribution to money-metric inequality is roughly *twice* as large under the
preferred model as under the benchmark: 6.30 per cent of baseline inequality
against 3.32 on the raw basis with the female reference, and 10.89 against 5.09
under the male reference (§7.2). The direction of every qualitative conclusion is
identical across the two — the sign of the preference contribution, the dominance
of the environment, and the order of the three environment channels all hold in
all eight rows of the
headline table — but the *magnitude* of the split between preferences and
environment is specification-sensitive at a factor of about two.

The mechanism is visible: a specification that cannot represent the statutory-week
mass in the offer density must represent the corresponding concentration of
observed hours somewhere, and the only other place available is the leisure
curvature, which moves substantially. The benchmark therefore prices a larger part
of the hours distribution as environment and a smaller part as preference. This is
an instance of exactly the confound the paper is about, showing up inside the
paper's own specification comparison, and it is the strongest argument in the
paper for reporting the decomposition under both models rather than one.

### 6.7 What a common-choice-set model would have found

*A different benchmark from §6.6, and the two should not be confused. §6.6's is the
**nested** benchmark — the same architecture minus the statutory-week coordinate —
and it exists to measure one coefficient. This one is the **common-choice-set**
benchmark: a conventional model with no opportunity object at all, which is not
nested in the preferred model and is not a candidate specification. It exists to
answer a question about method.*

The paper's premise is that putting every household on a common choice set forces
availability into the taste index. That is an argument, and it can be checked
rather than asserted. This subsection fits the benchmark the premise names — a
conventional common-choice-set model on the same data, the same priced packages
and the same welfare machinery — and reports what changes. It is the paper's own
counterfactual about method, and the result is **not** the one the premise most
naturally suggests.

**The benchmark.** Every household-indexed argument of the availability object is
replaced by a common reference value and the result is renormalised, so that all
households face the same offer environment; the preference block is then
re-estimated against that offset. What remains is a conventional discrete-choice
labour-supply model with hours constants, a fixed cost of work and a
sex-specific leisure block — the model a careful analyst without an opportunity
object would have fitted to these data. Job access and earning opportunities then
contribute **exactly zero** to the decomposition by construction; those zeros are
the benchmark's definition made arithmetic, not estimates that happened to vanish.

**Likelihood and information criteria, as descriptive provenance.** The benchmark
is 16 free parameters against 41 and is **129.1 nats worse** in objective, at
18,151.85 against 18,022.76 — a per-household log-score gap of 0.083. Both
information criteria prefer the richer model: $\mathrm{AIC}$ 36,127.5 against
36,335.7 and $\mathrm{BIC}$ 36,346.8 against 36,421.3. The likelihood-ratio
statistic against the restriction is 258.2 on 25 degrees of freedom, and it is
reported as an **upper bound**: the surviving opportunity coefficients are held at
their preferred-model values rather than re-optimised under the restriction, so
the freely-estimated restricted model would do at least as well. This whole block
is **descriptive provenance and not a test that settles the choice of
architecture**. The point that in-sample fit is close to uninformative across
choice-set specifications is well established, and the next paragraph is the
concrete demonstration of it.

**The benchmark fits the marginals as well or better.** Mean absolute deviation
between observed and model-implied shares, benchmark against preferred model:
hours **0.0080** against 0.0083, occupation **0.0029** against 0.0034, offered-wage
quintiles **0.0203** against 0.0261; employment 0.0042 against 0.0041. On three of
the four spaces the benchmark is *closer*, and on the fourth the two are
indistinguishable. A referee who judged these two models on marginal fit alone
would prefer the one with no opportunity object in it. **That is the argument for
not judging them on marginal fit alone**, and it is why the case for the
architecture in §6.5 rests on where variation *relocates* rather than on how well
either model fits.

**Where the availability information goes: into the taste parameters.** The
mechanism the paper claims is directly visible in the coefficients. The five
hours-band constants are recovered in the benchmark's *utility* index at
essentially the values they take as *availability* weights in the preferred model
— mean absolute difference **0.037**, maximum 0.075. The same constants, read
twice: under the preferred model they say a job of those hours is scarce or
plentiful; under the benchmark they say the household likes or dislikes those
hours. The fixed cost of work is the one that does not transfer cleanly, at
$+0.517$ against $-3.334$, because the employment margin in the preferred model
also carries the household's own region and unemployment rate, which the benchmark
makes common. And the consequence for how the two sexes are described is stark:
the male-minus-female leisure intercept gap is **$+0.428$ under the preferred model
and $-1.991$ under the benchmark** — a reversal of sign, not a change of
magnitude. Measured leisure preference shifts toward the group facing the less
favourable offer environment, which is exactly what the confound predicts.

**Welfare inequality falls.** Baseline money-metric inequality is **24.2 per cent
lower** under the benchmark on the raw basis, 0.101841 against 0.134277, and
**15.3 per cent lower** on the equivalized basis, 0.139869 against 0.165105.
Giving every household the same offer environment removes real dispersion in
well-being, because a large part of the dispersion *is* the offer environment.

**The preference-attribution gap is the surprise, and it is close to zero.** The
natural expectation — the one the paper's own premise invites — is that a model
with no opportunity object books the missing opportunity share as preference
heterogeneity. It does not. The preference *share* of the decomposition is
**6.4 per cent under the benchmark against 6.3 per cent under the preferred
model**, a difference of $+0.1$ percentage points against a numerical band of
$\pm 0.4$. The omitted market-side share has to go somewhere, and the three
destinations can be measured exactly, because the two models are evaluated on the
same integration scrambles and the arithmetic closes as an identity. Of the
**35.5 per cent** that job access and earning opportunities carry in the preferred
model:

| destination | female reference | male-reference sensitivity |
|---|---:|---:|
| to the preference share | $-4.0$ % | $-9.6$ to $-12.8$ % |
| to household endowments and needs | $+36.0$ to $+48.5$ % | $+42.3$ to $+54.2$ % |
| out of the measured total altogether | $+59.0$ to $+68.0$ % | $+58.6$ to $+67.3$ % |

*Ranges are across the raw and equivalized bases. The female-reference arm is
primary and the male-reference arm is the sensitivity; the two are never averaged.
A negative entry in the first row means the benchmark attributes* less *to
preferences than the preferred model does, not more.*

**The sentence this licenses, and its limit.** On the money-metric decomposition,
**omitting the opportunity object understates measured inequality and relabels
within the environment — moving market-side dispersion to the budget side and
dropping most of it from the total — rather than turning opportunity into taste.**
The misattribution to tastes is real, but it is on the **behavioural** side, in the
preference parameters themselves: the hours constants and the reversed sex gap
above. A conventional model of these data would not have reported a much larger
preference share of welfare inequality. It would have reported a *smaller total*,
a budget channel doing work the market channels should have done, and a sex
contrast in tastes pointing the wrong way.

That distinction matters for how this paper's contribution should be read. The
case for an opportunity object is not that it rescues a welfare decomposition from
attributing everything to taste — on this measure it does not. It is that without
one, the estimated preferences are wrong in an economically consequential
direction, the level of measured inequality is understated by a fifth to a
quarter, and the environment's internal composition is misdescribed.

**Figure 17** shows the two decompositions side by side. The benchmark's own
decomposition is internally exhaustive on the same test the preferred model passes,
so the comparison is between two complete accountings rather than between a
complete one and a residual.

---
---

## 7. The welfare decomposition

This is the core of the paper. Everything in it runs on the preferred singles
specification with the benchmark as the specification comparison, on the corrected
frame, on the common quadrature support, through the coalition-consistent
inversion, with **zero new tax–benefit pricing** — the priced-node cache was
tested for independence of the frame correction and reused, a test reported in
§7.7.

### 7.1 The four principal states

The four preference/environment cells, with their eight-scramble jackknife bands,
on the raw basis:

| model / reference | $I^{00}$ | $I^{10}$ | $I^{01}$ | $I^{11}$ |
|---|---:|---:|---:|---:|
| preferred, female reference (primary) | 0.134277 ± 0.001937 | 0.148316 ± 0.001534 | 0.030968 ± 0.000911 | $0.000\mathrm{e}{+}00$ |
| preferred, male structural zero | 0.134277 ± 0.001937 | 0.135998 ± 0.002341 | 0.030968 ± 0.000911 | $-2.035\mathrm{e}{-}31$ |
| benchmark, female reference | 0.139434 ± 0.002905 | 0.145693 ± 0.002747 | 0.015506 ± 0.000802 | $0.000\mathrm{e}{+}00$ |
| benchmark, male structural zero | 0.139434 ± 0.002905 | 0.140756 ± 0.003056 | 0.015506 ± 0.000802 | $0.000\mathrm{e}{+}00$ |

Baseline money-metric inequality among French single adults is a Gini of about
**0.134** under the preferred model. Equalising the environment alone takes it to
0.031 — under a quarter of where it started. Equalising both takes it to
numerical zero. **Exhaustiveness passes**, against a rule requiring
$|I^{11}| \le 0.00125$ and $\le 1$ per cent of $I^{00}$, and it passes at
numerical zero rather than inside the tolerance. Both accounting identities close
at machine precision in every arm. **Figure 11** shows the four
distributions and their Lorenz curves, raw and equivalized.

One feature is worth pausing on because it is counter-intuitive and it is real.
**Equalising preferences raises measured inequality**: $I^{10} > I^{00}$ in all
four arms. Giving every household the same tastes does not compress the
distribution of money-metric well-being; it widens it, because the households with
the worst opportunity sets are also the ones whose own tastes currently do most to
reconcile them to those sets. Since a contribution is defined as
$v(S) = I(\text{baseline}) - I(S)$ evaluated through the Owen rule, and the Owen
value's second term dominates, the *contribution* $C_{\mathrm{pref}}$ is nonetheless positive:
preference heterogeneity is inequality-reducing in the money metric.

**The movement from the pre-correction record is attributable to $\hat\theta$ and
to nothing else.** Each arm was also evaluated at the pre-correction parameter
vector on the same stems, support, operators and reference block, and both legs
reproduce the earlier numbers **bitwise** (maximum cell difference exactly
$0.000\mathrm{e}{+}00$). That is what licenses the attribution: everything but
$\hat\theta$ is held fixed and returns the old number exactly. The movement in
$I^{00}$ is $-0.016$ per cent on the preferred model and $-0.008$ per cent on the
benchmark.

### 7.2 The exact table

**Table 7.1 is the only source of percentages in this paper.** No percentage
appears anywhere in the text that is not read off it. Estimates are followed by
$\pm E_T$, the delete-one-scramble jackknife half-width at $t_{0.975,7}$. The
ratios and the sum are jackknifed **as whole quantities**, not composed from the
bands on their parts, for a reason given below.

*Symbols, once for both panels: $C_{\mathrm{pref}}$ is the preference
contribution, $C_{\mathrm{env}}$ the contribution of the complete non-preference
environment, and $C_{\mathrm{acc}}$, $C_{\mathrm{earn}}$, $C_{\mathrm{needs}}$
the nested contributions of job access, earning opportunities, and household
endowments and needs. $I^{00}$ is baseline inequality. Each is an Owen value:
the licensed reading is that equalising that channel across households removes
that share of baseline money-metric inequality.*

**Table 7.1a — Raw basis** (Gini points of $W^1$; ratios in per cent).

| model / reference | $I^{00}$ | $C_{\mathrm{pref}}$ | $C_{\mathrm{env}}$ | $C_{\mathrm{pref}}/I^{00}$ | $C_{\mathrm{env}}/I^{00}$ | $C_{\mathrm{acc}}$ | $C_{\mathrm{earn}}$ | $C_{\mathrm{needs}}$ | $C_{\mathrm{acc}}/I^{00}$ | $C_{\mathrm{earn}}/I^{00}$ | $C_{\mathrm{needs}}/I^{00}$ | $C_{\mathrm{acc}}{+}C_{\mathrm{earn}}$ | $(C_{\mathrm{acc}}{+}C_{\mathrm{earn}})/I^{00}$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| preferred, female | 0.134277 ± 0.001937 | 0.008464 ± 0.000914 | 0.125812 ± 0.001323 | 6.30 ± 0.61 | 93.70 ± 0.61 | 0.020004 ± 0.001290 | 0.027682 ± 0.002522 | 0.078126 ± 0.001457 | 14.90 ± 1.10 | 20.62 ± 1.63 | 58.18 ± 1.47 | 0.047687 ± 0.001772 | 35.51 ± 0.95 |
| preferred, male zero | 0.134277 ± 0.001937 | 0.014623 ± 0.000708 | 0.119653 ± 0.001762 | 10.89 ± 0.48 | 89.11 ± 0.48 | 0.018227 ± 0.001194 | 0.029947 ± 0.003024 | 0.071478 ± 0.001467 | 13.57 ± 1.01 | 22.30 ± 1.97 | 53.23 ± 1.52 | 0.048175 ± 0.002330 | 35.88 ± 1.28 |
| benchmark, female | 0.139434 ± 0.002905 | 0.004624 ± 0.000641 | 0.134810 ± 0.002497 | 3.32 ± 0.41 | 96.68 ± 0.41 | 0.016626 ± 0.002147 | 0.031876 ± 0.003606 | 0.086308 ± 0.002378 | 11.92 ± 1.68 | 22.86 ± 2.23 | 61.90 ± 1.79 | 0.048502 ± 0.002618 | 34.79 ± 1.50 |
| benchmark, male zero | 0.139434 ± 0.002905 | 0.007092 ± 0.000533 | 0.132342 ± 0.002683 | 5.09 ± 0.34 | 94.91 ± 0.34 | 0.016551 ± 0.002064 | 0.032818 ± 0.003903 | 0.082973 ± 0.002332 | 11.87 ± 1.62 | 23.54 ± 2.42 | 59.51 ± 1.86 | 0.049369 ± 0.002920 | 35.41 ± 1.63 |

**Table 7.1b — Coalition-consistent equivalized basis.**

| model / reference | $I^{00}$ | $C_{\mathrm{pref}}$ | $C_{\mathrm{env}}$ | $C_{\mathrm{pref}}/I^{00}$ | $C_{\mathrm{env}}/I^{00}$ | $C_{\mathrm{acc}}$ | $C_{\mathrm{earn}}$ | $C_{\mathrm{needs}}$ | $C_{\mathrm{acc}}/I^{00}$ | $C_{\mathrm{earn}}/I^{00}$ | $C_{\mathrm{needs}}/I^{00}$ | $C_{\mathrm{acc}}{+}C_{\mathrm{earn}}$ | $(C_{\mathrm{acc}}{+}C_{\mathrm{earn}})/I^{00}$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| preferred, female | 0.165105 ± 0.002014 | 0.013179 ± 0.000832 | 0.151926 ± 0.001271 | 7.98 ± 0.41 | 92.02 ± 0.41 | 0.015982 ± 0.001003 | 0.026814 ± 0.002377 | 0.109131 ± 0.001024 | 9.68 ± 0.68 | 16.24 ± 1.25 | 66.10 ± 1.23 | 0.042796 ± 0.001872 | 25.92 ± 0.85 |
| preferred, male zero | 0.165105 ± 0.002014 | 0.018117 ± 0.000649 | 0.146989 ± 0.001629 | 10.97 ± 0.31 | 89.03 ± 0.31 | 0.014263 ± 0.000889 | 0.028813 ± 0.002834 | 0.103913 ± 0.001086 | 8.64 ± 0.60 | 17.45 ± 1.51 | 62.94 ± 1.30 | 0.043075 ± 0.002375 | 26.09 ± 1.13 |
| benchmark, female | 0.166462 ± 0.002933 | 0.007075 ± 0.000609 | 0.159387 ± 0.002411 | 4.25 ± 0.30 | 95.75 ± 0.30 | 0.013523 ± 0.001635 | 0.031210 ± 0.003464 | 0.114654 ± 0.001711 | 8.12 ± 1.07 | 18.75 ± 1.78 | 68.88 ± 1.53 | 0.044733 ± 0.002726 | 26.87 ± 1.27 |
| benchmark, male zero | 0.166462 ± 0.002933 | 0.009067 ± 0.000556 | 0.157395 ± 0.002566 | 5.45 ± 0.27 | 94.55 ± 0.27 | 0.013401 ± 0.001560 | 0.032034 ± 0.003743 | 0.111960 ± 0.001683 | 8.05 ± 1.02 | 19.24 ± 1.93 | 67.26 ± 1.61 | 0.045435 ± 0.003020 | 27.29 ± 1.41 |

Both accounting identities — $C_{\mathrm{pref}} + C_{\mathrm{env}} = I^{00} - I^{11}$ and
$C_{\mathrm{acc}} + C_{\mathrm{earn}} + C_{\mathrm{needs}} = C_{\mathrm{env}}$ — hold at machine precision on all eight rows, and the
nested order is endowments and needs above earning opportunities above job access
in every one. **Figure 12** plots $C_{\mathrm{pref}}$ and
$C_{\mathrm{env}}$ as signed bars with their bands under both reference conventions and both
models; **Figure 13** does the same for the nested split.

**One number in the table should be read twice.** On the preferred model, female
reference, raw basis, the band on the market-side total
$C_{\mathrm{acc}} + C_{\mathrm{earn}}$ is
$\pm 0.95$ percentage points — *narrower* than the band on $C_{\mathrm{acc}}$ alone ($\pm 1.10$)
or on $C_{\mathrm{earn}}$ alone ($\pm 1.63$). Across integration scrambles job access and
earning opportunities move *against* each other, so adding the marginal bands
would have overstated the band on the market total by about a factor of three.
That is the concrete reason every sum and ratio in Table 7.1 is jackknifed as a
whole quantity: a band on a ratio is not a function of the bands on its numerator
and denominator when the two move together. Recovering the eight
leave-one-scramble-out replicates required to do this cost twenty-one minutes of
compute and is what makes the ratio bands honest.

### 7.3 Interpretation discipline

The following sentence is generated mechanically from Table 7.1 by the script that
writes the table, with a guard: if the nested order were not endowments and needs
above earning opportunities above job access in all eight rows, the script prints
a refusal instead of the sentence. It printed the sentence.

> **Within the currently modelled non-preference environment, budget-side
> endowments and needs are the largest nested contribution under both positive
> models and both reference-preference conventions.** On the final singles
> model with the female reference, equalising the whole non-preference environment
> removes 93.7 per cent of baseline money-metric inequality (±0.6) and equalising
> preferences a further 6.3 per cent (±0.6); inside the environment, endowments
> and needs carry 58.2 per cent (±1.5), earning opportunities 20.6 (±1.6) and job
> access 14.9 (±1.1), so that job access and earning opportunities together — the
> two channels that are about the market rather than the budget — carry 35.5 per
> cent (±0.9). Across all eight rows of the table the environment share runs 89.0
> to 96.7 per cent, the preference share 3.3 to 11.0 per cent with a constant
> sign, the endowments-and-needs share 53.2 to 68.9 per cent, and the nested
> order is endowments and needs above earning opportunities above job access in
> every one.

The interpretation discipline that travels with it is quoted from the record, and
its four qualifiers are not optional:

> The four qualifiers travel with it and are not optional: structural and
> model-conditional; not causal; provisional pending the bounded economics
> review; and **not** a statement that job opportunities are unimportant. The
> standing access sentence travels with the access channel — the present access
> density may combine personal capability and market availability, and does not
> yet separately identify the ability set from the opportunity set. No ordering
> between job access and earning opportunities is claimed in either direction.

Four consequences for how this paper may be read, stated once here and observed
throughout.

1. **No channel "explains" a percentage.** The licensed form is: *equalising
   channel $X$ across households removes $Y$ per cent of baseline money-metric
   inequality*. A contribution is the value of an equalisation operator in a
   cooperative game, not a variance share and not a causal effect.
2. **The bands are integration precision.** They say how well the integral is
   resolved on the basis it was computed on. They are not sampling confidence
   intervals, and sampling uncertainty of $\hat\theta$ propagated to these
   functionals is not estimated in this paper. The phrase *statistically
   indistinguishable from zero* is not used anywhere, because nothing here
   licenses it.
3. **No ordering is claimed between job access and earning opportunities.**
   The point estimates order them
   in every row, and the numbers are printed. But the access channel is exactly the
   one that does not yet separate the ability set from the opportunity set, so an
   ordering claim would be a claim about an object the design does not identify.
   The design does not identify that ordering, so no ranking is claimed.
4. **The two reference conventions are reported as a range and never averaged.**

### 7.4 Raw against equivalized

| object (preferred model, female reference) | raw | equivalized | change |
|---|---:|---:|---|
| $I^{00}$ | 0.134277 | **0.165105** | $+22.96\%$ |
| $C_{\mathrm{pref}}$ | $+0.008464$ | $+0.013179$ | |
| $C_{\mathrm{env}}$ | $+0.125812$ | $+0.151926$ | |
| $C_{\mathrm{pref}}/I^{00}$ | 6.30 % | 7.98 % | |
| job access / earning opportunities / endowments and needs | 0.0200 / 0.0277 / 0.0781 | 0.0160 / 0.0268 / 0.1091 | same order on both |
| mean $W^1$ | €1,384.1 / month | €1,265.7 / month | |

Equivalizing raises measured inequality by roughly a fifth and raises both
contributions, but **changes no qualitative conclusion**: the reference-sensitivity
classification, the sign of the preference contribution, the dominance of the
environment and the nested order are identical on both bases in all four arms. $I^{01}$ and
$I^{11}$ are numerically identical across the two bases by construction, because
those states already equalise endowments and needs — which is the
coalition-consistent equivalization
of §3.5 doing exactly what it is supposed to do.

What *does* move materially between the bases is the market-side total: 35.5 per
cent raw against 25.9 per cent equivalized on the preferred model with the female
reference. Equivalization loads more of the measured dispersion onto the
endowments-and-needs channel, which is unsurprising, since the scale is itself a
composition object and composition is an endowments-and-needs argument. Both figures are on
Table 7.1 and both are reported; neither is "the" answer.

**The calibration identity holds.** The ratified constraint — that a household at
its type-specific reference with disposable income $e_i \cdot m$ must have
equivalized welfare $m$ — was evaluated at $e \in \{1, 750, 1500, 3000\}$ and holds
to $4.4\times10^{-13}$, beside the accepted raw reference-recovery leg at
$3.5\times10^{-10}$ euros.

### 7.5 Reference sensitivity, reported as a range

The money-metric measure evaluates each household at a *reference preference
block*, and the singles module carries two ratified blocks: the female block as
primary, and the male block, completed on the union of preference terms with a
**structural zero** on the children-in-leisure term, as the sensitivity. The
structural zero is not a modelling convenience: the specification contains a
children-in-leisure coefficient for single women and **no male counterpart at
all**, so the male reference block cannot carry one, and setting it to zero is the
only completion the specification implies. Appendix B records how this was found —
by measurement, when the common support drove the female arms' residual to
numerical zero and left the male arms' at $1.1\times10^{-3}$.

The classification is **reference-sensitive in magnitude**: the
sign of the preference contribution, the dominance of the environment and the
nested order are identical under both references, and the *magnitude* of the
preference contribution differs by more than the integration bands.

| model | $C_{\mathrm{pref}}/I^{00}$, female → male | $C_{\mathrm{env}}/I^{00}$, female → male | $(C_{\mathrm{acc}}{+}C_{\mathrm{earn}})/I^{00}$ |
|---|---|---|---|
| preferred, raw | 6.30 % → 10.89 % | 93.70 % → 89.11 % | 35.51 % → 35.88 % |
| preferred, equivalized | 7.98 % → 10.97 % | 92.02 % → 89.03 % | 25.92 % → 26.09 % |
| benchmark, raw | 3.32 % → 5.09 % | 96.68 % → 94.91 % | 34.79 % → 35.41 % |
| benchmark, equivalized | 4.25 % → 5.45 % | 95.75 % → 94.55 % | 26.87 % → 27.29 % |

**Results are reported as the female-primary value, the male-sensitivity value,
and their range. They are never averaged.** The reason a range is the honest
object rather than a robustness check is that the difference between the two
blocks is genuinely economic and not an artefact of the child term: a shared-child
diagnostic attributes only **3.7 per cent** (preferred model) and **7.3 per cent**
(benchmark) of the female–male gap to the children-in-leisure term, and the
remainder comes from coefficients that genuinely differ between the two ratified
blocks. Note also that the market-side total is essentially *insensitive* to the
reference choice — 35.5 against 35.9 raw — so the sensitivity is concentrated in
the preference/environment split rather than in the environment's internal
structure.

That pattern is not confined to the reference convention. §5.5 perturbs a box on a
preference curvature and moves the same quantity by about 13 per cent while
leaving every other headline quantity inside its band; §8.4 pins the couples male
leisure block and moves the same quantity by up to 73 per cent while the
environment side moves by under 3.5 per cent. **The preference/environment split
is the fragile margin of this decomposition; the environment's internal structure
is the robust one.**

### 7.6 Draw stability of the welfare objects

§5.3 showed the positive model is stable in the draw count. That does not settle
the welfare objects, which are non-linear functionals of $\hat\theta$ through a
money-metric inversion. The question is answered separately at
$R \in \{50,100,200,400\}$ on the §5.3 parameter vectors, with **only
$\hat\theta$ varying** — the welfare basis, support, operators, inversion and
jackknife are the same objects at every rung, so the ladder isolates the
propagation of estimation-draw noise into the decomposition. The ladder is
anchored: the $R=100$ rung and the reported optimum agree to
$1.4\times10^{-9}$ in coordinates and reproduce the headline to every printed
digit. **Figure 10** is the picture.

| quantity (preferred model, female reference) | $R=50$ | $R=100$ | $R=200$ | $R=400$ | range / largest band |
|---|---:|---:|---:|---:|---:|
| $I^{00}$ | 0.133476 | 0.134277 | 0.134692 | 0.134561 | 0.59 |
| $C_{\mathrm{pref}}$ | 0.008164 | 0.008464 | 0.008765 | 0.008719 | 0.64 |
| $C_{\mathrm{env}}$ | 0.125313 | 0.125812 | 0.125926 | 0.125841 | 0.44 |
| $C_{\mathrm{acc}}$ | 0.019793 | 0.020004 | 0.020221 | 0.020210 | 0.33 |
| $C_{\mathrm{earn}}$ | 0.027023 | 0.027682 | 0.027615 | 0.027567 | 0.25 |
| $C_{\mathrm{needs}}$ | 0.078497 | 0.078126 | 0.078090 | 0.078064 | 0.30 |

Every sign is constant over $R$ and the nested order is unchanged at every rung
in every arm, raw and equivalized. **One exception is stated rather than
smoothed.** In the male structural-zero arm, $C_{\mathrm{pref}}$ moves from 0.014096 to 0.015030
over $R = 50 \to 400$ — a range of $1.019\times10^{-3}$ against its own jackknife
band of $7.08\times10^{-4}$, so range over band is 1.44, the only object in the
ladder that exceeds its band. It is also the object with the tightest band in the
study, so the exceedance is as much about the band as about the movement, and the
direction is monotone up to $R=200$ and flat thereafter. It touches no qualitative
conclusion — sign, environment dominance and the nested order are unchanged at
every rung — but it means **the male-reference preference contribution should not
be quoted to more than two significant figures**, and the $R=400$ value is the one
to prefer if a single number is wanted.

### 7.7 What the welfare layer cost, and what was checked

**Zero tax–benefit pricing calls.** The final welfare runs on the priced-node
cache built on the pre-correction frame, and reusing it required a test. The
literal test — hash the household budget-input vectors on both frames and require
bitwise equality for all 1,555 — **fails**, and it is reported failing: seven of
2,236 person rows differ, in exactly one column, `lhw`. That failure is not the
answer, because `lhw` is not a pricing input: the production earnings policy
*writes* `lhw` onto every decider of every priced alternative before the record
reaches the tax–benefit engine. It is a slot the node fills, not a number the
frame supplies. With the policy-written columns removed the check is bitwise equal
for all 1,555 households, and the argument was then *measured* rather than
asserted: the engine input frame actually assembled from both frames' templates,
at full slot coverage on all seven affected households (11,480 input rows), is
**bitwise identical**, while the template it was built from differs in `lhw` on
140 of those rows. **Verdict: pass. The cache is reused and the final welfare
costs no new pricing call.**

One disclosure the cache check does not cover, recorded so that it is a disclosed
choice rather than an oversight: the assembled welfare stem carries a per-household
anchor row and a panel-level consumption scale over all rows. The anchor is
excluded from every welfare object by construction, so it reaches the numbers only
through that scale, which shifts by $-1.402\times10^{-4}$ euros on 1774.5182 — a
relative $7.9\times10^{-8}$, four orders of magnitude below the integration bands.
The refresh is not taken.

Every arm passes the full check battery: the integration identity computed two
ways agrees exactly before any log or inversion consumes it; the exact proposal
density is finite on all 3,184,640 stochastic rows; reference recovery is
$3.5\times10^{-10}$ euros; the inversion is monotone for every household; the
complete reference vector reaches every household, with the utility range exactly
zero at the fully common state; and both accounting identities close at machine
precision.

**Two items remain open and are reported rather than reconciled.** The model's
child-count variable agrees with the under-14 count in 1,357 of 1,555 households
(87 per cent) — it is a preference argument and a needs argument under different
age cuts, and the two move under different channels. And no synthetic recovery
synthetic-recovery diagnostic at production scale has ever been run on the preferred singles specification
itself; the recovery evidence in this paper is on the couples module (§8.2).

### 7.8 What the decomposition looks like at the household level

A decomposition of an inequality index is a population statement, and it is worth
seeing what the mechanism looks like on two actual households. Figures 14 and 15
 are constructed by an explicit rule, applied before any
household was looked at.

**The rule.** A household's *preference profile* is
$p_i(h) = \omega_i \cdot \mathcal{B}\big((\bar L - h)/\lambda_\ell;\theta_\ell(g_i)\big)$,
with $\omega_i$ the leisure weight at the household's own age, age-squared and
(women only) child shifters — exactly the block the preference channel equalises. The
consumption side carries no cross-household variation at all, since the
consumption coefficient is the numeraire and the curvature is common, so it is not
part of the profile. A household's *opportunity profile* is the normalised offer
density over employment, hours, occupation and wage. Distance between preference
profiles is the scale-free sup-norm between the two leisure-utility curves;
distance between opportunity profiles is the **total-variation distance** between
the two offer densities, in $[0,1]$, computed in closed form — the common hours
factor integrates out exactly, and two log-normals with a shared dispersion cross
at most once in the log wage, so each occupation's $L^1$ integral is a two-piece
sum of Gaussian CDFs. No quadrature and no grid error.

Admissible pairs share the observed employment state and, if employed, the
observed occupation, the observed hours band on the model's own partition, and the
observed wage quintile. The constraint is applied inside the employed and the
non-employed strata and never across them, because "the same observed job"
presupposes a job; the paper uses the employed stratum, 19,116 admissible pairs.
The **forward** search takes pairs at or below the 10th percentile of preference
distance and maximises opportunity distance; the **reverse** search mirrors it.
Cleanliness requires the top pair to sit inside the similarity cut on the
constrained axis *and* to separate by at least 1.5 times the admissible median on
the maximised axis.

**The forward pair** — preference distance 0.038 against an admissible median of
0.783; opportunity distance 0.442 against 0.213, a separation of 2.08×, clean,
and same-sex:

- **A** — a man aged 50–54, high education, two children, intermediate
  urbanisation; observed employed in occupation 1 at 40 hours and €10.02 an hour.
  Estimated leisure weight 6.425, employment probability 0.874, median wage offer
  €13.93.
- **B** — a man aged 25–29, medium education, no children, intermediate
  urbanisation; observed employed in occupation 1 at 40 hours and €3.12 an hour.
  Estimated leisure weight 6.335, employment probability 0.702, median wage offer
  €8.80.

Two single men, both working 40 hours in the same occupation in the bottom wage
quintile, whom the model gives essentially the same preference profile and very
different opportunity: an employment probability of 0.874 against 0.702, and a
median wage offer of €13.93 against €8.80. That is panel (A) of Figure T1, on real
estimates.

**The reverse pair** — preference distance 3.466, a separation of 4.42×;
opportunity distance 0.034, clean, same-sex:

- **A** — a woman aged 35–39, medium education, no children, intermediate
  urbanisation; observed employed in occupation 1 at 24 hours and €21.75 an hour.
  Leisure weight 4.708, employment probability 0.899, median wage offer €10.16.
- **B** — a woman aged 45–49, medium education, five children, urban; observed
  employed in occupation 1 at 16 hours and €20.16 an hour. Leisure weight 10.264,
  employment probability 0.866, median wage offer €10.26.

Two single women with near-identical offer distributions and leisure weights of
4.71 against 10.26, who work 24 and 16 hours. That is panel (B).

Both top pairs are same-sex, so neither finding rests on the sex contrast in the
occupation-availability weights; the same-sex-restricted reverse ranking gives a
preference distance of 2.935. Reported and *not* used: in the non-employed stratum
the forward search reaches a preference distance of exactly **0.000** with an
opportunity distance of 0.540 — two households with literally identical estimated
preference profiles — but there is no observed job there, so it is not the paper's
figure.

**A second disclosure, found while building the regional illustration of §7.9 and
recorded rather than quietly fixed.** The stored profile artefact these two figures
are drawn from computes its market-access index from region columns that are
identically zero on this frame, rather than from the region indicators the
estimator and the welfare engine both evaluate. The gap is exactly each household's
own region coefficient, at machine precision. **The consequence is confined to
these two figures**: the participation numbers plotted here, and the
opportunity-distance measure that ranks the candidate pairs, are region-free. The
estimation, the welfare decomposition, the exact table and the geographic split of
§7.9 all go through the loader that rebuilds the indicators and are unaffected —
§7.9's own illustration uses the live indicators throughout. A repair has been
specified and has not yet passed its own proof, so **the pair shown here is the one
the region-free ranking selected and has not been re-selected**. Re-selection could
move the pair; it would not change any number in §7.
Since the ranking omits a term that varies across households, the pair below is
best read as *a* clean instance of the mechanism rather than as the extremal one.

**One structural disclosure travels with these figures.** Under the preferred
specification the hours-band index carries **no household-specific coordinate**.
Household variation in the offer density therefore lives in exactly three places —
the participation margin, the sex-specific occupation-availability weights, and the
wage-offer location — and nowhere else. The hours *marginal* still differs across
households, but only through the participation margin. The figures say this on
their face rather than letting a reader infer a household-specific hours
technology the model does not have. No identifier is written or plotted;
households are described by aggregates only.

### 7.9 Inside job access: the geographic split

The job-access channel can be split once more, into the part carried by **where a
household lives** and the part carried by everything else the access operator
owns. The split is a nesting of the accepted decomposition rather than a new one:
levels one and two are bitwise unchanged — all 44 numbers of §7.2 reproduce
exactly — and the two sub-players partition the access operator's own argument
slots, so equalising both reproduces the access operator bitwise. That is asserted
as an identity and measured, not assumed, and it holds to $0.0$ on every row.

**The two sub-players.** *Geographic / local-market access* owns the eight NUTS-1
region indicators, the urbanisation indicators, and the local unemployment rate at
the household's own region, education and sex. *Other access* owns everything
else: the occupation-availability conditional — which this specification conditions
on **sex alone** — and two survey-year indicators that are identically zero on a
single-year sample and are therefore numerically inert. Every substituted indicator
is replaced by its population share and the unemployment rate by its sample mean;
nothing is re-estimated and no coefficient is re-fitted.

**Table 7.2 — the split, at the female reference.**

| basis | job access | geographic access | other access | geographic, as a share of job access | geographic, as a share of $I^{00}$ |
|---|---:|---:|---:|---:|---:|
| raw | 0.020004 ± 0.001290 | **0.017528 ± 0.000887** | 0.002476 ± 0.000891 | **87.62 % ± 3.89** | **13.05 % ± 0.74** |
| equivalized | 0.015982 ± 0.001003 | **0.016289 ± 0.000831** | $-0.000307$ ± 0.000489 | **101.92 % ± 3.11** | **9.87 % ± 0.55** |

*Bands are the eight-scramble jackknife; ratios are jackknifed as whole quantities.
The male-reference sensitivity gives 90.13 % ± 4.16 and 105.71 % ± 3.33 for the
share of job access, and 12.24 % ± 0.65 and 9.13 % ± 0.47 for the share of $I^{00}$;
the two references are reported as a range and never averaged.*

The reading, generated from the table:

> **Within job access, the geographic terms carry essentially the whole channel.**
> On the final singles model with the female reference, equalising the geographic
> access environment removes 13.05 per cent (±0.74) of baseline money-metric
> inequality on the raw basis and 9.87 per cent (±0.55) on the equivalized basis,
> against a whole job-access channel of 14.90 per cent (±1.10) and 9.68 per cent
> (±0.68). Geography is therefore 87.6 per cent (±3.9) of the job-access channel
> raw and 101.9 per cent (±3.1) equivalized. Across all four rows the geographic
> share of job access runs 87.6 to 105.7 per cent, and the geographic share of
> total measured inequality 9.13 to 13.05 per cent.

**The residual is near zero and changes sign with the basis.** Other access runs
$-0.49$ to $+1.84$ per cent of baseline inequality across the four rows. Shares
here are **signed and never renormalised**, which is why the geographic share
exceeds 100 per cent on the equivalized rows: the residual there is *negative, not
missing*. A share above one says that equalising the other sub-player, in the
presence of the remaining equalisations, does not on average reduce measured
inequality.

**Why this is the shape the specification implies, and what it does not license.**
The two sub-players do not have comparable support, and the asymmetry is
structural rather than a finding about the world. The geographic block varies
household by household over eight regions, three urbanisation categories and a
region × education × sex unemployment rate. The remaining access block is the
occupation-availability conditional, whose access-assigned argument is **sex alone
— a two-cell table** — plus year indicators that are identically zero here. Almost
all of the between-household dispersion the access operator *can* remove is
therefore geographic **by construction of the estimated access block**. The correct
reading is about the composition of that block, not about the importance of place
in general.

In particular this is **not** a finding that region drives welfare inequality. Job
access as a whole carries 14.9 per cent of measured inequality on the raw basis and
9.7 per cent equivalized, against 58.2 and 66.1 per cent for endowments and needs.
The qualifiers of §7.3 travel unchanged: structural and model-conditional, not
causal, provisional pending the bounded economics review, and a statement about the
**currently modelled** geographic access block — region, urbanisation and the local
unemployment rate — not about geography in general. Region-dependent *budget* rules
are deliberately outside it: the only regional dependence in the tax–benefit system
here is the housing-allowance zone, which belongs to endowments and needs.

**The same-profile, different-region illustration.** **Figure 19** takes the two
real households of §7.8 and evaluates each under all 24 documented region ×
urbanisation access environments, with the local unemployment rate at that region's
value for the person's own education and sex. Preferences, sex, age, education,
experience, household composition, earning-capacity characteristics and the priced
budget are all held at their observed values, and the region-dependent budget rule
is held fixed too, so this is an **access counterfactual and no price is
recomputed**. The older man's employment-opportunity mass runs 0.768 to 0.858 across
environments and his money-metric welfare €1,736 to €1,837, a ratio of 1.058; the
younger man's runs 0.655 to 0.809 and €1,301 to €1,333, a ratio of 1.025.

One structural fact makes the picture cleaner than it might have been: because
every geographic variable in this specification enters only when the household
works, a purely
geographic counterfactual moves the **employment margin and nothing else**. Over
all 48 profile-by-environment cells the wage-offer location, the four occupation
shares and the hours normalising constant each take exactly one value per profile —
measured, not assumed. The whole regional difference is on the participation margin.

**This is not a causal region effect.** It is a model-implied comparison of the same
person under different estimated access environments, and it is labelled as such on
the figure itself. Nothing here identifies what would happen to a person who moved.

---

---

## 8. Couples

The couples module is a **parallel module**, presented as an extension of the
positive model and as a sensitivity-bounded companion on the welfare side. It is
not promoted to the headline, for a reason given in §8.4 that was fixed before the
arms were run. No couples number is compared to a singles number except where the
cross-type conditions of §8.5 have been evaluated and passed.

### 8.1 The specification and the frame

2,275 opposite-sex couple households, each with 101 joint alternatives, on the
corrected re-priced frame of §4.4. The specification is the singles architecture
transposed, with **one specification and no search**: hours opportunity **per
spouse** (five bands plus the 35-hour peak, with the employment level split
alongside them), occupation availability **sex-specific**, a wage block with
**common** education and experience slopes and **common** dispersion plus the
occupation location shifts, and access over the group-specific unemployment rate,
region and urbanisation. **46 free coordinates**, 12 pinned inert. Three absences are
recorded with reasons rather than left implicit: the household leisure-interaction
term (absent from the certified base and not identified on this frame), a couples
consumption curvature (log consumption by the certified convention), and a
male children-in-leisure term (children on the female leisure only — the singles
structural-zero convention).

Estimation follows the certified protocol and returns `SINGLE-OPTIMUM`: objective
**43,493.342239**, spread $1.353\times10^{-9}$ across ten polished points with
identical active-bound sets, interior Hessian minimum eigenvalue $+0.1105$, one
active bound, and a household-clustered CR1 sandwich at $G = 2{,}275$ and
$K_{\text{interior}} = 45$. The objective is **not comparable** to the singles
figure: a different frame and a different choice set.

### 8.2 Recovery, and the named weakness

Two synthetic-recovery diagnostics were run at ten replications each, both with
zero unrecovered coordinates, so no coordinate was fixed.

| diagnostic | simulated share with both spouses working | recovered | marginal | not recovered |
|---|---|---:|---:|---:|
| at the design point | 23.0 % (data: 85.3 %) | 42 | 4 | 0 |
| **at the fitted point — governs** | **82.9 %** | 38 | 8 | 0 |

The design-point diagnostic speaks only to where the design point sits; the
fitted-point diagnostic reproduces the data, so it is the one that governs.
**Synthetic-recovery diagnostics identify the male leisure block as weakly
recovered at the fitted point**, and the welfare sensitivity associated with that
block is therefore reported explicitly in §8.4: three of its four coordinates are
marginally recovered at the fitted
point — the intercept at 0.78 replication standard errors, the curvature at 0.85,
the age-squared term at 0.65 — though all four are RECOVERED at the design point.
This weakness is carried *with* the results, not around them, and §8.4 is where it
bites.

A pre-registration error was found and corrected in the process, and both rules
are kept on the record. The original recovery rule required
$\mathrm{mean}|{\rm bias}|/\mathrm{SE} \le 0.5$; that statistic is the mean
absolute $z$, whose null expectation is $\mathbb{E}|N(0,1)| = 0.798$, so it was a
test no unbiased estimator could pass. The corrected rule separates systematic
bias ($|\mathrm{mean\ bias}|/\mathrm{mean\ SE}$, null 0) from dispersion
($\mathrm{mean}|z|$, null 0.798). The observed median $\mathrm{mean}|z|$ is 0.773.

### 8.3 Fit, and the 35-hour peak per spouse

| object | male | female |
|---|---:|---:|
| employment rate, observed | 0.9266 | 0.9046 |
| employment rate, predicted | 0.9266 | 0.9046 |
| hours-grid share, mean absolute error | 0.0072 | 0.0096 |
| mean log wage, absolute error | 0.0576 | 0.0501 |
| log-wage dispersion, observed / predicted | 0.432 / 0.423 | 0.434 / 0.433 |
| occupation shares | matched to $10^{-8}$ | matched to $10^{-8}$ |

The joint participation quadrants — neither working, male only, female only, both
working — are observed at 2.20 / 7.34 / 5.14 / 85.32 per cent and predicted at
0.54 / 9.00 / 6.80 / 83.66, with a hard-assignment accuracy of 0.824. The one
visible weakness is the neither-working corner, which the model under-predicts by
a factor of four on a base of 2.2 per cent.

**The 35-hour peak, estimated separately per spouse, against the singles value of
2.5795:**

| | estimate | s.e. | $z$ | difference vs singles |
|---|---:|---:|---:|---:|
| female | **2.5474** | 0.0735 | 34.66 | $-0.032$ |
| male | **3.2915** | 0.1022 | 32.20 | $+0.712$ |

The female peak in couples reproduces the singles value to within three
hundredths — one third of a standard error — on a different frame, a different
choice set, and a joint likelihood. The male peak is substantially larger. Both
are estimated with $z$ statistics above 32. This is the most striking piece of
external consistency in the paper's positive layer, and it was not targeted.

**Rank, top-$k$ and Brier statistics are structurally degenerate here too, and
this is not a couples defect.** The chosen-rank median is 101 of 101, the top-$k$
rates are zero, and the preferred singles model shows the identical pattern. The
mechanism is the one in §6.2, and it is a property of the estimator's choice-set
construction rather than of either module.

### 8.4 Couples welfare, and why it is a companion rather than a headline

The couples welfare layer runs on its own common quadrature support — 2,048 joint
nodes built so that the population marginal is taken over the **joint** per-spouse
base component rather than spouse by spouse, because the product of two separate
per-spouse marginals is not the marginal of the product and would lose the
domination property that bounds the importance weights. Appendix C gives the
construction and its checks.

Couples have **no reference-group arm**, and this is structural rather than a
simplification. The singles decomposition needs a female/male pair because the two
singles groups carry *separate* preference blocks and a single household has one
sex. A couple has both at once, and the couples specification estimates **one**
shared preference vector with per-sex coordinates, so the reference block is that
vector at the couples-medoid arguments and there is nothing to average.

**The four principal states, with the carrier measure:**

| basis | $I^{0000}$ | $I^{1000}$ | $I^{0111}$ | $I^{1111}$ |
|---|---:|---:|---:|---:|
| raw | 0.144739 | 0.139613 | 0.009467 | $-2.965\mathrm{e}{-}30$ |
| equivalized | 0.141547 | 0.140573 | 0.009467 | $-2.835\mathrm{e}{-}30$ |

**Exhaustiveness holds for couples too**: the fully common state returns a
*constant* welfare vector — range exactly $0.0$ across all 2,275 households at
€1,713.16 a month — and both accounting identities close at exactly $0.0$. The
exhaustiveness audit is derived from the specification's own shifter lists rather
than transcribed: 23 household-varying arguments, every one assigned to exactly
one channel (11 to job access, 6 to earning opportunities, 5 to preferences,
1 to endowments and needs), none unassigned.

**The decomposition:**

| basis | $C_{\mathrm{pref}}$ | $C_{\mathrm{env}}$ | $C_{\mathrm{pref}}/I^{0000}$ | $C_{\mathrm{acc}}$ | $C_{\mathrm{earn}}$ | $C_{\mathrm{needs}}$ | order |
|---|---:|---:|---:|---:|---:|---:|---|
| raw | $+0.007296$ [0.006863, 0.007730] | $+0.137442$ [0.136339, 0.138546] | 5.04 % | 0.019562 | 0.045898 | **0.071982** | needs > earning opp. > access |
| equivalized | $+0.005220$ [0.004897, 0.005544] | $+0.136327$ [0.135100, 0.137554] | 3.69 % | 0.017816 | 0.040767 | **0.077743** | needs > earning opp. > access |

Levels: raw mean €1,836.8 and median €1,761.8 a month; equivalized mean €972.7 and
median €921.5. **The same nested order the singles module found, on both bases**, and
the same environment dominance. **Figures C1–C3** (Appendix D) carry the
distributions, the decomposition and the singles/couples comparison.

**A directional difference from singles, stated plainly.** For couples
$I^{1000} < I^{0000}$ on both bases: equalising preferences *reduces* measured
inequality. For singles the record has the opposite. Both sides nonetheless have a
positive preference contribution, because the Owen value's second term dominates
on the singles side. The singles interpretation of §7.1 therefore does **not**
transfer to couples and is not repeated here.

**The disposition: the male-leisure sensitivity is material.** Seven pinned refits
of the remaining 45 coordinates, all converged, move each MARGINAL male-leisure
coordinate to both ends of its recovery band. The band is deliberately
**conservative**: it is the design point plus or minus the diagnostic's mean
replication standard error, and all seven arms fall *outside* the couples
likelihood's own 95 per cent region for the pinned coordinate — the smallest
likelihood-ratio statistic among them is 4.17 against a chi-square(1) critical
value of 3.84 — so these are larger movements than the data alone would license.

The verdict is **material**, on 29 of 140 comparisons, and the structure matters
more than the count. Every flag is an out-of-band flag; not one is a sign change
and not one is an ordering change.

| quantity | worst relative move | material |
|---|---:|---|
| $C_{\mathrm{pref}}$ | **73.1 %** | yes |
| $C_{\mathrm{acc}}$ | 8.5 % | yes |
| $C_{\mathrm{needs}}$ / $C_{\mathrm{env}}$ | 3.4 % / 3.4 % | yes |
| $C_{\mathrm{earn}}$ | 1.2 % | no |
| $I^{0000}$ | 0.85 % | yes |
| mean / median welfare | 0.18 % / 0.26 % | no |

**The sensitivity is concentrated in the preference contribution**, which ranges
from 0.0014 to 0.0075 on the equivalized basis around a baseline of 0.0052 — a
five-fold spread — and that is precisely the channel that leans on the male
leisure block the recovery diagnostics identified as weakly recovered. The environment side moves
by under 3.5 per cent and the headline inequality by under 1 per cent, and they
leave their bands only because the bands are very tight. Sign, the nested order
and the levels are unchanged in every arm. **Figure C5** plots the
sensitivity.

By the rule fixed in advance, this makes **singles the quantitative welfare
headline**. The couples environment decomposition is the robust part of the couples
result and can be quoted with its own bands; **every couples preference-contribution
figure travels with the 0.0014–0.0075 range**.

### 8.5 Pooling: inequality yes, decomposition no

All four ratified cross-type conditions hold — the same real-euro year, the same
consumption numeraire, a common zero/origin convention, and the calibration
identity at a maximum absolute error of $1.11\times10^{-14}$ over
$e \in \{1,750,1500,3000\}$ and both measures — so the halt on cross-type
aggregation does **not** fire and pooling is licensed.

**Pooled, equivalized only** (2,275 couples and 1,555 singles; weighted shares
54.0 per cent couple, 46.0 per cent single):

| state | pooled | singles | couples |
|---|---:|---:|---:|
| $I^{0000}$ | **0.173235** | 0.165105 | 0.141547 |
| $I^{1000}$ | 0.166195 | 0.169716 | 0.140573 |
| $I^{0111}$ | 0.093217 | 0.030968 | 0.009467 |
| $I^{1111}$ | **0.068282** | 0.0 | 0.0 |

Pooled mean equivalized $W^1$ is €1,107.5 a month, against €1,265.7 for singles and
€972.7 for couples.

**The pooled decomposition is not exhaustive, exactly as predicted before it was
run.** The fully common pooled state is 39.4 per cent of the pooled baseline, and
the reason is visible rather than mysterious: the two type-specific reference
bundles land at €1,251.25 (single) and €951.75 (couple) equivalized, a ratio of
0.761. A pooled fully common state sends each type to *its own* reference, so it is
not common, and no operator in $\{\mathrm{pref},\mathrm{acc},\mathrm{earn},\mathrm{needs}\}$ can close the gap. **Pooled inequality
is well defined and is reported; the pooled decomposition is reported as a
diagnostic and is not a headline.** For the record, its Owen values are
$C_{\mathrm{pref}} = 0.015988$ for preferences and $C_{\mathrm{env}} = 0.088966$ for
the environment, with
job access at 0.016434, earning opportunities at 0.016679 and endowments and
needs at 0.055853. **Figure C4** carries it.

**One implication the economics review should look at directly.** On the
modified-OECD equivalized money metric, couples are worse off than singles at
every quantile: €698 against €823 at the tenth percentile, €922 against €1,242 at
the median, €973 against €1,266 at the mean. The arithmetic is transparent —
couples hold 33 per cent more raw equivalent income (€1,836.8 against €1,384.1)
while the scale asks 65 per cent more (mean $m$ of 1.92 against 1.16). That is an
implication of the ratified primary scale applied to this money metric, not a
finding this module can adjudicate.

**Nothing in this section is an intra-couple welfare statement.** The welfare unit
is the household throughout; the decomposition says nothing about how well-being
is distributed between spouses, and no such claim is made anywhere.

### 8.6 What travels with every couples number

The weakly recovered male leisure block (three of four coordinates marginal at
the governing fitted-point diagnostic); no synthetic-recovery diagnostic at
production scale has been run on the couples specification, exactly as none has
been run on the singles one; the access channel's joint-participation-regime limb
is structurally inert, because the joint regime law carries no household
covariate; the earning-opportunity channel's occupation limb is coordinate-empty
on the common support; and the standing non-identification sentence on the access
density. Additionally, the child-count variable agrees with the under-14 count in
1,755 of 2,275 couple households (77.1 per cent) and with the under-18 count in
93.8 per cent — the couples counterpart of the singles open item, reported and not
reconciled.

---

## 9. External validation

Nothing in this section identifies anything. Every comparison here is run under a
**validation-only** status: no external source is an instrument, none enters the
likelihood, no moment from one enters the objective, and no merge or covariate is
created from one. The question asked is narrower and worth asking on its own
terms — are the features the estimated model asserts visible in sources the model
never saw?

Two further disciplines govern how the comparisons are read. First, the estimation
sample is 1,555 French **single-adult** households, while every external source
covers a different population on a different field with different coverage rules.
A gap between the observed sample and an external aggregate is therefore a
statement about population, coverage and field definitions at least as much as
about the model, and **no such gap is described as a prediction error**. Second,
where an external classification cannot be uniquely mapped onto the model's own,
the comparison is not made at all rather than made through an ad hoc bridge.

### 9.1 Earnings: the within-sample benchmark, and the external one that is not available

The internal benchmark comes first, because it is the object any external
comparison would be read against. Among employed single adults the observed and
model-implied distributions of the selected hourly wage line up closely at the
centre, and by sex in opposite directions:

| group | observed median | model-implied median | fit | observed mean | model-implied mean | fit |
|---|---:|---:|---:|---:|---:|---:|
| all | €14.07 | €13.79 | $-0.29$ | €15.52 | €15.19 | $-0.33$ |
| men | €14.70 | €13.84 | $-0.86$ | €16.03 | €15.22 | $-0.81$ |
| women | €13.40 | €13.74 | $+0.34$ | €15.05 | €15.17 | $+0.12$ |

*Euros per hour, 2016 real; the fit column is model-implied minus observed. The
model-implied side is a self-normalised importance-sampling estimate over the
sampled alternatives, weighted by the household weight — the same construction as
every other share statistic in this paper.*

The median fit is **$-0.86$ an hour for men and $+0.34$ for women**, against
observed medians near €14: the model slightly compresses the sex gap in selected
wages, under-shooting men and over-shooting women, while matching the pooled median
to under thirty cents. That compression is the wage-side counterpart of the
offered-wage quintile misfit reported in §6.2, and it is the same open item rather
than a new one.

**The external earnings benchmark is DADS / Base Tous Salariés**, the matched
employer–employee source that would discipline the wage-offer block independently
of the choice data. It is **not available to this paper**: the accessible
restricted-data folder holds fourteen files, four EU-SILC and ten EU-LFS, and no
DADS or SES file at all, so there is no aggregate to read and none can be produced
without a new secured session and a new data request. The comparison is recorded as
future work and is not attempted, and nothing is put in its place.

`[PLACEHOLDER — the DADS wage comparison.]` When it is run, three things travel
with it, and they are stated now so that the framing is fixed before any number is
seen. DADS covers **employees**, so the self-employed in this sample have no
counterpart in it; it is an **establishment-reported earnings** field rather than a
survey-reported one; and its population is all French employees rather than adults
living alone. A difference between the model-implied wage distribution here and a
DADS aggregate therefore carries population, coverage and field differences before
it carries anything about the model, and **it will not be reported as a prediction
error**.

### 9.2 Hours: official benchmarks against the observed sample and the model

The hours-opportunity block is disciplined only by the EU-SILC choice data, and it
is the block with the sharpest external counterpart. The comparison uses 43,767
French EU-LFS 2016 person-records aged 20–60 with reported usual hours, aggregated
to the model's own five hours bands. The band partitions coincide exactly on
integer usual hours, so the comparison is like-for-like and no re-banding is
applied to either side — and that was checked off the estimation frame rather than
assumed from documentation, because three non-archive call sites in the codebase
still carry legacy band edges that are *not* the reporting bins; the frame's
realised dummy supports were read directly and the statutory band's overlap with
the other four is exactly zero. The by-sex model shares did not exist on the record
and were computed for this comparison; the pooled bins recomputed in the process
reproduce the paper's own hours-fit figure in 20 of 24 numbers bitwise, at a worst
deviation of $5.6\times10^{-17}$ — float summation order across the two sex blocks,
not a different computation.

**Figure 16** carries the comparison; its panel (b) puts the external benchmark,
the observed sample and the model-implied shares side by side on the statutory
band, and its panels (a) and (c) carry the underemployment evidence of §9.3.

The summary paragraph, generated from the table:

> The hours-opportunity block of the estimated model is disciplined only by the
> EU-SILC choice data, but the structure it recovers is visible in an independent
> labour-force source. The final singles model places the offer density
> overwhelmingly on the statutory 35-hour band and on full time: relative to the
> 35-hour band, the estimated per-alternative offer weight is 0.86 at 36.5–40.5
> hours but only 0.09 at 17.5–21.5 hours, 0.13 at 28.5–30.5 hours and 0.12 at
> 44.5–70 hours. In the 2016 French EU-LFS, restricted to ages 20–60, the 35-hour
> band accounts for 37.2 % of workers in the five bands the model prices, against
> 34.3 % in the observed sample and 34.6 % in the model-implied distribution; the
> concentration is larger for women than for men in all three (40.6 % against
> 34.6 % in the external source, 36.7 % against 32.4 % in the model), and it is not
> a single-year artefact — the same table one year earlier puts the statutory share
> at 37.3 % with the same sex ordering. Two independent moments in that source
> describe the short-hours end the same way. The share of employed people reporting
> a wish to work more hours falls monotonically in hours worked, from 46.6 % at
> 17.5–21.5 hours to 37.5 % at 28.5–30.5, 23.7 % at the statutory week, 19.8 % at
> 36.5–40.5 and 7.6 % at 44.5–70. Mean desired hours minus mean actual hours falls
> with it and is strictly positive on every band up to 39 hours — $+8.2$ hours at
> 17.5–21.5, $+3.7$ at 28.5–30.5, $+1.6$ at the statutory week and $+0.9$ at
> 36.5–40.5 — turning negative only at long hours, $-1.5$. The current model has no
> direct desired-hours counterpart; the external underemployment gradient is
> consistent with the estimated thinness of short-hours opportunities. None of this
> identifies the hours-opportunity parameters, and none of it enters the
> likelihood. It is an external consistency check: the two features the estimated
> block asserts — a sharp 35-hour concentration, stronger among women, and thin
> opportunities at short hours — are both present in a source the model never saw.

Three disclosures travel with it, and none is optional. First, the relative offer
weight is a weight on an **alternative**, not a model-implied share: the
model-implied band share also carries how many sampled latent jobs land in the band
and the whole preference side, which is why full time carries 86 per cent of the
statutory band's offer weight and a *larger* model-implied share than it. Second,
**the weight column carries no interval**, and the reason is on the record: an
interval on a difference of two band coefficients needs their covariance, and the
estimation record stores standard errors only. Manufacturing one from the two
marginal errors would be wrong in an unsigned direction, so the column is a point
object and the omission is stated on the figure's face. Third, **the estimated
hours-band weights are not sex-specific**: the final singles model carries one set
of hours-band coordinates common to men and women, so the relative-offer-weight
column is identical down the male, female and pooled blocks by construction, and
any sex contrast in the comparison lives in the *model-implied shares*, which do
differ by sex through the leisure block, the occupation-availability coordinates
and the wage-offer location — which is why the sex ordering in the comparison is a
statement about model-implied shares and a real one: the model reproduces
female-above-male in the statutory band **without any sex-specific hours
coordinate**. Finally, every share reported here is conditioned on employment, and
deliberately: the residual bucket outside the five priced bands carries a special
hours code rather than an hours figure, which is what pushes its mean desired hours
to 79 and which the follow-up moments show accounts for 97 per cent of the mass
above 70 hours. That bucket is flagged and excluded from every comparison rather
than used, and §9.3 records what the follow-up cross-tabulation showed it actually
contains.

### 9.3 Underemployment: external descriptive context, not a model comparison

The external source also carries a direct report of whether a worker wishes to work
more hours. Its national coding is settled against the EU-LFS codebook (version of
8 July 2021), which gives $1 =$ No and $2 =$ Yes; the delivered export's own field
name carried the opposite map and is superseded — a dated note records the
inversion, and no number in the export is affected by it, only two labels. The
variable is fully observed on all fifteen focal sex × band cells, so nothing here
rests on imputation. The follow-up moments the earlier draft was waiting on have
since landed, and they close the documentation question on evidence as well.

**What the external source says.** Among employed people in the five focal hours
bands, **20.3 per cent report wishing to work more hours, and this share declines
with current hours worked** — 46.6 per cent at 17.5–21.5 hours, 37.5 at 28.5–30.5,
23.7 at the statutory week, 19.8 at 36.5–40.5 and 7.6 at 44.5–70. Across all
employed people aged 20–60 the share is 22.9 per cent. The
desired-minus-actual-hours profile shows the same descriptive gradient: mean
desired hours minus mean **actual** hours within the band is $+8.2$ hours at
17.5–21.5, $+3.7$ at 28.5–30.5, $+1.6$ at the statutory week and $+0.9$ at
36.5–40.5, turning negative only at long hours, $-1.5$. It is positive on every
band up to 39 hours, it falls alongside the wish-more share, and it is larger for
men than for women in all four of those bands. Two moments that could have
disagreed do not.

**These are external facts about reported hours wishes, and that is all they are.**
The structural model has no desired-hours or underemployment outcome. These moments
are therefore **not compared with a model prediction, not used to validate an
estimated offer-weight parameter, and identify nothing in the model.** They are
reported only to document the labour-market context in which the estimated hours
distribution is interpreted. No rank association between the reported hours wishes
and any estimated quantity is computed anywhere in this paper, and none should be:
the two objects are not commensurable, so a correlation between them would not
mean what it appears to mean.

Panels (a) and (c) of **Figure 16** carry these two profiles and are labelled
external descriptive evidence on their face; neither plots a model quantity on any
axis. The long-hours band is drawn and marked rather than dropped, because wanting
more hours at fifty-plus is not underemployment and the band would otherwise be
read as though it were. Panel (b) is the validation panel and does not use this
variable at all.

Two provenance facts travel with this subsection. The follow-up moments reached
this side as a **transcription** of the secured-session export rather than as the
exported file itself, so they are read with a measured error rate: on the one file
that exists in both forms the transcription drifts in 2 of 168 comparable cells, at
worst by 0.09 of an hour, and those are digit-level slips inside a long float
rather than structural error. And the follow-up cross-tabulation overturns one
reading in §9.2: the external panel does carry the non-employed after all — 25.8
per cent of persons aged 20–60, weighted — coded into the residual bucket by a
special hours value, while the small bucket the export *named* non-employed is
employed people whose hours are not reported. Both buckets were already excluded
from every comparison, so no number above changes; the description of why does.

### 9.4 Occupation: why the fit panel is internal

The public French occupation classifications **cannot be uniquely harmonised** to
the task-based ISCO grouping this model uses. There is no defensible one-to-one
image, and constructing one would put an arbitrary mapping inside a validation
result. Three consequences are taken, and they are taken together:

1. **External occupation composition is not a model-validation result** in this
   paper, and no such comparison is reported.
2. **No ad hoc crosswalk is imposed** to manufacture one.
3. **The occupation panel of the paper is the internal observed-against-model
   fit** of §6.2 — the largest deviation across the five categories, including
   non-employment, is seven-tenths of a percentage point (**Figure 5**). That is
   the occupation-fit evidence this paper offers, and it is a within-sample
   statement about the estimated model rather than an external one.

The four-table crosswalk audit that exists is cited as **reproducibility evidence
only** — it documents what a mapping would have to assume — and is not used as
identification evidence anywhere.

**The regional occupation-demand construction: a negative result, in one
sentence.** A lagged 2015 employer-side recruitment-tension covariate at NUTS-2,
aggregated to the four task groups through that four-table crosswalk and entered in
the occupation margin as one coefficient, was estimated on three arms specified
in advance and closed as a negative result, and the only statement made about it is the
permitted one: *this lagged construction adds no detectable structural
occupation-access signal in the current sample and specification*. It is not
claimed that regional occupation demand is generally irrelevant, and it is not used
as identification evidence anywhere. The mapping is disclosed rather than assumed
away, and the disclosure is exactly why the crosswalk cannot carry a validation
claim: mapped recruitment-mass coverage is 0.5837, with 0.3799 of recruitment mass
withdrawn because no defensible weighting basis exists for it, 0.0324 genuine
non-significant mass in the official matrices, and four codes carrying 0.40 per cent
of mass with no crosswalk image and no imputation; the two candidate mappings
disagree on two of the four task groups, at column correlations of 0.62 and 0.66.

---

## 10. Limitations and scope

Each limitation is stated as what the design does and does not claim, with its
evidence. None of them is an apology.

### 10.1 Identification

**Access versus capability.** The access margin is a level shift on every working
package. The present access density may combine personal capability and market
availability; it does not yet separately identify $A_i$ from $O_i$. The design
claims that the estimated density describes *how available* packages are to a
household with given observables. It does not claim to separate the set of jobs a
person is capable or eligible to perform — the ability set in its reserved sense —
from the set the market puts in front of them. Every attribution to the access
channel in §7 is an attribution to that combined object, and **no result in this
paper ranks households by productivity**.

**Persistent unobserved heterogeneity.** The choice model carries a job-package
Gumbel shock and no household-level persistent term. Three heterogeneity
extensions were specified in advance and none satisfied the stated recovery
criterion, for the
three different measured reasons set out in §5.4. These results reject *those
parameterisations* on *this design*. They do not establish that preference or
opportunity heterogeneity is absent, and the paper does not claim that. Under the
standing rule that no extension is admitted without satisfying that criterion, the
preferred specification is formally retained rather than an extension invented.

**The age bound.** Two coordinates rest on an active box bound in the unit of
record. §5.2 shows this is a property of the unit — at a different leisure
normaliser the same point has both strictly interior — and §5.5 shows by
re-estimation under a five-fold wider box that releasing the bound empties the
active set, improves the objective by half a nat, moves the two released
coordinates to imprecisely estimated interior values, and moves nothing the paper
reads economically by as much as one standard error. Two legs of that diagnostic —
the profiles and the welfare re-evaluation — have not returned.

**What would identify more.** Each negative result names what would change its
arithmetic, and none of it is in the present data: repeated choices per household,
which would supply a second contrast on the employment margin; external moments on
job-offer or access rates, or on wage offers, which would pin the persistent terms
from outside the choice likelihood; and desired-hours moments, which would
discipline the hours-band density against a stated target rather than infer both
from realised hours. **No such moment enters the objective anywhere in this
paper** — including the EU-LFS comparison of §9, which is a validation and not an
identification device.

### 10.2 The welfare layer

**Normative-reference sensitivity is real, and is reported as a range.** §7.5. The
sign of the preference contribution, the environment's dominance and the nested
order are identical under both ratified reference blocks; the magnitude of the
preference contribution differs by more than the integration bands, and the
classification is reference-sensitive in magnitude. Results are reported
as the female-primary value, the male-sensitivity value and their range, and are
never averaged. Only 3.7 and 7.3 per cent of the female–male gap is attributable
to the children-in-leisure term, so the sensitivity is not a child-term artefact.

**Absolute levels depend on the numerical support design.** Moving from
household-specific to common quadrature support moved the fully-observed welfare
level by $-5.53$ per cent on the preferred model and $-7.74$ per cent on the
benchmark. The common support is a numerical-integration correction, not a common
realised opportunity set; the movement is disclosed, no proposal-invariance claim
is made, and absolute levels are not frozen as final. The levels are additionally
conditional on the inherited hours-normaliser convention and are not
convention-free magnitudes.

**Bands are integration precision; sampling uncertainty is not estimated.** Every
banded quantity travels with the three-way report of §3.6. The integration band
addresses numerical-integration error only; a profile envelope, where one exists,
addresses conditional uncertainty in one profiled coordinate only and is never
combined with the band; and the third row — sampling uncertainty of the estimated
parameter vector propagated to the welfare functionals — is stated rather than
elided: **it is not estimated in this paper**, and no reader should infer it from
the first two.

**The equivalence scale is a disclosed normative parameter, and the coalition-
consistent convention is a normative choice as well as an arithmetic one.** §3.5
and §7.4. The modified-OECD scale is the primary disclosed scale; a model-implied
scale is a later sensitivity and does not exist yet. The question of whether
"equalising needs" should move the scale is open and is the first item on the
economics review's list.

**Everything in §7 and §8 is provisional pending that review**, and carries the
label to that effect on its own artefacts.

### 10.3 Data

**The wage variable.** For every 2016 person with observed earnings and hours the
delivered hourly wage reproduces gross monthly earnings, annualised over the
months paid, divided by monthly hours — an identity that holds for 100 per cent of
such persons at machine precision. The structural wage density and its education
and experience loadings are therefore fitted against *observed* worker wages, not
against fitted conditional means. The construction of the delivered variable for
persons *without* observed wage inputs is incompletely documented: the imputation
do-file is unavailable, and of eleven documentation fields audited, seven are
unavailable without it and three more only partially documented. That construction
does not enter the likelihood — the non-worker wage location is provably inert, the
objective being bitwise unchanged when every non-working row's wage is overwritten
— and the genuinely imputed worker wage is confined to 21 workers with zero
recorded earnings.

**Hours support.** Ten households had observed weekly hours moved by the
data-construction clip. Three lie above the 70-hour cap and are projections onto
model support, now a recorded convention rather than an implicit one. Seven lay
between five and ten hours and were moved by a floor that was not a support
boundary — the latent hours support reaches five hours and the frame carries jobs
there — so their priced budgets were wrong by up to a quarter of disposable
income. The floor was corrected through the actual construction path: exactly
seven chosen alternatives changed, every drawn alternative was bitwise unchanged,
and both positive models were re-estimated on the corrected frame with no
coordinate moving more than a tenth of its previous standard error and the
specification comparison unchanged. The corrected frame is the sole forward-looking
frame and every number in this paper is on it.

**Take-up.** Benefit take-up rates are estimated on thin cells and enter
consumption through the take-up-adjusted disposable income. This is the input
weakness of the pipeline.

**Geography and time.** NUTS-2 (22 régions) is the finest household geography;
nothing below it exists, and the sampling units are clustering dimensions, not
geographies. The regional access shifters are therefore coarse objects, with
région cells of median 53.5 households, and any finer sorting is unobserved. Corse
has three households and no Corse-specific statement is possible. The estimation
data are a single-year cross-section, one choice per household, which is the source
of the identification limit in §10.1.

**Wage-quintile fit.** The model over-predicts the bottom offered-wage quintile by
about five percentage points and under-predicts the second through fourth (§6.2). A
repair through an hours-conditioned wage location, specified in advance, was tested and
failed on both information criteria and on five of seven fit metrics (§6.5). The
misfit is an open item of the specification.

### 10.4 Scope

**Singles are the primary application.** The bounded review that accepted the
preferred specification closes the *singles* positive specification only and
establishes nothing about couples or a population-wide final model.

**Couples are a parallel module with characterised limitations.** §8. The clean
both-flexible baseline is supported with a named weakness in the male leisure
block; couples welfare is a sensitivity-bounded companion, not the headline; the
pooled decomposition is not exhaustive and is reported as a diagnostic; and no
intra-couple welfare statement is made anywhere. The two semi-flexible couple types
— one spouse fixed at the observed state — are designed and their adapter passes
its contract tests, but no estimate on them exists and none is reported.

**Multi-adult households are excluded.** 934 households with three or more
decision-unit adults are outside the headline. Their admission would require five
assumptions the present design leaves unstated: resource pooling, the tax/benefit
unit, the allocation of consumption within the household, the needs of additional
adults, and the welfare unit. Two-adult households whose adults are not mutually
linked as partners are inventoried and excluded rather than forced into a couple
model; same-sex linked couples are inventoried, not estimated.

**One country, one year, one system.** Everything in this paper is France 2016
under the French tax–benefit system as EUROMOD implements it. The decomposition's
finding that the budget channel carries more measured dispersion than the market
channels is, among other things, a statement about a redistributive system with
substantial means-tested transfers. It is not portable without re-estimation, and
no portability is claimed.

---

## 11. Conclusion

Two single adults in the same job need not be equally well off, and a model that
gives them a common budget set cannot say so. This paper builds one that can. It
estimates a random-utility, random-opportunity model of job choice on 1,555 French
single-adult households in which a job is a package of hours, a wage and an
occupation, every package is priced through the actual tax–benefit system, and a
household-specific opportunity density is estimated jointly with Box–Cox
preferences in a single likelihood carrying 41 estimated structural parameters. It
then carries that estimated density into a money-metric welfare measure —
equivalent income at a common reference pay, which compensates for pay and holds
the household responsible for its own opportunity set — and decomposes the
inequality of that measure, by an Owen value on an exhaustive four-channel game,
into preferences, job access, earning opportunities, and endowments and needs.

Three things came out of it.

**Substantively**, the environment dominates: equalising the whole non-preference
environment removes 89 to 94 per cent of baseline money-metric inequality under
the preferred model's two reference conventions, and equalising preferences the
complement, with a constant sign. Inside the environment, the two market channels
are substantial — job access and earning opportunities together remove 35.5 per
cent of baseline inequality on the raw basis and 25.9 per cent on the
coalition-consistent equivalized basis — and the budget side is larger still, with
endowments and needs the largest nested contribution in every one of the eight rows
of the exact table. None of that says job opportunities are unimportant. It says
that in this population, under this system, the budget side of the environment
carries more of the measured dispersion than the market side does, and that the
market side is nonetheless about a third of it.

**Methodologically**, two ingredients turned out to be necessary rather than
optional, and both generalise beyond this application. The **coalition-consistent
inversion** — taking the reference preference block and the reference opportunity
block from the coalition on *both* sides of the money-metric indifference —
removes about 95 per cent of the residual that otherwise makes the decomposition
non-exhaustive. The **coalition-consistent equivalization** — letting the
equivalence scale move with the channel that equalises household composition —
removes the rest of it on the equivalized basis, and the residual it removes is
exactly the weighted Gini of the reciprocal scale, to six decimals. Any
decomposition that equalises demographics and reports equivalized outcomes faces
the second problem whether or not it notices.

**On identification**, the paper's negative results are as informative as its
positive ones. Three persistent-heterogeneity extensions were tested for
recoverability before any real-data estimation and all three failed, for three
different measured reasons, and between them they say what a single cross-section
of discrete choices can and cannot support: a persistent term needs both leverage
— enough within-household spread in the variable it loads on, against a
scale-one shock — and a second contrast the existing coordinates cannot absorb.
Depth on an axis is not depth on a profile. That is a design rule, not a
disappointment.

**What would identify more, and is not yet identified.** Six extensions are
designed, costed and parked. Each would discipline something the present design
infers; **none of them has identified anything in the model reported here**, and
nothing in this paper should be read as if one had.

| extension | what it would discipline | status |
|---|---|---|
| regional occupation-demand covariates | the occupation-availability margin from the employer side | tested; a negative result on the current construction, not identification evidence |
| labour-force-survey auxiliary moments | the hours-opportunity density against a stated target rather than realised hours | the 35-hour concentration is validated externally (§9), as is the underemployment gradient, on a settled coding and a corroborating hours-gap moment; **not yet identified** |
| matched employer–employee earnings | the wage-offer technology from outside the choice likelihood | data not available; no run possible; **not yet identified** |
| the expanded sample and repeated choices | the second contrast the persistent-heterogeneity extensions lack | **not yet identified** |
| semi-flexible couples (one spouse fixed) | the couples decision structure, and the male leisure block | designed, adapter tested, no estimate; **not yet identified** |
| multi-adult households | the five unstated assumptions of §10.4 | excluded by scope; **not yet identified** |

The paper's own next step is the bounded economics review the drafting note
enumerates, and in particular the normative question the equivalization result
forces: whether equalising needs means giving every household the reference
household's needs, in which case the scale must move with the channel, or
equalising resources while leaving needs alone, in which case what this paper
treats as a defect is a genuine needs term and the accounting must change. The
arithmetic under both readings is on the record. The economics is not settled, and
it should not be settled by whoever happens to write the code.

---

# Appendices

> **Legend for the technical appendices.** The appendices retain the internal
> specification labels, because reproduction needs them: **S8** is the *final
> singles model* of the main text; **LOC4 / S0** is the *occupation-conditioned
> wage specification benchmark*; **A, B, D, P** are the decomposition's four
> channels — job access, earning opportunities, household endowments and needs,
> and preferences. No label in this legend appears anywhere in §1–§11 or on any
> figure.

## Appendix A — The parameter tables

### A.1 The preferred specification (S8): all 41 estimated coordinates

Robust CR1 standard errors, $G = 1{,}555$ clusters, $K_{\text{interior}} = 39$,
read against $z_{0.975} = 1.959964$. Objective 18022.764617170084. The ten pinned
non-estimated coordinates are not displayed. Two coordinates rest on active box
bounds and carry no standard error; §5.2 and §5.5 establish what that does and
does not mean.

| coordinate | block | estimate | s.e. | 95 % lower | 95 % upper | $z$ | status |
|---|---|---:|---:|---:|---:|---:|---|
| `beta_l0_sm` | preferences — male leisure | 4.6721 | 2.0029 | 0.7465 | 8.5976 | 2.33 | interior |
| `beta_l_age_sm` | preferences — male leisure | 0.6782 | 0.7555 | −0.8026 | 2.1591 | 0.90 | interior |
| `beta_l_age2_sm` | preferences — male leisure | 1.0000 | — | — | — | — | active bound |
| `theta_l_sm` | preferences — male leisure | −1.7464 | 0.2471 | −2.2306 | −1.2622 | −7.07 | interior |
| `beta_l0_sf` | preferences — female leisure | 4.2437 | 1.8647 | 0.5889 | 7.8985 | 2.28 | interior |
| `beta_l_age_sf` | preferences — female leisure | −0.0187 | 0.4711 | −0.9422 | 0.9047 | −0.04 | interior |
| `beta_l_age2_sf` | preferences — female leisure | 1.0000 | — | — | — | — | active bound |
| `beta_l_nkids_sf` | preferences — female leisure | 1.1690 | 0.6083 | −0.0233 | 2.3614 | 1.92 | interior |
| `theta_l_sf` | preferences — female leisure | −1.0793 | 0.2451 | −1.5596 | −0.5990 | −4.40 | interior |
| `theta_c_singles` | preferences — consumption curvature | 0.1680 | 0.0740 | 0.0230 | 0.3130 | 2.27 | interior |
| `beta_E` | job access — employment + hours | −3.3344 | 0.3584 | −4.0368 | −2.6320 | −9.30 | interior |
| `beta_h_pt1` | job access — employment + hours | 0.1730 | 0.1736 | −0.1673 | 0.5134 | 1.00 | interior |
| `beta_h_pt2` | job access — employment + hours | 0.5497 | 0.1918 | 0.1738 | 0.9255 | 2.87 | interior |
| `beta_h_ft` | job access — employment + hours | 2.4303 | 0.1018 | 2.2308 | 2.6298 | 23.88 | interior |
| `beta_h_lh` | job access — employment + hours | 0.4293 | 0.1808 | 0.0750 | 0.7836 | 2.37 | interior |
| `beta_h_f35` | job access — the 35-hour peak | **2.5795** | 0.0983 | 2.3868 | 2.7722 | **26.24** | interior |
| `beta_E_gsur` | job access — market access | −1.2525 | 0.1983 | −1.6412 | −0.8638 | −6.32 | interior |
| `beta_E_drgn2` | job access — market access | −0.2149 | 0.3070 | −0.8166 | 0.3867 | −0.70 | interior |
| `beta_E_drgn3` | job access — market access | −0.0492 | 0.3542 | −0.7434 | 0.6451 | −0.14 | interior |
| `beta_E_drgn4` | job access — market access | −0.6585 | 0.3502 | −1.3448 | 0.0279 | −1.88 | interior |
| `beta_E_drgn5` | job access — market access | −0.3060 | 0.3100 | −0.9136 | 0.3017 | −0.99 | interior |
| `beta_E_drgn6` | job access — market access | −0.5412 | 0.3216 | −1.1716 | 0.0892 | −1.68 | interior |
| `beta_E_drgn7` | job access — market access | −0.3666 | 0.3325 | −1.0182 | 0.2850 | −1.10 | interior |
| `beta_E_drgn8` | job access — market access | −0.2803 | 0.3197 | −0.9069 | 0.3463 | −0.88 | interior |
| `beta_E_drgur` | job access — market access | −0.0156 | 0.2045 | −0.4165 | 0.3853 | −0.08 | interior |
| `beta_E_drgmd` | job access — market access | 0.0791 | 0.2392 | −0.3898 | 0.5480 | 0.33 | interior |
| `beta_occ_2_m` | job access — occupation availability | −1.3114 | 0.1480 | −1.6015 | −1.0213 | −8.86 | interior |
| `beta_occ_3_m` | job access — occupation availability | −1.9329 | 0.1950 | −2.3152 | −1.5507 | −9.91 | interior |
| `beta_occ_4_m` | job access — occupation availability | 0.0047 | 0.0937 | −0.1790 | 0.1884 | 0.05 | interior |
| `beta_occ_2_f` | job access — occupation availability | 0.0118 | 0.1233 | −0.2299 | 0.2535 | 0.10 | interior |
| `beta_occ_3_f` | job access — occupation availability | −0.4053 | 0.1319 | −0.6639 | −0.1467 | −3.07 | interior |
| `beta_occ_4_f` | job access — occupation availability | 0.7174 | 0.0991 | 0.5231 | 0.9116 | 7.24 | interior |
| `beta_w0` | earning opportunities — wage-offer density | 2.1249 | 0.0515 | 2.0240 | 2.2259 | 41.26 | interior |
| `beta_w_educL` | earning opportunities — wage-offer density | 0.0563 | 0.0383 | −0.0188 | 0.1313 | 1.47 | interior |
| `beta_w_educH` | earning opportunities — wage-offer density | 0.1513 | 0.0299 | 0.0926 | 0.2099 | 5.06 | interior |
| `beta_w_pexp` | earning opportunities — wage-offer density | 0.2197 | 0.0873 | 0.0487 | 0.3907 | 2.52 | interior |
| `beta_w_pexp2` | earning opportunities — wage-offer density | −0.0165 | 0.0392 | −0.0934 | 0.0603 | −0.42 | interior |
| `sigma` | earning opportunities — wage-offer density | 0.3895 | 0.0133 | 0.3635 | 0.4155 | 29.37 | interior |
| `delta_occ_2` | earning opportunities — occupation wage-location | −0.0484 | 0.0414 | −0.1296 | 0.0328 | −1.17 | interior |
| `delta_occ_3` | earning opportunities — occupation wage-location | 0.0467 | 0.0365 | −0.0249 | 0.1183 | 1.28 | interior |
| `delta_occ_4` | earning opportunities — occupation wage-location | 0.2739 | 0.0352 | 0.2049 | 0.3429 | 7.78 | interior |

### A.2 The nested benchmark (LOC4 / S0): all 40 estimated coordinates

Identical specification less `beta_h_f35`. Objective 18453.4750133318.

| coordinate | estimate | s.e. | $z$ | status |
|---|---:|---:|---:|---|
| `beta_l0_sm` | 4.9399 | 2.5907 | 1.91 | interior |
| `beta_l_age_sm` | 0.2980 | 1.1489 | 0.26 | interior |
| `beta_l_age2_sm` | 1.0000 | — | — | active bound |
| `theta_l_sm` | −2.4206 | 0.2510 | −9.64 | interior |
| `beta_l0_sf` | 8.0478 | 4.1551 | 1.94 | interior |
| `beta_l_age_sf` | −0.9463 | 1.2091 | −0.78 | interior |
| `beta_l_age2_sf` | 1.0000 | — | — | active bound |
| `beta_l_nkids_sf` | 1.9499 | 1.6407 | 1.19 | interior |
| `theta_l_sf` | −2.0827 | 0.2990 | −6.97 | interior |
| `theta_c_singles` | 0.0885 | 0.0765 | 1.16 | interior |
| `beta_E` | −2.5665 | 0.3607 | −7.12 | interior |
| `beta_h_pt1` | −0.6979 | 0.1651 | −4.23 | interior |
| `beta_h_pt2` | −0.4194 | 0.1818 | −2.31 | interior |
| `beta_h_ft` | 1.3588 | 0.0710 | 19.15 | interior |
| `beta_h_lh` | −0.9028 | 0.1388 | −6.50 | interior |
| `beta_E_gsur` | −1.2627 | 0.2007 | −6.29 | interior |
| `beta_E_drgn2` | −0.2147 | 0.3122 | −0.69 | interior |
| `beta_E_drgn3` | −0.0613 | 0.3618 | −0.17 | interior |
| `beta_E_drgn4` | −0.7006 | 0.3562 | −1.97 | interior |
| `beta_E_drgn5` | −0.2813 | 0.3159 | −0.89 | interior |
| `beta_E_drgn6` | −0.5126 | 0.3264 | −1.57 | interior |
| `beta_E_drgn7` | −0.3901 | 0.3367 | −1.16 | interior |
| `beta_E_drgn8` | −0.2800 | 0.3250 | −0.86 | interior |
| `beta_E_drgur` | −0.0135 | 0.2077 | −0.06 | interior |
| `beta_E_drgmd` | 0.0889 | 0.2422 | 0.37 | interior |
| `beta_occ_2_m` | −1.3046 | 0.1528 | −8.54 | interior |
| `beta_occ_3_m` | −1.8932 | 0.1999 | −9.47 | interior |
| `beta_occ_4_m` | 0.0394 | 0.0983 | 0.40 | interior |
| `beta_occ_2_f` | −0.0607 | 0.1264 | −0.48 | interior |
| `beta_occ_3_f` | −0.4589 | 0.1352 | −3.40 | interior |
| `beta_occ_4_f` | 0.6368 | 0.1045 | 6.09 | interior |
| `beta_w0` | 2.1177 | 0.0545 | 38.87 | interior |
| `beta_w_educL` | 0.0676 | 0.0399 | 1.70 | interior |
| `beta_w_educH` | 0.1394 | 0.0360 | 3.87 | interior |
| `beta_w_pexp` | 0.2250 | 0.0912 | 2.47 | interior |
| `beta_w_pexp2` | −0.0197 | 0.0410 | −0.48 | interior |
| `sigma` | 0.3927 | 0.0140 | 28.03 | interior |
| `delta_occ_2` | −0.0413 | 0.0440 | −0.94 | interior |
| `delta_occ_3` | 0.0511 | 0.0402 | 1.27 | interior |
| `delta_occ_4` | 0.2910 | 0.0429 | 6.79 | interior |

### A.3 Specification comparison

| | preferred (S8) | benchmark (LOC4 / S0) |
|---|---:|---:|
| coordinates / free / pinned / interior | 51 / 41 / 10 / 39 | 50 / 40 / 10 / 38 |
| objective | 18022.764617 | 18453.475013 |
| likelihood ratio, 1 d.f. | **861.42** | — |
| AIC | 36127.529 | 36986.950 |
| BIC (households) | 36346.848 | 37200.919 |
| free-block minimum eigenvalue | $+0.442$ | $+0.092$ |
| condition tier | clean | clean |
| active-bound set | 2 age-squared terms | 2 age-squared terms |
| employment share, observed / predicted | 0.8708 / 0.8668 | 0.8708 / 0.8653 |
| statutory band, observed / predicted | 0.2485 / 0.2520 | 0.2485 / 0.0546 |
| hours-grid share MAE | 0.0083 | 0.0338 |
| occupation, largest deviation | 0.0070 | 0.0074 |
| wage-quintile, largest deviation | 0.0532 | 0.0521 |

---

## Appendix B — The exhaustiveness saga, in one page

The decomposition is licensed to report shares only if the fully common state is
negligible. It was not, for a long time, and the sequence by which it became so is
a methodological result rather than a maintenance log: each step *found* a residual
object by measurement and removed it, and the residual that survived each step is
what identified the next one.

| # | residual object found | how it was found | measured effect of removing it |
|---|---|---|---|
| 1 | **the budget channel was missing** | the two-channel game (access and earning opportunities) failed exhaustiveness: household-specific budget, endowment and needs heterogeneity survived inside the priced budget | a fourth channel, endowments and needs, was added, formed from its own Owen marginals and not as a relabelled residual; the game became $\{\mathrm{pref},\mathrm{acc},\mathrm{earn},\mathrm{needs}\}$ |
| 2 | **the complete-environment game still failed, and failed badly** | with endowments and needs in, $I^{1111}/I^{0000} = 3.0288$ on the preferred model and $3.2566$ on the benchmark — equalising everything left an index three times the one we started from; the headline was **halted** | none: this is the diagnosis, not a fix. What it identified is that the residual was *not* budget heterogeneity, because that channel demonstrably removed the dispersion it was built to remove and the fully common state barely moved |
| 3 | **the inversion core was frozen at the baseline** | the money-metric solve took the preference and opportunity blocks from the coalition on the attained side and from the *baseline* on the reference side — the same object at two different coalitions on two sides of one indifference | $I^{1111}$ fell from 0.430622 to 0.021313 on the preferred model with the female reference: a **95.1 %** reduction, and 94.0–94.9 % in the other three arms |
| 4 | **the quadrature support was household-specific** | each household integrated over its own drawn nodes, so finite-support variation could appear as welfare inequality; a zero-cost broadcast precheck confirmed that a common support returns a bitwise identical welfare level for all 1,555 households | $I^{1111}$ fell to $-2.233\mathrm{e}{-}31$ and $-2.363\mathrm{e}{-}31$ in the two female-primary arms — numerical zero. The fully-observed level moved $-5.53$ % and $-7.74$ %, a quadrature-support difference and nothing else |
| 5 | **the male reference block's preference operator was incomplete** | the male arms did *not* reach zero — they sat at $1.113\mathrm{e}{-}3$ and $9.777\mathrm{e}{-}4$, inside the tolerance but visibly non-zero. With the support, budget profile, primitives and inversion all common, that cannot be an integration residual. It was not: at the fully common state the utility took exactly two values per node, one per sex, differing by up to 0.194, and the carrier was the children-in-leisure term, which the specification carries for women and **not at all for men** | representing both reference blocks on the **union** of preference terms, with the male child term at a **structural zero** because the specification implies no other value, drives the residual to $-2.035\mathrm{e}{-}31$. (Supplying the female coefficient to the male block also collapses it, to $-5.6\mathrm{e}{-}30$; that counterfactual is a **diagnostic only**, is not adopted, and carries no reported contribution) |
| 6 | **the draw-0 anchor row** | the assembled welfare stem carries a per-household anchor row that is excluded from every welfare object by construction, but reaches the numbers through the panel consumption scale | the scale shifts by $-1.402\mathrm{e}{-}4$ euros on 1774.5182, a relative $7.9\mathrm{e}{-}8$ — four orders of magnitude below the integration bands. Disclosed; the refresh is not taken |
| 7 | **the equivalence scale, frozen at the household's own value** | on the equivalized basis, $I^{1111}$ rose from zero to **0.071799** in all four arms, 43 % of baseline. The weighted Gini of $1/m$ is **0.071799** — the same number to six decimals | letting the scale move with the channel that equalises composition, so that the reference household's $m = 1$ applies in every state that equalises endowments and needs, restores $I^{1111} = 0.000\mathrm{e}{+}00$ and $-2.035\mathrm{e}{-}31$ exactly, as in the raw basis |

**The state now.** Exhaustiveness passes on both bases in all four singles arms and
on both bases for couples, at numerical zero rather than inside the tolerance, with
both accounting identities closing at machine precision. Steps 3 and 7 are the two
methodological contributions of §1.4; steps 2 and 5 are the two occasions on which
a measured residual identified a defect that no amount of reasoning about the
design had found.

**A general lesson.** At each step the residual was *not* forced to zero and *not*
renormalised. That discipline is what made the sequence work: a residual that is
allowed to stand is a diagnostic instrument, and each of these five objects was
found by asking what the surviving residual could possibly be, rather than by
inspecting the code.

---

## Appendix C — The numerical layer

**Importance sampling.** Alternatives are drawn from a defensive mixture: each
unit block allocates 75 base and 25 defensive draws — mixture weight
$\lambda = 0.25$ exactly — on disjoint ladder, base, defensive and counter address
spaces, so no region of the job space carries a proposal density that can vanish
relative to the target. The mixture bound is a checked gate, not an assumption.

**The common quadrature support (singles).** The two things that made the support
household-specific were the Owen scramble address and two household-conditional
limbs of the base proposal component. Both are changed and nothing else is. The
scramble is addressed at a household slot no household occupies (asserted, not
assumed), and the base component is replaced by its own weight-weighted population
marginal, with the occupation and wage limbs *not* independised — their dependence
through the household index is preserved exactly, checked to $7.11\times10^{-15}$
nats. Because every survey weight is positive, the construction gives
$\bar q(x) \ge \omega_i q_i(x)$ at every point for every household, so absolute
continuity is a construction property and the importance weight is bounded;
checked over 3,184,640 household $\times$ node comparisons at a minimum slack of
$+3.226$ nats. Seven pre-declared validity gates pass, including normalisation to
$3.00\times10^{-14}$, preservation of the structural non-employment probability
(0.2 declared, 0.199707 realised), and an effective-sample-size floor declared
*before* the numbers were seen: the median effective sample size on the common
support is about a third *higher* than on the incumbent household-specific support
in every arm.

**The common quadrature support (couples).** The singles recipe generalises with
exactly one substantive change, forced by the two-decider case: the population
marginal is taken over the **joint** per-spouse base component,
$\bar q(k_m,w_m,k_f,w_f) = \sum_i \omega_i\, p_{i,m}(k_m)\,\mathrm{LN}(w_m;\mu_{i,m}(k_m),\sigma)\,p_{i,f}(k_f)\,\mathrm{LN}(w_f;\mu_{i,f}(k_f),\sigma)$,
not spouse by spouse — because the two spouses' draws are dependent through the
household index and the product of marginals is not the marginal of the product,
so the product form would lose the domination property. Drawing remains one
coordinate per limb by a chain rule over four steps whose product telescopes
exactly to the joint marginal. $8 \times 256 = 2{,}048$ common nodes, Sobol
dimension 9, the eight seeds of record, a common scramble slot asserted
unoccupied, no observed pair, and per-spouse structural non-employment atoms with
exact zeros. Gates: the joint identity against the one-log-sum form at a maximum
relative error of $2.90\times10^{-16}$; domination with **zero violations in
4,659,200 household $\times$ node pairs** at a minimum log gap of $+3.57$;
per-spouse atoms present with exact zeros; realised non-employment probabilities of
0.161 (male) and 0.182 (female) against designs of 0.161 and 0.182; and a wage
mixture inverse-CDF residual of at most $5.6\times10^{-16}$. The node table carries
no household index, so the slot map is a pure gather: 1,911 slots from 2,048 nodes,
with $2{,}048 - 1{,}911 = 137$ exactly the collapse of the 138 both-non-employed
atom nodes to one priced row and zero residual collisions.

**Randomised QMC and bands.** The welfare functionals are integrals over the
estimated opportunity density, evaluated on an Owen-scrambled Sobol basis with
eight independent scrambles. Per household the per-scramble integral is formed on
its own sub-basis and averaged **before** the log and before the money-metric
inversion; that this equals the corresponding column selection on the single staged
basis was falsified numerically rather than asserted, at a largest relative
disagreement of $1.37$ and $1.42 \times 10^{-14}$ across all 1,555 households —
float64 summation order. Precision is a delete-one-scramble jackknife with
$t_{0.975,7} = 2.364624251$ and no bias term folded in; the jackknife bias signal is
computed and disclosed on every row as a diagnostic with no pass/fail role.
Precision standards are per class of quantity rather than one global tolerance: a
mean or median must be resolved to 0.25 per cent of its own scale, and a Gini or a
component level — a weighted sum of Gini differences, hence on the Gini scale — to
0.00125 in absolute terms.

**Why the ratio bands required re-deriving the replicates.** Seven of the sixteen
quantities in the headline table are ratios and one is a sum, and a jackknife band
on a ratio is not a function of the bands on its numerator and denominator, because
the two move together across scrambles. The eight leave-one-scramble-out replicates
were therefore recovered by importing the accepted state runner **unmodified** and
rebinding exactly two module globals — the jackknife function is wrapped so that
the dictionary it returns also carries the replicate list it was handed, with the
arithmetic untouched, and the output paths are redirected. The gate that licenses
the result: **1,284 stored numbers — every cell and every Owen contribution, all
four arms, all three bases — compared bitwise against the accepted record, 0
differ.** Twenty-one minutes of compute.

**Pricing geometry.** The couples common support was priced at 4,347,525
(household, slot) rows in 27.2 minutes, batched and household-sorted, with the
minimum-income take-up device neutralised in the engine and the household trait
applied once at assembly. On a common support no two slots of one household share
an input block, so the within-household identical-input test is vacuous and is
recorded as such; the property it protects — that a household's price does not
depend on its batch — is tested where it now lives, by pricing the same households
alone and then mixed with different companions in a different order, which returns
**bitwise identical output on every column**. A separate probe establishes that the
The endowments-and-needs-equalised price is bitwise independent of which household carries the reference
profile, which is what licenses collapsing the reference arm to one profile.
Consumption floors at the certified positive minimum on 87,160 of 4,659,200
actual endowment rows (1.87 per cent) and on zero reference rows.

**Engine-ready assembly.** The certified assembler recomputes the consumption and
leisure normalisers from whatever frame it is handed, which on a chosen-row-free
common support would silently redefine the units the parameters were estimated in.
The normalisers are therefore held frozen at the estimation panel's own values, and
the local builder is gated: fed the estimation frame's own nodes and the priced
panel, it must reproduce the certified engine-ready frame **bitwise on every column
the loader reads (maximum absolute difference 0.0)** and reproduce the objective of
record exactly. It does. Where that gate is uninformative by construction — the
household-constant block comes from the same frame — this is stated rather than
claimed as evidence.

**Two normalisation traps worth recording.** First, the logarithm of the node count
cancels for a **set-valued** reference map, because both sides of the indifference
are log-means over the same support, and does **not** cancel for a single-node map.
The first couples implementation subtracted it once, which put the carrier measure
at about €37 a month; it was caught on a magnitude sanity check before any state was
evaluated. The closed form was then checked against the monotone bisection of record
on every state, at worst relative disagreements of $1.9\times10^{-15}$ and
$3.6\times10^{-15}$. Second, the chosen-row flag is a loader-contract artefact on a
support that has no chosen row; it is set on the first common node — the same node
for every household — and its inertness is **measured**, not asserted: moving it
changes the welfare vector by $7.1\times10^{-15}$ relative.

**Reproducibility mechanics.** Three are worth keeping. Exact-fixed-point polishing
uses a relative-reduction tolerance at machine epsilon rather than zero. Reading a
results register back with a floating-point CSV parser silently drops the
seventeenth significant digit — it was caught by diffing every pre-existing cell
against the committed version, and the register is now read and written with a
non-parsing CSV path that refuses to write unless every pre-existing row
round-trips exactly. And the whole sprint runs on a CPU automatic-differentiation
backend rather than a GPU one, for two reasons: at 1,555 households by 101
alternatives the per-step work is small relative to kernel-launch overhead, so the
CPU route is about 2.7 times faster; and, more importantly, the public package's
GPU grammar cannot represent this specification exactly, because it lacks the
occupation-conditional wage location and occupation-specific hours. The model was
not simplified to fit the faster hardware.

---

## Appendix D — Couples tables

### D.1 The clean both-flexible baseline: 46 free coordinates

Robust CR1 standard errors, $G = 2{,}275$ clusters, $K_{\text{interior}} = 45$.
Objective 43493.342239. One active bound. Twelve further coordinates are pinned
inert and are not displayed.

| coordinate | block | estimate | s.e. | $z$ |
|---|---|---:|---:|---:|
| `beta_l0_m` | male leisure | 2.9316 | 0.5688 | 5.15 |
| `beta_l_age_m` | male leisure | −0.0070 | 0.0247 | −0.28 |
| `beta_l_age2_m` | male leisure | 0.0055 | 0.0026 | 2.14 |
| `theta_l_m` | male leisure | −1.0321 | 0.1224 | −8.43 |
| `beta_l0_f` | female leisure | 9.2815 | 3.8975 | 2.38 |
| `beta_l_age_f` | female leisure | −0.1808 | 0.1545 | −1.17 |
| `beta_l_age2_f` | female leisure | 0.0168 | 0.0121 | 1.39 |
| `beta_l_nkids_f` | female leisure | −0.5586 | 1.3010 | −0.43 |
| `theta_l_f` | female leisure | −1.8669 | 0.2361 | −7.91 |
| `beta_E_m` | hours opportunity, male | −2.7898 | 0.2820 | −9.89 |
| `beta_h_pt1_m` | hours opportunity, male | −0.5170 | 0.2601 | −1.99 |
| `beta_h_pt2_m` | hours opportunity, male | 0.4783 | 0.2358 | 2.03 |
| `beta_h_f35_m` | hours opportunity, male | **3.2915** | 0.1022 | **32.20** |
| `beta_h_ft_m` | hours opportunity, male | 3.3166 | 0.1037 | 31.99 |
| `beta_h_lh_m` | hours opportunity, male | 1.7476 | 0.1572 | 11.12 |
| `beta_E_f` | hours opportunity, female | −3.0782 | 0.2720 | −11.32 |
| `beta_h_pt1_f` | hours opportunity, female | 0.0255 | 0.1371 | 0.19 |
| `beta_h_pt2_f` | hours opportunity, female | 1.1063 | 0.1174 | 9.42 |
| `beta_h_f35_f` | hours opportunity, female | **2.5474** | 0.0735 | **34.66** |
| `beta_h_ft_f` | hours opportunity, female | 2.2099 | 0.0783 | 28.24 |
| `beta_h_lh_f` | hours opportunity, female | 0.0718 | 0.1712 | 0.42 |
| `beta_E_gsur` | employment access | −1.2111 | 0.1467 | −8.26 |
| `beta_E_drgn2` | employment access | −0.1589 | 0.2316 | −0.69 |
| `beta_E_drgn3` | employment access | 0.1010 | 0.2701 | 0.37 |
| `beta_E_drgn4` | employment access | −0.1052 | 0.2786 | −0.38 |
| `beta_E_drgn5` | employment access | −0.2099 | 0.2434 | −0.86 |
| `beta_E_drgn6` | employment access | −0.3905 | 0.2589 | −1.51 |
| `beta_E_drgn7` | employment access | −0.3387 | 0.2451 | −1.38 |
| `beta_E_drgn8` | employment access | −0.2634 | 0.2447 | −1.08 |
| `beta_E_drgur` | employment access | −0.2032 | 0.1525 | −1.33 |
| `beta_E_drgmd` | employment access | −0.3562 | 0.1721 | −2.07 |
| `beta_occ_2_m` | occupation availability, male | −1.5288 | 0.0916 | −16.69 |
| `beta_occ_3_m` | occupation availability, male | −2.1687 | 0.1174 | −18.48 |
| `beta_occ_4_m` | occupation availability, male | 0.3057 | 0.0517 | 5.92 |
| `beta_occ_2_f` | occupation availability, female | 0.2044 | 0.0802 | 2.55 |
| `beta_occ_3_f` | occupation availability, female | −0.1106 | 0.0847 | −1.31 |
| `beta_occ_4_f` | occupation availability, female | 0.9333 | 0.0688 | 13.56 |
| `beta_w0` | wage-offer density | 2.1453 | 0.0194 | 110.78 |
| `beta_w_educL` | wage-offer density | −0.0502 | 0.0214 | −2.35 |
| `beta_w_educH` | wage-offer density | 0.1730 | 0.0191 | 9.05 |
| `beta_w_pexp` | wage-offer density | 0.4485 | 0.0137 | 32.86 |
| `beta_w_pexp2` | wage-offer density | −0.1000 | — | — (active bound) |
| `sigma` | wage-offer density | 0.3779 | 0.0074 | 51.23 |
| `delta_occ_2` | occupation wage-location | −0.0937 | 0.0226 | −4.15 |
| `delta_occ_3` | occupation wage-location | 0.0243 | 0.0227 | 1.07 |
| `delta_occ_4` | occupation wage-location | 0.2227 | 0.0221 | 10.08 |

### D.2 The male-leisure sensitivity arms

Seven pinned refits of the remaining 45 coordinates, all converged, with an
objective spread of at most $2.7\times10^{-9}$ and the same single active bound as
the baseline.

| arm | objective | $\Delta$ vs baseline | likelihood ratio |
|---|---:|---:|---:|
| baseline | 43493.342239 | 0 | 0 |
| `beta_l0_m` low / high | 43497.338227 / 43495.640532 | $+4.00$ / $+2.30$ | 7.99 / 4.60 |
| `theta_l_m` low / high | 43496.746134 / 43497.449608 | $+3.40$ / $+4.11$ | 6.81 / 8.22 |
| `beta_l_age2_m` low / high | 43496.570333 / 43495.427341 | $+3.23$ / $+2.09$ | 6.46 / 4.17 |
| `theta_l_m` at the singles value | 43501.865656 | $+8.52$ | **17.05** |

All seven arms sit outside the couples likelihood's own 95 per cent region for the
pinned coordinate (the smallest ratio is 4.17 against a chi-square(1) critical
value of 3.84), so the band is conservative by construction and this must be read
with the verdict.

### D.3 The alternative couples measure

The mission's stated measure — both spouses placed at the reference leisure bundle
of 35 hours — is reported in full and **not** as a headline level. $I^{0000}$ is
0.370193 raw and 0.361790 equivalized; the fully common state is numerically zero
on both; the preference contribution is $+0.010276$ raw and $+0.008753$
equivalized; and the nested order is **job access above endowments and needs
above earning opportunities**, not the headline order, with the
job-access contribution at 0.2686 equivalized. Its levels are enormous — a raw mean
of about €272,000 a month — and that is the same full-compensation class as the
singles measures that replace the household's own opportunity set with a single
common bundle: a single bundle is worth far less than a whole opportunity set, so
the compensating income is large. Its Gini, 0.36, sits beside the singles
full-compensation measures at 0.32 and 0.33.

**The ordering flip is a fact about the measure, not about the world.** Stripping
the opportunity set to one common bundle leaves the whole environment to flow
through the attained value undamped, and the access channel then dominates. It is
flagged for the economics review and no substantive conclusion is drawn from it.

### D.4 Couples figures

| figure | content |
|---|---|
| C1 | couples welfare distributions across the four principal states, raw and equivalized |
| C2 | the couples decomposition, signed, with bands |
| C3 | singles against couples, side by side |
| C4 | the pooled diagnostic, with the non-exhaustive fully common state shown as such |
| C5 | the male-leisure sensitivity, all seven arms |

These five figures carry the status `COUPLES_PAPER` in the figure audit: they
are *not* in the singles paper set and are never promoted into it, but they are
a paper set in their own right rather than out of scope, which is what the audit
called them before the R-245 close-out. They are complete at PNG, PDF and CSV.
The three couples positive-model figures sit in the same block and are PNG
only, which the audit discloses rather than hides.

---

## Figures and tables

*Every caption below is self-contained: it states the population, whether the
object plotted is observed, model-implied, an external benchmark or illustrative,
whether it covers singles or couples, whether welfare is raw or equivalized, and
the reference convention where one applies. Captions carry no implementation
history. Throughout, **observed sample** means the 1,555 French single-adult
households of the estimation frame (2,275 opposite-sex couple households where a
caption says couples), and **model-implied** means a self-normalised
importance-sampling estimate over the sampled alternatives at the estimated
parameter vector, weighted by the household weight.*

**A note on what the opportunity figures show.** The model does not estimate a
count of jobs available to a person. The economic object is a household-specific
**estimated opportunity distribution** — a density over latent job packages in
employment, hours, occupation and wage. The number of sampled alternatives used
for numerical integration is a computational quantity and is not an economic
number of market opportunities. Accordingly, the opportunity figures in this paper
plot **densities and probability masses, not job draws**: employment opportunity
mass, the hours distribution, the occupation distribution and the wage-opportunity
distribution. Where a future version displays simulated job draws instead, an
equal fixed number is to be drawn from each estimated opportunity distribution and
the caption must read: *"Illustrative draws from the estimated opportunity
distribution. The number of displayed jobs is fixed for visualization and does not
represent the number of jobs available to the individual."*

### The paper set

| # | artefact | caption |
|---|---|---|
| **T1** | `figT1_conceptual` | **The identification problem, schematically.** Two panels, each showing preferences (indifference curves), job access (a density over hours), earning opportunities (wage-offer densities by occupation), the chosen job and the attained money-metric welfare level, for two households. Panel (a): the same preferences under different estimated opportunity environments. Panel (b): the same opportunity environment under different preferences. **Illustrative and schematic**: drawn from stylised parameters chosen for legibility, carrying no estimated quantity on any axis, and not a result. The opportunity objects are densities; no jobs are plotted and no count of available jobs is implied. |
| **1** | `fig01_observed_hours_35h_peak` | **Observed weekly hours, with the statutory band.** Distribution of usual weekly hours in the job actually held, employed members of the observed sample, France 2016, weighted. **Observed only** — no model quantity appears. The shaded band is the statutory $[33.5, 36.5)$ week. |
| **2** | `fig08_coefficients_by_block` | **The estimated coefficients of the final singles model, by economic block.** All 41 estimated coordinates with robust cluster-robust (CR1) 95 per cent intervals, $G = 1{,}555$ households. **Estimated quantities**; the ten pinned coordinates are not shown. Open markers are coordinates resting on an active box bound, which carry no standard error. Intervals are sampling intervals for the parameters, not the integration bands used for welfare. |
| **3** | `fig02_hours_bands_obs_vs_pred` | **Hours-band shares: observed against model-implied.** Observed sample and model-implied shares over the model's twelve hours bins, weighted. Singles. |
| **4** | `fig03_employment_obs_vs_pred` | **Employment rates: observed against model-implied.** Weighted employment rate, all households and separately by sex. Observed sample and model-implied. Singles. |
| **5** | `fig04_occupation_obs_vs_pred` | **Occupation shares: observed against model-implied.** Weighted shares over the four task-based occupation groups plus non-employment. Observed sample and model-implied. Singles. This is the paper's occupation-fit panel; it is **internal**, because the public French occupation classifications cannot be uniquely harmonised to the task-based grouping used here (§9.4). |
| **6** | `fig05_wage_offer_by_occupation` | **The estimated wage-offer density, by occupation.** Fitted log-normal densities of the hourly wage a job *would* pay, one per task-based occupation group, at the sample mean of education and experience, with a common dispersion and occupation-specific locations. **Model-implied opportunity object**, not a distribution of observed wages and not a distribution of realised pay: it is what the estimated offer technology says is available, conditional on a job in that occupation being available. Singles. |
| **7** | `figS6_04_negll_vs_draws` | **The objective against the number of sampled alternatives.** Optimised objective, objective per household, and free-block curvature at $R \in \{50, 100, 200, 400\}$ sampled latent jobs per household, on nested draw sets. **Numerical diagnostic.** Objective levels are *not* comparable across $R$; the panel is read for stability of shape, not level. Singles. |
| **8** | `figS6_05_key_coefficients_vs_R` | **Key estimated coordinates against the number of sampled alternatives.** Movement of the statutory-week peak, the employment level, occupation access by sex, the occupation wage-location shifts and the wage dispersion across $R \in \{50,100,200,400\}$, expressed in units of the $R = 100$ robust standard error. **Numerical diagnostic**, singles. |
| **9** | `figS6_06_participation_vs_draws` | **Participation against the number of sampled alternatives.** Observed and model-implied participation, and the fit error of the participation margin, across $R$. Observed sample against model-implied; singles. |
| **10** | `figW05_welfare_vs_R` | **The welfare decomposition against the number of sampled alternatives.** Baseline inequality and the four channel contributions at $R \in \{50,100,200,400\}$, with only the estimated parameter vector varying — welfare basis, integration support, operators and inversion are the same objects at every rung. **Model-implied**, singles, raw basis, final singles model at the female reference. |
| **11** | `figW01_welfare_distributions` | **The four principal welfare states.** Distributions and Lorenz curves of money-metric welfare — equivalent income at a common reference pay — under own preferences and own environment, reference preferences and own environment, own preferences and reference environment, and both at reference. **Model-implied**, singles, shown on both the raw and the coalition-consistent equivalized basis. The reference convention is the female preference block (primary). These are well-being levels under stated reference conventions; none is a compensating variation. |
| **12** | `figW02_headline_decomposition` | **Preferences against the complete environment.** Signed Owen contributions to the inequality of money-metric welfare, with numerical-integration bands, under both positive models and both reference-preference conventions. **Model-implied**, singles. A contribution is the value of an equalisation operator in a cooperative game: the licensed reading is *equalising this channel across households removes this share of baseline inequality*. Contributions may take either sign and are not shares of a positive total. Bands are eight-scramble jackknife integration precision, **not** sampling confidence intervals. |
| **13** | `figW03_nested_environment` | **The environment, split three ways.** The nested split of the environment contribution into job access, earning opportunities, and household endowments and needs, with numerical-integration bands, under both positive models and both reference conventions. **Model-implied**, singles, raw and equivalized. No ordering is claimed between job access and earning opportunities; the point estimates are printed and the ordering claim is declined (§7.3). Bands are integration precision. |
| **14** | `figE1_matched_pair` | **Same estimated preferences, same observed job, most different estimated opportunities.** Two real single-adult households selected by a rule fixed before any household was inspected: among 19,116 admissible pairs sharing the observed employment state, occupation, hours band and wage quintile, the pair at or below the tenth percentile of preference distance that maximises opportunity distance. Panels: (a) the estimated preference profile; (b) the hours margin of the estimated opportunity density, scaled by the employment opportunity mass; (c) the estimated probability of an offer in each task-based occupation group; (d) the estimated wage-offer density given employment. **Panels (b)–(d) are estimated opportunity distributions, not choice distributions and not job draws**; no count of available jobs is shown or implied. Dashed lines mark the observed job. Households are described by aggregates only; no identifier is plotted. |
| **15** | `figE1R_reverse_pair` | **Same estimated opportunities, same observed job, most different estimated preferences.** The mirror of Figure 14 under the same rule with the axes exchanged. Same panels, same reading: panels (b)–(d) are **estimated opportunity distributions, not job draws**. Households are described by aggregates only. |
| **16** | `figX1_external_hours_lfs_validation` | **External labour-market evidence on hours.** French EU-LFS 2016, all persons aged 20–60 with a reported usual-hours figure (43,767 records), against the final singles model. Panel (a), **external descriptive evidence only**: the share of employed people in each hours band reporting a wish to work more hours, by band. Panels (a) and (c) carry no model quantity on any axis and are not compared with, ranked against, or overlaid on a model prediction — the structural model has no desired-hours or underemployment outcome, so they document context rather than validate anything. The long-hours band is drawn but marked, because wanting more hours at 50-plus is not underemployment. Panel (b): shares of the statutory 35-hour band from three sources — **external benchmark, observed sample, and model-implied** — by sex and pooled. Panel (c), **external descriptive evidence only**: mean desired hours minus mean **actual** hours, by band and sex, positive on every band up to 39 hours and negative only at long hours. Panel (b) is the one validation panel. Validation only: no moment from this source enters the likelihood, and it identifies nothing. The external population is all persons aged 20–60, while the observed sample is single-adult households, so composition differs by construction and no gap here is a prediction error. |
| **17** | `figR01_benchmark_decomposition` | **What a common-choice-set model would have found.** The welfare-inequality decomposition under the final singles model against the same decomposition under a common-choice-set benchmark fitted to the same 1,555 single-adult households, the same priced job packages and the same welfare machinery. **Both sides are model-implied**, singles, and the same four channels are shown on each. Under the benchmark every household faces the same offer environment, so job access and earning opportunities contribute **exactly zero by construction** — those zeros are the benchmark's definition made arithmetic, not estimates that happened to vanish. Raw and coalition-consistent equivalized bases, at the female reference (primary); the male-reference arm is the sensitivity and the two are never averaged. The benchmark is **not a candidate specification and not nested** in the preferred model: it is what a conventional analyst without an opportunity object would have fitted, shown to make the consequence of that omission measurable. Bands are numerical-integration precision, not sampling confidence intervals. |
| **18** | `figG01_nested_geographic_access` | **Inside job access: the geographic split.** The three environment channels, and then the job-access channel split into geographic/local-market access and remaining access, for the 1,555 single-adult households. **Model-implied**, singles, raw and coalition-consistent equivalized bases, at the female reference (primary); the male-reference arm is the sensitivity and the two are never averaged. Shares are **signed and never renormalised**, so a geographic share above 100 per cent means the remaining-access contribution is negative, not missing. The split is a nesting of the decomposition of Figures 12–13, not a re-decomposition: levels one and two are bitwise unchanged. Bands are numerical-integration precision, not sampling confidence intervals. |
| **19** | `figG02_regional_access_environments` | **The same household under different regional job-access environments.** The two real single-adult households of Figure 14, each evaluated under all 24 documented region × urbanisation access environments, with the local unemployment rate at that region's value for the person's own education and sex. Left panels: employment-opportunity mass. Right panels: money-metric welfare, euros per month. **Model-implied and illustrative.** Preferences, sex, age, education, experience, household composition, earning-capacity characteristics and the priced budget are held at their observed values, and the region-dependent budget rule is held fixed, so this is an access counterfactual and no price is recomputed. **This is not a causal region effect**: it is the same person under different estimated access environments, and nothing here identifies what would happen to a person who moved. Because every geographic variable in this specification enters only when the household works, the hours, occupation and wage-offer summaries do not move at all — the whole regional difference is on the participation margin. |

### The couples set

| # | artefact | caption |
|---|---|---|
| **C1** | `figC01_couples_distributions` | **Couples welfare distributions.** Money-metric welfare — equivalent income at a common reference pay — for 2,275 opposite-sex couple households, **model-implied**, on both the raw and the coalition-consistent equivalized basis. Couples carry a single shared preference vector with per-sex coordinates and therefore have no reference-group arm; the reference block is that vector at the couples-medoid arguments. |
| **C2** | `figC02_couples_decomposition` | **The couples decomposition.** Signed Owen contributions of preferences against the complete environment, and the nested split of the environment, for couple households, raw and equivalized. **Model-implied.** Every preference-contribution figure on this panel travels with the male-leisure sensitivity range of §8.4; the environment side is the robust part. |
| **C3** | `figC03_singles_vs_couples` | **Singles and couples side by side, equivalized.** Baseline inequality, the channel contributions and welfare levels for the two household types on the coalition-consistent equivalized basis. **Model-implied.** Singles are the final singles model at the female reference; the male structural-zero arm is a sensitivity and the two are never averaged. Cross-type comparison is licensed here because the four ratified conditions — same real-euro year, same consumption numeraire, common zero convention, and the calibration identity — were evaluated and hold. |
| **C4** | `figC04_pooled` | **Pooled singles and couples, equivalized.** Pooled inequality of money-metric welfare over both household types, with the pooled Owen values shown as a **diagnostic, not a headline**: the pooled fully common state is 39.4 per cent of the pooled baseline because the two type-specific reference bundles differ, so the pooled decomposition is **not exhaustive**. Pooled inequality itself is well defined and is reported. This is an open welfare-reference question, not a numerical failure. |
| **C5** | `figC05_male_leisure_sensitivity` | **The couples male-leisure sensitivity.** Seven pinned refits moving each marginally-recovered male-leisure coordinate to both ends of a deliberately conservative band, and the resulting movement in each welfare quantity. **Model-implied**, couples, raw and equivalized. The sensitivity is concentrated in the preference contribution; sign, the nested order and the welfare levels are unchanged in every arm. This is why couples are a companion and singles the quantitative headline. |

### Supporting and diagnostic figures

| # | artefact | caption |
|---|---|---|
| **AB1–AB3** | `figAB01_leisure_weight_by_age`, `figAB02_mrs_by_age_sex`, `figAB03_hours_band_fit` | **The age-bound diagnostic.** The implied leisure-weight function by sex and age, the marginal rate of substitution by age and sex at a reference bundle, and hours-band fit, comparing the final singles model against an arm with the age block widened fivefold. **Model-implied**, singles. Diagnostic and supporting, not paper figures; §5.5 gives the verdict, which is to retain the model of record. |
| **S6.1–S6.3** | `figS6_01_coefficient_paths`, `figS6_02_coefficient_stability`, `figS6_03_fit_vs_draws` | **Draw-count stability, full detail.** Every estimated coefficient against the number of sampled alternatives, the same normalised by the $R = 100$ robust standard error, and the fit metrics. **Model-implied**, singles. Supporting detail behind Figures 7–9. |

**Completeness.** Every figure in the paper and couples sets is complete at PNG,
PDF and CSV, with one exception that is not an incompleteness: Figure T1 is a
schematic drawn from stylised parameters and carries no data sheet, so it has no
CSV by design and the audit records the exemption by name rather than passing it
silently.

**Two figures the paper does not have, by rule.** No rank, top-$k$ or Brier
statistic is a paper figure: those statistics are structurally degenerate on this
estimator's choice-set construction, for the reason given in §6.2, and the sheet
that carried them is **withdrawn** from the paper set. Its files remain on disk
and its label layer was not refreshed at the integration pass, precisely because
it is not a paper figure. And no ranking or quintile exercise in the
Decoster–Haan style is attempted; that literature is cited in §2 rather than
extended here.

**Tables.** The three tables generated outside the manuscript, each self-contained
on its own sheet, are the headline decomposition table (the only source of
percentages in this paper, §7.2), the external hours validation table (§9.2–§9.3),
and the within-sample wage fit (§9.1). A source map lists every external source,
what it validates, its population and its availability verdict.

---

## Self-check table

*Every numeral in the paper is bound below to a sprint table, figure or record. Paths are
relative to the two repositories: `MNL` = the estimation repository, `JMP` = the manuscript
repository. `SPRINT` abbreviates `MNL/experiments/JMP_SEMINAR_SPRINT`.*

### (a) Abstract and §1 — introduction

| numeral / claim | source |
|---|---|
| 1,555 single-adult households; 101 alternatives; 157,055 rows | `MNL/experiments/JMP_PS1/decision_note.md` §11.2; `SPRINT/decision_log.md` Entry 1 §1 |
| "41 estimated structural parameters"; 51 / 41 / 10 / 2 / 39 | `SPRINT/decision_log.md` Entry 2 (block table); `MNL/.../ps1r222_floor5/ps1r222_s5b_estimation_v1.json` `S8.n_free` |
| the guarded headline sentence, verbatim | `SPRINT/decision_log.md` Entry 8 §3 (emitted by `SPRINT/runs/headline_table/…build_headline_table_v1.py` from the table) |
| environment 89.0–93.7 % (preferred model, two references, two bases); 89.0–96.7 % over all eight rows | `SPRINT/tables/headline_decomposition_v1.csv`, `C_env_over_I00` column |
| job access 14.9 ± 1.1; earning opportunities 20.6 ± 1.6; combined 35.5 ± 0.9 (raw); combined 25.9 ± 0.9 (equivalized) | same, the final-model female-reference rows, `C_acc_over_I00`, `C_earn_over_I00`, `C_acc_plus_C_earn_over_I00` |
| endowments-needs 58.2 ± 1.5; 53.2–68.9 % across rows | same, `C_needs_over_I00` |
| preference share 3.3–11.0 %, constant sign | same, `C_pref_over_I00` |
| $\approx 95$ % residual removal by the coalition-consistent inversion | `decision_note.md` §20.3 |
| equivalization residual 0.071799 = weighted Gini of $1/m$ | `SPRINT/decision_log.md` Entry 7 §5 |
| Figure T1 is a schematic with no estimated numeral | `SPRINT/runs/figT1/make_figT1_v1.py`; figure label `SCHEMATIC — NO ESTIMATED QUANTITY` |

### (b) §2 — literature positioning

| claim | source |
|---|---|
| the four neighbouring literatures and the closest papers | `JMP/docs/JMP_literature_positioning_memo_v3.md` §§1–4 |
| the Decoster–Haan paragraph, verbatim, and its four positioning points | same, §3 "Added at Goal-1 R-227 s11" (deputy text entered verbatim by ruling) |
| the Jacquet–Jia–Thoresen distinctness argument (three differences) | same, §§4, 7 |
| Capéau, Decoster and Dekkers (2016): $\log q(x)=\eta_q'x$ on region, education, age, sex and the type-specific unemployment rate; log-normal wage offer; hours density conditioned on sex alone; **no occupation channel**; no welfare object and no decomposition | `JMP/JMP_literature/03_summaries/T1A/Capeau_et_al_2015_RURO.md` §§3, 5–7; `JMP/JMP_literature/03_summaries/T1A/Capeau_Decoster_2016.md` §5 |
| Aaberge, Colombino and Wennemo (2009) estimate the opportunity measure as **common scalars** $\theta_0,\pi_1,\pi_2$ with no covariates | `JMP/JMP_literature/03_summaries/T1A/Aaberge_et_al_2009.md` §§4b, 5, "no circumstance-varying access" |
| "$\theta g(h)$ is called the opportunity measure" | `JMP/JMP_literature/03_summaries/T1A/Dagsvik_et_al_2014_latent_jobs_arguments.md` p. 141 quotation |
| the non-separate non-parametric identification of $\Psi$ and $g_2(h)$ | `Capeau_et_al_2015_RURO.md` §4, §8 (their p. 157, n. 17) |

### (c) §3 — framework

| numeral / claim | source |
|---|---|
| Box–Cox utility; the four-factor opportunity density; the within-set centring convention | `JMP/manuscript/sections/02_framework.md` §2.1 |
| $\beta_c \equiv 1$; $\beta_{\mathrm{F35}} \equiv 0$; $\beta^{\rm occ}_{1,g}\equiv 0$; $\lambda_\ell = 10$ | same, self-check (a) |
| the restricted preferred model reproduces the benchmark objective to $2.9\times10^{-10}$ | `ps1r222_s5b_estimation_v1.json`, `model_comparison.nesting_on_the_corrected_frame.abs_gap` |
| the welfare family; $W^1$ as carrier; $W^4$/$W^6$ as normative-reference disclosures; the excluded best-paid-equivalent measure | `02_framework.md` §2.3 |
| common quadrature support: domination minimum slack $+3.226$ nats over 3,184,640 comparisons; effective sample size $\approx$ one third higher | `decision_note.md` §21.3, §21.4 |
| support change moved the observed level $-5.53$ % / $-7.74$ % | `decision_note.md` §21.6 |
| the coalition-consistent inversion; every input classified; no undeterminable input | `decision_note.md` §20.1, §20.2 |
| the four cells; "not compensating variation and requires no tax reform"; the level-analogue mapping | `02_framework.md` §2.4 (quoted from the R-202 design record) |
| exhaustiveness rule $|I^{11}|\le0.00125$ and $\le 1\%$ of $I^{00}$ | `decision_note.md` §17.3 |
| earlier failure at $I^{1111}/I^{0000}=3.0288$ / $3.2566$ | `decision_note.md` §19.4 |
| current pass: $I^{11}=0.000\mathrm{e}{+}00$ / $-2.035\mathrm{e}{-}31$ | `SPRINT/decision_log.md` Entry 7 §3 |
| $m\in[1.0,2.9]$, mean 1.163, 1,127 households at $m=1$; naive $I^{11}=0.071799$ = weighted Gini of $1/m$; medoid single person aged 34, $m=1$ | `SPRINT/decision_log.md` Entry 7 §5 |
| defensive mixture 75/25, $\lambda=0.25$; eight scrambles; $t_{0.975,7}=2.364624251$ | `02_framework.md` §2.5 |

### (d) §4 — data

| numeral | source |
|---|---|
| `FR_2016_a3`; 11,459 households; the eight-step waterfall to 1,555; the composition itemisation 930/452/53/21 | `JMP/manuscript/sections/03_data.md` §3.1, Table 3.1 |
| 2,275 couples; 2,236 persons; 4,547,080 represented; Table 4.2 composition | same |
| the parameter count 51 / 41 / 10 / 2 / 39; $k=41$; $K_{\rm interior}=39$ | `SPRINT/decision_log.md` Entry 2 |
| `yivwg` identity at 100.0 %; `wage == yivwg` bitwise on 1,348 rows; the 21 zero-earnings workers | `decision_note.md` §22.2–§22.4 |
| Table 4.3 hours bands and worker counts 34/172/389/436/296 on $n=1{,}327$ | `03_data.md` Table 3.3; `decision_note.md` §22.3 |
| Table 4.4 occupation key and weighted shares 27.5/15.4/9.4/47.6 % | `03_data.md` Table 3.4 |
| occupation composition by sex (38 % of men, 18 % of women in group 1) | `03_data.md` §3.2 |
| wage mean €15.47, median €14.05, range €2.06–€94.76, p01 €3.14, p99 €41.72 | `decision_note.md` §22.3 |
| geography: 22 NUTS-2 régions, cells 3–245, median 53.5, 5 under 30; 8 zones, 122–279; `drgur` 832 / `drgmd` 328 / `drgru` 395; `gsur` 47 values, $[0.053183,0.225]$, mean 0.09451 | `03_data.md` §3.3 |
| missing-region verification: $N=11{,}459$, difference 0, 22 codes, flag count 0, weighted share 0.0000 %, 245 genuine | `03_data.md` §3.3 (rulings document R-210) |
| Corse: three households | `03_data.md` §3.3 |
| `gsur` is the group-specific unemployment rate (external lookup, exclusion-restricted, offer-only) | `MNL/docs/methods/RURO_METHODS_AND_PIPELINE_MANUAL_v1.md` l. 476; `MNL/docs/specifications/RURO_CONTINUOUS_MNL_VARIABLE_DICTIONARY_v1.md`; `MNL/docs/specifications/RURO_model_spec_contract_v4_ruro_occ.md` §20 |
| take-up seed 20162016, rates 0.548 / 0.265, realised 0.542 / 0.292, the mask | `03_data.md` §3.4 |
| the minimum-income pricing convention: full entitlement in the engine, take-up once at assembly, bitwise identical to running with the policy off | `SPRINT/decision_log.md` Entry 5 ("The switch", proofs (a)–(c′)) |
| the couples defect: 1,805 of 2,275 (79.3 %), up to €1,343.52; singles spread exactly 0.0 on all 1,555 | same, "Bug 1", "SINGLES ARE CLEAN" |
| corrected couples frame: 757,904 × 32, gates 6/6, wall 1.46 min | same, "The frame" |

### (e) §5 — estimation and identification

| numeral | source |
|---|---|
| the estimator, the $-\log q$ correction, `exact_marginal` / `deterministic_unit` | `02_framework.md` §2.2; `SPRINT/decision_log.md` Entry 1 §4 |
| CR1: $G=1{,}555$, $c=1.0257255936675462$, $z_{0.975}=1.959963984540054$ | `decision_note.md` §11.1 |
| age-centring exact to $1.38\times10^{-10}$ against a $10^{-8}$ band | `decision_note.md` §1 |
| $\lambda_\ell=40$ re-expression: $+1.0 \to 0.034845$ / $0.055555$; invariance at $6.11\times10^{-16}$, $5.55\times10^{-16}$, $2.17\times10^{-10}$ EUR | `decision_note.md` §2A(b), §1 |
| draw-count rungs $R\in\{50,100,200,400\}$; largest move 0.21 SE ($R{=}400$), 0.20 ($R{=}200$), 0.56 ($R{=}50$) | `SPRINT/runs/drawcount_s6/s6_drawcount_estimation_v1.json`, `rungs.*.parameter_table` |
| participation 0.8708 observed; 0.8660 / 0.8668 / 0.8669 / 0.8665 predicted | same, `rungs.*.fit_suite.employment`; `SPRINT/figures/figS6_06_participation_vs_draws.csv` |
| negLL not comparable across $R$ | same, `comparability.NOT_comparable_across_R` |
| the single common $\beta_E$ disclosure on Figure 8 | `SPRINT/decision_log.md` Entry 8 §4 |
| HP: within-household spread 0.0732 / 0.1270; expected LR 0.0081 / 0.1351 vs 2.706 | `decision_note.md` §26.1, §26.4 |
| HO: loading SD 0.297; axis LR 1.02 / 13.56; $\approx$95 % absorbed; profile LR 0.0492 / 0.6996 vs 2.706 | `decision_note.md` §29.1, §29.4 |
| W3: correlation at the $\pm0.99$ box endpoint; leisure within-set spread 0.073 / 0.127; no valid null reference | `decision_note.md` §30.6, §30.7 |
| HP / HO real data not run, by rule | `decision_note.md` §26.5, §29.5 |
| age-bound diagnostic: box $\pm5\to\pm25$ and $\pm1\to\pm5$; $k$ identical at 41; active set 2 → 0; interior 39 → 41 | `SPRINT/runs/agebound_addendum_s2/ab_step1_estimation_v1.json`, `admissible_region`, `comparison` |
| objective 18022.2124 vs 18022.7646; gain 0.552; twice the gain 1.104; $\Delta$AIC $=\Delta$BIC $=-1.104$; **not** a chi-square statistic | same, `comparison.not_a_likelihood_ratio_test` |
| released coordinates 1.4466 (s.e. 1.036, $z$ 1.396) and 1.7218 (s.e. 0.895, $z$ 1.925) | `SPRINT/runs/agebound_addendum_s2/ab_parameter_movement_v1.csv` |
| largest movement 0.72 SE (`beta_l_nkids_sf`), then $-0.61$ and $-0.43$; F35 2.5795 → 2.5692 | same |
| hours-grid MAE 0.008345 → 0.008269; curvature $+0.442$ → $+0.439$ | `ab_step1_estimation_v1.json`, `comparison`; `SPRINT/runs/agebound_addendum_s2/ab_hours_band_fit_v1.csv` |
| the four-limb rule, declared before the artefacts were read; verdict `RETAIN_S8_CLOSE` failing limb B | `SPRINT/runs/agebound_addendum_s2/ab_verdict_v1.json` |
| released coefficients' 95 % intervals $[-0.584, 3.477]$ and $[-0.032, 3.475]$, both containing $+1.0$ | same, `B_materially_better_objective._freed_coefficients` |
| the implied leisure weight: strictly positive over 20–64, U-shaped, minima 4.55 at age 40 (men) and 4.36 at age 43 (women); endpoints 10.31 / 12.92 and 13.30 / 12.11; MRS minima €11.71 and €28.73 | same, `C_economically_sensible_profiles`; `SPRINT/runs/agebound_addendum_s2/ab_leisure_weight_profile_v1.csv`, `ab_mrs_profile_analytic_v1.csv` |
| 2 of 24 headline welfare quantities leave their band, both $C_{\mathrm{pref}}$ raw, at $+12.8$ % and $+5.2$ %; 6 of 126 over all bases | same, `D_non_negligible_fit_or_welfare_change`; `SPRINT/runs/agebound_addendum_s2/ab_welfare_comparison_v1.csv` |

### (f) §6 — singles results

| numeral | source |
|---|---|
| every coefficient, standard error and $z$ in §6.1 and Appendix A.1 | `SPRINT/figures/fig08_coefficients_by_block.csv` (41 rows) |
| every coefficient in Appendix A.2 | `ps1r222_s5b_estimation_v1.json`, `S0.parameter_table` |
| employment 0.8708 / 0.8668; statutory band 0.2485 / 0.2520 | same, `S8.household_level_predictive_fit` |
| hours-grid MAE 0.0083 (preferred) and 0.0338 (benchmark); the twelve-bin deviations | `SPRINT/model_comparison.csv`, `hours_grid_mae`; `ps1r222_s5b_estimation_v1.json`, `hours_grid` |
| occupation largest deviation 0.0070; wage-quintile largest deviation 0.0532 and the five quintile deviations | `ps1r222_s5b_estimation_v1.json`, `S8.occupation_and_wage_fit` |
| rank median 101, top-1/5/10 = 0.000, Brier 1.0229; the comparability rule | same, `scale_caveat`; `SPRINT/decision_log.md` Entry 1 §5 |
| the figure was withdrawn from the paper set | `SPRINT/figures/figure_index_paper_v1.csv`, row `fig06_chosen_rank_topk` |
| $\beta_{h,\rm F35}=2.5795$, s.e. 0.0983, $z$ 26.24; LR 861.42; $\Delta$AIC $-859.42$; $\Delta$BIC $-854.07$ | `ps1r222_s5b_estimation_v1.json`, `model_comparison.corrected` |
| $\delta_{\rm occ}$ estimates $-0.048$ / $+0.047$ / $+0.274$ | `fig08_coefficients_by_block.csv` |
| dropping $\delta_{\rm occ}$: $+49.888$ objective; `beta_w_educH` $0.15127\to0.33039$ ($+6.0$ SE); `beta_occ_4_f` $0.71695\to0.91515$ | `decision_note.md` §16.11 |
| the hours-conditioned wage location: $\Delta$AIC $-10.161$, $\Delta$BIC $+11.236$ / $+29.697$; $\delta_{h,\rm short}=+0.19034$ ($z$ 2.01), $\delta_{h,\rm lh}=-0.08460$ ($z$ $-2.57$); wage-quintile MAE $0.021761\to0.021830$; five of seven metrics degrade | `decision_note.md` §16.10–§16.13 |
| benchmark statutory-band prediction 0.0546 | `SPRINT/model_comparison.csv`, row `S0`, `f35_pred` |
| the preference-contribution factor of about two between the two specifications | `SPRINT/tables/headline_decomposition_v1.csv`, `C_pref_over_I00` |

### (f2) §6.7 — the common-choice-set benchmark

| numeral | source |
|---|---|
| benchmark objective 18,151.85 against 18,022.76; gap 129.1 nats; 16 free parameters against 41 | `SPRINT/runs/rum_benchmark_final/rb_step1_estimation_v1.json`, `step6_nesting.variants.RUM_B` |
| likelihood-ratio 258.2 on 25 degrees of freedom, reported as an **upper bound** | same, `LR_statistic_2x_negll_gap`, `df`, `statistic_is_an_upper_bound` |
| AIC 36,127.5 against 36,335.7; BIC 36,346.8 against 36,421.3; per-household log-score gap 0.083 | same |
| fit mean absolute deviation: hours 0.0080/0.0083, occupation 0.0029/0.0034, wage quintiles 0.0203/0.0261, employment 0.0042/0.0041 | `SPRINT/runs/rum_benchmark_final/rb_step2_fit_comparison_v1.csv`, `__summary__` rows |
| hours-band constants recovered as tastes: mean absolute difference 0.037, maximum 0.075; fixed cost of work $+0.517$ against $-3.334$ | `rb_step4_misclassification_v1.json`, `positive_side_misclassification` |
| male-minus-female leisure intercept gap $+0.428$ against $-1.991$ | same, `sex_specific_leisure_block.leisure_intercept_gap_male_minus_female` |
| baseline inequality 0.101841 against 0.134277 raw ($-24.2$ %) and 0.139869 against 0.165105 equivalized ($-15.3$ %) | `SPRINT/tables/rum_benchmark_decomposition_v1.csv`; `rb_step4_misclassification_v1.json`, `relative_change_in_measured_inequality` |
| preference share 6.4 % against 6.3 %; difference $+0.1$ points against a band of $\pm 0.4$ | same, `s_pref`, `M_share` |
| the three destinations of the omitted market-side share | same, `fraction_of_O_to_preferences`, `fraction_of_O_to_endowments_needs`, `fraction_of_O_leaving_the_total`, over the four arms |
| job access and earning opportunities exactly zero under the benchmark | `rum_benchmark_decomposition_v1.csv`, `C_acc`, `C_earn` on every `RUM_B` row |

### (g) §7 — welfare

| numeral | source |
|---|---|
| **every percentage in the paper** | `SPRINT/tables/headline_decomposition_v1.csv` (8 rows × 97 columns), mirrored at `headline_decomposition_v1.md` |
| the four principal states with bands | `SPRINT/decision_log.md` Entry 7 §3 |
| exhaustiveness at $0.000\mathrm{e}{+}00$ / $-2.035\mathrm{e}{-}31$; identities at machine precision | same |
| $I^{10}>I^{00}$ in all four arms; the Owen second-term explanation | same, Entry 7 §3 |
| attribution to $\hat\theta$: both legs reproduce the pre-correction numbers bitwise ($0.000\mathrm{e}{+}00$); movement $-0.0164$ % / $-0.0075$ % | same, Entry 7 §2 |
| the ratio and sum bands; the $C_{\mathrm{acc}}+C_{\mathrm{earn}}$ band $\pm0.95$ narrower than $\pm1.10$ and $\pm1.63$ | same, Entry 8 §2 |
| the bitwise gate on 1,284 numbers, 0 differ; wall 21.4 min | same, Entry 8 §1 |
| the emitted headline sentence and its guard | same, Entry 8 §3 |
| the interpretation discipline, quoted | same, Entry 8 §3 (final paragraph) |
| raw against equivalized: $I^{00}$ $+22.96$ %; mean $W^1$ €1,384.1 → €1,265.7 | same, Entry 7 §6 |
| the calibration identity at $4.4\times10^{-13}$; raw reference recovery $3.5\times10^{-10}$ EUR | same, Entry 7 §6, §7 |
| the child term carries 3.7 % / 7.3 % of the female–male gap | `decision_note.md` §21.9; `JMP/manuscript/sections/08_limitations.md` §8.3 |
| the draw-stability ladder table; the male-arm $C_{\mathrm{pref}}$ exception, range $1.019\times10^{-3}$ against band $7.08\times10^{-4}$, ratio 1.44 | `SPRINT/decision_log.md` Entry 7 §8; `SPRINT/runs/final_singles_welfare/ss9_welfare_vs_R_v1.csv`; `SPRINT/figures/figW05_welfare_vs_R.csv` |
| the cache-independence test: 7 of 2,236 rows differ in `lhw` only; policy-written columns removed → bitwise equal for all 1,555; the assembled input frame bitwise identical on 11,480 rows while the template differs on 140 | same, Entry 7 §1 |
| the anchor / consumption-scale disclosure: $-1.402\times10^{-4}$ on 1774.5182, relative $7.9\times10^{-8}$ | same, Entry 7 §1 |
| the check battery: 3,184,640 finite stochastic rows, monotone inversion, utility range exactly 0 at the fully common state | same, Entry 7 §7 |
| the child-count open item, 1,357 of 1,555 (87 %) | same, Entry 7 §7 |
| Figure E1: 19,116 admissible employed pairs; $d_{\rm pref}$ 0.038 vs median 0.783; $d_{\rm opp}$ 0.442 vs 0.213, separation 2.08×; the two household profiles; reverse $d_{\rm pref}$ 3.466, separation 4.42×, $d_{\rm opp}$ 0.034; same-sex-restricted 2.935; non-employed forward $d_{\rm pref}$ exactly 0.000 with $d_{\rm opp}$ 0.540 | same, Entry 8 §5; `SPRINT/runs/figE1_matched_households/e1_matched_households_v1.json` |
| the hours-index structural disclosure (no household-specific coordinate) | same, Entry 8 §5 |

### (g2) §7.9 — the geographic split of job access

| numeral | source |
|---|---|
| geographic access 0.017528 ± 0.000887 raw and 0.016289 ± 0.000831 equivalized; other access 0.002476 ± 0.000891 and $-0.000307$ ± 0.000489 | `SPRINT/tables/nested_geographic_access_v1.csv`, female-primary rows |
| geographic share of job access 87.62 % ± 3.89 raw and 101.92 % ± 3.11 equivalized; male-reference 90.13 % ± 4.16 and 105.71 % ± 3.33 | same, `C_geo_share_of_C_acc` |
| geographic share of baseline inequality 13.05 % ± 0.74 raw and 9.87 % ± 0.55 equivalized; male-reference 12.24 % ± 0.65 and 9.13 % ± 0.47 | same, `C_geo_over_I00` |
| other access runs $-0.49$ to $+1.84$ per cent of baseline across the four rows | same, `C_oth_over_I00` |
| the reading, verbatim apart from the audience-facing model name | generated by `SPRINT/runs/geo_nested_access/build_gn_table_v1.py` from the table |
| $C_{\mathrm{geo}} + C_{\mathrm{oth}} = C_{\mathrm{acc}}$ to $0.0$, and levels one and two bitwise unchanged on all 44 numbers | `SPRINT/runs/geo_nested_access/gn_step2_nested_v1.json`, `identity_2_...`, `identity_level_1` |
| the two sub-players' argument slots, and the sex-only occupation conditional | same, `step1.GEO_columns`, `step1.OTH_columns` |
| employment-opportunity mass 0.768–0.858 and 0.655–0.809; welfare €1,736–1,837 and €1,301–1,333; ratios 1.058 and 1.025 | `SPRINT/figures/figG02_regional_access_environments.csv`; `gn_step3_illustration_v1.json` |
| 24 access environments, 48 profile-by-environment cells; hours, occupation and wage-offer summaries each take one value per profile | same, `structural_constancy_under_a_geographic_counterfactual` |

### (h) §8 — couples

| numeral | source |
|---|---|
| 2,275 households × 101 joint alternatives; 46 free, 12 pinned; the three named absences | `SPRINT/decision_log.md` Entry 6 |
| objective 43493.342239; spread $1.353\times10^{-9}$; minimum eigenvalue $+0.1105$; one active bound; $G=2{,}275$, $K_{\rm interior}=45$ | same; `SPRINT/runs/couples_clean_baseline/r240_step3_estimation_v1.json` |
| the two recovery gates (42/4/0 and 38/8/0); the three MARGINAL male-leisure coordinates at 0.78 / 0.85 / 0.65 SE | `SPRINT/decision_log.md` Entry 6 |
| the pre-registration error and its correction; observed median $\mathrm{mean}|z|$ 0.773 against 0.798 | same |
| all fit numbers in §8.3 | `r240_step3_estimation_v1.json`, `fit` |
| the per-spouse 35-hour peaks 3.2915 and 2.5474 with $z$ 32.20 and 34.66 | same, `fit.f35_peak_vs_singles` |
| all coefficients in Appendix D.1 | `SPRINT/runs/couples_clean_baseline/r240_step3_parameter_table_v1.csv` |
| the couples common support and its gates | `SPRINT/decision_log.md` Entry 9 §3 |
| the four principal states and the constant fully common vector at €1,713.16 | same, Entry 9 §7 |
| the exhaustiveness audit: 23 arguments, job access 11 / earning opportunities 6 / preferences 5 / endowments and needs 1, 0 unassigned | same |
| the couples decomposition, both bases, with intervals | same |
| levels: raw mean €1,836.8 / median €1,761.8; equivalized €972.7 / €921.5 | same |
| the directional difference from singles | same |
| the sensitivity arms table and the material verdict (29 of 140; $C_{\mathrm{pref}}$ 73.1 %) | same, Entry 9 §8; `SPRINT/runs/final_couples_welfare/cw_step3b_sensitivity_table_v1.csv` |
| the $C_{\mathrm{pref}}$ range 0.0014–0.0075 around 0.0052 | same, Entry 9 §8 |
| the four cross-type conditions; the calibration identity at $1.11\times10^{-14}$ | same, Entry 9 §9 |
| the pooled states; $I^{1111}$ 39.4 % of $I^{0000}$; references €1,251.25 and €951.75, ratio 0.761; pooled mean €1,107.5; the pooled Owen values | same |
| couples worse off at every quantile: €698/€823, €922/€1,242, €973/€1,266; $+33$ % raw against $+65$ % scale; mean $m$ 1.92 against 1.16 | same, Entry 9 §9 |
| the child-count open item, 1,755 of 2,275 (77.1 %) and 93.8 % | same, Entry 9 §7 |
| Appendix D.3 (the alternative measure): $I^{0000}$ 0.370193 / 0.361790; $C_{\mathrm{pref}}$ $+0.010276$ / $+0.008753$; order $A>D>B$; $C_{\mathrm{acc}}$ 0.2686; raw mean €271,748; Gini 0.36 beside 0.32 and 0.33 | same, Entry 9 §7 |

### (i) §9 — external validation

| numeral | source |
|---|---|
| within-sample wage fit: observed / model-implied medians 14.07 / 13.79 (all), 14.70 / 13.84 (men), 13.40 / 13.74 (women); median fit $-0.86$ men and $+0.34$ women; means 15.52 / 15.19, 16.03 / 15.22, 15.05 / 15.17 | `SPRINT/tables/wage_fit_within_sample_v1.csv`, emitted by `SPRINT/runs/external_hours_lfs/build_wage_fit_v1.py` |
| no matched employer–employee file: 14 files, 4 EU-SILC and 10 EU-LFS, 0 DADS or SES | `SPRINT/runs/external_hours_lfs/xh1_table_record_v1.json`, `priority_2_ses_dads_wages`; `SPRINT/tables/external_source_map_v1.csv` |
| 43,767 EU-LFS 2016 records aged 20–60; the band partitions coincide on integer hours; the model side reproduces the hours-fit figure to $5.6\times10^{-17}$ | `xh1_table_record_v1.json`, `lfs_source`, `band_alignment_finding`, `gate_fig02_reproduction` |
| relative offer weights 0.86 / 0.09 / 0.13 / 0.12 against the statutory band | same, `opportunity_weights` |
| the statutory band at 37.2 % (external), 34.3 % (observed sample), 34.6 % (model-implied); women 40.6 % vs men 34.6 % external, 36.7 % vs 32.4 % model-implied | `SPRINT/figures/figX1_external_hours_lfs_validation.csv`, panel b |
| the gap profile $+8.2$ / $+3.7$ / $+1.6$ / $+0.9$ / $-1.5$ hours, desired minus **actual** within the band | `SPRINT/tables/external_hours_validation_v1.csv`, `lfs_desired_minus_actual_hours`, pooled; built by `SPRINT/runs/external_hours_lfs/build_xh2_moments_v1.py` from moment M1 |
| the superseded band-bound proxy (6.5 / 3.1 / 0.1 hours over each band's upper edge), retained as the earlier reading | `xh1_table_record_v1.json`, `desired_hours_excess` |
| the gap is positive on every band up to 39 hours, falls monotonically, and is larger for men than for women in all four | `xh2_moments_record_v1.json`, `moment_agreement`; `SPRINT/figures/figX1_external_hours_lfs_validation.csv`, panel c |
| the statutory share 37.3 % one year earlier, same sex ordering, no band moving more than 0.9 points | `xh2_moments_record_v1.json`, `m5_2015_mirror` |
| the paragraph, verbatim apart from the audience-facing relabelling and the resolved underemployment clause | `SPRINT/runs/external_hours_lfs/xh_paper_paragraph_v1.md`; `SPRINT/decision_log.md`, the integration-pass entry |
| the alternative-weight-not-share and no-interval disclosures; the legacy band-edge trap; the 20-of-24 bitwise gate | `SPRINT/decision_log.md` Entry 10 §§1–3; `xh1_table_record_v1.json`, `band_alignment_finding`, `gate_fig02_reproduction` |
| the long-hours decoupling and why the long-hours band is held out of the rank statistic | `SPRINT/decision_log.md` Entry 10 §6 |
| the hours-band coordinates are not sex-specific | `xh1_table_record_v1.json`, `opportunity_weights_are_not_sex_specific` |
| the contaminated residual bucket, and that the special code is 97 % of the mass above 70 hours | `xh1_table_record_v1.json`, `contamination`; `xh2_moments_record_v1.json`, `m3_special_codes` |
| the panel does carry the non-employed (25.8 % weighted, ages 20–60); the bucket the export *named* non-employed is 675 employed people with unreported hours | `xh2_moments_record_v1.json`, `m4_employment_base` and `label_notes` `XH2-LABEL-2`; the earlier `NOT_A_NON_EMPLOYMENT_RATE` reading is superseded in place in `SPRINT/tables/external_hours_validation_v1.md` |
| the delivered `wants_more_hours` field carries code 1 (No) and is the complement of its own name | `xh2_moments_record_v1.json`, `label_notes` `XH2-LABEL-1` and `wishmore_inversion_check`; checked, not asserted — the builder refuses to write unless the field reproduces the code-1 share on all seven bands |
| the moments reached this side as a transcription; 2 of 168 comparable cells drift, worst 0.09 of an hour | same, `sources` and `transcription_drift` |
| underemployment coding $1 =$ No, $2 =$ Yes (EU-LFS codebook, 8 July 2021); full coverage on all 15 focal cells | `xh1_table_record_v1.json`, `wishmore_coverage_finding`; the coding direction is ruled, not inferred from the delivered export, whose own note is superseded |
| 20.3 % of the employed wish more hours over the five priced bands | same, `wishmore_verdict.what_the_reversed_map_implies.implied_share_wishing_more_over_the_five_focal_bands` $= 0.20285744$ |
| the by-band gradient 46.6 / 37.5 / 23.7 / 19.8 / 7.6 per cent | `xh2_moments_record_v1.json`, `m2_pooled_only.code_2_share_all_bands` (moment M2, delivered pooled only — there is no sex split to publish or to suppress) |
| 22.9 % across all employed persons aged 20–60 | same, `m2_pooled_only.code_2_share_over_all_employed_persons` — moment M2 over the employed denominator moment M4 supplies |
| occupation fit: largest deviation seven-tenths of a percentage point over five categories | `SPRINT/figures/fig04_occupation_obs_vs_pred.csv` |
| the BMO permitted sentence and the mapping disclosure (0.5837 / 0.3799 / 0.0324 / 4 codes at 0.40 %; correlations 0.62 and 0.66) | `decision_note.md` §15.9, §15.10, §15.15, §21.9; `08_limitations.md` §8.2 |

### (j) §10–§11 and the appendices

| numeral / claim | source |
|---|---|
| every limitation in §10.1–§10.4 | `JMP/manuscript/sections/08_limitations.md` §§8.1–8.5, updated for the closures in §5.4 and §5.5 |
| the ten clipped households (3 cap, 7 floor); exactly 7 chosen rows changed; 0 drawn changes; largest move 0.0213 previous SE | `decision_note.md` §23.1(b), §25.2, §25.6 |
| the eleven documentation fields (7 unavailable, 3 partial); non-worker wage inert bitwise over 15,814 rows | `decision_note.md` §22.1, §22.5 |
| 934 multi-adult households and the five unstated assumptions | `MNL/experiments/JMP_PS1/runs/ps1sx_sample_audit/audit_note_v1.md` §5 |
| the six parked extensions, none identifying anything | `SPRINT/decision_log.md` Entry 1 §3 (R-233 §12 parked list); §9 above for the two that have partly returned |
| Appendix B, all seven rows | `decision_note.md` §17.3, §19.1, §19.4, §20.1, §20.3, §21.3, §21.6, §21.7, §21.9; `SPRINT/decision_log.md` Entry 7 §§1, 3, 5 |
| Appendix C, singles support gates V1–V7 and effective sample sizes | `decision_note.md` §21.3, §21.4 |
| Appendix C, couples support gates C4–C12 and the slot arithmetic | `SPRINT/decision_log.md` Entry 9 §3 |
| Appendix C, pricing: 4,347,525 rows in 27.2 min; the alone-vs-mixed invariance; the reference-profile probe; the 87,160 floored rows (1.87 %) | same, Entry 9 §5 |
| Appendix C, the engine-ready gate at maximum absolute difference 0.0 and the exact objective reproduction | same, Entry 9 §6 |
| Appendix C, the $\log S$ trap (~€37/month) and the closed-form checks at $1.9\times10^{-15}$ / $3.6\times10^{-15}$; the chosen-flag inertness at $7.1\times10^{-15}$ | same, Entry 9 §7 |
| Appendix C, the CSV round-trip defect (131 cells) and the register discipline | same, Entry 8 §7 |
| Appendix C, JAX CPU 20.9 s against Torch CUDA 56.2 s; the two missing generic capabilities | same, Entry 3 |
| the figure set, and why no audit count is quoted | `SPRINT/figures/figure_index_paper_v1.csv` (paper set), `figAB_index_agebound_addendum_s2_v1.csv`, `figX_index_external_hours_v1.csv`, `figW_index_final_singles_welfare_v1.csv`, `figC_index_final_couples_welfare_v1.csv`; the deferral of the whole-directory refresh is `SPRINT/decision_log.md` Entry 10 §9 |

### (k) Claim discipline — observed prohibitions

| prohibition | how it is observed |
|---|---|
| the exact table is the only source of percentages | every percentage in §1, §7 and §11 is read from `headline_decomposition_v1.csv`; no percentage is computed in prose |
| no "job opportunities explain $X$ %" | the licensed form — *equalising channel $X$ removes $Y$ % of baseline money-metric inequality* — is used throughout and is stated as a rule in §7.3 |
| no causal 35-hour language | the coefficient is named an institutionally motivated opportunity peak in §3.2, §4.2, §6.3 and §9; no counterfactual removing the statute exists anywhere |
| no job-access-versus-earning-opportunities ordering claim | §1.3 and §7.3 print the point estimates and explicitly decline the ordering; the standing non-identification of the access density is stated with it |
| couples numbers only with their sensitivity qualifier | §8.4 states the rule; the $C_{\mathrm{pref}}$ range 0.0014–0.0075 travels with every couples preference figure; §1.3, §8 and §11 say singles are the headline |
| "not statistically indistinguishable from zero" never used | the phrase is never used as a claim about any quantity; §7.3 point 2 records the prohibition and its reason, and §6.1 describes wide coefficients by whether their interval covers zero rather than by a null claim |
| MC bands are integration precision | stated in the drafting note, §3.6, §7.3 and §10.2; no band is described as a confidence interval anywhere |
| no unqualified "ability"; $A_i$ reserved | §3.1 fixes the four terms; $A_i$ appears only in the reserved sense and in the non-identification sentence |
| the non-identification sentence travels with the access channel | §1.2, §3.1, §7.3 and §10.1 |
| no cell described as a compensating variation | §3.4 states the prohibition and quotes the governing ruling |
| no cross-measure quantitative robustness claim | $W^4$/$W^6$ appear only as normative-reference disclosures (§3.3) and in Appendix D.3 as a measure fact |
| no intra-couple welfare statement | §8.5 states it explicitly |
| no Corse-specific statement | §4.3 records the disclosure; none is made |
| no internal specification or run label in the main text or on a figure | §1–§11 and every figure label layer are grep-clean of the internal labels; they survive only in the technical appendices, behind the legend at the head of Appendix A, and in the drafting note, which is stripped at final |
| no external-vs-sample gap called a prediction error | §9 opens with the rule and §9.1 restates it for the earnings comparison that is not yet available |
| external occupation composition is not a validation result | §9.4 states the three consequences; the occupation panel is the internal fit of §6.2, and the crosswalk audit is cited as reproducibility evidence only |
| the external sources identify nothing | §9 preamble, §9.2 and §9.3 each say so; no moment from any external source enters the objective |
| no count of available jobs is claimed or plotted | the note at the head of the figure section fixes the rule; the opportunity figures plot densities and probability masses, and Figures 14–16 say so on their face |
| no rank, top-$k$ or Brier statistic, and no Decoster–Haan-style ranking exercise | §6.2 gives the structural reason and the sheet is withdrawn from the paper set; the ranking literature is cited in §2 and not extended |

### (l) Open placeholders

| placeholder | what is missing | where it goes |
|---|---|---|
| the external earnings comparison | a matched employer–employee source (DADS / Base Tous Salariés); none is available without a new secured session and a new data request. §9.1 reports the within-sample wage fit and fixes in advance the framing the comparison will be read under | §9.1, `[PLACEHOLDER — the DADS wage comparison]` |
| the matched-pair re-selection | the opportunity-distance ranking behind Figures 14–15 omits the region term (§7.8). A repaired builder is specified and has **not** passed its own proof, so the pair is not re-selected. No number in §7 depends on it | §7.8 carries the disclosure; the figures stand as selected |
| parameter-uncertainty propagation and subgroup decompositions | propagation of estimation uncertainty in $\hat{\theta}$ through to the welfare functionals, and decompositions within sex and other subgroups. Not run. §3.6 and §10.2 already state that the reported bands are integration precision and that sampling uncertainty is **not** estimated in this paper; that statement stands unchanged | §10.2 states the limitation; no interval is reported in its place |

**Closed at this pass.** The geographic split of job access has returned and is
reported in §7.9 with its own table, its generated reading and two figures; the
placeholder is discharged and no share is quoted that is not in that table.

**One placeholder closed earlier.** The underemployment axis is no longer
open: the coding direction of the labour-force wish-to-work-more variable was
settled against the EU-LFS codebook (version of 8 July 2021, $1 =$ No, $2 =$ Yes),
and §9.3 now reports it as external evidence on hours constraints. The bounded
follow-up moments have since landed as well, and §9.3 carries them: mean actual
usual hours by sex and band turn the earlier one-sided bound into the gap itself,
and that gap has the same monotone profile as the wish-more share, so the coding
now rests on a corroborating moment and not on documentation alone. What remains
outstanding on this axis is provenance rather than evidence — the moments reached
this side as a transcription of the secured-session export, and the exported file
should replace it when it travels.

---

*End of paper. Every welfare and decomposition magnitude above carries
`FINAL_SINGLES_PROVISIONAL_PENDING_ECONOMICS_REVIEW` or
`FINAL_COUPLES_PROVISIONAL_PENDING_ECONOMICS_REVIEW` on its own artefacts, as the
drafting note records.*
