# FR P2a Phase-5 Inference Results — Extraction Memo v1

**Mission:** JMP-M07, Stage A (accepted-result extraction)
**Tool:** Claude Code, Sonnet, read-only on MNL and the nested `dclaborsupply-monorepo` package
**Numerical estimation:** Not performed. **New model execution:** Not performed.
**Governing document:** `docs/missions/JMP_M07_inference_results_integration_mission_charter_v1.md`

## 0. Scope of this deliverable

This memo, together with the companion file
`docs/results/FR_P2a_phase5_parameter_reporting_map_v1.csv`, is the Stage-A
"accepted-result extraction" deliverable defined in charter section 9
("Produce an exact source-to-table inventory. No raw-data access and no
numerical re-estimation."). Charter section 8 lists six required
Job_Market_paper outputs; of those, outputs 1 and 2 are the Stage-A
extraction artifacts produced here. Outputs 3–4 (`manuscript/sections/…`,
`manuscript/appendices/…`) are Stage-B economics drafting, performed by a
separate Opus chat per charter section 9. Outputs 5–6 (M08 welfare-input
handoff, M07 goal-manager acceptance memo) are Stage-D goal-manager outputs
("The Goal 1 Manager … creates the acceptance memo and the M08 handoff").
This memo does not create those four files.

Every number below is copied verbatim from the accepted Phase-5 artifacts
listed in section 8, or is a trivial rendering explicitly authorized by the
charter (robust-CI endpoints computed from the recorded estimate, robust
standard error, and the recorded `z_0.975`). No statistic is recomputed from
microdata; no gating, covariance, or test result is re-derived.

## 1. Canonical evidence

Per charter section 2, this extraction uses only the accepted Phase-5
result:

- MNL evidence commit: `905348c53b31049db854c16016fa064517c19892`
- MNL D11/closeout HEAD: `520441a653f04196bf1e92e3658a478b4feb3718`
- Job_Market_paper checkpoint: `1e54bcd7fe6eb5d202db97c204a655d385181442`
- nested `dclaborsupply-monorepo`: `27756a06ea189339aa82915ed2124628afed20eb`
- accepted attempt: `20260803T133122Z_14772_817e8deb503d408fa73b8b53d598c0db_dryrun_PHASE_5_DRY_RUN_COMPLETE`
- Phase-5 bundle: `d08947ce015f2b2a922c6d5591ebe600c53016922b3a1158d90f125cd2195232`

Source directory (MNL, read-only):
`outputs/p2a_singles2016/region_live_v1/phase5_inference_v1/attempts/20260803T133122Z_14772_817e8deb503d408fa73b8b53d598c0db_dryrun_PHASE_5_DRY_RUN_COMPLETE/`

All 19 members of `phase5_manifest.json.member_inventory` were inspected;
`gating_failures` is empty and every gate in `phase5_diagnostics.json` with
`"tier": "gating"` shows `"passed": true`. The single non-passing entry is
`W-4` (`"tier": "warning"`, `"passed": false`), which is the pre-registered,
non-gating near-boundary warning addressed in section 6 below.

## 2. Main empirical message

### Claim 1 — Confirmatory access-block rejection

- `H0-A`, 10 df: robust Wald `37.45`, robust p-value `4.7e-05`
  (source: `phase5_regional_tests.csv`, row `H0-A`, `W_robust=37.446975959270233`,
  `p_robust=4.7351579328540456e-05`).
- The regional/urbanisation/GSUR access block
  (`beta_E_gsur, beta_E_drgn2..drgn8, beta_E_drgur, beta_E_drgmd`) is jointly
  relevant.

This is a confirmatory test of the named ten-parameter access block. It is
**not** a test of the whole opportunity mechanism (the hours-access block
`beta_E, beta_h_pt1, beta_h_pt2, beta_h_ft, beta_h_lh` and the occupation
block are not part of `H0-A`).

### Claim 2 — Concentration in GSUR

- `H0-G`: robust Wald `29.21`, robust p-value `6.5e-08`
  (source: `phase5_regional_tests.csv`, row `H0-G`,
  `W_robust=29.208167292116848`, `p_robust=6.500461827702641e-08`).
- `beta_E_gsur = -1.105` (source: `phase5_parameter_table.csv`, row
  `beta_E_gsur`, `estimate=-1.1047680284010777`).
- Robust 95% interval `[-1.51, -0.70]` (recomputed as authorized from
  `estimate=-1.1047680284010777`, `se_robust=0.20441791001836224`, and
  `z_0.975=1.959963984540054` recorded in `phase5_diagnostics.json`, gate
  `W-4`, `observed.z_975`; full-precision result
  `[-1.505419769832017, -0.7041162869701383]`).
- `H0-B` NUTS-1 dummies: robust p-value `0.594`
  (source: `phase5_regional_tests.csv`, row `H0-B`,
  `p_robust=0.59428532005685808`).
- `H0-C` urbanisation terms: robust p-value `0.847`
  (source: `phase5_regional_tests.csv`, row `H0-C`,
  `p_robust=0.84722237348924945`).

> At the resolution and specification studied, measured access heterogeneity
> is concentrated in one GSUR dimension rather than diffuse across broad
> NUTS-1 geography or the two urbanisation indicators.

`gsur` is not translated into a substantive label beyond what
`phase5_parameter_map_v1.csv` documents (design column `gsur`); no additional
data-documentation claim is made here.

### Claim 3 — Variance-estimator robustness

Model-based and robust inference agree on all four `H0-A/B/C/G` rejection
decisions:

| null | q (df) | W_model | p_model | W_robust | p_robust | same-side-of-0.05 |
|---|---|---|---|---|---|---|
| H0-A | 10 | 36.254933058284301 | 7.6092403707792337e-05 | 37.446975959270233 | 4.7351579328540456e-05 | yes (reject) |
| H0-B | 7 | 5.8727461336166895 | 0.55468440309732081 | 5.5406502206474828 | 0.59428532005685808 | yes (fail to reject) |
| H0-C | 2 | 0.34026532887756678 | 0.84355289970082881 | 0.33158415259614427 | 0.84722237348924945 | yes (fail to reject) |
| H0-G | 1 | 27.483391678525457 | 1.5844935333993574e-07 | 29.208167292116848 | 6.500461827702638e-08 | yes (reject) |

(source: `phase5_regional_tests.csv`, all rows and columns.)

This is stability of the test verdicts across the two variance estimators,
**not** proof of correct specification.

## 3. Methods reporting

Per charter section 4, and sourced from the accepted artifacts as cited:

- **1,555 household contributions/clusters.**
  Source: `score_aggregate_summary.json.n_households = 1555`;
  `phase5_manifest.json.artifact_records[0].metadata.n_households = 1555`;
  `phase5_diagnostics.json`, gate `T-1/T-4`, `observed.n_households = 1555`.
- **Conditional 35-dimensional inference.**
  Source: `phase5_diagnostics.json`, gate `T-6`, `observed.rank_Hs = 37`
  (bread) and gate `T-9`/`T-14`/`W-3`, `dimension = 35` /
  `numerical_rank = 35` (the interior/conditional covariance actually
  reported); `score_aggregate_summary.json.dim_interior = 35`.
- **Two active-bound free parameters excluded from ordinary symmetric
  inference.** `beta_l_age2_sm`, `beta_l_age2_sf`
  (source: `phase5_diagnostics.json`, gate `T-22`,
  `bar.required_names` / `observed.supplied_names`; both are at their upper
  bound in `phase5_parameter_table.csv`, `status=active-bound`,
  `bound_side=upper`).
- **Literal `NA` for active-bound and pinned coordinates.**
  Source: `phase5_parameter_table.csv` — every active-bound and pinned row
  has `se_model, se_robust, ratio_robust_model, z, p = NA`; reproduced
  identically in the companion parameter-reporting map.
- **Accepted Hessian bread.**
  `bread_sha256 = e9ca080ecc7e40e43881b9422af0095f23ad2bfef3e84648d2031a33eb9e4061`
  (source: `phase5_manifest.json.accepted_binding.bread_sha256`, verified at
  gate `T-5`/`T-6`).
- **Household-score sandwich meat.**
  Source: `phase5_diagnostics.json`, gate `T-7` (meat validity, rank 35,
  built from the streamed per-household score aggregate) and gate `T-1/T-4`
  (score-identity check against the Phase-4 gradient,
  `max_abs_dev=1.4566126083082054e-13`).
- **Correction scalar `1555/1520`.**
  Source: `phase5_diagnostics.json`, gate `T-10`,
  `observed.correction_c = 1.0230263157894737`,
  `observed.correction_telescoped = "1555/1520"`,
  `observed.correction_formula = "[G/(G-1)] * [(N-1)/(N-K)] = G/(G-K)"`,
  with `G=1555`, `N=1555`, `K=35`.
- **Model-based and robust covariance both reported.**
  Source artifacts: `phase5_covariance_model.csv`/`.npy` and
  `phase5_covariance_robust.csv`/`.npy` (both listed in
  `phase5_manifest.json.member_inventory`; both PD/PSD per gate `T-9`).
- **Regional restrictions selected by parameter name.**
  Source: `phase5_regional_tests.csv` column `restriction_names`, e.g.
  `H0-A` = `beta_E_gsur;beta_E_drgn2;beta_E_drgn3;beta_E_drgn4;beta_E_drgn5;beta_E_drgn6;beta_E_drgn7;beta_E_drgn8;beta_E_drgur;beta_E_drgmd`.
- **No row-level score persistence.**
  Source: `phase5_diagnostics.json`, gate `T-23S`,
  `observed.no_row_level_score_member = true`,
  `observed.member_set_allowlisted = true`, `observed.leftovers = []`.

## 4. Parameter-table reporting

The 47-row parameter table is reported in full in the companion file
`docs/results/FR_P2a_phase5_parameter_reporting_map_v1.csv`
(SHA-256 `89a0465cc55f4bc05898559120591e4c28db15a18992bd2b33ba6538ce7b8481`),
built directly from `phase5_parameter_table.csv` (47 rows, values copied
verbatim) with `pin_reason` and the `gsur`/`reg2..8`/`drgur`/`drgmd` design
column cross-references copied from the committed context document
`docs/France_case/P2a/phase5_parameter_map_v1.csv` (MNL, tracked, read-only).
Rows are in the original 47-parameter order — **not** ranked by
significance, per charter section 5.

Per charter section 5 the CSV carries: parameter name; economic block
(`source_block`, the literal block name from the source table) and a
five-panel grouping (`economic_panel`); estimate; model-based SE; robust SE;
robust 95% confidence interval; status (interior / active bound / pinned);
literal `NA` for the inferential fields on active-bound and pinned rows; and
a concise economic label.

Panel assignment (charter section 5, five panels):

1. `1_preferences` — all `preference_*` blocks (singles male/female leisure,
   singles consumption, and the pinned couples male/female leisure rows).
2. `2_employment_hours_access` — `opportunity_hours`.
3. `3_regional_access` — `opportunity_market_regional_access` and the two
   pinned `opportunity_market_year` rows (`beta_E_y2015`, `beta_E_y2017`),
   which belong to the same opportunity/access equation and have no separate
   charter-specified panel.
4. `4_occupation_access` — `opportunity_occupation`.
5. `5_wage_density` — `wage_density`.

The `economic_label` column is a literal rendering of each parameter's name
and source block (e.g. `beta_E_gsur` → "regional access, GSUR dimension");
it is descriptive formatting, not a new statistical or economic claim, and
introduces no number not already present in the source columns.

Robust confidence intervals (`ci_robust_low`, `ci_robust_high`) are computed
only for the 35 interior rows, as
`estimate ± z_0.975 × se_robust` with `z_0.975 = 1.959963984540054` taken
verbatim from `phase5_diagnostics.json` gate `W-4`
(`observed.z_975`). This is the same formula and the same `z` value the
accepted artifact itself uses to compute the `W-4` near-boundary interval
(`observed.detail.beta_l0_sm.lo/.hi`, `observed.detail.beta_w_pexp2.lo/.hi`);
the values recomputed here for `beta_l0_sm` and `beta_w_pexp2` match those
recorded artifact values exactly. Active-bound and pinned rows carry literal
`NA` for `se_model`, `se_robust`, `ci_robust_low`, `ci_robust_high`.

## 5. W-4 and S-10 disclosure

Per charter section 6, carrying the accepted Tier-1 warning for
`beta_l0_sm` and `beta_w_pexp2`
(source: `phase5_diagnostics.json`, gate `W-4`, `observed.flagged =
["beta_l0_sm", "beta_w_pexp2"]`, `passed=false`, `tier=warning`):

> Robust symmetric intervals for `beta_l0_sm` and `beta_w_pexp2` approach the
> relevant parameter boundary. They are reported as local diagnostics and
> should not be interpreted as unrestricted evidence beyond the admissible
> parameter region. The welfare analysis therefore includes a pre-registered
> admissible local sensitivity for these coordinates.

Supporting numeric detail (source: `phase5_diagnostics.json`, gate `W-4`,
`observed.detail`):

| parameter | robust CI low | robust CI high | lower bound (lb) | upper bound (ub) |
|---|---|---|---|---|
| `beta_l0_sm` | -0.12309900960568587 | 9.683896877332586 | 0.05 | 50.0 |
| `beta_w_pexp2` | -0.1014429187847586 | 0.07539182354674019 | -0.1 | 0.1 |

Estimation was not reopened and Tier 2 was not triggered. The binding
specification for the M07/M08 sensitivity treatment is
`docs/design_notes/JMP_M07_S10_tier1_welfare_sensitivity_specification_v1.md`
(governing the four required scenarios and the material-loading trigger);
the routing rationale is
`docs/design_notes/JMP_M05C_W4_routing_memo_v1.md`. Neither document is
reproduced here beyond this pointer, per the charter's "keep implementation
detail proportionate" instruction.

## 6. LOC4 sequencing

Per charter section 7, governing document
`docs/design_notes/JMP_LOC4_pathB_ruling_v1.md` (Path B, binding before the
welfare mission):

- The paper-facing baseline remains the certified common-dispersion
  specification extracted in this memo.
- The LOC4 four-density variant is pre-registered as the first mandatory
  wage-density robustness axis. It has **not** been estimated; no LOC4
  numerical result is presented anywhere in this memo or the companion CSV.
- LOC4 does not block the first baseline welfare prototype (M08).
- LOC4 robustness must close before the paper freezes its preferred
  quantitative decomposition magnitudes (before M09 per the ruling's
  section 7 timing).

## 7. Non-scope confirmation

Consistent with charter section 11 and the Stage-A tool restriction, this
extraction did not: rerun inference; re-estimate the model; run welfare or
decomposition; implement LOC4; add industry `lindi` or external regional
covariates; modify `dclaborsupply-monorepo`; reopen software certification;
or interpret any preference parameter as responsibility. No statistical
rejection is described as causal identification anywhere above.

## 8. Availability

Every number required by charter sections 3–7 for the Stage-A extraction
scope (Claims 1–3, the methods paragraph, the 47-row parameter table, and
the W-4/S-10/LOC4 disclosures) was sourced from the accepted attempt's
members, `phase5_manifest.json`, or the committed governing documents cited
above. Nothing in this memo's scope is marked `UNAVAILABLE`.
