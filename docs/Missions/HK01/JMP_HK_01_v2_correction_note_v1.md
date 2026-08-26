# JMP-HK-01 Phase-1 register correction — v2 correction note

**Date:** 2026-08-25
**Mode:** read-only correction pass; no Phase-2 action; no fix to source files
**Input:** `JMP_HK_01_phase1_codex_review_v1.md` (Codex v1, verdict FAIL — NOT RATIFIABLE FOR PHASE 2)
**Controlling standard:** `docs/Missions/JMP_HK_01_authorization_and_PKG01A_crossref_ruling_v1.md` §3 taxonomy, §4 amendment, §8 untracked-deletion manifest fields
**Output:** `JMP_HK_01_inventory_and_disposition_register_v2.csv` (9,387 data rows, 24 columns)

No file was moved, deleted, renamed, archived, or committed in the production of this
correction. The only artifacts written are this note and the v2 register CSV, both new
files under `docs/Missions/HK01/`. `v1`, `v1_1`, the reference-protection map, and the
inventory summary are unmodified on disk.

## 0. How v2 was built

1. **Merge.** v2 = v1 (9,209 rows) with the 34 `(repo_tree, rel_path)` keys that v1.1
   also touches replaced by their v1.1 version (29 `Data/external/` R-124.3 overrides +
   5 changed-content rows — all already `HOLD` in v1.1, so this step is a pure carry-
   forward of the disclosed, non-silent v1.1 delta), plus the 178 v1.1-only rows
   (new U6-D attempts, new `notebook_dev_v3` files, new `__pycache__`, two new priced
   caches) appended. Result: 9,387 rows, confirmed against the review's own 34-overlap
   count (§6, finding 4). No row was dropped; no v1→v1.1 path was silently reclassified
   beyond what the delta summary already discloses.
2. **Schema extension (R5).** Two columns added: `archive_path`, `verification_status`,
   inserted after `proposed_action`. Populated only for
   `ARCHIVE_EXTERNAL_THEN_DELETE_UNTRACKED` rows.
3. **Five correction passes (R1–R5)** applied on top of the merged register, detailed
   below. Every reclassification also resets `deputy_ratification_required` and
   `immutability_ruling_protection` to the value already conventional for the target
   class elsewhere in the register (verified mechanically, not asserted):
   `CANONICAL_CURRENT` → `No (no action proposed)` / `""`;
   `HOLD` → `N/A (HOLD)` / `""`;
   `HISTORICAL_IMMUTABLE_IN_PLACE` → `No (no action proposed)` / `"Protected (accepted attempt / archived history / ruling-cited)"`;
   `ARCHIVE_MOVABLE` / `ARCHIVE_EXTERNAL_THEN_DELETE_UNTRACKED` → `Yes` / `""`.
4. Every touched row's `reason` field is rewritten to state the correction, cite the
   review section it cures, and (for the two register-wide sweeps) preserve the
   original v1 reason text inline for audit traceability.

File-integrity check: `JMP_HK_01_inventory_and_disposition_register_v2.csv` has 9,388
physical lines (header + 9,387 data rows) and 9,388 CSV-parsed rows — no embedded
physical newlines, same property the review relied on for v1.

## 1. Per-finding fix map

### R1 — pin/manifest protection (review verdict: FAIL)

| Row (v1 line) | Path | Before | After | Basis |
|---|---|---|---|---|
| 28 | `MNL/theta_p2a_singles_2016_v2.csv` | `ARCHIVE_MOVABLE` | `CANONICAL_CURRENT` | Named exact-path by committed `Job_Market_paper/docs/JMP_cross_repo_artifact_manifest_v1.md:75-80` as the provisional region-live theta; hash matches live bytes. Not eligible for archival while manifest-named (ruling §4). |

### R2 — current-reference protection (review verdict: FAIL, 7 rows)

| Row | Path | Before | After | Basis |
|---|---|---|---|---|
| 28 | `theta_p2a_singles_2016_v2.csv` | `ARCHIVE_MOVABLE` | `CANONICAL_CURRENT` | Same row as R1; also audited as current local state by the live manager handoff. |
| 265 | `MNL/docs/France_case/P2a/FR_P2a_region_live_manager_decisions_v1.md` | `ARCHIVE_MOVABLE` | `HOLD` | Cited by the *current* reconciliation report, which itself calls this file historical. See caveat below — HOLD, not `CANONICAL_CURRENT`, because the file is current-reference-*protected* but not itself current material. |
| 322 | `MNL/docs/France_case/P2a/FR_P2a_region_live_production_rebuild_plan_v1.md` | `ARCHIVE_MOVABLE` | `HOLD` | Same reconciliation report; same "historical" characterization. Same caveat as row 265. |
| 2247 | `Job_Market_paper/docs/JMP_literature_positioning_memo_v2.md` | `ARCHIVE_MOVABLE` | `CANONICAL_CURRENT` | Actively cited (line 25) by the currently-governing `JMP_welfare_measurement_decisions_memo_v2.md` (lines 5-8: "decisions govern the JMP welfare scaffolding"). |
| 9170 | `EUROMOD-STORAGE/scratch/staging/de_2017_pricing_smoke/alt_results.csv` | `ARCHIVE_EXTERNAL_THEN_DELETE_UNTRACKED` | `CANONICAL_CURRENT` | Cited by exact line numbers as primary evidentiary source throughout `MNL/docs/reference/euromod_income_concepts_and_disposable_income.md` (§10.4 + in-body cites at :63,:183,:329,:337,:425,:465); that document is a still-current, undated-successor "durable, authoritative reference / operational contract." |
| 9173 | `.../de_2017_pricing_smoke/REPORT.md` | `ARCHIVE_EXTERNAL_THEN_DELETE_UNTRACKED` | `CANONICAL_CURRENT` | Same document, §10.3/§10.4 + :337,:465. |
| 9174 | `.../de_2017_pricing_smoke/smoke.py` | `ARCHIVE_EXTERNAL_THEN_DELETE_UNTRACKED` | `CANONICAL_CURRENT` | Same document, §10.3 + :183,:329. |

**Caveat on rows 265 and 322 (judgment call, flagged for deputy attention):** the
deputy's correction instruction restricted this fix to `CANONICAL_CURRENT` or `HOLD`
only. The taxonomically precise class for these two rows is arguably
`HISTORICAL_IMMUTABLE_IN_PLACE` (ruling-adjacent accepted-history material that a
*current* review cites as the historical predecessor of an accepted decision) — but
that class was not offered as a target for this pass. Rather than assert current-active
status the review's own source text contradicts ("expressly records this file as
historical"), these two rows were defaulted fail-closed to `HOLD`. They remain
current-reference protected (not archivable) either way; a future pass should resolve
them to `HISTORICAL_IMMUTABLE_IN_PLACE` if the deputy agrees.

### R3 — ruling-protected history and accepted attempts (review verdict: FAIL)

| Item | Before | After | Basis |
|---|---|---|---|
| Row 2264, `JMP_HK_01_authorization_and_PKG01A_crossref_ruling_v1.md` | `HOLD` | `CANONICAL_CURRENT` | Live mission input authorizing HK01 itself and supplying this register's own binding taxonomy. |
| Row 2304, `JMP_M07_deputy_closeout_and_identity_ruling_v1.md` | `HOLD` | `CANONICAL_CURRENT` | `Status: Binding`, cited by current manuscript/contract surfaces; a presently-binding ruling is live governing material, not unresolved. |
| Row 2317, `JMP_M08_goal1_rulings_document_v3.md` | `ARCHIVE_MOVABLE` | `CANONICAL_CURRENT` | v3 appendix is the current consolidated governance record (R-87–R-110); a live rulings record is `CANONICAL_CURRENT` irrespective of another version being separately cited (review §5, stated directly). |
| 20 live U6-D rows (row 1253 `u6dpilot_U6D_PILOT_DONE`; rows 1258-1276, 19 files under `u6dgates3_U6D_GATES_DONE`) | `HISTORICAL_IMMUTABLE_IN_PLACE` | `HOLD` | A completion-marker directory name is not deputy acceptance; live/unratified U6-D evidence may never be `HISTORICAL_IMMUTABLE_IN_PLACE` pending deputy ratification / U6-E review — matches the v1.1 delta's own treatment of `u6dgates7`/`u6dgates4xb`/`u6dxc4xb`. |
| 52 `notebook_dev_v3` ruling-authorized outputs (37 v1 rows 681-717 + 15 v1.1 rows, merged) | `HOLD`, `ruling_ref=False` | `CANONICAL_CURRENT`, `ruling_ref=True` | `JMP_M08E_E2_closure_notebook_and_RUM_ruling_v1.md:156-160` authorizes this exact directory for aggregate development outputs; directory-level ruling citation propagated to file level per the requested standard (no content-specific violation established). Matched by path-prefix so the fix automatically covers both the 37 original and 15 newly-merged files. |

### R4 — disposition-class correctness (review verdict: FAIL; register-wide re-derivation)

The review's sample findings were re-derived against the **full register**, not just the
259-row sample, by mechanically testing the same evidentiary signal the review used
(the row's own `reason` text plus its seven reference-corpus boolean columns), and
defaulting fail-closed to `HOLD` wherever no independent pin/manifest/pointer/current-
document/ruling support exists:

| Class of unsupported row | Test applied | Register-wide population | Overlap already fixed by R3 | Net reclassified here | Before → After |
|---|---:|---:|---:|---:|---|
| Unsupported current-class presumption | `proposed_disposition==CANONICAL_CURRENT` and `reason` contains the unconfirmed-presumption boilerplate | 1,534 (v1) | 28 already converted to `HOLD` by the v1.1 `Data/external` R-124.3 merge (§0 step 1) | **1,506** | `CANONICAL_CURRENT` → `HOLD` |
| Unsupported immutable-history: marker-only | `proposed_disposition==HISTORICAL_IMMUTABLE_IN_PLACE` and `reason` is exactly "attempt directory name carries an accepted/completion status marker" with no citation clause | 353 | 20 (the live U6-D rows, already fixed under R3 with more specific reasoning) | **333** | `HISTORICAL_IMMUTABLE_IN_PLACE` → `HOLD` |
| Unsupported immutable-history: archive-location-only | `proposed_disposition==HISTORICAL_IMMUTABLE_IN_PLACE` and `reason` is exactly "already resides in an archive/superseded-history path" with no citation clause | 147 | 0 | **147** | `HISTORICAL_IMMUTABLE_IN_PLACE` → `HOLD` |

Historical rows whose `reason` *does* carry independent citation support (the
`['manifest', 'pin-hash', 'review-citation']`-style variants — 125 rows register-wide:
35+31+28+19+4+4+3+1) were left as `HISTORICAL_IMMUTABLE_IN_PLACE`; they were not part
of the review's "unsupported" finding and were re-verified to still carry a `True`
reference-corpus flag.

No silent v1→v1.1 conversion was found (review §6 finding 4, re-confirmed): all 34
overlapping keys resolve to disclosed, explicit changes (29 `Data/external` R-124.3
overrides, 5 content-hash deltas), all already recorded in the v1.1 delta summary.

### R5 — external-archive completeness (review verdict: FAIL)

1. **Reference-protected rows removed from archival.** Rows 9170, 9173, 9174 are no
   longer `ARCHIVE_EXTERNAL_THEN_DELETE_UNTRACKED` (reclassified `CANONICAL_CURRENT`
   under R2 above), so they are mechanically excluded from the archive plan. 48 of the
   original 51 external-delete rows remain in that class.
2. **Manifest fields added.** Two new register columns satisfy ruling §8's mandatory
   untracked-deletion manifest fields (original path = existing `abs_path`/`rel_path`;
   size = existing `size_bytes`; SHA-256 = existing `sha256_or_flag`):
   - `archive_path` = `<DEPUTY_DESIGNATED_ARCHIVE_ROOT>/HK01/<repo_tree>/<YYYYMMDD>/<rel_path>`,
     populated for all 48 remaining `ARCHIVE_EXTERNAL_THEN_DELETE_UNTRACKED` rows using
     the collision-resistant scheme the review already validated as coherent (§7); `N/A`
     elsewhere.
   - `verification_status` = `PENDING_NOT_YET_ARCHIVED (Phase 1/plan-time; no bytes
     copied or verified; archive_root and date are placeholders for deputy resolution
     and Phase-2 execution-time stamping)` for the same 48 rows; `N/A` elsewhere.

   **Open item for the deputy:** `<DEPUTY_DESIGNATED_ARCHIVE_ROOT>` and the `20260825`
   date stamp are still placeholders — this pass adds the *columns* the ruling requires
   but cannot itself designate a concrete external archive root (that is a deputy
   decision, and Phase 1/this correction pass remains read-only/no-execution). Do not
   treat these 48 `archive_path` values as final; they must be re-stamped with the real
   root and execution date at actual Phase-2 archive time, and `verification_status`
   must be flipped to a real verified/failed value only after bytes are copied and
   compared.

## 2. New class counts

| Disposition class | v1 (9,209) | v2 post-merge, pre-correction (9,387) | **v2 final (9,387)** | Δ vs v1 | Δ vs post-merge |
|---|---:|---:|---:|---:|---:|
| CANONICAL_CURRENT | 2,412 | 2,383 | **937** | −1,475 | −1,446 |
| HISTORICAL_IMMUTABLE_IN_PLACE | 625 | 625 | **125** | −500 | −500 |
| ARCHIVE_MOVABLE | 18 | 18 | **13** | −5 | −5 |
| ARCHIVE_EXTERNAL_THEN_DELETE_UNTRACKED | 51 | 51 | **48** | −3 | −3 |
| DELETE_TRACKED | 0 | 0 | **0** | 0 | 0 |
| HOLD | 6,103 | 6,310 | **8,264** | +2,161 | +1,954 |
| **Total** | 9,209 | 9,387 | **9,387** | +178 (v1.1 merge) | — |

Sum check: 937 + 125 + 13 + 48 + 8,264 = 9,387. ✓

The net movement is overwhelmingly conservative-direction (HOLD grows by 2,161 net,
absorbing the unsupported-presumption sweep), consistent with the review's fail-closed
instruction; the register-wide re-derivation (R4) accounts for the large majority of
that movement (1,506 + 333 + 147 = 1,986 of the 2,161), the R3 U6-D correction accounts
for 20, and the remaining rows come from the disclosed v1.1 `Data/external` merge (29)
and small movements elsewhere. Movement toward `CANONICAL_CURRENT` (60 rows: row 28 [R1+R2] + rows 2247, 9170, 9173,
9174 [R2] + rows 2264, 2304, 2317 [R3] + 52 `notebook_dev_v3` outputs [R3]) is fully
cited to a specific current manifest, contract, review, or ruling line reference — none
is a bare presumption.

## 3. Deliverable SHA-256

| File | SHA-256 |
|---|---|
| `JMP_HK_01_inventory_and_disposition_register_v2.csv` | `716e718cbc3090a53ea2be8ac981e5f565a7f00897b09253cff522e7e4804022` |
| `JMP_HK_01_inventory_and_disposition_register_v1.csv` (unchanged input, for reference) | `f96877582190c57ec672a02c68b7b10b56bddc00dbd341396d0372033556e97d` |
| `JMP_HK_01_inventory_and_disposition_register_v1_1.csv` (unchanged input, for reference) | `b45b38315a86cbcfc985864443cfae4639d4558212efea1d4752583076a7a883` |

(This note's own SHA-256 is necessarily computed after this file is finalized and is
reported alongside it, not embedded in it, to avoid a self-referential hash.)

## 4. What this pass did NOT do

- Did not re-run the reference-protection-map harvest, the 76-pin SHA-256 recheck, or
  the exhaustive current-document exact-string scan — it applied the review's own
  independently-verified findings (spot-checked above against the source documents,
  e.g. the `euromod_income_concepts_and_disposable_income.md` citations for rows
  9170/9173/9174) rather than re-deriving them from scratch.
- Did not resolve `resolved_repo=?` in the reference-protection map itself (map file
  untouched, as instructed) or propagate the `notebook_dev_v3` directory-citation
  `resolved_repo=MNL` fix into that map — only the register's file-level `ruling_ref`
  and disposition were corrected, per the requested register-only scope.
- Did not decide the delta summary's four self-flagged governance gaps beyond what the
  review already ruled non-problematic (item 4, EUROMOD-STORAGE scope) or what R1-R5
  required (items 2 and 3, cured above). Item 1 (R-124.3 directive provenance) and item
  5 (`IGNORED` git-status vocabulary standardization) remain open deputy decisions, not
  register defects — consistent with the review's own disposition of them.
- Moved, deleted, renamed, archived, or committed no file in MNL, Job_Market_paper, or
  EUROMOD-STORAGE. Phase 2 remains unauthorized pending deputy ratification of this v2
  register and the ruling §7 Phase-2 timing gates (U6-E review, U6 results/evidence
  commit, no active review/runner on affected paths).
