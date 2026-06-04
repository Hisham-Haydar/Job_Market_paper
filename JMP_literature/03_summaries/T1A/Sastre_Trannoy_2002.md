# Sastre & Trannoy 2002 — Shapley Inequality Decomposition by Factor Components: Some Methodological Issues

> **Filename note.** This file is saved under the path requested
> (`.../T1A/Capeau_et_al_2015_RURO.md`), but the attached source PDF is **Sastre
> & Trannoy (2002)**, not Capeau et al. (2015). The summary below is of the
> actual attached paper. The filename should be corrected to
> `Sastre_Trannoy_2002_Shapley_decomposition.md`; the Capeau RURO paper must be
> summarised separately from its own PDF. Nothing about RURO / latent jobs is in
> this source.

---

## 0. Metadata

- **BibTeX key:** SastreTrannoy2002 [verify exact key against your .bib]
- **Authors:** Mercedes Sastre; Alain Trannoy
- **Year:** 2002
- **Outlet:** *Journal of Economics / Zeitschrift für Nationalökonomie*, Supplement 9, pp. 51–89 (Springer-Verlag)
- **DOI/URL:** [verify — not printed on the supplied scan]
- **PDF filename:** `Sastre_Trannoy_2002_Shapley_inequality_decomposition_by_factor_components.pdf`
- **Tier:** T1A
- **JMP block(s) served:** **decomposition** (primary); secondarily **normative-interpretation** (only via the source-tree/hierarchy discussion) and **data-infrastructure** (income-source taxonomy). It does **not** serve estimation, identification, opportunity-mechanism, or welfare.

---

## 1. One-paragraph relevance to my JMP

This is a methodology paper on the **Shapley decomposition of inequality by factor components** — the exact decomposition family my headline three-way {access, ability, preference} Shapley–Shorrocks split belongs to. It does not touch labour supply, RURO, or welfare; its value is that it documents, on real data, the **pathologies** my decomposition must survive a referee on: the choice between *zero* and *equalised* elimination conventions, the **non-independence of contributions from the level of aggregation/clustering**, and the consequent need for a **nested (hierarchical) Shapley** structure with an economically meaningful tree. Because my three channels are themselves aggregates of finer structural sub-blocks (e.g. access = hours + market/participation + region + year + occupation offers; ability = returns to education + experience + residual dispersion $\sigma$), the paper's central warning — that the contribution assigned to a factor depends on how its siblings are grouped — bears directly on whether my "access share" is well-defined or an artifact of how I bundle sub-channels. It speaks to no single $W^k$; it is measure-agnostic decomposition machinery.

---

## 2. Data and setting

- **Country/years:** United Kingdom (1995 Family Expenditure Survey) and United States (1994 March Current Population Survey), drawn from the Luxembourg Income Study database.
- **Sample unit:** the household; the gross-income distribution is unweighted and not adjusted for family size, as is usual in source-decomposition studies.
- **Sample size:** [verify — not reported in the supplied pages].
- **Key variables:** household income disaggregated by source. The headline three-way partition is earnings (E, ≈72% of household income), capital income (C, 11.4%), and transfers (T, 16.8%). The appendix taxonomy splits these much finer (household-head wages, rest of wages, self-employment, cash property income, private pensions, social retirement, other replacement income, means-tested benefits, other benefits, private transfers, and direct taxes).
- **Budget-set construction:** N/A — this is an accounting decomposition of observed income sources, not a structural or behavioural model. There is no budget set, no choice set, no estimation.
- **Transport to my setting:** The *decomposition technique* transports fully to my France pooled 2015–2017 EUROMOD cross-section; the *data setting* does not and need not (different country, different vintage, pure income-accounting rather than structural welfare). **Features they have / use that I do not rely on here:** nothing they have is missing from my setting in a way that blocks reuse — the method is data-light. The relevant asymmetry runs the other way: my "sources" are **estimated structural channels** of a welfare object, not **observed additive income components**, so the additive-decomposition framing (§7) does not map one-to-one.

---

## 3. Model and objects (map object-by-object to mine)

There is **no structural model, no choice set, no utility, no opportunity mechanism, and no budget map** in this paper. It is an axiomatic/empirical study of a decomposition rule applied to an income matrix $X = [x_i^j]$ over individuals $i$ and sources $j$.

- Their choice set = my latent-jobs set? **N/A** (no choice set).
- Their deterministic utility = my preference utility $v$? **N/A** (no utility).
- Opportunity/availability mechanism analogous to my $g$ (hours / wage-ability / market / occupation)? **N/A** (none).
- Their budget map = my EUROMOD disposable income? **N/A**; their object is observed gross or net income by source.
- **Does any attribute enter both a "utility" and an "opportunity" block?** N/A — there are no such blocks. The analogous concern in *their* framework is whether a source enters two places in the **tree**; that is exactly the aggregation-dependence problem they study (§7 below), and it is the right analogy to flag for my own design, but it is **derived-by-analogy**, not explicit-in-source.

The only object that maps to mine is the **decomposition target**: their inequality index $I$ applied to a sum of components plays the role my Gini (or chosen index) applied to the welfare distribution $\Omega^k$ will play.

---

## 4. Estimation method

**N/A — there is no estimator, likelihood, choice-set sampling, or proposal density.** No starting values, no numerical optimisation, no normalisation. The "method" is the deterministic computation of Shapley factor contributions from an income-source matrix.

**Verdict: not reusable as an estimation method** (there is none). The *decomposition formulas* are reusable and are extracted in §10.

---

## 4b. Proposal / sampling-of-alternatives correction

**N/A.** There is no sampling of alternatives and no proposal/prior correction in this paper. The paper has nothing to say about my importance-sampling welfare integrator or proposal individualisation. (Flagging explicitly so this section is not mistakenly cross-referenced later: the source is silent here.)

---

## 5. Opportunity mechanism

**N/A — there is no opportunity mechanism, no feasibility/availability model, no offer probabilities, no reservation-wage or participation restriction, and no occupation object.** The paper does not model how anything is *available*; it decomposes the inequality of *realised* income by *accounting* source.

**Cost of this omission for my access/ability/preference decomposition:** none directly, because I do not look to this paper for an opportunity mechanism. The indirect lesson is structural, not substantive: the paper shows that even with *fully observed, additive* sources, attributing inequality to a "source" is non-unique once you allow regrouping — so my decomposition cannot inherit well-definedness from the structural model alone; it must additionally fix an elimination convention and a channel hierarchy (§7, §10). **No sector/industry conflation arises** because there is no occupation/sector object at all.

---

## 6. Welfare object — and its place on my $W^1$–$W^6$ map

**The paper computes no welfare object.** It decomposes inequality of **income** (gross and net), not of equivalent income or any preference-respecting money metric. There is:

- no equivalent income, no compensating/equivalent variation, no log-sum/inclusive value;
- no reference price, reference preference, reference bundle, or reference set;
- no discrete-choice subtleties, no ex-ante/ex-post distinction.

**Placement on my $W^1$–$W^6$ family: none.** The source does **not** contain $W^1$–$W^6$ or any Independence-of-$y$ / Independence-of-$A$ stance. Any attempt to locate it on the family map would be fabrication. The only contact point with my welfare layer is downstream: whatever $W^k$ distribution I produce, *this* paper governs how I may decompose its inequality by source/channel.

**Verdict: incompatible as a welfare source; directly usable as the decomposition rule applied to the welfare output.**

---

## 6b. Inclusive value and money-metric inversion

**N/A.** No inclusive value, no log-sum, no EV/CV, no money-metric inversion, no expectation over extreme-value shocks (analytic or simulated). The paper is silent on every item in this section. It cannot inform my analytic-in-shocks importance-sampling inversion.

---

## 7. Inequality / decomposition content  [MOST IMPORTANT for this paper]

This is the substantive core and the reason the paper is T1A for me.

**Inequality index.** Results are presented with the **Gini**; the authors state that results for other inequality indices exhibit the same pattern, so the conclusions do not depend on the choice of index. Note the cardinality caveat: the Shapley decomposition requires agreement not only with the ordinal meaning of an inequality index but also with its cardinal one.

**Decomposition rule.** Shapley factor-component decomposition (Shorrocks-1999 / Chantreuil–Trannoy lineage), plus two hierarchical refinements: **Nested-Shapley** and **Owen**. Each elementary source's contribution is its expected marginal impact on overall inequality averaged over all possible sequences of source elimination.

**Counterfactual construction — the central design choice (what is zeroed vs equalised).** Two conventions for treating sources *not* in the evaluated subset:
- **Zero decomposition:** sources outside the subset are **removed/set to zero**.
- **Equalised decomposition:** inequality from sources outside the subset is **removed by replacing each excluded source with its mean** $\mu(x^j)$, i.e. equalised across individuals.
The treatment of an **equally distributed source** distinguishes them: under the zero rule its contribution is negative (an apparent equalising effect), whereas the equalised rule assigns it exactly zero impact, the latter matching Shorrocks's (1982) reasonable-property requirement.

**Headline empirical finding driving the recommendation.** The **zero rule is highly volatile to the level of aggregation; the equalised rule is far more stable.** Concretely: collapsing earnings+capital into a single "market income" makes the UK transfers contribution jump from 14.2% to 47.2% under the zero approach, while moving only from 4.6% to 5.5% under the equalised approach; finer partitions can even turn the zero-rule transfers contribution **negative**. Therefore the authors favour the equalised approach because zero contributions depend far more on the level of aggregation, a pattern invariant to the index or country.

**Order-independence / exhaustiveness / the key failure.** The Shapley contributions are exhaustive (sum to total inequality) and symmetric. But the rule does not satisfy independence of the aggregation level: a source's contribution depends on how the *other* sources are treated/clustered. This is the property most relevant to me. Two remedies impose a hierarchy:
- **Nested-Shapley** (Chantreuil–Trannoy 1999): a two-stage between/within procedure on an exogenous, economically meaningful partition; it secures the *milder* requirement that a secondary factor's contribution is independent of the disaggregation of *other* primary factors (though still dependent on the treatment of the primary factor it belongs to).
- **Owen** value (Owen 1977): also satisfies the milder requirement, but the authors reject it as a default because it requires coalitions mixing elementary and aggregated sources whose economic meaning is doubtful, making Nested-Shapley more adequate.

**Tree-choice sensitivity.** With a fixed equalised Nested-Shapley rule, the **choice of income tree still matters**: across three economically defensible trees the contributions show moderate volatility, concentrated in the sources treated differently across structures (replacement income, redistributive transfers, property income), while the earnings contributions are barely affected, and the authors conclude it is impossible to escape that the choice of tree has a critical impact on the results. Net-income (post-tax) decompositions are additionally unstable: adding the tax stage can push transfers' contribution negative and market income's above 100%, and perturbs capital's contribution to a negative sign.

**Verdict for my three-way access/ability/preference Shapley–Shorrocks split (anchored on $W^3$/$W^5$/$W^1$):**
**Reusable as the governing methodology, with three concrete imports.**
1. **Adopt the equalised (not zero) elimination convention** for the headline. This is *explicit-in-source* as the more aggregation-robust choice and aligns with the Shorrocks zero-impact-of-an-equal-source property your spec already invokes. [The mapping of "equalise a source" to "equalise a structural channel" — i.e. neutralise the access/ability/preference channel to its population-reference state — is *derived-by-analogy*; your welfare spec's "equalisation" of a channel is conceptually the equalised convention, not the zero convention, and this paper is the citation for *why* that is the right default.]
2. **Treat the three channels as a fixed, economically motivated hierarchy and use Nested-Shapley if you ever report sub-channel contributions** (e.g. splitting access into hours/market/region/year/occupation, or ability into education/experience/$\sigma$). The paper's result is that a flat Shapley over many sub-channels will make your top-level "access share" depend on how finely you cut access — exactly the artifact your project-state already worries about for the couples preference-compression issue.
3. **Report tree/grouping sensitivity as a robustness object, not an afterthought** — the paper's own conclusion is that tree choice is consequential even under the stable rule.

**Two-way vs three-way note.** The paper is **factor-additive and flat-or-nested over income sources**, not organised as a two-way opportunity/preference cut. To reach my three channels I do not "extend" their two-way design (they have no such design); I instantiate their **general** k-factor rule with $k=3$ top-level channels and, optionally, a nested second level. The genuine gap is conceptual, stated in your own spec and *not* resolved here: their sources are **additive components of the target** ($\sum_j x^j = $ income), whereas my channels are **non-additive structural inputs** to a welfare object computed through a nonlinear inclusive value. The Shapley/Shorrocks machinery still applies (Shorrocks 1999 generalises beyond additive factors via the elimination/counterfactual formulation), but **the additive income-source intuition in this paper does not carry over literally**; cite it for the elimination-convention and aggregation-dependence lessons, not for an additive-share interpretation.

---

## 8. Identification and the separation of preferences from opportunities  [STRICT]

**N/A for behavioural identification — there is nothing to identify.** The paper estimates no preferences and no constraints; there is no panel, exclusion restriction, choice-set variation, or external instrument, because there is no behavioural model. It therefore says **nothing** about separating tastes from constraints, or ability from access.

**Honest transport statement:** This paper provides **no identification support** for my preference-vs-opportunity or ability-vs-access separation. That separation rests entirely on my structural model (functional form, the $g$/$v$ split, synthetic-recovery certification) and **not** on this source. The "your decomposition is mechanical" referee is met **only partly** here: this paper helps me defend the *decomposition step* (convention choice, aggregation robustness, exhaustiveness) but it **cannot** defend the *upstream structural separation* — and it is important not to overclaim that it does. The one transferable caution it raises against the mechanical-decomposition charge is endogeneity of the components: the authors quote Gottschalk and Smeeding (1997) that source decompositions can be misinterpreted because they do not distinguish endogenous from exogenous factors, and concede their own sources are not mutually exogenous. For me this is a *warning*, not a *solution*: my channels are model-constructed and interdependent, so the Shapley contributions are descriptive accounting under a fixed convention, not causal shares.

---

## 9. Key results and magnitudes

Benchmarks usable to sanity-check the *stability behaviour* (not the substance) of my own decomposition. UK 1995, Gini, household non-adjusted, three-source partition (E/C/T):
- Equalised Shapley relative contributions: earnings 83.6%, capital 11.8%, transfers 4.6%.
- Zero Shapley relative contributions: earnings 24.9%, capital 60.9%, transfers 14.2%.
The gap between the two conventions for the *same data and partition* is the headline magnitude: it is large, which is the whole point. US 1994 shows the zero rule can even make the earnings contribution negative.
- Aggregation sensitivity (UK transfers): zero rule 14.2% → 47.2% when earnings+capital are merged; equalised rule 4.6% → 5.5% for the same regrouping.
- Tree sensitivity (UK replacement income): −1.8% when treated as factor-linked income vs 3.8% when merged with the rest of transfers; private pension contribution ranges roughly 4.9%–7.6% across trees.

**What this benchmarks for me:** not a plausible opportunity share (different object entirely), but the *expected order of magnitude of convention/grouping-induced movement* — i.e. how much my access share could move purely from how I bundle sub-channels or which elimination rule I pick. The lesson is that **convention choice can move a contribution by tens of percentage points**, so my reported shares must be paired with a fixed, pre-registered convention and a grouping-robustness panel.

---

## 10. Estimators, theorems, or formal results

(Statements transcribed in LaTeX; equation numbers are the paper's.)

**(R1) Shapley value, marginalist form (eq. 2.1):**
$$Sh_i(N,v)=\sum_{S\subseteq N,\, i\in S}\frac{(s-1)!(n-s)!}{n!}\big[v(S)-v(S\setminus\{i\})\big].$$
- *Assumptions:* TU cooperative game; all orderings equally likely.
- *Technique:* expected marginal contribution averaged over all coalition orderings.
- *Reusability:* **yes** — this is the engine your Shapley–Shorrocks split already uses.

**(R2) Zero-income Shapley source contribution (eq. 3.3):**
$$Sh_j(K,X,I)=\sum_{S\subseteq K,\, j\in S}\frac{(s-1)!(k-s)!}{k!}\big[I(y(S))-I(y(S-\{j\}))\big],$$
with $y(S)=\big[\sum_{j\in S}x^j\big]$ (excluded sources removed).
- *Reusability:* **no for the headline** — this is the volatile zero convention the paper recommends against. Useful only as the disfavoured comparator.

**(R3) Equalised-income Shapley source contribution (eq. 3.4):**
$$Sh^e_j(K,X,I)=\sum_{S\subseteq K,\, j\in S}\frac{(s-1)!(k-s)!}{k!}\big[I(y^e(S))-I(y^e(S-\{j\}))\big],$$
with $y^e(S)=\big[\sum_{j\in S}x^j+\sum_{j\notin S}\mu(x^j)\big]$ (excluded sources set to their means).
- *Reusability:* **yes — adopt as the headline convention** (channel held at its population reference rather than zeroed). [The translation from "set excluded source to its mean" to "equalise an excluded structural channel to its reference state" is *derived-by-analogy*; cite R3 for the convention, implement the channel-equalisation in your own welfare/decomposition code.]

**(R4) Nested-Shapley contribution (eqs. 4.2–4.3):** two-stage between/within procedure on a partition $\mathcal P_K$, with the within-stage contribution of elementary source $j$ in aggregate $S_l$ equal to its equalised-Shapley contribution inside $S_l$ plus an equal split of the residual $\frac{1}{s_l}\big[NSh^e_{S_l}-I(y^e(S_l))\big]$.
- *Reusability:* **maybe — adopt only if reporting sub-channel contributions.** It secures independence from the disaggregation of *sibling* aggregates and keeps coalitions economically interpretable. Caveat: contributions remain dependent on the treatment of the *parent* channel, and the authors note Nested-Shapley is **not invariant to adding an initial tree stage** (net-income result).

**(R5) Owen value, equalised (eq. 4.6):** alternative hierarchical value mixing elementary and aggregate coalitions.
- *Reusability:* **no (default)** — rejected by the authors for relying on doubtfully-meaningful mixed coalitions; keep as a robustness comparator at most.

No probabilistic limit theorems, consistency proofs, or standard-error results are stated; the paper is finite-sample/accounting and **does not provide inference**. Your cluster-robust bootstrap on `idorighh` is *your* contribution, not this paper's.

---

## 11. Robustness and specification sensitivity

What they vary and what breaks — directly informs my robustness section:
- **Elimination convention (zero vs equalised):** breaks the zero rule (high aggregation-volatility, sign flips). **Stress-test:** report both; headline on equalised.
- **Level of aggregation / clustering of sibling sources:** breaks flat Shapley (the independence-of-aggregation failure). **Stress-test:** Nested-Shapley + a grouping panel showing your top-level access/ability/preference shares under at least two defensible sub-channel groupings.
- **Choice of hierarchy/tree:** moderate but non-negligible movement, concentrated in the regrouped sources. **Stress-test:** report channel shares under alternative trees (e.g. education-as-access vs education-as-ability — which is already your named ability/access re-allocation robustness).
- **Gross vs net (adding taxes as a stage):** destabilises Nested-Shapley (negative/over-100% contributions). **Relevance to me:** my welfare object is post-tax-benefit by construction (EUROMOD `ils_dispy`); I am not decomposing pre- vs post-tax income, so this specific pathology is less directly threatening — but it is a sharp reminder that **adding a coarse top-level split can destabilise everything below it**, which matters for how I place the singles/couples and year levels in any nested tree.
- **Inequality index:** robust — same patterns across indices (their claim).

**For my effective-sample-size / draw-count concerns:** this paper is silent (no simulation). Those gates come from your welfare-integration spec, not here.

---

## 12. What I can cite this paper for

- The **distinction between zero and equalised elimination conventions** in Shapley factor-component decomposition, and the **empirical case for preferring the equalised convention** on aggregation-robustness grounds.
- The **non-independence of Shapley contributions from the level of aggregation/clustering** of sibling factors — the core motivation for imposing a channel hierarchy.
- **Nested-Shapley** as the preferred hierarchical refinement over **Owen**, on the grounds of economically meaningful coalitions.
- The **sensitivity of decomposition results to the choice of hierarchy/tree**, justifying a tree-robustness panel.
- The **zero-impact-of-an-equally-distributed-source** property (equalised rule) as the principled treatment, linking to Shorrocks (1982).
- The endogeneity caution (Gottschalk–Smeeding) that source decompositions are descriptive, not causal.

---

## 13. What I should NOT cite this paper for  [overclaim risks]

- **Not** a source for any opportunity mechanism, latent-jobs/RURO structure, choice set, proposal correction, or identification of preferences vs constraints — it has none of these.
- **Not** a welfare paper: it computes **no** money-metric/equivalent income and contains **no** $W^1$–$W^6$ family and **no** Independence-of-$y$/Independence-of-$A$ stance. Do not map it onto my measure menu.
- **Not** a two-way opportunity/preference decomposition that I "extend" to three-way; it is a flat/nested **k-factor income-source** decomposition. Frame my three channels as an instantiation of the general rule, not an extension of their cut.
- **Do not transfer the additive income-source interpretation literally** to my non-additive structural channels; the share-equals-source-weight intuition (their §4.1 ratio interpretation) does not hold for a nonlinear welfare object.
- **Not** an inference source — no standard errors, no bootstrap; do not attribute my cluster-robust CIs to it.
- **Sector/industry:** there is no occupation/sector object here, so there is no `loc4`/`lindi` content to (mis)cite; do not invent one.
- **Random vs deterministic opportunities:** the paper is silent; do not enlist it on either side.
- **Theory-paper boundary:** this paper is unrelated to the Haydar–Maniquet axiomatic paper; do not let its "axiomatic properties of decomposition rules" language bleed into claims about the companion characterisation of $W^1$–$W^6$. Trannoy's separate body of social-choice work is **not** this paper.

---

## 14. Direct quotes worth citing

Short verbatim phrases with page numbers (page numbers are the printed journal pages on the scan):

1. p. 54 — the aggregation-level failure: "it does not satisfy the principle of independence of the aggregation level."
2. p. 54 — the two conventions: "zero income decomposition" vs "equalized income inequality decomposition."
3. p. 62 — the empirical verdict: zero contributions are "much more dependent on the level of aggregation than the equalized ones."
4. p. 70 — on Owen: its mixed coalitions "have a doubtful economic meaning."
5. p. 74 — tree choice: "the choice of a tree has a critical impact on the decomposition results."
6. p. 75 — mechanical application "may give odd results."

[All quotes kept under 15 words; verify exact wording/page against the PDF before pasting into the draft.]

---

## 15. Open questions and risks for my draft

- **Convention pre-registration.** I must fix the elimination convention (equalised) *before* reporting numbers, or invite the charge that I chose the convention that flattered the access share. This paper is the citation that makes equalised the defensible default — use it pre-emptively.
- **Channel hierarchy is a design decision, not a neutral one.** If I ever disaggregate access or ability, my top-level shares move with the grouping. I need a declared tree and a Nested-Shapley implementation, plus a robustness panel — otherwise the access share is not well-defined. This intersects directly with the project-state worry that pinned couples-preference parameters mechanically compress the couples preference component and inflate the couples opportunity share; the paper supplies the general reason that aggregation/treatment choices distort shares.
- **Additivity gap unresolved.** The paper's clean additive-source setting does not match my nonlinear welfare object; I must verify (in my own decomposition memo) that the Shorrocks elimination formulation — not the additive-share intuition — is what I am invoking, and state the exhaustiveness gate ($\sum$ components $= I(\Omega^k)$) as my own check, since the paper guarantees exhaustiveness only for its additive construction.
- **Descriptive, not causal.** The endogeneity caution means my shares are accounting under a convention; I should not phrase them as causal opportunity effects. Keep the normative reading (compensation-relevance) tied to the welfare measure stance, not to the decomposition arithmetic.
- **Inference is mine to supply.** No SEs here; my per-component cluster-robust bootstrap CIs (tight for opportunity, wide for preference, per the project state) are an addition this literature does not cover.

---

## 16. TL;DR for retrieval

Sastre & Trannoy (2002) is the **decomposition-methodology** anchor (no RURO, no welfare, no opportunity mechanism): it establishes the **equalised** elimination convention as more aggregation-robust than the **zero** convention, documents that flat Shapley contributions **depend on how sibling factors are clustered**, and recommends **Nested-Shapley over Owen** with a declared economic tree. For my JMP it governs the **decomposition step only** — convention choice, channel-hierarchy robustness, and the exhaustiveness/aggregation-dependence caveats around my three-way {access, ability, preference} Shapley–Shorrocks split — and explicitly does **not** inform any single $W^k$, the opportunity mechanism, or the preference-vs-opportunity identification.
