# JMP-HK-01 v5 surviving movable rows — Codex narrow review v1

**Date:** 2026-08-26  
**Mode:** narrow read-only disposition review; no source artifact moved, renamed, deleted, or archived  
**Input:** `docs/Missions/HK01/JMP_HK_01_inventory_and_disposition_register_v5.csv`  
**Authority:** `docs/Missions/JMP_HK_01_authorization_and_PKG01A_crossref_ruling_v1.md` §§3, 4, 8  
**Population:** exactly the eight v5 rows whose `proposed_disposition` is `ARCHIVE_MOVABLE`  
**Overall verdict:** **REJECT**

## 1. Review rule and evidence base

A row is accepted only if all five requested checks pass:

1. no current exact-path reference;
2. no pin, manifest, or pointer protection;
3. no immutability-ruling protection;
4. no sensitive or microdata content in the source bytes; and
5. the assigned destination is collision-free, is inside the owning repository, and
   preserves the complete source-relative path below
   `archive/HK01/2026-08-25_ratified_v1/`.

The exact-path scan covered `MNL/docs`, `Job_Market_paper/docs`, and
`Job_Market_paper/manuscript`. Neither repository has a root `contracts` directory;
contract documents below `docs` were therefore included by the two `docs` scans.
For each target, the scan tested the repository-relative path, `MNL/`-prefixed path,
absolute path forms, and the exact basename interpreted relative to a same-directory
referencing document. The last form matters: it found three current references that
the reference-protection map did not resolve as target-side rows.

Administrative self-mentions in the HK01 inventory versions, reference map, and proposed
supersession map are not current functional references. A CREATE instruction in a routine
prompt also is not a current contract, manuscript, pointer, or live review: the two such
prompt sources are `HOLD` at v5 physical lines 2340 and 2353, and the governing ruling §9
expressly treats routine prompts/action cards as disposable. Currentness of the three
decisive referencing documents is not inferred: v5 records them as
`CANONICAL_CURRENT` live inputs at physical lines 290, 291, and 565.

Shared mechanical evidence used in every row:

- The protection map was parsed target-side (`referenced_path_raw` and
  `resolved_relative_path`), not grepped indiscriminately through its
  `referencing_document` column. It contains zero target-side rows for all eight targets
  and zero target-side `pin`, `manifest`, or `pointer` rows.
- Both live pin registries were scanned directly and have zero target-string hits:
  `MNL/scripts/m08e/m08e_pins.py` (SHA-256
  `bcf0598d96058b005a72fba4fbc8458ed447ea6c96898afec986f627fc3b3a16`) and
  `MNL/scripts/welfare/m08_u6_pins_v2.py` (SHA-256
  `1324b04feb4856b30fca228e1c972edc4f42864c4e4888bf341d38f21b7f8403`).
- Direct manifest/pointer-registry scans also have zero target hits in
  `Job_Market_paper/docs/JMP_cross_repo_artifact_manifest_v1.md` (SHA-256
  `5033c6f8ff5be76591bd4287c062291df36a8d186db921562ab95dfd45e8f65c`)
  and `MNL/docs/estimation/RURO_ACTIVE_RESULTS_REGISTRY.md` (SHA-256
  `21d713a360501e3095dab0caa3674ff3c7eacf6be1f8774dfacae5755c7635f5`).
- Sixteen ruling-named documents across the two `docs` trees were scanned directly;
  none names any target. The map has zero target-side `ruling` rows, and all eight v5
  rows have `ruling_ref=False` and blank `immutability_ruling_protection`.
- Every source was read as raw bytes. All eight are strict UTF-8 Markdown with zero NUL
  bytes, zero non-whitespace control bytes, zero email addresses, and zero apparent
  row-level `idhh`/`source_idhh`/household-ID values. Recomputed size and SHA-256 match
  v5 for every row. Mentions of `idhh`, restricted-store controls, EUROMOD, or raw
  microdata are design/prohibition prose, not embedded individual records or microdata.
- All eight normalized destinations are below
  `C:/Users/hisham/Repo/MNL/archive/HK01/2026-08-25_ratified_v1/`, all are absent, and
  the eight normalized case-insensitive destination strings are unique (8/8).

## 2. Exactly five checks per row

| # | v5 `ARCHIVE_MOVABLE` row | (1) Current exact-path reference | (2) Pin / manifest / pointer | (3) Immutability ruling | (4) Sensitive / microdata bytes | (5) Assigned destination | Row verdict |
|---:|---|---|---|---|---|---|---|
| 1 | `docs/France_case/P2a/FR_P2a_region_live_phase4_remediation_report_v2.md` | **PASS.** No current target-side reference. Full-path/basename hits are confined to HK01 inventory/map/supersession administration. | **PASS.** Zero hits in both pin registries, both direct manifest/pointer registries, and protected-kind map rows. | **PASS.** Zero direct ruling hits and no map/register immutability flag. | **PASS.** 11,178 bytes; SHA-256 `24e694055d56dbf639404a365bccce4c1f6cfb3a9de31524f030664d0202ef02`; prose-only remediation report; no row-level records. | **PASS.** Absent and unique: `archive/HK01/2026-08-25_ratified_v1/docs/France_case/P2a/FR_P2a_region_live_phase4_remediation_report_v2.md`; normalized inside MNL; suffix equals the full source-relative path. | **ACCEPT** |
| 2 | `docs/France_case/P2a/FR_P2a_region_live_phase4_remediation_report_v3.md` | **PASS.** No current target-side reference. Full-path/basename hits are confined to HK01 inventory/map/supersession administration. | **PASS.** Zero hits in both pin registries, both direct manifest/pointer registries, and protected-kind map rows. | **PASS.** Zero direct ruling hits and no map/register immutability flag. | **PASS.** 11,246 bytes; SHA-256 `a7b530d484899885632d1d2366c6df336e2e7bbdf9fed418636b8e62fe9bef1e`; prose-only remediation report; no row-level records. | **PASS.** Absent and unique: `archive/HK01/2026-08-25_ratified_v1/docs/France_case/P2a/FR_P2a_region_live_phase4_remediation_report_v3.md`; normalized inside MNL; suffix equals the full source-relative path. | **ACCEPT** |
| 3 | `docs/France_case/P2a/FR_P2a_region_live_phase4_remediation_report_v4.md` | **FAIL.** Current `MNL/docs/France_case/P2a/FR_P2a_region_live_phase4_code_review_v5.md:18` names the exact same-directory path `FR_P2a_region_live_phase4_remediation_report_v4.md` among the files read in full. V5 physical line 290 classifies that referencing review `CANONICAL_CURRENT`, `review_ref=True`, and a live mission input. | **PASS.** Zero hits in both pin registries, both direct manifest/pointer registries, and protected-kind map rows. | **PASS.** Zero direct ruling hits and no map/register immutability flag. | **PASS.** 11,435 bytes; SHA-256 `0c1d17d8345d7ce5ff932cac1fc3ea3a8684168620e96f450401b5248d137590`; prose-only remediation report; no row-level records. | **PASS.** Absent and unique: `archive/HK01/2026-08-25_ratified_v1/docs/France_case/P2a/FR_P2a_region_live_phase4_remediation_report_v4.md`; normalized inside MNL; suffix equals the full source-relative path. | **REJECT** |
| 4 | `docs/France_case/P2a/FR_P2a_region_live_phase4_remediation_report_v5.md` | **FAIL.** Current `MNL/docs/France_case/P2a/FR_P2a_region_live_phase4_code_review_v6.md:16` names the exact same-directory path `FR_P2a_region_live_phase4_remediation_report_v5.md` among the files read in full. V5 physical line 291 classifies that referencing review `CANONICAL_CURRENT`, `manifest_ref=True`, `review_ref=True`, and a live mission input. | **PASS.** Zero hits in both pin registries, both direct manifest/pointer registries, and protected-kind map rows for this target itself. | **PASS.** Zero direct ruling hits and no map/register immutability flag. | **PASS.** 10,833 bytes; SHA-256 `ff313833cf6c1bb2f616e3bde05046702b7fe0c5ce8dc165cf8e7ada37bf9376`; prose-only remediation report; no row-level records. | **PASS.** Absent and unique: `archive/HK01/2026-08-25_ratified_v1/docs/France_case/P2a/FR_P2a_region_live_phase4_remediation_report_v5.md`; normalized inside MNL; suffix equals the full source-relative path. | **REJECT** |
| 5 | `docs/France_case/P2a/FR_P2a_region_live_phase5_code_review_v4.md` | **PASS.** The only non-HK01 exact full-path hit is a CREATE instruction at `Job_Market_paper/docs/prompts/JMP_M05B_closed_form_code_review_v4_prompt_v1.md:138`; that prompt is `HOLD`, has no protection flags at v5 line 2340, and is non-protective under ruling §9. | **PASS.** Zero hits in both pin registries, both direct manifest/pointer registries, and protected-kind map rows. | **PASS.** Zero direct ruling hits and no map/register immutability flag. | **PASS.** 18,414 bytes; SHA-256 `3a785d4fb09776c1654a49a83e607a41526fca92dc16d898765d004275454ce2`; code-review prose and aggregate controls only; no restricted member, score, or household record is embedded. | **PASS.** Absent and unique: `archive/HK01/2026-08-25_ratified_v1/docs/France_case/P2a/FR_P2a_region_live_phase5_code_review_v4.md`; normalized inside MNL; suffix equals the full source-relative path. | **ACCEPT** |
| 6 | `docs/France_case/P2a/FR_P2a_streaming_incrementA_review_v2.md` | **PASS.** The only non-HK01 exact full-path hit is a CREATE instruction at `Job_Market_paper/docs/prompts/JMP_M05C_incrementA_review_v2_prompt_v1.md:104`; that prompt is `HOLD`, has no protection flags at v5 line 2353, and is non-protective under ruling §9. | **PASS.** Zero hits in both pin registries, both direct manifest/pointer registries, and protected-kind map rows. | **PASS.** Zero direct ruling hits and no map/register immutability flag. | **PASS.** 11,579 bytes; SHA-256 `f61f72e93f714dd5fce4813820d58e564a4d2902b0328eede787388027b54133`; review prose about an ID/digest contract, with no actual household identifiers or microdata rows. | **PASS.** Absent and unique: `archive/HK01/2026-08-25_ratified_v1/docs/France_case/P2a/FR_P2a_streaming_incrementA_review_v2.md`; normalized inside MNL; suffix equals the full source-relative path. | **ACCEPT** |
| 7 | `docs/jmp_methodology/RURO_welfare_stage2_vdir_crosscheck_v1.md` | **FAIL.** Current `MNL/docs/jmp_methodology/RURO_welfare_stage2_vdir_crosscheck_v2.md:6-7` names the exact same-directory v1 path and explicitly says it is superseded/overturned. V5 physical line 565 nevertheless classifies v2 `CANONICAL_CURRENT`, `contract_ref=True`, `review_ref=True`, and a live mission input. The additional tree listing at `MNL/docs/doc_folder_structure.md:471` is not needed for the failure. | **PASS.** Zero hits in both pin registries, both direct manifest/pointer registries, and protected-kind map rows. | **PASS.** Zero direct ruling hits and no map/register immutability flag. | **PASS.** 10,221 bytes; SHA-256 `354301fc0e17e2e1b6a54aaf8013576b657d0fa801a6644270ded5437a68943d`; methodology prose only. It mentions raw microdata as a required but unavailable input; no microdata or person/household record is embedded. | **PASS.** Absent and unique: `archive/HK01/2026-08-25_ratified_v1/docs/jmp_methodology/RURO_welfare_stage2_vdir_crosscheck_v1.md`; normalized inside MNL; suffix equals the full source-relative path. | **REJECT** |
| 8 | `Results/P3a/pooled_P3a/JMP_pooled_P3a_estimation_report_v1.md` | **PASS.** No current target-side reference. Exact full-path hits are HK01 administration; basename hits outside it occur only in pre-existing `MNL/docs/archive/...` historical documents, not current inputs. | **PASS.** Zero hits in both pin registries, both direct manifest/pointer registries, and protected-kind map rows. | **PASS.** Zero direct ruling hits and no map/register immutability flag. | **PASS.** 24,542 bytes; SHA-256 `c7a66c97dd7c6ad29d63cf916bada6b343a2a28004ecff1b6bcce538e586888f`; aggregate estimation/reporting prose and parameter tables only; mentions `idhh` as a grouping variable but contains no ID values or microdata rows. | **PASS.** Absent and unique: `archive/HK01/2026-08-25_ratified_v1/Results/P3a/pooled_P3a/JMP_pooled_P3a_estimation_report_v1.md`; normalized inside MNL; suffix equals the full source-relative path. | **ACCEPT** |

## 3. Overall verdict

**REJECT.** Five rows pass all five checks, but three rows fail check 1:

- `FR_P2a_region_live_phase4_remediation_report_v4.md`;
- `FR_P2a_region_live_phase4_remediation_report_v5.md`; and
- `RURO_welfare_stage2_vdir_crosscheck_v1.md`.

Each is exact-path cited from a referencing document that the same v5 register calls
`CANONICAL_CURRENT` and a live mission input. Under the governing ruling §§3, 4, and 8,
those three cannot be moved while those references remain. The v5 eight-row movable set
therefore is not acceptable as a whole in its present form. No Phase-2 movement was
performed by this review.
