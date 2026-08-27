# JMP-M08 — LOC4 FOUR-DENSITY ROBUSTNESS: DESIGN MEMO v4

**Mission ID:** JMP-M08 · LOC4 (pre-registered first robustness axis)
**Class:** Design memo. **PROPOSED-PENDING-FREEZE** (second narrow corrective revision of an otherwise accepted design).
**Target repository path:** `docs/Missions/JMP_M08_LOC4_robustness_design_v4.md`
**Date:** 2026-08-26
**Supersedes:** `JMP_M08_LOC4_robustness_design_v3.md` as the binding design. **v3 is preserved as history**, immutable; `..._v2.md` and `..._v1.md` remain preserved beneath it.
**Authorising instruments:** Goal-1 **R-146.2**, over the re-review of v3; Goal-1 **R-145.2**; deputy **Part B — LOC4 Materiality and MC Precision**; deputy **LOC4 Ruling v1 — Path B**.

**Re-review disposition.** The re-review of v3 **CURED** mandated items 3 (the transcribed `E_Δ` estimator), 4 (the corrected C-8), 5 (the strengthened G-L4-8) and 6 (the frozen `δ_occ` bound), and **A1 disclosure 1**. **Exactly three residual corrections** remain and are implemented here. Everything else — R-a, the difference instrument, the arm-precision rider, the Path-B reconciliation, the estimation architecture, the M-5 indicator algebra and its frozen sign convention — stands unchanged.

**Revision register — v3 → v4 delta list.** Changes are confined to exactly the following locations:

| # | location | change |
|---|---|---|
| 1 | **§3.5.4** | Replaced in full. The M-5 accepted-replicate universe is **`T16` plus the four `T12_-b`** leave-one-superblock-out replicates. The six `T8_ab` bases are **removed from M-5**. The v3 "no principled ground to exclude" construction is **deleted** and replaced by the **transcription ground**, with the record field cited verbatim. |
| 2 | **§3.5.5, §3.7, §4.1, §4.3, §4.4, §4.5, C-9, C-15, Output Discipline** | Propagation of the `T8` deletion **from M-5 only**, wherever the M-5 replicate universe is named. |
| 3 | **§3.6, partial-CRN row** | **A1 disclosure 2**: one sentence replaced verbatim. The diagnostic/return consequence is unchanged. |
| — | header block and this revision register | updated |

**Assertion.** **No other section moved.** §0, §1 (including §1.5's frozen bound), §2, §3.1, §3.2 (including the transcribed `E_Δ` estimator and **`T8_ab`'s role inside `E_Δ`, which is untouched**), §3.3, §3.4, §3.5.1–§3.5.3, §4.2, §5.1, §5.2, §5.3, §5.4, §5.6, §6 and every coherence finding other than C-9 and C-15 are carried forward from v3 **verbatim and unchanged**.

**Authoritative inputs.** All numerals are transcribed from these with citation; nothing is recomputed except where a frozen deterministic formula is evaluated on a transcribed constant, which is marked as such (§1.5).

| # | instrument | role here |
|---|---|---|
| I-1 | `JMP_M08_welfare_input_handoff_v2.md` (FROZEN; Goal-1 R-110) | parameter source θ̂_margqh-v2; inference conventions; corrected W-4 set; frozen five-scenario S-10; the eight disclosures; the prohibited-claims list; rebinding obligations and gate order |
| I-2 | `FR_P2a_m08_u6cv1_stageA_binding_and_deputy_return_v1.md` | recorded schema of the 16x welfare stack: `q_W` family and `μ_ik`, `q_H` marginal, the frozen box, `S_i`, `n`, `n_k`, the measure-role table, the A-4 functional table, the `threshold_set_of_record` |
| I-3 | `RURO_model_spec_contract_v2_stijn_enhanced.md` | structural block definitions (§9 `O^W`, §10 `O^Occ`, §15 identification, §16–17 parameters/bounds, §18 exclusion table, §19 `M3` extension ladder) |
| I-4 | M08 prototype closure `M08_BASELINE_PROTOTYPE_LIMITED_MC_PRECISION` | headline set {W1 mean, W1 Gini, φ_A, φ_B}; the estimator of record |
| I-5 | deputy CV ruling §s10 | CRN comparison; MC error on LOC4-minus-baseline differences |
| I-6 | `JMP_LOC4_pathB_ruling_v1.md` (PATH B, binding before the welfare mission) | the LOC4 robustness contract (§4) and the quantitative materiality rule (§5) |
| I-7 | deputy **Part B — LOC4 Materiality and MC Precision** | fixed baseline denominators (R-a); direct CRN difference construction; precision/substantive two-layer system; MATERIAL / IMMATERIAL / INDETERMINATE_MC; the arm-precision rider |
| I-8 | Independent review of v2, adopted at Goal-1 R-145.2 | the six corrections and two A1 disclosures implemented in v3 |
| I-9 | **Re-review of v3, adopted at Goal-1 R-146.2** | items 3/4/5/6 and A1 disclosure 1 **CURED**; the three residual corrections implemented here |

**No computation, no code, no new draw, no welfare number, no parameter value, no EUROMOD execution is produced or implied by this memo.**

---

## 0. MEASURE ROLES AND ESTIMATOR OF RECORD

*(carried from v3 unchanged)*

### 0.1 Accepted M08 measure roles

Transcribed from I-2 §5.1:

| measure | role | reference `R(w)` construction | shares the 16x node set? | carries `q^W`? |
|---|---|---|---|---|
| **W1** | **PRIMARY** | `logsumexp_{j∈cols}(leisure_j + β_c BC(w) + opp_j) − log S_i` | **yes**, the same `cols` | **yes**, the same `corr` |
| **W3** | validation | `logsumexp_masked_{j∈cols}(u_j(w) + opp_j) − log S_i` | yes, less the O-3 drop mask | yes |
| **W4** | secondary | `leisure_term_home + β_c BC(w)` — **one alternative** | **no** — a single row | no |
| **W5** | diagnostic | `logsumexp_masked(u(w; Abar) + abar.opp) − log abar.n_alts` | **no** — the Abar household's own set | no |
| **W6** | secondary | `logsumexp(lt_univ + β_c BC(w)) − log n_j`, `w6_hours = [0, 20, 30, 35, 39, 48]`, `n_j = 6` | **no** — fixed deterministic grid | **no `opp` term at all** |

The headline comparison is a **W1** comparison; W3 is validation; W4/W6 differences are reported banded with the standing riders of I-2 §5.2 (A4-1: neither admits the CRN library; A4-2: W4's reference `core.home_idx = argmax(working == 0)` is itself a **sampled** node whose identity changes with the sub-basis).

### 0.2 Estimator of record

**Raw 16x, under `M08_BASELINE_PROTOTYPE_LIMITED_MC_PRECISION`** (I-2 §5.1, §6.1, §6.2):

```
V_actual = log [ (1 / S_i) · Σ_{j ∈ cols} exp( u^S_j + log ĝ^S_j − log q^W_j ) ]
S_i      = 1601 (T16) / 1201 (T12_-b) / 801 (T8_ab)
n = 1600 ladder nodes ;  n_k = 400 per superblock (300 base / 100 defensive) ;  4 superblocks
node 0   = the chosen alternative, deterministically prepended, at the accepted ZERO correction
```

**Inherited, unrepaired:**

- **A5-i.** `_cols_of` prepends node 0 to **every** sub-basis; `compute_measures` divides by `S_i = 1 + n`. The raw estimator of record is `Î_impl = (1/(n+1))[ y_0^det + Σ_{t=1..n} y_t ]`, not `(1/n)Σ y_t`. Repair is **outside this mission's authority** (I-2 memo C-7).
- **A5-ii.** The non-employment atom is **sampled** on the IS leg, not Rao-Blackwellised: `498,146 of 2,488,000` ladder rows are non-working, against the design working share `0.75·0.90 + 0.25·0.50 = 0.80`. The Rao-Blackwellised construction exists only on the **direct** estimator (`m08_ghat_samplers.vdir_rao_blackwell`).
- **C-8 dependency:** see §5.5. LOC4 inherits the estimator of record regardless; an upstream repair forces a re-run.

---

## 1. THE VARIANT

*(carried from v3 unchanged in its entirety)*

### 1.1 Name and object

**LOC4 four-density robustness** = the `M3` extension of I-3 §19 ("`O^W` conditional on `Occ`: occupation-specific Mincer means, shared σ"), instantiated on the **LOC4 four-category task-group collapse** of I-3 §6 (1 routine-manual, 2 nonroutine-manual, 3 routine-cognitive, 4 nonroutine-cognitive). "Four-density" is literal: the single structural wage-opportunity density becomes **four occupation-conditional wage densities sharing one σ**. This is the project's already-defined LOC4 four-density variant required by I-6 §4, using the existing LOC4 grouping definition; no alternative grouping is searched (I-6 §4, §7).

### 1.2 The baseline it perturbs

The certified structural wage block of θ̂_margqh-v2 is I-3 §9:

```
log f_W(w | X)  =  − 0.5·z²  − log σ  − log w
z               =  ( log w − μ_i(X) ) / σ
μ_i(X)          =  β_w0 + β_w_educL·educL + β_w_educH·educH
                     + β_w_pexp·pexp + β_w_pexp2·pexp²
```

**`δ_occ` is coordinate-empty in θ̂.** Occupation enters the certified model **only** through `O^Occ` (I-3 §10, §18).

Not to be confused with the *proposal*: I-2 §4 binds, from `scripts/pilot/pilot_wage_draw.py:174-188` via `m08_qw_streams.BaseComponent.factors`, that the proposal wage mean is `PW._build_log_wage_mean(educL, educH, pexp, pexp², loc4, year_tag, coef, use_year_controls)` — occupation-conditional, from the frozen pilot mincer payload, with **σ a single scalar common across occupations**. The asymmetry — occupation shifts where wages are *drawn from*, but not where the estimated model *believes* they are offered — is coherence finding **C-5** and the substantive motivation for the axis.

### 1.3 Coordinates added

```
μ_i(X, k)  =  μ_i(X)  +  δ_occ(k)  ,      k ∈ {1,2,3,4} = LOC4 ,
δ_occ(1)   ≡  0                            (reference category FIXED, routine-manual, I-3 §15.2)
σ          unchanged and SHARED across k   (I-3 §19, M3)
```

Free coordinates added: `delta_occ_2`, `delta_occ_3`, `delta_occ_4`. The vector is `47 + K`, with **`K = 3`, gender-pooled, mandatorily** — I-6 §4 forecloses sex-specific occupation densities, so `δ_occ` is gender-pooled regardless of whether the certified wage block is itself gender-split. SA-1 survives only as a reporting obligation. Evidence points to a gender-pooled wage block: I-1 §3 names `beta_w_pexp2` **unsuffixed** while every leisure coordinate carries `_sm` / `_sf`.

**I-6 §4 documentation clause discharged: mean only; dispersion not introduced.** An occupation-specific **location** is added; σ is shared across `k`. Occupation-specific `σ_k` is out of scope.

### 1.4 Identification source

**`δ_occ` is identified by within-occupation wage variation, and only by that.**

```
Δ log f_W  =  δ_occ(k)·( log w − μ_i ) / σ²   −   δ_occ(k)² / (2σ²)
                    ↑ w-dependent                    ↑ constant in w, occupation-indexed
```

The second term is **constant within occupation `k`** and **perfectly collinear with `β_occ_k`**; it is absorbed and contributes nothing identifying. What identifies `δ_occ` is the **first term**: within occupation `k`, high-wage and low-wage alternatives receive different index adjustments, a pattern `β_occ_k` cannot produce because it is constant in `w`. The identifying variation is the **within-occupation dispersion of sampled log wages, interacted with the occupation label** (N = 1,555; 101 alternatives per household).

Consequences: **(1)** shared σ is load-bearing — `σ_k` would add a second occupation-indexed channel and void the separation argument; **(2)** the I-3 §18 double-counting warning is deliberately entered and answered at §6.3, and `β_occ_k` is **not** dropped, pinned or restricted; **(3)** `δ_occ(1) ≡ 0` and the `O^Occ` reference are the same category — only contrasts are identified in both blocks.

### 1.5 Bounds — FROZEN BY EXACT FORMULA *(cured at v3; carried unchanged)*

**Derivation.** `δ_occ(k)` is a **location shift in log wage**. The recorded wage support of the priced nodes is the frozen box's closed interval

```
w ∈ [ w_min , w_max ] = [ 1.9411632533361265 , 101.91995852573758 ]     (I-2 §2(i))
```

whose **exact log-width is a recorded field of the frozen box**:

```
log_range_L = 3.9609003763945605                                        (I-2 §2(i))
```

confirmed independently at I-2 §2(v): `DefensiveComponent.log_L` recomputed from the frozen bounds equals `log_range_L` **bitwise**.

Every within-occupation log-wage support on the recorded stack is a **subset** of `[log w_min, log w_max]` — **zero off-box working ladder nodes** on every rung and in the independent re-verification (`0 off-box working ladder nodes of 1,989,854`, I-2 §2(iv)). Any two occupation-specific log-wage **locations** inside the recorded support therefore differ by **at most `log_range_L`**.

**The frozen formula.**

```
B  =  ceil( log_range_L )  =  ceil( 3.9609003763945605 )  =  4.0

δ_occ(k) ∈ [ −4.0 , +4.0 ]   for k ∈ {2,3,4} ;   δ_occ(1) ≡ 0
```

**The numerical slack is exactly `B − log_range_L = ceil(log_range_L) − log_range_L`** — deterministic, fixed by the same formula, not a judgement and not a range. Ceiling to the next integer in log points is the entire slack rule; no further margin is added and none may be added at execution.

**Properties.** `B` is (i) **deterministic** — a total function of one recorded, bitwise-verified frozen-box field; (ii) **fixed before estimation**, recorded here; (iii) **guaranteed non-binding on any economically admissible value**, admitting occupational wage-location ratios up to `e^4`; and (iv) **compact**, satisfying I-3 §17's bound-hit-diagnostic requirement and the four-leg standard. A bound-hit under this `B` is unambiguously diagnostic of a fit pathology, never an artefact of a tight box.

**Rejected alternatives:** `B = log_range_L` exactly (a location at the support edge would sit *on* the bound and produce a spurious bound-hit); `B` tied to `σ̂` (makes the box a function of the block being perturbed); `B` from a sample statistic of within-occupation wage means (not deterministic from the frozen record); unbounded `δ_occ` (I-3 §17).

A `δ_occ` coordinate active at `±4.0` is treated exactly as `beta_l_age2_sm` / `beta_l_age2_sf` at I-1 §2.1 — excluded from the covariance by construction, SE/z/p **literal NA** — and, per §5.3, read jointly with the strengthened G-L4-8.

### 1.6 What does NOT change — exhaustive

| object | status under LOC4 | source |
|---|---|---|
| Leisure / preference block | form frozen; coordinates re-estimated | I-3 §16 |
| Access block `O^E` (`β_E`, `β_pt1`, `β_pt2`, `β_ft`, `β_gsur`, `β_E_educH`) | form frozen; coordinates re-estimated | I-3 §8, §16 |
| `O^Occ` block (`β_occ_k`) | form frozen; coordinates re-estimated; **not pinned** | I-3 §10; §1.4(2) |
| Hours bands / `q_H` marginal (PT1 .15, PT2 .10, F35 .24, FT .20, LH .10, BG .21; 9-piece partition) | **bitwise frozen** | I-2 §3 |
| Employment margin (`π0 = 0.10`, `π0_r = 0.50`; design working share `0.80`) | **bitwise frozen** | I-2 §4 |
| Defensive mixture `λ = 0.25`; log-uniform `r_W`; uniform `r_Occ` over 4; uniform `r_H` | **bitwise frozen** | I-2 §2(i), §4 |
| Job-space geometry: `n = 1600`, `n_k = 400`, `S_i = 1601 / 1201 / 801`, node 0, 4 superblocks | **bitwise frozen** | I-2 §5.1, §6.1, §6.2 |
| Proposal convention (`log_q_H`, `log_prior`, `prior`) | **bitwise frozen** | I-1 §1.2 |
| Pilot mincer payload and `q^W` | **bitwise frozen** | I-2 §4 |
| EUROMOD / tax-benefit mapping (`ils_dispy`, FR 2015–2017, `drgn1`) | **bitwise frozen**, conditional on **G-L4-6** | I-3 §14.3; I-6 §4 |
| Welfare metric, inequality index, decomposition rule | **bitwise frozen** | I-6 §4 |
| Estimation sample and draw geometry (N = 1,555; 101 alternatives/hh; successor_v2 pins) | **bitwise frozen**, re-hashed fail-closed | I-1 §1.2 |
| Scope: singles P2a only; no couples, no pooled years, no `dclaborsupply` change (gitlink `27756a06`) | unchanged | I-1 §6.6 |

---

## 2. ESTIMATION PLAN

*(carried from v3 unchanged)*

### 2.1 What is estimated

**Full re-estimation of the entire `47 + K` vector** under the corrected marginal/MIS proposal convention, on the successor_v2 frame, from the same 101-alternative draws. Not a profiled fit, not a two-step, not a warm-started perturbation of the certified block only: every preference, access, hours, wage and occupation coordinate is free simultaneously, because `δ_occ` is not separable from `β_occ_k` or from the leisure block by construction (§1.4).

The 10 pinned coordinates stay pinned. The two upper-bound-active leisure coordinates are **not** pre-set: they are freed and allowed to re-locate, and whether they remain active at `+1.0` is a reported diagnostic.

**Prohibited:** any evaluated vector mixing θ̂_margqh-v2 coordinates with LOC4 coordinates other than as a documented warm start whose end point is a converged optimum in its own right. The suspended joint-convention estimate (`c024b893…f0580d`) is **never** a parameter source, warm start, or robustness arm (I-1 §1.3).

Reconciliation with I-6 §3 is at §6.2.

### 2.2 Convergence standard

The **amended four-leg convergence standard** applies unchanged in form, with the **deputy convergence-class rule governing leg (c)**. The legs' definitions are **not transcribable from this mission's attachment set** — `FR_P2a_m08e_E3_reestimation_note_v2.md` (sha256 `970eda4c0d3dcc140b1608159c64fff420eb8395964e2e3b34f500c1a660a5f5`), `convergence_records.json` (sha256 `9cf81c03e3e7e0ec58d87582f9454d5b076b53bccfe8d3154188878db926b50e`). Entered as **NA-on-this-record**; mandatory transcription at freeze — **OL-3**. Fixed now: the standard applies **in full**, no relaxation for the higher parameter count; leg (c) is adjudicated by the **deputy convergence-class rule** (a class is assigned and reported); the target is the analogue of `E3-CONVERGED-SINGLE-OPTIMUM`, and **a LOC4 fit that does not attain a single-optimum verdict is a return, not a headline**.

### 2.3 Inference

Per Phase-4/5 conventions (I-1 §2), on the new free set: household-cluster **CR1**, `G = N = 1,555`; finite-sample factor `c = 1555/(1555 − K_free)` — **`K_free` changes, so `c` changes**, and the certified `1555/1520 = 1.0230263157894737` may **not** be carried across; covariance dimension = the LOC4 interior set (certified 35 interior, plus interior members of `δ_occ`, less any bound-active coordinate, excluded by construction and reported literal NA). Disclosure 7 and the prohibited-claims list bind LOC4 output as they bind baseline output: **`δ_occ` may not be described as a causal occupational wage premium**, and baseline-versus-LOC4 coefficient changes may not be described as statistically significant differences.

### 2.4 W-4 diagnostic and the S-10 rule

Certified flagged set: **{ `beta_l0_sm`, `beta_l0_sf`, `beta_l_nkids_sf` }** (I-1 §2.2).

> **No S-10 re-derivation unless the flagged set changes.** Identical membership ⇒ the frozen five-scenario design of I-1 §3 is **not reopened** and **no S-10 battery is run on the LOC4 arm**. Changed membership (including a newly-flagged `δ_occ` coordinate) ⇒ **a return, not an autonomous re-derivation**.

Differences are taken at **scenario 1 on the baseline arm and θ̂^LOC4 on the LOC4 arm**. S-10 on the LOC4 arm is triggered only in Branch B (§4.4), under deputy disposition. The standing S-10 disclosure applies: Tier-1 deterministic sensitivity; not a confidence region, bootstrap or posterior; it does not produce welfare confidence intervals.

---

## 3. THE COMPARISON DESIGN

### 3.1 Governing convention: fixed baseline denominators (R-a) — *carried unchanged*

> **Adopt R-a: use the BASELINE ARM as the fixed scale. Do not allow the LOC4 result to enlarge its own precision tolerance.** (I-7)

Every denominator in §3.3–§3.4 is a **baseline-arm constant**, transcribed once, pinned pre-execution, held fixed for the whole mission. No denominator reads the LOC4 arm.

### 3.2 Direct blockwise CRN differences, and the exact `E_Δ` estimator — *cured at v3; carried unchanged, including `T8_ab`'s role*

> For every functional, compute the common-random-number difference directly:
> `Delta_T_b = T_LOC4_b − T_BASE_b`
> Estimate `E_Delta` directly from the blockwise differences. **Do not add the two arm-level error bands.** (I-7)

**3.2.1 The paired-difference bases.** The accepted block structure is 4 superblocks (`n_k = 400`, 300 base / 100 defensive, `400 ≡ 0 (mod 4)`, realised defensive fraction exactly `0.25` in every `D_k`), generating the full basis `T16`, the **four** leave-one-out bases `T12_-b` (b = 1…4) and the **six** pair bases `T8_ab` (a<b, the `C(4,2)` pairs), confirmed by the recorded alternative counts `S_i = 1601 / 1201 / 801` (I-2 §5.1, §6.1).

For every functional `T`, the paired difference is formed **on each basis, within basis**:

```
Δ_T16      =  T_LOC4( T16 )      −  T_BASE( T16 )
Δ_T12_-b   =  T_LOC4( T12_-b )   −  T_BASE( T12_-b )       b = 1…4
Δ_T8_ab    =  T_LOC4( T8_ab )    −  T_BASE( T8_ab )        the six pairs
```

**3.2.2 The error functional — transcribed, not constructed.** `E_Δ` is the **same error functional as the accepted arm-level `E_T`**, applied to the paired differences. Source field: `…_u6ffn16_U6F_FUNCTIONALS16_DONE/u6f_functionals16_v1.json`, `step3_functionals`, and the `threshold_set_of_record` recorded there (transcribed at I-2 §6.4); the arm-level construction is carried over verbatim with `Δ` substituted and nothing else altered:

```
Δ_T12_bar     =  (1/4) · Σ_{b=1..4} Δ_T12_-b
SE_MC(Δ)      =  sqrt[ (3/4) · Σ_{b=1..4} ( Δ_T12_-b  −  Δ_T12_bar )² ]
Δ_T8_bar      =  (1/6) · Σ_{a<b}    Δ_T8_ab
E_Δ           =  max( | Δ_T16 − Δ_T8_bar | ,  1.96 · SE_MC(Δ) )
```

The `(3/4)` factor is the delete-one jackknife factor `(m−1)/m` at `m = 4`; `1.96` and the `max(·)` envelope are the accepted construction's own. **No constant is invented, rescaled or re-derived.** **The six `T8_ab` bases retain exactly this role — inside `E_Δ`'s `|Δ_T16 − Δ_T8_bar|` term — and v4 does not touch it.**

**3.2.3 Three prohibitions.**

1. **`E_Δ` is never formed from the arms' own bands** — not their sum, quadrature sum, or difference. **[A1 disclosure 1, as cured at v3.]** Combining arm bands **ignores the positive CRN covariance and therefore generally overstates uncertainty under the intended paired design**; the direction is not guaranteed in every case and is not assured at all in the partial-CRN regime. The prohibition stands **because the deputy instrument mandates the direct construction**, not because the direction of the error is universal.
2. **`Δ_T,b` is computed within basis** — same basis index, same nodes, both arms. Never across bases.
3. **The difference is taken on the assembled functional**, not propagated through its components.

**3.2.4 The `n/(n+1)` scale caveat.** The estimator of record normalises by `S_i = n+1` rather than `n` (§0.2, A5-i), and the resulting scale factor is **basis-dependent** — `1600/1601` at `T16`, `1200/1201` at `T12_-b`, `800/801` at `T8_ab`. The paired differences entering `E_Δ` are therefore shrunk by **slightly different deterministic factors across bases**, contaminating the `|Δ_T16 − Δ_T8_bar|` term with a deterministic component. Named as **C-16**; **not** corrected by rescaling.

### 3.3 Layer 1 — PRECISION gates on the difference *(carried unchanged)*

| class | baseline-arm scale | precision gate |
|---|---|---|
| mean | `S_k0 = max( |mean_Wk_baseline| , |median_Wk_baseline| , IQR_Wk_baseline , 1 € )` | `E_Δ,mean / S_k0 ≤ 0.0025` |
| median | same `S_k0` | `E_Δ,median / S_k0 ≤ 0.0025` |
| Gini | — (absolute) | `E_Δ,Gini ≤ 0.00125` |
| component levels (φ) | — (absolute) | `E_Δ,φ ≤ 0.00125` |
| normalized contributions | `S_r0 = max( 1 , |r0| )`, `r0` the **baseline** contribution | `E_Δ,r / S_r0 ≤ 0.005` |

**Transcribed baseline-arm constants** (I-2 §6.4):

| object | baseline `T16` | baseline arm's own `E_T` | baseline level-gate ratio |
|---|---|---|---|
| `W1_mean` | `1396.13` | `3.02142` | `0.866` (pass) |
| `W1_median` | `1340.43` | `11.5733` | `3.316` (FAIL) |
| `W1_gini` | `0.173955` | `0.000869933` | `0.696` (pass) |
| `W1_phi_A_level` | `0.00617588` | `0.000468934` | `0.375` (pass) |
| `W1_phi_B_level` | `0.0114346` | `0.00119598` | `0.957` (pass) |
| `W1_s_opp` ( ≡ `r_phi_A+phi_B` ) | `0.101236` | `0.0094323` | `1.886` (FAIL) |

`IQR_W1_baseline` is **not on this record** — **OL-9**; until transcribed, `S_k0` is known only to be **at least** `1396.13`. `S_r0` for `s_opp` resolves to the **unit floor** (`r0 = 0.101236 < 1`), so that gate is effectively absolute at `E_Δ,r ≤ 0.005`.

### 3.4 Layer 2 — SUBSTANTIVE thresholds *(carried unchanged)*

| # | criterion | threshold `m` | Part B form | Path-B source |
|---|---|---|---|---|
| M-1 | mean money-metric welfare | `0.01` | `|Δ_mean| / max(|mean_Wk_baseline|, 1 €) ≥ 0.01` | I-6 §5.3 |
| M-2 | median money-metric welfare | `0.01` | `|Δ_median| / max(|median_Wk_baseline|, 1 €) ≥ 0.01` | I-6 §5.3 |
| M-3 | welfare Gini | `0.005` | `|Δ_Gini| ≥ 0.005` | I-6 §5.2 |
| M-4 | opportunity-attributable share | `0.02` | `|Δ_s_opp| ≥ 0.02` | I-6 §5.1 |
| M-5 | **sign / ordering of a headline decomposition component** | — (binary configuration test) | **see §3.5** | I-6 §5.4 |
| M-6 | qualitative conclusion | — | the paper's qualitative conclusion about the importance of opportunity heterogeneity changes | I-6 §5.5 |

> **"Do not invent a component-level materiality cutoff. Component materiality is assessed through stable sign/order changes and the qualitative-conclusion criterion."** (I-7)
> **"Other normalized component differences are reported with bands but do not receive an invented 2pp threshold."** (I-7)

`φ_A` and `φ_B` receive the precision gate `E_Δ,φ ≤ 0.00125` and **no substantive cutoff**; their materiality runs **only** through M-5 and M-6. Likewise `φ_P`, `R_bg`, `r_phi_A`, `r_phi_B`, `r_phi_P`, `r_R_bg` and the `I_{·}` family: bands, no invented threshold, no verdict of their own.

**M-6 must be pre-registered** as a single decidable statement before execution — **OL-11**, blocking.

### 3.5 M-5 — ARM-TO-ARM CHANGE IN THE COMPONENTS' QUALITATIVE CONFIGURATION

**3.5.1 The component set.** *(unchanged)* `C = { φ_A , φ_B }` — the headline decomposition components of the accepted closure (I-4). The ordered pair set is `P = { (A, B) }`, with a fixed lexicographic operand order. `φ_P` and `R_bg` are evaluated by the same indicators and **reported as diagnostics**, not verdict-bearing; extending `C` to them would import components outside the closure's headline set and is a deputy question.

**3.5.2 The paired indicators.** *(unchanged)* For each accepted basis `b` (see §3.5.4), with `φ^{L4}_{c,b}` and `φ^{0}_{c,b}` the component levels of the LOC4 and baseline arms **on the same basis**:

```
SIGN CHANGE, per component c ∈ C :

    S_{c,b}  =  1{  sgn( φ^{L4}_{c,b} )  ≠  sgn( φ^{0}_{c,b} )  }

ORDERING CHANGE, per ordered pair (c,d) ∈ P :

    O_{cd,b} =  1{  sgn( φ^{L4}_{c,b} − φ^{L4}_{d,b} )  ≠  sgn( φ^{0}_{c,b} − φ^{0}_{d,b} )  }
```

Both indicators compare **arm to arm within a basis**. Neither reads `Δ`'s sign.

**3.5.3 The deterministic sign convention — frozen, unchanged.**

```
sgn(x)  =  +1   if  x >  0.0
        =  −1   if  x <  0.0
        =   0   if  x == 0.0     (exact IEEE-754 float64 equality; +0.0 and −0.0 both map to 0)
```

- **Three-valued, with exact zero as its own class.** A move from `0` to `+1`, or `−1` to `0`, **counts as a sign change**.
- **Exact comparison, no tolerance, no epsilon band** — matching the convention already of record for the frozen box (*"closed interval, exact float64, **no tolerance**"*, I-2 §2(i)). A near-zero tolerance would be an **invented substantive cutoff**, prohibited by I-7.
- **Ordering differences use a fixed operand order** — `φ_c − φ_d` in lexicographic label order, computed in float64 in that order, once, passed to `sgn`. An **exact tie** (`== 0.0`) is its own class, so moving into or out of an exact tie counts as an ordering change.
- **No re-ordering, re-association or re-summation of the subtraction is permitted.**

**3.5.4 The accepted-replicate family — REPLACED per residual correction 1**

**The M-5 replicate universe is the full basis `T16` plus the four leave-one-superblock-out replicates `T12_-b` (b = 1…4). The six `T8_ab` bases are NOT part of M-5.**

**The ground is transcription, not judgement.** M-5 operationalises the sign/ordering limb that already exists on the record, and that limb names its own replicate family. The `threshold_set_of_record` states it verbatim:

> **"signs and ordering identical between `T16` and every `T12` LOO"** (I-2 §6.4, `threshold_set_of_record`)

M-5's sole extension of that instrument is the one the deputy mandate requires: the comparison runs **arm to arm** (LOC4 versus baseline within a basis) rather than **basis to basis within one arm**. The replicate family is carried across **unchanged**, because it is the recorded instrument's own.

**Importing the six `T8_ab` bases into M-5 would be an unauthorised strengthening.** The record's sign/order limb does not range over `T8`; adding it would impose a unanimity requirement the accepted instrument never imposed, on the two bases with the fewest alternatives (`S_i = 801` against `1601`), and would make `INDETERMINATE_MC` returns arise from a criterion of this memo's own construction rather than from the record's. Constructing a stricter test than the instrument being transcribed is exactly the invention the ROLE and I-7 prohibit — the prohibition runs against invented strictness as much as against invented leniency.

**The v3 construction is deleted.** v3 justified including `T8_ab` on the ground that "there is no principled ground on which to exclude the sub-bases the accepted machinery already produces." That reasoning is withdrawn: the principled ground is the record field quoted above, and *"the machinery produces it"* is not a warrant for importing a basis into an instrument that does not name it.

**`T8_ab`'s role is unchanged and untouched.** The six pair bases remain **exactly where the accepted estimator uses them** — inside `E_Δ`'s `|Δ_T16 − Δ_T8_bar|` term (§3.2.2). Nothing in this correction alters the `E_Δ` formula, its inputs, or the bases it reads. M-5 and `E_Δ` are different instruments transcribed from different fields of the same record, and they legitimately read different basis families.

**3.5.5 The verdict rule.** Per indicator `I ∈ { S_c : c ∈ C } ∪ { O_cd : (c,d) ∈ P }`, over the **accepted replicate family `{ T12_-1 , T12_-2 , T12_-3 , T12_-4 }`** and the full basis `T16`:

```
I is MATERIAL                  iff   I_{T16} = 1   AND   I_b = 1  for EVERY  b ∈ { T12_-1 … T12_-4 }
I is IMMATERIAL                iff   I_{T16} = 0   AND   I_b = 0  for EVERY  b ∈ { T12_-1 … T12_-4 }
I is INDETERMINATE_MC          otherwise   (the T12 replicates disagree, or disagree with T16)
```

**M-5 aggregate:** MATERIAL if any indicator is MATERIAL; otherwise INDETERMINATE_MC if any indicator is INDETERMINATE_MC; otherwise IMMATERIAL.

**M-5 is a binary configuration test, not a magnitude test.** The `|Δ̂| ∓ E_Δ` band rule of §4.1 **does not apply to it**, and no `E_Δ` is formed for it. Its uncertainty is handled entirely by the unanimity requirement across `T16` and the four `T12_-b` — the same device, over the same replicate family, that the accepted `threshold_set_of_record` uses for its own sign/ordering limb.

### 3.6 CRN construction — where it is exact, where only partial *(A1 disclosure 2 sentence replaced per residual correction 3; all else unchanged)*

**Design intent:** `δ_occ` enters the **structural index only**. It does not enter `q^W`, the `q_H` marginal, `q_Occ`, `log_prior`, the employment margin, `λ`, or the node identities.

**Exact on the base half (75%), conditional on G-L4-1.** `q^W`'s wage mean is built from the frozen pilot mincer payload, not from θ (I-2 §4). If the base draw path reads no coordinate of θ, then across arms these are bitwise identical: `working`, `hours`, `wage`, `loc4`, `log_q_E`, `log_q_H`, `log_q_W`, `log_q_Occ`, `log_prior`, `log_q_base`, `stream_seed`, `base_position`, `component_label`, `in_support_box`, the priced consumption, node 0 and its zero correction, superblock membership, `S_i`. Verified by the bitwise-column instrument of record (I-2 §2(iii): 17 of 17 columns bitwise equal, `columns_not_bitwise: []`).

**At risk on the defensive half (25%): the frozen box.** `DefensiveComponent.draw` maps its uniforms **through** the box, so a box move regenerates every defensive node and voids the pairing on that half. The record establishes the box is evaluated at θ and **has moved before**: `box_at_theta_v2.box_moved: true`, `delta_log_L: 0.06107235168894798`, with `311000 = 1555 × 200` defensive nodes re-priced and `additional_nodes_due_to_box_move: 155500` (I-2 §2(ii)).

| branch | condition | CRN status | consequence |
|---|---|---|---|
| **CRN-exact** | box at θ̂^LOC4 bitwise equals `box_hash_sha256 = 67ef22b3742ccc04a25c377cec60e18478b6fd07e539c0340497a274c0ce2c52` / `float64_bytes_sha256 = 8e44ec2a926aa06fd844a0be97fdbfdc29d3299ca1a7b3a1eb46a7191ae6e361`; `h_min/h_max = 5.0/70.0`, `w_min/w_max = 1.9411632533361265/101.91995852573758`, `log_range_L = 3.9609003763945605` unchanged | exact on **all** nodes | the **designed experiment**; `E_Δ` per §3.2.2 is the difference band; materiality verdicts are issued |
| **CRN-partial** | box moves at θ̂^LOC4 | exact on the base 75%; **broken** on the defensive 25% | **[A1 disclosure 2] This is a DIAGNOSTIC REGIME, not the same experiment. "A partial-CRN run may target the same LOC4-minus-baseline functional difference, but it does not implement the pre-registered fully paired precision experiment: the defensive quarter loses CRN covariance cancellation, so its resulting band is not the designed full-CRN difference band."** All outputs are **labelled diagnostic**; `E_Δ` may not be presented as a CRN difference band; **no materiality verdict is issued from a partial-CRN run without deputy disposition** — it is a return |
| **halt** | box moves **and** re-pricing is required | — | EUROMOD re-pricing at the recorded scope (155,500 per defensive half; 311,000 across both) is a cost and custody event, disclosed with the pairing loss |

**No CRN repair is attempted.** Re-seeding, re-mapping, or reusing pre-move defensive uniforms to manufacture pairing is prohibited: pre-rebind defensive nodes do not survive anywhere in the stack (I-2 §2(ii)).

**What CRN does not buy.** Both arms are evaluated at their **own full re-estimated vectors**. CRN pairs the *randomness*, not the *parameters*. `Δ` is the effect of the **specification change as a whole**, not the partial effect of the `δ_occ` term (**C-7**).

### 3.7 Reporting order *(M-5 replicate family propagated)*

**Tier 1 — the two-layer battery:** `W1_mean` (M-1), `W1_median` (M-2), `W1_gini` (M-3), `W1_s_opp` (M-4), each with its §3.3 precision gate and §4.1 band rule; **M-5 on the arm-to-arm configuration of `φ_A` and `φ_B`** per §3.5, reported as the indicator table `{ S_A , S_B , O_AB }` × **`{ T16 , T12_-1 , T12_-2 , T12_-3 , T12_-4 }`** with the per-indicator verdict; and M-6 against the pre-registered statement.

**Tier 2 — bands, no materiality verdict:** all other normalized contributions, the `I_{·}` family, `φ_P` and `R_bg` (including their diagnostic `S`/`O` indicators, reported over the same `T16` + four `T12_-b` family), and the W3 validation comparison. W4 and W6 differences are reported banded with the I-2 §5.2 riders (A4-1, A4-2).

Every reported object is a **difference** or an **arm-to-arm indicator**. Arm levels appear only as the fixed denominators of §3.1 and as banded standalone magnitudes under the rider of §4.2.

---

## 4. THE DECISION TREE

### 4.1 The classification rule *(M-5 carve-out and replicate family propagated)*

For a magnitude criterion with threshold `m` and its `Δ̂`, `E_Δ`:

```
LOC4_MATERIAL                        when   |Δ̂| − E_Δ  ≥  m
LOC4_IMMATERIAL                      when   |Δ̂| + E_Δ  <  m
LOC4_MATERIALITY_INDETERMINATE_MC    otherwise
```

> **"Apply the same rule to baseline-relative mean/median ratios."** (I-7)

For M-1 and M-2 the tested object is the **ratio**; since its denominator is a fixed baseline constant, the rule transfers exactly, with `Δ̂` and `E_Δ` both divided by `max(|mean_Wk_baseline|, 1 €)` (resp. median) before comparison to `m = 0.01`.

**The band rule governs M-1, M-2, M-3 and M-4 only.** **M-5 is a binary configuration test classified by the unanimity rule of §3.5.5 over `T16` and the four `T12_-b`**; no `E_Δ` is formed for it. **M-6** is a pre-registered qualitative determination (OL-11) and carries no band.

**`LOC4_MATERIALITY_INDETERMINATE_MC` is a return.** It is a **verdict**, not a state to be resolved by re-running until it resolves. Prohibited without deputy disposition: extending the ladder beyond 16x to shrink `E_Δ`; re-drawing; re-seeding; dropping an object from Tier 1; substituting a Tier-2 object for a Tier-1 one; re-reading a functional's threshold class; **widening the sign convention of §3.5.3 with a tolerance to force M-5 unanimity; or altering M-5's replicate family in either direction — neither adding the `T8_ab` bases nor dropping any `T12_-b` replicate.**

**Aggregation**, per I-6 §5 ("materially different if **any one** occurs"):

- **LOC4 IMMATERIAL overall** iff M-1…M-4 each return `LOC4_IMMATERIAL`, **M-5 returns IMMATERIAL** per §3.5.5, and M-6 records no change.
- **LOC4 MATERIAL overall** iff **any** of M-1…M-4 returns `LOC4_MATERIAL`, **or M-5 returns MATERIAL**, or M-6 records a change.
- **Return** if **any** of M-1…M-4 returns `LOC4_MATERIALITY_INDETERMINATE_MC`, **or M-5 returns INDETERMINATE_MC**, or the run is in the partial-CRN diagnostic regime (§3.6), or the strengthened G-L4-8 blocks (§5.3).

### 4.2 THE ARM-PRECISION RIDER *(carried unchanged)*

> **"Do not adopt the proposed rule that either arm's standalone level-precision failure automatically removes the LOC4 materiality verdict. A standalone arm that fails its level gate remains banded and cannot be promoted as a standalone magnitude.**
> **But a LOC4-minus-baseline materiality verdict is permitted when:**
>
> * **both arms pass validity, support, reference and estimand-comparability gates; and**
> * **the direct CRN difference passes its own precision gate.**
>
> **If the direct difference fails precision, report it as uncertified and make no materiality verdict.**
> **If either arm fails validity, support, reference or estimand comparability, no difference verdict is permitted."** (I-7)

This **supersedes and withdraws** v1's blanket rule. Level precision (one arm's standalone magnitude) and difference precision (the paired CRN difference) are separate; only the latter gates the verdict.

| object | baseline level gate | v1 treatment (WITHDRAWN) | treatment under the rider |
|---|---|---|---|
| `W1_s_opp` | **FAIL** (`1.886`) | no verdict permitted | **verdict-eligible on M-4**, given the arm gates and `E_Δ,r / S_r0 ≤ 0.005`. The **level** `0.101236` remains **banded and non-promotable** |
| `W1_median` | **FAIL** (`3.316`) | banded | **verdict-eligible on M-2** under the same conditions; the level remains banded |
| `W1_mean`, `W1_gini`, `φ_A`, `φ_B` | pass | headline | unchanged; passing a level gate does **not** license a difference verdict |

**The arm gates that block a difference verdict** are **G-L4-3**, **G-L4-4**, **G-L4-5**, **G-L4-6**, **G-L4-7**. Failure in any ⇒ **no difference verdict at all, for any functional**.

### 4.3 Branch A — LOC4 IMMATERIAL

**Condition:** M-1…M-4 each `LOC4_IMMATERIAL`; **M-5 IMMATERIAL — i.e. `S_A = S_B = O_AB = 0` in the full basis `T16` and in every one of the four `T12_-b` replicates**; M-6 no change against the pre-registered statement (OL-11); the run is in the full-CRN regime; G-L4-8 does not block.

**Verdict:** **retain the certified baseline as the preferred specification and report LOC4 as robustness** (I-6 §5).

**Pipeline consequences:**

- **Rebinds:** nothing. No welfare artifact, `q^W` object, `Z`, `ĝ` sampler, coalition target or pricing ladder rebinds.
- **Re-runs:** nothing.
- **Stays frozen:** θ̂_margqh-v2 as sole parameter source; the frozen box; the five-scenario S-10 set; the 16x stack; the prototype closure and its headline set.
- **New obligation:** a **disclosure** in every manuscript, notebook, table, figure and memo carrying a decomposition number — that the wage block was tested against the LOC4 occupation-conditional four-density extension and the headline objects were immaterially affected — reported with `Δ̂`, `E_Δ`, **the M-5 indicator table over `T16` and the four `T12_-b`**, the classification per criterion, and the CRN regime. The disclosure must state that the axis tests **occupation-conditional wage location only**: not dispersion (`σ_k`), not occupation-conditional hours (`O^H | Occ`, `M4`), not regional opportunity (`M2`), not industry (`lindi`, deferred at I-6 §6). Immateriality on this axis is not immateriality on the occupation dimension.
- **I-6's mandatory-before-final-claims status is discharged for this axis**; I-6 §6.4's sequencing is satisfied and preferred quantitative welfare results may be frozen.

### 4.4 Branch B — LOC4 MATERIAL

**Condition:** any of M-1…M-4 returns `LOC4_MATERIAL`, **or M-5 returns MATERIAL** (the full-basis comparison exhibits a sign or ordering change between arms *and* every one of the four `T12_-b` replicates exhibits that same change), or M-6 records a change.

**Verdict:** **the preferred specification must be reconsidered before final paper-facing quantitative claims** (I-6 §5). The manager selects neither arm on its own authority. **This is a return**, under two independent deputy triggers.

**Pipeline consequences:**

- **Nothing rebinds pending disposition.** The pipeline is **held**, not switched. θ̂_margqh-v2 remains the parameter source of record.
- **Stays frozen:** everything. The M08 prototype closure is not withdrawn.
- **The return packet carries:** the LOC4 convergence class and four-leg result; the `47 + K` parameter table with CR1 SEs on the recomputed `c`; the W-4 flagged membership; per-criterion `Δ̂`, `E_Δ` and classification; **the full M-5 indicator table across `T16` and the four `T12_-b`**; the CRN regime with the box-hash comparison; the strengthened G-L4-8 evidence (curvature, rank, conditioning of the extended `(β_Occ, δ_occ)` block); and every coherence finding of §5.5 that fired.
- **If and only if the deputy promotes LOC4**, the full rebinding cascade of I-1 §6 executes in its stated order — rebinding → deterministic + N-test batteries (N1–N9, in full, **before any pricing**) → U6 → pricing ladder → welfare → decomposition → S-10 → LOC4 — with S-10 re-derived under a deputy-approved revision register, and the RUM benchmark re-estimating its own preferences under the promoted specification (`g ≡ 1` with a retained θ̂ remains forbidden).
- **If baseline is retained**, Branch A's disclosure applies **strengthened**: it must report that the axis produced a material difference and that baseline was retained by ruling, with the LOC4 numbers shown.
- **I-6 §7** classifies "a parsimonious two-group LOC4 comparison" as *useful later*; it is **not** authorised by a material verdict.

### 4.5 Branch C — LOC4_MATERIALITY_INDETERMINATE_MC

**Condition:** any of M-1…M-4 falls in the `otherwise` band; **or M-5 returns INDETERMINATE_MC — the four `T12_-b` replicates disagree with each other or with `T16` on any indicator**; or the direct difference fails its own precision gate (the object is **reported as uncertified with no materiality verdict**, per the rider); or an arm fails validity/support/reference/comparability (**no difference verdict is permitted at all**); or the run is in the **partial-CRN diagnostic regime** (§3.6); or the LOC4 fit does not attain a single-optimum convergence verdict (§2.2); or **G-L4-8 blocks** (§5.3).

**Verdict:** **return.**

**Pipeline consequences:** nothing rebinds; nothing is re-run to break the tie on manager authority; the §4.1 prohibitions apply — including, explicitly, that an M-5 disagreement is **not** resolved by introducing a tolerance into the sign convention, **nor by adding or removing replicates from M-5's family**. The return states which limb was indeterminate and why, and — where the cause is precision rather than substance — carries the cost estimate of the extension that would resolve it. Indeterminacy traceable to the `LIMITED_MC_PRECISION` closure is an expected outcome of that closure, not a failure of this mission.

---

## 5. FROZEN vs STAGE-A-BOUND; GATES; OPEN ITEMS; COHERENCE

### 5.1 Frozen by this design *(carried unchanged; M-5's replicate family now part of what is frozen)*

The variant's functional form (§1.3); **the `δ_occ` bound `B = ceil(log_range_L) = 4.0` and its exact slack rule (§1.5)**; the exhaustive no-change list (§1.6); full simultaneous re-estimation with `β_occ_k` free (§2.1); the four-leg standard without relaxation (§2.2); the no-S-10-without-membership-change rule (§2.4); fixed baseline denominators, R-a (§3.1); **direct blockwise CRN differences with the transcribed `E_Δ` error functional, including its use of the six `T8_ab` bases (§3.2.2)**; the two-layer precision/substantive system with no invented cutoffs (§3.3–§3.4); **the M-5 arm-to-arm configuration test with its exact sign convention and its transcribed `T16` + four `T12_-b` replicate family (§3.5)**; the MATERIAL/IMMATERIAL/INDETERMINATE_MC rule with the M-5 carve-out (§4.1); the arm-precision rider (§4.2); the three-branch tree with a **held** pipeline in Branches B and C; the no-CRN-repair rule and the partial-CRN diagnostic marking (§3.6).

### 5.2 Stage-A-bound at execution *(carried unchanged)*

| id | item | bound from | status |
|---|---|---|---|
| SA-1 | Gender convention of the certified wage block | `e4_parameter_table.csv` `21a05fb5…` | reporting obligation only; `K = 3` mandated by I-6 §4 |
| SA-2 | Four-leg convergence legs; class rule for leg (c) | E3 chain; `convergence_records.json` `9cf81c03…` | open (OL-3) |
| SA-3 | Whether any draw-generating object reads θ | `m08_qw_streams` schema; the 17-column instrument | open |
| SA-4 | Box at θ̂^LOC4 vs `67ef22b3…` / `8e44ec2a…` | `u6f_frozen_box_v1.json` | open |
| SA-5 | Analytic `Z` closed form and its wage-factor support | the normalisation ruling | open (OL-5) |
| SA-6 | `δ_occ` bound | — | **CLOSED** at v3 §1.5 |
| SA-7 | LOC4 W-4 flagged membership | E4-analogue `step3_w4.corrected_detail` | open |
| SA-8 | Block replicate families for `{Δ_T,b}` | — | **CLOSED** at §3.2.1 |
| SA-9 | `IQR_W1_baseline`, required to pin `S_k0` | the functionals artifact | open (OL-9) |
| SA-10 | The inherited curvature battery's tier boundaries and rank/conditioning criteria, for G-L4-8 | the E4 curvature/inference instrument | open (OL-12) |

### 5.3 Validation gates *(carried unchanged)*

| gate | statement | blocks a difference verdict? | failure handling |
|---|---|---|---|
| **G-L4-1** | **CRN exactness.** 17 recorded columns bitwise equal across arms on the base half; `columns_not_bitwise: []` | no — classifies the regime | non-empty ⇒ classify per §3.6; a change in a column that should not depend on θ is a halt |
| **G-L4-2** | **Box invariance.** Both box hashes compared at θ̂^LOC4 | no — classifies the regime | move ⇒ **partial-CRN diagnostic regime** (§3.6); disclose; never repair |
| **G-L4-3** | **Proposal invariance.** `log_q_H`, `log_prior`, `prior`, `log_q_W`, `log_q_Occ`, `log_q_W_mixture` bitwise unchanged; the `q_H` 9-piece partition and its `unit_mass_certificate` (`exact_integral = 1/1`, `float64_integral = 1.0`, `float64_equals_one_bitwise: true`, `float64_abs_deviation = 0.0`) re-verified | **YES** (validity) | any change ⇒ the variant has leaked into the proposal ⇒ **halt** |
| **G-L4-4** | **Geometry invariance.** `n = 1600`, `n_k = 400`, `S_i = 1601` on `T16`, node 0 once per household at zero correction, 0 node exclusions, 4 superblocks, defensive fraction exactly `0.25` | **YES** (reference / comparability) | halt |
| **G-L4-5** | **Support invariance.** Zero off-box working ladder nodes on both arms, on the same rows | **YES** (support) | halt |
| **G-L4-6** | **EUROMOD occupation-invariance.** Confirm `ils_dispy` does not depend on occupation (I-3 §14.3 requires this and does not assert it; I-6 §4 requires the mapping preserved) | **YES** (estimand comparability) | dependence ⇒ the budget mapping moves between arms ⇒ **halt and return**; not repairable inside LOC4 |
| **G-L4-7** | **Normalisation.** N1–N9 analogues re-run **in full** on the extended block **before any pricing**, against the rebound `ĝ = g̃ / Z_i^S`. Prior passes void as gates | **YES** (validity) | halt; the M08E lesson, not negotiable |
| **G-L4-8** | **`δ_occ` / `β_occ_k` separation — STRENGTHENED.** The fitted correlation structure and bound-hit status of the `δ_occ` and `β_occ_k` coordinates are **read jointly with the inherited curvature battery's evidence for the extended `(β_Occ, δ_occ)` sub-block**: minimum eigenvalue, rank, condition-number tier, Cholesky success — the same instruments and criteria the certified fit reports (free-37 min eig `0.089577`, rank `37/37`, condition `473,932`, clean tier; interior-35 min eig `0.124326`, rank 35, Cholesky succeeds — I-1 §2), applied to the extended block. Criteria are **inherited, not invented**; tier boundaries Stage-A-bound (SA-10 / OL-12) | **YES for promotion** | **BLOCKING.** A near-singular block **blocks paper-facing LOC4 welfare magnitudes**, level *and* difference. No longer a reportable finding alone |

**The blocking consequence of G-L4-8:** if the extended `(β_Occ, δ_occ)` block is near-singular by the inherited criteria — **(1)** **no LOC4 welfare magnitude may be paper-facing**, level, difference, share or indicator; **(2)** **no materiality verdict is issued in either direction**, and an *immaterial* reading may **not** discharge the mandatory robustness or license freezing preferred results; **(3)** the outcome is a **return** (§4.5) carrying the curvature evidence, correlation structure, bound-hit table and the §1.4/§6.3 identification argument; **(4)** **the response is never re-parameterisation** — pinning `β_occ_k`, dropping a `δ_occ` coordinate, merging LOC4 categories or widening `B` would each silently change the estimand and fail the rider's estimand-comparability gate.

### 5.4 Normalisation invariance — does `Z` move under `δ_occ`? *(carried unchanged)*

`ĝ = g̃ / Z_i^S`, with **analytic `Z` over the full mixed support** (I-1 §6.4). The answer forks on one schema fact:

- **Unbounded support `w ∈ (0, ∞)`:** the log-normal factor integrates to **exactly 1 for every `k` and every `δ_occ`** — a location shift does not change total mass. **`Z` is invariant.** I-2 §4 supports this on the proposal side: `q_W` is explicitly **untruncated** ("no bound, no clip, no rejection", only an `eps = 1e-300` guard); `w_min`/`w_max` are recorded as *realised sample statistics*.
- **Box support `w ∈ [1.9411632533361265, 101.91995852573758]`:** the factor is **truncated**, its mass is `Φ((log w_max − μ_i − δ_occ(k))/σ) − Φ((log w_min − μ_i − δ_occ(k))/σ)`, which **depends on `δ_occ(k)`**. **`Z` moves — household-specifically and occupation-specifically**, and the closed form must be **extended to carry `δ_occ`**.

**Standing prohibition.** Silently reusing the baseline `Z` in the truncated branch would reintroduce **exactly the M08E defect** — a household-specific, coalition-varying `log Z` offset. Because `Δ` is taken across arms, a `Z` error would **not cancel under CRN**; it would sit directly in the headline difference.

> **`Z` is treated as `δ_occ`-dependent until the normalisation ruling's closed form is read and shown otherwise (SA-5).** The burden of proof runs toward extension. G-L4-7 gates it. An invariance claim asserted without the closed form in hand is a halt.

### 5.5 Coherence check

**Carried unchanged from v3:** **C-1**, **C-2** (CLOSED by R-a), **C-3** (v1's blanket rider SUPERSEDED AND WITHDRAWN by §4.2), **C-4**, **C-5**, **C-6**, **C-7**, **C-8** (corrected at v3: the deterministic chosen-node **numerator** cancels exactly under bitwise node-0 identity; the **`n/(n+1)` normalisation factor does not** — `1600/1601` at `T16`, `1200/1201` at `T12_-b`, `800/801` at `T8_ab`; LOC4 inherits the estimator of record regardless; upstream repair ⇒ re-run), **C-10**, **C-11**, **C-12**, **C-13**, **C-14**, **C-16** (base-dependent shrinkage contaminates `E_Δ`'s bias term; not corrected; disclosed), **C-17** (G-L4-8's blocking creates a route in which LOC4 can neither be promoted nor discharge the mandatory robustness; all admissible responses are deputy-level).

**Amended in v4 (propagation only):**

| id | finding | status |
|---|---|---|
| **C-9** | The closure's headline set is internally heterogeneous: mean and Gini receive a **two-layer band test**, while **φ_A and φ_B receive a precision gate and no substantive cutoff**, their materiality running only through M-5 and M-6. **[v4 propagation]** For φ_A and φ_B, "immaterial" means *"the components' qualitative configuration — each component's sign, and the pairwise ordering — is **identical between the LOC4 and baseline arms** in the full basis `T16` and in every one of the four `T12_-b` leave-one-superblock-out replicates"*. It **never** means "the change is small": no cutoff exists against which smallness could be certified, and none may be invented. | **Named, not designed around.** |
| **C-15** | **M-5's unanimity requirement remains demanding, and is transcribed rather than chosen. [v4 propagation]** M-5 requires agreement across `T16` and the four `T12_-b`. A component whose level is small relative to its Monte-Carlo error — `φ_A`'s baseline level is `0.00617588` against an arm-level `E_T` of `0.000468934` — can plausibly change sign class on a leave-one-out basis in one arm and not the other, purely from sampling. `INDETERMINATE_MC` therefore remains a live M-5 outcome, and it is a return. **Two riders.** *(i)* Removing the six `T8_ab` bases from M-5 (v4 residual correction 1) is **not** a weakening adopted to reduce indeterminacy: it is the transcription of the recorded instrument's own replicate family (§3.5.4), and the reduced strictness is a consequence, not a motive. *(ii)* M-5's replicate family (`T16` + four `T12_-b`) and `E_Δ`'s basis usage (which reads the six `T8_ab` inside `|Δ_T16 − Δ_T8_bar|`) now **differ**, and correctly so: they are separate instruments transcribed from separate fields of the same record, and neither may be conformed to the other for tidiness. | **Named, not designed around.** The response to an indeterminate M-5 is **not** to drop the `T12` family, widen the sign convention, or exempt small components — each would be an invented relaxation. If M-5 returns indeterminate the mission returns, carrying the full indicator table so the deputy can see exactly which basis and which indicator disagreed. |

### 5.6 Open items *(carried unchanged)*

| id | item | status |
|---|---|---|
| **OL-1** | LOC4 Path-B ruling text | **CLOSED** (v2). `JMP_LOC4_pathB_ruling_v1.md`; reconciled at §6; errata at §6.4 |
| **OL-4** | Materiality thresholds on differences | **CLOSED** (v2) by deputy Part B |
| **OL-2** | `δ_occ` bound `B` | **CLOSED** (v3) at §1.5 |
| **OL-8** | Block replicate index for `{Δ_T,b}` | **CLOSED** (v3) at §3.2.1 |
| **OL-3** | Four-leg convergence leg definitions and the class rule for leg (c) | **OPEN — BLOCKING** |
| **OL-5** | `Z` closed-form support (§5.4, SA-5) | **OPEN — BLOCKING before any pricing** |
| **OL-6** | EUROMOD occupation-invariance (G-L4-6) | **OPEN — BLOCKING.** Under the rider it gates *every* difference verdict (C-14) |
| **OL-7** | Dependency on the CV1 return disposition | **OPEN — tracked.** Per C-8, an upstream estimator repair forces a **re-run** |
| **OL-9** | `IQR_W1_baseline`, required to pin `S_k0` | **OPEN — transcription at execution.** `S_k0` known only to be at least `1396.13` |
| **OL-10** | Errata pins: stale `docs/design_notes/` path (ERR-1); rulings-register byte-identity reconciliation (ERR-2) | **OPEN — housekeeping, resolved at freeze** |
| **OL-11** | Pre-registered statement of the paper's qualitative conclusion, to make M-6 decidable (C-13) | **OPEN — BLOCKING before execution** |
| **OL-12** | Transcription of the inherited curvature battery's tier boundaries and rank/eigenvalue criteria for G-L4-8 (SA-10, C-17) | **OPEN — BLOCKING before execution** |

---

## 6. PATH-B RECONCILIATION

*(carried from v3 unchanged in its entirety)*

### 6.1 The I-6 §4 robustness contract, clause by clause

| I-6 §4 clause | where satisfied | verdict |
|---|---|---|
| "use the existing LOC4 grouping definition" | §1.1 — the four-category task-group collapse of I-3 §6; no alternative grouping constructed or searched | **SATISFIED** |
| "change only the pre-registered wage-density component" | §1.3 — the only form change is `μ_i(X) → μ_i(X) + δ_occ(k)` inside `O^W`; §1.6 enumerates everything else frozen; G-L4-3/4/5 verify no leakage | **SATISFIED at the level of model form**; §6.2 for coefficients |
| "preserve the sample" | §1.6 — N = 1,555, France 2016 singles, 101 alternatives/hh, successor_v2 pins re-hashed fail-closed | **SATISFIED** |
| "preserve the utility specification" | §1.6; §6.2 | **SATISFIED** |
| "preserve the access index" | §1.6 — `O^E` and `O^Occ` forms frozen | **SATISFIED** |
| "preserve the tax-benefit mapping" | §1.6 and **G-L4-6** | **SATISFIED, conditional on OL-6** |
| "preserve the welfare metric, inequality index and decomposition rule" | §1.6; §0.1 measure roles unchanged | **SATISFIED** |
| "document whether mean and/or dispersion changes are introduced" | §1.3 — **mean (location) only; σ shared; no dispersion change** | **SATISFIED** |
| "prevent double counting between occupation-access coefficients and wage-density shifts" | §6.3 | **ANSWERED** |
| "compare the same headline welfare and decomposition outputs" | §3.7 — W1 PRIMARY with W3 validation; identical functionals on both arms through the same code paths on the same nodes under CRN | **SATISFIED** |

**The four prohibited additions, each explicitly absent:**

| prohibited addition | status |
|---|---|
| **sex-specific occupation densities** | **ABSENT.** `δ_occ` gender-pooled, `K = 3`; v1's `K = 6` alternative foreclosed |
| **industry** | **ABSENT.** No `lindi`, no NACE. I-3 §6's naming rule observed: **occupation opportunity**, never sector opportunity. I-6 §6 defers `lindi` |
| **external regional covariates** | **ABSENT.** None added. `β_gsur` and the `drgn*` coding are **carried unchanged** from the certified access block — carrying an existing coefficient is not adding a covariate. The `M2` axis is untouched |
| **alternative grouping searches** | **ABSENT.** One grouping fixed ex ante, reference fixed at `k = 1`. I-6 §7's two-group comparison is *useful later* and **not** authorised here |

### 6.2 The re-estimation reconciliation (I-6 §3 versus §4) — C-11

I-6 §3 is headed **"Frozen baseline"** and governs **"the first welfare prototype"** — the M08 baseline mission, complete and closed. I-6 §4 governs a **different** mission whose defining act is to "change only the pre-registered wage-density component." A wage-density component cannot be *changed* without estimating the coordinates of the changed density; a `δ_occ` that is not estimated is not a four-density model. I-6 §6's sequencing confirms the two are distinct steps.

**The operative distinction is form versus coefficients.** I-6 §4's preservation list — sample, utility specification, access index, tax-benefit mapping, welfare metric, inequality index, decomposition rule — is a list of **specifications and mappings**, not fitted numerals. A partially-frozen refit would be a maximum-likelihood estimate of nothing.

**Recorded as an incoherence risk, not resolved by fiat.** If the deputy reads I-6 §3 as binding on the robustness mission too, **LOC4 as specified is not executable**, and that is a **return**.

### 6.3 The double-counting clause, answered

Occupation enters through two economically distinct channels: **`β_occ_k` — occupation as *availability*** (in `O^Occ`, shifting how much of occupation `k` is offered, **uniformly in the wage**), and **`δ_occ(k)` — occupation as *price*** (in `O^W`, shifting where the wage distribution sits *within* occupation `k`, **non-uniformly in the wage**).

```
Δ log f_W  =  δ_occ(k)·( log w − μ_i ) / σ²   −   δ_occ(k)² / (2σ²)
```

The **constant term** — the part that would double-count — is **perfectly collinear with `β_occ_k` and absorbed by it**. It is not double-counted; it is *assigned*, unambiguously, to the access channel. What remains and identifies `δ_occ` is the **`w`-interaction**, which `β_occ_k` cannot produce. **The separating variation is within-occupation wage variation, and only that.** This is why the design does not pin, drop or restrict `β_occ_k`.

**Verification, not assertion — and blocking.** **G-L4-8** measures the realised separation, **read jointly with the extended block's curvature, rank and conditioning evidence** (§5.3). **Near-degeneracy blocks paper-facing LOC4 magnitudes and returns the mission** (C-17). Pinning `β_occ_k` to force separation would silently change the estimand and fail the rider's estimand-comparability gate.

Shared σ (§1.3) is part of the answer: `σ_k` would introduce a *second* occupation-indexed channel and the clean assignment would fail.

### 6.4 Errata recorded

| id | erratum | correction |
|---|---|---|
| **ERR-1** | **Stale path in the Phase-5 memo.** The Phase-5 memo cites the LOC4 Path-B ruling at a `docs/design_notes/` path; that path is stale, and the ruling of record is `JMP_LOC4_pathB_ruling_v1.md` | Citation corrected to the located file. The located ruling carries **no `Target repository path` field of its own**, so its canonical location must be **pinned at freeze**, not inferred (**OL-10**) |
| **ERR-2** | **Rulings-register byte-identity note.** No sha256 accompanied the attachment, so byte-identity between the register's referent and the located file **has not been reconciled** | The sha256 of `JMP_LOC4_pathB_ruling_v1.md` is computed and reconciled against the register's note **at freeze**, before v4 is committed. Until then §6 is read from the attached text (**OL-10**) |

Neither erratum changes any substantive clause of §6.1–§6.3.

---

## OUTPUT DISCIPLINE

**Mission ID:** JMP-M08 · LOC4 four-density robustness (design v4, second narrow corrective revision).

**Authoritative inputs:** I-1 … I-9 as tabled, with sha256 pins carried in-line where the instruments carry them. Governing revision authority: **Goal-1 R-146.2** over the re-review of v3.

**Decisions made in v4 (exactly three residual corrections; nothing else reopened):**

1. **M-5's replicate family corrected to the transcribed one** — the accepted-replicate universe for M-5 is the **full basis `T16` plus the four `T12_-b` leave-one-superblock-out replicates**, exactly as the recorded `threshold_set_of_record` states: *"signs and ordering identical between `T16` and every `T12` LOO"* (I-2 §6.4). The six `T8_ab` bases are **removed from M-5**. The v3 "no principled ground to exclude" construction is **deleted** and replaced by the **transcription ground**: M-5 transcribes the recorded sign/order instrument, and importing `T8` would be an **unauthorised strengthening** of a criterion this memo is transcribing rather than authoring. The arm-to-arm indicators `S_{c,b}`, `O_{cd,b}` and the frozen `sgn(0)` / exact-tie convention are **unchanged**.
2. **The `T8` deletion propagated from M-5 only** — through §3.5.5, §3.7, §4.1, §4.3, §4.4, §4.5, C-9, C-15 and this section, wherever the M-5 replicate universe is named. **`T8_ab`'s role inside `E_Δ`'s `|Δ_T16 − Δ_T8_bar|` term is untouched**, and §3.2.2's formula is carried forward verbatim.
3. **A1 disclosure 2 sentence replaced verbatim** — the partial-CRN row of §3.6 now reads: *"A partial-CRN run may target the same LOC4-minus-baseline functional difference, but it does not implement the pre-registered fully paired precision experiment: the defensive quarter loses CRN covariance cancellation, so its resulting band is not the designed full-CRN difference band."* The diagnostic/return consequence is unchanged.

**Assertion:** no other section moved. Items 3, 4, 5 and 6 of the v3 mandate (the transcribed `E_Δ` estimator, the corrected C-8, the strengthened G-L4-8, the frozen `δ_occ` bound) and A1 disclosure 1 were **CURED at v3** and are carried forward here unaltered.

**Unresolved decisions:** **OL-3** (four-leg definitions), **OL-5** (`Z` closed form, before pricing), **OL-6** (EUROMOD occupation-invariance; gates every difference verdict), **OL-11** (pre-registered qualitative conclusion), **OL-12** (curvature tier boundaries for G-L4-8) — all BLOCKING; OL-7 (CV1 disposition, a re-run dependency), OL-9 (`IQR_W1_baseline`), OL-10 (errata pins). **Closed:** OL-1, OL-4 (v2); OL-2, OL-8 (v3).

**Exact output filename:** `docs/Missions/JMP_M08_LOC4_robustness_design_v4.md`
**Preserved history:** `docs/Missions/JMP_M08_LOC4_robustness_design_v3.md`, `..._v2.md`, `..._v1.md`, all immutable.

**Status:** PROPOSED-PENDING-FREEZE.

**Next authorised action:** submit v4 against the three residual corrections for freeze. On freeze, **execute LOC4 autonomously** — subject to the five blocking open items being discharged first, none of which is a matter of manager discretion. Return to the deputy if LOC4 difference precision is **indeterminate on a headline threshold**, if **M-5 returns MATERIAL or INDETERMINATE_MC over `T16` and the four `T12_-b`**, if the run falls into the **partial-CRN diagnostic regime**, if **G-L4-8 blocks**, if **disclosure fails**, if a **package change** is required, or if the **preferred specification cannot be selected**.

**Statement.** No welfare number, decomposition number, inequality index, parameter value, priced node, re-estimation, new draw, or EUROMOD execution was produced. Every numeral is transcribed from a named record with a citation, or — in the single marked case of §1.5 — is the value of a frozen deterministic formula evaluated on one bitwise-verified transcribed constant. Every threshold is transcribed from deputy Part B or Path-B §5 with both instruments cited; the `E_Δ` error functional and **M-5's replicate family** are transcribed from the accepted record with their source fields named. **No threshold, cutoff, tolerance, sign-band, denominator or replicate family was invented**, in either the lenient or the strict direction, and every gap in the record is named as an open item rather than filled.