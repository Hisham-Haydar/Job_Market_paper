All source files read. Producing the memo in chat as instructed.

---

# JMP_M08_measure_definition_binding_memo_v1.md

**Mission:** JMP-M08 (Singles Welfare Execution — measure-definition binding)
**Status:** PROPOSED-PENDING-RATIFICATION
**Author role:** Paper-and-empirical-design workstream (advisory; no computation, no code, no welfare number produced)
**Target path:** `docs/Missions/JMP_M08_measure_definition_binding_memo_v1.md`
**Date:** 2026-08-07

**Theory/JMP boundary statement.** The four `.tex` files examined (`Main__1_.tex`, `one_file.tex`, `Model.tex`, `Measures.tex`) constitute the separate Haydar–Maniquet theory paper *"Jobs and Well-Being Measurement"* (Main__1_.tex:91–92). This memo extracts **definitions and reference constructions only**, as cited primitives. Axioms, theorems, and characterization results are **noted by existence and location only**; no proof content is transcribed as JMP material, and nothing herein merges the theory paper into the JMP. The theory paper is a **working draft** (multiple "To be proven" annotations, e.g. Measures.tex:13, 37); all source ambiguities are flagged to the PI in §6, never resolved by invention.

**Authoritative inputs (this memo):**

| Input | Role |
|---|---|
| `one_file.tex` (971 lines; contains Model, Axioms, Measures, Results) | primary definitional source (line citations below refer to it unless prefixed) |
| `Measures.tex` (standalone Measures section) | cross-check copy; one divergence from `one_file.tex` found (§6, O-7) |
| `Model.tex`, `Main__1_.tex` | model primitives; document structure |
| `JMP_M08_singles_welfare_execution_contract_v3.md` (D2 at :454–467; D19 at :447; §3.2a U2/U11/U13 at :723–953; V2 at :1822) | contract side of the fidelity map |
| `RURO_welfare_scaffold_design_contract_v2.md` §3.1–3.4 (:140–241), §6 (:395–424) | scaffold measure/reference schema |
| `JMP_M08_final_E2_literature_and_decomposition_architecture_ruling_v1.md` §3 | deputy role assignments checked in §3 |

---

## 1. Definition extraction (W1–W6)

**Model primitives** (one_file.tex:104–115 / Model.tex:3–12): universal job set 𝒥 fixed; pre-tax income function **y**: 𝒥 → ℝ₊; consumption set Z = ℝ₊ × 𝒥, bundle z = (c, j); preferences R ∈ ℛ monotonic in consumption; ability set A ⊆ 𝒥; well-being measure W(z, R, A; **y**), with the convention z = (c, j) for some j ∈ A whenever W is measured (one_file.tex:114). Standing domain assumptions in the results section: R continuous and monotonic; 𝒥 finite (one_file.tex:375–378).

All six measures share the schema *"W(z,R,A;**y**) = w ⟺ z I max_R{B}"* — an indifference construction between the actual bundle and the own-preference optimum over a measure-specific counterfactual budget B — differing only in how B is built. This matches the scaffold's "declared reference + own-preference inversion" architecture exactly (scaffold §3.2:186–193).

### W1 — Equal-Pay measure (own set, pay ignored)

Defining passage, one_file.tex:258–267 (≡ Measures.tex:3–12):

> "We restrict our attention to the individual's ability set, without looking at the pre-tax incomes associated to these jobs, and we look at the preferred job and its corresponding consumption level that leaves the individual indifferent to their current bundle."
> W(z,R,A;**y**) = w ⟺ z I max_R{B}, where z′ = (c′,j′) ∈ B ⟺ j′ ∈ A and c′ = w.

- **Reference object:** own ability set A under a flat consumption level w at every job.
- **Money-metric anchor:** the flat pay level w itself.
- Results-section name: "The Equal-Pay measure W¹" (one_file.tex:546). Characterization exists (Thm at :548–552, via Responsibility For Equal Pay + Independence of **y**) — noted by existence only.

### W2 — Best-Paid-Equivalent measure (own set, uniform tax/subsidy)

Defining passage, one_file.tex:270–285 (≡ Measures.tex:15–30):

> "…we look at the preferred job in this set to which the individual is indifferent to their current bundle, where 'preferred job' means that the tax (or subsidy) that would leave them indifferent is minimal, and we apply this tax (or subsidy) to all the jobs in the ability set to identify the 'best-paid equivalent' job, the pay of which is the well-being of the individual."
> W(z,R,A;**y**) = w ⟺ z I max_R{B}, where ∃ t ∈ ℝ such that z′=(c′,j′) ∈ B ⟺ j′ ∈ A and c′ = **y**(j′) − t, and w = max_{j∈A} **y**(j) − t.

- **Reference object:** own ability set A under a **uniform tax/subsidy t applied to pre-tax incomes** on A.
- **Money-metric anchor:** the post-t pay of the **best-paid job in the own set**: w = max_{j∈A} **y**(j) − t. **This is the "own-set best-paid-equivalent reference" the charter delegates to Stage A: it is fully pinned down by (i) the household's own A, (ii) the pre-tax pay vector **y** restricted to A, and (iii) the indifference-determined uniform t.**
- Non-degeneracy anchor: "In particular, if z = argmax_A R, then W(z,R,A;**y**) = max_{j∈A}**y**(j)" (one_file.tex:285) — at the own optimum, W2 equals the own-set top pay, which varies across households.
- The associated reference preference **R^c** appears in the Measure-2 prose (one_file.tex:287–291): z=(c;j) R^c z′=(c′,j′) ⟺ c ≥ c′. Textually **identical in content to R^h** (§6, O-2). Characterization exists (Thm :616–620, via Full Responsibility + Compensation for the Horizontal Reference Preference R^h) — existence only.

### W3 — Laisser-Faire measure (own set, uniform subsidy)

Defining passage, one_file.tex:294–304 (≡ Measures.tex:39–49):

> "All individuals have the same well-being at laisser-faire. Otherwise, compute the amount of tax t that leaves the individual indifferent between their current bundle and maximizing over their ability set and paying t (better to write it as a subsidy I guess)."
> W(z,R,A;**y**) = w ⟺ z I max_R{B}, where z′=(c′,j′) ∈ B ⟺ j′ ∈ A and c′ = **y**(j′) + w.

- **Reference object:** own set A under a uniform additive shift w to pre-tax incomes.
- **Money-metric anchor:** the shift w. Normalisation "laissez-faire value = shift" is demoted in the results section to a **cardinal scale convention** (Lemma "Laissez-faire value; scale convention", one_file.tex:726–736: κ(w) = w is a choice of scale, conclusion stated ordinally). Existence and uniqueness of the shift is a lemma (:670–675).
- Degeneracy at baseline: at the own laissez-faire optimum, w = 0 for every individual — the theory-side fact underlying the deputy's §3.1 ruling.

### W4 — Staying-Home Equivalent measure

Defining passage, one_file.tex:306–311 (≡ Measures.tex:51–56):

> "Assume there is a 'job', say o, consisting of staying home, with **y**(o)=0, such that everybody has it in their ability set: for all A ∈ 𝒜, o ∈ A. … W(z,R,A;**y**) = w ⟺ z I (w, o)."

- **Reference object:** the **non-employment option o**, with two structural premises: **y**(o) = 0 (zero pre-tax pay) and **universal membership** o ∈ A for every A.
- **Money-metric anchor:** the consumption level w making the individual indifferent between z and staying home at w.

### W5 — Reference-Ability LF measure (uniform subsidy on Ā)

Defining passage, one_file.tex:314–331 (≡ Measures.tex:59–77):

> "We fix a reference ability set Ā ⊆ 𝒥. … compute the amount of subsidy that, when added uniformly to all jobs in the reference ability set, makes the individual indifferent between their current bundle and the best job they would choose in that subsidized reference set."
> W(z,R,A;**y**) = w ⟺ z I max_R{B}, where z′=(c′,j′) ∈ B ⟺ j′ ∈ **Ā** and c′ = **y**(j′) + w.

- **Reference object:** the **common reference set Ā** (not the own A) under a uniform additive shift w.
- **Money-metric anchor:** w, normalised so "if z = argmax_(Ā,**y**) R, then W = 0" (one_file.tex:331) — the inversion-sanity zero the scaffold gate already uses (scaffold :414–416).
- Sign domain: the shift ranges over ℝ, "covering the tax case w < 0" (one_file.tex:876–877) — the empirical bracket must admit negative w.
- Special case Ā = 𝒥 discussed at :332; characterizations exist for general Ā (:896–903) and Ā = 𝒥 (:950–956) — existence only.

### W6 — Equal-pay over the universal set ("Min-of-Equal-Pay")

Defining passage, one_file.tex:335 (≡ Measures.tex:80):

> "We compute the consumption level that would leave an individual indifferent between their actual bundle and getting this consumption level with their preferred job over all existing jobs. If there exists w ∈ ℝ₊ such that z I argmax_(𝒥, **y**^w) R and z′ I′ argmax_(𝒥, **y**^w) R′ then W(z,R,A;**y**) = W(z′,R′,A′;**y**′)."

- **Reference object:** the **universal set 𝒥** under the **equal-pay profile** **y**^w(j) = w for all j ∈ 𝒥 (profile made explicit in the results section, one_file.tex:813).
- **Money-metric anchor:** the flat level w at which the individual's preferred job over 𝒥 (at flat pay) is indifferent to z. Note the Measures-section statement is a **solidarity implication rather than an explicit function definition** — the direct formula W6(z,R,A;**y**) = that w is implicit (§6, O-5). Results-section name: "The Min-of-Equal-Pay measure W⁶" (:797).

### Reference preferences in the source

- **R^h (horizontal reference preference)** — defining passage, one_file.tex:180–184: "the reference class 𝓡̃ is the singleton containing the *horizontal* reference preference R^h ∈ ℛ, defined by z=(c,j) R^h z′=(c′,j′) ⟺ c ≥ c′, that is, the preference that ranks bundles purely by consumption, ignoring job identity."
- **R^c** — Measure-2 prose only (one_file.tex:287–291), defined by the **identical condition** c ≥ c′.

### Property matrix

Reproduced at Measures.tex:84–101 and one_file.tex:339–354 (existence noted; two internal source issues flagged at §6, O-6/O-7). Rows relevant to §3 below: Full Responsibility (+ for W2, W3 only); Ind. of A (+ for W4, W5, W6); Full Compensation (+ for W4, W6); Resp. Ref. Abilities (+ for W5 only).

---

## 2. Fidelity map (theory source vs. contract D2/D19 and scaffold §3.2–3.4)

The scaffold table (scaffold :199–206) and contract D2 (contract :454–463) are declared identical (D2 source column, :430); both were checked independently against the source.

| Measure | Contract D2 / scaffold gloss | Verdict | Notes |
|---|---|---|---|
| W1 | "preferred job in own set A, pay ignored"; scaffold adds "(consumption c′=w at the preferred feasible job)"; Ind-y +, Ind-A − | **MATCH** | Gloss and formula match :258–267 and the matrix rows exactly. |
| **W2** | "best-paid equivalent in own set A"; scaffold "(uniform tax/subsidy t; w = max_{j∈A} y(j) − t)"; Ind-y −, Ind-A − | **MATCH on the formula; CONTRACT-UNDERSPECIFIED on the income-concept translation** — headline, see below | Scaffold formula is verbatim-faithful to :270–284. |
| W3 | "laissez-faire in own set A, with pay"; scaffold "(c′ = y(j′) + w)"; Ind-y −, Ind-A − | **MATCH** | Same translation note as W2, but validation-only, so not a headline. |
| W4 | "staying-home equivalent (non-employment o, y(o)=0)"; Ind-y +, Ind-A + | **MATCH** | U2's predicate resolution (`working == 0`, lowest draw; contract :723–753) is consistent with **y**(o)=0 read as zero *pre-tax pay* — non-employment carries zero earnings while its disposable income c_{i,o} is positive, which the theory permits. One theory premise needs an empirical assertion (§5, W4). |
| **W5** | "uniform subsidy to reference set Ā"; scaffold "(j′ ∈ Ā, c′ = y(j′) + w)"; Ind-y −, Ind-A + | **MATCH on the formula; CONTRACT-UNDERSPECIFIED shared with W2 (translation)**; the concrete Ā is a charter-delegated binding, correctly supplied by U11, not a divergence | Normalisation W5 = 0 at the reference optimum matches the scaffold's inversion-sanity gate verbatim (scaffold :414–416 vs. :331). |
| W6 | "best job in whole economy J"; scaffold "(preferred job over J under y^w)"; Ind-y +, Ind-A + | **MATCH, with a low-consequence gloss caution** | The scaffold's parenthetical is faithful. D2's short gloss "best job in whole economy" could be misread as *best-paid* job in 𝒥; the source object is the **preferred job over 𝒥 at flat pay y^w** (:335, :813), and the results section names it "Min-of-Equal-Pay" (:797). No Shapley requirement on W6, so no material consequence; recommend the manuscript use the equal-pay-over-𝒥 wording. |

### Headline finding (W2/W5, the decomposition measures): the pre-tax-side vs. consumption-side translation is not bound

The theory defines the W2/W3/W5 counterfactual budgets by uniform shifts applied to **pre-tax incomes y(j′)** (":c′ = **y**(j′) − t" at :278; "c′ = **y**(j′) + w" at :302, :328), with W2's anchor max_{j∈A}**y**(j) also a **pre-tax** object. The empirical pipeline evaluates own utility over **EUROMOD disposable-income bundles c_ij** (scaffold §3.2, §6.1(iii):402–412), and Stage One's accepted W3 inversion applies the shift inside the own-utility inversion Φ_i(·) — operationally a **consumption-side** shift. Under a nonlinear tax-benefit mapping, a uniform pre-tax shift and a uniform disposable-income shift are **not the same object**: a pre-tax-faithful implementation would require targeted EUROMOD evaluation of shifted-**y** packages; a consumption-side implementation is a lump-sum equivalent-income construction. Neither D2, the scaffold §3.2 table, nor §3.2a resolves which side the shift binds on for W2's t and W5's w, nor which pay concept anchors W2's max_{j∈A}**y**(j) (gross pay at the alternative vs. disposable c_ij). **Because W2 is the primary and W5 the secondary decomposition measure, this is the memo's named headline binding gap.** This memo supplies no resolution (that would be design invention outside its mandate); it is enumerated for ratification at §6, O-1, with the implementability consequences at §5.

---

## 3. Role coherence against the theory paper's property matrix

Checked against the deputy ruling §3.1–§3.2 role assignments. Coherence noted only; the deputy's choices are not re-argued.

- **W2 as the non-degenerate Full-Responsibility primary — COHERENT.** Matrix: Full Responsibility "+" for W2. Characterization by Full Responsibility + Compensation for R^h exists (:616–620). Non-degeneracy is theory-supported: at the own optimum W2 = max_{j∈A}**y**(j) (:285), which varies with A and **y**(A) across households.
- **W3 as the laissez-faire/full-responsibility validation endpoint — COHERENT.** Matrix: Full Responsibility "+"; characterization via Full Responsibility + Independence of Irrelevant Jobs exists (:748–753). The deputy's degeneracy premise (baseline Ω³ ≃ 0 for every household) is exactly the theory's laissez-faire normalisation: at the own no-tax optimum the unique shift is w = 0 (:670–675 existence/uniqueness; :726–736 scale convention). W3's reference-recovery role matches the scaffold inversion-sanity gate.
- **W5 as the access-compensated dual under R^h — COHERENT, with one source flag.** Matrix: Ind. of A "+", Resp. Ref. Abilities "+" — the compensate-the-set / responsible-for-pay dual reading. The "under R^h" clause reads correctly against the source: both W5 characterizations use *Compensation for the Horizontal Reference Preference R^h* as an axiom (:898–901, :952–954). **Flag (coherence-relevant, not role-changing):** the property matrix itself records "Comp. for R^h" as "−" for W5 (one_file.tex:345), which is in apparent tension with R^h appearing in W5's own characterization. This is a draft-internal source issue for the PI (§6, O-6), not an incoherence in the deputy's assignment.
- One additional coherence note: as defined in the source, **R^h does not enter the computation of the W5 number** — Measure 5's B is built from Ā and **y**+w, and the max is taken under the household's *own* R (:314–329). R^h enters W5's *axiomatic characterization* only. The contract's treatment of R_h as a frozen, hash-invariant *citation-side* reference object (V2(e), :1822) is therefore harmless and correct; it is not a computational input. Recorded so no implementer looks for an R^h evaluation step.

---

## 4. R^h binding to be frozen at U13

**Exact definition, quoted with source:** one_file.tex:180–184 —

> z = (c, j) R^h z′ = (c′, j′) ⟺ c ≥ c′

"the preference that ranks bundles purely by consumption, ignoring job identity."

**Binding scope (restating U13 as corrected at v3 A2.1, contract :907–953):** R^h is frozen as the **W5 measure-side reference preference only** — the Exercise-A citation object under which W5 is axiomatically characterized. It is **never** the preference-equalisation operand; that operand is the ratified singles-female accepted coefficient block θ̄^pref plus the frozen dwt-weighted taste-covariate references (§5A.6, §5A.9.1, R-72 S2), with the singles-male block as the mandatory V23 mirror. Per the ratified R-72 language, θ̄^pref ≠ R^h and the two must not be identified. Per §3 above, R^h has no computational role in producing the W5 number; the U13 freeze binds the cited normative object and the V2(e) hash-invariance of its declaration.

**Source caveat for the freeze record:** the theory draft also defines **R^c** (Measure-2 prose, :287–291) by the *identical* condition c ≥ c′. The freeze should name **R^h** by the :180–184 passage (where the axiom "Compensation for the Horizontal Reference Preference" is anchored) and record the R^c/R^h naming redundancy as a source item (§6, O-2), so a later theory-paper revision renaming one of them cannot silently break the citation.

---

## 5. Implementability notes (per definition; flags only, no design)

Common to all six: each measure is a one-dimensional monotone bracketing inversion of the own-utility map at the declared reference (scaffold §3.2), on the frozen alternative support with c_ij, π, and references coalition-invariant (V2/V3/V4).

- **W1** — needs: own-set enumeration (the household's own 101-alternative support) and evaluation of own utility at flat consumption w across that support. Pure consumption-side; **no new EUROMOD exposure**. Note: "pay ignored" means the counterfactual consumption is w at every job — no pay vector needed.
- **W2 (primary)** — needs: (i) own-set enumeration; (ii) **the pay object anchoring max_{j∈A}y(j)** — as written this is *pre-tax* pay at the alternative level, so the pipeline must either carry a gross-pay column on the frozen engine-ready support or the anchor must be re-bound (O-1); (iii) monotone solve in t with the anchor computed from the same frozen pay object; (iv) a domain rule for c′ = **y**(j′) − t < 0 given Z = ℝ₊ × 𝒥 (O-3). **Flag:** a pre-tax-faithful uniform-t implementation requires targeted EUROMOD evaluation of shifted-y packages, which the accepted artifacts do not supply and Gate 4/D12 does not currently authorize for own-set packages — flagged, not designed around.
- **W3 (validation)** — Stage One machinery exists and passed (D9/D11/D12); the shift-side question (O-1) applies but its validation role is unaffected in mechanics.
- **W4** — needs: the o-predicate row per household (`working == 0`, lowest draw; U2) and the inversion against (w, o). **Required empirical assertion (theory premise):** o ∈ A for *every* household, i.e. `home_count ≥ 1` for all rows — checkable from the existing predicate machinery; a household with no working==0 alternative violates the theory premise and must block, not be approximated.
- **W5 (secondary)** — needs: construction of Ā = `type_conditional_median_opportunity` by shared code (U11); c_ij for every reference package of Ā finite and positive before evaluation (Gate 4/D12 — targeted EUROMOD evaluation is the *authorized* channel here, scaffold :402–412); a bracket admitting **negative w** (:876–877); inversion-sanity zero at the reference optimum (:331). The O-1 shift-side question applies to Ā's uniform subsidy identically.
- **W6** — needs: J = pooled support of offered job types (scaffold §3.4) and own-utility evaluation at flat pay w over **all of J**, including job types outside the household's own drawn support. Pay is replaced by w, so no EUROMOD exposure; but utility evaluation at non-own job types requires the model's non-pecuniary components to be well-defined there — flag for the implementation review, since the accepted artifacts evaluate utility on own supports.

---

## 6. Open items for Goal-1 ratification

1. **O-1 (headline; blocks W2/W5 freeze):** bind the shift side and income concept for the uniform t/w constructions — pre-tax-faithful (requires new targeted EUROMOD exposure; currently unauthorized for own-set packages) versus consumption-side equivalent-income (Stage-One W3 precedent; departs from the literal theory formula under a nonlinear tax-benefit map) — and, for W2, the pay object anchoring max_{j∈A}y(j). PI decision plus a contract amendment; whichever is chosen must be recorded as the JMP's stated operationalisation of the cited primitive.
2. **O-2 (source):** R^c (:287–291) and R^h (:180–184) are defined by the identical condition; flag the naming redundancy to the PI. The U13 freeze should cite R^h at :180–184.
3. **O-3 (source + implementation):** W2's counterfactual consumption c′ = y(j′) − t can be negative while Z = ℝ₊ × 𝒥; the source does not state the domain restriction. Flag; do not invent a truncation rule.
4. **O-4 (source):** W2's prose says the indifference-tax is "minimal" (:270), while the formal statement only asserts existence of t; uniqueness is proven for W3's shift (:670–675) but not restated for W2. Flag for the PI to confirm the intended existence/uniqueness claim.
5. **O-5 (source):** W6 is stated as a solidarity implication, not an explicit function (:335); the direct definition (the w solving z I argmax_(𝒥,y^w)R) is implicit. Flag for an explicit restatement in the theory draft before manuscript citation.
6. **O-6 (source, coherence-relevant):** property-matrix entry "Comp. for R^h" = "−" for W5 (:345) sits in apparent tension with R^h appearing as an axiom in both W5 characterizations (:898–901, :952–954). Also, W2's "Comp. for Ref. Pref." = "−" (:346) versus the Measure-2 prose claim that W2 satisfies Compensation for Reference Preferences with R^c (:287) — presumably the row quantifies over a different reference class, but the source does not say. Flag both to the PI.
7. **O-7 (source, file divergence):** the "Resp. Ref. Abilities" matrix entry for W3 is "?" in Measures.tex:100 but "−" in one_file.tex:353. The two copies are otherwise aligned; identify which is current before any matrix content is cited.
8. **O-8 (empirical assertion):** ratify the W4 premise check `home_count ≥ 1` for all households as a blocking assertion (§5, W4).
9. **O-9 (manuscript wording):** adopt the "preferred job over 𝒥 at equal pay" wording for W6 in paper text rather than D2's "best job in whole economy" gloss (§2).

---

**Output discipline block.**
**Mission ID:** JMP-M08.
**Authoritative inputs:** as tabled above.
**Decisions made:** none — this memo binds nothing; it is PROPOSED-PENDING-RATIFICATION and supplies extractions, the fidelity map, coherence notes, the U13 R^h citation text, and the open-item register.
**Unresolved decisions:** O-1 through O-9 (O-1 is the headline and blocks the W2/W5 measure freeze).
**Exact output filename:** `JMP_M08_measure_definition_binding_memo_v1.md` (target `docs/Missions/`).
**Next authorized action:** Goal-1 Manager ratification pass over §6 (O-1 first), then incorporation of the ratified bindings into the execution contract per the deputy ruling §4 amendment discipline. No computation, code, or welfare execution is authorized by this memo.