# JMP-M08 — LOC4 FOUR-DENSITY ROBUSTNESS: DESIGN MEMO v3

**Mission ID:** JMP-M08 · LOC4 (pre-registered first robustness axis)
**Class:** Design memo. **PROPOSED-PENDING-FREEZE** (narrow corrective revision of an otherwise accepted design).
**Target repository path:** `docs/Missions/JMP_M08_LOC4_robustness_design_v3.md`
**Date:** 2026-08-26
**Supersedes:** `JMP_M08_LOC4_robustness_design_v2.md` as the binding design. **v2 is preserved as history**, immutable, neither edited nor withdrawn; `..._v1.md` remains preserved as proposed history beneath it.
**Authorising instruments:** Goal-1 **R-145.2**, over the independent economics/numerical review of v2; deputy **Part B — LOC4 Materiality and MC Precision**; deputy **LOC4 Ruling v1 — Path B**.

**Review disposition.** The independent review **rejected v2 narrowly**. Explicitly **ACCEPTED and unchanged in v3**: the R-a baseline-scale convention; the direct CRN difference instrument; the arm-precision rider; the Path-B reconciliation (§6); and the estimation architecture (§1–§2). **Exactly six corrections are mandated**, plus two A1 disclosures. Nothing else is reopened.

**Revision register.** Changes from v2 are confined to: the header block; **§1.5** (item 6 — the bound is frozen by exact formula); **§3.2** (item 3 — the `E_Δ` estimator transcribed; A1 disclosure 1 — softened overstatement; A1 disclosure 2 — partial-CRN marked as a diagnostic regime); **§3.5** (item 1 — replaced in full); **§3.7** (item 2 — M-5 propagation); **§4.1, §4.3, §4.4, §4.5** (item 2 — M-5 propagation); **§5.2** (SA-6 and SA-8 closed; SA-10 added); **§5.3** (item 5 — G-L4-8 strengthened to blocking); **§5.5** (item 4 — C-8 corrected; item 2 — C-9 language corrected; C-15, C-16, C-17 added); **§5.6** (open-item refresh); the closing Output Discipline block. **§0, §1.1–§1.4, §1.6, §2, §3.1, §3.3, §3.4, §3.6, §4.2, §5.1, §5.4 and §6 are carried forward intact.** No change was made outside these named locations.

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
| I-8 | **Independent review of v2, adopted at Goal-1 R-145.2** | the six mandated corrections and the two A1 disclosures implemented here |

**No computation, no code, no new draw, no welfare number, no parameter value, no EUROMOD execution is produced or implied by this memo.**

---

## 0. MEASURE ROLES AND ESTIMATOR OF RECORD

*(carried from v2 intact; C-8's correction is at §5.5)*

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
- **C-8 dependency:** see the **corrected** statement at §5.5. LOC4 inherits the estimator of record regardless; an upstream repair forces a re-run.

---

## 1. THE VARIANT

*(§1.1–§1.4 and §1.6 carried from v2 intact; §1.5 replaced per mandated item 6)*

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

### 1.5 Bounds — FROZEN BY EXACT FORMULA *(mandated item 6; replaces v2 §1.5; OL-2 CLOSED)*

v2 left `B` to a "with slack" rule at freeze. **That discretion is removed.** The bound is fixed here, before estimation, by a deterministic formula evaluated on a transcribed constant.

**Derivation.** `δ_occ(k)` is a **location shift in log wage**. The recorded wage support of the priced nodes is the frozen box's closed interval

```
w ∈ [ w_min , w_max ] = [ 1.9411632533361265 , 101.91995852573758 ]     (I-2 §2(i))
```

whose **exact log-width is a recorded field of the frozen box**:

```
log_range_L = 3.9609003763945605                                        (I-2 §2(i))
```

and which I-2 §2(v) independently confirms: `DefensiveComponent.log_L` recomputed from the frozen bounds equals `log_range_L` **bitwise**.

Every within-occupation log-wage support on the recorded stack is a **subset** of `[log w_min, log w_max]` — there are **zero off-box working ladder nodes** on every rung and in the independent re-verification (`0 off-box working ladder nodes of 1,989,854`, I-2 §2(iv)). Therefore any two occupation-specific log-wage **locations** that both lie inside the recorded support differ by **at most `log_range_L`**. A `|δ_occ(k)|` exceeding that width would place occupation `k`'s wage location outside the support of every recorded wage node — economically meaningless and numerically off-box.

**The frozen formula.**

```
B  =  ceil( log_range_L )                     evaluated on the frozen box
   =  ceil( 3.9609003763945605 )
   =  4.0

δ_occ(k) ∈ [ −4.0 , +4.0 ]   for k ∈ {2,3,4} ;   δ_occ(1) ≡ 0
```

**The numerical slack is exactly `B − log_range_L = ceil(log_range_L) − log_range_L`** — a deterministic quantity fixed by the same formula, not a judgement, not a range, not a parameter of the analyst. Ceiling to the next integer in log points is the entire slack rule; no further margin is added and none may be added at execution.

**Properties, stated so the choice is auditable.** `B` is (i) **deterministic** — a total function of one recorded, bitwise-verified frozen-box field; (ii) **fixed before estimation** and recorded here, not at freeze and not at run time; (iii) **guaranteed non-binding on any economically admissible value**, since it admits occupational wage-location ratios up to `e^4`, far beyond any observed between-occupation gap; and (iv) **compact**, satisfying I-3 §17's bound-hit-diagnostic requirement and the four-leg standard's need for a compact admissible set. A bound-hit on `δ_occ` under this `B` is therefore unambiguously diagnostic of a fit pathology — near-degeneracy with `β_occ_k`, or a divergent direction — and never an artefact of a tight box.

**Rejected alternatives, named:** `B = log_range_L` exactly — rejected, because a location at the support edge would sit *on* the bound and produce a spurious bound-hit, which is exactly the diagnostic this design needs to remain clean; `B` tied to `σ̂` — rejected (already in v1/v2), because it makes the box a function of the block being perturbed; `B` from a sample statistic of within-occupation wage means — rejected, because it is not deterministic from the frozen record and would require reading data before estimation; unbounded `δ_occ` — rejected per I-3 §17.

A `δ_occ` coordinate active at `±4.0` is treated exactly as `beta_l_age2_sm` / `beta_l_age2_sf` at I-1 §2.1 — excluded from the covariance by construction, SE/z/p **literal NA**, never a numeral, never blank, never zero, never imputed downstream — and, per §5.3, it is read jointly with the strengthened G-L4-8.

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

*(carried from v2 intact — explicitly accepted by the review)*

### 2.1 What is estimated

**Full re-estimation of the entire `47 + K` vector** under the corrected marginal/MIS proposal convention, on the successor_v2 frame, from the same 101-alternative draws. Not a profiled fit, not a two-step, not a warm-started perturbation of the certified block only: every preference, access, hours, wage and occupation coordinate is free simultaneously, because `δ_occ` is not separable from `β_occ_k` or from the leisure block by construction (§1.4).

The 10 pinned coordinates stay pinned. The two upper-bound-active leisure coordinates are **not** pre-set: they are freed and allowed to re-locate, and whether they remain active at `+1.0` is a reported diagnostic.

**Prohibited:** any evaluated vector mixing θ̂_margqh-v2 coordinates with LOC4 coordinates other than as a documented warm start whose end point is a converged optimum in its own right. The suspended joint-convention estimate (`c024b893…f0580d`) is **never** a parameter source, warm start, or robustness arm (I-1 §1.3).

Reconciliation with I-6 §3 ("No parameter is re-estimated inside the welfare mission") is at §6.2.

### 2.2 Convergence standard

The **amended four-leg convergence standard** applies unchanged in form, with the **deputy convergence-class rule governing leg (c)**. The four legs' definitions are **not transcribable from this mission's attachment set** — they live in `FR_P2a_m08e_E3_reestimation_note_v2.md` (sha256 `970eda4c0d3dcc140b1608159c64fff420eb8395964e2e3b34f500c1a660a5f5`) and `convergence_records.json` (sha256 `9cf81c03e3e7e0ec58d87582f9454d5b076b53bccfe8d3154188878db926b50e`). Entered as **NA-on-this-record**; mandatory transcription at freeze — **OL-3**. Fixed now:

- the standard applies **in full**, no relaxation for the higher parameter count;
- leg (c) is adjudicated by the **deputy convergence-class rule**: a class is assigned and reported, not collapsed to pass/fail;
- the target is the analogue of `E3-CONVERGED-SINGLE-OPTIMUM`. **A LOC4 fit that does not attain a single-optimum verdict is a return, not a headline.**

### 2.3 Inference

Per Phase-4/5 conventions (I-1 §2), on the new free set: household-cluster **CR1**, `G = N = 1,555`; finite-sample factor `c = 1555/(1555 − K_free)` — **`K_free` changes, so `c` changes**, and the certified `1555/1520 = 1.0230263157894737` may **not** be carried across; covariance dimension = the LOC4 interior set (certified 35 interior, plus interior members of `δ_occ`, less any bound-active coordinate, which is excluded by construction and reported literal NA). Disclosure 7 and the prohibited-claims list bind LOC4 output as they bind baseline output: **`δ_occ` may not be described as a causal occupational wage premium**, and baseline-versus-LOC4 coefficient changes may not be described as statistically significant differences.

### 2.4 W-4 diagnostic and the S-10 rule

The corrected W-4 warning is run on the LOC4 free set. Certified flagged set: **{ `beta_l0_sm`, `beta_l0_sf`, `beta_l_nkids_sf` }** (I-1 §2.2).

> **No S-10 re-derivation unless the flagged set changes.** Identical membership ⇒ the frozen five-scenario design of I-1 §3 is **not reopened** and **no S-10 battery is run on the LOC4 arm**. Changed membership (including a newly-flagged `δ_occ` coordinate) ⇒ **a return, not an autonomous re-derivation**: the set is frozen by deputy ruling §4 and R-109.

Differences are taken at **scenario 1 on the baseline arm and θ̂^LOC4 on the LOC4 arm**. S-10 on the LOC4 arm is triggered only in Branch B (§4.4), under deputy disposition. The standing S-10 disclosure applies: Tier-1 deterministic sensitivity, not a confidence region, not a bootstrap, not a posterior; it does not produce welfare confidence intervals.

---

## 3. THE COMPARISON DESIGN

### 3.1 Governing convention: fixed baseline denominators (R-a) — *carried intact, accepted*

> **Adopt R-a: use the BASELINE ARM as the fixed scale. Do not allow the LOC4 result to enlarge its own precision tolerance.** (I-7)

Every denominator in §3.3–§3.4 is a **baseline-arm constant**, transcribed once, pinned pre-execution, held fixed for the whole mission. No denominator reads the LOC4 arm.

### 3.2 Direct blockwise CRN differences, and the exact `E_Δ` estimator *(mandated item 3; A1 disclosures 1 and 2)*

> For every functional, compute the common-random-number difference directly:
> `Delta_T_b = T_LOC4_b − T_BASE_b`
> Estimate `E_Delta` directly from the blockwise differences. **Do not add the two arm-level error bands.** (I-7)

**3.2.1 The paired-difference bases.** The accepted block structure is 4 superblocks (`n_k = 400`, 300 base / 100 defensive, `400 ≡ 0 (mod 4)`, realised defensive fraction exactly `0.25` in every `D_k`), generating the full basis `T16`, the **four** leave-one-out bases `T12_-b` (b = 1…4) and the **six** pair bases `T8_ab` (a<b, the `C(4,2)` pairs). These are confirmed by the recorded alternative counts `S_i = 1601 / 1201 / 801` for `T16 / T12_-b / T8_ab` (I-2 §5.1, §6.1). **OL-8 is closed by this transcription.**

For every functional `T`, the paired difference is formed **on each basis, within basis**:

```
Δ_T16      =  T_LOC4( T16 )      −  T_BASE( T16 )
Δ_T12_-b   =  T_LOC4( T12_-b )   −  T_BASE( T12_-b )       b = 1…4
Δ_T8_ab    =  T_LOC4( T8_ab )    −  T_BASE( T8_ab )        the six pairs
```

**3.2.2 The error functional — transcribed, not constructed.** `E_Δ` is the **same error functional as the accepted arm-level `E_T`**, applied to the paired differences. Source field: `…_u6ffn16_U6F_FUNCTIONALS16_DONE/u6f_functionals16_v1.json`, `step3_functionals`, and the `threshold_set_of_record` recorded there (transcribed at I-2 §6.4); the arm-level construction it defines is carried over verbatim, with `Δ` substituted for the arm-level statistic and nothing else altered:

```
Δ_T12_bar     =  (1/4) · Σ_{b=1..4} Δ_T12_-b
SE_MC(Δ)      =  sqrt[ (3/4) · Σ_{b=1..4} ( Δ_T12_-b  −  Δ_T12_bar )² ]
Δ_T8_bar      =  (1/6) · Σ_{a<b}    Δ_T8_ab
E_Δ           =  max( | Δ_T16 − Δ_T8_bar | ,  1.96 · SE_MC(Δ) )
```

The `(3/4)` factor is the delete-one jackknife factor `(m−1)/m` at `m = 4` blocks; `1.96` and the `max(·)` envelope over a bias-type term and a dispersion term are the accepted construction's own, not this memo's. **No constant in this estimator is invented, rescaled, or re-derived.**

**3.2.3 Three prohibitions.**

1. **`E_Δ` is never formed from the arms' own bands** — not their sum, not their quadrature sum, not their difference. **[A1 disclosure 1 — softened.]** v2 asserted flatly that combining arm bands "systematically overstates uncertainty"; that overstates the case. The correct statement: combining the arms' bands **ignores the positive CRN covariance and therefore generally overstates uncertainty under the intended paired design**. The direction is not guaranteed in every case — it depends on the sign and magnitude of the realised covariance, and it is not assured at all in the partial-CRN regime of §3.6. The prohibition stands **because the deputy instrument mandates the direct construction**, not because the direction of the error is universal. Any implementation combining arm bands is non-compliant with I-7 regardless of which way it errs.
2. **`Δ_T,b` is computed within basis** — the same basis index, the same nodes, both arms. Never across bases.
3. **The difference is taken on the assembled functional**, not propagated through its components. For ratio and share objects, `Δ` is the difference of the assembled functional.

**3.2.4 The `n/(n+1)` scale caveat.** The estimator of record normalises by `S_i = n+1` rather than `n` (§0.2, A5-i), and the resulting scale factor is **basis-dependent** — `1600/1601` at `T16`, `1200/1201` at `T12_-b`, `800/801` at `T8_ab`. Consequently the paired differences entering `E_Δ` are shrunk by **slightly different deterministic factors across bases**, which contaminates the `|Δ_T16 − Δ_T8_bar|` term with a deterministic component. This is named as **C-16** (§5.5) and is **not** corrected by rescaling: the estimator of record is inherited as implemented.

### 3.3 Layer 1 — PRECISION gates on the difference *(carried intact, accepted)*

These test whether the **difference is resolved**. They are *not* materiality thresholds.

| class | baseline-arm scale | precision gate |
|---|---|---|
| mean | `S_k0 = max( |mean_Wk_baseline| , |median_Wk_baseline| , IQR_Wk_baseline , 1 € )` | `E_Δ,mean / S_k0 ≤ 0.0025` |
| median | same `S_k0` | `E_Δ,median / S_k0 ≤ 0.0025` |
| Gini | — (absolute) | `E_Δ,Gini ≤ 0.00125` |
| component levels (φ) | — (absolute) | `E_Δ,φ ≤ 0.00125` |
| normalized contributions | `S_r0 = max( 1 , |r0| )`, `r0` the **baseline** contribution | `E_Δ,r / S_r0 ≤ 0.005` |

**Transcribed baseline-arm constants** (I-2 §6.4) for pinning `S_k0`, `S_r0`:

| object | baseline `T16` | baseline arm's own `E_T` | baseline level-gate ratio |
|---|---|---|---|
| `W1_mean` | `1396.13` | `3.02142` | `0.866` (pass) |
| `W1_median` | `1340.43` | `11.5733` | `3.316` (FAIL) |
| `W1_gini` | `0.173955` | `0.000869933` | `0.696` (pass) |
| `W1_phi_A_level` | `0.00617588` | `0.000468934` | `0.375` (pass) |
| `W1_phi_B_level` | `0.0114346` | `0.00119598` | `0.957` (pass) |
| `W1_s_opp` ( ≡ `r_phi_A+phi_B` ) | `0.101236` | `0.0094323` | `1.886` (FAIL) |

`IQR_W1_baseline` is **not on this record** and is a required component of `S_k0` — **OL-9**; until transcribed, `S_k0` is known only to be **at least** `1396.13`. `S_r0` for `s_opp` resolves to the **unit floor**, since the transcribed `r0 = 0.101236` lies below `1`; that gate is therefore effectively absolute at `E_Δ,r ≤ 0.005`.

### 3.4 Layer 2 — SUBSTANTIVE thresholds *(carried intact, accepted; M-5's operationalisation replaced at §3.5)*

| # | criterion | threshold `m` | Part B form | Path-B source |
|---|---|---|---|---|
| M-1 | mean money-metric welfare | `0.01` | `|Δ_mean| / max(|mean_Wk_baseline|, 1 €) ≥ 0.01` | I-6 §5.3 |
| M-2 | median money-metric welfare | `0.01` | `|Δ_median| / max(|median_Wk_baseline|, 1 €) ≥ 0.01` | I-6 §5.3 |
| M-3 | welfare Gini | `0.005` | `|Δ_Gini| ≥ 0.005` | I-6 §5.2 |
| M-4 | opportunity-attributable share | `0.02` | `|Δ_s_opp| ≥ 0.02` | I-6 §5.1 |
| M-5 | **sign / ordering of a headline decomposition component** | — (binary configuration test) | **see §3.5** | I-6 §5.4 |
| M-6 | qualitative conclusion | — | the paper's qualitative conclusion about the importance of opportunity heterogeneity changes | I-6 §5.5 |

**Two prohibitions, transcribed:**

> **"Do not invent a component-level materiality cutoff. Component materiality is assessed through stable sign/order changes and the qualitative-conclusion criterion."** (I-7)
> **"Other normalized component differences are reported with bands but do not receive an invented 2pp threshold."** (I-7)

Accordingly `φ_A` and `φ_B` receive the precision gate `E_Δ,φ ≤ 0.00125` and **no substantive cutoff**; their materiality is assessed **only** through M-5 and M-6. Likewise `φ_P`, `R_bg`, `r_phi_A`, `r_phi_B`, `r_phi_P`, `r_R_bg` and the `I_{·}` family: bands, no invented threshold, no verdict of their own.

**M-6 is not operational on the record** and must be **pre-registered** as a single decidable statement before execution — **OL-11**, blocking. This is a pre-registration requirement, not an invented threshold.

### 3.5 M-5 — ARM-TO-ARM CHANGE IN THE COMPONENTS' QUALITATIVE CONFIGURATION *(mandated item 1; replaces v2 §3.5 in full)*

**What was wrong in v2.** v2 operationalised M-5 as *stability of the sign of the difference*: `sign(Δ_T,b)` identical across replicates. That is not what I-6 §5.4 asks. Path-B asks whether **"the sign or ordering of a headline decomposition component changes"** — a change in the *components' own qualitative configuration between the two arms*, not a property of the difference's sign. A decomposition whose components keep identical signs and identical ordering in both arms exhibits no such change even if `Δ` has a stable sign; conversely a component that flips sign between arms exhibits the change even where `Δ`'s own sign is unstable. **The v2 formulation is withdrawn and replaced.**

**3.5.1 The component set.** `C = { φ_A , φ_B }` — the headline decomposition components of the accepted closure (I-4). The ordered pair set is `P = { (A, B) }`, with a fixed lexicographic operand order. `φ_P` and `R_bg` are evaluated by the same indicators and **reported as diagnostics**, not verdict-bearing; extending `C` to them would import components outside the closure's headline set and is a deputy question, not a manager choice.

**3.5.2 The paired indicators.** For each accepted basis `b` (see §3.5.4), with `φ^{L4}_{c,b}` and `φ^{0}_{c,b}` the component levels of the LOC4 and baseline arms **on the same basis**:

```
SIGN CHANGE, per component c ∈ C :

    S_{c,b}  =  1{  sgn( φ^{L4}_{c,b} )  ≠  sgn( φ^{0}_{c,b} )  }

ORDERING CHANGE, per ordered pair (c,d) ∈ P :

    O_{cd,b} =  1{  sgn( φ^{L4}_{c,b} − φ^{L4}_{d,b} )  ≠  sgn( φ^{0}_{c,b} − φ^{0}_{d,b} )  }
```

Both indicators compare **arm to arm within a basis**. Neither reads `Δ`'s sign.

**3.5.3 The deterministic sign convention — fixed here, no cutoff invented.**

```
sgn(x)  =  +1   if  x >  0.0
        =  −1   if  x <  0.0
        =   0   if  x == 0.0     (exact IEEE-754 float64 equality; +0.0 and −0.0 both map to 0)
```

- **Three-valued, with exact zero as its own class.** A move from `0` to `+1`, or from `−1` to `0`, therefore **counts as a sign change**. This is deliberate: exact zero is a distinct qualitative configuration of a decomposition component.
- **Exact comparison, no tolerance, no epsilon band.** This matches the convention already of record for the frozen box — *"closed interval, exact float64, **no tolerance**"* (I-2 §2(i)). Introducing a near-zero tolerance would be an **invented substantive cutoff** and is prohibited by I-7.
- **Ordering differences are evaluated in a fixed operand order** — `φ_c − φ_d` in the lexicographic order of the component labels, computed in float64 in that order, once, with the result passed to `sgn`. An **exact tie** (`φ_c − φ_d == 0.0`) is its own class, so a move into or out of an exact tie counts as an ordering change.
- **No re-ordering, re-association or re-summation of the subtraction is permitted**, since float64 subtraction is order-sensitive; the operand order is part of the frozen convention.

**3.5.4 The accepted-replicate set.** The **full basis** is `T16`. The **accepted replicates** are the ten accepted sub-bases: the **four** `T12_-b` and the **six** `T8_ab`. `T8` is included because M-5 is a robustness statement about a qualitative configuration and there is no principled ground on which to exclude the sub-bases the accepted machinery already produces. The consequence — that unanimity over the noisiest bases (`T8_ab`, `S_i = 801`) is demanding and makes `INDETERMINATE_MC` a likely M-5 outcome — is named as **C-15** and is not designed around.

**3.5.5 The verdict rule.** Per indicator `I ∈ { S_c : c ∈ C } ∪ { O_cd : (c,d) ∈ P }`:

```
I is MATERIAL                  iff   I_{T16} = 1   AND   I_b = 1  for EVERY accepted replicate b
I is IMMATERIAL                iff   I_{T16} = 0   AND   I_b = 0  for EVERY accepted replicate b
I is INDETERMINATE_MC          otherwise   (the replicates disagree, or disagree with the full basis)
```

**M-5 aggregate:** MATERIAL if any indicator is MATERIAL; otherwise INDETERMINATE_MC if any indicator is INDETERMINATE_MC; otherwise IMMATERIAL.

**M-5 is a binary configuration test, not a magnitude test.** The `|Δ̂| ∓ E_Δ` band rule of §4.1 **does not apply to it**, and no `E_Δ` is formed for it. Its uncertainty is handled entirely by the unanimity requirement across the accepted bases — which is the same device the accepted `threshold_set_of_record` uses for its own sign/ordering limb (*"signs and ordering identical between `T16` and every `T12` LOO"*, I-2 §6.4), here extended from one arm to the **arm-to-arm comparison** and from the `T12` family to all accepted sub-bases.

### 3.6 CRN construction — where it is exact, where only partial *(carried; A1 disclosure 2 applied)*

**Design intent:** `δ_occ` enters the **structural index only**. It does not enter `q^W`, the `q_H` marginal, `q_Occ`, `log_prior`, the employment margin, `λ`, or the node identities.

**Exact on the base half (75%), conditional on G-L4-1.** `q^W`'s wage mean is built from the frozen pilot mincer payload, not from θ (I-2 §4). If the base draw path reads no coordinate of θ, then across arms these are bitwise identical: `working`, `hours`, `wage`, `loc4`, `log_q_E`, `log_q_H`, `log_q_W`, `log_q_Occ`, `log_prior`, `log_q_base`, `stream_seed`, `base_position`, `component_label`, `in_support_box`, the priced consumption, node 0 and its zero correction, superblock membership, `S_i`. Verified — not assumed — by the bitwise-column instrument of record (I-2 §2(iii): 17 of 17 columns bitwise equal, `columns_not_bitwise: []`).

**At risk on the defensive half (25%): the frozen box.** `DefensiveComponent.draw` maps its uniforms **through** the box, so a box move regenerates every defensive node and voids the pairing on that half. The record establishes the box is evaluated at θ and **has moved before**: `box_at_theta_v2.box_moved: true`, `delta_log_L: 0.06107235168894798`, with `311000 = 1555 × 200` defensive nodes re-priced and `additional_nodes_due_to_box_move: 155500` (I-2 §2(ii)).

| branch | condition | CRN status | consequence |
|---|---|---|---|
| **CRN-exact** | box at θ̂^LOC4 bitwise equals `box_hash_sha256 = 67ef22b3742ccc04a25c377cec60e18478b6fd07e539c0340497a274c0ce2c52` / `float64_bytes_sha256 = 8e44ec2a926aa06fd844a0be97fdbfdc29d3299ca1a7b3a1eb46a7191ae6e361`; `h_min/h_max = 5.0/70.0`, `w_min/w_max = 1.9411632533361265/101.91995852573758`, `log_range_L = 3.9609003763945605` unchanged | exact on **all** nodes | the **designed experiment**; `E_Δ` per §3.2.2 is the difference band; materiality verdicts are issued |
| **CRN-partial** | box moves at θ̂^LOC4 | exact on the base 75%; **broken** on the defensive 25% | **[A1 disclosure 2] This is a DIAGNOSTIC REGIME, not the same experiment.** A partial-CRN run does not estimate the quantity the full-CRN design defines: a quarter of the nodes are unpaired, the covariance structure `E_Δ` was specified against no longer holds, and the resulting band is not the designed difference band. All outputs are **labelled diagnostic**; `E_Δ` may not be presented as a CRN difference band; **no materiality verdict is issued from a partial-CRN run without deputy disposition** — it is a return |
| **halt** | box moves **and** re-pricing is required | — | EUROMOD re-pricing at the recorded scope (155,500 per defensive half; 311,000 across both) is a cost and custody event, disclosed with the pairing loss |

**No CRN repair is attempted.** Re-seeding, re-mapping, or reusing pre-move defensive uniforms to manufacture pairing is prohibited: pre-rebind defensive nodes do not survive anywhere in the stack (I-2 §2(ii)).

**What CRN does not buy.** Both arms are evaluated at their **own full re-estimated vectors**. CRN pairs the *randomness*, not the *parameters*. `Δ` is the effect of the **specification change as a whole**, not the partial effect of the `δ_occ` term (**C-7**). Sentences of the form "adding occupation to the wage block moves W1 mean by …" are prohibited.

### 3.7 Reporting order *(M-5 propagation)*

**Tier 1 — the two-layer battery:** `W1_mean` (M-1), `W1_median` (M-2), `W1_gini` (M-3), `W1_s_opp` (M-4), each with its §3.3 precision gate and §4.1 band rule; **M-5 on the arm-to-arm configuration of `φ_A` and `φ_B`** per §3.5, reported as the indicator table `{ S_A , S_B , O_AB }` × `{ T16 , four T12_-b , six T8_ab }` with the per-indicator verdict; and M-6 against the pre-registered statement.

**Tier 2 — bands, no materiality verdict:** all other normalized contributions, the `I_{·}` family, `φ_P` and `R_bg` (including their diagnostic `S`/`O` indicators), and the W3 validation comparison. W4 and W6 differences are reported banded with the I-2 §5.2 riders (A4-1, A4-2).

Every reported object is a **difference** or an **arm-to-arm indicator**. Arm levels appear only as the fixed denominators of §3.1 and as banded standalone magnitudes under the rider of §4.2.

---

## 4. THE DECISION TREE

### 4.1 The classification rule *(Part B verbatim; M-5 carve-out per mandated item 2)*

For a magnitude criterion with threshold `m` and its `Δ̂`, `E_Δ`:

```
LOC4_MATERIAL                        when   |Δ̂| − E_Δ  ≥  m
LOC4_IMMATERIAL                      when   |Δ̂| + E_Δ  <  m
LOC4_MATERIALITY_INDETERMINATE_MC    otherwise
```

> **"Apply the same rule to baseline-relative mean/median ratios."** (I-7)

For M-1 and M-2 the tested object is the **ratio**; since its denominator is a fixed baseline constant, the rule transfers exactly, with `Δ̂` and `E_Δ` both divided by `max(|mean_Wk_baseline|, 1 €)` (resp. median) before comparison to `m = 0.01`.

**The band rule governs M-1, M-2, M-3 and M-4 only.** **M-5 is a binary configuration test and is classified by the unanimity rule of §3.5.5**; no `E_Δ` is formed for it and the band rule is not applied to it. **M-6 is a pre-registered qualitative determination** (OL-11) and likewise carries no band.

**`LOC4_MATERIALITY_INDETERMINATE_MC` is a return.** It is a **verdict**, not a state to be resolved by re-running until it resolves. Prohibited without deputy disposition: extending the ladder beyond 16x to shrink `E_Δ`; re-drawing; re-seeding; dropping an object from Tier 1; substituting a Tier-2 object for a Tier-1 one; re-reading a functional's threshold class; **or widening the sign convention of §3.5.3 with a tolerance to force M-5 unanimity.**

**Aggregation**, per I-6 §5 ("materially different if **any one** occurs"):

- **LOC4 IMMATERIAL overall** iff M-1…M-4 each return `LOC4_IMMATERIAL`, **M-5 returns IMMATERIAL** per §3.5.5, and M-6 records no change.
- **LOC4 MATERIAL overall** iff **any** of M-1…M-4 returns `LOC4_MATERIAL`, **or M-5 returns MATERIAL**, or M-6 records a change.
- **Return** if **any** of M-1…M-4 returns `LOC4_MATERIALITY_INDETERMINATE_MC`, **or M-5 returns INDETERMINATE_MC**, or the run is in the partial-CRN diagnostic regime (§3.6), or the strengthened G-L4-8 blocks (§5.3).

### 4.2 THE ARM-PRECISION RIDER *(Part B verbatim; carried intact, accepted)*

> **"Do not adopt the proposed rule that either arm's standalone level-precision failure automatically removes the LOC4 materiality verdict. A standalone arm that fails its level gate remains banded and cannot be promoted as a standalone magnitude.**
> **But a LOC4-minus-baseline materiality verdict is permitted when:**
>
> * **both arms pass validity, support, reference and estimand-comparability gates; and**
> * **the direct CRN difference passes its own precision gate.**
>
> **If the direct difference fails precision, report it as uncertified and make no materiality verdict.**
> **If either arm fails validity, support, reference or estimand comparability, no difference verdict is permitted."** (I-7)

This **supersedes and withdraws** v1's blanket rule that either arm's level failure removes the verdict. The corrected logic separates **level precision** (a property of one arm's standalone magnitude) from **difference precision** (a property of the paired CRN difference); only the latter gates the verdict.

| object | baseline level gate | v1 treatment (WITHDRAWN) | treatment under the rider |
|---|---|---|---|
| `W1_s_opp` | **FAIL** (`1.886`) | no verdict permitted | **verdict-eligible on M-4**, given the arm gates and `E_Δ,r / S_r0 ≤ 0.005`. The **level** `0.101236` remains **banded and non-promotable** |
| `W1_median` | **FAIL** (`3.316`) | banded | **verdict-eligible on M-2** under the same conditions; the level remains banded |
| `W1_mean`, `W1_gini`, `φ_A`, `φ_B` | pass | headline | unchanged; passing a level gate does **not** license a difference verdict — the difference precision gate still applies |

**The arm gates that block a difference verdict** are validity, support, reference and estimand comparability — **G-L4-3**, **G-L4-4**, **G-L4-5**, **G-L4-6**, **G-L4-7**. Failure in any of those ⇒ **no difference verdict at all, for any functional**.

### 4.3 Branch A — LOC4 IMMATERIAL

**Condition:** M-1…M-4 each `LOC4_IMMATERIAL`; **M-5 IMMATERIAL — i.e. `S_A = S_B = O_AB = 0` in the full basis and in every accepted replicate**; M-6 no change against the pre-registered statement (OL-11); the run is in the full-CRN regime; G-L4-8 does not block.

**Verdict:** **retain the certified baseline as the preferred specification and report LOC4 as robustness** (I-6 §5).

**Pipeline consequences:**

- **Rebinds:** nothing. No welfare artifact, `q^W` object, `Z`, `ĝ` sampler, coalition target or pricing ladder rebinds.
- **Re-runs:** nothing.
- **Stays frozen:** θ̂_margqh-v2 as sole parameter source; the frozen box; the five-scenario S-10 set; the 16x stack; the prototype closure and its headline set.
- **New obligation:** a **disclosure** in every manuscript, notebook, table, figure and memo carrying a decomposition number — that the wage block was tested against the LOC4 occupation-conditional four-density extension and the headline objects were immaterially affected — reported with `Δ̂`, `E_Δ`, the M-5 indicator table, the classification per criterion, and the CRN regime. The disclosure must state that the axis tests **occupation-conditional wage location only**: not dispersion (`σ_k`), not occupation-conditional hours (`O^H | Occ`, `M4`), not regional opportunity (`M2`), not industry (`lindi`, deferred at I-6 §6). Immateriality on this axis is not immateriality on the occupation dimension.
- **I-6's mandatory-before-final-claims status is discharged for this axis**; I-6 §6.4's sequencing is satisfied and preferred quantitative welfare results may be frozen.

### 4.4 Branch B — LOC4 MATERIAL

**Condition:** any of M-1…M-4 returns `LOC4_MATERIAL`, **or M-5 returns MATERIAL** (the full-basis comparison exhibits a sign or ordering change between arms *and* every accepted replicate exhibits that same change), or M-6 records a change.

**Verdict:** **the preferred specification must be reconsidered before final paper-facing quantitative claims** (I-6 §5). The manager selects neither arm on its own authority. **This is a return**, under two independent deputy triggers: "LOC4 changes sign/order or the qualitative conclusion" (if M-5 or M-6 fired) and "the preferred specification cannot be selected."

**Pipeline consequences:**

- **Nothing rebinds pending disposition.** The pipeline is **held**, not switched. θ̂_margqh-v2 remains the parameter source of record.
- **Stays frozen:** everything. The M08 prototype closure is not withdrawn.
- **The return packet carries:** the LOC4 convergence class and four-leg result; the `47 + K` parameter table with CR1 SEs on the recomputed `c`; the W-4 flagged membership; per-criterion `Δ̂`, `E_Δ` and classification; **the full M-5 indicator table across `T16`, the four `T12_-b` and the six `T8_ab`**; the CRN regime with the box-hash comparison; the strengthened G-L4-8 evidence (curvature, rank, conditioning of the extended `(β_Occ, δ_occ)` block); and every coherence finding of §5.5 that fired.
- **If and only if the deputy promotes LOC4**, the full rebinding cascade of I-1 §6 executes in its stated order — rebinding → deterministic + N-test batteries (N1–N9, in full, **before any pricing**) → U6 → pricing ladder → welfare → decomposition → S-10 → LOC4 — with S-10 re-derived under a deputy-approved revision register, and the RUM benchmark re-estimating its own preferences under the promoted specification (`g ≡ 1` with a retained θ̂ remains forbidden).
- **If baseline is retained**, Branch A's disclosure applies **strengthened**: it must report that the axis produced a material difference and that baseline was retained by ruling, with the LOC4 numbers shown.
- **I-6 §7** classifies "a parsimonious two-group LOC4 comparison" as *useful later*; it is **not** authorised by a material verdict.

### 4.5 Branch C — LOC4_MATERIALITY_INDETERMINATE_MC

**Condition:** any of M-1…M-4 falls in the `otherwise` band; **or M-5 returns INDETERMINATE_MC — the accepted replicates disagree with each other or with the full basis on any indicator**; or the direct difference fails its own precision gate (the object is **reported as uncertified with no materiality verdict**, per the rider); or an arm fails validity/support/reference/comparability (**no difference verdict is permitted at all**); or the run is in the **partial-CRN diagnostic regime** (§3.6); or the LOC4 fit does not attain a single-optimum convergence verdict (§2.2); or **G-L4-8 blocks** (§5.3).

**Verdict:** **return.**

**Pipeline consequences:** nothing rebinds; nothing is re-run to break the tie on manager authority; the §4.1 prohibitions apply — including, explicitly, that an M-5 disagreement is **not** resolved by introducing a tolerance into the sign convention. The return states which limb was indeterminate and why, and — where the cause is precision rather than substance — carries the cost estimate of the extension that would resolve it, for the deputy to authorise or decline. The M08 prototype was closed under `LIMITED_MC_PRECISION`; indeterminacy traceable to that constraint is an expected outcome of the closure, not a failure of this mission.

---

## 5. FROZEN vs STAGE-A-BOUND; GATES; OPEN ITEMS; COHERENCE

### 5.1 Frozen by this design *(carried, updated to v3's §1.5/§3.2/§3.5)*

The variant's functional form (§1.3: occupation-specific wage **location**, shared σ, fixed reference, `K = 3` gender-pooled); **the `δ_occ` bound `B = ceil(log_range_L) = 4.0` and its exact slack rule (§1.5)**; the exhaustive no-change list (§1.6); full simultaneous re-estimation with `β_occ_k` free (§2.1); the four-leg standard without relaxation (§2.2); the no-S-10-without-membership-change rule (§2.4); fixed baseline denominators, R-a (§3.1); **direct blockwise CRN differences with the transcribed `E_Δ` error functional (§3.2.2)**; the two-layer precision/substantive system with no invented cutoffs (§3.3–§3.4); **the M-5 arm-to-arm configuration test with its exact sign convention and unanimity rule (§3.5)**; the MATERIAL/IMMATERIAL/INDETERMINATE_MC rule with the M-5 carve-out (§4.1); the arm-precision rider (§4.2); the three-branch tree with a **held** pipeline in Branches B and C; the no-CRN-repair rule and the partial-CRN diagnostic marking (§3.6).

### 5.2 Stage-A-bound at execution

| id | item | bound from | v3 status |
|---|---|---|---|
| SA-1 | Gender convention of the certified wage block | `e4_parameter_table.csv` `21a05fb5…` | reporting obligation only; `K = 3` mandated by I-6 §4 |
| SA-2 | Four-leg convergence legs; class rule for leg (c) | E3 chain; `convergence_records.json` `9cf81c03…` | open (OL-3) |
| SA-3 | Whether any draw-generating object reads θ | `m08_qw_streams` schema; the 17-column instrument | open |
| SA-4 | Box at θ̂^LOC4 vs `67ef22b3…` / `8e44ec2a…` | `u6f_frozen_box_v1.json` | open |
| SA-5 | Analytic `Z` closed form and its wage-factor support | the normalisation ruling | open (OL-5) |
| SA-6 | `δ_occ` bound | — | **CLOSED.** Frozen at §1.5 by exact formula on `log_range_L`; nothing to bind at execution |
| SA-7 | LOC4 W-4 flagged membership | E4-analogue `step3_w4.corrected_detail` | open |
| SA-8 | Block replicate families for `{Δ_T,b}` | — | **CLOSED.** Transcribed at §3.2.1: `T16`, four `T12_-b`, six `T8_ab`, confirmed by `S_i = 1601 / 1201 / 801` |
| SA-9 | `IQR_W1_baseline`, required to pin `S_k0` | the functionals artifact | open (OL-9) |
| **SA-10** | **The inherited curvature battery's tier boundaries and rank/conditioning criteria**, for the strengthened G-L4-8 | the E4 curvature/inference instrument | **new in v3** (OL-12) |

### 5.3 Validation gates *(G-L4-8 strengthened per mandated item 5; others carried intact)*

| gate | statement | blocks a difference verdict? | failure handling |
|---|---|---|---|
| **G-L4-1** | **CRN exactness.** 17 recorded columns bitwise equal across arms on the base half; `columns_not_bitwise: []` | no — classifies the regime | non-empty ⇒ classify per §3.6; a change in a column that should not depend on θ is a halt |
| **G-L4-2** | **Box invariance.** Both box hashes compared at θ̂^LOC4 | no — classifies the regime | move ⇒ **partial-CRN diagnostic regime** (§3.6); disclose; never repair |
| **G-L4-3** | **Proposal invariance.** `log_q_H`, `log_prior`, `prior`, `log_q_W`, `log_q_Occ`, `log_q_W_mixture` bitwise unchanged; the `q_H` 9-piece partition and its `unit_mass_certificate` (`exact_integral = 1/1`, `float64_integral = 1.0`, `float64_equals_one_bitwise: true`, `float64_abs_deviation = 0.0`) re-verified | **YES** (validity) | any change ⇒ the variant has leaked into the proposal ⇒ **halt** |
| **G-L4-4** | **Geometry invariance.** `n = 1600`, `n_k = 400`, `S_i = 1601` on `T16`, node 0 once per household at zero correction, 0 node exclusions, 4 superblocks, defensive fraction exactly `0.25` | **YES** (reference / comparability) | halt |
| **G-L4-5** | **Support invariance.** Zero off-box working ladder nodes on both arms, on the same rows | **YES** (support) | halt |
| **G-L4-6** | **EUROMOD occupation-invariance.** Confirm `ils_dispy` does not depend on occupation (I-3 §14.3 requires this and does not assert it; I-6 §4 requires the mapping preserved) | **YES** (estimand comparability) | dependence ⇒ the budget mapping moves between arms ⇒ **halt and return**; not repairable inside LOC4 |
| **G-L4-7** | **Normalisation.** N1–N9 analogues re-run **in full** on the extended block **before any pricing**, against the rebound `ĝ = g̃ / Z_i^S`. Prior passes void as gates | **YES** (validity) | halt; the M08E lesson, not negotiable |
| **G-L4-8** | **`δ_occ` / `β_occ_k` separation — STRENGTHENED. [mandated item 5]** The fitted correlation structure and bound-hit status of the `δ_occ` and `β_occ_k` coordinates are **read jointly with the inherited curvature battery's evidence for the extended `(β_Occ, δ_occ)` sub-block**: the Hessian sub-block's minimum eigenvalue, its rank, its condition-number tier, and Cholesky success — the same instruments and criteria the certified fit reports (free-37 min eig `0.089577`, rank `37/37`, condition `473,932`, clean tier; interior-35 min eig `0.124326`, rank 35, Cholesky succeeds — I-1 §2), applied to the extended block. Criteria are **inherited, not invented**; the tier boundaries are Stage-A-bound (SA-10 / OL-12) | **YES for promotion** — see below | **BLOCKING.** A near-singular `(β_Occ, δ_occ)` block — rank deficiency, a minimum eigenvalue below the inherited criterion, a condition number outside the clean tier, or Cholesky failure on the sub-block — **blocks paper-facing LOC4 welfare magnitudes**, level *and* difference. It is **no longer a reportable finding alone** |

**The blocking consequence of G-L4-8, stated exactly.** If the extended `(β_Occ, δ_occ)` block is near-singular by the inherited criteria:

1. **No LOC4 welfare magnitude may be paper-facing** — not a level, not a difference, not a share, not an indicator. The arm's welfare objects are uninterpretable because the two occupation channels are not empirically distinguished, and a magnitude read off an unidentified block is not a robustness result.
2. **No materiality verdict is issued**, in either direction. In particular an *immaterial* reading may **not** be used to discharge the mandatory robustness or to license freezing preferred quantitative results: an uninterpretable robustness arm discharges nothing.
3. **The outcome is a return** (§4.5), carrying the curvature evidence, the correlation structure, the bound-hit table, and the identification argument of §1.4/§6.3 against which the degeneracy is to be read.
4. **The response is never re-parameterisation.** Pinning `β_occ_k`, dropping a `δ_occ` coordinate, merging LOC4 categories, or widening `B` to escape a bound-hit would each silently change the estimand and fail the rider's estimand-comparability gate. Near-degeneracy is reported and returned; it is not constrained away. (**C-4**, **C-17**.)

### 5.4 Normalisation invariance — does `Z` move under `δ_occ`? *(carried intact)*

`ĝ = g̃ / Z_i^S`, with **analytic `Z` over the full mixed support** (I-1 §6.4). The answer forks on one schema fact:

- **Unbounded support `w ∈ (0, ∞)`:** the log-normal factor integrates to **exactly 1 for every `k` and every `δ_occ`** — a location shift does not change total mass. **`Z` is invariant.** I-2 §4 supports this on the proposal side: `q_W` is explicitly **untruncated** ("no bound, no clip, no rejection", only an `eps = 1e-300` guard); `w_min`/`w_max` are recorded as *realised sample statistics*.
- **Box support `w ∈ [1.9411632533361265, 101.91995852573758]`:** the factor is **truncated**, its mass is `Φ((log w_max − μ_i − δ_occ(k))/σ) − Φ((log w_min − μ_i − δ_occ(k))/σ)`, which **depends on `δ_occ(k)`**. **`Z` moves — household-specifically and occupation-specifically**, and the closed form must be **extended to carry `δ_occ`**. The schema carries an `in_support_box` column and zero off-box nodes on every rung, consistent with a box-bounded welfare job space.

**Standing prohibition.** Silently reusing the baseline `Z` on the LOC4 arm in the truncated branch would reintroduce **exactly the M08E defect** — a household-specific, coalition-varying `log Z` offset. Because `Δ` is taken across arms, a `Z` error would **not cancel under CRN**; it would sit directly in the headline difference.

> **`Z` is treated as `δ_occ`-dependent until the normalisation ruling's closed form is read and shown otherwise (SA-5).** The burden of proof runs toward extension. G-L4-7 gates it. An invariance claim asserted without the closed form in hand is a halt.

### 5.5 Coherence check — re-run for v3

**Carried unchanged:** **C-1** (the closure headline set is precision-selected; `s_opp` and `φ_A+φ_B` fail their level gates — partially resolved by the rider, which makes `s_opp`'s *difference* verdict-eligible while its level stays banded); **C-2** (CLOSED by R-a); **C-3** (v1's blanket rider SUPERSEDED AND WITHDRAWN by §4.2); **C-4** (deliberate double-counting, answered at §6.3 — and now, per item 5, escalated in consequence: see **C-17**); **C-5** (baseline asymmetry: occupation shifts the proposal wage location but is absent from the structural block; disclosed up front); **C-6** (`Z` may or may not move; default posture **moves**); **C-7** (the comparison is specification-level, not coordinate-level); **C-10** (the paper can certify that LOC4 does not move the opportunity share by ≥ 2pp while being unable to certify the share's own level — every M-4 sentence must be a *difference* sentence); **C-11** (I-6 §3 versus §4, reconciled at §6.2 as form-preserved / coefficients-free, with the alternative reading a return); **C-12** (the Path-B substantive battery and the closure headline set are different sets; both reported side by side); **C-13** (M-6 has no operational definition — OL-11, blocking); **C-14** (the rider's arm gates are validity-type; G-L4-6 has never been confirmed, so until it passes **no difference verdict is permitted for any functional**).

**Corrected in v3:**

| id | finding | status |
|---|---|---|
| **C-8** | **CORRECTED per mandated item 4.** v2 stated that "the `y_0^det/(n+1)` term is present identically in both arms and cancels". That is **right about the numerator and incomplete about the factor**. Precisely: under bitwise node-0 identity across arms (verified by G-L4-1), the **deterministic chosen-node numerator `y_0^det` cancels exactly** in the paired difference. But the **`n/(n+1)` normalisation factor does not cancel**: the difference of the two implemented estimators equals `(n/(n+1))` times the difference of the plain `n`-averages — a **shrinkage toward zero** of `1600/1601` at `T16`, and analogously `1200/1201` at `T12_-b` and `800/801` at `T8_ab`. Where the functional passes through the log and the money-metric root-finder, the shrinkage propagates non-linearly and is not removable by rescaling. | **Named. LOC4 inherits the estimator of record regardless** — no rescaling, no correction factor, no repair is applied, because repair is a change to the raw estimator and outside this mission's authority (I-2 memo C-7). **If the upstream A5-i/A5-ii returns are dispositioned in a way that changes the raw estimator, LOC4's comparison must be re-run**, because the object being differenced will have changed. |
| **C-9** | **CORRECTED language per mandated item 2.** The closure's headline set is internally heterogeneous: mean and Gini receive a **two-layer band test**, while **φ_A and φ_B receive a precision gate and no substantive cutoff**, their materiality running only through M-5 and M-6. v2 glossed M-5 as "sign and ordering stable across all replicates", which was the withdrawn Δ-ordering formulation. **Corrected:** for φ_A and φ_B, "immaterial" means *"the components' qualitative configuration — each component's sign, and the pairwise ordering — is **identical between the LOC4 and baseline arms** in the full basis and in every accepted replicate"*. It **never** means "the change is small": no cutoff exists against which smallness could be certified, and none may be invented. | **Named, not designed around.** |

**New in v3:**

| id | finding | status |
|---|---|---|
| **C-15** | **M-5's unanimity requirement is demanding, and most so on the noisiest bases.** M-5 requires agreement across `T16`, the four `T12_-b` **and** the six `T8_ab`, the last of which carry the fewest alternatives (`S_i = 801` against `1601`). A component whose level is small relative to its Monte-Carlo error — `φ_A`'s baseline level is `0.00617588` against an arm-level `E_T` of `0.000468934` — can plausibly change sign class on a `T8` basis in one arm and not the other, purely from sampling. `INDETERMINATE_MC` is therefore a **likely** M-5 outcome, and it is a return. | **Named, not designed around.** The response is **not** to drop the `T8` family, widen the sign convention, or exempt small components — each would be an invented relaxation of a criterion the deputy fixed. If M-5 returns indeterminate the mission returns, carrying the full indicator table so the deputy can see exactly which basis and which indicator disagreed. |
| **C-16** | **The base-dependent shrinkage factors contaminate the `E_Δ` bias term.** `E_Δ`'s first argument is `|Δ_T16 − Δ_T8_bar|`, but by C-8 the paired differences at `T16` and `T8_ab` carry **different deterministic scale factors** (`1600/1601` versus `800/801`). That term therefore mixes a genuine Monte-Carlo discrepancy with a deterministic normalisation-scale discrepancy, and does so in the direction of **inflating** `E_Δ`. | **Named, not designed around.** No de-biasing, rescaling or basis-harmonisation is applied: the error functional is transcribed from the accepted arm-level construction (§3.2.2) and the estimator of record is inherited (C-8). The consequence — a modestly conservative `E_Δ`, pushing marginal cases toward `INDETERMINATE_MC` rather than toward a false `MATERIAL` — is disclosed with the results rather than corrected. It is a further instance of the same A5-i inheritance and is discharged by the same upstream repair. |
| **C-17** | **G-L4-8's promotion to blocking creates a route in which LOC4 can neither be promoted nor discharge the mandatory robustness.** If the extended `(β_Occ, δ_occ)` block is near-singular, the LOC4 arm produces no paper-facing magnitude (§5.3), so LOC4 cannot be preferred; but an uninterpretable arm also cannot certify that the baseline survived a robustness test, so I-6's mandatory-before-final-claims requirement is **not** discharged and preferred quantitative results **cannot be frozen**. The mission ends in a return with the robustness obligation still outstanding. | **Named, not designed around.** This is the correct consequence of the review's correction, not a defect in it: a robustness axis that cannot be identified has not been run. The admissible responses are all deputy-level — a different identification strategy for the occupation channels, a parsimonious grouping (I-6 §7's *useful later* two-group comparison), or a ruling that the axis is not identifiable on this sample. **None of them is a manager action, and none is taken by re-parameterising the block to force identification** (§5.3(4)). |

### 5.6 Open items — refreshed

| id | item | v3 status |
|---|---|---|
| **OL-1** | LOC4 Path-B ruling text | **CLOSED** in v2. `JMP_LOC4_pathB_ruling_v1.md`; reconciled clause-by-clause at §6; errata at §6.4 |
| **OL-4** | Materiality thresholds on differences | **CLOSED** in v2 by deputy Part B |
| **OL-2** | `δ_occ` bound `B` | **CLOSED in v3.** Frozen at §1.5: `B = ceil(log_range_L) = 4.0`, slack exactly `ceil(L) − L`, fixed before estimation, derived from a bitwise-verified frozen-box field. No discretion survives |
| **OL-8** | Block replicate index for `{Δ_T,b}` | **CLOSED in v3.** §3.2.1: `T16`; four `T12_-b`; six `T8_ab` |
| **OL-3** | Four-leg convergence leg definitions and the class rule for leg (c) | **OPEN — BLOCKING.** NA-on-this-record; transcription from the E3 chain |
| **OL-5** | `Z` closed-form support (§5.4, SA-5) | **OPEN — BLOCKING before any pricing** |
| **OL-6** | EUROMOD occupation-invariance (G-L4-6) | **OPEN — BLOCKING.** Under the rider it gates *every* difference verdict (C-14) |
| **OL-7** | Dependency on the CV1 return disposition | **OPEN — tracked.** Per the corrected C-8, an upstream estimator repair forces a **re-run** of the comparison |
| **OL-9** | `IQR_W1_baseline`, required to pin `S_k0` | **OPEN — transcription at execution.** `S_k0` is known only to be at least `1396.13` |
| **OL-10** | Errata pins: stale `docs/design_notes/` path (ERR-1); rulings-register byte-identity reconciliation (ERR-2) | **OPEN — housekeeping, resolved at freeze** |
| **OL-11** | Pre-registered statement of the paper's qualitative conclusion, to make M-6 decidable (C-13) | **OPEN — BLOCKING before execution** |
| **OL-12** | **Transcription of the inherited curvature battery's tier boundaries and rank/eigenvalue criteria**, required to operationalise the strengthened G-L4-8 (SA-10, C-17) | **OPEN — BLOCKING before execution. New in v3.** The certified fit records `condition 473,932` as *clean tier* but the tier boundary itself is not on this record; without it, "near-singular" is not decidable, and inventing a boundary is prohibited |

---

## 6. PATH-B RECONCILIATION

*(carried from v2 intact — explicitly accepted by the review)*

### 6.1 The I-6 §4 robustness contract, clause by clause

| I-6 §4 clause | where satisfied | verdict |
|---|---|---|
| "use the existing LOC4 grouping definition" | §1.1 — the four-category task-group collapse of I-3 §6; no alternative grouping constructed or searched | **SATISFIED** |
| "change only the pre-registered wage-density component" | §1.3 — the only form change is `μ_i(X) → μ_i(X) + δ_occ(k)` inside `O^W`; §1.6 enumerates everything else frozen; G-L4-3/4/5 verify no leakage into proposal, geometry or support | **SATISFIED at the level of model form**; §6.2 for coefficients |
| "preserve the sample" | §1.6 — N = 1,555, France 2016 singles, 101 alternatives/hh, successor_v2 pins re-hashed fail-closed | **SATISFIED** |
| "preserve the utility specification" | §1.6; §6.2 | **SATISFIED** |
| "preserve the access index" | §1.6 — `O^E` and `O^Occ` forms frozen | **SATISFIED** |
| "preserve the tax-benefit mapping" | §1.6 and **G-L4-6** | **SATISFIED, conditional on OL-6** |
| "preserve the welfare metric, inequality index and decomposition rule" | §1.6; §0.1 measure roles unchanged; decomposition architecture untouched | **SATISFIED** |
| "document whether mean and/or dispersion changes are introduced" | §1.3 — **mean (location) only; σ shared; no dispersion change** | **SATISFIED** |
| "prevent double counting between occupation-access coefficients and wage-density shifts" | §6.3 | **ANSWERED** |
| "compare the same headline welfare and decomposition outputs" | §3.7 — W1 PRIMARY with W3 validation; identical functionals on both arms through the same code paths on the same nodes under CRN | **SATISFIED** |

**The four prohibited additions, each explicitly absent:**

| prohibited addition | status |
|---|---|
| **sex-specific occupation densities** | **ABSENT.** `δ_occ` gender-pooled, `K = 3`; v1's `K = 6` alternative is foreclosed by this clause |
| **industry** | **ABSENT.** No `lindi`, no NACE. I-3 §6's naming rule observed: the layer is **occupation opportunity**, never sector opportunity. I-6 §6 defers `lindi` |
| **external regional covariates** | **ABSENT.** None added. `β_gsur` and the `drgn*` coding are **carried unchanged** from the certified access block — carrying an existing coefficient is not adding a covariate. The `M2` axis is untouched |
| **alternative grouping searches** | **ABSENT.** One grouping fixed ex ante, reference fixed at `k = 1`. No search, no selection. I-6 §7's two-group comparison is *useful later* and **not** authorised here |

### 6.2 The re-estimation reconciliation (I-6 §3 versus §4) — C-11

I-6 §3 is headed **"Frozen baseline"** and governs **"the first welfare prototype"** — the M08 baseline mission, complete and closed. I-6 §4 governs a **different** mission, "the first robustness after a successful baseline welfare prototype", whose defining act is to "change only the pre-registered wage-density component." A wage-density component cannot be *changed* without estimating the coordinates of the changed density; a `δ_occ` that is not estimated is not a four-density model. I-6 §6's sequencing confirms the two are distinct steps.

**The operative distinction is form versus coefficients.** I-6 §4's preservation list — sample, utility specification, access index, tax-benefit mapping, welfare metric, inequality index, decomposition rule — is a list of **specifications and mappings**, i.e. functional forms and fixed objects, not fitted numerals. A partially-frozen refit would be a maximum-likelihood estimate of nothing and would produce a vector that is neither the baseline nor a converged LOC4 optimum.

**Recorded as an incoherence risk, not resolved by fiat.** If the deputy reads I-6 §3 as binding on the robustness mission too, **LOC4 as specified is not executable**, and that is a **return** — not something to be worked around by profiling, pinning, or a two-step.

### 6.3 The double-counting clause, answered

**The clause:** "prevent double counting between occupation-access coefficients and wage-density shifts" (I-6 §4).

**The answer is an identification argument, not a restriction.** Occupation enters through two economically distinct channels:

- **`β_occ_k` — occupation as *availability*.** In `O^Occ` it shifts how much of occupation `k` is *offered*, **uniformly in the wage**: how many such jobs are there?
- **`δ_occ(k)` — occupation as *price*.** In `O^W` it shifts *where the wage distribution sits within* occupation `k`, with an effect on the log-density that is **not uniform in the wage**: what do such jobs pay?

Double counting would require the two coordinates to move the same object. They do not:

```
Δ log f_W  =  δ_occ(k)·( log w − μ_i ) / σ²   −   δ_occ(k)² / (2σ²)
```

The **constant term** — the part that would double-count — is **perfectly collinear with `β_occ_k` and absorbed by it**. It is not double-counted; it is *assigned*, unambiguously, to the access channel. What remains and identifies `δ_occ` is the **`w`-interaction**, a pattern `β_occ_k` cannot produce. **The separating variation is within-occupation wage variation, and only that.** This is why the design does not pin, drop or restrict `β_occ_k`: the collinear direction is already assigned by construction.

**Verification, not assertion — and now blocking.** **G-L4-8** measures the realised separation, **read jointly with the extended block's curvature, rank and conditioning evidence** (§5.3). **Near-degeneracy is no longer a reportable finding alone: it blocks paper-facing LOC4 magnitudes and returns the mission** (C-17). Pinning `β_occ_k` to force separation would silently change the estimand and fail the rider's estimand-comparability gate, voiding every difference verdict. The honest response to a degenerate fit is to report and return it; the dishonest response is to constrain it away.

Shared σ (§1.3) is part of the answer: occupation-specific `σ_k` would introduce a *second* occupation-indexed channel in the wage block and the clean assignment above would fail. Excluding dispersion is not only I-6-compliant scoping; it is what keeps the double-counting answer valid.

### 6.4 Errata recorded

| id | erratum | correction |
|---|---|---|
| **ERR-1** | **Stale path in the Phase-5 memo.** The Phase-5 memo cites the LOC4 Path-B ruling at a `docs/design_notes/` path. That path is stale; the ruling of record is `JMP_LOC4_pathB_ruling_v1.md` | The citation is corrected to the located file. The located ruling carries **no `Target repository path` field of its own**, so its canonical location must be **pinned at freeze**, not inferred (**OL-10**) |
| **ERR-2** | **Rulings-register byte-identity note.** The register carries a byte-identity note for this ruling. No sha256 accompanied the attachment, so byte-identity between the register's referent and the located file **has not been reconciled** | The sha256 of `JMP_LOC4_pathB_ruling_v1.md` is computed and reconciled against the register's note **at freeze**, before v3 is committed, per the standing control that every card returning a file emits its sha256 in the same message. Until then §6 is read from the attached text (**OL-10**) |

Neither erratum changes any substantive clause of §6.1–§6.3.

---

## OUTPUT DISCIPLINE

**Mission ID:** JMP-M08 · LOC4 four-density robustness (design v3, narrow corrective revision).

**Authoritative inputs:** I-1 … I-8 as tabled, with sha256 pins carried in-line where the instruments carry them. Governing revision authority: **Goal-1 R-145.2** over the independent review of v2.

**Decisions made in v3 (six mandated corrections plus two A1 disclosures; nothing else reopened):**

1. **M-5 replaced** — an **arm-to-arm** test of the components' qualitative configuration per paired basis, `S_{c,b}` and `O_{cd,b}` as defined at §3.5.2, with a three-valued exact-float64 sign convention (`sgn(0) = 0` as its own class, exact ties their own class, fixed operand order, no tolerance), MATERIAL on unanimity of full basis and every accepted replicate, IMMATERIAL on universal absence, INDETERMINATE_MC on disagreement. The v2 Δ-ordering formulation is withdrawn.
2. **M-5 propagated** through §3.7 and §4.1–§4.5, with an explicit carve-out from the `|Δ̂| ∓ E_Δ` band rule, and **C-9's language corrected**.
3. **`E_Δ` transcribed exactly** from the accepted arm-level construction (`u6f_functionals16_v1.json`, `step3_functionals`, `threshold_set_of_record`), applied to the paired differences over `T16`, the six `T8_ab` and the four `T12_-b`: `SE_MC(Δ) = sqrt[(3/4)·Σ_b(Δ_T12_-b − Δ_T12_bar)²]`, `E_Δ = max(|Δ_T16 − Δ_T8_bar|, 1.96·SE_MC(Δ))`. No constant invented or re-derived.
4. **C-8 corrected** — the deterministic chosen-node **numerator** cancels exactly under bitwise node-0 identity; the **`n/(n+1)` normalisation factor does not** (`1600/1601` at `T16`, `1200/1201` at `T12`, `800/801` at `T8`); LOC4 inherits the estimator of record regardless; an upstream repair forces a re-run. Consequence for the `E_Δ` bias term named as C-16.
5. **G-L4-8 strengthened** — read jointly with the inherited curvature/rank/conditioning battery on the extended `(β_Occ, δ_occ)` block; a near-singular block **blocks paper-facing LOC4 welfare magnitudes**, issues no verdict in either direction, discharges no robustness obligation, and returns (C-17). Re-parameterisation to force identification is prohibited.
6. **`δ_occ` bound frozen** — `B = ceil(log_range_L) = ceil(3.9609003763945605) = 4.0`, slack exactly `ceil(L) − L`, derived from a bitwise-verified frozen-box field, fixed **before** estimation. No "with slack" discretion survives.

**A1 disclosures adopted:** the §3.2 overstatement softened — combining arm bands **ignores the positive CRN covariance and therefore generally overstates uncertainty under the intended paired design**, with the prohibition resting on the deputy mandate rather than on a universal direction; and the **partial-CRN branch marked as a diagnostic regime**, not the same full-CRN experiment — outputs labelled diagnostic, `E_Δ` not presentable as a CRN difference band, no materiality verdict without deputy disposition.

**Unresolved decisions:** **OL-3** (four-leg definitions), **OL-5** (`Z` closed form, before pricing), **OL-6** (EUROMOD occupation-invariance; gates every difference verdict), **OL-11** (pre-registered qualitative conclusion), **OL-12** (curvature tier boundaries for the strengthened G-L4-8) — all BLOCKING; OL-7 (CV1 disposition, now a re-run dependency), OL-9 (`IQR_W1_baseline`), OL-10 (errata pins). **Closed:** OL-1, OL-4 (in v2); **OL-2, OL-8 (in v3)**.

**Exact output filename:** `docs/Missions/JMP_M08_LOC4_robustness_design_v3.md`
**Preserved history:** `docs/Missions/JMP_M08_LOC4_robustness_design_v2.md` and `..._v1.md`, both immutable.

**Status:** PROPOSED-PENDING-FREEZE.

**Next authorised action:** submit v3 against the six mandated corrections for freeze. On freeze, **execute LOC4 autonomously** — subject to the five blocking open items being discharged first, none of which is a matter of manager discretion. Return to the deputy if LOC4 difference precision is **indeterminate on a headline threshold**, if **M-5 returns MATERIAL or INDETERMINATE_MC**, if the run falls into the **partial-CRN diagnostic regime**, if **G-L4-8 blocks**, if **disclosure fails**, if a **package change** is required, or if the **preferred specification cannot be selected**.

**Statement.** No welfare number, decomposition number, inequality index, parameter value, priced node, re-estimation, new draw, or EUROMOD execution was produced. Every numeral is transcribed from a named record with a citation, or — in the single marked case of §1.5 — is the value of a frozen deterministic formula evaluated on one bitwise-verified transcribed constant. Every threshold is transcribed from deputy Part B or Path-B §5 with both instruments cited; the `E_Δ` error functional is transcribed from the accepted arm-level construction with its source field named. **No threshold, cutoff, tolerance, sign-band or denominator was invented**, and every gap in the record is named as an open item rather than filled.