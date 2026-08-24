# FR P2a — JMP-M08 Coalition-Robust Welfare Proposal `q^W`: Design Memo v1

**Mission:** JMP-M08 — France 2016 Singles Welfare Integration and Baseline Decomposition Prototype
**Register item:** U6 — welfare-proposal remediation (proposal axis)
**Commissioning authority:** Deputy Programme Director, *JMP-M08 U6 Ruling — Welfare Proposal Remediation v1* (2026-08-18), §4 "Required welfare-proposal architecture", §5, §6 Stage U6-A
**Document class:** design memo (economics + sampler specification). **No computation, no code, no welfare number, no re-estimation, no commit.**
**Status:** **PROPOSED — PENDING GOAL-1 FREEZE.** Nothing here is frozen. The Goal-1 design freeze is the freezing instrument.
**Target repository path (as instructed):** `MNL/docs/France_case/P2a/FR_P2a_m08_qw_proposal_design_v1.md`
**Author role:** M08 design author (advisory)

**Authoritative inputs**

1. Deputy ruling *JMP_M08_U6_welfare_proposal_remediation_ruling_v1.md* — binding; §§2, 3, 4.1–4.5, 5, 6, 8, 9.
2. `FR_P2a_m08_stageD_basis_addendum_v1.md` — the evidence of record: frozen inputs table, R-89 promotion rule, cross-check operationalisation, 1x battery outcome, halt conditions.
3. `JMP_M08_access_equalisation_operand_design_v1.md` (U12, as ratified by R-71) — access operator `A`, D1 cell routing, V1–V13.
4. `JMP_M08_ability_preference_operators_design_v1.md` (R9) — operators `B`, `P`, the coalition table, V14–V23.
5. `RURO_model_spec_contract_v2_stijn_enhanced.md` §§5, 6, 11, 13 — the accepted proposal factorisation and the `log_prior` identity.
6. Frozen artifacts named in the addendum: execution contract v5, certified spec, accepted θ̂ (47 rows), the 1x draw-geometry parquet (157,055 = 1,555 × 101, seed 2026), the 1x pricing cache, MNL HEAD `5b0e3d29`.

**Not used as data:** management memos; the historical couples-inclusive W3 gate report is indicative only (charter §2).

**Governance discrepancy registered on the first page, not resolved here.** Deputy §7 requires the permanent design artifact at `Job_Market_paper/docs/Missions/JMP_M08_U6_welfare_proposal_remediation_design_v1.md`, and Stage U6-A restricts repository writes to `Job_Market_paper`. The commissioning instruction names an MNL path. Both cannot be the single permanent artifact. See **O-14**. No file is written by this memo, so nothing is prejudiced.

---

## 0. Executive statement

The remediation is a **node-level defensive mixture** over the certified node space, with deterministic (stratified) component allocation and balance-heuristic weights, so that

```
q_i^W(j) = (1 − λ) · q_i(j) + λ · r_i(j),      λ frozen, 0 < λ < 1
```

is an exact, normalised, analytically evaluable density at every node, and `−log q_i^W(j)` replaces `−log q_i(j)` in the welfare-side `V_i^{IS}` construction only.

The design turns on one property, stated here and proved factor by factor in §2:

> **Uniform coalition domination.** The defensive component `r_i` is chosen so that
> `M_i := max_{S ⊆ {A,B,P}} sup_{j ∈ B_i} f_i^S(j) / r_i(j) < ∞`,
> where `f_i^S = exp(u_i^S) · ĝ_i^S` is the coalition-`S` target and `B_i` is the frozen priced support box.
> Then for **every** coalition, `sup_j f_i^S(j)/q_i^W(j) ≤ M_i / λ`: the importance weights are bounded, the estimator has finite variance, `1/√m` convergence is restored, and the bound is *coalition-invariant by construction* rather than by inspection.

Two further findings that this memo is obliged to surface because they bear directly on whether the repair can succeed:

- **The eight coalition opportunity densities collapse to four.** `P` acts only on `u_i`; it does not touch any factor of `g`. Hence `ĝ_i^S` depends only on `S ∩ {A,B}`, so there are exactly four distinct opportunity objects — `ĝ^∅, ĝ^A, ĝ^B, ĝ^{AB}` — and, because EUROMOD pricing depends only on `(h, w)` and household characteristics, the `{S}` and `{S ∪ P}` direct cross-checks can share **identical priced draw sets**. This halves the §4.4 sampler build and halves the direct-pricing volume (§3.5). It is a consequence of the ratified operator definitions, not a new choice.
- **The persistent ~1-nat direct-vs-IS disagreement may be a normalisation constant, not a tail phenomenon, and if so no proposal repair will close it.** `V^{IS}` estimates `log ∫ exp(u)·g̃`, while `V^{dir}` (sampling from the normalised `ĝ`) estimates `log ∫ exp(u)·g`. If the accepted opportunity factors are specified up to a household-specific constant `Z_i` — which the *estimation* likelihood cannot detect, since a household-common additive shift in `V` cancels exactly in `ℓ_h = V_chosen − log Σ_j exp(V_j)` — then `V^{IS} − V^{dir} ≡ log Z_i` exactly, with no dispersion beyond Monte-Carlo error. §6.6 pre-registers a cheap, EUROMOD-free discriminating test and §8 registers the consequence as a candidate return condition. This memo does **not** apply any normalisation correction: that would be a welfare-specification change, which is outside the authorised proposal axis.

---

## 1. The density

### 1.1 Node space, support, and base measure (unchanged)

A node is `j = (e, loc4, h, w)` with `e ∈ {0,1}`, `loc4 ∈ {1,2,3,4}`, and `(h, w)` continuous on the frozen priced box. The base measure `ν` is counting on `{e} × {loc4}` and Lebesgue on `(h, w)`. This is the certified machinery's node space; nothing is added or removed.

**Support convention (frozen, one choice, per deputy §4.2).** All densities — `q_i`, `r_i`, `q_i^W`, and every `ĝ_i^S` used by the direct estimator — are defined and normalised over the **same** frozen box

```
B_i = {e = 0}  ∪  ( {e = 1} × {1,2,3,4} × [h_min, h_max] × [w_min, w_max] )
```

with `(h_min, h_max, w_min, w_max)` bound at Stage A to the accepted draw-geometry bounds already implicit in the certified B-pool and the priced chunk grid. Two consequences, both disclosed rather than engineered away:

1. The accepted `V^{IS}` is **already** a box-restricted object — the certified estimation draws are bounded — so preserving the identical box introduces no new truncation relative to the accepted estimate. Any `g`-mass outside the box is a pre-existing, shared convention.
2. It is nevertheless a level convention that a money-metric welfare number inherits. §6.7 pre-registers a closed-form, EUROMOD-free disclosure of the outside-box `g`-mass per coalition (lognormal CDF tail; category probabilities are exhausted inside the box by construction). **O-4** asks Goal 1 to rule on whether this is a caveat-block item or a return item.

The compactness of `B_i` is what makes the domination argument in §2 *analytic* rather than asymptotic, and it is why the design does not need a Pareto or Student-t tail component: on a compact box, a density bounded away from zero already dominates every competitor.

### 1.2 The base component `q_base` — reused verbatim

`q_base := q_i`, the frozen estimation proposal, **unmodified**, in its accepted factorised form (spec contract §5, §11):

```
log q_i(j) = log q_E(e | x_i) + 1{e=1} · [ log q_Occ(loc4) + log q_H(h) + log q_W(w | loc4, x_i) ]
```

with the certified B-pool settings: `π0 = 0.10` employment-margin control; empirical `loc4` shares for `q_Occ`; the D1 five-mode hours mixture for `q_H`; the W1 occupation-conditional wage density for `q_W`; seed 2026. **Exact parameter values, column names, and the atom/chosen-row conventions are bound at Stage A against the frozen draw-geometry parquet (sha256 `5bcf0e54…`) and the certified spec (sha256 `492bcfa9…`); this memo states objects, never guessed strings.**

Reusing `q_base` verbatim is not conservatism. It (i) preserves the efficiency the estimation proposal genuinely has near the mode, (ii) permits the reuse coupling of §4.3 that keeps the already-priced 1x nodes inside the new ladder, and (iii) satisfies the deputy's requirement (§4.2) that `q_i` retain strictly positive mixture mass.

### 1.3 Why the base fails, stated economically

The welfare integrand is `exp(u_i(c_ij, ℓ_ij)) · g_i(j)`. The estimation proposal `q` was designed to cover `g` — the *opportunity* density — and it was tuned in a setting where the level of the integral never had to be right, because household-common shifts cancel in the conditional likelihood. The welfare target carries an additional factor `exp(u)` that appears **nowhere in `q`**, and `u` is increasing in consumption, hence in `w·h`. With Box-Cox consumption utility, `exp(u)` grows like `exp(β_c c^{θ_c}/θ_c)` — faster than any polynomial in `w`. The weight function

```
ω(j) = exp(u(c(w,h))) · g^W(w | loc4) / q_W(w | loc4)
```

is therefore increasing in `w` over the upper part of the box whenever `q_W` is no heavier-tailed than `g^W` — which it is not, both being occupation-conditional lognormal-type objects. An unbounded, monotonically increasing weight function on the sampling region is exactly the signature the Stage-D evidence reports: sub-`1/√m` convergence, sub-linear ESS growth, drift stalling at 0.09/0.07 nats against a 0.05-nat gate, and a level (not ratio) discrepancy against the direct estimator. **More draws under the same `q` do not fix an unbounded weight function; they only sample its tail more often.** That is the whole content of deputy §3.2, and it is why the repair must be on the shape of the proposal, not on `m`.

A secondary, distinct failure sits in `q_H`: the D1 five-mode mixture places near-zero density between focal points, while `g^H` and `exp(u(ℓ))` are smooth in `h`. Wherever `q_H` is small and the target is not, the ratio spikes. This is a *hole* problem rather than a *tail* problem, and it is cured by the same instrument.

### 1.4 The defensive component `r_i`, factor by factor

`r_i` is a product of four exactly normalised factors on `B_i`. Every factor is chosen so that its ratio against **every** coalition variant of the corresponding `g` factor is bounded by a constant computable before pricing.

| Factor | Defensive form `r` | Exact density on `B_i` | Analytic ratio bound `sup g^S/r`, uniform in `S` |
|---|---|---|---|
| Employment margin | Bernoulli with `π0^r = 0.5` | `r_E(0) = 0.5`, `r_E(1) = 0.5` | `≤ 2` for any coalition employment probability in `[0,1]` |
| Occupation | **Uniform on the 4 LOC4 categories** | `r_Occ(k) = 1/4` | `≤ 4`, for *any* probability vector on the simplex |
| Hours | **Uniform on `[h_min, h_max]`** | `r_H(h) = 1/(h_max − h_min)` | `(h_max − h_min) · sup_h g^H(h)`, coalition-free (see §2.3) |
| Wage | **Log-uniform on `[w_min, w_max]`**, occupation-free | `r_W(w) = 1 / (w · log(w_max/w_min))` | `log(w_max/w_min) / (σ√(2π))` — **independent of the Mincer location `μ`** (Proposition 1, §2.4) |

```
r_i(j) = r_E(e) · 1{e=1} · [ r_Occ(loc4) · r_H(h) · r_W(w) ]
```

Each factor is a textbook density with a closed form; `log r_i(j)` is exact and requires no normalising constant to be estimated. The defensive component deliberately **drops all household conditioning**: `r_i` is the same object for every household except through the box bounds. That is not laziness — a household-conditioned defence would re-import exactly the covariate structure whose coalition-substitution is the thing we must be robust to.

The log-uniform wage choice deserves a sentence of economics. On the log-wage scale it is the flat (maximum-entropy) density; it says the defence takes no view on where in the priced wage range a job offer sits. Because a lognormal is Gaussian in `log w`, and a Gaussian on a bounded interval is bounded above by its mode height, the flat log-scale density dominates the *entire family* of lognormals with common `σ` and any location — which is precisely the family the coalitions traverse.

### 1.5 Mixture form, `λ`, and the variance rationale

**Node-level (joint), not per-factor.** The mixture is taken over the whole node density, not inside each factor:

```
q_i^W(j) = (1 − λ) q_i(j) + λ r_i(j)
log q_i^W(j) = logaddexp( log(1−λ) + log q_i(j),  log λ + log r_i(j) )
```

A per-factor mixture `Π_f[(1−λ_f)q_f + λ_f r_f]` is also analytically evaluable, but it is strictly worse: its density is bounded below by `λ^4 · r`, giving a weight bound `M/λ^4` (≈625× at λ=0.25) instead of `M/λ` (≈4×), and it almost never produces a node that is defended in all four coordinates simultaneously — which is exactly what joint-tail coverage requires. **Dq2: single scalar `λ`, node-level mixture.**

**The classical bound (Hesterberg 1995; Owen–Zhou 2000).** Since `q^W ≥ λ r` pointwise,

```
f^S / q^W  ≤  f^S / (λ r)  ≤  M/λ         for every coalition S,
Var_{q^W}( f^S/q^W )  ≤  (1/λ) · Var_r( f^S/r ) ,
```

so the defensive mixture inherits, up to `1/λ`, the finite variance of the safe component while retaining the base component's efficiency where the base is good. Validity does not depend on `λ`: for **any** `λ ∈ (0,1)` the weights are bounded and the estimator is unbiased and `√m`-consistent. `λ` is a pure efficiency parameter. This matters for governance: freezing `λ` a priori risks efficiency, never validity, which is why the deputy's no-post-hoc-tuning rule is costless here.

**Proposed value: `λ = 0.25`.** Reasoning, in order of weight:

1. The cost of defence in the benign region is a variance inflation of at most `(1−λ)^{-1} = 1.33`; the benefit is the replacement of an unbounded weight function by one bounded by `4M`. Given the recorded evidence (V6/V22 FAIL at 1x with deltas 0.051–0.059 against a 0.05 cap; drift 0.09/0.07 against 0.05), a token `λ` would not move the diagnostics enough to be worth the pricing.
2. The literature range for defensive mixtures is `λ ∈ [0.1, 0.5]`; `0.25` sits at the centre of the interval on the log scale and is a clean stratification period (§4.2: one defensive node in four).
3. `100, 200, 400` are all divisible by `4`, so `λ = 0.25` is realisable *exactly* at every rung of the ladder under deterministic allocation — the realised defensive fraction is `0.25` at 1x, 2x and 4x, with zero label noise contaminating the U6 adjacent-step drift statistic. `λ = 0.2` or `0.3` would not have this property on this ladder.

`λ` is nonetheless registered as **O-1**: the Goal-1 freeze must ratify the value. §8 records a permissible pre-registered efficiency ladder if Goal 1 prefers one, together with the condition that makes it compliant with deputy §4.2.

### 1.6 Exact evaluation and the correction identity

Every node persists: `component_label ∈ {base, defensive}`, `log_q_base`, `log_r_def`, `lambda`, `log_q_W`, the stream seed, and the node index within the household stream (deputy §4.2). The implementation must assert, as a deterministic pre-EUROMOD test:

```
| log_q_W − logaddexp(log(1−λ)+log_q_base, log(λ)+log_r_def) | < 1e-10      (all rows)
| log_q_base − ( log q_E + working·(log q_Occ + log q_H + log q_W) ) | < 1e-8  (spec contract §11 identity, preserved)
```

and must make the old and new corrections **structurally unconfusable** (deputy §6, Stage U6-B): distinct column names, a `correction_kind` tag on every welfare artifact, and a guard that refuses to construct a welfare `V^{IS}` from a frame carrying only `log_prior`.

**Scope of the substitution (verbatim binding, §5):** `−log q_i^W` replaces `−log q_i` **in the welfare-side `V_i^{IS}` construction only**. Estimation artifacts, the accepted likelihood, the accepted `log_prior` column, and every certified estimation output remain untouched.

---

## 2. Coalition robustness

### 2.1 The eight targets, and the design criterion

For coalition `S ⊆ {A, B, P}` the welfare integrand is

```
f_i^S(j) = exp( u_i^S(c_ij, ℓ_ij; θ̂) ) · ĝ_i^S(j),        V_i^S = log ∫_{B_i} f_i^S dν
```

with `u^S` carrying the `P`-substituted taste covariates and group block when `P ∈ S`, and `ĝ^S` carrying the `A`/`B`-substituted arguments. The proposal is **coalition-invariant** (deputy §4.1): one `q^W` for all eight coalitions, both active measures, and all four S-10 scenarios, which is what preserves common random numbers and prevents a proposal difference masquerading as a coalition effect.

**Design criterion (Dq3).** `r_i` must satisfy

```
M_i := max_{S} sup_{j ∈ B_i}  f_i^S(j) / r_i(j)  <  ∞ ,
```

with the `g`-side of `M_i` computable in closed form before any pricing exists, and the `exp(u)`-side bounded by continuity on the compact box and reported numerically at first pricing. Domination of the *maximum over `S`* — not of each `S` separately by a bespoke proposal — is what makes one proposal serve eight coalitions.

### 2.2 Employment margin

`A` moves `g^E` (region → dwt population-share-weighted index; GSUR → dwt sample mean), `B` moves its education-interacted cells, `P` does not enter. The coalition can therefore push the employment probability anywhere in `[0,1]`, but the margin is a **two-point object**: `r_E ≡ 0.5` dominates any two-point distribution with ratio `≤ 2`, for every `S`, with no further argument required. Under the mixture the atom carries mass `(1−λ)·0.10 + λ·0.5 = 0.2` at `λ = 0.25`, a doubling of the accepted atom mass — material, because access equalisation is precisely the operator that moves employment availability, and the 1x geometry gave the non-employment state only `0.10`.

### 2.3 Hours

`g^H` is coalition-invariant: U12 §3.4 records the certified hours-band shifters as carrying no household covariates, so `A`'s action on the hours cell is the identity; `B` touches only education-assigned cells (none in `g^H` under the certified spec, verified at Stage A); `P` touches only `u`. The hours ratio bound is therefore a single number, not a max over eight. Uniform `r_H` additionally fills the inter-modal holes of the D1 mixture, which is where the *hole* failure of §1.3 lives.

### 2.4 Wage — the load-bearing case

**Proposition 1 (location-free domination).** Let `g^W(w; μ, σ)` be lognormal with location `μ` and common `σ`, and let `r_W(w) = 1/(w · L)` with `L = log(w_max/w_min)` on `[w_min, w_max]`. Then for every `μ ∈ ℝ`,

```
sup_w  g^W(w; μ, σ) / r_W(w)  =  L · sup_w [ w · g^W(w; μ, σ) ]
                              =  L · sup_w (1/(σ√(2π))) exp( −(log w − μ)² / (2σ²) )
                              =  L / (σ√(2π)) .
```

*Proof:* `w·g^W(w;μ,σ) = (1/(σ√2π))·exp(−(log w − μ)²/2σ²)`, whose supremum over `w > 0` is attained at `log w = μ` and equals `1/(σ√2π)`, independent of `μ`. ∎

This is the property that delivers coalition robustness in the one dimension where the coalitions actually bite. Under `B`, the Mincer location becomes `μ_i^B = ē·b + p̄_exp·b_pexp + p̄²_exp·b_pexp2 + δ_occ[loc4_j]`; under `{A,B}` the same, with the occupation *weights* pooled. Whatever the substitution, `σ` is common and coalition-invariant (R9 §2.3: `σ` equalisation is the identity in M08), so **every** coalition's wage factor lies in the one-parameter family `{g^W(·; μ, σ) : μ ∈ ℝ}` and is dominated by `r_W` with the *same* constant `L/(σ√2π)`. No enumeration of coalitions is needed, and no future re-ratification of the reference objects can break the bound.

Note also what this buys against `δ_occ`: `μ` shifts by occupation, and the occupation composition itself moves under `A`. Because the bound is `μ`-free, the occupation × wage interaction — the single cell where `A` and `B` interact (R9 §2.4) — cannot destabilise the weights.

**LOC4 forward statement.** If the four-density variant makes dispersion occupation-specific (`σ_occ`), the bound becomes `L / (min_k σ_k · √(2π))` — still finite, still location-free, still coalition-uniform. The design is LOC4-stable in form; only the constant changes.

### 2.5 Occupation

Any coalition occupation object — `p̂(·|dgn,educ3)`, `p̄(·|educ3)`, `p̃(·|dgn)`, `p̄̄(·)` — is a probability vector on four categories. Uniform `r_Occ = 1/4` dominates the **entire simplex** with ratio `≤ 4`. Coalition robustness here is not an argument but an identity: no admissible coalition table, present or future, can exceed the bound. This is the strongest form the criterion takes anywhere in the design.

### 2.6 Preference, and the `{A,B}` / `{B,P}` / `{A,B,P}` failures

`P` leaves `g` untouched and enters only through `exp(u^P)`, via dwt-referenced taste covariates and the step-(b) group-block selection. Since `u` is continuous on the compact box and the coalition set is finite, `max_S sup_j exp(u_i^S(j))` is a maximum over eight finite numbers. The three 1x V6/V22 failures — `{A,B}` 0.0508, `{B,P}` 0.0585, `{A,B,P}` 0.0572 — are precisely the coalitions that combine an opportunity substitution with a large change in where the target's mass sits relative to `q`:

| Coalition | What moves the target away from `q` | Which defensive factor absorbs it |
|---|---|---|
| `{A,B}` | full opportunity equalisation: pooled employment index, `p̄̄(loc4)` occupation, reference Mincer location | `r_E` (2), `r_Occ` (4), `r_W` (location-free, Prop. 1) — all three bounds are `S`-uniform |
| `{B,P}` | reference wage location **and** reference tastes: the `exp(u)` factor and the wage factor move together, in the same direction, for households far from the references | `r_W` bounds the wage ratio at any `μ`; `exp(u^S)` bounded on the compact box; the joint mixture (§1.5) covers the *joint* displacement, which a per-factor mixture would not |
| `{A,B,P}` | grand coalition: every household faces the identical `g` and identical tastes; the target is maximally far from a household-conditioned `q` | the defence is deliberately **household-unconditioned**, so it does not degrade as the target moves away from own-`x` — this is the case where an own-`x`-conditioned defence would fail |

The last row is the design's key asymmetry and worth stating in the validation memo: the defensive component is *most* useful exactly where the base proposal is *least* useful, because the base is conditioned on the household's own covariates and the grand coalition removes precisely that conditioning.

---

## 3. Per-coalition `ĝ^S` samplers (deputy §4.4)

### 3.1 Four objects, eight coalitions

`ĝ_i^S` depends only on `S ∩ {A, B}`:

| Distinct object | Serves coalitions | Employment/market args | Occupation table | Wage location |
|---|---|---|---|---|
| `ĝ^∅` | `∅`, `{P}` | own `region`, `gsur`, own `educ` | `p̂(loc4 \| dgn_i, educ3_i)` | own `μ_i` |
| `ĝ^A` | `{A}`, `{A,P}` | dwt share-weighted region index, `ḡsur`; own `educ` slot | `p̄(loc4 \| educ3_i)` | own `μ_i` |
| `ĝ^B` | `{B}`, `{B,P}` | own region/GSUR; `ē` in the educ slot | `p̃(loc4 \| dgn_i)` | `μ_i^B(ē, p̄_exp, p̄²_exp)` |
| `ĝ^{AB}` | `{A,B}`, `{A,B,P}` | pooled region/GSUR **and** `ē` | `p̄̄(loc4)` | `μ_i^B` |

The GSUR × educ cell is evaluated per R9 §2.6 (each operator writes only its own argument slot); occupation objects are conditionals of the one frozen joint `Π(loc4, dgn, educ3)` (R9 §2.5), which is what makes the composition path-independent and `V14`-checkable.

**Pricing consequence.** EUROMOD prices `(h, w)` given household characteristics; it does not see `u`. So the `{S}` and `{S ∪ P}` direct cross-checks use **bit-identical priced draw sets**, differing only in the utility evaluation applied afterwards. Four sampler builds, four priced draw sets, eight evaluable cross-checks. **Dq7**; cost impact in §3.5.

### 3.2 Factor-sequential draw, with exact densities

For household `i` and coalition object `ĝ^S`, one draw is generated in a fixed order from five reserved uniforms (§4.1):

1. **Employment margin.** `e ~ Bernoulli(p_i^{S,work})` with `p_i^{S,work} = g^{E,S}(1) / (g^{E,S}(0) + g^{E,S}(1))`, evaluated at the coalition-substituted region/GSUR/educ arguments. If `e = 0`, the node is the non-employment atom and the draw terminates.
2. **Occupation.** `loc4 ~ Categorical(p^S(· | ·))` from the row of the table named in §3.1.
3. **Hours.** `h ~ g^H(·)` normalised over `[h_min, h_max]`. Coalition-invariant. **The certified `g^H` is a band-shifter exponential form; its normalising constant over the hours support must be computed exactly and is required for the sampler to exist at all** — see §3.4 and **O-6**.
4. **Wage.** `w ~ g^W(· | loc4; μ_i^S, σ)` truncated to `[w_min, w_max]`, with the truncation constant `Φ((log w_max − μ)/σ) − Φ((log w_min − μ)/σ)` carried explicitly. Inverse-CDF sampling, so the mapping from the reserved uniform to `w` is monotone and reproducible.

Each step persists its exact log-density; their sum is `log ĝ_i^S(j)`, used for the direct estimator's own bookkeeping and for the normalisation audit. **Rao-Blackwellisation of the atom (Dq8, recommended):** the direct estimator should be written as

```
V_i^{dir,S} = log [ ĝ^{E,S}(0)·exp(u_i^S(atom))  +  ĝ^{E,S}(1) · (1/R) Σ_{r=1..R} exp(u_i^S(j_r)) ] ,   j_r ~ ĝ^S | work
```

with the atom term **exact**. This is not a redefinition of the cross-check — it is the same integral with one stratum integrated analytically — and it removes the largest single variance component, which directly reduces the pilot-derived `R` and therefore the pricing bill. Registered as **O-7** because it changes the estimator's algebraic form, which Goal 1 may prefer to ratify explicitly.

### 3.3 Pricing interface

Sampled nodes enter the **unchanged certified target-only D-BEN Option B path** (addendum, session authorisation). No pricing-path change, no interpolation, no synthetic `c_ij`. Nodes are deduplicated against the existing pricing cache on the certified key before submission; cache misses are the cost driver.

### 3.4 The normalisation audit — a mandatory, EUROMOD-free gate

Deputy §4.4 requires that samplers "pass normalization and moment/category-frequency tests against the analytic coalition object before EUROMOD pricing". This memo strengthens that into the design's first deterministic test, because it is also the discriminator for the persistent direct-vs-IS disagreement (§0, §6.6):

For each of the four `ĝ^S` and each household, compute analytically or by high-accuracy quadrature over `B_i`

```
Z_i^S := ∫_{B_i} g̃_i^S dν      (g̃ = the accepted, as-implemented opportunity object)
```

and record `log Z_i^S`. Then:

- **Category test:** simulated `loc4` frequencies match `p^S` within a pre-registered tolerance at a pre-registered draw count.
- **Moment tests:** simulated `E[log w]`, `Var[log w]`, `E[h]` match the analytic truncated-lognormal / normalised-`g^H` moments.
- **Normalisation test:** `|log Z_i^S| ≤ 1e-8` for every `i`, `S`. **If this fails, the sampler is still constructible (normalise by `Z_i^S`), but the IS and direct estimators are then measuring different objects and the ~1-nat disagreement is explained by construction.** In that event: **HALT and return to deputy** (§8). Do not apply a `Z` correction to `V^{IS}` — that is a welfare-specification change outside this mission's authorised axis.

### 3.5 Cost driver — flagged, not designed around

Two independent volumes, both new EUROMOD pricing:

| Item | Volume (1,555 households) | Notes |
|---|---|---|
| `q^W` ladder, 1x | ≈ 25 new nodes/hh → **≈ 38,900** | base sub-stream reuse (§4.3) keeps 75 base nodes already priced |
| `q^W` ladder, 2x cumulative | ≈ 100 new nodes/hh → **≈ 155,500** | 50 new base + 50 defensive |
| `q^W` ladder, 4x cumulative | ≈ 300 new nodes/hh → **≈ 466,500** | only reached if 2x fails the frozen rule (deputy §4.3) |
| Direct cross-check | 4 objects × flagged-subset size × `R` | `R` from the pilot rule `MC-SE(V^{dir}) ≤ 0.05` nats; if the conditional CV of `exp(u)` is of order 2, `R` is of order `(CV/0.05)² ≈ 1,600` |

**The direct cross-check, not the ladder, is the binding cost.** Four objects × a flagged subset of a few hundred households × `R` in the thousands is a volume an order of magnitude above the ladder. Two honest mitigations are *within* the frozen definition — the `{S}`/`{S∪P}` draw sharing (§3.1) and the atom Rao-Blackwellisation (§3.2) — and one is *outside* it and therefore registered rather than adopted: stratifying the `ĝ^S` draw on `(e, loc4)` with exact stratum weights would cut `R` materially at zero bias, but it changes the estimator from a plain mean to a stratum-weighted mean (**O-8**). A further structural inefficiency to flag: defensive draws sit by construction in low-density regions, so their cache-hit rate will be *worse* than the base draws' — the node counts above are lower bounds on distinct pricing evaluations.

Per deputy §5 and the addendum's STEP-5 guard: if projected direct pricing exceeds six hours, **return a costed execution plan to the Goal 1 Manager**; do not truncate the certification set and do not redefine the gate.

---

## 4. Nested ladder and common random numbers

### 4.1 One stream per household, fixed consumption order

For household `i`, a single counter-based PRNG stream is seeded by `(master_seed = 2026, idhh)`. For node index `t = 1, …, 400` it yields, in a fixed and never-reordered sequence, five independent uniforms `(u^E_t, u^{Occ}_t, u^H_t, u^W_t, u^{spare}_t)`, mapped to a node by inverse CDF under whichever component `t` is allocated to. Counter-based generation makes node `t` reproducible without generating `1..t−1`, which makes the ladder extension exactly reproducible and the determinism test (`V11`) trivially satisfiable.

### 4.2 Deterministic (stratified) allocation, balance-heuristic weights

Component labels are **not** drawn: node `t` is defensive iff `t ≡ 0 (mod 4)`, base otherwise. Consequences:

- The realised defensive fraction is exactly `λ = 0.25` at `t ≤ 100`, `t ≤ 200`, and `t ≤ 400` — at every rung, with no label noise entering the U6 adjacent-step drift statistic. Under random labels, the 1x/2x drift would carry a spurious component from the realised-fraction difference.
- The estimator is the **deterministic-mixture / balance-heuristic MIS estimator** (Veach–Guibas; Owen–Zhou 2000), which the deputy explicitly permits as "an algebraically equivalent multiple-importance-sampling construction" (§4.2). Its denominator is exactly `(n_base/n)·q(j) + (n_def/n)·r(j) = q^W(j)`, so the persisted `log_q_W` column is unchanged in form and `−log q^W` remains exact. Deterministic allocation has variance no greater than random-label mixture sampling.

### 4.3 Nesting and reuse

The 1x node set is `{t ≤ 100}`, 2x is `{t ≤ 200}`, 4x is `{t ≤ 400}`: strict prefixes, hence genuinely nested bases for Gate 1(i). The chosen-alternative row and the non-employment support rows are carried outside the drawn block under the **accepted conventions, preserved verbatim** (deputy §4.3), and are excluded from the ladder indexing — with the important rider in **O-5**: if the accepted convention includes a node *deterministically*, that node is not an i.i.d. mixture draw and its treatment (exact stratum vs. IS row) must be bound at Stage A, not assumed.

**Base sub-stream reuse.** Base-labelled nodes consume the base uniforms in the same order as the certified 1x geometry, so the first 75 base nodes of the new 1x basis are *bit-identical* to nodes 1–75 of the frozen geometry parquet (sha256 `5bcf0e54…`) and are already priced. This is a coupling of random numbers, not a change of density: base rows remain i.i.d. draws from `q`, defensive rows i.i.d. from `r`, and the MIS denominator is unaffected. It also makes the old-`q` and new-`q^W` records directly comparable on shared rows — a free diagnostic. Halt condition 1 of the addendum (faithful 1x reproduction against the stored cache draws) applies to this reuse and must be verified before any extension is generated.

---

## 5. What is unchanged — verbatim binding

The following are **unchanged and binding**; any need to alter one is a halt and a return, not a design decision:

- **`θ̂`** — the accepted 47-coordinate vector (`theta_hat_p2a_singles2016_v1.csv`, sha256 `0684ee52…`), bitwise identical in every coalition save the declared step-(b) preference-block selection (`V19`). **No re-estimation.**
- **The model specification** — `estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml`, sha256 `492bcfa9…`.
- **Channel operators and cell routing** — D1 (factor × argument cell) as ratified by R-71; the U12 access operand; the R9 `B` and `P` operators; the mirror guard (R9 §2.7).
- **Welfare references and measure bindings** — the own-set `W³` reference, `Ā = type_conditional_median_opportunity` `(dgn, educ3)` / opportunity-only inclusive-value rank / lower median / own priced support, with `maximal_opportunity` excluded from M08; `J`, `o`, `R^h`; all frozen and hash-identical across all eight coalitions (`V2`).
- **The tax-benefit mapping and the certified pricing path** — target-only D-BEN Option B; the hash-pinned P2a pricing cache; the chunk grid; `c_ij` bitwise invariant across coalitions (`V4`, `V16`).
- **`π` / the estimation proposal on the estimation axis** — the accepted `log_prior` column and the accepted likelihood are untouched (`V3`).
- **The frozen gates** — U6 `median_abs_adjacent_step_delta_viis ≤ 0.05` nats per group over multipliers `[1,2,4]` with adjacent steps `[[1,2],[2,4]]`; the V6/V22 rule with materiality `min(0.05, 0.5·(1 − f_baseline))` evaluated **on each basis' own denominator**; the 0.5-nat direct-agreement tolerance; the R-89 smallest-qualifying-`m` promotion rule with its deputy-return failure branch.
- **S-10** — the four scenarios; `q^W` is numerically identical across all four (it depends on no perturbed coordinate) and this is hash-asserted.
- **LOC4 sequencing** — LOC4 is not implemented in M08; the §2.4 forward statement pre-registers the boundary so LOC4 cannot reopen it.

**Scope of the change:** `−log q_i^W` replaces `−log q_i` in the welfare-side `V_i^{IS}` construction only.

---

## 6. Pre-registered diagnostics

All emitted per basis (1x/2x/4x) and per coalition (all eight), aggregate-only persistence (standing rule 6). Gating status is stated for each; **nothing here relaxes or adds a gate.**

**6.1 Weight distribution (report).** ESS and ESS/m; max normalised weight; weight CV; the deciles of the normalised weight distribution.

**6.2 Bound conformance (report; falsifiable).** The ex-ante analytic bound `M̄/λ` from §2 alongside the realised max unnormalised weight. The realised value **must** fall below the bound; a violation means the box, the domination argument, or the density evaluation is wrong — a code defect, not a result. This is the design's own falsification test.

**6.3 Tail index (report, NON-GATING).** The Pareto-smoothing shape diagnostic `k̂` on the weight tail per coalition per basis. Prediction under this design: `k̂ < 0.5` by construction, since bounded weights have a finite-variance tail. `k̂ ≥ 0.7` would falsify the domination claim and should be read alongside 6.2. **`k̂` is a diagnostic only; no weight is smoothed, clipped, or truncated (§7.4).**

**6.4 Defensive-mass share (report).** The share of total unnormalised weight mass contributed by defensive-labelled nodes, per coalition. Near-zero means the defence is idle and `λ` is over-spent; near-one means the base is contributing nothing and the diagnosis of §1.3 is confirmed with force. Interpretive only.

**6.5 U6 drift table (gating, unchanged).** Group-median `|Δ V_i^{IS}|` for adjacent steps `1→2` and `2→4`, per group, at the accepted `θ̂`; max and p95 reported, not gated. Compared against 0.05 nats, "into `m`", per R-89.

**6.6 Direct cross-check on all eight coalitions (gating, unchanged) — plus one discriminator.** Per coalition, on its frozen flagged subset: median, p90, and share of `|V^{dir,S} − V^{IS,S}| > 0.5`; persistent iff the subset **median** exceeds 0.5 nats; `R` from the pilot rule `MC-SE(V^{dir}) ≤ 0.05` nats (pilot size 20 households). **Added, non-gating:** report the **signed** difference `V^{IS,S} − V^{dir,S}` with its median *and IQR*, and the per-household `log Z_i^S` from §3.4 alongside. Pre-registered reading, fixed before the numbers exist:
  - median large, IQR small, and `median ≈ median(log Z_i^S)` ⇒ the disagreement is a **normalisation constant**, not a tail defect; the proposal repair will not close it; deputy return under §8.
  - median large, IQR large, `log Z ≈ 0` ⇒ residual **tail/variance** defect; the repair is the right instrument and either succeeded or did not.
  - median small ⇒ closed.

**6.7 Support disclosure (report, EUROMOD-free).** Per coalition, the analytic `g`-mass outside the frozen box `B_i` (truncated-lognormal tail; hours tail), household-median and p90. A level convention, disclosed; see **O-4**.

**6.8 Normalisation audit (gating, §3.4).** `log Z_i^S` for the four objects; category-frequency and moment tests; all before any EUROMOD pricing of sampled nodes.

**6.9 Functional-level stability (report, explicitly NON-GATING).** Deputy §3.1 permits this **only after** the repaired proposal passes the frozen raw-level gates, and only as a supplement. Defined as: the two active decomposition measures' inequality levels, the three Shapley channel contributions, and `C_A + C_B`, each reported across bases 1x/2x/4x with their basis-to-basis differences. **This may not be cited in support of promotion, may not substitute for 6.5 or 6.6, and must be labelled non-gating wherever it appears.**

---

## 7. Rejected alternatives

**7.1 Larger `m` under the old `q`.** Rejected on evidence and on theory. Evidence: sub-`1/√m` convergence, sub-linear ESS growth, drift stalling at 0.09/0.07 nats. Theory: §1.3 shows the weight function is unbounded and increasing over the sampling region, so the variance may be infinite; when it is, no `m` delivers `1/√m`, and the sample maximum grows with `m`. Deputy §3.2 forbids 8x/16x/32x extensions; this memo supplies the reason that makes the prohibition principled rather than budgetary.

**7.2 Per-coalition tailored proposals as the primary instrument.** Rejected. It breaks common random numbers, so coalition differences — which *are* the decomposition — would confound a proposal difference with an operator effect; it breaks the nested-ladder comparability that Gate 1(i) requires; and it multiplies the pricing volume by four to eight. Deputy §4.1 permits a coalition-specific proposal **only** for the independent `ĝ^S`-direct cross-check, which is exactly the use in §3.

**7.3 Self-normalised importance sampling.** Rejected. SNIS estimates ratios of integrals; it is biased at `O(1/m)` for the *level*, and the M08 gates are level-anchored — `V^{IS}` is a log-level compared against `V^{dir}` at a 0.5-nat absolute tolerance, and the welfare measures are money-metric levels, not shares. Deputy §4.2 requires the exact correction `−log q^W_i(j)` for exactly this reason. SNIS would also make the normalisation defect of §3.4 invisible, which is the opposite of what the evidence needs.

**7.4 Weight truncation, clipping, or Pareto smoothing of the weights.** Rejected as an estimator. All three trade variance for bias in the *level*, and the level is the gated quantity; worse, they suppress the diagnostic signature of the tail mismatch rather than removing its cause, so a gate could pass while the integration remains wrong. `k̂` is retained as a **diagnostic** (6.3); no weight is modified.

**7.5 Per-factor mixtures instead of a node-level mixture.** Rejected: weight bound degrades from `M/λ` to `M/λ⁴`, and joint-tail coverage is lost (§1.5).

**7.6 Household-conditioned defensive component (e.g. own-`x` lognormal with inflated `σ`).** Rejected: it re-imports the covariate conditioning that the coalitions remove, so its adequacy would vary across coalitions and degrade precisely at `{A,B,P}` (§2.6). The location-free bound of Proposition 1 is unavailable for a conditioned defence.

**7.7 Deterministic quadrature or a QMC grid over `(loc4, h, w)`.** Not adopted. It is potentially far more efficient per priced node, but it abandons the accepted node conventions, cannot reuse the frozen 1x cache, requires a full re-price of every household, and would constitute a change to the certified draw machinery rather than a proposal repair — outside the authorised axis (deputy §1, §4.5). Recorded here so that the option is on the record if the repair fails and the deputy reopens the design.

---

## 8. Open items for the Goal-1 design freeze

| # | Item | Status / recommendation |
|---|---|---|
| **O-1** | **`λ`.** Proposed `λ = 0.25`, frozen before pricing (§1.5). | Requires ratification. Because validity is `λ`-free, a **pre-registered** ladder `λ ∈ {0.15, 0.25, 0.40}` with a selection rule fixed in writing before any pricing would also be compliant with deputy §4.2; a rule chosen *after* seeing priced outcomes would not. Goal 1 to rule which. |
| **O-2** | **Box bounds `(h_min, h_max, w_min, w_max)`** and whether the box is global or per-household. Global recommended (comparability; single analytic bound). | Bind at Stage A against the frozen geometry parquet. |
| **O-3** | **`π0^r = 0.5`** for the defensive employment margin. | Proposed; ratify or set. |
| **O-4** | **Outside-box `g`-mass** (§1.4, 6.7): caveat-block disclosure or return item. | Recommend caveat block, since the accepted estimation object shares the convention. |
| **O-5** | **Chosen-alternative and non-employment conventions.** If either node is included *deterministically*, it is not an i.i.d. mixture draw; its exact treatment must be bound. | Stage A binding; **halt if the accepted convention cannot be reproduced faithfully** (addendum halt condition 1). |
| **O-6** | **Normalisation of `g^H`** (and of any band-shifter form) over the hours support. A genuine sampler cannot exist without it. | Stage A, pre-EUROMOD. Candidate halt. |
| **O-7** | **Atom Rao-Blackwellisation** in `V^{dir}` (§3.2). Materially reduces `R`; changes the estimator's algebraic form. | Recommend adopt; requires explicit ratification. |
| **O-8** | **Stratified `(e, loc4)` sampling** from `ĝ^S`. Unbiased, large `R` reduction; changes the cross-check estimator from a plain mean. | Registered, **not** adopted without ratification. |
| **O-9** | **`R`** from the pilot (20 households, `MC-SE ≤ 0.05` nats) — an outcome, not a choice, but the pilot subsample must be pre-registered. | Pre-register the subsample before the pilot runs. |
| **O-10** | **The normalisation finding (§0, §3.4, 6.6).** If `log Z_i^S ≠ 0`, the ~1-nat disagreement is explained by construction and the proposal repair cannot close it. | **Candidate deputy return** under ruling §8 ("accepted structural inputs or coalition operators would need to change"). No `Z` correction is applied under this mission. |
| **O-11** | **Explicit `1/n` normalisation** in `V^{IS}` across bases. A missing or basis-varying `1/n` shifts levels by `log 2` per rung and would contaminate the U6 drift statistic. | Stage A assertion; expected already satisfied (the recorded 1x→2x drifts of 0.09 are far below `log 2 ≈ 0.693`). |
| **O-12** | **Persistence schema** for `component_label`, `log_q_base`, `log_r_def`, `lambda`, node index, stream seed; and the guard that makes old-`q` and new-`q^W` corrections unconfusable. | Deputy §4.2, §6 Stage U6-B. |
| **O-13** | **Occupation-conditioning of `r_W`.** Proposed occupation-*free* (one log-uniform for all `loc4`), which is what makes Proposition 1's bound uniform across the occupation composition changes induced by `A`. | Confirm; the alternative (per-`loc4` defence) weakens coalition robustness for no gain. |
| **O-14** | **Artifact location conflict** between deputy §7 (`Job_Market_paper/docs/Missions/JMP_M08_U6_welfare_proposal_remediation_design_v1.md`) and the commissioning path (`MNL/docs/France_case/P2a/FR_P2a_m08_qw_proposal_design_v1.md`). | Goal-1 disposition required before any write. |

---

## 9. Output discipline

- **Mission ID:** JMP-M08; register item U6 (welfare-proposal remediation, proposal axis).
- **Authoritative inputs:** deputy ruling *JMP_M08_U6_welfare_proposal_remediation_ruling_v1.md*; `FR_P2a_m08_stageD_basis_addendum_v1.md`; U12 access-operand design (as ratified by R-71); R9 ability/preference operators design; `RURO_model_spec_contract_v2_stijn_enhanced.md` §§5, 6, 11, 13; the hash-pinned frozen artifacts listed in the addendum.
- **Decisions made (all PROPOSED):** **Dq1** frozen common support box `B_i` for `q`, `r`, `q^W`, and every `ĝ^S`; **Dq2** node-level two-component defensive mixture with a single scalar `λ`; **Dq3** the uniform coalition-domination criterion `max_S sup_j f^S/r < ∞`; **Dq4** defensive factors `r_E = Bernoulli(0.5)`, `r_Occ = Uniform(4)`, `r_H = Uniform[h_min,h_max]`, `r_W = log-uniform[w_min,w_max]`; **Dq5** `λ = 0.25`; **Dq6** deterministic prefix-consistent allocation (`t ≡ 0 mod 4`) with balance-heuristic MIS weights, one counter-based stream per household, base sub-stream reuse of the frozen 1x draws; **Dq7** four distinct `ĝ^S` objects serving eight coalitions with shared priced draw sets across the `P`/non-`P` pairs; **Dq8** factor-sequential `ĝ^S` samplers with exact densities and an exact non-employment stratum; **Dq9** the pre-EUROMOD normalisation/moment/category test battery; **Dq10** `−log q^W` replaces `−log q` on the welfare axis only.
- **Unresolved decisions:** **O-1 … O-14** (§8). **O-6** and **O-10** are candidate halts; **O-14** blocks any write.
- **Exact output filename:** `MNL/docs/France_case/P2a/FR_P2a_m08_qw_proposal_design_v1.md` *(subject to O-14; the deputy-mandated path is `Job_Market_paper/docs/Missions/JMP_M08_U6_welfare_proposal_remediation_design_v1.md`)*.
- **Next authorised action:** Goal 1 Manager review and freeze of Dq1–Dq10 and disposition of O-1–O-14. On freeze, Dq1–Dq10 and §6's diagnostic list are transcribed into the amended execution contract, after which Stage U6-B (implementation and deterministic tests, MNL application layer, no `dclaborsupply` source change) is the first authorised implementation step. **No EUROMOD execution, no code, and no commit is authorised by this memo.**

**Statement:** no welfare number, no decomposition number, no parameter value, no priced node, and no re-estimation is produced or implied by this memo. No file has been written.	