# JMP Cross-Repository Artifact Manifest — v1

Read-only. Date: 2026-07-22. Companion to `JMP_cross_repo_manager_handoff_v1.md`.

Status vocabulary: **canonical** (certified reference), **accepted** (validated result),
**provisional** (real but not strictly diagnosed), **diagnostic** (informative, not a result),
**superseded** (replaced), **invalid** (rejected). Safety flags are conservative: a "no" means
"not demonstrated by committed evidence," not necessarily "known wrong." Paths are repo-relative
unless prefixed with `EUROMOD-STORAGE/` (canonical local store `C:\Users\hisham\MNL\EUROMOD-STORAGE`,
git-excluded).

---

## A. Certified pooled baseline (canonical)

**Artifact:** Certified 47-param pooled joint estimate `joint_pooled_v1_bll0_tlmpin`
- Repository: MNL
- Path: `docs/France_case/P3a/execution_logs/Bpool/RURO_realdata_2016_2017_joint_901_v1.md`
  (embedded results JSON); `EUROMOD-STORAGE/outputs/post_estimation/realdata_joint_901_tlmpin_certified/joint/`
- Track: pooled 2015–2017, couples 901 / singles 101
- Producing code: `scripts/bpool` JAX estimator (engine = dclaborsupply `likelihood/engine_jax.py`, lifted from `scripts/bpool/jax_ll_probe.py` + `jax_joint_hessian.py`)
- Upstream data: `EUROMOD-STORAGE/new_data/fr_p3a_bpool_engine_ready__{singles,couples,mnlmeta}`
- Status: **canonical**
- Headline: **negLL 238504.636097**; real-data Hessian PD, min_eig +0.459, cond 1.295e6; cluster-robust SE (idorighh, 9657 clusters); synthetic recovery certified (901 Check-5 min_eig +1.706); triple-engine reproduced (|Δ|=0)
- Safe for warm start: **yes** · inference: **yes** · writing: **yes** · welfare: **yes** (as the structural input)
- Caveats: `beta_l0_m` couples-male leisure at floor (leisure block wide SEs by design); comment block in the YAML mislabels the param count as 49 in places (authoritative free count is 47).

**Artifact:** Certified theta CSV
- Repository: MNL · Path: `scripts/bpool/specs/theta_hat_realdata_901_v1.csv`
- Track: pooled baseline · Producing code: `scripts/bpool` estimator · Upstream: as above
- Status: **canonical** · Headline: 47 params with `se_hessian` + `se_clustered`
- warm start: **yes** · inference: **yes** · writing: **yes** · welfare: **yes**
- Caveats: authoritative theta for the baseline; keep as the single source of truth.

**Artifact:** Certified spec YAML
- Repository: MNL · Path: `scripts/bpool/specs/estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml`
- Status: **canonical** · Headline: 48→47 free (`beta_ll`=0, `theta_l_m`=−0.8); `wage_spec: vw`
- warm start: **yes** · inference: **yes** · writing: **yes** · welfare: **yes**
- Caveats: descriptive comments say "49 params" in places — cosmetic, non-authoritative.

**Artifact:** Certified cluster-robust SE JSON
- Repository: MNL · Path: `EUROMOD-STORAGE/outputs/post_estimation/realdata_joint_901_tlmpin_certified/joint/certified_cluster_robust_se.json`
- Status: **canonical** · Headline: sandwich SE, cluster=idorighh
- warm start: n/a · inference: **yes** · writing: **yes** · welfare: n/a · Caveats: none.

---

## B. 49-param gender-split relaxation (invalid as baseline)

**Artifact:** `gsplit` 49-param spec + gate
- Repository: MNL · Paths: `scripts/bpool/specs/estimation_spec_joint_pooled_v1_bll0_tlmpin_gsplit.yaml`;
  gate `docs/France_case/P3a/execution_logs/Bpool/RURO_jax_recovery_gate_gsplit_901_v1.md`;
  fit `RURO_realdata_2016_2017_joint_901_gsplit_v1.md`; theta `theta_hat_realdata_901_gsplit_v1.csv`
- Track: pooling-relaxation experiment · Producing code: `scripts/bpool` · Upstream: pooled bpool data
- Status: **invalid** (as a baseline) / **diagnostic**
- Headline: real-data negLL 238362.788142 (lower, but a *wrong* target); synthetic Check-5 PD (min_eig +1.532) yet Checks 2–4 FAIL; 3/4 relaxed params do not recover (e.g. `beta_h_pt2_m` true −1.19 → +0.039, wrong sign)
- warm start: **no** · inference: **no** · writing: **no** (except as a documented negative result) · welfare: **no**
- Caveats: PD real-data Hessian did NOT imply identification — tight-SE bias. Explicit precedent for "PD Hessian is not sufficient without recovery."

---

## C. FR-2016 singles P2a track

### C1. Region-live fit (provisional)

**Artifact:** Region-live estimation results JSON
- Repository: MNL · Path: `outputs/p2a_singles2016/estimation_results_p2a_singles2016.json` (mtime 2026-07-13, `command_line: propagate_regionlive.py`)
- Track: FR-2016 singles P2a (1,555 HH, 101 alts) · Producing code: notebook cell P2a-10 (`fr_data_walkthrough.ipynb`) → propagated by `propagate_regionlive.py` (**script missing from disk**)
- Upstream: `fr_singles_engine_ready_p2a_bpool_v2.parquet` (region/urb/gsur revived from `singles_dec`)
- Status: **provisional**
- Headline: **summary joint_ll −19053.4655**; note "region/urb/gsur revived"; 2 at-bound (`beta_l_age2_sm/sf`)
- warm start: **yes** (as a start value) · inference: **no** · writing: **no** · welfare: **no**
- Caveats: propagated, not strictly re-estimated with diagnostics; producing script absent.

**Artifact:** Region-live theta CSV
- Repository: MNL · Path: `theta_p2a_singles_2016_v2.csv` (root) · Track: P2a singles region-live
- Producing code: P2a-10 / propagate script · Status: **provisional**
- Headline: region block populated (`beta_E_gsur −1.306`, `beta_E_drgn2..8`, `beta_E_drgur −0.530`, `beta_E_drgmd −0.668`); `beta_E` −0.75 (vs region-dead −4.31)
- warm start: **yes** · inference: **no** · writing: **no** · welfare: **no**
- Caveats: cols 2–3 are bounds, not Hessian SE; `p2a_fit_provenance.json` still points `theta_csv` at the `_v1` (region-dead) file — pointer defect.

**Artifact:** Region-live engine-ready parquet + metadata
- Repository: MNL · Paths: `outputs/p2a_singles2016/fr_p2a_singles2016__singles.parquet` + `__mnlmeta.json` (mtime 2026-07-13); root `fr_singles_engine_ready_p2a_bpool_v2.parquet`
- Track: P2a singles region-live · Producing code: P2a-10 wiring · Status: **provisional**
- Headline: `drgn1, drgur, drgmd, drgru, gsur` populated (loader sees reg2 mean 0.181, gsur mean 0.098)
- warm start: **yes** · inference: n/a · writing: **no** · welfare: **yes** (already consumed — see C4) · Caveats: this is the wiring fix; keep as the engine-ready v2.

**Artifact:** Region-live fit provenance
- Repository: MNL · Path: `p2a_fit_provenance.json` (root)
- Status: **provisional** · Headline: `negll_fit 19053.4655`, `repair_note: "region/urb/gsur revived; 19071.6562 -> 19053.4655; beta_E absorbed regional variation"`
- warm start: n/a · inference: **no** · writing: **no** · welfare: **no**
- Caveats: `theta_csv` field points to `_v1` (stale); `engine_ready` correctly points to `_v2`.

### C2. Region-dead fit (diagnostic / superseded-in-place)

**Artifact:** Region-dead post-estimation set — SE, solver diag, diagnostics bundle, params CSV, PNGs, master record
- Repository: MNL · Paths: `outputs/p2a_singles2016/p2a_se_clustered.csv`, `p2a_singles2016_solver_diagnostics.json` (objective −19071.656, "notebook P2a", gradient_norm null), `p2a_singles2016_diagnostics_bundle.json`, `p2a_singles2016_params.csv`, `p2a_singles2016_*.png`, `P2A_MASTER_RECORD.md` (all mtime 2026-07-12)
- Track: P2a singles region-dead · Producing code: notebook P2a-5..P2a-8 · Status: **diagnostic** (and **superseded-in-place**: describes 19071.6562 while the sibling JSON is now 19053.4655)
- Headline: negLL 19071.6562; region block a flat direction (5 near-zero eigenvalues, loadings on `beta_E_drgn*`/`drgur`/`drgmd`)
- warm start: **no** · inference: **no** · writing: **no** · welfare: **no**
- Caveats: these files were NOT regenerated for region-live; do not read them as region-live diagnostics. The flat-direction result is the motivation for the wiring repair.

### C3. Exploratory notebooks

**Artifact:** `fr_data_walkthrough.ipynb`
- Repository: dclaborsupply · Path: `notebooks/fr_data_walkthrough.ipynb`
- Track: P2a end-to-end exploration · Status: **diagnostic** (exploratory; not a pipeline)
- Headline: sole home of region-live (P2a-10 executed, negLL 19053.4655, iters 353); cells `regionlive00`–`05` (re-freeze, SE, report, Hessian, anchor) authored but `execution_count: null` (**never run**)
- warm start: **no** · inference: **no** · writing: **no** · welfare: **no**
- Caveats: a notebook cell is not a production pipeline; downstream region-live diagnostics unexecuted.

**Artifact:** `fr_singles_pipeline_v1.ipynb`
- Repository: dclaborsupply · Path: `notebooks/fr_singles_pipeline_v1.ipynb`
- Track: P2a "pipeline" extract · Status: **diagnostic / superseded**
- Headline: reproduces **only region-dead 19071.6562** (stated anchor; asserts at target 19071.6562); no P2a-9/P2a-10, no region-live cells
- warm start: **no** · inference: **no** · writing: **no** · welfare: **no**
- Caveats: does NOT reflect the region-live repair; misleading if read as "the pipeline."

### C4. P2a welfare outputs (provisional, built on region-live theta)

**Artifact:** P2a singles welfare + inequality bundle
- Repository: MNL (scripts) → EUROMOD-STORAGE (outputs)
- Paths: `EUROMOD-STORAGE/outputs/welfare/p2a_singles2016/{singles_ViIS_p2a_v1.parquet, singles_measures_p2a_v1.parquet, inequality_p2a_v1.json, run_manifest_p2a_v1.json}`; report `docs/jmp_methodology/RURO_welfare_P2a_singles_Vi_and_measures_report_v1.md`
- Track: P2a singles welfare · Producing code: `scripts/welfare/run_p2a_singles_welfare.py` (no re-estimation; θ fixed input)
- Upstream: region-live theta (`theta_hat_p2a_singles2016_v1.csv`, theta_hash `5f3722dc`), spec_hash `492bcfa9`
- Status: **provisional**
- Headline: 1,555 HH; W3 zero-recovery ~2e-10, ViIS parity ~2e-15; pooled Gini **W1 0.176 / W4 0.261 / W6**; W4 median compensation 8505 EUR (was 4364 on region-dead)
- warm start: n/a · inference: **no** · writing: **no** · welfare: **no** (do not declare welfare readiness)
- Caveats: inherits region-live provisional status; the +95% W4 shift shows welfare is materially sensitive to the un-rebuilt wiring fix; own thin-ESS / EUROMOD reprice-parity blockers remain.

---

## D. Legacy / superseded pipeline artifacts (MNL)

**Artifact:** Active-results registry (stale)
- Path: `docs/estimation/RURO_ACTIVE_RESULTS_REGISTRY.md` · Status: **superseded**
- Headline: lists continuous-RURO v3 + job-choice M2h/M2e (Feb-2026 GAMSPy) as "current"; omits the certified JAX baseline
- All safety flags: **no** · Caveats: repoint or archive; misleads on what the baseline is.

**Artifact:** Continuous-RURO / job-choice / corrected-P3a / NC-pilot / GAMSPy-CONOPT branches
- Paths: `outputs/estimates/fr/spec/v3/gamspy/…`; `outputs/estimates/fr/spec/job_choice/…`; `Results/P3a/pooled_P3a/…`; `docs/France_case/NC_pilot/`, `Results/NC_pilot/…`; `docs/estimation/GAMSPy_*`, `scripts/runners/legacy/`, `_gams_work/`
- Status: **superseded** · All safety flags: **no**
- Caveats: correctly quarantined under `docs/archive/**` / `gamspy/**`, but MNL root `README.md` still advertises continuous+job-choice as the two "active" branches.

---

## E. Writing / design artifacts (Job_Market_paper)

**Artifact:** `JMP_project_state_v1.md` — Status: **accepted** (current state anchor, 2026-06-02).
Safe for writing: **yes** (with the minor two-vs-three-factor headline wording noted in the staleness audit).
No welfare readiness implied.

**Artifact:** `JMP_welfare_spec_v5.md` — Status: **accepted** (design memo). Safe for writing: **yes**;
welfare: **no** (design only; explicitly does not authorise implementation). Names a next artifact
`RURO_welfare_scaffold_design_contract_v2.md` that is **absent**.

**Artifact:** `JMP_literature_review_skeleton_v1.md` — Status: **accepted / canonical framing**
(2026-06-05, newest). Safe for writing: **yes**. Sets access/ability/preference as canon.

**Artifact:** `CLAUDE.md`, `README.md`, `JMP.md` (Job_Market_paper) — Status: **superseded / misleading**.
All safety flags: **no**. Caveats: assert "model not estimated," empty `Code/`, "single commit,"
two-factor framing — contradict the certified estimate. See staleness audit for repairs.

---

## F. Explicitly MISSING artifacts (region-live promotion blockers)

For the FR-2016 singles P2a **region-live** result, the following are **not present** in any repository
or in `EUROMOD-STORAGE` (only region-dead equivalents, or unexecuted notebook stubs, exist):

- region-live gradient (not persisted)
- region-live **Hessian / eigenvalues / rank / condition number** (P2a-9c unexecuted; committed inference-diagnostics report: "Hessian not present")
- region-live **cluster-robust SE** (committed SE CSV is region-dead; robust_se "available: false")
- region-live **post-estimation report** (all committed PNGs/param-table region-dead)
- verified **cold-reload regression anchor** at 19053.4655 (P2a-8c unexecuted)
- the **producing script `propagate_regionlive.py`** itself (referenced in `command_line`; absent from both repos, no git record)
- a **production (non-notebook) rebuild path** for region-live in `dclaborsupply` packages/exports

These are the artifacts the manager must obtain (or the rebuild must generate) before region-live can
move to a strict-estimation verdict.
