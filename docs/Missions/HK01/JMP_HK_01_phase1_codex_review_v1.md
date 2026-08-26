# JMP-HK-01 Phase-1 bounded independent review — Codex v1

**Date:** 2026-08-24  
**Mode:** read-only review; no Phase-2 action; no fix  
**Controlling standard:** `docs/Missions/JMP_HK_01_authorization_and_PKG01A_crossref_ruling_v1.md` §3 taxonomy and §4 amendment  
**Overall verdict:** **FAIL — NOT RATIFIABLE FOR PHASE 2**

The five requested items all fail. The principal blockers are one actionable row named by a committed manifest; seven actionable rows exact-path cited by current contracts/reviews; live or binding ruling material and live U6-D rows in the wrong classes; non-HOLD classes supported only by presumptions/path-name heuristics in the disposition sample; and an external-archive plan that omits two mandatory §8 manifest fields. No file was moved, deleted, renamed, archived, or fixed in this review.

## 1. Scope and method

Reviewed the five packet deliverables:

1. `JMP_HK_01_inventory_and_disposition_register_v1.csv` — 9,209 data rows;
2. `JMP_HK_01_inventory_summary_v1.md`;
3. `JMP_HK_01_reference_protection_map_v1.csv` — 8,616 data rows;
4. `JMP_HK_01_inventory_and_disposition_register_v1_1.csv` — 212 data rows;
5. `JMP_HK_01_delta_summary_v1.md`.

The CSVs contain no embedded physical newlines, so cited CSV row numbers below are also physical file-line numbers (header = line 1).

Independent checks performed:

- enumerated tracked manifest- and pointer-named sources from each repository with `git ls-files`, rather than trusting the register flags;
- loaded both live pin registries, `MNL/scripts/m08e/m08e_pins.py` and `MNL/scripts/welfare/m08_u6_pins_v2.py`, and joined their normalized repo/path/hash tuples to the actionable rows;
- recomputed SHA-256 for all 76 pin entries (52 M08E and 24 U6), not merely a sample;
- searched every tracked textual file in both repositories for the relative path, absolute path, slash-normalized variants, basename, and registered SHA-256 of each of the 69 actionable v1 rows; HK01 packet files were excluded from this reference search;
- reconstructed attempt units from every `/attempts/<attempt-id>/` path in both registers;
- used a deterministic 259-row disposition sample described in §5;
- checked all 51 external-archive rows for uniqueness, path safety, existence, size, SHA-256, action text, and §8 manifest fields.

The binding ruling defines current material at lines 34-37, immutable history at lines 39-43, the prerequisites for `ARCHIVE_MOVABLE` at lines 45-53, and the fail-closed HOLD default at lines 67-71. Section 4 says exact current references and accepted/ruling-protected history override supersession (lines 73-95). Section 8 requires an untracked-deletion manifest to record original path, archive path, size, SHA-256, and verification status (lines 221-225).

## 2. Verdict summary

| Item | Verdict | Decisive result |
|---|---|---|
| R1 pin/manifest protection | **FAIL** | v1 row 28 proposes `ARCHIVE_MOVABLE` for `theta_p2a_singles_2016_v2.csv`, but the committed cross-repo artifact manifest names that exact path. |
| R2 current-reference protection | **FAIL** | Seven actionable rows are exact-path cited by documents whose text establishes current contract/review status. |
| R3 ruling-protected history | **FAIL** | Twenty live U6-D rows are incorrectly immutable; three live/binding ruling records and 52 ruling-authorized notebook-output rows are not in either permitted R3 class. |
| R4 disposition-class correctness | **FAIL** | The 259-row sample contains protected actionable rows and widespread unsupported non-HOLD classifications; no silent v1→v1.1 conversion was found. |
| R5 external-archive completeness | **FAIL** | The row-level path scheme is coherent, but three rows are current-reference protected and the plan omits archive path and verification status from the required manifest record. |

## 3. R1 — pin/manifest protection

**Verdict: FAIL.**

### Pin and pointer results

The two registries contain 76 entries. The M08E registry declares its expected-path/hash block at `MNL/scripts/m08e/m08e_pins.py:139`; the U6 registry declares repo/path/hash/authority/provenance at `MNL/scripts/welfare/m08_u6_pins_v2.py:106-109`. All 76 files exist and all 76 recomputed SHA-256 values match. Their v1 classes are 52 `CANONICAL_CURRENT` and 24 `HISTORICAL_IMMUTABLE_IN_PLACE`; none is actionable. Representative checks include the frozen geometry pin (`m08e_pins.py:141-146`), the U6 governing handoff (`m08_u6_pins_v2.py:112-117`), and both superseded immutable U6 sidecars (`m08_u6_pins_v2.py:237-254`).

The independent join against the two tracked accepted-pointer files found no actionable match.

### Committed-manifest blocker

The join against 174 tracked manifest-named sources found one actionable match:

- v1 row/line **28**, MNL `theta_p2a_singles_2016_v2.csv`, is `ARCHIVE_MOVABLE` and has every protection flag `False`. Its reason says the row is unreferenced. However, committed `Job_Market_paper/docs/JMP_cross_repo_artifact_manifest_v1.md:75-80` names this exact path and records it as the provisional region-live theta. The manifest itself is tracked at commit `81302c9b066b82451a2b1b460fff1ac8ff0cba82`. The row's recorded hash, `9c8d7ee7f4ee5b1bd4ae3edd2970dd96fe348c242cc4b6bdcd15de82fc1ba981`, also matches the live file byte-for-byte.

The manifest status need not be “canonical” to trigger §3/§4 protection: `ARCHIVE_MOVABLE` requires that the row not be referenced by a current manifest. Row 28 therefore cannot be ratified as actionable.

## 4. R2 — current-reference protection

**Verdict: FAIL.**

The exhaustive exact-string scan produced 31 source/action matches. After restricting the result to the requested current contracts, manuscript maps, and live review/ruling documents, seven actionable rows remain protected:

| v1 row | Proposed class | Exact current reference | Why current/protective |
|---:|---|---|---|
| 28 | `ARCHIVE_MOVABLE` | `Job_Market_paper/docs/JMP_cross_repo_manager_handoff_v1.md:239` | The protection map itself calls this a `contract` at map row 129, but leaves `resolved_repo=?`; the live handoff audits the current local state at lines 20-23. |
| 265 | `ARCHIVE_MOVABLE` | `MNL/docs/France_case/P2a/FR_P2a_region_live_plan_reconciliation_report_v1.md:28,228` | Current reconciliation review; it expressly records this manager-decision file as historical. The protection map records the citation at row 5677 but leaves it unresolved. |
| 322 | `ARCHIVE_MOVABLE` | `MNL/docs/France_case/P2a/FR_P2a_region_live_plan_reconciliation_report_v1.md:25,229` | Same current review; it expressly records the v1 rebuild plan as historical. The protection map records the citation at row 5679 but leaves it unresolved. |
| 2247 | `ARCHIVE_MOVABLE` | `MNL/docs/jmp_methodology/JMP_welfare_measurement_decisions_memo_v2.md:12-26` | The memo says at lines 5-8 that its decisions govern the JMP welfare scaffolding; line 25 cites the exact path `docs/JMP_literature_positioning_memo_v2.md`. |
| 9170 | `ARCHIVE_EXTERNAL_THEN_DELETE_UNTRACKED` | `MNL/docs/reference/euromod_income_concepts_and_disposable_income.md:703` | This document declares itself a foundational “operational contract” at line 3 and durable authoritative reference at lines 14-18. |
| 9173 | `ARCHIVE_EXTERNAL_THEN_DELETE_UNTRACKED` | same document, line 694 | Same current operational-contract protection. |
| 9174 | `ARCHIVE_EXTERNAL_THEN_DELETE_UNTRACKED` | same document, line 692 | Same current operational-contract protection. |

Rows 9170, 9173, and 9174 are respectively `scratch/staging/de_2017_pricing_smoke/alt_results.csv`, `REPORT.md`, and `smoke.py`. The protection map already contains the three path citations from both the DCLS gitlink and standalone copies at map rows 16-18 and 34-36, but `resolved_repo=?` prevented propagation to the v1 action rows. The independent MNL grep confirms that the current MNL operational contract also contains them.

The remaining exact-string hits were in prompts, successor reports, an older execution report, code/configuration, or documents without demonstrated current contract/manuscript/live-review status; they were not used to enlarge this bounded R2 finding.

## 5. R3 — ruling-protected history and accepted attempts

**Verdict: FAIL.**

### Attempt-directory population

The v1 register contains 181 distinct attempt units. The inventory's completion-name rule identifies 148 units; every one is mechanically in `CANONICAL_CURRENT` or `HISTORICAL_IMMUTABLE_IN_PLACE`. That mechanical result does not cure the following acceptance error: a completion marker is not itself deputy acceptance.

The delta summary correctly self-flags two live U6-D directories as not yet accepted (`JMP_HK_01_delta_summary_v1.md:179-194`), but v1 assigns all 20 contained rows to `HISTORICAL_IMMUTABLE_IN_PLACE` solely from their directory names:

- v1 row **1253**: `.../20260824T083919Z_..._u6dpilot_U6D_PILOT_DONE/u6d_pilot_v1.json`;
- v1 rows **1258-1276**: all 19 files under `.../20260824T121651Z_..._u6dgates3_U6D_GATES_DONE/`.

Those rows must remain non-actionable live U6-D material pending ratification/review; the v1.1 treatment is the correct precedent. All ten new v1.1 attempt units, including the three new `*_DONE` units, are HOLD.

Across the full v1 historical class, 353 rows rely only on a completion-like directory marker and have no recorded pin/manifest/pointer/current-document/ruling support. Their accepted status is therefore not independently established by the register. This is also an R4 evidence-quality failure.

### Ruling records and ruling-authorized output

The following R3 classes are wrong independently of the U6-D issue:

- v1 row **2264**, the controlling `JMP_HK_01_authorization_and_PKG01A_crossref_ruling_v1.md`, is HOLD. It is the live mission input that authorizes HK01 at its lines 12-16 and supplies the binding taxonomy at lines 30-71; it is `CANONICAL_CURRENT` under §3.
- v1 row **2304**, `JMP_M07_deputy_closeout_and_identity_ruling_v1.md`, is HOLD even though the document declares `Status: Binding` and `M07 disposition: Accepted and closed` at lines 3-8 and is cited by current manuscript/contract surfaces. It must be canonical current or immutable history, not unresolved HOLD.
- v1 row **2317**, tracked `JMP_M08_goal1_rulings_document_v3.md`, is `ARCHIVE_MOVABLE`. Its v3 appendix is the current consolidated governance record carrying R-87 through R-110 (`JMP_M08_goal1_rulings_document_v3.md:176-188`). A live rulings record is `CANONICAL_CURRENT`, irrespective of whether another version is cited.
- `JMP_M08E_E2_closure_notebook_and_RUM_ruling_v1.md:156-160` authorizes aggregate development outputs only under `outputs/p2a_singles2016/notebook_dev_v3/`. Nevertheless, all 37 v1 rows **681-717** and all 15 new v1.1 rows **3-17** are HOLD with `ruling_ref=False`. Under the requested R3 standard, these 52 live ruling-authorized output artifacts are `CANONICAL_CURRENT` unless a content-specific violation is established; the directory citation cannot simply be dropped at file level.

The positive population checks are: all 11 v1 rows with `ruling_ref=True` are `CANONICAL_CURRENT`; all 625 rows labelled as accepted/protected history are non-actionable; and all 76 pin entries are in one of the two permitted R3 classes. The 26 raw-microdata HOLD rows were not treated as “ruling-protected history”: their field records §8 deletion prohibition, not an acceptance or immutable-lineage ruling.

## 6. R4 — disposition-class correctness sample

**Verdict: FAIL.**

### Reproducible sample

For each stratum, rows were ordered by the hexadecimal SHA-256 of
`<register filename>|<repo_tree>|<rel_path>` and the first requested number was selected. All actionable rows were selected, not sampled. Total reviewed: **259 rows**.

| Register / class | Reviewed | Population |
|---|---:|---:|
| v1 `CANONICAL_CURRENT` | 50 | 2,412 |
| v1 `HISTORICAL_IMMUTABLE_IN_PLACE` | 50 | 625 |
| v1 `ARCHIVE_MOVABLE` | 18 (all) | 18 |
| v1 `ARCHIVE_EXTERNAL_THEN_DELETE_UNTRACKED` | 51 (all) | 51 |
| v1 HOLD | 40 | 6,103 |
| v1.1 HOLD | 50 | 212 |
| **Total** | **259** | |

There are no `DELETE_TRACKED` rows to sample.

### Findings in the sample

1. **Unsupported current-class presumption.** Thirty of the 50 sampled canonical rows use the identical reason “presumed live repository material” while explicitly conceding that no pin/manifest/contract/manuscript citation independently confirms the call. Examples are v1 rows 82, 648, 1485, and 1707. Section 3 does not authorize a blanket tracked-and-clean presumption, and §5 says current governance/acceptance records—not version or repository presence alone—must decide canonical status. Across the full v1 register, 1,534 of 2,412 canonical rows use this unconfirmed-presumption reason. These rows are unsupported and default to HOLD unless their current role is established.

2. **Unsupported immutable-history heuristics.** Of the 50 sampled historical rows, 29 rely only on a completion-like attempt-directory name and 12 rely only on already being under an archive/superseded path. Representative rows are 874 (marker only) and 91 (archive location only). A name or resting location is not by itself an acceptance record, immutable ruling, or accepted lineage. Only nine sampled historical rows also carry pin/manifest/review support. The live U6-D sample rows 1253, 1269, and 1271 demonstrate the concrete false-positive consequence.

3. **Actionable-class errors.** All 18 movable rows and all 51 external-delete rows were reviewed. Movable rows 28, 265, 322, 2247, and 2317 fail current-reference/current-governance requirements. External-delete rows 9170, 9173, and 9174 fail current-reference protection. The remaining actionable rows satisfy the basic tracked/untracked shape test, but R5 separately blocks the external plan.

4. **HOLD discipline and conversions.** Every sampled HOLD row has a no-action proposal. Comparing the two registers by `(repo_tree, rel_path)` yields 34 overlapping paths: five HOLD→HOLD content deltas and 29 `CANONICAL_CURRENT`→HOLD conversions for `MNL/Data/external/`. All 29 conversions are explicitly disclosed in the delta summary at lines 155-178 and in v1.1 rows 185-213. No silent conversion was found.

### Sample row record

- v1 canonical: 82, 243, 355, 453, 493, 495, 648, 1358, 1390, 1436, 1453, 1485, 1540, 1625, 1707, 1709, 1718, 1731, 1739, 1818, 1833, 1837, 1839, 2008, 2076, 2082, 2185, 2196, 2223, 2313, 2331, 2349, 2389, 2430, 2465, 2568, 2636, 2640, 2682, 2697, 2710, 2724, 2726, 2874, 7198, 7201, 7295, 7362, 7364, 7376.
- v1 historical: 91, 111, 126, 137, 150, 171, 179, 747, 757, 803, 810, 820, 828, 874, 876, 892, 901, 907, 912, 927, 939, 948, 962, 975, 985, 1011, 1026, 1034, 1084, 1104, 1113, 1145, 1160, 1163, 1165, 1186, 1201, 1204, 1217, 1228, 1241, 1248, 1253, 1269, 1271, 1585, 1744, 1759, 1777, 2410.
- v1 movable: 28, 265, 273, 299-302, 307, 310-311, 318, 322, 327, 547, 564, 1663, 2247, 2317.
- v1 external-delete: 2919 and 9135-9184.
- v1 HOLD: 2878, 3134, 3163, 3166, 3251, 3391, 3514, 3528, 3776, 3971, 4087, 4099, 4228, 4289, 4382, 4443, 4621, 4867, 4923, 5073, 5191, 5663, 5934, 5969, 5994, 6365, 6444, 6732, 7018, 7439, 7775, 7806, 8107, 8244, 8383, 8463, 8593, 8638, 8931, 9082.
- v1.1 HOLD: 7, 13, 15, 20-22, 26, 29, 33, 39, 48-49, 52, 58-61, 65-67, 70, 74-75, 77, 83, 89, 96-97, 106, 110, 114-116, 118, 126, 132, 135-137, 139, 144, 150, 162, 175, 180, 184-185, 188, 193, 207.

## 7. R5 — external-archive completeness

**Verdict: FAIL.**

All 51 external-delete rows were checked. Positive results:

- 51/51 are untracked;
- 51/51 have a numeric size and 64-hex SHA-256;
- 51/51 paths exist now, and every recorded size and SHA-256 matches the live bytes;
- 51/51 `(repo_tree, rel_path)` keys are unique, relative, and contain no `..` traversal;
- every row uses the same coherent, collision-resistant destination scheme: `<archive_root>/HK01/<repo_or_tree>/<YYYYMMDD>/<rel_path>`.

The plan nevertheless fails §8 in two independent ways.

First, rows 9170, 9173, and 9174 are exact-path cited by the current foundational operational contract described in R2. They are not eligible for the proposed delete-after-archive action without a later disposition ruling.

Second, the common action text says to “record source path/size/sha256” and “verify bytes,” but it does **not** say that the manifest record must contain the resulting **archive path** or **verification status**. Those are mandatory fields at controlling-ruling lines 221-225. The placeholders `<archive_root>` and `<YYYYMMDD>` are also unresolved, and no concrete external archive root or archive-manifest destination/name is identified. Thus the mapping scheme is coherent, but the execution plan is not a complete §8 manifest plan.

## 8. Delta summary's four self-flagged gaps

The delta summary has four actual governance/schema gaps in §7 items 1, 2, 3, and 5. Its item 4 expressly says no EUROMOD-STORAGE scope ambiguity is raised.

1. **`Data/external` v1 canonical versus R-124.3 HOLD — SAFE CLASS CHANGE; AUTHORITY NOT IN FILE CORPUS.** The 29 v1→v1.1 conversions are explicit, not silent. HOLD is correct under the controlling §3 fail-closed default because v1 itself says its canonical call was unconfirmed. An independent search found no on-disk R-124.3 instrument outside the delta documents, so the claimed directive's provenance remains for deputy confirmation; the safe HOLD result does not depend on authenticating it.

2. **Live U6-D DONE-marker precedent — CONFIRMED DEFECT.** v1 row 1253 and rows 1258-1276 are incorrectly immutable. The v1.1 HOLD treatment for later live U6-D completion-marked attempts is correct. This is an R3/R4 blocker.

3. **`notebook_dev_v3` directory ruling not propagated — CONFIRMED DEFECT.** The binding ruling authorizes the aggregate output location at lines 156-160. All 52 current files are left HOLD with `ruling_ref=False` (v1 rows 681-717; v1.1 rows 3-17). This is an R3/R4 blocker.

4. **`__pycache__` scan precedent / `IGNORED` vocabulary — DISCLOSED SCHEMA EXTENSION, NOT A DISPOSITION DEFECT.** v1.1 rows 140-144 are all HOLD and Git independently confirms `.gitignore:2` ignores `__pycache__/`. Including present build artifacts in a housekeeping delta is within the authorized development-tree scope. Standardizing the status vocabulary is a future schema decision, but no action or silent conversion arises now.

The delta's EUROMOD-STORAGE item is also confirmed as non-problematic for scope: v1 already inventoried that tree and 50 of the 51 external-archive candidates use a distinct `EUROMOD-STORAGE` tree prefix. This does not cure the R2/R5 defects affecting three of those rows.

## 9. Overall disposition

**Overall: FAIL — return the packet to the deputy as not ratifiable for Phase 2.**

This is a review verdict only. No proposed row was changed, no fix was made, and Phase 2 remains unauthorized.
