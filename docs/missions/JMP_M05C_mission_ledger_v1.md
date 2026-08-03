# JMP-M05C Mission Ledger v1

**Mission:** JMP-M05C — Minimal Streaming Inference Implementation
**Goal manager:** Goal 1 Manager — Empirical JMP (operating contract v1)
**Charter:** `JMP_M05C_minimal_streaming_implementation_mission_charter_v1.md` (deputy-issued, binding)
**Binding design:** design v4 (unchanged statistical target) + `JMP_M05C_streaming_inference_design_addendum_v1.md` (deputy-issued; precedence per its §11)
**Ledger opened:** 2026-08-02
**Target repository path:** `docs/missions/JMP_M05C_mission_ledger_v1.md`

## 1. Binding revisions and dependencies

| Object | Value |
| --- | --- |
| MNL starting base | `ffd060f7a0f4535150498aae6361a3df35cf8b53` (post M05B archive/evidence/test-42 salvage; addendum commit to be recorded at Increment A pre-step) |
| `Job_Market_paper` | `7195fc50f6a73e20bdf62fc4baae48c18dedd345` (instrument checkpoint pending inventory) |
| Nested `dclaborsupply` = gitlink | `27756a06ea189339aa82915ed2124628afed20eb` (frozen; modification = E2) |
| Accepted bundles | Phase-3 `2cf23764…864b`; Phase-4 `5484…65f3` (canonical separate-hash convention; re-verify at every preflight) |
| Statistical target | UNCHANGED from design v4 + deputy acceptance D-1–D-8: conditional-35 estimand, meat/bread, `c = 1555/1520`, NA reporting, regional protocol, gate formulas |
| Streaming contract | addendum §§2–9: bounded-batch scoring, streaming 37×37 and 35×35 meat accumulation, canonical score-stream digest, **no row-level score persistence anywhere, ever**, aggregate-only artifacts, fresh-process reproduction, no restricted score store |
| Threat model | frozen per M05B deputy decision v2 §2 (carried forward) |
| M05B closure | closed without implementation acceptance; evidence commit `73d447b6…`; test-42 salvage `ffd060f7…`; archive manifest `7f899416…`; full lessons register in the M05B ledger and pause decision v1 |

## 2. Increment tracker

| Stage | Status | Budget |
| --- | --- | --- |
| Pre-step — addendum commit (MNL) + starting-revision record | OPEN (card M05C-AC-1) | — |
| Increment A — streaming score reducer | OPEN (card M05C-AC-1) | review A + max 1 narrow remediation; REJECT = E2 |
| Review A (fresh Codex, read-only) | PENDING | binary consequence per charter §6 |
| Increment B — covariance and inference objects | PENDING (blocked on A approval) | review B + max 1 |
| Increment C — runner, transactions, reproduction | PENDING (blocked on B approval) | review C + max 1 |
| Final integrated review | PENDING | must return APPROVE before commit or dry run |
| Exact-state commit + ONE aggregate-only full dry run + Goal-1 audit | PENDING | deputy packet follows |
| Production real run | deputy-reserved | — |

## 3. Roles

Manager: this chat (Fable). Implementer: **fresh Claude Code Opus session, never exposed to the rejected M05B implementation** (thinking on, high effort, workspace `C:\Users\hisham\Repo`). Reviewer: fresh read-only Codex session per increment, maximum reasoning. Deputy: final packet or E2 only.

## 4. Standing rules

Reviewer-runnable proof rule (charter §5) verbatim in every increment card: production-path tests, bounded deterministic fixtures, exact command lines, expected outputs, failure tests; replacing the production evaluator, score reducer, covariance builder, or runner orchestration under review invalidates the test. Package boundary import-only (§7). Non-scope (§10): no restricted store use or reference; no household-level score persistence; no welfare/decomposition/synthetic recovery; no couples/pooled years. Halts per charter §11. Retention/replication questions from M05B: likely moot under aggregate-only design; final packet states disposition.

## 5. Next authorized action

Card M05C-AC-1: pre-step addendum commit, then Increment A in the fresh implementer session.
