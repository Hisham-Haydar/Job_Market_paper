# Prompt — Close JMP-M05 Design v4 and Commit Documentation

**Manager:** Goal 1 Manager — Empirical JMP  
**Primary tool for edits/commits:** Claude Code  
**Independent micro-review:** the same independent reviewer role, in a new review turn  
**Scope:** mechanical closure and documentation only

## ROLE

Execute the deputy-approved E0 closure of JMP-M05, obtain the independent
micro-recheck PASS, and create two documentation-only checkpoints.

Do not implement Phase 5.
Do not compute scores, covariance matrices, standard errors, or tests.
Do not run optimizers, gradients, Hessians, welfare, decomposition, EUROMOD, or
notebooks.
Do not change accepted numerical artifacts.
Do not rewrite history.

## AUTHORITATIVE INPUTS

- `JMP_M05_deputy_programme_acceptance_v1.md`
- `JMP_M05_goal_manager_acceptance_v1.md`
- `JMP_M05_mission_ledger_v3.md`
- `FR_P2a_region_live_phase5_inference_design_v3.md`
- `FR_P2a_region_live_phase5_inference_micro_recheck_v1.md`
- all Stage-A/B/C/D instruments and evidence files
- `JMP_M05_PI_disclosure_determination_v1.md`

## STAGE 1 — CREATE DESIGN v4

Use Claude Code.

Tool/model:

- Claude Code
- Sonnet
- thinking on
- medium effort
- MNL workspace

Create:

`docs/France_case/P2a/FR_P2a_region_live_phase5_inference_design_v4.md`

Start from v3. Make only these changes:

1. update version-identity front matter from v3 to v4 as mechanically required;
2. in the §1.1 annotation replace `1.8e-5` with `1.85e-6`, or the more precise
   `1.8516646205e-6`;
3. replace the inconsistent no-weakening statement with exactly:

   `T-7 is minimally loosened only to implement the valid upward-rounded certification, while remaining 16.55× tighter than the rank convention.`

4. record that the six version-identity front-matter lines were admitted by the
   deputy programme director;
5. make no other substantive, numerical, gate, artifact, or interpretation
   change.

Produce a byte-level v3/v4 changed-line report in the terminal response. Do not
create another report file.

## STAGE 2 — INDEPENDENT MICRO-RECHECK v2

Use the independent reviewer in a separate chat from the author/editor.

Model:

- Opus or equivalent
- thinking on
- medium effort

Attach:

- design v3;
- design v4;
- micro-recheck v1;
- deputy acceptance v1.

Create:

`docs/France_case/P2a/FR_P2a_region_live_phase5_inference_micro_recheck_v2.md`

Verify only:

- corrected relative-change figure;
- exact prescribed T-7 sentence;
- certified constant unchanged at `6.0424e-12`;
- 16.55× comparison unchanged;
- front-matter exception is authorized;
- no other substantive change.

The final line must be exactly:

`MICRO-RECHECK PASS`

If it does not pass, stop and escalate to the Goal 1 Manager. No further
remediation cycle is authorized.

## STAGE 3 — MNL DOCUMENTATION COMMIT

Use Claude Code, Sonnet, thinking on, medium effort, MNL workspace.

Verify:

- MNL pre-commit HEAD and ancestry from `982c522...`;
- nested HEAD/gitlink `27756a...`;
- Phase-3 and Phase-4 bundles rehash exactly;
- no source, config, test, data, output, or accepted artifact changed;
- only the authorized documentation evidence is untracked/modified.

Stage the complete Phase-5 design evidence set under
`docs/France_case/P2a/`, including:

- source-verification report;
- parameter-map CSV;
- source-inventory JSON;
- design v1, v2, v3, v4;
- methods review;
- methods recheck;
- micro-recheck v1 and v2.

Commit once with:

`docs(p2a): freeze Phase-5 inference design`

Report the full new MNL HEAD and clean status. Do not modify the nested repo.

## STAGE 4 — JOB_MARKET_PAPER DOCUMENTATION COMMIT

Use Claude Code, Sonnet, thinking on, medium effort,
`Job_Market_paper` workspace.

Inventory all untracked/modified JMP-M05 management files. Stage only the
authorized Stage-B/C/D instruments and final decision records, including when
present:

- Stage-B author addendum;
- Stage-C reviewer addendum;
- Stage-D cycle instruction;
- superseded prompt records retained for provenance;
- mission ledger v3;
- Goal 1 manager acceptance v1;
- deputy programme acceptance v1;
- PI disclosure determination v1;
- this closure prompt or its committed operational equivalent.

Do not stage unrelated files. Stop on unrelated changes.

Commit once with:

`docs(jmp): accept M05 inference design and authorize M05B`

Report:

- full new `Job_Market_paper` HEAD;
- exact committed file list;
- clean status.

## FINAL RETURN TO GOAL 1 MANAGER

Return:

- design-v4 changed-line report;
- micro-recheck-v2 verdict and path;
- new MNL documentation HEAD;
- new `Job_Market_paper` HEAD;
- both worktree statuses;
- nested HEAD/gitlink;
- Phase-3 and Phase-4 bundle hashes;
- confirmation that no Phase-5 implementation or inference occurred.

The Goal 1 Manager then instantiates and launches JMP-M05B without returning to
the deputy programme director.
