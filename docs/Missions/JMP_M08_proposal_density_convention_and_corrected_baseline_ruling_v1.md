# JMP-M08 Deputy Ruling — Proposal-Density Convention and Corrected Baseline v1

**Programme:** Goal 1 — Empirical JMP  
**Decision-maker:** Deputy Programme Director  
**Date:** 2026-08-18  
**Status:** Binding  
**Classification:** Econometric estimand consistency; pre-welfare halt  
**EUROMOD:** Not authorised for this mission  
**Current M08 welfare execution:** Halted  
**Current P2a estimate:** Preserved as certified historical specification; suspended as paper-facing welfare input

## 1. Decision

Reject the proposed disclosure-only disposition.

The welfare axis may not use the exact marginal proposal density while retaining
as its structural input a parameter vector estimated under a non-equivalent
joint component–hours correction.

The project’s paper-facing model defines alternatives by economically relevant
job attributes. The proposal component is a sampling device and is not an
economic job attribute, utility argument, opportunity channel, or decomposition
factor. Therefore the relevant proposal density on the paper’s job space is the
density induced on that space after integrating out the proposal-component
label, unless a formal sampled-choice derivation proves that the accepted
likelihood targets a different explicitly augmented economic choice space.

The manager’s verification has already refuted the only proposed shortcut:
the joint-versus-marginal difference is not absorbed by the accepted hours and
employment coefficients and changes the likelihood at fixed parameters.

Consequently:

1. the accepted P2a computation remains certified **for the exact joint-labelled
   convention it implemented**;
2. it is not overwritten, called a software failure, or retrospectively altered;
3. it is suspended as the parameter source for M08 welfare;
4. a bounded proposal-correction consistency mission must determine the correct
   sampled-choice estimand and, on the expected marginal-density finding,
   produce a newly estimated and inferred baseline;
5. no welfare, decomposition, S-10, LOC4, notebook-v3, or paper-facing
   quantitative result proceeds until that corrected baseline is accepted.

## 2. Why disclosure-only is not sufficient

A proposal convention is ancillary only when changing it leaves the same
population objective and the same structural parameter vector.

That condition fails here:

- the proposal components overlap on the hours support;
- the component label is not part of the structural job description;
- the joint correction and marginal correction are not related by a
  household-common or alternative-common constant;
- the difference is not in the span of the accepted hours/employment index;
- the chosen-row treatment prevents an otherwise proposed absorbing direction;
- a likelihood probe detects a non-zero objective difference.

Using the old \(\widehat\theta\) with the marginal welfare correction would
therefore combine:

- parameters from one sampled-likelihood estimand; and
- welfare from a different job-space integration convention.

That would violate the JMP’s central consistency requirement across estimation,
welfare measurement, and decomposition.

## 3. Scientific status of the two conventions

### 3.1 Historical joint-labelled convention

The old convention may be described as internally reproducible for an augmented
draw space in which the proposal-component label is retained.

It must not be described as automatically equivalent to the proposal marginal on
the economic job space. Its scientific interpretation requires an explicit
target measure on the augmented space, including the treatment of overlapping
components and the deterministically included chosen alternative.

The accepted P2a estimate and Phase-3/4/5 artifacts remain immutable history
under this label.

### 3.2 Marginal job-space convention

The welfare implementation’s exact D1 marginal is the leading correct convention
for the paper’s job space:

\[
q_H^{marg}(h)
=
\sum_c \alpha_c q_H(h\mid c),
\]

or the exact stratified/multiple-importance-sampling analogue implied by the
actual fixed-allocation draw algorithm.

It must be derived from the actual sampler, not assumed from generic mixture
notation.

## 4. Authorised successor mission

Authorise:

**JMP-M08E — Proposal-Correction Consistency and Corrected Empirical Baseline**

This is a bounded econometric correction mission, not a general software or
model-expansion programme.

### Stage E0 — exact sampled-choice derivation

Produce:

`Job_Market_paper/docs/Missions/JMP_M08E_proposal_correction_estimand_audit_v1.md`

The audit must derive, from the executed draw algorithm and accepted likelihood:

1. the economic alternative space;
2. whether the proposal-component label belongs to that space;
3. whether component counts are random-mixture or fixed-stratum draws;
4. the correct proposal density or multiple-importance-sampling weight for an
   employed hours draw;
5. the correction for the deterministically included chosen alternative;
6. the correction for non-employment;
7. the product construction with occupation and wage draws;
8. whether duplicate economic alternatives generated by different components
   represent duplicate jobs or duplicate numerical nodes;
9. the exact population objective approximated by the old and proposed
   conventions;
10. a proof or falsification of equivalence.

Required analytic tests:

- integrate at least three known functions over the hours support, including a
  constant, a band indicator, and a smooth non-constant function;
- show which estimator is unbiased/consistent for the intended integral;
- reproduce the 14-cell delta table and the likelihood positive control;
- test the chosen-row rule in a toy choice problem with an analytic denominator.

### Stage E0 decision gate

- If the audit proves the old joint convention is correct for the intended,
  explicitly defined economic job space, halt and return to the deputy because
  the welfare axis must then be redefined to the same augmented estimand.
- If the audit confirms the marginal or exact MIS convention for the unlabeled
  job space, proceed autonomously to E1–E5.
- If neither convention is valid because the chosen-row hybrid requires a third
  correction, use that derived correction and record it before any full-sample
  execution.

## 5. Corrected-baseline path if the marginal/MIS convention is confirmed

### Stage E1 — immutable corrected proposal fields

Create a new application-specific engine-ready input and specification identity.
Do not overwrite the accepted P2a frame.

The new frame must preserve bitwise:

- household sample;
- alternative draws;
- chosen indicators;
- wages, hours, occupation, and all covariates;
- priced consumption;
- proposal component labels;
- all accepted non-proposal columns.

Change only the explicitly audited proposal-density fields:

- exact marginal/MIS `log_q_H`;
- exact total `log_prior`;
- exact `prior`;
- any chosen-row correction required by E0.

Persist old and new fields side by side in the restricted construction evidence
until acceptance.

The Goal 1 Manager must register a non-colliding successor specification
identifier after repository inspection. The old `P2a` identifier is not reused.

### Stage E2 — corrected likelihood implementation and tests

Prefer a data/configuration correction using the accepted generic likelihood
engine. Do not modify `dclaborsupply` source unless technically unavoidable.

Required tests:

1. exact analytic marginal/MIS identity;
2. proposal mass equals one under the relevant base measure;
3. no component label enters utility or structural opportunity terms;
4. old objective reproduced bitwise when old prior fields are selected;
5. corrected objective reproduced independently by NumPy and JAX;
6. chosen-first and row-order contracts unchanged;
7. no raw or priced data mutation;
8. synthetic recovery under the corrected convention;
9. a deliberately wrong joint correction fails the analytic toy test.

A generic package change is a deputy escalation.

### Stage E3 — corrected estimation

Use the accepted P2a parameter vector as a warm start, but perform a genuine
full-sample optimisation under the corrected objective.

Required:

- the accepted sample of 1,555 households;
- the same structural utility and opportunity specification;
- the same pins and bounds unless the new optimum mechanically requires a
  pre-registered numerical treatment;
- at least one independent perturbation/start check;
- explicit objective improvement and convergence diagnostics;
- no EUROMOD execution.

The corrected estimate becomes a candidate baseline only after the synthetic
recovery and convergence gates pass.

### Stage E4 — curvature and inference

Run the existing accepted Phase-4 and Phase-5 numerical pipelines against the
corrected estimate:

- exact JAX Hessian;
- rank and eigenvalue diagnostics;
- regional Schur diagnostics;
- conditional active-set inference;
- full-sample streaming robust covariance;
- named H0-A/B/C/G battery;
- W-4/S-10 routing under the corrected estimate.

Do not reopen general Phase-5 software certification. This is a new numerical
application of the accepted inference machinery.

### Stage E5 — independent economics/econometrics review and acceptance

Use:

- GPT-5.6 Codex for one bounded production-path review of the corrected proposal
  construction and objective;
- GPT-5.6 Thinking for one independent econometric/results review.

Acceptance requires:

1. the proposal correction matches E0 exactly;
2. the corrected input differs only in authorised proposal fields;
3. the estimator targets the intended unlabeled job space;
4. synthetic recovery passes;
5. estimation, curvature, and inference gates pass;
6. every new result traces to accepted artifacts;
7. the old and new conventions are compared without retroactively discrediting
   the old computation;
8. a successor welfare-input handoff is frozen.

## 6. Required comparison and manuscript treatment

Produce a comparison table containing:

- old and corrected objective at the old estimate;
- old and corrected optimum objective;
- parameter differences;
- changes in active bounds;
- changes in H0-A/B/C/G;
- changes in the W-4 coordinates;
- any changed qualitative access conclusion.

The old P2a result is described as:

> the certified historical estimate under the joint component–hours proposal
> convention.

The corrected result, if accepted, becomes:

> the paper-facing estimate under the job-space marginal/MIS proposal
> convention used consistently in estimation and welfare integration.

Do not call the difference a robustness exercise. It is an estimand-consistency
correction.

The accepted M07 inference section is frozen as historical v2. If the corrected
results are accepted, create a new inference revision through a bounded
manuscript-integration task; do not silently edit the old accepted files.

## 7. Effect on M08, U6, LOC4, package, and notebook

### M08 and U6

Hold the completed \(q^W\) code and tests. Do not delete them and do not price
new nodes.

After the corrected estimate is accepted:

- rebind \(q^W\) and every coalition target to the corrected parameter vector;
- rerun all pre-EUROMOD proposal and normalisation tests;
- then resume U6-C Codex review and the pricing ladder.

### LOC4

LOC4 remains mandatory but is downstream of the corrected baseline. Do not run
LOC4 against the suspended P2a estimate.

### Package

Keep `dclaborsupply` source frozen. Escalate only if the accepted engine cannot
consume the corrected proposal fields without a generic change.

### Notebook

Keep `fr_singles_pipeline_v2.ipynb` frozen.

The successor notebook is delayed until:

1. the corrected baseline is accepted;
2. M08 welfare/decomposition is accepted.

Then create `MNL/notebooks/france/fr_singles_pipeline_v3.ipynb` from accepted
production scripts and manifests. Do not use the notebook to implement or debug
this correction.

## 8. Documentation proportionality

Permanently retain only:

1. this deputy ruling;
2. one estimand-audit memo;
3. corrected code/config/input manifests;
4. one Codex review;
5. corrected estimation/curvature/inference result packet;
6. one independent econometric review;
7. one acceptance and M08 handoff.

Routine prompts, action cards, and progress notes remain disposable chat.

## 9. Return conditions

Return to the deputy if:

- E0 concludes the old joint convention is the correct estimand;
- the chosen-row correction cannot be derived;
- the corrected convention requires changing structural utility or opportunity
  terms;
- a generic package change is required;
- synthetic recovery fails;
- the corrected model does not converge or has unacceptable curvature;
- Phase-5 inference cannot be produced;
- the corrected result overturns the paper’s core empirical mechanism;
- disclosure cannot be controlled.

Otherwise, the Goal 1 Manager may manage E0–E5 autonomously and return only with
the accepted corrected-baseline packet and revised M08 handoff.
