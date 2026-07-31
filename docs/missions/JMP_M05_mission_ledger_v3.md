# JMP-M05 Mission Ledger v3

**Mission:** JMP-M05 — Household-Clustered Inference
**Goal manager:** Goal 1 Manager — Empirical JMP (operating contract v1)
**Supersedes:** ledger v2 (committed at `dfd65b27…`, historical)
**Ledger updated:** 2026-07-31
**Target repository path:** `docs/missions/JMP_M05_mission_ledger_v3.md`
**Ledger status:** Operational file. Not canonical state. Not a decision log.

---

## 1. Stage tracker — design stage COMPLETE

| Stage | Status | Evidence |
| --- | --- | --- |
| M-0 checkpoint | CLOSED | `1d31d10a…` (ten files) |
| A — Source verification | CLOSED | audit `SOURCE CONTRACT COMPLETE WITH NONBLOCKING GAPS`; completeness `REPORT COMPLETE WITH NONBLOCKING GAPS`; ruling R-1 |
| A′ — Closure checkpoint | CLOSED | `dfd65b271cce9f3fd854d6604c78dc769d4521a5` |
| B — Design memo | CLOSED | design v1 `READY WITH OPEN DECISIONS` (23/23 headings); ruling R-7 |
| C — Independent methods review | CLOSED | `APPROVE AFTER FIXES`, 7 fixes, no E2; ruling R-11 |
| D — Remediation | CLOSED at 2 of 2 | cycle 1 → v2 → recheck `RECHECK FAIL` (1 residual); cycle 2 → v3 → micro-recheck: substantive PASS ×2, overall `MICRO-RECHECK FAIL` on two procedural grounds; rulings R-13–R-15 |
| E — Goal 1 decision | ISSUED | `JMP_M05_goal_manager_acceptance_v1.md`, verdict `READY WITH STRATEGIC OPEN DECISIONS` |
| Deputy strategic gate | OPEN | packet assembled per card M05-AC-9 |

Remediation budget: **2 of 2 used, exhausted.** Post-budget items are deputy dispositions, not goal-manager actions.

---

## 2. Rulings register (complete)

R-1 Stage-A source contract accepted. R-2 findings F-1–F-5 + firmed conditionals ratified as binding verified inputs. R-3 completeness memo filed verbatim at the contract filename. R-4 MNL commits reserved to the deputy (canonical anchor). R-5 JMP-repo docs checkpoints authorized under delegation. R-6 task-manager repository-channel limitation accepted. R-7 design v1 accepted for independent review. R-8 Stage-C routing: non-project ChatGPT reasoning chat (Codex reserved for implementation-stage code review). R-9 interim disclosure safe-harbor: no household-level derived artifact committed or pushed pending the PI determination. R-10 D-7 (`idhh`-ascending) provisionally endorsed. R-11 Stage-C review accepted; seven fixes ratified verbatim; cycle 1 opened. R-12 v2 versioning with §1.1 revision register; v1 retained as review-cited object. R-13 v2 accepted for recheck; three task-plan supersessions ratified (S-10 flagged for deputy). R-14 recheck accepted; residual 1 narrow; cycle 2 opened, route (a) upward-rounded certification. R-15 (a) six version-identity front-matter lines admitted (C-d precedent; commission-wording defect owned by the goal manager), submitted for deputy ratification; (b) §1.1 items classified E0 with reviewer-prescribed text, not executed under delegation per the pre-registered halt; (c) Stage D closed, no cycle 3.

## 3. Errata and supersessions

ERR-1 design-prompt bound direction (lower→**upper**), superseded via Stage-B addendum. ERR-2 heading/verdict contract (prompt's 23 headings govern; task-plan §14 properties as content requirements). Task-plan supersessions ratified through review (R-13): S-10 → two-tier trigger (affects M08/M09 and X-005 trigger — deputy ratification requested); plan §6.2(1)/§6.3 conservatism and referee claims removed; plan §11.1 T-7 tolerance → quantified backward-error bound. Phase-4 execution-report "optional npy" understatement flagged for next MNL documentation pass.

## 4. Decision table for the deputy (freeze requests)

| # | Decision | Recommended baseline | State |
| --- | --- | --- | --- |
| D-1 | Finite-sample correction | two-factor, `N=G=1555`, `K=35` (restricted local dimension), `c = 1555/1520 = 1.0230263157894737`, HC1/CR1-analogue convention | ready to freeze |
| D-2 | Active-bound treatment | conditional 35×35 sandwich; upper-bound coordinates as equality restrictions; literal `NA` + status `active-bound`; no symmetric Wald; two-tier later-method trigger | review-cleared substantively; freeze after §15(3) disposition |
| D-3 | Score artifact | `.npy` authoritative + summaries + non-authoritative `%.17g` CSV; unconditional custody fields + T-23; restricted-custody fallback | freeze after PI disclosure determination (route selection only) |
| D-4 | Fixed-pin reporting | literal `NA`; two structural-inapplicability categories; no normalisation category; mandatory footnote | ready to freeze |
| D-5 | Regional protocol | H0-A 10-df omnibus certified; H0-B/C/G secondary; `E_R` algebra; `p_model`/`p_robust` | ready to freeze |
| D-6 | Gates and tolerances | T-1–T-23 + warning tier; κ_BE certified `6.0424e-12` upward-rounded | ready to freeze after E0 micro-edit |
| D-7 | Canonical row order | `idhh`-ascending stable argsort (= verified loader order) | ratification requested |
| D-8 | K↔covariance linkage | if D-2 → unrestricted 37, then `K = 37` in the same edit | ready to freeze as linked constraint |

Open inputs: deputy disposition of micro-recheck residuals (acceptance memo §15.3); PI disclosure determination (E3, outstanding).

## 5. Artifact register (final, design stage)

Committed — `Job_Market_paper`: M-0 set at `1d31d10a…`; A′ set (`completeness`, `ledger v2`, commit prompt) at `dfd65b27…`.
Untracked by design — `Job_Market_paper`: two superseded v1 prompts; `stageB_author_addendum_v1`; `stageC_reviewer_addendum_v1`; `stageD_cycle1_instruction_v1`; `ledger v3`; `goal_manager_acceptance_v1` (commit authorization requested, §15.4b of the acceptance memo).
Untracked pending deputy — `MNL/docs/France_case/P2a/` (nine files): audit report; parameter map CSV; source inventory JSON; design v1, v2, v3; methods review; recheck; micro-recheck. Plus pending: design v4 + reviewer PASS conversion upon deputy authorization.
`MNL` HEAD unchanged at `982c5221…`; nested `dclaborsupply`/gitlink unchanged at `27756a06…`; both bundles rehash exactly.

## 6. Escalation and remediation log (final)

| # | Class | Item | Resolution |
| --- | --- | --- | --- |
| 1 | Mgmt correction (deputy) | Stage-A correction memo, Defects A–C | v2 prompts; M-0 checkpoint; no budget consumed |
| 2 | E0 | M-0 staging quirks; casing artifact | resolved in-task; normalization queued |
| 3 | E0/E1 | ERR-1, ERR-2 | Stage-B addendum; no halt |
| 4 | E0 | Completeness-memo filename mismatch | hash-verified rename (M05-AC-3a) |
| 5 | E1 | Stage-C seven fixes | cycle 1 (v2) |
| 6 | E1 | Recheck residual 1 (T-7 constant) | cycle 2 (v3), route (a) |
| 7 | E0 + scope ruling | Micro-recheck items: §1.1 annotation typo/wording; front-matter exception | R-15; pre-registered halt honored; deputy disposition requested |

## 7. Next authorized action

Execute card **M05-AC-9**: deliver the final return packet to the ChatGPT deputy programme director (strategic gate). No further goal-manager action on the design artifacts is authorized before the deputy's decisions on acceptance-memo §15.
