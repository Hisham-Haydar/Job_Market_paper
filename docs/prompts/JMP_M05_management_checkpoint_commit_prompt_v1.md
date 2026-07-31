# Prompt — Commit JMP-M05 Management Checkpoint v1

**Tool:** Claude Code  
**Model:** Sonnet  
**Thinking:** On  
**Effort:** Medium  
**Workspace:** `Job_Market_paper` repository

ROLE

Create one documentation-only checkpoint for the JMP-M05 management structure.

Do not modify file contents.
Do not inspect or modify MNL, dclaborsupply, empirical code, data, outputs, or
theory-paper files.
Do not rewrite Git history.

VERIFY CURRENT PUBLIC/EXPECTED BASE

Expected prior `Job_Market_paper` governance commit:

`30fbe2da40dd5c032fad8bd81f2840ef60ab0ba0`

If local HEAD differs, report the actual HEAD and inspect whether it is a clean
descendant. Stop if history diverges unexpectedly.

INVENTORY

Run:

- `git status --porcelain --untracked-files=all`
- `git diff --check`

The intended management checkpoint consists of these files, when present:

- `docs/governance/JMP_management_hierarchy_and_delegation_v1.md`
- `docs/governance/JMP_Goal1_manager_operating_contract_v1.md`
- `docs/missions/JMP_M05_task_plan_v1.md`
- `docs/missions/JMP_M05_task_plan_manager_acceptance_v1.md`
- `docs/missions/JMP_M05_design_stage_delegation_packet_v1.md`
- `docs/missions/JMP_M05_mission_ledger_v1.md`
- `docs/missions/JMP_M05_stageA_correction_memo_v1.md`
- `docs/missions/JMP_M05_task_manager_operating_prompt_v2.md`
- `docs/prompts/JMP_M05_source_verification_prompt_v2.md`
- `docs/prompts/JMP_M05_methods_review_prompt_v1.md`

Do not stage the superseded v1 source-verification or task-manager prompts if
they were never committed. If they are already tracked, do not delete them;
leave them tracked and ensure v2 is explicitly marked as current through the
new correction memo.

If any unrelated modified or untracked file exists, stop and list it.

VALIDATE

- all markdown files parse as text;
- required filenames exist;
- v2 source prompt permits only three new audit outputs;
- v2 task-manager prompt expects only those three outputs;
- management contract contains the required action-card fields;
- `git diff --check` passes.

STAGE ONLY THE INTENDED FILES

Run:

- `git diff --cached --check`
- `git diff --cached --stat`
- `git diff --cached --name-status`

Commit once with:

`docs(jmp): delegate M05 design-stage management`

POST-COMMIT REPORT

Report:

- full new commit SHA;
- exact committed file list;
- `git status --porcelain --untracked-files=all`;
- whether the worktree is clean.

Do not modify the ledger merely to insert this same commit's SHA. Record the SHA
in the terminal report; the Goal 1 Manager may add it at the next planned
ledger update.

Do not begin Stage A.
Stop.
