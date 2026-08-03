# JMP-M05B E2 Deputy Decision v1

**Mission:** JMP-M05B — Phase-5 Inference Implementation and Certification  
**Escalation:** Independent code review v1 returned `REJECT`  
**Decision-maker:** ChatGPT JMP Deputy Programme Director  
**Date:** 2026-08-01  
**Verdict:** BOUNDED REMEDIATION AUTHORIZED

## 1. Decision

The code-review REJECT is accepted as valid.

The statistical design, accepted likelihood route, parameter-space rulings,
covariance algebra, and regional-test design remain closed. The defects are
implementation and certification defects concentrated in custody,
authorization, transactionality, artifact authentication, runtime provenance,
and lifecycle-valid testing.

Authorize one bounded remediation implementing exactly the twelve required
fixes in `FR_P2a_region_live_phase5_code_review_v1.md`.

Do not reopen design v4, D-1 through D-8, the accepted model, the accepted theta,
the likelihood, the parameterization, or any numerical gate constant.

## 2. Repository state accepted at escalation

- MNL HEAD:
  `983a2ecf1d16592b9f90085f6a6b690b8a964110`
- `Job_Market_paper` HEAD:
  `7195fc50f6a73e20bdf62fc4baae48c18dedd345`
- nested `dclaborsupply` HEAD and MNL gitlink:
  `27756a06ea189339aa82915ed2124628afed20eb`
- accepted Phase-3 and Phase-4 bundles: rehash verified
- Phase-5 implementation and review v1: preserved uncommitted
- no `complete/`
- no household-level score bytes created

## 3. Remediation-budget ruling

The REJECT remediation counts as **remediation cycle 1 of 2** under JMP-M05B.

After remediation:

- review v2 `APPROVE` permits the exact-state commit gate;
- review v2 `APPROVE AFTER FIXES` permits one final narrow remediation cycle;
- review v2 `REJECT` is an E2 halt and returns to the deputy programme director;
- no third remediation cycle is authorized under the current mission.

## 4. Authorized remediation scope

Implement exactly the review-v1 required fixes:

1. remove or fully gate public full-score reproduction;
2. resolve restricted destinations against actual Git ancestry and discovered
   worktrees;
3. move final gate-register evaluation after T-12, T-13, T-20, and T-23;
4. authenticate and use the binding Phase-5 parameter-map CSV;
5. authenticate and use the accepted full-gradient pin coordinates;
6. rehash/reload Phase-3, Phase-4, theta, and consumed inputs after evaluation;
7. reproduce T-12 without a duplicate unregistered score artifact;
8. bind a provisioned restricted store with external staging and atomic
   publication;
9. initialize and preserve unconditional custody fields on every attempt;
10. install and verify the optimizer/prohibited-module guard across all
    execution paths;
11. record actual chunk size and post-contract/post-evaluation runtime state;
12. add deterministic tests for fixes 1–11 and remove lifecycle-invalid and
    tautological tests.

No scope beyond these items is authorized.

## 5. Restricted-store ruling

For the **reviewed dry-run stage**, use a persistent Windows directory outside
every Git worktree and outside temporary directories.

Preferred root, subject to local verification:

`C:\Users\hisham\MNL\restricted_artifacts\p2a_phase5`

This path is in the existing non-repository data-store area, not the MNL Git
repository at `C:\Users\hisham\Repo\MNL`.

The Goal 1 manager must commission local provisioning and verify:

- no ancestor is a Git worktree;
- inherited ACLs are disabled;
- access is restricted to Hisham, `SYSTEM`, and local Administrators;
- publication uses unique non-overwriting staging plus atomic directory rename;
- published attempt directories are operationally immutable: no overwrite,
  closed member set, hashes and manifest fixed;
- the custody locator is redacted from commit-eligible artifacts;
- household-level arrays never enter Git.

This is sufficient for the implementation review and one dry run. Before a
production real run, the deputy programme director may require confirmation of
institutional backup/retention.

## 6. Independent review v2

Authorize a new Codex read-only review bound to the exact remediated state.

Review v2 must:

- verify all twelve fixes individually;
- confirm no design change;
- confirm no package modification;
- inspect the provisioned-store contract without exposing sensitive locator
  details;
- verify the corrected no-full-score deterministic suite;
- verify lifecycle-valid tests for pre-commit, committed, and dry-run states;
- remain fail-closed;
- create a new review file; review v1 remains immutable history.

No commit and no full dry run may occur before review v2 `APPROVE`.

## 7. Stale Phase-4 test 42

Authorize a separate housekeeping correction.

It is not one of the twelve Phase-5 fixes and does not consume remediation
budget.

The change must be isolated and separately committed:

- replace the stale assertion that accepted Phase-4 `complete/` is absent;
- verify accepted `complete/` is byte-identical before and after the test;
- direct test-created dry-run evidence to an isolated temporary location;
- leave the accepted Phase-4 bundle unchanged.

The Phase-5 review v2 may verify this separate change, but the code and commit
must remain logically separate from the Phase-5 implementation commit.

## 8. Commit and execution gates

After review v2 `APPROVE`:

1. create the isolated test-42 housekeeping commit;
2. create the exact reviewed Phase-5 implementation/review commit;
3. require MNL and nested worktrees clean;
4. bind the dry run to the exact post-commit MNL HEAD, nested HEAD/gitlink,
   review-v2 path/hash, Phase-3 bundle, and Phase-4 bundle;
5. run exactly one full dry run;
6. never create `complete/`;
7. return to the Goal 1 manager for audit.

The production real run remains unauthorized.

## 9. Next delegated action

The Goal 1 manager is authorized to manage:

- restricted-store provisioning;
- bounded remediation cycle 1;
- deterministic tests;
- independent review v2;
- at most one final narrow remediation if review v2 says
  `APPROVE AFTER FIXES`;
- separate test-42 housekeeping;
- exact-state commits;
- one full dry run and its audit.

Return to the deputy programme director only after the audited dry-run packet,
or immediately on another E2 halt.
