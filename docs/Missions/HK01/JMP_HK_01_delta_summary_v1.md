JMP-HK-01 PHASE-1 DELTA PASS (v1.1) -- DELTA SUMMARY

READ-ONLY. No files were moved, deleted, renamed, committed or archived in
the production of this pass. The only files written are this document and
`JMP_HK_01_inventory_and_disposition_register_v1_1.csv`, both under
`docs/Missions/HK01/`.

# 1. WHAT CHANGED SINCE v1 AND WHY

v1's register CSV has a filesystem birth-time of 2026-08-24 14:19:18 +0200.
Between that scan and this delta pass:

1. **Pricing stopped.** The U6-D ladder pushed a 4x pricing-geometry
   extension (8 new `priced_qw_4x_*` chunks under the existing
   `fr_singles_pricing_p2a_qw` cache) and a full new cross-check pricing
   cache (`fr_singles_pricing_p2a_xc`, 32 files) came into existence, all
   after the v1 cutoff.
2. **Two MNL housekeeping commits landed before v1 even ran**
   (`9b2fe82` "close U6-C" at 10:21:47+0200) and a matching
   Job_Market_paper commit (`5efc37a` "commit U6 deputy instruments") --
   both are already fully reflected in v1's tracked-file rows and are
   **not** part of this delta.
3. **U6-D phase progressed** from pilot/ladder/first three gates attempts
   (all already captured in v1) through ten further attempts:
   `u6dgates4` (STOPPED_ERROR), `u6dgates5`/`u6dgates6`
   (STOPPED_QW-ALIGN), `u6dgates7` (U6D_GATES_DONE), `u6dladder4x`
   (U6D_LADDER_PRICED), `u6dgates4x` (STOPPED_ERROR), `u6dgates4xb`
   (U6D_GATES_DONE), `u6dxc_dry` (U6D_XCHECK_DRYRUN), `u6dxc4x`
   (STOPPED_ERROR), `u6dxc4xb` (U6D_XCHECK_DONE) -- 118 files across the
   ten new attempt directories.
4. Four of the five `scripts/welfare/run_m08_u6d_*.py` / `m08_u6d_qw_basis.py`
   driver scripts were edited further after v1's scan (sizes grew by
   ~350-5,300 bytes each); their five compiled `__pycache__/*.pyc`
   siblings are new build artifacts.
5. `notebooks/france/fr_singles_results_discussion_v1.ipynb` grew from
   1,126,685 to 2,184,260 bytes (re-executed with more analysis cells),
   and its companion dev tree `outputs/p2a_singles2016/notebook_dev_v3/`
   gained 15 new files (37 -> 52).
6. A new governance directive (R-124.3, "LISTED-ONLY all-HOLD" for
   `Data/{processed,interim,external,pilot,inspecting}`) requires
   reclassifying the 29 already-tracked, byte-identical files under
   `Data/external/` from v1's CANONICAL_CURRENT to HOLD.

# 2. CORRECTIONS TO THE INPUT HINTS

The task brief's prior-recon hints materially overstated the delta in two
places, both verified and corrected here rather than taken on faith:

* The five `scripts/welfare/m08_u6d_*.py` scripts and
  `notebooks/france/fr_singles_results_discussion_v1.ipynb` were
  **already present in v1** (not new). Re-hashing found four of the five
  scripts and the notebook **changed content** since v1 (a genuine delta);
  `run_m08_u6d_pilot.py` re-hashed identical to v1 (no delta, excluded).
* `docs/Missions/JMP_HK_01_authorization_and_PKG01A_crossref_ruling_v1.md`
  and `docs/Missions/JMP_M08_RUM_benchmark_estimand_design_v1.md` were
  **already present in v1** with identical hashes today -- there is
  **zero delta** for Job_Market_paper. (The RUM design memo has no
  citation as a contract/design memo anywhere in the current doc corpus
  beyond v1's own HOLD listing of it.)
* `scripts/welfare/m08_u6_basis.py` and `m08_u6_pins_v2.py` show as
  git-`M` (modified vs. HEAD `9b2fe82`) today, but re-hashing shows the
  **working-tree content is byte-identical to what v1 already recorded**
  -- v1 scanned them in this same modified-but-uncommitted state. No
  delta row for either.
* `restricted/`, `phase4_curvature_v1`'s dryrun attempt, and the earlier
  U6 attempts (`u6probe1x`, `u62x`, `u6full`, `u6step0`, `u6r_smoke` x3,
  `u6resume2/3/4`) were fully hash-verified file-by-file against v1:
  **zero new or changed files** in any of them.

# 3. DELTA ROW COUNTS

| Disposition class | Delta rows |
|---|---|
| CANONICAL_CURRENT | 0 |
| HISTORICAL_IMMUTABLE_IN_PLACE | 0 |
| ARCHIVE_MOVABLE | 0 |
| DELETE_TRACKED | 0 |
| ARCHIVE_EXTERNAL_THEN_DELETE_UNTRACKED | 0 |
| HOLD | 212 |
| **TOTAL** | **212** |

Every delta row is HOLD. This is a deliberate, conservative consequence of
three facts: (a) none of the new/changed material is cited by any
manifest, pin registry, pointer, contract, manuscript or ruling scanned;
(b) the ruling and this mission's explicit instruction forbid classifying
live U6-D evidence as HISTORICAL_IMMUTABLE_IN_PLACE, ARCHIVE_MOVABLE,
DELETE_TRACKED or ARCHIVE_EXTERNAL_THEN_DELETE_UNTRACKED while it is still
awaiting deputy ratification / U6-E review; and (c) the R-124.3 directive
mandates HOLD for the `Data/external/` rows regardless of mechanical-scan
result. Breakdown by source:

* 1 row -- changed notebook (`fr_singles_results_discussion_v1.ipynb`)
* 15 rows -- new `notebook_dev_v3/` files
* 118 rows -- ten new U6-D attempt directories
* 4 rows -- changed U6-D driver scripts
* 5 rows -- new `__pycache__` build artifacts
* 40 rows -- new EUROMOD-STORAGE priced-cache files (8 `qw_4x` + 32 `xc`)
* 29 rows -- `Data/external/` disposition-override rows (R-124.3; content
  unchanged, classification changed CANONICAL_CURRENT -> HOLD)

212 total.

# 4. THE TWO NEW PRICED CACHES

Both `u6d_ladder_v1.json` records (in `u6dladder_U6D_LADDER_PRICED` and
`u6dladder4x_U6D_LADDER_PRICED`) point `step3_pricing.cache_dir` at the
same directory,
`C:\Users\hisham\MNL\EUROMOD-STORAGE\outputs\p2a_singles2016\region_live_v1\fr_singles_pricing_p2a_qw`.
Walking that directory (and its sibling created for the cross-check
attempts) against file mtimes vs. the v1 cutoff (2026-08-24 14:19:18+0200)
identifies **exactly two new cache trees**, not two new files -- naming
follows the `priced_qw_*` / `priced_xc_*` convention (distinct from the
already-PUBLISHED-pinned `priced_u6_*` cache used by the original U6
pipeline, which is untouched):

1. **`fr_singles_pricing_p2a_qw` (partial-new):** the pre-existing
   directory (its `priced_qw_1x_*` / `priced_qw_2x_*` chunks, 16 files,
   pre-date the cutoff and are already in v1) gained 8 new
   `priced_qw_4x_*` chunks, written 14:29:34-14:37:20 local by the
   `u6dladder4x` attempt.
   Aggregate fingerprint (sha256 of the sorted `name:size:sha256` manifest
   of the 8 new files) = `ffb0832ad1f9a4b84b0177d39d22542d6ce5dbaf853acda5383dd930f5acfba7`
2. **`fr_singles_pricing_p2a_xc` (entirely new):** created after the
   cutoff, 32 files (`priced_xc_ghat_{empty,A,B,AB}_*`, 8 chunks x 4
   variants), written 14:48:09-15:56:19 local by the
   `u6dxc4x`/`u6dxc4xb` cross-check attempts.
   Aggregate fingerprint = `53b3305cfe5ddac7af7cf47523a5bf8d578ad1d6793b04b3633b381be7219ec6`

Per-file sha256 for all 40 files is recorded in the delta register
(`repo_tree=EUROMOD-STORAGE`). "Aggregate fingerprint" above is a
synthesised sha256 over the sorted `filename:size_bytes:sha256` lines of
each tree, computed for this report only (not a field in the register
schema); it is not a substitute for the per-file hashes.

# 5. THE SEVEN STOPPED RECORDS

All ten new U6-D attempt directories are itemised in the register with
HOLD disposition. The seven carrying a stopped/aborted marker:

| Attempt dir suffix | Marker | Reason code |
|---|---|---|
| `u6dgates_STOPPED_ERROR` (u6dgates) | already in v1, unchanged | not part of this delta |
| `u6dgates2_STOPPED_ERROR` | already in v1, unchanged | not part of this delta |
| `u6dgates4_STOPPED_ERROR` | STOPPED_ERROR | aborted run, no citation |
| `u6dgates5_STOPPED_QW-ALIGN` | STOPPED_QW-ALIGN | halted for QW-alignment check, not an error |
| `u6dgates6_STOPPED_QW-ALIGN` | STOPPED_QW-ALIGN | halted for QW-alignment check, not an error |
| `u6dgates4x_STOPPED_ERROR` | STOPPED_ERROR | aborted run, no citation |
| `u6dxc4x_STOPPED_ERROR` | STOPPED_ERROR | aborted run, no citation |

(The task brief listed `u6dgates_STOPPED_ERROR` and
`u6dgates2_STOPPED_ERROR` among "seven STOPPED records" too; both are
already in v1 unchanged and therefore correctly excluded from this delta
register -- five of the seven are new-since-v1 and are the rows above.)

# 6. THE Data/{...} ALL-HOLD DIRECTIVE

Only `Data/external/` exists among the five directive-named directories
(`processed`, `interim`, `external`, `pilot`, `inspecting`) in either
repo -- confirmed by directory search under both `Data/`/`data/` roots in
MNL and Job_Market_paper. 29 files, all TRACKED, all git-clean
(byte-identical to v1, spot-verified by re-hash). v1 had classified all 29
CANONICAL_CURRENT ("presumed live repository material... NOT
independently confirmed by an explicit pin/manifest/contract/manuscript
citation"). Per R-124.3 all 29 are reclassified HOLD in this delta
register; see the governance-gap note below.

# 7. GOVERNANCE GAPS IDENTIFIED

1. **Data/external CANONICAL_CURRENT vs. R-124.3.** v1 classified all 29
   `Data/external/` files CANONICAL_CURRENT on a *presumption* of live
   repository material, explicitly flagging that this was NOT confirmed
   by an actual pin/manifest/contract/manuscript citation. R-124.3 now
   mandates HOLD, listed-only, for this directory regardless. The two are
   in direct tension: v1's own text already conceded the CANONICAL_CURRENT
   call was unconfirmed, so the R-124.3 override is not correcting a
   confident v1 finding, it is replacing an admitted-uncertain default.
   Deputy should confirm R-124.3 is meant to *supersede* v1's Data/
   dispositions going forward, not merely apply prospectively.
2. **v1's DONE-marker precedent for U6-D attempts conflicts with this
   mission's live-evidence rule.** v1 classified the earlier
   `u6dpilot_U6D_PILOT_DONE` and `u6dgates3_U6D_GATES_DONE` directories
   HISTORICAL_IMMUTABLE_IN_PLACE, reasoning "Accepted attempt record:
   attempt directory name carries an accepted/completion status marker."
   This mission's own instruction explicitly forbids that: live U6-D
   evidence must NEVER be classified HISTORICAL_IMMUTABLE_IN_PLACE while
   still awaiting deputy ratification, "even though pricing has stopped."
   The two new DONE-marked directories in this delta
   (`u6dgates7`, `u6dgates4xb`, and `u6dxc4xb`) were therefore classified
   HOLD here, not HISTORICAL_IMMUTABLE_IN_PLACE -- an intentional
   departure from v1's own precedent. **v1's existing rows for
   `u6dpilot_U6D_PILOT_DONE` and `u6dgates3_U6D_GATES_DONE` remain
   HISTORICAL_IMMUTABLE_IN_PLACE on disk (v1 is not touched by this
   read-only pass) and should be revisited by the deputy** -- they may be
   mis-classified under the same rule.
3. **`outputs/p2a_singles2016/notebook_dev_v3/` directory-level ruling
   citation not propagated to file rows.** The reference protection map
   (v1, re-harvested and confirmed unchanged in this pass) records exactly
   one citation: `JMP::docs/Missions/JMP_M08E_E2_closure_notebook_and_RUM_ruling_v1.md`
   cites `outputs/p2a_singles2016/notebook_dev_v3` as a ruling-authorized
   output location, but leaves `resolved_repo` as `?` (unresolved) and v1
   propagated `ruling_ref=False` to every individual file inside that
   directory rather than `True`. All 52 files in the directory (37 from
   v1, 15 new here) are therefore HOLD rather than CANONICAL_CURRENT even
   though the directory itself is affirmatively ruling-cited. Recommend
   the deputy resolve `resolved_repo=MNL` for that citation and decide
   whether directory-level ruling citations should propagate to
   contained-file `ruling_ref` in a future register revision.
4. **EUROMOD-STORAGE scope is confirmed in-scope by v1's own precedent**
   (6,224 EUROMOD-STORAGE rows already exist in v1 with `repo_tree=
   EUROMOD-STORAGE`), so no new scope-ambiguity flag is raised for the
   two new priced-cache trees documented in Section 4 -- they follow the
   same `repo_tree=EUROMOD-STORAGE` / `tracked_status=UNTRACKED` /
   `git_status=NO_VCS` convention v1 already established.
5. **`__pycache__/*.pyc` has no v1 scanning precedent.** v1's register
   contains zero pycache rows. This pass introduces a `git_status=IGNORED`
   flag value (not one of v1's four values: `??`, `clean`, `M`,
   `NO_VCS`) to describe gitignored-but-present build artifacts; the
   deputy should confirm whether build artifacts are meant to be in scope
   at all for future passes, and if so, standardise the git_status
   vocabulary.

# 8. READ-ONLY STATEMENT

This delta pass performed no writes, moves, deletions, renames or commits
in either repository or in EUROMOD-STORAGE. The only artifacts produced
are this file and `JMP_HK_01_inventory_and_disposition_register_v1_1.csv`,
both newly created under `docs/Missions/HK01/`. No existing file --
including the v1 register, v1 summary, v1 reference-protection map, or any
inventoried source path -- was modified, moved or deleted in the course of
this work.
