# 8. Limitations and scope

*Drafting note, to be stripped at final.* Status tags carry the same meaning as
in §2 and §3: **[ACCEPTED]** — on the record of an accepted run or a ratified
ruling; **[PROVISIONAL]** — computed and internally verified, but carrying an
explicit provisional label on its own artifacts; **[PENDING]** — designed or
authorized but not yet run, not yet ruled, or not yet on disk. Every numeral
below is bound to a source in the self-check table at the end of the section.
Drafted under Goal-1 R-231.4 against outline v1 §8; that ruling is **not on
disk** — the Goal-1 rulings register ends at R-227 (R-227.2 on the dashboard) —
and the authorization is therefore recorded here as **[PENDING]** rather than
cited. Each limitation is stated as what the design does and does not claim,
with its evidence. The section carries the R-227 s12 terminology rule: no
unqualified "ability" appears, and "ability set $A_i$" is used only in its
reserved sense.

---

## 8.1 Identification scope

**(a) Access versus capability.** The opportunity density of §2.1 is a density
over job packages, and its access margin $g^{E}$ is a level shift on every
working package. The present access density may combine personal capability
and market availability; it does not yet separately identify $A_i$ from $O_i$.
The design therefore claims that the estimated density describes *how
available* packages are to a household with given observables. It does not
claim to separate the set of jobs a person is capable or eligible to perform —
the ability set $A_i$ in its reserved sense — from the set the market puts in
front of them, $O_i$. Every attribution to the access channel in §5 is an
attribution to that combined object, and no result in this paper ranks
households by productivity. **[ACCEPTED]**

**(b) Persistent unobserved heterogeneity.** The choice model carries a
job-package Gumbel shock and no household-level persistent term. Two
pre-registered extensions were tested for recoverability on the corrected
singles frame by synthetic recovery from the accepted specification's own
point, with the expected likelihood-ratio depth computed exactly under the
truth's marginal choice probabilities, so the finding does not depend on a
draw. Neither is recoverable from a single cross-section of choices at this
sample size, and each fails for a measured reason.

- *A random leisure intercept* (HP) loads on the Box–Cox leisure transform,
  which at the estimated curvature is nearly flat across a household's own
  alternatives: its within-household spread is **0.07** for men and **0.13**
  for women against a Gumbel of scale one. The expected likelihood-ratio
  signal against a zero variance is **0.0081** and **0.1351** at the two
  non-zero truths, against the **2.706** the boundary test requires. The
  expected objective peaks exactly at the truth, so the estimator is right and
  the design is uninformative. Real-data estimation was not run, by rule.
  **[ACCEPTED]** (R-226)
- *A common working-alternative frailty* (HO) loads on the working indicator
  and has four times HP's leverage. But it shifts every working alternative
  equally, so it is exactly a binary mixed logit on the employment margin with
  one observation per household, and re-fitting the accepted coordinates under
  a zero variance absorbs about **95%** of its signal through the employment
  intercept. The profile depth a likelihood-ratio test actually computes is
  **0.0492** and **0.6996**, again against **2.706**. Real-data estimation was
  not run, by rule. **[ACCEPTED]** (R-227.2)

These results reject *those two parameterisations* on *this design*. They do
not establish that preference or opportunity heterogeneity is absent, and the
paper does not claim that. Under the standing rule that no extension is
admitted without passing its recoverability gate, the preferred singles
specification is formally retained rather than an extension being invented.
**[ACCEPTED]** A third extension, *wage-residual dependence* (W3), in which
the person-level wage residual is correlated with a persistent preference
component, is authorized on its own feasibility gates and has not been run;
it requires a defined persistent preference component, which the HP result
does not supply. **[PENDING]** (R-220 s6–s7)

**(c) What would identify more.** Each negative result names what would
change its arithmetic, and none of it is in the present data: repeated choices
per household, which would supply a second contrast on the employment margin;
external moments on job-offer or access rates, or on wage offers, which would
pin the persistent terms from outside the choice likelihood; and desired-hours
moments, which would discipline the hours-band density against a stated target
rather than infer both from realised hours. No such moment enters the
objective. **[ACCEPTED]** as design statements.

## 8.2 External evidence

**The regional occupation-demand construction (BMO).** A lagged 2015
employer-side recruitment-tension covariate at NUTS-2, aggregated to the four
task groups through a four-table crosswalk and entered in the occupation
margin as one coefficient, was estimated on three pre-registered arms and
closed as a negative result. The permitted statement, and the only one made,
is: *this lagged BMO construction adds no detectable structural
occupation-access signal in the current sample and specification.* It is not
claimed that regional occupation demand is generally irrelevant, and BMO is
not used as identification evidence in the headline model. The standing
classification is an external opportunity identification aid at NUTS-2 and
not a causal instrument; the 2015 lag is timing discipline, not an exclusion
restriction. **[ACCEPTED]** (`R1_BMO_NEGATIVE_RESULT_CLOSED`, R-218 §9)

The mapping is disclosed rather than assumed away. Mapped recruitment-mass
coverage is **0.5837**; **0.3799** of recruitment mass was withdrawn because no
defensible weighting basis exists for it; **0.0324** is genuine non-significant
probability mass in the official matrices; four BMO codes carrying **0.40%** of
mass have no crosswalk image and are not imputed. The high-confidence
sensitivity retains **0.3810**. The two mappings disagree on two of the four
task groups (column correlations **0.62** and **0.66**); the coefficient is
indistinguishable from zero under both, so the interpretation gate did not
have to adjudicate. **[ACCEPTED]**

**Hours-band concentration and the LFS.** The concentration of observed hours
in the statutory band is the motivating picture of §3.2 and is carried in the
estimated offer density as an institutionally motivated 35-hour opportunity
peak. The external check named for it — the French LFS / EU-LFS desired-hours
and underemployment series — is designated *external validation only*: an
out-of-sample comparison of the model-implied hours gap and 35-hour mass
against a published national series, with no merge, no covariate and no moment
in the objective. Stated hours preferences are self-reported conditional on
the current job and are exactly the object the model infers; using them for
identification would assume away the question. The comparison has not been
obtained. **[PENDING]**

## 8.3 The welfare layer

**Normative-reference sensitivity is real.** The equivalent-income measure
evaluates each household at a reference preference block, and the singles
module carries two ratified blocks: the female block as primary and the male
block, completed on the union of preference terms with a structural zero on
the children-in-leisure term, as sensitivity. The preference contribution has
the same sign and the environment remains dominant under both, but the
female/male difference exceeds the numerical-integration bands, and the
classification of record is `REFERENCE_SENSITIVE_MAGNITUDE`. The shared-child
diagnostic attributes only **3.7%** (S8) and **7.3%** (LOC4) of that difference
to the child term; the remainder comes from coefficients that genuinely differ
between the ratified blocks. Results are reported as the female-primary value,
the male-sensitivity value and their range. They are never averaged.
**[PROVISIONAL]** (R-217 / R-218)

**Absolute welfare levels depend on the numerical support design.** Moving
the decomposition from own-support to common quadrature support moved the
fully-observed welfare level by **−5.5%** (S8) and **−7.7%** (LOC4). The common
support is a numerical-integration correction, not a common realised
opportunity set; the movement is disclosed, no proposal-invariance claim is
made, and absolute levels are not frozen as final
(`ABSOLUTE_WELFARE_LEVELS_NOT_FINAL`). The accepted-specification welfare
levels are additionally conditional on the inherited hours-normaliser
convention and are not convention-free magnitudes. **[PROVISIONAL]**

**MC bands are integration precision; sampling uncertainty is not estimated.**
Every banded quantity travels with the three-way report of §2.5. The RQMC band
addresses numerical-integration error only; the profile envelope, where one
exists, addresses conditional uncertainty in one profiled coordinate only; and
the third row — sampling uncertainty of the estimated parameter vector
propagated to the welfare functionals — is stated rather than elided: **it is
not estimated in this paper**, and no reader should infer it from the first
two. The one licensed robustness statement in the welfare layer is
correspondingly narrow: the opportunity share of the carrier measure is robust
to the S0→S8 change *at the achieved RQMC precision*, on the carrier measure
only, and this is not statistical invariance. No cross-measure quantitative
robustness claim is made. **[ACCEPTED]**

**All decomposition values are provisional.** Every welfare and decomposition
value on the record was computed on the pre-correction singles frame, is
retained as history under `PRE_CORRECTION_PROVISIONAL_WELFARE_HISTORY`, and
is not valid for final magnitudes. The exhaustiveness target of the
decomposition is not met on the pre-correction record, so no headline share is
formed. Final welfare is computed once, for the corrected benchmark and the
final positive model, and the refresh is deferred to that step.
**[PROVISIONAL]** (R-222 s9)

## 8.4 Data

**The wage variable.** For every FR 2016 person with observed earnings and
hours, the delivered hourly wage reproduces gross monthly earnings, annualised
over the months paid, divided by monthly hours — an identity that holds for
**100%** of such persons at machine precision. The structural wage density and
its education and experience loadings are therefore fitted against observed
worker wages, not against fitted conditional means. The construction of the
delivered variable for persons *without* observed wage inputs is incompletely
documented: the imputation do-file is unavailable, and of the eleven
documentation fields audited, seven are recorded as unavailable without it and
three more as only partially documented. That construction does not
enter the likelihood — the non-worker wage location is provably inert, the
objective being bitwise unchanged when every non-working row's wage is
overwritten — and the genuinely imputed worker wage is confined to **21**
workers with zero recorded earnings. The earlier characterisation of the
variable as a full-population predicted wage was withdrawn by a dated
correction and is not restated. **[ACCEPTED]** (R-220 s1–s2)

**Hours support: the audit and the floor correction.** Ten households in the
singles sample had observed weekly hours moved by the data-construction clip.
Three lie above the **70-hour** cap and are projections onto model support, now
a recorded convention rather than an implicit one. **Seven** lay between five
and ten hours and were moved by a floor that was not a support boundary — the
latent hours support reaches five hours and the frame carries jobs there — so
their priced budgets were wrong by up to a quarter of disposable income. The
floor was corrected through the actual construction path: exactly seven chosen
alternatives changed, every drawn alternative was bitwise unchanged, and both
positive models re-estimated on the corrected frame with no coordinate moving
more than a tenth of its previous standard error and the specification
comparison unchanged. The corrected frame is the sole forward-looking singles
frame. **[ACCEPTED]** (R-222 / R-224 / R-227 s1)

**Geography and time.** NUTS-2 (22 régions) is the finest household geography
in the data; nothing below it exists, and the sampling units are clustering
dimensions, not geographies. The regional-access shifters and the BMO
construction are therefore NUTS-2 objects, with région cells of median 53.5
households, and any finer sorting is unobserved. The estimation data are a
single-year cross-section (France 2016): one choice per household, which is
the source of the identification limit in §8.1(b). **[ACCEPTED]**

## 8.5 Scope

**Singles as the primary application.** The estimated and accepted module is
the 1,555 single-adult households; the bounded review that accepted the
preferred specification closes the *singles* positive specification only and
establishes nothing about couples or a population-wide final model.
**[ACCEPTED]** (R-183 / R-184.1)

**Couples as a parallel module with characterised limitations.** A joint
household specification over 2,275 opposite-sex couples has been estimated
through phase 4 and is *not promoted*: the synthetic recovery gate fails. Three
limitations are characterised rather than resolved. The couples-male leisure
intercept is identified but not precisely estimated, and the earlier statement
that couples-male leisure is present is treated as unconfirmed. The pooled
occupation block fails on two independent axes — the largest fit misfit and a
coverage failure (**7/10**) whose probability under a correct model is about
**1.2%** — so pooling occupation opportunity across sexes is read as
mis-specified for couples. And take-up rates enter from thin cells. The lane is
re-ordered as three decision types — both spouses flexible, and two
semi-flexible types with one spouse fixed at the observed state — behind a
gated generic proposal capability; the adapter contract and pricing tests pass,
and no expanded-sample estimate or couples welfare quantity exists. No couples
number is compared to a singles number. **[PROVISIONAL]** (R-188 / R-190.2 /
R-227 ss4–8)

**Multi-adult households.** Households with three or more decision-unit
adults (**934** in the candidate expanded sample) are excluded from headline
welfare as `EXTENDED_HOUSEHOLD_BUDGET_ROBUSTNESS`. Their admission would
require five assumptions the present design leaves unstated: resource pooling,
the tax/benefit unit, the allocation of consumption within the household, the
needs of additional adults, and the welfare unit. Two-adult households whose
adults are not mutually linked as partners are inventoried and excluded rather
than forced into a couple model; same-sex linked couples are inventoried, not
estimated. **[ACCEPTED]** (R-223 s6 / R-225 / R-227)

**The equivalence scale as a disclosed normative parameter.** Cross-type
welfare reporting, when it exists, is in equivalised units only, with the
modified OECD scale as the primary disclosed normative scale and the
model-implied scale as a later sensitivity. The ratified design attaches a
calibration identity to cross-type aggregation — a household at its
type-specific reference with disposable income $e_i \cdot m$ must have
equivalised welfare $m$ — and aggregation halts if it fails. The identity has
not yet been evaluated, because no type-specific reference bundle is on disk.
**[ACCEPTED]** as design (R-227 s9); **[PENDING]** as evaluation.

---

## Self-check table

### (a) Numerals → source

| numeral (as used above) | source |
|---|---|
| leisure-transform within-household spread 0.07 (men) / 0.13 (women) | `MNL/experiments/JMP_PS1/decision_note.md` §26.1 (0.0732 / 0.1270) |
| HP expected LR 0.0081 / 0.1351 vs 2.706 | `decision_note.md` §26.4; rulings document v4, R-226 line |
| HO loading four times HP's spread; axis signal two orders larger | `decision_note.md` §29.1, §29.4 |
| HO ~95% absorbed by re-fitting (95.2% / 94.8%); profile LR 0.0492 / 0.6996 vs 2.706 | `decision_note.md` §29.4 |
| HP / HO real data not run by rule | `decision_note.md` §26.5, §29.5; dashboard §1 labels |
| W3 authorized, gates A–G, not run | dashboard §3 item 3, §6; rulings document v4, deputy text (1) under "Appended 2026-09-02 — R-219..R-224" |
| BMO three arms, all CIs include zero | `decision_note.md` §21.9 "R1_BMO (ruling s9)" table; dashboard "R1 BMO — CLOSED at R-218" |
| the permitted BMO sentence, verbatim | `decision_note.md` §21.9; dashboard §1 `R1_BMO_NO_ADDITIONAL_OCCUPATION_ACCESS_SIGNAL` |
| coverage 0.5837; withdrawn 0.3799; non-significant 0.0324; 4 codes / 0.40%; HC090 0.3810 | `decision_note.md` §15.9, §15.10, §15.15 |
| column correlations 0.62 / 0.66 (loc4 2 and 3) | `decision_note.md` §15.10 |
| LFS: external validation only; no merge, covariate or moment | `decision_note.md` §10.2 ("Recommended use"); outline v1 §7 "(if obtained)" |
| child term 3.7% (S8) / 7.3% (LOC4) of the female/male gap | `decision_note.md` §21.9 "The shared-child diagnostic" |
| `REFERENCE_SENSITIVE_MAGNITUDE`, difference exceeds the RQMC bands | `decision_note.md` §21.9 classification table; dashboard §1 |
| common-support movement −5.5% (S8) / −7.7% (LOC4) | `decision_note.md` §21.9 "Absolute welfare levels (ruling s8)"; dashboard §1 (−5.53% / −7.74%) |
| welfare levels conditional on the inherited hours-normaliser convention | `decision_note.md` §11.6 item 2 (R-184.1) |
| three-way report; sampling uncertainty not estimated | `manuscript/sections/02_framework.md` §2.5 |
| `s_opp` "robust to the S0→S8 change at the achieved RQMC precision", W1-only | `decision_note.md` §11.6 item 4 (R-184.1) |
| pre-correction welfare = history; refresh deferred to final S9 | `decision_note.md` §25.9; dashboard §1 (R-222 s9) |
| exhaustiveness not met; no headline share formed | `decision_note.md` §17.3; dashboard §1 `HEADLINE_PERCENTAGES_HALTED` |
| wage identity 100% (11,870 / 11,870, median relative error 2.0e-08) | `decision_note.md` §22.2, §24.1 |
| eleven documentation fields: seven unavailable, three partial, one resolved from the data; do-file unavailable | `decision_note.md` §22.1 (audit table) |
| non-worker wage inert (bitwise over 15,814 rows); 21 imputed workers | `decision_note.md` §22.5 (P1), §22.3 |
| dated withdrawal of the predicted-wage characterisation | `decision_note.md` §23.5; rulings document v4, "CORRECTIVE APPEND 2026-09-02 - R-220 s10" |
| ten clipped households; 3 cap / 7 floor; raw hours 72, 86, 96; error up to a quarter of disposable income (−24.5%) | `decision_note.md` §23.1(b), §23.2 |
| 70-hour cap as a recorded support-projection convention | `decision_note.md` §23.4; dashboard §1 `HOURS_CAP_70_SUPPORT_PROJECTION_CONVENTION_RECORDED` |
| support reaches 5 h; 2,225 drawn alternatives below 10 h | `decision_note.md` §23.1(b) |
| exactly 7 chosen rows changed; 0 drawn node-level changes; largest move 0.0213 previous SE; 0 coordinates > 0.1 SE | `decision_note.md` §25.2, §25.6 |
| NUTS-2, 22 régions, median cell 53.5; sampling units are clustering dimensions | `manuscript/sections/03_data.md` §3.3; notebook Table 12.1 / §12(a) |
| France 2016 single-year cross-section; 1,555 singles; 2,275 couples | `03_data.md` §3.1 |
| review closes the singles positive specification only | `decision_note.md` §11.6 closing boundaries (R-184.1) |
| couples `GATE_FAIL`; `beta_l0_m` identified but not precisely estimated; `beta_occ_2` coverage 7/10, P ≈ 1.2% | `decision_note.md` §14.7, §14.8; dashboard "Couples lane" |
| pooled occupation the largest fit misfit | `decision_note.md` §13.6, §14.7 |
| take-up thinness (couples flag) | `03_data.md` §3.4; notebook §11(a) |
| three-type design; `SEMI_FLEXIBLE_MARGINAL_PROPOSAL` gated; adapter tests pass, no estimate, no welfare quantity | rulings document v4, R-227 ss4–8; MNL commit `8419dd4`, `experiments/JMP_PS1/semi_flexible_adapter_summary.md` |
| 934 multi-adult households; the five assumptions | `MNL/experiments/JMP_PS1/runs/ps1sx_sample_audit/audit_note_v1.md` §5; `sample_expansion_design.yaml` §7 |
| unlinked two-adult households and same-sex couples inventoried, not estimated | `audit_note_v1.md` §5 |
| modified OECD primary; model-implied scale a later sensitivity; calibration identity; halt on failure; not yet evaluated | `decision_note.md` §28.2; rulings document v4, R-227 s9 |
| the Goal-1 R-231.4 drafting authorization | **not on disk** — register ends at R-227 / R-227.2 |

### (b) Claims → status

| claim / design element | status |
|---|---|
| the non-identification sentence: access density may combine personal capability and market availability; $A_i$ not separately identified from $O_i$ | **[ACCEPTED]** (R-227 s12) |
| no household is ranked by productivity; access attributions are to the combined object | **[ACCEPTED]** |
| HP not recoverable at this sample; real data not run | **[ACCEPTED]** (R-226) |
| HO not recoverable at this sample; real data not run; fails for a different reason than HP | **[ACCEPTED]** (R-227.2) |
| both negatives reject the parameterisations, not heterogeneity in general | **[ACCEPTED]** |
| S8 formally retained absent an admitted extension | **[ACCEPTED]** (R-220 s9 rule; R-227.2 disposition) |
| W3 wage-residual dependence | **[PENDING]** — authorized, not run |
| repeated choices / external moments / desired-hours moments as what would identify more | **[ACCEPTED]** as design statements |
| the BMO permitted sentence, verbatim; not "regional demand is irrelevant" | **[ACCEPTED]** (R-218 §9) |
| BMO as identification aid, not a causal instrument; lag is not an exclusion restriction | **[ACCEPTED]** (R-182 §5; §15.11) |
| the mapping disclosure set | **[ACCEPTED]** (R-193 / R-210) |
| the LFS route as external validation only; not obtained | **[PENDING]** |
| normative-reference sensitivity is real; reported as a range, never averaged | **[PROVISIONAL]** |
| absolute levels depend on support design; movement disclosed; not final | **[PROVISIONAL]** |
| welfare levels conditional on the inherited hours-normaliser convention | **[ACCEPTED]** (R-184.1) |
| MC bands are integration precision; sampling uncertainty of the functionals not estimated | **[ACCEPTED]** |
| the only licensed robustness statement (`s_opp`, W1-only, at achieved RQMC precision) | **[ACCEPTED]** (R-184.1) |
| no cross-measure quantitative robustness claim | **[ACCEPTED]** (R-182) |
| all decomposition values provisional; refresh deferred to final S9 | **[PROVISIONAL]** |
| `yivwg` is the observed hourly wage for workers | **[ACCEPTED]** (R-220 s1) |
| non-worker construction incompletely documented and inert | **[ACCEPTED]** (R-220 s2) |
| ten-household audit; 70-hour cap as support projection | **[ACCEPTED]** (R-220 s3) |
| five-hour floor correction; corrected frame sole forward-looking frame | **[ACCEPTED]** (R-222 / R-224 / R-227 s1) |
| NUTS-2 as the finest geography; single-year cross-section | **[ACCEPTED]** |
| singles as the primary application; review closes singles only | **[ACCEPTED]** (R-183 / R-184.1) |
| couples as a parallel module; `GATE_FAIL`; nothing promoted | **[PROVISIONAL]** |
| the three-type semi-flexible design; capability gated; adapter tests pass | **[PROVISIONAL]** (R-227 ss4–8; MNL `8419dd4`) |
| multi-adult households excluded; the five unstated assumptions | **[ACCEPTED]** (R-223 s6 / R-227) |
| equivalence scale as a disclosed normative parameter; calibration identity as a halt | **[ACCEPTED]** as design; **[PENDING]** as evaluation |
| the Goal-1 R-231.4 drafting authorization | **[PENDING — not on disk; register ends at R-227 / R-227.2]** |

### (c) Prohibitions observed in this section

No headline number: no welfare level, no inequality index, no component
magnitude, no share, and no couples estimate. The numerals that appear are
limits disclosures — identification depths, coverage fractions, the size of a
movement or of a gap share, and household counts — not results. No "robust to
X" without its licensed scope: the single robustness statement carried is the
R-184.1 wording with its W1-only, achieved-precision qualifier. No causal
35-hour language: the peak is named as an institutionally motivated 35-hour
opportunity peak and nowhere as an effect of the statute. No unqualified
"ability"; $A_i$ appears only as the reserved ability set. No averaging of the
two reference blocks. No claim that heterogeneity is absent, that regional
demand is irrelevant, or that the non-identification of $A_i$ from $O_i$ has
been resolved. No apology: each limitation is stated as scope with its
evidence, and what the design does not claim is stated as plainly as what it
does.
