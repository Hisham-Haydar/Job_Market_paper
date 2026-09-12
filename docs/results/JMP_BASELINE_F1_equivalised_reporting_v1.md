# E3-EQ: BASELINE-F-1 equivalised reporting v1

Date: 2026-09-12

Authority: `JMP_market_set_bridge_and_parallel_work_ruling_v1.md`, "Parallel
continuation — E3-EQ" section.

Scope: pure reporting over the already-verified BASELINE-F-1 construction.
This memo performs **no new welfare construction**. It equivalises the
already-committed and independently verified `W1_F_obs`/`C_obs` values and
reports the worker-only ratio. The verified `W_F` construction is unchanged.

Verified implementation commit: `d729cf895e9197716e58875aa1bf13824f022e2e`
(MNL). Verified aggregate-output commit: `6048c9f74032f7334488db7b160fdde
73354255e` (MNL). MNL repository HEAD at the time of this report:
`b5550af594797c699c24af97f92f5338a3de5203` — matches the verification's
"verified b5550af" reference; no drift.

Reproducible reporting code: `MNL/scripts/welfare/
report_baseline_f1_equivalised_v1.py`. Outputs written to
`MNL/outputs/welfare/baseline_f1_equivalised_v1/` (aggregates only; not
household-level; safe for Git). Household-level inputs remain at
`C:/Users/hisham/MNL/EUROMOD-STORAGE/restricted/baseline_f1_prep_v1/
{singles,couples}_household_v1.jsonl` and are not reproduced here.

## 1. Scale provenance

**Located, for both samples.** The household equivalence scale used
throughout is the modified-OECD (OECD-modified / Eurostat) scale:

    m_i = 1 + 0.5 * (n_adults_14_plus_i - 1) + 0.3 * n_children_under_14_i

(first adult = 1.0, each further household member aged 14 or over = 0.5, each
child under 14 = 0.3). No competing formula (a raw EUROMOD `eq_scale`, an
OECD-original scale, a `sqrt(household size)` scale) exists anywhere in the
MNL or Job_Market_paper repositories; this is the single definition found. It
is applied only to welfare *outputs*, never inside the structural utility,
consistent with `JMP_measure_map_v1.md` ("Equivalisation: None before utility
or in literal `C_obs`... `m_oecd` applied only to the resulting welfare
output").

The formula is computed identically by two sample-specific artifacts, each a
side-product of a different sprint mission, both carrying the run-manifest
label `FINAL_{SINGLES,COUPLES}_PROVISIONAL_PENDING_ECONOMICS_REVIEW`. Neither
carries a stronger acceptance status than the other, and this memo flags that
provisional status for both rather than treating one as more settled.

**Both scale artifacts carry `FINAL_*_PROVISIONAL_PENDING_ECONOMICS_REVIEW`;
ratification is an open Deputy/PI item, and every equivalised figure in this
memo (§2 `C_eq`/`W_F_eq`, both samples) is reported subject to it.**

| | Singles | Couples |
|---|---|---|
| Builder | `experiments/JMP_SEMINAR_SPRINT/runs/final_singles_welfare/run_ss9_step4a_equivalence_scale_v1.py` | `experiments/JMP_SEMINAR_SPRINT/runs/final_couples_welfare/run_cw_step2b_medoid_v1.py` |
| Artifact | `ss9_equivalence_scale_v1.parquet` | `cw_equivalence_scale_v1.parquet` (a side-product of the channel-D reference-medoid selection, R-242.3) |
| SHA-256 | `9e9082bd4933c1a6e0a1a71e99d2b4b0463977c6851a2e74d56bd594ada7759d` | `cfb3f1a196f96d4865971b9206e142dbb675ccc05eeae4a208e36b2c442110e7` |
| Artifact population | 1,555 households (P2a singles-2016) | 2,275 households (floor-5 corrected couples roster) |
| Join to BASELINE-F1 ACCEPTED_FRAME | `source_idhh = idhh`, 0 of 1,540 unmatched | `source_idhh = idhh`, 0 of 2,223 unmatched |
| Composition source | that artifact's own person-roster reconstruction (`dag`, cutoff 14) | that artifact's own floor-5 member roster (`dag`, cutoff 14), reconstructed through the couples reprice's own `prepare()` |

Both artifacts disclose their `n_children_under_14`/`n_14plus`-based scale as
distinct from the model's own preference-side `n_children` covariate; neither
recomputation touches the certified `W_F` construction.

**Correction to an earlier draft of this memo.** A first pass of this report
incorrectly stated that no couples equivalence-scale composition artifact
existed and issued a `HALT_COUPLES_SCALE_MISSING` refusal for couples §2.
That claim was wrong: `cw_equivalence_scale_v1.parquet` already existed,
using the identical modified-OECD formula, and was located by the
independent E3-EQ verifier (`JMP_BASELINE_F1_equivalised_reporting_
verification_v1.md`, sub-point (c)) rather than by the original search. The
narrower claim that the couples ACCEPTED_FRAME's *own columns* carry no
roster remains correct (it carries only normalized male/female ages and an
aggregate `n_children`), but "nothing exists in the repo" was an oversight,
not a genuine gap. §2 below now reports couples `C_eq`/`W_F_eq` in full.

## 2. Equivalised and unequivalised aggregates

Weights: `dwt`. Convention: S12/M08 dwt-weighted mean, weighted-midpoint-rank
median, and Lerman–Yitzhaki weighted Gini, identical to
`baseline_f1_verification_v1.md` §"Aggregate reconstruction" (reused via
`weighted_summary()` in the reporting script, algebraically identical to
`_weighted_summary()` in `run_baseline_f1_full_sample.py`). Units: household
EUR/month. `C_eq`/`W_F_eq` use the modified-OECD scale (dimensionless
consumption-equivalent units per adult-equivalent).

### Singles (N = 1,540)

| Object | N | dwt mean | dwt median | dwt Gini |
|---|---:|---:|---:|---:|
| **C_eq** (equivalised) | 1,540 | 1766.486 | 1588.291 | 0.263292 |
| **W_F_eq** (equivalised) | 1,540 | 1302.072 | 1165.141 | 0.249807 |
| C_obs (unequivalised, secondary) | 1,540 | 1948.920 | 1760.629 | 0.252337 |
| W_F_obs (unequivalised, secondary) | 1,540 | 1434.812 | 1319.978 | 0.237552 |
| m_oecd (scale itself) | 1,540 | 1.137279 | 1.000000 | 0.099302 |

The unequivalised `W_F_obs` row reproduces the committed verified values
(mean `1434.811649926925`, median `1319.977951506895`, Gini
`0.23755220907703214`) exactly — 0 difference, consistent with "do not alter
the verified `W_F` construction."

### Couples (N = 2,223)

| Object | N | dwt mean | dwt median | dwt Gini |
|---|---:|---:|---:|---:|
| **C_eq** (equivalised) | 2,223 | 2245.110 | 2062.837 | 0.226805 |
| **W_F_eq** (equivalised) | 2,223 | 1310.615 | 1237.352 | 0.197403 |
| C_obs (unequivalised, secondary) | 2,223 | 4253.333 | 3854.225 | 0.231022 |
| W_F_obs (unequivalised, secondary) | 2,223 | 2495.801 | 2356.493 | 0.210354 |
| m (scale itself) | 2,223 | 1.922223 | 1.800000 | 0.107821 |

The unequivalised `W_F_obs` row reproduces the committed verified couples
values (mean `2495.800865909865`, median `2356.493005647621`, Gini
`0.21035441022764906`) exactly — 0 difference.

Full-precision JSON: `MNL/outputs/welfare/baseline_f1_equivalised_v1/
{singles,couples}_equivalised_reporting_v1.json`.

## 3. Worker-only ratio W_F_obs / C_obs

Worker = observed employed decider (singles) / at least one partner employed
(couples) — i.e. NOT `observed_nonworker`, the same predicate BASELINE-F-1
already uses for its C2 worker-ratio-domain check. **This ratio is not a
welfare loss statement**: `W_F_obs/C_obs = exp((L_obs - L_home)/beta_c) < 1`
reflects only that the observed job's systematic leisure term is below home
leisure's, at fixed `theta_c = 0` utility; it says nothing about whether the
job is good or bad for the household net of the wage income it also delivers,
and `1 - ratio` is not interpreted as a monetary loss anywhere in this memo.

### Singles workers (N = 1,336 of 1,540; 204 nonworkers excluded)

| Statistic | Value |
|---|---:|
| dwt-weighted mean | 0.733194 |
| dwt-weighted median | 0.755301 |
| dwt-weighted Gini | 0.102706 |
| p5 | 0.483756 |
| p10 | 0.565329 |
| p25 | 0.654448 |
| p75 | 0.844003 |
| p90 | 0.875987 |
| p95 | 0.884855 |

### Couples workers (N = 2,173 of 2,223; 50 households where neither partner
works excluded)

| Statistic | Value |
|---|---:|
| dwt-weighted mean | 0.609601 |
| dwt-weighted median | 0.625906 |
| dwt-weighted Gini | 0.120548 |
| p5 | 0.355183 |
| p10 | 0.439664 |
| p25 | 0.552517 |
| p75 | 0.685645 |
| p90 | 0.767435 |
| p95 | 0.805686 |

Histogram and ECDF (dwt-weighted, 40 bins): `MNL/outputs/welfare/
baseline_f1_equivalised_v1/worker_ratio_histogram_ecdf_v1.png`. Underlying
aggregate bin edges/counts and thinned ECDF points (≤200 points, no
household-level values) are in the same-named JSON files under
`worker_ratio.distribution`.

### Invariance to common equivalisation

The ratio is invariant to any positive per-household equivalisation constant
by construction: `(W_F_obs/m) / (C_obs/m) = W_F_obs/C_obs` for any `m > 0`,
independent of what `m` equals. This is confirmed two ways:

- **Singles**, using the real accepted `m_oecd`: max absolute difference
  between `ratio` and the recomputed `W_F_eq/C_eq` across all 1,336 workers
  is `2.22e-16` (floating-point noise).
- **Couples**, using the real accepted `m` from `cw_equivalence_scale_v1
  .parquet`: max absolute difference across all 2,173 workers is `1.11e-16`.

Both confirm the invariance holds to numerical precision for every household
individually, not merely on average.

## 4. Outputs

- This memo: `Job_Market_paper/docs/results/
  JMP_BASELINE_F1_equivalised_reporting_v1.md`.
- Reproducible reporting code: `MNL/scripts/welfare/
  report_baseline_f1_equivalised_v1.py` (reads only already-verified
  restricted household levels and the accepted frames/scale artifact; writes
  no new restricted files).
- Aggregate JSON: `MNL/outputs/welfare/baseline_f1_equivalised_v1/
  {singles,couples}_equivalised_reporting_v1.json`.
- Figure: `MNL/outputs/welfare/baseline_f1_equivalised_v1/
  worker_ratio_histogram_ecdf_v1.png`.
- Household-level records: unchanged, restricted, not touched by this task.

## RETURN

- Memo: this file.
- Commit hash: MNL repository HEAD unchanged at `b5550af594797c699c24af97f9
  2f5338a3de5203` (no MNL commit made by this task beyond the new untracked
  aggregate files under `outputs/welfare/baseline_f1_equivalised_v1/` and the
  new script `scripts/welfare/report_baseline_f1_equivalised_v1.py`, pending
  the user's explicit commit approval per repository discipline). No changes
  were made to `baseline_f1.py`, its parameter tables, its accepted frames, or
  any restricted household file.
- Scale provenance: singles —
  `MNL/experiments/JMP_SEMINAR_SPRINT/runs/final_singles_welfare/
  run_ss9_step4a_equivalence_scale_v1.py` → `ss9_equivalence_scale_v1.parquet`
  (SHA-256 `9e9082bd4933c1a6e0a1a71e99d2b4b0463977c6851a2e74d56bd594ada7759d`);
  couples — `MNL/experiments/JMP_SEMINAR_SPRINT/runs/final_couples_welfare/
  run_cw_step2b_medoid_v1.py` → `cw_equivalence_scale_v1.parquet` (SHA-256
  `cfb3f1a196f96d4865971b9206e142dbb675ccc05eeae4a208e36b2c442110e7`). Both are
  the identical modified-OECD formula and both carry the run-manifest label
  `FINAL_{SINGLES,COUPLES}_PROVISIONAL_PENDING_ECONOMICS_REVIEW` — flagged
  here as an open provisional-status item for a Deputy/PI call on formal
  ratification, not a missing-data escalation.
- **Independent verification: one substantive correction, now resolved.** The
  E3-EQ verifier (`JMP_BASELINE_F1_equivalised_reporting_verification_v1.md`)
  passed unequivalised reproduction, singles equivalised reconstruction,
  worker-ratio stats, and the invariance check outright, and caught that this
  memo's first draft incorrectly claimed no couples equivalence-scale artifact
  existed. That claim has been corrected in §1/§2 above using the located
  `cw_equivalence_scale_v1.parquet`; the verifier's report and this memo's
  numbers were not yet cross-checked against each other a second time — a
  fresh verification pass over the corrected couples numbers is the
  recommended next step before this memo is treated as fully closed.
