# JMP-M08 U6-CV1 — Cross-Fitted Control-Variate Closure: Design Memo v1

**Mission stage:** JMP-M08 · U6-CV1 — Cross-Fitted Control-Variate Closure
**Commissioning authority:** Deputy Programme Director, operative sections §§3–8 (pasted verbatim in the commissioning instruction and binding on this memo)
**Document class:** design memo (estimator specification + integrity architecture). **No computation, no code, no EUROMOD execution, no new draw, no welfare number, no decomposition number.** Every numeral below is either a transcribed constant from a named binding instrument or a symbol.
**Status:** **PROPOSED — PENDING GOAL-1 FREEZE.** Nothing here is frozen. The Goal-1 design freeze is the freezing instrument.
**Target repository path:** `docs/Missions/JMP_M08_U6_CV1_control_variate_design_v1.md`
**Author role:** M08 design author (advisory). No file has been written.

**Authoritative inputs**

1. The deputy ruling, operative sections §§3–8, as pasted (binding, verbatim).
2. `JMP_M08_welfare_input_handoff_v2.md` (FROZEN; Goal-1 R-110) — §1 parameter source θ̂_margqh-v2 (theta-bytes `2cf320c3aa4b…`), §1.2 successor input pins, §3 five-scenario S-10, §4 the eight disclosures, §5 the prohibited-claims constraint, §6 rebinding obligations and gate order.
3. `MP_M08_U6_welfare_proposal_remediation_design_v1.md` — the frozen `q^W` architecture: node-level defensive mixture, λ, deterministic allocation, factor forms, atom treatment, CRN/nesting.
4. The U6-D embedded precision ruling as executed: the four-superblock construction of `T16`, `T8_ab`, `T12_-b`, `SE_MC(T16)`, `E_T`, and the functional thresholds.
5. The deputy support-box / `c_scale` ruling governing the 16x basis (piecewise `q^W` off box; box frozen before D9…D16; D1…D8 not regenerated or repriced).
6. The frozen fixed direct-validation panel `F_star` (hashed, n = 203) and the priced R = 93 direct redraws.

**Not used as evidence:** management memos; any object carrying the suspended joint-convention θ̂; any welfare or decomposition numeral (none is cited, computed, or implied).

---

## 0. Executive statement, and the findings surfaced before the design

CV1 attaches a **cross-fitted, analytically-centred linear control-variate correction to each importance-sampling integral, on the integral scale, before `log` and before money-metric inversion**, using only the already-priced 16x basis, a frozen library of controls with exact expectations under the frozen `q^W`, and coefficients estimated on nodes disjoint from the block on which they are applied. It changes the **estimator**; it does not change the **estimand**, the proposal, the draws, θ̂, the normalisation, the operators, the references, S-10, LOC4, or the package source.

The economics of the instrument is narrow and should be stated plainly so that nothing is expected of it that it cannot deliver. The residual Monte-Carlo error in `Î` is driven by the covariance between the importance weight and the node's *observable* coordinates — occupation, hours position, and where in the priced wage range the node sits — because `exp(u)` is monotone in consumption and consumption is monotone in `w·h`. A linear projection on those coordinates removes exactly the part of the weight's variation that the design already knows analytically. It removes **no** part of the variation that is orthogonal to those coordinates, and it removes **nothing at all** from a level offset.

Five findings are surfaced here, before the design, because each bears on whether CV1 can succeed and one of them is potentially blocking.

- **F-1 (blocking candidate — two-box exposure of the 16x basis).** The support-box ruling froze a rebound defensive box *before* D9…D16 and forbade regenerating or repricing D1…D8. If the defensive nodes in D1…D8 were **generated** under the pre-rebind box while `q^W` is **evaluated** under the rebound box, then the design-generating density and the evaluation density differ on part of the basis. That is a property of the *raw* 16x estimator, not something CV1 introduces, and it is outside CV1's authority to repair. For CV1 it has a specific and unavoidable consequence: the analytic centring constants of every box-dependent control are block-group specific, and cannot be formed at all unless Stage A recovers, from the recorded implementation schema, which box generated each block and which box each node's `q^W` evaluation used. **If the two differ for any node, that is a named finding to be returned, not designed around.** See §6, C-1.
- **F-2 (the component-indicator control is exactly degenerate).** Under the frozen deterministic `t ≡ 0 (mod 4)` allocation, the centred proposal-component indicator has a **bitwise zero mean in every block whose node count is divisible by four**. Its contribution to every block estimate is therefore exactly zero, whatever coefficient it receives: it delivers **no variance reduction**. It is retained because it is exact insurance — it becomes non-degenerate precisely if the design's 3:1 balance is ever broken — and because including it partials component-composition variation out of the other coefficients. It must not be counted as one of the working controls when the library's power is assessed. See §2.2.
- **F-3 (CV cannot move a level offset, so gate G8 is a guard, not a verdict).** The registered possibility that the persistent direct-vs-IS disagreement is a household-specific normalisation constant rather than a tail defect (v1 memo §0, §3.4, O-10) is untouched by CV1: a variance instrument cannot close a bias in the level. A CV that materially reduces `E_T` may leave the `F_star` median exactly where it was. The `F_star` gate is therefore correctly read as a guard that CV1 broke nothing — never as evidence that CV1 worked, and never as evidence that it failed.
- **F-4 (the sub-basis coefficient rule is not specified by the ruling, and the obvious convention biases adoption toward YES).** The adoption criterion is `E_T`, which is built from `T8_ab` and `T12_-b`. If the four coefficient vectors estimated on the full 16x design are simply reused inside the sub-bases, then `T12_-b` depends on block `b` through `β̂`, the four leave-one-block-out values are drawn toward one another, `SE_MC` is **understated**, `E_T` is **understated**, and adoption becomes easier exactly in the direction that a self-supervised programme cannot afford. §3.3 specifies a nested rule that removes the leak; §6 registers it as requiring Goal-1 ratification because it extends the ruling.
- **F-5 (§8 of the ruling was not supplied to this memo).** Only the heading "FULL QUANTITATIVE PROMOTION IF CV SUCCEEDS" is available. This memo therefore implements §§3–7 and states the reporting consequences of adoption and rejection; the **promotion** consequences remain Goal-1/deputy bound. See O-9.

If F-1 fires and the box-dependent controls must be dropped, the surviving library is the occupation indicators alone (box-free, exactly categorical) plus the degenerate component indicator. That library will not plausibly deliver the ruling's 20 % improvement on a previously failing primary functional, and CV1 would then be rejected on its own frozen rule rather than repaired. This is stated now, before any result exists.

---

## 1. The target

### 1.1 Which integral is adjusted

Fix a household `i`, a coalition `S ⊆ {A,B,P}`, an S-10 scenario `s ∈ {1,…,5}`, and an integral type `τ ∈ {attained, reference}`. The welfare-side inclusive value is constructed with the non-employment atom held **exact and outside** the sampled average (frozen atom Rao-Blackwellisation; not reintroduced):

```
V_i^{S,s,τ}  =  log [  ĝ_i^{E,S}(0) · exp( u_i^{S,s}(atom) )   +   ĝ_i^{E,S}(1) · I_i^{S,s,τ}  ]
```

with the **work-conditional normalised opportunity integral**

```
I_i^{S,s,τ}  :=  ∫  exp( u_i^{S,s}(j) ) · ĝ_i^{S,τ}( j | e = 1 )  dν(j) ,
                 ĝ_i^{S,τ} = g̃_i^{S,τ} / Z_i^{S,τ}   (analytic Z over the full mixed support)
```

**`I_i^{S,s,τ}` is the object CV1 adjusts, and it is the only object CV1 touches.** Everything downstream — the atom term, `ĝ^{E,S}(0)` and `ĝ^{E,S}(1)`, the `log`, the money-metric inversion, the aggregation to `W1`/`W4`/`W6`, the inequality indices, the Shapley/fixed-background accounting, the S-10 CRN differencing — is applied to the CV-adjusted `Î` in **bit-identical code paths and identical order** to those applied to the raw `Î`. No other substitution occurs anywhere in the stack.

The raw estimator on the 16x basis is the design average of the importance weights

```
y_t  :=  f_i^{S,s,τ}(j_t) / q_i^W(j_t) ,      f_i^{S,s,τ} = exp(u_i^{S,s}) · ĝ_i^{S,τ}(· | e = 1)
Î_raw =  (1/n) Σ_{t=1..n} y_t ,   n = the frozen 16x work-node count for household i
```

where `q_i^W` is evaluated **piecewise** per the support-box ruling: `q_i^W(j) = (1−λ)q_i(j) + λ r_i(j)` on the box and `q_i^W(j) = (1−λ)q_i(j)` for an ordinary-`q` node off the box, with `λ = 0.25` (transcribed) and `r_i ≡ 0` off box.

### 1.2 The adjusted estimator

Let `c(j) ∈ ℝ^P` be the frozen control vector (§2), a function of the node's own attributes only, and let

```
μ_i  :=  E_{q_i^W}[ c(J) ]   ∈ ℝ^P      (exact, analytic, §2)
h(j) :=  c(j) − μ_i                      (the centred control)
```

Partition the 16x node index into the four frozen 4x superblocks `B_1,…,B_4`. For evaluation block `k` and a coefficient vector `β̂^{(-k)}` computed **only from nodes outside `B_k`** (§3),

```
Î^{(k)}  =  (1/n_k) Σ_{t ∈ B_k} [ y_t − β̂^{(-k)′} h(j_t) ]  =  ȳ_k − β̂^{(-k)′} ( c̄_k − μ_i )

Î_CV     =  (1/4) Σ_{k=1..4} Î^{(k)}
```

### 1.3 Unbiasedness for the same normalised integral

**Proposition 1 (design-mean-zero centring).** Let block `B_k` contain exactly `3n_k/4` base-labelled nodes drawn i.i.d. from `q_i` and exactly `n_k/4` defensive-labelled nodes drawn i.i.d. from `r_i`, with the labels fixed by the deterministic `t ≡ 0 (mod 4)` rule. Then for any node-measurable `c` with finite expectation under both components,

```
E[ (1/n_k) Σ_{t∈B_k} c(j_t) ]  =  (1−λ) E_{q_i}[c]  +  λ E_{r_i}[c]  =  E_{q_i^W}[c]  =  μ_i ,
hence  E[ (1/n_k) Σ_{t∈B_k} h(j_t) ]  =  0 .
```

*Proof.* The allocation is deterministic, so the block mean is the fixed convex combination of two i.i.d. sample means with weights exactly `1−λ` and `λ`; take expectations component-wise. The identity `E_{q^W}[c] = (1−λ)E_q[c] + λE_r[c]` holds for the mixture density `q^W = (1−λ)q + λr` **irrespective of the components having different supports**: `r` integrates to one over the box, `q` integrates to one over its own (possibly larger) support, and the mixture identity is linearity of the integral. ∎

Two riders that the implementation must assert rather than assume: the exact `λ` share requires `n_k ≡ 0 (mod 4)` and **zero node exclusions** of any kind within the block; and Proposition 1 requires that every node in `B_k` be a genuine i.i.d. draw from its labelled component — no deterministically inserted chosen-alternative row, no deterministically inserted support row inside the indexed block (v1 memo O-5). Both are gate items (§4, G-A and G-B).

**Proposition 2 (unbiasedness of the fold estimate).** With `β̂^{(-k)` measurable with respect to nodes outside `B_k`, and blocks mutually independent,

```
E[ Î^{(k)} ]  =  E[ E[ ȳ_k − β̂^{(-k)′}( c̄_k − μ_i ) | β̂^{(-k)} ] ]
              =  E[ I − β̂^{(-k)′} · 0 ]  =  I_i^{S,s,τ} .
```

*Proof.* Conditional on `β̂^{(-k)}` the block is an independent design sample; `E[ȳ_k] = E_{q^W}[f/q^W] = ∫ f dν = I` by the same mixture argument as Proposition 1 applied to `y`; and `E[c̄_k − μ_i] = 0` by Proposition 1. Independence of `β̂^{(-k)}` from `B_k` is what licenses pulling it out of the inner expectation — this is the entire content of cross-fitting, and it is why an in-sample OLS control variate would **not** be unbiased. ∎

**Corollary 1 (target identity).** `E[Î_CV] = (1/4)Σ_k E[Î^{(k)}] = I_i^{S,s,τ}`. The adjusted estimator is unbiased for **the same normalised opportunity integral** — same `ĝ = g̃/Z`, same support convention, same `c_ij`, same θ̂, same coalition operator, same reference object — as the raw estimator. CV1 is an estimator change and nothing else.

**Corollary 2 (the `log` is not made worse, and is made slightly better).** `V = log Î` is a concave transform, so neither the raw nor the adjusted estimator is unbiased for `log I`; the leading transform bias is `−Var(Î)/(2I²) + O(n^{-2})` for both. Because CV1 weakly reduces `Var(Î)` when the controls have any explanatory power at all, it weakly reduces this bias by the same factor. This is a secondary benefit, not a claim: it is stated so that no reader infers that applying `log` after a CV introduces a new bias term. Nothing in the memo relies on it.

**Corollary 3 (Shapley linearity).** The fixed-background Shapley weights are constants determined by the coalition lattice, not by the data. Any collection of estimators of the eight coalition values therefore satisfies the accepted accounting identity exactly, by linearity. Gate G-7 (§4) is consequently a test of **implementation**, not of CV validity; it cannot be passed by a CV that is wrong nor failed by a CV that is right.

**What is explicitly not claimed.** CV1 is not claimed to reduce bias in `I` (there is none to reduce), not claimed to close a normalisation offset (F-3), not claimed to improve `V^{dir}` (which it never touches), and not claimed to reduce variance at all for a household whose weight is orthogonal to the control span (in which case `β* = 0` and `Î_CV` differs from `Î_raw` only by estimation noise in `β̂`, which is `O_p(n^{-1})` in the estimator and is the price of the insurance).

---

## 2. The frozen library and its exact analytic expectations

### 2.1 Scope, and what is deliberately excluded

Permitted families, per ruling §4, with the ruling's own restrictions carried verbatim: **no interactions; no polynomial order above two; one omitted category per complete indicator family; no feature selection based on failed functionals; no post-result tuning; the non-employment atom remains Rao-Blackwellised and is not reintroduced.**

Every control is a function of the node's own recorded attributes `(component label, loc4, h, w)` and of frozen geometry constants. **No control requires a price, a utility evaluation, θ̂, a coalition operator, or a reference object.** Three consequences follow immediately and are gate items:

- The control matrix `C_i` (rows `c(j_t)`) and the centring vector `μ_i` are **coalition-invariant, scenario-invariant, and integral-type-invariant**. One `C_i` and one `μ_i` per household serve all eight coalitions × five scenarios × both integral types. Only `y` varies.
- CV1 consumes **zero new EUROMOD pricing and zero new draws**, satisfying ruling §3 by construction rather than by discipline.
- Since `μ_i` is a property of the *proposal*, and the proposal is fitted auxiliary machinery independent of θ̂, `μ_i` is recomputable from the frozen draw-geometry pins alone.

Notation, all household-indexed, all bound at Stage A against the recorded schema (standing practice 13 — the invariant list is derived from the implementation's recorded schema, never from memory):

| symbol | meaning |
|---|---|
| `λ = 0.25` | frozen mixture weight (transcribed) |
| `[h_lo, h_hi]`, `H = h_hi − h_lo` | frozen defensive hours box |
| `[w_lo, w_hi]`, `ℓ_lo = log w_lo`, `ℓ_hi = log w_hi`, `L = ℓ_hi − ℓ_lo` | frozen defensive wage box, log scale |
| `q_Occ,i(k)`, `k = 1..4` | certified empirical LOC4 proposal shares |
| `q_H,i(h) = Σ_{m=1..5} π_{i,m} f_m(h)` | the exact D1 five-mode hours **marginal** (margqh convention), normalised on its own support `S_H` |
| `q_W,i(· | loc4 = k)` | occupation-conditional log-normal `(μ_{i,k}, σ_{i,k})` on its own certified support `[ℓ_a, ℓ_b]` |
| `ℓ := log w` | the log-wage coordinate |

`E_q` is always taken over **`q`'s own support**, which may extend beyond the defensive box; `E_r` is always taken over the box. The mixture identity of Proposition 1 makes this asymmetry harmless.

### 2.2 Family 1 — proposal-component indicator (one control; **exactly degenerate**)

Two categories, `{base, defensive}`; omit `base`; retain `c_comp(t) = 1{t ≡ 0 (mod 4)}`.

```
E_{q^W}[ c_comp ]  =  λ  =  0.25       (exact by construction of the deterministic allocation)
centred values:  0.75  (defensive),   −0.25  (base)
```

**The derivation is trivial and the finding is not.** `c_comp` is a function of the *node index*, not of the node, and under the deterministic rule its block mean is not a random variable. With `n_k ≡ 0 (mod 4)` and no exclusions, the block sum of centred values is `(n_k/4)(0.75) + (3n_k/4)(−0.25) = 0`, and because `0.75` and `0.25` are exact binary doubles and all partial sums are integer multiples of `0.25` within representable range, the sum is **bitwise zero**. Hence `Î^{(k)}` is invariant to `β̂_comp`, and this control contributes **exactly zero variance reduction**.

It is retained for two reasons and neither is variance reduction: (i) it is the design's own balance assertion, promoted into the estimator — if the 3:1 balance is ever broken by an exclusion, the control becomes live and automatically restores unbiasedness of the centring; (ii) in the multivariate regression it partials the between-component composition out of the other coefficients, leaving them to be identified from within-component variation, which is where the actual sampling noise lives.

**F-2 is registered as a reporting obligation:** when the library's power is described in any artifact, the working-control count is `P − 1`, not `P`.

### 2.3 Family 2 — occupation-category indicators (three controls; **unconditionally exact**)

`c_occ,k(j) = 1{loc4(j) = k}`, `k ∈ {2,3,4}`; **omit `k = 1`** (lowest index — a deterministic, result-independent omission rule fixed here).

```
E_{q}[ c_occ,k ]    =  q_Occ,i(k)                       (categorical, exact)
E_{r}[ c_occ,k ]    =  1/4                              (uniform on the four categories, exact)
E_{q^W}[ c_occ,k ]  =  (1 − λ)·q_Occ,i(k) + λ·(1/4)     =  0.75·q_Occ,i(k) + 0.0625
```

This family is **box-free**: `loc4` is defined identically on and off the box, so neither the off-box `q`-mass nor the F-1 two-box exposure touches it. It is the only family that survives every adverse Stage-A finding, which is why §0 identifies it as the fallback library.

Economic content worth one sentence: because `q_W` is occupation-conditional, the occupation indicators are a coarse, exactly-known projection of the wage location, and they carry a large share of the weight's cross-node variation for free.

### 2.4 Family 3 — hours-band indicators (`K_H − 1` controls; **conditionally exact**)

Let the certified hours bands, intersected with `S_H`, be `A_1, …, A_{K_H}`, and let `A_0` denote the residual "outside every band or outside the defensive box" region if it is non-empty. Index `A_0` as `0`; **omit the lowest-indexed non-empty category** (`A_0` if non-empty, else `A_1`). Retain `c_H,k(j) = 1{h(j) ∈ A_k}` for the remaining `k`.

```
E_{r}[ c_H,k ]    =  | A_k ∩ [h_lo, h_hi] | / H                      (uniform hours; exact interval length)
E_{q}[ c_H,k ]    =  ( Σ_{m=1..5} π_{i,m} · F_m( A_k ∩ S_H ) ) / ( Σ_{m=1..5} π_{i,m} · F_m( S_H ) )
E_{q^W}[ c_H,k ]  =  0.75 · E_q[ c_H,k ]  +  0.25 · E_r[ c_H,k ]
```

**Exactness condition.** `E_q` is exact if and only if each D1 mixture component `f_m` has a closed-form band probability `F_m(A)` — a normal-family CDF difference if the modes are continuous, or a membership sum if the modes are atoms at focal hours. **Stage A binds the component family from the recorded schema. If any component's band probability is not available in closed form, the entire hours-band family is omitted before execution** (ruling §4, final sentence). It is omitted as a family, not band by band, because a partial family is no longer complete and its omitted category loses its meaning.

**Box condition.** `E_r` is exact only under the box that actually generated the defensive nodes. If F-1 fires, this family is either block-group-centred (using two exact constants) or omitted — see §6, C-1.

Economic content: this family is the direct instrument against the *hole* failure diagnosed in v1 §1.3 — the D1 mixture places near-zero density between focal points while the target is smooth there — because the band indicators are exactly the coordinates on which base and defensive nodes differ most.

### 2.5 Family 4 — first and second log-wage moments (two controls; **conditionally exact**)

`c_ℓ(j) = ℓ(j) = log w(j)` and `c_ℓℓ(j) = ℓ(j)²`. No higher order (ruling §4).

**Under `r` (log-uniform in `w` ⇔ uniform in `ℓ` on `[ℓ_lo, ℓ_hi]`), closed form:**

```
E_r[ ℓ ]   =  ( ℓ_lo + ℓ_hi ) / 2
E_r[ ℓ² ]  =  ( ℓ_hi³ − ℓ_lo³ ) / ( 3L )  =  ( ℓ_hi² + ℓ_hi ℓ_lo + ℓ_lo² ) / 3
```

*Derivation:* `ℓ ~ U[ℓ_lo, ℓ_hi]` because the density `r_W(w) = 1/(wL)` transforms to `1/L` under `w ↦ log w`; the two moments are the uniform moments, evaluated exactly.

**Under `q`,** condition on occupation and average with the exact categorical weights:

```
E_q[ ℓ ]   =  Σ_{k=1..4} q_Occ,i(k) · m1( μ_{i,k}, σ_{i,k} )
E_q[ ℓ² ]  =  Σ_{k=1..4} q_Occ,i(k) · m2( μ_{i,k}, σ_{i,k} )
```

*Untruncated case* (`q_W` log-normal on `(0,∞)`):

```
m1 = μ_{i,k} ,          m2 = μ_{i,k}² + σ_{i,k}²
```

*Truncated case* (`q_W` log-normal truncated to `[ℓ_a, ℓ_b]`), with `α = (ℓ_a − μ)/σ`, `β = (ℓ_b − μ)/σ`, `Z = Φ(β) − Φ(α)`, and `T` the standard normal truncated to `[α, β]`:

```
E[T]  =  ( φ(α) − φ(β) ) / Z
E[T²] =  1  +  ( α φ(α) − β φ(β) ) / Z
m1    =  μ + σ · E[T]
m2    =  μ²  +  2 μ σ · E[T]  +  σ² · E[T²]
```

*Derivation:* write `ℓ = μ + σT`; the two displayed truncated-standard-normal moments are the standard results obtained from `∫ t φ(t) dt = −φ(t)` and `∫ t² φ(t) dt = Φ(t) − tφ(t)` over `[α,β]`, divided by `Z`; expand `E[ℓ²] = E[(μ+σT)²]`. Both are closed-form in `Φ` and `φ` and evaluate to full double precision.

**Then, for both controls,** `E_{q^W}[·] = 0.75 · E_q[·] + 0.25 · E_r[·]`.

**Exactness condition.** Stage A must bind, from the recorded schema, (i) whether the implemented `q_W` is truncated and on what support, and (ii) the recorded `(μ_{i,k}, σ_{i,k})`. If the implemented `q_W` is not in the log-normal family assumed here, **both moment controls are omitted before execution**; they are not replaced by a numerical approximation, because a numerically-centred control breaks Corollary 1 at exactly the order the gate is trying to protect.

**Box condition.** `E_r` again depends on the generating box; F-1 applies as in §2.4.

Economic content: `ℓ` and `ℓ²` are the linear-quadratic projection of the log of the object that drives `exp(u)`. Since `exp(u)` is convex and increasing in `w`, a second-order log-scale projection captures the bulk of the weight's systematic curvature over the priced range while remaining inside the ruling's order-two restriction. This is the family expected to do most of the work, and it is also the family most exposed to F-1.

### 2.6 The frozen library, assembled

| # | control | family | exact `E_{q^W}` | status |
|---|---|---|---|---|
| 1 | `1{defensive}` | component | `λ = 0.25` | exact; **degenerate (F-2)** |
| 2–4 | `1{loc4 = k}`, `k = 2,3,4` | occupation | `0.75 q_Occ,i(k) + 0.0625` | **unconditionally exact** |
| 5 … 4+`K_H`−1 | `1{h ∈ A_k}`, `k ≠` omitted | hours band | `0.75 E_q + 0.25 E_r`, §2.4 | exact **iff** D1 component CDFs closed-form **and** box resolved |
| next | `ℓ` | wage moment | `0.75 Σ_k q_Occ,i(k) m1 + 0.25 (ℓ_lo+ℓ_hi)/2` | exact **iff** `q_W` family/truncation recorded **and** box resolved |
| next | `ℓ²` | wage moment | `0.75 Σ_k q_Occ,i(k) m2 + 0.25 (ℓ_hi²+ℓ_hiℓ_lo+ℓ_lo²)/3` | as above |

`P = 1 + 3 + (K_H − 1) + 2 = K_H + 5` at full strength; `P = 4` in the fallback library. **No interaction, no cube, no household-clustered pooling, no coalition-specific control, no scenario-specific control, no control derived from `y`.** The library is fixed by this table and is not revisited after any result is seen.

---

## 3. Cross-fitting

### 3.1 Folds

The folds are the **four frozen 4x superblocks** `B_1, B_2, B_3, B_4` of the 16x basis — the same partition that already defines `T12_-b` (leave-one-block-out), `T8_ab` (block pairs, six of them), and `SE_MC(T16)`. No new partition is created, no re-blocking, no reshuffling, and the block map is asserted bitwise identical across all coalitions, scenarios and integral types (CRN preservation, gate G-6).

### 3.2 The per-fold coefficient estimator — exact linear algebra, fixed now

For an evaluation block `k` inside a sub-basis `𝔅 ⊆ {1,2,3,4}`, let `E = 𝔅 \ {k}` be the estimation index set, `n_E = |E|`.

Build, **from the estimation nodes only**:

```
h_t   =  c(j_t) − μ_i                    (analytic centring; t ∈ E)
h̄_E   =  (1/n_E) Σ_{t∈E} h_t             (empirical in-fold mean — a different object from μ_i)
ȳ_E   =  (1/n_E) Σ_{t∈E} y_t
H̃_E   =  rows ( h_t − h̄_E )              (in-fold demeaned)
ỹ_E   =  ( y_t − ȳ_E )
G_E   =  H̃_E′ H̃_E / n_E                  (P × P)
g_E   =  H̃_E′ ỹ_E / n_E                  (P)
s_E   =  trace( G_E ) / P                 (scale reference, estimation-fold only)
```

**The intercept is present and unpenalised, and it is discarded.** Operationally this is the in-fold demeaning above: the fitted model is `y ≈ a + β′h` with `a` profiled out. The intercept is not cosmetic — it is what makes the constant-integrand identity (gate G-2) hold to machine precision, and it is what makes a degenerate `y` produce exactly `β̂ = 0`.

**Ridge / conditioning convention (frozen here, before any result):**

```
A      =  G_E  +  ρ · s_E · I_P
L      =  cholesky( A )                     (lower, float64)
β̂^{(-k)} =  L^{−T} L^{−1} g_E
ρ ladder (frozen, in order):  ρ ∈ { 1e-8 , 1e-6 , 1e-4 }
```

Rules, all pre-registered and all independent of any functional's outcome:

1. **Degenerate-column rule.** Any control column whose in-fold sample variance is **bitwise zero** is removed from `H̃_E` for that fold and its coefficient set to `0`. This preserves unbiasedness exactly (a zero coefficient contributes nothing) and is a degeneracy handler, not feature selection: it is triggered by the design, never by a functional's success or failure, and it is logged per fold.
2. **Ridge escalation.** Start at `ρ = 1e-8`. If the Cholesky fails, or if the reciprocal condition estimate of `A` falls below `1e-12`, escalate one rung and retry. Record which rung was used, per (household, coalition, scenario, integral, fold).
3. **Terminal fallback.** If `ρ = 1e-4` still fails, set `β̂^{(-k)} = 0` for that fold. This reduces that fold **exactly** to the raw block mean, preserving unbiasedness and positivity, and is recorded as a `CV_FOLD_DEGENERATE` event. The count of such events is reported; it is never repaired by widening the ladder after the fact.
4. **No result-driven penalty choice, ever.** The ladder above is the whole of the convention. `ρ` is not tuned, not cross-validated, not selected per functional, and not revisited.

The scale reference `s_E` uses only estimation-fold data, so the ridge itself carries no information from the held-out block. `ρ = 1e-8` relative to the mean eigenvalue scale is deliberately negligible: it exists to defeat the near-collinearity that is *expected* between the hours-band indicators and the D1 mixture modes, and between the occupation indicators and the occupation-conditional wage moments — not to shrink.

### 3.3 The sub-basis rule (F-4), and the fold estimates

The ruling specifies the construction for `T16`: hold out one 4x block, estimate on the other 12x. The adoption criterion `E_T`, however, is built from sub-bases. The rule adopted here extends the ruling minimally and in the conservative direction:

> **Nested cross-fitting rule.** For **any** sub-basis `𝔅 ⊆ {1,2,3,4}` and any evaluation block `k ∈ 𝔅`, the coefficient is estimated on `𝔅 \ {k}` — never on blocks outside `𝔅`.
> `Î_CV(𝔅) = (1/|𝔅|) Σ_{k∈𝔅} [ ȳ_k − β̂^{(𝔅\{k})′}( c̄_k − μ_i ) ]`

Consequences: `T16` uses `𝔅 = {1,2,3,4}`, i.e. 12x estimation — **exactly the deputy's prescription**. `T12_-b` uses 8x estimation and is **exactly independent of block `b`**, so the block jackknife `SE_MC(T16) = sqrt[(3/4) Σ_b (T12_-b − T12_bar)²]` retains its intended meaning. `T8_ab` uses 4x estimation, which gives a noisier `β̂` and therefore, if anything, a **larger** `|T16 − T8_bar|` — again the conservative direction for `E_T`.

**Rejected alternative (named, per F-4):** reusing the four 12x-estimated coefficient vectors inside every sub-basis. It is cheaper and it is the obvious implementation, but it makes `T12_-b` depend on block `b` through `β̂`, draws the four leave-one-out values together, understates `SE_MC`, understates `E_T`, and biases the adoption decision toward YES. It is rejected on that ground alone.

Coefficient fits per (household, coalition, scenario, integral): four at 12x, twelve at 8x, twelve at 4x. All are `P × P` Cholesky solves with `P ≤ K_H + 5`; the arithmetic burden is immaterial next to the already-completed pricing.

### 3.4 The invariant, and how it is asserted

> **Invariant CV-I.** The evaluation block never contributes, in any way, to the coefficient applied to it.

Four assertions, all deterministic, all cheap, all run before any adjusted integral is formed:

- **CV-I.a — index disjointness.** For every `(𝔅, k)`: assert on **integer index arrays** that the estimation set equals `𝔅 \ {k}` exactly, that its intersection with `B_k` is empty, and that their union is `𝔅`. Assert on indices, never on values.
- **CV-I.b — NaN-poisoning probe.** Recompute `β̂^{(𝔅\{k})}` after replacing every `y_t`, `t ∈ B_k`, with `NaN`. The result must be **bitwise identical**. A single non-finite coefficient proves the held-out block entered the fit.
- **CV-I.c — shift probe.** Add an arbitrary frozen constant `κ` to every `y_t`, `t ∈ B_k`. Assert `β̂^{(𝔅\{k})}` is bitwise unchanged **and** `Î^{(k)}` changes by exactly `κ` (to within the recorded floating-point tolerance of the block mean). This is a two-sided proof: the coefficient is blind to the block, and the block mean is exactly linear in it.
- **CV-I.d — no leakage through `μ` or `ρ`.** Assert that `μ_i` is a function of the frozen geometry pins only (hash-checked, §2.1) and that `s_E`, `ρ` and the degenerate-column set were computed from `E` only.

A failure of any of CV-I.a–d is a **halt**, not a warning, and CV1 is rejected without further evaluation.

---

## 4. Integrity gates as implementable tests

The ruling's §6 list plus the §7 `F_star` condition, restated as ten gates. Each states its statistic, its tolerance, its evidence artifact, and its failure consequence. Tolerances are transcribed from the ruling where the ruling gives them.

| gate | test | tolerance | consequence on failure |
|---|---|---|---|
| **G-1** | **Analytic control expectations.** Each `μ_{i,p}` computed by two independent routes and compared: (a) the closed form of §2; (b) an exact second route — exhaustive categorical summation for indicator families, and fixed-node Gauss–Legendre quadrature on the density (never on draws) for the hours mixture and the truncated-normal moments, at a node count whose analytic error bound is certified below the tolerance. Plus two identities: each complete indicator family's expectations **including the omitted category** sum to `1`; and `μ_p = 0.75 E_q[c_p] + 0.25 E_r[c_p]` recomputed from separately stored components. | `1e-12` absolute on the identities and on the two-route agreement | **CV1 rejected.** The control is not repaired or re-derived after the fact. |
| **G-2** | **Constant-integrand identity.** Replace `y_t ← κ` (frozen constant) for all `t`. Assert every fold coefficient is exactly `0` and `Î_CV = κ`. | `1e-12` relative | CV1 rejected (indicates a missing or penalised intercept). |
| **G-3** | **Zero-coefficient bitwise reproduction.** Force `β̂ ≡ 0` throughout. Assert `Î_CV` equals the raw estimator **bitwise**, where the raw comparator `Î_raw^{blockavg} = (1/4)Σ_k ȳ_k` is computed under the **identical block-then-average reduction order**. Separately report `|Î_raw^{blockavg} − Î_raw^{flat}|` as a reduction-order diagnostic. | bitwise for the first; `1e-12` relative for the diagnostic | CV1 rejected. **Note:** specifying the comparator's reduction order is not a weakening — a flat-sum comparator cannot be bitwise-equal to a block-average in floating point, and a gate written against it would be unfalsifiable. |
| **G-4** | **Positivity and finiteness.** Every adjusted integral `Î^{(k)}` and `Î_CV(𝔅)`, for every household, coalition, scenario, integral type and sub-basis, is finite and **strictly positive**. | exact | **CV1 rejected globally** (ruling §6: "Any non-positive integral … rejects CV1"). **No clipping, no flooring, no truncation, no per-household fallback** — those would reintroduce level bias into a level-gated quantity, which is the ground on which weight truncation was already rejected in the v1 design (§7.4). The count and identity of offending cases is reported. |
| **G-5** | **Target identity.** Re-hash and assert unchanged: θ̂ bytes `2cf320c3aa4b…`; the four successor input pins; the frozen support box hash; the coalition operator, reference and `Z` objects; the five S-10 scenario vectors; the package gitlink `27756a06`. Plus the algebraic assertion that the CV enters solely as an additive term with analytic design-mean zero (Corollary 1). | exact / hash equality | halt (fail-closed, per handoff §1.2). |
| **G-6** | **Block and CRN identities.** Assert the node index array, the block map, the component-label pattern, and the **control matrix `C_i`** are bitwise identical across all eight coalitions, all five scenarios, and both integral types; assert `μ_i` identical likewise. Assert `n_k ≡ 0 (mod 4)`, exact `λ` share per block, and **zero node exclusions**. Assert no deterministically-inserted row (chosen alternative, support row) lies inside the indexed 16x block. | bitwise / exact counts | halt. (This gate absorbs Proposition 1's riders, listed there as G-A and G-B.) |
| **G-7** | **Shapley exactness.** The accepted fixed-background accounting identity over the eight coalition values holds under CV to the accepted tolerance, and the same identity holds under raw. Per Corollary 3 this is an implementation test. | the accepted tolerance, unchanged | halt. |
| **G-8** | **`F_star` direct-vs-CV.** On the hashed fixed panel (n = 203), for **all eight** coalitions, `median_{F_star} |V^{dir} − V^{IS,CV}| ≤ 0.5` nats, reusing the priced `R = 93` redraws with **zero new direct pricing** (report if otherwise; the six-hour guard applies). Report `n`, p90, max, share > 0.5, signed median and IQR per coalition, and the raw-16x panel values alongside. | `0.5` nats on the median, per coalition | CV not adopted. **Read per F-3:** this is a guard, never a verdict on CV quality. |
| **G-9** | **No support / sign / operator change.** Zero off-box count change; support box, operators, references, disclosure set unchanged; and every functional's **sign and ordering** identical between raw `T16` and CV `T16`, and between CV `T16` and every CV `T12_-b`. No sign claim where the 95 % MC interval covers zero. | exact | CV not adopted (and a sign flip is additionally reported as a finding). |
| **G-10** | **Synthetic analytic bias demonstration**, two parts, both at zero new draws and zero pricing — see §4.1. | see §4.1 | CV1 rejected. |

### 4.1 G-10 in full

**Part (a) — in-span exactness (deterministic).** Choose frozen constants `a, b, d` and define the synthetic integrand `f°(j) = q_i^W(j) · ( a + b·ℓ(j) + d·1{loc4(j) = 2} )`, so that `y°_t = a + b ℓ_t + d·1{loc4_t = 2}` and the true value is available in closed form as

```
I°_i  =  a  +  b · μ_{i,ℓ}  +  d · μ_{i,occ2}
```

using precisely the §2 constants. Because `y°` lies exactly in the span of the intercept and two library controls, the fitted residual is zero, `β̂` recovers `(b, d)` exactly, and the CV-adjusted estimate must equal `I°_i` to floating-point precision — with **zero Monte-Carlo error**, for every household, while the raw estimator has non-zero error. **Tolerance `1e-12` relative.** This simultaneously demonstrates unbiasedness, the correctness of `μ_i`, and the mechanism.

**Part (b) — out-of-span bias, using the 1,555 independent household replicates.** Choose a frozen `a° ≠ 0` and define `f°(j) = q_i^W(j) · exp( a° ℓ(j) )`, whose exact value is again closed-form:

```
I°_i  =  0.75 · Σ_k q_Occ,i(k) · M_k( a° )   +   0.25 · ( e^{a° ℓ_hi} − e^{a° ℓ_lo} ) / ( a° L )
```

with `M_k(a°)` the (truncated) log-normal moment-generating function in `ℓ` — `exp(a°μ_{i,k} + a°²σ_{i,k}²/2)` untruncated, and the standard `Φ`-shifted form under truncation. `exp(a°ℓ)` is deliberately **outside** the span of `{1, ℓ, ℓ², indicators}` and deliberately mimics the exponential-in-log-wage shape of the true welfare integrand. Each household's node stream is independent, so the 1,555 values of `(Î°_CV,i − I°_i)/I°_i` are independent replicates of the same design. Pre-registered statistic and threshold, fixed here before any number exists:

```
t°  =  mean_i( relative error )  /  [ sd_i( relative error ) / sqrt(1555) ]
PASS iff  |t°| ≤ 3.0 ,  and the same statistic computed for the raw estimator is reported alongside.
```

Both parts consume only the existing node attributes. Neither requires a price, a utility evaluation, θ̂, or a new draw.

---

## 5. The adoption rule as a decision table

Ruling §7 is a **single global conjunction**. There is no per-functional switching, no per-coalition switching, no per-measure switching, no "adopt for Ginis only", and no hybrid. Either every paper-facing functional is computed under CV, or every one is computed under raw 16x.

Let `E_T^raw` and `E_T^CV` denote the U6-D precision statistic `E_T = max(|T16 − T8_bar|, 1.96·SE_MC(T16))` computed under the raw and CV estimators respectively, with `SE_MC(T16) = sqrt[(3/4) Σ_b (T12_-b − T12_bar)²]` in both cases, and with the CV sub-bases constructed by the nested rule of §3.3.

| # | condition (ruling §7) | implementable test | evidence artifact |
|---|---|---|---|
| **A-1** | `E_T` weakly decreases for the four named functionals | `E_T^CV ≤ E_T^raw` for **each** of: `W1` mean, `W1` Gini, `φ_A + φ_B`, `s_opp` | paired `E_T` table, raw vs CV, all functionals, none omitted |
| **A-2** | no `W1` component-level `E_T` rises by more than 10 % | `E_T^CV ≤ 1.10 · E_T^raw` for **each** component level in the frozen set `{φ_A, φ_B, φ_P, R_bg, φ_A+φ_B}` | same table, ratio column |
| **A-3** | all signs and ordering unchanged | sign and rank of every functional identical: raw `T16` vs CV `T16`, and CV `T16` vs each CV `T12_-b` | sign/order table (gate G-9) |
| **A-4** | at least one **previously failing primary functional** improves by 20 % | ∃ a functional that **failed its U6-D threshold under raw** with `E_T^CV ≤ 0.80 · E_T^raw`. The set of "previously failing" functionals is taken from the accepted raw-16x U6-D record and is **fixed before CV numbers exist** | the accepted raw-16x functional/threshold table, transcribed |
| **A-5** | every CV integrity gate passes | G-1 … G-10 all PASS | the gate table |

**Verdict rule.** `CV1-ADOPT` iff A-1 ∧ A-2 ∧ A-3 ∧ A-4 ∧ A-5. Otherwise `CV1-REJECT(named condition)` and **the raw 16x estimator is retained unchanged**. No condition is weighed against another; no near-miss is discretionary; the named failing condition is recorded.

### 5.1 What is reported under adoption

- Every paper-facing functional is the CV value, on the 16x basis, with the **raw 16x value reported as a companion column in every table** — never suppressed, never relegated to a footnote.
- A methods disclosure states, in the manuscript and the technical appendix: that the reported integrals are cross-fitted control-variate estimates of the *same* normalised opportunity integral (Corollary 1); the exact frozen library; the four-superblock fold structure; the frozen ridge convention and constant; the degeneracy of the component control (F-2); and that the CV is a **variance** instrument that neither adds nor removes bias in `I` and does not address any level offset (F-3).
- The eight required disclosures of handoff §4 and the standing prohibited-claims constraint of §5 apply unchanged and in full. In particular, disclosure 3 (finite-`R` approximation) and disclosure 7 (inference scope) are untouched: **CV1 does not propagate proposal-draw uncertainty, does not produce confidence intervals, and `E_T` remains a Monte-Carlo precision statistic, not a sampling-uncertainty statement.**
- The `F_star` panel table is reported under both estimators.

### 5.2 What is reported under rejection

- The raw 16x results stand exactly as recorded, unmodified.
- CV1 is reported in the technical appendix as a **negative methodological result**: the design, the frozen library, the named failing condition, and the gate table. This is a reporting obligation, not an option — a suppressed failed attempt is precisely the selection the pre-registration exists to prevent.
- **No CV number may appear in, support, or motivate any paper-facing claim**, in any table, figure, footnote or draft. No sentence of the form "the control-variate variant gives …" is admissible for a functional that did not clear the global rule.
- No re-specification of the library, no second `λ`, no `ρ` re-tuning, no additional control family, and no 32x / QMC / second proposal redesign is self-authorised. The next step is a deputy return with the gate table attached.

---

## 6. Frozen vs Stage-A-bound, open items, and the coherence check

### 6.1 Frozen by this memo (subject to Goal-1 freeze)

**Dcv1** the adjusted object is the work-conditional integral `I_i^{S,s,τ}`, before `log` and inversion, with the atom exact and outside; **Dcv2** the linear, analytically-centred, cross-fitted CV form of §1.2; **Dcv3** the library of §2.6 with the omission rules (omit `base`; omit lowest-indexed category, off-box residual indexed `0`); **Dcv4** the closed-form expectations of §§2.2–2.5, with the stated exactness conditions and the omit-before-execution rule; **Dcv5** the four 4x superblocks as folds; **Dcv6** the per-fold estimator of §3.2 including the **unpenalised intercept**, the relative-trace ridge `ρ ∈ {1e-8, 1e-6, 1e-4}` ladder, the bitwise-zero-variance column drop, and the `β̂ = 0` terminal fallback; **Dcv7** the nested sub-basis rule of §3.3; **Dcv8** the CV-I.a–d assertions; **Dcv9** the ten gates with the tolerances of §4; **Dcv10** the global adoption conjunction of §5 and the reporting consequences of §§5.1–5.2.

### 6.2 Stage-A-bound (from the recorded implementation schema, never from memory — standing practice 13)

The exact recorded form of the welfare-side `V^{IS}` including the atom decomposition; `n` and `n_k` and the divisibility assertions; the D1 mixture component family and its band probabilities; the implemented `q_W` family, truncation and recorded `(μ_{i,k}, σ_{i,k})`; the recorded `q_Occ,i`; the certified hours band edges; the frozen box constants and **which box generated each block**; the recorded treatment of the chosen-alternative and support rows relative to the indexed block; whether the reference integral shares the 16x node set and `q^W`; the accepted Shapley accounting identity and its tolerance; the accepted raw-16x functional/threshold table that fixes A-4's "previously failing" set.

### 6.3 Open items for the Goal-1 freeze

| # | item | status / recommendation |
|---|---|---|
| **O-1** | **F-1 two-box exposure.** Which box generated each block; which box each node's `q^W` used. | **Blocking.** Stage-A determination required before any `μ_i` is formed. If generation and evaluation boxes differ for any node, **return** — do not repair inside CV1. |
| **O-2** | Hours-band family exactness (D1 component CDFs). | Omit the family before execution if not closed-form. Ratify the omit-as-a-family rule. |
| **O-3** | Wage-moment exactness (`q_W` family/truncation). | Omit both moment controls before execution if not established. |
| **O-4** | The nested sub-basis rule (§3.3, F-4). | **Requires ratification**: it extends the ruling's §5 construction to sub-bases, and `E_T` is the adoption criterion. The rejected alternative is named. |
| **O-5** | The ridge constant `ρ = 1e-8` and its ladder. | Proposed and frozen here per the ruling's "freeze any conditioning/ridge convention before results". Ratify or set a different constant **now**. |
| **O-6** | G-3's block-average reduction-order comparator. | Ratify; a flat-sum comparator makes the bitwise gate unfalsifiable. |
| **O-7** | G-10(b)'s `\|t°\| ≤ 3.0` threshold and the frozen `a°`, `a`, `b`, `d`, `κ` constants. | Pre-register the numerical constants at freeze, before execution. |
| **O-8** | Whether the reference integral shares the 16x nodes and `q^W`. | If it does not, its own library and expectations must be derived, or CV is not applicable to it — and a CV applied to one leg only is a design the ruling's §5 ("attained/reference integral") does not contemplate. Stage-A binding; candidate return. |
| **O-9** | **Ruling §8 not supplied** (F-5). | The promotion consequences of `CV1-ADOPT` are unbound by this memo. Goal-1 to obtain and transcribe §8 before the adoption verdict is acted on. |
| **O-10** | Fate of the `CV_FOLD_DEGENERATE` count. | Recommend: reported, non-gating; but a count above a pre-registered share should be a named finding rather than a footnote. Goal 1 to set the share **before** execution. |

### 6.4 Coherence check

The design was checked against its own frozen environment. Incoherences are named below; none is designed around.

- **C-1 (F-1, blocking).** The support-box ruling permits a 16x basis whose blocks were generated under two different defensive boxes. The CV's centring constants are box-dependent for two of four families. **Resolution posture:** determine per block at Stage A; if the boxes differ, the correct CV centring is block-group specific and remains exact — but the prior question of whether the *raw* estimator's own design expectation is affected belongs to the raw estimator's record and to the deputy, not to CV1. **Named finding; return, not repair.**
- **C-2 (F-2).** A permitted control family is exactly degenerate under a frozen design choice. Retained with the degeneracy stated, and excluded from any statement of the library's power.
- **C-3 (F-3).** Gate G-8 cannot discriminate CV quality if the residual disagreement is a level constant. Named; G-8 is read as a guard.
- **C-4 (F-4).** The ruling specifies cross-fitting for `T16` but the adoption statistic is built from sub-bases. Closed by the nested rule, ratification requested at O-4.
- **C-5.** The ruling forbids "feature selection based on failed functionals"; §3.2's degenerate-column rule is data-dependent. Reconciled: the trigger is bitwise zero in-fold variance of a *control*, which is a property of the design and is independent of every functional's outcome. The reconciliation is stated so that a reviewer does not have to reconstruct it.
- **C-6.** Positivity risk (G-4) is largest exactly for the households where CV is most valuable — high-variance households with small `Î`. The rule that a single non-positive integral rejects CV1 globally is therefore genuinely binding, not decorative, and no fallback softens it.
- **C-7.** Unbiasedness (Proposition 1) requires that no deterministically-inserted row sits inside an indexed block; the v1 design left the chosen-alternative and support-row treatment as an open Stage-A item (O-5 there). If such a row is inside the block, the CV is **not** unbiased and the correct response is to exclude that row from both the raw and CV averages — which is a change to the raw estimator and therefore **outside CV1's authority**. Named; gate G-6 detects it; a detection is a return.
- **C-8.** `E_T` mixes an absolute difference and a jackknife interval; under CV both components move. A-1's "weakly decreases" is therefore evaluated on `E_T` itself and not on either component separately — as the ruling writes it. Component-wise movements are reported for transparency, non-gating.
- **C-9.** No incoherence was found between CV1 and: handoff §6 (rebinding, gate order — CV1 sits strictly downstream of U6 and upstream of nothing that it alters); the S-10 CRN differencing (the control matrix is scenario-invariant, so CRN differencing is *strengthened*, not weakened); LOC4 sequencing (CV1 touches no density, so the LOC4 forward statement is unaffected); or the package gitlink freeze (CV1 is application-layer arithmetic on existing arrays).

---

## 7. Output discipline

- **Mission ID:** JMP-M08 · U6-CV1 — Cross-Fitted Control-Variate Closure.
- **Authoritative inputs:** deputy ruling §§3–8 (verbatim, as pasted); `JMP_M08_welfare_input_handoff_v2.md` (FROZEN, R-110); `MP_M08_U6_welfare_proposal_remediation_design_v1.md`; the U6-D embedded precision ruling as executed (`T16`/`T8_ab`/`T12_-b`/`SE_MC`/`E_T` construction and thresholds); the deputy support-box and `c_scale` ruling for the 16x basis; the hashed `F_star` panel and the priced `R = 93` direct redraws.
- **Decisions made (all PROPOSED):** **Dcv1–Dcv10**, §6.1.
- **Unresolved decisions:** **O-1 … O-10**, §6.3. **O-1 is blocking**; **O-4, O-5, O-6, O-7** must be ratified *before* execution or the pre-registration is void; **O-8** and **O-9** are candidate returns.
- **Exact output filename:** `docs/Missions/JMP_M08_U6_CV1_control_variate_design_v1.md`.
- **Next authorised action:** Goal-1 Manager review, freeze of Dcv1–Dcv10, and disposition of O-1–O-10 — **beginning with O-1**, since a two-box finding voids two of the four control families and, with them, the plausibility of clearing adoption condition A-4. On freeze, Dcv1–Dcv10 and the §4 gate table are transcribed into the amended execution contract, after which the first authorised implementation step is Stage CV1-B (deterministic tests G-1, G-2, G-3, G-10(a) and the CV-I probes only, on the existing 16x arrays, MNL application layer, no `dclaborsupply` source change, gitlink frozen at `27756a06`). **No adjusted welfare integral, no EUROMOD execution, no new draw, no code and no commit is authorised by this memo.**

**Statement:** no welfare number, no decomposition number, no inequality index, no parameter value, no priced node, no re-estimation, and no new draw is produced or implied by this memo. Every numeral appearing above is either a transcribed constant from a named binding instrument (`λ = 0.25`; `1e-12`; `0.5` nats; `10 %`; `20 %`; `R = 93`; `n = 203`; the θ̂ and gitlink hash prefixes) or a convention frozen here for the first time and flagged as such (`ρ ∈ {1e-8, 1e-6, 1e-4}`; `|t°| ≤ 3.0`). No file has been written.