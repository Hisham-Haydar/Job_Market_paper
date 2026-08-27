# JMP-M08 — LOC4 FOUR-DENSITY ROBUSTNESS: DESIGN MEMO v2

**Mission ID:** JMP-M08 · LOC4 (pre-registered first robustness axis)
**Class:** Design memo. **PROPOSED-PENDING-INDEPENDENT-REVIEW.**
**Target repository path:** `docs/Missions/JMP_M08_LOC4_robustness_design_v2.md`
**Date:** 2026-08-26
**Supersedes:** `JMP_M08_LOC4_robustness_design_v1.md` (2026-08-26) **as the binding design**. v1 is **preserved as proposed history**, immutable, neither edited nor withdrawn — it is the accurate record of the design *as it stood before the difference-materiality ruling*, and it is the citable history for the open items that ruling closed.
**Authorising instruments:** deputy **Part B — LOC4 Materiality and MC Precision** (binding, transcribed in §3–§4); Goal-1 **R-144.1**.

**Revision register.** Changes from v1 are confined to: §0 (new); §3 (rebuilt on Part B); §4 (rebuilt on Part B); §6 (new, Path-B reconciliation); §5.2 SA-1; §5.5 (coherence rerun, findings C-3 superseded, C-9…C-13 added); §5.6 (open-item refresh); the header, input table and closing Output Discipline block. **§1, §2 and §5.1/§5.3/§5.4 are carried forward substantially intact**; where a carried section is touched, the amendment is marked inline **[v2 amendment]**. No change was made outside these named locations.

**Authoritative inputs.** All numerals are transcribed from these with citation; nothing is recomputed.

| # | instrument | role here |
|---|---|---|
| I-1 | `JMP_M08_welfare_input_handoff_v2.md` (FROZEN; Goal-1 R-110) | parameter source θ̂_margqh-v2; inference conventions; corrected W-4 set; frozen five-scenario S-10; the eight disclosures; the prohibited-claims list; rebinding obligations and gate order |
| I-2 | `FR_P2a_m08_u6cv1_stageA_binding_and_deputy_return_v1.md` | recorded schema of the 16x welfare stack: `q_W` family and `μ_ik`, `q_H` marginal, the frozen box, `S_i`, `n`, `n_k`, the measure-role table, the A-4 functional table, the `threshold_set_of_record` |
| I-3 | `RURO_model_spec_contract_v2_stijn_enhanced.md` | structural block definitions (§9 `O^W`, §10 `O^Occ`, §15 identification, §16–17 parameters/bounds, §18 exclusion table, §19 `M3` extension ladder) |
| I-4 | M08 prototype closure `M08_BASELINE_PROTOTYPE_LIMITED_MC_PRECISION` | headline set {W1 mean, W1 Gini, φ_A, φ_B} + qualitative sign/order claims; the estimator of record |
| I-5 | deputy CV ruling §s10 | CRN comparison; MC error on LOC4-minus-baseline differences |
| I-6 | **`JMP_LOC4_pathB_ruling_v1.md`** — LOC4 Ruling v1, PATH B (binding before the welfare mission) | **LOCATED. OL-1 CLOSED.** The LOC4 robustness contract (§4) and the quantitative materiality rule (§5). See §6. |
| I-7 | **deputy Part B — LOC4 Materiality and MC Precision** | **the difference-materiality instrument.** Fixed baseline denominators (R-a); direct CRN difference construction; the precision/substantive two-layer system; MATERIAL / IMMATERIAL / INDETERMINATE_MC; the arm-precision rider. **OL-4 CLOSED.** |

**No computation, no code, no new draw, no welfare number, no parameter value, no EUROMOD execution is produced or implied by this memo.**

---

## 0. MEASURE ROLES AND ESTIMATOR OF RECORD

Stated here because Part B requires v2 to carry them explicitly.

### 0.1 Accepted M08 measure roles

Transcribed from I-2 §5.1:

| measure | role | reference `R(w)` construction | shares the 16x node set? | carries `q^W`? |
|---|---|---|---|---|
| **W1** | **PRIMARY** | `logsumexp_{j∈cols}(leisure_j + β_c BC(w) + opp_j) − log S_i` | **yes**, the same `cols` | **yes**, the same `corr` |
| **W3** | validation | `logsumexp_masked_{j∈cols}(u_j(w) + opp_j) − log S_i` | yes, less the O-3 drop mask | yes |
| **W4** | secondary | `leisure_term_home + β_c BC(w)` — **one alternative** | **no** — a single row | no |
| **W5** | diagnostic | `logsumexp_masked(u(w; Abar) + abar.opp) − log abar.n_alts` | **no** — the Abar household's own set | no |
| **W6** | secondary | `logsumexp(lt_univ + β_c BC(w)) − log n_j`, `w6_hours = [0, 20, 30, 35, 39, 48]`, `n_j = 6` | **no** — fixed deterministic grid | **no `opp` term at all** |

**Consequence for LOC4, unchanged from v1:** the headline comparison is a **W1** comparison. W3 is reported as validation. W4/W6 differences are reported banded, with the standing riders of I-2 §5.2 (A4-1: neither admits the CRN library; A4-2: W4's reference `core.home_idx = argmax(working == 0)` is itself a **sampled** node whose identity changes with the sub-basis, so W4 carries Monte-Carlo error of a kind CRN on the attained leg cannot remove).

### 0.2 Estimator of record

**Raw 16x, under `M08_BASELINE_PROTOTYPE_LIMITED_MC_PRECISION`.** Transcribed from I-2 §5.1, §6.1, §6.2:

```
V_actual = log [ (1 / S_i) · Σ_{j ∈ cols} exp( u^S_j + log ĝ^S_j − log q^W_j ) ]
S_i      = 1601 (T16) / 1201 (T12_-b) / 801 (T8_ab)
n = 1600 ladder nodes ;  n_k = 400 per superblock (300 base / 100 defensive) ;  4 superblocks
node 0   = the chosen alternative, deterministically prepended, at the accepted ZERO correction
```

**Inherited, unrepaired, and unchanged in v2:**

- **A5-i.** `_cols_of` prepends node 0 to **every** sub-basis and `compute_measures` divides by `S_i = 1 + n`. The raw estimator of record is therefore `Î_impl = (1/(n+1))[ y_0^det + Σ_{t=1..n} y_t ]`, not `(1/n)Σ y_t`. Repairing this is a change to the raw estimator and is **outside this mission's authority**, exactly as it was outside CV1's (I-2 memo C-7).
- **A5-ii.** The non-employment atom is **sampled** on the IS leg, not Rao-Blackwellised: `498,146 of 2,488,000` ladder rows are non-working, against the design working share `0.75·0.90 + 0.25·0.50 = 0.80`. The Rao-Blackwellised construction exists only on the **direct** estimator (`m08_ghat_samplers.vdir_rao_blackwell`).
- **C-8 dependency, unchanged.** Under CRN the `y_0^det/(n+1)` term is present identically in both arms and cancels in `Δ` **to the extent that node 0 is bitwise identical across arms** — which G-L4-1 verifies, and which is why this inheritance is tolerable here. **If the outstanding CV1 returns are dispositioned in a way that changes the raw estimator, LOC4's comparison must be re-run**, because the object being differenced will have changed.

LOC4 does **not** repair, re-scope, or work around any of the above.

---

## 1. THE VARIANT

*(carried from v1 substantially intact; amendments marked)*

### 1.1 Name and object

**LOC4 four-density robustness** = the `M3` extension of I-3 §19 ("`O^W` conditional on `Occ`: occupation-specific Mincer means, shared σ"), instantiated on the **LOC4 four-category task-group collapse** of I-3 §6 (1 routine-manual, 2 nonroutine-manual, 3 routine-cognitive, 4 nonroutine-cognitive). "Four-density" is literal: the single structural wage-opportunity density becomes **four occupation-conditional wage densities sharing one σ**, one per LOC4 category. **[v2 amendment]** This is the project's already-defined LOC4 four-density variant required by I-6 §4, using the existing LOC4 grouping definition; no alternative grouping is searched (I-6 §4, §7).

### 1.2 The baseline it perturbs, stated exactly

The certified structural wage block of θ̂_margqh-v2 is I-3 §9:

```
log f_W(w | X)  =  − 0.5·z²  − log σ  − log w
z               =  ( log w − μ_i(X) ) / σ
μ_i(X)          =  β_w0 + β_w_educL·educL + β_w_educH·educH
                     + β_w_pexp·pexp + β_w_pexp2·pexp²
```

**`δ_occ` is coordinate-empty in θ̂.** The structural `μ_i(X)` carries **no occupation term**; occupation enters the certified model **only** through `O^Occ` (I-3 §10, §18).

This must not be confused with the *proposal*. I-2 §4 binds, from `scripts/pilot/pilot_wage_draw.py:174-188` via `m08_qw_streams.BaseComponent.factors`, that the **proposal** wage mean is `PW._build_log_wage_mean(educL, educH, pexp, pexp², loc4, year_tag, coef, use_year_controls)` — i.e. `μ_ik` in the proposal **is** occupation-conditional, drawn from the frozen pilot mincer payload, with **σ a single scalar common across occupations**. The asymmetry — occupation shifts where wages are *drawn from*, but not where the estimated model *believes* they are offered — is a property of the accepted baseline. Recorded as coherence finding **C-5** (§5.5); it is the substantive motivation for the axis.

### 1.3 Coordinates added

```
μ_i(X, k)  =  μ_i(X)  +  δ_occ(k)  ,      k ∈ {1,2,3,4} = LOC4 ,
δ_occ(1)   ≡  0                            (reference category FIXED, routine-manual, I-3 §15.2)
σ          unchanged and SHARED across k   (I-3 §19, M3)
```

Free coordinates added: `delta_occ_2`, `delta_occ_3`, `delta_occ_4`. The vector is `47 + K`.

**[v2 amendment — SA-1 narrowed by I-6.] `K = 3`, mandatorily.** v1 left a fork between `K = 3` (gender-pooled) and `K = 6` (gender-split), to be bound from the parameter table. **I-6 §4 forecloses the fork**: "Do not add sex-specific occupation densities … in the first LOC4 robustness." `δ_occ` is therefore **gender-pooled regardless of whether the certified wage block is itself gender-split**. The parameter-table read (SA-1) survives only as a *reporting* obligation — the memo must state which gender convention the certified wage block uses — and no longer as a design fork. Available evidence points to a gender-pooled wage block: I-1 §3 names the wage coordinate `beta_w_pexp2` **unsuffixed** while every leisure coordinate carries `_sm` / `_sf`.

**[v2 amendment — I-6 §4 documentation clause.] Mean only; dispersion not introduced.** I-6 §4 requires the mission to "document whether mean and/or dispersion changes are introduced." This design introduces an occupation-specific **mean (location)** and **no** occupation-specific dispersion: σ is shared across `k`. Occupation-specific `σ_k` is out of scope and is a distinct later axis. This is documented here, pre-execution, as the clause requires.

### 1.4 Identification source

**The claim: `δ_occ` is identified by within-occupation wage variation, and only by that.**

The added structural log-density contribution at a working alternative in occupation `k` with wage `w`:

```
Δ log f_W  =  δ_occ(k)·( log w − μ_i ) / σ²   −   δ_occ(k)² / (2σ²)
                    ↑ w-dependent                    ↑ constant in w, occupation-indexed
```

The second term is **constant within occupation `k`** and therefore **perfectly collinear with `β_occ_k`** of the certified `O^Occ` block. It contributes nothing identifying: any level shift it induces is absorbed by the re-estimated `β_occ_k`. What identifies `δ_occ` is the **first term**, which varies with `log w` *within* occupation `k`: occupation-`k` alternatives at high wages and at low wages receive *different* index adjustments, whereas `β_occ_k` adjusts them identically. The identifying variation is the **within-occupation dispersion of sampled log wages, interacted with the occupation label**, on the France 2016 singles sample (N = 1,555; 101 alternatives per household).

Three consequences, all binding:

1. **Shared σ is load-bearing.** With occupation-specific `σ_k` the `w`-dependent term acquires a second occupation-indexed channel and the separation argument no longer isolates a single coordinate.
2. **The `O^Occ` double-counting warning of I-3 §18 is deliberately entered, not evaded** — and I-6 §4 requires it to be *prevented*, not merely acknowledged. See §6.3 for the answer to that clause. The design does **not** drop, pin or restrict `β_occ_k`.
3. **Reference-category asymmetry.** `δ_occ(1) ≡ 0` and the `O^Occ` reference are the *same* category (I-3 §15.2, §15.6). Only contrasts are identified in both blocks; no statement about the level of either is admissible.

### 1.5 Bounds

`δ_occ(k) ∈ [−B, +B]`, symmetric, `B` a single scalar common to all `k`, **recorded pre-execution**. `B` is not fixed in this memo (open item **OL-2**, bound at freeze). Recommended rule: set `B` so that the implied multiplicative wage-location bracket strictly contains every observed raw between-LOC4 log-wage gap on the singles sample with slack, so that `B` is economically non-binding and any bound-hit is diagnostic of a fit pathology rather than of a tight box. Rejected alternatives: `B` tied to `σ̂` (makes the box a function of the block being perturbed); unbounded `δ_occ` (I-3 §17 requires a bound-hit diagnostic for every coordinate, and the four-leg standard needs a compact admissible set).

A `δ_occ` coordinate active at a bound is treated exactly as `beta_l_age2_sm` / `beta_l_age2_sf` at I-1 §2.1 — excluded from the covariance by construction, SE/z/p **literal NA**, never a numeral, never blank, never zero, never imputed downstream.

### 1.6 What does NOT change — exhaustive

| object | status under LOC4 | source |
|---|---|---|
| Leisure / preference block | form frozen; coordinates re-estimated | I-3 §16 |
| Access block `O^E` (`β_E`, `β_pt1`, `β_pt2`, `β_ft`, `β_gsur`, `β_E_educH`) | form frozen; coordinates re-estimated | I-3 §8, §16 |
| `O^Occ` block (`β_occ_k`) | form frozen; coordinates re-estimated; **not pinned** | I-3 §10; §1.4(2) |
| Hours bands / the `q_H` marginal (PT1 .15, PT2 .10, F35 .24, FT .20, LH .10, BG .21; 9-piece partition) | **bitwise frozen** | I-2 §3 |
| Employment margin (`π0 = 0.10`, `π0_r = 0.50`; design working share `0.80`) | **bitwise frozen** | I-2 §4 |
| Defensive mixture `λ = 0.25`; log-uniform `r_W`; uniform `r_Occ` over 4; uniform `r_H` | **bitwise frozen** | I-2 §2(i), §4 |
| Job-space geometry: `n = 1600`, `n_k = 400`, `S_i = 1601 / 1201 / 801`, node 0, 4 superblocks | **bitwise frozen** | I-2 §5.1, §6.1, §6.2 |
| Proposal convention (`log_q_H`, `log_prior`, `prior`) | **bitwise frozen**; LOC4 touches the structural index only | I-1 §1.2 |
| Pilot mincer payload and `q^W` (incl. its own occupation-conditional `μ_ik`, scalar σ) | **bitwise frozen** | I-2 §4 |
| EUROMOD / tax-benefit mapping (`ils_dispy`, FR 2015–2017, `drgn1`) | **bitwise frozen**, conditional on **G-L4-6** | I-3 §14.3; I-6 §4 |
| Welfare metric, inequality index, decomposition rule | **bitwise frozen** | I-6 §4 |
| Estimation sample and draw geometry (N = 1,555; 101 alternatives/hh; successor_v2 pins) | **bitwise frozen**, re-hashed fail-closed | I-1 §1.2 |
| Scope: singles P2a only; no couples, no pooled years, no `dclaborsupply` change (gitlink `27756a06`) | unchanged | I-1 §6.6 |

---

## 2. ESTIMATION PLAN

*(carried from v1 substantially intact)*

### 2.1 What is estimated

**Full re-estimation of the entire `47 + K` vector** under the corrected marginal/MIS proposal convention, on the successor_v2 frame, from the same 101-alternative draws. Not a profiled fit, not a two-step, not a warm-started perturbation of the certified block only: every preference, access, hours, wage and occupation coordinate is free simultaneously, because `δ_occ` is not separable from `β_occ_k` or from the leisure block by construction (§1.4).

The 10 pinned coordinates stay pinned. The two upper-bound-active leisure coordinates are **not** pre-set to their certified values: they are freed and allowed to re-locate, and whether they remain active at `+1.0` is a reported diagnostic.

**Prohibited:** any evaluated vector mixing θ̂_margqh-v2 coordinates with LOC4 coordinates other than as a documented warm start whose end point is a converged optimum in its own right. The suspended joint-convention estimate (theta-bytes `c024b893…f0580d`) is **never** a parameter source, warm start, or robustness arm (I-1 §1.3).

**[v2 amendment — reconciliation with I-6 §3.]** I-6 §3's "No parameter is re-estimated inside the welfare mission" governs the **baseline welfare prototype**, not this robustness mission; I-6 §4 defines the robustness mission as one that *changes the wage-density component*, which is unimplementable without re-estimation. The reconciliation is form-versus-coefficients and is set out at §6.2.

### 2.2 Convergence standard

The **amended four-leg convergence standard** applies unchanged in form, with the **deputy convergence-class rule governing leg (c)**.

The four legs' definitions are **not transcribable from this mission's attachment set** — they live in `FR_P2a_m08e_E3_reestimation_note_v2.md` (sha256 `970eda4c0d3dcc140b1608159c64fff420eb8395964e2e3b34f500c1a660a5f5`) and `convergence_records.json` (sha256 `9cf81c03e3e7e0ec58d87582f9454d5b076b53bccfe8d3154188878db926b50e`), neither attached. Entered as **NA-on-this-record**; mandatory transcription at freeze — **OL-3**. Fixed now:

- the standard applies **in full**, with no relaxation for the higher parameter count;
- leg (c) is adjudicated by the **deputy convergence-class rule**: the fit is assigned a convergence class and that class is reported, not collapsed to pass/fail;
- the target is the analogue of `E3-CONVERGED-SINGLE-OPTIMUM`. **A LOC4 fit that does not attain a single-optimum verdict is a return, not a headline.** A multi-optimum LOC4 surface is itself a substantive finding about `δ_occ`/`β_occ_k` separation.

### 2.3 Inference

Per Phase-4/5 conventions (I-1 §2), on the new free set:

- household-cluster **CR1**, `G = N = 1,555`;
- finite-sample factor `c = (G/(G−1))·((N−1)/(N−K_free)) = 1555/(1555 − K_free)`. **`K_free` changes, so `c` changes**; the certified numeral `1555/1520 = 1.0230263157894737` is the *baseline* value and **may not be carried across**;
- covariance dimension = the LOC4 interior set (certified 35 interior, plus interior members of `δ_occ`, less any coordinate that becomes bound-active). Bound-active coordinates are excluded by construction and reported literal NA;
- the inference-scope disclosure (I-1 §4, disclosure 7) and the prohibited-claims list (I-1 §5) bind LOC4 output as they bind baseline output. **`δ_occ` may not be described as a causal occupational wage premium**, and baseline-versus-LOC4 coefficient changes may not be described as statistically significant differences — the two vectors estimate different likelihood estimands and no covariance for their difference is constructed.

### 2.4 W-4 diagnostic and the S-10 rule

The corrected W-4 warning (non-gating) is run on the LOC4 free set. The certified flagged set is **{ `beta_l0_sm`, `beta_l0_sf`, `beta_l_nkids_sf` }** (I-1 §2.2).

> **No S-10 re-derivation unless the flagged set changes.** If the LOC4 W-4 flagged **membership** is identical to the certified set, the frozen five-scenario S-10 design of I-1 §3 is **not reopened** — not its coordinate set, not its D15 rule, not its scenario vectors — and **no S-10 battery is run on the LOC4 arm** within this mission.
>
> If the flagged membership **changes** in either direction (including a newly-flagged `δ_occ` coordinate), that is **a return, not an autonomous re-derivation**: the five-scenario set is frozen by deputy ruling §4 and R-109, and altering it is a numerical-semantics change.

**Why no S-10 on the LOC4 arm in the headline comparison.** The headline object is a difference in point welfare objects under CRN. Running S-10 on both arms would produce a 5 × 2 grid whose cross-arm differences confound specification effect with perturbation effect, and whose LOC4 `Δ_j` would mechanically differ from the frozen baseline `Δ_j` because they are half-robust-SE quantities from a different covariance. Differences are taken at **scenario 1 on the baseline arm and θ̂^LOC4 on the LOC4 arm**. S-10 on the LOC4 arm is triggered only in decision-tree branch B (§4.4), under a deputy disposition. The standing S-10 disclosure applies throughout: Tier-1 deterministic sensitivity, not a confidence region, not a bootstrap, not a posterior, and it does not produce welfare confidence intervals.

---

## 3. THE COMPARISON DESIGN — REBUILT ON THE DEPUTY DIFFERENCE-MATERIALITY INSTRUMENT

**This section replaces v1 §3 in its entirety.** v1 §3.4 recorded that the `threshold_set_of_record` was a *level* instrument with level-scaled denominators undefined on a difference, recorded two candidate readings (R-a, R-b), and selected neither. **Part B adopts R-a.** OL-4 is closed. What follows is the deputy instrument, not a manager construction.

### 3.1 Governing convention: fixed baseline denominators (R-a)

> **Adopt R-a: use the BASELINE ARM as the fixed scale. Do not allow the LOC4 result to enlarge its own precision tolerance.** (I-7)

Every denominator in §3.3 and §3.4 is a **baseline-arm constant**, transcribed once, pinned pre-execution, and held fixed for the whole mission. No denominator reads the LOC4 arm. This forecloses the pathology in which a LOC4 arm with a large level automatically widens its own tolerance and thereby manufactures immateriality.

### 3.2 Direct blockwise CRN differences

> For every functional, compute the common-random-number difference directly:
> `Delta_T_b = T_LOC4_b − T_BASE_b`
> Estimate `E_Delta` directly from the blockwise differences. **Do not add the two arm-level error bands.** (I-7)

**Construction, stated to remove ambiguity:**

```
for each accepted block replicate b:
      Δ_T,b   =   T_LOC4(b)   −   T_BASE(b)          ← same b, same nodes, both arms
Δ̂        =   T_LOC4(T16)  −  T_BASE(T16)
E_Δ      =   the block error estimate computed DIRECTLY on { Δ_T,b }
```

**Three prohibitions, each a defect if violated:**

1. **`E_Δ` is never formed from the arms' own bands.** Not their sum, not their quadrature sum, not their difference. `E_T(LOC4) ⊕ E_T(BASE)` in any form discards the CRN covariance term, systematically overstates uncertainty, and converts genuine material differences into `INDETERMINATE_MC` returns. An implementation that does this is a defect, not a conservative choice.
2. **`Δ_T,b` is computed within replicate `b`, never across replicates.** The same block index, the same nodes, both arms.
3. **The difference is taken on the functional, not on the components of the functional.** For ratio and share objects, `Δ` is the difference of the assembled functional, not a difference propagated through its parts.

**The replicate index `b` is Stage-A-bound (OL-8).** The recorded block machinery is the 4-superblock structure (`n_k = 400`, 300 base / 100 defensive, `400 ≡ 0 (mod 4)`, realised defensive fraction exactly `0.25` in every `D_k`) with the associated leave-one-out family (`T16` → `T12_(-b)`). Which of these constitutes "the accepted block replicates" for `{Δ_T,b}` must be bound from the recorded schema per standing practice 13, not from memory. Both layers are named here so the binding is a read, not a choice.

### 3.3 Layer 1 — PRECISION gates on the difference (Part B, verbatim thresholds)

These test whether the **difference is resolved**. They are *not* materiality thresholds.

| class | baseline-arm scale | precision gate |
|---|---|---|
| mean | `S_k0 = max( |mean_Wk_baseline| , |median_Wk_baseline| , IQR_Wk_baseline , 1 € )` | `E_Δ,mean / S_k0 ≤ 0.0025` |
| median | same `S_k0` | `E_Δ,median / S_k0 ≤ 0.0025` |
| Gini | — (absolute) | `E_Δ,Gini ≤ 0.00125` |
| component levels (φ) | — (absolute) | `E_Δ,φ ≤ 0.00125` |
| normalized contributions | `S_r0 = max( 1 , |r0| )`, `r0` the **baseline** normalized contribution | `E_Δ,r / S_r0 ≤ 0.005` |

**Transcribed baseline-arm constants available on this record** (I-2 §6.4), for pinning `S_k0` and `S_r0`:

| object | baseline `T16` | baseline arm's own `E_T` | baseline level-gate ratio |
|---|---|---|---|
| `W1_mean` | `1396.13` | `3.02142` | `0.866` (pass) |
| `W1_median` | `1340.43` | `11.5733` | `3.316` (FAIL) |
| `W1_gini` | `0.173955` | `0.000869933` | `0.696` (pass) |
| `W1_phi_A_level` | `0.00617588` | `0.000468934` | `0.375` (pass) |
| `W1_phi_B_level` | `0.0114346` | `0.00119598` | `0.957` (pass) |
| `W1_s_opp` ( ≡ `r_phi_A+phi_B` ) | `0.101236` | `0.0094323` | `1.886` (FAIL) |

**`IQR_W1_baseline` is not on this record** and is a required component of `S_k0`. It must be transcribed from the functionals artifact at execution — **OL-9**. Until it is, `S_k0` is known only to be **at least** `|mean| = 1396.13`, since the max is over a set containing that value.

**`S_r0` for `s_opp` resolves to the unit floor**: the transcribed baseline `r0 = 0.101236` lies below `1`, so `S_r0` is governed by the `max(1, ·)` floor and the `s_opp` precision gate is effectively absolute at `E_Δ,r ≤ 0.005`. This is a reading of the transcribed record, not a computed quantity, and it is stated because it materially changes how demanding that gate is.

### 3.4 Layer 2 — SUBSTANTIVE thresholds (Part B; these coincide with Path-B §5)

These test whether a **resolved** difference is **material**. Every one of them is jointly sourced: **deputy Part B** supplies the operational form, **I-6 §5** supplies the economic content. Both instruments are cited on every row, per the ROLE's requirement.

| # | criterion | threshold `m` | Part B form | Path-B source |
|---|---|---|---|---|
| M-1 | mean money-metric welfare | `0.01` | `|Δ_mean| / max(|mean_Wk_baseline|, 1 €) ≥ 0.01` | I-6 §5.3 ("mean or median money-metric welfare changes by at least 1 percent") |
| M-2 | median money-metric welfare | `0.01` | `|Δ_median| / max(|median_Wk_baseline|, 1 €) ≥ 0.01` | I-6 §5.3 |
| M-3 | welfare Gini | `0.005` | `|Δ_Gini| ≥ 0.005` | I-6 §5.2 ("welfare Gini changes by at least 0.005") |
| M-4 | opportunity-attributable share | `0.02` | `|Δ_s_opp| ≥ 0.02` | I-6 §5.1 ("opportunity-attributable inequality share changes by at least 2 percentage points") |
| M-5 | sign / ordering | — | sign or ordering of a headline decomposition component changes; **must agree across all accepted block replicates** | I-6 §5.4 |
| M-6 | qualitative conclusion | — | the paper's qualitative conclusion about the importance of opportunity heterogeneity changes | I-6 §5.5 |

**Two explicit prohibitions, transcribed:**

> **"Do not invent a component-level materiality cutoff. Component materiality is assessed through stable sign/order changes and the qualitative-conclusion criterion."** (I-7)
>
> **"Other normalized component differences are reported with bands but do not receive an invented 2pp threshold."** (I-7)

Accordingly: **`φ_A` and `φ_B` receive a precision gate (`E_Δ,φ ≤ 0.00125`) and NO substantive cutoff.** Their materiality is assessed **only** through M-5 and M-6. Likewise `φ_P`, `R_bg`, `r_phi_A`, `r_phi_B`, `r_phi_P`, `r_R_bg` and the `I_{·}` family: reported with bands, no invented threshold, no materiality verdict of their own. This is a substantive change from v1, where φ_A and φ_B sat in a headline set whose treatment implied thresholds that do not exist. See **C-9**.

**M-6 is not operational on the record.** "The paper's qualitative conclusion about the importance of opportunity heterogeneity" must be **written down pre-execution as a single decidable statement**, so that "changes" has a determinate meaning ex ante. This is a pre-registration requirement, not an invented threshold. **OL-11**, blocking before execution.

### 3.5 Sign and ordering

> **"Sign and ordering changes must agree across all accepted block replicates."** (I-7)

Operationally: `sign(Δ_T,b)` identical for every accepted replicate `b` and equal to `sign(Δ̂)`; and the ordering relation among headline decomposition components (in the first instance `φ_A` versus `φ_B`) identical in `Δ̂` and in every `Δ_T,b`. **Disagreement across replicates is not a material finding and is not an immaterial finding — it is an `INDETERMINATE_MC` on M-5**, and therefore a return (§4.3).

### 3.6 CRN construction — where it is exact, where only partial

*(carried from v1 §3.2 intact; unchanged by Part B, which presupposes CRN rather than specifying it)*

**Design intent:** `δ_occ` enters the **structural index only**. It does not enter `q^W`, the `q_H` marginal, `q_Occ`, `log_prior`, the employment margin, `λ`, or the node identities.

**Exact on the base half (75%), conditional on G-L4-1.** `q^W`'s wage mean is built from the frozen pilot mincer payload, not from θ (I-2 §4). If the base draw path reads no coordinate of θ, then across arms these are bitwise identical: `working`, `hours`, `wage`, `loc4`, `log_q_E`, `log_q_H`, `log_q_W`, `log_q_Occ`, `log_prior`, `log_q_base`, `stream_seed`, `base_position`, `component_label`, `in_support_box`, the priced consumption, node 0 and its zero correction, superblock membership, `S_i`. Verified — not assumed — by the bitwise-column instrument of record (I-2 §2(iii): 17 of 17 columns bitwise equal, `columns_not_bitwise: []`).

**At risk on the defensive half (25%): the frozen box.** `DefensiveComponent.draw` maps its uniforms **through** the box, so any box move regenerates every defensive node and voids the pairing on that half. The record establishes that the box is evaluated at θ and **has moved before**: `box_at_theta_v2.box_moved: true`, `delta_log_L: 0.06107235168894798`, with `311000 = 1555 × 200` defensive nodes re-priced and `additional_nodes_due_to_box_move: 155500` (I-2 §2(ii)).

| branch | condition | CRN status | consequence for `E_Δ` |
|---|---|---|---|
| **CRN-exact** | box at θ̂^LOC4 bitwise equals `box_hash_sha256 = 67ef22b3742ccc04a25c377cec60e18478b6fd07e539c0340497a274c0ce2c52` / `float64_bytes_sha256 = 8e44ec2a926aa06fd844a0be97fdbfdc29d3299ca1a7b3a1eb46a7191ae6e361`; `h_min/h_max = 5.0/70.0`, `w_min/w_max = 1.9411632533361265/101.91995852573758`, `log_range_L = 3.9609003763945605` unchanged | exact on **all** nodes | `E_Δ` is a fully paired difference band; this is the intended regime and the reason LOC4 is affordable |
| **CRN-partial** | box moves at θ̂^LOC4 | exact on the base 75%; **broken** on the defensive 25% | the unpaired quarter contributes its full variance with no cancellation. `E_Δ` must be **reported under the partial pairing and labelled as such**, and may not be presented as a CRN difference band |
| **halt** | box moves **and** re-pricing is required | — | EUROMOD re-pricing at the recorded scope (155,500 per defensive half; 311,000 across both) is a cost and a custody event, disclosed with the pairing loss |

**No CRN repair is attempted.** Re-seeding, re-mapping, or reusing pre-move defensive uniforms to manufacture pairing is prohibited: I-2 §2(ii) establishes that pre-rebind defensive nodes do not survive anywhere in the stack.

**What CRN does not buy.** Both arms are evaluated at their **own full re-estimated vectors** (§2.1). CRN pairs the *randomness*, not the *parameters*. `Δ` is therefore the effect of the **specification change as a whole**, not the partial effect of the `δ_occ` term. Sentences of the form "adding occupation to the wage block moves W1 mean by …" are prohibited; the admissible form is "the LOC4 specification differs from the baseline specification in W1 mean by …". (**C-7**.)

### 3.7 Reporting order

**Tier 1 — the two-layer battery of §3.3–§3.5** on: `W1_mean`, `W1_median`, `W1_gini`, `W1_s_opp`, plus M-5 on the headline decomposition components (`φ_A`, `φ_B`) and M-6.

**Tier 2 — reported with bands, no materiality verdict:** all other normalized contributions, the `I_{·}` family, `φ_P`, `R_bg`, and the W3 validation comparison. W4 and W6 differences are reported banded with the I-2 §5.2 riders attached (A4-1, A4-2).

Every reported object is a **difference**. Arm levels appear only as the fixed denominators of §3.1 and as banded standalone magnitudes under the rider of §4.2.

---

## 4. THE DECISION TREE — REBUILT ON THE DEPUTY CLASSIFICATION RULE

**This section replaces v1 §4 in its entirety.**

### 4.1 The classification rule (Part B, verbatim)

For threshold `m` and its associated `Δ̂`, `E_Δ`:

```
LOC4_MATERIAL                        when   |Δ̂| − E_Δ  ≥  m
LOC4_IMMATERIAL                      when   |Δ̂| + E_Δ  <  m
LOC4_MATERIALITY_INDETERMINATE_MC    otherwise
```

> **"Apply the same rule to baseline-relative mean/median ratios."** (I-7)

For M-1 and M-2 the tested object is the **ratio**; since its denominator is a fixed baseline constant (§3.1), the rule transfers exactly, with `Δ̂` and `E_Δ` both divided by `max(|mean_Wk_baseline|, 1 €)` (resp. median) before comparison to `m = 0.01`.

**`LOC4_MATERIALITY_INDETERMINATE_MC` is a return.** It is a **verdict**, not a state to be resolved by re-running until it resolves. Specifically prohibited without deputy disposition: extending the ladder beyond 16x to shrink `E_Δ`; re-drawing; re-seeding; dropping an object from Tier 1; substituting a Tier-2 object for a Tier-1 one; or re-reading a functional's threshold class.

**Aggregation to a mission verdict**, per I-6 §5 ("materially different if **any one** occurs"):

- **LOC4 IMMATERIAL overall** iff every Tier-1 criterion (M-1…M-6) returns `LOC4_IMMATERIAL` (or, for M-5/M-6, returns unambiguous agreement/no-change).
- **LOC4 MATERIAL overall** iff **any** Tier-1 criterion returns `LOC4_MATERIAL`.
- **Return** if **any** Tier-1 criterion returns `LOC4_MATERIALITY_INDETERMINATE_MC`, or if M-5 disagrees across replicates. This is also an explicit deputy return trigger ("LOC4 difference precision is indeterminate on a headline threshold").

### 4.2 THE ARM-PRECISION RIDER (Part B, verbatim — and it supersedes v1's C-3 rider)

> **"Do not adopt the proposed rule that either arm's standalone level-precision failure automatically removes the LOC4 materiality verdict. A standalone arm that fails its level gate remains banded and cannot be promoted as a standalone magnitude.**
> **But a LOC4-minus-baseline materiality verdict is permitted when:**
>
> * **both arms pass validity, support, reference and estimand-comparability gates; and**
> * **the direct CRN difference passes its own precision gate.**
>
> **If the direct difference fails precision, report it as uncertified and make no materiality verdict.**
> **If either arm fails validity, support, reference or estimand comparability, no difference verdict is permitted."** (I-7)

**This supersedes v1 §5.5 finding C-3 and its Tier-2 rider.** v1 held that "where either arm fails its level threshold, no materiality verdict is issued on that functional." **That blanket rule is rejected by the deputy and is withdrawn.** The corrected logic separates **level precision** (a property of one arm's standalone magnitude) from **difference precision** (a property of the paired CRN difference), and only the latter gates the materiality verdict.

**Operational consequences, stated concretely on the transcribed record:**

| object | baseline arm's level gate | v1 treatment (WITHDRAWN) | v2 treatment under the rider |
|---|---|---|---|
| `W1_s_opp` | **FAIL** (ratio `1.886`) | no materiality verdict permitted | **verdict-eligible on M-4**, provided both arms pass validity/support/reference/comparability and `E_Δ,r / S_r0 ≤ 0.005`. The **level** `0.101236` remains **banded and non-promotable** as a standalone magnitude |
| `W1_median` | **FAIL** (ratio `3.316`) | outside the closure headline set; banded | **verdict-eligible on M-2** under the same two conditions; the level remains banded |
| `W1_mean`, `W1_gini`, `φ_A`, `φ_B` | pass | headline | unchanged; still require the **difference** precision gate — passing a level gate does not license a difference verdict |

**The arm gates that do still block a difference verdict** are validity, support, reference and estimand comparability — not precision. In this design those are exactly **G-L4-3** (proposal invariance), **G-L4-4** (geometry invariance), **G-L4-5** (support invariance, zero off-box nodes on both arms on the same rows), **G-L4-6** (EUROMOD occupation-invariance, the estimand-comparability gate), and **G-L4-7** (normalisation). A failure in any of those means **no difference verdict is permitted at all**, for any functional.

### 4.3 Branch A — LOC4 IMMATERIAL

**Condition:** every Tier-1 criterion returns `LOC4_IMMATERIAL`; M-5 agrees across all accepted block replicates; M-6 records no change against the pre-registered statement (OL-11).

**Verdict:** **retain the certified baseline as the preferred specification and report LOC4 as robustness** (I-6 §5, final paragraph).

**Pipeline consequences:**

- **Rebinds:** nothing. No welfare artifact, no `q^W` object, no `Z`, no `ĝ` sampler, no coalition target, no pricing ladder rebinds.
- **Re-runs:** nothing.
- **Stays frozen:** θ̂_margqh-v2 as sole parameter source; the frozen box; the five-scenario S-10 set; the 16x stack; the prototype closure and its headline set.
- **New obligation:** a **disclosure** in every manuscript, notebook, table, figure and memo carrying a decomposition number — that the wage block was tested against the LOC4 occupation-conditional four-density extension and the headline objects were immaterially affected — reported with `Δ̂` and `E_Δ` in full, the classification per criterion, and the CRN status of §3.6. The disclosure must state that the axis tests **occupation-conditional wage location only**: not dispersion (`σ_k`), not occupation-conditional hours (`O^H | Occ`, the `M4` axis), not regional opportunity (`M2`), not industry (`lindi`, deferred at I-6 §6). Immateriality on this axis is not immateriality on the occupation dimension.
- **I-6's mandatory-before-final-claims status is discharged for this axis**, and the sequencing of I-6 §6.4 is satisfied: preferred quantitative welfare results may be frozen.

### 4.4 Branch B — LOC4 MATERIAL

**Condition:** any Tier-1 criterion returns `LOC4_MATERIAL`.

**Verdict:** **the preferred specification must be reconsidered before final paper-facing quantitative claims** (I-6 §5). The manager does **not** select LOC4 as preferred, and does **not** select baseline as preferred, on its own authority. **This is a return** — and it is a return under two independent deputy triggers: "LOC4 changes sign/order or the qualitative conclusion" (if M-5/M-6 fired) and "the preferred specification cannot be selected."

**Pipeline consequences:**

- **Nothing rebinds pending the deputy disposition.** The welfare pipeline is **held**, not switched. θ̂_margqh-v2 remains the parameter source of record throughout the return.
- **Stays frozen during the return:** everything. The M08 prototype closure is not withdrawn; it remains a correctly-scoped acceptance of the baseline arm.
- **The return packet carries:** the LOC4 convergence class and four-leg result; the `47 + K` parameter table with CR1 SEs on the recomputed `c`; the W-4 flagged membership; per-criterion `Δ̂`, `E_Δ` and classification; the CRN status with the box-hash comparison; the `δ_occ`/`β_occ_k` separation evidence (G-L4-8); and every coherence finding of §5.5 that fired.
- **If and only if the deputy promotes LOC4** does the full rebinding cascade of I-1 §6 execute in its stated order — rebinding → deterministic + N-test batteries (N1–N9, in full, **before any pricing**) → U6 → pricing ladder → welfare → decomposition → S-10 → LOC4 — with S-10 re-derived under a deputy-approved revision register (§2.4), and with the RUM benchmark re-estimating its own preferences under the promoted specification (I-1 §6.3; `g ≡ 1` with a retained θ̂ remains forbidden).
- **If the deputy retains baseline**, Branch A's disclosure applies **strengthened**: it must report that the axis produced a material difference and that the baseline was retained by ruling, with the LOC4 numbers shown. A material difference disclosed as immaterial is a prohibited claim.
- **I-6 §7 downstream note:** "a parsimonious two-group LOC4 comparison if the four-density variant materially changes the results" is classified *useful later*. It is **not** part of this mission and is not authorised by a material verdict; it is a candidate for the deputy's disposition.

### 4.5 Branch C — LOC4_MATERIALITY_INDETERMINATE_MC

**Condition:** any Tier-1 criterion falls in the `otherwise` band; or M-5 disagrees across replicates; or the direct difference fails its own precision gate (in which case the object is **reported as uncertified with no materiality verdict**, per the rider); or an arm fails validity/support/reference/comparability (in which case **no difference verdict is permitted at all**); or the LOC4 fit does not attain a single-optimum convergence verdict (§2.2).

**Verdict:** **return.**

**Pipeline consequences:** nothing rebinds; nothing is re-run to break the tie on manager authority; the prohibitions of §4.1 apply. The return states which limb was indeterminate and why, and — where the cause is precision rather than substance — carries the cost estimate of the precision extension that would resolve it, for the deputy to authorise or decline. The M08 prototype was closed under `LIMITED_MC_PRECISION` precisely because precision was accepted as a scoped constraint; indeterminacy traceable to that constraint is an expected outcome of the closure, not a failure of this mission.

---

## 5. FROZEN vs STAGE-A-BOUND; GATES; OPEN ITEMS; COHERENCE

### 5.1 Frozen by this design

*(carried from v1, updated to v2's §3/§4)*

The variant's functional form (§1.3: additive occupation-specific wage **location**, shared σ, fixed reference, `K = 3` gender-pooled); the exhaustive no-change list (§1.6); full simultaneous re-estimation with `β_occ_k` free (§2.1); the four-leg standard applied without relaxation (§2.2); the no-S-10-without-membership-change rule (§2.4); direct blockwise CRN differences with `E_Δ` estimated on `{Δ_T,b}` and never from arm bands (§3.2); fixed baseline denominators, R-a (§3.1); the two-layer precision/substantive system with no invented cutoffs (§3.3–§3.4); the MATERIAL/IMMATERIAL/INDETERMINATE_MC rule and the arm-precision rider (§4.1–§4.2); the three-branch tree with a **held** pipeline in Branches B and C (§4.3–§4.5); the no-CRN-repair rule (§3.6).

### 5.2 Stage-A-bound at execution (from the recorded schema — standing practice 13)

| id | item | bound from | v2 status |
|---|---|---|---|
| SA-1 | Gender convention of the certified wage block | `e4_parameter_table.csv` `21a05fb5…` | **narrowed** — reporting obligation only; `K = 3` is mandated by I-6 §4 regardless |
| SA-2 | Four-leg convergence legs; convergence-class rule for leg (c) | E3 chain; `convergence_records.json` `9cf81c03…` | unchanged (OL-3) |
| SA-3 | Whether any draw-generating object reads θ (CRN-exactness precondition) | `m08_qw_streams` recorded schema; the 17-column instrument | unchanged |
| SA-4 | Box at θ̂^LOC4 vs `67ef22b3…` / `8e44ec2a…` | `u6f_frozen_box_v1.json` | unchanged |
| SA-5 | Analytic `Z` closed form and its wage-factor support (§5.4) | the normalisation ruling | unchanged (OL-5) |
| SA-6 | `δ_occ` bound `B`, recorded pre-execution | §1.5 rule, at freeze | unchanged (OL-2) |
| SA-7 | LOC4 W-4 flagged membership | E4-analogue `step3_w4.corrected_detail` | unchanged |
| **SA-8** | **Definition of the accepted block replicate index `b`** for `{Δ_T,b}` | recorded block schema (4 superblocks / the `T12_(-b)` LOO family) | **new in v2** (OL-8) |
| **SA-9** | **`IQR_W1_baseline`**, required to pin `S_k0` | the functionals artifact | **new in v2** (OL-9) |

### 5.3 Validation gates — N-series analogues on the extended block

*(carried from v1 intact; the §4.2 rider makes explicit which of these are the "validity, support, reference, estimand-comparability" gates that block a difference verdict)*

| gate | statement | blocks a difference verdict? | failure handling |
|---|---|---|---|
| **G-L4-1** | **CRN exactness.** The 17 recorded columns bitwise equal across arms on the base half; `columns_not_bitwise: []` required | no — classifies the pairing | non-empty ⇒ classify per §3.6; a change in a column that should not depend on θ is a halt |
| **G-L4-2** | **Box invariance.** Both box hashes compared at θ̂^LOC4 | no — classifies the pairing | move ⇒ CRN-partial branch; disclose; **never** repair |
| **G-L4-3** | **Proposal invariance.** `log_q_H`, `log_prior`, `prior`, `log_q_W`, `log_q_Occ`, `log_q_W_mixture` bitwise unchanged; the `q_H` 9-piece partition and its `unit_mass_certificate` (`exact_integral = 1/1`, `float64_integral = 1.0`, `float64_equals_one_bitwise: true`, `float64_abs_deviation = 0.0`) re-verified | **YES** (validity) | any change ⇒ the variant has leaked into the proposal ⇒ **halt** |
| **G-L4-4** | **Geometry invariance.** `n = 1600`, `n_k = 400`, `S_i = 1601` on `T16`, node 0 once per household at zero correction, 0 node exclusions in the attained leg, 4 superblocks, realised defensive fraction exactly `0.25` | **YES** (reference / comparability) | any change ⇒ halt |
| **G-L4-5** | **Support invariance.** Zero off-box working ladder nodes on both arms, on the same rows | **YES** (support) | non-zero ⇒ halt |
| **G-L4-6** | **EUROMOD occupation-invariance.** Confirm on the French baseline that `ils_dispy` does not depend on occupation (I-3 §14.3 requires this confirmation and does not assert it; I-6 §4 requires the tax-benefit mapping preserved) | **YES** (estimand comparability) | dependence ⇒ the budget mapping moves between arms ⇒ **halt and return**; not repairable inside LOC4 |
| **G-L4-7** | **Normalisation.** N1–N9 analogues re-run **in full** on the extended block **before any pricing**, against the rebound `ĝ = g̃ / Z_i^S`. Prior passes are void as gates | **YES** (validity) | any failure ⇒ halt; this is the M08E lesson and is not negotiable |
| **G-L4-8** | **`δ_occ` / `β_occ_k` separation.** Report the fitted correlation structure between the `δ_occ` and `β_occ_k` coordinates and each coordinate's bound-hit status | no — diagnostic | near-degeneracy is a **reported finding** (C-4); it is **not** answered by pinning `β_occ_k` |

### 5.4 Normalisation invariance — does `Z` move under `δ_occ`?

*(carried from v1 intact)*

The welfare-layer opportunity object is `ĝ = g̃ / Z_i^S`, with **analytic `Z` over the full mixed support** (I-1 §6.4). `g̃` carries the structural wage factor. The answer forks on one schema fact:

- **If `Z`'s closed form integrates the wage factor over the unbounded support `w ∈ (0, ∞)`:** the log-normal factor integrates to **exactly 1 for every `k` and every `δ_occ`** — a location shift does not change total mass. **`Z` is invariant under `δ_occ`.** I-2 §4 supports this branch on the proposal side: `q_W` is explicitly **untruncated** ("no bound, no clip, no rejection", only an `eps = 1e-300` guard), and `w_min`/`w_max` are recorded as *realised sample statistics*, not design bounds.
- **If `Z`'s closed form integrates the wage factor over the frozen box `w ∈ [1.9411632533361265, 101.91995852573758]`:** the factor is **truncated**, its mass is `Φ((log w_max − μ_i − δ_occ(k))/σ) − Φ((log w_min − μ_i − δ_occ(k))/σ)`, which **depends on `δ_occ(k)`**. **`Z` moves — household-specifically and occupation-specifically.** The schema carries an `in_support_box` column and zero off-box nodes on every rung, which is at least consistent with a box-bounded welfare job space. The analytic `Z` closed form must then be **extended to carry `δ_occ`**.

**Standing prohibition.** Silently reusing the baseline `Z` on the LOC4 arm in the truncated branch would reintroduce **exactly the M08E defect** — a household-specific, coalition-varying `log Z` offset corrupting welfare comparisons. Because `Δ` is taken across arms, a `Z` error would **not cancel under CRN**; it would sit directly in the headline difference.

> **`Z` is treated as `δ_occ`-dependent until the normalisation ruling's closed form is read and shown otherwise (SA-5).** The burden of proof runs toward extension, not invariance. G-L4-7 gates it. An invariance claim asserted without the closed form in hand is a halt.

### 5.5 Coherence check — rerun for v2. Incoherence is a named finding, never designed around.

**Carried from v1, unchanged:**

| id | finding | status |
|---|---|---|
| **C-1** | **The headline set is precision-selected, and the paper's own object was not in it.** {W1 mean, Gini, φ_A, φ_B} is exactly the MC-passing subset of I-2 §6.4, while `W1_phi_A+phi_B_level` (`E_T = 0.00164734`, ratio `1.318`) and `W1_s_opp` (`E_T = 0.0094323`, ratio `1.886`) fail. | **PARTIALLY RESOLVED in v2.** The arm-precision rider (§4.2) makes `s_opp` **verdict-eligible on the difference** via M-4, which is precisely what I-6 §5.1 requires. What remains unresolved: the **level** of the opportunity share is still banded and non-promotable. See **C-10**. |
| **C-2** | The `threshold_set_of_record` was a level instrument with denominators undefined on a difference. | **CLOSED** by I-7's adoption of R-a. |
| **C-3** | Both arms may fail precision on the same functional; v1 issued a blanket "no verdict where either arm fails its level gate". | **SUPERSEDED AND WITHDRAWN.** The deputy explicitly rejects this rule (§4.2). v1's Tier-2 rider is void. The governing rule is the arm-precision rider: level failure bands the standalone magnitude but does not remove the difference verdict. |
| **C-4** | **Deliberate double-counting.** I-3 §18 forbids occupation in two blocks except as a deliberate extension; separation rests entirely on the `w`-interaction. | **Named; answered at §6.3** as required by I-6 §4. G-L4-8 verifies. Near-degeneracy is **reported as a finding about the model**, not repaired by pinning `β_occ_k` — pinning would silently change the estimand. |
| **C-5** | **Baseline asymmetry.** Occupation shifts the **proposal** wage location but is **absent** from the **structural** wage block. The model draws as if occupation matters for wages and estimates as if it does not. | **Named; disclosed up front.** Must appear in the Branch A disclosure. Presenting LOC4 as merely exploratory, rather than as the repair of a known asymmetry, would misstate the record. |
| **C-6** | `Z` may or may not move; the record here does not settle it. | Named; resolved by reading the closed form (SA-5), not by assumption. Default posture: **moves**. |
| **C-7** | The comparison is specification-level, not coordinate-level. | Named; coordinate-level attribution language prohibited throughout. |
| **C-8** | The upstream CV1 return (A5-i, A5-ii) is unresolved and adjacent. | **Unchanged**, and restated at §0.2. LOC4 inherits the estimator as implemented and does not repair it. If those returns change the raw estimator, **LOC4's comparison must be re-run.** |

**New in v2:**

| id | finding | status |
|---|---|---|
| **C-9** | **The closure's headline set is now internally heterogeneous.** I-4's headline set is {W1 mean, W1 Gini, φ_A, φ_B}. Under I-7, mean and Gini receive a **two-layer** test (precision gate + substantive threshold), while **φ_A and φ_B receive a precision gate and no substantive cutoff** — their materiality runs only through M-5 (sign/order) and M-6 (qualitative conclusion), because inventing a component-level cutoff is prohibited. Two members of one "headline set" are therefore tested by different logics. | **Named, not designed around.** No component-level cutoff is invented. The consequence is stated plainly in reporting: for φ_A and φ_B, "immaterial" means *"sign and ordering stable across all replicates and the qualitative conclusion unchanged"* — **never** *"the change is small"*, since no cutoff exists against which smallness could be certified. |
| **C-10** | **The paper can certify that LOC4 does not move the opportunity share by ≥ 2pp while being unable to certify the share's own level.** `s_opp`'s baseline level gate fails at ratio `1.886`; under the rider its **difference** is verdict-eligible but its **level** stays banded. | **Named as a reporting hazard.** Binding consequence: any sentence reporting the M-4 verdict must be a **difference** sentence. Reporting "the opportunity share is X and LOC4 does not change it" would promote a banded magnitude by juxtaposition, which the rider forbids. The admissible form reports the difference and its band, with the level carried only as a banded figure explicitly marked non-promotable. |
| **C-11** | **I-6 §3 ("No parameter is re-estimated inside the welfare mission") versus §2.1's full re-estimation.** Read flatly, the two conflict. | **Named and reconciled at §6.2**, not designed around: §3 governs the *baseline welfare prototype*; §4 defines the *robustness mission* as one that changes the wage-density component, which is unimplementable without re-estimation. The reconciliation is form-preserved / coefficients-free. If the deputy reads §3 as binding on the robustness mission too, **LOC4 as specified is not executable** and that is a return, not a redesign. |
| **C-12** | **The Path-B substantive battery and the closure headline set are different sets.** I-6 §5.3 makes **median** a materiality criterion (M-2), but `W1_median` is **not** in the closure's headline set and fails its baseline level gate badly (ratio `3.316`). Conversely φ_A and φ_B are in the closure headline set but receive no Path-B substantive threshold (C-9). | **Named.** v2 tests the **Path-B battery** (M-1…M-6), because I-6 §5 is the instrument that defines materiality; the closure headline set governs what the *prototype* certified, not what LOC4 must test. The two sets are reported side by side so the difference is visible rather than silently resolved. |
| **C-13** | **M-6 has no operational definition on the record.** "The paper's qualitative conclusion about the importance of opportunity heterogeneity" is not written down anywhere as a decidable statement, so "changes" is not decidable ex ante — and M-6 is a deputy return trigger. | **Named. Blocking (OL-11).** Resolved by **pre-registration**, not by invention: a single written statement of the qualitative conclusion, recorded before execution, against which change is assessed. Deciding M-6 post hoc against an unrecorded conclusion would be exactly the failure mode the pre-registration discipline exists to prevent. |
| **C-14** | **The rider's arm gates are validity-type, not precision-type — and one of them (G-L4-6) has never been confirmed.** The rider permits a difference verdict only if both arms pass *estimand comparability*, which here is EUROMOD occupation-invariance. I-3 §14.3 **requires that confirmation and does not assert it**; it has not been performed on this record. | **Named. Blocking (OL-6).** Until G-L4-6 passes, **no difference verdict is permitted for any functional** — not merely a precision caveat. This is a stronger consequence than v1 assigned it, and it follows directly from the rider. |

### 5.6 Open items — refreshed

| id | item | v2 status |
|---|---|---|
| **OL-1** | LOC4 Path-B ruling text | **CLOSED.** Located: `JMP_LOC4_pathB_ruling_v1.md` — "JMP LOC4 Ruling v1 — Path B with Mandatory First Robustness", ChatGPT JMP Deputy Programme Director, binding before the welfare mission. Reconciled clause-by-clause at §6. Two errata recorded at §6.4. |
| **OL-4** | Materiality thresholds on differences | **CLOSED** by deputy Part B (I-7): R-a adopted, baseline-arm fixed denominators, direct CRN differences, two-layer system, MATERIAL/IMMATERIAL/INDETERMINATE_MC, arm-precision rider. |
| **OL-2** | `δ_occ` bound `B` | **OPEN — bound at freeze.** Rule at §1.5; numeral recorded pre-execution. |
| **OL-3** | Four-leg convergence leg definitions and the class rule for leg (c) | **OPEN — BLOCKING.** NA-on-this-record; mandatory transcription from the E3 chain. |
| **OL-5** | `Z` closed-form support (§5.4, SA-5) | **OPEN — BLOCKING before any pricing.** |
| **OL-6** | EUROMOD occupation-invariance (G-L4-6) | **OPEN — BLOCKING, and now stronger:** under the rider it gates *every* difference verdict (C-14). |
| **OL-7** | Dependency on the CV1 return disposition (C-8) | **OPEN — tracked, not blocking at freeze.** If the raw estimator changes, LOC4 re-runs. |
| **OL-8** | Definition of the accepted block replicate index `b` for `{Δ_T,b}` (SA-8) | **OPEN — Stage-A bound.** New in v2. |
| **OL-9** | `IQR_W1_baseline`, required to pin `S_k0` (SA-9) | **OPEN — transcription at execution.** New in v2. Until pinned, `S_k0` is known only to be at least `1396.13`. |
| **OL-10** | Errata pins: the stale `docs/design_notes/` path (ERR-1) and the rulings-register byte-identity reconciliation (ERR-2) | **OPEN — housekeeping, resolved at freeze.** New in v2; see §6.4. |
| **OL-11** | Pre-registered statement of the paper's qualitative conclusion, to make M-6 decidable (C-13) | **OPEN — BLOCKING before execution.** New in v2. |

---

## 6. PATH-B RECONCILIATION

I-6 is a binding contract on this mission. This section maps it clause by clause onto the design so that compliance is verifiable rather than asserted.

### 6.1 The I-6 §4 robustness contract, clause by clause

| I-6 §4 clause | where satisfied | verdict |
|---|---|---|
| "use the existing LOC4 grouping definition" | §1.1 — the four-category task-group collapse of I-3 §6 (routine-manual / nonroutine-manual / routine-cognitive / nonroutine-cognitive); no alternative grouping is constructed or searched | **SATISFIED** |
| "change only the pre-registered wage-density component" | §1.3 — the only functional-form change is `μ_i(X) → μ_i(X) + δ_occ(k)` inside `O^W`. §1.6 enumerates everything else as frozen. G-L4-3/4/5 verify that the change has not leaked into the proposal, geometry or support | **SATISFIED at the level of model form**; see §6.2 for the coefficient question |
| "preserve the sample" | §1.6 — N = 1,555, France 2016 singles, 101 alternatives/hh, successor_v2 pins re-hashed fail-closed | **SATISFIED** |
| "preserve the utility specification" | §1.6 — leisure/preference block form frozen; §6.2 for coefficients | **SATISFIED** |
| "preserve the access index" | §1.6 — `O^E` form frozen (`β_E`, `β_pt1`, `β_pt2`, `β_ft`, `β_gsur`, `β_E_educH`); `O^Occ` form frozen | **SATISFIED** |
| "preserve the tax-benefit mapping" | §1.6 and **G-L4-6** — `ils_dispy`, FR 2015–2017, `drgn1` bitwise frozen, with occupation-invariance an explicit gate whose failure halts the mission | **SATISFIED, conditional on OL-6** |
| "preserve the welfare metric, inequality index and decomposition rule" | §1.6; §0.1 measure roles unchanged; the decomposition architecture and its coalition structure untouched | **SATISFIED** |
| "document whether mean and/or dispersion changes are introduced" | §1.3 **[v2 amendment]** — **mean (location) only; σ shared across `k`; no dispersion change.** Documented pre-execution | **SATISFIED** |
| "prevent double counting between occupation-access coefficients and wage-density shifts" | §6.3 | **ANSWERED** — see below |
| "compare the same headline welfare and decomposition outputs" | §3.7 — the comparison is on W1 (PRIMARY) with W3 as validation; identical functionals on both arms, evaluated through the same code paths on the same nodes under CRN | **SATISFIED** |

**The four prohibited additions of I-6 §4, each explicitly absent:**

| prohibited addition | status in this design |
|---|---|
| **sex-specific occupation densities** | **ABSENT.** `δ_occ` is gender-pooled, `K = 3`. This is not a preference: v1's `K = 6` alternative is **foreclosed** by this clause (§1.3 [v2 amendment]), and SA-1 is reduced to a reporting obligation. |
| **industry** | **ABSENT.** No `lindi`, no NACE, no industry variable enters any block. I-3 §6's naming rule is observed throughout: the layer is **occupation opportunity**, never sector opportunity. I-6 §6 defers `lindi`; this mission does not touch it. |
| **external regional covariates** | **ABSENT.** No regional covariate is added anywhere. `β_gsur` and the `drgn*` coding are **carried unchanged** from the certified access block — carrying an existing coefficient is not adding a covariate. The `M2` region-opportunity axis of I-3 §19 is untouched. |
| **alternative grouping searches** | **ABSENT.** One grouping, fixed ex ante, reference category fixed at `k = 1`. No search, no selection, no comparison of groupings. I-6 §7's "parsimonious two-group LOC4 comparison" is classified *useful later* and is explicitly **not** authorised by this mission (§4.4). |

### 6.2 The re-estimation reconciliation (I-6 §3 versus §4) — C-11

**The apparent conflict.** I-6 §3 says "No parameter is re-estimated inside the welfare mission." §2.1 of this design mandates full re-estimation of `47 + K`.

**The reconciliation.** I-6 §3 is headed **"Frozen baseline"** and governs **"the first welfare prototype"** — the M08 baseline mission, in which the certified parameters are consumed, not produced. That mission is complete and closed. I-6 §4 governs a **different** mission — "the first robustness after a successful baseline welfare prototype" — whose defining act is to "change only the pre-registered wage-density component." A wage-density component cannot be *changed* without estimating the coordinates of the changed density; a `δ_occ` that is not estimated is not a four-density model. The sequencing at I-6 §6 confirms the two are distinct steps (item 2: baseline welfare prototype; item 3: first robustness mission).

**The operative distinction is form versus coefficients.** I-6 §4's preservation list — sample, utility specification, access index, tax-benefit mapping, welfare metric, inequality index, decomposition rule — is a list of **specifications and mappings**, i.e. functional forms and fixed objects. It is not a list of fitted numerals. Preserving "the utility specification" means the utility function's form is unchanged; it cannot mean the fitted preference coefficients are frozen while the wage block moves, because a partially-frozen refit is not a maximum-likelihood estimate of anything and would produce a vector that is neither the baseline nor a converged LOC4 optimum.

**Recorded as an incoherence risk, not resolved by fiat.** This reading is stated openly as **C-11**. If the deputy reads I-6 §3 as binding on the robustness mission as well, then **LOC4 as specified is not executable**, and that is a **return** — not something to be worked around by profiling, pinning, or a two-step. This memo does not assume its own reading is correct; it names the ambiguity and states the consequence of the alternative reading.

### 6.3 The double-counting clause, answered

**The clause:** "prevent double counting between occupation-access coefficients and wage-density shifts" (I-6 §4).

**The answer is an identification argument, not a restriction.** Occupation enters the model through two economically distinct channels:

- **`β_occ_k` — occupation as *availability*.** In the access block `O^Occ`, `β_occ_k` shifts how much of occupation `k` is *offered*: it raises or lowers the mass of occupation-`k` job packages in the opportunity set, **uniformly in the wage**. It answers: how many such jobs are there?
- **`δ_occ(k)` — occupation as *price*.** In the wage block `O^W`, `δ_occ(k)` shifts *where the wage distribution sits within* occupation `k`, and its effect on the log-density is **not uniform in the wage**. It answers: what do such jobs pay?

Double counting would occur if the two coordinates moved the same object. They do not, and the algebra of §1.4 shows exactly why:

```
Δ log f_W  =  δ_occ(k)·( log w − μ_i ) / σ²   −   δ_occ(k)² / (2σ²)
```

The **constant term** — the part of `δ_occ` that would double-count `β_occ_k` — is **perfectly collinear with `β_occ_k` and is absorbed by it**. It is not double-counted; it is *assigned*, unambiguously, to the access channel. What remains, and what identifies `δ_occ`, is the **`w`-interaction**: within occupation `k`, high-wage and low-wage alternatives receive different index adjustments. `β_occ_k` cannot produce that pattern, because it is constant in `w`.

**The separating variation is therefore within-occupation wage variation, and only that.** This is the precise sense in which the two channels are separately identified, and it is why the design does **not** need to pin, drop, or restrict `β_occ_k` to satisfy the clause: the collinear direction is already assigned by construction.

**Verification, not assertion.** **G-L4-8** measures the realised separation: the fitted correlation structure between the `δ_occ` and `β_occ_k` coordinates, and each coordinate's bound-hit status, are reported. **Near-degeneracy is a reported finding (C-4), not a trigger for re-parameterisation.** Pinning `β_occ_k` to force separation would silently change the estimand and make the LOC4 arm non-comparable to the baseline — which would fail the rider's estimand-comparability gate and void every difference verdict. The honest response to a degenerate fit is to report it; the dishonest response is to constrain it away.

**Also relevant, and stated so it is not mistaken for evasion:** shared σ (§1.3) is part of the answer. Occupation-specific `σ_k` would introduce a *second* occupation-indexed channel in the wage block, and the clean assignment above would no longer hold. Excluding dispersion is not only I-6-compliant scoping; it is what keeps the double-counting answer valid.

### 6.4 Errata recorded

| id | erratum | correction |
|---|---|---|
| **ERR-1** | **Stale path in the Phase-5 memo.** The Phase-5 memo cites the LOC4 Path-B ruling at a `docs/design_notes/` path. That path is stale: the ruling of record is the located file `JMP_LOC4_pathB_ruling_v1.md`. | The citation is corrected to the located file. **Note additionally:** the located ruling carries **no `Target repository path` field of its own**, so its canonical repository location must be pinned at freeze rather than inferred. Recorded under **OL-10**; a citation is not authoritative until the path is pinned. |
| **ERR-2** | **Rulings-register byte-identity note.** The rulings register carries a byte-identity note for this ruling. No sha256 accompanied the attachment supplied to this mission, so byte-identity between the register's referent and the located file **has not been reconciled here**. | The sha256 of `JMP_LOC4_pathB_ruling_v1.md` is computed and reconciled against the register's byte-identity note **at freeze**, before v2 is committed. Per standing practice, every card returning a file for review emits that file's sha256 in the same message, reconciled before certifying. Until reconciled, §6's clause-by-clause map is **read from the attached text**, which is what this memo cites, and the register reconciliation is an outstanding control — recorded under **OL-10**. |

Neither erratum changes any substantive clause of §6.1–§6.3: the reconciliation is against the ruling's text, which is in hand. They are custody defects, recorded rather than absorbed.

---

## OUTPUT DISCIPLINE

**Mission ID:** JMP-M08 · LOC4 four-density robustness (design v2).

**Authoritative inputs:** I-1 … I-7 as tabled, with sha256 pins carried in-line where the instruments carry them. Governing revision authority: deputy **Part B**, Goal-1 **R-144.1**.

**Decisions made in v2 (beyond v1's, which are carried):** R-a adopted — all denominators are fixed baseline-arm constants and the LOC4 arm never enlarges its own tolerance (§3.1); differences constructed directly and blockwise as `Δ_T,b = T_LOC4,b − T_BASE,b`, with `E_Δ` estimated **on those differences** and never from the arms' bands (§3.2); a two-layer system separating **difference precision** from **substantive materiality**, with the Part B formulas transcribed and no cutoff invented for component levels or for non-opportunity normalized contributions (§3.3–§3.4); `MATERIAL` / `IMMATERIAL` / `INDETERMINATE_MC` per the `|Δ̂| ∓ E_Δ` rule, applied also to baseline-relative ratios (§4.1); **the arm-precision rider adopted verbatim, superseding and withdrawing v1's blanket C-3 rider** (§4.2); `K = 3` gender-pooled mandated by I-6 §4 rather than left as a fork (§1.3); mean-only, no dispersion change, documented as I-6 §4 requires (§1.3); the double-counting clause answered by the availability-versus-price identification argument with G-L4-8 as verification and near-degeneracy as a reported finding (§6.3); measure roles and the estimator of record stated explicitly with the A5-i/A5-ii inheritance and the C-8 re-run dependency unchanged (§0).

**Unresolved decisions:** OL-2 (bound `B`, at freeze); **OL-3** (four-leg definitions — BLOCKING); **OL-5** (`Z` closed form — BLOCKING before pricing); **OL-6** (EUROMOD occupation-invariance — BLOCKING, and under the rider it now gates *every* difference verdict); OL-7 (CV1 disposition dependency); OL-8 (replicate index); OL-9 (`IQR_W1_baseline`); OL-10 (errata pins); **OL-11** (pre-registered qualitative conclusion, to make M-6 decidable — BLOCKING before execution). Closed in v2: **OL-1**, **OL-4**.

**Exact output filename:** `docs/Missions/JMP_M08_LOC4_robustness_design_v2.md`
**Preserved history:** `docs/Missions/JMP_M08_LOC4_robustness_design_v1.md`, immutable.

**Status:** PROPOSED-PENDING-INDEPENDENT-REVIEW.

**Next authorised action:** commission **one bounded independent economics/numerical review of v2**, per the deputy's LOC4 Design Revision clause. On **ACCEPT**, freeze v2 and **execute LOC4 autonomously** — subject to the blocking open items above being discharged first, since none of them is a matter of manager discretion. Return to the deputy if the review **rejects the baseline-scale convention**, if LOC4 difference precision is **indeterminate on a headline threshold**, if LOC4 **changes sign/order or the qualitative conclusion**, if **disclosure fails**, if a **package change** is required, or if the **preferred specification cannot be selected**.

**Statement.** No welfare number, decomposition number, inequality index, parameter value, priced node, re-estimation, new draw, or EUROMOD execution was produced. Every numeral above is transcribed from a named record with a citation; every threshold is transcribed from deputy Part B or from Path-B §5 with both instruments cited; **no threshold, cutoff, bound, denominator or tolerance was invented**; and every gap in the record is named as an open item rather than filled.