# JMP-M08 — Common-Opportunity RUM Benchmark: Estimand Design

**Mission:** JMP-M08 — France 2016 Singles Welfare Integration and Baseline Decomposition Prototype
**Sub-item:** deputy ruling `JMP_M08E_E2_closure_notebook_and_RUM_ruling_v1.md` §3 (binding)
**Register item:** proposed as `RUM-BENCH` — number to be assigned by the Goal 1 Manager
**Document class:** design memo (economics + estimand specification). No computation, no code execution, no estimation, no welfare number, no EUROMOD call.
**Status:** **PROPOSED — PENDING GOAL-1 FREEZE.** Nothing here is frozen. The Goal-1 freeze instrument is the binding step; Stage A binds the residual column/coordinate strings.
**Target repository path:** `docs/Missions/JMP_M08_RUM_benchmark_estimand_design_v1.md`
**Author role:** M08 design author (advisory)

**Authoritative inputs used**

1. `JMP_M08E_E2_closure_notebook_and_RUM_ruling_v1.md` §3 (the mandate, verbatim), §1 (E2 closure status), §4 (corrected S-10 set), §5 (routing and return).
2. `FR_P2a_m08e_E0_estimand_audit_v1.md` — §1 (executed draw algorithm), §2.1 (job space, base measure, population objective), §2.2 (sampled-likelihood estimand and Lemmas 1–2), §2.3 (chosen row), §2.4 (non-employment atom), §5 (VERDICT `E0-CONFIRMED-MARGINAL`), §5.1 (the exact fields the corrected convention changes).
3. `JMP_M08_access_equalisation_operand_design_v1.md` (U12) — §1.1 (core), §2 (D1 cell partition), §3 (operand coordinate by coordinate), §5 (access/ability boundary), §6 (rejected alternatives), §7 (V1–V7).
4. `JMP_M08_ability_preference_operators_design_v1.md` (R9) — §2 (ability operator and references), §2.5 (frozen joint `Π`), §3 (preference operator), §4.1 (the eight coalitions), §4.4 (grand-coalition degeneracy and the `c_ij` residual), §4.5 (level-of-aggregation gap).
5. `RURO_model_spec_contract_v2_stijn_enhanced.md` — §3 (index), §5 (alternatives/proposal), §7 (preference utility), §8–§10 (opportunity blocks), §11 (proposal correction), §12 (likelihood and safeguards), §15–§17 (normalisations, parameters, pins).
6. `Aaberge_Colombino_Wennemo_2009.md` (project literature note) — used **only** as the taxonomy of conventional choice-set specifications (job dummy `d₀`, hours-peak dummies `d₁,d₂`) and for the in-sample-fit-is-uninformative finding.

**Not used as data:** project memory; management memos; the Haydar–Maniquet theory paper, which is cited in §4 **definitionally only** (which arguments each `Wᵏ` takes), never as JMP material.

---

## 0. One-paragraph summary

The benchmark is a conditional sampled-likelihood model on the **same** job space, the **same** frozen draw geometry under the **corrected marginal** proposal convention, and the **same** budget mapping, in which every household's index carries **one frozen, normalised, household-invariant opportunity density `ḡ(j)`** in place of its own `g(j; xᵢ, θ̂ᵒᵖᵖ)`, and in which the preference block is **re-estimated** against that index. The proposed `ḡ` is the grand-opportunity-coalition object `ĝ^{AB}` from the ratified `A` and `B` operators, **after an explicit normalisation step that the operators memo does not perform**. Two admissible free-parameter sets exist and the choice between them is the single most consequential open item (§1.6, item **B1**). The estimand is scientifically well-defined; §6 records four named findings, one of which — that `g ≡ 1` has **no population estimand at all** on the accepted job space — strengthens the ruling's prohibition and requires a wording correction in the manuscript's main question.

---

## 1. The estimand, exactly

### 1.1 The population object

Carried forward unchanged from the E0 audit §2.1. A job is `j = (e, loc4, h, w)` on the mixed space

```
J  =  {⊥}  ⊔  ( {1,2,3,4} × [H_MIN, H_MAX] × (0,∞) )
```

with base measure `ν = δ_⊥ ⊕ (counting on loc4) ⊗ (Lebesgue on h) ⊗ (Lebesgue on w)`.

The accepted **RURO** population object is

```
p_i^RURO(j)  =  exp( u_i(c_ij, ℓ_ij; θ^pref) + log g(j; x_i, θ^opp) ) / Z_i(θ)
Z_i(θ)       =  ∫_J exp( u_i + log g ) dν
```

with `log g` factorised as in U12 §1.1 into `g^E`, `g^Occ`, `g^H`, `g^W`.

The **RUM** population object replaces the household-indexed opportunity factor by a single frozen density:

```
p_i^RUM(j; θ^pref)  =  exp( u_i(c_ij, ℓ_ij; θ^pref) + log ḡ(j) ) / Z̄_i(θ^pref)
Z̄_i(θ^pref)         =  ∫_J exp( u_i + log ḡ ) dν
∫_J ḡ dν            =  1                                   [normalisation — §2.2, mandatory]
```

**`Z̄ᵢ` remains household-specific.** This must be said plainly because the name "common-opportunity" invites the opposite reading: only the *opportunity* factor is common. `u_i` still varies across households through the EUROMOD-evaluated budget `c_ij`, through leisure `ℓ_ij`, through the taste covariates, and through the sex-specific preference block. The RUM is therefore **not** a model in which all households have the same choice probabilities; it is a model in which all households face the same **job market** and differ in budget, demographics and tastes. That is precisely the conventional labour-supply setting.

The population criterion and target are the direct analogues of E0 §2.1:

```
Q̄_0(θ^pref)  =  E[ u_i(j*_i; θ^pref) + log ḡ(j*_i) ]  −  E[ log Z̄_i(θ^pref) ]
θ̂^pref,RUM   =  argmax  Q̄_0
```

### 1.2 The sampled estimand

Identical machinery, identical draws, identical correction. Per household `i`, over the accepted 101 rows (1 chosen + 100 simulated):

```
ℓ_i^RUM(θ^pref)  =  [ u_i(j*_i) + log ḡ(j*_i) ]
                  − log Σ_{r=0..R} exp( u_i(j_r) + log ḡ(j_r) − log q̃_i(j_r) )
```

with `log q̃_i` the **corrected marginal** `log_prior` column, i.e. the M08E-corrected geometry in which

```
q_H^marg(h) = Σ_k (w_k / width_k) · 1{h ∈ B_k}
log q̃_i     = log q_E + working · ( log q_H^marg + log q_W + log q_Occ )
```

the chosen row carries exactly `0.0`, and the simulated non-employment rows carry exactly `log(π0)` (E0 §5.1). **No field of the geometry changes and no draw is re-run.** The RUM re-uses the corrected geometry byte-for-byte; its sha256 is hash-asserted (N3, §5.2). Lemma 1 of E0 §2.2 transfers verbatim: with `q̃ = q` `ν`-a.e., the sampled sum converges to `Z̄_i(θ^pref)`, and the chosen row's zero correction, the `−log R` constant and the `O(1/R)` term behave exactly as recorded in E0 §2.3. The RUM inherits the corrected convention's consistency and its finite-`R` bias order; it inherits nothing else.

**Non-employment treatment is unchanged**: `⊥` is the same atom, drawn with the same `π0`, with `hours = wage = 0` and `loc4 = −1`, and the same with-replacement duplication handled by the same identity (E0 §2.4). Under the RUM the *weight* on `⊥` relative to the working rows is set by `ḡ`'s employment margin rather than by the household's own regional/GSUR environment.

### 1.3 What is identified when `g` is common

`log ḡ(j)` is a **known function of the job coordinates alone**. It therefore enters the sampled logit as an alternative-specific **offset**, and the estimation problem is a conditional logit with offset on the free set. Four exact consequences:

**(i) The additive constant is not recoverable and must be imposed.** Adding any constant `c` to `log ḡ` adds `c` to every row of every household — including the chosen row — and cancels in the log-softmax. So `ℓ_i^RUM` and `θ̂^pref,RUM` are exactly invariant to the normalisation of `ḡ`. **The likelihood cannot tell a density from a kernel.** This is the M08E defect in its most general form, and it is why §2.2's normalisation step is mandatory rather than cosmetic: it is invisible at estimation and decisive at welfare (§4.2). Checked by **N6**.

**(ii) The offset is not inert.** `ḡ` varies over `j`, and so does the preference index (through `c_ij` and `ℓ_ij`). The offset reweights which alternatives are treated as plentiful and therefore moves `θ̂^pref`. What survives as *effective* content is the component of `log ḡ` not spanned, across the drawn rows, by the `j`-variation the free parameters can generate. Under the enlarged free set of RUM-B (§1.6) that span is larger and the effective content of `ḡ` is correspondingly smaller.

**(iii) Occupation availability is very nearly inert.** `loc4` enters neither the budget nor `u_i`: under the RUM it appears only in `log p̄̄(loc4)` and in the conditional wage location `μ̄(loc4)`. A common pmf over a coordinate that enters nothing else is a constant across households and does not discriminate between alternatives except through its coupling with `w`. The operational statement is sharp: **the identified content of the occupation and wage factors of `ḡ` is the common marginal offered-wage density**

```
φ̄(w)  =  Σ_loc  p̄̄(loc4 = loc) · φ_LN( w | μ̄(loc), σ̂ )
```

**and the `loc4` decomposition of it carries no separate content in the benchmark.** This is the exact mirror of U12 §3.4's hours-degeneracy statement and of R9 §2.3's `σ`-degeneracy statement, and it belongs in the same manuscript caveat block. It also fixes the LOC4 interface: under the four-density variant, LOC4 moves the RUM benchmark **only** through `φ̄(w)`, which is a one-line forward statement rather than a re-design (§5.4).

**(iv) The RUM admits no access/ability split.** With a single common opportunity object there is no household-varying availability and no household-varying wage technology, so nothing in the benchmark corresponds to the `A`/`B` cells of the D1 partition. The RUM's only coherent decomposition is preference-versus-common-environment, and the common environment contributes **zero** to cross-household variation by construction. The RUM-versus-RURO comparison is therefore against the **headline** opportunity-versus-preference cut only (charter §4.3), never against the nested access-versus-ability split. Stated for the manuscript so that no reader infers a benchmark for the nested numbers.

### 1.4 Which RURO parameters have no RUM counterpart

Under the primary free set, the entire opportunity side loses free-parameter status and survives only as frozen arithmetic inside `ḡ`:

| RURO block | Status in the RUM |
|---|---|
| `g^E`: employment intercept, region dummies, GSUR level | frozen inside `ḡ`; evaluated once at the ratified access references (U12 §3.2) |
| `g^E`: GSUR×education cells | frozen; both slots at reference (R9 §2.6, `{A,B}` row) |
| `g^Occ`: the conditional table `p̂(loc4 \| dgn, educ3)` | frozen as the dwt marginal `p̄̄(loc4)` (R9 §2.5, `{A,B}` row) |
| `g^H`: hours-band shifters | frozen (already household-invariant in the certified spec) |
| `g^W`: Mincer block `β_w0, β_w_educL, β_w_educH, β_w_pexp, β_w_pexp²` | frozen at the ability references `ē, p̄ₑₓₚ, p̄ₑₓₚ²` (R9 §2.2) |
| `g^W`: `δ_occ[loc4]` | frozen; enters only `μ̄(loc4)` |
| `g^W`: `σ` | frozen; already common in the certified spec |
| `u_i`: the two singles preference blocks | **re-estimated** |
| couples-side pins (`theta_l_m`, `beta_ll`, and the remaining couples coordinates) | vacuous under singles-only scope (R9 §3.3); asserted for provenance, verified non-entering at Stage A |

**The ability channel has no RUM counterpart whatsoever.** There is no household-specific wage-offer distribution in the benchmark, so a household's own education and experience no longer shape which `(h, w)` packages it is treated as able to reach. This is the single largest structural difference and it should be named in the manuscript as such, not left to be inferred from a parameter table.

Exact coordinate strings for every row above bind at Stage A against the frozen spec YAML and the accepted corrected-baseline parameter file. This memo names objects, not guessed strings.

### 1.5 How the preference block's interpretation changes

`θ̂^pref,RUM` is **not** the RURO preference block re-measured. It is a reduced-form taste block that must additionally rationalise every systematic association between household characteristics and realised `(e, h, w)` that the common `ḡ` cannot represent. Three concrete statements, all pre-registered here so that they are read as predictions and not as post-hoc rationalisation:

1. **Sex.** The RURO model routes part of the male–female difference in realised employment and occupation through `g^Occ(· | dgn)` and the regional employment margin. Under the RUM those channels are common, so the difference must be carried by the sex-specific preference block — principally `beta_l0_sf`, `beta_l_nkids_sf` and the leisure–age profile. **Predicted direction:** measured leisure preference shifts *toward* the group facing the less favourable offer environment. If the estimated shift is in the opposite direction, that is a finding requiring explanation, not a nuisance.
2. **Consumption channel.** Wage variation reaches `u_i` only through `c_ij`. With a common offered-wage density, the chosen row's wage becomes the only wage information the preference block can use, so `beta_c_*` and `theta_c_*` should be expected to move as well. Boundary activity on the consumption Box-Cox exponents is a live possibility and must be reported, not clipped away.
3. **Boundary coordinates.** The accepted vector carries two upper-bound-active age² leisure coefficients (R9 §3.4). The RUM may or may not reproduce that active set. The pre-registered rule: the admissible region and bound set are **identical** to the certified ones; whichever coordinates are bound-active in the RUM are excluded from the covariance object with literal `NA` under the certified convention; and any RURO-versus-RUM comparison of preference *estimates* carries that caveat explicitly.

This section is the paper's mechanism, stated in advance: **the misclassification claim is the claim that these three shifts occur and that they move the welfare object.**

### 1.6 The free-parameter set — two admissible readings, one ratification item

The ruling's operative sentence is: *replace heterogeneous household opportunity objects with one frozen common opportunity measure and re-estimate the preference parameters.* Two readings comply with it and with the prohibition; they differ in what counts as a "preference parameter", and the difference is welfare-decisive rather than cosmetic.

**RUM-A — certified preference block only.** Free set = exactly the singles coordinates of `u_i` in the certified specification. `ḡ = ĝ^{AB}` in full, including its hours and employment-margin factors. The operand is then *identical* to the ratified grand-opportunity coalition `{A,B}`, so the difference between `I^RUM-A(Ωᵏ)` and `I({A,B})` isolates one thing exactly: **the re-estimation channel** — how much the preference estimates themselves absorb when opportunities are omitted. That is the paper's question in its purest form and it is unavailable under any other design.

**RUM-B — conventional preference block.** Free set = RUM-A's set **plus** a fixed-cost-of-work constant and hours-band constants, both entering `u_i` (not `ḡ`), which is where the conventional literature puts them: the ACW taxonomy's job dummy `d₀` and hours-peak dummies `d₁, d₂`. To avoid an arbitrary and unidentified split between a frozen `ḡ` shape and a collinear free constant, RUM-B's `ḡ` drops the corresponding factors and uses their proper uniform counterparts on those coordinates (§2.3). RUM-B is therefore the *recognised* conventional benchmark specification, estimated on the same sample and the same job-package support.

**Why the choice is welfare-decisive and not a fit question.** In RUM-B the employment and hours constants sit inside `u_i`, and `u_i` is what the money-metric inversion evaluates on the reference side. Moving a constant from `ḡ` into `u` therefore changes the welfare number even when it leaves the fitted index unchanged. **The conventional analyst's welfare object treats institutional hours bunching and the fixed cost of work as tastes and does not compensate them.** That is not an artefact of our design; it is the substance of the misclassification the paper is about, and RUM-B is the specification in which it is visible.

**Recommendation.** Adopt **RUM-B as the manuscript's headline benchmark** and **RUM-A as the required companion**, run and reported together. Grounds: (i) ACW establishes that the conventional model carrying both job and peaks dummies is the recognised specification, and a benchmark denied those two constants invites the objection that the comparison was rigged; (ii) RUM-B is where the misclassification appears in welfare currency; (iii) RUM-A is not redundant — it is the only object that pins the re-estimation channel against `{A,B}`, and it costs one additional estimation on an already-built engine. The pair also **brackets** the misclassification, which is a stronger reportable result than either alone.

**This is ratification item B1 and it is the most consequential unratified choice in this memo.** If Goal 1 reads the ruling as mandating RUM-A alone, that is a legitimate reading of the text; the author's position is that shipping RUM-A alone exposes the headline claim to a straightforward referee objection, and that this constitutes grounds for a deputy return under ruling §5 ("a generic package change required by Goal 1" being the nearest existing channel). No escalation is raised now; the item is placed before the Goal-1 freeze.

**One framing constraint, from ACW, that applies to both variants.** ACW's central negative finding is that in-sample fit is essentially uninformative across choice-set specifications. The RUM-versus-RURO comparison must therefore **never** be reported as a model-selection contest won on likelihood grounds. It is a *what-a-conventional-analyst-would-have-concluded* exercise. Any likelihood or fit comparison between the two models is reported as descriptive provenance only, with the ACW caveat attached.

---

## 2. The common opportunity measure `ḡ`

### 2.1 The proposed construction

**Proposal: `ḡ` is the grand-opportunity-coalition object `ĝ^{AB}`, normalised to a `ν`-density.**

`ĝ^{AB}` is the resolved opportunity object of coalition 5 in R9 §4.1 — the composition of the ratified access operator (U12 §3) and the ratified ability operator (R9 §2), which is household-invariant by construction because every household-indexed argument in every factor of `log g` has been replaced by a frozen reference:

```
log ĝ^{AB}(j)  =  log g^E( work_j ; region̄, ḡsur, ē )
                + work_j · [  log p̄̄(loc4_j)
                            + log g^H(h_j)
                            + log φ_LN( w_j | μ̄(loc4_j), σ̂ )  ]
μ̄(loc)         =  X̄ b̂ + δ̂_occ[loc],      X̄ = ( ē, p̄ₑₓₚ, p̄ₑₓₚ² )
```

Every reference on the right is already ratified: `region̄` and `ḡsur` by U12 §3.2 and R4; `ē, p̄ₑₓₚ, p̄ₑₓₚ²` by R9 §2.2 under the index-mean convention (S1); `p̄̄(loc4)` as the dwt marginal of the frozen joint `Π` in R9 §2.5. Every coefficient is the accepted corrected-baseline `θ̂ᵒᵖᵖ`. **Zero new machinery, zero new reference decisions, no re-estimation of any opportunity coefficient, and no new job package** — so U12's V4 conclusion transfers and the EUROMOD reference-coverage gate is not re-triggered.

### 2.2 Normalisation — a required correction to the mandate's characterisation

The commissioning text describes candidate (a) as "already household-invariant by construction, normalised". **The first half is correct; the second is not, and recording this is the point of the M08E lesson.** As the ratified operators define it, `ĝ^{AB}` is a product of heterogeneous objects: `g^E` and `g^H` are `exp` of linear indices, i.e. **positive kernels**; `p̄̄(loc4)` is a genuine pmf; `φ_LN(· | μ̄, σ̂)` is a genuine density in `w`. Their product is a positive kernel on `J`, not a `ν`-density. Treating an unnormalised kernel as a density is exactly the defect that spawned M08E.

**Required step, with the constant available in closed form.** Because the wage factor integrates to one in `w` for every `loc4` and the occupation factor sums to one, the normalising constant reduces to a two-term expression whose hours integral is a finite sum over the certified bands:

```
Z^ḡ  =  ∫_J ĝ^{AB} dν
     =  g^E(⊥)  +  g^E(work) · [ Σ_b  width_b · exp( band-index_b ) ]
ḡ(j) =  ĝ^{AB}(j) / Z^ḡ
```

with the band partition read from the certified hours basis (the omitted reference band carries index zero). The construction is exact, closed-form, and requires no quadrature. **No numeric evaluation is performed in this memo**; the closed form is stated so that Stage A implements arithmetic rather than approximation, and so that N1 is an exact assertion rather than a tolerance-limited one.

**Three consequences that must travel with the freeze.**

1. **Estimation-invariant, welfare-decisive.** By §1.3(i), `Z^ḡ` does not affect `θ̂^pref,RUM` at all. It *does* affect `V̄_i = log Σ_j exp(u_i + log ḡ − log q̃)`, which shifts by `−log Z^ḡ` for every household. Because the money-metric inversion runs through a Box-Cox utility in consumption, a common shift in the attained index does **not** cancel against a frozen reference side (U12 V2 holds the references fixed) and does **not** translate into a common shift in money units. It changes welfare levels non-uniformly and therefore changes measured inequality.
2. **The same convention must apply to the RURO side.** If the household-specific `ĝ_i` is normalised per household, each household's index shifts by `−log Z^ḡ_i`, and that shift **varies across households** — it is a first-order welfare object, not a bookkeeping constant. RUM-versus-RURO differences computed under mismatched conventions would be partly a normalisation artefact. Asserted by **N1b**.
3. **The convention is a frozen, disclosed choice.** It is recorded in the resolved config and in the manuscript's methods, in the same paragraph as the corrected marginal proposal convention, because the two are the same class of error caught twice.

### 2.3 The RUM-B variant of `ḡ`

If B1 is ratified toward RUM-B, `ḡ^B` is derived from the same construction by replacing the two factors whose content moves into `u_i` with their proper uniform counterparts on the same coordinates:

- **hours:** the uniform density on `[H_MIN, H_MAX]` in place of `g^H` (proper: the support is bounded);
- **employment margin:** the uniform two-point measure on `{⊥, work}` in place of `g^E`;
- **unchanged:** `p̄̄(loc4)` and `φ_LN(· | μ̄, σ̂)`.

`ḡ^B` is normalised by the same closed form with the substituted factors. It remains one frozen common density built from accepted objects; it is a derived member of the same family, not a second construction. Its identified content is exactly `φ̄(w)` of §1.3(iii), which is the honest description of what a conventional benchmark on this job space can represent: *everyone faces the same offered-wage distribution and the same job market; hours bunching and the cost of working are tastes.*

### 2.4 Assessment against the four ratified criteria

| Criterion | `ĝ^{AB}` normalised (proposed) |
|---|---|
| **Normalisation exactness** | Achieved by the closed form of §2.2 — but **only after** the added step. Recorded as a correction, not a claim. |
| **Constructibility from accepted objects** | Complete. Every reference and every coefficient is already ratified or certified; nothing new is estimated, drawn, or invented. |
| **Comparability with the RURO decomposition's opportunity concept** | Exact under RUM-A: the operand *is* coalition `{A,B}`, so the RUM/coalition gap isolates re-estimation with no operand difference. Partial under RUM-B, by design and with the difference named. |
| **No selection contamination** | Satisfied. Built from accepted parametric factors and the accepted dwt covariate distribution, never from the empirical distribution of realised job choices (U12 §6.4). |

### 2.5 Rejected alternatives

**(b) dwt-weighted mean of the household-specific normalised densities, `ḡ = Σ_i dwt_i · ĝ_i` — rejected.** It earns credit on one criterion: a convex combination of densities *is* a density, so normalisation is automatic. It fails on three. (i) **Family membership** — a mixture of members of the accepted parametric family is not generally a member, so `ḡ` could not be described in the paper as the offer environment of any reference worker, and "constructible from accepted objects" degrades to "computable from them" (U12 §6.1(ii)). (ii) **No fixed point** — no household sits at the mixture, so the idempotence check N5b has no test case and becomes an assertion. (iii) **Comparability destroyed** — the mixture is not the `{A,B}` operand, so the RUM-versus-coalition gap would confound the re-estimation channel with an operand difference, which is the one comparison this design exists to make clean. Additionally, a mixture cannot be described cell-by-cell under D1, so the manuscript could not state which bookkeeping cells the benchmark equalises.

**(c) a reference-arguments evaluation chosen fresh for the RUM — rejected as redundant or worse.** If the reference arguments are the ratified ones, this *is* proposal (a) and is not a distinct alternative. If they are any other arguments, the project acquires a **second, unratified reference for one concept**, which is the double-interpretation failure U12 §1.2(a) and §6.2 exist to prevent; and if the fresh reference is a *named cell* it reintroduces U12 §6.3's best-cell contamination — the omitted region in the certified specification is the most favourable environment, so anchoring there converts the benchmark into a distance-to-best construct rather than a common environment.

**(d) `g ≡ 1` (the literal "no opportunity structure" model) — rejected, and not merely by ruling.** See §6, finding **F1**: on the accepted job space this object has **no population estimand**. It is recorded here because it is the alternative a reader will assume was the natural benchmark.

**(e) the pooled empirical distribution of realised jobs — rejected**, on U12 §6.4's grounds unchanged: realised jobs are choices, not offers, so the object is selection-contaminated and would silently re-import preferences into the benchmark's opportunity measure.

---

## 3. Estimation plan

**3.1 Inputs, held identical and hash-asserted.** The corrected M08E draw geometry parquet (sha256 asserted against the accepted meta), its `log_prior` / `prior` columns, the `c_ij` matrix, the sample (France 2016 singles P2a region-live, 1,555 household clusters, 101 rows per household). No re-draw, no re-pricing, **no EUROMOD execution**.

**3.2 The correction, applied identically.** `−log q̃` subtracted once from every alternative including the chosen row's exact `0.0`; the marginal `q_H`; the `log(π0)` atom on simulated non-employment rows; the `log_prior` identity re-verified on the RUM's engine-ready input to the certified tolerance. No second subtraction anywhere downstream (spec contract §11).

**3.3 The index.** `V_i^RUM(j) = u_i(c_ij, ℓ_ij; θ^pref) + log ḡ(j) − log q̃_i(j)`, with `log ḡ` supplied as a **precomputed per-row column** derived from the row's job coordinates alone (which is what makes N2 a real test rather than a code review).

**3.4 Free set, fixed set, pins, bounds.** Per §1.6 under the ratified reading of B1. Bounds and the admissible region identical to the certified ones; the numerical safeguards of spec contract §12 unchanged (`C, L > 0`; row-wise max-stabilised log-sum-exp; Box-Cox exactness screen at the estimated exponents).

**3.5 Multi-start and convergence.** The **amended four-leg convergence standard including minimal-observed-point selection**, as applied at E3 v2, applies **verbatim**; the leg definitions, tolerances and attempt-directory classification convention bind at Stage A against the E3 v2 execution contract and `FR_P2a_m08e_E3_reestimation_note_v2.md`. Two RUM-specific additions, pre-registered:

- **The accepted optimum must be attained from at least one start not derived from `θ̂^RURO`.** Including `θ̂^pref,RURO` among the starts is permitted and useful; permitting it to be the *only* start would reintroduce the ruling's prohibition through the back door of a lazy local optimum.
- **All attempt directories are reported with their actual classifications** — the R5 discipline from ruling §1, applied prospectively rather than as a correction.

**3.6 Inference.** Certified Phase-4/5 conventions: curvature/eigenvalue screen on the free set; household-clustered sandwich covariance over the 1,555 clusters; conditional covariance excluding any bound-active coordinate with literal `NA`; the W-4 near-boundary diagnostic re-run on the RUM vector and reported. **The certified covariance shapes do not transfer** — the RUM's free set is smaller and its information matrix is rebuilt from scratch.

**3.7 S-10.** Proposed: **not required for the RUM vector.** The corrected S-10 coordinate set (ruling §4) is defined against the corrected RURO baseline and its five Tier-1 scenarios are a sensitivity on the *paper's preferred model*, not on a benchmark. The W-4 diagnostic **is** required, so any RUM-side boundary exposure is disclosed rather than assumed absent. Ratification item **B2**.

**3.8 Sequencing.** Execution occurs only after the final R1/R5 ACCEPT (ruling §1) and after the Goal-1 freeze of this memo. Until both, this document is design only.

---

## 4. The welfare side

### 4.1 How `W¹–W⁶` evaluate under the RUM

Per the mandate: **common `ḡ` in the attained core; references unchanged.** The attained core becomes

```
V̄_i  =  log Σ_{j ∈ C_i} exp( u_i(c_ij, ℓ_ij; θ̂^pref,RUM) + log ḡ(j) − log π(j; x_i) )
```

and every measure's reference construction — the own-set baseline for `W³`, the frozen `Ā` for `W⁵`, the staying-home job `o` for `W⁴`, the all-jobs set `J` for `W⁶` — is **hash-identical** to the RURO welfare run (the U12 V2 discipline, extended across models rather than across coalitions). The `c_ij` matrix is likewise hash-identical: the RUM changes availability, never the budget.

**A named consequence, and it is not small.** In the theory family, the measures differ in part by how they treat the individual's own ability set `A`: `W¹`, `W²`, `W³` are `A`-dependent; `W⁴`, `W⁵`, `W⁶` satisfy Independence of `A`. (Cited definitionally only; no axiom, proof, or theory-paper material is imported into the JMP.) Under the RUM every household's opportunity *weights* are common, so the `A`-argument is common up to the node support — the households' drawn `(loc4, h, w)` nodes still differ, because the draws came from the individualised proposal `π`. Therefore:

- **Any between-measure difference arising purely from `A`-dependence collapses under the RUM**, to within simulation error. Differences arising from dependence on the pay schedule `y` and on preferences `R` survive intact, because `c_ij` and `θ^pref` remain household-specific.
- **The `W¹–W⁶` spread under the RUM is therefore a different object from the spread under RURO** and must be reported with that statement attached. Reporting "the RUM shows a narrower normative spread" without it would be a category error: part of the narrowing is mechanical.
- **The residual `A`-driven spread is a usable diagnostic.** It is generated by node-support heterogeneity alone and is exactly the quantity R9 §4.4 identifies as the obstacle to an exact grand-coalition degeneracy test. It therefore gives an **empirical read on the V20b simulation tolerance** at no additional cost — a free cross-check that should be harvested.

### 4.2 What "RUM welfare inequality" means

`I(Ωᵏ,RUM)` is the money-metric welfare inequality a conventional analyst would report having fitted the recognised benchmark on this sample. Its cross-household variation comes from exactly three sources: the preference block (covariates and the sex-specific coefficients), the budget mapping `c_ij` (the endowment/needs content R9 §4.4 flags as unassigned in the three-channel game), and simulation error. **Opportunity heterogeneity contributes zero by construction** — that is the definition of the benchmark, not a finding.

Three level-comparability requirements follow, and all three are gates rather than notes: identical normalisation convention on both models' opportunity objects (§2.2, N1b); identical frozen references and `c_ij` (N9); identical weighting (`dwt = db090` for all population-facing statistics, with unweighted household counts reported alongside, per ruling §2).

### 4.3 The comparison the ruling requires

Reported as one table plus one transition matrix, all dwt-weighted:

1. **Observed disposable-income inequality** — labelled `OBSERVED DISPOSABLE-INCOME INEQUALITY — DESCRIPTIVE BENCHMARK` (ruling §2, verbatim). Never described as welfare inequality without opportunities.
2. **Common-opportunity RUM welfare inequality** — `I(Ωᵏ,RUM)` for the reported `k`.
3. **Corrected RURO welfare inequality** — `I(Ωᵏ,RURO)` at the accepted corrected baseline.
4. **`W¹–W⁶` measure spread**, both models, with the §4.1 caveat attached to the RUM column.
5. **Welfare rank correlation** between `Ω^RUM` and `Ω^RURO` over the same households, per measure.
6. **Welfare-decile movements** — the decile transition matrix, plus the share of households moving at least one and at least two deciles.
7. **The corrected RURO access/ability/preference decomposition** — reported alongside, with §1.3(iv)'s statement that the RUM offers no counterpart to the nested split.
8. **The re-estimation channel** — `I(Ωᵏ,RUM-A)` against `I({A,B})` at the RURO `θ̂`, reported as a **named diagnostic and never as a Shapley component**. Under RUM-A the operand is identical, so the gap is attributable to re-estimation alone. Ratification item **B4**.

**Pre-registered priority among these metrics.** A persistent direct-versus-IS disagreement on the welfare integration remains open on the M08 axis, and the working hypothesis is that it reflects a normalisation constant rather than a tail defect. If it is unresolved at execution: **ordinal metrics (5, 6) are primary and level metrics (2, 3, 4, 8) are conditional**, because a common normalisation offset is rank-preserving within a model but not level-preserving across models. This priority is frozen now, before any welfare number exists (charter §5.7). If the disagreement is instead diagnosed as a tail defect, the level metrics are blocked pending its resolution and the ESS escalation of N10 applies.

---

## 5. What is frozen, what binds at Stage A, and the validation set

### 5.1 Frozen by the Goal-1 freeze of this memo

The estimand equations of §1.1–§1.2; the corrected marginal correction applied identically with a byte-identical geometry; `ḡ = ĝ^{AB}` normalised, with the closed form of §2.2; the resolved reading of B1 and the corresponding free set; the four rejected alternatives with their grounds; the estimation and inference standards of §3; the reference-invariance and `c_ij`-invariance requirements of §4.1; the comparison metric list and the pre-registered metric priority of §4.3; the directional predictions of §1.5; the validation set of §5.2.

### 5.2 Validation checks (N-series), to be frozen verbatim in the Stage-A contract

| # | Check | Assertion | On failure |
|---|---|---|---|
| **N1** | **Normalisation** | `∫_J ḡ dν = 1` via the closed form of §2.2, to a tolerance declared at Stage A. | Gate. This is the M08E defect's tripwire. |
| **N1b** | **Convention parity** | The household-specific RURO opportunity object is normalised under the *same* convention as `ḡ`; the per-household constants are recorded. | Gate. Otherwise the model comparison is partly an artefact. |
| **N2** | **Household invariance** | `log ḡ` recomputed from each row's `(work, loc4, h, w)` alone reproduces the stored column bitwise; the column has zero variance conditional on the job coordinates. | Gate. Direct test that no `x_i` leaked into the benchmark. |
| **N3** | **π-invariance** | Geometry sha256 and the `prior` / `log_prior` columns byte-identical to the accepted corrected M08E geometry. | Gate (mirrors U12 V3). |
| **N4** | **No new package** | Row count, alternative support and the `c_ij` hash unchanged; no EUROMOD call in the run manifest. | Gate (mirrors U12 V4). |
| **N5** | **Operand identity** | Under RUM-A, `log ḡ + log Z^ḡ` is bitwise identical to the resolved `{A,B}` opportunity object. | Gate. This is what licenses the §4.3(8) diagnostic. |
| **N5b** | **Fixed point** | For a synthetic row set whose access- and ability-assigned arguments equal the ratified references, the household-specific RURO object equals `ḡ` bitwise (up to the recorded constant). | Gate (the U12 V1 analogue). |
| **N6** | **Constant-invariance** | Adding an arbitrary constant to `log ḡ` leaves the negLL and `θ̂` unchanged. | Gate. Verifies the offset is applied to *all* rows including the chosen one; a failure means the chosen row was skipped. |
| **N7** | **Free-set integrity** | The free coordinate list matches the ratified B1 reading exactly; no opportunity coefficient is free; the pinned couples coordinates enter no singles row's `u_i`. | Gate; halt if a pinned coordinate enters (R9 §3.3). |
| **N8** | **Convergence and rank** | Full rank of the observed information on the free set; single-optimum determination under the four-leg standard; the non-RURO-derived start reaches the accepted optimum; bound activity reported. | Report and halt per the E3 standard. |
| **N9** | **Welfare comparability** | Reference constructions (own-set, `Ā`, `J`, `o`) and `c_ij` hash-identical between the RUM and RURO welfare runs. | Gate. |
| **N10** | **Counterfactual ESS** | Re-run the ESS / max-normalised-weight diagnostic for the RUM welfare integration. The RUM changes the IS *target* while `π` is unchanged, so the RURO baseline ESS does **not** transfer. | Apply the frozen escalation rule to the RUM target. If the flagged set widens materially and the direct redraw estimator remains blocked, **halt** (ruling §5). |

### 5.3 Bound at Stage A, not here

Exact coordinate and column strings for every object in §1.4 and §2.1; the numeric values of the ratified references; the evaluated normalising constant; the four legs and their tolerances; N1's declared tolerance and the bitwise scope of N2/N5; output paths under the M08 workspace; the resolved-config provenance block.

### 5.4 LOC4 forward statement (pre-registered so LOC4 cannot reopen this design)

Under the LOC4 four-density variant, the benchmark changes **only** through the common marginal offered-wage density `φ̄(w)` of §1.3(iii): a four-density wage block changes `μ̄(loc)` and possibly makes `σ` occupation-specific, both of which enter `ḡ` and nothing else. `p̄̄(loc4)` is re-derived from the same frozen joint `Π`. No part of §1, §3 or §4 requires amendment. The boundary restatement of R9 §2.3 carries over verbatim: occupation *availability* is access, occupation-specific wage mean and dispersion are ability, and only one of mean and dispersion may carry a given occupation effect.

### 5.5 Open items for the Goal-1 freeze

| # | Item | Author's recommendation |
|---|---|---|
| **B1** | RUM-A vs RUM-B as the headline benchmark (§1.6) | **RUM-B headline, RUM-A required companion.** Most consequential item; candidate escalation if declined. |
| **B2** | Whether S-10 applies to the RUM vector (§3.7) | No; W-4 diagnostic required and reported. |
| **B3** | Which measures headline the RUM column given the `A`-collapse (§4.1) | Report all six; attach the collapse caveat to the RUM column; headline an `A`-independent measure to avoid the mechanical narrowing. |
| **B4** | Whether the RUM-A/`{A,B}` gap is reported as the "re-estimation channel" (§4.3(8)) | Yes, as a named diagnostic; never as a Shapley component. |
| **B5** | Tolerances for N1, and the bitwise scope of N2/N5 | Bitwise where the object is deterministic arithmetic on stored columns; declared tolerance only for N1. |
| **B6** | Disposition if the RUM fails the four-leg standard or lands on an economically implausible `θ̂` | Pre-registered: **report as a finding.** Do not re-specify to obtain convergence or plausibility without a deputy ruling — that would be a post-hoc specification search on the benchmark side. |
| **B7** | Whether the manuscript's main question is re-worded per finding F1 (§6) | Yes; routed as a rider to M07I rather than handled here. |

---

## 6. Coherence check

**Verdict: the proposed estimand is scientifically well-defined**, conditional on the normalisation step of §2.2 being executed as specified. Without it the object is a positive kernel and the M08E defect recurs one layer up. No incoherence in the proposed estimand was found, and no deputy-return condition under ruling §5 is triggered by this memo. Four findings are recorded rather than designed around.

**F1 — `g ≡ 1` has no population estimand on the accepted job space.** Under `g ≡ 1`, `Z_i = ∫_J exp(u_i(c_ij, ℓ_ij)) dν`. The wage coordinate is unbounded, and disposable income is increasing in `w`; for any admissible consumption Box-Cox exponent, `exp(u_i)` is bounded away from zero as `w → ∞` — increasing without bound for a positive exponent, converging to a positive constant for a negative one. **The `w`-integral diverges in either case.** The "no opportunity structure" model is therefore not merely disallowed by the ruling; it does not exist as a population object on `J`. What makes this dangerous rather than academic is that the *sampled* likelihood remains perfectly finite, because `q̃` has integrable tails: the computation returns numbers that converge to nothing. This is the same failure mode as the joint/marginal convention defect and as the unnormalised-kernel defect — a well-behaved computation on an ill-defined estimand — and it is now the third instance. Two consequences: (i) the ruling's prohibition has an independent mathematical foundation and should be stated with it in the manuscript; (ii) the paper's main question must be operationalised as *"when opportunity **heterogeneity** is omitted"*, not *"when opportunities are omitted"*, because on this job space opportunities cannot be omitted — only made common. Routed to M07I as item B7.

**F2 — the `A`-argument collapse changes what the `W¹–W⁶` spread measures under the RUM** (§4.1). Not an incoherence; a caveat that must be attached to a metric the ruling requires, and a free diagnostic for the V20b tolerance.

**F3 — the benchmark inherits the open direct-versus-IS disagreement.** The RUM changes the IS target while leaving `π` unchanged, so the counterfactual-ESS exposure of U12 V6 applies to it as it does to the coalitions (N10). If the disagreement is a normalisation constant, the ordinal comparison metrics are robust and the level metrics are not; the metric priority of §4.3 is pre-registered on that basis. If it is a tail defect, level metrics are blocked, not adjusted.

**F4 — RUM-A is a weaker-than-conventional benchmark, and the author says so before the results exist.** Denying the benchmark the fixed-cost and hours-peak constants that the conventional literature always fits biases the comparison toward "opportunities matter". The mitigation is B1's companion, not a caveat sentence. This is recorded as a named risk so that it cannot later be presented as a discovery by a referee.

---

## 7. Output discipline

- **Mission ID:** JMP-M08, deputy ruling `JMP_M08E_E2_closure_notebook_and_RUM_ruling_v1.md` §3. Register item proposed as `RUM-BENCH`, number to be assigned.
- **Authoritative inputs:** as listed in the header block (E2 ruling; E0 estimand audit; U12 access operand memo; R9 ability/preference operators memo; RURO spec contract v2; ACW 2009 project literature note, taxonomy only).
- **Decisions made (all PROPOSED, none frozen):** the RUM estimand of §1.1–§1.2; `ḡ = ĝ^{AB}` normalised, with the closed-form constant of §2.2; the identification statements of §1.3, including the near-inertness of occupation availability and the absence of any access/ability counterpart; the no-RUM-counterpart table of §1.4; the three pre-registered directional predictions of §1.5; the RUM-A/RUM-B pair with RUM-B recommended as headline; four rejected `ḡ` constructions with grounds; the estimation and inference plan of §3, including the non-RURO-derived-start requirement; the welfare treatment and metric priority of §4; the N1–N10 validation set; the LOC4 forward statement.
- **Unresolved decisions:** B1–B7 (§5.5), of which **B1 is blocking** for the free-set specification and therefore for the Stage-A contract.
- **Exact output filename:** `docs/Missions/JMP_M08_RUM_benchmark_estimand_design_v1.md`
- **Next authorised action:** Goal 1 Manager review and freeze of this memo (with B1–B7 resolved), followed by the Stage-A binding of §5.3. **RUM estimation remains unauthorised until the final R1/R5 ACCEPT** (ruling §1) and the Goal-1 freeze are both in place. No deputy return is requested.