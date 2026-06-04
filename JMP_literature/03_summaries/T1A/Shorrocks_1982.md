# Shorrocks 1982 — Inequality Decomposition by Factor Components

## 0. Metadata
- **BibTeX key (suggested):** `shorrocks1982decomposition`
- **Author:** A. F. Shorrocks (London School of Economics; Queen's University)
- **Year:** 1982
- **Outlet:** *Econometrica*, Vol. 50, No. 1 (January 1982), pp. 193–211
- **URL:** JSTOR stable URL `https://www.jstor.org/stable/1912537` (explicit on PDF). DOI `10.2307/1912537` [verify — not printed on PDF]
- **PDF filename:** `Shorrocks_1982_Inequality_Decomposition_by_Factor_Components.pdf`
- **Tier:** T1A
- **JMP block(s) served:** **decomposition** (primary); **normative-interpretation** (the two "contribution" readings of §5, which formalise the counterfactual-neutralisation idea); **motivation** (foundational citation for additive factor decomposition). It does **not** serve estimation, identification, welfare, or opportunity-mechanism (access/ability) — the paper contains no choice model, no welfare object, and no opportunity structure.

## 1. One-paragraph relevance to my JMP
This is the foundational reference for **additive decomposition of an inequality index into the contributions of distinct components**, and it supplies the axiomatic backbone for the claim that a decomposition can be made *unique* and *index-independent*. It speaks to **Exercise B (the source decomposition)** rather than to any single channel: it is about *how* to allocate inequality to components, not about *which* components (access / ability / preference) are the right ones. Its central cautionary result — that without the right symmetry axioms the proportional contribution of a component can be driven to *any* value in $(-\infty,\infty)$ (the three-person example, eq. 30) — is precisely the "your decomposition is mechanical / arbitrary" referee threat my §8 must pre-empt, and it is the reason my decomposition must be pinned by exhaustiveness/order-independence axioms (Shapley–Shorrocks) rather than by a "natural" formula. **Crucial boundary:** the rule Shorrocks derives (cov$(Y^k,Y)/\sigma^2(Y)$) applies to **additive income sources** $Y=\sum_k Y^k$; my access/ability/preference channels are **not** additive money components but counterfactual neutralisations of structural blocks, so the cov-rule does **not** transport directly — the Shapley-value machinery (Shorrocks 2013) is the correct tool, and this 1982 paper is the additive special case / conceptual ancestor.

## 2. Data and setting
**N/A — no data, no empirical application, no country/year.** This is a purely methodological/theoretical paper in the theory of inequality measurement. Populations appear only as abstract income vectors $Y=(Y_1,\dots,Y_n)$ and as illustrative hypotheticals (notably a three-person population in the eq. 30 example). Income "sources" are abstract factor components $Y^k$ (the running examples named are earnings, investment income, and transfer payments). There is **no** budget-set construction, **no** microdata, **no** panel, **no** instrument, **no** vacancy/offer data. Nothing here transports as *setting* to my France pooled 2015–2017 EUROMOD cross-section; what transports is the **decomposition theory**, which is setting-free.

## 3. Model and objects (map object-by-object to mine)
There is **no structural/behavioural model** to map — no choice set, no deterministic utility $v$, no opportunity density $g$, no budget map. The single object is a partition of total income into factor components and an inequality index $I(Y)$.
- **Their factor components $Y^k$** vs **my channels:** their $Y^k$ are *additive* sub-vectors summing to total income, $Y=\sum_k Y^k$ (the decomposition is defined for "disjoint and exhaustive components of income," explicit-in-source, §3). My {access, ability, preference} are **not** additive income sub-vectors; they are structural blocks of the model whose effect on welfare inequality is isolated by *equalisation/neutralisation counterfactuals*, not by summing money pieces. **This is the single most important object-level mismatch** and the basis for several boundary flags below.
- **Their total $Y$** vs **my welfare vector $\Omega^k$:** their decomposed aggregate is the *income* distribution; my decomposed aggregate is a *money-metric equivalent-income* distribution $\Omega^k$ computed from attained utility $V_i$. Shorrocks's aggregate is observed income; mine is a constructed welfare object — so even the thing being decomposed differs in kind.
- **Opportunity / availability mechanism:** none. (Detailed in §5 below.)
- **Budget map = my EUROMOD disposable income?** No budget map at all.
- **Job attribute entering BOTH utility and opportunity?** N/A — no utility and no opportunity object exist here, so the double-counting flag does not arise. The analogue concern in *this* paper is whether components are disjoint and exhaustive (they are required to be).

## 4. Estimation method
**N/A.** No likelihood, no estimator, no choice-set construction, no numerical optimisation, no starting values. The paper derives decomposition *rules* (closed-form allocations of an index to components), not estimates. **Verdict: not reusable as an estimation method** (there is none); reusable only as the *decomposition* layer (see §7, §10).

## 4b. Proposal / sampling-of-alternatives correction
**N/A.** No alternatives are sampled; no proposal density; no $\log(\text{prior})$ correction. The paper has no choice-theoretic content whatsoever. Nothing here bears on my importance-sampling welfare integrator or my proposal-individualisation concern.

## 5. Opportunity mechanism  [MOST IMPORTANT — here: explicitly absent]
**There is no opportunity mechanism, by construction.** The paper takes the *realised* distributions of factor incomes $\{Y^k\}$ as given primitives and asks only how to allocate the inequality of their sum. There is no feasibility, no availability, no offer probability, no reservation wage, no participation restriction, and no dependence on circumstances (region, education, demographic type, local labour market).
- **access:** not modelled.
- **ability:** not modelled.
- **occupation as availability:** not modelled; no occupation object, hence **no risk of occupation/industry conflation** in this source.

Shorrocks himself flags the cost of this omission in his own terms (§5, concluding remarks, explicit-in-source): factor decomposition examines each component *separately* and **neglects feedback effects** on other sources (his example: a tax decomposition identifies the contribution of taxes to post-tax inequality but ignores taxes' effect on the *pre-tax* distribution). He states that evaluating such indirect effects would require specifying behavioural relationships, which factor decompositions deliberately avoid — and he calls this "both the strength and weakness" of the approach.

**What this omission costs my access/ability/preference decomposition (derived-by-analogy):** because Shorrocks's rule is purely statistical and behaviour-free, applying an *additive-component* logic to my channels would silently assume the channels are non-interacting additive money pieces with no general-equilibrium/behavioural feedback. My channels are behaviourally entangled (neutralising access changes attained utility and hence the chosen bundle, which is exactly a "feedback effect" Shorrocks excludes). This is the formal reason my decomposition needs the Shapley counterfactual construction (which handles interactions by symmetric averaging over orderings) rather than the 1982 covariance rule.

## 6. Welfare object — and its place on my $W^1$–$W^6$ map
**The paper computes no welfare object.** No money-metric, no equivalent income, no compensating/equivalent variation, no log-sum/inclusive value. It operates entirely on income distributions and inequality indices. There is **no** reference price, reference preference, reference bundle, or reference set, and no ex-ante/ex-post distinction (there is no choice and no uncertainty).

**Place on my $W^1$–$W^6$ map: none — do not claim this source contains $W^1$–$W^6$ or any Independence-of-$\mathbf{y}$ / Independence-of-$A$ stance.** It is index-and-component theory upstream of the welfare object. The one genuine point of contact is conceptual and lives in §5: Shorrocks's two interpretations of "the contribution of factor $k$" (below, §7) formalise the *neutralisation counterfactual* that my decomposition uses to isolate a channel — but this is a decomposition-construction idea, not a welfare measure. **Verdict: incompatible as a welfare object; usable only at the decomposition layer.**

## 6b. Inclusive value and money-metric inversion
**N/A.** No inclusive value, no log-sum, no EV/CV, no money-metric inversion, no expectation over shocks (analytic or simulated). The paper has no discrete-choice or random-utility content.

## 7. Inequality / decomposition content  [CORE OF THIS PAPER]
This is the section the paper exists for. All of the following is **explicit-in-source**.

**Indices covered.** Variance $\sigma^2$; squared coefficient of variation $I_2$; Gini $G$; the Generalized Entropy family $I_c$ (eq. 19), including Theil $I_1$ and $I_0$; and — via the weak-consistency extension of §4 — the Atkinson family.

**Decomposition family and the "natural" rule.** For additive components $Y=\sum_k Y^k$, the *natural* decomposition assigns to factor $k$ its own variance plus **half** of every interaction (covariance) term involving it, giving the contribution
$$ S_k^*(\sigma^2) \;=\; \mathrm{cov}(Y^k,\,Y), \qquad s_k^*(\sigma^2)=\frac{\mathrm{cov}(Y^k,Y)}{\sigma^2(Y)} $$
(eqs. 3–4). The same proportional contributions arise for $I_2$ (eqs. 6–7); a separate "natural" rule (the pseudo-Gini, eqs. 10–11) is given for the Gini and a pseudo-Theil for $I_1$ (eqs. 20–21).

**The non-uniqueness warning (the load-bearing result for my defence).** Theorem 1 (eqs. 13–14) shows that any index written in the quasi-separable weighted-sum form $I(Y)=\sum_i a_i(Y)Y_i$ admits a contribution $S(Y^k,Y)=\sum_i a_i(Y)Y_i^k$ — but the weights $a_i(Y)$ are **not unique**. Corollary 1 (eq. 27) characterises the *entire family* of admissible rules via arbitrary functions $\lambda_j(Y)$, and eq. 28 shows the proportional contributions can be made to match those of *any other* index. The three-person illustration (eq. 30) is the punchline: by choosing $\lambda_1$ freely, the proportional contribution of a factor "can be made to give any value between plus and minus infinity" — i.e. an unaxiomatised decomposition is empirically meaningless.

**The uniqueness theorem.** Adding **Assumption 6 (Two-Factor Symmetry)** to Assumptions 1–5 yields **Theorem 3 (eq. 31): a unique rule for every inequality index**,
$$ s_k(I)\;=\;\frac{S(Y^k,Y)}{I(Y)}\;=\;\frac{\mathrm{cov}(Y^k,Y)}{\sigma^2(Y)} \quad\text{for all } Y\neq\mu e, $$
with two consequences stated explicitly: (i) the decomposition rule is unique, and (ii) the *proportional* contributions are **independent of the inequality index chosen** (they coincide with the natural decomposition of the variance / $I_2$).

**Weakly consistent decompositions (§4).** Replacing additive consistency (Assumption 4) with a weaker aggregator condition (Assumption 4′) and invoking Aczél's theorem gives Theorem 4: there is a monotonic transform $f$ (unique up to scale) such that transformed contributions sum to the transformed index. This extends the framework to indices that are monotonic transforms of the quasi-separable form, **including the Atkinson family** ($f(y)=(1-y)^{1-\varepsilon}$). Under a non-additive aggregator the *proportional* contributions need no longer sum to one or be index-invariant.

**Counterfactual construction (the two interpretations, §5 — directly relevant to my channel neutralisation).** Shorrocks formalises "the contribution of factor $k$" two ways:
- **(A) "pure" contribution** — inequality if factor $k$ were the *only* source of differences: $C_k^A = I\!\big(Y^k+(\mu-\mu_k)e\big)$ (eq. 39): hold $Y^k$, give everyone the *mean* of every other source.
- **(B) "eliminated" contribution** — the fall in inequality if factor $k$ differences were *removed*: $C_k^B = I(Y) - I\!\big(Y-Y^k+\mu_k e\big)$ (eq. 40): replace each $Y_i^k$ by its mean.

For the variance, the unique rule sits exactly between them: $S(Y^k,Y)=\mathrm{cov}(Y^k,Y)=\tfrac12(C_k^A+C_k^B)$. **(A) zeroes out all other sources; (B) zeroes out the target source** — and (B) is the formal sibling of my "equalise this channel and read the inequality fall" counterfactual. Shorrocks notes (A) ignores interactions while (B) loads *all* of factor $k$'s interactions onto $k$, and that in general neither $C^A$ nor $C^B$ alone yields a *consistent* (summing) decomposition except when components are uncorrelated.

**Verdict for my three-way Shapley–Shorrocks split (anchored on $W^3$/$W^5$/$W^1$).** **Reusable as foundational principle, not as formula.** Three transfers, one non-transfer:
1. **Transfers:** the *consistency/exhaustiveness* requirement (Assumption 4) and the *index-independence* property (Theorem 3) are exactly the disciplines I want — they justify (a) requiring my Shapley components to sum to $I(\Omega^k)$ and (b) reporting across Gini/Theil/Atkinson without re-qualifying every number.
2. **Transfer:** interpretation (B) (eq. 40) is the additive-world version of my channel-equalisation counterfactual.
3. **Transfer (as warning):** the eq. 30 $(-\infty,\infty)$ result is the citation that *motivates* axiomatic pinning of any decomposition.
4. **Does NOT transfer:** the closed-form rule $\mathrm{cov}(Y^k,Y)/\sigma^2(Y)$ itself, because (i) my channels are **not** additive income components, and (ii) the asymmetry between (A) and (B) when components interact is exactly what the **Shapley average over all orderings** resolves — which is the 2013 development, **not** present in this 1982 paper.

**This paper is a $K$-factor additive (income-source) decomposition.** It is neither a two-way opportunity/preference split nor a three-way access/ability/preference split, and it is **not** a Shapley-value paper. Extending it to my three channels requires (a) reconceiving the "components" as structural-block neutralisations and (b) replacing the half-the-covariance interaction split with the Shapley symmetric-orderings average.

## 8. Identification and the separation of preferences from opportunities  [STRICT]
**N/A in the structural-econometric sense** — there is no estimation, no tastes-vs-constraints identification problem, and nothing here addresses separating *ability* from *access*. The paper's "identification" is purely about *which allocation rule* is pinned down by which axioms, an algebraic question.

**Why it nonetheless belongs in my identification/defence note (derived-by-analogy, state as such):** the eq. 30 result is the cleanest existing statement that a decomposition with too few axioms is *not identified as a number* — its proportional contribution ranges over the whole real line. This is the formal precedent I cite when a referee charges that the access/ability/preference split is "mechanical" or "arbitrary": the answer is that the split is pinned by exhaustiveness + order-independence (Shapley–Shorrocks), exactly the kind of axiomatic discipline Shorrocks (1982) shows is *necessary* to obtain a unique, interpretable decomposition. **It does not, however, solve my structural identification** (preferences vs opportunities, or ability vs access) — that must come from functional form, the certified synthetic-recovery argument, and the opportunity-density structure, none of which this paper touches. Do not let this citation be read as identifying the *channels*; it only disciplines the *allocation* once channels are defined.

## 9. Key results and magnitudes
No empirical magnitudes (no data). The "results" are the theorems. The one quantitative illustration worth carrying is the **three-person example (eq. 30)**: with the Gini and a freely chosen $\lambda_1$, the proportional factor contribution spans the entire interval $(-\infty,\infty)$ — a qualitative "magnitude" that benchmarks *how badly* an unaxiomatised decomposition can behave, not any substantive share. Nothing here benchmarks the plausible size of my own opportunity share or welfare spread.

## 10. Estimators, theorems, or formal results
- **Theorem 1 (eqs. 13–14).** *Statement:* Assumptions 2–4 imply $S(Y^k,Y)=a(Y)\!\cdot\!Y^k=\sum_i a_i(Y)Y_i^k$ with $I(Y)=a(Y)\!\cdot\!Y$. *Assumptions:* continuity + symmetric treatment of factors (A2), independence of level of disaggregation (A3), consistent (additive) decomposition (A4). *Technique:* the additivity of A4 forces a Cauchy functional equation in the contribution map; its solution (Aczél) is linear, i.e. a weighted sum of factor incomes. *Reusability:* **yes, as principle** — gives the quasi-separable contribution form and motivates the exhaustiveness requirement; not a formula I apply to non-additive channels.
- **Corollary 1 (eq. 27) + eq. 28.** *Statement:* the admissible decomposition rules form a large family indexed by arbitrary continuous $\lambda_j(Y)$; proportional contributions under one index can be reproduced under any other. *Technique:* characterise the solution space of the single linear restriction (14) via a basis of the homogeneous system (22)–(23). *Reusability:* **yes, as the non-uniqueness warning** (the motivation for axiomatic pinning).
- **Theorem 2 (eqs. 29).** *Statement:* population symmetry and the equal-factor normalisation (Assumption 5) constrain but do **not** uniquely pin the rule. *Reusability:* maybe — supports the claim that "reasonable but weak" axioms are insufficient; secondary.
- **Theorem 3 (eq. 31).** *Statement:* Assumptions 1–6 imply the **unique, index-independent** rule $s_k(I)=\mathrm{cov}(Y^k,Y)/\sigma^2(Y)$. *Assumptions:* A1–A5 plus **Two-Factor Symmetry (A6)**. *Technique:* A6 plus a permutation-matrix construction kills all free $\lambda_j$. *Reusability:* **yes, as principle** (index-independence justifies my across-index robustness reporting); **no, as formula** (covariance rule needs additive components).
- **Theorem 4 (eqs. 35–38).** *Statement:* under weak consistency (Assumption 4′) there is a monotonic $f$, unique up to scale, with transformed contributions summing to the transformed index; covers the Atkinson family. *Technique:* associativity of the aggregator $F$ + Aczél's representation theorem. *Reusability:* **maybe** — relevant if I want to decompose an index (Atkinson) that is only a monotonic transform of a quasi-separable form; note proportional shares then lose index-invariance and additive summing.

## 11. Robustness and specification sensitivity
What the paper itself "stress-tests" is the **axiom set**: it shows step-by-step how adding axioms (A4 → A5 → A6, then the weakening A4 → A4′) changes the admissible decomposition family from "the whole real line" to "unique." Two takeaways for my robustness section:
- **Index choice:** Theorem 3 says the *proportional* contributions are index-independent under A1–A6 — direct support for reporting my decomposition across **Gini / Theil / Atkinson** without expecting the *shares* to move for index-choice reasons alone (any movement I see is then attributable to the decomposition rule or the welfare measure, not the index). This is a useful internal consistency check.
- **Aggregation rule:** §4 warns that under a non-additive aggregator (e.g. multiplicative, $f=\log$), proportional shares need not sum to one — so if I ever decompose a non-additively-aggregable index I must report this explicitly. For my purposes the additive/exhaustive route (Shapley) is the safer default.
There is nothing here on choice-set size, number of draws, multistart, or opportunity-set definitions — those concerns are foreign to this paper.

## 12. What I can cite this paper for
- The **foundational principles of factor decomposition**: continuity, symmetric treatment of factors, independence of the level of disaggregation, and **consistency/exhaustiveness** (contributions sum to total inequality) — Assumptions 1–4.
- That a decomposition lacking sufficient symmetry axioms is **not pinned down** — the proportional contribution can take *any* value (eq. 30, three-person example). The motivation-for-axiomatics citation.
- That, with two-factor symmetry added, there is a **unique decomposition rule whose proportional contributions are independent of the inequality index** (Theorem 3, eq. 31) — support for cross-index robustness reporting.
- The **two formal readings of "a factor's contribution"** (the "only source" reading (A), eq. 39; the "eliminate the differences" reading (B), eq. 40) — the additive-world formalisation of channel-neutralisation counterfactuals.
- The honest statement that factor decompositions **neglect behavioural feedback between components** (§5, tax-incidence example) — useful when I caveat that my channel neutralisations are *accounting* counterfactuals, not general-equilibrium ones.
- The **weak-consistency extension to the Atkinson family** (Theorem 4), if I decompose an Atkinson index.

## 13. What I should NOT cite this paper for  [overclaim risks]
- **NOT a Shapley-value decomposition.** This 1982 paper is the *additive factor-component* rule (half-the-covariance interaction split); the Shapley-value / symmetric-orderings construction is **Shorrocks (2013)** (and the cooperative-game lineage), **not** here. Cite 2013 for the Shapley average, not 1982.
- **NOT a two-way *or* three-way opportunity/preference decomposition.** It decomposes by **additive income sources**, not by access / ability / preference. Do **not** describe its components as "opportunity vs preference."
- **NO welfare object.** It contains no money-metric, equivalent income, EV/CV, or inclusive value; do not present its $S(Y^k,Y)$ as a decomposition of *welfare* — my object is the inequality of $\Omega^k$, not of income.
- **Do NOT claim it contains $W^1$–$W^6$** or any Independence-of-$\mathbf{y}$ / Independence-of-$A$ stance — it has no responsibility/compensation content of any kind.
- **NO opportunity / access / occupation content**, hence no occupation-vs-industry issue arises; do not import any "sectoral"/availability language from it.
- **NO random-opportunity framing** (and none to "correct"); it is silent on opportunities entirely. Consistent with my deterministic-opportunities stance, but it makes no claim either way.
- The **cov$(Y^k,Y)/\sigma^2(Y)$ formula does not apply to my channels** — they are not additive money components. Citing the *formula* (rather than the *principle*) for a structural-block decomposition would be a misuse.
- **Theory-paper boundary:** this is an empirical-JMP citation for decomposition method; it has no bearing on, and must not be conflated with, the Haydar–Maniquet axiomatic welfare-characterisation paper. Shorrocks's axioms are *inequality-decomposition* axioms, not the companion paper's *welfare-measure* axioms.

## 14. Direct quotes worth citing
To respect source copyright I keep verbatim quotation minimal and give precise locations so exact wording can be pulled from the PDF when drafting:
- On the central non-uniqueness danger, the three-person example concludes that a factor's proportional contribution can be made to take <em>any</em> value between plus and minus infinity (**p. 202, around eq. 30**) — the single most quotable line for the "decomposition needs axioms" point.
- On feedback effects being excluded, and this being "both the strength and weakness" of factor decomposition (**p. 210, final paragraph of §5**) — paraphrase or short exact pull when caveating accounting-vs-behavioural counterfactuals.
- On the index-independence payoff: that with Assumptions 1–6 no qualification by choice of index is needed (**p. 205, after Theorem 3**).
- Interpretations (A) and (B) of a factor's contribution (**p. 209, eqs. 39–40**) — cite by equation, no prose quote needed.

(*Verbatim strings deliberately not reproduced here; copy exact wording from the cited pages of the PDF for the manuscript.*)

## 15. Open questions and risks for my draft
- **Additivity is the hidden assumption.** Everything in this paper rests on $Y=\sum_k Y^k$. My channels are not additive money pieces, so I must be explicit in the draft that I borrow Shorrocks's *principles* (exhaustiveness, index-independence) while replacing his *construction* with the Shapley average — and cite 2013 for the latter. The risk is a referee conflating the two; pre-empt by stating the distinction once, clearly.
- **Interaction handling.** Shorrocks's (A)/(B) asymmetry under correlated components is exactly the path-dependence the Shapley average is designed to remove. My §8 should make the link: the eq. 30 indeterminacy and the (A)≠(B) gap are *the same problem*, and order-independence is the resolution. This strengthens the "not mechanical" defence.
- **Feedback / general equilibrium.** Shorrocks's own caveat (behavioural feedback ignored) applies to my channel neutralisations: equalising access changes attained utility and the chosen bundle. I should state that my decomposition is a *structural-accounting* counterfactual at the estimated $\hat\theta$, not a GE counterfactual, and that this is a deliberate, standard scope limit (citing Shorrocks's framing of strength-and-weakness).
- **Index choice for the headline.** Theorem 3's index-independence holds for *additive* components; under my non-additive Shapley split the index-invariance is not guaranteed by this theorem. I should *check empirically* that shares are stable across Gini/Theil/Atkinson rather than *assert* it from Shorrocks 1982 — and report the check.

## 16. TL;DR for retrieval
Foundational additive **factor-component** inequality decomposition: with continuity, symmetric factor treatment, disaggregation-independence, consistency, and **two-factor symmetry**, every inequality index has the **unique, index-independent** contribution rule $\mathrm{cov}(Y^k,Y)/\sigma^2(Y)$ (Theorem 3, eq. 31); without enough axioms the proportional contribution is **indeterminate** over $(-\infty,\infty)$ (eq. 30). Serves my **decomposition** block as the *principle* layer (exhaustiveness + index-independence + the (A)/(B) neutralisation readings, eqs. 39–40), **not** as a usable formula — my access/ability/preference channels are non-additive, so the Shapley-average construction (Shorrocks 2013) is required, and this paper carries **no welfare object, no opportunity mechanism, and no $W^1$–$W^6$ content**.
