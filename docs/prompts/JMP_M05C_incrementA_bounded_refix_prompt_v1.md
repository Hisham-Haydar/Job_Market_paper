# Prompt — JMP-M05C Increment-A Bounded Refix

**Tool:** Claude Code  
**Model:** Opus  
**Thinking:** On  
**Effort:** High  
**Workspace:** MNL with read-only nested dclaborsupply  
**Starting MNL HEAD:** `b5169293b647dda3e07070c678f8d46d33b1bf89`  
**Commit:** Prohibited  
**Increment B:** Prohibited  
**Full-population run:** Prohibited

## ROLE

Implement exactly the five fixes authorized by
`JMP_M05C_incrementA_E2_deputy_decision_v1.md`.

Do not change the streaming statistical design.
Do not modify dclaborsupply.
Do not add covariance, bread, standard-error, regional-test, runner,
transaction, or reproduction functionality.
Do not persist row-level scores.
Do not commit.

## READ IN FULL

- `JMP_M05C_incrementA_E2_deputy_decision_v1.md`
- `JMP_M05C_streaming_inference_design_addendum_v1.md`
- `JMP_M05C_minimal_streaming_implementation_mission_charter_v1.md`
- `FR_P2a_streaming_incrementA_report_v1.md`
- `FR_P2a_streaming_incrementA_review_v1.md`
- `JMP_M05C_E2_incrementA_review_reject_v1.md`
- current Increment-A source and tests
- accepted source inventory and parameter map

## PRE-REFIX STATE DISPOSITION

Inside this task:

1. record MNL HEAD, nested HEAD/gitlink, and both statuses;
2. inventory the complete modified/untracked working set;
3. locate the four unexpected test-29 attempt files identified by Review A;
4. compute path, size, and SHA-256 for each;
5. verify none contains household score rows, accepted bundle members, or
   required evidence;
6. delete exactly those four files;
7. remove empty attempt directories created solely by those files;
8. verify the remaining working set equals the authorized Increment-A files,
   report, review, and this remediation report.

Stop if any path or content differs from the reviewed description.

## FIX 1 — FAILURE-PATH SCORE RELEASE

Refactor the public reducer failure boundary so the final caller-visible
exception object graph cannot retain the transient score matrix.

Requirements:

- internal exceptions may be caught and converted to a sanitized public error;
- clear or sever internal traceback, cause, and context before the public error
  is raised;
- raise the public error from `None`;
- ensure the final public traceback contains no frame whose locals hold the
  score matrix or row-level bytes;
- preserve a useful non-sensitive error code/message;
- do not log score values.

Add a recursive exception-graph test that traverses:

- final exception;
- traceback frames and locals;
- context;
- cause;
- exception args/payloads;
- containers reachable from those objects within a bounded safe traversal.

Fail if it discovers:

- any 2-D array with 37 columns;
- any array equal to or sharing memory with the supplied score batch;
- score bytes or memoryview;
- a retained object exposing the score batch.

Retain successful-path release and no-file/no-stdout/no-stderr tests.

## FIX 2 — STRICT ID VALIDATION

Before digest update:

- require the verified canonical production ID representation;
- reject float dtype even when values are mathematically integral;
- reject object, string, boolean, unsigned-overflow, non-native/coercion-based,
  non-finite, fractional, and out-of-int64 values;
- perform no lossy cast before validation;
- only after validation encode each ID as signed int64 little-endian.

Add tests proving:

- `.5` IDs refuse;
- integral floats refuse;
- NaN/Inf refuse;
- out-of-range values refuse;
- strings/object arrays refuse;
- canonical production int64 IDs pass;
- forged floats cannot reproduce the integer digest.

## FIX 3 — T-16 FIRST 64

Change the production T-16 test to the first 64 canonical households.

Report:

- exact forward and reverse modes;
- batch tuple;
- frozen bar;
- observed deviation;
- pass result.

Keep the 24-household check only if renamed as smoke coverage.

## FIX 4 — VERBATIM PROOFS

Rewrite the Increment-A report PROOFS section.

Every command must:

- start from the repository root unless another directory is stated;
- invoke the exact virtual-environment interpreter, preferably:
  `.\.venv\Scripts\python.exe`;
- be read-only;
- create no reviewer-owned source file;
- require no edit;
- use file-free `-c` or committed tests for red-bar demonstrations;
- state exact expected output/counts;
- explicitly deselect test 29 from every full-suite command.

Regenerate and freeze the exact counts after all new tests are present.

## FIX 5 — STATE AND TEST-29 RULE

Ensure every full-suite command uses an explicit deselection equivalent to:

`-k "not test_29_subprocess_dry_run_never_optimizes"`

unless test 29 is the sole isolated target with a temporary output root and
automatic cleanup.

Add a guard test or documented wrapper command that makes accidental
full-suite execution of test 29 fail before writing into accepted attempt
locations.

## VALIDATION

1. compile/parse all changed Python and documentation;
2. run the complete Increment-A test set twice;
3. run the exception-object-graph tests 20 consecutive times;
4. run strict-ID validation tests 20 consecutive times;
5. run first-64 T-11/T-16 production-path proofs;
6. run the safe broader suite with explicit test-29 deselection twice;
7. execute every printed PROOFS command verbatim in the intended environment;
8. run `git diff --check`;
9. rehash accepted Phase-3 and Phase-4 bundles;
10. verify nested clean and unchanged;
11. verify no row-level score artifact exists anywhere under the repositories;
12. verify no unexpected attempt files remain;
13. verify no Increment-B code exists.

## CREATE

Create:

`docs/France_case/P2a/FR_P2a_streaming_incrementA_refix_report_v1.md`

Use exactly these headings:

1. Refix verdict
2. Scope
3. Starting state
4. State disposition
5. Files inspected
6. Files modified
7. Fix 1 — failure-path score release
8. Fix 2 — strict ID validation
9. Fix 3 — first-64 T-16
10. Fix 4 — reviewer-runnable proofs
11. Fix 5 — test-29 state rule
12. Statistical-design preservation
13. Package-boundary preservation
14. Test results
15. Verbatim proof results
16. Artifact and repository integrity
17. Residual warnings
18. Whether Review A v2 may begin
19. Immediate next action

Final verdict must be one:

- READY FOR REVIEW A V2
- BLOCKED

Do not commit.
Do not begin Increment B.
