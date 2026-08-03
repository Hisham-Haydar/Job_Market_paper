# JMP-M05C Increment-A E2 Deputy Decision v1

**Mission:** JMP-M05C — Minimal Streaming Inference Implementation  
**Escalation:** Increment-A independent review v1 returned `REJECT`  
**Decision-maker:** ChatGPT JMP Deputy Programme Director  
**Date:** 2026-08-02  
**Verdict:** ONE BOUNDED INCREMENT-A REFIX AUTHORIZED

## 1. Strategic ruling

The Increment-A review `REJECT` is accepted as valid.

The review also establishes that the redesign is working as intended:

- the accepted loader and likelihood are genuinely exercised;
- the streaming reducer's successful-path aggregates are numerically correct;
- the first-64 T-11/T-16 comparisons pass with wide margins;
- the 35×35 and 37×37 meat objects are internally consistent;
- the accepted parameter mapping and R-32 rulings are preserved;
- no package, covariance, runner, transaction, or welfare scope was introduced;
- no household-level score artifact was persisted.

The five defects are closed implementation, testing, proof, and state-management
defects. They do not reopen the statistical design, package boundary, or
streaming architecture.

Authorize one bounded Increment-A refix implementing exactly the five fixes in
`FR_P2a_streaming_incrementA_review_v1.md`, followed by a fresh independent
Review A v2.

Increment B remains blocked until Review A v2 returns `APPROVE`.

## 2. Authorized five-fix scope

### A-1 — Failure-path transient-score release

Restructure the public failure boundary so the exception returned to a caller
does not retain a transient `(batch, 37)` score array or its bytes through:

- `__traceback__`;
- `__context__`;
- `__cause__`;
- exception payloads;
- frame locals reachable from the final raised exception.

The implementation may sanitize and replace internal exceptions, but must
preserve a useful error class and non-sensitive diagnostic message.

Tests must recursively inspect the complete final exception object graph and
fail if they find:

- a two-dimensional score-shaped array;
- a 37-column row-level array;
- score-byte payloads;
- a retained batch object containing score rows.

Existing file, stdout/stderr, and message checks remain required.

### A-2 — Canonical household-ID validation

Reject household-ID inputs before digest update when they are:

- floating-point, including numerically integral floats;
- non-integral;
- non-finite;
- outside signed int64 range;
- object/string/coercion-based representations;
- non-canonical relative to the verified production ID contract.

No lossy cast may occur before validation.

The accepted digest encoding remains signed int64 little-endian. After this fix,
R-32a is frozen subject to Increment-C binding of the complete reproduction
tuple required by R-32b.

### A-3 — Frozen T-16 slice

The production T-16 test and proof must use the first 64 canonical households.

Any 24-household comparison may remain only as a separately labelled smoke
test. It must not be described as T-16 evidence.

### A-4 — Verbatim reviewer-runnable proofs

Repair the PROOFS packet so every command:

- invokes the exact repository virtual-environment interpreter;
- runs read-only;
- requires no file creation by the reviewer;
- requires no source edit;
- records current exact expected counts;
- executes from a stated working directory;
- can be pasted verbatim by a fresh reviewer.

Replace stale counts with the verified current counts or, where a count may
legitimately vary because of the added five-fix tests, regenerate and freeze the
new exact counts in the remediation report.

### A-5 — Exact-state restoration

Inside the remediation task itself:

1. inventory and hash the four unexpected test-29 attempt files;
2. record their paths, sizes, and hashes in the remediation report;
3. confirm they contain no accepted artifact and no household score data;
4. delete them;
5. verify the exact expected working set before tests and before Review A v2.

No human pre-step is permitted.

Every mission-wide full-suite command must explicitly deselect:

`test_29_subprocess_dry_run_never_optimizes`

unless the task is a dedicated isolated test-29 task with its own temporary
output root and cleanup contract.

## 3. Process amendment for Increments B and C

Amend JMP-M05C §6 as follows.

For each remaining increment, the Goal 1 Manager may authorize **one bounded
refix after a review verdict of `REJECT`** without returning to the deputy
programme director only when all conditions below hold:

1. the reviewer explicitly confirms the statistical design is unchanged;
2. the package boundary passes;
3. the accepted likelihood and data route pass;
4. no new architecture, estimand, disclosure rule, or repository-role decision
   is required;
5. the reviewer supplies a finite, closed implementation-level fix list;
6. the Goal 1 Manager records the conversion and the fix list in the mission
   ledger;
7. the refix is followed by a fresh independent review of the same increment;
8. no increment receives more than one such refix.

Immediate E2 escalation remains mandatory when:

- any finding affects design, package, likelihood, data, architecture,
  disclosure, or accepted artifacts;
- the fix list is open-ended;
- the fresh review still returns `REJECT`;
- the reviewer identifies false-green production-path substitution;
- another remediation would be needed.

This amendment applies prospectively to Increments B and C and retroactively
authorizes the present Increment-A refix.

## 4. State-disposition rule

Adopt mission-wide:

> Every deletion, move, reconciliation, cleanup, or expected-state restoration
> must be executed and verified inside the gated task prompt. It may never be
> delegated to an informal human pre-step.

Each implementation/review prompt must state:

- exact permitted working-set members;
- exact cleanup actions;
- pre- and post-action inventories;
- which tests are deselected and why;
- the required final status.

## 5. Review A v2 ruling

Use:

- fresh Codex session;
- strongest available Codex review model;
- maximum reasoning;
- read-only mode.

Review A v2 is limited to:

- the original Increment-A contract;
- the five fixes above;
- exact-state integrity;
- no design/package/scope expansion.

The verdict is binary:

- `APPROVE`; or
- `REJECT`.

No `APPROVE AFTER FIXES` is available for Increment A.

A v2 `REJECT` is an E2 halt.

## 6. Commit and progression gate

After Review A v2 `APPROVE` only:

1. commit the exact reviewed Increment-A implementation, tests, report, and
   Review A v2;
2. require MNL and nested worktrees clean;
3. update the JMP-M05C ledger;
4. authorize Increment B.

No full-population score run is authorized in Increment A.

## 7. Current state

Binding starting state:

- MNL HEAD:
  `b5169293b647dda3e07070c678f8d46d33b1bf89`;
- nested dclaborsupply HEAD/gitlink:
  `27756a06ea189339aa82915ed2124628afed20eb`;
- `Job_Market_paper` HEAD:
  `7195fc50f6a73e20bdf62fc4baae48c18dedd345`;
- accepted Phase-3 and Phase-4 bundles rehash exactly;
- no household-level score bytes exist;
- restricted store is not part of JMP-M05C;
- Increment B is not authorized before Review A v2 approval.
