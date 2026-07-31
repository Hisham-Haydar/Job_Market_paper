# JMP-M05 Mission Ledger v1

**Mission:** JMP-M05 — Household-Clustered Inference
**Goal manager:** Goal 1 Manager — Empirical JMP (this persistent chat)
**Delegation authority:** `JMP_M05_design_stage_delegation_packet_v1.md`
**Ledger opened:** 2026-07-30
**Target repository path:** `docs/missions/JMP_M05_mission_ledger_v1.md`
**Ledger status:** Operational file. Not canonical state. Not a decision log.

---

## 1. Current stage

**Stage A — Source verification: OPEN.**

Stages B (design memo), C (independent methods review), D (narrow remediation),
and E (final Goal 1 decision) are PENDING and may not begin before Stage A
closes.

| Stage | Status | Gate to close |
| --- | --- | --- |
| A — Source verification | OPEN | Report received; completeness verified by task manager; no DESIGN-BLOCKING item UNKNOWN; Goal 1 manager acceptance of factual findings |
| B — Design memo | PENDING | Memo delivered at charter path by separate Opus author chat |
| C — Independent methods review | PENDING | Review report delivered by separate reviewer chat |
| D — Narrow remediation | PENDING (0 of 2 cycles used) | Reviewer findings resolved or escalated |
| E — Final Goal 1 decision | PENDING | `JMP_M05_goal_manager_acceptance_v1.md` issued |

---

## 2. Task-plan acceptance integration

`JMP_M05_task_plan_manager_acceptance_v1.md` (verdict: ACCEPTED WITH BINDING
CORRECTIONS) is hereby integrated into this ledger.

Consequences:

1. The commit hold stated in that memo ("Do not commit until the Goal 1
   manager integrates this acceptance into the mission ledger") is released.
   `JMP_M05_task_plan_v1.md`, `JMP_M05_task_plan_manager_acceptance_v1.md`,
   and this ledger may now be committed to `Job_Market_paper` under
   `docs/missions/` as one housekeeping commit. The commit SHA must be
   recorded in §9 when made.
2. The five binding corrections C-1 to C-5 are IN FORCE for every Stage A–E
   artifact (restated in §4).
3. The provenance gap in acceptance §2 (missing `Job_Market_paper` HEAD,
   governance commit SHA, committed governance-file list, worktree status) is
   assigned to Stage A: the approved source-verification prompt's
   repository-provenance section covers all four items.

---

## 3. Roles and appointments

| Role | Assignment | Status |
| --- | --- | --- |
| Principal investigator | Hisham | standing |
| Deputy programme director | ChatGPT JMP project | standing; next contact only at the Stage E return |
| Goal 1 manager | this chat | active |
| JMP-M05 task manager | new dedicated chat "JMP-M05 Task Manager — Inference Design", operating prompt `JMP_M05_task_manager_operating_prompt_v1.md` | APPOINTED 2026-07-30 |
| Source-verification executor | Claude Code, read-only mode, using `JMP_M05_source_verification_prompt_v1.md` verbatim | authorized |
| Design author (Stage B) | separate Opus chat, thinking on, using `JMP_M05_inference_design_prompt_v1.md` plus the accepted source report and corrections C-1–C-5 as appended authoritative inputs | not yet commissioned |
| Independent reviewer (Stage C) | separate chat, distinct from author and task manager, using `JMP_M05_methods_review_prompt_v1.md` | not yet commissioned |

Separation-of-roles rule (hierarchy §5): manager, task manager, author, and
reviewer are four distinct chats. No chat approves its own artifact.

---

## 4. Binding corrections in force (C-1 to C-5)

- **C-1 — Likelihood benchmark.** The `12.25` nats-per-household observation is
  a diagnostic clue only. No artifact may assert continuous-density terms, or
  use the `ln(101)` uniform benchmark as a bound, until the verified likelihood
  composition establishes feasibility of the uniform parameterization, the
  additive structure, absence/presence of density and normalization terms, and
  the sum/mean/weighting convention.
- **C-2 — Scope of the regional test.** The ten-parameter joint test is a test
  of the modeled regional/urbanisation/GSUR access block only — never "no
  opportunity heterogeneity", never the complete opportunity-versus-preference
  test, never a direct test of the decomposition share.
- **C-3 — Cluster terminology.** Household-clustered versus OPG language is
  conditional on the verified primitive contribution structure (task plan V-5).
  No unconditional claims about when clustering becomes non-degenerate.
- **C-4 — Active-bound covariance.** The 35-dimensional conditional covariance
  is a working hypothesis requiring independent methodological review, not an
  accepted decision. No symmetric Wald inference for `beta_l_age2_sm` or
  `beta_l_age2_sf` under the baseline.
- **C-5 — Opportunity-language discipline.** All language must distinguish
  regional/access-block inference, the full opportunity mechanism, and the
  later welfare decomposition.

---

## 5. Open-items register

### 5.1 Source gaps (from task plan §1, mapped to verification tasks)

| Gap | Verification task(s) | Blocking class | Status |
| --- | --- | --- | --- |
| G-A parameter-map / free-vector ordering | V-2 | DESIGN-BLOCKING | PENDING |
| G-B JAX likelihood module and additive composition | V-4 | DESIGN-BLOCKING | PENDING |
| G-C bounds configuration and KKT evidence | V-3 | open (blocking only via HM-KKT) | PENDING |
| G-D weighting and sum/mean convention | V-6 | open, nonblocking for score definition; constrains reporting | PENDING |
| G-E cluster-identifier alignment | V-5, V-7 | DESIGN-BLOCKING | PENDING |
| G-F Phase-4 bundle filenames and bread provenance | V-10 | open (blocking for immutable bread provenance) | PENDING |

Blocking triage rule (task plan §17 step 3): if any of V-2, V-4, V-5, V-7
returns UNKNOWN, the corresponding halt fires and the mission returns to the
deputy programme director. If only V-6, V-8, or V-9 returns UNKNOWN, Stage B
may proceed with the dependent decisions marked open.

### 5.2 Full verification inventory

| Item | Content | Status |
| --- | --- | --- |
| V-1 | Revision reconciliation: confirm `982c5221…` descends from execution revision `fee60723…` with only acceptance memo, execution report, and bundle intervening; record both revisions with labels | PENDING |
| V-2 | 47-vector and 37-free ordered name lists, source path, committed hash | PENDING |
| V-3 | Active-bound identities, bound values and directions, KKT sign check against published gradient (positions 2 and 6, 0-based, provisional until confirmed by name) | PENDING |
| V-4 | Additive likelihood composition, term-by-term, with sign and scaling | PENDING |
| V-5 | Primitive term count; whether household clustering is binding or degenerate (equals household OPG) | PENDING |
| V-6 | Survey-weight status; sum versus mean | PENDING |
| V-7 | `idhh` alignment to loader group order; 1,555 unique, complete; alignment mechanism | PENDING |
| V-8 | Regional covariate definitions; omitted reference category; free positions 15–24 confirmation | PENDING |
| V-9 | Pin values and classification (structural inapplicability / normalization / convention) | PENDING |
| V-10 | Phase-4 bundle inventory, hash recomputation, authoritative bread file, CSV/NPY equality | PENDING |
| V-11 | JAX x64 confirmation, versions, platform | PENDING |
| V-12 | Governance file paths as committed | PENDING |

### 5.3 Manager decisions to be closed in Stages B–E

1. Finite-sample correction (working presumption: two-factor with K = 35;
   pre-registered fallback to cluster-only if V-5/V-6 break the N = G reading).
2. Active-bound treatment (working presumption: conditional 35-interior
   covariance; subject to C-4 review).
3. Score-artifact format.
4. Fixed-pin reporting rule.
5. Regional-block covariance and joint-test protocol.
6. Exact numerical gates and tolerances.

None is closed at ledger opening.

---

## 6. Halt conditions in force

Charter §13 halts, unchanged, plus task-plan §15 additions: HM-REV, HM-MAP,
HM-LL, HM-WGT, HM-CLUS, HM-KKT, HM-X64, HM-SCOPE. Any fired halt is recorded
in §8 and escalated per hierarchy §7 (E2 to deputy programme director unless
resolvable as E0/E1 within the mission).

---

## 7. Delegated-authority boundaries (restated)

This manager may not: change mission scope; change the active baseline; alter
the RURO specification; weaken gates; implement Phase 5; compute inference;
authorize a real execution; start synthetic recovery, welfare, or
decomposition; change canonical governance files. Remediation is capped at two
narrow cycles.

---

## 8. Escalation and remediation log

| # | Date | Class | Description | Resolution |
| --- | --- | --- | --- | --- |
| — | — | — | none recorded | — |

Remediation cycles used: **0 of 2**.

---

## 9. Artifact register

| Artifact | Repository target | Status |
| --- | --- | --- |
| `JMP_M05_task_plan_v1.md` | `docs/missions/` | accepted; commit released (§2), SHA to record |
| `JMP_M05_task_plan_manager_acceptance_v1.md` | `docs/missions/` | commit released (§2), SHA to record |
| `JMP_M05_mission_ledger_v1.md` | `docs/missions/` | this file; created 2026-07-30 |
| `JMP_M05_task_manager_operating_prompt_v1.md` | `docs/missions/` | created 2026-07-30 |
| `FR_P2a_region_live_phase5_source_verification_v1.md` | `docs/France_case/P2a/` | expected from Stage A |
| `phase5_parameter_map_v1.csv` | `docs/France_case/P2a/` | expected from Stage A |
| `phase5_source_inventory_v1.json` | `docs/France_case/P2a/` | expected from Stage A |
| `FR_P2a_region_live_phase5_inference_design_v1.md` | `docs/France_case/P2a/` | expected from Stage B; not committed before review |
| `FR_P2a_region_live_phase5_inference_methods_review_v1.md` | `docs/France_case/P2a/` | expected from Stage C |
| `JMP_M05_goal_manager_acceptance_v1.md` | `docs/missions/` | expected from Stage E |

---

## 10. Next authorized action

Open the task-manager chat with
`JMP_M05_task_manager_operating_prompt_v1.md`, then issue
`JMP_M05_source_verification_prompt_v1.md` verbatim to Claude Code in
read-only mode against working trees containing `Job_Market_paper`, `MNL`,
and the nested `dclaborsupply` at the recorded revisions. No design memo
before the source report is received, checked, and accepted.
