# JMP-M08 — Ability and Preference Equalisation Operators Design (register item R9)

**Mission:** JMP-M08 — France 2016 Singles Welfare Integration and Baseline Decomposition Prototype
**Register item:** R9 — ability operator (`B`) and preference operator (`P`); mirrors of U12
**Document class:** design memo (economics + operator specification). No computation, no code, no welfare number, no re-estimation.
**Status:** **PROPOSED — PENDING RATIFICATION** by the Goal 1 Manager. Nothing here is frozen; Stage A (charter §6) is the freezing instrument.
**Target repository path:** `docs/Missions/JMP_M08_ability_preference_operators_design_v1.md`
**Author role:** M08 design author (advisory)

**Authoritative inputs**

1. **Goal-1 ruling R-71** (adopted as binding): D1–D10 ratified; D1 as scaffold §7 amendment with the cell table transcribed verbatim; R2/R3 ratified; R4 = share-weighted **index** baseline, share-weighted probability the single sensitivity, median-region rejected; R5 = `ω_s` are within-`educ3` dwt population sex shares; R6 = **all** operand population references dwt-weighted (`dwt = db090`), unweighted variant not run in M08; R7 = V1–V13 ratified with the stated tolerances, `V_i^dir` **unblocked** and mandatory at Stage D on flagged subsets under the frozen 0.5-nat tolerance; R8 = verify-then-escalate at Stage A; R10/R11 as proposed.
2. `JMP_M08_access_equalisation_operand_design_v1.md` (U12, as ratified by R-71) — the mirror this memo must be consistent with.
3. `JMP_M08_singles_welfare_decomposition_mission_charter_v1.md` (§4.1–4.3, §5, §6, §7 Stage F/G, §9, §10, §11).
4. `JMP_M08_welfare_input_handoff_v1.md` (§1, §2.1–2.6).
5. `RURO_welfare_scaffold_design_contract_v2.md` (anchors; §2; §3.1–3.4; §4; §6; §7; §9).
6. `RURO_welfare_gate_report_W3_v1.md` (Preflight 2; Gate 1(ii); Gate 2; decomposition-readiness).
7. Normative bookkeeping rules (access-purity; gender-in-offers vs gender-in-tastes; age split).

**Not used as data:** management memos (handoff §1; charter §2).

---

## 1. What both operators are

Under D1 (ratified), the decomposition unit is the **(factor × argument) cell**. An equalisation operator is therefore not a parameter-block swap but an **argument substitution into a fixed function evaluation**: it replaces the household-specific arguments occupying its assigned cells by frozen reference values, and evaluates the *accepted* functional form at the accepted `θ̂` (handoff §1; charter §5.3, §10). Nothing is re-estimated, and no coefficient is re-fitted.

Both operators act inside the attained-utility core only, as `g_ref` does (U12 §1.1):

```
V_i = log Σ_{j∈C_i} exp( u_i(c_ij, ℓ_ij; θ^pref) + log g(j; x_i, θ^opp) − log π(j; x_i) )
log g = log g^E(·; x_i) + work_j · [ log g^Occ(loc4_j | x_i) + log g^H(h_j) + log g^W(w_j | loc4_j; x_i) ]
```

Every measure's reference (own-set baseline for `W^3`, `Ā`, `J`, `o`) and the `c_ij` matrix stay frozen across all coalitions (U12 V2, ratified). `π` is never touched by any operator (U12 V3, ratified). No operator introduces a job package, so the reference-coverage / EUROMOD gate is never re-triggered (U12 V4, ratified; contract §6.1(iii)).

---

## 2. The ability operator `B`

### 2.1 Assigned cells (from the ratified D1 table)

| Cell | Argument(s) `B` substitutes |
|---|---|
| `g^W`: Mincer location `μ_i = X_i b + δ_occ[loc4_j]` | `educ` dummies, `pexp`, `pexp²` |
| `g^W`: `σ` | none available — degenerate (§2.3) |
| `g^W`: `δ_occ[loc4_j]` | none — coefficients, not arguments (§2.4) |
| `g^E`: education-interacted cells (GSUR×educ, and any `educ`-interacted market/hours term) | `educ` argument slot only |
| `g^Occ`: the `educ3` conditioning argument | `educ3` |

### 2.2 Reference objects, precisely

All references are **dwt-weighted** over the accepted P2a singles sample, `dwt = db090` (R6). All are frozen and recorded before execution (handoff §2.1). Exact column names are bound at Stage A against the frozen spec YAML and the accepted engine-ready parquet; the memo states the object, not a guessed column string (charter §6; contract §9).

| Reference object | Definition | Source |
|---|---|---|
| `ē` — education | the dwt-weighted **share vector** over the education dummies (`educL`, `educH`; `educM` omitted), substituted for the household's dummy vector | accepted education dummy columns on the engine-ready singles parquet; weights `db090` |
| `p̄ₑₓₚ` — experience level | dwt-weighted mean of `pexp` | accepted `pexp` column |
| `p̄ₑₓₚ²` — experience square | dwt-weighted mean of `pexp²` (**not** `(p̄ₑₓₚ)²`) | accepted `pexp2` column (or the accepted squared construction, bound at Stage A) |
| `p̃(loc4 \| dgn)` — education-pooled occupation availability | the `educ3`-marginal of the frozen joint table (§2.5) | accepted `p(loc4 \| dgn, educ3)` × dwt joint distribution of `(dgn, educ3)` |

**Why `E[pexp²]` and not `(E[pexp])²`.** R4 ratified the **share-weighted index** as the baseline convention for the region cell: the reference is the population mean of the *linear index*, not the index at a synthetic mean worker. Substituting `E[pexp]` and `E[pexp²]` separately is the exact analogue — it makes the reference Mincer location equal the dwt-weighted mean of the accepted experience index. Substituting `(E[pexp])²` would evaluate the index at a mean worker and discard the second-moment content of the experience profile, i.e. it is the *probability/level* analogue that R4 designated a sensitivity rather than the baseline. Proposed accordingly: **baseline = index-mean `(E[pexp], E[pexp²])`; single sensitivity = profile-at-mean-worker `(E[pexp], (E[pexp])²)`**, mirroring R4's one-baseline-one-sensitivity pattern (ratification item **S1**).

The same logic gives the education reference: the dwt **share vector** (index-mean) is baseline; the share-weighted-probability variant is the single sensitivity (mirror of R4). Setting education to a *named level* — including `educM`, the omitted category — is rejected (§6, A4), for the reason median-region was rejected.

### 2.3 `σ`: degenerate, and what that means for the ability component

The certified specification carries **one common `σ`** across households (contract anchors; the wage block is `beta_w0, beta_w_educL, beta_w_educH, beta_w_pexp, beta_w_pexp2, sigma`, all common). There is therefore no household-specific dispersion argument to substitute, and `B`'s action on the `σ` cell is the **identity** — exactly the status of `g^H` in the access operator (U12 §3.4).

**Implication, to be stated in the manuscript rather than buried.** In M08, the ability component contains **no wage-dispersion content whatsoever**. It is a *location*-only ability channel: it measures the money-metric inequality attributable to differences in the education- and experience-driven level of the wage offer distribution (and, via §2.4, the wage consequences of own occupation availability under own vs. reference location), and it is a **lower bound** on ability inequality with respect to any heterogeneity in wage-offer dispersion the certified specification does not carry. This is the direct analogue of the access component's hours-availability lower-bound caveat (U12 §3.4), and it belongs in the same caveat block.

**LOC4 forward statement (handoff §2.3; charter §5.5, §10).** Under the four-density variant, dispersion may become occupation-specific (`σ_occ`). At that point the `σ` cell ceases to be degenerate and `σ_occ` becomes an **ability** coefficient attached to an **access**-assigned availability weight — the same structural configuration `δ_occ` already occupies (§2.4). The boundary restatement is pre-registered now so LOC4 cannot reopen the bookkeeping: occupation *availability* is access; occupation-specific wage *mean and dispersion* are ability; only one of mean and dispersion may carry a given occupation effect (Path-B ruling, no double counting).

### 2.4 `δ_occ`: untouched, and the single cell where `B` and `A` interact

`δ_occ` is a vector of **common coefficients** indexed by the drawn `loc4_j` on each row. It is not a household argument, so as an argument-substitution matter the ability operator does not touch it: `B` neither replaces `δ_occ` nor re-evaluates the row's `loc4_j`.

The economic consequence must be stated exactly, because it is the one place where the two opportunity operators interact:

- Under **`B` alone**, the household still faces its **own** (sex- and education-conditional) occupation availability, but its wage location no longer depends on its own education or experience. The wage attached to each row still depends on `loc4_j` through `δ_occ`. So `B`'s effect includes the wage consequences of the household's *own* occupation-availability composition, evaluated at the reference Mincer location.
- Under **`A` alone** (U12), the household faces the sex-pooled availability but keeps its own Mincer location, so `A`'s effect includes the wage consequences of *reweighted* availability at own location.
- The residual — the interaction between availability weights and `δ_occ` — is exactly the term neither operator can claim alone. **Shapley symmetry is what allocates it**, splitting it evenly between the access and ability marginal contributions across orderings. This is the substantive reason order-independence is not a formality in this application, and it should be said in the paper: the access/ability split of the occupation channel's wage content is an artefact of the Shapley symmetry axiom, not an identified quantity.

### 2.5 Occupation availability: `B` selects a marginal of one frozen joint table

`p(loc4 | dgn, educ3)` is a conditional table whose two conditioning arguments are assigned to different channels: `dgn` → access (U12 §3.3), `educ3` → ability (D1). The two operators must therefore act on the same object without colliding.

**Proposed construction.** Freeze one joint object,

```
Π(loc4, dgn, educ3) = π_dwt(dgn, educ3) · p̂(loc4 | dgn, educ3)
```

with `π_dwt` the dwt-weighted population distribution of `(dgn, educ3)` on the P2a singles sample and `p̂` the accepted conditional table. Each operator then **selects the appropriate conditional of `Π`**, indexed by which conditioning coordinates remain at own value:

| Coalition state | Occupation object faced |
|---|---|
| neither `A` nor `B` | `p̂(loc4 \| dgn_i, educ3_i)` — accepted baseline |
| `A` only | `p̄(loc4 \| educ3_i)` — sex-pooled within education (U12 §3.3) |
| `B` only | `p̃(loc4 \| dgn_i)` — education-pooled within sex |
| `A` and `B` | `p̄̄(loc4)` — the dwt-weighted marginal |

This formulation is **equivalent to** R5's ratified weights (`ω_s(educ3) = π_dwt(s | educ3)`) and makes composition **path-independent by construction**: applying `A` then `B` and `B` then `A` both yield `p̄̄(loc4)`, because both are conditionals of one joint object rather than sequentially re-weighted mixtures. Defining the pooling weights instead as free, step-specific mixtures would make the order matter and would break the commutation property §4.3 relies on. Checked by **V14**.

The joint uses only accepted objects: the accepted conditional table and the accepted covariate distribution under `db090`. It is **not** the empirical joint of realised occupations, which is choice- and selection-contaminated (U12 §6.4).

### 2.6 Interaction terms: shared cell, disjoint argument slots

The GSUR×education cells of `g^E` are a product of an access-assigned argument (`gsur`) and an ability-assigned argument (`educ`). Under D1 the *cell* is shared but the *argument slots* are not:

| Coalition state | GSUR×educ term evaluated at |
|---|---|
| baseline | `gsur_i × educ_i` |
| `A` only | `ḡsur × educ_i` |
| `B` only | `gsur_i × ē` |
| `A` and `B` | `ḡsur × ē` |

Each operator writes only its own slot. This is not double counting — each changes a different input — and it is why the operators commute (§4.3). Note that `ḡsur` here is the U12-ratified dwt-weighted GSUR mean, unchanged.

### 2.7 The mirror guard (verbatim)

> **The ability operator must not alter occupation-availability weights (the `dgn` argument of `g^Occ`) or any access-assigned cell.**

Enforced bitwise by **V15**.

---

## 3. The preference operator `P`

### 3.1 What is heterogeneous in `u_i`, and the necessary distinction

`u_i(c_ij, ℓ_ij; θ^pref)` carries **two** sources of cross-household heterogeneity in the singles P2a application, and the operator must treat them differently:

**(a) Covariate arguments** — the taste shifters entering the leisure term: `age_norm`, `age_norm2`, the education-in-leisure dummy (`beta_l_educH_*`), and the children term (`beta_l_nkids_sf`). These are substituted by dwt-weighted references, exactly as `A` and `B` substitute theirs. **The operator substitutes covariate arguments; it never re-estimates a coefficient** (charter §5.3, §10).

**(b) Group-specific coefficient blocks** — singles male and singles female carry separate preference blocks (`beta_c_sm/sf`, `theta_c_*`, `beta_l0_sm/sf`, `theta_l_sm/sf`, `beta_l_age_*`, `beta_l_age2_sm/sf`, `beta_l_nkids_sf`). This is **gender-in-tastes**, which the bookkeeping assigns to preference and declares non-compensable. Non-compensable means *the paper does not compensate it*; it does **not** mean the preference channel excludes it. If `P` leaves the group-specific blocks standing, gender-in-tastes survives all three operators, the grand coalition is not degenerate, and exhaustiveness fails (charter §9.8; V8's precondition).

`P` therefore has two steps: a **covariate-substitution step** (a) and a **group-block selection step** (b). Step (b) is a *selection among accepted coordinates of `θ̂`* — not an estimation, not a re-fit, and not a modification of any accepted value. It is nonetheless the single most consequential unratified choice in this memo (§7, item S2).

### 3.2 Covariate references (step a)

All dwt-weighted (`db090`), index-mean convention per R4, frozen and recorded before execution:

| Reference | Definition |
|---|---|
| `āge` | dwt-weighted mean of `age_norm` |
| `āge²` | dwt-weighted mean of `age_norm2` — **not** `(āge)²`, per the R4 index-mean convention (§2.2, S1) |
| `ēduc_leisure` | dwt-weighted share of the education-in-leisure dummy |
| `n̄kids` | dwt-weighted mean number of children |

**Age-in-leisure is equalised here**, per the age split: age enters ability via experience-in-wages (`B`, §2.2) and preference via age-in-leisure (`P`), and each channel equalises its own occurrence. Age appears in no access cell (U12 §3.5, verified at Stage A).

**Education appears in two channels, and this is not a violation of access-purity.** Access-purity governs the *opportunity side*: it forbids education from being counted as access, which is why D1 routes the education arguments of `g^E` and `g^Occ` to ability. Education-in-*leisure* is a taste shifter occupying a `u_i` cell, and D1 assigns `u_i` cells to preference. The structure is identical to the ratified age split — one variable, two cells, two channels, distinguished by the cell it occupies, never double counted because each occurrence is substituted exactly once by exactly one operator. The normative content is real and should be ratified explicitly (item **S3**): under this routing, education-correlated *taste* differences are preference-classified and therefore not compensated.

### 3.3 The pinned-preference switch: `held`, and non-binding in M08

Contract §7 exposes `decomposition_readiness.preference_equalisation_pinned_switch: held | swapped`, default `held`; R-71 ratifies `held`. Under `held`, the pinned coordinates `theta_l_m` and `beta_ll` are **kept at their pinned values under preference equalisation** rather than swapped for the reference preference. So `held` *does* constrain the preference operand: it removes those two coordinates from step (b)'s substitution map.

**But in M08 the constraint is vacuous.** `theta_l_m` is the couples-male leisure Box-Cox exponent and `beta_ll` is the household leisure interaction (`= 0`); both are couples-side objects among the 10 pins of the certified pooled 47-coordinate specification, and neither enters a singles row's `u_i`. Under charter §5.1 (singles only), `held` therefore has no numerical consequence in M08 — a degenerate switch, in the same category as `σ` (§2.3) and hours availability (U12 §3.4). Contract §7's warning that the switch "sizes the couples preference component and therefore the couples opportunity share" is a couples statement and is not imported (charter §2).

Required disposition: the flag is asserted as `held` in the resolved config for provenance, its non-binding status in M08 is recorded in the validation memo, and **Stage A must verify that neither pinned coordinate enters any singles row's `u_i` and halt if one does** (charter §6, §11).

### 3.4 Two boundary-active preference coordinates

The accepted vector carries two **active upper bounds at 1.0**: `beta_l_age2_sm` and `beta_l_age2_sf` — the age² leisure coefficients, excluded from the covariance object with literal `NA` (handoff §1; the recorded Phase-5 treatment). Two consequences:

1. Whichever group block is selected in step (b), the reference preference **contains a bound-active coefficient**. No inferential claim about the preference component may be routed through `beta_l_age2_*` without boundary-aware inference (handoff §2.2).
2. However, `P` equalises `age_norm2` in the same move. Once the age² argument is common across households, the bound-active coefficient multiplies a common value and contributes **nothing to cross-household variation** in the equalised state. So this particular exposure is largely neutralised on the coalition side — which is worth reporting, because it narrows the Tier-2 exposure of the preference component to `beta_l0_sm` (§5.3).

---

## 4. Coalition structure

### 4.1 The eight coalitions

Let `A` = access, `B` = ability, `P` = preference, and let `I(S)` be the inequality of the money-metric welfare vector `Ω^k` when the channels in `S` are equalised. Every coalition is a composition of the three operators applied to the *same* accepted core, with references frozen (U12 V2) and `π` and `c_ij` untouched.

| # | `S` | Operator composition | Role |
|---|---|---|---|
| 1 | `∅` | identity | baseline `I(Ω^k)`; the total being decomposed |
| 2 | `{A}` | `g_ref` access cells; own educ/pexp; own tastes | access-only marginal base |
| 3 | `{B}` | `ē, p̄ₑₓₚ, p̄ₑₓₚ²`; `p̃(loc4\|dgn)`; own access; own tastes | ability-only marginal base |
| 4 | `{P}` | reference taste covariates + reference group block; own `g` | preference-only marginal base |
| 5 | `{A,B}` | full opportunity equalisation; `p̄̄(loc4)`; own tastes | **headline opportunity coalition** (charter §4.3) |
| 6 | `{A,P}` | access + preference; own wage technology arguments | ability-residual coalition |
| 7 | `{B,P}` | ability + preference; own access | access-residual coalition |
| 8 | `{A,B,P}` | grand coalition | degeneracy target; V8/V20 precondition |

### 4.2 Exact Shapley weights

For `n = 3` channels, the contribution of channel `k` is

```
C_k = Σ_{S ⊆ N\{k}}  [ |S|! · (3 − |S| − 1)! / 3! ] · [ I(S) − I(S ∪ {k}) ]
```

with weights, equivalently the average over the `3! = 6` elimination orderings:

| `\|S\|` | number of such `S` | weight per term |
|---|---|---|
| 0 | 1 | `2!/3! = 1/3` |
| 1 | 2 | `1!·1!/3! = 1/6` each |
| 2 | 1 | `2!/3! = 1/3` |

Weights sum to 1 for each `k`. Telescoping across orderings gives `C_A + C_B + C_P = I(∅) − I({A,B,P})`, so **exhaustiveness holds if and only if `I({A,B,P}) = 0`** — the precondition of V8, and the reason §4.4 and §5.4 matter.

### 4.3 The operators commute on disjoint cells

**Claim.** For any `S`, `I(S)` is independent of the order in which the operators in `S` are applied.

**Justification.** Under D1 each operator substitutes values into a set of argument slots of a fixed evaluated function; the slot sets assigned to the three channels are pairwise disjoint. Substituting into disjoint slots of a function evaluation is order-independent — it is not composition of maps on a shared state, it is assembling one argument tuple. Two cells are *shared* across channels, and both are handled so that commutation survives:

- **GSUR×educ** (§2.6): a product of two slots, one per channel; each operator writes only its own slot.
- **The occupation table** (§2.5): both operators select a conditional of one frozen joint `Π`, indexed by which conditioning coordinates remain at own; the selection is path-independent by construction.

There is one asymmetry worth naming: `P`'s step (b) substitutes a *coefficient block*, not an argument. It still commutes with `A` and `B`, because `θ^pref` occupies no cell either operator touches (`A` and `B` act only inside `log g`). Asserted by **V19**.

Checked by **V14** (both orders, bitwise identical resolved objects, all coalitions).

### 4.4 Degeneracy mechanism of the grand coalition — and a bounded design conflict

Under `{A,B,P}` every household faces: the same resolved `g` (same `g^E` index, same `p̄̄(loc4)`, same `g^H`, same `g^W` location — `σ` already common), the same taste covariates, and the same `θ^pref` block. If `Ω^k` were a functional of `(u, g)` alone, degeneracy would be exact and V8 would be a pure numerical assertion.

It is not. Two sources of cross-household variation survive all three operators:

1. **The budget mapping `c_ij`.** Disposable income at each row depends on the household's own non-labour income and demographics. The RURO specification routes non-labour income into preferences via `C` as an identification anchor (`RURO_model_spec_contract_v1` §11.5), but `c_ij` is an accepted per-row EUROMOD-evaluated object. Equalising it would require either a wholesale EUROMOD re-evaluation (forbidden, contract §6.1(iii)) or an invented additive shift (forbidden, charter §6: do not invent).
2. **The node support.** The alternatives were drawn from the individualised proposal `π`, so the `(w, h, loc4)` nodes differ across households. Under the grand coalition all households share an integrand only if that integrand is household-invariant — which fails precisely because of (1). Even with (1) resolved, `V_i` would be an importance-sampling estimate of a common integral on different node sets, i.e. degenerate **only up to simulation error**.

Both bear directly on the ratified V8 tolerance. `1e-9 · max(1, |I(Ω^k)|_baseline)` is an exactness tolerance; the accepted singles ESS diagnostics (W3 gate report: median 20.3 / 18.8; 1,918/2,243 and 2,493/2,764 below 30) imply simulation error orders of magnitude above that. **V8 as ratified will fail for a mechanical reason unless it is split.** Proposed split (item **S4**), mirroring R8's verify-then-escalate posture:

- **V20a — analytic degeneracy (exact, tolerance `1e-9`):** the resolved equalised objects — the `u` coefficient block, the taste covariate vector, and every resolved `g` factor — are **hash-identical across all households** under `{A,B,P}`.
- **V20b — numerical degeneracy (declared simulation tolerance):** residual `I(Ω^k)` at the grand coalition within a tolerance derived from the counterfactual ESS diagnostic (U12 V6) and declared at Stage A, not `1e-9`.
- **V20c — enumeration (constructive, no computation):** enumerate every source of cross-household variation in `Ω^k` under the grand coalition and assign each to a channel or escalate. If `c_ij` heterogeneity remains unassigned, **halt to the deputy** (charter §11: "the welfare family cannot be implemented under the accepted theory/JMP boundary"; §9.8 exhaustiveness).

**Recommended resolution to put to the deputy:** declare a fourth **endowment/needs** channel owning the budget mapping, and read the charter's three-channel game as the **nested** decomposition inside it — preserving exhaustiveness at both levels without inventing a `c_ij` operator. This is not adopted here; it is the escalation proposal.

### 4.5 A level-of-aggregation gap the charter text does not close

Charter §4.3 makes the headline cut opportunity-vs-preference with access-vs-ability nested inside; charter §7 Stage F instructs evaluating the eight coalitions of the **three-channel** game and reporting "access-only and access-plus-ability shares". Under the three-channel game, `C_A + C_B + C_P = I` exactly, so `C_A + C_B` is a coherent exhaustive definition of opportunity content. But it is **not** equal to the opportunity value of the two-channel game `{opportunity = A∪B, preference}`:

```
C_O^(2)  =  ½[ I(∅) − I({A,B}) ] + ½[ I({P}) − I({A,B,P}) ]     ≠     C_A + C_B   in general
```

The two differ in how the three-way `A–B–P` interaction is allocated. Proposed disposition (item **S5**): adopt the charter's three-channel game as primary, **define** opportunity content ≡ `C_A + C_B`, and report `C_O^(2)` and the gap `|C_A + C_B − C_O^(2)|` as a pre-registered diagnostic (**V21**), described as a level-of-aggregation gap and not as an error. Pre-registering the definition before results exist is required by charter §5.7.

---

## 5. S-10 interaction (handoff §2.1; charter §7 Stage G)

The four scenarios are: (1) baseline; (2) `beta_l0_sm` perturbed; (3) `beta_w_pexp2` perturbed; (4) both. U12 §8.1 established that `g_ref` is *numerically* invariant across all four because no access-assigned coefficient is perturbed. **The mirrors are not in that position, and the statement must be split precisely.**

### 5.1 Invariant, and hash-asserted

The **operand arguments** are functions of the data and `db090` only, never of `θ`:

`ē`, `p̄ₑₓₚ`, `p̄ₑₓₚ²`, `āge`, `āge²`, `ēduc_leisure`, `n̄kids`; the dwt joint `π_dwt(dgn, educ3)`; the derived occupation objects `p̄(loc4|educ3)`, `p̃(loc4|dgn)`, `p̄̄(loc4)`; the D1 cell routing; the coalition enumeration and Shapley weights; the substitution map of `P`'s step (b) (which coordinates are replaced by which, as a *map*, not as values); `π`; `c_ij`; the alternative support; every measure reference.

All hash-asserted identical across the four scenarios, and recorded before execution.

### 5.2 Legitimately varying, and not hash-asserted

`beta_w_pexp2` **is an ability-channel coefficient**. The ability operator's reference index — the equalised Mincer location `μ̄ = b·x̄ + δ_occ[loc4_j]` — is evaluated at the scenario's `θ`, so `μ̄` differs in scenarios 3 and 4. Likewise, if `P`'s reference group block is singles-male, the equalised `θ̄^pref` differs in scenarios 2 and 4 because `beta_l0_sm` is perturbed. Consequently the **equalised values**, every `I(S)`, and every Shapley component vary across scenarios. This is the sensitivity the exercise exists to measure; it must be reported in full, including sub-threshold continuous changes (charter §7 Stage G), and must **not** be suppressed by an invariance assertion.

The compact statement for the contract: *arguments are scenario-invariant and hash-asserted; equalised values are scenario-dependent by construction and reported.*

### 5.3 A design hazard the reference-group choice creates

If the singles-**female** block is selected as `θ̄^pref`, then `θ̄^pref` is invariant to scenario 2's perturbation of `beta_l0_sm` (and `beta_l0_sf` is a vigilance coordinate, not perturbed — handoff §2.5). The reference-group choice therefore **changes the S-10 exposure of the preference component**, and a choice made after seeing scenario results could suppress the very sensitivity S-10 is designed to reveal. Two consequences, both pre-registered:

1. The reference-group choice is frozen at Stage A, before any coalition value is computed (charter §5.7, §6).
2. Both directions are reported (§7, item S2: baseline group + the mirror as the single sensitivity), so the exposure is visible either way.

### 5.4 Material loading and the Tier-2 trigger (handoff §2.2)

U12 §8.1 flagged that the access component loads on both flagged coordinates through coalition values. For the mirrors the position is stronger and should be stated plainly now:

- The **ability** component loads on `beta_w_pexp2` **by construction** — the flagged coordinate is a coefficient of the ability operator's own reference index.
- The **preference** component loads on `beta_l0_sm` by construction if the male block is the reference, and through coalition values in any case.

Handoff §2.2 makes boundary-aware or resampling inference mandatory if "any welfare or decomposition functional loads materially on one" of the flagged coordinates. The first-gate material-loading assessment should therefore be **expected to return positive for at least one component**, and Tier-2 should be scheduled as the anticipated path rather than treated as an exception. Materiality remains a numerical question answered at the first gate, not asserted here. `beta_l0_sf` is monitored throughout with no bound asserted absent an accepted record (handoff §2.5). The two W-4 coordinates remain visible in every ability- and preference-component table and caveat block (handoff §2.4).

---

## 6. Rejected alternatives

### Ability operator

**A1 — Equalise `σ` by importing a dispersion reference from outside the accepted artifacts** (e.g. an occupation-specific dispersion anticipated from the LOC4 design). Fails twice: it requires an object not in the accepted inputs (handoff §1; charter §5.3, §10), and it pre-empts the Path-B ordering that makes LOC4 the first robustness axis rather than an M08 component (handoff §2.3; charter §5.5).

**A2 — Equalise ability by replacing the per-row wage `w_j`** (substituting a common wage grid or a reference wage). Fails on three counts: (i) it alters the alternative support and therefore `c_ij`, re-triggering the reference-coverage / EUROMOD gate and reprice parity (U12 V4; contract §6.1(iii); charter Stage B); (ii) it conflates the wage *technology* with the job *package*, so occupation availability — an access cell — is silently equalised, double counting across the §2.4 boundary; (iii) it breaks the guarantee that no operator introduces a package.

**A3 — Equalise `δ_occ` to a common occupation-invariant value.** Fails on exhaustiveness and attribution: `δ_occ` is the sole cell through which access and ability interact (§2.4); flattening it zeroes the interaction that Shapley symmetry allocates, mechanically shrinking the access component for a reason with no economic content, and it violates the mirror guard by writing into the wage consequences of an access-assigned weight.

**A4 — Set education to a named level (e.g. the omitted `educM`) rather than the dwt share vector.** Fails for exactly the reason R-71 rejected median-region: anchoring on a chosen cell converts the ability component into a distance-to-that-cell statistic rather than a decomposition of observed inequality, and the omitted category is a normalisation artifact carrying no reference status.

### Preference operator

**P1 — Set the pinned switch to `swapped`.** Fails: contract §7 records `held` as the default and R-71 ratified it; and in the singles application swapping would activate couples-only coordinates (`theta_l_m`, `beta_ll`) on singles rows — a specification error rather than a normative choice (§3.3).

**P2 — Construct `θ̄^pref` by linearly averaging the two group coefficient blocks.** Fails on three counts: (i) a linear average of Box-Cox curvature parameters (`theta_l_*`, `theta_c_*`) is not the preference of any agent and is not a member of the accepted family — the family-membership objection that killed the population-average density in U12 §6.1; (ii) `beta_l0_sm` is a W-4 flagged, near-bound coordinate, so the average imports a boundary artifact into every coalition value; (iii) no household is at the average, so the fixed-point check V18 has no test case and idempotence becomes an assertion rather than a test.

**P3 — Reuse `R^h` (the measure-side reference preference) as `θ̄^pref`.** Fails on contract §2's double-interpretation prohibition, and is the exact mirror of U12 §6.2's rejection of `Ā` as the access operand: `R^h` fixes a *measure's* normative stance in the direct evaluation channel (`reference_preference.W5: "R_h"`); reusing it as the decomposition operand collapses Exercise A into Exercise B, which the contract keeps in separate documents as a structural guard.

**P4 — Absorb the budget mapping into `P` by replacing `c_ij` or applying a reference income shift.** Fails: wholesale EUROMOD re-evaluation is forbidden and silent interpolation of missing `c_ij` is forbidden (contract §6.1(iii)); an invented additive shift is exactly what charter §6 prohibits. The budget-mapping heterogeneity must be escalated under V20c (§4.4), not absorbed.

---

## 7. Validation mirrors (V14+)

To be frozen verbatim in the Stage-A execution contract alongside V1–V13.

| # | Check | Assertion | On failure |
|---|---|---|---|
| **V14** | **Operator commutation / mixture path-independence** | For every coalition, applying the constituent operators in both (all) orders yields bitwise-identical resolved objects; the `{A,B}` occupation object equals the frozen `p̄̄(loc4)`; the GSUR×educ term matches the §2.6 table cell-for-cell. | Gate. A failure means the D1 slot disjointness is violated somewhere. |
| **V15** | **Ability V7-analogue (mirror guard)** | Under `B`, the following are bitwise invariant per row: the `dgn` conditioning of the occupation availability weights, the region/GSUR level cells of `g^E`, `g^H`, `π`, and `c_ij`. | Gate. This is the operational form of §2.7. |
| **V16** | **Preference V7-analogue** | Under `P`, `log g` is bitwise invariant per row in **all** factors, and `c_ij` and `π` are bitwise invariant. | Gate. |
| **V17** | **Ability fixed point** | A household (or synthetic row set) at `(ē, p̄ₑₓₚ, p̄ₑₓₚ²)` and in the reference education cell sees `V_i` and every `Ω_i^k` unchanged to ≤ `1e-12` (mirror of V1's ratified tolerance). | Gate. |
| **V18** | **Preference fixed point** | A household at the reference taste covariates **and** in the reference group block sees `V_i` and every `Ω_i^k` unchanged to ≤ `1e-12`. Requires that the reference group block be an actual accepted block — which is why P2 fails. | Gate. |
| **V19** | **No re-estimation, mechanically asserted** | The 47-coordinate `θ̂` is bitwise identical in every coalition, with the sole exception of the declared step-(b) substitution; the substitution map is hash-recorded and is a pure selection among accepted coordinates. | Gate (charter §5.3, §10). |
| **V20** | **Degeneracy, split three ways** | **a)** resolved equalised `u` block, taste covariates, and every `g` factor hash-identical across households under `{A,B,P}` (tolerance `1e-9`); **b)** residual `I(Ω^k)` within a declared simulation tolerance derived from the counterfactual ESS, not `1e-9`; **c)** every remaining source of cross-household variation enumerated and assigned or escalated. | a) gate; b) gate at the declared tolerance; c) **halt to deputy** if `c_ij` heterogeneity is unassigned. Supersedes V8's single-tolerance form (item S4). |
| **V21** | **Level-of-aggregation gap** | Report `C_A + C_B`, `C_O^(2)`, and their difference. Diagnostic, **not** a gate. | Report; interpret as aggregation level, never as an error. |
| **V22** | **Counterfactual ESS for the mirrors** | Extend the ratified U12 V6 (threshold 30) to the `{B}`, `{P}`, `{A,B}`, `{A,P}`, `{B,P}`, `{A,B,P}` coalitions: the IS target changes under each while the proposal does not. The Stage-D `V_i^dir` cross-check at the frozen 0.5-nat tolerance (R-71) applies to the flagged subsets **of each coalition**, not only the baseline. | Apply the frozen escalation rule per coalition; halt if the flagged set widens beyond the Stage-A materiality number. |
| **V23** | **Reference-group pre-registration** | The `θ̄^pref` group selection and its mirror sensitivity are recorded, with timestamp and hash, **before** any coalition value is computed. | Gate (charter §5.7, §6; §5.3 of this memo). |

---

## 8. Decisions proposed

- **B1** `B` substitutes `educ`, `pexp`, `pexp²` in `g^W`'s `μ_i`, plus the `educ` slot of the education-assigned `g^E` cells and the `educ3` conditioning of `g^Occ` (§2.1).
- **B2** References: dwt education share vector; dwt means of `pexp` and `pexp²` separately (index-mean convention per R4); `p̃(loc4|dgn)` as the `educ3`-marginal of the frozen joint `Π` (§2.2, §2.5).
- **B3** `σ` equalisation is the identity; the M08 ability component is location-only and is a lower bound with respect to dispersion heterogeneity; LOC4 boundary restated in advance (§2.3).
- **B4** `δ_occ` is untouched as an argument-substitution matter; it is the sole access–ability interaction cell, allocated by Shapley symmetry, and this is stated in the paper (§2.4).
- **B5** Occupation availability is handled by marginal selection from one frozen joint object, making composition path-independent (§2.5).
- **B6** The mirror guard of §2.7 is transcribed verbatim into the execution contract and enforced by V15.
- **P1'** `P` has two steps: covariate substitution (dwt references for `age_norm`, `age_norm2`, education-in-leisure, children) and group-block selection; coefficients are selected, never re-estimated (§3.1–3.2).
- **P2'** Age-in-leisure equalised in `P`; education-in-leisure is a preference cell and this does not violate access-purity (§3.2).
- **P3'** `held` is honoured, constrains step (b) by excluding `theta_l_m` and `beta_ll`, and is **non-binding in M08** under singles-only scope; Stage A verifies and halts otherwise (§3.3).
- **P4'** `θ̄^pref` ≠ `R^h`; the two are distinct objects and must not be identified (§6, P3).
- **C1** Eight coalitions, Shapley weights `{1/3, 1/6, 1/6, 1/3}`, operators commute on disjoint argument slots (§4.1–4.3).
- **S-10** Arguments hash-asserted invariant; equalised values legitimately scenario-dependent and reported in full (§5).

---

## 9. Open items for ratification

- **S1** The index-mean convention for squared and dummy arguments: baseline `(E[pexp], E[pexp²])` and dwt share vector for education; single sensitivity = profile-at-mean-worker and share-weighted-probability. Mirror of R4.
- **S2** **The `θ̄^pref` group-block selection** — the most consequential open choice in this memo. Proposed: declare one accepted singles block as the reference by explicit normative ratification, report the other as the single pre-registered sensitivity, and record the choice under V23 before any result exists. Coefficient averaging is rejected (P2). *Note: `R^h` does not pin this. `R^h` is the measure-side reference preference named in the config for `W^5`'s reference evaluation; its full definition is not present in the attachments, and it is a different object with a different role. Stage A must extract `R^h`'s exact definition from the accepted spec/charter text under the R8 verify-then-escalate procedure and halt if it is undefined (charter §11: "a required reference set/operator is undefined").*
- **S3** Ratify the education-in-leisure routing to preference (§3.2) as an explicit normative call, with its consequence stated: education-correlated taste differences are preference-classified and not compensated.
- **S4** Ratify the V8 → V20a/b/c split and the declared simulation tolerance for V20b. The ratified `1e-9 · max(1, |I|)` is retained for V20a's exactness assertions only; applied to V20b it is expected to fail mechanically (§4.4).
- **S5** Ratify the headline definition: opportunity content ≡ `C_A + C_B` from the three-channel game, with `C_O^(2)` and the gap reported as V21 diagnostics (§4.5).
- **S6** Rule on the §4.4 grand-coalition residual: adopt the endowment/needs fourth-channel escalation, or direct an alternative that preserves exhaustiveness without a `c_ij` operator. This is a candidate charter §11 halt and should be routed with R8's Stage-A verification.
- **S7** Ratify V14–V23 and fix the V22 per-coalition materiality escalation number alongside the Stage-A V6 number.
- **S8** Confirm the expected-positive Tier-2 posture of §5.4 — that boundary-aware/resampling inference is scheduled as the anticipated path for the ability and preference components rather than treated as an exception.
- **S9** Direct the manuscript disposition of the two degeneracy findings (`σ` in ability, `held` in preference), alongside the R10-ratified hours-availability caveat, as a single specification-limits block.

---

## 10. Output discipline

- **Mission ID:** JMP-M08; register item R9 (mirrors U12).
- **Authoritative inputs:** Goal-1 ruling R-71; ratified U12 memo; charter; welfare input handoff; scaffold contract v2; W^3 gate report; bookkeeping rules.
- **Decisions made:** B1–B6, P1'–P4', C1, S-10 disposition (§8), all PROPOSED.
- **Unresolved decisions:** S1–S9 (§9). S6 (and S4 in part) are candidate charter §11 halts, to be routed with the R8 Stage-A verification.
- **Exact output filename:** `docs/Missions/JMP_M08_ability_preference_operators_design_v1.md`
- **Next authorised action:** Goal 1 Manager review and ratification of B1–B6, P1'–P4', C1 and disposition of S1–S9. On ratification, the D1 cell table, the three operator definitions, the coalition table with Shapley weights, and V1–V23 are transcribed verbatim into `docs/missions/JMP_M08_singles_welfare_execution_contract_v1.md` (charter §6) before any welfare number is computed. No implementation, no computation, and no commit is authorised by this memo.

**Statement:** no welfare number, no decomposition number, no parameter value, and no re-estimation is produced or implied by this memo. No file has been written.
