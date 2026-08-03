# Prompt — JMP-M05C Increment-A Independent Review v2

**Tool:** Codex  
**Model:** GPT-5.6 Codex or strongest available Codex review model  
**Reasoning:** Maximum  W
**Mode:** Read-only  
**Session:** Fresh  
**Workspace:** Exact remediated MNL state with read-only nested dclaborsupply

## ROLE

Independently review the exact Increment-A remediated state.

The review is limited to the accepted Increment-A contract and the five fixes
authorized by `JMP_M05C_incrementA_E2_deputy_decision_v1.md`.

Do not modify files.
Do not run the full 1,555-household score calculation.
Do not begin Increment B.
Do not commit.

## READ

- streaming design addendum;
- JMP-M05C charter;
- Increment-A implementation report v1;
- Increment-A review v1;
- E2 escalation v1;
- deputy decision v1;
- Increment-A refix report v1;
- complete current Git diff;
- current Increment-A source and tests;
- accepted source inventory and parameter map.

## REVIEW GATES

### A. Preserved scientific contract

1. accepted production loader and likelihood are still genuinely exercised;
2. 37-score sum, 37×37 meat, 35×35 meat, digest, and metadata remain the only
   Increment-A outputs;
3. no package modification;
4. no covariance, runner, transaction, or later-increment code;
5. no row-level score persistence.

### B. Fix 1 — exception object graph

6. failure returns a useful sanitized error;
7. the final exception traceback/context/cause/payload graph contains no
   transient score matrix, row-level score array, score bytes, or batch object
   retaining score rows;
8. tests recursively inspect the final exception graph rather than only message
   or filesystem effects;
9. success and failure leave no row-level file or console output.

### C. Fix 2 — ID contract

10. no lossy cast occurs before validation;
11. float, fractional, NaN/Inf, object/string, boolean, and out-of-range IDs
    refuse;
12. canonical production IDs pass;
13. forged `.5` IDs cannot hash as truncated integers;
14. published signed-int64-little-endian contract matches actual bytes.

### D. Fix 3 — T-16

15. the production T-16 test uses the first 64 canonical households;
16. the frozen bar and observed deviation are reported accurately;
17. any smaller check is labelled only as smoke coverage.

### E. Fix 4 — proofs

18. every proof uses the exact virtual-environment interpreter;
19. every proof is read-only and pasteable verbatim;
20. no proof requires file creation or source editing by the reviewer;
21. expected test counts are current and exact;
22. reviewer execution reproduces them.

### F. Fix 5 — exact state

23. the four unexpected files were inventoried and correctly disposed of inside
    the task;
24. no unexpected attempt file remains;
25. every full-suite command explicitly deselects test 29 unless it is an
    isolated test-29 task;
26. working set equals the authorized exact set;
27. no accepted artifact changed.

### G. Numerical and repository integrity

28. first-64 T-11/T-16 production-route proofs pass;
29. meat and selector consistency remain correct;
30. R-32a/b/c treatment matches the decision;
31. accepted bundles rehash;
32. nested repository is clean;
33. `git diff --check` passes;
34. no household-level score bytes exist;
35. exact state is commit-ready.

## CREATE

Create:

`docs/France_case/P2a/FR_P2a_streaming_incrementA_review_v2.md`

Use exactly these headings:

1. Review-A-v2 verdict
2. Scope and exact state
3. Production-path integrity
4. Failure-path no-persistence
5. Household-ID and digest contract
6. First-64 numerical conformance
7. Reviewer-runnable proofs
8. Exact-state integrity
9. Statistical-design preservation
10. Package-boundary preservation
11. Accepted-artifact integrity
12. Residual defects
13. Whether Increment A may be committed
14. Whether Increment B may begin
15. Immediate next action

The first section must contain exactly one:

**FINAL VERDICT: APPROVE**

or:

**FINAL VERDICT: REJECT**

No `APPROVE AFTER FIXES` verdict is permitted.

Do not modify or commit anything.
Do not begin Increment B.
