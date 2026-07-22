# JMP Cross-Repository Documentation Repair Report — v1

Date: 2026-07-22. Role: documentation maintainer. Scope: repair only the active documentation
surfaces that mislead humans or AI/RAG. No estimation, EUROMOD, welfare, post-estimation, notebooks,
or data preparation was run. No scientific code, model specification, parameter/theta file, data, or
estimation-output JSON was modified. The region-live P2a result was **not** promoted; the certified
baseline was **not** changed. Not committed.

---

## 1. Repair verdict

**PASSED WITH WARNINGS.**

All enumerated authorized surfaces were repaired and the four target stale phrases are gone from the
repaired files. Two warnings remain: (a) two active non-archive documents **outside** the authorized
edit set still carry "two active empirical branches" and were flagged, not edited; (b) the P2a
provenance theta pointer is deliberately left **unresolved** (see §8) because the evidence does not
demonstrably single out `theta_p2a_singles_2016_v2.csv`.

## 2. Repositories inspected

| Repository | Path | HEAD | Action |
|---|---|---|---|
| Job_Market_paper | `c:\Users\hisham\Repo\Job_Market_paper` | `5f6b727` | 4 docs repaired |
| MNL | `c:\Users\hisham\Repo\MNL` | `509dca1` | 9 docs/provenance files repaired |
| dclaborsupply-monorepo | `c:\Users\hisham\Repo\MNL\dclaborsupply-monorepo` | `2ea3847` | inspected; no contradiction; **not changed** |

## 3. Job_Market_paper files repaired

- **`README.md`** — retitled to the access/ability/preference framing; replaced the two-way
  "opportunity vs preference" one-paragraph and method language with the three-way cut; removed the
  "empirical model is not yet estimated" status and replaced it with the certified 47-param baseline
  (negLL 238504.6360973987) plus a statement that estimation code/provenance live in `MNL` and
  `dclaborsupply-monorepo`; stated welfare design fixed but results not yet certified; repointed
  authority from `JMP.md` to `JMP_project_state_v1.md`; corrected the `Code/` row (engine is not here);
  named the welfare spec and literature skeleton as canonical; kept microsimulation as an input and
  the Haydar–Maniquet theory paper separate.
- **`CLAUDE.md`** — same three-way replacement; corrected "empirical model is not yet implemented"
  and the "`Code/` empty" / "single commit" claims; stated the estimator/certified estimate live in
  the sibling repos; adjusted the mock-figure notes to say the model is estimated but the plotted
  numbers are placeholders, not the certified estimate.
- **`JMP.md`** — added a dated status banner (model estimated & certified; three-way cut; welfare
  designed not certified; theory paper separate; authority repointed to `JMP_project_state_v1.md`) and
  updated the one two-way decomposition sentence to three-way. The narrative body is retained as
  labelled background.
- **`JMP_project_state_v1.md`** — **headline consistency repair only**: one clarifying sentence after
  the central-question blockquote making explicit that "job opportunities" resolve into the three-way
  access/ability/preference cut (already developed in §2.2/§3.3/§6.1). The substantive document was
  otherwise not rewritten.

## 4. MNL files repaired

- **`README.md`** — added a certified-baseline banner naming `joint_pooled_v1_bll0_tlmpin` as the sole
  certified baseline (negLL 238504.6360973987, JAX, singles 101 / couples 901, synthetic-recovery
  certified, PD real-data Hessian, clustered on `idorighh`); replaced "two active empirical branches"
  with a legacy/provenance framing for continuous-RURO and job-choice; rewrote the "Current Baseline
  Results" section to name the certified baseline and mark the Feb-2026 GAMSPy runs legacy.
- **`docs/estimation/RURO_ACTIVE_RESULTS_REGISTRY.md`** — added a certified-baseline banner; marked the
  listed GAMSPy job-choice/continuous runs LEGACY/provenance; noted the P2a track as separate and
  provisional. Registry body preserved as history.
- **`outputs/p2a_singles2016/P2A_MASTER_RECORD.md`** — repaired the mojibake title (`RURO � P2a` →
  `RURO — P2a`); added a two-vintage banner documenting region-dead (19071.6562, diagnostic/superseded)
  and region-live (19053.4655, provisional, awaiting production rebuild) distinctly; clarified which
  in-folder artifacts are the region-dead (2026-07-12) vintage; did **not** represent region-live as
  accepted; corrected the provenance line to reflect the `_v2` engine-ready parquet and the identical
  v1/v2 theta.
- **`p2a_fit_provenance.json`** — added `theta_pointer_status` (UNRESOLVED, see §8) and `result_status`
  (PROVISIONAL, not accepted, awaiting rebuild). **`theta_csv` and all scientific values left
  unchanged.** File re-parses as valid JSON.
- **`files_structure_detailed.md`** — repaired the corrupted line 7 (`Dot-prefiJMP_ability_opportunity_cut_v1.mdxed`
  → `Dot-prefixed`).

## 5. dclaborsupply files repaired

**None.** The active `README.md` was inspected and does **not** contradict the audit: it already names
the certified FR reproduction (negLL 238504.6360973987), states that `loc_empirical` and
`vw_occupation` have no dedicated JAX implementation and must not be used for JAX estimation, and does
not claim the region-live P2a result is accepted. Per the "do not modify package claims except where an
active README directly contradicts the audit" rule, no edit was made. The documented limitations
(`loc_empirical` / `vw_occupation` not JAX-validated; occupation-conditioned proposal draws ≠ either
structural wage specification) are preserved intact.

## 6. Canonical baseline language

Standardized across all repaired surfaces to: *the sole certified baseline is the 47-parameter pooled
specification `joint_pooled_v1_bll0_tlmpin` — France 2015–2017 pooled; JAX; singles 101 / couples 901
alternatives; negLL 238504.6360973987; synthetic-recovery certified; real-data Hessian positive
definite; clustered inference on `idorighh`.* Estimation code and provenance are stated to live in
`MNL` (`scripts/bpool`) and `dclaborsupply-monorepo` (`packages/dclaborsupply/.../likelihood/engine_jax.py`),
not in the writing repo.

## 7. Three-way decomposition language

Standardized to **access / ability / preference** (wage technology = ability;
market/job/hours/region/occupation availability = access), with the two-way "opportunity vs preference"
split explicitly retired or labelled shorthand. Applied in Job_Market_paper `README.md`, `CLAUDE.md`,
`JMP.md`, and the `JMP_project_state_v1.md` headline clarifier. Matches the canonical framing in
`JMP_literature_review_skeleton_v1.md` and `JMP_welfare_spec_v5.md`.

## 8. P2a provisional-status language

Region-live (target negLL 19053.4655) is labelled **provisional / not accepted / awaiting production
rebuild with strict diagnostics** and is stated as **not safe for inference, manuscript results, or
certified welfare** in `P2A_MASTER_RECORD.md`, `p2a_fit_provenance.json` (`result_status`), and the
MNL results-registry banner. Region-dead (19071.6562) is labelled diagnostic/superseded and preserved
as history.

**Theta pointer decision — UNRESOLVED (evidence-based).** The instruction was to correct the pointer
only if the region-live result *demonstrably* uses `theta_p2a_singles_2016_v2.csv`, else mark it
unresolved. Direct comparison shows `theta_p2a_singles_2016_v1.csv` and `_v2.csv` contain the **same
region-live theta**, identical to float precision (both `beta_E = -0.752653`, region/urb/gsur populated:
`beta_E_gsur -1.3062`, `beta_E_drgur -0.5305`). v1 is **not** region-dead. Because it is not
demonstrable that the fit uses v2 specifically, the `theta_csv` value was **left unchanged** and an
explicit `theta_pointer_status: UNRESOLVED` note was added instead of guessing. (This corrects the
earlier audit's assumption that v1 was region-dead.)

## 9. Corruption repairs

| File | Corruption | Repair |
|---|---|---|
| `MNL/files_structure_detailed.md` L7 | filename spliced into a word: `Dot-prefiJMP_ability_opportunity_cut_v1.mdxed` | restored to `Dot-prefixed` |
| `MNL/outputs/p2a_singles2016/P2A_MASTER_RECORD.md` L1 | mojibake replacement char in the title (`RURO � P2a`) | restored to `RURO — P2a` |

`MNL/Project_files_structure.md` remains UTF-16 LE by design; a banner was prepended preserving that
encoding (BOM `FF FE` retained) rather than re-encoding the file.

## 10. Remaining stale or historical files

**Warnings — active, misleading, but outside the authorized edit set (flagged, not edited):**
- `MNL/docs/methods/RURO_METHODS_AND_PIPELINE_MANUAL_v1.md:58` — "There are two active empirical
  branches." **Still requires repair** (not in the authorized file list this pass).
- `MNL/docs/mirrored/root/README.md:3` — a mirror of the old root README, still says "two active
  empirical branches." **Still requires repair** (re-sync the mirror from the repaired root `README.md`).

**Intentionally historical (correctly labelled, no further action):**
- `MNL/Project_files_structure.md`, `RURO_MNL_project_files_structure.md`, `01_repo_inventory.md`,
  `03_migration_matrix.md` — now carry dated historical-snapshot banners.
- `MNL/files_structure_detailed.md` — a dated (2026-06-13) generated inventory; corruption repaired;
  content is a self-describing snapshot.
- Job_Market_paper `JMP.md`, `notes.md` — retained as labelled background; `JMP.md` carries the new
  status banner.
- All `docs/archive/**` occurrences of the target phrases — correctly quarantined; not touched.
- The cross-repo audit docs (`JMP_cross_repo_*_v1.md`) quote the old phrases as findings; those are
  intentional references, not live claims.

## 11. Validation searches

Search over active, non-archive `.md` (excluding `.git`, `docs/archive/**`, and this report):

| Phrase | Active hits (excluding audit/repair docs that quote them as findings) | Status |
|---|---|---|
| "model is not yet estimated" | none | repaired (only the staleness-audit doc quotes it) |
| "model is not yet implemented" | none | repaired (only audit/handoff docs quote it) |
| "two active empirical branches" | `RURO_METHODS_AND_PIPELINE_MANUAL_v1.md:58`; `docs/mirrored/root/README.md:3` | **still requiring repair** (out of authorized scope) |
| "opportunity component and preference component" | none | not present in active docs |

Classification of remaining occurrences:
- **Intentionally historical:** archive-path hits; audit/handoff docs quoting old text as findings.
- **Locally correct:** the repaired root `README.md`/`RURO_ACTIVE_RESULTS_REGISTRY.md` now say "two
  historical empirical branches" / "LEGACY" (not the stale claim).
- **Still requiring repair:** the methods manual and the mirrored root README (§10 warnings).

Other validations:
- `p2a_fit_provenance.json` re-parses as **valid JSON**; `theta_csv` and `negll_fit` unchanged.
- **No scientific artifact changed:** a name-only diff filtered for `*.parquet`, `*.csv`, `*.yaml`,
  `*.yml`, and `estimation_results*.json` returns **nothing** in MNL; nothing of the kind in the other
  repos. Only documentation and the authorized provenance JSON were touched.

## 12. Files intentionally not changed

- **Certified baseline scientific artifacts** — `scripts/bpool/specs/estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml`,
  `theta_hat_realdata_901_v1.csv`, execution logs, `estimation_results*.json` — untouched.
- **P2a scientific artifacts** — `estimation_results_p2a_singles2016.json`, `theta_p2a_singles_2016_v1/v2.csv`,
  `p2a_se_clustered.csv`, `*.parquet`, `*_mnlmeta.json`, diagnostics/solver JSONs, PNGs — untouched.
- **`p2a_fit_provenance.json` scientific values** — `negll_fit`, `theta_csv`, `engine_ready`, `pinned`,
  `at_bound`, `band_convention`, `draws_design`, `repair_note` — unchanged; only two status/annotation
  fields added.
- **dclaborsupply package docs/code** — not modified (README inspected, no contradiction).
- **Out-of-scope active docs** — `RURO_METHODS_AND_PIPELINE_MANUAL_v1.md` and `docs/mirrored/root/README.md`
  — flagged, not edited.

**Observation (transparency):** during the session the working-tree copies of
`P2A_MASTER_RECORD.md` and `p2a_fit_provenance.json` were modified by an external process/user (I did
not make those changes and ran no reset/checkout). Relative to committed `HEAD` (`509dca1`), which
already carried negLL 19053.4655, the only differences in those two files are my documentation/provenance
annotations. No scientific content was altered by me.

## 13. Git diff summary

**Job_Market_paper** (`git diff --stat`, tracked):
```
 CLAUDE.md               | 16 ++++++++--------
 JMP.md                  |  9 +++++++--
 JMP_project_state_v1.md |  2 ++
 README.md               | 31 ++++++++++++++++++-------------
 4 files changed, 35 insertions(+), 23 deletions(-)
```
Untracked (new): `docs/JMP_cross_repo_documentation_repair_report_v1.md` (this file), plus the four
prior cross-repo audit docs from the preceding audit pass.

**MNL** (`git diff --stat`, excluding the `dclaborsupply-monorepo` gitlink):
```
 01_repo_inventory.md                            |   2 ++
 03_migration_matrix.md                          |   2 ++
 Project_files_structure.md                      | Bin 5281220 -> 5281888 bytes
 README.md                                       |  42 +++++++++++++++++--------
 RURO_MNL_project_files_structure.md             |   2 ++
 docs/estimation/RURO_ACTIVE_RESULTS_REGISTRY.md |   8 +++-
 files_structure_detailed.md                     |   2 +-
 outputs/p2a_singles2016/P2A_MASTER_RECORD.md    |  13 ++++++--
 p2a_fit_provenance.json                         |   4 ++-
 9 files changed, 56 insertions(+), 19 deletions(-)
```
(`Project_files_structure.md` is a binary/UTF-16 diff = the prepended banner; the two `LF→CRLF`
warnings are cosmetic line-ending notices, no content impact.) Pre-existing modified file
`.claude/settings.local.json` and the `dclaborsupply-monorepo` gitlink (dirty due to its new untracked
audit file) are not part of this repair.

**dclaborsupply-monorepo** (`git diff --stat`): **empty** — no tracked changes. (Its only untracked
file is the validation doc from the preceding audit pass.)

## 14. Immediate next action

Two housekeeping repairs remain, both outside this pass's authorized edit set — repair
`MNL/docs/methods/RURO_METHODS_AND_PIPELINE_MANUAL_v1.md` (line 58 "two active empirical branches") and
re-sync `MNL/docs/mirrored/root/README.md` from the repaired root `README.md`. These are documentation
warnings only; they do not affect the certified baseline or the provisional status of region-live. The
substantive technical next gate is unchanged: **production rebuild of the FR-2016 singles P2a
region-live fit with strict diagnostics** before any promotion (see
`FR_P2a_region_live_promotion_readiness_v1.md`). Do not commit automatically.
