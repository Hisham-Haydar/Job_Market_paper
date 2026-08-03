# Prompt — Close JMP-M05C and Promote the Accepted Phase-5 Evidence

**Tool:** Claude Code  
**Model:** Sonnet  
**Thinking:** On  
**Effort:** Medium-high  
**Workspaces:** MNL and Job_Market_paper  
**Numerical execution:** prohibited  
**Phase-5 recomputation:** prohibited

## ROLE

Close JMP-M05C by accepting and committing the already-audited full-population
aggregate-only attempt.

Do not run Phase 5 again.
Do not create `complete/`.
Do not modify numerical code, configuration, accepted artifacts, theta,
Hessian, likelihood, parameter maps, package source, or notebooks.

Read first:

- `JMP_M05C_deputy_phase5_acceptance_v1.md`;
- `JMP_M05C_goal_manager_dryrun_acceptance_v1.md`;
- `JMP_M05C_mission_ledger_v4.md`;
- accepted `phase5_manifest.json`;
- Increment-A/B/C final reviews;
- certification proportionality rule.

## STAGE 1 — VERIFY THE ACCEPTED ATTEMPT

Expected execution anchor:

`bd7e3af2a0056b43f3fb8b50b858f358ed7a8825`

Expected attempt:

`20260803T133122Z_14772_817e8deb503d408fa73b8b53d598c0db_dryrun`

Expected bundle SHA-256:

`d08947ce015f2b2a922c6d5591ebe600c53016922b3a1158d90f125cd2195232`

Verify:

1. exact 19-member allowlist;
2. every member SHA-256 against the manifest;
3. recomputed bundle SHA-256;
4. `inference_grade = full-sample`;
5. `n_households = 1555`;
6. no row-level score artifact;
7. no household identifier paired with scores;
8. no temporary/staging member;
9. no `complete/`;
10. accepted Phase-3/Phase-4 bundles;
11. nested HEAD/gitlink;
12. execution-anchor ancestry.

Stop on any mismatch.

## STAGE 2 — CREATE THE CANONICAL ACCEPTANCE POINTER

Create in MNL:

`docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md`

Use headings:

1. Acceptance verdict
2. Canonical execution anchor
3. Canonical attempt path
4. Accepted bundle and member hashes
5. Statistical gates
6. Reproduction
7. Aggregate-only disclosure
8. W-4 caveat
9. Active-bound interpretation
10. Regional/access interpretation
11. Evidence commit
12. Downstream use

The verdict must be:

`PHASE-5 FULL-SAMPLE INFERENCE ACCEPTED`

The file must state that the accepted attempt is canonical without creating a
`complete/` copy.

## STAGE 3 — MNL EVIDENCE COMMIT

Stage only:

- the exact 19 accepted attempt members;
- `FR_P2a_region_live_phase5_result_acceptance_v1.md`;
- `JMP_M05C_goal_manager_dryrun_acceptance_v1.md`, if maintained in MNL;
- the repository copy of `JMP_M05C_deputy_phase5_acceptance_v1.md`, if assigned
  to MNL;
- directly related final audit evidence not yet committed.

Do not stage unrelated files.

Commit once:

`results(p2a): accept full-sample Phase-5 inference`

Report:

- full evidence commit SHA;
- exact committed file list;
- execution anchor retained as `bd7e3af2...`;
- clean/dirty status after the evidence commit.

## STAGE 4 — D11 TEST-ONLY FIX

Change only the stale output-root-absence assertions in `test_N6` and `test_P5`.

Replace them with before/after canonical-root listing equality or the already
binding refusal/no-write property.

Do not modify production code.

Run:

- the two corrected tests;
- Increment-C suite;
- safe full repository suite with test 29 deselected;
- accepted bundle checks;
- `git diff --check`.

Expected full-suite result:

`276 passed, 1 deselected`

or an exact documented equivalent if test collection changed only because of
committed documentation.

Commit separately:

`test(p2a): make Phase-5 lifecycle checks post-run safe`

Report the full D11 commit SHA.

## STAGE 5 — JOB_MARKET_PAPER CHECKPOINT

Inventory the accumulated M05B/M05C governance set.

Stage only governance, mission, prompt, ledger, decision, and acceptance
documents associated with M05B/M05C, including:

- certification proportionality rule;
- pause/redesign decisions;
- M05C charter and addendum;
- E2 decisions;
- mission ledger v4;
- Goal 1 dry-run acceptance;
- deputy Phase-5 acceptance;
- W-4 routing record if created;
- closeout prompt.

Do not stage unrelated manuscript, theory-paper, data, or package files.

Commit once:

`docs(jmp): close M05C and accept Phase-5 inference`

## FINAL RETURN

Return to the Goal 1 Manager:

- evidence commit SHA;
- D11 commit SHA;
- Job_Market_paper checkpoint SHA;
- canonical attempt path and bundle SHA;
- exact suite result after D11;
- MNL, nested, and Job_Market_paper statuses;
- confirmation that no second numerical run occurred;
- confirmation that no `complete/` exists;
- confirmation that JMP-M05C is closed.
