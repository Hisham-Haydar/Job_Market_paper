# JMP Cross-Repository Manager Handoff — v1

Read-only cross-repository state audit. Date: 2026-07-22. Auditor: automated cross-repo audit
per `Job_Market_paper/docs/prompts/JMP_cross_repo_state_audit_prompt_v1.md`.

**Scope discipline.** This is a read-only analytical handoff. No estimation, EUROMOD, or notebook
was run; no code, spec, data, output, or existing document was modified. Evidence from committed
files and artifacts overrides prose claims. This document does not change the active baseline and
does not declare welfare readiness.

**Two final verdicts (see §16–17 and the companion docs):**
- Cross-repository coherence: **COHERENT WITH DOCUMENTATION REPAIRS.**
- FR P2a region-live: **READY AFTER PRODUCTION REBUILD** (details in
  `dclaborsupply-monorepo/docs/validation/FR_P2a_region_live_promotion_readiness_v1.md`).

---

## 1. Repository identities

All three repositories are on `main` and are **exactly one commit ahead** of the reference anchors
in the audit prompt. Every reference commit is present in local history (no rewind/divergence);
the extra commit in each is newer legitimate work. Per the LOCAL-STATE RULE, the actual current
local state is audited below.

| Repository | Local path | Branch | Local HEAD | Reference anchor | Divergence | Working tree |
|---|---|---|---|---|---|---|
| Job_Market_paper | `c:\Users\hisham\Repo\Job_Market_paper` | main | `5f6b727` | `c7a8cad` | +1 ahead | clean |
| MNL | `c:\Users\hisham\Repo\MNL` | main | `509dca1` | `0daab08` | +1 ahead | 1 unstaged: `.claude/settings.local.json` |
| dclaborsupply-monorepo | `c:\Users\hisham\Repo\MNL\dclaborsupply-monorepo` (nested inside MNL working tree; separate repo, own `origin`) | main | `2ea3847` | `6bcbc92` | +1 ahead | clean |

The one commit ahead in each:
- Job_Market_paper `5f6b727` — "Create cross-repo state audit prompt for JMP" (the prompt driving this audit).
- MNL `509dca1` — "Update P2A Singles 2016 Outputs and Configuration Files" (propagates region-live values; see §7).
- dclaborsupply `2ea3847` — "Refactor fr_data_walkthrough and fr_singles_pipeline notebooks."

None of these three repositories are at the exact reference commit; each is one clean commit newer.
This is a benign fast-forward divergence, not corruption.

## 2. Repository role allocation

| Repository | Authoritative role |
|---|---|
| **Job_Market_paper** | **Research / writing.** Project-state memos, welfare design spec, literature corpus and review skeleton, contribution framing. Contains **no** estimation or welfare engine code (the referenced `Code/` directory does not exist). |
| **MNL** | **Certified provenance and legacy pipeline** — *and* the current working host for the active FR-2016 singles P2a track. Holds the certified 47-param spec, theta, execution logs and diagnostics; the legacy GAMSPy/CONOPT, continuous-RURO, job-choice, corrected-P3a and NC-pilot branches; and the committed P2a singles-2016 outputs + welfare scripts. |
| **dclaborsupply-monorepo** | **Reusable package / application layer.** Two-package monorepo (`dclaborsupply` core + `dclaborsupply_app`) carrying the validated JAX likelihood engine (`likelihood/engine_jax.py`), NumPy reference, loaders, spec parser, solvers, SE, diagnostics, welfare. Also holds the P2a exploratory notebooks (`fr_data_walkthrough.ipynb`, `fr_singles_pipeline_v1.ipynb`). |

Note the coupling risk: the P2a track's **producing code** (notebooks + the certified spec YAML + engine)
lives in dclaborsupply and MNL, but its **artifacts** are written into MNL and into the local
`EUROMOD-STORAGE` store. Data inputs and the active spec YAML are external to dclaborsupply.

## 3. Current JMP research question

Empirical structural JMP on **latent jobs, money-metric welfare, and an access / ability / preference
decomposition of welfare inequality.** Current canonical framing (newest docs — `JMP_literature_review_skeleton_v1.md`
line 6, `JMP_welfare_spec_v5.md`, `JMP_project_state_v1.md` §6.1): how much of inequality in
money-metric well-being is due to **unequal access** to jobs vs **ability** (wage technology) vs
**heterogeneous preferences**, once labour supply is a choice among latent jobs. The obsolete
**two-way "opportunity vs preference"** split is explicitly retired in the skeleton but still persists
in stale root docs (see §15 and the staleness audit). Distinct from the separate Haydar–Maniquet
axiomatic theory paper.

## 4. Current contribution

Consistent treatment of opportunity across three layers with a single estimated opportunity density:
(1) structural latent-jobs labour-supply estimation, (2) ex-ante household money-metric welfare
(preference-respecting equivalent income, W¹–W⁶ family), (3) Shapley–Shorrocks decomposition of
welfare inequality into access, ability and preference. Explicitly **not** a country ranking.

## 5. Formal active baseline

**The 47-parameter pooled specification `joint_pooled_v1_bll0_tlmpin`** — and nothing else.

- France pooled 2015–2017; JAX backend; couples 901 alternatives (30×30 joint grid + chosen),
  singles 101 alternatives.
- Spec: `MNL/scripts/bpool/specs/estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml`
  (48→47 free: `beta_ll` fixed 0, `theta_l_m` pinned −0.8).
- Certified **negLL = 238504.636097** (execution log
  `MNL/docs/France_case/P3a/execution_logs/Bpool/RURO_realdata_2016_2017_joint_901_v1.md`).
- Real-data Hessian **PD, min_eig +0.459**, cond 1.295e6, "SEPARATELY IDENTIFIED"; cluster-robust SE
  on `idorighh` (9657 clusters). Synthetic-recovery certified (901 Check-5 re-gate, PD min_eig +1.706).
- Reproduced **bit-for-bit** by the NumPy engine, the JAX engine and `compute_index`
  (`|lift − certified| = 0.0e+00`, `03_migration_matrix.md`).

The **49-param `gsplit`** variant is **NOT** the baseline: it failed the synthetic-recovery gate
(3/4 relaxed params do not recover; tight-SE bias) despite a PD real-data Hessian. The 47-param
spec remains certified. The FR-2016 singles P2a region-live fit (§7) is a **separate singles-only
track**, not a candidate to replace this pooled baseline.

## 6. Current pooled-estimation status

**Settled / historical.** The certified 47-param pooled baseline is complete, PD, synthetically
recovered, independently reproduced, and cluster-robust. No open pooled-estimation task. Active
momentum has moved to the singles-2016 P2a track and welfare measurement built on top of the baseline.

## 7. Current singles-P2a status

**Provisional / diagnostic — data-wiring repair propagated, but NOT production-rebuilt or strictly
diagnosed.** Classification: **diagnostic result with a propagated (not re-estimated) improvement;
promotion-blocked.**

- Track: FR 2016 singles, 1,555 households (841 female + 714 male), certified B-pool draws, 101 alts.
- Two results: **region-dead negLL 19071.6562** (region/urbanisation/gsur columns zero-stubbed at
  engine-ready assembly) and **region-live negLL 19053.4655** (those columns revived). ΔnegLL ≈ 18.19.
- The region-live improvement is a **corrected data-wiring bug, not a specification change**: same
  spec (`vw`), same bounds, same start, same JAX engine; region/urb/gsur (`drgn1, drgur, drgmd,
  drgru, gsur`) were repopulated from source into `fr_singles_engine_ready_p2a_bpool_v2.parquet`,
  `beta_E` moved −4.31→−2.90 (it had been absorbing regional variation).
- **Where region-live lives:** the fit itself is a single executed notebook cell (P2a-10 in
  `fr_data_walkthrough.ipynb`, iters=353, converged). Its values were then **propagated into MNL's
  committed artifacts** (`outputs/p2a_singles2016/estimation_results_*.json` summary joint_ll
  −19053.4655; `p2a_fit_provenance.json`; `theta_p2a_singles_2016_v2.csv`; engine-ready `_v2` parquet
  + mnlmeta) by a script recorded as `command_line = propagate_regionlive.py` (MNL commit `509dca1`).
- **What is MISSING for region-live** (see §13 of the promotion-readiness doc): region-live Hessian /
  eigenvalues / rank / condition number; region-live gradient; region-live cluster-robust SE;
  region-live post-estimation report; verified cold-reload anchor at 19053.4655; and the producing
  script `propagate_regionlive.py` itself (not on disk in either repo, no git record). The committed
  SE CSV, solver diagnostics, all post-estimation PNGs and `P2A_MASTER_RECORD.md` are the **region-dead
  (2026-07-12) vintage**; only three files (results JSON, `_v2` parquet, mnlmeta) were regenerated
  region-live (2026-07-13). Region-dead diagnostics showed **five near-zero eigenvalues loading on the
  region block** — the very identification question the repair must resolve is unverified.

## 8. Current couples status

**Settled inside the certified pooled baseline** (couples 901, N=7,438). No separate active couples
track. The couples-specific gender-split relaxation (`gsplit`) was tried and rejected on synthetic ID.

## 9. Current welfare status

**Designed and core-validated on W³ only — NOT ready; no welfare finding certified.** Do not declare
welfare readiness.

- `JMP_welfare_spec_v5.md` is a **design memo** (W¹–W⁶ family, ex-ante household money-metric
  equivalent income, Exercise A menu vs Exercise B source decomposition). It explicitly does not
  authorise implementation.
- A welfare computational core exists in the P2a track: `MNL/scripts/welfare/run_p2a_singles_welfare.py`
  produced `EUROMOD-STORAGE/outputs/welfare/p2a_singles2016/` (V_i^IS + W1/W3/W4/W6 + inequality;
  W3 zero-recovery ~2e-10, ESS/parity checks pass). **These welfare outputs were recomputed on the
  un-rebuilt region-live theta** (theta_hash `5f3722dc`): pooled Gini **W1 0.176 / W4 0.261 / W6 ~**,
  with W4 median compensation jumping **4364→8505 EUR (+95%)** vs the region-dead theta. Welfare
  therefore **inherits the provisional region-live status** and its own thin-ESS / EUROMOD reprice-parity
  blockers noted in the writing repo. No decomposition (Exercise B) is implemented.

## 10. Current literature and writing status

Literature corpus and pipeline are the dominant activity in Job_Market_paper (tiered summaries T1A/T1B/T2,
indexes INDEX_00–08 with v2 supersessions, DR03 control files). The newest substantive writing artifact
is `JMP_literature_review_skeleton_v1.md` (2026-06-05), which sets the current canonical
access/ability/preference framing and a closest-competitor table. No manuscript body/`Code/` yet.
The state anchors are `JMP_project_state_v1.md` + `JMP_welfare_spec_v5.md` (both 2026-06-02).

## 11. Accepted results

- **Certified 47-param pooled baseline** `joint_pooled_v1_bll0_tlmpin`, negLL 238504.636097, PD Hessian
  (real-data min_eig +0.459), cluster-robust SE, synthetic-recovery certified, triple-engine reproduced.
  Safe for warm start, inference, and writing.

## 12. Provisional results

- **FR 2016 singles P2a region-live fit**, negLL 19053.4655 (data-wiring repair; converged in a notebook
  cell; propagated to committed artifacts). Not strictly diagnosed. Not safe for inference/welfare/writing
  until production-rebuilt.
- **P2a singles welfare / inequality** (Gini W1 0.176 / W4 0.261) computed on the provisional region-live
  theta. Provisional; not a certified welfare finding.

## 13. Diagnostic-only results

- **Region-dead P2a fit**, negLL 19071.6562, with a flat regional direction (5 near-zero eigenvalues) —
  now understood as an artifact of the zero-stub wiring bug. Retain as the diagnostic baseline that
  motivates the repair; not a result.
- **49-param `gsplit`** — diagnostic evidence that pooling-relaxation is not synthetically identified
  (tight-SE bias). Not a baseline.

## 14. Superseded or invalid results

- `RURO_ACTIVE_RESULTS_REGISTRY.md` "current baseline runs" (continuous-RURO v3, job-choice M2h/M2e,
  Feb-2026 GAMSPy) — **superseded** by the certified JAX joint-pooled baseline; the registry omits it.
- Legacy GAMSPy/CONOPT, continuous-RURO, job-choice, corrected-P3a, NC-pilot branches — superseded;
  correctly quarantined under `docs/archive/**` and `outputs/estimates/**/gamspy/**`, but still
  advertised as "active" by the MNL root `README.md`.
- Region-dead committed P2a **post-estimation artifacts** (SE CSV, solver diagnostics, PNGs, master
  record) are superseded by the region-live values but were **not regenerated** — they are stale-in-place.

## 15. Cross-repository contradictions

1. **"Model not estimated" vs certified estimate.** Job_Market_paper `CLAUDE.md`, `README.md`, `JMP.md`
   state the empirical model is not yet implemented/estimated and `Code/` is empty; the model is in fact
   certified (47-param baseline). `Code/` does not exist. **High priority — misleads AI/RAG.**
2. **Two-factor vs three-factor framing.** README/CLAUDE/JMP/notes use "opportunity vs preference";
   current canon is access/ability/preference (skeleton labels the two-way split "obsolete").
3. **P2a master record vs its own JSON.** `MNL/outputs/p2a_singles2016/P2A_MASTER_RECORD.md` documents
   negLL 19071.6562 and the old parquet, while the sibling `estimation_results_*.json` /
   `p2a_fit_provenance.json` now carry 19053.4655 and `_v2` parquet. Internal inconsistency after `509dca1`.
4. **Provenance theta pointer.** `p2a_fit_provenance.json` `theta_csv` still points to `_v1`, though
   `509dca1` created the region-live `theta_p2a_singles_2016_v2.csv`.
5. **Active-results registry vs certified baseline** (see §14).
6. **Welfare-folder location claims.** Repo-local `outputs/welfare/` has no P2a folder; the P2a welfare
   outputs live in the canonical `EUROMOD-STORAGE/outputs/welfare/p2a_singles2016/` (confirmed present).
7. **File corruption:** `MNL/files_structure_detailed.md` line 7 has a filename spliced into a word
   (`Dot-prefiJMP_ability_opportunity_cut_v1.mdxed`); `P2A_MASTER_RECORD.md` line 1 mojibake;
   `Project_files_structure.md` is UTF-16 garble.

None of these contradictions touches the validity of the certified 47-param baseline. They are
documentation/artifact-hygiene defects, hence the "COHERENT WITH DOCUMENTATION REPAIRS" verdict.

## 16. Current blocker

The FR-2016 singles P2a **region-live fit exists only as a notebook cell + a propagated artifact set
produced by a now-missing script**, with **no strict diagnostics** (Hessian/eigenvalues/rank, gradient,
cluster-robust SE, post-estimation) and **no verified joint identification** of the region/urbanisation
parameters it activates — while its numbers have already flowed downstream into committed welfare
results. It cannot be promoted, and welfare built on it cannot be certified, until it is rebuilt through
production code with a full diagnostic bundle. Secondary blocker: stale root documentation in
Job_Market_paper and MNL that would mislead any AI/RAG reader about project state.

## 17. Recommended next gate

**One gate:** *Production rebuild of the FR-2016 singles P2a region-live fit through the reusable
`dclaborsupply` package/exports path (not a notebook), emitting a committed, reproducible artifact
bundle: engine-ready `_v2` parquet provenance, theta CSV, estimation JSON, optimizer status, gradient,
**PD Hessian with eigenvalues / rank / condition number confirming joint identification of region ×
urbanisation**, cluster-robust SE (cluster=idorighh), post-estimation report, a committed
`propagate/rebuild` script, and a verified cold-reload regression anchor at negLL 19053.4655 — without
promoting the result or altering the certified 47-param baseline.*

Passing this gate yields a strict-estimation verdict for region-live and unblocks a re-examination of
the P2a welfare numbers. The documentation repairs in §15 are a required **parallel** housekeeping action
(they gate safe AI/RAG handoff) but are not the technical gate.

## 18. Files the manager must inspect

Certified baseline / provenance:
- `MNL/docs/France_case/P3a/execution_logs/Bpool/RURO_realdata_2016_2017_joint_901_v1.md` (negLL, Hessian, SE)
- `MNL/scripts/bpool/specs/estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml`,
  `theta_hat_realdata_901_v1.csv`
- `MNL/docs/France_case/P3a/execution_logs/Bpool/RURO_jax_recovery_gate_gsplit_901_v1.md` (gsplit rejection)

P2a region-live:
- `MNL/outputs/p2a_singles2016/` (whole folder — note the region-dead/region-live vintage split by mtime)
- `MNL/p2a_fit_provenance.json`, `MNL/theta_p2a_singles_2016_v2.csv`
- `dclaborsupply-monorepo/notebooks/fr_data_walkthrough.ipynb` (cells P2a-9, P2a-10, `regionlive00`–`05`)
- `dclaborsupply-monorepo/notebooks/fr_singles_pipeline_v1.ipynb` (still region-dead only)
- `EUROMOD-STORAGE/outputs/welfare/p2a_singles2016/` (welfare recomputed on region-live theta)

Writing / staleness:
- `Job_Market_paper/JMP_project_state_v1.md`, `JMP_welfare_spec_v5.md`, `JMP_literature_review_skeleton_v1.md`
- `Job_Market_paper/CLAUDE.md`, `README.md`, `JMP.md` (stale — see staleness audit)
- `MNL/docs/estimation/RURO_ACTIVE_RESULTS_REGISTRY.md`, `MNL/README.md`, `MNL/files_structure_detailed.md`

Companion audit documents (this batch):
- `Job_Market_paper/docs/JMP_cross_repo_artifact_manifest_v1.md`
- `Job_Market_paper/docs/JMP_cross_repo_documentation_staleness_audit_v1.md`
- `Job_Market_paper/docs/JMP_open_decisions_cross_repo_v1.md`
- `dclaborsupply-monorepo/docs/validation/FR_P2a_region_live_promotion_readiness_v1.md`
