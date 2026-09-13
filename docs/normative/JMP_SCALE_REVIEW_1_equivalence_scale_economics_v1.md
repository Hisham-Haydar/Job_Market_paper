# SCALE-REVIEW-1: economics review of the modified-OECD equivalence scale

Date: 2026-09-12
Mission ID: SCALE-REVIEW-1 (Deputy freeze ruling, Priority A)
Type: conceptual economics review. No computation, no data access, no new
construction. Figures quoted below are read from already-verified memos.

## Authoritative inputs

1. Deputy freeze ruling, "GOAL 1 — SEMINAR ARCHITECTURE FREEZE THROUGH 17
   SEPTEMBER", Priority A and Priority B.
2. `JMP_BASELINE_F1_equivalised_reporting_v1.md` (E3-EQ reporting memo,
   corrected §1/§2).
3. `JMP_BASELINE_F1_equivalised_reporting_verification_v1.md` (independent
   verifier, including the follow-up PASS on corrected couples §2).
4. `JMP_measure_map_v1.md` standing rule: equivalisation applied only to
   welfare outputs, never inside the structural utility or in literal `C_obs`.
5. Project standing constraint: do not conflate preferences with
   responsibility.

Scope boundary observed: this review does not touch `W_EA`, finite-offer
architectures, or the decomposition, all of which are on hold or unauthorised.

---

## 1. Is modified-OECD appropriate for France 2015–2017 EU-SILC/EUROMOD?

**Yes. It is the standard, and it is the standard for precisely this data.**

The OECD-modified (Eurostat) scale

    m_i = 1 + 0.5·(n_adults_14+ − 1) + 0.3·n_children_<14

is the scale Eurostat uses to construct every headline EU-SILC income
distribution statistic (equivalised disposable income, AROP, S80/S20, Gini)
and is what INSEE uses for French income distributions under the name *unités
de consommation*. EUROMOD-based distributional work defaults to it. Using
anything else as primary would make the paper's inequality levels
non-comparable to every published French benchmark, at no offsetting gain.

Live alternatives, and why none displaces it as primary:

| Scale | Form | Status |
|---|---|---|
| Square root | `m = √n` | OECD Income Distribution Database / LIS default. Legitimate, but a cross-country convention, not the EU-SILC one. |
| OECD "original"/Oxford | `1, 0.7, 0.5` | Largely historical; weights children much more heavily. Useful as a robustness bound, not as primary. |
| Per-capita / unequivalised | `m = n` / `m = 1` | Bounding cases, not defensible welfare scales. |
| Behavioural / demand-system scales | Barten, Engel, Rothbarth, Browning–Chiappori–Lewbel indifference scales | Theoretically the "right" object, but **not identified** from demand or labour-supply data without unverifiable restrictions (Pollak–Wales 1979; Blundell–Lewbel 1991 identify only the shape, not the level). Estimating one here would import a second, weaker identification problem into a paper whose selling point is careful identification. |

A referee will not question modified-OECD. A referee may well question a
bespoke scale.

**Verdict on Q1: appropriate. No live alternative displaces it as primary.**

---

## 2. CENTRAL QUESTION — is dividing `W1_F` by `m_i` coherent?

**Yes, within sample, with a precise and defensible interpretation. No, for
cross-sample level comparison between singles and couples.**

### 2.1 Why it is coherent

The concern is that `m` prices economies of scale in *consumption needs*
while `W1_F` is a *leisure-inclusive* money metric. The concern dissolves once
the units of `W1_F` are stated carefully.

`W1_F` solves `U(W1_F, L(o); θ) = U(C_obs, L(j_obs); θ)`. It is not a
leisure-and-consumption composite in mixed units: it is **the consumption
level, evaluated at a single common reference leisure (home), that is
welfare-equivalent to the attained bundle.** Its unit is euros of consumption
at the reference bundle. The leisure information has already been converted
into a consumption number by the time `m` is applied. So `m` is applied to an
object of exactly the units `m` was built to deflate.

The algebra makes this explicit. With

    W1_F_obs = C_obs · ρ_i,    ρ_i = exp{[L(j_obs) − L(o)]/β_c}

equivalisation and the leisure adjustment commute:

    W1_F_obs / m_i = (C_obs / m_i) · ρ_i

`m` never touches `ρ`. The equivalised money metric is exactly *equivalised
consumption, discounted by the household's leisure factor.* This is the same
structure that produces the exact scale-invariance of the worker ratio already
verified in §3 of the E3-EQ memo (max abs diff 2.22e-16); the invariance is
not a numerical coincidence but a direct consequence of the multiplicative
separation.

**Defensible interpretation, to be used verbatim in the paper:**

> `W_F_eq` is the per-adult-equivalent consumption, at a common home-leisure
> reference, that would make the household as well off as it is at its
> attained job-and-consumption bundle.

Within a composition-homogeneous sample this is a well-defined money-metric
well-being index: the reference bundle is common, `ρ` is constructed on a
common scale, and `m` varies only with needs. Inequality in `W_F_eq` within
the singles sample, or within the couples sample, is interpretable.

### 2.2 Where it breaks — and it does break

The mismatch the mission identifies is real, but it is located in
**cross-sample comparison, not in the construction.**

For a couple, `ρ_i` embeds *two* adults' departure from home leisure. If the
leisure index is roughly additive across partners, a two-earner couple carries
something close to a squared leisure discount relative to a comparable single,
while the consumption denominator rises by only ~0.5 per additional adult.
There is no "leisure-needs" normalisation anywhere in the object: the time
endowment doubles, the needs scale does not.

This is visible in the verified numbers and it is not small:

| | Singles | Couples |
|---|---:|---:|
| `C_eq` mean | 1766.49 | 2245.11 |
| `W_F_eq` mean | 1302.07 | 1310.61 |
| Worker-ratio mean `W_F_obs/C_obs` | 0.7332 | 0.6096 |

Couples hold a ~27% advantage in equivalised consumption. That advantage is
almost exactly annihilated in `W_F_eq` (1302 vs 1311, a 0.7% gap) by the
larger leisure discount. **That near-equality is an artifact of the
asymmetric treatment of the two margins, not a finding.**

### 2.3 Consequent restrictions (binding on the seminar deck)

- **Do not** place the singles and couples `W_F_eq` means side by side, and
  **do not** state or imply that singles and couples are similarly well off.
  Priority D deck work must respect this.
- Report the two samples in separate panels, each with its own reference,
  exactly as the freeze ruling already specifies.
- Any statement in *ratio* form (`W_F/C`) is immune to the scale entirely and
  may be stated unconditionally.
- One further caveat for the write-up: a Gini computed on a money metric is a
  descriptive dispersion statistic, not a social-welfare-function-based index
  (money-metric utility need not be concave — Blackorby–Donaldson 1988).
  Describe it as such; do not attach a welfare-loss reading to it.

Two structurally cleaner alternatives exist — normalising the leisure factor
by the adult time endowment, or building an individual-level money metric via
a collective model with a sharing rule. Both are architecture changes. Both
are **October options**, not seminar work, and are named here only so the
reviewer record shows the restriction was chosen rather than overlooked.

---

## 3. Children: needs at 0.3 in the denominator, preference shifter in the numerator

**Not double counting. But the numerator channel is mislabelled if it is
called a preference, and the two channels partly offset.**

The two entries are conceptually distinct objects:

- **Denominator (normative).** Children raise consumption needs. This is a
  fixed household technology parameter imposed from outside the model,
  identical for all households with the same composition, and exogenous to
  choice.
- **Numerator (behavioural).** Children shift the female leisure term, hence
  the chosen job, hence `L(j_obs)`, hence `ρ`. Children affect `W1_F` only
  through the bundle the household actually attains.

Needs and behaviour are different accounting channels, so there is no
double-count. Two things nonetheless require explicit handling.

**(a) The child leisure shifter is not a taste parameter.** In a unitary
discrete-choice labour supply model, the coefficient on children in the female
leisure index is a reduced-form object absorbing time preferences, the price
and rationing of formal childcare, informal care availability, and
home-production technology. Calling it "preference" would contradict the
paper's own central claim — that opportunity-related variation is routinely
misclassified as preference heterogeneity — and would violate the project's
standing rule against conflating preferences with responsibility. The paper
must describe it as a behavioural shifter of unresolved composition.

**(b) The channels offset, which will mislead readers if unflagged.** A
household with children has a *larger* denominator (pushing `W_F_eq` down) and,
insofar as children reduce hours, a *higher* `ρ` (pushing `W_F_eq` up). The
observed child gradient in `W_F_eq` is therefore a net of two opposite forces
and is not a needs gradient.

**Recommended paper wording:**

> Children enter the reported welfare measure through two distinct channels.
> They raise measured consumption needs through the equivalence scale, and
> they shift household labour supply and hence the leisure term of the money
> metric. The second is a behavioural channel which, in a unitary
> specification, absorbs both time preferences and the constraints on formal
> and informal childcare; we do not interpret it as a pure taste parameter,
> and the observed child gradient in equivalised well-being nets the two
> channels against each other.

---

## 4. Is equivalisation NECESSARY?

**Not for internal validity. Yes for the "well-being" framing and for external
comparability.**

Given that singles and couples are reported separately and never pooled, the
usual first-order reason for equivalising — making heterogeneous household
types commensurable — is largely absent. So state the case precisely.

**What it buys**

1. *Comparability.* Every published French and EU inequality figure is
   equivalised. Unequivalised household Ginis are comparable to nothing.
2. *Within-sample composition control, which is not a no-op.* The singles
   sample is not composition-homogeneous: `m_oecd` has mean 1.137 and Gini
   0.099, i.e. a material lone-parent presence. Equivalisation strips out
   dispersion that is pure family size rather than differential well-being.
3. *Conceptual coherence with the paper's object.* The paper claims to measure
   *well-being* inequality. An unadjusted household total is a budget concept,
   not a well-being concept. Reporting only unequivalised aggregates would be
   a weaker match to the stated research question than reporting equivalised
   ones.

**What it risks**

1. *An unidentified normative parameter enters a paper built on identification
   discipline.* The scale is a value judgement, not an estimate (Pollak–Wales).
2. *Direction of effect is not uniform, so the choice is not innocuous.* On
   the verified numbers, equivalisation *raises* measured inequality among
   singles (`C`: 0.2523 → 0.2633) and *lowers* it among couples (0.2310 →
   0.2268). The scale is negatively correlated with resources among singles
   (lone parents) and positively among couples. A single sentence asserting
   "equivalisation reduces measured inequality" would be false in this paper.
3. *Potential interaction with the eventual decomposition.* Composition is
   correlated with both the leisure shifter and, plausibly, the opportunity
   environment. Scale choice can therefore move decomposition shares. This is
   the one genuinely load-bearing risk, and it is not testable until
   decomposition is authorised.
4. *The leisure/needs asymmetry of §2*, mitigated but not eliminated by
   separate reporting.

**Conclusion:** equivalised primary, unequivalised reported alongside as
secondary (as the E3-EQ memo already does), plus the sensitivity set in §6.

---

## 5. Recommendation

**RATIFY modified-OECD as the primary scale, WITH STATED CAVEATS.**

Not unconditional ratification, because of §2.2 and §3; not an alternative
primary, because no alternative dominates on either theoretical or
comparability grounds and the deviation cost is high.

Caveats to be carried in the paper and the deck:

- C1. The scale is a normative convention, not an estimate.
- C2. It is applied only to welfare outputs, never inside the structural
  utility or to literal `C_obs` — per `JMP_measure_map_v1.md`, unchanged.
- C3. `W_F_eq` **levels are not comparable between the singles and couples
  samples** (§2.2). Separate panels only.
- C4. The worker ratio `W_F_obs/C_obs` is exactly scale-invariant and may be
  stated without scale caveats.
- C5. Children enter through two conceptually distinct channels and the child
  leisure term is behavioural, not a taste parameter (§3).
- C6. Money-metric Ginis are descriptive dispersion statistics, not
  welfare-functional indices.

**On the `FINAL_*_PROVISIONAL_PENDING_ECONOMICS_REVIEW` label:** the economics
review is hereby **closed** for both artifacts, subject to C1–C6. The
independent verifier established that `ss9_equivalence_scale_v1.parquet` and
`cw_equivalence_scale_v1.parquet` implement the identical modified-OECD
algebra, re-derive their own `m` to 0.000e+00, and join the BASELINE-F-1
ACCEPTED_FRAMEs with 0/1,540 and 0/2,223 unmatched. The formula and the joined
values are economically ratified.

**One residual item, non-blocking.** The couples artifact is a side-product of
the separate R-242 floor-5 couples pipeline and is built on a 2,275-household
floor-5 roster, whereas the BASELINE-F-1 couples ACCEPTED_FRAME has 2,223
households and carries no roster of its own. Coverage is complete and the join
is clean, so nothing is missing, but the *age composition* underlying `m` for
couples is inherited from a different pipeline's roster reconstruction rather
than from the frame it is applied to. This is a provenance dependency, not a
defect, and does not block Priority B. It should be recorded in the decision
log as an inherited-composition dependency.

---

## 6. SCALE-SENS-1: robustness set and non-load-bearing criterion

### 6.1 Robustness set

**Parametric family** (Buhmann et al. 1988; Coulter–Cowell–Jenkins 1992),
which traces the well-known U-shape of measured inequality in the scale
elasticity:

    m = n^θ,   θ ∈ {0, 0.25, 0.50, 0.75, 1.00},   n = household size in persons

θ = 0 (unequivalised) and θ = 1 (per-capita) are **diagnostic bounds only**,
reported for transparency and excluded from the pass criterion, since neither
is defended by anyone as a welfare scale.

**Named discrete scales:**

| Label | Weights (first adult, further 14+, child <14) |
|---|---|
| Unequivalised | 1, 0, 0 |
| Modified-OECD (baseline) | 1, 0.5, 0.3 |
| OECD original / Oxford | 1, 0.7, 0.5 |
| Square root | `√n` |
| Per-capita | 1, 1, 1 |

**Dedicated child-weight sweep**, holding the further-adult weight at 0.5 and
varying the child weight `c ∈ {0.0, 0.3, 0.5, 0.7}`. This isolates the §3
channel directly — it is the one place where the needs side and the
behavioural side of the model attach to the same household characteristic.

### 6.2 Objects to recompute, singles and couples separately

For each scale: dwt-weighted mean, median and Gini of `C_eq` and `W_F_eq`;
the gap `Gini(C_eq) − Gini(W_F_eq)`; and the within-sample Spearman rank
correlation of `W_F_eq` against its modified-OECD baseline ranking. The worker
ratio is reported once as a fixed point — it does not move, by construction,
and serves as an internal check on the sweep code.

When decomposition is authorised (not now), the opportunity share and the
preference share are added to this list.

### 6.3 Criterion for judging the scale non-load-bearing

The scale choice is **non-load-bearing** if, for each sample separately and
across the interior range θ ∈ [0.25, 0.75] and all named scales except the two
bounds:

- **(i) Sign and ordering invariance.** Every qualitative claim the paper makes
  survives under all scales in the set. The operative example on current
  numbers is `Gini(W_F_eq) < Gini(C_eq)` — true for singles (0.2498 < 0.2633)
  and couples (0.1974 < 0.2268) at baseline, and required to hold throughout.
- **(ii) Rank stability.** Spearman ρ between `W_F_eq` under any alternative
  scale and under modified-OECD is ≥ 0.95 within sample.
- **(iii) Magnitude tolerance.** `Gini(W_F_eq)` moves by no more than ±0.02 in
  absolute terms, and any headline share or percentage statement moves by no
  more than ±5 percentage points.
- **(iv) Decomposition stability** *(applies only once decomposition is
  authorised).* No channel's share moves by more than 5 pp, and the ranking of
  channels by size is unchanged.

**Disposition rules.** If (i)–(iii) all pass, modified-OECD goes in the main
text, the full sweep goes in an appendix table, and one sentence in the text
records that results are insensitive to the scale within the defensible range.
If any of (i)–(iii) fails, the affected statement must be reported as
scale-conditional with its range given in the main text, and no unconditional
version of that statement may appear anywhere in the paper or the deck.

---

## RETURN

**Mission ID:** SCALE-REVIEW-1.

**Authoritative inputs:** the five items listed at the head of this memo.

**Decisions made:**
1. Modified-OECD is appropriate for France 2015–2017 EU-SILC/EUROMOD and is
   ratified as the primary scale, subject to caveats C1–C6 (§5).
2. Dividing `W1_F` by `m` is coherent within sample; the object has the
   interpretation stated in §2.1. Cross-sample `W_F_eq` level comparison
   between singles and couples is **prohibited** (§2.2, caveat C3). The
   observed near-equality of singles and couples `W_F_eq` means is an artifact
   of the leisure/needs asymmetry and must not be presented as a finding.
3. The children double-entry is coherent and not double counting; the child
   leisure term is to be described as behavioural, not as a preference (§3).
4. Equivalisation is not necessary for internal validity but is retained as
   primary for well-being framing and comparability, with unequivalised
   reported alongside (§4).
5. The `FINAL_*_PROVISIONAL_PENDING_ECONOMICS_REVIEW` label is **closed** on
   both scale artifacts (§5).
6. The SCALE-SENS-1 robustness set and non-load-bearing criterion are
   specified in §6.

**Unresolved decisions:**
- Formal Deputy/PI sign-off converting this review into a ratified entry in the
  decision log.
- Inherited-composition dependency: couples `m` derives from the R-242 floor-5
  roster rather than from the BASELINE-F-1 couples frame. Non-blocking; to be
  recorded, not resolved before the seminar.
- Whether SCALE-SENS-1 executes before or after 17 September. Recommendation:
  **after**. It is a sweep over already-verified reporting code, adds nothing
  the seminar needs, and criterion (iv) cannot be evaluated until decomposition
  is authorised.
- Leisure-endowment normalisation of `ρ`, and any individual-level money metric
  via a collective model. **October options**, explicitly not seminar work.

**Exact output filename:**
`Job_Market_paper/docs/results/JMP_SCALE_REVIEW_1_equivalence_scale_economics_v1.md`

**Next authorised action:** Priority B — the equivalised baseline is now
unblocked. The E3-EQ memo and its independent verification already satisfy
Priority B's numeric requirements for both samples; the remaining step is the
fresh cross-check pass the E3-EQ memo itself recommends over its corrected
couples §2 (which the verifier's follow-up section has since supplied with a
PASS), followed by the deck/table update under Priority D, applying caveats
C3, C5 and C6 to the presentation. SCALE-SENS-1 is specified but not
authorised for execution by this memo.
