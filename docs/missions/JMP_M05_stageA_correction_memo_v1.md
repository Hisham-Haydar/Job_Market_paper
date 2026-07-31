# JMP-M05 Stage-A Management Correction Memo v1

**Status:** Binding before Stage-A source verification  
**Reviewed artifacts:**

- `JMP_M05_mission_ledger_v1.md`
- `JMP_M05_task_manager_operating_prompt_v1.md`
- `JMP_M05_source_verification_prompt_v1.md`

## 1. Manager verdict

The Goal 1 manager's Stage-A structure is substantively sound, but three operational defects must be corrected before the source audit is issued.

## 2. Defect A — report creation versus read-only prohibition

The v1 source-verification prompt requires creation of three report files while also saying that nothing may be modified.

Those instructions conflict.

The corrected contract is:

- existing source, configuration, tests, data, accepted artifacts, and governance files are read-only;
- creation of exactly three new source-verification report files is permitted;
- no other file may change;
- no commit is permitted.

Use `JMP_M05_source_verification_prompt_v2.md`.

## 3. Defect B — task-manager cleanliness test

The v1 task-manager prompt requires the reports to exist while also requiring a completely unchanged worktree.

The corrected check is:

- `Job_Market_paper` and nested `dclaborsupply` remain unchanged;
- MNL may contain exactly the three intended new report files;
- no pre-existing tracked file may be modified;
- no other untracked file may be created;
- no commit may be made.

Use `JMP_M05_task_manager_operating_prompt_v2.md`.

## 4. Defect C — incomplete housekeeping commit

The proposed housekeeping commit should not contain only the task plan, acceptance memo, and ledger.

The complete management checkpoint should include every newly introduced governance, delegation, mission-management, and operational-prompt file required to reproduce the current workflow.

The commit must be created before Stage A so the audit runs against a stable governance checkpoint.

Do not require the commit to contain its own SHA inside the same commit. Record the SHA in the terminal report and add it to the ledger at the next planned documentation update.

## 5. Current public repository anchors

At review time:

- `Job_Market_paper` public main points to governance commit  
  `30fbe2da40dd5c032fad8bd81f2840ef60ab0ba0`;
- MNL public main points to accepted Phase-4 checkpoint  
  `982c52217031158c4a2368709d4a6b211ebcde76`;
- `dclaborsupply-monorepo` public main points to  
  `27756a06ea189339aa82915ed2124628afed20eb`.

The local commit and worktree state must still be verified by Claude Code.

## 6. Required sequence

1. Give the Goal 1 manager the autonomous operating contract.
2. Replace the v1 source-verification and task-manager prompts with v2.
3. Commit the complete management checkpoint.
4. Open the Sonnet task-manager chat with the v2 operating prompt.
5. Run the v2 source-verification prompt through Claude Code.
6. Return the source report and task-manager completeness verdict to the Goal 1 manager, not to the deputy programme director.
