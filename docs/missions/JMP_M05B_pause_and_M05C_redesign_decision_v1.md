# JMP-M05B Pause and JMP-M05C Redesign Decision v1

**Programme:** Goal 1 — Empirical JMP  
**Decision-maker:** ChatGPT JMP Deputy Programme Director  
**Date:** 2026-08-02  
**Status:** Binding  
**Verdict:** CLOSE JMP-M05B WITHOUT IMPLEMENTATION ACCEPTANCE; LAUNCH JMP-M05C

## 1. Finding

Independent review v4 correctly rejected the JMP-M05B implementation.

The decisive findings are:

1. `_phase5_contract_impl()` remained a second ordinary import-callable
   application route exposing all ingredients needed to construct the complete
   household-score matrix;
2. the nominal canonical path was itself non-executable because the score
   provider failed the evaluator's `callable()` precondition;
3. tests masked the production mismatch by replacing the evaluator;
4. the declared surface inventory was therefore false;
5. authorization, T-12, STOPPED, reauthentication, retained-member, lifecycle,
   and documentation defects remained.

The statistical design and package boundary continued to pass. The failure is
an implementation-architecture and implementer-reliability failure.

## 2. JMP-M05B disposition

JMP-M05B is closed as:

`PAUSED — NO IMPLEMENTATION ACCEPTED`

No Phase-5 source from the rejected working set may be merged into or committed
on the main application line.

The reviews, reports, surface inventory, and escalation records must be retained
as evidence. The rejected source diff must be archived outside Git before the
working tree is cleaned.

No additional repair of the rejected architecture is authorized.

## 3. Strategic redesign

Launch:

`JMP-M05C — Minimal Streaming Inference Implementation`

The redesign removes the source of the custody/authorization spiral:

- no household-level score matrix is persisted;
- no row-level score CSV or NPY is created;
- no restricted score store is required;
- scores are computed in bounded transient batches;
- only aggregate sufficient statistics and one global score-stream digest are
  retained.

The scientific target is unchanged. The persistence contract is simplified.

## 4. Superseded decision

The previous D-3 requirement to preserve an authoritative `1555×37` household
score `.npy` is superseded.

The replacement contract is defined in:

`JMP_M05C_streaming_inference_design_addendum_v1.md`

All other accepted statistical decisions remain frozen unless that addendum
states otherwise.

## 5. Review boundary

The new implementation is reviewed as a scientific inference pipeline, not as
a capability-security system.

Review must establish:

- exact use of the accepted likelihood and parameter maps;
- correct score aggregation;
- fresh-process numerical reproduction;
- no row-level score persistence;
- deterministic aggregate artifacts;
- truthful transaction/provenance records;
- no optimizer, model, package, welfare, or decomposition change.

Review must not require:

- cryptographic in-process authorization;
- an unforgeable Python token;
- exactly one import-callable score-capable helper;
- security against a user who can rewrite or monkeypatch source code.

## 6. Test-42 salvage

The isolated Phase-4 test-42 housekeeping is authorized for salvage and a
separate commit.

It must:

- leave the accepted Phase-4 `complete/` bundle byte-identical;
- isolate all test-created evidence;
- run repeatedly;
- be independently checked;
- remain separate from JMP-M05C implementation.

Recommended commit:

`test(p2a): make Phase-4 dry-run test acceptance-safe`

## 7. Rejected-state preservation

Before cleaning MNL:

1. archive the complete rejected uncommitted working set outside every Git
   worktree;
2. include a binary Git diff, untracked-file archive, file inventory, review
   files, and SHA-256 manifest;
3. confirm no household score bytes exist;
4. retain the archive locally for forensic reference;
5. commit only the non-executable review/report evidence to MNL main;
6. restore MNL to a clean source state before JMP-M05C begins.

The rejected implementation code itself must not be committed to main.

## 8. Restricted-store disposition

The provisioned restricted store remains empty and is no longer a dependency of
Phase 5.

No further ACL, atomic-publication, replication, or backup work is required for
JMP-M05C.

It may remain provisioned but unused. It must not be referenced by the new
runner or manifest.

If a later mission requires household influence diagnostics, bootstrap
replicates, or row-level score retention, it must obtain a new explicit
disclosure and storage ruling.

## 9. Replication and retention ruling

The public or shared replication layer may contain:

- code;
- canonical configuration;
- parameter maps;
- aggregate score sums;
- aggregate meat matrices;
- model and robust covariance matrices;
- parameter and regional-test tables;
- scalar diagnostics;
- the global score-stream digest;
- manifests and hashes.

It must not contain:

- EU-SILC/EUROMOD microdata;
- household identifiers;
- household-level score rows;
- row-level score hashes;
- temporary score batches.

Licensed replicators recompute the aggregate objects inside their authorized
data environment.

No special replication ACL is required for the approved aggregate outputs,
subject to ordinary disclosure review.

## 10. Fresh implementation requirement

JMP-M05C must use:

- a fresh Claude Code implementation session;
- accepted source and design documents, not rejected implementation code;
- incremental implementation;
- reviewer-runnable production-path proofs;
- no fixture replacement of the production evaluator in integration tests;
- independent review after each increment.

The rejected code may be consulted only as a negative-design record, not copied
as the implementation base.

## 11. Authorization

Authorize the Goal 1 Manager to:

1. archive and clean the rejected state;
2. salvage test 42;
3. commit review/report evidence;
4. create the JMP-M05C mission ledger;
5. manage the three implementation increments and independent reviews;
6. commit only review-approved increments;
7. perform one full audited dry run after final integrated approval.

The production real run remains unauthorized.
