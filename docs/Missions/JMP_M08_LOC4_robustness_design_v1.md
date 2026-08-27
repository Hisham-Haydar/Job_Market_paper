# JMP-M08 — LOC4 FOUR-DENSITY ROBUSTNESS: DESIGN MEMO v1

**Mission ID:** JMP-M08 · LOC4 (pre-registered first robustness axis)
**Class:** Design memo. **PROPOSED-PENDING-GOAL1-FREEZE.**
**Target repository path:** `docs/Missions/JMP_M08_LOC4_robustness_design_v1.md`
**Date:** 2026-08-26
**Authorising instrument:** deputy CV ruling §s10, which authorises LOC4 to begin upon acceptance of the M08 prototype under limited MC precision (that acceptance has occurred).

**Authoritative inputs (all numerals below are transcribed from these, with citation; nothing is recomputed).**

| # | instrument | role here |
|---|---|---|
| I-1 | `JMP_M08_welfare_input_handoff_v2.md` (FROZEN; Goal-1 R-110) | parameter source θ̂_margqh-v2; inference conventions; corrected W-4 set; frozen five-scenario S-10; the eight disclosures; the prohibited-claims list; rebinding obligations and gate order (§6.5 places LOC4 last and mandatory) |
| I-2 | `FR_P2a_m08_u6cv1_stageA_binding_and_deputy_return_v1.md` | the recorded schema of the 16x welfare stack: `q_W` family and `μ_ik`, `q_H` marginal, the frozen box, `S_i`, `n`, `n_k`, the A-4 functional table, the `threshold_set_of_record` |
| I-3 | `RURO_model_spec_contract_v2_stijn_enhanced.md` | the structural block definitions (§9 `O^W`, §10 `O^Occ`, §15 identification, §16–17 parameters/bounds, §18 exclusion table, §19 `M3` extension ladder) |
| I-4 | M08 prototype closure `M08_BASELINE_PROTOTYPE_LIMITED_MC_PRECISION` | the headline set {W1 mean, W1 Gini, φ_A, φ_B} + qualitative sign/order claims |
| I-5 | deputy CV ruling §s10 | the comparison instrument: CRN; MC error on **LOC4-minus-baseline differences**; existing LOC4 materiality thresholds applied to those differences; interval crossing a boundary ⇒ indeterminate ⇒ return |
| I-6 | LOC4 **Path-B ruling**, carried forward unchanged at I-1 §0 (v1 §2.3) | mandatory-before-final-quantitative-claims status. **Its text is not in this mission's attachment set**; see open item **OL-1**. |

**No computation, no code, no new draw, no welfare number, no parameter value, no EUROMOD execution is produced or implied by this memo.**

---

## 1. THE VARIANT

### 1.1 Name and object

**LOC4 four-density robustness** = the `M3` extension of I-3 §19 ("`O^W` conditional on `Occ`: occupation-specific Mincer means, shared σ"), instantiated on the **LOC4 four-category task-group collapse** of I-3 §6 (1 routine-manual, 2 nonroutine-manual, 3 routine-cognitive, 4 nonroutine-cognitive). "Four-density" is literal: the single structural wage-opportunity density becomes **four occupation-conditional wage densities sharing one σ**, one per LOC4 category.

### 1.2 The baseline it perturbs, stated exactly

The certified structural wage block of θ̂_margqh-v2 is I-3 §9:

```
log f_W(w | X)  =  − 0.5·z²  − log σ  − log w
z               =  ( log w − μ_i(X) ) / σ
μ_i(X)          =  β_w0 + β_w_educL·educL + β_w_educH·educH
                     + β_w_pexp·pexp + β_w_pexp2·pexp²
```

**`δ_occ` is coordinate-empty in θ̂.** The structural `μ_i(X)` carries **no occupation term**; occupation enters the certified model **only** through `O^Occ` (I-3 §10, §18: "occupation must enter `O^Occ` only, never `U`, never `O^H`, never `O^W`").

This must not be confused with the *proposal*. I-2 §4 binds, from `scripts/pilot/pilot_wage_draw.py:174-188` via `m08_qw_streams.BaseComponent.factors`, that the **proposal** wage mean is
`PW._build_log_wage_mean(educL, educH, pexp, pexp², loc4, year_tag, coef, use_year_controls)` — i.e. `μ_ik` in the proposal **is** occupation-conditional, drawn from the frozen pilot mincer payload, with **σ a single scalar common across occupations** (`mincer["wage_model_W1"]["sigma"]`; I-2 §4: "the memo writes `σ_{i,k}`; the schema carries `σ`"). The asymmetry — occupation shifts where wages are *drawn from*, but not where the estimated model *believes* they are offered — is a property of the accepted baseline, not a discovery of this mission. It is recorded here as coherence finding **C-5** (§5.5) and is the substantive motivation for the axis.

### 1.3 Coordinates added

```
μ_i(X, k)  =  μ_i(X)  +  δ_occ(k)  ,      k ∈ {1,2,3,4} = LOC4 ,
δ_occ(1)   ≡  0                            (reference category FIXED, routine-manual, per I-3 §15.2)
σ          unchanged and SHARED across k   (per I-3 §19, M3: "shared σ")
```

Free coordinates added: `delta_occ_2`, `delta_occ_3`, `delta_occ_4`.

**K is Stage-A-bound, not asserted here.** The vector is `47 + K`. `K = 3` if the certified wage block is gender-pooled on the singles P2a sample; `K = 6` if it is gender-split (`_sm` / `_sf`). The available evidence points to gender-pooled — I-1 §3 names the wage coordinate `beta_w_pexp2` **unsuffixed** while every leisure coordinate carries `_sm` / `_sf` — but `K` must be bound from `e4_parameter_table.csv` (sha256 `21a05fb569da1d776fa166549f847ef5115a5a1d47f373f8edcdaa7d641d78c3`) at Stage A of execution, per standing practice 13 (invariant lists derive from the recorded schema, never from memory). **Recommended baseline: `K = 3`, gender-pooled, matching the certified wage block's own gender convention whatever it is.** Rejected alternative: gender-split `δ_occ` (`K = 6`) — rejected at this stage because it compounds a first robustness axis with a second (gender interaction) and would make a material verdict uninterpretable as to which change drove it.

### 1.4 Identification source

**The claim: `δ_occ` is identified by within-occupation wage variation, and only by that.** The argument must be recorded pre-execution because it is the single non-obvious identification question on this axis.

Write the added structural log-density contribution at a working alternative in occupation `k` with wage `w`:

```
Δ log f_W  =  δ_occ(k)·( log w − μ_i ) / σ²   −   δ_occ(k)² / (2σ²)
                    ↑ w-dependent                    ↑ constant in w, occupation-indexed
```

The second term is **constant within occupation `k`** and therefore **perfectly collinear with `β_occ_k`** of the certified `O^Occ` block. It contributes nothing: any level shift it induces is absorbed by the re-estimated `β_occ_k`. What remains — and what identifies `δ_occ` — is the **first term**, which varies with `log w` *within* occupation `k`. Concretely: `δ_occ` is identified because occupation-`k` alternatives at high wages and occupation-`k` alternatives at low wages receive *different* index adjustments, whereas `β_occ_k` adjusts them identically. The identifying variation is the **within-occupation dispersion of sampled log wages, interacted with the occupation label**, on the France 2016 singles sample (N = 1,555; 101 alternatives per household, I-1 §1).

Three consequences, all binding:

1. **Shared σ is load-bearing, not cosmetic.** With occupation-specific `σ_k`, the `w`-dependent term acquires a second occupation-indexed channel and the separation argument above no longer isolates a single coordinate. `σ_k` is **out of scope** for LOC4 and is a distinct later axis.
2. **The `O^Occ` double-counting warning of I-3 §18 is deliberately entered, not evaded.** I-3 §18 permits occupation in a second block "only as a deliberate later extension after `M0`–`M3` are stable"; §19 names this extension `M3`. LOC4 *is* that extension. The design therefore does **not** drop or restrict `β_occ_k`: both blocks stay free, and the separation rests entirely on the `w`-interaction. If the fit cannot separate them, that is a **finding** (§5.5, C-4) — the design does not respond by pinning `β_occ_k`.
3. **Reference-category asymmetry.** `δ_occ(1) ≡ 0` and the `O^Occ` reference are the *same* category (I-3 §15.2, §15.6). Only contrasts are identified in both blocks; no statement about the level of either is admissible.

### 1.5 Bounds

`δ_occ(k) ∈ [−B, +B]`, symmetric, `B` a single scalar common to all `k`, **recorded pre-execution**.

`B` is **not fixed in this memo** (open item **OL-2**), because the ROLE prohibits numerals beyond transcribed constants and because the principled rule requires reading the sample. **Recommended rule at freeze:** set `B` so that the implied multiplicative wage-location bracket strictly contains every observed raw between-LOC4 log-wage gap on the singles sample with slack, i.e. so that `B` is economically non-binding and any bound-hit is diagnostic of a fit pathology rather than of a tight box. Rejected alternatives: (i) `B` tied to `σ̂` — rejected because it makes the box a function of the very block being perturbed; (ii) unbounded `δ_occ` — rejected because I-3 §17 requires a bound-hit diagnostic for every coordinate and the four-leg convergence standard needs a compact admissible set.

Bound-hit handling is not new machinery: a `δ_occ` coordinate active at a bound is treated exactly as `beta_l_age2_sm` / `beta_l_age2_sf` are treated at I-1 §2.1 — excluded from the covariance by construction, SE/z/p reported as **literal NA**, never a numeral, never blank, never zero, never imputed downstream.

### 1.6 What does NOT change — exhaustive

| object | status under LOC4 | source |
|---|---|---|
| Leisure / preference block (`β_c`, `θ_c`, `β_l0_*`, `θ_l_*`, `β_l_age*`, `β_l_nkids_sf`) | functional form frozen; coordinates re-estimated | I-3 §16 |
| Access block `O^E` / hours-opportunity (`β_E`, `β_pt1`, `β_pt2`, `β_ft`, `β_gsur`, `β_E_educH`) | functional form frozen; coordinates re-estimated | I-3 §8, §16 |
| `O^Occ` block (`β_occ_k`) | functional form frozen; coordinates re-estimated; **not pinned** | I-3 §10; §1.4(2) above |
| Hours bands / the `q_H` marginal (6 components, 9-piece piecewise-constant partition; PT1 .15, PT2 .10, F35 .24, FT .20, LH .10, BG .21) | **bitwise frozen** | I-2 §3 |
| Employment margin (`π0 = 0.10` on `q`, `π0_r = 0.50` on `r`; design working share `0.75·0.90 + 0.25·0.50 = 0.80`) | **bitwise frozen** | I-2 §4 |
| Defensive mixture `λ = 0.25`; log-uniform `r_W`; uniform `r_Occ` over 4; uniform `r_H` | **bitwise frozen** | I-2 §2(i), §4 |
| Job-space geometry: `n = 1600`, `n_k = 400` (300 base / 100 defensive), `S_i = 1601 / 1201 / 801`, node 0 = chosen row at zero correction, 4 superblocks | **bitwise frozen** | I-2 §5.1, §6.1, §6.2 |
| Proposal convention (`log_q_H`, `log_prior`, `prior` — the corrected marginal/MIS convention) | **bitwise frozen**; LOC4 touches the structural index only, never the proposal | I-1 §1.2 |
| The pilot mincer payload and `q^W` (including its own occupation-conditional `μ_ik` and scalar `σ`) | **bitwise frozen** — see §3.2 | I-2 §4 |
| EUROMOD mapping (`ils_dispy`, FR 2015–2017 input files, `drgn1` regional coding) | **bitwise frozen**, conditional on gate **G-L4-6** (§5.3) | I-3 §14.3 |
| Estimation sample and draw geometry (N = 1,555; 101 alternatives per household; successor_v2 stem pins of I-1 §1.2) | **bitwise frozen**, re-hashed fail-closed before opening | I-1 §1.2 |
| Scope: singles P2a only — no couples, no pooled years, no `dclaborsupply` change (gitlink `27756a06`) | **unchanged** | I-1 §6.6 |

---

## 2. ESTIMATION PLAN

### 2.1 What is estimated

**Full re-estimation of the entire `47 + K` vector** under the corrected marginal/MIS proposal convention, on the successor_v2 frame, from the same 101-alternative draws. Not a profiled fit, not a two-step, not a warm-started perturbation of the certified block only: every preference, access, hours, wage and occupation coordinate is free simultaneously, because `δ_occ` is not separable from `β_occ_k` or from the leisure block by construction (§1.4).

The 10 pinned coordinates stay pinned. The two upper-bound-active leisure coordinates (`beta_l_age2_sm`, `beta_l_age2_sf`) are **not** pre-set to their certified values: they are freed and allowed to re-locate, and whether they remain active at `+1.0` is a reported diagnostic. Pre-setting them would convert a robustness fit into a constrained refit of a different estimand.

**Prohibited:** mixing θ̂_margqh-v2 coordinates with LOC4 coordinates in any single evaluated vector other than as a documented warm start whose end point is a converged optimum in its own right. The suspended joint-convention estimate (theta-bytes `c024b893…f0580d`) is **never** a parameter source, warm start, or robustness arm here (I-1 §1.3) — LOC4 is run against the corrected baseline only.

### 2.2 Convergence standard

The **amended four-leg convergence standard** applies unchanged in form, with the **deputy convergence-class rule governing leg (c)**.

**The four legs' definitions are not transcribable from this mission's attachment set.** They live in the E3 instrument chain (`FR_P2a_m08e_E3_reestimation_note_v2.md`, sha256 `970eda4c0d3dcc140b1608159c64fff420eb8395964e2e3b34f500c1a660a5f5`) and its `convergence_records.json` (sha256 `9cf81c03e3e7e0ec58d87582f9454d5b076b53bccfe8d3154188878db926b50e`), neither of which is attached. Per evidence discipline they are entered here as **NA-on-this-record** and are a mandatory transcription at freeze — open item **OL-3**. What *is* fixed now:

- the standard is applied **in full**, in its amended four-leg form, to the LOC4 fit, with no relaxation for the higher parameter count;
- leg (c) is adjudicated by the **deputy convergence-class rule**, i.e. the LOC4 fit is assigned a convergence class and that class is reported, not collapsed to pass/fail;
- the target verdict is the analogue of `E3-CONVERGED-SINGLE-OPTIMUM`. **A LOC4 fit that does not attain a single-optimum verdict is a return, not a headline.** A multi-optimum LOC4 surface is itself a substantive finding about `δ_occ`/`β_occ_k` separation (§1.4) and is reported as such.

### 2.3 Inference

Per Phase-4/5 conventions (I-1 §2), **on the new free set**:

- household-cluster **CR1**, `G = N = 1,555` (one independent likelihood contribution per household, notwithstanding 101 rows per household in the sampled denominator);
- finite-sample factor `c = (G/(G−1))·((N−1)/(N−K_free))`, i.e. `1555/(1555 − K_free)`. **`K_free` changes**, so `c` changes; the certified numeral `1555/1520 = 1.0230263157894737` is the *baseline* value and **may not be carried across**. Recomputing `c` is a required step of the LOC4 fit, not an inherited constant;
- covariance dimension = the LOC4 **interior** set: certified 35 interior, plus the interior members of `δ_occ`, less any coordinate that becomes bound-active. Any bound-active coordinate — leisure or `δ_occ` — is excluded from the covariance by construction and reported literal NA (I-1 §2.1);
- the standing inference-scope disclosure (I-1 §4, disclosure 7) and the prohibited-claims list (I-1 §5) bind LOC4 output exactly as they bind baseline output. In particular: **`δ_occ` estimates may not be described as a causal occupational wage premium**, and baseline-versus-LOC4 coefficient changes may not be described as statistically significant differences — the two vectors estimate different likelihood estimands and no covariance for their difference is constructed (I-1 §5, fifth bullet, applied here verbatim to the specification pair).

### 2.4 W-4 diagnostic and the S-10 rule

The corrected W-4 warning (non-gating) is run on the LOC4 free set. The certified flagged set is **{ `beta_l0_sm`, `beta_l0_sf`, `beta_l_nkids_sf` }** (I-1 §2.2), with `beta_w_pexp2` no longer flagged.

**The rule, stated exactly:**

> **No S-10 re-derivation unless the flagged set changes.** If the LOC4 W-4 flagged **membership** is identical to `{ beta_l0_sm, beta_l0_sf, beta_l_nkids_sf }`, the frozen five-scenario S-10 design of I-1 §3 is **not reopened** — not its coordinate set, not its D15 perturbation rule, not its scenario vectors — and **no S-10 battery is run on the LOC4 arm at all** within this mission.
>
> If the flagged membership **changes** in either direction (a certified coordinate drops out, or any coordinate — including a `δ_occ` coordinate — is newly flagged), that is **a return, not an autonomous re-derivation**. The five-scenario set is frozen by deputy ruling §4 and the final disposition at R-109 (I-1 §3); altering it is a numerical-semantics change and therefore a deputy escalation.

**Why no S-10 on the LOC4 arm in the headline comparison.** The headline object is a *difference in point welfare objects between two specifications*, computed under CRN. S-10 is a Tier-1 deterministic sensitivity battery around a point estimate; running it on both arms would produce a 5 × 2 grid whose cross-arm differences confound specification effect with perturbation effect, and whose LOC4 Δ_j would mechanically differ from the frozen baseline Δ_j because they are half-robust-SE quantities computed from a different covariance. LOC4 differences are therefore taken at **scenario 1 (the corrected baseline vector) on the baseline arm, and at θ̂^LOC4 on the LOC4 arm**. S-10 on the LOC4 arm is triggered **only** in decision-tree branch B (§4.2), i.e. only if LOC4 is promoted, and only under a deputy disposition that re-derives the frozen set.

The standing S-10 disclosure applies throughout: the battery is Tier-1 deterministic sensitivity — not a confidence region, not a bootstrap, not a posterior, not comprehensive parameter-uncertainty propagation, and it does not produce welfare confidence intervals (I-1 §3, §4 disclosure 5, §5 sixth bullet).

---

## 3. THE COMPARISON DESIGN (the deputy §s10 instrument)

### 3.1 What is compared, in order

Every reported object is a **difference**, `Δ = LOC4 − baseline`, never a pair of levels presented for eyeballing.

**Tier 1 — the headline set** (the M08 prototype closure's own set, I-4), reported first and alone:

| # | object | baseline `T16` | baseline `E_T` | baseline ratio | class |
|---|---|---|---|---|---|
| H-1 | `W1_mean` | `1396.13` | `3.02142` | `0.866` | mean_median |
| H-2 | `W1_gini` | `0.173955` | `0.000869933` | `0.696` | gini |
| H-3 | `W1_phi_A_level` (φ_A) | `0.00617588` | `0.000468934` | `0.375` | component_level |
| H-4 | `W1_phi_B_level` (φ_B) | `0.0114346` | `0.00119598` | `0.957` | component_level |

(all four transcribed from I-2 §6.4; all four **pass** the level thresholds — this is exactly why they, and only they, are the closure's headline set.)

Plus the closure's **qualitative sign/order claims**: the sign of each headline object's difference, and the ordering `φ_A` vs `φ_B`, compared between arms.

**Tier 2 — the banded set:** the remaining W1 functionals of I-2 §6.4 (`W1_median`, the `I_{·}` family, `φ_P`, `R_bg`, `φ_A+φ_B`, the normalized-contribution family including `s_opp`), plus W4 and W6. Tier 2 is reported **banded and explicitly non-headline**, and inherits the precision constraint of coherence finding **C-3** (§5.5): 13 of 22 W1 functionals, 17 of 22 W4 and 17 of 22 W6 already fail their level thresholds on the baseline arm alone (`n_fail: 47` of 66, I-2 §6.4). A difference between two arms of which at least one fails precision on a functional **cannot be certified material on that functional**.

### 3.2 CRN construction — where it is exact, where only partial

**The design intent:** `δ_occ` enters the **structural index only**. It does not enter the proposal `q^W`, the proposal `q_H` marginal, `q_Occ`, `log_prior`, the employment margin, the mixture weight `λ`, or the node identities. If that holds, the two arms are evaluated on **the same nodes, with the same importance weights' denominator**, and the difference removes essentially all of the shared Monte-Carlo noise.

**Where CRN is exact — the base half (75% of nodes), conditional on gate G-L4-1.** `q^W`'s wage mean is built from the frozen pilot mincer payload (`PW._build_log_wage_mean(…, coef, …)`), not from θ (I-2 §4). If the base draw path reads no coordinate of θ, then across the two arms these are **bitwise identical**: `working`, `loc4`, `hours`, `wage`, `log_q_E`, `log_q_H`, `log_q_W`, `log_q_Occ`, `log_prior`, `log_q_base`, `stream_seed`, `base_position`, `component_label`, `in_support_box`, the priced consumption, node 0 and its accepted **zero** correction, superblock membership, and `S_i`. Exactness is **verified**, not assumed, by the bitwise-column comparison already established as the instrument of record (I-2 §2(iii): 17 of 17 columns bitwise equal, `columns_not_bitwise: []`).

**Where CRN is at risk — the defensive half (25% of nodes): the frozen box.** `DefensiveComponent.draw` maps its uniforms **through** the box (I-2 §2(ii)), so any box move regenerates every defensive node and voids the pairing on that half. And the record establishes that **the box is evaluated at θ and has moved before**: `u6e_ladder8_v1.json` carries `box_at_theta_v2.box_moved: true`, `box_at_theta_v2.delta_log_L: 0.06107235168894798`, and the rebind re-priced `311000 = 1555 × 200` defensive nodes with `additional_nodes_due_to_box_move: 155500` (I-2 §2(ii)).

**Therefore box invariance under `δ_occ` may not be assumed.** It is a Stage-A binding of the execution mission, and it forks the design:

| branch | condition | CRN status | consequence for the difference SE |
|---|---|---|---|
| **CRN-exact** | box at θ̂^LOC4 is bitwise identical to `box_hash_sha256 = 67ef22b3742ccc04a25c377cec60e18478b6fd07e539c0340497a274c0ce2c52` / `float64_bytes_sha256 = 8e44ec2a926aa06fd844a0be97fdbfdc29d3299ca1a7b3a1eb46a7191ae6e361` | exact on **all** nodes; `h_min/h_max = 5.0/70.0`, `w_min/w_max = 1.9411632533361265/101.91995852573758`, `log_range_L = 3.9609003763945605` all unchanged | difference SE is the **paired** SE; the shared component of MC error cancels; this is the design's intended regime and the reason LOC4 is affordable |
| **CRN-partial** | box moves at θ̂^LOC4 | exact on the base 75%; **broken** on the defensive 25% (nodes regenerate) | the difference is paired on three quarters of the stack and unpaired on one quarter; the unpaired quarter contributes its **full** variance to `Var(Δ)`, with no cancellation. **The difference SE must be reported under the partial pairing and labelled as such** — it may not be presented as a CRN difference SE |
| **halt** | box moves **and** re-pricing is required | — | a box move forces EUROMOD re-pricing at the recorded scope (155,500 per defensive half; 311,000 across both). This is a cost and a custody event, not a patch: it is disclosed and the pairing loss is disclosed with it |

**No CRN repair is attempted.** Re-seeding, re-mapping, or re-using pre-move defensive uniforms to manufacture pairing is prohibited: I-2 §2(ii) establishes that pre-rebind defensive nodes do not survive anywhere in the stack, and reconstructing them would be a change to the raw estimator.

**One thing CRN does *not* buy, stated so it is not over-claimed.** Both arms are evaluated at their **own full re-estimated vectors** (§2.1). CRN pairs the *randomness*, not the *parameters*. `Δ` is therefore the effect of the **specification change as a whole** — including every induced movement in the leisure, access and `O^Occ` coordinates — and **not** the partial effect of the `δ_occ` term. Any sentence of the form "adding occupation to the wage block moves W1 mean by …" is prohibited; the admissible form is "the LOC4 specification differs from the baseline specification in W1 mean by …".

### 3.3 MC error on the differences: the block-jackknife `E_T(Δ)`

`E_T` is computed **on the difference**, using the existing leave-one-superblock-out structure (`T16` → the `T12` LOO family; `n_k = 400` per superblock, 300 base / 100 defensive, `400 ≡ 0 (mod 4)`, realised defensive fraction exactly `0.25` in every `D_k` — I-2 §6.1).

**The construction, stated to remove ambiguity:**

```
for each LOO block T12_(-b):
      Δ_(-b)  =  functional(LOC4 | T12_(-b))  −  functional(baseline | T12_(-b))     ← same b, same nodes
E_T(Δ)     =  block-jackknife of { Δ_(-b) }
```

**`E_T(Δ)` is the jackknife *of the difference*. It is emphatically not the difference of `E_T(LOC4)` and `E_T(baseline)`, nor their quadrature sum.** The latter would discard the CRN covariance term and systematically overstate the uncertainty, converting genuine material differences into indeterminates. This is a named halt: an implementation that computes `E_T(Δ)` from the two arms' separately-reported `E_T` values is a defect, not a conservative choice.

The qualitative sign/order limb transfers as: the sign of `Δ` and the `φ_A`/`φ_B` ordering must be identical in `T16` and in **every** `T12` LOO — the same "signs and ordering identical" limb as the threshold set of record (I-2 §6.4), applied to differences.

### 3.4 Materiality thresholds — TRANSCRIPTION AND A NAMED GAP

**Source instrument named:** `…_u6ffn16_U6F_FUNCTIONALS16_DONE/u6f_functionals16_v1.json`, field **`threshold_set_of_record`**, transcribed at I-2 §6.4 (with the STEP-0 correction of the pricing report for the normalized-contribution rows).

**Transcribed verbatim:**

| class | threshold of record |
|---|---|
| means / medians | `E_T / S_k ≤ 0.0025`, with `S_k = max(|mean|, |median|, IQR, 1 €)` |
| Ginis | `E_T ≤ 0.00125` |
| component levels (`φ_A`, `φ_B`, `φ_P`, `R_bg`, `φ_A+φ_B`) | own class at `E_T ≤ 0.00125` |
| normalized contributions | `E_r / S_r ≤ 0.005`, `S_r = max(1, |r_T|)`, requiring `|I(∅)| > 20·E_{I(∅)}` |
| sign / order limb | signs and ordering identical between `T16` and **every** `T12` LOO |

**The gap, stated plainly rather than papered over.** This set is a **Monte-Carlo-precision threshold set on the levels of a single estimate** — it answers "is this number resolved?", not "is this difference material?". The deputy §s10 instrument directs that "the existing LOC4 materiality thresholds" be applied to the differences. On the record available to this memo, **no LOC4-specific materiality threshold set exists as a distinct frozen instrument**; what exists is the set above. Applying it to differences is well-defined for two of the four classes and **undefined for the other two**:

| class | transfers to `Δ`? | why |
|---|---|---|
| Ginis (`E_T ≤ 0.00125`) | **yes, unambiguously** | absolute threshold, no scale denominator |
| component levels (`E_T ≤ 0.00125`) | **yes, unambiguously** | absolute threshold; covers H-3 and H-4 |
| means / medians (`E_T/S_k ≤ 0.0025`) | **NO — denominator undefined** | `S_k = max(|mean|, |median|, IQR, 1 €)` is a **level** scale. On a difference, is `S_k` the baseline arm's level scale, the LOC4 arm's, the difference's own scale, or `max(1 €, |Δ|)`? Each reading gives a different verdict on H-1. **Not adjudicable at design stage.** |
| normalized contributions (`E_r/S_r ≤ 0.005`, `S_r = max(1,|r_T|)`) | **NO — same defect** | same level-scale ambiguity, plus the side condition `|I(∅)| > 20·E_{I(∅)}` which is a property of a single arm, not of a pair |

**Per the ROLE's instruction, no numerals are proposed here to fill this gap.** It is entered as blocking open item **OL-4** for the Goal-1 freeze. Two candidate readings are recorded without selection, so the freeze has something concrete to rule on: **(R-a)** the denominator is taken from the **baseline arm's** level scale, making the threshold a fixed yardstick independent of the LOC4 result and immune to the pathology in which a LOC4 arm with a large level automatically enlarges its own tolerance; **(R-b)** the denominator is `max(1 €, |Δ|)`, making the criterion a relative-precision test of the difference itself. These have opposite failure modes and the choice is a numerical-semantics decision, hence deputy territory.

**Consequence for the mission as designed:** H-2, H-3 and H-4 (Gini, φ_A, φ_B) are testable against the transcribed thresholds **today**; **H-1 (`W1_mean`) is not testable until OL-4 is ruled**. The mission may therefore be executed to the point of producing `Δ` and `E_T(Δ)` for all four headline objects, but **the materiality verdict on H-1 is withheld pending OL-4** and the mission cannot close without it.

---

## 4. THE DECISION TREE

The instrument is: `Δ` reported with `E_T(Δ)`; the interval is `Δ ± E_T(Δ)` read against the applicable threshold; **an interval crossing a materiality boundary ⇒ indeterminate ⇒ return** (I-5).

The tree is evaluated on the **headline set first and separately**. Tier 2 does not drive the verdict; it is disclosed.

### 4.1 Branch A — IMMATERIAL

**Condition:** for every headline object, the interval `Δ ± E_T(Δ)` lies wholly inside the materiality threshold; and the qualitative sign/order claims are identical across arms and across every `T12` LOO.

**Verdict:** **the baseline specification stands.** LOC4 is a passed robustness axis, not a competing specification.

**Pipeline consequences:**

- **Rebinds:** nothing. No welfare artifact, no `q^W` object, no `Z`, no `ĝ` sampler, no coalition target, no pricing ladder rebinds.
- **Re-runs:** nothing.
- **Stays frozen:** θ̂_margqh-v2 as the sole parameter source; the frozen box; the five-scenario S-10 set; the 16x stack; the prototype closure and its headline set.
- **New obligation (this is the branch's actual output):** a **disclosure**, carried in every manuscript, notebook, table, figure and memo that reports the decomposition — that the wage block was tested against a LOC4 occupation-conditional four-density extension and that the headline welfare objects were immaterially affected, reported with `Δ` and `E_T(Δ)` in full and with the CRN status of §3.2 stated. The disclosure must state that the axis tests **occupation-conditional wage location only**, not occupation-conditional dispersion (`σ_k`), not occupation-conditional hours (`O^H | Occ`, the `M4` axis of I-3 §19), and not regional opportunity (`M2`). Immateriality on this axis is not immateriality on the occupation dimension.
- **LOC4's Path-B mandatory-before-final-claims status (I-1 §0, v1 §2.3) is discharged for this axis only**, subject to OL-1.

### 4.2 Branch B — MATERIAL

**Condition:** for at least one headline object, the interval lies wholly outside the materiality threshold; or a qualitative sign or ordering claim flips.

**Verdict:** **the preferred-specification question goes to the deputy. This is a return under §s10.** The manager does **not** select LOC4 as preferred, and does **not** select baseline as preferred, on its own authority — the choice between two converged specifications that produce materially different welfare decompositions is a numerical-semantics decision.

**Pipeline consequences:**

- **Nothing rebinds pending the deputy disposition.** The welfare pipeline is **held**, not switched. θ̂_margqh-v2 remains the parameter source of record throughout the return.
- **Stays frozen during the return:** everything. The M08 prototype closure is not withdrawn; it remains a correctly-scoped acceptance of the baseline arm.
- **The return packet carries:** the LOC4 convergence class and four-leg result; the `47 + K` parameter table with CR1 SEs on the recomputed `c`; the W-4 flagged membership; `Δ` and `E_T(Δ)` for the headline set and the banded set; the CRN status (exact / partial) with the box-hash comparison; the identification evidence on `δ_occ` versus `β_occ_k` separation (§1.4); and the coherence findings of §5.5 that fired.
- **If and only if the deputy promotes LOC4** does the full rebinding cascade of I-1 §6 execute in its stated order — rebinding → deterministic + N-test batteries (N1–N9, in full, **before any pricing**) → U6 → pricing ladder → welfare → decomposition → S-10 → LOC4 — with S-10 re-derived under a deputy-approved revision register (§2.4), and with the RUM benchmark re-estimating its own preferences under the promoted specification (I-1 §6.3; `g ≡ 1` with a retained θ̂ remains forbidden).
- **If the deputy retains baseline**, Branch A's disclosure obligation applies, **strengthened**: the disclosure must report that the axis produced a material difference and that the baseline was retained by ruling, with the LOC4 numbers shown. A material difference disclosed as immaterial is a prohibited claim.

### 4.3 Branch C — INDETERMINATE

**Condition:** for any headline object, the interval `Δ ± E_T(Δ)` **crosses** the materiality boundary; **or** the sign/order limb disagrees between `T16` and any `T12` LOO; **or** the applicable threshold is undefined (which is the current status of **H-1**, pending OL-4); **or** the LOC4 fit does not attain a single-optimum convergence verdict (§2.2).

**Verdict:** **return.** Indeterminate is a **verdict**, not a state to be resolved by re-running until it resolves.

**Pipeline consequences:**

- **Nothing rebinds. Nothing is re-run to break the tie on manager authority.** Specifically prohibited without deputy disposition: extending the ladder beyond 16x to shrink `E_T(Δ)`; re-drawing; re-seeding; dropping a headline object from the comparison; substituting a Tier-2 object for a Tier-1 one; or re-reading the threshold class of a functional to move it into an absolute-threshold class.
- **Stays frozen:** everything, as in Branch B.
- **The return states which limb was indeterminate and why**, and — where the cause is precision rather than substance — carries the cost estimate of the precision extension that would resolve it, for the deputy to authorise or decline. The M08 prototype was closed under `LIMITED_MC_PRECISION` precisely because precision was accepted as a scoped constraint; LOC4 indeterminacy caused by that same constraint is an expected outcome of the closure, not a failure of this mission.

---

## 5. FROZEN vs STAGE-A-BOUND; GATES; OPEN ITEMS; COHERENCE

### 5.1 Frozen by this design (not reopened at execution)

The variant's functional form (§1.3: additive occupation-specific wage location, shared σ, reference `k = 1` fixed); the exhaustive no-change list (§1.6); full simultaneous re-estimation with `β_occ_k` free (§2.1); the four-leg standard applied without relaxation (§2.2); the difference-only reporting rule and Tier-1/Tier-2 ordering (§3.1); the jackknife-of-the-difference construction (§3.3); the no-CRN-repair rule (§3.2); the three-branch tree with its held-pipeline semantics (§4).

### 5.2 Stage-A-bound at execution (derived from the recorded schema, never from memory — standing practice 13)

| id | item | bound from |
|---|---|---|
| SA-1 | `K` and the gender convention of the wage block | `e4_parameter_table.csv` `21a05fb5…` |
| SA-2 | The four-leg convergence standard's leg definitions and the convergence-class rule for leg (c) | E3 instrument chain; `convergence_records.json` `9cf81c03…` |
| SA-3 | Whether any object on the draw-generating path reads θ (the CRN-exactness precondition) | `m08_qw_streams` recorded schema; the 17-column bitwise instrument |
| SA-4 | The box at θ̂^LOC4 vs `box_hash_sha256 67ef22b3…` / `float64_bytes_sha256 8e44ec2a…` | `u6f_frozen_box_v1.json` |
| SA-5 | The analytic `Z` closed form and its wage-factor support (§5.4) | the normalisation ruling |
| SA-6 | `δ_occ` bound `B` and its pre-execution record | §1.5 rule, at freeze |
| SA-7 | LOC4 W-4 flagged membership | E4-analogue `step3_w4.corrected_detail` |

### 5.3 Validation gates — N-series analogues on the extended block

| gate | statement | failure handling |
|---|---|---|
| **G-L4-1** | **CRN exactness.** The 17 recorded columns are bitwise equal across arms on the base half. `columns_not_bitwise: []` required on the base half. | any non-empty list ⇒ CRN is not exact; classify and report per §3.2; a non-empty list on a column that *should not* depend on θ is a halt |
| **G-L4-2** | **Box invariance.** Both box hashes compared at θ̂^LOC4. | move ⇒ CRN-partial branch of §3.2; disclose; **never** repair |
| **G-L4-3** | **Proposal invariance.** `log_q_H`, `log_prior`, `prior`, `log_q_W`, `log_q_Occ`, `log_q_W_mixture` bitwise unchanged; the `q_H` 9-piece partition and its `unit_mass_certificate` (`exact_integral = 1/1`, `float64_integral = 1.0`, `float64_equals_one_bitwise: true`, `float64_abs_deviation = 0.0`) re-verified. | any change ⇒ the LOC4 variant has leaked into the proposal ⇒ **halt**; the variant is defined as structural-only |
| **G-L4-4** | **Geometry invariance.** `n = 1600`, `n_k = 400`, `S_i = 1601` on `T16`, node 0 present exactly once per household at zero correction, 0 node exclusions in the attained leg, 4 superblocks with realised defensive fraction exactly `0.25`. | any change ⇒ halt |
| **G-L4-5** | **Support invariance.** Zero off-box working ladder nodes on both arms, on the same rows. | non-zero ⇒ halt |
| **G-L4-6** | **EUROMOD occupation-invariance.** Confirm on the French baseline that `ils_dispy` does not depend on occupation (I-3 §14.3 explicitly requires this confirmation and does not assert it). | dependence ⇒ **the comparison is not a wage-block-only perturbation** and the budget mapping moves between arms ⇒ **halt and return**; this is not repairable inside LOC4 |
| **G-L4-7** | **Normalisation.** N1–N9 analogues re-run **in full** on the extended block **before any pricing**, against the rebound `ĝ = g̃ / Z_i^S`. Prior passes are void as gates (I-1 §6.2 applied to the extended block). | any failure ⇒ halt; this is the M08E lesson and is not negotiable |
| **G-L4-8** | **`δ_occ` / `β_occ_k` separation.** Report the fitted correlation structure between the `δ_occ` and `β_occ_k` coordinates and the bound-hit status of each. | near-degeneracy is a **finding** (C-4), reported; it is **not** answered by pinning `β_occ_k` |

### 5.4 Normalisation invariance — does `Z` move under `δ_occ`?

The deputy's framing is exactly right and the answer forks on one schema fact.

The welfare-layer opportunity object is `ĝ = g̃ / Z_i^S`, with **analytic `Z` over the full mixed support** (I-1 §6.4). `g̃` carries the structural wage factor. Therefore:

- **If `Z`'s closed form integrates the wage factor over the unbounded support `w ∈ (0, ∞)`:** the log-normal wage factor integrates to **exactly 1 for every occupation `k` and every value of `δ_occ`**, because `δ_occ` shifts the location of a proper density and a location shift does not change its total mass. **`Z` is invariant under `δ_occ`.** In this branch the only wage-channel effect on `Z` is through the *other* re-estimated coordinates, and the normalisation machinery needs no extension. I-2 §4 supports this branch on the proposal side: `q_W` is explicitly **untruncated** — "no bound, no clip, no rejection", only an `eps = 1e-300` guard — and `w_min`/`w_max` are recorded as *realised sample statistics*, not design bounds (`u6f_frozen_box_v1.json.wage_basis`).

- **If `Z`'s closed form integrates the wage factor over the frozen box `w ∈ [1.9411632533361265, 101.91995852573758]`:** the factor is **truncated**, its mass is `Φ((log w_max − μ_i − δ_occ(k))/σ) − Φ((log w_min − μ_i − δ_occ(k))/σ)`, which **depends on `δ_occ(k)`**. **`Z` moves — household-specifically and occupation-specifically.** The recorded schema carries an `in_support_box` column and the record reports zero off-box nodes on every rung (I-2 §2(iii)–(iv)), which is at least consistent with the welfare job space being box-bounded. In this branch the analytic `Z` closed form **must be extended to carry `δ_occ`**, and the extension is mandatory rather than optional.

**Consequence, stated as a standing prohibition.** Silently reusing the baseline `Z` on the LOC4 arm in the truncated branch would reintroduce **exactly the M08E defect**: a household-specific, coalition-varying `log Z` offset corrupting welfare comparisons — the defect that triggered the mid-course correction and cost 53.42 nats. Because the difference `Δ` is taken across arms, a `Z` error would not cancel under CRN; it would sit directly in the headline. Therefore:

> **`Z` is treated as `δ_occ`-dependent until the normalisation ruling's closed form is read and shown otherwise (SA-5).** The burden of proof runs toward extension, not toward invariance. G-L4-7 gates it. An invariance claim asserted without the closed form in hand is a halt.

### 5.5 Coherence check — incoherence is a named finding, never designed around

| id | finding | status |
|---|---|---|
| **C-1** | **The headline set is precision-selected, and the paper's own object is not in it.** {W1 mean, Gini, φ_A, φ_B} is exactly the MC-passing subset of I-2 §6.4. But `W1_phi_A+phi_B_level` **fails** (`E_T = 0.00164734`, ratio `1.318`) and `W1_s_opp ≡ W1_r_phi_A+phi_B` **fails** (`E_T = 0.0094323`, ratio `1.886`). The paper's headline economic quantity — the **total opportunity share** — is therefore **outside** the headline set, while its two summands are inside it. LOC4 can return "immaterial on φ_A and φ_B" while saying nothing certifiable about their sum. | **Named. Not designed around.** LOC4 does **not** report a materiality verdict on `φ_A+φ_B` or `s_opp`; they sit in Tier 2, banded, with the failure ratios shown. Inferring immateriality of the sum from immateriality of the parts is a prohibited claim. |
| **C-2** | **The threshold set is a level instrument used as a difference instrument.** Two of four classes have level-scaled denominators that are undefined on a difference (§3.4). | **Named.** Blocking open item **OL-4**. No numerals proposed; two readings recorded for the freeze to rule on. **H-1's verdict is withheld** until it is ruled. |
| **C-3** | **Both arms may fail precision on the same Tier-2 functional.** The baseline arm alone carries `n_fail: 47` of 66 (W1 13/22; W4 17/22; W6 17/22). | **Named.** Tier 2 carries a standing rider: where either arm fails its level threshold, no materiality verdict is issued on that functional — the difference is reported and left uncertified. |
| **C-4** | **Deliberate double-counting.** I-3 §18 forbids occupation in two blocks except as a deliberate extension; LOC4 is that extension (§19, `M3`). Separation rests entirely on the `w`-interaction (§1.4). | **Named.** G-L4-8 measures it. If the fit cannot separate `δ_occ` from `β_occ_k`, that is **reported as a finding about the model**, not repaired by pinning `β_occ_k` — pinning would silently change the estimand and make the comparison a different one from the one pre-registered here. |
| **C-5** | **Baseline asymmetry, disclosed up front.** In the accepted baseline, occupation shifts the **proposal** wage location (`μ_ik` occupation-conditional, I-2 §4) but is **absent** from the **structural** wage block (`δ_occ` coordinate-empty). The model draws as if occupation matters for wages and estimates as if it does not. | **Named as a property of the baseline, disclosed now.** It is the motivation for the axis and must appear in the Branch A disclosure; discovering it post hoc, or presenting LOC4 as a purely exploratory extension rather than the repair of a known asymmetry, would misstate the record. |
| **C-6** | **`Z` may or may not move (§5.4), and the record available here does not settle it.** | **Named.** Resolved by reading the closed form (SA-5), not by assumption. Default posture is "moves". |
| **C-7** | **The comparison is specification-level, not coordinate-level.** Both arms re-estimate everything; CRN pairs randomness, not parameters (§3.2). | **Named.** Coordinate-level attribution language is prohibited in all LOC4 output. |
| **C-8** | **The upstream CV1 return is unresolved and adjacent.** I-2 returns `STOP(A4 / O-8)` with A5-i (node 0 inside every sub-basis's averaged set) and A5-ii (the atom is sampled on the IS leg, not Rao-Blackwellised) still open. A5-i in particular means the raw estimator of record is `(1/(n+1))[y_0^det + Σ y_t]`. | **Named as an inheritance, not a LOC4 defect.** LOC4 inherits the estimator as implemented and **does not repair it** (repair is outside this mission's authority, exactly as it was outside CV1's, per memo C-7). Under CRN the `y_0^det/(n+1)` term is present identically in both arms and **cancels in `Δ` to the extent that node 0 is bitwise identical across arms** — which G-L4-1 verifies and which is the reason this inheritance is tolerable here. If those returns are dispositioned in a way that changes the raw estimator, **LOC4's comparison must be re-run**, because the object being differenced will have changed. This is a dependency, and it is recorded as such. |

### 5.6 Open items (for the Goal-1 freeze)

| id | item | blocking? |
|---|---|---|
| **OL-1** | The **LOC4 Path-B ruling** text (I-1 §0, v1 §2.3) is not in this mission's attachment set. Its Path-B specification must be reconciled against §1 of this memo — in particular whether "Path-B" prescribes a specific LOC4 construction that differs from the `M3` four-density form adopted here. | **BLOCKING** — a mismatch would void §1 |
| **OL-2** | `δ_occ` bound `B`: rule recommended (§1.5), numeral not fixed. | blocking before execution, not before freeze |
| **OL-3** | The four-leg convergence standard's leg definitions and the deputy convergence-class rule for leg (c): NA-on-this-record; mandatory transcription. | **BLOCKING** |
| **OL-4** | **Materiality thresholds on differences**: transferable for Ginis and component levels; **undefined** for means/medians and normalized contributions (§3.4, C-2). Two readings recorded, neither selected. | **BLOCKING for H-1**; the mission cannot issue a headline verdict without it |
| **OL-5** | `Z` closed-form support (§5.4, SA-5). | **BLOCKING before any pricing** |
| **OL-6** | EUROMOD occupation-invariance confirmation (G-L4-6), which I-3 §14.3 requires and does not assert. | **BLOCKING** |
| **OL-7** | Dependency on the disposition of the CV1 return (C-8): if the raw estimator changes, LOC4 re-runs. | tracked, not blocking at freeze |

---

## OUTPUT DISCIPLINE

**Mission ID:** JMP-M08 · LOC4 four-density robustness (design).

**Authoritative inputs:** I-1 through I-6 as tabled above, with sha256 pins carried in-line where the instruments carry them.

**Decisions made:** the variant is the `M3` occupation-conditional wage **location** with shared σ and fixed reference (§1.3); identification is the within-occupation wage interaction, with the constant part conceded to `β_occ_k` (§1.4); full simultaneous re-estimation of `47 + K`, no profiling, no pinning (§2.1); no S-10 on the LOC4 arm unless W-4 membership changes, and a membership change is a return rather than an autonomous re-derivation (§2.4); differences only, Tier-1 headline first (§3.1); CRN exact on the base half conditional on G-L4-1, and **not assumed** on the defensive half because the record shows the box moves with θ (§3.2); `E_T(Δ)` is the jackknife **of the difference** (§3.3); the three-branch tree with a **held** pipeline in Branches B and C (§4); `Z` is treated as `δ_occ`-dependent until the closed form says otherwise (§5.4); eight coherence findings named rather than designed around (§5.5).

**Unresolved decisions:** OL-1 … OL-7, of which OL-1, OL-3, OL-4, OL-5 and OL-6 are blocking. Of these, **OL-4 is the one that constrains the headline**: `W1_gini`, `φ_A` and `φ_B` are testable against transcribed absolute thresholds today; **`W1_mean` is not**, because the threshold set of record supplies a level-scaled denominator with no defined meaning on a difference, and this memo proposes no numeral to fill it.

**Exact output filename:** `docs/Missions/JMP_M08_LOC4_robustness_design_v1.md`

**Status:** PROPOSED-PENDING-GOAL1-FREEZE.

**Next authorised action:** Goal-1 freeze review of this memo, resolving OL-1 and OL-3 from the instrument chain and escalating **OL-4** to the deputy as a numerical-semantics question (materiality-on-differences denominator convention), with OL-5 and OL-6 dispositioned as Stage-A bindings of the execution mission. **No execution mission is authorised by this memo.**

**Statement.** No welfare number, decomposition number, inequality index, parameter value, priced node, re-estimation, new draw, or EUROMOD execution was produced. Every numeral above is transcribed from a named record with a citation; no threshold, bound, or tolerance was invented, and every gap in the record is named as an open item rather than filled.