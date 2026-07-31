# JMP-M05 Task-Plan Manager Acceptance v1

**Mission:** JMP-M05 — Household-Clustered Inference  
**Artifact reviewed:** `JMP_M05_task_plan_v1.md`  
**Manager verdict:** ACCEPTED WITH BINDING CORRECTIONS  
**Commit status:** Do not commit until the Goal 1 manager integrates this acceptance into the mission ledger.

## 1. Accepted elements

The task plan correctly:

- keeps the stage design-only;
- identifies the required parameter-map, likelihood, bounds, weighting, clustering, and Hessian sources;
- refuses to invent paths;
- distinguishes the 47-, 37-, and proposed 35-dimensional parameter spaces;
- recognizes the inferential complication created by two active-bound parameters;
- treats the ten fixed pins separately from estimated parameters;
- centers household scores and the ten regional/access parameters;
- treats the finite-sample correction as a convention requiring an explicit definition;
- requires source verification before finalizing the design memo.

The verdict `READY WITH SOURCE GAPS` is accepted.

## 2. Missing handoff information

The prior governance-checkpoint return was not supplied to the deputy programme director.

The Goal 1 manager must retrieve and record:

- current `Job_Market_paper` HEAD;
- the commit containing the governance files;
- exact committed governance-file list;
- clean/dirty status of the repository.

This is a provenance gap, not a reason to stop JMP-M05 unless the governance files are uncommitted or inconsistent.

## 3. Binding correction C-1 — Likelihood benchmark

The task plan states that a fitted choice-only likelihood cannot have average negLL above `ln(101)`.

That conclusion is too categorical without first establishing:

- that a uniform-choice parameterization is feasible under the actual proposal/prior corrections and offsets;
- that the accepted objective is an unweighted sum of one discrete-choice term per household;
- that no continuous-density or normalization terms enter;
- that the optimizer reached an objective no worse than the feasible uniform benchmark.

The source audit must treat the observed `12.25` nats per household as a diagnostic clue, not proof of continuous-density terms.

The design memo must use only the verified likelihood composition.

## 4. Binding correction C-2 — Scope of the regional test

The ten regional/access parameters are not automatically the whole opportunity mechanism.

A joint null on these ten parameters tests the modeled regional/urbanisation/GSUR access block. It must not be described as:

- no opportunity heterogeneity of any kind;
- the complete opportunity-versus-preference test;
- a direct test of the final decomposition share.

The headline opportunity component may also depend on wage/ability, hours, occupation, proposal, or other offer-side mechanisms actually present in the accepted specification.

## 5. Binding correction C-3 — Cluster terminology

If each household contributes one primitive household likelihood term, the household-cluster sandwich equals the household-level OPG sandwich.

The design memo may then describe it as household-clustered and misspecification-robust, while explaining the algebraic equivalence.

It must not claim that clustering will necessarily become non-degenerate for couples or pooled years. That depends on the primitive likelihood contribution and repeated-unit structure actually implemented.

## 6. Binding correction C-4 — Active-bound covariance

The task plan's proposed 35-dimensional conditional covariance is a working hypothesis, not an accepted decision.

The design memo and independent reviewer must establish:

- the exact active-bound direction and KKT consistency;
- whether conditioning on the active set is the intended estimand;
- the correct conditional bread and meat;
- the limits of treating the active set as fixed;
- whether any alternative boundary-aware inference is required for paper claims.

No symmetric Wald inference may be reported for the two active-bound parameters under the baseline unless a later approved method justifies it.

## 7. Binding correction C-5 — Opportunity-language discipline

The regional block is important evidence about one access channel. It is not by itself the empirical carrier of the entire paper's opportunity claim.

All design and paper-facing language must distinguish:

- regional/access block inference;
- full opportunity mechanism;
- later welfare decomposition.

## 8. Delegated next stage

The Goal 1 manager is authorized to complete the remainder of the JMP-M05 design stage without returning after each task.

Required sequence:

1. read-only source verification;
2. Goal 1 manager acceptance of the source report;
3. inference design memo;
4. independent methodological review;
5. no more than two narrow remediation cycles;
6. final Goal 1 manager decision packet.

No code implementation or real inference is authorized.

## 9. Required final return

Return to the deputy programme director only with:

- source-verification report;
- final inference-design memo;
- independent methods-review report;
- Goal 1 manager acceptance memo;
- mission ledger;
- completed decision summary for:
  - finite-sample correction;
  - active-bound treatment;
  - fixed-pin reporting;
  - score artifact;
  - regional joint tests;
- exact remaining open decisions;
- recommendation on whether to launch the implementation mission.
