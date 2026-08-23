# JMP-M08 Welfare Input Handoff v2 (FROZEN)

**From:** Goal 1 Manager — Empirical JMP (closing JMP-M08E)  **Date:** 2026-08-23
**Class:** Frozen input contract for the M08 welfare mission.
**Authority:** Goal-1 **R-110**, over the deputy instruments
`JMP_M08_proposal_density_convention_and_corrected_baseline_ruling_v1.md`
(sha256 `6d9fa09fe999da9069c4cbeef367ffaeb4fb8faca0d7dfcf2c4ef4993daa2a4b`) and
`JMP_M08E_E2_closure_notebook_and_RUM_ruling_v1.md`
(sha256 `23d06aef44ee179f87c90e35ad8eca91a5831e6cbf0e46de82d532e546068b46`), and the deputy final disposition recorded at
**R-109**.
**Target repository path:** `docs/Missions/JMP_M08_welfare_input_handoff_v2.md`
**Status:** FROZEN on commit. Changes require a deputy-approved revision register.

## 0. Supersession note

This document **supersedes** `JMP_M08_welfare_input_handoff_v1.md`
(sha256 `3c7313da331179e9acb1a2ed9fdd591f2c468df30924ff6a73c1b46091763ee9`, dated 2026-08-05) as the input contract for
the welfare mission.

**v1 is immutable.** It is neither edited, retyped, nor withdrawn: it remains the
accurate record of the input contract *as it stood under the joint
component–hours proposal convention*, and it is the citable history for every
M08 Stage-A/Stage-D artifact produced before the convention correction. What
changes is which document *binds*: from this freeze forward, the welfare mission
takes its parameter source, inference objects, S-10 design, disclosure
obligations, and rebinding obligations from **this** document.

Three v1 provisions are **superseded on their face** and are restated in
corrected form below:

| v1 provision | disposition |
| --- | --- |
| §1 parameter row (θ̂ at theta-bytes `c024b893…f0580d`, MNL `520441a6…`) | **SUPERSEDED** — that vector is the *certified historical estimate under the joint component–hours proposal convention*; suspended as a parameter source by R-98. See §1 below. |
| §2.1 S-10 **four**-scenario battery over `beta_l0_sm` + `beta_w_pexp2` | **SUPERSEDED** by the **five**-scenario battery over the corrected W-4 set. See §3 below. |
| §2.5 vigilance item on `beta_l0_sf` (bound not carried in accepted artifacts) | **DISCHARGED** — `beta_l0_sf` is now a *mandatory* S-10 coordinate and its bound record (`lb = 0.05`) is carried in the E4 v2 corrected W-4 artifact. |

v1 provisions **carried forward unchanged**: the LOC4 Path-B ruling (v1 §2.3,
mandatory before final quantitative decomposition claims, downstream of this
baseline per the convention ruling §7); the Tier-2 trigger (v1 §2.2); W-4
visibility in every welfare and decomposition output (v1 §2.4); and the scope
restriction to singles P2a with no estimation, no couples, no pooled years
(v1 §2.6). The prohibition on sourcing any welfare number from management
memos (v1 §1, R-57/A-5) also stands.

## 1. PARAMETER SOURCE

The single permissible parameter source for M08 welfare, decomposition, S-10 and
LOC4 is:

> **θ̂_margqh-v2** — the paper-facing estimate under the job-space marginal/MIS
> proposal convention used consistently in estimation and welfare integration.

| item | value |
| --- | --- |
| Specification identifier | `p2a_singles2016_region_live_margqh_v1` |
| theta-bytes sha256 | `2cf320c3aa4bd42424929f3092088abccf0a2240ba2eb1be0ad7fc068ba51971` |
| Objective at θ̂ (negLL) | `18499.489277699933` |
| Sample | France 2016 single-adult households, **N = 1,555**; 101 nodes per household |
| Parameters | 47 named — **35 interior**, 2 active at upper bound, 10 pinned |

### 1.1 Artifacts of record

**E3 v2 — final estimation attempt** (verdict `E3-CONVERGED-SINGLE-OPTIMUM`):

`outputs/p2a_singles2016/region_live_margqh_v1/e3_estimation_v2/attempts/`
`20260819T214600Z_672360_410223ff1ccd4d12b85d48b36d60fb1e_margqh_v2_phase3equiv_tightened_E3_CONVERGED_SINGLE_OPTIMUM/`

| member | sha256 |
| --- | --- |
| `e3_manifest.json` (self-excluded) | `5e03b3a8a4d77b723d9616b7adda6caa1b5a6b6355bee3740f4b6daa4821a263` |
| `theta_estimated_margqh_v2.csv` | `fddb49984c03313f150bdfa6761efcab600b3cfd5e910d1d9e520b4d9fcd7c38` |
| `convergence_records.json` | `9cf81c03e3e7e0ec58d87582f9454d5b076b53bccfe8d3154188878db926b50e` |
| `e3_console.log` | `a2dddab439da75ceca813627ff9d33fb54bc75eba923af0f11236962438be2f5` |

**E4 v2 — final curvature/inference attempt** (verdict `E4-PASS`, 14/14 gating
gates including T-12S and T-23S):

`outputs/p2a_singles2016/region_live_margqh_v1/e4_curvature_inference_v2/attempts/`
`20260819T214723Z_763848_8304bf6f33d94beba38b05a498049d01_margqh_v2_p4p5equiv_E4_PASS/`

| member | sha256 |
| --- | --- |
| `e4_manifest.json` (self-excluded; 31 members, 30 hashed) | `ffbc759ffb9199d288b1d8e3c221a9a3589fa8abed0096e85ab6573ace861303` |
| `e4_parameter_table.csv` | `21a05fb569da1d776fa166549f847ef5115a5a1d47f373f8edcdaa7d641d78c3` |
| `e4_standard_errors.csv` | `ec7d42d062cee9ad33f81d34153fa138a4e67db37978eff297f90a779f32fe5b` |
| `e4_s10_coordinates.csv` | `5bbdf73f65401c0a1791d6e909629693438b5e9cee0097ac971126adaad94b08` |
| `e4_w4_leisure_block.csv` | `a8a5b4281388f9877bdd40c70c62bf87f1790a2465c6b5d1b06952ff84c9bd00` |
| `e4_regional_tests.csv` | `dddf2154c7b4d9fb0a54d2975ad9961f89ef847cf941a6133b740a957cdbd26f` |

**E2 closure — R1 probe attempt** (`R1_PROBES_PASS`):

`outputs/p2a_singles2016/region_live_margqh_v1/e2_closure_r1_v1/attempts/`
`20260823T152543Z_180012_69c59793f2284da6ae0daa2a42682fef_r1probes_R1_PROBES_PASS/`
— `r1_probes_manifest.json` `694ebf9047d9b5cd915efb9313c6bbf149450018980978d3c331c519ff314a17`;
`r1_probe_evidence.json` `b49518e4eb61765e7c8c0d2f97c67f6957fc52a096a87c72642d69b1813010d5`.

### 1.2 Successor input pins (fail-closed)

Every consumer re-hashes these **before** opening them. A mismatch is a halt,
not a warning.

| role | repo-relative path | sha256 |
| --- | --- | --- |
| stem parquet | `outputs/p2a_singles2016/region_live_margqh_v1/successor_v2/fr_p2a_singles2016_regionlive_margqh_v1__singles.parquet` | `4cc6a223c184ed78e6b78bf330f6559e295c520c207078bd9e312d3eec71dced` |
| stem meta | `…/successor_v2/fr_p2a_singles2016_regionlive_margqh_v1__mnlmeta.json` | `83b5af3fa073d9535c30b104ceb2ad8aa453b6d79fdfba6ffc88f6e48b2b26ba` |
| draws geometry | `…/successor_v2/inputs/fr_p2a_draws_geometry_margqh_v1__singles.parquet` | `3a0408d6e1083f252a33b47956f144bb4ff0562330a79e87147652e904bb7da6` |
| geometry meta | `…/successor_v2/inputs/fr_p2a_draws_geometry_margqh_v1__meta.json` | `887e4926fce33b6830d20aee235f61feddf3af74bce0850af3bdb830c7111bcc` |

Pin gate and runners of record:
`scripts/m08e/m08e_pins.py` `bcf0598d96058b005a72fba4fbc8458ed447ea6c96898afec986f627fc3b3a16` (52 registered keys; `resolve()`
removed with `RouteRemoved`; per-call re-hash; gate-state enforcement);
`scripts/m08e/m08e_e3_reestimate_v2.py` `4c0a5344c820308d79d79d6098cade7442db6fcbf6cb44e4414182b7c3ee75c4`;
`scripts/m08e/m08e_e4_curvature_inference_v2.py` `c315aabbea9ed0d9a218ff720c7b6567eaaa2d703a36658835126318fa06efaa`.

The successor input differs from the accepted P2a frame **only** in the audited
proposal fields — `log_q_H`, `log_prior`, `prior` — as E0 required; household
sample, alternative draws, chosen indicators, wages, hours, occupation, all
covariates and priced consumption are bitwise identical to the accepted frame.

### 1.3 The suspended joint-convention estimate

The accepted P2a estimate (theta-bytes `c024b893…f0580d`, Phase-3/4/5 artifacts
at MNL `520441a6…`) is **certified historical evidence only**.

It is:

- **retained** and immutable, and correctly described as *the certified
  historical estimate under the joint component–hours proposal convention*;
- **never** a parameter source for any welfare, decomposition, S-10 or LOC4
  quantity — not as a baseline, not as a robustness arm, not as a warm start for
  a paper-facing number, and not in combination with any marginal-convention
  welfare integration;
- **never** described as a software failure, unreproducible, or retrospectively
  discredited. It is internally reproducible for the augmented labeled draw
  space it implemented. The difference is an **estimand-consistency correction**,
  not a robustness exercise.

Mixing the two — old θ̂ with marginal-convention welfare integration — is the
exact defect the convention ruling forbids and is a halt condition.

## 2. INFERENCE

| item | value |
| --- | --- |
| Estimator | household-cluster **CR1** |
| Clusters | **G = N = 1,555** (one independent likelihood contribution per household, notwithstanding 101 rows per household in the sampled denominator) |
| Finite-sample factor | c = (G/(G−1))·((N−1)/(N−K)) = **1555/1520 = 1.0230263157894737** |
| Covariance dimension | **35 × 35 — conditional active-set inference** |
| Curvature at θ̂ | free-37 min eig `0.089577`, rank 37/37, condition `473,932` (clean tier); interior-35 min eig `0.124326`, rank 35, Cholesky succeeds |
| Score identity | `2.416e-13`; `V_robust` min eig `2.151e-05`; T-19 max ratio `1.290e-05` |

### 2.1 Active bounds and literal NA

`beta_l_age2_sm` and `beta_l_age2_sf` are **active at their upper bound +1.0**
with positive KKT multipliers (`0.9015740632508` and `1.3569149522637312`).
Standard symmetric Wald inference is non-regular there. Their standard errors,
z-statistics and p-values are reported as **literal NA** — never as a numeral,
never blank, never zero, and never imputed downstream. They are excluded from the
35-dimensional covariance by construction.

Neither coordinate may be described as "precisely estimated at one",
"significantly equal to one", or statistically different from nearby admissible
values.

### 2.2 Corrected W-4 set

The corrected W-4 warning (non-gating) flags exactly:

**{ `beta_l0_sm`, `beta_l0_sf`, `beta_l_nkids_sf` }**

`beta_w_pexp2` is **no longer flagged**; `beta_l0_sf` and `beta_l_nkids_sf` are
**newly flagged**. The W-4 membership is identical in E4 v1 and E4 v2. The W-4
"picture persists" flag is **false**: the corrected set is not the certified
historical set, and the historical two-coordinate set is not carried forward.

Corrected W-4 detail (from `e4_manifest.json` → `step3_w4.corrected_detail`):

| coordinate | θ̂ | robust SE | CI lo | CI hi | lb | ub |
| --- | --- | --- | --- | --- | --- | --- |
| `beta_l0_sm` | `4.873263586119733` | `2.5736489013490713` | `-0.17099556937552585` | `9.917522741614992` | `0.05` | `50.0` |
| `beta_l0_sf` | `8.269656713002707` | `4.212811396108413` | `0.012698102970313485` | `16.526615323035102` | `0.05` | `50.0` |
| `beta_l_nkids_sf` | `1.9630314196977938` | `1.6521765774561448` | `-1.2751751682169008` | `5.2012380076124884` | `-5.0` | `5.0` |

The **relevant boundary direction** for all three — and specifically for
`beta_l0_sf`, whose robust CI lower endpoint `0.012698102970313485` lies *below*
its recorded lower bound `0.05` — is the **LOWER** bound. §3 perturbs downward
accordingly.

### 2.3 Named access battery at θ̂ (evidence, not licence)

| null | q | W_robust | p_robust | tier |
| --- | ---: | --- | --- | --- |
| H0-A (joint regional access) | 10 | `38.768687151452788` | `2.7868585048712358e-05` | confirmatory |
| H0-B (drgn2…drgn8) | 7 | `5.5840362491942734` | `0.58906781338296366` | secondary |
| H0-C (drgur, drgmd) | 2 | `0.28431386865496761` | `0.86748510761101227` | secondary |
| H0-G (`beta_E_gsur`) | 1 | `30.705162291371472` | `3.0036487479710722e-08` | secondary |

Reporting is bound by disclosure 6 (§4) and by the A4 prohibited-claims list
(§5): H0-B/H0-C are **strict non-rejections**, never equality claims; H0-A is not
a causal regional effect.

## 3. S-10 — FIVE Tier-1 scenarios (SUPERSEDES contract v5's four-scenario sections)

**Supersession.** `JMP_M08_singles_welfare_execution_contract_v5.md`
(sha256 `c7b0338f71af2fb31c4ce20e99691713e53a8e4bd1e31d01c493432799f15005`) and
`JMP_M07_S10_tier1_welfare_sensitivity_specification_v1.md`
(sha256 `acbf163740b8ae97ed59bf2734fc029f1fb42b1d7e88bf7f05a46d78675b19db`) specify a **four**-scenario Tier-1 battery over
`beta_l0_sm` and `beta_w_pexp2`, derived from the now-suspended baseline. Every
such section is **superseded** by this §3, on the authority of the deputy
E2-closure ruling **§4** ("CORRECTED S-10 SET … Run exactly five Tier-1 scenarios
later … `beta_w_pexp2` is removed from the mandatory corrected-baseline S-10
set") and the deputy final disposition adopted at **R-109**. The contract's
*mechanics* — the admissible perturbation rule, the pre-execution recording
requirement, the materiality thresholds, and the convergence/invariance
diagnostics — survive unchanged; only the coordinate set, the scenario count and
the numerical vectors change.

The two-coordinate S-10 table in
`FR_P2a_m08e_E4_curvature_inference_note_v2.md` is an **intermediate historical
construction** and must not be used as the manuscript-facing S-10 design.

### 3.1 Admissible perturbation rule (unchanged, D15)

    Δ_j       = min{ 0.5 · SE_robust_j ,  0.5 · (θ̂_j − lb_j) }
    θ^sens_j  = θ̂_j − Δ_j

Derived mechanically from the E4 v2 attempt's `e4_s10_coordinates.csv`
(sha256 `5bbdf73f65401c0a1791d6e909629693438b5e9cee0097ac971126adaad94b08`) and, for the two coordinates that file does not
carry, from the same attempt's `e4_parameter_table.csv`
(sha256 `21a05fb569da1d776fa166549f847ef5115a5a1d47f373f8edcdaa7d641d78c3`) and the corrected W-4 bound record in
`e4_manifest.json` (sha256 `ffbc759ffb9199d288b1d8e3c221a9a3589fa8abed0096e85ab6573ace861303`). No re-estimation, no
optimisation, no new draw.

| coordinate | θ̂_j | SE_rob_j | lb_j | 0.5·SE | 0.5·dist | **Δ_j** | binding arm | **θ^sens_j** | θ^sens − lb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `beta_l0_sm` | `4.873263586119733` | `2.5736489013490713` | `0.05` | `1.2868244506745357` | `2.4116317930598665` | `1.2868244506745357` | half-SE | `3.586439135445197` | `3.5364391354451974` |
| `beta_l0_sf` | `8.269656713002707` | `4.212811396108413` | `0.05` | `2.1064056980542065` | `4.109828356501353` | `2.1064056980542065` | half-SE | `6.1632510149485` | `6.1132510149485` |
| `beta_l_nkids_sf` | `1.9630314196977938` | `1.6521765774561448` | `-5.0` | `0.8260882887280724` | `3.481515709848897` | `0.8260882887280724` | half-SE | `1.1369431309697213` | `6.136943130969721` |

All three bind on the **half-SE** arm; all three perturb toward the **LOWER**
bound; all three land **strictly inside** the admissible box. Each moves exactly
0.5 robust SE. Values are shortest-round-trip IEEE-754 double literals: parse
them as `float`, do not re-round.

### 3.2 The five scenario vectors (FROZEN)

In every scenario, **all 44 non-S-10 coordinates equal the baseline θ̂_margqh-v2
bitwise** — including the two bound-active coordinates
`beta_l_age2_sm = beta_l_age2_sf = 1.0` and the 10 pins. Only the cells shown
below differ from baseline. This table **is** the frozen scenario set; it is
recorded here, before execution, as the contract requires.

| # | scenario | `beta_l0_sm` | `beta_l0_sf` | `beta_l_nkids_sf` | all other 44 |
| --- | --- | --- | --- | --- | --- |
| **1** | corrected baseline | `4.873263586119733` | `8.269656713002707` | `1.9630314196977938` | θ̂ |
| **2** | `beta_l0_sm` alone | **`3.586439135445197`** | `8.269656713002707` | `1.9630314196977938` | θ̂ |
| **3** | `beta_l0_sf` alone | `4.873263586119733` | **`6.1632510149485`** | `1.9630314196977938` | θ̂ |
| **4** | `beta_l_nkids_sf` alone | `4.873263586119733` | `8.269656713002707` | **`1.1369431309697213`** | θ̂ |
| **5** | all three jointly | **`3.586439135445197`** | **`6.1632510149485`** | **`1.1369431309697213`** | θ̂ |

Scenario 5 is **not** the sum of scenarios 2–4: it is run jointly precisely to
capture the nonlinear interaction of the three weak leisure directions.

Every headline welfare level, welfare-inequality index and decomposition share
is reported under all five scenarios with the contract's convergence and
invariance diagnostics. Per disclosure 5 and the A4 list, this battery is a
**Tier-1 deterministic sensitivity battery** — not a confidence region, not a
bootstrap, not a posterior, not comprehensive parameter-uncertainty propagation,
and in particular it does not resolve uncertainty in the two exactly
active-bound age-squared terms.

## 4. THE EIGHT REQUIRED DISCLOSURES (binding reporting obligations)

Transcribed **verbatim** from `FR_P2a_m08e_econometric_review_v1.md`
(sha256 `bde266437e28f8811f39aaba0b25a6407025f25af5b6fa797fe903c23e6c5546`), overall verdict
**ACCEPT-WITH-REQUIRED-DISCLOSURES**, adopted as binding at Goal-1 **R-110**.
Each is a reporting obligation on every manuscript, notebook, table, figure and
memo that carries a number derived from θ̂_margqh-v2.

1. **Convention and historical comparison.** The old vector must be called the **certified historical estimate under the joint component–hours proposal convention**. The corrected vector must be called the **paper-facing estimate under the job-space marginal/MIS proposal convention used consistently in estimation and welfare integration**. The change is an estimand-consistency correction, not a conventional robustness exercise and not retrospective evidence that the historical computation was unreproducible. 

2. **Proposal density is not an economic opportunity variable.** The manuscript must distinguish the numerical proposal density (q_H) from the structural opportunity/access objects. The correction integrates out a sampling label; it does not itself represent an improvement or deterioration in workers’ actual job opportunities.

3. **Finite-(R) approximation.** With (R=100), the estimator retains finite sampled-choice-set approximation error of order (1/R). The recovery exercise supports small, economically moderate bias on the realized design; it does not establish exact finite-(R) unbiasedness.

4. **Recovery scope.** The synthetic evidence validates recovery conditional on the actual 1,555 household-specific sampled sets, covariates, prices, pins and bounds. It is not a proof of nonparametric identification, external validity, correct specification of the complete job-offer process, or robustness to regenerating the proposal draws.

5. **Leisure-block and boundary disclosure.** `beta_l_age2_sm` and `beta_l_age2_sf` are active at their upper bounds and have no regular Wald inference. `beta_l0_sm`, `beta_l0_sf`, and `beta_l_nkids_sf` form the mandatory corrected W-4/S-10 set. Welfare conclusions must report the five prescribed scenarios and must not characterize that exercise as comprehensive parameter-uncertainty propagation.  

6. **Access-result wording.** The defensible statement is that the corrected joint access battery rejects, with the evidence concentrated in the coefficient retaining the name `GSUR`. This is one modeled access channel, conditional on the maintained structural specification. It is neither a causal regional effect nor evidence that all opportunity inequality is regional. H0-B/H0-C non-rejections, where reported, must remain strict non-rejections rather than equality claims.

7. **Inference scope.** Standard errors are household-cluster CR1 and conditional on the realized active set and maintained inputs. They do not automatically cover spatial dependence, survey-design uncertainty, generated-input uncertainty, proposal-draw uncertainty, or uncertainty from the subsequent welfare and decomposition algorithms.

8. **Downstream status and population scope.** The baseline concerns France 2016 single-adult households, (N=1555). Acceptance of (\widehat\theta_{\text{margqh-v2}}) does not itself accept any W1–W6 level, inequality index, RUM–RURO comparison, or access/ability/preference decomposition. Those results become manuscript-facing only after rebinding, normalization checks, S-10, LOC4, and their own accepted welfare/decomposition gates.

## 5. STANDING PROHIBITED-CLAIMS CONSTRAINT (review §A4)

Transcribed **verbatim** from the same review. This is a *standing* constraint:
it binds continuously, is not discharged by any single disclosure, and applies to
draft text as well as final text.

Inferential claims that must not be made from this baseline include:

* that CR1 accounts for cross-household regional or spatial dependence;
* that it incorporates tax-benefit pricing, wage-imputation, proposal-draw, or other generated-input uncertainty;
* that non-rejection of H0-B or H0-C establishes equality or absence of those channels;
* that H0-A identifies a causal effect of region on job access;
* that old-versus-corrected coefficient changes are statistically significant differences—the two vectors estimate different likelihood estimands, and no covariance for their difference has been constructed;
* that S-10 produces welfare confidence intervals.

## 6. WELFARE REBINDING OBLIGATIONS

Acceptance of θ̂_margqh-v2 is acceptance of a **parameter source only**. Nothing
downstream is accepted in advance. Before any pricing, any welfare number, or any
decomposition share:

1. **Full rebinding.** Every q^W object, the normalisation Z, the ĝ sampler, and
   every decomposition coalition target **rebinds to the corrected θ̂**. No
   object, cache, checkpoint or intermediate carrying the suspended θ̂ survives
   into a paper-facing computation. Held q^W code and tests are retained (per the
   convention ruling §7) but are **not** accepted evidence until rebound and
   rerun.
2. **Pre-EUROMOD batteries rerun.** The deterministic proposal/normalisation
   battery and the N-test battery (N1–N9) are **rerun in full** against the
   rebound objects **before any pricing**. Prior passes were obtained under the
   suspended parameter vector and are void as gates.
3. **RUM benchmark re-estimates its own preferences.** The common-opportunity RUM
   benchmark **re-estimates the preference parameters** under its own frozen
   common-opportunity measure, on the same sample, job-package support, EUROMOD
   disposable-income mapping, corrected marginal/MIS proposal convention, utility
   family, non-employment treatment, and estimation/inference standards.
   Constructing the benchmark by **setting g = 1 while retaining the RURO θ̂ is
   forbidden**. The earlier W1/W4/W6 Ginis are superseded RURO-pipeline
   development results and are **not** a RUM benchmark.
4. **U6 resumes on the held frozen design.** U6 resumes per the design frozen at
   R-91/R-92 as amended by R-94/R-95/R-96 — node-level mixture λ = 0.25;
   ĝ = g̃/Z_i^S with analytic Z over the full mixed support; deterministic
   t ≡ 0 (mod 4) allocation with balance-heuristic MIS; atom
   Rao-Blackwellisation; O-8 stratified direct estimator active on its trigger;
   the exact D1 mixture marginal on the welfare-side q_H. The design is **not**
   reopened; it is rebound and rerun.
5. **Order of gates.** Rebinding → deterministic + N-test batteries → U6 →
   pricing ladder → welfare → decomposition → S-10 (five scenarios) → LOC4. LOC4
   remains mandatory before any final quantitative decomposition claim and is
   **never** run against the suspended estimate.
6. **Scope unchanged.** Singles P2a only. No couples, no pooled years, no
   estimation of any kind on the welfare axis, and no generic `dclaborsupply`
   change (gitlink frozen at `27756a06`); a required generic package change is a
   deputy escalation.

## 7. Status

**FROZEN on commit.** The M08E chain of record backing this freeze:

| document | sha256 |
| --- | --- |
| `FR_P2a_m08e_E0_estimand_audit_v1.md` | `9d5e7ec99642e1736c5746c12b52e4c2e139baa47af1239182b3f65658ca2ee7` |
| `FR_P2a_m08e_successor_input_and_recovery_note_v1.md` | `5cfd7425cd19934089fa44c0597f810487765ad7c79e332be47e6c69463d89a5` |
| `FR_P2a_m08e_E3_reestimation_note_v2.md` | `970eda4c0d3dcc140b1608159c64fff420eb8395964e2e3b34f500c1a660a5f5` |
| `FR_P2a_m08e_E4_curvature_inference_note_v2.md` | `458565c9d33c88cda3cca6f61a6a6093ae07ac2b9a4bf815fb6dfee1eec76719` |
| `FR_P2a_m08e_codex_review_v1.md` | `332a48076846ab27e64bbaedc939571be7a818a8416cc66d2eca6d06491fb4d1` |
| `FR_P2a_m08e_codex_reverification_v1.md` | `da96496cf94a4ff1b8009c51749e73ddb8a5b97361f9ed89908da5a32543ea2d` |
| `FR_P2a_m08e_final_verification_R1_R5_v1.md` | `15bcfbdecbd6370c792f635653ce1015fcfc8c08ed09912c5de4de68b885723a` |
| `FR_P2a_m08e_econometric_review_v1.md` | `bde266437e28f8811f39aaba0b25a6407025f25af5b6fa797fe903c23e6c5546` |

No welfare number, decomposition number, inequality index, or EUROMOD execution
is produced or implied by this document. It freezes inputs and obligations; it
does not produce results.
