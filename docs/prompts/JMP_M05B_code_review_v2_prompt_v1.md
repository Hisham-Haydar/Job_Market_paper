# Prompt — Independent JMP-M05B Code Review v2

**Tool:** Codex  
**Model:** GPT-5.6 Codex  
**Reasoning:** Maximum  
**Mode:** Read-only  
**Workspace:** MNL with read-only access to nested dclaborsupply and the
redacted restricted-store provisioning evidence

## ROLE

Independently review the exact remediated JMP-M05B implementation.

Review v1 remains immutable history. This review must verify all twelve required
fixes and determine whether the exact state may be committed and used for one
full dry run.

Do not edit files.
Do not compute the full 1,555-household score matrix.
Do not run the Phase-5 dry run.
Do not commit.
Do not expose the full restricted-store locator or ACL-sensitive information.

## READ IN FULL

- Phase-5 design v4 and binding methods reviews;
- JMP-M05B charter;
- deputy E2 decision v1;
- implementation report v1;
- code review v1;
- remediation report v1;
- complete current Git diff;
- Phase-5 runner, helpers, config, tests, `.gitignore`;
- authenticated parameter-map CSV;
- source inventory;
- restricted-store provisioning record through a redacted/local read-only view;
- accepted Phase-3 and Phase-4 manifests and bundle verifiers.

## REVIEW GATES

### A. Statistical and package preservation

1. no statistical-design change;
2. no likelihood/loader duplication;
3. no dclaborsupply modification;
4. accepted theta, bounds, pins, maps, covariance formulas, tests, and constants
   unchanged except review-required authentication/lifecycle corrections.

### B. Fix 1 — authorization

5. no ungated public full-score route;
6. every full-score process requires exact review-v2/revision/cleanliness,
   bundle, map, and custody gates;
7. no caller-selected arbitrary output path;
8. fail-closed behavior proven.

### C. Fix 2 — Git ancestry

9. actual worktrees are dynamically discovered;
10. MNL, nested, Job_Market_paper, and additional worktrees are rejected;
11. symlink/junction/relative/case/path escapes are rejected;
12. target is bound to provisioned restricted root.

### D. Fix 3 — orchestration

13. T-12/T-13/T-20/T-23 attach before final summary;
14. all-pass maps to one preserved `PHASE_5_DRY_RUN_COMPLETE` attempt;
15. failures map truthfully to STOPPED;
16. `complete/` is impossible.

### E. Fix 4 — parameter map

17. CSV schema/hash/content are authenticated;
18. it is used at every 47→37→35 projection;
19. name/order/status/value tampering fails.

### F. Fix 5 — gradient

20. accepted full-gradient source is authenticated;
21. pin falsification uses actual pin coordinates;
22. no zeros assigned by construction.

### G. Fix 6 — post-evaluation checks

23. Phase-3 and Phase-4 bundles are reloaded and rehashed after evaluation;
24. theta, map, gradient, config, and consumed inputs are reloaded/rechecked;
25. mutation tests fail before publication.

### H. Fix 7 — T-12 closure

26. hash reproduction leaves no duplicate registered or unregistered score file;
27. exact restricted-member set enforced on success and failure.

### I. Fix 8/9 — custody transaction

28. store is persistent, access-restricted, outside all Git roots;
29. staging is unique and non-overwriting;
30. directory publication is atomic;
31. overwrite is refused;
32. failed partial writes preserve truthful STOPPED evidence;
33. custody fields exist on every attempt before evaluation;
34. commit-eligible records redact the locator.

### J. Fix 10 — optimizer/module guard

35. guard is installed proactively;
36. lazy imports and child processes are covered;
37. T-20 cannot pass without a verified active guard.

### K. Fix 11 — runtime metadata

38. actual chunk sizes recorded;
39. post-contract and post-evaluation x64/runtime state recorded;
40. manifest is authoritative.

### L. Fix 12 — tests/lifecycle

41. deterministic integration coverage exists for fixes 1–11;
42. tautological tests removed;
43. lifecycle-invalid tests replaced;
44. suite is valid uncommitted, committed, and after dry run;
45. no-full-score tests pass repeatedly;
46. no household score bytes and no dry-run attempt were created by review.

### M. Transaction and commit readiness

47. review v1 REJECT cannot authorize execution;
48. review v2 binding is exact and fail-closed;
49. working set contains only intended files;
50. `git diff --check` passes;
51. accepted bundles and nested state unchanged.

## CREATE

`docs/France_case/P2a/FR_P2a_region_live_phase5_code_review_v2.md`

Use exactly these headings:

1. Phase-5 review-v2 verdict
2. Scope and exact state
3. Statistical-design preservation
4. Package-boundary preservation
5. Fix 1 — authorization
6. Fix 2 — Git ancestry
7. Fix 3 — orchestration
8. Fix 4 — parameter-map binding
9. Fix 5 — full-gradient authentication
10. Fix 6 — post-evaluation reauthentication
11. Fix 7 — T-12 member closure
12. Fix 8/9 — custody and transaction
13. Fix 10 — optimizer guard
14. Fix 11 — runtime metadata
15. Fix 12 — tests and lifecycle
16. Accepted-artifact integrity
17. Residual defects
18. Required fixes
19. Whether exact state may be committed
20. Whether one full dry run may follow after commit
21. Immediate next action

The first section must contain exactly one:

**FINAL VERDICT: APPROVE**

or:

**FINAL VERDICT: APPROVE AFTER FIXES**

or:

**FINAL VERDICT: REJECT**

Do not modify or commit anything.
Do not run the full Phase-5 dry run.
