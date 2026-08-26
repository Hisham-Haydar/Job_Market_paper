# JMP-HK-01 Phase-1 register micro re-check — Codex v2

**Date:** 2026-08-25  
**Mode:** bounded read-only re-check; no Phase-2 action  
**Subject:** `JMP_HK_01_inventory_and_disposition_register_v3.csv`  
**Comparator:** `JMP_HK_01_inventory_and_disposition_register_v2.csv`  
**Defect authority:** `JMP_HK_01_phase1_codex_rereview_v1.md`  
**Scope:** only the 11 named defect loci, plus v2→v3 row/class and R4-population invariance  
**Overall verdict:** **RATIFIABLE**

## 1. Result

All 11 defects identified by the prior rereview are cured in v3. The eight protected
rows have non-action instructions consistent with their settled classes; the three
R5 rows have been removed from the archive plan at the field level; the 20 U6-D rows
have the corrected HOLD label; and line 28 now has `manifest_ref=True`.

The cure did not alter the settled disposition taxonomy. V2 and v3 each contain
9,387 unique data rows and 24 columns. Every `proposed_disposition` cell is identical,
the class counts are identical, and all 1,986 R4 records are unchanged in every field.

## 2. Eleven-locus re-check

CSV line numbers below are physical lines, with the header at line 1.

| Locus | Required cure | Direct v3 observation | Result |
|---:|---|---|---|
| 1 | Line 28 action made non-actionable | `CANONICAL_CURRENT`; `None - protected (CANONICAL_CURRENT)`; archive fields `N/A` / `N/A` | **PASS** |
| 2 | Line 265 action made non-actionable | `HOLD`; `None - HOLD, no action`; archive fields `N/A` / `N/A` | **PASS** |
| 3 | Line 322 action made non-actionable | `HOLD`; `None - HOLD, no action`; archive fields `N/A` / `N/A` | **PASS** |
| 4 | Line 2247 action made non-actionable | `CANONICAL_CURRENT`; `None - protected (CANONICAL_CURRENT)`; archive fields `N/A` / `N/A` | **PASS** |
| 5 | Line 2317 action made non-actionable | `CANONICAL_CURRENT`; `None - protected (CANONICAL_CURRENT)`; archive fields `N/A` / `N/A` | **PASS** |
| 6 | Line 9170 delete/archive action removed | `CANONICAL_CURRENT`; `None - protected (CANONICAL_CURRENT)` | **PASS** |
| 7 | Line 9173 delete/archive action removed | `CANONICAL_CURRENT`; `None - protected (CANONICAL_CURRENT)` | **PASS** |
| 8 | Line 9174 delete/archive action removed | `CANONICAL_CURRENT`; `None - protected (CANONICAL_CURRENT)` | **PASS** |
| 9 | Lines 9170/9173/9174 removed from archive-plan fields | All three have `archive_path=N/A` and `verification_status=N/A`. Register-wide, the only 48 rows with non-`N/A` archive fields are the 48 `ARCHIVE_EXTERNAL_THEN_DELETE_UNTRACKED` rows. | **PASS** |
| 10 | Correct all 20 U6-D action labels | Lines 1253 and 1258–1276 are all `HOLD` and all read `None - HOLD pending U6 ratification`; the old label occurs zero times on this population. The new exact label occurs exactly 20 times register-wide. | **PASS** |
| 11 | Correct line 28 `manifest_ref` | `False` in v2 → `True` in v3. The cited manifest independently names `MNL/theta_p2a_singles_2016_v2.csv` at `docs/JMP_cross_repo_artifact_manifest_v1.md:75-80`. | **PASS** |

As a register-wide guard on loci 1–8, a case-insensitive scan found zero protected
`CANONICAL_CURRENT`, `HISTORICAL_IMMUTABLE_IN_PLACE`, or `HOLD` rows whose action
contains `git mv`, `archive location`, `Copy to external`, `delete original`, or
`supersession-map`.

## 3. V2→v3 invariance checks

| Check | v2 | v3 | Result |
|---|---:|---:|---|
| Physical lines | 9,388 | 9,388 | **PASS** |
| Parsed data rows | 9,387 | 9,387 | **PASS** |
| Unique `(repo_tree, rel_path)` keys | 9,387 | 9,387 | **PASS** |
| Columns | 24 | 24 | **PASS** |
| `CANONICAL_CURRENT` | 937 | 937 | **PASS** |
| `HISTORICAL_IMMUTABLE_IN_PLACE` | 125 | 125 | **PASS** |
| `ARCHIVE_MOVABLE` | 13 | 13 | **PASS** |
| `ARCHIVE_EXTERNAL_THEN_DELETE_UNTRACKED` | 48 | 48 | **PASS** |
| `DELETE_TRACKED` | 0 | 0 | **PASS** |
| `HOLD` | 8,264 | 8,264 | **PASS** |
| Differing `proposed_disposition` cells | 0 | 0 | **PASS** |

The complete parsed row diff changes exactly 28 physical lines:
`28, 265, 322, 1253, 1258–1276, 2247, 2317, 9170, 9173, 9174`.
Only `proposed_action`, `archive_path`, `verification_status`, and line 28's
`manifest_ref` differ. No other field or row differs.

### R4 population

The R4 population was identified by the v2 R4-correction marker in `reason` and checked
by `(repo_tree, rel_path)` key and then field-by-field:

- v2 population: 1,986 rows;
- v3 population: 1,986 rows;
- membership-key differences: 0;
- records with any field difference: 0; and
- non-`HOLD` records in either population: 0.

Thus both the settled classes and the complete R4 population are untouched.

## 4. File identities

| File | SHA-256 |
|---|---|
| `JMP_HK_01_inventory_and_disposition_register_v2.csv` | `716e718cbc3090a53ea2be8ac981e5f565a7f00897b09253cff522e7e4804022` |
| `JMP_HK_01_inventory_and_disposition_register_v3.csv` | `30d0999e56e29a6ef513359b0a708512f1780d4b63f76cc22d5aba23a16f2937` |

## 5. Verdict

**RATIFIABLE.** Every defect in the expressly bounded 11-locus re-check is cured;
row count, class assignments, class counts, and the 1,986-record R4 population are
unchanged from v2. This verdict does not authorize or perform Phase 2.
