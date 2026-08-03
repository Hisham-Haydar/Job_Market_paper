# Prompt — Archive Rejected JMP-M05B State and Salvage Test 42

**Tool:** Claude Code  
**Model:** Sonnet  
**Thinking:** On  
**Effort:** High  
**Workspace:** MNL and non-Git local archive root  
**Scope:** Preservation, cleanup, evidence commits, test-42 salvage only

## ROLE

Close the paused JMP-M05B working state without losing evidence and prepare a
clean base for JMP-M05C.

Do not implement JMP-M05C.
Do not run scores or inference.
Do not modify dclaborsupply.
Do not alter accepted Phase-3 or Phase-4 artifacts.

## STAGE 1 — INVENTORY

Record:

- MNL HEAD and complete status;
- nested HEAD/gitlink and status;
- every modified and untracked file;
- Phase-3 and Phase-4 bundle hashes;
- confirmation that no score bytes, attempt, output root, or `complete/` exists.

## STAGE 2 — LOCAL FORENSIC ARCHIVE

Use a persistent non-Git root:

`%USERPROFILE%\MNL\archives\jmp_m05b_paused_review_v4_<timestamp>`

Create:

- `working_tree_binary.patch` from tracked changes;
- an archive of all untracked files preserving relative paths;
- exact file inventory;
- copies of reviews v1-v4, remediation/closure reports, and surface inventory;
- `archive_manifest.json` with SHA-256 for every member;
- a top-level archive SHA-256.

Confirm the archive is outside every Git worktree and contains no household
score bytes.

Do not commit the archive.

## STAGE 3 — COMMIT EVIDENCE ONLY

From the archived set, retain in MNL only the non-executable documentation
evidence required for project history:

- implementation report;
- remediation reports;
- architectural-closure report;
- code reviews v1-v4;
- surface inventory marked as rejected/historical;
- any source-free escalation evidence already assigned to MNL docs.

Do not retain rejected runner/helper/config/test changes.

Commit documentation only with:

`docs(p2a): record paused M05B implementation reviews`

Report the exact committed file list and new MNL HEAD.

## STAGE 4 — CLEAN REJECTED SOURCE

Restore all rejected Phase-5 source, config, and test changes to the clean
accepted base plus the documentation commit.

Remove untracked rejected implementation files only after archive hash
verification.

Require:

- MNL clean;
- nested clean;
- accepted bundles unchanged;
- no Phase-5 output;
- no score bytes.

## STAGE 5 — TEST-42 SALVAGE

Apply only the accepted Phase-4 test-42 housekeeping correction:

- isolate test-created evidence;
- hash accepted Phase-4 `complete/` before and after;
- require byte identity;
- run the corrected test 10 times;
- run related no-Hessian tests;
- create/update the housekeeping report.

Obtain a narrow independent read-only review of this isolated diff.

After approval, commit separately with:

`test(p2a): make Phase-4 dry-run test acceptance-safe`

## RETURN

Return to the Goal 1 Manager:

- archive locator in redacted form;
- archive manifest SHA;
- evidence-only documentation commit SHA;
- test-42 commit SHA;
- exact committed file lists;
- MNL and nested clean status;
- bundle hashes;
- confirmation no rejected source remains;
- confirmation no score bytes exist.

Do not begin JMP-M05C.
