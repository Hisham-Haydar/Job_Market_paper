# MISSION JMP-M05 — Household-Clustered Inference

**Mission status:** Authorized for design only  
**Date:** 2026-07-30  
**Programme:** Goal 1 — Empirical JMP

## 1. Programme goal

Produce a publishable empirical JMP on opportunity-sensitive money-metric well-being inequality.

This mission establishes statistically defensible uncertainty quantification for the accepted France 2016 singles P2a estimate.

## 2. Paper contribution

The paper cannot report parameter uncertainty, regional-block significance, later welfare uncertainty, or decomposition uncertainty without a certified inference layer.

This mission unlocks a defensible statement about the precision of preference and opportunity parameters while preserving the distinction between interior parameters, active-bound parameters, and fixed pins.

## 3. Canonical starting state

- MNL HEAD: `982c52217031158c4a2368709d4a6b211ebcde76`
- Nested `dclaborsupply` HEAD and MNL gitlink:  
  `27756a06ea189339aa82915ed2124628afed20eb`
- Phase-3 bundle SHA-256:  
  `2cf237648743f59bd742b12feceaea67c5fd377b26faf4fb6fad6f452f86864b`
- Phase-4 bundle SHA-256:  
  `5484886985aecd28e511719e42f45b85ad0e1755d1f951dbd13a79281d9665f3`
- Households/clusters: 1,555
- Alternatives per household: 101
- Total parameters: 47
- Free parameters: 37
- Fixed pins: 10
- Active-bound free parameters:
  - `beta_l_age2_sm`
  - `beta_l_age2_sf`
- Accepted negLL: `19053.46553160093`
- Accepted free Hessian: 37×37, rank 37, strictly positive definite

## 4. Research question

What model-based and household-cluster-robust uncertainty measures are statistically defensible for the accepted parameter vector, especially for the ten regional/access parameters and the 35 interior free parameters?

## 5. Scope

Design only:

1. household log-likelihood score contributions;
2. model-based covariance;
3. household-cluster-robust sandwich covariance;
4. finite-sample correction;
5. active-bound treatment;
6. fixed-pin reporting;
7. regional/access individual and joint tests;
8. numerical gates;
9. immutable output contract;
10. package/API implications.

## 6. Non-scope

Do not:

- implement code;
- compute scores or covariances;
- run inference;
- invoke optimizer, gradient, or Hessian;
- run synthetic recovery;
- run welfare, decomposition, EUROMOD, or notebooks;
- alter the accepted estimate or artifacts;
- redesign the RURO specification;
- broaden into couples, pooled years, or alternative countries.

## 7. Authoritative files

Governance:

- `docs/governance/JMP_program_governance_v1.md`
- `docs/governance/JMP_canonical_state_v1.md`
- `docs/governance/JMP_roadmap_v1.md`
- `docs/governance/JMP_decision_log_v1.md`

Accepted evidence:

- `FR_P2a_region_live_phase3_manager_acceptance_v1.md`
- `FR_P2a_region_live_phase4_manager_acceptance_v1.md`
- `FR_P2a_region_live_phase4_execution_report_v2.md`
- `phase4_diagnostics.json`
- `optimizer_diagnostics.json`
- `estimation_results.json`
- `theta_estimated.csv`
- current specification and parameter-map sources;
- current JAX likelihood and score-related sources.

Exact repository paths must be verified rather than guessed.

## 8. Decisions already frozen

- cluster is household `idhh`;
- cluster count is exactly 1,555;
- all 101 alternatives for one household belong to one cluster;
- free-vector dimension is 37;
- fixed pins are excluded from differentiation;
- score identity is:
  \[
  \sum_g s_g = -\nabla \mathrm{negLL};
  \]
- score-identity tolerance remains:
  `np.allclose(..., atol=1e-8, rtol=1e-8)`;
- bread derives from the accepted negLL Hessian;
- no optimizer may run;
- Phase 5 does not replace synthetic recovery.

## 9. Decisions to be made

The design memo must recommend one baseline for each:

1. **Finite-sample correction**
   - CR0;
   - cluster-only \(G/(G-1)\);
   - or a justified two-factor correction.

2. **Active-bound treatment**
   - reporting rule for the two active-bound parameters;
   - covariance object for the 35 interior parameters;
   - interpretation limits for symmetric Wald inference.

3. **Score artifact**
   - committed CSV;
   - committed binary artifact;
   - or hashed binary artifact plus committed summaries.

It must also decide:

4. fixed-pin standard-error representation;
5. regional-block covariance and joint-test protocol;
6. exact numerical gates and tolerances.

## 10. Pre-registered gates

A design is acceptable only if it:

- defines household scores formally and unambiguously;
- fixes the sign convention;
- explains sample scaling;
- uses stable solves rather than unnecessary explicit inverses;
- specifies a defensible finite-sample correction;
- treats active-bound parameters non-naively;
- reports pins in a way that cannot be mistaken for estimated certainty;
- defines model and robust regional-block inference;
- gives exact shapes, fingerprints, and validation gates;
- preserves Phase-3 and Phase-4 dependencies;
- separates real-data inference from synthetic recovery;
- avoids France-specific assumptions in any proposed package API.

## 11. Required artifacts

Planning artifact:

- `docs/missions/JMP_M05_task_plan_v1.md`

Design artifact:

- `docs/France_case/P2a/FR_P2a_region_live_phase5_inference_design_v1.md`

No code or result artifacts are authorized in this mission stage.

## 12. Tool allocation

- Top-level mission and acceptance: ChatGPT JMP project
- Task planning: Claude Project 1, Sonnet, thinking on
- Statistical design memo: Claude Project 1, Opus, thinking on
- Targeted literature verification: Deep Research only if a narrow unresolved issue remains
- Code implementation: not authorized
- Independent code review: not applicable until implementation is authorized

## 13. Halt conditions

Stop and return to the programme manager if:

- canonical files conflict;
- exact score or likelihood source cannot be verified;
- parameter ordering is ambiguous;
- cluster count differs from 1,555;
- a design requires changing the accepted model;
- the finite-sample correction cannot be justified;
- active-bound treatment is left unresolved;
- the task expands into implementation.

## 14. Commit policy

Do not commit the task plan or design memo before manager review.

No code, outputs, or repository state may be changed.

## 15. Return packet

Return:

1. `JMP_M05_task_plan_v1.md`;
2. later, `FR_P2a_region_live_phase5_inference_design_v1.md`;
3. exact authoritative file list used;
4. unresolved source-path or statistical questions;
5. recommended answers to the three manager decisions.

## 16. Next action after acceptance

After the design memo is accepted and the three manager decisions are frozen, create a separate Phase-5 implementation-and-certification mission charter.
