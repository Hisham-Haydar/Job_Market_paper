# Prompt — Phase-4 Test-42 Acceptance-Safe Housekeeping v1

**Tool:** Claude Code  
**Model:** Sonnet  
**Thinking:** On  
**Effort:** Medium  
**Workspace:** MNL  
**Commit:** Separate from Phase-5 implementation

## ROLE

Correct only the stale committed Phase-4 test:

`test_42_phase4_subprocess_dry_run_never_evaluates_hessian`

Do not modify Phase-4 production code, config, accepted artifacts, manifests,
or numerical logic.
Do not run a real Hessian.
Do not alter Phase-5 code in this task.

## REQUIRED CHANGE

Replace the stale assertion that the accepted Phase-4 `complete/` directory is
absent with an acceptance-safe contract:

1. hash and inventory the accepted Phase-4 `complete/` bundle before the test;
2. run the derivative-free subprocess dry run with all generated evidence
   isolated under a temporary test directory outside the accepted output root,
   or under a test-owned temporary root;
3. assert no Hessian/gradient/optimizer evaluation;
4. hash and inventory accepted `complete/` after the test;
5. require exact byte identity and identical member set;
6. remove the temporary test output automatically;
7. leave no worktree changes other than the test source.

## VALIDATE

- run the corrected test 10 consecutive times;
- run related Phase-4 no-Hessian tests;
- verify accepted Phase-4 bundle hash remains
  `5484886985aecd28e511719e42f45b85ad0e1755d1f951dbd13a79281d9665f3`;
- run `git diff --check`.

CREATE

`docs/France_case/P2a/FR_P2a_phase4_test42_housekeeping_report_v1.md`

Do not commit until the change has been independently reviewed with the
Phase-5 review-v2 packet.

After approval, commit separately with:

`test(p2a): make Phase-4 dry-run test acceptance-safe`
