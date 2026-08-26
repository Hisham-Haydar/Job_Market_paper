# JMP-HK-01 Phase-1 register correction — v3 correction note

**Date:** 2026-08-25
**Mode:** read-only correction pass; no Phase-2 action; no fix to source files
**Input:** `JMP_HK_01_phase1_codex_rereview_v1.md` (Codex re-review v1, verdict **NOT-RATIFIABLE**, five FAILs: R1, R2, R3, R5, plus the R5 protected-row defect)
**Controlling standard:** `docs/Missions/JMP_HK_01_authorization_and_PKG01A_crossref_ruling_v1.md` §§3, 4, 8
**Output:** `JMP_HK_01_inventory_and_disposition_register_v3.csv` (9,387 data rows, 24 columns, unchanged shape)

No file was moved, deleted, renamed, archived, or committed in the production of this
correction. Scope is deliberately narrow: **classes are settled and were not touched.**
Only `proposed_action`, `archive_path`, `verification_status`, and (one row) `manifest_ref`
were edited, on exactly the rows the re-review named. `proposed_disposition` is
byte-identical, row-for-row, between v2 and v3 (verified mechanically, not asserted).

## 1. Fix map

| # | Re-review defect | Rows | Field(s) changed | Before → After |
|---|---|---|---|---|
| 1a | R1/R2: protected `CANONICAL_CURRENT` row still instructs `git mv`/archive | 28 | `proposed_action` | `git mv to an archive location; add a supersession-map entry; verify no current exact-path reference remains before commit (ruling s4/s8). Phase 2 only, after deputy ratification.` → `None - protected (CANONICAL_CURRENT)` |
| 1b | R2: `HOLD` rows still instruct `git mv`/archive | 265, 322 | `proposed_action` | same `git mv…` text → `None - HOLD, no action` |
| 1c | R2: protected `CANONICAL_CURRENT` row still instructs `git mv`/archive | 2247 | `proposed_action` | same `git mv…` text → `None - protected (CANONICAL_CURRENT)` |
| 1d | R3: `CANONICAL_CURRENT` ruling row still instructs `git mv`/archive | 2317 | `proposed_action` | same `git mv…` text → `None - protected (CANONICAL_CURRENT)` |
| 1e | R1/R2/R3: `deputy_ratification_required` consistency | 28, 265, 322, 2247, 2317 | — (verified only) | Already convention-consistent in v2 (`No (no action proposed)` for the three `CANONICAL_CURRENT` rows; `N/A (HOLD)` for the two `HOLD` rows) — no edit required; asserted mechanically before write. |
| 2 | R5: protected `CANONICAL_CURRENT` rows still carry populated archive-plan fields + delete instruction | 9170, 9173, 9174 | `archive_path`, `verification_status`, `proposed_action` | `archive_path`/`verification_status`: populated placeholder values → `N/A` / `N/A`; `proposed_action`: `Copy to external dated archive…then delete original…` → `None - protected (CANONICAL_CURRENT)` |
| 3 | R3: the 20 U6-D `HOLD` rows retain the misleading inherited "ruling-protected history" label | 1253, 1258–1276 (20 rows) | `proposed_action` | `None -- ruling-protected history stays in place (s3.2/s4).` → `None - HOLD pending U6 ratification` |
| 4 | R1: `manifest_ref` not set True despite the cited manifest naming the exact path | 28 | `manifest_ref` | `False` → `True` (per `Job_Market_paper/docs/JMP_cross_repo_artifact_manifest_v1.md:75-80`, already cited in the row's `reason`) |

**Explicitly not touched:** `reason` text (not flagged as defective by the re-review — only
`proposed_action`/archive fields/`manifest_ref` were cited); the 333 `HOLD` rows and 125
`HISTORICAL_IMMUTABLE_IN_PLACE` rows that also carry a "ruling-protected history…" style
label — the re-review's R3 critique of that label was scoped explicitly to the 20 U6-D
rows (R4, which governs the 333-row population, **PASSED** with no action-text finding);
any `proposed_disposition` value, anywhere in the register.

## 2. Self-verification table

All checks below compare v2 (input) against v3 (output), 9,387 rows each, run
independently via both a Python full-file diff and raw `grep` on the v3 CSV.

| # | Check | Method | Result |
|---|---|---|---|
| 1 | Row/column count parity (9,387 rows × 24 cols, both files) | Python `csv` diff | **PASS** |
| 2 | `proposed_disposition` class counts identical v2→v3 (937 / 125 / 13 / 48 / 0 / 8,264) | Python `Counter` diff | **PASS** — all six classes unchanged |
| 3 | Only the 28 named physical lines differ v2→v3; only `proposed_action`/`archive_path`/`verification_status`/`manifest_ref` changed on any of them | Python row-for-row diff | **PASS** — changed-line set = exactly `{28,265,322,1253,1258–1276,2247,2317,9170,9173,9174}` |
| 4 | Zero non-HOLD-compatible actions (`git mv`, `archive location`, `Copy to external`, `delete original`, `supersession-map`) remain on any `CANONICAL_CURRENT`/`HISTORICAL_IMMUTABLE_IN_PLACE`/`HOLD` row | Python substring scan, all 9,387 rows | **PASS** — 0 found |
| 5 | `grep -c "git mv to an archive location"` on v3 | grep | **13** — exactly the 13 `ARCHIVE_MOVABLE` rows; 0 on lines 28/265/322/2247/2317 (checked individually) |
| 6 | `grep -c "Copy to external dated archive"` on v3 | grep | **48** — exactly the 48 `ARCHIVE_EXTERNAL_THEN_DELETE_UNTRACKED` rows; 0 on lines 9170/9173/9174 (checked individually) |
| 7 | `archive_path`/`verification_status` populated only outside `N/A` on exactly 48 rows, all `ARCHIVE_EXTERNAL_THEN_DELETE_UNTRACKED` | Python scan, all 9,387 rows | **PASS** — 48 = 48; 9170/9173/9174 confirmed `N/A`/`N/A` |
| 8 | Old U6-D label (`ruling-protected history stays in place`) count on lines 1253/1258–1276 | grep + Python, scoped to the 20 lines | **0** (was 20 in v2) |
| 9 | New U6-D label count register-wide | `grep -c "None - HOLD pending U6 ratification"` | **20** |
| 10 | New protected-`CANONICAL_CURRENT` label count register-wide | `grep -c "None - protected (CANONICAL_CURRENT)"` | **6** (lines 28, 2247, 2317, 9170, 9173, 9174) |
| 11 | New protected-`HOLD` label count register-wide | `grep -c "None - HOLD, no action"` | **2** (lines 265, 322) |
| 12 | Row 28 `manifest_ref` | Python field read | `True` (was `False`) |
| 13 | Out-of-scope populations unchanged: 125 `HISTORICAL_IMMUTABLE_IN_PLACE` label rows (untouched, correctly retained); 353→333 `HOLD` label rows (Δ20 = exactly the U6-D fix, remaining 333 R4-downgrade rows untouched, out of scope) | Python `Counter` by class | **PASS** |
| 14 | `proposed_disposition` column byte-identical, row-for-row, v2 vs v3 | Python list equality over full column | **PASS** |

**Net result: zero non-HOLD-compatible actions remain on any protected row; zero
populated archive fields outside the 48 eligible rows; class counts unchanged from v2
(classes untouched, as instructed).**

## 3. Deliverable SHA-256

| File | SHA-256 |
|---|---|
| `JMP_HK_01_inventory_and_disposition_register_v2.csv` (unchanged input) | `716e718cbc3090a53ea2be8ac981e5f565a7f00897b09253cff522e7e4804022` |
| `JMP_HK_01_inventory_and_disposition_register_v3.csv` (this pass's output) | `30d0999e56e29a6ef513359b0a708512f1780d4b63f76cc22d5aba23a16f2937` |
| `JMP_HK_01_phase1_codex_rereview_v1.md` (input re-review, unchanged) | `d568ffe689ebc6bf3a1ff681e00f4c3a52be9e9cf84313f4d44b818dae12bf39` |

*(This note's own SHA-256 is computed after the file is finalized and reported alongside
it below, not embedded in it, to avoid a self-referential hash — same convention as the
v2 note.)*

## 4. What this pass did NOT do

- Did not touch `proposed_disposition` on any row (verified byte-identical column-wise).
- Did not touch `reason` text on any row — the re-review did not flag `reason` as
  defective; only `proposed_action`/archive-plan fields/`manifest_ref` were cited.
- Did not extend the U6-D label fix beyond the 20 rows the re-review named, and did not
  touch the 333 R4-downgraded `HOLD` rows or the 125 `HISTORICAL_IMMUTABLE_IN_PLACE`
  rows that carry a similarly-worded but *in-scope-correct* label — R4 passed the
  re-review with no action-text finding on that population.
- Moved, deleted, renamed, archived, or committed no file in MNL, Job_Market_paper, or
  EUROMOD-STORAGE. Phase 2 remains unauthorized pending deputy ratification of this v3
  register.
