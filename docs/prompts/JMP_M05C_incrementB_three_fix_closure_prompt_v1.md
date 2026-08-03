# Prompt — JMP-M05C Increment-B Three-Fix Mechanical Closure

**Tool:** Claude Code  
**Model:** Opus  
**Thinking:** On  
**Effort:** Medium-high  
**Workspace:** MNL with read-only nested dclaborsupply  
**Starting MNL HEAD:** `92e299de6313bad0b0421c0db3dd268fdbcfdb59`  
**Commit:** Prohibited until focused closure review PASS  
**Increment C:** Prohibited until focused closure review PASS

## ROLE

Close exactly the three residual Increment-B defects frozen by
`JMP_M05C_incrementB_proportionality_decision_v1.md`.

This is a mechanical closure, not a broad remediation cycle.

Do not alter:

- the numerical or econometric implementation;
- covariance formulas;
- gradient source;
- parameter maps;
- active-bound interpretation;
- schemas or constants;
- accepted likelihood, theta, Hessian, or bundles;
- Increment-A source;
- dclaborsupply.

Do not add runner, transaction, reproduction, or Increment-C functionality.

## READ

- `JMP_certification_proportionality_rule_v1.md`
- `JMP_M05C_incrementB_proportionality_decision_v1.md`
- Increment-B report v1;
- Review B v1;
- refix report v1;
- Review B v2;
- complete current Increment-B source and tests.

## STEP 1 — FREEZE THE THREE TESTS FIRST

Before changing implementation, add exactly three focused tests reproducing:

1. caller-supplied/forged T-22 expected active-name set;
2. serializer refusal after an invalid empty grade leaves the destination
   nonexistent or byte-identical;
3. score-summary extension attempts to:
   - persist a `5×37` score block;
   - overwrite `inference_grade`;
   - overwrite any protected field.

Run the three tests and record that they fail against the pre-fix state for the
expected reason.

Do not modify the probes after implementation begins except to correct a
test-only syntax error. Any correction must be reported with a before/after
hash.

## STEP 2 — FIX B-1

Remove caller control of the expected T-22 name set.

Derive the expected names internally from the authenticated parameter map, or
use the frozen constant only after proving exact equality with that map.

The public gate may receive observed gradient values, but not a replacement
expected-name authority.

## STEP 3 — FIX B-2

Validate `inference_grade` and every other refusal condition before any
filesystem write action.

Require destination nonexistence or exact byte preservation after refusal.

No open/truncate/temp-file/rename operation may occur before validation passes.

## STEP 4 — FIX B-3

Preferred fix: remove `extra=` from `write_score_aggregate_summary`.

If a specific accepted scalar extension is required, replace it with explicit
named keyword-only scalar fields and an allowlist. Do not accept a generic
mapping.

Protected payload fields must be constructed exclusively by the serializer and
must not be caller-overridable.

Reject arrays, frames, bytes, memoryviews, row-level sequences, and nested
containers carrying them before any write.

## VALIDATION

Run:

1. the three frozen probes;
2. complete Increment-B tests twice;
3. committed Increment-A suite;
4. safe broader suite with test 29 deselected;
5. all twelve existing reviewer-runnable proofs;
6. `git diff --check`;
7. accepted Phase-3 and Phase-4 bundle rehash;
8. nested status check;
9. search proving no row-level score artifact exists;
10. check that no Increment-C code was added.

## CREATE

`docs/France_case/P2a/FR_P2a_streaming_incrementB_closure_report_v1.md`

Use exactly these headings:

1. Closure verdict
2. Scope
3. Starting state
4. Frozen probe provenance
5. Probe B-1 — T-22 authority
6. Probe B-2 — pre-write refusal
7. Probe B-3 — no arbitrary extension persistence
8. Files modified
9. Numerical-core preservation
10. Statistical-design preservation
11. Package-boundary preservation
12. Test results
13. Proof results
14. Artifact and repository integrity
15. Nonblocking technical debt
16. Whether focused review may begin
17. Immediate next action

Final verdict:

- READY FOR FOCUSED INCREMENT-B CLOSURE REVIEW
- BLOCKED

Do not commit.
Do not begin Increment C.
