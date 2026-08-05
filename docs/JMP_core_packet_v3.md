<!-- GOVERNANCE FRONT MATTER — not manuscript text -->

**Mission:** JMP-M07I — Manuscript Identity Alignment, Stage D (single authorized correction cycle)
**Output file (repository path):** `docs/JMP_core_packet_v3.md`
**Supersedes:** `JMP_core_packet_v2.md`, which supersedes `JMP_core_packet_v1.md` — both retained immutable as history
**Corrections applied:** Stage-B review §7, corrections 1 and 3
**Numerical work:** none performed; no estimate, welfare number or decomposition magnitude is created in this document

**Authoritative inputs used**
- `JMP_M07_deputy_closeout_and_identity_ruling_v1.md` (binding empirical-identity ruling)
- `JMP_M07I_manuscript_identity_alignment_charter_v1.md` (this mission's charter)
- `FR_P2a_empirical_inference_v2.md` (the only permitted numerical source)
- `JMP_core_packet_v1.md`, `JMP_abstract_clean_v1.md`, `JMP_extended_abstract_clean_v1.md`, `JMP_intro_skeleton_v1.md` (documents under revision)
- `JMP_literature_positioning_memo_v2.md` (positioning, carried forward unchanged in substance)

**Binding inputs named by the charter but not supplied to Stage A**
`FR_P2a_inference_appendix_note_v2.md`; `JMP_M07_goal_manager_acceptance_v1.md`; `JMP_M08_welfare_input_handoff_v1.md`; `JMP_project_state_latest.md`. All four were supplied by Stage B or Stage D and their deferrals adjudicated. Consequence retained: this document makes no statement about welfare-design internals or appendix content beyond what `FR_P2a_empirical_inference_v2.md` establishes. See `JMP_project_state_identity_addendum_v2.md` §5.

**Decisions made here**
1. Paper-facing empirical identity is France 2016 single-adult households, P2a region-live, 1,555 households.
2. Couples and pooled 2015–2017 work are recorded as historical/certification anchors and chartered later extensions only.
3. Headline decomposition remains opportunity versus preference; the access-versus-ability split is the nested supporting cut inside the opportunity component.
4. All welfare and decomposition magnitudes are placeholders pending M08 acceptance and the pre-registered LOC4 robustness.

**Unresolved decisions**
- Title divergence: the identity documents carry *Opportunity Constraints as a Driver of Welfare Inequality: A Latent-Jobs Structural Decomposition Approach*; programme governance headers carry *Unequal Job Opportunities and Well-Being Inequality: A Latent-Jobs Structural Decomposition*. The charter forbids a title decision in this mission, so the provisional identity-document title is kept and the divergence is escalated.
- Exact construction of the opportunity-equalization and preference-neutralization counterfactuals is not settled by any accepted artifact. It is deferred to the M08 welfare mission charter or to a subsequently frozen welfare-design artifact. The M08 welfare-input handoff does not contain that construction and is not cited as its source.
- Whether the headline inequality index differs from the Gini (the accepted inference section contemplates both).

**Next authorised action:** Goal 1 Manager acceptance memo (`docs/missions/JMP_M07I_identity_alignment_acceptance_v1.md`). Stage B is complete and the single authorized correction cycle is spent; no further Stage-B round is available under the charter.

---

## 1. Working title

**Opportunity Constraints as a Driver of Welfare Inequality: A Latent-Jobs Structural Decomposition Approach.**

Provisional and unchanged from v1. A title decision is out of scope for JMP-M07I; see the front-matter escalation.

## 2. One-sentence project pitch

A France-based structural labour-supply paper that estimates latent job opportunities in a RURO framework on France 2016 single-adult households, computes money-metric household welfare conditional on the constrained feasible set, and makes the decomposition of welfare inequality into opportunity and preference components — via a Shapley-Shorrocks rule, with the opportunity component split further into access and ability — the central empirical contribution.

## 3. Core question

How much of observed inequality in money-metric well-being is attributable to unequal job opportunities rather than to heterogeneous preferences, once labour supply is modelled as discrete choice over latent job packages and welfare is evaluated under constrained feasible sets?

The question is posed in three-way language. The **opportunity environment** enters through two distinguishable channels: **access**, which governs which job packages are available to whom, and **ability**, which governs the wage a given individual commands within the packages available. **Preferences** govern how a household ranks consumption–leisure bundles among the packages it can reach. The first and headline empirical cut separates the opportunity environment from preferences. The access-versus-ability split is a nested supporting decomposition inside the opportunity component, not a competing headline. The paper's central object is not a welfare ranking and not a reform table, but the mechanism generating welfare inequality.

## 4. Safe empirical claims

**Identity and sample.** The JMP is a single-country **France 2016** structural labour-supply project built on **SRCV / EUROMOD-input microdata**. The accepted empirical application is the **single-adult (P2a) region-live specification**, which contributes **1,555 household observations**. Each household in this sample is single-adult, so each contributes one likelihood term.

**Model.** Labour supply is modelled in a **RURO / latent-jobs** framework with sampled latent alternatives. Job packages differ in the hours they carry, in the occupation they belong to, and in the regional labour market in which they are located; each channel has its own block of access parameters. Wages are governed by an estimated log-wage density. Tax-benefit microsimulation is used **only** to map job packages into disposable income; it is a supporting input to the budget mapping, not the paper's behavioural contribution.

**Estimation and inference (accepted).** Inference uses a sandwich covariance estimator with likelihood contributions clustered at the household level, giving **1,555 clusters**, and a finite-sample correction scalar of **1555/1520** of the HC1/CR1 family. Because each household contributes one likelihood term, the robust standard errors are correctly described as **misspecification-robust rather than dependence-robust**. The parameter vector has **47 coordinates**: **10 pinned**, **37 free**, of which **2 sit at an active upper bound** and **35 are interior**. The covariance object supporting symmetric inference is therefore **conditional and 35-dimensional**, and active-bound and pinned coordinates carry literal `NA` in every inferential field. Both model-based and robust covariance matrices are reported.

**Findings that may be stated.** The regional/urbanisation/GSUR access block is **jointly relevant**: the joint restriction of all ten coordinates to zero is rejected (robust Wald `37.45`, 10 df, robust *p* = `4.7e-05`). Within that block, the restriction on the single GSUR coordinate is rejected on its own (robust Wald `29.21`, robust *p* = `6.5e-08`; point estimate `beta_E_gsur = -1.105`, robust 95% interval `[-1.51, -0.70]`), while the joint restriction on the seven NUTS-1 dummies is **not rejected** (robust *p* = `0.594`) and the joint restriction on the two urbanisation indicators is **not rejected** (robust *p* = `0.847`). The paper's bounded statement of this result is: *at the resolution and specification studied, measured access heterogeneity is concentrated in one GSUR dimension rather than diffuse across broad NUTS-1 geography or the two urbanisation indicators.* Test verdicts do not depend on the choice of variance estimator.

**Wage density.** The certified baseline uses a **single log-wage density with a common dispersion parameter**, shifted in location by education and potential experience. A **four-density LOC4 variant** is pre-registered as the first mandatory wage-density robustness axis; it has not been estimated and no LOC4 result exists.

**Near-boundary diagnostic.** One pre-registered non-gating diagnostic did not pass: robust symmetric intervals for `beta_l0_sm` and `beta_w_pexp2` approach the relevant parameter boundary. This is disclosed as a local diagnostic, is not gating, did not reopen estimation, and routes into a **pre-registered four-scenario admissible local sensitivity** at the welfare stage.

**Welfare and decomposition (design, not results).** The welfare object is **money-metric household welfare** constructed conditional on the constrained feasible set; in this application every household is single-adult. The baseline inequality index is the **Gini of household welfare**, with the headline index reported where it differs. The decomposition is a **Shapley-Shorrocks** attribution of measured welfare inequality to an **opportunity-attributable** component and a **preference-related** component, reported alongside the **opportunity share**, with the nested access/ability split inside the opportunity component.

**Boundary.** The paper is an **empirical structural JMP**, distinct from the separate axiomatic theory paper co-authored with F. Maniquet.

**Historical/certification anchor (technically necessary).** Eight couples leisure coordinates in the 47-coordinate vector are pinned because the singles objective does not reference them, and two survey-year dummies are pinned because their covariates are identically zero in a 2016-only sample. These coordinates are retained for completeness of the parameter vector and carry no inferential content in this application. This is the only context in which couples and pooled years may appear as anything other than a chartered later extension.

## 5. Claims I should not make yet

- **No welfare or decomposition magnitude exists.** Do not state, imply or place a number on the opportunity share, the welfare Gini, or any component of the decomposition. M08 has not been accepted.
- **Do not claim clean separation.** Do not say that preferences and opportunities are cleanly separated in the data, or that the split is identified beyond the maintained structural assumptions.
- **Respect strict non-rejection language.** A failure to reject the NUTS-1 or urbanisation restrictions is *not* evidence that those coordinates are zero, and the battery is silent about regional dimensions outside the tested coordinates.
- **Do not label `gsur`.** No substantive interpretation of the GSUR coordinate beyond its design-column identity is asserted anywhere.
- **Do not over-read stability across variance estimators.** Agreement of model-based and robust verdicts is stability of the verdicts, not evidence of correct specification.
- **No causal or policy claims.** The access battery is a statement about an estimated structural model; it supports no causal claim about the effect of location on employment and no policy conclusion.
- **No unconditional active-set claim.** All reported inference is conditional on the observed active set; an unconditional claim triggers the existing Tier-2 halt.
- **No responsibility label on estimated components.** The preference-related component of the decomposition is a preference-related component and nothing more. The paper's responsibility-sensitive reading is a stated interpretive stance of the authors, not a property established by the estimates.
- **Do not freeze preferred magnitudes before LOC4**, and do not substitute asymptotic delta-method standard errors for the sequenced bootstrap.
- **Do not present couples or pooled years as delivered results**, as co-primary applications, or on a timetable. Equally, do not describe the singles application as a fallback or as obsolete; that characterisation is superseded. As a governance condition stated here rather than inside the staged-extension sentence: under the deputy ruling the couples and pooled-year extension is future work conditional on successful validation of the singles pipeline. This condition governs mission sequencing and must not be appended to the authorized staged sentence in any paper-facing document.
- **Do not drift** into country-ranking language, into reform-incidence framing, or into the separate axiomatic theory project.

## 6. Current abstract

Reproduced from `manuscript/JMP_abstract_clean_v2.md`. See that file for the controlling text.

## 7. Current extended abstract

Reproduced from `manuscript/JMP_extended_abstract_clean_v2.md`. See that file for the controlling text.

## 8. Baseline France application

The baseline is **France 2016, SRCV / EUROMOD-input cross-section, single-adult (P2a) region-live sample, 1,555 households**, estimated in a **RURO / latent-jobs** framework with sampled latent alternatives. The unit of welfare analysis is the **household**; in this application each household is single-adult. Preferences are Box-Cox in consumption and leisure with sex-specific singles leisure terms. The opportunity environment enters through an **access block** — hours bands, occupation groups, and the regional/urbanisation/GSUR dimension — and through an **estimated log-wage density** shifted by education and potential experience, which is the channel through which ability-related characteristics operate. Disposable income for each sampled alternative is computed through EUROMOD under French tax-benefit rules. The welfare object is **money-metric household welfare conditional on the constrained feasible set**; the baseline inequality index is the **household welfare Gini**; the baseline decomposition is a **Shapley-Shorrocks** attribution to opportunity and preference components, with access and ability nested inside the opportunity component.

This is the application for which accepted estimation and inference evidence exists, and it is therefore the writing anchor for every paper-facing empirical statement. The authorized staged-extension sentence, used verbatim and without addition:

> The empirical analysis first establishes the complete estimation–welfare–decomposition pipeline for France 2016 single-adult households; extension to couples and pooled years is subsequent work.

## 9. Main table

**Table 1: France 2016 singles P2a decomposition of household welfare inequality.** Core columns: baseline household welfare Gini; welfare Gini after opportunity equalization; welfare Gini after preference neutralization; welfare Gini after both adjustments; Shapley share attributed to the opportunity environment; Shapley share attributed to preference heterogeneity. A nested panel reports the split of the opportunity share into access and ability. All cells are `[[WELFARE MAGNITUDE — PLACEHOLDER, M08]]` until the M08 acceptance packet exists, and no cell is frozen as a preferred magnitude before the LOC4 four-density robustness is completed. The pre-registered four-scenario W-4 sensitivity (baseline; `beta_l0_sm` perturbed; `beta_w_pexp2` perturbed; both perturbed) is reported alongside, with all changes reported continuously including changes below the materiality thresholds.

The exact construction of the two counterfactuals is not specified in this document and is not settled by any accepted artifact; it is deferred to the M08 welfare mission charter or to a subsequently frozen welfare-design artifact.

## 10. Main figure

**Figure 1: Shapley decomposition of the France 2016 singles household welfare Gini.** A single stacked bar showing the opportunity and preference contributions to household welfare inequality, with the opportunity segment subdivided into access and ability. Deliberately simple in the first version; alternative circumstance definitions, richer job hierarchies and alternative welfare measures are postponed until the baseline result exists.

## 11. Immediate writing priority

Standardise all project-facing text on one stable paper identity: **France 2016 single-adult households (P2a region-live, 1,555 households), RURO / latent job packages, money-metric household welfare conditional on constrained feasible sets, household welfare Gini, Shapley-Shorrocks decomposition into opportunity and preference with a nested access/ability cut.** In practice this means that the abstract, extended abstract, introduction skeleton and any supervisor-facing note use the same baseline wording, carry the accepted inference statements with their exact caveats, use placeholders for all welfare magnitudes, and confine couples and pooled years to a single staged-extension sentence. The writing keeps decomposition as the central contribution, keeps the paper distinct from the separate theory project, and states the empirical status honestly: estimation and inference accepted, welfare integration and decomposition not yet delivered.

## 12. Immediate empirical priority

Sequencing is set by the deputy closeout, not by this document. The authorised primary mission is **JMP-M08 — France 2016 Singles Welfare Integration and Baseline Decomposition Prototype**, which is a point-estimate prototype and functional-sensitivity mission rather than the final welfare-inference freeze. Its gating conditions, as recorded in the closeout: the existing singles welfare-integration blockers must be resolved before any welfare number is promoted; the four-scenario W-4 sensitivity is mandatory; LOC4 Path B is binding, so M08 runs on the certified baseline and LOC4 is the first mandatory robustness afterwards; no preferred quantitative decomposition magnitude is frozen before LOC4; and bootstrap uncertainty is sequenced after the preferred specification is resolved, with no delta-method substitute. JMP-M07I neither adds to nor relaxes any of this.
