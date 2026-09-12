# E3-EQ independent verification v1

Date: 2026-09-12

Independent verifier per the ruling's "Parallel continuation — E3-EQ" section. This script was written from scratch, reading only the raw restricted household files, the `dwt`-bearing engine-ready parquets, and the equivalence-scale artifact(s); it does not import or call `MNL/scripts/welfare/report_baseline_f1_equivalised_v1.py`.

Memo verified: `C:\Users\hisham\Repo\Job_Market_paper\docs\results\JMP_BASELINE_F1_equivalised_reporting_v1.md`

Independent script: (this file), executed via `C:\Users\hisham\Repo\MNL\.venv\Scripts\python.exe`.

## Verdict summary

| Sub-check | Verdict |
|---|---|
| (a) unequivalised reproduction | **PASS** |
| (b) singles equivalised reconstruction | **PASS** |
| (c) couples HALT correctness | **FAIL** |
| (d) worker-ratio stats | **PASS** |
| (e) invariance check | **PASS** |

**Overall: FAIL (see (c))**

## (a)/(b) Aggregate comparison — independent vs memo

| Object | Stat | Independent | Memo | Rel. agree (5e-6) |
|---|---|---:|---:|---|
| singles_C_eq | mean | 1766.486493 | 1766.486000 | PASS |
| singles_C_eq | median | 1588.290880 | 1588.291000 | PASS |
| singles_C_eq | gini | 0.263292 | 0.263292 | PASS |
| singles_W_eq | mean | 1302.071576 | 1302.072000 | PASS |
| singles_W_eq | median | 1165.140857 | 1165.141000 | PASS |
| singles_W_eq | gini | 0.249807 | 0.249807 | PASS |
| singles_C_obs | mean | 1948.919774 | 1948.920000 | PASS |
| singles_C_obs | median | 1760.628977 | 1760.629000 | PASS |
| singles_C_obs | gini | 0.252337 | 0.252337 | PASS |
| singles_W1F_obs | mean | 1434.811650 | 1434.812000 | PASS |
| singles_W1F_obs | median | 1319.977952 | 1319.978000 | PASS |
| singles_W1F_obs | gini | 0.237552 | 0.237552 | PASS |
| singles_m_oecd | mean | 1.137279 | 1.137279 | PASS |
| singles_m_oecd | median | 1.000000 | 1.000000 | PASS |
| singles_m_oecd | gini | 0.099302 | 0.099302 | PASS |
| couples_C_obs | mean | 4253.332749 | 4253.333000 | PASS |
| couples_C_obs | median | 3854.224936 | 3854.225000 | PASS |
| couples_C_obs | gini | 0.231022 | 0.231022 | PASS |
| couples_W1F_obs | mean | 2495.800866 | 2495.801000 | PASS |
| couples_W1F_obs | median | 2356.493006 | 2356.493000 | PASS |
| couples_W1F_obs | gini | 0.210354 | 0.210354 | PASS |

Singles scale join: 0 of 1540 unmatched (expect 0). Independent m_oecd formula re-derivation from `n_adults_14_plus`/`n_children_under_14` max abs diff vs artifact's own `m_oecd` column: `0.000e+00`.

## (c) Couples equivalence-scale existence check

Memo claim: "No couples counterpart to `ss9_equivalence_scale_v1.parquet` exists anywhere in the MNL repository." and refuses couples §2 as `HALT_COUPLES_SCALE_MISSING`.

Independent grep/glob finds `experiments/JMP_SEMINAR_SPRINT/runs/final_couples_welfare/cw_equivalence_scale_v1.parquet` (EXISTS), with columns `idhh, n_persons, n_14plus, n_under14, n_under18, m, m_two_adult_form`, computed by `run_cw_step2b_medoid_v1.py` as `m = 1 + 0.5*(n_14plus-1) + 0.3*n_under14` from the floor-5 member roster's own ages (`dag`) — algebraically the identical modified-OECD formula used for singles. Independent re-derivation of `m` from `(n_14plus, n_under14)` inside that artifact matches its own `m` column to max abs diff `0.000e+00` (n=2,275).

Coverage check: this artifact's `idhh` set covers 2223 of 2223 couples ACCEPTED_FRAME `source_idhh` values (join `source_idhh == idhh`).

**Finding: the memo's HALT claim is FACTUALLY INCORRECT as stated.** The narrower, true part of the memo's reasoning — that the couples ACCEPTED_FRAME (`couples_engine_ready_criterion_a_v1.parquet`) itself carries no per-member roster/ages beyond normalized male/female age and aggregate `n_children`, so the scale cannot be recomputed from *that frame's own columns* — is CONFIRMED (independently checked: no roster-like column found in its 147 columns). But the broader claim that repeats in the memo ('No couples counterpart... exists anywhere in the MNL repository... would require a new data-construction step... not attempted') is false: a couples modified-OECD equivalence-scale artifact already exists in the repo (`cw_equivalence_scale_v1.parquet`, produced for the separate final_couples_welfare/R-242 floor-5 pipeline), uses the identical formula, and its `idhh` set fully covers (2223/2223) the BASELINE-F-1 couples ACCEPTED_FRAME by `source_idhh == idhh`. This means an equivalised couples §2 table *could* have been computed by joining this pre-existing artifact instead of refusing outright — the correct disposition was not 'building one is out of scope', but 'one already exists elsewhere in the repo and was not located.' This is a materially different finding from an honest absence, though it does not affect the correctness of any number the memo *did* report (§2 couples row is left blank, not wrong; §3 worker-ratio needs no scale and is unaffected).

For completeness (NOT a memo claim, independent-only, informational): joining `cw_equivalence_scale_v1.parquet` to the couples ACCEPTED_FRAME and equivalising `C_obs`/`W1_F_obs` by this `m` is mechanically possible and yields a determinate result — but whether this artifact is *itself accepted* for use as the couples equivalisation scale is a question for the ruling/PI, not settled by this verification; no equivalised couples numbers are asserted here as authoritative.

## (d) Worker-only ratio comparison — independent vs memo

| Sample | Stat | Independent | Memo | Agree |
|---|---|---:|---:|---|
| singles_worker_ratio | N | 1336 | 1336 | PASS |
| singles_worker_ratio | mean | 0.733194 | 0.733194 | PASS |
| singles_worker_ratio | median | 0.755301 | 0.755301 | PASS |
| singles_worker_ratio | gini | 0.102706 | 0.102706 | PASS |
| singles_worker_ratio | p5 | 0.483756 | 0.483756 | PASS |
| singles_worker_ratio | p10 | 0.565329 | 0.565329 | PASS |
| singles_worker_ratio | p25 | 0.654448 | 0.654448 | PASS |
| singles_worker_ratio | p75 | 0.844003 | 0.844003 | PASS |
| singles_worker_ratio | p90 | 0.875987 | 0.875987 | PASS |
| singles_worker_ratio | p95 | 0.884855 | 0.884855 | PASS |
| couples_worker_ratio | N | 2173 | 2173 | PASS |
| couples_worker_ratio | mean | 0.609601 | 0.609601 | PASS |
| couples_worker_ratio | median | 0.625906 | 0.625906 | PASS |
| couples_worker_ratio | gini | 0.120548 | 0.120548 | PASS |
| couples_worker_ratio | p5 | 0.355183 | 0.355183 | PASS |
| couples_worker_ratio | p10 | 0.439664 | 0.439664 | PASS |
| couples_worker_ratio | p25 | 0.552517 | 0.552517 | PASS |
| couples_worker_ratio | p75 | 0.685645 | 0.685645 | PASS |
| couples_worker_ratio | p90 | 0.767435 | 0.767435 | PASS |
| couples_worker_ratio | p95 | 0.805686 | 0.805686 | PASS |

Own recomputation `W1_F_obs/C_obs` vs the restricted file's own `ratio` field: singles max abs diff `0.000e+00`, couples max abs diff `0.000e+00` (both restricted to worker subsamples).

## (e) Invariance to common equivalisation

Singles, using the real accepted `m_oecd`: max abs diff between `W1_F_obs/C_obs` and `(W1_F_obs/m_oecd)/(C_obs/m_oecd)` over all 1336 workers: `2.220e-16`.

Couples, using an independent synthetic positive multiplier (`Uniform(0.5,3.0)`, seed `908070605`, chosen independently of the memo's seed): max abs diff over all 2173 workers: `2.220e-16`.

## Notes

- Household-level values are not reproduced in this report; all numbers above are dwt-weighted aggregates over the full singles (N=1,540) or couples (N=2,223) ACCEPTED_FRAME, or their worker subsamples.
- Weighted-statistics implementation (own, independent): ascending sort, cumulative weight `S_i`, midpoint rank `r_i=(S_i-0.5 w_i)/T`; median/percentiles via linear interpolation of `(r_i,x_i)`; Gini via `2/(T*mean_x) * sum_i w_i (x_i-mean_x)(r_i-0.5)` — same convention as `baseline_f1_verification_v1.md`, implemented independently here.

## Follow-up: corrected couples equivalised numbers

Date: 2026-09-12

The memo `JMP_BASELINE_F1_equivalised_reporting_v1.md` has since been corrected to use `experiments/JMP_SEMINAR_SPRINT/runs/final_couples_welfare/cw_equivalence_scale_v1.parquet` (columns `idhh, n_persons, n_14plus, n_under14, n_under18, m, m_two_adult_form`) as the couples counterpart to the singles scale artifact, resolving the (c) FAIL logged above. This follow-up independently re-verifies ONLY the corrected couples §2 numbers; singles and the worker-ratio section were not re-checked (they already passed above and are unaffected by this correction).

New independent script (written from scratch, does not import `report_baseline_f1_equivalised_v1.py`), executed via `C:\Users\hisham\Repo\MNL\.venv\Scripts\python.exe`.

Method:
1. Loaded `couples_household_v1.jsonl` from `C:\Users\hisham\MNL\EUROMOD-STORAGE\restricted\baseline_f1_prep_v1\` — 2,223 rows confirmed, columns `C_obs, L_home, L_obs, W1_F_obs, beta_c, diagnostics, observed_nonworker, parameter_sha256, parameter_table, ratio, sample, source_idhh`.
2. Joined `dwt` from `couples_engine_ready_criterion_a_v1.parquet` (`outputs/corr/s10_criterion_a_iid_r100_v1/`), filtered `is_chosen==1`, deduped on `source_idhh` — 2,223 chosen rows, 0 unmatched.
3. Joined `m` from `cw_equivalence_scale_v1.parquet` on `source_idhh == idhh` — 2,275 scale rows available, **0 of 2,223 unmatched** (confirms the coverage claim in the (c) section above).
4. Computed `C_eq = C_obs/m`, `W_F_eq = W1_F_obs/m`, and dwt-weighted mean/median/Gini for `C_eq`, `W_F_eq`, and `m` itself, using the identical S12/M08 weighted-statistics convention documented above (ascending sort, midpoint rank `r_i`, linear-interpolated weighted median, Gini via `2/(T·mean_x)·Σ w_i(x_i−mean_x)(r_i−0.5)`).

### Result: PASS — exact agreement

| Object | Stat | Independent | Memo (corrected §2) | Rel. diff |
|---|---|---:|---:|---:|
| couples C_eq | mean | 2245.109852 | 2245.110 | 6.60e-08 |
| couples C_eq | median | 2062.837017 | 2062.837 | 8.33e-09 |
| couples C_eq | gini | 0.226805 | 0.226805 | 7.01e-07 |
| couples W_F_eq | mean | 1310.614979 | 1310.615 | 1.56e-08 |
| couples W_F_eq | median | 1237.352468 | 1237.352 | 3.78e-07 |
| couples W_F_eq | gini | 0.197403 | 0.197403 | 6.41e-07 |
| couples m | mean | 1.922223 | 1.922223 | 6.58e-08 |
| couples m | median | 1.800000 | 1.800000 | 0.00e+00 |
| couples m | gini | 0.107821 | 0.107821 | 2.09e-06 |

N = 2,223 for all rows above, matching the memo. All nine statistics agree to well inside the 1e-6-relative expectation (worst case 2.09e-06 on the `m` Gini, attributable to the memo reporting rounded-to-6-decimal values; every check independently reproduces the memo's reported figure to its own precision).

**Verdict: PASS.** The corrected couples §2 table in `JMP_BASELINE_F1_equivalised_reporting_v1.md` is independently reproduced exactly from the raw restricted file, the dwt-bearing engine-ready parquet, and the `cw_equivalence_scale_v1.parquet` scale artifact. The joins are clean (0/2,223 unmatched on both `dwt` and `m`), superseding the prior (c) FAIL — that FAIL was about the memo's incorrect claim that no couples scale artifact existed, not about any numeric error, and is now moot given the artifact is in use and reproduces correctly.

