DEPUTY RULING — PKG-01A CROSS-REFERENCE AND JMP-HK-01

# 1. GOAL-2 CROSS-REFERENCE

Record this exact one-line entry in the existing Goal-1 decision log:

> PKG-01A closed under Goal 2 on branch `pkg/pk01a-notebook-api-stabilisation`; code close `b82d03de82bc505e4b0d12ce83daccbc5e1749a0`, branch tip with acceptance record `301e54678ced97a0dc1d081cf07a7934f98ea077`; package `main`, MNL's pinned package revision, and the MNL gitlink remain unchanged.

Do not copy the PKG-01A acceptance memo or package source files into
Job_Market_paper. No further Goal-1 action arises from PKG-01A now.

# 2. JMP-HK-01 AUTHORIZATION

JMP-HK-01 is authorized as a two-phase Goal-1 housekeeping mission.

It is a repository hygiene mission, not an M08 scientific mission.

SCOPE:

* MNL;
* Job_Market_paper;
* their JMP-related tracked and untracked output, staging, scratch and
  development trees.

dclaborsupply-monorepo is excluded from disposition or cleanup.
It may be inspected read-only only to identify references.
Its tracked build/ cleanup remains PKG-01B work.
The MNL/Job_Market_paper repository merger remains deferred.

# 3. BINDING TAXONOMY

Use exactly these five disposition classes:

1. CANONICAL_CURRENT

Current accepted code, evidence, result, contract, manuscript object,
pointer or live mission input.

2. HISTORICAL_IMMUTABLE_IN_PLACE

Ruling-protected history, accepted superseded reports, accepted attempt
records, or any artifact whose current path is part of the accepted
evidentiary lineage.

3. ARCHIVE_MOVABLE

Tracked superseded material that is:

* not pinned;
* not referenced by a current manifest, registry, acceptance pointer,
  contract, manuscript or live review;
* not protected by an immutability ruling;
* still useful enough to retain visibly.

4. DELETE_TRACKED

Tracked material with no current evidentiary, operational, manuscript
or protected historical-retention role. Delete only with git rm;
Git history retains it.

5. ARCHIVE_EXTERNAL_THEN_DELETE_UNTRACKED

Untracked material may be deleted only after it is copied to an
external dated archive and recorded in a source-path / size / SHA-256
archive manifest.

Any unresolved classification defaults to:

HOLD — NO ACTION

HOLD is not an actionable disposition and may not be silently converted.

# 4. ARCHIVE AMENDMENT

Do not move a ruling-protected or accepted historical artifact merely
because it is superseded.

Such an artifact remains:

HISTORICAL_IMMUTABLE_IN_PLACE

unless a later deputy ruling explicitly authorizes relocation.

A supersession map does not override:

* an immutable-history ruling;
* a manifest path or hash;
* a pin registry;
* an accepted pointer;
* an exact path cited by a current contract, manuscript or review.

Therefore ARCHIVE via git mv is approved only for unpinned,
unreferenced, non-ruling-protected tracked material.

Pinned paths and accepted attempt directories are categorically exempt.

# 5. PHASE-1 TIMING AND CONTENT

Begin Phase 1 only after:

1. the current pricing work has stopped; and
2. the working discussion notebook has returned to the Goal 1 Manager.

Phase 1 is read-only.

It must create:

1. `JMP_HK_01_inventory_and_disposition_register_v1.csv`
2. `JMP_HK_01_inventory_summary_v1.md`
3. `JMP_HK_01_reference_protection_map_v1.csv`

The register must contain at least:

* repository/tree;
* absolute and repository-relative path;
* tracked/untracked status;
* file type;
* size;
* SHA-256 where applicable;
* current Git status;
* latest modifying commit for tracked files;
* manifest references;
* pin-registry references;
* accepted-pointer references;
* current-document path references;
* immutability-ruling protection;
* canonical successor, if any;
* proposed disposition;
* reason;
* proposed archive or deletion action;
* whether deputy ratification is required.

The inventory must mechanically scan:

* committed manifests;
* both current pin registries;
* accepted pointers;
* current mission contracts;
* current manuscript and result maps;
* exact path strings in accepted reviews and rulings.

Do not infer canonical status from the highest version number alone.
Use acceptance records, pointers, manifests and current governance.

# 6. PHASE-1 TOOL ROUTING

The Goal 1 Manager must issue a complete NEXT ACTION CARD.

Preferred execution:

* Tool: Claude Code
* Model: Sonnet
* Thinking: ON
* Effort: High
* Mode: read-only inventory
* MNL: read-only
* Job_Market_paper: read-only
* dclaborsupply-monorepo: read-only reference scan only
* No files moved, deleted, renamed, committed or archived

After the inventory, commission one bounded independent review:

* Tool: GPT-5.6 Codex
* Mode: read-only
* Reasoning: High

The Codex review is restricted to:

* pin/manifest protection;
* current-reference protection;
* ruling-protected history;
* disposition-class correctness;
* completeness of the external-archive plan for untracked material.

Return the inventory register, summary and Codex verdict to the deputy
for ratification.

Phase 2 is not self-authorized by a Phase-1 PASS.

# 7. PHASE-2 TIMING

Phase 2 may begin only after all of the following:

1. U6-E independent review is complete;
2. the U6 results/evidence commit is complete;
3. no active review or runner targets an affected path;
4. the deputy has ratified the exact Phase-1 disposition register.

Do not perform cleanup merely because Phase 1 identifies candidates.

# 8. PHASE-2 EXECUTION RULES

Use separate gated commits for MNL and Job_Market_paper.

Prohibited:

* wildcard recursive deletion;
* `git clean -fd`;
* `git clean -fdx`;
* deleting or moving accepted attempt directories;
* moving pinned files;
* editing manifests or pin registries merely to permit cleanup;
* deleting raw data;
* copying household-level or restricted files into
  Job_Market_paper;
* cleaning dclaborsupply-monorepo;
* merging repositories.

For tracked deletions:

* use `git rm`;
* confirm no current reference remains;
* preserve Git history.

For ARCHIVE_MOVABLE:

* use `git mv`;
* create a supersession-map entry;
* verify no current exact-path reference remains before commit.

For untracked deletion:

* archive outside all active Git repositories;
* create a manifest containing original path, archive path, size,
  SHA-256 and verification status;
* verify the copied bytes before deleting the original;
* never use a broad clean command.

After execution, rerun every manifest, pin-registry and current-reference
check against the resulting trees.

# 9. DOCUMENTATION PROPORTIONALITY

Permanently retain only:

1. one JMP-HK-01 mission charter;
2. the Phase-1 disposition register;
3. one independent Phase-1 review;
4. one deputy-ratified execution register;
5. one final execution/acceptance record.

Routine prompts, action cards and progress notes remain disposable chat.

Do not create a separate memo for each deleted or moved file.

# 10. RETURN RULE

Return to the deputy with the Phase-1 packet before any movement or
deletion.

After deputy ratification, manage Phase 2 autonomously and return only
if:

* a pinned or ruling-protected artifact would need to move;
* a current reference cannot be reconciled;
* an untracked destructive deletion cannot be archived and verified;
* an accepted result or manifest would be altered;
* cleanup would touch dclaborsupply-monorepo;
* or the approved register would need substantive revision.
