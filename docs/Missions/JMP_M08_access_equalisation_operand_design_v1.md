# JMP-M08 — Access-Equalisation Operand Design (register item U12)

**Mission:** JMP-M08 — France 2016 Singles Welfare Integration and Baseline Decomposition Prototype
**Register item:** U12 — access-equalisation operand (`g_ref`)
**Document class:** design memo (economics + operator specification). No computation, no code execution, no welfare number, no re-estimation.
**Status:** **PROPOSED — PENDING RATIFICATION** by the Goal 1 Manager. Nothing here is frozen. Stage A (charter §6) is the freezing instrument.
**Target repository path:** `docs/Missions/JMP_M08_access_equalisation_operand_design_v1.md`
**Author role:** M08 design author (advisory)

**Authoritative inputs used**

1. `JMP_M08_singles_welfare_decomposition_mission_charter_v1.md` (§4.3 decomposition, §5 scope rulings, §6 Stage-A contract, §7 Stage F, §9 acceptance gates, §10 prohibitions, §11 halt conditions).
2. `JMP_M08_welfare_input_handoff_v1.md` (§1 accepted inputs, §2.1 S-10 obligation, §2.2 Tier-2 trigger, §2.3 LOC4 Path-B ruling, §2.4 W-4 visibility, §2.5 `beta_l0_sf` vigilance, §2.6 scope).
3. `RURO_welfare_scaffold_design_contract_v2.md` (anchors; §2 welfare-vs-decomposition boundary; §3.1 core and IS estimator; §3.2 measure table; §3.4 reference sets; §4 config schema; §6 gates; §7 decomposition-readiness; §9 forbidden items).
4. `RURO_welfare_gate_report_W3_v1.md` (Preflight 2 engine construction; Gate 1(ii) ESS; Gate 2 inversion; Gate 4 reference coverage; decomposition-readiness block counts).
5. Normative bookkeeping rules as stated in the commissioning instruction (access-purity for education; gender-in-offers vs gender-in-tastes; age split).

**Not used as data:** management memos (handoff §1, charter §2).

---

## 1. What the operand is, and what it is not

### 1.1 The object

The Shapley–Shorrocks game of charter §4.3 has three channels — access, ability, preference. Playing the game requires, for each channel, an **equalisation operator**: a map that replaces the household-specific determinants of that channel by a common object, so that the channel's contribution to inequality can be read off the inequality fall. U12 specifies the operand for the access channel only: the object substituted for each household's access-side offer environment.

The operand acts **inside the attained-utility core**, not on the measure side. Per scaffold contract §3.1 and the engine construction traced in the W3 gate report (Preflight 2), the core is

```
V_i = log Σ_{j∈C_i} exp( u_i(c_ij, ℓ_ij; θ^pref) + log g(j; x_i, θ^opp) − log π(j; x_i) )
```

and, following the engine's own factorisation (`V = u + log_h + log_w + log_market − log_prior`, with the mirrored proposal `log_prior = log q_E + working·(log q_Occ + log q_H + log q_W)`), the opportunity density factorises as

```
log g(j; x_i) = log g^E(work_j ; x_i)
              + work_j · [ log g^Occ(loc4_j | x_i) + log g^H(h_j) + log g^W(w_j | loc4_j ; x_i) ]
```

**The access-equalisation operator replaces the access-assigned cells of this factorisation by a frozen common object `g_ref`, holding `u_i`, `g^W`, and `π` at their accepted household-specific values.** It changes the *weights* on the household's existing drawn alternatives. It does not change the alternatives, the consumption vector `c_ij`, the proposal, or the parameter vector.

### 1.2 Three things it is not

**(a) It is not the welfare reference `Ā`.** The scaffold contract ratifies `Abar_reference.primary = "type_conditional_median_opportunity"` (§4 config) as the reference *set* for `W^5`, evaluated under the named reference preference `R^h` (§4 `reference_preference.W5: "R_h"`). The two objects differ on four axes, and conflating them is precisely the double-interpretation that scaffold contract §2 forbids:

| | `Ā` (welfare reference, Exercise A) | `g_ref` (equalisation operand, Exercise B) |
|---|---|---|
| **Role** | fixes the *normative stance* of a measure — how much of the set is compensated | fixes the *counterfactual environment* of a channel in the decomposition game |
| **Where it enters** | the **direct evaluation channel** — the inversion/reference side (contract §3.2) | the **attainment channel** — inside `V_i` only |
| **Object type** | a *set* of reference job packages requiring their own `c_ij` (contract §6.1(iii)) | a *density* over the household's existing rows; introduces **no** new package |
| **Sex conditioning** | type-conditional by ratified default (contract §3.3, §4) | **sex-pooled** (§4 below), because gender-in-offers is compensable |
| **EUROMOD exposure** | can trigger the reference-coverage gate (contract §6.1(iii)) | cannot — reweighting only (see V4, §7) |

The divergence in sex conditioning is deliberate, not an inconsistency. `Ā` is type-conditional because a measure's reference must be evaluated for a household *as it is*; `g_ref` is sex-pooled because the decomposition's job is to remove the compensable part of what the household is exposed to.

**(b) It is not the proposal `π`.** The W3 gate report is explicit that the common employment (`π0 = 0.10`) and hours (fixed D1 five-mode mixture) channels are **proposal** channels, and that the structural market block (GSUR/region/year) "lives in `g`, not in `π`". `π` is a sampling artifact. Altering it would invalidate the accepted `−log π` correction (contract §3.1, mandatory) and re-open reprice parity (charter Stage B). **The `prior` column is held byte-identical across every coalition** (check V3).

**(c) It is not a re-estimation.** `g_ref` is a plug-in evaluation of accepted objects at frozen reference arguments (charter §5.3, §10; handoff §1).

---

## 2. Required change of the decomposition unit: cells, not blocks

The scaffold contract exposes channel membership as three *parameter-name lists* (`welfare.blocks: preference / ability / access`, §4, §7). The W3 gate report records the realised counts as preference 20 / ability 6 / access 23.

**A parameter-list partition cannot implement the bookkeeping rules.** Education enters the certified access factors (occupation availability is `p(loc4 | dgn, educ3)`; the market index carries education-interacted GSUR terms), while access-purity requires education to route *exclusively* through the wage/ability channel. If the access operator is defined as "replace the access parameter list", education-driven offer differences are attributed to access, violating access-purity. If instead the operand is education-conditioned to protect access-purity, education-driven offer heterogeneity survives *both* the access and the ability operator and lands outside all three channels — breaking the grand-coalition degeneracy that Shapley exhaustiveness requires (charter §7 Stage F.3, §9.8).

**Proposed resolution (D1).** The decomposition unit is the **(factor × argument) cell**, not the parameter block. Each cell of the opportunity density is assigned to exactly one channel:

| Cell | Channel | Ground |
|---|---|---|
| `g^E`: intercept, region dummies, GSUR level | **access** | regional/urbanisation environment is offer-side (charter §4.3 access) |
| `g^E`: education interactions (GSUR×educ and any `educ`-interacted hours/market term) | **ability** | access-purity: education routes exclusively through wage/ability |
| `g^Occ`: dependence on `dgn` | **access** | gender-in-offers is access/compensable |
| `g^Occ`: dependence on `educ3` | **ability** | access-purity |
| `g^H`: hours-band shifters | **access** (degenerate — see §3.4) | employment/hours availability (charter §4.3) |
| `g^W`: `μ_i` via `educ`, `pexp` | **ability** | accepted wage technology; education and experience-via-wages |
| `g^W`: `δ_occ[loc4_j]` occupation mean-shift | **ability** | wage technology, not availability (§5) |
| `g^W`: `σ` (dispersion) | **ability** | wage dispersion (charter §4.3 ability) |
| `u_i`: age-in-leisure, kids, `β_l0`, `θ_l`, `β_c`, `θ_c` | **preference** | tastes (charter §4.3); age-in-leisure per the age split |
| `π` | **none** | sampling artifact (§1.2(b)) |

Consequences, stated plainly: the **ability** operator becomes "replace `educ` and `pexp` wherever they appear, in `g^W` *and* in the education-assigned cells of `g^E`/`g^Occ`, plus `σ`", and the **access** operator becomes "replace everything else on the offer side, at own education". Under the grand coalition every cell is replaced, every household faces the identical `g`, and the exhaustiveness precondition is testable (V8).

This is a genuine amendment to the scaffold contract's §7 interface (which assumes a name-list partition). It is submitted for ratification as **R1** (§9).

---

## 3. The operand, coordinate by coordinate

### 3.1 Construction principle: covariate-reference, not density-averaging

Two constructions are available. **Covariate-reference:** evaluate the *accepted* parametric access factors at a frozen reference argument vector `x̄^acc`. **Distribution-reference:** replace the whole factor by an averaged probability object. The proposal adopts **covariate-reference wherever the accepted object is a parametric index, and distribution-reference only where the accepted object is itself a conditional probability table**.

Reasons: (i) the counterfactual remains a member of the accepted family — it is the offer environment of a well-defined reference worker, and every number in it is `exp` of the accepted index at accepted `θ^opp`, requiring no new estimation (handoff §1; charter §5.3); (ii) it makes the fixed-point identity of V1 (§7) an *exact* check rather than a vacuous one; (iii) it permits the cell-level bookkeeping of §2, which a pooled mixture cannot (see §6.1).

### 3.2 Employment / market margin `g^E` — **access, pooled**

Replace `x_i` in the access-assigned cells of `g^E` by:

- **Region:** the population-share vector over `drgn1` for the P2a singles sample, substituted for the household's region indicator vector. This sets the region contribution to the **share-weighted mean of the linear index**, which is well defined, unique, and pinned by the data — as opposed to a chosen region, which is not (§6.3). Note explicitly: this is the mean of the index, not the mean of the implied employment probability; the share-weighted-probability variant is pre-registered as a sensitivity, not the baseline.
- **GSUR:** the sample mean of the accepted `gsur` column over P2a singles.
- **Education-interacted cells:** *not* replaced (they are ability cells, D1).

Because `g^E` is the only factor present at the non-employment alternative, the operator moves the **employment-availability margin** — the relative weight of the non-employment row against the employed rows — for every household. This is correct: employment availability is named access in charter §4.3.

### 3.3 Occupation availability `g^Occ` — **access in the sex argument only**

The accepted object is a conditional table `p(loc4 | dgn, educ3)`. For a table, "evaluating at a reference covariate" *is* selecting a different cell. The access-assigned argument is `dgn`; the ability-assigned argument is `educ3`. The operand is therefore the **sex-pooled, education-conditional** table

```
p̄(loc4 | educ3)  =  Σ_{s ∈ {m,f}} ω_s(educ3) · p(loc4 | dgn = s, educ3)
```

with `ω_s(educ3)` the frozen population sex shares within the education cell, computed once on the P2a singles sample and recorded before execution. Every household of a given `educ3` receives the same occupation-availability distribution regardless of sex; education-conditional structure is left standing for the ability operator to remove.

This single substitution is the operational content of "gender-in-offers is compensable." It is also the cell that LOC4 will move (§8.2).

### 3.4 Hours availability `g^H` — **access, but empirically degenerate**

The certified hours-band shifters carry no household covariates: `g^H(h_j)` is identical across households. The access operator's action on this cell is therefore the **identity**, and the hours cell contributes exactly zero to the access component.

**This must be stated in the paper, not buried.** Under the certified specification, measured access heterogeneity is generated by region×GSUR employment availability and by sex-differentiated occupation availability — and by nothing else. The access component is a lower bound on offer-side inequality with respect to any hours-availability heterogeneity the specification does not carry. Any `educ`-interacted hours term found in the frozen YAML is an *ability* cell under D1, not an access cell; Stage A must enumerate the hours block against the frozen spec and record the finding.

### 3.5 Age — **absent by design**

Age enters the certified model twice: as experience in the wage index (ability) and as age-in-leisure in `u_i` (preference). It enters **no access factor**. The operand therefore neither conditions on age nor equalises it. Adding age to the access conditioning set would import either experience (ability) or leisure taste (preference) into access, violating the age split in both directions. Stage A must verify against the frozen spec YAML that no age or experience term appears in any access-assigned cell, and **halt** if one does (charter §6, §11).

### 3.6 Summary of the conditioning decision

| Coordinate | In `g_ref`'s conditioning set? | Criterion | What the access component then measures |
|---|---|---|---|
| **Sex** | **No — pooled** | gender-in-offers compensable | includes between-sex offer inequality; excludes gender-in-tastes, which stays in `u_i` at own `θ^pref` |
| **Education** | **Yes — held at own** | access-purity: education is ability-only | *within-education* access inequality; education's offer-side content is charged to ability, where the bookkeeping puts it |
| **Region** | **No — pooled to the share-weighted index** | regional environment is named access | includes the full regional/GSUR employment-availability gradient |
| **Age / experience** | **N/A — absent from access** | age split | nothing; verified, not assumed |

The **headline cut is insensitive to the education row.** Charter §4.3 makes the primary decomposition opportunity-environment vs preferences, with access-vs-ability nested inside. The opportunity operator equalises access *and* ability cells jointly, so wherever education's offer content is charged, it stays inside opportunity. The education decision is consequential only for the nested split — which is exactly the status charter §4.3 and the project role assign to it.

---

## 4. The central tension, resolved

**The tension.** Gender-in-offers is compensable. A sex-conditional operand — the natural analogue of the ratified type-conditional `Ā` — would substitute each household's own-sex offer environment, leaving the male–female offer gap untouched by access equalisation. That gap would then survive into the ability, preference, and interaction terms of the Shapley average, i.e. it would be **misclassified out of the compensable channel**, and in the singles application it would be misclassified largely into components the paper explicitly refuses to call responsibility (charter §4.3). Against that, a fully pooled operand changes type composition: it substitutes an environment no observed household faces, and the counterfactual mixes over characteristics the bookkeeping treats asymmetrically.

**Resolution.** Pool the operand **only over the coordinates the bookkeeping declares compensable**, and hold at own value the coordinates the bookkeeping routes elsewhere. This is neither "type-conditional" nor "fully pooled"; it is *bookkeeping-conditional*, and it is the only conditioning rule that makes the access component equal to what the paper claims it measures. Composition change is confined to sex and region — precisely the two dimensions declared compensable — and is therefore a feature of the counterfactual, not a contaminant of it.

**What the access component consequently measures, stated for the paper:** the money-metric inequality attributable to differences across single adults in employment availability by region and local labour-market conditions, and in occupational availability by sex, holding own education, own wage technology, and own tastes fixed. It is *not* a measure of total offer-side inequality (education's offer content is charged to ability by the access-purity convention, and hours availability is degenerate in the certified spec), and it is model-conditional and non-causal (charter §4.3).

---

## 5. The wage-density boundary: where the cut runs through the job-package draw

A job package is `j = (work_j, loc4_j, h_j, w_j)`. The access/ability boundary cuts **between availability and technology**, and the cut is clean because the two live in different factors of the same log-additive index:

- **Access owns the weights on packages:** `g^E`, the `dgn` argument of `g^Occ`, `g^H`.
- **Ability owns the wage attached to a package:** `g^W(w_j | loc4_j; x_i)` in full — the Mincer index `μ_i = X_i b + δ_occ[loc4_i]`, including the **occupation mean-shift `δ_occ`**, and `σ`.

**The operational statement of the boundary.** Under the access operator, the per-row wage term `log g^W(w_j | loc4_j; x_i)` is **not re-evaluated**. It is read from the accepted per-row construction unchanged. The access operator changes only which rows carry weight. This is checkable bitwise (V7) and is the sharpest available non-double-counting test.

**The residual composition effect, and why it is correct.** Reweighting occupation availability changes the *marginal* distribution of offered wages a household faces, because `δ_occ` differs across `loc4`. That composition effect is properly part of access: "which occupations are open to you" has wage consequences, and attributing them to access is what makes access an *opportunity* concept rather than a bookkeeping curiosity. It is not double counting, because the technology `(b, δ_occ, σ)` is untouched and remains available in full for the ability operator to equalise. The mirror-image guard applies to the ability operator: it must replace `educ`/`pexp`/`σ` in `g^W` **without** altering the occupation availability weights — otherwise ability would absorb access.

**One-line rule for the frozen contract:** *access moves the measure over job packages; ability moves the wage map defined on job packages; neither may write into the other's factor.*

---

## 6. Rejected alternatives

### 6.1 Population-average opportunity density, `g_ref = N⁻¹ Σ_i g_i` — **rejected**

Fails on four counts. (i) **Bookkeeping.** A mixture over households mixes over education and experience, importing ability into the access operand and violating access-purity directly; the mixture cannot be decomposed cell-by-cell, so the D1 routing of §2 is unimplementable under it. (ii) **Family membership.** A mixture of members of the accepted density family is generally not a member; there is no `x̄` and no accepted index producing it, so it cannot be described in the paper as the environment of a reference worker, and the claim "constructible from accepted objects" degrades to "computable from accepted objects". (iii) **Unverifiable fixed point.** No household is at the mixture, so V1 (§7) has no test case and the idempotence property is asserted rather than checked. (iv) **Exhaustiveness.** Because the mixture confounds channels, the grand coalition is no longer guaranteed degenerate in a way traceable to a cell partition, and a V8 failure would be undiagnosable.

### 6.2 Type-conditional median opportunity (the ratified `Ā` primary) — **rejected as the operand**

Fails on two counts. (i) **Bookkeeping.** "Type-conditional" is sex-conditional (contract §3.3, §4 `unit.report_groups`). It leaves gender-in-offers unequalised and therefore misclassifies a compensable difference out of the access component — the exact failure §4 exists to prevent. (ii) **Boundary discipline.** Reusing the Exercise-A measure reference as the Exercise-B channel operand is the double-interpretation scaffold contract §2 forbids in terms: the measure stance and the decomposition channel are "the same normative cut operationalised two ways and must never be double-interpreted." Its rejection here is *not* a criticism of `Ā`, which remains ratified for `W^5` on the measure side.

### 6.3 A named reference cell (e.g. male / medium-education / Île-de-France) — **rejected**

Fails on four counts. (i) **Best-cell contamination.** The omitted region in the certified specification is Île-de-France, the most favourable environment; anchoring there converts the access component into a distance-to-best statistic rather than a decomposition of observed inequality. (ii) A sex-specific cell reintroduces §6.2's defect. (iii) An education-specific cell moves education into the access operator, violating access-purity. (iv) **Post-hoc thresholds.** Cell choice is not pinned by the bookkeeping — many cells qualify — so the selection is exactly the kind of post-hoc reference set charter §5.7 forbids and §6 requires frozen before results exist.

### 6.4 Re-drawing the offer set from the pooled empirical distribution of realised jobs — **rejected**

(i) Realised jobs are choices, not offers; the pooled empirical distribution is selection-contaminated and its use would silently re-import preferences into the access operand. (ii) It requires redraw machinery: the `V_i^dir` redraw-from-`ĝ_i` estimator is recorded **BLOCKED** in the W3 gate report (Gate 1, flagged-subset cross-check, "not implemented in Stage One; not approximated"). Building an operand on blocked machinery is a halt condition, not a design.

---

## 7. Pre-registered validation checks

To be frozen verbatim in the Stage-A execution contract (charter §6) before any welfare number exists. Each is a real check with a stated failure action.

| # | Check | Assertion | On failure |
|---|---|---|---|
| **V1** | **Fixed point / idempotence** | For a household (or synthetic test row set) whose access-assigned arguments equal `x̄^acc`, the access operator returns `V_i` and every `Ω_i^k` unchanged to ≤1e-12. | Gate the run. |
| **V2** | **Reference coalition-invariance** | Each measure's reference construction (own-set baseline for `W^3`, `Ā`, `J`, `o`) and the `c_ij` matrix are hash-identical across all eight coalitions. | Gate. Prevents the reference co-moving with the channel and cancelling the effect. |
| **V3** | **π-invariance** | The `prior` column is hash-identical across all eight coalitions. | Gate (contract §3.1). |
| **V4** | **No new package** | Alternative support, row count, and `c_ij` hash unchanged under every coalition ⇒ the reference-coverage / EUROMOD gate (contract §6.1(iii), W3 Gate 4) is not re-triggered, and `abar_j_o_required` is unchanged. | Gate; a failure means the operand has silently become a set-substitution. |
| **V5** | **Density integrity** | `p̄(loc4 \| educ3)` sums to 1 within each education cell; counterfactual `log g` finite on every row; count of non-finite = 0. | Gate. |
| **V6** | **Counterfactual ESS** | Re-run the contract §6.1(ii) ESS diagnostic (`ESS_i`, max normalised weight) under **every non-baseline coalition**. The counterfactual changes the IS *target* while the proposal is unchanged, so baseline ESS does not transfer. Baseline singles ESS is already weak (W3 gate report: median 20.3 / 18.8; 1,918/2,243 and 2,493/2,764 below the threshold of 30). | Apply the frozen escalation rule to the counterfactual, not only the baseline. If the flagged set widens materially and `V_i^dir` remains blocked, **halt** (charter §11). |
| **V7** | **No double counting with the wage/occupation technology** | (a) the 47 coordinates form an exact partition over preference/ability/access cells — no coordinate in two channels, none omitted; (b) the per-row `log g^W` contribution is **bitwise identical** between baseline and access-equalised runs, confirming `δ_occ`, `μ_i`, `σ` are untouched by the access operator. | Gate. Membership is frozen and unchanged after results (charter §9.10). |
| **V8** | **Grand-coalition degeneracy** | With access+ability+preference all equalised, `I(Ω^k)` ≤ the frozen tolerance. | Record the residual and **halt**; do not renormalise silently. Exhaustiveness (charter §9.8) is the acceptance gate. |
| **V9** | **Sex-pooling audit** | Under access equalisation, the between-sex difference in mean counterfactual access index is exactly zero. | Report; a non-zero value means a sex-conditioned cell was missed. |
| **V10** | **Directional sanity (reported, not gated)** | Households whose own access index is below the reference in every access cell weakly gain. | Report. Not a theorem once occupation composition interacts with own wage technology; gating it would be an invented identity. |
| **V11** | **Determinism** | Bit-for-bit reproducible on re-run given identical inputs (mirrors contract §5 Step 1(d)). | Gate. |

Two additional binding checks arising from document reconciliation:

| # | Check | Note |
|---|---|---|
| **V12** | **Block-count reconciliation** | The W3 gate report records `welfare.blocks` as preference 20 / ability 6 / access 23 = **49 names** against a **47**-coordinate certified vector. Stage A must reconcile the arithmetic against the frozen spec YAML and the accepted θ̂ (handoff §1) and **halt** if the declared membership is not an exact partition. That report was also produced on the pooled couples-inclusive build at working-tree HEAD `7cac2e3`; per charter §2 its membership counts are indicative for P2a singles and are not imported as validated. |
| **V13** | **Occupation-term separability** | Stage A must bind each factor of §1.1 to the exact engine term (`log_h`, `log_w`, `log_market`, and wherever the occupation contribution is assembled) and **halt** if the occupation contribution is not separable from the market index in the accepted production path — the access operator is not implementable without that separation. |

---

## 8. Interaction with standing obligations

### 8.1 S-10 four-scenario sensitivity (handoff §2.1) — operand held fixed, and provably so

The S-10 perturbations move `beta_l0_sm` (preference, in `u_i`) and `beta_w_pexp2` (wage/ability, in `g^W`). **Neither is an access-assigned coordinate.** Therefore:

1. The reference arguments `x̄^acc` (region share vector, GSUR mean) and the frozen table `p̄(loc4 | educ3)` with its weights `ω_s(educ3)` are **numerically identical** across all four scenarios;
2. because the access-assigned index coefficients are themselves unperturbed, `g_ref` is numerically identical across all four scenarios — not merely "held fixed by convention" but **invariant by construction**;
3. this is asserted by hash of the resolved operand object in each of the four scenario runs;
4. the operand and its reference arguments are recorded **before** execution, alongside the Δⱼ and θ^sens_j vectors that handoff §2.1 requires be recorded before execution.

S-10 sensitivity of the access *component* therefore operates entirely through attainment and through the other two channels' equalised values — never through the operand. Confirmed.

**Material-loading assessment (handoff §2.2, Tier-2 trigger) — flagged in advance.** The access *component* is a Shapley average over coalitions that include the ability- and preference-equalised states, so it depends on `beta_w_pexp2` and `beta_l0_sm` through those coalition values even though the operand does not. **The material-loading question therefore cannot be answered in the negative a priori for the access component**; it must be answered numerically at the mission's first gate, as handoff §2.2 requires. `beta_l0_sf` is monitored alongside per handoff §2.5, with no bound asserted absent an accepted record. The two W-4 coordinates remain visible in every access-component table and caveat block (handoff §2.4).

### 8.2 LOC4 (handoff §2.3, Path B; charter §5.5, §10)

LOC4 changes exactly the two objects this memo cuts between: the occupation availability table and the occupation-specific wage density. Pre-register now, so LOC4 cannot reopen the bookkeeping:

- **Form is LOC4-stable.** The operand remains "sex-pooled within `educ3` of whatever accepted occupation availability object is in force"; the definition does not change.
- **Numbers change.** `p̄(loc4 | educ3)` and the counterfactual index values will differ under the four-density variant. This is the first robustness axis, as handoff §2.3 requires, not a respecification.
- **Boundary restatement under four densities:** occupation *availability* remains **access**; occupation-specific wage *mean* and *dispersion* (`δ_occ`, and any `σ_occ`) are **ability**. No double counting: the mean-and/or-dispersion formulation of the Path-B ruling governs, and only one of the two may carry a given occupation effect.
- LOC4 is not implemented in M08 (charter §10). No final quantitative claim is issued before it closes (charter §1, §5.5).

### 8.3 A blocking dependency this memo does not resolve

The operand's effect on each `Ω_i^k` is mediated by the measure-side inversion normalisation, and there is an unresolved item there. The W3 gate report records `Ω^3 ≈ −2.91e-10` for **every** household and `I(Ω^3)` degenerate, "correct by construction" because `W^3`'s reference is the household's own set — with the non-trivial variation expected to "arise only once a decomposition imposes an equalised channel." A decomposition of a baseline vector whose inequality is identically zero is not a decomposition of inequality; and if the own-set reference is allowed to co-move with the channel, the operator's effect cancels (which V2 catches).

**U12 does not settle this.** The operand is well defined either way — it acts on `g` inside `V_i`, and its construction does not depend on the resolution. But the *interpretation* of the resulting `Ω` and the non-degeneracy of the `W^3` anchor do. Per charter §6 ("if an exact reference rule or operator is absent or internally inconsistent, halt before execution and return a bounded design conflict — do not invent it"), this is returned as a bounded design conflict and listed as R8 below. It is a candidate charter §11 halt ("a required reference set/operator is undefined").

---

## 9. Proposed config surface (design only)

Mirroring the scaffold contract §4 schema style, so the operand is config-driven and the welfare source carries no France/2016 constants (contract §9):

```yaml
decomposition:
  channels: ["access", "ability", "preference"]
  routing_unit: "factor_argument_cell"        # D1 — replaces name-list blocks (contract §7 amendment)

  access_operand:
    construction: "covariate_reference_plus_pooled_conditional_table"
    conditioning_set: ["education"]           # own education retained; sex/region pooled; age absent
    pooled_over: ["sex", "region", "gsur"]
    employment_market:
      region_reference: "population_share_weighted_index"
      region_sensitivity: ["share_weighted_probability", "median_region"]
      gsur_reference: "sample_mean"
    occupation:
      reference: "sex_pooled_within_education"
      pooling_weights: "population_sex_shares_within_educ3"
      weights_frozen_before_execution: true
    hours: "identity"                          # degenerate in certified spec (§3.4)
    wage_density: "untouched"                  # ability (§5); V7(b) asserts bitwise identity
    proposal_pi: "untouched"                   # V3
    survey_weights: "OPEN — see R6"

  invariants:
    reference_coalition_invariant: true        # V2
    operand_invariant_across_s10: true         # §8.1, hash-asserted
    grand_coalition_degeneracy_tolerance: "declared"   # V8
```

---

## 10. Decisions made in this memo (all PROPOSED)

- **D1** Decomposition unit is the (factor × argument) cell, not the parameter name list (§2).
- **D2** `g_ref` is covariate-reference for parametric factors, distribution-reference only for the accepted conditional table (§3.1).
- **D3** Sex: pooled (§3.3, §4).
- **D4** Education: held at own; education's offer-side content routed to ability (§3.6).
- **D5** Region and GSUR: pooled to share-weighted index / sample mean (§3.2).
- **D6** Age/experience: absent from access; verified against the frozen spec, not assumed (§3.5).
- **D7** Access/ability boundary: access moves the measure over packages; ability moves the wage map on packages; `δ_occ` is ability and `log g^W` is bitwise invariant under the access operator (§5).
- **D8** `π` never touched (§1.2b, V3); no new job package, so no new EUROMOD exposure (V4).
- **D9** Measure references frozen across all eight coalitions (V2).
- **D10** `g_ref` numerically invariant across the four S-10 scenarios, hash-asserted (§8.1).

---

## 11. Unresolved decisions — for Goal 1 Manager ratification

- **R1** Ratify D1 as an amendment to scaffold contract §7 (name-list → cell routing), or reject and instruct an alternative that preserves both access-purity and grand-coalition degeneracy.
- **R2** Ratify the sex-pooling decision (D3) as the frozen conditioning rule for access, notwithstanding its divergence from the type-conditional `Ā`.
- **R3** Ratify the education routing (D4). This is the single most consequential normative choice in the memo for the nested access-vs-ability split.
- **R4** Ratify the region reference form: share-weighted **index** (proposed) vs share-weighted **probability** vs median region; and fix which are sensitivities.
- **R5** Ratify the occupation pooling weights `ω_s(educ3)` as population sex shares within education cell, and whether pooling is within-`educ3` (proposed) or unconditional.
- **R6** **Survey weights.** `dwt` is present in the accepted data but unread in the accepted pipeline. Decide whether every population reference in the operand (region shares, GSUR mean, `ω_s`) is unweighted (consistent with the accepted estimation) or `dwt`-weighted (consistent with population interpretation). This must be frozen before execution; it cannot be decided after seeing the access share.
- **R7** Ratify the V1–V13 check set and fix the numerical tolerances, including the V8 grand-coalition tolerance and the V6 counterfactual ESS threshold and escalation rule.
- **R8** **Resolve or escalate the `W^3` reference/normalisation conflict of §8.3.** Candidate charter §11 halt.
- **R9** Confirm the ability operator's definition is authored consistently with D1/D7 (it is the mirror of this memo and is not specified here) — a separate register item is required.
- **R10** Direct the disposition of §3.4: how the degeneracy of hours-availability heterogeneity under the certified specification is stated in the manuscript caveat block.
- **R11** Confirm the interaction rule for the `W^5` leg: `Ā` held at its ratified type-conditional value across all coalitions while access is pooled, reported as interpretation only (charter §4.3, contract §9 on the `W^1`/`W^5` dual).

---

## 12. Output discipline

- **Mission ID:** JMP-M08; register item U12.
- **Authoritative inputs:** as listed in the front matter (charter; welfare input handoff; scaffold contract v2; W^3 gate report; bookkeeping rules).
- **Decisions made:** D1–D10 (§10), all PROPOSED.
- **Unresolved decisions:** R1–R11 (§11); the §8.3 conflict is a candidate charter §11 halt.
- **Exact output filename:** `docs/Missions/JMP_M08_access_equalisation_operand_design_v1.md`
- **Next authorised action:** Goal 1 Manager review and ratification of D1–D10 and disposition of R1–R11. Nothing in this memo is frozen until ratified; on ratification, D1–D10 and V1–V13 are transcribed verbatim into `docs/missions/JMP_M08_singles_welfare_execution_contract_v1.md` (charter §6) before any welfare number is computed. No implementation, no computation, and no commit is authorised by this memo.

**Statement:** no welfare number, no decomposition number, no parameter value, and no re-estimation is produced or implied by this memo. No file has been written.
