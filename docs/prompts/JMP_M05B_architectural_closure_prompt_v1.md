# Prompt — JMP-M05B Architectural Closure Cycle

**Tool:** Claude Code  
**Model:** Opus  
**Thinking:** On  
**Effort:** High  
**Workspace:** MNL with read-only access to nested dclaborsupply, Job_Market_paper
governance, and the provisioned restricted store  
**Starting MNL base:** `983a2ecf1d16592b9f90085f6a6b690b8a964110`  
**Commit:** prohibited until independent review v4 `APPROVE`  
**Full dry run:** prohibited

## ROLE

Perform the one deputy-authorized architectural closure of JMP-M05B.

This is not a third ordinary remediation cycle. Replace surface-by-surface
authorization with one canonical gated process entry capable of full scoring.

Implement only:

1. the single-entry architecture and closed-form surface inventory;
2. the six narrow residual groups authorized by
   `JMP_M05B_E2_deputy_decision_v2.md`.

Do not change the accepted statistical design, likelihood, loader, theta,
parameters, bounds, pins, covariance formulas, correction scalar, hypotheses,
T/W constants, package source, or output interpretation.

Do not compute the full 1,555-household score matrix.
Do not run the Phase-5 dry run.
Do not commit.

## READ IN FULL

- `JMP_M05B_E2_deputy_decision_v2.md`
- `JMP_M05B_phase5_implementation_mission_charter_v1.md`
- `JMP_M05B_mission_ledger_v1.md`
- Phase-5 design v4 and binding methods reviews;
- implementation report v1;
- code reviews v1, v2, and v3;
- remediation reports v1 and v2;
- source-verification report, parameter-map CSV, and source inventory;
- restricted-store provisioning record through a redacted read-only view;
- complete current Git diff.

## A. SINGLE GATED PROCESS ENTRY

The only application-level process entry capable of full scoring must be the
canonical entry in:

`scripts/p2a/run_p2a_phase5_inference.py`

Parent dry-run and T-12 child are two internally authorized roles of the same
entry, not separate public scoring surfaces.

Required architecture:

1. canonical entry parses CLI and loads the canonical Phase-5 YAML itself;
2. canonical YAML bytes/digest are bound before any score-capable object exists;
3. review, revisions, cleanliness, gitlink, bundles, parameter map, gradient,
   config, and restricted-store identity are authenticated;
4. only then is an opaque process-local authorization context created;
5. full scoring is performed only inside a nested closure or private worker that
   requires that context;
6. ordinary contract helpers may construct metadata/contracts but cannot
   produce the full score matrix;
7. no caller can pass `cfg5`, booleans, records, contexts, roots, or output paths
   into a score-capable function;
8. remove or structurally disable the direct
   `_phase5_contract` + `_phase5_evaluate` full-score route;
9. tests and fixtures must use bounded synthetic score fixtures, not bypass
   authorization through internal calls.

Do not rely solely on an underscore, a module-private sentinel, or a caller-
supplied object as the boundary.

## B. T-12 CHILD CAPABILITY

The T-12 child must invoke the same canonical process entry.

Implement a single-use parent-issued child capability that is:

- generated only inside an authorized parent attempt;
- bound to attempt ID, parent PID, exact MNL/nested revisions, review digest,
  Phase-3/4 bundle digests, config digest, parameter-map digest, store identity,
  and child role;
- stored only inside the authenticated restricted staging transaction;
- consumed atomically once;
- invalid after consumption or attempt termination;
- not accepted from an arbitrary caller-selected path;
- deleted or incorporated into truthful STOPPED evidence according to the
  closed member contract.

The child must rerun all authorization gates and complete post-evaluation
reauthentication before returning its score digest.

## C. CANONICAL CONFIGURATION BINDING

Every value used by scoring or custody must derive from the canonical YAML
loaded by the process entry.

Reject:

- in-memory substituted config;
- copied provisioning record paired with another root;
- caller-selected restricted root;
- config digest mismatch;
- store-identity mismatch.

Manifest and T-13 must describe and reauthenticate the same configuration object
actually consumed.

## D. CLOSED-FORM SURFACE INVENTORY

Create:

`docs/France_case/P2a/phase5_full_score_surface_inventory_v1.json`

Required schema fields:

- inventory version;
- MNL base revision;
- files scanned;
- application surface count;
- canonical surface:
  - source file;
  - symbol/process entry;
  - parent role;
  - T-12 child role;
  - authorization prerequisites;
  - canonical config source/digest rule;
  - restricted-store binding;
  - post-evaluation reauthentication;
- removed/disabled former surfaces;
- generic low-level package primitives explicitly excluded from application
  surface count, with rationale;
- tests proving every noncanonical route refuses or is incapable;
- inventory SHA-256.

Required result:

`application_full_score_surface_count = 1`

Add a deterministic static-and-behavioral test that fails if another
application-level full-score call site or public score-capable route is added.

## E. STOPPED RENAME SAFETY

Immediately before STOPPED rename:

- re-resolve and revalidate the staging source and every ancestor;
- reject reparse points/junctions/symlinks;
- verify containment and store identity.

Immediately after rename:

- resolve and validate the STOPPED endpoint and every ancestor;
- verify same-volume authenticated-root containment;
- fail closed and preserve truthful evidence if the endpoint is not valid.

## F. POST-EVALUATION REAUTHENTICATION

After every full score evaluation, parent and T-12 child:

- rerun closed-set Phase-3 and Phase-4 bundle verification;
- reload and rehash every consumed input;
- rederive theta, gradient, map, bounds, pins, and canonical config from source;
- verify restricted-store identity and provisioning record;
- compare to the exact objects used during evaluation;
- refuse publication on any mutation.

No cached semantic object may substitute for a required reload.

## G. TRUTHFUL COMPLETE INVENTORY

Inventory every retained filesystem object:

- regular files;
- directories;
- junctions;
- symlinks;
- unreadable members;
- partial/unbookkept members.

Require agreement among:

- top-level custody state;
- observed inventory;
- declared membership;
- member hashes;
- STOPPED bundle membership and hash.

A byte written before bookkeeping must still be discovered and truthfully
reported.

## H. BEHAVIORAL TESTS

Add deterministic tests for:

1. direct contract/evaluate route cannot full-score;
2. in-memory config substitution refuses;
3. copied provisioning record with different root refuses;
4. second-use/replayed child capability refuses;
5. T-12-window mutation triggers STOPPED before publication;
6. STOPPED junction replacement refuses and records truthfully;
7. partial-write fault records bytes and hashes truthfully;
8. no-publication on every failure;
9. surface inventory count is exactly one;
10. every noncanonical application route refuses;
11. no household score bytes are created by the test suite.

Use bounded synthetic fixtures only.

## I. LIFECYCLE-AWARE WORKING-SET TESTS

Replace hard-coded current-inventory assumptions with exact state profiles:

1. reviewed-uncommitted state;
2. clean post-commit state;
3. post-dry-run state with exactly one preserved attempt.

The complete no-full-score suite must pass under simulated fixtures for all
three profiles.

Do not permit subset assertions where exact equality is required.

## J. DOCUMENTATION CLEANUP

Correct:

- stale review-v2 CLI help;
- obsolete review heading/path references;
- every residual comparator description.

Use the exact approved mixed comparator description:

`a == b or abs(a-b) <= 1e-15 * max(abs(a), abs(b), 1.0)`

Do not call it a purely relative bar.

## K. VALIDATION

1. parse/compile Python and YAML;
2. run the complete no-full-score suite twice;
3. run critical single-entry, replay-refusal, config-binding, mutation,
   STOPPED-inventory, and lifecycle tests 10 consecutive times;
4. verify `application_full_score_surface_count = 1`;
5. run `git diff --check`;
6. rehash accepted Phase-3 and Phase-4 bundles;
7. verify nested repository clean and unchanged;
8. verify restricted store contains no household-level score artifact;
9. verify no Phase-5 output root or `complete/`;
10. verify reviews v1/v2/v3 remain immutable and non-authorizing.

## CREATE

`docs/France_case/P2a/FR_P2a_region_live_phase5_architectural_closure_report_v1.md`

Use exactly these headings:

1. Closure verdict
2. Scope
3. Starting state
4. Threat-model compliance
5. Single gated process entry
6. Parent and T-12 child roles
7. Authorization-context construction
8. Canonical configuration binding
9. Full-score surface inventory
10. Removed or disabled former surfaces
11. STOPPED rename safety
12. Post-evaluation reauthentication
13. Truthful retained-member inventory
14. Behavioral integration tests
15. Lifecycle-aware tests
16. Documentation corrections
17. Statistical-design preservation
18. Package-boundary preservation
19. Test results
20. Artifact and custody integrity
21. Residual warnings
22. Whether review v4 may begin
23. Immediate next action

FINAL VERDICT:

- READY FOR CLOSED-FORM REVIEW V4
- BLOCKED

Do not commit.
Do not run the full dry run.
