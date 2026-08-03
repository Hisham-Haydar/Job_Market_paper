# JMP-M05C Deputy Phase-5 Acceptance v1

**Programme:** Goal 1 — Empirical JMP  
**Mission:** JMP-M05C — Minimal Streaming Inference Implementation  
**Decision-maker:** ChatGPT JMP Deputy Programme Director  
**Date:** 2026-08-03  
**Verdict:** PHASE-5 INFERENCE ACCEPTED — NO SECOND NUMERICAL RUN REQUIRED

## 1. Strategic decision

The audited full-population aggregate-only dry run is accepted as the canonical
Phase-5 inference result.

A second numerical "production real run" is not authorized because it would
repeat the same full-sample computation without adding scientific information.

The accepted attempt already:

- used all 1,555 households;
- produced `inference_grade: full-sample`;
- generated the complete aggregate inference artifact set;
- passed every gating gate;
- satisfied the full-population score identity;
- reproduced the aggregate score stream and meat matrices bitwise in a fresh
  process;
- persisted no household-level score rows;
- bound the accepted model, theta, Hessian, specification, configuration,
  package revision, and Phase-3/Phase-4 bundles.

The remaining distinction between "dry run" and "production run" is publication
status, not numerical content. Phase-5 therefore closes by **acceptance and
evidence promotion**, not by recomputation.

## 2. Canonical accepted result

Execution anchor:

`bd7e3af2a0056b43f3fb8b50b858f358ed7a8825`

Nested dclaborsupply revision and gitlink:

`27756a06ea189339aa82915ed2124628afed20eb`

Accepted attempt:

`20260803T133122Z_14772_817e8deb503d408fa73b8b53d598c0db_dryrun`

Accepted attempt status:

`PHASE_5_DRY_RUN_COMPLETE`

Accepted Phase-5 bundle SHA-256:

`d08947ce015f2b2a922c6d5591ebe600c53016922b3a1158d90f125cd2195232`

Accepted score-stream SHA-256:

`7f71a532ff66a1e882f4a085ca78e14a9788e6c98cff8c04957b9df4c3ff4a80`

Accepted Phase-3 bundle:

`2cf237648743f59bd742b12feceaea67c5fd377b26faf4fb6fad6f452f86864b`

Accepted Phase-4 bundle:

`5484886985aecd28e511719e42f45b85ad0e1755d1f951dbd13a79281d9665f3`

## 3. Statistical acceptance

Accept:

- full-population score identity maximum absolute deviation:
  `1.457e-13`, against the `1e-8` gate;
- T-12S fresh-process reproduction: bitwise score-stream digest and exact
  aggregate score/meat reproduction;
- T-23S: aggregate-only member set, no row-level score artifact, no leftovers;
- 35-dimensional conditional robust covariance;
- finite-sample correction:
  `1555/1520 = 1.0230263157894737`;
- accepted active-bound and pinned-parameter reporting;
- H0-A/B/C/G regional/access inference outputs;
- complete environment and revision capture.

The numerical application anchor remains the execution commit
`bd7e3af2...`. Later evidence or test-only commits must be recorded separately.

## 4. Reviewer-substitution ruling

No post-reset Codex re-verification is required before acceptance.

The substitutions used during Increment B and Increment C are disclosed. They
do not justify another review cycle because:

- the statistical core passed throughout;
- the final production-path dry run exercised the complete full-population
  computation;
- T-12S independently reproduced the sufficient statistics;
- the Goal 1 audit verified the final artifact bundle;
- no unresolved finding falls within the blocking classes of the certification
  proportionality rule.

A later optional code audit may be performed as package maintenance, but it is
not a prerequisite for the JMP.

## 5. W-4 ruling

W-4 flags:

- `beta_l0_sm`;
- `beta_w_pexp2`.

Apply S-10 Tier 1 now:

1. carry both names into the Phase-5 interpretation memo and inference appendix;
2. state that their symmetric robust 95% intervals are near the parameter
   boundary and should be interpreted cautiously;
3. do not treat this warning as evidence against the accepted model or as a
   reason to re-estimate Phase 3;
4. in M07/M08, record whether each coordinate materially loads on the welfare
   or decomposition functional and include one targeted local sensitivity.

S-10 Tier 2 is not triggered now.

Tier 2 becomes mandatory only if:

- the paper makes direct inference on a boundary coordinate;
- the welfare/decomposition functional loads materially on one of the flagged
  coordinates; or
- an unconditional active-set claim is proposed.

## 6. Retention and replication ruling

The special restricted-score retention and ACL question is closed as moot for
Phase 5.

The accepted workflow retains no household-level score matrix, household-level
score hashes, or temporary score batch.

The MNL evidence commit may contain the 19 aggregate-only artifacts, subject to
a final mechanical scan confirming:

- exact allowlist membership;
- no household identifiers;
- no row-level score object;
- no temporary or staging member;
- hashes match the accepted manifest.

Ordinary disclosure review still applies before any public replication release,
but no special restricted-score store or replication ACL is required.

## 7. D11 ruling

Authorize the one-line lifecycle correction to `test_N6` and `test_P5`.

The correction must replace the permanent output-root-absence assertion with
the property actually under test:

- the tested refusal/run does not change the canonical root's listing; or
- the relevant CLI refusal arm succeeds without writing.

The D11 correction is test-only. It must not alter the runner, numerical
artifacts, accepted attempt, manifest, or production result.

After the fix, the full suite must return to the pre-run green state:

`276 passed, 1 deselected`

or the exact equivalent count after documentation-only test collection changes,
with no unexplained failure.

## 8. Authorized commits

Authorize three separate checkpoints.

### MNL evidence commit

Commit:

- the exact 19-member accepted attempt;
- the Goal 1 dry-run acceptance memo;
- this deputy acceptance or an exact repository copy;
- the mission ledger v4 where appropriate;
- a canonical Phase-5 acceptance pointer identifying the attempt path, bundle
  hash, execution anchor, and accepted status.

Recommended message:

`results(p2a): accept full-sample Phase-5 inference`

Do not create or copy a `complete/` directory. The acceptance pointer makes the
existing immutable attempt canonical.

### MNL D11 test-only commit

After the evidence commit, apply and validate D11 separately.

Recommended message:

`test(p2a): make Phase-5 lifecycle checks post-run safe`

### Job_Market_paper instrument checkpoint

Commit the accumulated M05B/M05C governance, prompts, decisions, ledgers, and
acceptance records in one documentation-only checkpoint.

Recommended message:

`docs(jmp): close M05C and accept Phase-5 inference`

## 9. Mission disposition

JMP-M05C is accepted and closed.

The Phase-5 inference objects are reportable as accepted empirical results,
subject to:

- the W-4 caveat;
- the distinction between the regional/access block and the complete opportunity
  mechanism;
- the conditional 35-dimensional active-set interpretation;
- ordinary manuscript review.

No second Phase-5 numerical run is required.
