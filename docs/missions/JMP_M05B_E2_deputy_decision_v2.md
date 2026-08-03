# JMP-M05B E2 Deputy Decision v2

**Mission:** JMP-M05B — Phase-5 Inference Implementation and Certification  
**Escalation:** Final exact-state review v3 returned `REJECT` after remediation cycle 2 of 2  
**Decision-maker:** ChatGPT JMP Deputy Programme Director  
**Date:** 2026-08-02  
**Verdict:** ONE ARCHITECTURAL CLOSURE CYCLE AUTHORIZED

## 1. Strategic ruling

The review-v3 REJECT is accepted as valid.

The statistical design remains closed and accepted. No defect concerns the
likelihood, parameterization, accepted estimate, covariance formulas,
finite-sample correction, regional hypotheses, package boundary, or any frozen
D-1 through D-8 decision.

The remaining defects arise because authorization and custody were added
surface-by-surface around a score engine that remains import-callable. A third
ordinary patch cycle is not authorized. Instead, authorize one final
**architectural closure cycle** whose purpose is to reduce the application-level
full-score capability to one gated process entry by construction.

This is an exceptional architecture correction, not remediation cycle 3.

If the follow-on review does not return `APPROVE`, JMP-M05B is paused and the
Phase-5 execution architecture must be redesigned as a new mission. No further
patch cycle is authorized under JMP-M05B.

## 2. Frozen threat model

The certification boundary protects against:

- accidental or unsupported invocation;
- bypass through documented or import-callable application routes;
- stale or caller-supplied configuration;
- forged review/revision/custody inputs;
- output-path substitution;
- Git-worktree leakage;
- transaction and failure-record inconsistencies;
- mutation between evaluation and publication.

The boundary does **not** claim security against an adversary who already has
arbitrary code execution in the same Python interpreter and may monkeypatch,
rewrite, introspect, or replace source code.

Python capability objects are therefore required to be operationally
unforgeable through supported interfaces and ordinary imports, not
cryptographically unforgeable against arbitrary in-process code execution.

The reviewer may not expand the threat model beyond this statement.

## 3. Exactly one full-score-capable application surface

The accepted architecture must have exactly one application-level process
entry capable of evaluating all 1,555 household scores:

`run_p2a_phase5_inference.py` through its canonical gated process entry.

The canonical entry may execute either:

1. the parent dry-run role; or
2. an internally authorized T-12 child role.

Both roles must pass through the same process entry and the same canonical
authorization architecture.

No other application function, helper, test seam, import route, or caller-
supplied configuration route may be capable of producing the full 1,555×37
score matrix.

Low-level generic package derivatives remain outside this surface count. They
are mathematical building blocks, not authorized Phase-5 application
orchestration and may not independently construct the accepted Phase-5 score
artifact.

## 4. Capability and configuration directive

The full-score call must require an opaque process-local authorization context
created only after all canonical gates pass.

The supported architecture must ensure:

- no public constructor for the authorization context;
- no caller-supplied boolean, record, configuration object, or output path can
  substitute for it;
- canonical Phase-5 YAML is loaded by the gated entry and bound by digest;
- restricted-store identity is bound to the authenticated provisioning record;
- the score-building call is unreachable from the ordinary contract-only
  helpers;
- the T-12 child uses a single-use parent-issued capability bound to the exact
  attempt, revisions, review, bundles, configuration, and store identity;
- the child capability is consumed once and cannot authorize a second attempt.

A nested scoring closure or equivalent private worker architecture is preferred.
The implementation must not pretend that a module-private sentinel alone is a
cryptographic security boundary.

## 5. Closed-form surface inventory

Before independent review, create and commit with the implementation:

`docs/France_case/P2a/phase5_full_score_surface_inventory_v1.json`

It must enumerate every application-level route capable of requesting or
triggering a full score evaluation.

Required result:

- `surface_count = 1`;
- the sole surface is the canonical gated process entry;
- parent and T-12 child roles are recorded as roles of that same surface;
- every formerly exposed route is listed as removed or structurally incapable;
- the inventory includes source file, symbol, role, authorization prerequisites,
  configuration source, custody destination rule, and test proving refusal of
  all noncanonical routes.

The inventory is a review input, not self-certifying evidence.

If the reviewer identifies a second application-level full-score surface, the
result is automatic `REJECT`.

## 6. Remaining narrow fix groups

In the same architectural closure cycle, implement exactly these six groups:

1. revalidate STOPPED rename source immediately before rename and validate the
   resulting endpoint after rename;
2. run complete post-evaluation reauthentication in every full-score process,
   including the T-12 child;
3. inventory every retained filesystem member, including directories,
   junctions, unreadable members, and partial files, with truthful top-level
   custody and STOPPED bundle hashes;
4. add behavioral integration tests for direct-route refusal, canonical-config
   binding, T-12 mutation, STOPPED junction replacement, partial-write
   truthfulness, and no-publication outcomes;
5. replace the working-set guard with exact lifecycle-aware assertions valid in
   uncommitted, committed, and one-preserved-dry-run states;
6. correct stale review-v2 help text and every remaining comparator description
   to the approved mixed absolute/relative R-23b-rev language.

No other design, numerical, package, or feature change is authorized.

## 7. Reviewer-continuity ruling

Use the same independent reviewer role:

- Codex;
- GPT-5.6 Codex or current strongest code-review model;
- maximum reasoning;
- fresh session;
- read-only.

Review v4 must use the same 51-gate framework where applicable, plus the
closed-form surface inventory.

The reviewer must:

- verify the seven authorized groups;
- respect the frozen threat model;
- not add new security objectives;
- not require protection against arbitrary same-process source modification;
- treat the surface class as settled when exactly one canonical application
  surface exists and every noncanonical route is structurally incapable.

## 8. Review-v4 decision rule

Review v4 may return only:

- `APPROVE`; or
- `REJECT`.

`APPROVE AFTER FIXES` is not available because no remediation budget remains.

`APPROVE` requires:

- exactly one application-level full-score surface;
- all six narrow groups pass;
- all applicable original review gates pass;
- no statistical-design or package change;
- no full dry run or household score artifact created during remediation or
  review.

`REJECT` pauses JMP-M05B and returns immediately to the deputy programme
director. No further code change is authorized.

## 9. Commit and dry-run gate

After review v4 `APPROVE` only:

1. commit the isolated Phase-4 test-42 housekeeping separately;
2. commit the exact reviewed Phase-5 implementation, surface inventory,
   remediation report, and review v4;
3. require clean MNL and nested worktrees;
4. bind one full dry run to exact revisions, review-v4 path/hash, accepted
   Phase-3 and Phase-4 bundles, canonical config digest, parameter-map digest,
   and restricted-store identity;
5. run exactly one full dry run;
6. preserve its attempt; never create `complete/`;
7. return the audited dry-run packet to the deputy programme director.

The production real run remains unauthorized.
