# Unequal Job Opportunities and the Measurement of Welfare Inequality
## Seminar deck — slide-by-slide content

**This is a content document, not slides.** It fixes what each slide says, what it
carries, what is said over it, and how long it takes. Typesetting is a separate
job and nothing here presumes a template.

**Assumed length: a 45-minute seminar slot.** The plan below budgets **38.5 minutes
of delivered content across 20 slides**, leaving **6.5 minutes of slack** for
interruption, which in this audience is where the value is. Do not plan to fill
the slack.

**A 25-minute version is marked throughout.** Each slide carries a `25-MIN`
disposition: `KEEP`, `KEEP (compressed, X min)`, `MERGE`, or `CUT → backup`. The
compressed plan is **23 minutes across 15 slides**, leaving 2 minutes of slack.
The cuts are listed once at the end so they can be applied without re-reading.

**Terminology.** Audience-facing throughout: *final singles model*, *observed
sample*, *model-implied*, *job access*, *earning opportunities*, *household
endowments and needs*, *preferences*. No internal specification or run label
appears on any slide. The channel names are words; the letters are not used.

**Numbers.** Every number on every slide traces to a named artefact. The
provenance table at the end lists them in one place. **No number appears on a
slide that is not in that table**, and the decomposition percentages come from
the exact table and nowhere else.

---

# Part I — The question (slides 1–5, 9.5 min)

## Slide 1 — Title

**Message.** A money-metric welfare decomposition that separates what people want
from what they can get.

**Carries.** Title, name, affiliation, date. Sub-line: *France 2016, EU-SILC
priced through EUROMOD.*

**Speaker notes.** Twenty seconds. Say the one-sentence version of the paper and
move: *"I estimate a labour-supply model in which each household faces its own
distribution of available jobs, and then I ask how much of welfare inequality is
about preferences and how much is about the environment people face."* Do not
preview the answer yet; slide 2 earns it.

**Timing.** 0.5 min. **25-MIN: KEEP (0.5).**

## Slide 2 — Two people, the same job, different reasons

**Message.** The same observed choice is consistent with opposite explanations,
and standard models resolve the ambiguity by assumption rather than by evidence.

**Carries.** No figure. Two short vignettes in text: two single adults, both
working 40 hours in the same occupation in the bottom wage quintile.

**Speaker notes.** This is the motivating slide and it should be told, not read.
Two people make the same choice. One had a wide range of jobs open and picked
this one; the other had almost nothing else available. A model that puts both on
a common budget set must book the entire difference as *taste* — and will then
report that they are equally well off, or that the second one simply prefers what
she has. That is not a measurement error at the margin; it is the central
identification problem in applied welfare analysis of labour supply. Land the
sentence: **whatever the choice set cannot express, the taste parameter absorbs.**

**Timing.** 2.0 min. **25-MIN: KEEP (compressed, 1.0) — one vignette, not two.**

## Slide 3 — What the model has to separate

**Message.** Preferences and opportunities are separately meaningful objects, and
the paper's job is to estimate both rather than assume one away.

**Carries.** **Figure T1** — the conceptual schematic. Panel (a): same
preferences, different estimated opportunity environments. Panel (b): same
opportunity environment, different preferences.

**Speaker notes.** Walk the panels slowly; this is the only slide where the whole
argument is visible at once. Say explicitly what the figure is: **a schematic,
drawn from stylised parameters, with no estimated quantity on any axis.** Say
what the opportunity object is and what it is not — it is a *density over latent
job packages*, not a list and not a count. Pre-empt the question that always
comes: *no, the model does not estimate how many jobs a person has; the number of
sampled alternatives is a numerical-integration quantity and carries no economic
content.* Flag that slide 14 shows the same two-panel structure on two real
households.

**Timing.** 2.5 min. **25-MIN: KEEP (compressed, 2.0) — panel (a) only.**

## Slide 4 — Why random opportunities rather than a common choice set

**Message.** A common-choice-set model can fit these data; it cannot represent
the question, because the object that would answer it has been assumed constant.

**Carries.** No figure. A two-column contrast: *common-choice-set model* against
*random-opportunity model*, on four rows — what varies across households, where
unexplained variation goes, what welfare comparison is available, what is
identified.

**Speaker notes.** Be fair to the alternative: a common-choice-set model is not
wrong, it answers a different question, and it is cheaper. The point is
structural. If every household faces the same set, then differences in observed
choices *must* load on preferences, and a welfare measure built on it inherits
that. Then give the paper's own internal evidence rather than an assertion — and
this is the strongest positive-side argument in the paper, so do not rush it.
When the occupation term is removed from the earning-opportunity block, the
effect does not vanish: it **relocates**, with the tertiary-education loading
moving by six standard errors and the female nonroutine-cognitive access
coefficient moving with it. The same variation gets booked to whichever channel
the model leaves open. That is a channel-separation result, and it is exactly
what a decomposition has to get right.

**Timing.** 2.5 min. **25-MIN: KEEP (2.0) — keep the relocation result; it is the
argument.**

## Slide 5 — What the opportunity distribution is made of

**Message.** Availability is four estimated factors — whether work is available,
at what hours, in which occupation, and at what pay — and they are estimated
jointly with preferences in one likelihood.

**Carries.** A four-box diagram: job access · hours · occupation · wage offer.
Under it, one line: *estimated jointly with Box–Cox preferences in a single
likelihood; the decomposition later groups these as job access, earning
opportunities, and household endowments and needs.*

**Speaker notes.** Name each factor and what varies with the household: access
varies with the group-specific unemployment rate, region and urbanisation;
occupation availability is sex-specific; the wage-offer location varies with
education and experience and shifts by occupation. Say the honest structural
caveat here rather than burying it: **the hours factor carries no
household-specific coordinate**, so household variation in the offer density
lives in the participation margin, the occupation weights, and the wage location
— and nowhere else. Saying that yourself, early, is worth more than being asked.

**Timing.** 2.0 min. **25-MIN: KEEP (compressed, 1.0) — the four boxes and the
hours caveat, nothing else.**

---

# Part II — How it is estimated (slides 6–9, 8.5 min)

## Slide 6 — Data and the sampled-job estimator

**Message.** 1,555 French single-adult households, each given its observed job
plus 100 drawn latent jobs, estimated by conditional logit with the standard
sampling correction.

**Carries.** A single schematic of one household's choice set: the observed
package, plus drawn packages, each priced. Sample line: *EU-SILC / SRCV 2016;
1,555 households; 101 alternatives each; 157,055 priced rows.*

**Speaker notes.** One slide, and deliberately no certification detail — no gate
counts, no convergence protocol, no hash. The job space is continuous in wage and
hours, so the choice set is sampled rather than enumerated, and the
sampling-of-alternatives correction is what makes the sampled-set likelihood
consistent for the full-set parameters. Say the one consequence the audience will
otherwise trip on: because the observed row is inserted deterministically and the
drawn rows carry a proposal correction, **within-set rank and top-k statistics are
structurally degenerate here** — they are not reported, and their absence is a
property of the estimator, not a weakness being hidden. If asked about the
technical layer, point to the appendix and move on.

**Timing.** 2.0 min. **25-MIN: MERGE with slide 7 (2.5 combined).**

## Slide 7 — Pricing: what a job is worth

**Message.** Every job package is run through the tax–benefit system, so
consumption is computed rather than surveyed — and the mapping is deterministic.

**Carries.** One worked example: a household, a package (hours × wage), and the
disposable income the system returns.

**Speaker notes.** This is the slide that makes the counterfactual legitimate, and
it is worth two clean minutes. EUROMOD is arithmetic: the same household, hours
and wage always return the same euro figure. **Nothing in the estimation
simulates a tax–benefit outcome.** All the randomness in the pipeline is in
*which* points get evaluated, never in what a point is worth. That is what lets
the model price a job the person did not take. Mention take-up once — the
minimum-income benefit is granted in full inside the engine and take-up is
applied afterwards as a household trait — and say why: take-up is a property of
the household, not of the batch it was priced in.

**Timing.** 2.0 min. **25-MIN: MERGE into slide 6.**

## Slide 8 — Identification: what is pinned, and what stays conditional

**Message.** The positive model is estimated and stable; two things about it
remain conditional, and both are stated as limits rather than defended.

**Carries.** A short table: *what the data pin* (the four availability factors,
the preference block, the statutory-week peak) against *what stays conditional*
(access versus capability; persistent household heterogeneity).

**Speaker notes.** Two conditional items, said plainly. First, **the access margin
does not separate what a person is capable of from what the market offers them**
— the estimated access density may combine both, and this paper claims no
ordering between the job-access and earning-opportunity channels in either
direction, even though the point estimates order them and are printed. Second,
the model carries no persistent household-level term, and slide 9 is why. Say the
general disclaimer once, here: the decomposition is **structural and
model-conditional, and it is not causal.**

**Timing.** 2.0 min. **25-MIN: KEEP (2.0) — add one sentence of slide 9's lesson.**

## Slide 9 — The loading principle: three closed lanes, one design rule

**Message.** Three pre-registered heterogeneity extensions all failed
recoverability, for three different measured reasons, and together they state a
usable rule about what a single cross-section can support.

**Carries.** A three-row table — *random leisure intercept* · *working-alternative
frailty* · *wage-residual/preference dependence* — with a column for the
mechanism of failure.

**Speaker notes.** This is the slide that turns an appendix of failures into a
result, and in a methods-literate audience it is often the most interesting five
minutes of the talk. Two conditions must hold together for a persistent
household-level term to be identified here. **Leverage:** the variable it loads on
must have enough within-household spread across the choice set, measured against
a scale-one Gumbel, to reorder a household's own alternatives. The Box–Cox
leisure transform has a within-set spread of 0.073 for men and 0.127 for women —
that is the wall the random intercept and the wage-residual lane both hit. **A
second contrast:** even with leverage, the term must move something the existing
coordinates cannot absorb. The frailty term has four times the leverage and still
fails, because a term that shifts every working alternative equally is a shift the
employment intercept can simply re-fit, and with one choice per household there is
no second margin to pin them apart. Then the punchline, which is a genuine
methodological point: **depth on an axis is not evidence; only depth on a profile
is.** Holding the rest of the model fixed gives that lane a likelihood-ratio depth
of up to 13.56; re-optimising the rest gives 0.6996, against the 2.706 a boundary
test needs. Close by saying what this does *not* say: it rejects three
parameterisations on this design, not the existence of heterogeneity.

**Timing.** 2.5 min. **25-MIN: CUT → backup.** Fold one sentence into slide 8:
*"three heterogeneity extensions were tested and all three failed recoverability,
for three different reasons; the backup slide has the design rule."*

---

# Part III — What the model fits (slides 10–13, 7.5 min)

## Slide 10 — Hours, and the statutory week

**Message.** The model reproduces the observed hours distribution including the
35-hour concentration, and it does so through the availability side rather than
through tastes.

**Carries.** **Figure 1** (observed weekly hours with the statutory band) and
**Figure 3** (hours-band shares, observed against model-implied).

**Speaker notes.** Observed 24.85 per cent in the statutory band against 25.20
model-implied; mean absolute error 0.83 of a percentage point across twelve bins.
The statutory-week coordinate is the single largest one-coordinate improvement in
the specification — a likelihood-ratio statistic of 861 on one degree of freedom.
Then the wording discipline, and use exactly this wording: it is an
**institutionally motivated opportunity peak in the estimated offer density**. It
is *not* an estimate of the causal effect of the 35-hour statute, and no
counterfactual removing the statute is computed anywhere. Concede the identified
weak spot without being asked: the model under-predicts the 40.5–44.5 band by 3.4
points.

**Timing.** 2.0 min. **25-MIN: MERGE with slide 11 (2.0 combined).**

## Slide 11 — Employment, occupation, and wages

**Message.** Employment and occupation fit closely; the offered-wage distribution
is the one substantial misfit and is reported rather than smoothed.

**Carries.** **Figure 4** (employment, all and by sex), **Figure 5** (occupation
shares), and the within-sample wage-fit table.

**Speaker notes.** Employment 0.8708 observed against 0.8668 model-implied.
Occupation: largest deviation across the five categories, including
non-employment, is 0.70 of a percentage point. Then be straightforward about the
wage side, because a referee will find it anyway: the model **over-predicts the
bottom offered-wage quintile by 5.3 points** and under-predicts the second, third
and fourth. On selected wages the median fit is **−€0.86 an hour for men and
+€0.34 for women** — the model slightly compresses the sex gap while matching the
pooled median to under thirty cents. Say that a pre-registered repair was tried —
an hours-conditioned wage location — and that it **failed**: it did not fix the
misfit and was not promoted. Occupation fit is shown *internally* here for a
reason that slide 13 explains.

**Timing.** 2.0 min. **25-MIN: MERGE into slide 10; keep employment, occupation
and the wage misfit; drop the by-sex wage detail.**

## Slide 12 — Does the answer depend on the number of drawn jobs?

**Message.** No: the estimates and the welfare decomposition are stable from 50
to 400 drawn alternatives per household.

**Carries.** **Figure 8** (key coordinates against draw count in standard-error
units) and **Figure 10** (the headline contributions against draw count).

**Speaker notes.** Thirty seconds of content and a minute of credibility. Every
sign is constant and the nested order holds at every rung. State the one
exception rather than claiming uniformity: in the male-reference arm the
preference contribution moves by 1.44 times its own band across the ladder — and
it is also the object with the tightest band in the study, so the exceedance is as
much about the band as the movement. The consequence is a reporting rule: **the
male-reference preference contribution is not quoted to more than two significant
figures.**

**Timing.** 1.0 min. **25-MIN: CUT → backup.**

## Slide 13 — External validation

**Message.** The hours structure the model recovers is visible in a labour-force
source the model never saw; the earnings benchmark that would validate the wage
block is not available, and that is stated rather than substituted.

**Carries.** **Figure 16**, both panels: (a) the share of employed people wishing
more hours against the model's estimated relative offer weight by band; (b) the
statutory band in the external benchmark, the observed sample and the
model-implied distribution.

**Speaker notes.** Frame it before showing it: **validation only — no moment from
any external source enters the likelihood, and none of this identifies
anything.** Panel (b): the statutory band takes 37.2 per cent of workers in the
external source, 34.3 per cent in the observed sample and 34.6 per cent
model-implied, and the concentration is larger for women than men in all three —
which the model reproduces **without any sex-specific hours coordinate**. Panel
(a): 20.3 per cent of employed people in the priced bands report wanting more
hours, and the share falls monotonically in hours worked, so the bands the model
prices as thin in opportunity are the bands where workers report constrained
hours. Say the limit in the same breath: **the model has no direct desired-hours
counterpart**, so these are consistent, not commensurable. Two things not to skip.
The external population is all adults aged 20–60 while the sample is single-adult
households, so **a gap here is a population difference, not a prediction error**.
And the matched employer–employee earnings source is simply not available in the
accessible data, so no external wage comparison is attempted and none is faked.

**Timing.** 2.5 min. **25-MIN: KEEP (compressed, 1.0) — panel (b) and the
population caveat; drop panel (a).**

---

# Part IV — What it finds (slides 14–18, 10.5 min)

## Slide 14 — The welfare measure, and two real households

**Message.** Welfare is equivalent income at a common reference pay: it
compensates for pay and holds the household responsible for its own opportunity
set — and the mechanism is visible on real households.

**Carries.** **Figure 14** (the forward matched pair) — panels for the estimated
preference profile, the hours margin of the opportunity density, occupation
availability, and the wage-offer density.

**Speaker notes.** Define the measure in one sentence and say what normative
choice it encodes: what flat consumption level, available at every job in this
household's own set, would leave them as well off as they are — so pay is
compensated and the set is the household's own responsibility. Then the pair, and
stress that it was **selected by a rule fixed before any household was looked at**,
from 19,116 admissible pairs matched on observed employment, occupation, hours
band and wage quintile: two single men, both working 40 hours in the same
occupation in the bottom wage quintile, whom the model gives essentially the same
preference profile and very different opportunity — employment probability 0.874
against 0.702, median wage offer €13.93 against €8.80. This is slide 3's panel (a)
on real estimates. Repeat once that these panels are **densities, not job draws**.

**Timing.** 2.0 min. **25-MIN: KEEP (1.5) — the measure and the pair, no panel
walk-through.**

## Slide 15 — The headline

**Message.** Equalising the whole non-preference environment removes 93.7 per
cent of money-metric welfare inequality; equalising preferences removes a further
6.3 per cent.

**Carries.** **Figure 12** (preferences against environment, signed, with bands)
and the exact-table row.

**Speaker notes.** Read the sentence as it is written, because it is generated
from the table with a guard and its qualifiers are not decoration: *within the
currently modelled non-preference environment, budget-side endowments and needs
are the largest nested contribution under both positive models and both
reference-preference conventions.* Baseline inequality is a Gini of 0.134;
equalising the environment alone takes it to 0.031; equalising both takes it to
numerical zero — and that last point is a **tested property, not an assumption**:
the fully common state is zero to machine precision, which is what licenses
reporting shares at all. Then the licensed reading, which must be said out loud:
**no channel "explains" a percentage.** A contribution is the value of an
equalisation operator in a cooperative game — the form is *equalising this channel
removes this share of baseline inequality* — not a variance share and not a causal
effect. And the bands are **numerical-integration precision, not sampling
confidence intervals**; sampling uncertainty in the parameters is not propagated
here, and that row is stated rather than elided. One counter-intuitive fact worth
30 seconds if the room is engaged: equalising preferences *raises* measured
inequality, because the households with the worst opportunity sets are the ones
whose own tastes currently do most to reconcile them to those sets.

**Timing.** 2.5 min. **25-MIN: KEEP (2.5) — this is the slide the talk exists for.**

## Slide 16 — Inside the environment

**Message.** Household endowments and needs carry the largest nested share; job
access and earning opportunities together carry about a third.

**Carries.** **Figure 13** (the nested split, signed, with bands).

**Speaker notes.** Endowments and needs 58.2 per cent (±1.5), earning
opportunities 20.6 (±1.6), job access 14.9 (±1.1) — so the two market-side
channels together are **35.5 per cent (±0.9)**, and that combined figure is
reported separately from endowments and needs on purpose. Two disciplines. First,
**do not say job opportunities explain the environment share**: the environment is
the *complete* non-preference environment, and the market-side part of it is a
third, not all of it. Second, **no ordering is claimed between job access and
earning opportunities** — the point estimates order them and are printed, but the
access margin is exactly the one that does not separate capability from
availability, so an ordering claim would be a claim about something the design
does not identify. If asked why the budget channel is so large, give the honest
reading: this is France 2016, a system with substantial means-tested transfers,
and the result is partly a statement about that system. It is not portable without
re-estimation.

**Timing.** 2.0 min. **25-MIN: KEEP (1.5) — the three numbers, the combined
market-side figure, and the no-ordering rule.**

## Slide 17 — What is fragile, and what is not

**Message.** Three independent perturbations all move the preference share and
leave the environment's internal structure alone — so the preference/environment
split is the fragile margin and the nested order is the robust one.

**Carries.** A three-row table: *reference-preference convention* · *a bound on a
preference curvature* · *pinning the couples male leisure block* — against the
move in the preference share and the move in the environment side.

**Speaker notes.** This is the most useful slide for a critical audience and it is
a strength, not a concession. The reference convention moves the preference share
from 6.30 to 10.89 per cent; the age-bound diagnostic moves the same quantity by
about 13 per cent; pinning the couples male leisure block moves it by up to 73 per
cent. The environment side moves by under 3.5 per cent in all of them, and no
sign and no ordering changes anywhere. Then the reporting rule: the two reference
conventions are reported as a **range and never averaged** — 3.3 to 11.0 per cent
across all eight rows, with a constant sign — and this is a normative choice made
explicit, not a robustness check. Note that the market-side total is essentially
*insensitive* to the reference convention, 35.5 against 35.9, so the sensitivity
sits precisely in the preference/environment split and not in the environment's
internal structure.

**Timing.** 2.0 min. **25-MIN: KEEP (1.5) — the three rows and the range rule.**

## Slide 18 — Couples

**Message.** The couples module reproduces the same nested order and the same
environment dominance, but its preference share is materially sensitive, so
singles remain the quantitative headline.

**Carries.** **Figure C2** (the couples decomposition) or **Figure C3** (singles
and couples side by side, equivalized).

**Speaker notes.** 2,275 opposite-sex couples, one specification and no search.
Lead with the finding that was not targeted and is the most striking piece of
internal consistency in the paper: the **female statutory-week peak in couples
reproduces the singles value to within three hundredths** — a third of a standard
error — on a different frame, a different choice set and a joint likelihood. Then
the substance: same nested order on both bases, same environment dominance. Then
the discipline, and do not soften it. The recovery gate named the male leisure
block as the module's weakness *before* the welfare arms were run, and the
sensitivity analysis confirms it bites: the preference contribution moves by up to
73 per cent, so **no single couples preference percentage is presented as
structurally robust**, and every couples preference figure travels with its range.
One directional difference from singles, stated because it is real: for couples,
equalising preferences *reduces* measured inequality, the opposite of the singles
result, so the singles interpretation does not transfer. If asked about pooling:
pooled equivalized inequality is well defined and reported, but the pooled
*decomposition* is not exhaustive — the two household types have different
reference bundles, so the fully common pooled state is 39.4 per cent of the pooled
baseline. That is an **open welfare-reference question, not a numerical failure**.

**Timing.** 2.0 min. **25-MIN: KEEP (compressed, 1.0) — the statutory-week
replication, the same order, and the sensitivity caveat.**

---

# Part V — Close (slides 19–20, 2.5 min)

## Slide 19 — Limits, and what would identify more

**Message.** The design's limits are known and each names the evidence that would
lift it.

**Carries.** A two-column table: *limit* against *what would change it*.

**Speaker notes.** Four limits, thirty seconds each at most. **Access versus
capability** — separating them needs external moments on job-offer or access
rates. **Persistent heterogeneity** — needs repeated choices per household, which
would supply the second contrast slide 9 showed is missing. **The hours block has
no desired-hours target** — external desired-hours moments would discipline it
against a stated target rather than inferring both from realised hours. **One
country, one year, one system** — nothing here is portable without re-estimation,
and no portability is claimed. Say the honest scope line: multi-adult households
are excluded, and their admission needs five assumptions this design leaves
unstated. Also state, once, that the welfare magnitudes are **provisional pending
one bounded economics review**.

**Timing.** 1.5 min. **25-MIN: CUT → fold two sentences into slide 20.**

## Slide 20 — Conclusion

**Message.** Separating preferences from opportunities is feasible on survey data
with a tax–benefit engine, and doing it changes what welfare inequality is
attributed to.

**Carries.** Three bullets: the method, the headline, the honest margin.

**Speaker notes.** Close on the contribution rather than the number. The method:
a household-specific opportunity distribution estimated jointly with preferences,
with every job priced through the real tax–benefit system, and a decomposition
that is exhaustive **by measurement rather than by assumption** — the fully common
state is numerically zero. The finding: the non-preference environment carries
roughly nine-tenths of measured money-metric welfare inequality, and inside it the
budget side carries more than the market side. The margin: the preference share is
the fragile quantity, it is reported as a range across the two normative
conventions, and it is where the next round of evidence should go. Then stop
talking.

**Timing.** 1.0 min. **25-MIN: KEEP (1.0) — absorb the two limits sentences.**

---

# Backup slides

Not in the running order. Each is a single slide, held for a specific question.

## B1 — The estimated coefficients

**Held for.** *"What are the actual parameter estimates?"*

**Carries.** **Figure 2** — all 41 estimated coordinates by economic block with
robust 95 per cent intervals. The full table with standard errors is in the paper's
Appendix A.

**Notes.** The final singles model carries **41 estimated structural parameters**.
Read off the two things worth reading: the leisure curvatures differ sharply by
sex and are precisely estimated, and the occupation-availability weights differ
strongly by sex — men concentrated in and around routine manual, women's
availability tilted toward nonroutine cognitive. That sex-specific structure is
what keeps occupational sorting out of the taste block. Note that two coordinates
rest on an active bound and carry no standard error, and that the ten pinned
coordinates are not displayed.

## B2 — Exhaustiveness: how the decomposition was made to close

**Held for.** *"Why should I believe the four channels are exhaustive?"* — and it
is the best question in the room.

**Carries.** A five-row table: the defect, what it did, and what fixed it.

**Notes.** This is a methodological result and it should be told as one, because
the honest answer is that it did **not** close at first. An earlier implementation
failed the exhaustiveness test on both limbs in every arm — equalising everything
left an index **three times** the one it started from — and the headline was
correctly **halted**. Three things were found and removed. A missing budget
channel, added as a fourth player formed from its own marginals rather than as a
relabelled residual. An asymmetry in the money-metric inversion, where the
reference side was frozen at the baseline while the attained side moved with the
coalition; correcting it removed about 95 per cent of the residual. And a male
reference block that was incomplete, because the specification carries a
children-in-leisure term for women and none for men. With all three fixed the
fully common state is numerically zero. **Exhaustiveness here is a tested
property, and the test was pre-stated before any cell was read.**

## B3 — Equivalization, and why the scale has to move

**Held for.** *"You divide by an equivalence scale — doesn't that break the
decomposition?"*

**Carries.** The raw-against-equivalized comparison table.

**Notes.** It does, under the natural convention, and exactly: freezing each
household's own scale in all states leaves a residual of 0.071799, which is
**precisely the weighted Gini of one over the scale** — the same number to six
decimals. Dividing a common numerator by a household-specific divisor reintroduces
exactly the dispersion of the divisor. The fix is the one the inversion already
legislates: household composition **is** an endowments-and-needs object, so the
scale moves with the channel that equalises composition, and exhaustiveness is
restored exactly. Equivalizing raises measured inequality by about a fifth and
changes no qualitative conclusion, but it does move the market-side total from
35.5 to 25.9 per cent — both are reported and neither is "the" answer. Then the
normative point, which is genuinely open and should be put to the room: does
"equalising needs" mean giving every household the reference household's needs, in
which case the scale must move — or equalising resources while leaving needs
alone, in which case the residual is a genuine needs term? **This paper takes the
first reading because it is the one under which the four channels close. The
second is coherent and requires a different accounting.**

---

# The 25-minute version, in one place

**Plan: 23 minutes across 15 slides, 2 minutes slack.**

| action | slides |
|---|---|
| **CUT → backup** | 9 (the loading principle), 12 (draw stability), 19 (limits — two sentences fold into 20) |
| **MERGE** | 6 + 7 → one data/estimator/pricing slide (2.5); 10 + 11 → one fit slide (2.0) |
| **COMPRESS** | 2 → 1.0 (one vignette); 3 → 2.0 (panel (a) only); 5 → 1.0; 13 → 1.0 (panel (b) only); 14 → 1.5; 16 → 1.5; 17 → 1.5; 18 → 1.0 |
| **KEEP UNCHANGED** | 1 (0.5), 4 (2.0), 8 (2.0), 15 (2.5), 20 (1.0) |

**What must survive any cut.** The T1 distinction; the channel-relocation result
on slide 4; the licensed reading of a contribution on slide 15; the combined
market-side figure and the no-ordering rule on slide 16; the fragility claim on
17; the couples sensitivity caveat on 18.

**What must never be cut, at any length.** That the bands are integration
precision and not confidence intervals; that no channel "explains" a percentage;
that the statutory-week coefficient is an opportunity peak and not a causal
estimate; and that the couples preference share is not structurally robust.

---

# Provenance — every number on every slide

*Paths are relative to the estimation repository; `SPRINT` abbreviates
`MNL/experiments/JMP_SEMINAR_SPRINT`. Every decomposition percentage comes from
the exact table and from nowhere else.*

| slide | number | source |
|---|---|---|
| 6 | 1,555 households; 101 alternatives; 157,055 rows | paper §4.1, §5.1 |
| 9 | within-set spread 0.073 / 0.127; axis depth to 13.56; profile depth 0.0492 / 0.6996 against 2.706 | paper §5.4 |
| 10 | statutory band 0.2485 observed / 0.2520 model-implied; hours mean absolute error 0.0083; band shortfall −0.034 | `SPRINT/figures/fig02_hours_bands_obs_vs_pred.csv`; paper §6.2 |
| 10 | statutory-week likelihood-ratio 861.42 on 1 d.f. | paper §6.3 |
| 11 | employment 0.8708 / 0.8668; occupation largest deviation 0.0070; bottom wage quintile +0.053 | `SPRINT/figures/fig03_…csv`, `fig04_…csv`; paper §6.2 |
| 11 | median wage fit −€0.86 men, +€0.34 women | `SPRINT/tables/wage_fit_within_sample_v1.csv` |
| 12 | range-over-band 1.44, male-reference preference contribution | paper §7.6 |
| 13 | statutory band 37.2 % external / 34.3 % observed / 34.6 % model-implied; women 40.6 vs men 34.6 external | `SPRINT/figures/figX1_external_hours_lfs_validation.csv` |
| 13 | 20.3 % wishing more hours; monotone gradient | `SPRINT/runs/external_hours_lfs/xh1_table_record_v1.json` |
| 14 | 19,116 admissible pairs; 0.874 vs 0.702; €13.93 vs €8.80 | `SPRINT/runs/figE1_matched_households/e1_matched_households_v1.json`; paper §7.8 |
| 15 | environment 93.70 ± 0.61; preferences 6.30 ± 0.61 | `SPRINT/tables/headline_decomposition_v1.csv`, `C_env_over_I00`, `C_pref_over_I00` |
| 15 | baseline 0.134277; environment-only 0.030968; fully common numerical zero | same, `I00`, `I01`, `I11` |
| 16 | endowments and needs 58.18 ± 1.47; earning opportunities 20.62 ± 1.63; job access 14.90 ± 1.10 | same, `C_needs_over_I00`, `C_earn_over_I00`, `C_acc_over_I00` |
| 16 | market-side total 35.51 ± 0.95 | same, `C_acc_plus_C_earn_over_I00` |
| 17 | preference share 6.30 → 10.89; range 3.3–11.0 across eight rows | same, `C_pref_over_I00` |
| 17 | market-side total 35.5 vs 35.9 across references | same, `C_acc_plus_C_earn_over_I00` |
| 17 | age-bound ≈13 %; couples male-leisure 73.1 %; environment side under 3.5 % | paper §5.5, §8.4 |
| 18 | 2,275 couples; female peak 2.5474 against singles 2.5795; preference share range 0.0014–0.0075 | paper §8.1, §8.3, §8.4 |
| 18 | pooled fully common state 39.4 % of pooled baseline | paper §8.5 |
| B1 | 41 estimated structural parameters | `SPRINT/figures/fig08_coefficients_by_block.csv`; paper Appendix A |
| B2 | pre-correction ratio 3.03; ≈95 % residual removed by the inversion | paper Appendix B |
| B3 | own-scale residual 0.071799 = weighted Gini of the inverse scale; +22.96 %; 35.5 → 25.9 | paper §3.5, §7.4 |

---

*Deck content v1, for the seminar working paper of the same date. Every welfare
and decomposition magnitude above is provisional pending the one bounded
economics review, on the same status the paper's drafting note records.*
