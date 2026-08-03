# Prompt — Provision JMP-M05B Restricted Artifact Store v1

**Tool:** Claude Code  
**Model:** Sonnet  
**Thinking:** On  
**Effort:** Medium  
**Mode:** Local infrastructure only  
**Workspace:** Common parent with access to `C:\Users\hisham\Repo\MNL` and the
non-repository data-store area

## ROLE

Provision and verify the restricted artifact store required by JMP-M05B fix 8.

Do not modify MNL source code, tests, accepted artifacts, Git history, or the
nested package.
Do not compute scores or run Phase 5.
Do not create household-level data.

## TARGET

Preferred root:

`C:\Users\hisham\MNL\restricted_artifacts\p2a_phase5`

If that path is unavailable, stop and report the actual non-Git persistent data
roots visible on the machine. Do not choose another path silently.

## VERIFY BEFORE CREATION

1. Resolve the MNL Git root:
   `C:\Users\hisham\Repo\MNL`.
2. Discover all Git worktrees under `C:\Users\hisham\Repo` and any parent or
   sibling path that could contain the target.
3. Prove the target and every ancestor below the user profile are not inside a
   Git worktree.
4. Confirm the target is not under a temporary directory or cloud-synchronised
   public folder.
5. Record the filesystem type and free space.

## PROVISION

Create:

- `restricted_artifacts\p2a_phase5\staging`
- `restricted_artifacts\p2a_phase5\published`

Apply Windows ACLs:

- disable inherited permissions;
- grant FullControl to the current Hisham account;
- grant FullControl to `SYSTEM`;
- grant FullControl to local Administrators;
- remove other inherited or explicit user/group access unless required by the
  machine's mandatory policy.

Do not print the full ACL-sensitive locator into a public or commit-eligible
report beyond the redacted form approved below.

## OPERATIONAL IMMUTABILITY CONTRACT

Verify that the future implementation can:

1. create a unique staging directory;
2. write a closed member set there;
3. fsync/close all files;
4. write hashes and a custody manifest;
5. atomically rename the whole staging directory into `published`;
6. refuse overwrite if the destination exists;
7. preserve failed staging directories with a STOPPED suffix;
8. never write restricted artifacts under any Git root.

Do not test with real scores. Use tiny synthetic byte files only.

## CREATE

Create one local, non-Git provisioning record:

`C:\Users\hisham\MNL\restricted_artifacts\p2a_phase5\restricted_store_provisioning_v1.json`

It must contain:

- redacted locator;
- creation timestamp;
- current-user SID;
- ACL summary;
- Git-ancestry checks;
- filesystem facts;
- atomic-rename synthetic test result;
- overwrite-refusal test result;
- disclosure class;
- custodian;
- retention status;
- SHA-256 of the record.

Do not commit this record.

## RETURN

Return to the Goal 1 manager:

- provisioning verdict;
- redacted root, e.g. `%USERPROFILE%\MNL\restricted_artifacts\p2a_phase5`;
- whether all Git-ancestry checks passed;
- whether ACL restriction passed;
- whether atomic publication and overwrite refusal passed;
- provisioning-record SHA-256;
- any institutional-backup caveat.

Use one verdict:

- RESTRICTED STORE READY
- READY WITH RETENTION WARNING
- BLOCKED
