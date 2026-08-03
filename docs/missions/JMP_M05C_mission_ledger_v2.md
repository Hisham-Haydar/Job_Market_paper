# JMP-M05C Mission Ledger v2

**Mission:** JMP-M05C — Minimal Streaming Inference Implementation
**Goal manager:** Goal 1 Manager — Empirical JMP (operating contract v1)
**Supersedes:** ledger v1 (retained)
**Ledger updated:** 2026-08-02
**Target repository path:** `docs/missions/JMP_M05C_mission_ledger_v2.md`

## 1. Binding revisions

| Object | Value |
| --- | --- |
| MNL Increment-A HEAD | `92e299de6313bad0b0421c0db3dd268fdbcfdb59` (implementation base `b5169293…` ← addendum commit ← post-closeout `ffd060f7…`) |
| `Job_Market_paper` | `7195fc50…` (instrument checkpoint still pending untracked-set inventory) |
| Nested = gitlink | `27756a06…` (frozen) |
| Accepted bundles | Phase-3 `2cf23764…864b`; Phase-4 `5484…65f3` (manifest-excluded hash-of-hashes, separate; convention now written out in full in every fresh-session card) |
| Binding design | design v4 + streaming addendum v1 (committed at `b5169293…`); threat model frozen per M05B decision v2 §2 |

## 2. Increment tracker

| Stage | Status |
| --- | --- |
| Increment A — streaming score reducer | **CLOSED** at `92e299de…`: delivered → Review A v1 REJECT (NP-1, DG-1, T16-1, PR-1, ST-1) → E2 → deputy-authorized bounded five-fix refix → Review A v2 **APPROVE** (35/35 gates; both blocking probes re-run; id-recycling re-derivation confirmed; R-34a guard upheld) → seven-file exact-state commit |
| Increment B — covariance and inference objects | **OPEN** (card M05C-AC-7); Review B required before C |
| Increment C — runner, transactions, reproduction | PENDING |
| Final integrated review → exact-state commit → ONE aggregate-only dry run → Goal-1 audit → deputy packet | PENDING |
| Production real run | deputy-reserved |

## 3. Rulings register (M05C)

R-32a digest encoding int64-LE — upheld by review; freeze condition (non-integral-ID rejection) **met** via DG-1 fix. R-32b digest scoped to fixed (encoding, batch size, AD mode) tuple — upheld; freeze at Increment C reproduction gate. R-32c eager x64 activation — upheld under fresh-process probe; binding for the Increment C runner. R-32d test-29 byproduct handling → superseded by the structural conftest guard (R-34a, reviewer-upheld). R-33 Review A v1 REJECT ratified; E2 executed. R-34a–d refix scope rulings incl. detector re-derivation mandate. R-35 Review A v2 accepted; R-35b Review-v1-in-commit entailment (clean-tree requirement). R-36 Increment A closed.

## 4. Standing rules (mission-wide, deputy decision + amendments)

1. All state deletions/moves/cleanups execute inside gated task prompts, verified — never as human pre-steps.
2. Every full-suite command deselects test 29 (structural conftest guard; `MNL_ALLOW_TEST29=1` for isolated-target runs with cleanup contract).
3. Increments B/C only: one implementation-only REJECT with a closed fix list may be converted by the Goal 1 Manager into one bounded refix + fresh review without a deputy round-trip (deputy decision §3 conditions), disclosed in the final packet; a second REJECT for the same increment, or any design/package/architecture issue, is an immediate E2.
4. Reviewer-runnable proofs: exact interpreter/activation command, file-free, read-only, exact expected outputs; evaluator/reducer/covariance-builder/orchestration substitution invalidates a test.
5. Fresh-session cards carry full paths and conventions — no programme shorthand (lesson from the M05C-AC-6 stop; two definitional slips logged against the manager).
6. No row-level score persistence anywhere, ever; no restricted-store reference; addendum §3 lists the only persistable artifacts.

## 5. Incidents log (M05C)

E2 #1: Review A v1 REJECT — resolved by deputy decision (bounded refix). Manager process errors, owned: ST-1 human pre-step (rule 1 adopted); M05C-AC-6 underspecified preflight for a fresh session + wrong attempts-count wording (rule 5 adopted). Implementer self-caught: lazy-x64 false-green (Increment A); id-recycling detector false-green (refix) — both independently re-derived by review.

## 6. Next authorized action

Card M05C-AC-7 — Increment B in the same implementer session; Review B follows under standing rule 3.
