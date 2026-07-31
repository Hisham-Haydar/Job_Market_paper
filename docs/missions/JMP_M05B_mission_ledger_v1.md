# JMP-M05B Mission Ledger v1

**Mission:** JMP-M05B — Phase-5 Inference Implementation and Certification
**Goal manager:** Goal 1 Manager — Empirical JMP (operating contract v1)
**Charter:** `docs/missions/JMP_M05B_phase5_implementation_mission_charter_v1.md` (deputy-issued; placeholders substituted per delegation item 1)
**Ledger opened:** 2026-07-31
**Target repository path:** `docs/missions/JMP_M05B_mission_ledger_v1.md`
**Ledger status:** Operational file. Not canonical state. Not a decision log.

---

## 1. Binding revisions and dependencies

| Object | Value |
| --- | --- |
| Numerical application anchor (MNL) | `982c52217031158c4a2368709d4a6b211ebcde76` |
| MNL Phase-5 design docs HEAD | `983a2ecf1d16592b9f90085f6a6b690b8a964110` (clean descendant of the anchor; 11 evidence files) |
| `Job_Market_paper` acceptance docs HEAD | `f7cac339d54c4622e2ac0c9b9710070209fc7a6f` |
| Nested `dclaborsupply` HEAD = MNL gitlink | `27756a06ea189339aa82915ed2124628afed20eb` (frozen; package modification is an E2 halt) |
| Phase-3 bundle | `2cf237648743…52f86864b` — rehash verified 2026-07-31 |
| Phase-4 bundle | `5484886985ae…79d9665f3` — rehash verified 2026-07-31 |
| Accepted negLL | `19053.46553160093` |
| Structure | 47 total / 37 free / 35 interior / 10 pins / 2 active **upper** bounds; 1,555 household clusters |
| Authoritative bread | Phase-4 `hessian_free.npy`, loaded and symmetrised per design v4 |
| Binding design set | design **v4** + methods review v1 + recheck v1 + micro-recheck **v2** + deputy acceptance v1 + PI disclosure determination v1 |
| Canonical working root | `C:\Users\hisham\Repo\` on WSS22-CS02; `C:\Users\hisham\MNL` is a data store (EUROMOD-STORAGE), never a commit venue |

## 2. Stage tracker

| Stage | Status | Gate |
| --- | --- | --- |
| M-0B — M05B management checkpoint | OPEN (card M05B-AC-0) | charter with substituted SHAs + delegation prompt + this ledger committed at `Job_Market_paper` |
| I-1 — Implementation | PENDING | charter §4 scope, §7 pure-helper architecture; no likelihood/loader duplication |
| I-2 — Deterministic tests | PENDING | charter §8 sixteen-test floor passes without touching accepted artifacts |
| I-3 — Independent code review (Codex, read-only) | PENDING | `FR_P2a_region_live_phase5_code_review_v1.md`; APPROVE / APPROVE AFTER FIXES / REJECT |
| I-4 — Code remediation | PENDING (0 of 2) | narrow cycles only; REJECT or E2 escalates |
| I-5 — Exact-state commit | PENDING | after review APPROVE; `feat(p2a): implement reviewed Phase-5 inference gate`; clean trees; dry run bound to exact HEADs/hashes |
| I-6 — One full dry run | PENDING | writes only `attempts/dryrun_<timestamp>/`; never creates `complete/`; restricted custody for score bytes; no rerun without manager review |
| I-7 — Dry-run audit + goal-manager acceptance | PENDING | `JMP_M05B_goal_manager_dryrun_acceptance_v1.md`; verdicts READY FOR ONE REAL PHASE-5 EXECUTION / READY AFTER NARROW FIXES / BLOCKED |
| Deputy gate | PENDING | deputy alone authorizes the single production real run |

## 3. Frozen statistical decisions (charter §6; deputy acceptance §3)

Household score = derivative of the verified per-group log-likelihood; `Σ_g s_g = −∇negLL` at `atol=rtol=1e-8`; canonical row order `idhh`-ascending stable argsort; conditional covariance 35×35 with bread `H_II⁻¹` and meat from the 35 selected score columns; correction scalar `1555/1520` with the uncorrected CR0 object available in diagnostics or derivable from stored meat and bread (deputy D-1); literal `NA` for active-bound and pinned coordinates, no symmetric Wald; H0-A confirmatory, H0-B/C/G secondary; regional tests are one access channel, never the complete opportunity mechanism; authoritative score bytes under **restricted custody** (PI determination v1) — never committed or pushed; gates T-1–T-23 incl. certified `κ_BE = 6.0424e-12` upward-rounded; environment logging (python/numpy/scipy/jax/jaxlib/platform/threads) mandatory in every Phase-5 manifest.

## 4. Roles

| Role | Assignment |
| --- | --- |
| Goal manager | this chat (Fable, thinking on) |
| Implementer | Claude Code, Opus (Sonnet fallback), thinking on, high effort, workspace `C:\Users\hisham\Repo` |
| Independent code reviewer | **Codex 5.6, maximum reasoning, read-only** — in-role per hierarchy Level 4; must be distinct from the implementer session |
| Task manager | none appointed — the manager runs the checklist directly (operating contract §3: no subordinate chat without substantive checking value); implementer ≠ reviewer ≠ manager separation preserved |
| Deputy | strategic gate only: dry-run return packet or E2 halt |

## 5. JMP-M05 closure record

Design stage closed 2026-07-31 under deputy acceptance v1: D-1–D-8 frozen; supersessions ratified (incl. S-10 two-tier trigger governing M08/M09 and the X-005 revisit condition); R-15a ratified; E0 closure v4 + micro-recheck v2 `MICRO-RECHECK PASS`; checkpoints `983a2ecf…` (MNL) and `f7cac339…` (JMP). Incidents log: MNL commit-subject malform corrected by same-session amend of the unpushed commit, tree byte-identical (E0; future prompts mandate single-line `git commit -m`); prior-session false negative on bundle existence corrected — bundles tracked in-repo under `outputs/p2a_singles2016/region_live_v1/…`, verified twice; venue facts established (Phase-0 table, WSS22-CS02). Canonical-state note: the deputy pre-specified that the numerical anchor remains `982c5221…` and the new MNL HEAD is a separate documentation checkpoint; updating `JMP_canonical_state_vN` is the deputy's action, recorded here as pending on their side.

## 6. Halt conditions in force

Charter §15 verbatim: source/bundle/revision mismatch; score-identity failure; parameter-order ambiguity; any need to change likelihood/model/specification; any package-modification requirement; T-1–T-23 implementation ambiguity; code-review REJECT; disclosure/custody infeasibility; any attempt to promote `complete/`; unrelated dirty worktree. Plus standing: no production real run; no welfare/decomposition/synthetic recovery/EUROMOD/notebooks/couples/pooled years.

## 7. Next authorized action

Execute card **M05B-AC-0** (management checkpoint), then **M05B-AC-1** (implementation commissioning).
