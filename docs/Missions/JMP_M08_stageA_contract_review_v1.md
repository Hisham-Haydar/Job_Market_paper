# Independent Stage-A Contract Review

**Subject:** `JMP_M08_singles_welfare_execution_contract_v2.md`
**Review level:** economics and decomposition architecture; no software assessment; no contract rewrite.
**Governing amendment:** Deputy Programme Director’s final decomposition-architecture ruling.  

## A1 — DEPUTY-RULING FIDELITY: PASS

The amended architecture implements the deputy ruling correctly.

The contract makes `W2` the primary decomposition measure, `W5` the secondary measure, and confines `W3` to validation, welfare-family comparison, reference recovery, and inversion diagnostics. It expressly prohibits both redefining `W3` and constructing a “common-reference W3.” 

Section 5.2 retains exactly the three-channel game (N={A,B,P}), rejects a fourth endowment/needs operator, and freezes (c_{ij}), tax-benefit inputs, alternative support, (\pi), and measure references across coalitions. 

Sections 5.3–5.5 correctly introduce

[
R_{\mathrm{bg}}^k=I^k({A,B,P}),
\qquad k\in{W2,W5},
]

and the two required accounting identities. They replace the former grand-coalition-zero condition with the five deputy-ordered gates: operator completeness, Shapley arithmetic, total accounting, residual reporting, and no silent renormalisation. 

The primary opportunity share is correctly defined as

[
s_{\mathrm{opp}}
================

\frac{\phi_A^{W2}+\phi_B^{W2}}
{I^{W2}(\varnothing)},
]

and the two-percentage-point S-10 trigger is attached specifically to this quantity. Contributions are reported signed; negative contributions are not suppressed or causally reinterpreted. `R_bg` is explicitly excluded from the labels endowment, needs, circumstance, unfairness, and causal component.  

No correction is required on A1.

---

## A2 — ECONOMIC COHERENCE OF THE OPERATORS: FAIL

The access and ability operators are economically coherent, but the contract contains one material contradiction in the preference operator.

### Finding A2.1 — `R_h` is incorrectly identified as the preference-equalisation operand

Contract §3.1, D7 states:

> “**Preference:** assign a common reference preference (horizontal reference `R^h`, ratified at U13); revalue feasible sets; recompute.”

Contract §3.2, U13 similarly records:

> “Ratified: the named default **`R_h`** … for preference-equalisation.”

But §5A.9.1 establishes a different, ratified decomposition operand:

> “The `θ̄^pref` group-block selection … is ratified as the **singles-female block**. The **singles-male block is the single pre-registered mirror sensitivity**.”

The ability/preference operator memo expressly rejects identifying the two objects:

> “`θ̄^pref` ≠ `R^h`; the two are distinct objects and must not be identified.”

It explains that `R^h` is the **measure-side reference preference for `W5`**, whereas (\bar\theta^{pref}) is the **preference-channel decomposition operand**. Reusing `R^h` in the preference operator would collapse the Exercise-A welfare reference into the Exercise-B decomposition operator, violating the scaffold’s measure/decomposition non-double-interpretation guard.   

### Minimal correction

Amend D7 and U13 so that they state:

* `R_h` is exclusively the measure-side reference preference used in constructing `W5`;
* the preference equalisation operator uses the ratified **singles-female accepted coefficient block**, together with the frozen dwt-weighted taste-covariate references;
* the singles-male block is the mandatory pre-registered mirror sensitivity;
* the preference operator re-evaluates utility on the **fixed alternative support**. It does not “revalue feasible sets” in any way that could imply changing support or measure references.

The remaining operator architecture passes: education is routed through ability on the opportunity side; gender-in-offers is access while gender-in-tastes remains preference; age is split between experience-via-wages and age-in-leisure; the frozen joint occupation table produces the four path-independent conditionals; and the (\delta_{\mathrm{occ}}) interaction is allocated through Shapley symmetry.  

---

## A3 — W2 NON-DEGENERACY: PASS

The contract provides a credible non-degenerate primary welfare object.

`W3` is degenerate because its own-set laissez-faire reference normalizes each household at its own attained laissez-faire position. Consequently,

[
\Omega_i^{W3}\simeq 0
]

is correct by construction.

`W2` uses a different reference: the **best-paid equivalent in the household’s own set**. The money metric is determined by the uniform tax or subsidy that equates attained utility to the best alternative in that own set, with the resulting level anchored to the own-set maximum pay. Nothing in that construction imposes a common zero across households. Variation in own-set wage support, job composition, attained utility, and preferences can therefore generate cross-household variation in (\Omega_i^{W2}). 

The contract also correctly distinguishes a credible ex-ante non-degeneracy argument from an empirical result. Section 7.3 states that Stage D must report (I^{W2}(\varnothing)) before forming Shapley values and that an empirically degenerate `W2` would trigger the deputy’s explicit return condition. This is the correct treatment: non-degeneracy is not fabricated as a result, but neither is there a structural identity forcing degeneracy. 

No correction is required on A3.

---

## A4 — S-10 INTEGRATION: PASS

The S-10 architecture is correctly integrated.

D15 reproduces the exact perturbation rule,

[
\Delta_j
========

\min\left{
0.5,se^{rob}_j,,
0.5(\widehat\theta_j-lb_j)
\right},
\qquad
\theta_j^{sens}=\widehat\theta_j-\Delta_j,
]

and specifies exactly four scenarios: baseline, `beta_l0_sm` only, `beta_w_pexp2` only, and the joint perturbation. No additional search points are permitted.  

Section 5A.10 correctly separates:

* scenario-invariant operand arguments, substitution maps, support, (c_{ij}), (\pi), occupation tables, and measure references, all hash-asserted;
* scenario-dependent equalised values, coalition inequalities, and Shapley contributions, which legitimately change because the perturbed coefficients enter the evaluated ability and preference functions. 

The expected-positive Tier-2 posture is appropriately stated as an anticipation rather than an empirical verdict. Material loading remains a numerical question. The contract keeps both W-4 coordinates visible, retains the two-percentage-point trigger on (s_{\mathrm{opp}}), and monitors `beta_l0_sf` without perturbing it or claiming an unverified bound.  

The exact numerical U10 values still have to be inserted from the digest-bound reporting map at freeze. The contract already treats that as a mechanical pre-execution requirement rather than as a discretionary design choice. It is not an A4 architecture failure.

---

## A5 — INTERNAL CONSISTENCY: FAIL

The principal supersessions and reporting re-anchoring are correct, but four internal inconsistencies remain.

### Finding A5.1 — the channel-membership register is still arithmetically unresolved

Contract §3.1, D5 records:

> “**Preference (20)** … **Ability (6)** … **Access (23)** … counts … **MATCH**.”

Those counts sum to 49, not to the certified 47-coordinate vector.

Contract §5A.8, V12 then acknowledges the contradiction:

> “preference 20 / ability 6 / access 23 = **49 names** against a **47-coordinate** certified vector”

and requires Stage A to halt if an exact partition cannot be established. V7 simultaneously requires:

> “the 47 coordinates form an exact partition … no coordinate in two channels, none omitted.”

Thus D5’s “MATCH” claim and V7/V12 cannot all be true at once. 

### Minimal correction

Replace D5 with the exact P2a-singles factor-by-argument-cell register derived from the frozen 47-coordinate specification. The corrected register must distinguish:

* actual coordinates;
* common anchors;
* pins;
* couples-only coordinates that are inactive for singles;
* coefficients appearing in more than one factor but whose **argument slots** are assigned separately;
* degenerate identity cells.

Then close V12 and confirm V7(a) against the corrected register.

### Finding A5.2 — V20a is not an executable invariant as written

V20a requires:

> “resolved equalised `u` block, taste covariates, and every `g` factor **hash-identical across households**”

while assigning a tolerance of `1e-9`.

This combines two incompatible test concepts:

1. hash identity is exact and does not admit a numerical tolerance;
2. V4 deliberately keeps household-specific alternative support unchanged. Row-evaluated (g)-factor arrays need not be identical across households when wages, hours, occupations, and row order differ, even if all household-specific **arguments assigned to A, B, and P** have been equalised.

The intended economic gate—operator completeness—is valid. The stated mechanical test is not sufficiently defined. 

### Minimal correction

Define V20a over canonical equalisation objects rather than unqualified row-level factors:

* the common substituted argument vector;
* the selected preference block;
* the frozen occupation marginal;
* the factor specifications and coefficients;
* a canonical ordering or common evaluation grid where numerical evaluation is needed.

Use either:

* exact hash identity for serialized canonical operands; or
* a numerical maximum-difference test with tolerance `1e-9`.

Do not attach a numerical tolerance to raw hash equality.

### Finding A5.3 — V6 retains a superseded “redraw remains blocked” failure action

V6 states:

> “If the flagged set widens materially and `V_i^dir` remains blocked, **halt**.”

But U7 and V22 now state that `V_i^dir` is unblocked and mandatory on each coalition’s flagged subset at the frozen 0.5-nat agreement tolerance. V22 supplies the operative rule:

> “The Stage-D `V_i^dir` cross-check … applies to the flagged subsets **of each coalition**.”

The V6 failure action is therefore stale.  

Moreover, the V6 materiality number, V22 per-coalition materiality number, and U6 draw-growth rule remain explicitly unfrozen. The contract correctly blocks execution, but it cannot yet be frozen as an executable contract while these quantities are unresolved. 

### Minimal correction

Replace the stale V6 action with the V22-consistent rule:

* run the mandatory redraw cross-check on the coalition-specific flagged subset;
* apply the frozen 0.5-nat agreement test;
* halt under the ratified flagged-set widening or persistent-disagreement rule.

Before freeze, record the exact V6/V22 materiality numbers and the U6 draw-growth decision, or retain an explicit execution block under a pre-registered escalation rule.

### Finding A5.4 — two mechanical cross-references remain inconsistent

D21 states:

> “Its admissible sources are enumerated verbatim at §5.4.”

The residual source list is in §5.3, not §5.4.

V2 describes “each measure’s reference construction” through the parenthetical:

> “own-set baseline for `W3`, `Ā`, `J`, `o`”

but omits the newly primary `W2` own-set best-paid reference. Later §5A.0 correctly identifies the operative decomposed references as `W2`’s own-set best-paid reference and `W5`’s (\bar A).  

### Minimal correction

* Change the D21 cross-reference from §5.4 to §5.3.
* Expand V2’s parenthetical reference inventory to name the `W2` own-set best-paid reference and the `W5` (\bar A) reference explicitly.

The other A5 elements pass: V8 and V20b are retired; V20c is correctly re-homed as residual-source enumeration; V1/V17/V18 are re-anchored to `W2`/`W5`; the female reference block and mandatory male mirror are stated consistently in §5A; and subgroup reporting is re-anchored from `W3` to `W2`.

---

## A6 — NO INVENTION / NO UNPRODUCED RESULTS: FAIL

Two bounded breaches remain.

### Finding A6.1 — the contract self-adopts an unratified Shapley tolerance

U8 first acknowledges:

> “v1 proposal only; no constant anywhere”

and §3.2a then states:

> “the ruling … states the two arithmetic gates in terms of `ε_Shapley` **without fixing its value; this contract fixes it**”

as

[
\varepsilon_{\mathrm{Shapley}}
==============================

10^{-9}\max{1,\lvert I^k(\varnothing)\rvert}.
]

The rationale is an analogy to the inversion bracket-width tolerance. That is a new design decision. The deputy ruling supplies the symbol (\varepsilon_{\mathrm{Shapley}}), but not this numerical convention. The operator memo’s prior `1e-9` convention concerned analytic operand equality/V20a, not the new Shapley arithmetic gates. 

This conflicts with the charter’s instruction that an absent threshold must trigger a bounded design conflict rather than be invented. 

### Minimal correction

Either:

* cite a written Goal-1 or deputy ratification that expressly fixes
  (\varepsilon_{\mathrm{Shapley}}
  =10^{-9}\max{1,\lvert I^k(\varnothing)\rvert})
  for gates 5.4(2)–5.4(3); or
* return U8 to pending status and keep decomposition execution blocked until the value is ratified.

The contract cannot ratify its own proposed tolerance.

### Finding A6.2 — substantive welfare magnitudes appear despite the no-results discipline

Section 6.5.3 quotes:

> “survey-weighted Ginis: W1 = 0.173, W4 = 0.329, W6 = 0.337; across-measure bracket [0.173, 0.337]”

Yet §9.3 concludes:

> “No computation, no welfare number …”

The figures may come from earlier accepted F5 material, but they are substantive welfare magnitudes, not placeholders, and are unnecessary to establish that `dwt` is the headline weighting convention.  

### Minimal correction

Delete the numerical Ginis and bracket from §6.5.3. Retain only the nonnumerical provenance showing that:

* the accepted welfare-family report uses `dwt`;
* the committed config specifies `weight_col: "dwt"`;
* the committed implementation identifies the primary index as survey-weighted.

No operative couples, pooled-years, LOC4, fourth-channel, policy-reform, or re-estimation content has otherwise entered the authorized M08 execution scope.

---

# Overall verdict

## PASS-WITH-REQUIRED-CORRECTIONS — 4 consolidated corrections

The deputy’s substantive decomposition architecture is accepted. No redesign of the `W2`/`W5` residual-accounting game is required. One documentary correction cycle must implement all four items below:

1. **Correct the preference operand identity.** Remove the D7/U13 identification of `R_h` with preference equalisation; use the ratified singles-female block plus frozen taste-covariate references, with the singles-male mandatory mirror.

2. **Close the internal operator-and-gate register.** Produce the exact 47-coordinate factor-by-argument-cell partition; close V12; correct V2’s reference inventory and D21’s cross-reference; make V20a executable; align V6 with V22; and freeze the U6/V6/V22 rules or maintain an explicit execution block.

3. **Remove the self-ratified Shapley tolerance.** Obtain an explicit authoritative ratification of the proposed (\varepsilon_{\mathrm{Shapley}}) formula or leave U8 pending and block execution.

4. **Remove substantive welfare magnitudes.** Delete the W1/W4/W6 Ginis and numerical bracket from the weighting-provenance section.

After these corrections, the contract still cannot authorize welfare execution until the separately declared **v4 Codex ACCEPT**, exact U10 scenario values, all remaining Stage-A freeze numbers, and the final contract freeze are recorded.
