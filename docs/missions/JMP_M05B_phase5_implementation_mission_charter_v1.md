# MISSION JMP-M05B — Phase-5 Inference Implementation and Certification

**Programme:** Goal 1 — Empirical JMP  
**Mission stage authorized:** implementation through audited full dry run  
**Production real run:** not authorized  
**Manager:** Goal 1 Manager — Empirical JMP

## 1. Programme contribution

Implement and certify the accepted Phase-5 household-level inference design for
the France 2016 singles P2a region-live estimate.

This mission must produce a review-approved, committed implementation and one
audited full real-data dry run. It must not produce or promote an accepted
production inference result.

## 2. Binding design

The implementation must match exactly:

- `FR_P2a_region_live_phase5_inference_design_v4.md`;
- `FR_P2a_region_live_phase5_inference_methods_review_v1.md`;
- `FR_P2a_region_live_phase5_inference_methods_recheck_v1.md`;
- `FR_P2a_region_live_phase5_inference_micro_recheck_v2.md`;
- `JMP_M05_deputy_programme_acceptance_v1.md`;
- `JMP_M05_PI_disclosure_determination_v1.md`.

The Goal 1 Manager must replace the revision placeholders below with the exact
documentation checkpoint SHAs before commissioning implementation:

- `983a2ecf1d16592b9f90085f6a6b690b8a964110`
- `f7cac339d54c4622e2ac0c9b9710070209fc7a6f`

This mechanical substitution may not change mission substance.

## 3. Accepted numerical dependencies

- numerical application anchor:
  `982c52217031158c4a2368709d4a6b211ebcde76`;
- nested dclaborsupply HEAD/gitlink:
  `27756a06ea189339aa82915ed2124628afed20eb`;
- Phase-3 bundle:
  `2cf237648743f59bd742b12feceaea67c5fd377b26faf4fb6fad6f452f86864b`;
- Phase-4 bundle:
  `5484886985aecd28e511719e42f45b85ad0e1755d1f951dbd13a79281d9665f3`;
- accepted negLL:
  `19053.46553160093`;
- 47 total, 37 free, 35 interior, 10 pins, 2 active upper bounds;
- 1,555 household contributions/clusters;
- authoritative bread:
  Phase-4 `hessian_free.npy`, loaded and symmetrised as specified.

The later documentation HEAD must be a clean descendant of the numerical
application anchor.

## 4. Scope

Implement in MNL:

1. Phase-5 contract and dry-run/real-run runner integration;
2. exact 47→37→35 name-keyed mapping;
3. household per-group score construction;
4. score identity and fresh-process reproduction;
5. model and robust covariance;
6. finite-sample correction `1555/1520`;
7. active-bound and pin reporting;
8. regional/access covariance and H0-A/B/C/G tests;
9. T-1 through T-23 and warning-tier diagnostics;
10. immutable transaction structure;
11. restricted-custody score-artifact handling;
12. environment and provenance logging;
13. deterministic tests and documentation.

Do not change the accepted model, theta, likelihood, input data, draws, pricing,
parameter values, pins, or bounds.

## 5. Package boundary

Do not modify `dclaborsupply-monorepo` in this mission.

If implementation reveals a genuinely generic package deficiency, document it
as a proposed `PKG-M02` issue and continue only if the MNL application can use a
thin local adapter without duplicating or changing the likelihood.

Any required upstream package change is an E2 halt requiring a separate package
mission.

## 6. Frozen statistical decisions

- household score is the derivative of each verified per-group log-likelihood;
- sum of household scores equals negative negLL gradient;
- score identity uses `atol=1e-8`, `rtol=1e-8`;
- canonical row order is `idhh` ascending by stable argsort;
- conditional covariance is 35×35;
- bread is `H_II^-1`;
- robust meat uses 35 selected score columns;
- correction scalar is `1555/1520`;
- no symmetric inference for active-bound or pinned coordinates;
- H0-A is confirmatory; H0-B/C/G are secondary;
- regional tests do not represent the complete opportunity mechanism;
- authoritative score bytes use restricted custody.

## 7. Implementation architecture

Prefer one Phase-5 runner or a narrowly integrated Phase-5 branch in the
existing P2a runner, following the established Phase-3/4 contract and
transaction conventions.

The implementation must expose testable pure helpers for:

- parameter mapping;
- canonical score ordering;
- score aggregation;
- restricted meat;
- bread construction;
- finite-sample correction;
- covariance diagnostics;
- regional selectors/restrictions;
- reporting-table population;
- disclosure/custody metadata;
- manifest and bundle hashing.

Do not duplicate the likelihood or loader logic.

## 8. Required tests

At minimum:

1. exact 47/37/35 map and fingerprints;
2. active-bound/pin status;
3. cluster count and canonical order;
4. synthetic score-identity fixture;
5. production-route score aggregation without running the full dry run;
6. bread hash and symmetrisation;
7. PSD/backward-error gates including certified T-7 constant;
8. covariance algebra and correction scalar;
9. regional restriction dimensions and name-keying;
10. NA reporting contract;
11. custody metadata and T-23;
12. no optimizer/respecification/welfare/EUROMOD route;
13. transaction and failure preservation;
14. review binding and revision gates;
15. dry-run cannot publish `complete/`;
16. real run remains refused before a later execution authorization.

Tests must not alter accepted artifacts.

## 9. Independent code review

Use Codex in read-only mode after implementation and non-real tests pass.

The reviewer must verify:

- exact conformance to design v4;
- no duplicated/reinterpreted likelihood;
- no package modification;
- no optimizer;
- all T/W gates implement the approved formulas;
- active-bound and pin treatment;
- score artifact disclosure handling;
- transaction safety;
- deterministic tests;
- dry-run/real-run authorization separation.

Required review file:

`docs/France_case/P2a/FR_P2a_region_live_phase5_code_review_v1.md`

Verdict:

- APPROVE;
- APPROVE AFTER FIXES;
- REJECT.

Allow up to two narrow code-remediation cycles. E2 issues escalate.

## 10. Commit gate

After exact review APPROVE:

- commit the reviewed implementation and review;
- require clean MNL and nested worktrees;
- bind the dry run to exact MNL HEAD, nested HEAD/gitlink, review path and hash,
  Phase-3 bundle, and Phase-4 bundle.

Recommended commit message:

`feat(p2a): implement reviewed Phase-5 inference gate`

## 11. Full dry run

After commit and clean preflight, authorize exactly one full dry run over all
1,555 households.

The dry run may compute scores and covariance objects but:

- must write only under `attempts/dryrun_<timestamp>/`;
- must not create or promote `complete/`;
- must use restricted custody for household-level score bytes;
- must preserve a stopped attempt on any gate failure;
- must not be rerun without Goal 1 manager review.

## 12. Required dry-run return packet

Return to the Goal 1 Manager:

- implementation report;
- code review;
- committed MNL HEAD;
- review SHA;
- full dry-run console, diagnostics, and manifest;
- non-disclosive score summary;
- covariance and regional-test diagnostics;
- exact T-1–T-23 and warning outcomes;
- custody metadata with non-public locator redacted as needed;
- repository statuses;
- confirmation no `complete/` exists.

## 13. Mission acceptance gate

The Goal 1 Manager performs a factual dry-run audit and creates:

`JMP_M05B_goal_manager_dryrun_acceptance_v1.md`

Return to the ChatGPT deputy programme director only with one verdict:

- READY FOR ONE REAL PHASE-5 EXECUTION;
- READY AFTER NARROW FIXES;
- BLOCKED.

The deputy programme director alone authorizes the single production real run.

## 14. Non-scope

Do not:

- execute the real production run;
- create accepted standard errors or paper claims;
- run synthetic recovery;
- run welfare/decomposition;
- change the notebook;
- run EUROMOD;
- add couples or pooled years;
- modify the public package;
- commit household-level score arrays to Git.

## 15. Halt conditions

Stop and escalate on:

- source/bundle/revision mismatch;
- score identity failure;
- parameter-order ambiguity;
- need to change likelihood/model/specification;
- package modification requirement;
- T-1 through T-23 implementation ambiguity;
- code review REJECT;
- disclosure/custody contract infeasibility;
- any attempt to promote `complete/`;
- unrelated dirty worktree.
