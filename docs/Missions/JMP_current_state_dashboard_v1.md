<!-- GOVERNANCE DOCUMENT — CURRENT-STATE SURFACE -->

# JMP Current-State Dashboard v1

**Programme:** Goal 1 — Empirical JMP
**Last updated:** 2026-09-03, at Goal-1 **R-233** (**the programme is in RESEARCH-FIRST / PRESENTATION-FIRST SEMINAR SPRINT mode** — *"MORE RESEARCH, LESS GOVERNANCE"*: a narrow documentation cap, the GPU hands-on research environment as priority zero, a closed singles candidate set, one welfare measure, clean both-flexible couples only, and external identification paused but not abandoned. R-230 and R-231 are **FILLED** — the CPL-A adapter is accepted with C1 escalated, and the HP/HO disposition plus the PKG-03 C1–C4 conventions are ruled: **C1 is the O-5 convention**, C2/C3 are flexible-only, the C4 channel inventory is deferred. One item is **RETURNED**: the seminar parameter count of 35 is not reproduced by any count on disk (51 coordinates / 41 free / 10 pinned / 39 interior), so no parameter count is published until the deputy resolves it. Carried forward unchanged from R-232: **S9 SELECTION IS COMPLETE and corrected S8 is FORMALLY RETAINED as the final positive model** — W3 joined HP and HO as NOT IDENTIFIED, so no heterogeneity extension earned admission and, under the deputy's §9 rule, no S9 extension is invented; "S9" names the selection, not a specification. LOC4 remains the benchmark for the specification-sensitivity finding. `TORCH_BACKEND_JMP_READY` becomes `PENDING_PARITY_EXPORT`; the export itself is a later card, at freeze. No welfare number is promoted and no provisional label is lifted.)
**Standing:** Established by the PI STANDING DIRECTION — PRACTICAL RESEARCH
MODE (recorded verbatim at Goal-1 R-168): *"Maintain one current-state
dashboard rather than multiple overlapping status memos."*

**This file is THE status surface from R-168 forward.** Superseded status
memos are no longer created. Existing status memos remain valid as immutable
history of the moment they recorded; they are not the current state. Update
this file in place; do not fork a v2 for a status change.

This dashboard is a pointer surface, not an authority. Where it and a ratified
document differ, the ratified document governs.

---

## 1. Programme status labels — all current

| Label | Object it qualifies | Set at |
|---|---|---|
| **`SEMINAR_RESEARCH_SPRINT_MODE`** + **`SPRINT_DOCUMENTATION_CAP_IN_FORCE`** | the programme for roughly fifteen days — RESEARCH-FIRST / PRESENTATION-FIRST, *"MORE RESEARCH, LESS GOVERNANCE"*, on the premise that *"Accepted specifications are reproducible benchmarks, not restrictions on scientific experimentation."* The cap is narrow and operative: exploratory work retains ONLY `experiments/JMP_SEMINAR_SPRINT/{run_registry.csv, model_comparison.csv, decision_log.md, configs/, runs/, figures/, JMP_GPU_lab.ipynb}`; each run needs a config, a result JSON, a parameter CSV, runtime/convergence, key fit diagnostics and ONE registry row — **no prompt archive, no per-run memo, no per-run software review**, and no new mission-document family | **R-233** |
| **`GPU_RESEARCH_ENVIRONMENT_PRIORITY_ZERO`** | a researcher-facing native-Windows Torch/CUDA workflow in an ISOLATED environment — **the MNL package pin does not move** (`27756a06`). Exactly ONE local application parity check against the CPU/JAX route on the same data, theta and specification (objective, gradient, parameter ordering, Hessian where practical): *"one technical sanity check, not a new certification programme."* If the Torch grammar cannot represent the economic model exactly, **the model is not simplified to use CUDA** — JAX is used and the missing generic capability is named. The research bundle is built and verified at `MNL/experiments/JMP_SEMINAR_SPRINT/export/gpu_research_bundle_v1/`; it is a RESEARCH bundle and **not** the final parity export | **R-233** |
| **`SINGLES_CANDIDATE_SET_CLOSED`** | the singles specification sprint — corrected S8, the simple occupation-conditioned structural wage model (which *is* corrected LOC4/S0), and W3 only if its gate passed. It did not, so it is closed. **NOT opened:** hours-conditioned structural wages, occupation × hours interactions, occupation-specific slopes, occupation-specific dispersion, further HP or HO variants, large specification searches | **R-233** |
| **`SEMINAR_PARAMETER_COUNT_35_VS_41_RETURNED`** | the seminar parameter count — **RETURNED to the deputy, not adopted**. R-233 §4 states 35 actually estimated parameters; the corrected-frame record is **51 coordinates, 41 free, 10 pinned, 39 interior**, `k = 41` is the constant in every AIC/BIC on the record and `K_interior = 39` the primary CR1 constant (R-184.1). No convention on disk yields 35; the nearest are 39 and 34. **No parameter count is published in seminar prose or tables until this is resolved.** What §4 says unambiguously IS adopted: the historical 47-coordinate pooled vector is not carried into seminar tables or prose, and the ten pinned non-estimated couples coordinates are not displayed in the singles parameter table | **R-233** |
| **`C1_O5_CHOSEN_ROW_CONVENTION_RULED`** | the chosen-row convention — **the O-5 convention governs.** The observed chosen alternative is inserted **deterministically**, inclusion probability **one**, log proposal correction **zero**; stochastic alternatives use the **exact marginal** proposal density. `log_prior = 0` on the chosen row and `log_prior = log q_exact_marginal` on sampled rows are RETAINED; for semi-flexible couples `q_joint = q_flexible · 1_fixed`. **Singles and accepted couples are NOT re-anchored to PKG-03's draft rule — the PKG-03 handoff is amended instead.** Required metadata: `proposal.convention: exact_marginal` and `proposal.chosen_inclusion: deterministic_unit`, with `exact_marginal` referring to **stochastic** draws only. A stochastic row that duplicates the chosen pair economically keeps both row roles with their own corrections and is **not** silently deduplicated | **R-231** |
| **`C2_C3_FLEXIBLE_ONLY_VALIDATION_RULED`** | the age gate and the wage-support screen — **flexible decision-makers only**. A fixed spouse may be older than 64 and remains a roster member with fixed observed state, earnings and budget input; G-18 is amended to validate only the flexible spouse and **the 1,453 households are not excluded on the fixed spouse's age**. The fixed spouse's observed wage is not sampled, not varied and carries no proposal density — finite, coherent and EUROMOD-valid is enough. The corrected flexible-only counts stand, **including CM = 587** | **R-231** |
| **`C4_CHANNEL_INVENTORY_DEFERRED`** | the 20 inherited `MISSING_CHANNEL` cases — the mandatory-channel rule applies to **model terms**, not every raw engine-ready column. Each item gets either exactly one explicit channel (if consumed as a structural term) or a declared **data role** (identifier, join key, proposal bookkeeping, fixed-spouse coordinate, EUROMOD budget input, report or validation-only). **No silent defaults; no mislabelling fixed budget inputs as preferences or opportunities to pass validation.** A validator that demands structural channels for raw non-model columns returns to Goal 2 as a **schema correction**. **DEFERRED** — not seminar-critical, gated behind the Goal-2 return, and parked with the lane by R-233 §13 | **R-231** |
| **`PKG03A_PARKED_AVAILABLE_INFRASTRUCTURE`** | the Goal-2 semi-flexible handoff — recorded as available infrastructure and **parked** until after the presentations, unless clean both-flexible couples finish substantially early. Feature commit `5b82e162…`, bundle SHA `4FC99B87…`, wheel SHA `74EB24AD…`. Goal-1 evidence parked with it: the r6 adapter RE-TEST at **19/19 on all three real tests** (MNL `b9fb98c`). **No package-main movement. No MNL-pin movement.** `SEMI_FLEXIBLE_MARGINAL_PROPOSAL` stays GATED | **R-230**, parked **R-233** |
| **`EXTERNAL_IDENTIFICATION_PAUSED_NOT_ABANDONED`** | BMO, LFS auxiliary identification, DADS external wages, the expanded sample, semi-flexible couples and multi-adult households — **execution paused**, retained as future identification / validation extensions. The presentation may show what each *would* discipline; it may **NOT** imply any of them has already identified the current model | **R-233** |
| **`HP_RANDOM_LEISURE_INTERCEPT_NOT_RECOVERABLE`** + **`HO_COMMON_WORKING_FRAILTY_NOT_RECOVERABLE`** | the two heterogeneity lanes — the deputy's own classification of the negative synthetic-recovery findings, adopted verbatim. These **reject the tested specifications, not the existence of unobserved heterogeneity in general**, and no additional HP or HO variant may be opened in the present sprint. They sit alongside, and do not replace, `HP_NOT_IDENTIFIED_UNDER_CURRENT_DESIGN` (R-226) and `HO_NOT_IDENTIFIED_UNDER_CURRENT_DESIGN` (R-227.2) | **R-231** |
| **`FORMALLY_RETAIN_CORRECTED_S8_AS_FINAL_POSITIVE_MODEL`** | corrected S8 on the R-222 `floor5_v1` frame — **the final positive model**. Set by the S9 selection: no heterogeneity extension earned admission, so under the deputy’s §9 rule S8 is retained rather than an S9 extension invented. **Replaces** `S8_ACCEPTED_POSITIVE_BENCHMARK_NOT_FINAL_JMP_MODEL` (R-220 s5), whose "not final while persistent heterogeneity and final model selection remain open" condition is now discharged | **R-232** |
| **`S9_SELECTION_COMPLETE`** + **`NO_S9_EXTENSION_ADMITTED`** | the S9 stage — **complete**. There is no S9 specification; from here "S9" names the **selection**, not a model | **R-232** |
| **`LOC4_REMAINS_SPECIFICATION_SENSITIVITY_BENCHMARK`** | LOC4/S0 — retained as the nested reference and as the benchmark the specification-sensitivity finding is stated on; not demoted, not a rival, **not a candidate** | **R-232** |
| **`PERSISTENT_HETEROGENEITY_CLOSED_UNDER_CURRENT_DESIGN`** | HP, HO and W3 together — all three authorized persistent-heterogeneity designs return NOT IDENTIFIED on the corrected frame, through **three different mechanisms**. A statement about **this design and this data** (one cross-sectional choice per household, 1,555 households, 101 sampled alternatives, at the estimated Box-Cox curvature) — explicitly **NOT** a finding that preference, opportunity or wage-residual/preference heterogeneity is absent, and no such claim may be made in paper-facing prose | **R-232** |
| **`W3_NOT_IDENTIFIED_UNDER_CURRENT_DESIGN`** | the wage-residual / preference dependence `beta_l0_i = beta_l0^g + sigma_l·nu_i` with `corr(nu_i, e_w_i) = rho_wl` — feasibility gate D fails on **all three** parameters *including the product* `gamma = rho·sigma_l` (0/4, 1/4, 0/3 truths). A **third** distinct failure mode: `sigma_l` never reaches zero while `rho` runs to its ±0.99 box endpoint at every truth, so `gamma` is nearly unbiased yet has **no obtainable interval**. The LR against S8 has **no valid null reference** — `rho` is unidentified at `sigma_l = 0` and `sigma_l` is on its boundary. No real-data run; the real-data instrument was deliberately never built | **R-229** |
| **`W3_CONTRIBUTES_NO_S9_CANDIDATE`** | S9 selection — W3 supplies no supported candidate | **R-229** |
| **`S8_PREFERRED_SINGLES_POSITIVE_SPECIFICATION`** | S8 = S0 + S3 (LOC4/S0 plus the explicit 35-hour opportunity peak), the preferred **singles positive** specification | **R-183** (`_PENDING_BOUNDED_REVIEW` set R-182, discharged by `S8_ACCEPTED`) |
| **`S0_ACCEPTED_NESTED_REFERENCE_BENCHMARK`** | S0, the nested reference benchmark | **R-182** |
| **`ACCESS_ABILITY_ORDER_UNRESOLVED_UNDER_S8`** | the A/B ordering under S8 — **unresolved, not reversed** | **R-182** |
| **`NO_CROSS_MEASURE_QUANTITATIVE_ROBUSTNESS_CLAIM`** | W4/W6 against W1 — normative sensitivities only | **R-182** |
| **`FC1_CLOSED_AT_R227`** | the five-hour-floor correction and the corrected S8/LOC4 anchors — **accepted and closed**; `floor5_v1` is used prospectively and pre-correction results remain historical | **R-227 s1** |
| **`HP_NOT_IDENTIFIED_UNDER_CURRENT_DESIGN`** | the random leisure intercept `beta_l0_i = beta_l0^g + sigma_l·nu_i` — expected LR 0.0081 / 0.1351 against the 2.706 the boundary test needs, short *in expectation*; STEP 3 real data **not run by rule**, so no `HP_SUPPORTED_CANDIDATE` / `HP_NOT_SUPPORTED` verdict is issued | **R-226** |
| **`HP_CONTRIBUTES_NO_S9_CANDIDATE`** | S9 selection — under the deputy's §9 rule, if no heterogeneity extension earns admission **S8 is formally retained** as the final positive model | **R-226** |
| **`HO_NOT_IDENTIFIED_UNDER_CURRENT_DESIGN`** | the opportunity-intensity frailty — `log g^E_ij` gains `sigma_o·eta_i` on every working alternative. The loading has four times HP's within-choice-set spread and the **axis** expected LR is 1.02 / 13.56 at truths 0.5 / 1.0 (HP: 0.008 / 0.135), but `eta` shifts every working alternative equally, so HO is exactly a **binary mixed logit on the employment margin with one observation per household**; re-fitting the S8 coordinates under `sigma_o = 0` absorbs ~95 % of the signal (`beta_E` −3.334 → −3.791), leaving **PROFILE** expected LRs of **0.0492 / 0.6996** against 2.706. STEP 3 real data **not run by rule** | **R-227.2** |
| **`HO_CONTRIBUTES_NO_S9_CANDIDATE`** | S9 selection — HO supplies no supported candidate | **R-227.2** |
| **`BOTH_AUTHORISED_HETEROGENEITY_LANES_NEGATIVE`** | HP (§26) and HO (§29) have both returned NOT IDENTIFIED. Under the deputy's §9 rule this makes **formal retention of S8** the standing disposition; `HPO_GATED` is retained and is *harder*, not easier, after HO. **W3 (§30) then returned NOT IDENTIFIED as well (R-229)**, and the retention was taken formally at **R-232** | **R-227.2**, extended **R-229** |
| **`SEXP_PRIMARY_A1_CANDIDATE_NOT_FINAL_POPULATION`** | the 18–64 / τ=0.20 expanded sample (5,573 households, weighted 13,880,855) — a candidate **for estimation**, not yet the final JMP population; `BENCH_CURRENT_3830` stays the clean benchmark and the 17–65 arm is descriptive only | **R-227 ss2–3** |
| **`SEMI_FLEXIBLE_MARGINAL_PROPOSAL`** | the one missing capability for CM/CF — **GATED** on eight requirements, generic implementation required, before any real-data expanded-couple estimation | **R-227 s8** |
| **`COUPLES_WELFARE_UNIT_RATIFIED`** | type-specific references, cross-type reporting in equivalized units only, modified OECD primary — with the **calibration identity** as a hard cross-type halt, **not yet evaluated** | **R-227 s9** |
| **`PARITY_AXIS_ADDITIONS_ONLY_HALT_DISCHARGED_R227_CARVEOUT`** | the additions-only parity axis — discharged for **exactly three paths** on recorded before/after hashes; §5 carries the record | **R-227 s10** |
| **`TERMINOLOGY_REDLINE_PENDING_02_FRAMEWORK_03_DATA`** | `manuscript/sections/02_framework.md` and `03_data.md` — flagged for a redline pass under the §7 standing note; deliberately not edited at R-227 | **R-227 s12** |
| **`R1_BMO_NEGATIVE_RESULT_CLOSED`** | the `R1_BMO_NUTS2_OCCUPATION_TENSION` leg — **closed as a negative result**; supersedes `R1_BMO_OMITTED_PENDING_ACCESS` (R-198), which was discharged when R-210 lifted the s5c halt | **R-218 §9** |
| **`R1_BMO_NO_ADDITIONAL_OCCUPATION_ACCESS_SIGNAL`** | the BMO tension coefficient across all three arms — no detectable structural occupation-access signal **in the current sample and specification**; not a claim that regional occupation demand is generally irrelevant, and not identification evidence in the headline model | **R-218 §9** |
| **`DB040_F_RECODE_NOT_USED`** + **`FULL_SAMPLE_GENUINE_REGION_OBSERVED`** | the EU-SILC missing-region recode — it **never fired**; `DB040_F == -1` count `0` over all 11,459 register households, so the s5c contamination concern is closed and the s5c restricted sample IS the full sample | **R-210** |
| **`COMMON_SUPPORT_EXHAUSTIVENESS_VALIDATED`** | the common quadrature support as the decomposition estimator — a **numerical integration** correction, explicitly NOT a common realized economic opportunity set | **R-217 §12**, gate passed **R-218** |
| **`FEMALE_PRIMARY_PLUS_MALE_ZERO_SENSITIVITY`** | the reference-preference block on the union basis — female primary, male structural-zero sensitivity, **never averaged**; supersedes `FEMALE_PRIMARY_PLUS_MALE_SENSITIVITY` for the common-support arms | **R-217 §12** |
| **`REFERENCE_SENSITIVE_MAGNITUDE`** | the `C_P` magnitude on S8 and LOC4 — same sign and environment dominant under both references (branch A), but the female/male difference exceeds the RQMC bands | **R-218** |
| **`SHARED_CHILD_COEFFICIENT_DIAGNOSTIC`** | the arm inserting the female child coefficient into the otherwise male block — **diagnostic only**; not the official male reference, not an estimated male coefficient, not a preferred specification, not a headline arm | **R-217 §4** |
| **`ABSOLUTE_WELFARE_LEVELS_NOT_FINAL`** | the common-support W00 magnitudes — they move −5.53% (S8) and −7.74% (LOC4) against the prior own-support estimates; the support-design movement is disclosed and no proposal-invariance claim is made | **R-217 §8** |
| ~~`MALE_REFERENCE_OPERATOR_CORRECTION_PENDING`~~ | set at **R-217 §12** and **DISCHARGED at R-218**: the structural-zero correction was applied and `I1111` collapsed to exact numerical zero in the corrected male arms | set R-217 §12, discharged **R-218** |
| **`NUTS2_EXTERNAL_OPPORTUNITY_IDENTIFICATION_AID`** + **`NOT_A_CAUSAL_INSTRUMENT`** | the BMO regional design | **R-182 §5** |
| **`CORSE_RETAINED_AS_OWN_NUTS2_CELL`** | Corse's 3 households and their own 2015 BMO NUTS-2 tension value | **R-182 §5(b)** |
| `LOC4_PREFERRED_STRUCTURAL_SPECIFICATION` | the preferred structural specification | R-157 |
| `BASELINE_ACCEPTED_NESTED_REFERENCE_SPECIFICATION` | the corrected common-dispersion model | R-157 |
| `T2A_PROFILE_ACCEPTED_WITH_COMPONENT_SIGN_QUALIFICATION` | T2-A `beta_w_pexp2` profile | R-161 |
| `LOC4_PROFILE_ACCEPTED` | the profile evidence | R-161 |
| `W1_MEAN_PROFILE_STABLE` | W1 mean over the profile region | R-161 |
| `A_GREATER_THAN_B_GREATER_THAN_P_PROFILE_STABLE` | component ordering | R-161 |
| `PHI_B_SIGN_UNRESOLVED_95_PROFILE` | `sgn(phi_B)` inside the 95% profile-LR region | R-161, re-affirmed **R-175** |
| **`LOC4_PREFERRED_MC_BANDED_LEVELS`** | the JMP-M08T2 closing verdict | **R-175** |
| **`MC_BANDED_LEVELS`** | the LOC4 W1 magnitudes | **R-175** |
| **`MC_BANDED_NORMALIZED_DIAGNOSTIC`** | `r_phi_P` and `r_R_bg` | **R-175** |
| `MC_BAND_ONLY_NONSMOOTH` | the W1 median | R-161, re-affirmed **R-175** |
| `T2B_RQMC_IMPLEMENTATION_ACCEPTED_PREPRICING` | the T2-B RQMC implementation and its pre-pricing gate | R-168 |
| `M08_BASELINE_PROTOTYPE_LIMITED_MC_PRECISION` | the closed M08 prototype | R-138 §9 |
| `PROVISIONAL_NOT_PROMOTED_MC_PRECISION` | the 16x welfare functionals (baseline arm) | R-138 |
| `PARITY_AXIS_DISPOSITION_RETIRED_SUPERSEDED_BY_RENAME_AWARE_ALIAS_CLOSURE` | the old Stage-2 parity record | R-157 §9 |
| **`W0_USES_OBSERVED_HOURLY_WAGES_FOR_WORKERS`** | the production wage convention — `yivwg` reproduces `yem*(12/yemmy)/(lhw*52/12)` for every FR_2016_a3 person with observed wage inputs, so the structural wage density and the education/experience loadings are fitted against **observed** worker wages, not fitted conditional means | **R-220 s1** |
| **`W1_NOT_DISTINCT_FROM_W0`** | the W1 arm — not estimated; the correctly annualized observed-wage reconstruction is numerically equivalent to `yivwg` for workers and supplies no model comparison | **R-220 s2** |
| **`W2_VACUOUS_UNDER_PRODUCTION_LIKELIHOOD`** | the W2 arm — not estimated; non-worker `yivwg` enters neither the likelihood, nor `g^W`, nor the `q^W` sampler, nor the chosen non-employment alternative | **R-220 s2** |
| **`W0_W1_W2_AXIS_CLOSED`** | the wage-treatment axis as a whole — **closed** | **R-220 s2** |
| ~~`S8_ACCEPTED_POSITIVE_BENCHMARK_NOT_FINAL_JMP_MODEL`~~ | S8 — set at **R-220 s5** (itself replacing `S8_ACCEPTED_POSITIVE_BENCHMARK_PENDING_WAGE_ROBUSTNESS`), and **REPLACED at R-232** by `FORMALLY_RETAIN_CORRECTED_S8_AS_FINAL_POSITIVE_MODEL`: its condition was *"not final while persistent heterogeneity and final model selection remain open"*, and both are now closed | set **R-220 s5**, replaced **R-232** |
| ~~`FINAL_POSITIVE_MODEL_SELECTION_HALTED_PENDING_LHW_FLOOR_CORRECTION`~~ | final positive-model selection — set at **R-220 s3** on the 7 unintended `lhw`-clip households, and **DISCHARGED at R-224**: the correction was authorized at R-222, executed, and accepted with every gate PASS and no return condition fired | set **R-220 s3**, discharged **R-224** |
| **`HOURS_CAP_70_SUPPORT_PROJECTION_CONVENTION_RECORDED`** | the 70-hour cap — the correct behaviour, now a recorded convention rather than an implicit one | **R-220 s3** |
| **`LHW_FLOOR_10_UNINTENDED_DATA_CONSTRUCTION_INCONSISTENCY`** | the `hours_floor_low = 10` clip — classified an unintended data-construction inconsistency, not a support projection: `hours_inactive_threshold = 5` already puts 6–9-hour observations inside the latent working support | **R-222** |
| **`LHW_FLOOR_5_CORRECTION_ACCEPTED`** | the successor frame `fr_p2a_singles2016_regionlive_margqh_floor5_v1` — the **sole forward-looking France singles frame**; supersedes `LHW_FLOOR_5_CORRECTION_AUTHORIZED` (R-222) | **R-224** |
| **`S8_CORRECTED_FRAME_ACCEPTED_POSITIVE_ANCHOR`** | corrected S8 — the positive-model anchor **prospectively**; the pre-correction estimate is retained as history and is not edited out of anywhere it was written | **R-224** |
| **`LOC4_CORRECTED_FRAME_ACCEPTED_POSITIVE_ANCHOR`** | corrected LOC4/S0 — same disposition | **R-224** |
| **`RUM_BENCHMARK_STALE_FOR_FINAL_REPORTING_PENDING_CORRECTED_FRAME_UPDATE`** | the existing RUM benchmark — **STALE for final reporting**; no rerun now, re-estimated **once** at final S9 reporting on the same corrected frame the final RURO model uses | **R-222 s8** |
| **`PRE_CORRECTION_PROVISIONAL_WELFARE_HISTORY`** + **`NOT_VALID_FOR_FINAL_MAGNITUDES`** | **every** existing S8/LOC4 welfare and decomposition value — pre-correction history; the common-support welfare infrastructure itself is **not** rejected | **R-222 s9** |
| **`WELFARE_REFRESH_DEFERRED_TO_FINAL_S9`** | the welfare panels — no automatic reprice is triggered by the estimation-frame change; the common-support cache-independence test is deferred to final S9 | **R-222 s9** |
| **`EXTENDED_HOUSEHOLD_BUDGET_ROBUSTNESS`** | the multi-adult (3+ adults) sample lane — held out of the headline welfare sample until pooling, tax unit, allocation, additional-adult needs and welfare unit are explicit | **R-223 s6** |
| **`PROVISIONAL_PIPELINE_RESULT_PENDING_WAGE_ROBUSTNESS`** | **every** welfare number produced by Lane A, Channel D and the ex-ante diagnostic, without exception | **R-202 s2**, re-imposed R-204 §8 and R-207 |
| **`HEADLINE_PERCENTAGES_HALTED`** | the `s_P` / `s_E` headline shares — halted, not renormalised, the exhaustiveness target unchanged | **R-203**, re-affirmed **R-205**, **R-208** |
| **`CHANNEL_D_IMPLEMENTATION_VALIDATED`** | the channel-D execution — a valid diagnostic result | **R-207 §8** |
| **`BUDGET_HETEROGENEITY_NOT_THE_I1111_SOURCE`** | channel D as a candidate residual — refuted | **R-205**, ratified **R-207 §8** |
| **`FEMALE_PRIMARY_PLUS_MALE_SENSITIVITY`** | the reference-preference block; sign of `C_P`, the broad P/E reading and the A/B/D ordering are all preserved on both S8 and LOC4 | **R-204 §7**, retained **R-207 §7** |
| `EX_ANTE_SUPPORT_DIAGNOSTIC_IN_PROGRESS` | the ex-ante continuum diagnostic — **DISCHARGED**: it ran to R-207's §5 failure branch, and the object was returned at **R-208** and ruled on at **R-209** | set R-207 §8, discharged R-208 |

### 1.1 The corrected anchors of record (R-222 / R-224)

The pre-correction frame is superseded **prospectively**. Nothing estimated on it
is withdrawn; it is retained as history and stays on the record wherever it was
written.

| object | value |
|---|---|
| successor frame id | `fr_p2a_singles2016_regionlive_margqh_floor5_v1` |
| successor **geometry** sha256 | `a91b1f81752c8406a0b12f38a2e4e9bab0aa04640cb31bf730cacf7795be23e1` |
| successor **stem** sha256 | `6f558f5ecfeabd4aa60a8199f43576c27f15cb203a6b9dc0e2df04b20145173b` |
| pre-correction stem sha256 (untouched) | `4cc6a223c184ed78e6b78bf330f6559e295c520c207078bd9e312d3eec71dced` |
| rows / households | 157,055 / 1,555 — **unchanged** |
| what moved | `hours_floor_low` 10 → 5; 7 chosen alternatives, 0 drawn alternatives at node level |

**negLLs of record.** These replace the pre-correction values in every forward
comparison; a heterogeneity model on the corrected frame may **never** be compared
against a benchmark estimated on the old one (R-222 s10).

| model | corrected negLL (of record) | pre-correction negLL (history) |
|---|---|---|
| **S8** | **`18022.764617170084`** | `18022.456443792806` |
| **LOC4 / S0** | **`18453.4750133318`** | `18453.054494167016` |

**The S8-versus-LOC4 structural conclusion is unchanged.** `beta_h_f35` keeps its
sign and INTERIOR status at `2.5795` (robust se `0.0983`, z `26.24`); the 1-df LR
statistic is `861.42` and still rejects S0 at 0.001; ΔAIC `−859.42` and
ΔBIC(households) `−854.07` still order S8 first. Both corrected models are
SINGLE-OPTIMUM, full-rank and `clean`-tier, with the active-bound set
`{beta_l_age2_sf, beta_l_age2_sm}` and the W-4 flagged set unchanged in both.
Evidence: `experiments/JMP_PS1/runs/ps1r222_floor5/` (MNL) and decision note §25.

**Superseded at R-175:** `RQMC_FINAL_PRECISION_PENDING` (set R-157 / R-161) —
the pass has run and is disposed of. The evaluation runner's mechanical
`PHI_B_POSITIVE_PROFILE_STABLE` output is superseded by
`PHI_B_SIGN_UNRESOLVED_95_PROFILE`.

**Withdrawn from the S8 claim set at R-182:**
`A_GREATER_THAN_B_GREATER_THAN_P_PROFILE_STABLE`. It stands **on the LOC4/S0 arm**
where it was set; it must **not** be carried into any S8 or successor claim.
Under S8 the A/B leg is unresolved, so the collective ordering disappears.
`PHI_B_SIGN_UNRESOLVED_95_PROFILE` is **untouched** — S8 carries an RQMC
numerical-integration band only, no profile envelope, and its positive numerical
`phi_B` level cannot be promoted into a sign statement.

**Primary claim region.** The conventional 95% profile-LR support region, with
the active-set/boundary caveat (R-161). The 90% region is a supplementary
sensitivity only.

**Pricing standing.** Eight-scramble RQMC pricing **has run** (R-175):
2,549,225 nodes in 5.2123 h of EUROMOD time against the 7 h guard; sealed
priced panel `b1879fcf2c210d337a4f4d3bfff93d06a6e044f8da1326f6ca3a5ab168d76f00`.
Both statistical t-bands remain deleted from the R3 pass path and are diagnostic
only. **No further numerical instrument is authorized on this benchmark.**

**Frozen at R-175, banded.** The eight manuscript-facing LOC4 quantities —
W1 mean `1339.0426 ± 2.1105`, W1 Gini `0.15114755 ± 0.0010869`,
`phi_A 0.00291492 ± 0.00039130`, `phi_B 0.00070562 ± 0.00065901`,
`phi_P −0.35279421 ± 0.00078335`, `R_bg 0.50032122 ± 0.00072355`,
`phi_A+phi_B 0.00362054 ± 0.00067681`, `s_opp 0.02395367 ± 0.0043248`. These are
numerical-integration bands, **never** confidence intervals.

**Nothing from the welfare-decomposition lanes is claimable.** No `s_P` / `s_E`
share, no `C_P` / `C_E` / `C_A` / `C_B` / `C_D` magnitude and no ex-ante cell may
be reported. The headline is HALTED at R-203, stays halted through R-205 and
R-208, and every number carries
`PROVISIONAL_PIPELINE_RESULT_PENDING_WAGE_ROBUSTNESS`. The sign facts that ARE on
the record are diagnostic only: `C_P < 0` in every arm, `I1111` about three times
`I0000` in every arm, and the reference-preference operator acting as an
amplifier rather than a source.

**Still not claimable.** Cross-measure W4/W6 quantitative robustness; a
precision-certified `r_phi_P` or `r_R_bg`; any collective component-sign
statement; any combination of the RQMC band with the profile envelope; any
causal transfer/absorption language (R-157 claim-set conditions). The claim
boundaries of record are `JMP_M08_LOC4_manuscript_claim_set_v2.md`.

---

## 2. Missions — open and closed

| Mission | State | Closing / governing document |
|---|---|---|
| JMP-M05 — household-clustered inference, design | CLOSED | `JMP_M05_deputy_programme_acceptance_v1.md` |
| JMP-M05B — phase-5 implementation | CLOSED (paused, superseded by M05C) | `JMP_M05B_pause_and_M05C_redesign_decision_v1.md` |
| JMP-M05C — minimal streaming inference | CLOSED | `JMP_M05C_deputy_phase5_acceptance_v1.md` |
| JMP-M07 — inference/results integration | CLOSED | `JMP_M07_deputy_closeout_and_identity_ruling_v1.md` |
| JMP-M07I — manuscript identity alignment | CLOSED | `JMP_M07I_identity_alignment_acceptance_v1.md`, rider `JMP_M07I_manuscript_claim_rider_v1.md` |
| JMP-M08 — singles welfare decomposition | CLOSED as prototype under `M08_BASELINE_PROTOTYPE_LIMITED_MC_PRECISION` | `JMP_M08_singles_welfare_decomposition_mission_charter_v1.md`; rulings R-129/R-131/R-138 |
| JMP-M08E — estimand correction / E2 closure | CLOSED | `JMP_M08E_E2_closure_notebook_and_RUM_ruling_v1.md` |
| JMP-HK-01 — housekeeping / archive | CLOSED | `HK01/` register set; MNL `192ef57`, JMP `9e15e56` |
| JMP-M08T2 — LOC4 boundary analysis and final numerical precision | **CLOSED at R-175**, verdict `LOC4_PREFERRED_MC_BANDED_LEVELS` | acceptance `JMP_M08_LOC4_preferred_spec_acceptance_v1.md`; claim set `JMP_M08_LOC4_manuscript_claim_set_v2.md`; charter `JMP_M08T2_LOC4_boundary_and_final_precision_charter_v1.md` |
| **JMP_PS1 — positive-specification sprint (S1..S8)** | **ESTIMATION PHASE CLOSED at R-183** — S8 accepted, verdict `S8_ACCEPTED`; the sprint continues only as the BMO exploratory leg | `Design/JMP_post_meeting_research_agenda_v1.md` §3–4, §12; MNL `experiments/JMP_PS1/decision_note.md` §11 |
| **JMP couples — joint household specification** | **COMPUTATIONS COMPLETE through phase 4** (p1–p6; C-P3 estimated, C-P4 built, synthetic gate run to R=10) — **NOT PROMOTED**, verdict `GATE_FAIL` on `beta_l0_m`, `beta_occ_2`, `beta_w_educL` | ruling R-182 §7; R-187 / R-188 / R-189.2 / R-190.2; MNL `experiments/JMP_PS1/decision_note.md` §12–14 |
| **`R1_BMO_NUTS2_OCCUPATION_TENSION`** — regional exploratory | **STOPPED at step 0 s5c**, `R1_BMO_OMITTED_PENDING_ACCESS` — formula frozen before results (§15.1), crosswalk chain rebuilt and audited, Corse constructible (88/88), but the raw missing-location flag is unrecoverable on all ten routes. **The data were found at R-199**, so the resumption is concrete: the sealed enclave bundle (R-195) and the restricted-data script pack (R-200) are built and carried in by hand | ruling R-182 §5–6, R-193, R-194, R-199, R-200; MNL `experiments/JMP_PS1/decision_note.md` §15 |
| **Agenda item 8 — conditional wage draws (`q^W` part A, `g^W` part B)** | **ANSWERED, NOTHING PROMOTED** — part A retains `q^W \| occupation` unchanged on efficiency (pooled ESS 46.373 vs 45.0 / 41.0); part B's additive hours wage-location block is LR/AIC-favourable, BIC-adverse, degrades the fit battery and does not repair the wage-quintile misfit | R-201, R-202; MNL `experiments/JMP_PS1/decision_note.md` §16 |
| **Lane A — provisional four-cell welfare pipeline** | **HALTED at exhaustiveness** — `I11 = R_bg` is about 3× `I00`, so `s_P` / `s_E` are void; the architecture (cell map, operator accounting, bitwise `W00` gate, jackknife bands, pre-stated threshold) stands and is reusable | ruling R-202 s2; R-203; decision note §17, §18 |
| **Channel D — complete-environment decomposition** | **EXECUTED AND VALIDATED, HEADLINE STILL HALTED** — D removes budget dispersion entirely (`c_home` 0.371 → 0.000000) yet `I1111` barely moves, so **D is not the residual**; the priced NODE SUPPORT survives | ruling R-204; R-205; decision note §19 |
| **Ex-ante continuum diagnostic** | **RUN TO THE FAILURE BRANCH** — 8 of the 9 ruled sources measured ABSENT as drivers; the surviving object is the money-metric inversion's household-specific FROZEN REFERENCE CORE, returned at R-208 and ruled on at R-209 | interim R-206, superseded by R-207; R-208 / R-209; decision note §19.7 |
| **Lane B — wage treatment (`W0`/`W1`/`W2`)** | **CLOSED at R-220 s2** — `W0_W1_W2_AXIS_CLOSED`; the STEP-1 W2-gate halt is discharged, W1 and W2 are not estimated. The audit that produced this: — the audit overturns the ruling's premise: in FR_2016_a3 `yivwg` **is** the observed hourly wage (`yem×(12/yemmy)/(lhw×52/12)`) for **100%** of persons who have one, so W1 is a near no-op (10 households, all hours-clip artefacts) and W2's stated object — the non-worker wage location — is **provably inert** (bitwise-unchanged negLL over all 15,814 non-working rows). No estimation run | deputy ruling ss1,3,4 / R-218; MNL `experiments/JMP_PS1/decision_note.md` §22 |
| **Lane B — the ten-household `lhw` audit (R-220 s3)** | **ANSWERED `NO`; FINAL POSITIVE-MODEL SELECTION HALTED** — the chosen node is priced at `hours_model × yivwg × 52/12` (verified 88/88), so the ten clipped households carry earnings wrong by −27% to +67% and disposable income by −24.5% to +13.1%. **3 are intentional support projections** (the 70 h cap); **7 are an unintended inconsistency** (the 10 h floor — the model's hours support reaches 5 h and the frame carries 2,225 sub-10 h alternatives). Smallest correction + one re-estimation proposed, not run | R-220 s3; MNL `experiments/JMP_PS1/decision_note.md` §23 |

### JMP-M08T2 — closed

| Stage | State |
|---|---|
| T2-A — `beta_w_pexp2` profile over its full legal interval | ACCEPTED (R-161), with `PHI_B_SIGN_UNRESOLVED_95_PROFILE` |
| T2-B — randomized QMC, part 1: node construction and gates G1..G9 | ACCEPTED PRE-PRICING (R-168) |
| T2-B — part 2: eight-scramble pricing | **RUN** — 2,549,225 nodes, 5.2123 h EUROMOD |
| Final RQMC precision / final-precision functional stage | **ACCEPTED BANDED (R-175)** — all seven W1 level gates PASS; the `normalized_contributions` family failed on 2 of 6 rows and is disposed of as `MC_BANDED_NORMALIZED_DIAGNOSTIC` |
| Charter §8 independent Tier-2 review (permanent output 4) | RETURNED — `LOC4_PREFERRED_MC_BANDED_LEVELS`; MNL `docs/France_case/P2a/FR_P2a_m08_loc4_tier2_independent_review_v1.md` |

**Two T2-A reporting corrections stand (R-175, review H1):** the convergence
reading is **29 constrained optimizations + 1 accepted unrestricted optimum**,
not 30; and the in-region count is **20 of 30**, not 30. Neither contaminates
the numerical record.

**Sprint boundary.** The M08T2 result is the final numerical record for the
**current LOC4 benchmark**. It is not automatically the final JMP structural
specification if JMP_PS1 selects an S8 successor.

### JMP_PS1 — estimation phase closed at R-183

Exploratory tier (R-172): no mission charter and no independent review for
S1..S7; a spec earns one bounded review only once it clears the agenda §3.2
candidate bar; full welfare and acceptance are reserved for S0 and the selected
S8. Battery part 1 accepted at R-174 with the **F-BOX** and **F-ACTIVE**
findings. PS1-C (fit suite), PS1-E (S0/S8 welfare) and PS1-F (official-data
audit) accepted at **R-179 / R-180 / R-181**. The deputy S8 ruling was adopted at
**R-182**; the lean S8 acceptance run (S8A) returned **NO PROFILE TRIGGER** and
its commissioned bounded independent review returned **`S8_ACCEPTED`** at
**R-183**, closing S8 autonomously under the ruling's §2/§9 branch.

| PS1 leg | State |
|---|---|
| S1..S7 | disposed of by R-182 §8 — S1 invariance-only, S2 not included, S4 rejected, S5 split rejected, S6 **equivocal, not admitted** (parked), S7 rejected |
| S8 = S0 + S3 | **ACCEPTED** — the preferred singles positive specification |
| S8 acceptance run (S8A) | negLL `18022.456443792806` (**pre-correction**; the negLL of record is now `18022.764617170084` on the corrected frame — see §1.1); ΔAIC `−859.1961`; SINGLE-OPTIMUM over 10 polished points (spread `7.64e-10`); exact nesting to 0 ulp with Δ-gradient `−307.387`; PD full-rank clean Hessians (41-free and 39-interior); **W-4 set EMPTY**; **13/13** primary welfare rows pass on a bitwise-identical θ with no re-pricing |
| Bounded independent review | RETURNED — A1–A7 all ACCEPT; verdict **`S8_ACCEPTED`**; four refinements binding as claim language (R-184.1) |

**R-184.1 — binding claim language.** Recorded in full at MNL
`experiments/JMP_PS1/decision_note.md` §11.6. In short: S6 is *"equivocal, not
admitted"* (never "rejected"); S8 welfare **levels** are **conditional on the
inherited hours-normalizer convention** and are not convention-free final
magnitudes, with the MC-banded discipline continuing; `beta_h_f35` is an
*"institutionally motivated 35-hour opportunity peak"* of reduced-form
availability and **never** *"the effect of the 35-hour law"*; and `s_opp` is
*"robust to the S0→S8 change at the achieved RQMC precision"*, **not** statistical
invariance. Also hard: 13/13 numerical-precision passes do **not** validate
structural identification, and this review closes the **singles** positive
specification only. **CR1 convention, stated explicitly:** `K_interior = 39` is
PRIMARY (`c = 1.0257255936675462`); `K_free = 41` (`c = 1.0270805812417436`) is
the recorded alternative, inflating every robust SE by 0.066% and changing zero
significance verdicts. Both constants are in the acceptance manifest.

**T2-B R3 closure chain (settled).** Round-1 Codex review accepted R1, R2 and
R4–R9 and rejected R3 (R-164). One bounded correction cycle followed (R-165);
the round-2 re-review rejected R3 a second time on completeness and the matter
was returned to the deputy (R-166). The deputy E2 ruling authorized one final
exceptional bounded correction scoped to R3F-1..R3F-4 (R-167). The
commissioned fresh Codex read-only review returned R3F-1..R3F-4 all ACCEPT and
OVERALL ACCEPT (R-168), confirming mechanically that the generator is
unchanged, the node frames are byte-unchanged, the t-band remains absent and
there is no extra gate change.

### Couples lane — phases 1–4 complete, nothing promoted

Phases 1–2 built the couples frame (2,275 households) and priced it; phase 3
(R-187) estimated the first parsimonious joint specification C-P3 over the four
participation quadrants; phase 4 (R-188) ran three probes and the combined
candidate C-P4 against a 901-standard synthetic recovery gate, completed to
R=10 replicates at R-189.2 / R-190.2.

| Leg | State |
|---|---|
| C-P3 first parsimonious estimation | ESTIMATED; couples-male leisure PRESENT at `beta_l0_m = 2.84` |
| Probe A — free `beta_ll` | REFUTED — no within-household discrimination gain, destabilizes `beta_l0_m` |
| Probe B — `beta_w_pexp2` box | run, not admitted |
| Probe C — region / urbanisation in `beta_E` | NON-CONVERGENT (distinct optima, 9-coordinate block) — not admitted |
| C-P4 combined candidate, synthetic gate R=10 | **`GATE_FAIL`** — `beta_l0_m`, `beta_occ_2`, `beta_w_educL` |

Reading of record: `beta_l0_m` is **identified but not precisely estimated** —
treat the point estimate as directionally right and the CR1 SE as understated in
the region it lands. `beta_occ_2` is a genuine coverage failure (7/10) with the
same root cause as the largest C-P3 fit misfit: pooling occupation opportunity
across sexes is mis-specified for couples. `beta_l_age_f`, `beta_l_age2_f`,
`beta_occ_4` and `beta_w0` settle as noise; `beta_w_educL` is flagged by the
letter of the rule only. **No couples specification is promoted.** The named
successor missions (occupation sex-split with a mandatory synthetic re-gate; the
quadrant covariance gap; `beta_l0_m` SE calibration; take-up thinness; probe-C
non-convergence) are recorded in the decision note §14.8 — none is opened.

**Re-ordered at R-223 — the three-type design, queued behind SX1.** The couples
lane is no longer the four-participation-quadrant CMF-only frame. Once the R-223
PHASE-1 sample-expansion audit returns, it is implemented as three decision types
in order — **CMF** (both spouses flexible), **CM** (male flexible, female fixed)
and **CF** (female flexible, male fixed) — at approximately 100 sampled joint
household alternatives, with the fixed spouse's observed hours, earnings and
labour-market status repeated in every joint alternative and each joint household
state priced through EUROMOD on the complete roster. One self-employed spouse no
longer excludes a household: it is held fixed and the household is semi-flexible.
Households with three or more adults are **not** in this step — they are
`EXTENDED_HOUSEHOLD_BUDGET_ROBUSTNESS` and stay out of the headline welfare
sample until the pooling, tax-unit, allocation, needs and welfare-unit assumptions
are explicit. `GATE_FAIL` still travels with every existing couples number; none
of the phase 1-4 results is promoted by the re-ordering.

### R1 BMO — CLOSED at R-218 · `R1_BMO_NEGATIVE_RESULT_CLOSED`

**The leg is closed as a negative result.** R-210 lifted the s5c halt: the
restricted-environment result showed `DB040_F == -1` count **`0`** over all
11,459 register households, so the missing-region recode **never fired**, every
household coded `drgn2 = 1` is genuine Île-de-France, and the s5c cell that ten
routes were opened to partition is degenerate in its second component. The
partition s5c demanded was not merely available — there was never anything to
partition. `R1_BMO_OMITTED_PENDING_ACCESS` is therefore **discharged, not
satisfied**: the unblock condition below was met by proving the blocker did not
exist. The estimation then ran on the three authorized arms and returned a clean
negative:

| variant | n | estimate | robust SE | 95% CI | excludes zero | ΔBIC |
|---|---:|---:|---:|---|---|---:|
| (A) FULL_FRACTIONAL | 1555 | +0.037359 | 0.052651 | [−0.06584, +0.14055] | False | +6.794 |
| (B) HIGH_CONFIDENCE_090 | 1555 | −0.021430 | 0.044449 | [−0.10855, +0.06569] | False | +7.117 |
| (C) LEAVE_CORSE_OUT × FULL_FRACTIONAL | 1552 | +0.035042 | 0.052626 | [−0.06810, +0.13819] | False | +6.859 |
| (C) LEAVE_CORSE_OUT × HIGH_CONFIDENCE_090 | 1552 | −0.019980 | 0.044562 | [−0.10732, +0.06736] | False | +7.146 |

Six arms, all SINGLE-OPTIMUM, no W-4 flag, PD curvature including the extended
occupation block. `beta_occ_tension` is indistinguishable from zero everywhere,
costs a degree of freedom under every information criterion, and leaves the
occupation-access block unmoved to within `0.107` SE. The result is **well-powered
on the covariate side**, not a null from thin support: all 22 régions and all 88
grid cells load, 89.9% of alternative rows carry a task group, and the covariate
has sd ≈ 0.82–0.92 within each `loc4` slice. The instrument varied and the model
did not respond. Sign changes around zero are **not** interpreted as mapping
sensitivity.

**The only permitted statement:** *this lagged BMO construction adds no
detectable structural occupation-access signal in the current sample and
specification.* It is **not** claimed that regional occupation demand is
generally irrelevant, and BMO is **not** used as identification evidence in the
headline model. S8 remains preferred, unchanged.

**One prerequisite recorded, deliberately not repaired (R-218 §10).**
`m08_normalisation.py` builds `log_S_occ` as a scalar (`:211`, broadcast at
`:221`). Before any future specification introduces genuinely region-varying or
household-varying occupation access, the occupation normaliser must be made
household-specific and validated. The A/B/P attribution was BLOCKED on exactly
this object — the `log S_occ` dispersion runs 42–88× the component-level
tolerance — and the item closes only because the coefficient it scales is zero.

The pre-R-210 history is retained below as the record of how the leg reached
this point.

---

#### History — the leg as it stood at `R1_BMO_OMITTED_PENDING_ACCESS` (R-198)

The formula was frozen **before** any estimation (decision note §15.1,
`2026-08-30T07:18:03Z`). The crosswalk chain proved to be **four** tables, not
two — no PCS-2003 → ISCO-08 table exists. Deputy s5b returned **Corse
CONSTRUCTIBLE, no halt** (88/88). The directionality audit (s2) found v1 clean on
inversion but **in breach on weighting** on two counts plus a parse gap; all
three are corrected and v1's `W` is withdrawn. With no defensible weighting basis,
66 BMO codes carrying **37.99 %** of recruitment mass are withdrawn under s2's own
fallback: mapped coverage falls to **0.5837** and the HIGH_CONFIDENCE_090
sensitivity runs on **0.3810** of recruitment mass. The correction reverses
nothing on the retained support (90 codes move, none changes its dominant `loc4`),
and the s6 interpretation gate is live, not decorative (`loc4` 2 and 3 correlate
only `0.62` / `0.66` across the two mappings).

Step 0 s5c then **stopped the leg**. The DRD ends with
`replace drgn2 = 1 if drgn2 == .`, so every household with missing `db040` is
delivered as Île-de-France; s5c forbids giving those households the IDF BMO value
and requires the raw flag to be recovered. **All ten enumerated routes fail** —
`db040` is absent from all 18 EUROMOD FR vintages, no `_f` quality flag attaches to
`drgn1`/`drgn2`/`db040`, and the raw EU-SILC household register is not on this
machine. 245 households (**15.76 %**) are unpartitionable. Pre-registered STEP 1 /
STEP 2 are written down and **not run**.

**Unblock condition, and the only one:** EU-SILC `DB040_F` joined on
`DB030 == idorighh`. Until that access exists the leg is **omitted from the
paper** — omitted, **not rejected**; no R1 result may be reported, and the frozen
formula and audited crosswalks stand ready for a resumption that does not need
re-litigating.

*(End of history. The unblock condition above was met at R-210 — and met by
proving the blocker did not exist: the recode never fired, so no join was
needed. The derivation is from a universe aggregate, not a row join
(`DERIVED_FROM_UNIVERSE_AGGREGATE_NOT_A_ROW_JOIN`); the D-file never left the
restricted session and no per-household information was used. See the closure
at the head of this section.)*

---

## 3. Current priorities — verbatim from the PI standing direction

> CURRENT PRIORITIES
> 1. close T2-B and final RQMC;
> 2. run EXP_H35_PEAK_v1;
> 3. update the discussion notebook/report;
> 4. complete the paper outline and main tables;
> 5. only then decide which exploratory result enters the formal
>    accepted specification.

**The live order at R-232 — four items, in this order. This SUPERSEDES the R-224
order below, whose items 1-4 (HP, HO, W3 feasibility, S9 selection) are ALL CLOSED.**

> 1. **Final welfare** — computed for the retained **corrected S8** only; there is
>    no S9 model to compute it for. First test whether the existing common-support
>    priced node cache is independent of the seven corrected chosen rows; reuse the
>    prices if its nodes and budget inputs are hash-identical, and reprice only if
>    job-node wages, hours, household budget inputs or common-support geometry
>    change (R-222 s9). **No automatic reprice.**
> 2. **RUM final rerun** — the headline common-opportunity RUM benchmark is
>    re-estimated **once**, on the same corrected frame corrected S8 uses (R-222 s8).
>    The companion RUM variant is re-estimated only if its nesting/LR comparison
>    stays in the manuscript.
> 3. **Discussion notebook / report update** — the results and discussion surfaces
>    rebound to the corrected-frame anchors and to the S9 verdict.
> 4. **Torch parity export** — at selected-model freeze, from the corrected
>    engine-ready bundle, the retained specification, the `exact_marginal`
>    declarations and the final parameter vector and inference objects, carrying
>    **both proposal conventions**. `TORCH_BACKEND_JMP_READY` is now
>    **`PENDING_PARITY_EXPORT`** — its R-220 s11 condition ("until S9 is accepted or
>    S8 is formally retained") was met at R-232; the export itself is a later card.

**Queued alongside, blocking none of the four.** The generic
`SEMI_FLEXIBLE_MARGINAL_PROPOSAL` capability (R-227 s8) — PKG-03 delivered and
exercised the adapter on real France data at **R-228** (3/3 real smoke tests,
proposal identity passing, MNL gitlink unmoved at `27756a06`), but the **eight-item
gate is NOT discharged** and three conflicts must be settled before any real-data
expanded-couple estimation: the C1 observed-row `prior` convention clash, the C2
fixed-spouse age bound (24.3 % of couple households fail certified gate G-18 on age
alone), and the C4 `MISSING_CHANNEL` spec-schema gap. The corrected A1 composition
counts are **CMF 2,532 / CM 587 / CF 629 / NF 4,362** — **CM is 587, not the
published 585**. Also queued: the **02_framework / 03_data terminology redline** (§7).
**The superseded live order at R-224 — seven items, in this order. Items 1-4 are
now CLOSED: HP at R-226, HO at R-227.2, W3 at R-229 and S9 selection at R-232.
It SUPERSEDED the R-218 order below, whose item 1 (Lane B) is CLOSED.**

> 1. **HP** — the first persistent-preference model: a **random leisure
>    intercept** (R-224). It is estimated on the corrected frame and compared
>    against **corrected** S8 (R-222 s10).
> 2. **HO** — one persistent-opportunity model, run **separately** from HP
>    (R-220 s8), also against corrected S8. HPO stays conditional on an
>    independent identification source and is not estimated from the same choice
>    outcomes alone.
> 3. **W3 feasibility** — authorized at R-220 s6 and runnable in parallel: one
>    parsimonious `beta_l_i = X_i beta_l + sigma_l nu_i` with
>    `corr(nu_i, e_w_i) = rho_wl`, behind gates A–G (R-220 s7). Real-data W3
>    follows HP recovery and uses the corrected frame. If synthetic recovery
>    fails: `W3_NOT_IDENTIFIED_UNDER_CURRENT_DESIGN`, and defer.
> 4. **S9 selection** — S8 versus supported HP, supported HO, W3 if its gates
>    pass, HPO only if separately authorized. The richest model is **not**
>    selected automatically; if no extension earns admission, S8 is formally
>    retained as the final positive model rather than an S9 being invented
>    (R-220 s9).
> 5. **Final welfare** — computed for the **corrected S8** benchmark and the
>    final S9 model only. First test whether the existing common-support priced
>    node cache is independent of the seven corrected chosen rows; reuse the
>    prices if its nodes and budget inputs are hash-identical, and reprice only
>    if S9 changes job-node wages, hours, household budget inputs or
>    common-support geometry (R-222 s9). No automatic reprice.
> 6. **RUM final rerun** — the headline common-opportunity RUM benchmark is
>    re-estimated **once**, at final reporting, on the same corrected frame the
>    final RURO model uses (R-222 s8). The companion RUM variant is re-estimated
>    only if its nesting/LR comparison stays in the manuscript.
> 7. **Torch parity export** — prepared only at selected-model freeze, from the
>    corrected engine-ready bundle, the final selected specification, the
>    `exact_marginal` declarations and the final parameter vector and inference
>    objects. `TORCH_BACKEND_JMP_READY` stays pending until S9 is accepted or S8
>    is formally retained (R-220 s11, R-222 s11, Torch routing note).

**Queued behind SX1 — the couples three-type design (R-223).** The R-223 PHASE-1
sample-expansion audit (SX1) is read-only and may run now; it owns
`experiments/JMP_PS1/sample_expansion_audit.csv` and
`experiments/JMP_PS1/sample_expansion_design.yaml`. **No expanded-sample
estimation begins until SX1 returns**, and the couples lane is then re-ordered to
the three-type design — both-flexible (CMF), male-flexible/female-fixed (CM),
female-flexible/male-fixed (CF) — at approximately 100 sampled joint household
alternatives, with the fixed spouse's observed state repeated in every joint
alternative and each joint state priced through EUROMOD on the complete household
roster. Multi-adult welfare estimation is **not** in that step; it is
`EXTENDED_HOUSEHOLD_BUDGET_ROBUSTNESS`. This queue position is behind items 1–4
above: it is a sample-design extension, not a substitute for the heterogeneity
sequence.

**The superseded live order at R-218 — four items, in this order. This SUPERSEDED
the R-209.2 order below, whose item 1 is DISCHARGED.**

> 1. **Lane B** — the `W0`/`W1`/`W2` wage treatment, with HP/HO following. The
>    wage-robustness lane is now the front of the queue.
> 2. **HP/HO** — the identification comparison, then the HPO gate verdict.
> 3. **S9** — selection and its final numerical evaluation; the common-budget
>    prices are reused if job nodes and pricing inputs are unchanged, or one
>    final aligned S9 reference-budget reprice is performed, with final welfare
>    computed for S8 and S9 only (R-204 §8).
> 4. **Headline freeze** — only after Lane B and S9 are complete. Every share
>    remains `PROVISIONAL_PIPELINE_RESULT_PENDING_WAGE_ROBUSTNESS` and absolute
>    welfare levels remain `ABSOLUTE_WELFARE_LEVELS_NOT_FINAL` until that point.

**One obligation parked at the S9 freeze.** The laptop-parity export obligation
is recorded here BY NAME and deferred to the headline-freeze step; it carries no
on-disk record beyond this line and nothing about it is reconstructed. It is not
owed before S9.

**Discharged: item 1 of the R-209.2 order.** The inversion correction landed at
R-212 (coalition-consistent inversion, ~95% of `I1111` removed) and the residual
it exposed was closed at R-213 (common quadrature support) and R-217/R-218 (the
male-reference structural zero, `I1111` at exact numerical zero in all corrected
arms). The R-209.2 text is retained below unedited as the record of that
sequence.

**The superseded live order at R-209.2 — three items, in this order:**

> 1. **The inversion correction.** *(DISCHARGED at R-218.)* The ex-ante diagnostic ran to R-207's §5
>    failure branch and R-208 named the surviving object: the money-metric
>    inversion's HOUSEHOLD-SPECIFIC FROZEN REFERENCE CORE — the baseline-coalition
>    choice set (`c_norm`, `l_norm`, `working`, `u_baseline`, `opp_baseline`, with
>    the group's `theta_c` / `theta_l`) that `FrozenReferenceCore` holds fixed by
>    contract s5.1 and that no operator in `{P,A,B,D}` equalises, by design. This
>    is **not** a numerical design problem — the anchor, the proposal correction
>    and finite-RQMC variation are each measured ABSENT as drivers, so a common
>    quadrature device would not reach it. R-209 adopts the ruling on that object,
>    and correcting it comes first.
> 2. **Lane B** — the `W0`/`W1`/`W2` and HP/HO work R-204 §8 sequenced in
>    parallel with the D operator and the preference mirror.
> 3. **S9** — after which the common-budget prices are reused if job nodes and
>    pricing inputs are unchanged, or one final aligned S9 reference-budget
>    reprice is performed, with final welfare computed for S8 and S9 only
>    (R-204 §8).

Writing continues alongside — the outline, the main tables and the manuscript.
The inversion correction has landed, so the provisional exhaustive decomposition
may now be written up **under its labels**: every share carries
`PROVISIONAL_PIPELINE_RESULT_PENDING_WAGE_ROBUSTNESS`, absolute welfare levels
carry `ABSOLUTE_WELFARE_LEVELS_NOT_FINAL`, the female/male references are
reported as primary and sensitivity and **never averaged**, and no signed
preference percentage and no A-versus-B ranking is frozen. The one authorized
provisional statement is the D-largest sentence at R-218, with its four
qualifiers.

**Position on the older list at R-198 — the ESTIMATION sprint is COMPLETE.**
Item 1 **DONE** (M08T2 closed at R-175). Item 2 — `EXP_H35_PEAK_v1` — **DONE**:
it was the PS1 S3 leg, the battery's only PROMOTE, and it is now the accepted
S8's one added coordinate. Item 3 — the discussion notebook/report — **DONE**:
refreshed to the S8 state and extended with the sprint second-half sections.
Item 5 is **ANSWERED for singles**: S8, at R-183.

Both sprint second-half legs have run to their stopping points and **neither
produces a promoted specification**: couples reached `GATE_FAIL` at R=10 and R1
BMO stopped at s5c as `R1_BMO_OMITTED_PENDING_ACCESS`. That is a finished
computational programme, not an interrupted one. **No further estimation is
queued.** The writing order set there still stands, alongside the R-209.2 list
above:

> 1. **Complete the paper outline** — `Design/JMP_paper_outline_v1.md`, section
>    by section, against the claim set of record;
> 2. **Main tables** — build the manuscript-facing tables from the accepted
>    records (S8 singles, the LOC4 banded eight, the specification path), each
>    carrying its own status label and band discipline;
> 3. **Manuscript** — write against the completed outline and tables.

Nothing on **that** list needs a new run. What R-199..R-209 added is not
estimation but the welfare-decomposition lane, which is where the live work now
is. Anything else that turns out to need a run is a scientific decision and
returns to the deputy before it is started.

The full standing direction — including the exploratory-work licence, the
four-artifact retention limit per exploratory run, and the `EXP_H35_PEAK_v1`
specification — is recorded verbatim in the consolidated rulings document at
R-168, section *(2) PI Standing Direction — Practical Research Mode*.

**Return to the deputy only for a scientific decision, not routine
documentation or execution mechanics.**

---

## 4. Pointers — authorities of record

| Document | Path | sha256 |
|---|---|---|
| Consolidated rulings document (R-59 … R-233, + the R-212 and R-220 corrective appends, the R-220 s1/s2/s5 follow-up, the R-219..R-224 append, the R-225..R-227 append, the R-228..R-232 append and the R-233 append) | `docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | `2b4c5c45d36b923d3676c1bb84bea922d290db88c51fa57abb401c7ea226c22a` |
| JMP-M08T2 mission charter | `docs/Missions/JMP_M08T2_LOC4_boundary_and_final_precision_charter_v1.md` | `d4de2055ca5db8c6e3d3ea4c945b027ee0a80c0764ba4dc2c99d7d8154968d80` |
| **M08T2 acceptance (charter output 5)** | `docs/Missions/JMP_M08_LOC4_preferred_spec_acceptance_v1.md` | `7a042b75bc535c2e72cd85daebc0521c7a23e44b26013b9c90d09770f87ff8f6` |
| **LOC4 manuscript claim set v2 — OPERATIVE (charter output 6)** | `docs/Missions/JMP_M08_LOC4_manuscript_claim_set_v2.md` | `5a60ffdf3d0beefc006ba284af30009e0a3c99cf41a6f07a4506d7a1917e9ba6` |
| **Independent Tier-2 review (charter output 4)** | `MNL/docs/France_case/P2a/FR_P2a_m08_loc4_tier2_independent_review_v1.md` | `06d2c0fc9cfd62ff1eb220e62cc34f660a739e0d594f079e47ed7307bab4b396` |
| RQMC final-precision results memo | `MNL/docs/France_case/P2a/FR_P2a_m08_loc4_rqmc_final_precision_results_v1.md` | `a456113473cebad748915ad1448134d891023951d05fb1be96ab1f6c914d90f7` |
| LOC4 preferred-spec packet index | `docs/Missions/JMP_M08_LOC4_preferred_spec_packet_index_v1.md` | `8fa35535bf4662d4f417580964de109225f5fff661a430d5316e681ee2d58017` |
| LOC4 manuscript claim set v1 — SUPERSEDED, history only | `docs/Missions/JMP_M08_LOC4_manuscript_claim_set_proposal_v1.md` | `c9051c9df6ff3a0f901aaaeec44de76f93effddd3e68a9c7eecb31d132aea5e4` |
| **Paper outline v1 — the working surface for the writing phase** | `Design/JMP_paper_outline_v1.md` | *not pinned — live working document* |

Paths are relative to the `Job_Market_paper` repository root except where marked
`MNL/`. The rulings-doc hash above is the post-R-209.2 value; it is the value the
live sha gates pin.

**Rulings-doc currency at R-209.2.** The consolidated document now ends at
**R-209**. The R-184..R-209 append carries chat-side lines for the whole span and
five deputy rulings verbatim under their own headings — (1) R-193, (2) R-202
clause s2, (3) R-204, (4a) the R-206 interim marked SUPERSEDED BY (4b), and (4b)
R-207. Its sha256 advanced
`9ff2a1f0…92d4` → `eb4d947b1687bffe69298a5822d8855d6e7dd59b183b3d0f75703eb8cfbf6895`,
and **all five dependent sites in §4.1 were advanced path-only in the commits
that staled them**, with every binding cell's claim strings re-asserted against
the new bytes (7/7 PASS). **One scope fact remains on the record openly:**
R-208 / R-209 carry no deputy-verbatim text on disk and appear as chat-side
lines only.

**Currency advanced at R-212.4 — the R-202 scope defect is CURED.** The dated
corrective append *CORRECTIVE APPEND 2026-09-01 - R-212: the complete R-202
ruling (ten sections)* enters R-202 **in full and verbatim**. It cures two
defects: the R-184..R-209 append had recorded clause s2 only, and its own scope
note read "s1 and s3..s7", undercounting the ruling — R-202 has **ten**
sections, not seven. Nothing above the append was edited. sha256 advanced
`eb4d947b…6895` → `5fdef80a6b1d15fbff2c30f5b923f1a1920d25c74fcb6234f8f1cfb219b2cee0`
(196,859 → 204,744 bytes, prefix byte-identical), with all five dependent sites
advanced path-only in the same commit and all seven claim strings re-asserted
against the new bytes (7/7 PASS). MNL decision note §18 is consequently
**filled** from ruling s7 and no longer stands `AWAITING SOURCE TEXT`. Two
findings are entered openly rather than adjudicated: the complete text's
section 2 is **shorter than and differs in wording from** the s2 block already
at heading (2) — heading (2) remains the location of record for the operational
four-cell text Lane A executed — and section 7 contains **no** Jacquet–Jia–
Thoresen positioning sentence, so that sub-item stays open rather than
reconstructed.

**Currency advanced at R-218.2 — the R-210..R-218 span is on the record.** The
append *Appended 2026-09-02 — R-210..R-218 + three deputy rulings* enters the
nine chat-side lines R-210..R-218 and, under their own headings, the three
deputy rulings of that span that carry verbatim text: (1) the R-210 `DB040_F`
disposition and R1_BMO authorization, (2) the R-213 common-quadrature-support
authorization, and (3) the R-217 male-reference structural-zero completion. Each
was gated on its own first section title before the append was written —
"1. DB040_F DISPOSITION", "1. CONCEPTUAL STATUS",
"1. MISSING MALE CHILD COEFFICIENT". Nothing above the append was edited. sha256
advanced `5fdef80a…2cee0` → `2a2b7ac34c64a415b5286c0e8dfea21f06c18ae07489c68e49812cbca80e7c35`
(204,744 → 240,347 bytes, prefix byte-identical, pure CRLF), with **seven**
dependent sites advanced path-only in the same commit and all seven claim
strings re-asserted against the new bytes (7/7 PASS) **before** the re-pin was
completed. Three scope statements are entered openly: R-211, R-214 and R-215
carry no deputy-verbatim text on disk and appear as chat-side lines only; the
COR-2, R1E and Torch items named at R-214 are recorded BY NAME and are not
reconstructed; and R-212 carries two distinct things under one number — the
chat-side D4 adoption, and clause R-212.4, the corrective append described
immediately above, which is not repeated.

**Chain continued at R-220.** The *CORRECTIVE APPEND 2026-09-02 - R-220 s10: the
wage-premise provenance correction* advanced the same document
`2a2b7ac3…0e7c35` → `92f6013582c520ff9924ad53c7bdec71a0d57d7a6b1804a395c7df6550d64dd2`
(240,347 → 245,753 bytes, prefix byte-identical, pure CRLF), with the **seven**
dependent sites advanced path-only in the same commit and the five rulings-text
claim strings re-asserted against the new bytes (5/5 PASS) **before** the re-pin
was completed. It appends only: no earlier ruling text, including R-202, was
edited. The R-220 s1 / s2 / s5 status labels were not supplied to the executing
agent and are deliberately **not** entered; a follow-up dated correction must
carry them verbatim.

**Chain continued at R-220.2.** The *FOLLOW-UP DATED CORRECTION 2026-09-02 -
R-220 s1 / s2 / s5: the status text* advanced the same document
`92f60135…50d64dd2` → `b8a2664e11bd462456697e1e511564aeeca915fd189bb7c477c61797ca1d7f89`
(245,753 → 249,603 bytes, prefix byte-identical, pure CRLF), with the **seven**
dependent sites advanced path-only in the same commit and the five rulings-text
claim strings re-asserted against the new bytes (5/5 PASS) **before** the re-pin.
It completes the R-220 s10 append by entering the s1 / s2 / s5 text verbatim; the
s10 append's own statement that the text was missing is **not** edited out, and
stands as the record of why the follow-up exists.

**Chain continued at R-224.1.** The append *Appended 2026-09-02 - R-219..R-224 +
three deputy texts + the Torch routing note* advanced the same document
`b8a2664e...ca1d7f89` -> `60744343f6987985e471c3b93644c8ca2af6bd02b84b990c1258535badab2f0f`
(249,603 -> 289,121 bytes, prefix byte-identical, pure CRLF), with the **seven**
dependent sites advanced path-only in the same commit and the seven rulings-text
claim strings re-asserted against the new bytes (7/7 PASS) **before** the re-pin.
It carries the complete R-220 ruling, the R-222 floor-correction ruling, the R-223
sample-audit direction and the Torch routing note; the two earlier R-220 entries
are not edited.

**Chain continued at R-227.1.** The append *Appended 2026-09-02 - R-225..R-227 +
the FC1-closeout deputy ruling* advanced the same document
`60744343...dab2f0f` -> `0f0fd14891b453bd8b9f6b177a94d468d10df6fac0ff859af8a856fd6476571e`
(289,121 -> 315,320 bytes, +26,199 bytes / +521 lines, prefix byte-identical,
pure CRLF), with the **seven** dependent sites advanced path-only in the same
commit and the seven rulings-text claim strings re-asserted against the new bytes
(7/7 PASS) **before** the re-pin. It carries ONE deputy text verbatim — the R-227
FC1-closeout ruling, on the signature gate `1. FC1` — plus chat-side lines for
R-225 (the sample-expansion audit return) and R-226 (the HP return).

**Chain continued at R-232, and the currency line that governs.** The append
*Appended 2026-09-03 - R-228..R-232 + the S9 selection record* advanced the same
document `0f0fd148...6476571e` -> `5135afb038968da93c13a881571a9fb359374c3ebac2ceb558727178de241b5a`
(315,320 -> 331,606 bytes, +16,286 bytes / +204 lines, prefix byte-identical, pure
CRLF, 0 stray LF). **The consolidated document now ends at R-232.** **EIGHT**
dependent sites were advanced path-only in the commits that staled them — not seven;
see §4.1 — and **thirteen** rulings-text claim strings were re-asserted against the
new bytes (13/13 PASS) **before** the re-pin. It carries **no** new deputy-verbatim
text, and that is recorded rather than left to inference: the card directed an
HP/HO-disposition ruling on the signature gate `1. HP AND HO`, no such text was
supplied and none is on disk in either repository, and the three sections the card's
own DEPUTY TEXTS block named — R-204 §1 `1. ADD CHANNEL D`, R-204 §8 `8. SEQUENCING`
and R-220 §9 `9. S9 SELECTION` — are **already** on the record there under their own
headings and are cited by location rather than duplicated. **R-220 §9 is the operative
authority for the S9 verdict.** R-228, R-229 and R-232 are chat-side lines; **R-230
and R-231 are entered by number only and held open** — no text was supplied for either
and neither has an on-disk record, so the numbering is not silently re-used.

**Chain continued at R-233, and the currency line that now governs.** The append
*Appended 2026-09-03 — R-233 + two deputy texts, and R-230 / R-231 FILLED*
advanced the same document
`5135afb0...de241b5a` -> `2b4c5c45d36b923d3676c1bb84bea922d290db88c51fa57abb401c7ea226c22a`
(331,606 -> 365,724 bytes, +34,118 bytes / +940 lines, prefix byte-identical, pure
CRLF, 0 stray LF). **The consolidated document now ends at R-233.** The **EIGHT**
dependent sites were advanced path-only in the same commit and **fourteen**
rulings-text claim strings were re-asserted against the new bytes (14/14 PASS)
**before** the re-pin. It carries **TWO** deputy texts verbatim — the
HP/HO-disposition and PKG-03 C1–C4 conventions ruling on the signature gate
`1. HP AND HO`, and the seminar research-sprint direction on the signature gate
`1. DOCUMENTATION CAP`. **The gap the R-232 append recorded is CURED:** that
append stated as a fact that no `1. HP AND HO` text was supplied and none was on
disk in either repository; the text is now on disk under heading (1) of the R-233
append, on exactly that gate. The earlier statement was true when written and is
**left standing unedited** — this is the dated continuation, not a correction.
**R-230 and R-231 are FILLED and no longer held open**; R-232 is **not** re-entered
and is cross-referenced by location, since duplicating a ruling already carried in
full is what the R-212 corrective append exists to prevent.

### 4.1 The rulings-doc pin recursion

Every append to the rulings document changes its sha256 and therefore stales
the live gates that pin it by hash. Under R-162 the re-pin of each dependent
site lands in the **same commit** as the append that stales it — an append
carries its own re-pins. Under **R-162.2** the sweep covers **both**
repositories, not the MNL executable gates alone. The dependent sites are:

**MNL — live executable gates (3):**

- `scripts/loc4/run_loc4_stage2_comparison.py` — `M6_RULINGS_SHA`
- `notebooks/france/fr_singles_results_discussion_v1.ipynb` — the `bind_evidence`
  pin in the §4(a) Monte-Carlo cell (`instrument_authority`)
- `notebooks/france/fr_singles_results_discussion_v1.ipynb` — the `bind_evidence`
  pin in the §8 welfare cell (`measure_disposition`)

**MNL — documentary citation pins in the PS1 decision note (3):**

- `experiments/JMP_PS1/decision_note.md` — the §11.5 citation pin (the S8R
  review's location of record)
- `experiments/JMP_PS1/decision_note.md` — the §18 citation pin (the complete
  ten-section R-202 ruling's location of record; live since R-212.4)
- `experiments/JMP_PS1/decision_note.md` — the §28 citation pin (the R-227
  FC1-closeout ruling's location of record, on the signature gate `1. FC1`; live
  since R-227.1, **first advanced at R-232** — it was missed by the "seven" count
  and caught by the standing re-grep instruction)
- `experiments/JMP_PS1/decision_note.md` — the **§33** citation pin (the
  R-231 HP/HO-disposition and C1–C4 conventions ruling's location of record, on the
  signature gate `1. HP AND HO`). **Created by the R-233 commit and live from the
  NEXT append** — it was not staled by R-233 itself, so R-233's sweep was correctly
  eight. §§32 and 34 of that note were deliberately left **path-only** so this
  increment is one site and not three

**JMP — documentary pin tables (2):**

- `docs/Missions/JMP_current_state_dashboard_v1.md` — this file's §4 pointer table
- `docs/Missions/JMP_M08_LOC4_preferred_spec_acceptance_v1.md` — the `[rulings]`
  row of its source table (M08T2 charter output 5). Advancing that row is a
  **pin advance only**; the acceptance's findings and verdict are immutable and
  are not edited.

**EIGHT live sites at R-233 — NINE from the next append.** Eight is the count that was re-counted at R-232 and RE-CONFIRMED at R-233 by re-grepping; nine is what the next sweep must find, because the R-233 commit adds the MNL `decision_note.md` §33 pin listed above. **The count is declared forward here precisely so it is not carried one append too long a second time.** The count was **seven** through
R-227.1 and is eight from R-232: the R-227 append added the §28 decision-note pin and
the "seven" figure was carried forward one append too long. That is exactly the failure
this paragraph warns about, so the instruction stands and is now load-bearing: the count
grows as citation pins are added; **check by `grep`-ing the OLD sha across both
repositories rather than working from this list alone.** At R-233 that grep was run
again over both repositories and returned exactly these eight sites and no
ninth, so the count is confirmed rather than assumed for a second append
running.

**Sites that are NEVER advanced.** The §11 chain arrows and the §24 chain sentence
in `MNL/experiments/JMP_PS1/decision_note.md`, and this file's own chain line, are
**historical** — they record which append moved which hash, and a rewritten arrow
would destroy exactly the record it exists to keep. Extend the chain with a new
sentence; never rewrite an arrow. At R-224.1 three such occurrences of
`b8a2664e…ca1d7f89` were left standing deliberately and each was classified
individually before being left.

Re-pinning is **path-only**: the hash is advanced, and each binding cell's
claim strings are re-asserted under its own read of the new file. If a claim
string no longer appears, the append has moved text the gate depends on and
the re-pin must not be completed.

### 4.2 Evidence and code (MNL repository)

| Object | Path |
|---|---|
| T2-B RQMC modules, gates and tests (incl. part-2 rebind / price / stage / evaluate) | `scripts/rqmc/` |
| T2-B Codex review chain (rounds 1–3, incl. the R3-final ACCEPT) | `docs/France_case/P2a/FR_P2a_m08_rqmc_preflight_codex_review_v1.md` |
| T2-B part-2 evaluation record (the numbers R-175 was taken on) | `outputs/p2a_singles2016/region_live_margqh_v1/rqmc_t2b_v1/attempts/20260828T150001Z_…_t2beval_T2B_EVALUATE_PRIMARY_GATE_FAIL/rqmc_t2b_part2_evaluate_v1.json` |
| JMP_PS1 sprint instrument and decision note | `scripts/ps1/`, `experiments/JMP_PS1/decision_note.md` |
| **JMP_PS1 four permanent files (the §9 cap)** | `experiments/JMP_PS1/{specification_matrix.yaml, model_comparison.csv, post_estimation_comparison.html, decision_note.md}` |
| **S8 acceptance run (S8A) — the R-183 evidence** | `experiments/JMP_PS1/runs/ps1s8a_acceptance/` |
| **PS1-C / PS1-E / PS1-F run dirs** | `experiments/JMP_PS1/runs/{ps1c_fit_suite, ps1e_welfare_s8, ps1f_audit}/` |
| **Couples lane p1–p6 — the R-187…R-190.2 evidence** | `experiments/JMP_PS1/runs/ps1h_couples_p1/` (the four `.parquet` frames stay on disk, uncommitted) |
| **R1 BMO — crosswalks, audit, probes, sealed enclave bundle** | `experiments/JMP_PS1/runs/ps1r1_bmo/` incl. `r1bmo_secure_env_bundle_v1.zip` (`65ff967bb1b077bebaec78db9c82abe1180e706891fd112cc085af57b72894d5`); `source/` third-party downloads and the unpacked bundle tree stay on disk, uncommitted |
| **R1 BMO — restricted-data script pack (R-200)** | `experiments/JMP_PS1/runs/ps1r1_bmo/restricted_pack_v1/` — `RUNBOOK.md` plus `inventory.py`, `silc_db040_test.py`, `lfs_hours_table.py`; self-contained, no internet, group floor 10, linkability INSPECTED not assumed (R-202.3) |
| **EU-SILC DOCSILC065 (2015) index — the s5c access record** | `Data/documentation/DOCSILC065_2015_index.md` |
| **Agenda item 8 — `q^W` proposal arms and the `g^W` structural test** | `experiments/JMP_PS1/runs/{ps1s16a_qw_proposal, ps1s16b_gw_structural}/` (geometry parquets and console logs stay on disk, uncommitted) |
| **Lane A — the four-cell pipeline and its halt** | `experiments/JMP_PS1/runs/ps1_laneA_fourcell/` |
| **Channel D + the ex-ante diagnostic** | `experiments/JMP_PS1/runs/ps1_channelD/` — capped per leg (D, ex-ante, driver diagnostic). **`channelD_household_profiles_v1.csv` and `channelD_reference_profile_v1.parquet` are household-level and stay on disk, uncommitted**, per R-204 §2's report-as-aggregates requirement; the D̄ price panel and probe scratch likewise |
| **Welfare-decomposition comparison table (R-204 §9)** | `experiments/JMP_PS1/welfare_decomposition_comparison.csv` — cells × models × reference arms, bands, statuses, and the `estimand` column separating sampled-set-conditioned history from the ex-ante convention |
| LOC4 Stage-2 comparison runner (carries `M6_RULINGS_SHA`) | `scripts/loc4/run_loc4_stage2_comparison.py` |
| Parity-path closure record of operative record | `docs/France_case/P2a/FR_P2a_m08_parity_path_closure_v1.md` |
| Results/discussion working notebook | `notebooks/france/fr_singles_results_discussion_v1.ipynb` |

**Package gitlink of record:** `dclaborsupply-monorepo` at `27756a06`. No
package main/gitlink change is licensed by any current status, including the
exploratory licence.

---

## 5. Pre-commit battery

Reproduced before and after every gated commit; read-only, seconds. Run from
`scripts/welfare` with the MNL project venv.

1. Gate self-pin: `m08_u6_pins_v2.open_gate(...)` over the expected pin set
   plus the U6 pin set — **76 pins** (52 + 24).
2. Re-hash every pinned key via `base_path` / `verified_path`.
3. `parity_axis_evidence("5b0e3d29e28126e1b3ee0340a243c09755da0b3b")`.
4. Assert the `dclaborsupply-monorepo` gitlink is still `27756a06`.

**R-179.1 — the battery is run in FULL, always.** All four steps and all 76 pins,
before **and** after every gated commit. **No scoped subset is licensed** by any
status, exploratory tier included; a scoped run is not a battery run.

**Commit trap.** Committing a *modification* to a file that did not exist at the
frozen axis still reads as `A` in the `frozen..HEAD` tree diff, so it is safe.
Check with `git cat-file -e 5b0e3d29…:<path>` before any commit that touches a
file that might predate the axis.

**DISCHARGED at R-227 s10 — the dated, one-time parity carve-out. The battery now passes 4/4.**
`parity_axis_evidence` is additions-only: between the frozen axis and HEAD every
changed path must read as `A`. Three read as `M`, and from `fc63661` that halted
step 3. The deputy has now authorized a **dated, one-time carve-out for exactly
those three paths and no others**. This is the record it requires.

| # | path | sha256 **before** (frozen axis) | sha256 **after** (HEAD) | change |
|---|---|---|---|---|
| 1 | `docs/France_case/About_data/feedback_bpool_chosen_row_is_reconstructed.md` | `c58b3cf1…cb425` | `309d4d79…b474bc` | +14 / −2 lines, **prose only** |
| 2 | `docs/France_case/About_data/reference_drd_fr_input_variables.md` | `94845ca3…86a4c9` | `9a1c7def…7a83c2` | +6 / −1 lines, **prose only** |
| 3 | `scripts/welfare/m08_p2a_parity.py` | `441b416d…81046` | `7bb2821e…f65b4ae7` | +13 / −2 lines, **one optional parameter** |

Full 64-hex values are recorded in `R227_PARITY_CARVEOUT` in
`MNL/scripts/welfare/m08_u6_rebind.py` and in MNL `decision_note.md` §28.1.

**Paths 1 and 2 are prose only.** Both are documentation files with no executable
content and no code path, changed by MNL `fdf6a92` under the R-220 s10-ordered
wage-premise sweep of the live surfaces. The diffs are the corrected `yivwg`
provenance text and the ten-household `lhw`-clip caveat, each carrying its own
dated correction marker. No number, threshold, tolerance, comparator or default
anywhere in the pipeline is touched by either.

**Path 3 is limited to `cell_hook`, default `None`.** The complete diff against
the frozen axis is: `Callable` added to a `typing` import; one optional keyword
argument `cell_hook: Optional[Callable[[int, Dict[str, Any]], None]] = None` on
`reconstruct_pipeline`; seven docstring lines; and, inside the existing cell loop,
`if cell_hook is not None: cell_hook(idx, ns)`. Nothing else — **no reconstruction,
pricing, comparator, tolerance or default-semantics change**. With `cell_hook`
unset the function executes exactly the statements it executed at the frozen axis,
in the same order.

**The control-leg evidence, at production scale.** The R-222 STEP-1 control leg
re-derived the frozen geometry *through the modified function* with no hook:
`max_abs_diff_overall = 0.0`, and `0.0` on each of the eight compared columns
individually (`hours`, `wage`, `working`, `loc4`, `log_prior`, `is_chosen`,
`idhh_true`, `idperson_true`), over **157,055 rows / 1,555 households**,
`matches_frozen_geometry: true`. Recorded at
`MNL/experiments/JMP_PS1/runs/ps1r222_floor5/ps1r222_s1_manifest_v1.json`
→ `control_authentication`.

**The gate config carries the carve-out list and its authority, and nothing else.**
`MNL/scripts/welfare/m08_u6_rebind.py` gains `R227_PARITY_CARVEOUT` (the three
paths with both endpoint hashes, kind, introducing commit and evidence),
`R227_PARITY_CARVEOUT_AUTHORITY`, `R227_PARITY_CARVEOUT_DATE = "2026-09-02"` and
the resolver `_resolve_r227_carveout`. Three properties matter:

1. **The additions-only criterion is UNCHANGED.** As with `HK01_R100_RENAME_ALIASES`
   (R-148.1), this does not widen the criterion to admit modifications generally.
   It discharges three *named* modifications *on evidence*; every other `M`, `D`
   or `R` row still halts.
2. **Both endpoints are re-hashed on every call** — `sha256_before` against the
   bytes at the frozen axis, `sha256_after` against the bytes at HEAD.
3. **The `after` pin is what makes it one-time.** A *further* edit to any of these
   three paths changes the HEAD bytes, fails the check and halts the axis again.
   That is "no further path enters the carve-out" read forward in time as well as
   sideways: no fourth path may join, and these three may not move again without a
   new deputy authority.

**Battery of record at R-232 — MNL `ddd4981`, ALL PASS 4/4.** Run before and after the
S9-selection commit, in full, all four steps and all 76 pins. Step 1 gate self-pin OK;
step 2 `open_gate` 52 + 24 = 76 OK; step 3 76/76 pins re-hashed (`base_path` for the 52
governing keys, `verified_path` for the 24 U6 keys); step 4 `parity_axis_evidence`
`materially_intact = True` over **707** changed paths — **700 additions**, **4** HK-01
renames resolved by the R-148.1 alias table and **3** by the R-227 s10 carve-out with
`both_endpoints_match` on each, and **0** paths modified, deleted or renamed outside
those; step 5 gitlink still `27756a06`. The four files the S9 commit touches all
post-date the frozen axis, so each reads `A` and none approaches the carve-out; the
three carve-out paths were not touched and their `after` pins are unmoved.

**Result.** Battery step 3 now returns `materially_intact = True` — 536 changed
paths, of which **529 additions**, **4** HK-01 renames resolved by the R-148.1
alias table and **3** resolved by this carve-out with `both_endpoints_match = True`
on each. Steps 1, 2 and 4 pass as before: gate self-pin, 76/76 pins re-hashed,
gitlink still `27756a06`. The halt on the **next U6 / welfare run** is lifted. No
new general parity review is required and none was run. **Do not widen the
criterion to admit modifications generally, and do not detach the axis** — those
remain the wrong answers; this carve-out is the right one, and it is closed.

---

## 6. Next action

**S9 SELECTION IS COMPLETE (R-232) and corrected S8 is FORMALLY RETAINED as the final positive model. The next action is the final welfare on corrected S8.** All three authorized heterogeneity lanes returned NOT IDENTIFIED — HP (R-226), HO (R-227.2) and W3 (R-229) — HPO was never authorized and its gate is unmet, `W0_W1_W2_AXIS_CLOSED` removed the wage-treatment discriminant, and R1_BMO is a closed negative result. Under the deputy's §9 rule that makes the disposition `FORMALLY_RETAIN_CORRECTED_S8_AS_FINAL_POSITIVE_MODEL`: **no S9 extension is invented and no S9 model exists**; "S9" names the selection. LOC4 remains the benchmark for the specification-sensitivity finding. Then the RUM rerun, the notebook/report update and the parity export, in the §3 order. Two lanes run alongside and neither blocks the four: the **generic `SEMI_FLEXIBLE_MARGINAL_PROPOSAL` capability** (R-227 s8; PKG-03 delivered the adapter at R-228 but the eight-item gate is **not** discharged), and the **02_framework / 03_data terminology redline** (§7). MNL `decision_note.md` §31.

**Two things the S9 record states against its own verdict, and they travel with it.** First, **no 901-standard synthetic recovery gate has ever been run on singles S8 itself** — the gate belongs to promotion and S8 was accepted on the real-data protocol of record. What exists is the `sigma = 0` leg of the HP and HO gates and the W3 null control, whose DGP at truth 0 *is* corrected-frame S8 exactly: 38 coordinates interior in all replications, worst |bias| 0.686 SE, **0 departures resolved beyond twice the Monte-Carlo error**, mean coverage 0.958. At R = 10 the MC error of a bias is itself about 0.30 SE, so that evidence is favourable and **weak**, and it is recorded as a limitation rather than as a pass. Second, the access-versus-earning-capacity ordering is **not** stable across the pair — `phi_A > phi_B` under S0, `phi_B > phi_A` under S8 — which is `ACCESS_ABILITY_ORDER_UNRESOLVED_UNDER_S8` (R-182), carried forward **unresolved and unclaimed**. Neither point changes the verdict; both are on the record with it.

**W3 is closed as a negative result (R-229), and it closes a *third* way.** `W3_NOT_IDENTIFIED_UNDER_CURRENT_DESIGN`. HP failed for want of leverage; HO had leverage but no second contrast; **W3 fails at a box endpoint**. `sigma_l` never reaches zero, while `rho_wl` runs to ±0.99 in 6-8 of 10 replications at **every** truth — including the truth where `rho = 0` is correct — because the likelihood is flat along the direction trading `tau = sigma_l·sqrt(1-rho²)` against `rho` at constant `gamma = rho·sigma_l`. Gate D therefore fails on **all three** parameters *including the product*: `gamma` 0/4 truths, `sigma_l` 1/4, `rho_wl` 0/3. "Only the product is recoverable" was **not** the outcome — `gamma` is nearly unbiased (+0.088 / +0.073 at |gamma| = 0.5) and still has **no obtainable interval**, the delta method needing the 2×2 block a box endpoint destroys. The **LR against S8 has no valid null reference**: `rho_wl` is unidentified at `sigma_l = 0` (the objective is bitwise free of it there) and `sigma_l` is on its boundary, so neither χ²₂ nor the 0.5χ²₁+0.5χ²₂ mixture applies; the card asked for the mixture and the answer is that it does not exist. **The binding constraint is named and is shared with HP:** `BC(leisure)` varies by only 0.073 (men) / 0.127 (women) *within* a household's own choice set at the estimated Box-Cox curvature — making the heterogeneity observable bought two orders of magnitude of information and was still short by a factor of two — so **any successor design is to be judged on the within-choice-set spread of whatever it loads on, before it is built**. No real-data W3 estimate exists and the real-data instrument was deliberately never built. Three coherence findings are **RETURNED, not resolved**: on real data `e_w` is the residual at the *chosen* node and therefore an outcome, not a household attribute; the structural wage density there is used both as conditioning variable and as likelihood factor; and the coherent alternative is the full Löffler-style joint in which the whole wage-**offer** distribution shifts with `nu`. Per the deputy's s4 the Löffler German elasticity magnitudes are **not** transferable here and no elasticity is computed. MNL `decision_note.md` §30.

**HP is closed as a negative result (R-226), and it closes a specific way.** `HP_NOT_IDENTIFIED_UNDER_CURRENT_DESIGN`: the random leisure intercept's expected LR against `sigma_l = 0` is **0.0081** at truth 0.5 and **0.1351** at truth 1.0, against the **2.706** the boundary test needs — short *in expectation*, so no draw and no start could change it, while the argmin of `E[negLL(sigma)]` sits exactly at the truth in every case, so the estimator is right and the design is uninformative. Per the ruling's own rule this is a stop: **STEP 3 real data was not run**, no real-data HP estimate exists, and **no `HP_SUPPORTED_CANDIDATE` / `HP_NOT_SUPPORTED` verdict is issued** — that verdict is defined on STEP-3 evidence the gate withholds. It is **not** a finding that preference heterogeneity is absent, only that this parameterisation of it, read off one cross-sectional choice per household at the estimated Box-Cox curvature, carries almost no identifying information. HO is a **separate lane**, untouched by this; `HPO_GATED` is retained; W3 needs a defined persistent preference component and so does not follow from this lane. Under the deputy's §9 rule, if no heterogeneity extension earns admission, **S8 is formally retained** as the final positive model rather than an S9 extension being invented. MNL `decision_note.md` §26.

**The expanded sample is authorized as a CANDIDATE and is not being estimated (R-227 ss2–8).** `SEXP_PRIMARY_A1` — 18–64, τ = 0.20, status-based flexibility, wage screen on flexible deciders only — is accepted **for estimation, not as the final JMP population**; `BENCH_CURRENT_3830` stays the clean benchmark that every expanded result reports against; the 17–65 arm is descriptive only; the 23 singles failing τ are **not** grandfathered and non-nesting is accepted. CMF/CM/CF are authorized with shared couple preference parameters, but **nothing may be estimated on real expanded-couple data until the generic `SEMI_FLEXIBLE_MARGINAL_PROPOSAL` capability passes its eight-item gate**, and the MNL package pin does not move without a separate integration gate. Couples welfare additionally waits on the §9 calibration identity, which is a **hard halt** on cross-type aggregation and has **not yet been evaluated** — there are no type-specific reference bundles on disk to evaluate it against.

**`W0_W1_W2_AXIS_CLOSED`** (R-220 s2). The wage-treatment axis is closed without estimating W1 or W2: `W1_NOT_DISTINCT_FROM_W0` and `W2_VACUOUS_UNDER_PRODUCTION_LIKELIHOOD`. The §22.7 W2-gate halt is **discharged** — it was raised because the W2 object could not be fixed from the ruling text, and s2 resolves it by ruling that there is no W2 to estimate. S8 now carries **`S8_ACCEPTED_POSITIVE_BENCHMARK_NOT_FINAL_JMP_MODEL`** (R-220 s5).

**HO is closed as a negative result (R-227.2), and it closes a *different* way from HP.** `HO_NOT_IDENTIFIED_UNDER_CURRENT_DESIGN`. HP failed for want of leverage — its random leisure intercept loaded on a compressed `BC(leisure; theta_l)` and barely moved a choice. HO has the leverage: its loading is the working indicator, whose mean within-household SD is **0.297** against HP's 0.073 / 0.127, and on HP's own axis diagnostic its expected LR is **1.02** and **13.56** at truths 0.5 and 1.0, two orders of magnitude above HP's. It fails for want of a **second contrast**. Because `eta` shifts every working alternative by the same amount, the within-branch distributions are untouched and `P_i(work|eta) = logistic(A_i − B_i + sigma_o·eta)`: HO is *exactly* a binary mixed logit on the employment margin with **one observation per household**. A normal mixture of logits is close to a logit with a larger scale, so a model without the frailty imitates it by moving `beta_E` and the scale of the employment index — measured, re-minimising the S8 coordinates under `sigma_o = 0` absorbs **94.5–95.2 %** of the axis signal at every truth (`beta_E` −3.334 → −3.791), leaving **profile** expected LRs of **0.0492** and **0.6996** against the **2.706** the boundary test needs. The design first clears 2.706 at `sigma_o = 1.5` — a p90/p10 access-intensity ratio of ~47×, far beyond anything the observed access shifters suggest. In the finite sample the mean `σ̂_o` is **0.762** at truth 0.5 and **0.765** at truth 1.0: the estimator returns the same number whichever truth generated the data. Per the ruling's own rule this is a stop — **STEP 3 real data was not run**, and `run_ho_s3_realdata.py` enforces that in code rather than by memory; no `HO_SUPPORTED_CANDIDATE` / `HO_NOT_SUPPORTED` verdict is issued. It is **not** a finding that opportunity heterogeneity is absent. A panel or repeated choice, an external job-offer/access moment, or a loading that varies *within* the working branch would each change the arithmetic; none is authorised. `sigma_o` is an **opportunity / access-intensity** parameter — not "ability", whose channel is the untouched wage-density block. MNL `decision_note.md` §29.

**The five-hour floor correction is DONE and ACCEPTED (R-222 → R-224).** The R-220 s3 halt is discharged. `hours_floor_low` moved 10 → 5 through the actual construction path — the production notebook's cells re-run under one declared knob change, with a control leg reproducing the frozen geometry at `max_abs_diff = 0.0` — never by patching parquet cells. Every gate PASSED: exactly **7** chosen alternatives changed and all **155,500** drawn alternatives are bitwise unchanged at node level (the 700 remaining drawn-row diffs are the single household-passthrough column `lhw`, fully explained); the **5** raw observations above the 70-hour cap are untouched under `HOURS_CAP_70_SUPPORT_PROJECTION_CONVENTION`; the chosen-earnings identity passes **7/7** at max relative difference `6.1e-08`; the bounded reprice touched 3 of 8 chunks with **0** EUROMOD hard errors, bound 7 rows one-to-one with `yivwg` bitwise preserved, and reproduced every unaffected priced row bitwise against the pinned cache. Disposable income falls in all seven cases, by **21.66–137.09 EUR/month**. Four estimations were run, not two. **No s7 return condition fired; VERDICT: ACCEPT.** The corrected anchors are in §1.1; `HP_HO_W3_REALDATA_HELD` is released onto the corrected frame, and **no** HP, HO or W3 real-data estimation may use the pre-correction frame.

Lane B STEP 0 is complete and is a **negative result for the wage axis as ruled**. The audit (decision note §22) establishes that `yivwg` is the observed hourly wage for every FR_2016 individual who has one — the `Heckman-type` / `18-65, not in education, not self-employed, not pensioners` wording the ruling quotes comes from the **FR_2018+** DRD and from the **synthetic HHoT training** codebook, not from the estimation data. W1 therefore perturbs 10 households (all `lhw`-clip artefacts, ΔnegLL −6.082) and W2's integration object does not exist in the certified architecture. R-220 s2 answered that by ruling there is no W2 to estimate, so the lane needed no unblock. The only non-vacuous version of the object is the ruling-s6 `W3` person-specific wage-residual extension, which is now authorized on its own gates (A–G, R-220 s7) as item 3 of the §3 order — not as a wage-treatment arm.

The estimation sprint is complete and no estimation is queued. The inversion
correction is **discharged**: R-212 made the inversion coalition-consistent,
R-213 put every household on a common quadrature support, and R-217/R-218 closed
the male-reference operator with the structural zero, so exhaustiveness now
passes in all arms and the provisional exhaustive decomposition exists. The live
work is the **persistent-heterogeneity lane** — HP, then HO, then W3 feasibility —
on the corrected frame.
Writing runs alongside: take the outline
`Design/JMP_paper_outline_v1.md` section by section, then the main tables, then
the manuscript — welfare magnitudes may now appear **only under their labels**
(`PROVISIONAL_PIPELINE_RESULT_PENDING_WAGE_ROBUSTNESS`,
`ABSOLUTE_WELFARE_LEVELS_NOT_FINAL`), with the female reference primary and the
male structural-zero reference as sensitivity, never averaged, and with no signed
preference percentage and no A-versus-B ranking frozen.

**What may be reported, and how.** Singles S8 is the preferred positive
specification and carries the R-184.1 claim language verbatim. The LOC4 banded
eight are numerical-integration bands, never confidence intervals. **Couples enter
the paper as first estimates only, labelled provisional** — no couples
specification is promoted and `GATE_FAIL` must travel with any couples number.
**R1 BMO is closed as a negative result** under
`R1_BMO_NEGATIVE_RESULT_CLOSED` / `R1_BMO_NO_ADDITIONAL_OCCUPATION_ACCESS_SIGNAL`
(this supersedes `R1_BMO_OMITTED_PENDING_ACCESS`). The only permitted statement
is that this lagged BMO construction adds no detectable structural
occupation-access signal in the current sample and specification; it is **not**
a claim that regional occupation demand is generally irrelevant, and BMO is
**not** identification evidence in the headline model.

**The D-largest sentence is the one authorized provisional claim** from the
decomposition (R-218 §6), and it travels with its four qualifiers without
exception — structural and model-conditional, not causal, provisional pending
wage robustness and S9, and not a statement that job opportunities are
unimportant.

**Documentation discipline (R-182 §9).** The four-file permanent cap stands:
update only `specification_matrix.yaml`, `model_comparison.csv`,
`post_estimation_comparison.html` and `decision_note.md`. No new charter, profile
memo, regional memo, ordering memo or governance chain. Exploratory runs keep at
most their four-artifact sets.

**Nothing is owed on JMP-M08T2.** It is closed at R-175; no further numerical
instrument is authorized on the LOC4 benchmark. **Nothing is owed to the deputy on
S8** — R-183 closed it autonomously. Return only if a later step rejects S8, a new
W-4/boundary issue appears, or RQMC reuse fails.

**Welfare and the RUM benchmark, after the correction.** Do **not** refresh the
S8 or LOC4 welfare panels now. Every existing S8/LOC4 welfare and decomposition
value carries `PRE_CORRECTION_PROVISIONAL_WELFARE_HISTORY` and
`NOT_VALID_FOR_FINAL_MAGNITUDES` on top of the labels it already carried; the
common-support welfare infrastructure itself is **not** rejected, and the refresh
is `WELFARE_REFRESH_DEFERRED_TO_FINAL_S9`. At final S9, first test whether the
existing common-support priced-node cache is independent of the seven corrected
chosen rows and reuse the prices if it is hash-identical and unaffected. The RUM
benchmark is `RUM_BENCHMARK_STALE_FOR_FINAL_REPORTING_PENDING_CORRECTED_FRAME_UPDATE`
— it is **not** rerun now, and is re-estimated once at final reporting on the
corrected frame.

**No new pricing is licensed beyond the one bounded reprice that has run.**
R-222 s4 authorized exactly one bounded EUROMOD reprice for the seven corrected
chosen alternatives; it ran, and no whole-grid reprice was or is authorized.
R-207 §6 still refuses a second common-node-set EUROMOD run unless the
zero-EUROMOD ex-ante diagnostic demonstrates one is required, and R-208
established that a common realized node set would not reach the surviving object.
R-207 §9's return conditions remain live for anything that changes that.

---

## 7. Standing note — terminology in paper-facing prose (R-227 s12)

**This is a standing drafting rule, not a one-off correction.** It applies to
every paper-facing surface from R-227 forward: the manuscript, the outline, the
abstracts, the positioning memo and any figure or table caption that reaches a
reader. It does not require rewriting historical governance records.

**Avoid unqualified "ability" in paper-facing prose.** Use one of the four
permitted terms instead, chosen for what is actually meant:

| use | for |
|---|---|
| **job access / feasibility** | which jobs are available to the person at all |
| **earning capacity / wage-offer technology** | what the person is paid conditional on the job |
| **preferences** | the consumption–leisure trade-off |
| **endowments / needs** | non-labour income, household composition, the budget side |

**"Ability set `A_i`" is RESERVED.** It denotes the set of jobs a person is
capable or eligible to perform, and nothing else. Do not use it loosely for the
opportunity set, the access density, or the wage distribution.

**Opportunity-set dominance is NOT productivity.** Dominance is a *later
comparison relation* between opportunity sets or distributions. It is not the
definition of earning ability and must not be presented as one.

**The required non-identification sentence, to be carried explicitly wherever the
access density is introduced:**

> The present access density may combine personal capability and market
> availability; it does not yet separately identify `A_i` from `O_i`.

**Flagged for a redline pass, deliberately NOT edited at R-227:**
`manuscript/sections/02_framework.md` and `manuscript/sections/03_data.md`. Both
predate this rule and both are paper-facing. The redline is a separate,
scheduled pass — see the drafting checklist in `Design/JMP_paper_outline_v1.md`,
which carries the same rule at the point of use.
