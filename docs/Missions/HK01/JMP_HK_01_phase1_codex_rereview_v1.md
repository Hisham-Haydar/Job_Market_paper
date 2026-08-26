# JMP-HK-01 Phase-1 narrow re-review — Codex v1

**Date:** 2026-08-25  
**Mode:** read-only re-review; one memo; no fix; no Phase-2 action  
**Scope:** strictly R1–R5 of `JMP_HK_01_phase1_codex_review_v1.md`  
**Subjects:** `JMP_HK_01_inventory_and_disposition_register_v2.csv` and `JMP_HK_01_v2_correction_note_v1.md`  
**Controlling standard:** `docs/Missions/JMP_HK_01_authorization_and_PKG01A_crossref_ruling_v1.md` §§3, 4, and 8  
**Overall verdict:** **NOT-RATIFIABLE**

The v2 disposition-class corrections and the R4 re-derivation are mechanically present. The packet is nevertheless not ratifiable because the register did not update `proposed_action` consistently with the corrected classes. Eight protected rows still instruct a future Phase-2 archive or delete operation: lines 28, 265, 322, 2247, 2317, 9170, 9173, and 9174. In addition, the three R5-protected rows at lines 9170, 9173, and 9174 still carry populated `archive_path` and `verification_status` values. Those records contradict the binding rule that HOLD means no action (controlling ruling lines 67–71), that `git mv` is confined to unreferenced material (lines 84–93), and that the protected three be removed from the archive plan.

No source file, register row, action, archive field, or disposition was changed in this re-review.

## 1. Inputs and method

The register SHA-256 is confirmed as `716e718cbc3090a53ea2be8ac981e5f565a7f00897b09253cff522e7e4804022`, matching the supplied `716e718c…` identity and the correction note. The correction note SHA-256 is `fb2be32ce293ba238236f535429662e88e979fb762b819c47942775390a7a657`.

The CSV has 9,388 physical and CSV-parsed lines: one header plus 9,387 unique `(repo_tree, rel_path)` data rows and 24 columns. CSV references below are physical file lines, with the header at line 1.

I reconstructed the correction note's merge baseline independently: 9,209 v1 rows, with the 34 overlapping v1.1 keys replaced, plus 178 v1.1-only rows, produces 9,387 rows. I then compared the baseline and v2 row by row, checked the exact R1–R3 and R5 populations, re-read the cited controlling/source passages, sampled 150 of the 1,986 R4-specific reclassifications to HOLD, and audited the evidentiary shape of every remaining non-HOLD row.

## 2. Verdict summary

| Finding | Verdict | Result |
|---|---|---|
| R1 — pin/manifest protection | **FAIL** | Line 28 is now `CANONICAL_CURRENT`, but its `proposed_action` still instructs `git mv` to archive. |
| R2 — current-reference protection | **FAIL** | All seven class values are safe; HOLD is acceptable for lines 265/322 pending deputy taxonomy follow-up. All seven nevertheless retain their former archive/delete actions. |
| R3 — ruling-protected history and accepted attempts | **FAIL** | The requested class/ref corrections are present, but current ruling line 2317 still instructs `git mv`; the 20 U6-D HOLD rows also retain a misleading “ruling-protected history” action label. |
| R4 — register-wide re-derivation | **PASS** | The 1,986 R4 reclassifications reconcile exactly; a deterministic 150-row sample has zero exceptions; no unsupported non-HOLD class remains on the bounded R4 evidence test. |
| R5 — external-archive completeness | **FAIL** | The 48 eligible rows have the two fields and acceptable plan-time placeholders, but the three protected rows still have archive paths, pending verification entries, and delete instructions. |

## 3. R1 — pin/manifest protection

**Verdict: FAIL — class corrected, protection not coherently implemented.**

Register line 28, `MNL/theta_p2a_singles_2016_v2.csv`, is `CANONICAL_CURRENT`, as requested. The source support is unchanged and sound: `Job_Market_paper/docs/JMP_cross_repo_artifact_manifest_v1.md:75-80` names the exact path, and `docs/JMP_cross_repo_manager_handoff_v1.md:237-240` includes it in the live P2a region-live state.

The same register row still says:

> `git mv to an archive location; add a supersession-map entry; verify no current exact-path reference remains ... Phase 2 only`

That action is incompatible with `CANONICAL_CURRENT` and with the manifest-path override in controlling-ruling lines 84–93. The row simultaneously says `deputy_ratification_required = No (no action proposed)`, making the record internally contradictory. `manifest_ref` also remains `False`; the supporting citation exists only in `reason`. The stale `git mv` instruction is independently sufficient to leave R1 uncured.

## 4. R2 — current-reference protection

**Verdict: FAIL — all seven class calls are acceptable, but all seven action records remain unsafe.**

| Register line | Corrected class | Re-review of class basis | Actual `proposed_action` |
|---:|---|---|---|
| 28 | `CANONICAL_CURRENT` | Exact manifest and live-handoff protection confirmed. | `git mv` to archive |
| 265 | `HOLD` | Exact current-review citation confirmed; source calls the row historical. | `git mv` to archive |
| 322 | `HOLD` | Exact current-review citation confirmed; source calls the row historical. | `git mv` to archive |
| 2247 | `CANONICAL_CURRENT` | Current welfare memo cites the exact path as an active reference. | `git mv` to archive |
| 9170 | `CANONICAL_CURRENT` | Current operational contract cites `alt_results.csv`. | Copy externally, verify, then delete original |
| 9173 | `CANONICAL_CURRENT` | Current operational contract cites `REPORT.md`. | Copy externally, verify, then delete original |
| 9174 | `CANONICAL_CURRENT` | Current operational contract cites `smoke.py`. | Copy externally, verify, then delete original |

The exact source evidence remains decisive:

- `MNL/docs/France_case/P2a/FR_P2a_region_live_plan_reconciliation_report_v1.md:25,28,228-229` cites lines 265/322 and expressly describes them as historical predecessors.
- `MNL/docs/jmp_methodology/JMP_welfare_measurement_decisions_memo_v2.md:5-8,12-26` declares its governing role and cites line 2247's exact path.
- `MNL/docs/reference/euromod_income_concepts_and_disposable_income.md:3,14-18,692-703` declares itself a foundational operational contract and cites the three EUROMOD-STORAGE paths.

**Rows 265/322 ruling:** HOLD is acceptable pending deputy taxonomy follow-up. The current review establishes exact-path protection but calls both artifacts historical; it does not, by that fact alone, establish deputy acceptance or immutable evidentiary-lineage status. `CANONICAL_CURRENT` would contradict the source's historical characterization, while `HISTORICAL_IMMUTABLE_IN_PLACE` requires an acceptance/lineage predicate not resolved in this correction. The binding fail-closed default at controlling-ruling lines 67–71 therefore permits HOLD. It must, however, be **HOLD — NO ACTION**. The retained `git mv` instructions prevent R2 from passing.

## 5. R3 — ruling-protected history and accepted attempts

**Verdict: FAIL — the requested class/ref populations are correct, but one binding ruling remains archive-instructed.**

Positive checks:

- The 20 live, unratified U6-D rows are all `HOLD`: line 1253 and lines 1258–1276. All 20 have blank `immutability_ruling_protection` and `deputy_ratification_required = N/A (HOLD)`. None remains `HISTORICAL_IMMUTABLE_IN_PLACE`.
- The three governing rows are all `CANONICAL_CURRENT`: line 2264 (`JMP_HK_01_authorization_and_PKG01A_crossref_ruling_v1.md`), line 2304 (`JMP_M07_deputy_closeout_and_identity_ruling_v1.md`), and line 2317 (`JMP_M08_goal1_rulings_document_v3.md`). The sources confirm the calls: the controlling ruling defines current live mission inputs at lines 34–37; the M07 ruling declares `Status: Binding` and `Accepted and closed` at lines 3–8; the M08 v3 record carries the current R-87–R-110 appendix at lines 176–188.
- Exactly 52 `MNL/outputs/p2a_singles2016/notebook_dev_v3/` rows exist at register lines 681–717 and 9211–9225. All 52 are `CANONICAL_CURRENT`, all 52 have `ruling_ref=True`, and all 52 are non-actionable. `JMP_M08E_E2_closure_notebook_and_RUM_ruling_v1.md:156-160` authorizes aggregate development output under that exact directory.

The blocker is register line 2317: despite being `CANONICAL_CURRENT`, it retains the old `git mv to an archive location` action and simultaneously says `No (no action proposed)`. This violates the current-material definition at controlling-ruling lines 34–37. Also, all 20 U6-D rows retain the inherited action text `None -- ruling-protected history stays in place (s3.2/s4)`. It is non-destructive, and their operative fields are HOLD/blank, but its “ruling-protected history” label is inconsistent with the required never-immutable-while-unratified treatment.

## 6. R4 — register-wide re-derivation

**Verdict: PASS.**

### Full-population reconciliation

The R4 transitions reproduce the correction note exactly:

| Unsupported baseline class/rationale | Population reclassified to HOLD | Full-population exceptions |
|---|---:|---:|
| `CANONICAL_CURRENT`; unconfirmed “presumed live repository material” only | 1,506 | 0 |
| `HISTORICAL_IMMUTABLE_IN_PLACE`; completion-marker only, excluding the 20 R3 U6-D rows | 333 | 0 |
| `HISTORICAL_IMMUTABLE_IN_PLACE`; archive-location only | 147 | 0 |
| **R4 total** | **1,986** | **0** |

For all 1,986 rows, the baseline reason matches the identified unsupported boilerplate, all seven baseline reference flags are false, v2 is HOLD, the v2 reason carries the R4 correction and preserves the original reason, `immutability_ruling_protection` is blank, both archive-plan fields are `N/A`, deputy ratification is an N/A/HOLD value, and `proposed_action` contains no move/archive/delete instruction.

The separate 20-row `HISTORICAL_IMMUTABLE_IN_PLACE → HOLD` U6-D transition belongs to R3, giving 500 historical-to-HOLD changes overall. The full transition matrix and final class counts also reconcile: 937 current, 125 immutable historical, 13 archive-movable, 48 external-archive/delete, 0 delete-tracked, and 8,264 HOLD, totaling 9,387.

### Deterministic 150-row sample

Within each R4 stratum, candidate rows were ordered by hexadecimal SHA-256 of `v1|<repo_tree>|<rel_path>` and the first quota was selected: 75 presumed-current, 40 marker-only history, and 35 archive-location-only history. Every sampled row passed all eight full-population predicates stated above; zero sample exceptions were found.

- Presumed-current sample (75): 20, 217, 313, 383, 412, 525, 532, 538, 550, 599, 628, 673, 1129, 1335, 1405, 1412, 1428, 1470, 1482, 1502, 1509, 1524, 1553, 1599, 1606, 1654, 1660, 1709, 1710, 1840, 1887, 1909, 2029, 2159, 2168, 2187, 2189, 2197, 2252, 2347, 2371, 2384, 2385, 2401, 2425, 2441, 2444, 2477, 2490, 2493, 2501, 2515, 2516, 2560, 2568, 2598, 2606, 2629, 2636, 2639, 2641, 2678, 2690, 2733, 2739, 2748, 2781, 2807, 2808, 2836, 2846, 2856, 2879, 2947, 2972.
- Marker-only-history sample (40): 734, 793, 794, 801, 869, 874, 875, 885, 886, 890, 905, 920, 922, 932, 941, 945, 955, 963, 977, 980, 983, 987, 992, 993, 1022, 1032, 1033, 1035, 1037, 1043, 1044, 1115, 1188, 1194, 1201, 1206, 1213, 1219, 1221, 1231.
- Archive-location-only-history sample (35): 90, 94, 110, 112, 114, 122, 126, 129, 131, 133, 140, 142, 144, 149, 151, 155, 158, 161, 165, 181, 182, 1572, 1573, 1580, 1742, 1748, 1756, 1760, 1763, 1764, 1765, 1770, 1773, 1778, 1780.

### Remaining non-HOLD support

All 1,123 remaining non-HOLD rows were checked by class:

- 929 of 937 `CANONICAL_CURRENT` rows carry at least one true manifest/pin/pointer/contract/manuscript/review/ruling flag. The eight flag-false exceptions are precisely the source-specific R1–R3 corrections at lines 28, 2247, 2264, 2304, 2317, 9170, 9173, and 9174; their cited source predicates were independently confirmed above.
- All 125 `HISTORICAL_IMMUTABLE_IN_PLACE` rows carry at least one true reference-corpus flag and the protected-history field.
- All 13 `ARCHIVE_MOVABLE` rows are tracked, git-clean, independently uncited members of identified same-directory supersession chains, with deputy ratification required. They are the same remaining movable population already exhaustively cleared of the R1/R2 protected-row defects in the original review.
- All 48 `ARCHIVE_EXTERNAL_THEN_DELETE_UNTRACKED` rows are untracked scratch/staging material with no reference flag, numeric size, and a 64-hex SHA-256. R5 governs the plan-field defect separately.

No unsupported non-HOLD **class** remains on the bounded R4 test. This PASS does not excuse the contradictory `proposed_action` fields identified under R1–R3 and R5.

## 7. R5 — external-archive completeness

**Verdict: FAIL — schema and eligible-row population pass; protected-row removal fails.**

The eligible population is correctly reduced from 51 to 48 `ARCHIVE_EXTERNAL_THEN_DELETE_UNTRACKED` rows: register line 2919 and lines 9135–9169, 9171–9172, and 9175–9184. Every one of the 48 has:

- an `archive_path` of the form `<DEPUTY_DESIGNATED_ARCHIVE_ROOT>/HK01/<repo_tree>/20260825/<rel_path>`;
- `verification_status = PENDING_NOT_YET_ARCHIVED (...)`;
- numeric `size_bytes` and a 64-hex SHA-256; and
- an archive/copy/verify/delete action deferred to Phase 2 and deputy ratification.

The placeholder treatment is acceptable for this Phase-1 plan. The deputy can resolve the external root, and the execution date/status necessarily remain provisional until Phase 2 copies and verifies bytes. Before any deletion, controlling-ruling lines 221–226 still require the manifest to carry the resolved original path, archive path, size, SHA-256, and actual verification status.

The protected rows were **not removed from the archive plan as complete records**:

| Register line | Corrected class | `archive_path` / `verification_status` | `proposed_action` |
|---:|---|---|---|
| 9170 | `CANONICAL_CURRENT` | Still populated | Copy, verify, then delete original |
| 9173 | `CANONICAL_CURRENT` | Still populated | Copy, verify, then delete original |
| 9174 | `CANONICAL_CURRENT` | Still populated | Copy, verify, then delete original |

These are the only three non-external-delete rows with non-`N/A` archive-plan fields. Their presence directly contradicts correction-note lines 24–26 and 119–123, which say the fields are populated only for the 48 remaining external-delete rows and are `N/A` elsewhere. Class membership alone does not safely remove a row from an archive plan when the same row still supplies a destination, a pending verification entry, and an explicit delete instruction.

## 8. Overall disposition

**Overall: NOT-RATIFIABLE.**

R4 passes, and the requested R1–R3 class/ref corrections are materially present. Ratification is blocked by the internally contradictory archive/delete instructions on eight protected rows and, for R5, by the retained archive-plan fields on lines 9170, 9173, and 9174. This is a review verdict only; no fix was made, and Phase 2 remains unauthorized.
