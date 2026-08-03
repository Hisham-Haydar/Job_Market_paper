# Prompt — JMP-M05B Bounded Remediation Cycle 1

**Tool:** Claude Code  
**Model:** Opus  
**Thinking:** On  
**Effort:** High  
**Workspace:** `C:\Users\hisham\Repo` with MNL, nested dclaborsupply, and
read-only access to the provisioned restricted store  
**Starting state:** preserved uncommitted implementation and review v1 at MNL
HEAD `983a2ecf1d16592b9f90085f6a6b690b8a964110`

## ROLE

Implement exactly the twelve required fixes from
`FR_P2a_region_live_phase5_code_review_v1.md`.

This is remediation cycle 1 of 2.

Do not reopen the statistical design.
Do not change the accepted likelihood, model, specification, theta, parameter
values, bounds, pins, covariance formulas, finite-sample correction, regional
hypotheses, or T/W constants.
Do not modify dclaborsupply.
Do not run the full 1,555-household score calculation.
Do not run a Phase-5 dry run.
Do not commit.

## READ IN FULL

- `JMP_M05B_E2_deputy_decision_v1.md`
- `JMP_M05B_phase5_implementation_mission_charter_v1.md`
- `JMP_M05B_mission_ledger_v1.md`
- `FR_P2a_region_live_phase5_inference_design_v4.md`
- `FR_P2a_region_live_phase5_implementation_report_v1.md`
- `FR_P2a_region_live_phase5_code_review_v1.md`
- `FR_P2a_region_live_phase5_source_verification_v1.md`
- `phase5_parameter_map_v1.csv`
- `phase5_source_inventory_v1.json`
- PI disclosure determination
- restricted-store provisioning record, read-only

## FIX 1 — CLOSE FULL-SCORE AUTHORIZATION BYPASS

Remove the public ungated `reproduce` route, or make every process capable of
computing the full 1,555×37 score matrix require the same internal gates as the
approved dry-run route:

- exact approved review-v2 path/hash and verdict;
- expected MNL HEAD;
- expected nested HEAD and matching gitlink;
- clean MNL and nested worktrees;
- Phase-3 and Phase-4 bundle authentication;
- parameter-map authentication;
- restricted-store contract;
- no public caller-selected output path.

The contract route must fail closed before full scoring if any authorization
gate is absent.

## FIX 2 — ACTUAL GIT-ANCESTRY CONFINEMENT

Discover Git worktrees dynamically rather than using a two-root list.

At minimum discover and reject destinations under:

- MNL;
- nested dclaborsupply;
- sibling Job_Market_paper;
- any other Git worktree reachable under the configured repository parent;
- any path whose ancestor contains `.git` as a directory or worktree file.

Bind the target to the provisioned restricted-store root and reject symlink,
junction, relative-path, case-folding, and `..` escapes.

## FIX 3 — FINAL GATE ORDER

Attach T-12, T-13, T-20, and T-23 before the final gate-register decision.

Prove:

- all T gates pass → exactly one preserved
  `PHASE_5_DRY_RUN_COMPLETE` attempt;
- no `complete/` is ever created;
- any failed T gate → one STOPPED attempt with truthful diagnostics.

Do not run the real full dry run during remediation.

## FIX 4 — BIND PARAMETER-MAP CSV

Load and authenticate:

`docs/France_case/P2a/phase5_parameter_map_v1.csv`

Require:

- schema;
- file SHA;
- 47 rows;
- exact name/order/status/value equality with specification, Phase-4 contract,
  accepted theta, free map, interior map, pins, and bounds;
- exact use of this authenticated map at every 47→37→35 projection.

No projection may rely on an unauthenticated duplicate map.

## FIX 5 — AUTHENTICATE FULL GRADIENT

Load and hash-authenticate the accepted 47-element `gradient_final` source.

Use its pin coordinates for the pin-gradient falsification.

Do not assign zeros by construction. Require the verified pin components to
satisfy the accepted exact-zero contract.

## FIX 6 — POST-EVALUATION REAUTHENTICATION

After every callable/evaluation path and before any result publication:

- rerun the closed-set Phase-3 bundle verifier;
- rerun the closed-set Phase-4 bundle verifier;
- reload and rehash every consumed artifact;
- reload/recheck accepted theta, parameter map, gradient source, and config;
- compare actual post-evaluation hashes to accepted values.

Do not compare cached pre-run strings.

## FIX 7 — T-12 WITHOUT DUPLICATE ARTIFACT

Reproduce the authoritative `.npy` hash in a child process without retaining a
second score file in the final restricted member set.

Permitted approaches include:

- child writes to unique external staging and the parent hashes then securely
  removes it before publication; or
- child streams deterministic bytes/hash through a controlled pipe without
  final-file retention.

Require an exact closed restricted-member set. No unregistered `_t12` file may
remain after success or failure.

## FIX 8 — TRANSACTIONAL RESTRICTED PUBLICATION

Use only the provisioned restricted store.

Implement:

- unique non-overwriting external staging;
- closed member-set validation;
- hashes and custody manifest written before publication;
- atomic directory-level rename into `published`;
- overwrite refusal;
- STOPPED preservation of partial staging with locator/hash evidence;
- redacted locators in commit-eligible artifacts.

Never write restricted score bytes inside a Git worktree.

## FIX 9 — UNCONDITIONAL CUSTODY STATE

Initialize T-23 disclosure, custody, custodian, retention, publication,
restricted-member, and locator-redaction fields in every manifest before any
contract or evaluation step.

Every exception finalizer must preserve accurate custody state, including
whether no restricted bytes were created.

## FIX 10 — OPTIMIZER AND MODULE GUARD

Install the optimizer guard proactively in the fresh execution process.

T-20 must fail unless the guard is confirmed installed.

Check prohibited modules:

- before imports/callables;
- after lazy imports;
- before and after each score/evaluation callable;
- in the T-12 child;
- before publication.

Test lazy imports and restoration/failure behavior.

## FIX 11 — RUNTIME AND CHUNK METADATA

Record in the manifest:

- actual canonical chunk size;
- comparison chunk size;
- Python/NumPy/SciPy/JAX/jaxlib/platform/thread facts;
- JAX x64 state after the production contract enables it;
- post-evaluation environment snapshot.

Do not rely only on pre-contract metadata.

## FIX 12 — TESTS

Add deterministic no-full-score integration tests covering fixes 1–11:

- authorization/review/Git gates;
- dynamic Git-worktree rejection and path escapes;
- parameter-map tampering;
- full-gradient tampering;
- post-call bundle/input mutation;
- T-12 cleanup and exact member set;
- restricted partial writes and atomic publication;
- early STOPPED custody truthfulness;
- lazy optimizer import;
- all-pass gate ordering and dry-run-complete status;
- no `complete/`.

Remove or replace:

- the two tautological assertions identified by review v1;
- the three lifecycle-invalid assertions identified by review v1.

Tests must be valid in:

1. uncommitted reviewed state;
2. post-commit state;
3. post-dry-run state.

Use tiny fixtures or bounded production-route subsets only. Do not compute the
full score matrix.

## PRESERVE

- the review-v1 file unchanged;
- the accepted Phase-3 and Phase-4 artifacts;
- all design evidence;
- no household-level score bytes;
- no package changes;
- no dry-run attempts.

## VALIDATION

1. parse/compile Python and YAML;
2. run the corrected Phase-5 no-full-score suite twice;
3. run new critical authorization/custody tests at least ten consecutive times;
4. run applicable pre-existing suites;
5. run `git diff --check`;
6. verify both accepted bundles;
7. verify nested repository clean;
8. verify no restricted score bytes exist;
9. verify no `complete/`;
10. verify review v1 remains REJECT and cannot authorize execution.

CREATE

`docs/France_case/P2a/FR_P2a_region_live_phase5_remediation_report_v1.md`

Use exactly these headings:

1. Remediation verdict
2. Scope
3. Starting state
4. Files inspected
5. Files modified
6. Fix 1 — authorization bypass
7. Fix 2 — Git ancestry
8. Fix 3 — gate ordering
9. Fix 4 — parameter-map binding
10. Fix 5 — full-gradient authentication
11. Fix 6 — post-evaluation reauthentication
12. Fix 7 — T-12 member closure
13. Fix 8 — restricted transaction
14. Fix 9 — unconditional custody
15. Fix 10 — optimizer guard
16. Fix 11 — runtime metadata
17. Fix 12 — lifecycle-valid tests
18. Statistical-design preservation
19. Package-boundary preservation
20. Test results
21. Artifact-integrity results
22. Residual warnings
23. Whether review v2 may begin
24. Immediate next action

FINAL VERDICT

Use exactly one:

- READY FOR PHASE-5 REVIEW V2
- READY WITH WARNINGS
- BLOCKED

Do not commit.
Do not run the full Phase-5 dry run.
