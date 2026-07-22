# JMP Cross-Repository Documentation Staleness Audit — v1

Read-only. Date: 2026-07-22. Companion to `JMP_cross_repo_manager_handoff_v1.md`.

Every item below is a documentation/artifact defect that could mislead a human or an AI/RAG reader.
None invalidates the certified 47-param baseline. Proposed actions are **archive** (move to an
archive path, keep history), **rewrite** (correct in place), or **repair** (fix a corrupted byte/line).
No file was modified by this audit.

---

## 1. Stale research-question language

| # | Repo · File · Loc | Stale claim | Current truth | Action |
|---|---|---|---|---|
| 1.1 | Job_Market_paper · `README.md` L11–13, L21–23 | "decomposes welfare inequality into an opportunity component and a preference component… central throughout" | Three-way access/ability/preference cut (skeleton L6 calls two-way "obsolete") | **rewrite** |
| 1.2 | Job_Market_paper · `CLAUDE.md` L13–15 | two-factor opportunity/preference decomposition; "keep that distinction central" | same as 1.1 | **rewrite** |
| 1.3 | Job_Market_paper · `JMP.md` L23, L35 | "decomposition into opportunity and preference components" | same as 1.1 | **rewrite** (or archive; see 6.3) |
| 1.4 | Job_Market_paper · `notes.md` L10 | two-component framing | raw historical notes | **archive** (mark historical) |
| 1.5 | Job_Market_paper · `JMP_project_state_v1.md` §1.1 headline RQ (L18, L24–27) | headline still "opportunity vs preference," though §6.1 develops the three-way cut | three-way cut is canon | **rewrite** headline only (doc is otherwise current) |

## 2. Obsolete two-factor opportunity/preference language

Same offenders as §1 (README, CLAUDE, JMP, notes). The canonical replacement wording is fixed in
`JMP_literature_review_skeleton_v1.md` L6: *"access / ability / preference three-way cut throughout
(never the obsolete two-way opportunity/preference split). Wage technology = ability;
market/job/hours/region/occupation availability = access."* Use that phrasing verbatim in the rewrites.
**Action:** rewrite README/CLAUDE/JMP to the three-way cut; keep `notes.md` as historical.

## 3. Documents incorrectly saying the model is not estimated

| # | Repo · File · Loc | False claim | Truth | Action |
|---|---|---|---|---|
| 3.1 | Job_Market_paper · `CLAUDE.md` L7, L27, L31 | "empirical model is not yet implemented"; "`Code/` … currently empty"; "the repo has a single commit" | model is certified (47-param baseline); `Code/` does not exist; repo has 20+ commits | **rewrite** (highest priority — actively misdirects AI) |
| 3.2 | Job_Market_paper · `README.md` L37, L49 | "The empirical model is not yet estimated — all figures are mock/illustrative"; references `Code/` | estimated & certified; engine lives in MNL/dclaborsupply, not here | **rewrite** |
| 3.3 | Job_Market_paper · `JMP.md` "Work already done" / "What remains" (L23, L37–43) | frames project as pre-implementation ("first task is to implement the minimal prototype") | model estimated; welfare core built (W³) | **rewrite or archive**; stop labelling it "authoritative" |

## 4. Obsolete baselines

| # | Repo · File | Stale baseline claim | Action |
|---|---|---|---|
| 4.1 | MNL · `docs/estimation/RURO_ACTIVE_RESULTS_REGISTRY.md` | lists continuous-RURO v3 + job-choice M2h/M2e (Feb-2026 GAMSPy) as "current baseline runs"; omits the certified 47-param JAX joint-pooled baseline | **rewrite** to name `joint_pooled_v1_bll0_tlmpin` (negLL 238504.636097) as the sole certified baseline; move the GAMSPy runs to a "legacy" section |
| 4.2 | MNL · `README.md` | "two active empirical branches: continuous RURO + job-choice RURO"; production in `scripts/enhanced/` + `scripts/Job_model/` | **rewrite** to point at `scripts/bpool` joint-pooled baseline; mark continuous/job-choice legacy |
| 4.3 | MNL · `outputs/p2a_singles2016/P2A_MASTER_RECORD.md` L3, L14 | documents negLL **19071.6562** (region-dead) and old engine-ready parquet, while sibling JSON/provenance now carry **19053.4655** and `_v2` | **rewrite** (or add a region-live addendum) so provenance matches its own artifacts; do NOT delete the region-dead record — mark it region-dead explicitly |

## 5. Stale active-results registries

Covered by 4.1 (`RURO_ACTIVE_RESULTS_REGISTRY.md`). Additionally:
- MNL · `p2a_fit_provenance.json` — `theta_csv` field points to `_v1` (region-dead) while `509dca1`
  created region-live `theta_p2a_singles_2016_v2.csv`. **repair** the pointer to `_v2` (or document
  which theta is authoritative). Ambiguous provenance is a promotion blocker.
- MNL · `01_repo_inventory.md`, `03_migration_matrix.md` — dated audit snapshots; `01` self-notes it
  is ad-hoc and "can be deleted." Trustworthy for the baseline (they reproduce 238504.6360973987) but
  should be **archived** with dates to avoid being read as live status.

## 6. Misleading Claude/RAG instructions

| # | Repo · File | Problem | Action |
|---|---|---|---|
| 6.1 | Job_Market_paper · `CLAUDE.md` | instructs AI that the model is unbuilt, `Code/` empty, two-factor split central, decomposition shares are "placeholders for a not-yet-run model"; points to stale `JMP.md` as authoritative | **rewrite**; repoint "authoritative" to `JMP_project_state_v1.md` |
| 6.2 | Job_Market_paper · `README.md` | reinforces 6.1 for human readers; references non-existent `Code/` | **rewrite** |
| 6.3 | Job_Market_paper · `JMP.md` | labelled "authoritative" by README/CLAUDE but is pre-estimation | **rewrite or archive**; remove the "authoritative" pointer |

MNL has **no** root `CLAUDE.md` (searched; none) — no MNL AI-instruction file to repair, but its stale
`README.md`/registry (4.1–4.2) play the same misleading role for RAG.

## 7. Accidental file corruption

| # | Repo · File · Loc | Corruption (verbatim) | Action |
|---|---|---|---|
| 7.1 | MNL · `files_structure_detailed.md` **line 7** | `…Dot-prefiJMP_ability_opportunity_cut_v1.mdxed files outside excluded directories remain included.` — the word "Dot-prefixed" has the filename `JMP_ability_opportunity_cut_v1.md` spliced into it (a corrupt find/replace) | **repair** line 7 to read "Dot-prefixed" |
| 7.2 | MNL · `outputs/p2a_singles2016/P2A_MASTER_RECORD.md` **line 1** | `# FR 2016 Singles RURO � P2a Rebuild Master Record` — mojibake replacement char (encoding damage) | **repair** the byte (likely an em-dash) |
| 7.3 | MNL · `Project_files_structure.md` | entire file is UTF-16 / spaced-byte garble (`��F o l d e r  P A T H…`), a raw Windows `tree` dump | **repair** (re-export as UTF-8) or **archive** |
| 7.4 | MNL · `RURO_MNL_project_files_structure.md` | stale snapshot "Generated 2026-05-12" from the deleted `U:\…\MNL` path | **archive** |

## 8. Exact proposed replacement / archival actions (summary checklist)

Job_Market_paper (writing repo):
1. **rewrite** `CLAUDE.md`, `README.md`, `JMP.md` — certified 47-param baseline; welfare core W³-validated,
   not ready; access/ability/preference cut; engine lives in MNL/dclaborsupply; remove `Code/` claims.
2. **rewrite** `JMP_project_state_v1.md` §1.1 headline RQ to the three-way cut (rest is current).
3. **repoint** "authoritative document" to `JMP_project_state_v1.md`; **archive** `notes.md` as historical.
4. Create the promised `RURO_welfare_scaffold_design_contract_v2.md` only when welfare implementation is
   authorised (not now).

MNL (provenance/legacy repo):
5. **rewrite** `RURO_ACTIVE_RESULTS_REGISTRY.md` and `README.md` to make `joint_pooled_v1_bll0_tlmpin`
   the sole certified baseline and clearly quarantine continuous/job-choice/GAMSPy as legacy.
6. **rewrite/addendum** `P2A_MASTER_RECORD.md` so it matches the region-live JSON, or explicitly label
   itself the region-dead record; **repair** the `theta_csv` pointer in `p2a_fit_provenance.json`.
7. **repair** `files_structure_detailed.md` L7, `P2A_MASTER_RECORD.md` L1; **repair/archive**
   `Project_files_structure.md`, `RURO_MNL_project_files_structure.md`.
8. **archive** `01_repo_inventory.md`, dated audit snapshots, stray root logs (`debug.log`,
   `gate_gsplit_901_run.log`, `gate_output.txt`) and superseded root parquet/theta clutter
   (`fr_singles_engine_ready_v1..v5*.parquet`, `theta_trial_singles_2016_*`).

dclaborsupply (package repo):
9. Add a header note to `fr_singles_pipeline_v1.ipynb` stating it reproduces **region-dead only**
   (19071.6562), so it is not mistaken for the current pipeline.

**Do not delete** any superseded doc — archive with a dated marker so history and provenance survive.
The certified baseline docs (`RURO_realdata_2016_2017_joint_901_v1.md`, the spec YAML, theta CSV,
`03_migration_matrix.md`, `JMP_project_state_v1.md`, `JMP_welfare_spec_v5.md`,
`JMP_literature_review_skeleton_v1.md`) are current and require **no** change beyond items 2 and 5–6 above.
