# JMP-HK-01 — FINAL EXECUTION / ACCEPTANCE RECORD (v1)

**Mission:** JMP-HK-01 (Goal-1 repository-hygiene mission, two phases)
**Date:** 2026-08-26
**Controlling authority:** `docs/Missions/JMP_HK_01_authorization_and_PKG01A_crossref_ruling_v1.md` §§3, 4, 8, 9
**Executing ruling:** Deputy ruling *"HK-01 V7 AND FINAL FOUR MOVES"* (Goal-1 R-148.1)
**Retained under ruling §9 as:** item 5, *the final execution/acceptance record*
**Status:** **JMP-HK-01 CLOSED**

This is the single permanent acceptance record for the mission. Per ruling §9 no
additional review memo and no scanner-defect memo were created, and no per-file memo
was written for any moved or deleted artifact.

---

## 1. Disposition-register lineage and hashes

Every register version is preserved on disk unchanged. v7 is the deputy-ratified
execution register (ruling §9 item 4).

| Version | File | SHA-256 | Role |
|---|---|---|---|
| v3 | `JMP_HK_01_inventory_and_disposition_register_v3.csv` | `30d0999e56e29a6ef513359b0a708512f1780d4b63f76cc22d5aba23a16f2937` | Codex re-review v1 correction pass |
| v4 | `JMP_HK_01_inventory_and_disposition_register_v4.csv` | `4cb3bda72d26f5b723756a85b31ab617361e18f6e467b7cf00855073c9a61126` | Phase-1 packet register |
| v5 | `JMP_HK_01_inventory_and_disposition_register_v5.csv` | `ed8a186ac7520bb319ff513a3edc8ceb1f721164a33271474c881ddcba8451b8` | 8 `ARCHIVE_MOVABLE` rows; input to the Codex narrow review |
| v6 | `JMP_HK_01_inventory_and_disposition_register_v6.csv` | `cc2f1725615831d7231532f6f39356583c8f6271e54601a8d11343baa6963ce0` | 3 rows reclassified `HISTORICAL_IMMUTABLE_IN_PLACE`; 5 movable remain |
| **v7** | `JMP_HK_01_inventory_and_disposition_register_v7.csv` | **`7b710381cf8c41bdbadd7b230a4b8b40274ca696024f1875305a2c8fb5a4734e`** | **Ratified execution register.** Parent = v6 `cc2f1725…63ce0` |

**Parent metadata.** v7's parent is register v6, SHA-256
`cc2f1725615831d7231532f6f39356583c8f6271e54601a8d11343baa6963ce0`, verified byte-for-byte
before v7 was derived and re-verified unchanged afterwards. Consistent with the v5→v6
convention and with ruling §9, the register CSVs carry no in-file metadata row; the
parent SHA and the disposition counts are recorded here.

**v7 counts (all verified):** `CANONICAL_CURRENT` 937 · `HISTORICAL_IMMUTABLE_IN_PLACE`
136 · `ARCHIVE_MOVABLE` 4 · `DELETE_TRACKED` 0 ·
`ARCHIVE_EXTERNAL_THEN_DELETE_UNTRACKED` 29 · `HOLD` 8,281 · **TOTAL 9,387**.

v7 is 9,387 rows × 24 columns, identical to v6 in stable IDs and row order, and differs
from v6 at exactly one physical CSV line — line 1663. The v7 mechanical gate passed
16 of 16 checks.

---

## 2. Row 1663 — the one substantive v6→v7 change

**Artifact:** `MNL/Results/P3a/pooled_P3a/JMP_pooled_P3a_estimation_report_v1.md`
(24,542 bytes, SHA-256 `c7a66c97dd7c6ad29d63cf916bada6b343a2a28004ecff1b6bcce538e586888f`)

**Reclassified:** `ARCHIVE_MOVABLE` → `HISTORICAL_IMMUTABLE_IN_PLACE`

**Deputy's reason, recorded verbatim in the register:**

> A live Supersedes: exact-path citation and a same-document basename changelog citation
> establish an active evidentiary-lineage dependency. The historical predecessor must
> remain immutable at its existing path.

**Both citations** — both in the current successor
`MNL/Results/P3a/pooled_P3a/JMP_pooled_P3a_estimation_report_v2.md`
(SHA-256 `699479f3c5b8b323e58b804c1cfe5eb114eb209432315ce2cedc66a5f944a9ad`, register
disposition `CANONICAL_CURRENT`):

1. **Live exact-path `Supersedes:` citation**, line 6, inside a Markdown code span:
   ``**Supersedes:** `Results/P3a/pooled_P3a/JMP_pooled_P3a_estimation_report_v1.md` ``
2. **Same-document changelog basename citation**, line 535, a changelog table row:
   ``| `JMP_pooled_P3a_estimation_report_v1.md` | First execution report (superseded by this v2) |``

**Register treatment.** Path, hash and size preserved. `archive_path`,
`verification_status` and `deputy_ratification_required` cleared to empty.
`proposed_action` set to the non-executable
`None -- remain in place at current path (HISTORICAL_IMMUTABLE_IN_PLACE).`
`immutability_ruling_protection` and `reason` both carry the deputy's verbatim text.

**Neither citing document was edited.** Per the ruling, the v2 report and its changelog
were left exactly as found; the predecessor was protected instead of the citation being
removed. The v2 report's last modifying commit remains `33eaba2`, unchanged by this
mission.

---

## 3. The three v6-protected files

Reclassified `ARCHIVE_MOVABLE` → `HISTORICAL_IMMUTABLE_IN_PLACE` at v6, on the Codex
narrow review's three check-1 FAILs. All three remain at their original paths,
byte-identical, and were re-verified after the moves.

| # | Path (MNL) | SHA-256 | Live citation that protects it |
|---|---|---|---|
| 1 | `docs/France_case/P2a/FR_P2a_region_live_phase4_remediation_report_v4.md` | `0c1d17d8345d7ce5ff932cac1fc3ea3a8684168620e96f450401b5248d137590` | `docs/France_case/P2a/FR_P2a_region_live_phase4_code_review_v5.md:18` — same-directory basename, referencing review is `CANONICAL_CURRENT` |
| 2 | `docs/France_case/P2a/FR_P2a_region_live_phase4_remediation_report_v5.md` | `ff313833cf6c1bb2f616e3bde05046702b7fe0c5ce8dc165cf8e7ada37bf9376` | `docs/France_case/P2a/FR_P2a_region_live_phase4_code_review_v6.md:16` — same-directory basename, referencing review is `CANONICAL_CURRENT`, `manifest_ref=True` |
| 3 | `docs/jmp_methodology/RURO_welfare_stage2_vdir_crosscheck_v1.md` | `354301fc0e17e2e1b6a54aaf8013576b657d0fa801a6644270ded5437a68943d` | `docs/jmp_methodology/RURO_welfare_stage2_vdir_crosscheck_v2.md:6-7` — same-directory exact path, referencing doc is `CANONICAL_CURRENT`, `contract_ref=True`, `review_ref=True` |

Together with row 1663, four artifacts were protected in place rather than archived.

---

## 4. The four executed tracked moves

All four are MNL-internal, executed with `git mv` under one gated MNL commit. Each
destination preserves the complete original repository-relative path beneath the archive
root `archive/HK01/2026-08-25_ratified_v1/` — no flattening. All four registered by Git
as **R100** (pure rename, zero content change).

| # | Old path (MNL) | New path (MNL) | SHA-256 (unchanged) |
|---|---|---|---|
| 1 | `docs/France_case/P2a/FR_P2a_region_live_phase4_remediation_report_v2.md` | `archive/HK01/2026-08-25_ratified_v1/docs/France_case/P2a/FR_P2a_region_live_phase4_remediation_report_v2.md` | `24e694055d56dbf639404a365bccce4c1f6cfb3a9de31524f030664d0202ef02` |
| 2 | `docs/France_case/P2a/FR_P2a_region_live_phase4_remediation_report_v3.md` | `archive/HK01/2026-08-25_ratified_v1/docs/France_case/P2a/FR_P2a_region_live_phase4_remediation_report_v3.md` | `a7b530d484899885632d1d2366c6df336e2e7bbdf9fed418636b8e62fe9bef1e` |
| 3 | `docs/France_case/P2a/FR_P2a_region_live_phase5_code_review_v4.md` | `archive/HK01/2026-08-25_ratified_v1/docs/France_case/P2a/FR_P2a_region_live_phase5_code_review_v4.md` | `3a785d4fb09776c1654a49a83e607a41526fca92dc16d898765d004275454ce2` |
| 4 | `docs/France_case/P2a/FR_P2a_streaming_incrementA_review_v2.md` | `archive/HK01/2026-08-25_ratified_v1/docs/France_case/P2a/FR_P2a_streaming_incrementA_review_v2.md` | `f61f72e93f714dd5fce4813820d58e564a4d2902b0328eede787388027b54133` |

**Final MNL commit SHA:** `192ef57a76cffc6375f2f50f2c2893ef292bb4be`
**Message:** `chore(hk01): phase-2 tracked archive moves per ratified register v7`
**Stat:** 4 files changed, 0 insertions(+), 0 deletions(-) — four renames at 100% similarity.

No Job_Market_paper commit was created for the moves (all four movers are MNL-internal;
an empty JMP commit was expressly not created). **Zero tracked deletions** and **zero
further untracked deletions** were performed. No destination collision occurred: all four
destinations were verified absent immediately before the moves, and the four normalized
destination strings are unique.

### 4.1 Final pre-move scan (the four survivors)

Run immediately before movement, in every form the ruling enumerates: full relative
paths; basenames; same-directory **and** repository-context basename resolution; Markdown
links and code spans; quoted filenames; `Supersedes:` / `Superseded-by:` fields;
CHANGELOG references; manifests, pins and acceptance pointers; current reviews and
live-task targets; and the Phase-2 supersession-map status column.

| Row | Artifact | Exact-path | Basename (all resolutions) | Pin / manifest / pointer | Immutability ruling | Sensitive / microdata | Destination | Verdict |
|---|---|---|---|---|---|---|---|---|
| 299 | `FR_P2a_region_live_phase4_remediation_report_v2.md` | CLEAR | CLEAR — hits confined to HK01 administration | CLEAR (0/76 pins) | CLEAR | CLEAR | absent, unique | **MOVE** |
| 300 | `FR_P2a_region_live_phase4_remediation_report_v3.md` | CLEAR | CLEAR — hits confined to HK01 administration | CLEAR (0/76 pins) | CLEAR | CLEAR | absent, unique | **MOVE** |
| 307 | `FR_P2a_region_live_phase5_code_review_v4.md` | CLEAR — sole non-HK01 hit is a `CREATE` instruction at `Job_Market_paper/docs/prompts/JMP_M05B_closed_form_code_review_v4_prompt_v1.md:138` | CLEAR | CLEAR (0/76 pins) | CLEAR | CLEAR | absent, unique | **MOVE** |
| 327 | `FR_P2a_streaming_incrementA_review_v2.md` | CLEAR — sole non-HK01 hit is a `CREATE` instruction at `Job_Market_paper/docs/prompts/JMP_M05C_incrementA_review_v2_prompt_v1.md:104` | CLEAR | CLEAR (0/76 pins) | CLEAR | CLEAR | absent, unique | **MOVE** |

The scan corpus was the **complete working tree** of MNL, Job_Market_paper and (read-only)
dclaborsupply-monorepo — tracked, untracked **and** git-ignored content — not a
`docs`-restricted subset. MNL returned **zero** hits for all four basenames anywhere in
its working tree. Job_Market_paper returned 94 hits, every one inside
`docs/Missions/HK01/` (HK01 administration: registers v1–v7, the reference-protection
map, the supersession map, the Codex review) or `docs/prompts/` (the two `CREATE`
instructions above). dclaborsupply-monorepo returned zero.

Rows 307 and 327 are the two survivors whose supersession-map entries carried a live
exact-path reference. Both were **explicitly disproved as protective** rather than
waived: each sole reference is an authoring `CREATE` instruction inside a routine mission
prompt for a closed M05B/M05C increment. Ruling §9 expressly treats routine prompts and
action cards as disposable chat, and ruling §4 lists what a supersession map cannot
override — an exact path cited by a current **contract, manuscript or review**. A prompt
is none of those, both prompt rows are `HOLD` with no protection flags, and neither is a
live-task target. Rows 299 and 300 have no non-administrative reference in any form.

---

## 5. The 29 completed external archive/deletes

29 untracked artifacts (all under `EUROMOD-STORAGE`) were copied to the dated external
archive outside every active Git repository, byte-verified, and only then deleted at
source. Recorded in `JMP_HK_01_phase2_archive_manifest_v1.csv`
(SHA-256 `a634e509c1ba0296335ad0a2bcc76d3450dea39c16a8ab5fe94ecad4e65227c1`).

Reconciliation against v7, all passing:

* register rows with `ARCHIVE_EXTERNAL_THEN_DELETE_UNTRACKED` = 29; manifest rows with
  `verification_status = ARCHIVED_VERIFIED_SOURCE_DELETED` = 29;
* the two `row_id` sets are identical;
* for all 29, `sha256_source` = `sha256_archive` = `register_sha256_source`;
* `size_verified = True`, `hash_verified = True`, `source_deleted = True` on 29 of 29.

No broad clean command was used at any point. No raw data was deleted.

---

## 6. The 18 microdata HOLD rows

18 manifest rows carry `verification_status = HOLD_RECLASSIFIED_HALTED`: register rows
9137–9147, 9152, 9153, 9155, 9160, 9162, 9171, 9172 — the `EUROMOD-STORAGE`
`scratch/de_pilot` and `scratch/staging/de_2017*` artifacts. Basis recorded in the
manifest: *"R-132 §6 safety reclass to HOLD; row halted, not archived, not deleted.
Basis: household-level records (idhh + disposable income, 40 HH)."*

All 18 verified in v7: disposition `HOLD` 18/18; register rows byte-identical to v6
18/18; `archived_utc` empty and `source_deleted = False` 18/18. **None was archived,
copied into Job_Market_paper, moved or deleted.** No household-level or restricted file
was copied into Job_Market_paper at any point in the mission.

---

## 7. Row 2919 — restoration

**Artifact:** `Job_Market_paper/Literature/md_extractions/__bbox_tmp_Bargain et al_2010_
"Making work pay" in a rationed labor market.html` (the filename contains a raw U+009D
byte), 1,483,064 bytes, SHA-256
`7bce41c298b86000e880578233a9adf85d73ec9816571ef14a86df6766942c6b`.

Register v4 recorded this row as `UNTRACKED` with `git_status = ??`, but the path **is**
tracked in JMP HEAD `1f458de7`. Acting on the misclassification, the row was archived and
its source deleted. Because `DELETE_TRACKED = 0` is mandated, the action was reverted:
the file was **restored** — its SHA-256 matches the register value exactly — and the
archive copy was removed. The manifest carries it as
`HALTED_REGISTER_MISCLASSIFICATION_RESTORED` with `source_deleted = False`.

Verified in v7 and again after the moves: **TRACKED**, disposition **HOLD**, SHA-256
`7bce41c2…42c6b` matching both the register and the manifest `register_sha256_source`,
and byte-identical to the v6 register row. The mission's net tracked-deletion count is
zero.

### 7.1 Line-ending divergence in the restored copy (recorded, not remediated)

The restored working-tree file is **content-identical but not blob-identical** to the
copy in the Git index, and this is recorded here rather than silently smoothed over:

| | Bytes | SHA-256 | Line endings |
|---|---|---|---|
| Working tree (restored) | 1,483,064 | `7bce41c298b86000e880578233a9adf85d73ec9816571ef14a86df6766942c6b` | 17,974 CRLF |
| Index blob `d7678fa9` | 1,465,090 | `847c7151f603ca09477d0fc7fa43efabe0877a5e80c6fd1cb422b57cb8e66fb1` | 17,974 LF |

LF-normalized, the two are **exactly equal** — the divergence is line endings only, with
no content difference whatsoever. JMP sets `.gitattributes` to `* -text` (the line-ending
pin from commit `5efc37a`), so Git performs no CRLF conversion in either direction; the
restored copy therefore carries CRLF where the committed blob carries LF, and the path
consequently shows as ` M` in `git status`.

**Three points of record.** First, this state **pre-existed this closeout** — the file
was already ` M` when the final closeout began, and this mission never touched it.
Second, it is **deliberately left unremediated**: the register's authoritative
`sha256_or_flag` for row 2919 is `7bce41c2…42c6b`, which is the *working-tree* value, so
running `git restore` on the path today would rewrite it to the LF blob and move it
**away** from the value the register and manifest both pin. Third, no data was lost —
the restoration is complete and content-exact, which is the property the ruling's
"byte-identical" requirement exists to guarantee.

The path was left uncommitted and untouched. Row 2919 is a `HOLD` row, not one of the
four movers, and no tracked deletion of it stands.

---

## 8. Scanner defects recorded

Recorded here, in the acceptance record, rather than in a separate memo (ruling §9).

### 8.1 The U+009D defect

The Phase-1 inventory scanner failed to match a filename containing a raw **U+009D**
byte (`__bbox_tmp_Bargain et al_2010_…html`, from a mojibaked `â€œ…â€\x9d` sequence).
The path was tracked in Git but the scanner's tracked-set lookup missed it, so the row
was classified `UNTRACKED` / `git_status = ??`. That misclassification is what drove the
erroneous archive-and-delete of a tracked file, later reverted (§7). The same byte breaks
naive console printing of the register — any tool reading these registers must decode and
emit UTF-8 explicitly.

**Class of defect:** filename/​byte-level normalization gap between the scanner's
tracked-set lookup and the Git index.

**Downstream consequence, still visible.** The archive-and-restore cycle this defect
caused left the restored file with CRLF line endings against an LF index blob (§7.1). It
is content-exact and was deliberately not remediated, because the register pins the
working-tree SHA-256, not the blob's.

### 8.2 Basename-reference scanner gaps (all of them)

Four distinct gaps were found in the reference machinery over this arc. Every one is a
**false-negative** gap — each caused a genuinely referenced artifact to be proposed as
movable.

| # | Gap | Consequence | Caught by |
|---|---|---|---|
| 1 | **Same-directory bare-basename resolution.** The Phase-1 reference-protection map resolved references only when a citation gave the full repository-relative path. A current document citing a sibling by bare basename alone produced no target-side row. | Three artifacts were wrongly proposed `ARCHIVE_MOVABLE` at v5 (remediation reports v4 and v5, and `RURO_welfare_stage2_vdir_crosscheck_v1.md`). | Codex narrow review (rows 3, 4, 7) → fixed at v6 |
| 2 | **Target-side vs referencing-side column confusion.** The protection map's first column is the *referencing* document; grepping it indiscriminately makes an artifact's own outbound citations look like inbound protection, and vice versa. The map holds **zero** target-side rows for all eight v5 candidates while holding many rows *authored by* them. | Latent false confidence in both directions. | Codex narrow review §1, by parsing target-side only |
| 3 | **Corpus scope gap — the decisive one.** The Codex narrow review's exact-path scan covered only `MNL/docs`, `Job_Market_paper/docs` and `Job_Market_paper/manuscript`. The document that cites row 1663 lives at `MNL/Results/P3a/pooled_P3a/JMP_pooled_P3a_estimation_report_v2.md` — **outside every scanned tree**. | Row 1663's live `Supersedes:` citation was invisible to the review, producing the factually wrong ACCEPT of §9 below. | Deputy v7 ruling → fixed at v7; final scan corpus widened to the complete working trees of all three repositories |
| 4 | **Changelog-table basename citations.** A basename appearing inside a Markdown changelog table row is a real evidentiary-lineage citation, but matched none of the link-, path- or `Supersedes:`-shaped patterns the earlier scanners looked for. | Row 1663's second citation (line 535 of the v2 report) was missed by both the protection map and the narrow review. | Deputy v7 ruling → fixed at v7 |

**Remediation applied in this closeout.** The final pre-move scan abandoned pattern- and
corpus-restricted scanning entirely: it searched the four bare basenames across the
**entire working tree** of MNL, Job_Market_paper and dclaborsupply-monorepo, including
untracked and git-ignored content, then classified every hit by hand. A bare-basename
sweep is a strict superset of every path form, link form, code-span form, quoted form,
`Supersedes:` form and changelog form, so gaps 1, 3 and 4 cannot recur under it; gap 2 is
avoided by not consulting the protection map as the primary evidence at all.

---

## 9. Review-error disposition — the Codex row-8 factual error

`JMP_HK_01_v5_movable_rows_codex_review_v1.md`
(SHA-256 `c1e92cf3671917be3cbe5fb3abd305091f0a4632e475226b9ba3dd644ce4b6f0`), row 8,
returned **ACCEPT** for `Results/P3a/pooled_P3a/JMP_pooled_P3a_estimation_report_v1.md`,
asserting *"No current target-side reference. Exact full-path hits are HK01
administration; basename hits outside it occur only in pre-existing `MNL/docs/archive/…`
historical documents, not current inputs."*

**That ACCEPT was factually wrong.** It did not address:

1. the **live exact-path `Supersedes:` citation** at line 6 of the current v2 report;
2. the **same-document changelog basename citation** at line 535 of that same report;
3. the **Phase-2 supersession-map status** for row 1663 —
   `HALTED_AWAITING_DEPUTY`, carrying `B2: 1 live exact-path reference(s) remain, which
   falsifies the ARCHIVE_MOVABLE predicate`, and naming the referencing document
   explicitly as `MNL/Results/P3a/pooled_P3a/JMP_pooled_P3a_estimation_report_v2.md`.

The root cause is scanner gap 3 of §8.2: the review's corpus stopped at
`MNL/docs`, so the citing document at `MNL/Results/…` was never read. The error was
narrow and mechanical, not a judgement failure — the review's other seven rows were
correct, and its three check-1 FAILs are what produced the v6 protections in §3.

**The supersession map held the correct status.** Its fail-closed
`HALTED_AWAITING_DEPUTY` on row 1663 was right where the later, narrower review was
wrong.

### 9.1 The §4 principle, recorded

> **A review may not override an unresolved fail-closed supersession-map reference
> without explicitly addressing and disproving it.**

An unresolved supersession-map status is binding. Silence in a subsequent review does not
clear it; only an explicit, evidenced disproof does. This principle was applied twice in
this closeout, with opposite outcomes:

* **Row 1663** — the map's live reference was **confirmed**, not disproved. The artifact
  was reclassified `HISTORICAL_IMMUTABLE_IN_PLACE` and left in place.
* **Rows 307 and 327** — the map's live references were **explicitly disproved** on the
  record (§4.1): each sole citation is a `CREATE` authoring instruction in a routine,
  ruling-§9-disposable mission prompt for a closed increment, which is not a contract,
  manuscript, pointer or live review under ruling §4. Only then were they moved.

Per the deputy ruling, the other four rows were not reopened and no further Codex review
was commissioned; they stand reverified clear under the complete scan.

---

## 10. Post-move gate results

The full battery was run **before** the moves, **after** the moves but before the commit,
and **after** the commit. All three runs: **13 of 13 PASS**.

| # | Check | Pre-move | Post-commit |
|---|---|---|---|
| A1 | all 76 pins pass (52 `m08e_pins.py` + 24 `m08_u6_pins_v2.py`) | **PASS** 76/76 | **PASS** 76/76 |
| A2 | no pinned path names any of the four movers | **PASS** 0/76 | **PASS** 0/76 |
| A3 | both pin-registry self-SHAs unchanged (`bcf0598d…`, `1324b04f…`) | **PASS** | **PASS** |
| B1 | zero broken manifests or acceptance pointers | **PASS** 4/4 | **PASS** 4/4 |
| B2 | no manifest or acceptance pointer names a mover | **PASS** | **PASS** |
| C1 | zero dangling exact-path or basename references in MNL (all forms, whole working tree) | **PASS** 0 hits | **PASS** 0 hits |
| C2 | JMP hits are HK01 administration or ruling-§9 prompts only | **PASS** 0 protective | **PASS** 0 protective |
| C3 | dclaborsupply-monorepo names no mover | **PASS** 0 hits | **PASS** 0 hits |
| D1 | zero live review targets moved; no current review cites a mover | **PASS** 4/4 in place | **PASS** 4/4 in place |
| E1 | zero moved protected artifacts (3 v6-protected + row 1663) | **PASS** 4/4 | **PASS** 4/4 |
| E2 | row 2919 restored, tracked, byte-identical | **PASS** | **PASS** |
| F1 | content hashes unchanged for all four moved files | **PASS** | **PASS** |
| G1 | no file outside the four approved rows changed | **PASS** | **PASS** |

Manifest and pointer integrity re-verified by SHA-256 after execution:
`JMP_cross_repo_artifact_manifest_v1.md` `5033c6f8…`;
`RURO_ACTIVE_RESULTS_REGISTRY.md` `21d713a3…`;
`JMP_HK_01_phase2_archive_manifest_v1.csv` `a634e509…`;
`JMP_HK_01_phase2_supersession_map_v1.csv` `0fc7a8fb…`.

No citing document, manifest or pin registry was edited at any point to make cleanup
pass. The only MNL working-tree modification outside the four moves is
`notebooks/france/fr_singles_results_discussion_v1.ipynb`, which was already modified
before this mission began, was never touched by it, and was deliberately left
uncommitted.

---

## 11. Confirmation

**No raw data, no accepted attempt directory, no pinned artifact, no ruling-protected
path and no live review target moved or disappeared during JMP-HK-01.**

Specifically: all 76 pins resolve and hash-verify unchanged; all four protected artifacts
(the three v6 protections and row 1663) remain at their original paths byte-identical;
row 2919 is restored, tracked, and content-exact at the SHA-256 the register and manifest
both pin, with the line-ending caveat of §7.1 recorded; all 18 microdata rows remain `HOLD`,
un-archived and un-deleted; the mission performed zero tracked deletions; no
household-level or restricted file was copied into Job_Market_paper; dclaborsupply-monorepo
was inspected read-only and not cleaned; and the two repositories were not merged.

Exactly four tracked artifacts changed location, all four within MNL, all four at 100%
rename similarity with content hashes unchanged, under MNL commit
`192ef57a76cffc6375f2f50f2c2893ef292bb4be`.

**JMP-HK-01 is closed.**
