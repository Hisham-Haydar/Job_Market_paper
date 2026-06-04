# Aaberge & Colombino 2006 â€” Designing Optimal Taxes with a Microeconometric Model of Household Labour Supply

> **Extraction note (read first).**
> - **Source of truth:** the attached PDF, Statistics Norway *Discussion Papers* No. 475 (Sept. 2006). All section/equation/table references below are to that document; **no page numbers are cited** (the source is referenced by its own section/eq/table numbering, which is explicit in text).
> - **Template used:** `JMP_T2_focused_extraction_prompt_v2.md`. The exhaustive `JMP_T1_exhaustive_extraction_prompt_v2.md` was **not attached**, so I could not "use it exactly." I have populated the full T2 skeleton (sections 0,1,2,5,6,7,8,9,12,13,16) at T1A depth. The T1-only sections (3,4,10,11,14,15) are listed at the end as `[T1-only â€” rerun with the real T1 prompt]`, with pointers to the source material that would fill them, so the rerun is cheap.
> - **Filename correction:** requested as `Aaberge_et_al_2009.md`; the attached PDF is **Aaberge & Colombino (2006), DP475**, not the 2009 Wennemo choice-set paper (which already has a file in the project). Saved as `Aaberge_Colombino_2006.md`. Intended repo path: `JMP_literature/03_summaries/T1A/Aaberge_Colombino_2006.md`.
> - **Vocabulary:** I use **access / ability / preference** in my own analysis; where I report what the *source* does I use its own two-factor language (*preferences / opportunities*) and its own Roemerian *Equality-of-Outcome / Equality-of-Opportunity* (EO/EOp) language, flagging the obsolete framing.
> - **W-namespace warning, stated up front:** this paper contains a family it calls $W_1, W_2, W_3, W_\infty$ â€” these are **rank-dependent social welfare functions** (single-series Ginis: $W_1$ Bonferroni, $W_2$ Gini, $W_\infty$ utilitarian), an *inequality-aggregation* family. They are **not** the JMP's $W^1$â€“$W^6$ equivalent-income measure family. The paper does **not** contain the JMP's $W^1$â€“$W^6$. See Â§6 and Â§13.

---

## 0. Metadata

- **Suggested BibTeX key:** `aaberge_colombino_2006_optimaltaxes`
- **Authors:** Rolf Aaberge (Statistics Norway, Research Dept.); Ugo Colombino (Dipartimento di Economia, Torino).
- **Year / outlet:** 2006, Statistics Norway *Discussion Papers* No. 475, Research Department, Oslo (working paper / discussion paper).
- **Handle (explicit in source):** `https://hdl.handle.net/10419/192457` (EconStor). No DOI in source.
- **Likely journal version:** Aaberge & Colombino, *Scandinavian Journal of Economics* (â‰ˆ2013), "Using a microeconometric model of household labour supply to design optimal income taxes." **[verify â€” not in source; do not cite a DOI without checking]**
- **PDF filename:** `Aaberge_Colombino_2006_Designing_Optimal_Taxes_with_a_Microeconometric_Model_of_Household_Labour_Supply.pdf`
- **Tier:** T1A.
- **JMP blocks served:** estimation (the RURO/latent-jobs estimator lineage); opportunity-mechanism (the offered-hours / offered-wage / sector opportunity densities â†’ maps onto access vs ability); welfare (a common, opportunity-aware individual welfare function â€” a *precedent*, not the JMP's equivalent income); decomposition / normative-interpretation (Roemer EO vs EOp, a *different* opportunity construct); motivation.
- **JEL (source):** H21, H31, J22.

---

## 1. One-paragraph relevance to my JMP

This is a direct ancestor of the JMP's structural layer: it is the Aabergeâ€“Colombinoâ€“StrÃ¸m (1999) RURO/latent-jobs estimator â€” choice over *jobs* (packages of hours $h$, wage $w$, and sector $s$), with utility weighted by an estimated **opportunity density** $p(h,w,s)$ â€” applied here to Norwegian singles and couples with 78 parameters. Its opportunity density is **already factorised** into an offered-**wage** sub-density (lognormal in own education and experience â†’ my **ability** channel, the Independence-of-$\mathbf{y}$ dimension) and offered-**hours** plus **sector** plus **market-vs-non-market** sub-densities (â†’ my **access** channel, the Independence-of-$A$ dimension), which makes it a clean citation that the access/ability split is *operational* inside the offer mechanism, not an invention of the JMP. It also runs a welfare layer (a *common*, opportunity-aware individual welfare function) and an opportunity-sensitive normative criterion (Roemer EOp), but **both differ in kind from the JMP's objects** â€” the welfare object is a common-utility comparability device rather than a preference-respecting equivalent income, and "opportunity" in its EOp criterion means **family-background circumstances**, not the feasible-job-set content the JMP attributes. So it anchors my *estimator* and my *opportunity-mechanism* sections strongly, my *welfare* and *decomposition* sections only as contrast.

---

## 2. Data, setting, and model in brief

- **Country / data:** Norway; the 1995 Survey of Level of Living, income year 1994. **[verify â€” internal inconsistency in source: the abstract says "1994," the conclusions and Appendix say "1995"; most consistent reading is survey 1995 / tax rule and incomes 1994].**
- **Unit:** decision unit is the household â€” single females, single males, and married/cohabiting **couples making joint labour-supply decisions** (the couple is the joint unit, as in my baseline).
- **Age window:** estimation restricted to ages **18â€“54** (to exclude retirement, per Appendix A); the welfare-function estimation and the optimal-tax simulation use ages **20â€“62** (Table 4.1, Â§6). **[verify â€” the 18â€“54 vs 20â€“62 mismatch is in the source as written].**
- **Core model:** a discrete-choice random-utility labour-supply model, "an extension of the standard multinomial logit," in the Aabergeâ€“Dagsvikâ€“StrÃ¸m / Aabergeâ€“Colombinoâ€“StrÃ¸m (1999) tradition (explicit in Â§2 fn 3). Agents choose among **jobs** characterised by $(w,h,j)$, not merely among hours; for a given agent wages may differ job to job. Behaviour is a comparison of *utility levels* across a continuum/large set of latent jobs, with an estimated density of opportunities. Estimated by simultaneous maximum likelihood across the three groups.
- **Feature I do not have:** the EOp layer uses **father's years of schooling** as a circumstance/type variable (3 types). My French pooled EUROMOD cross-section has no comparable parental-background circumstance, so the paper's *EOp* exercise does not transport even though its *estimator* does. (Conversely, the paper has no occupation/ISCO offer layer; its only "sector" variable is public-vs-private â€” see Â§5.)

---

## 5. Opportunity mechanism

**Explicit in source.** The set $B$ of opportunities available to a household includes non-market opportunities (a "job" with $w=0,h=0$). Because the analyst does not observe $B$, it is represented by a density $p(h,w,j)$ of job *types*, interpreted as the relative frequency/availability of jobs of type $(h,w,j)$ in the choice set (Â§2, eq (2.4) and its discussion). The choice density (eq (2.4)) is the systematic utility $v$ **weighted by availability** $p$, normalised over the feasible set â€” i.e. "relative attractiveness weighted by availability," which is structurally the JMP's `u + log g âˆ’ log Ï€` integrand with $p$ playing the role of the offer density $g$.

The opportunity density is specified (Appendix A, eq (A3)) for singles as
$$
p(h,w,s) \;=\;
\begin{cases}
p_0\, g_{1s}(h)\, g_{2s}(w)\, g_3(s), & h>0,\\[2pt]
1-p_0, & h=0,
\end{cases}
$$
with $p_0$ the proportion of **market** opportunities, and the three conditional densities:

- $g_{1s}(h)$ â€” **offered hours** density (eq (A7)): uniform over hours except multiplicative peaks at **part-time (18â€“20 weekly hours)** and **full-time (37â€“40)**, parameters $\pi$ varying by gender.
- $g_{2s}(w)$ â€” **offered wage** density (eq (A9)): **lognormal**, $\log w = \beta_0 + \beta_1\,\mathrm{Exp} + \beta_2\,\mathrm{Exp}^2 + \beta_3\,\mathrm{Ed} + \sigma\eta$, $\eta\sim N(0,1)$, with experience $\mathrm{Exp}=\text{age}-\text{schooling}-5$; parameters vary by gender **and by sector**.
- $g_3(s)$ â€” **sector** density (eq (A8)): public vs private, parameters $\mu$ by gender.

For couples the same architecture is specified jointly over $(h_M,h_F,w_M,w_F,s_M,s_F)$ with separate market/non-market proportions $p_0^M,p_0^F$ (eqs (A10)â€“(A19)).

**Mapping to access / ability (derived-by-analogy; the source uses two-factor "preferences/opportunities" and does not name access/ability).**
- $g_2$ (offered-wage technology in own education/experience and residual $\sigma$) $\to$ **ability** â€” exactly the Independence-of-$\mathbf{y}$ / pay dimension of the JMP cut.
- $g_1$ (offered hours), $g_3$ (sector), and $p_0$ (market vs non-market) $\to$ **access** â€” the Independence-of-$A$ / feasible-set dimension.
- Systematic utility $v$ $\to$ **preference**.

So the AC opportunity density is *already* split into one pay sub-density and several feasibility sub-densities; the JMP's three-way structural-to-normative map (preference $=v$; ability+access $=g$, cut $g$ in two) is the *same partition*, re-labelled and re-purposed for a welfare decomposition rather than for tax simulation.

**Boundary flag â€” "sector" here is public/private, not ISCO and not NACE.** The paper's $s$ is a **public-vs-private employment-sector** dummy. It is **neither** the JMP's occupation offer layer (`loc4`/ISCO, which I treat as *access*) **nor** the reserved industry variable (`lindi`/NACE). Do not cite this paper's "sector" as occupation or as industry. In JMP vocabulary a public/private offered-job split is best read as a further *access* sub-block.

---

## 6. Welfare object

**What the paper computes (explicit in source, Â§4).** Because estimated preferences are heterogeneous and the sample mixes singles and couples, the paper confronts interpersonal comparability and resolves it with a **common individual welfare function** $V$ (eq (4.1)): all individuals are treated as singles, $V$ is allowed to vary with age and number of children, and couples' disposable income is divided by $\sqrt{2}$ for scale economies, with each partner assigned the resulting income (eq (4.2)). Crucially, $V$ is **estimated with the same opportunity-weighted density** (eq (2.4) with $v$ replaced by $V$), inserting the previously estimated offered-hours and offered-wage distributions for $p$ â€” so the welfare object is **opportunity-aware**: the proportion of the population at a given $(c,L)$ is the welfare value of $(c,L)$ weighted by how available that incomeâ€“leisure combination is.

**Money-metric vs other.** $V$ is a **common-utility** comparability device, not a money-metric / equivalent income in the King (1983) / Fleurbaey sense. It is *not* the JMP's preference-respecting equivalent income, and it is *not* converted to an income/subsidy against a reference. The paper cites Fleurbaey & Maniquet (2006), "Fair Income Tax," and Boadway et al. (2002) in fn 5 precisely on the comparability-under-heterogeneous-leisure-preferences problem â€” a useful citation hook for my Â§2.1, but the paper does **not** adopt the equivalent-income solution.

**Constrained vs universal; ex-ante vs ex-post.** Welfare is computed **ex-post** on the *simulated chosen* pair $(c,h)$ under each tax rule (Â§6, step 3: "apply to the chosen $(c,h)$ the common utility function"), not on an ex-ante inclusive value / log-sum. It is opportunity-*aware* in estimation of $V$ (offered densities enter), but the per-person welfare number is read off a realised bundle, not off the JMP's $V_i=\log\sum\exp(\cdot)$. This is the AC/JJT "ex-post chosen-alternative" form that my welfare memo lists as a **secondary, correction-free cross-check (D3)**, not as the headline ex-ante object.

**Where it sits on my $W^1$â€“$W^6$ map.** **Not established / N/A.** The paper does not have an Independence-of-$\mathbf{y}$/Independence-of-$A$ stance and does not span a compensationâ€“responsibility spectrum at the *measure* level. The closest correspondence is conceptual only: a common-utility welfare function evaluated on realised bundles is nearest to a **Full-Responsibility, ex-post** reading, but this is an analogy, not a placement on the characterised family. **Do not claim this paper instantiates any $W^k$.**

---

## 7. Inequality / decomposition content

**Inequality / SWF family (explicit in source, Â§5).** Aggregation uses a family of **rank-dependent social welfare functions** $W_k$ (eq (5.1)â€“(5.2)) of Mehran (1976)/Yaari (1988) type, with associated inequality measures $I_k$ (eq (5.4)): $I_1$ Bonferroni, $I_2$ Gini; $W_1$ Bonferroni, $W_2$ Gini, $W_3$ an intermediate, $W_\infty$ utilitarian (inequality-neutral). Inequality aversion **decreases in $k$**. These are "illfare-ranked single-series Ginis" (Donaldsonâ€“Weymark 1980). **This $W_k$ is an inequality-aggregation family and shares only a letter with my $W^1$â€“$W^6$ equivalent-income family â€” see Â§13.**

**Opportunity content (explicit in source, Â§5).** The normative novelty is **Equality of Opportunity (EOp)** in the sense of Roemer (1998): outcomes are the joint product of *circumstances* (beyond control) and *effort* (own responsibility). **Circumstances/types are defined by father's years of education** (Type 1 $<5$, Type 2 $5$â€“$8$, Type 3 $>8$); **effort is proxied by the within-type quantile/rank** of the welfare distribution. The EOp criterion maximises (a weighted version of) the across-type minimum at each effort quantile; the paper introduces an **extended EOp family** $\tilde W_k$ (eq (5.6)) and a mixture distribution $\tilde F$ (eq (5.7)) of the worst-off type-segments, decomposed analogously to $W_k$ (eq (5.8)â€“(5.9)). EO (Equality of Outcome) is the special case ignoring the type structure.

**Counterfactual construction / order properties.** The "decomposition" here is the EOp construction (across-type minimum / mixture of worst-off segments), **not** a Shapleyâ€“Shorrocks attribution and **not** order-independent-by-construction in the Shapley sense. There is no exhaustive components-sum-to-total identity of the JMP type.

**Reusable for my three-way access/ability/preference Shapley split?** **Indirectly, as lineage and contrast, not as method.** (i) The paper's responsibility cut is **circumstances (family background) vs effort**, a *different* opportunity referent from the JMP's **job-set access/ability vs preference**; it is two-way and Roemerian, not three-way and structural. (ii) To get to the JMP's split you would *not* extend this EOp construction; you would instead Shapley-equalise the **structural** blocks ($g_2$ ability, $g_1/g_3/p_0$ access, $v$ preference) that this paper *estimates but does not decompose*. So the citable contribution is: this paper supplies the **estimated opportunity sub-densities** that a three-way decomposition needs, and a **precedent for treating opportunity as compensation-relevant and effort/preference as responsibility-relevant**, while leaving the structural Shapley attribution itself unaddressed.

---

## 8. Identification and separation of preferences from opportunities

**What identifies tastes vs constraints here (explicit-in-source mechanism; the cleanly-stated exclusion is derived-by-reading).** Preferences ($v$) and opportunities ($p$) are separated by **functional-form and covariate exclusion** inside a jointly estimated MNL-type likelihood:
- The **offered-wage** density $g_2$ depends on **own education and experience** (eq (A9)); these enter *opportunity*, not the systematic utility $v$ (eq (A2)). Education/experience shifting *offered pay* but not *tastes* is the exclusion that pins the **ability** channel apart from preference.
- The **offered-hours** density $g_1$ carries **part-time/full-time peaks** (eq (A7)); concentration of observed hours at those peaks beyond what tastes-over-leisure would generate identifies the **access** (hours-availability) channel.
- The **sector** density $g_3$ and **market proportion** $p_0$ absorb participation/sectoral availability.
- Pooling **singles and couples** in one simultaneous likelihood (the opportunity densities are shared across marital status â€” Appendix A) adds cross-group restrictions that help identify the offer side.

**Transport to my France pooled cross-section (no panel, no external instrument).** The **estimator transports directly** â€” this is the lineage of my RURO baseline, and identification rests on the same within-cross-section functional-form + exclusion logic rather than on panel variation or instruments, which is exactly my setting. Two honest caveats: (i) separation of *ability* (returns in $g_2$) from *preference* leans on the maintained exclusion that education/experience are offer-side, not taste-side â€” the same assumption my ability/access cut depends on, so this paper is support for the assumption's standard-ness, not independent proof of it; (ii) the paper's *EOp* identification (father's education types) does **not** transport, as that variable is absent from my data. So cite for **estimator identification**, not for **circumstance-based EOp identification**.

---

## 9. Key results and magnitudes

- **Model size:** **78 parameters** capturing heterogeneity in preferences and in opportunities across singles and couples (abstract, Â§2, Â§7).
- **Labour-supply elasticities (Table 3.2, aggregate, own-wage, unconditional total hours):** married females $\approx$ **0.52**, married males $\approx$ **0.39**, single females $\approx$ **0.02**, single males $\approx$ **0.02**. Headline behavioural facts: married women far more elastic than married men; **low-income households much more elastic than high-income** (Table 3.1; Â§3); backward-bending supply for singles in the middle deciles.
- **Optimal-tax findings (Â§6, Tables 6.2â€“6.6):** within a 6-parameter piecewise-linear rule and **fixed total net revenue**, every optimal rule implies an **average tax rate below the 1994 rule**, with **lower marginal rates on low/average income and higher marginal rates on high income**; more egalitarian SWF $\Rightarrow$ more progressive rule. Unconstrained, the **top marginal rate is $100\%$** above $\approx$ **NOK 700,000 (1994) $\approx$ â‚¬87,000**; a second exercise caps $\tau_3 \le 0.60$. **EO and EOp optimal rules are very similar** (EOp even marginally more progressive in places) â€” a notable null on the EO-vs-EOp distinction at the policy-rule level.

---

## 12. What I can cite this paper for

1. **Estimator lineage and legitimacy of the RURO/latent-jobs design** â€” choice over jobs $(h,w,s)$, utility weighted by an estimated opportunity density, in the Aabergeâ€“Colombinoâ€“StrÃ¸m tradition; the structural backbone of my baseline.
2. **The opportunity density is *factorised* into a pay sub-density and feasibility sub-densities** â€” i.e. that separating offered **wages** (ability) from offered **hours/sector/market** (access) is standard practice inside the offer mechanism, not a JMP innovation (eqs (A3),(A7)â€“(A9)).
3. **Welfare can be made opportunity-aware** by estimating the welfare function with the same offer-weighted density (Â§4) â€” precedent for "welfare under different feasible sets," while being explicit that AC use a *common-utility* device, not equivalent income.
4. **Responsibility-sensitive normative framing has standing in this literature** â€” opportunity (circumstances) as compensation-relevant, effort as responsibility-relevant (Roemer EOp, Â§5) â€” motivation for my compensationâ€“responsibility spectrum.
5. **The rank-dependent / single-series-Gini SWF family** ($W_1$ Bonferroni, $W_2$ Gini, $W_\infty$ utilitarian; $I_1,I_2$) as an inequality-aggregation toolkit (Â§5) â€” usable as an inequality index citation, kept terminologically separate from my $W^1$â€“$W^6$.
6. **Empirical regularities** for sanity-checking my French estimates: married-women > married-men elasticity, low-income > high-income elasticity.

---

## 13. What I should NOT cite this paper for (overclaim risks)

1. **$W^1$â€“$W^6$ namespace collision.** The paper's $W_1,W_2,W_3,W_\infty$ are **rank-dependent SWFs / single-series Ginis**, *not* the JMP's equivalent-income measure family. Never imply this paper contains, characterises, or instantiates my $W^1$â€“$W^6$. (It does not.)
2. **Two-way, not three-way; and a *different* two-way.** Its responsibility cut is **circumstances (father's education) vs effort**, Roemerian â€” not **opportunity vs preference** and not **access/ability/preference**. Do not present it as a two-factor opportunity/preference decomposition that "just needs extending" to three channels; the channel it splits is family background, a different object.
3. **Sector $\ne$ occupation $\ne$ industry.** Its $s$ is **public/private**; do not cite it as ISCO occupation (`loc4`) or as NACE industry (`lindi`). In my map a public/private offer split is *access*, but it is not my occupation layer.
4. **Welfare object mismatch.** It is **common-utility, ex-post on the chosen bundle**, *not* preference-respecting ex-ante equivalent income. Do not cite it as a money-metric equivalent-income computation or as an ex-ante inclusive-value welfare object; at most it is precedent for my **D3 secondary** ex-post CE cross-check.
5. **No Shapleyâ€“Shorrocks.** Do not attribute an order-independent, exhaustive components-sum-to-total decomposition to this paper.
6. **Deterministic-opportunities boundary.** The JMP treats opportunities as **deterministic**; do not import any "random opportunities" reading from the RURO label here.
7. **Theory-paper boundary.** This is an empirical AC paper; it is unrelated to the Haydarâ€“Maniquet theory paper. Never route any normative characterisation/proof through it, and never let "Aabergeâ€“Colombino welfare function" stand in for the companion paper's axiomatic $W^1$â€“$W^6$.
8. **Data-year and age-window precision.** Report the 1994/1995 data year and the 18â€“54 vs 20â€“62 windows as flagged `[verify]`, not as settled facts, given the internal inconsistencies in the source.

---

## 16. TL;DR for retrieval

Aaberge & Colombino (2006, Statistics Norway DP475) estimate a 78-parameter RURO/latent-jobs household labour-supply model on Norwegian 1994/95 data (singles + couples, joint), in which an estimated **opportunity density factorises into an offered-wage sub-density in own education/experience (= my *ability* channel) and offered-hours/sector/market sub-densities (= my *access* channel)**, then use it to simulate **optimal piecewise-linear taxes** under fixed revenue, finding lower average rates with higher top-end marginal rates and near-identical EO and EOp optima. For the JMP it is **estimator-lineage T1A** â€” strong support for the structural backbone and for the access/ability factorisation of the offer mechanism â€” but its **welfare object is common-utility/ex-post (not equivalent income)**, its **$W_k$ are single-series-Gini SWFs (not my $W^1$â€“$W^6$)**, and its **"opportunity" is Roemerian family-background circumstances (not feasible-job-set access/ability)**, so it must not be cited as a money-metric equivalent-income decomposition or as a three-way opportunity/preference split.

---

## [T1-only sections â€” rerun with `JMP_T1_exhaustive_extraction_prompt_v2.md` (not attached)]

These section numbers are referenced by the T2 template as belonging to the fuller T1 template, but I do not have the T1 prompt and will not invent its required structure. Source material that would populate them, for a cheap rerun:

- **Â§3 (full model / equation inventory):** Â§2 eqs (2.1)â€“(2.4); Appendix A eqs (A1)â€“(A9) singles, (A10)â€“(A19) couples; Type-III extreme-value error (eq (2.3)).
- **Â§4 (estimation details):** simultaneous ML, likelihood = product of densities over single-F / single-M / couples; ages 18â€“54; parameter tables A1 (singles utility), A2 (couples utility), A3 (job/hours/wage densities), A4 (incomes & labour supply under the current rule).
- **Â§10 (robustness / specification variants):** unconstrained vs $\tau_3\le 0.60$ exercises (Tables 6.2 vs 6.3); EO vs EOp (Tables 6.2â€“6.6); inequality-aversion sweep over $k=1,2,3,\infty$.
- **Â§11 (limitations):** common-utility comparability device rather than equivalent income; circumstance variable limited to father's education; ex-post welfare read on simulated bundles; static cross-section.
- **Â§14 (related-literature positioning):** Mirrlees (1971), Saez (2001), Laroque (2005); Roemer (1998), Roemer et al. (2003); Aabergeâ€“Colombinoâ€“StrÃ¸m (1999, 2000); Fleurbaeyâ€“Maniquet (2006); Dagsvik (1994); Ben-Akivaâ€“Watanatada (1981).
- **Â§15 (data infrastructure):** 1995 Survey of Level of Living; Norwegian 1994 tax rule (Table 6.1); 6-parameter piecewise-linear optimal-rule class (eq (6.1)).
# Aaberge & Colombino 2013 â€” Using a Microeconometric Model of Household Labour Supply to Design Optimal Income Taxes

> **Notation warning, read first.** This paper uses the symbol $W_k$ for a family
> of *rank-dependent social welfare functions* (Bonferroni, Gini, $W_3$,
> utilitarian). These are **not** the JMP's money-metric measures $W^1,\dots,W^6$
> on the compensationâ€“responsibility spectrum. The two objects share notation and
> nothing else. Every reference to "$W_k$" below is AC's SWF unless explicitly
> tied to the JMP family. Do not import AC's $W_k$ into the JMP $W$-family.

## 0. Metadata
- **BibTeX key:** AabergeColombino2013
- **Authors:** Rolf Aaberge (Statistics Norway); Ugo Colombino (University of Torino).
- **Year:** 2013.
- **Outlet:** *The Scandinavian Journal of Economics*, Vol. 115, No. 2 (April 2013), pp. 449â€“475.
- **DOI:** 10.1111/sjoe.12015.
- **PDF filename:** `Aaberge_and_Colombino_-_2013_-_Using_a_Microeconometric_Model_of_Household_Labour_Supply_to_Design_Optimal_Income_Taxes.pdf`.
- **JEL / keywords:** H21, H31, J22; microsimulation, optimal taxation, random utility model (p. 449).
- **Tier:** T1A.
- **JMP block(s) served:** opportunity-mechanism (the structural opportunity density $p$); estimation (the RURO / continuous-multinomial-logit likelihood); welfare (a money-metric, common-utility interpersonal-comparability construction â€” as a *precedent and a contrast*, not a template); normative-interpretation (the inequality-measurement apparatus); motivation. It does **not** serve the decomposition block (no source decomposition is performed).

## 1. One-paragraph relevance to my JMP
This is a canonical statement of the latent-jobs / RURO structural labour-supply model the JMP estimates: a utility $\times$ availability factorisation in which households choose among jobs characterised by wage, hours, and non-pecuniary attributes, with an explicit estimated **opportunity density** $p(h,w,s)$ â€” the direct ancestor of the JMP's $g$ and of the $\log h+\log w+\log\text{market}$ channels (explicit-in-source, pp. 454â€“455). It is most useful to the JMP's **access** and (partially) **ability** discussion, because $p$ is exactly the object the JMP cuts into those two sub-blocks â€” though AC themselves do **not** cut $p$ and operate a strict **two-way** preference-vs-opportunity split, not the JMP's three-way {access, ability, preference}. It is also a precedent for the welfare step, but a *contrasting* one: AC's welfare is **preference-neutralising** (a common utility function for interpersonal comparability) and **ex post** (evaluated at the simulated realised job), whereas the JMP is **preference-respecting** and **ex ante** (inclusive value over the feasible set). It speaks to no JMP welfare measure as a match; it is the foil the JMP departs from on both the preference axis and the ex-ante axis.

## 2. Data and setting
- **Country / years:** Norway, 1994 (estimation); 2001 (out-of-sample prediction only). Estimation data from the 1995 Norwegian Survey of Level of Living, with detailed income from tax records; prediction data from the 2002 survey (pp. 453, 455, 458â€“459).
- **Sample unit:** individuals and households; couples modelled as a **joint** decision unit (pp. 453â€“454).
- **Sample size:** 1,842 couples, 309 single females, 312 single males (p. 455).
- **Sample restrictions:** ages 20â€“62; self-employed and permanent-disability-benefit recipients excluded (p. 455).
- **Key variables:** gross wage $w$, hours $h$, non-pecuniary job characteristics $s$ (stated example: "occupational sector"), pre-tax non-labour income $I$, net disposable income $c$ (pp. 454).
- **Budget-set construction:** $c=f(wh,I)$, with $f$ the full Norwegian tax rule; budget sets are complex and non-convex from the detailed tax system (p. 454).
- **Transport to my France pooled 2015â€“2017 EUROMOD cross-section:** partial. Shared: a single cross-section, household/couple units, a tax-benefit budget map (their $f$ â†” my EUROMOD `ils_dispy`), preference + opportunity heterogeneity. **Features they have that I do not / differ:** (i) an **out-of-sample panel-like validation** (estimate on 1994, predict 2001 from a second survey wave) â€” I have no second wave to predict onto and certify by **synthetic recovery** instead; (ii) their setting is single-country single-year, so no pooling-across-years machinery; (iii) Norwegian register-quality income. **Features I have that they lack here:** an estimated occupation-as-access object kept out of utility (they put "occupational sector" in *both* $v$ and $p$ â€” see Â§3); a multi-year pooled sample.

## 3. Model and objects (map object-by-object to mine)
- **Choice set = my latent-jobs set?** Yes in spirit. Agents choose a job from $B$, "the set of all opportunities available to the household," including the non-market option ($w=0,h=0$) (p. 454, explicit). Jobs are $(w,h,s)$ packages; wages can **differ from job to job** for the same agent (p. 454, explicit) â€” the key departure from a fixed common hours grid that the JMP also makes.
- **Deterministic utility = my preference utility $v$?** Yes. They factorise $U[f(wh,I),h,s,j]=v[f(wh,I),h,s]\,\varepsilon(j)$, with $v$ systematic and $\varepsilon(j)$ iid type-III extreme value (eq. (2), p. 454, explicit). Maps to my preference block $v$.
- **Explicit opportunity / availability mechanism analogous to my $g$?** **Yes** â€” the density $p(h,w,s)$ of available jobs of type $(h,w,s)$ (p. 454, explicit). This is the direct ancestor of my $g$. **But AC do not separate it into hours / wage(ability) / market / occupation sub-channels** â€” $p$ is a single joint density over $(h,w,s)$. The hours and market(participation) channels are present (jobs in certain hours ranges more/less likely; non-market option included); a wage channel is present (wages vary job-to-job, $p$ is over $w$); an occupation/sector channel is present ($s$). The **decomposition of $p$ into ability vs access is mine, derived-by-analogy**, not theirs.
- **Budget map = my EUROMOD disposable income?** Analogous: their $f(wh,I)\to c$ â†” my EUROMOD `ils_dispy`. Explicit (eq. (1), p. 454).
- **âš‘ FLAG â€” attribute entering BOTH utility and opportunity.** The non-pecuniary characteristic $s$ (their example: **occupational sector**) enters **both** the utility $v[f(wh,I),h,s]$ **and** the opportunity density $p(h,w,s)$ (eqs. (2)â€“(3), p. 454â€“455, explicit). They further state they "account for the disutility of hours of work and choice of sector" (p. 456, explicit), confirming sector is in utility, while $p(h,w,s)$ puts it in availability. **They give no identification justification for this double entry in this paper** (the estimated specification is deferred to Aaberge & Colombino 2011 [not in this source]). This is exactly the configuration the JMP forbids at baseline (occupation in opportunity only). Treat AC as a *cautionary precedent*, not a license.
- **Terminological note.** AC call $s$ "occupational sector" and later "choice of sector" â€” i.e. they **conflate occupation and sector** in their own language (pp. 454, 456). The JMP keeps `loc4` (occupation) strictly distinct from `lindi` (NACE industry); do not adopt AC's "sector" usage.

## 4. Estimation method
- **Likelihood / estimator:** maximum likelihood on the choice density (eq. (3), p. 455). The contribution of an observed $(h,w,s)$ is $\varphi(h,w,s)=v[f(wh,I),h,s]\,p(h,w,s)\big/\!\int\!\!\int\!\!\int v[f(xy,I),y,z]\,p(y,x,z)\,dx\,dy\,dz$ (explicit). The model has **78 parameters** estimated jointly (pp. 452, 455, explicit).
- **Choice-set construction (estimation):** density (3) is written as a continuous multinomial logit with an **integral** denominator; the per-observation contribution weights attractiveness $v$ by availability $p$. The paper does **not** describe a finite sampled-alternative set or a McFadden sampling correction for the *estimation* step here; the operational specification and the derivation are deferred to Aaberge et al. (1999) and Aaberge & Colombino (2011) [not in this source] (footnote 5, p. 455). Density (3) is noted to be a special case of Dagsvik (1994) and related to Ben-Akiva & Watanatada (1981) continuous logit (footnote 5, explicit).
- **Proposal / sampling density; $-\log(\text{prior})$ correction:** **not present as an explicit term in this paper's estimation likelihood.** The role my $-\log\pi$ plays is, in AC, occupied structurally by $p$ itself (an *estimated structural* opportunity density, not a *sampling proposal*). A finite-draw construction appears only in the **optimal-tax simulation** (Â§4b), not in estimation. So: **no explicit per-alternative $-\log\pi$ correction is documented here** [the estimation-stage treatment is in AC 1999/2011, not in source].
- **Normalisation / scale:** $\varepsilon(j)$ iid type-III extreme value fixes scale in the usual logit sense (p. 454, explicit). No further scale discussion in this paper.
- **Numerical method / starts:** ML maximisation of (3); details not given here (deferred to AC 2011). The *optimal-tax* search uses an iterative grid-search over $\approx 200{,}000$ tax rules per optimisation (footnote 17, p. 466) â€” that is the policy search, not the structural ML.
- **What pins preferences separately from opportunities:** the parametric factorisation $v\times p$ plus the extreme-value assumption, identified off the joint distribution of realised $(h,w,s)$ (derived-by-analogy from eqs. (2)â€“(3); AC give no explicit identification proof in this paper). See Â§8.
- **Verdict â€” reusable for my RURO/JAX pipeline?** **Yes, as the conceptual template** (the $v\times p$ factorisation and choice density (3) are precisely my factorisation). **No, as a drop-in estimator**: this paper omits the operational sampling/correction machinery my JAX pipeline needs (the $-\log\pi$ step), and its $p$ is undivided. Reuse the *factorisation and the availability-weighting intuition*; obtain the sampling-correction and identification detail from the operational papers (AC 1999/2011, Dagsvik), not from here.

## 4b. Proposal / sampling-of-alternatives correction  [brief â€” mostly N/A for estimation]
- **Estimation stage:** no sampled-alternative proposal or correction is described (the likelihood is the continuous density (3)).
- **Simulation stage (optimal tax):** for each household they simulate an opportunity set = the **observed job plus 199 market and non-market alternatives drawn from the estimated $p$ densities**, then draw $\varepsilon$ from the type-III EV distribution at each alternative and select the utility-maximising alternative (p. 465, step (a), explicit). The "proposal" here **is** the estimated structural $p$; there is no separate importance-sampling correction term, because this is a forward simulation (draw-and-argmax), not a corrected likelihood.
- **Individualised vs common proposal:** $p$ can depend on agent characteristics â€” "for different agents, the relative number of market opportunities might differ" (p. 454, explicit) â€” and households face exogenous opportunity **joint density functions of $h,w,s$** (p. 456, explicit). So $p$ is, in principle, **partly individualised**, but the parameterisation of that individualisation is in AC 2011 [not in source]. The elasticity computation perturbs the **means of the wage densities** by 10% (p. 456, explicit), indicating $p$'s wage channel has an individual/agent-specific mean â€” analogous to my individualised wage mean $\mu_i$.
- **McFadden-style?** Not in this paper. Footnote 16 (p. 466) shows AC are *aware* of the McFadden (1978) expected-maximum-utility route and deliberately do **not** use it for welfare.
- **Relevance to my integrator:** AC corroborate that the wage channel of the opportunity density is the individualised, high-dispersion channel (the 10%-mean perturbation), consistent with my proposal-individualisation finding (wage/occupation individualised; hours/employment common). But AC supply **no** explicit per-draw log-prior, so they cannot be cited for the correctness of my $-\log\pi$ step.

## 5. Opportunity mechanism  [MOST IMPORTANT â€” split by channel]
AC's opportunity mechanism is a **single estimated structural density $p(h,w,s)$** over available jobs (p. 454, explicit). It is a genuine density over alternatives (not a reservation-wage rule, not bare offer probabilities), and it can vary with agent characteristics (p. 454, explicit). Functional form of $p$: **not given in this paper** (a "convenient parametric specification," deferred to AC 2011) [not in source]. Mapping to my three sub-objects:

- **access (hours / market-participation / region / year / occupation offers):**
  - *Hours / participation:* explicit. $p$ lets "jobs with hours of work in a certain range [be] more or less likely to be found," and $B$ includes the non-market option $w=0,h=0$ (pp. 454, explicit). This is my hours-availability + market/participation channel.
  - *Region / year:* **not present** in this single-cross-section Norwegian model (no regional or temporal offer shifters described). [not established here]
  - *Occupation offers:* present **but contaminated** â€” occupational sector enters $p$ **and** $v$ (see Â§3 flag). So AC's "occupation availability" is not a clean access object the way my `loc4`-in-$g$-only object is.
- **ability (the wage technology):** present **only as a wage channel of $p$**, not as a separated Mincer-type technology. Wages vary job-to-job and $p$ governs which wages are available; the elasticity exercise perturbs wage-density means (pp. 454, 456, explicit). **Returns to own education/experience and a residual-productivity dispersion $\sigma$ are not specified in this paper** [in AC 2011, not in source]. So AC give me the *idea* that wage availability lives in the opportunity density, but **not** an explicit ability sub-block to cite.
- **occupation as availability vs something else:** AC treat occupation/sector as a job *characteristic* that is simultaneously a source of (dis)utility and an availability dimension â€” **not** a clean access-only object, and **conflated with "sector"** (pp. 454, 456). âš‘ Flag the occupation/sector conflation and the double-entry whenever citing AC on occupation.

**No-omission check:** AC do **have** an explicit opportunity mechanism (unlike the fixed-grid equivalent-income tradition), so the "what an omission would cost" clause does not apply. The relevant cost to my **three-way** decomposition is different: AC's $p$ is **undivided**, so they provide no within-opportunity ability/access identification â€” my ability/access cut cannot lean on AC for identification, only for the existence of the joint density.

## 6. Welfare object â€” and its place on my $W^1$â€“$W^6$ map
- **Does the paper compute welfare?** Yes. AC build an **individual welfare function** $V$ used by the social planner, distinct from the estimated behavioural utility (pp. 452â€“453, 460).
- **Type:** a **money-metric, common-utility** interpersonal-comparability construction in the King (1983) / Deatonâ€“Muellbauer (1980) / Hammond (1991) tradition (pp. 452â€“453, explicit citations). $V$ is a **common** (same-parameter) Boxâ€“Cox utility over equivalent income $y$ and leisure $L$:
  $$\log V(y,h)=\gamma_2\frac{y^{\gamma_1}-1}{\gamma_1}+\gamma_4\frac{L^{\gamma_3}-1}{\gamma_3}\qquad\text{(eq. (4), p. 460)}$$
  with $L=1-(h/0.8736)$, and equivalent income $y=c$ for singles, $y=c/\sqrt 2$ for couples (eq. (5), p. 460; square-root scale, footnote 11, p. 461). Estimated parameters (Table 5, p. 461): $\gamma_1=-0.649$, $\gamma_2=3.026$, $\gamma_3=-12.262$, $\gamma_4=0.045$.
- **âš‘ Preference axis â€” the decisive contrast.** $V$ is a **common utility function** deliberately chosen to **neutralise preference heterogeneity** so that levels are interpersonally comparable; it "is not used to simulate behaviour, only to evaluate" the chosen bundles (pp. 452â€“453, explicit). This is the **opposite** of the JMP's **preference-respecting** stance. AC's welfare object therefore does **not** sit anywhere on my $W^1$â€“$W^6$ spectrum (all six of which respect own preferences); it corresponds to the **preference-equalisation pole** (my Shapley preference-channel reference, the common reference preference $R^h$ / the JJT preference-neutralised CV$^{\text{circ}}$ pole), not to a measure on the menu.
- **Universal vs constrained set; ex-ante vs ex-post:** welfare levels are computed **ex post**, by applying $V$ to the **simulated chosen** $(y,h)$ (p. 466, step (c), explicit). It is **not** an inclusive-value object. AC explicitly note the alternative expected-maximum-utility (log-sum) route and state they do not use it (footnote 16, p. 466). Reference price / preference: a fixed **common** preference (the $\gamma$'s) and the $\sqrt2$ equivalence scale for couples.
- **Verdict:** **incompatible as a welfare-object template** for the JMP on two axes (preference-neutralising vs preference-respecting; ex-post vs ex-ante). **Adaptable as a precedent** for (i) using a common reference preference as a comparability device â€” the exact device my decomposition's preference-equalisation step uses â€” and (ii) the King-style money-metric lineage. Cite AC for the *common-utility comparability method* and as the *contrast* the JMP's preference-respecting ex-ante object improves upon for an opportunity question.

## 6b. Inclusive value and money-metric inversion
- **Inclusive value as welfare core?** **No.** AC use the **simulated realised choice**, not the log-sum/expected-maximum. They are explicit that the expected-maximum-utility (McFadden 1978) method is an *alternative they did not adopt*, judging the simulation method "more flexible and robust for producing disaggregated results" (footnote 16, p. 466).
- **Money-metric inversion?** The money metric is **equivalent income $y$ constructed directly** ($y=c$ or $c/\sqrt2$), then evaluated through the common $V(y,h)$. There is **no one-dimensional root-solve inversion** of an own-utility map (because preferences are neutralised by the common $V$, and $y$ is built directly). This contrasts with my bracketing root-solve of the household's **own**-utility map.
- **Expectation over EV shocks â€” analytic or simulated?** **Simulated.** In the chosen method they "draw a value $\varepsilon$ from the type III extreme value distribution" at each alternative and take the argmax (p. 465, step (a), explicit). My welfare layer is **analytic in the shocks** (closed-form log-sum, no $\varepsilon$ draws). This is a clean methodological dividing line: AC = simulated argmax + ex-post evaluation; JMP = analytic log-sum + ex-ante inversion.

## 7. Inequality / decomposition content  [three-way where relevant]
- **Inequality apparatus:** AC use **rank-dependent social welfare functions** $W=\int_0^1 q(t)F^{-1}(t)\,dt$ (eq. (6), p. 462) with weight family $q_k(t)$ (eq. (7)): $k=1$ Bonferroni ($-\log t$), $k\ge2$ the $\frac{k}{k-1}(1-t^{k-1})$ form; $W_\infty=\mu$ utilitarian (eq. (8)). Associated inequality measures $C_k=1-W_k/\mu$ (eq. (9), p. 463): $C_1=$ Bonferroni, $C_2=$ **Gini** â€” the "Gini nuclear family" (Aaberge 2007, cited p. 463). The Yaari (1987, 1988) **dual independence axiom** characterises the rank-dependent family (p. 462, a *cited* characterisation, not AC's own theorem).
- **Decomposition rule:** **none.** AC perform **no** source decomposition of welfare inequality. There is no Shapley, Shorrocks, factor-component, RIF, or subgroup decomposition into opportunity vs preference (or access/ability/preference). They *compute* inequality-averse social welfare under several criteria and compare *optimal tax rules*; that is a different exercise.
- **Counterfactual construction:** their counterfactuals are **policy** counterfactuals (alternative tax rules), not **source-equalisation** counterfactuals. Nothing is "zeroed out" in the inequality-attribution sense.
- **âš‘ Notation collision (restate):** AC's $W_1$ (Bonferroni), $W_2$ (Gini), $W_3$, $W_\infty$ (utilitarian) are **social welfare functions**, categorically distinct from the JMP's money-metric $W^1$â€“$W^6$.
- **Verdict â€” reusable for my three-way Shapleyâ€“Shorrocks split anchored on $W^3$/$W^5$/$W^1$?** **No** for the decomposition itself (AC have none). **Yes, narrowly,** for the *inequality-index* layer: the Gini / Bonferroni / rank-dependent indices and the Gini-nuclear-family framing are a citable, axiomatically grounded choice of $I(\Omega^k)$. To get from AC to my design you would have to **add the entire decomposition layer** (the source-equalisation counterfactuals and the Shapley averaging), which AC do not contain.

## 8. Identification and the separation of preferences from opportunities  [STRICT]
- **What identifies tastes vs constraints:** the **parametric factorisation** $U=v\cdot\varepsilon$ with the structural availability density $p$, plus the **type-III extreme-value** assumption, identified off the observed joint distribution of realised $(h,w,s)$ (eqs. (2)â€“(3); derived-by-analogy â€” AC state the factorisation and the EV assumption but give **no explicit identification theorem** in this paper). The separation rests on **functional form and distributional assumptions**, not on choice-set variation across an instrument, not on panel repeated choices, not on an external opportunity shifter.
- **Ability vs access within the opportunity side:** **not addressed.** AC do not separate $p$ into a wage-technology (ability) and a feasibility (access) sub-block, so they offer **no** identification argument for the within-opportunity cut my decomposition needs. This is the single biggest gap between AC and the JMP's identification burden.
- **Transport to my France pooled cross-section (no panel, no external instrument):** the *preference-vs-opportunity* separation transports â€” it too rests on parametric/functional-form identification, exactly my situation. The *ability-vs-access* separation does **not** transport from AC because it is absent there; I must secure it from functional-form restrictions (education/experience in the wage block only) and defend it directly, not by citing AC.
- **Validation standard:** AC certify reliability by **out-of-sample prediction** (estimate on 1994, predict the 2001 income distribution; Table 4, p. 459, "rather successful at reproducing the income distribution"). This is **not** synthetic-parameter recovery. My baseline is certified by **synthetic recovery**; AC are a precedent for *some* external validation discipline but not for my specific gate. Do not cite AC as a synthetic-recovery precedent.
- **Referee defence ("your decomposition is mechanical"):** AC are useful here only as the source of the *structural opportunity density* that makes the opportunity/preference split a modelled object rather than a residual; they are **not** a defence of the ability/access sub-split, which I must argue independently.

## 9. Key results and magnitudes
- **Overall wage elasticity of labour supply $\approx 0.12$** (low aggregate response) (p. 456, explicit).
- **Heterogeneity:** married women far more wage-elastic than married men; low-income households much more elastic than high-income (p. 456, explicit; Table 1, p. 457). Cross-wage elasticities are non-trivial, supporting joint household modelling (p. 457).
- **Out-of-sample fit:** simulated vs observed 2001 decile income distributions track closely (Table 4, p. 459).
- **Optimal-tax findings (AC's headline, *not* a JMP quantity):** monotonically increasing MTRs; **negative** MTR on the lowest bracket (EITC-like); **100% MTR** on very high incomes (affecting $\approx1.5$â€“$2\%$ of taxpayers); a lump-sum that is a **tax** (property-tax-like); lower average tax rate; more egalitarian SWF $\Rightarrow$ more progressive optimal rule (Bonferroni $>$ Gini $>$ utilitarian in progressivity) (pp. 452, 466â€“472, Tables 7â€“11).
- **Benchmarks for my opportunity share / welfare spread:** **none directly.** AC report no opportunity share, no unfair share, no decomposition shares, no across-measure welfare spread. The only transferable magnitude is the **low aggregate wage elasticity ($\sim0.12$) with strong income-gradient heterogeneity**, useful as an external plausibility check on my estimated behavioural responses, not on my decomposition.

## 10. Estimators, theorems, or formal results
1. **Choice density (continuous multinomial logit / RURO contribution).** Statement: $\varphi(h,w,s)=\dfrac{v[f(wh,I),h,s]\,p(h,w,s)}{\int\!\int\!\int v[f(xy,I),y,z]\,p(y,x,z)\,dx\,dy\,dz}$ (eq. (3), p. 455). Assumptions: utility factorises as $v\cdot\varepsilon$ (eq. (2)); $\varepsilon$ iid type-III EV; $p$ a structural availability density. Technique: (i) factorise utility into systematic $v$ and EV $\varepsilon$; (ii) weight $v$ by availability $p$; (iii) integrate over the continuous job space; (iv) ML on (3). **Reusability:** **yes** â€” this *is* my factorisation; reuse directly, but supply the sampling-of-alternatives correction ($-\log\pi$) and the ability/access cut, neither of which appears here.
2. **Individual welfare function (Boxâ€“Cox).** $\log V(y,h)=\gamma_2\frac{y^{\gamma_1}-1}{\gamma_1}+\gamma_4\frac{L^{\gamma_3}-1}{\gamma_3}$ (eq. (4), p. 460). Assumptions: common parameters across individuals (preference neutralisation); $L=1-h/0.8736$; equivalent income via eq. (5). **Reusability:** as the **preference-equalisation reference** device only (my Shapley preference channel), *not* as the headline welfare object (which is preference-respecting).
3. **Rank-dependent SWF and inequality.** $W=\int_0^1 q(t)F^{-1}(t)\,dt$ (eq. (6)); $q_k$ (eq. (7)); $W_\infty=\mu$ (eq. (8)); $C_k=1-W_k/\mu$ (eq. (9), pp. 462â€“463), with $C_2=$ Gini. **Yaari dual-independence axiom** characterises the family (cited, p. 462). **Reusability:** **maybe** â€” a citable inequality-index layer $I(\Omega^k)$ for the welfare distributions; orthogonal to the decomposition.
4. **Optimal-tax program** $\max_{\vartheta} W[\cdot]$ s.t. revenue $\ge G$ and household utility-maximisation (eq. (10), p. 464), over piecewise-linear five-bracket rules (eq. (11), p. 465). **Reusability:** **no** â€” out of scope for the JMP (this is policy design, not measurement/decomposition).

## 11. Robustness and specification sensitivity
- **What they vary:** the social welfare criterion ($W_1$ Bonferroni / $W_2$ Gini / $W_3$ / $W_\infty$ utilitarian) â€” and report how the optimal tax rule shifts (Tables 7â€“11). They constrain the top MTR $\le100\%$ (footnote 19) and note results might change with intercountry mobility / taxable-income responses (p. 473).
- **What they do NOT vary (relevant to my stress-tests):** choice-set size, number of $\varepsilon$ draws, number of starts, alternative opportunity-set definitions, circumstance partitions, reference-preference choices, or an ability/access boundary. The simulation uses a **fixed** opportunity set of observed-job + 199 draws (p. 465) â€” one data point on choice-set size ($\approx200$), with **no** sensitivity analysis around it and **no** effective-sample-size diagnostic.
- **For my recovery/stability tests:** AC provide little. Their reliability evidence is the out-of-sample prediction, not a draw-count or recovery stress-test. The absence of an ESS / draw-growth check in a $\approx200$-alternative simulation is itself a (silent) gap my Â§6 welfare-integration gate is designed to close; AC are not a precedent for that gate.

## 12. What I can cite this paper for
- The **RURO / latent-jobs factorisation** $U=v\cdot\varepsilon$ with an **explicit estimated opportunity density $p(h,w,s)$** that weights attractiveness by availability (eqs. (2)â€“(3); the canonical statement the JMP's $g$ descends from).
- The conceptual move that **wage rates vary job-to-job and the choice set is a probability density, not a fixed grid** (p. 454) â€” the departure from the common-hours-grid tradition that the JMP shares.
- **Joint (unitary) modelling of couples'** labour supply within this framework (pp. 453â€“454).
- The **common-utility money-metric** approach to interpersonal comparability (King 1983 lineage) â€” as a *precedent and explicit contrast* for the JMP's preference-respecting choice, and as the device behind the JMP's preference-equalisation reference.
- The **Gini nuclear family / rank-dependent SWF** inequality apparatus (eqs. (6)â€“(9); Aaberge 2007) as a citable inequality-index layer.
- The **microsimulation-as-design** methodology (iterating an estimated structural model against a social objective) â€” motivational/contextual.
- The **low aggregate wage elasticity ($\approx0.12$) with strong income-gradient heterogeneity** in a Norwegian RURO model (Table 1) â€” an external plausibility benchmark for behavioural responses.

## 13. What I should NOT cite this paper for  [overclaim risks]
- **A source decomposition.** AC perform **no** decomposition of welfare inequality into opportunity vs preference, let alone the JMP's three-way **access/ability/preference** split. Do not cite AC for any decomposition result or method.
- **Ex-ante / inclusive-value welfare.** AC's welfare is **ex post** (simulated realised choice); they explicitly decline the expected-maximum-utility route (footnote 16). Do not present AC as an inclusive-value welfare precedent.
- **Preference-respecting welfare.** AC's welfare object is **preference-neutralising** (a common utility function). Do not read it as a preference-respecting equivalent income; on the preference axis it is the *opposite* pole.
- **The $W^1$â€“$W^6$ family.** AC do **not** contain the compensationâ€“responsibility family or the Independence-of-$y$ / Independence-of-$A$ classification. Their $W_k$ are rank-dependent **social welfare functions** (notation collision); never map AC's $W_k$ onto the JMP's $W^k$.
- **An ability/access cut.** AC's opportunity density $p$ is **undivided**; do not cite them for any ability-vs-access separation or identification.
- **"Sector" / industry language.** AC call the non-pecuniary job characteristic "occupational sector" and "choice of sector," **conflating occupation and industry**, and place it in **both** utility and opportunity. Do not import this usage; the JMP's `loc4` (occupation) is access-only and is never called sector/industry (`lindi`).
- **Random-/probabilistic-opportunity framing.** AC describe "exogenous opportunity joint density functions" and a probabilistically represented choice set (pp. 454, 456). The JMP treats opportunities as **deterministic**. Do not cite AC as endorsing a random-opportunity ontology for the JMP.
- **Synthetic-recovery certification.** AC validate by out-of-sample prediction, not synthetic recovery; do not cite them as a recovery-gate precedent.
- **Theory-paper boundary.** AC is an empirical optimal-tax paper, not the Haydarâ€“Maniquet axiomatic theory paper. AC *cite* Fleurbaeyâ€“Maniquet (2006) for interpersonal comparability (footnote 9, p. 460) â€” a citation, not the companion characterisation. Never attribute the companion paper's axioms/proofs to AC, and never read AC as a theory contribution.

## 14. Direct quotes worth citing
- p. 454: "the set of all opportunities available to the household." (defines $B$, the latent-jobs feasible set, incl. the non-market option)
- p. 455: "the relative attractiveness â€” weighted by a measure of availability." (the $v\times p$ intuition â€” ancestor of my $g$-weighting)
- p. 454: "wage rates ... can differ from job to job." (the departure from a fixed hours grid)
- p. 453: "using a common utility function ... interpersonally comparable individual welfare measures." (the preference-neutralising comparability device â€” the JMP's contrast)
- p. 466 (footnote 16): "measured instead by the expected maximum utility (McFadden, 1978)." (the inclusive-value route AC explicitly do **not** take)

## 15. Open questions and risks for my draft
- **Where AC stop is where the JMP starts.** AC supply the joint opportunity density but neither divide it (ability/access) nor decompose inequality by source. My contribution is precisely the layer AC omit; I must not let AC's authority appear to cover the decomposition â€” a careful referee will see AC as adjacent, not as cover.
- **Double-entry caution.** AC put occupation/sector in both $v$ and $p$ with no stated identification justification (here). This is the configuration my baseline forbids; I should cite AC as the *reason* to be disciplined (occupation in $g$ only), not as a precedent that double-entry is fine.
- **Ex-post vs ex-ante is a defensible, citable fork.** AC's footnote 16 (simulation vs expected-maximum-utility, "asymptotically equivalent") is useful: it lets me position the JMP's analytic ex-ante log-sum as the principled choice for an *opportunity* question, citing AC for the awareness of both routes while explaining why the access channel requires the ex-ante object.
- **Preference-neutralisation risk.** Because AC's welfare neutralises preferences, a reader might assume my welfare does too. I must foreground the preference-respecting + ex-ante combination as the double departure from AC, early in the welfare section.
- **Integration-error blind spot.** AC's $\approx200$-alternative simulation carries no ESS / draw-growth diagnostic; my welfare-integration gate addresses a problem AC leave unexamined. Frame this as a methodological tightening, not a contradiction.

## 16. TL;DR for retrieval
Aaberge & Colombino (2013) is the canonical RURO / latent-jobs labour-supply model â€” utility $v$ times an estimated structural opportunity density $p(h,w,s)$, EV shocks, joint couples, 78 parameters, Norway 1994 â€” making it the direct ancestor of the JMP's $g$ and the **access** (and partially **ability**) channels, though AC keep $p$ **undivided** (a two-way preference/opportunity split, not the JMP's three-way). Its welfare layer is the JMP's twofold **contrast**: a **preference-neutralising** common-utility money-metric evaluated **ex post** on the simulated realised job (explicitly declining the inclusive-value route), versus the JMP's **preference-respecting, ex-ante** inversion. Cite it for the factorisation, the availability-weighting intuition, joint couples, and the Gini-nuclear-family inequality apparatus; never cite it for a decomposition, an ability/access cut, the $W^1$â€“$W^6$ family (notation collision with AC's rank-dependent $W_k$), preference-respecting or ex-ante welfare, or "sector" usage.
# Aaberge, Colombino & Wennemo 2009 â€” Evaluating Alternative Representations of the Choice Sets in Models of Labor Supply

## 0. Metadata
- **BibTeX key:** AabergeColombinoWennemo2009 [verify against your `.bib`]
- **Authors:** R. Aaberge (Research Department, Statistics Norway); U. Colombino (Department of Economics, University of Turin); T. Wennemo (Research Department, Statistics Norway).
- **Year:** 2009.
- **Outlet:** *Journal of Economic Surveys*, Vol. 23, No. 3, pp. 586â€“612.
- **DOI:** 10.1111/j.1467-6419.2008.00573.x.
- **PDF filename:** `Aaberge_et_al_2009_Evaluating_Alternative_Representations_of_the_Choice_Sets_in_Models_of_Labor.pdf`.
- **Tier:** T1A.
- **JMP block(s) served:** estimation; identification (functional-form separation of preferences from opportunities); opportunity-mechanism (**access** = hours/market-availability density; **ability** = endogenous wage equation, but *not* as an opportunity-density channel); data-infrastructure (sampling-of-alternatives + proposal correction); recovery-test design (synthetic "true-model" Monte Carlo). **Does not serve:** welfare measurement, money-metric inversion, inequality decomposition, normative interpretation â€” these are *not established* in this paper.

---

## 1. One-paragraph relevance to my JMP
This is the methodological backbone for the *estimation machinery* of my RURO pipeline, not for its welfare or decomposition layers. It states the continuous/discrete RUM labour-supply model with an explicit **opportunity density** `p(h)` over hours (my **access** channel), the McFadden sampling-of-alternatives correction `âˆ’ln q(h)` (my mandatory proposal/prior correction), and a fully estimated "true" specification with a Boxâ€“Cox utility (my **preference** block) plus market/non-market and hours-peak opportunity dummies. Most directly, its central design â€” generate synthetic data from a *known* "true" model, re-estimate alternative specifications, and judge them by **out-of-sample policy prediction** rather than in-sample fit â€” is the template for my synthetic-recovery certification standard. The paper carries **no welfare object, no equivalent income, and no inequality decomposition**; its **ability** channel exists only as a simultaneously estimated wage equation, and it has **no occupation channel at all**, so it cannot be cited for those parts of my design.

---

## 2. Data and setting
- **Country / year:** Norway, 1995 (the estimation sample for the "true" model is the 1995 Norwegian Survey of Level of Living; the tax systems simulated are the 1994 system and a hypothetical revenue-constant flat tax) (p. 596, p. 597â€“598).
- **Dataset / sample unit:** individuals â€” married/cohabiting **females**, ages 20â€“62; other household members' behaviour held exogenous (p. 596). Although the underlying model was developed for joint couple behaviour, this paper estimates **female** supply only "to simplify the execution and the interpretation of the simulation exercise" (p. 596).
- **Sample size:** 1,842 married/cohabiting females (the "true" estimation sample). Monte Carlo: 30 synthetic samples of 1,842 each; the systematic exercise uses a large pooled synthetic sample of 6 Ã— 1,842 = 11,052 (p. 594).
- **Key variables:** yearly hours of work `h`; gross wage `w`; exogenous (including spouse) income `I`; disposable income `f(wh, I)` via the tax-transfer function; age `A`; numbers of children below 3, 3â€“6, 7â€“14 (`C1, C2, C3`) (p. 595).
- **Budget-set construction:** `f(wh, I)` maps gross to net income through the (possibly nonlinear, nonconvex) tax-transfer rule; wages for non-workers are imputed from a two-step Heckman wage equation, and wages are treated as **endogenous** with the wage function estimated jointly by ML alongside utility and the opportunity density (notes 7â€“8, p. 606).
- **Transport to my setting:** **Partial.** The estimator and choice-set logic transport directly to my **France pooled 2015â€“2017 EUROMOD cross-section**. Differences I do *not* share / they do *not* have: their `f` is a Norwegian 1994 tax rule, not EUROMOD `ils_dispy`; they estimate **singles-female only**, not my three groups including **couples as a joint unit**; they have **no panel, no administrative match, no external opportunity instrument, no vacancy/offer data** â€” the same constraint I face, so it is a like-for-like cross-sectional identification setting, not a richer one.

---

## 3. Model and objects (object-by-object map)
- **Choice set vs my latent-jobs set:** Their choice object is a set of jobs/opportunities indexed by hours `h` plus unobserved attributes `j` (eq. 1, p. 589). This is the **hours-indexed** ancestor of my latent-jobs set; their jobs carry hours (and, via the wage equation, an implied wage), but **no occupation and no explicit multi-attribute job package** beyond hours and the EV1-distributed `Îµ(j)`. Note 3 (p. 606) records that the companion Aabergeâ€“Colombinoâ€“StrÃ¸m models treat `B` as market *and* non-market opportunities characterised by hours, wage, and other attributes â€” but in *this* paper the realised object is hours-only.
- **Deterministic utility vs my preference `v`:** Their `v(f(wh,I), h)` is a **Boxâ€“Cox** form in consumption (disposable income) and leisure, with leisure shifted by `log A`, `(log A)Â²`, and the three children counts (eq. 10, p. 595). This is the direct analogue of my **preference** block; my locking of consumption to EUROMOD `ils_dispy` corresponds to their `f(wh,I)` argument. Explicit-in-source.
- **Opportunity / availability mechanism vs my `g`:** **Yes, explicit.** The density of opportunities `p(h)` (eq. 11, p. 595) splits into a **market/non-market** mass `p0` (parameter `Î¸0`, eq. 13) and, conditional on a market job, an **hours-availability** density `g(h)` that is uniform except for peaks at part-time (910â€“1066 h) and full-time (1898â€“2106 h), governed by `Ï€1, Ï€2` (eq. 12). In the choice index these enter additively as `Î¸0 d0(h) + Ï€1 d1(h) + Ï€2 d2(h)` (eq. 14, p. 595).
  - **hours channel:** present (`Ï€1, Ï€2` peaks; uniform elsewhere) â†’ my **access**/hours sub-block.
  - **market/participation channel:** present (`Î¸0`, the "job" dummy) â†’ my **access**/employment sub-block.
  - **wage channel (ability):** **not in the opportunity density.** Wage is handled as an **endogenous wage equation** estimated jointly (notes 7â€“8), i.e. a measurement/selection equation, *not* a `log w` channel inside `g`. So my "wage/ability sub-block of `g`" has **no exact counterpart** here â€” derived-by-analogy only.
  - **occupation channel:** **absent.** No occupation, ISCO, `loc4`, or any task variable. (Therefore no sector/industry conflation risk arises â€” there is simply nothing of the kind in the paper.)
- **Budget map vs my EUROMOD disposable income:** Their `f(wh,I)` â‰ˆ my EUROMOD-standardised disposable income map; conceptually identical role, different implementation.
- **Attribute-in-both-channels flag:** **No double entry.** Hours enter utility `v` (through leisure and net income) *and* the opportunity density (`Ï€1, Ï€2` peaks), but the paper treats this as the standard separation â€” the smooth utility in `(consumption, leisure)` versus discrete availability dummies at specific hours ranges â€” and the second-order analysis (eqs. 5â€“8, p. 591â€“592) is precisely about not conflating them. No job attribute is placed in both the *systematic utility* and the *opportunity density* in a way they flag as needing an identification justification. Consistent with my "do not add occupation/sector to both utility and opportunity at the first step" rule.

---

## 4. Estimation method
- **Likelihood / estimator:** Maximum likelihood on the multinomial-logit choice probability derived from EV1 shocks (eqs. 2â€“4, 14â€“16). Wage functions and the opportunity-density parameters are estimated **jointly** with the utility parameters by ML (note 7, p. 606).
- **Choice-set construction:** Two contrasted modes. (i) **Fixed grid:** mid-values of 6 or 24 equally spaced intervals on `[0, 3640]` (eq. 16, p. 596). (ii) **Sampled alternatives:** the observed `h` plus 5 or 23 draws (â†’ 6 or 24 points) from the empirical offered-hours distribution; for the *true* model's own estimation, the chosen value plus **999** draws (= **1,000** alternatives) (p. 596).
- **Proposal / sampling density:** `q(h)`, the empirical density of offered hours (eq. 9; the offered-hours density `g` of eq. 12). Under simple random sampling all `q` cancel; the paper instead uses the more efficient empirical-frequency sampling (p. 593).
- **Prior/proposal correction:** **Yes â€” `âˆ’ln q(h)` is subtracted from the choice index** in both estimation (eq. 15, p. 596) and the consistency result (eq. 9, p. 593), attributed to McFadden (1978) and Ben-Akiva & Lerman (1985). It is **always well defined** on the support where `q(h) > 0`. This is exactly my `âˆ’log Ï€` proposal/prior correction.
- **Normalisation / scale:** EV1 scale normalisation implicit in the logit (standard); no separate scale parameter discussed.
- **Numerical method / starting values / multistart:** Not detailed â€” ML is stated but the optimiser, starting values, and any multistart are **not reported** [verify; treat as not-established].
- **What pins down preferences vs the opportunity mechanism:** Functional-form separation â€” smooth Boxâ€“Cox `v` over `(net income, leisure)` versus additive availability dummies `Î¸0, Ï€1, Ï€2` localised to market participation and specific hours bands (eqs. 10â€“14). See Â§8.
- **Verdict â€” reusable for my RURO/JAX pipeline?** **Yes, for the estimation core.** The sampled-alternatives likelihood with the `âˆ’ln q` correction (eq. 15) *is* the object my engine implements; the named step to reuse is the per-alternative additive correction and the conditional-logit-with-sampling consistency argument. **No** for any welfare/decomposition step (absent here).

## 4b. Proposal / sampling-of-alternatives correction  [extract]
- **Mechanism:** Replace the true (large/continuous) set `B` by a sample `S` = chosen point + draws from `q(h)`; estimate using `Ï†(h|S) = exp(v âˆ’ ln q(h)) / Î£_{xâˆˆS} exp(v âˆ’ ln q(x))` (eq. 9, p. 593). Each drawn alternative carries its **own** `ln q` term â€” i.e. a per-alternative log-prior, as in my per-row `prior` column.
- **McFadden-style?** **Yes**, explicitly (McFadden 1978; Ben-Akiva & Lerman 1985).
- **Individualised or common?** The general discussion allows the sampling frequencies to be "differentiated according to personal characteristics of the decision units" (p. 593), i.e. *partly individualised in principle*. But in *this paper's* implemented "true" model the offered-hours density `g`/`q` and the opportunity parameters `Î¸0, Ï€1, Ï€2` are **common scalars**, not functions of `x_i` (eqs. 12â€“14; Table A1, p. 608). So the realised proposal here is **common across units in the hours and market channels** â€” there is no wage- or occupation-conditioned draw, because there is no occupation and the wage is a separate equation.
- **Relation to my integrator:** This supports my importance-sampling welfare integrator's *correction form* exactly. On my proposal-individualisation concern, the paper is the **common-channel** baseline: it individualises *nothing* in the offered-hours/market proposal, whereas my proposal individualises the wage and occupation channels and leaves hours/employment common. The paper therefore corroborates the *correctness* of the `âˆ’log Ï€` machinery but does **not** itself demonstrate an individualised proposal.

---

## 5. Opportunity mechanism  [MOST IMPORTANT â€” by channel]
The opportunity mechanism is a **density over alternatives** (eq. 11), not offer probabilities per firm and not a reservation-wage rule. Functional form: a binary market/non-market split `p(h) = p0Â·g(h)` for `h>0`, `1âˆ’p0` for `h=0` (eq. 11), with `p0/(1âˆ’p0)=exp(Î¸0)` (eq. 13); `g(h)` piecewise-uniform with multiplicative peaks `exp(Ï€1)`, `exp(Ï€2)` over the part-time and full-time hours bands (eq. 12). In the likelihood these become additive index terms `Î¸0 d0 + Ï€1 d1 + Ï€2 d2` (eqs. 14â€“15).

Mapping to my three sub-objects:
- **access (hours / market-participation):** **Directly present.** `Î¸0` = market vs non-market availability; `Ï€1, Ï€2` = relative density of jobs at part-time/full-time loads. This is the cleanest ancestor of my access sub-block's employment and hours-availability parameters.
- **access (region / year / occupation offers):** **Absent in the estimated model.** No regional, urbanisation, year, or occupation shifters of the density. The text notes (Section 2.3, p. 593) that *other* Aabergeâ€“Colombino papers let the density vary with personal characteristics, but this paper does **not** estimate such variation. So my region/year/occupation access machinery is **not** evidenced here â€” cite the companion papers, not this one, for circumstance-varying access.
- **ability (wage technology):** **Not in `g`.** Returns to education/experience and residual productivity dispersion `Ïƒ` â€” my ability sub-block â€” have **no counterpart inside the opportunity density** here. Wage is an endogenous, jointly estimated equation (notes 7â€“8), conceptually adjacent but architecturally distinct from a `log w` opportunity channel. Derived-by-analogy at best; do not cite this paper for an ability *opportunity* layer.
- **Occupation as availability vs something else:** **Not present** (no occupation object). No sector/industry conflation to flag.

**What the omissions cost my decomposition:** This paper supplies the *form* of an hours/market access density and the proof that it can be estimated jointly with preferences, but it does **not** supply (i) circumstance-varying access, (ii) a wage/ability opportunity channel, or (iii) any occupation channel. My three-way access/ability/preference cut therefore draws its *structure* from later Aabergeâ€“Colombino work and my own design, with this paper underwriting only the hours/market-access piece and the estimation correction.

---

## 6. Welfare object â€” and its place on my WÂ¹â€“Wâ¶ map
**The paper computes no welfare object.** There is **no money-metric welfare, no equivalent income, no compensating/equivalent variation, and no expected-utility (inclusive-value) welfare measure** anywhere in the paper. Its "evaluation" is **outcome prediction** â€” participation rates, hours of work, and disposable income, in-sample (1994 tax) and out-of-sample (flat-tax reform) â€” compared against the synthetic "true" model (eqs. 17â€“18; Tables 2â€“7, B1â€“B6). No reference price/preference/bundle/set is defined, because no welfare conversion is performed.

- **Universal vs constrained set:** N/A (no welfare integral).
- **Discrete-choice welfare subtleties (log-sum, Hicksian/Marshallian, ex-ante/ex-post):** N/A for welfare. (The only log-sum appearance is the Ben-Akivaâ€“Lerman expected-maximum used to analyse choice-set *aggregation* bias â€” see Â§6b â€” not as a welfare core.)
- **Location on my WÂ¹â€“Wâ¶ map:** **None.** The paper does **not** contain WÂ¹â€“Wâ¶, the Ind-y/Ind-A classification, or any compensationâ€“responsibility stance. Do not attribute any measure-family content to it.
- **Verdict:** **Incompatible as a welfare source** â€” it is an estimation/prediction-methodology paper. For Aabergeâ€“Colombino *welfare* content, cite the welfare-bearing companion papers, not this one.

## 6b. Inclusive value and money-metric inversion  [extract]
- **Inclusive value as welfare core?** **No.** The expected-maximum / log-sum appears once, as `vÌ‚â„“ = vÌ„â„“ + ln(Nâ„“) + ln(Dâ„“)` (eq. 5, p. 591) â€” the Ben-Akivaâ€“Lerman expected maximum over a sub-interval, used to characterise the **bias from aggregating alternatives** (eqs. 5â€“8). It is a choice-set-approximation diagnostic, **not** a welfare functional.
- **Money-metric inversion?** **None.** No own-utility map is inverted to a money figure; no closed-form welfare shortcut; no one-dimensional welfare solve.
- **Expectation over EV1 shocks â€” analytic or simulated?** For the *likelihood/choice probability*, analytic (closed-form logit). For the *prediction exercises*, **simulated**: they draw EV1 shocks per individual per alternative and take the argmax to assign the chosen alternative (p. 598, p. 601). This is the opposite of my analytic-in-shocks welfare integrator: my inclusive value is the closed-form log-sum with no shock draws, whereas their *prediction* step explicitly draws shocks and simulates the argmax.
- **Relation to my design:** Use this paper to justify the *estimation* log-sum/correction, **not** an analytic-in-shocks welfare inversion (which it does not do).

---

## 7. Inequality / decomposition content  [three-way where relevant]
- **Inequality index:** **None.** No Gini, MLD, Theil, variance-of-logs, or Atkinson.
- **Decomposition rule:** **None of the welfare kind.** There is **no** Shapley, Shorrocks, factor-component, subgroup, or RIF decomposition of welfare inequality.
- **What *is* present (do not confuse):** a **prediction-performance meta-regression** â€” `ln(z_k) = Î±0 + Î±1 x1k + â€¦ + interactions` (eq. 19, p. 602; Tables 8â€“9), regressing a model's relative prediction error `z_k` (eq. 18) on indicators for *model design features* (sampled vs fixed; 6 vs 24 alternatives; job dummy; peaks dummies). This attributes **prediction error to choice-set design choices**, which is categorically different from attributing **welfare inequality to access/ability/preference**.
- **Counterfactuals:** The only counterfactual is a policy counterfactual â€” a revenue-constant flat tax simulated through each model (p. 602) â€” used to test prediction performance, not to equalise or neutralise a welfare source.
- **Order/path-independence / exhaustiveness:** N/A (no inequality decomposition).
- **Verdict â€” reusable for my three-way Shapleyâ€“Shorrocks split?** **No.** The paper contributes nothing to my decomposition layer. It is **not** a two-way opportunity-vs-preference decomposition either; it has **no welfare-inequality decomposition at all**. To reach my three-way split, one would have to add (i) a welfare object, (ii) an inequality index, and (iii) a Shapley equalisation â€” none of which exist here. Flag this explicitly against any temptation to read the eq. 19 regression as a "decomposition."

---

## 8. Identification and the separation of preferences from opportunities  [STRICT]
- **What identifies tastes vs constraints:** **Functional-form restriction.** Preferences enter through a smooth Boxâ€“Cox `v` in `(net income, leisure)` with demographic leisure-shifters (eq. 10); opportunities enter through *additive, discrete* index terms localised to market participation (`Î¸0`) and to narrow hours bands at part-time/full-time (`Ï€1, Ï€2`) (eqs. 11â€“14). The identifying logic: concentration of observed hours at part-time/full-time loads, beyond what a smoothly varying utility would predict, is read as **availability** (the density peaks), not taste. Wages are separately identified via the jointly estimated wage equation with Heckman correction for non-workers (notes 7â€“8).
- **Ability vs access within the opportunity side:** **Not separated as such.** "Ability" (the wage equation) and "access" (the hours/market density) are *distinct parameter blocks* and so are in-principle distinguishable, but the paper does **not** frame or test an ability-vs-access identification; the wage equation is a measurement/selection device, not an opportunity channel.
- **External shifters / panel / repeated choices:** **None.** Single cross-section; no exclusion restriction from local unemployment or vacancies; no panel. Identification rests entirely on functional form plus distributional (EV1) assumptions.
- **Transport to my France pooled cross-section:** **Yes** â€” the functional-form-plus-distributional identification is exactly what I rely on, and the paper shares my constraint of **no panel and no external instrument**. This is therefore a *like-setting* precedent for parametric/synthetic-recovery identification, not a richer design I could borrow an instrument from.
- **Against the "your decomposition is mechanical" referee:** The paper's most useful contribution here is **methodological honesty about parametric identification** â€” it demonstrates (Tables 8â€“9, conclusions) that **in-sample fit barely discriminates between specifications**, while **out-of-sample policy prediction does**. That directly supports my standard of **synthetic recovery over in-sample fit**: a specification that fits is not thereby validated. Use this as a cited justification for recovery-based certification. (Note: the paper validates *prediction performance* across choice-set designs, not parameter recovery per se, though Table A2 does report the parameter estimates of all 16 models against the true values for inspection.)

---

## 9. Key results and magnitudes
- **"True"-model parameter estimates (Table A1, p. 608)** â€” population values for the synthetic exercise (estimate (std dev)): consumption Boxâ€“Cox `Î±1 = 0.39 (0.11)`, `Î±2 = 4.42 (0.44)`; leisure `Î±3 = âˆ’4.57 (0.53)`, `Î±4 = 168.88 (27.47)`; `Î±5 (log age) = âˆ’94.29 (15.32)`, `Î±6 (log ageÂ²) = 13.35 (2.16)`; children `Î±7 = 0.44 (0.23)`, `Î±8 = 1.23 (0.24)`, `Î±9 = 1.05 (0.19)`; opportunity density: job dummy `Î¸0 = âˆ’0.60 (0.10)`, part-time peak `Ï€1 = 0.46 (0.10)`, full-time peak `Ï€2 = 1.57 (0.07)`.
- **In-sample replication (1994 tax):** Across the 16 models, little statistically significant effect of choice-set representation; the only significant feature in the participation regression is **Job-dummy Ã— 24-alternatives** (p. 602; Table 8). Message: "the ability of a model to replicate observed outcomes is not very informative" (p. 605).
- **Out-of-sample (flat-tax reform):** Clear, large effects. Switching from fixed to sampled alternatives reduces the **hours-of-work** relative prediction error by **83%** (model IIIa vs Ia; p. 605). Disposable-income mean relative error under the flat tax: model Ia â‰ˆ **âˆ’4.3%** overall vs â‰ˆ **âˆ’2.4% to âˆ’2.6%** for the richer models IIb/IIIc/IVd (Table 5, p. 600).
- **Behavioural content of the flat tax:** It stimulates labour supply, with the strongest response among **lower-income** deciles â€” participation rises by roughly **11% and 10%** in the two lowest deciles and **~5%** in the third, modest thereafter; high-decile females change hours little but gain the largest disposable-income increases (p. 602).
- **Variance of prediction error:** **No notable difference across models** in the standard deviation of the prediction error (motivating the second exercise's focus on the *mean*) (p. 605).
- **Population referred to:** married/cohabiting Norwegian females 20â€“62, 1994 vs flat-tax regimes. Magnitudes are **prediction-error** magnitudes (and elastic/parameter values), **not** welfare-share or opportunity-share findings â€” none of the latter exist in this paper, so it cannot benchmark my opportunity share or welfare spread.

---

## 10. Estimators, theorems, or formal results
1. **Continuous/discrete RUM choice probability with opportunity density.**
   - Statement (LaTeX): `\varphi(h) = \dfrac{\exp(v(f(wh,I),h))\,p(h)}{\int \exp(v(f(wx,I),x))\,p(x)\,dx}` (eq. 2, p. 590); discrete analogue eq. 3; equal-availability special case `p(h)=a` gives the bare logit (eq. 4).
   - Assumptions: EV1 (type-I extreme value) shocks; utility additively separable in `v` and `Îµ(j)`.
   - Technique: (i) random-utility maximisation; (ii) EV1 â‡’ closed-form logit; (iii) opportunity density `p(h)` weights alternatives multiplicatively.
   - Reusability: **Yes** â€” this is the core form of my per-alternative value before the proposal correction.
2. **Sampling-of-alternatives consistency (McFadden 1978).**
   - Statement (LaTeX): `\varphi(h\mid S) = \dfrac{\exp(v(f(wh,I),h)-\ln q(h))}{\sum_{x\in S}\exp(v(f(wx,I),x)-\ln q(x))}` (eq. 9, p. 593; with opportunity terms, eq. 15, p. 596).
   - Assumptions: positive sampling density `q(h)`; chosen point included in `S`; uniform-conditioning property for the correction.
   - Technique: (i) replace true set `B` by sample `S`; (ii) subtract per-alternative `\ln q`; (iii) consistency from McFadden (1978)/Ben-Akivaâ€“Lerman (1985).
   - Reusability: **Yes, central** â€” this is exactly my `âˆ’log Ï€` correction; reuse the per-alternative log-prior form verbatim in the engine.
3. **Aggregation-bias expansion.**
   - Statement (LaTeX): expected maximum on sub-interval `\hat v^{\ell} = \bar v^{\ell} + \ln(N^{\ell}) + \ln(D^{\ell})` (eq. 5, p. 591), with the typical literature approximation (eq. 8) dropping the `0.5\,\sigma_{hh}v_{hh} + \ln N + \ln D` terms.
   - Assumptions: second-order Taylor expansion of `v` within sub-intervals.
   - Technique: (i) Ben-Akivaâ€“Lerman aggregation; (ii) Taylor expansion; (iii) show dropped terms bias fixed-grid estimates unless equal across intervals.
   - Reusability: **Maybe** â€” useful as a written justification for *sampling rather than fixing* a coarse hours grid, and for why a too-coarse grid biases estimates; not needed computationally if I already sample.

(No numbered theorems are stated in the paper; results are presented as derivations and simulation findings. Do not invent theorem numbers.)

---

## 11. Robustness and specification sensitivity
- **What they vary:** alternative generation (fixed vs sampled); number of alternatives (6 vs 24); inclusion of the job (market) dummy; inclusion of the peaks dummies â€” the full 2Ã—2Ã—2Ã—2 = 16-model grid (Table 1, p. 597).
- **What breaks / what is robust:** the **standard deviation** of prediction error is insensitive to all four design choices; the **mean** prediction error is insensitive **in-sample** but **sensitive out-of-sample**, where sampling + heterogeneous availability sharply reduce error (Tables 2â€“9; conclusions p. 605â€“606).
- **For my recovery/stability tests:** (i) **choice-set size** matters less than sampled-vs-fixed and the availability dummies â€” informs my draw-count / number-of-alternatives stress test (my 101/901 alternatives are far above their 6/24, and they already used 1,000 for the true-model fit). (ii) The result that **a coarse fixed grid degrades the *tails* of predicted distributions** (lower/upper deciles, p. 599) is a direct caution for my **effective-sample-size** concern in thin-coverage households. (iii) The headline robustness lesson â€” **in-sample fit is uninformative; out-of-sample/recovery is the discriminating test** â€” is the precedent for my synthetic-recovery gate.
- **Reference-state / ability-access boundary sensitivity:** **Not studied** (no welfare references, no ability/access cut). N/A.

---

## 12. What I can cite this paper for
- The RUM labour-supply choice probability with an explicit **opportunity density** over hours, and the market/non-market plus hours-peak parameterisation (`Î¸0, Ï€1, Ï€2`) (eqs. 10â€“14).
- The **sampling-of-alternatives + `âˆ’ln q` proposal correction** as the consistent estimator on a sampled choice set (eqs. 9, 15), attributable here and to McFadden (1978)/Ben-Akivaâ€“Lerman (1985).
- The methodological claim that **choice-set representation has little effect on in-sample fit but a material effect on out-of-sample policy prediction** (conclusions, p. 605â€“606) â€” my justification for valuing recovery/out-of-sample behaviour over in-sample fit.
- The synthetic **"true-model â†’ re-estimate â†’ compare" Monte Carlo template** as a precedent for recovery-style validation (Sections 3â€“5).
- That the **opportunity density can be estimated jointly with Boxâ€“Cox preferences and an endogenous wage equation by ML** (note 7).
- The bias analysis showing **fixed coarse grids bias estimates / degrade distribution tails** (eqs. 5â€“8; p. 599).

---

## 13. What I should NOT cite this paper for  [overclaim risks]
- **No welfare object.** It computes **no** money-metric welfare, equivalent income, or EV/CV. Do not cite it for any welfare construction or for my ex-ante inclusive-value welfare.
- **No inequality decomposition (and not even two-way).** It has **no** welfare-inequality decomposition. Do not read the eq. 19 prediction-error meta-regression as an opportunity-vs-preference (or access/ability/preference) decomposition.
- **No WÂ¹â€“Wâ¶ / no compensationâ€“responsibility content.** It contains none of the Ind-y/Ind-A classification or the measure family. Do not attribute these to it.
- **No ability-as-opportunity-channel.** The wage is an endogenous equation, not a `log w` channel in `g`; do not cite it for my wage/ability opportunity sub-block.
- **No circumstance-varying access in the estimated model.** The estimated opportunity density uses common scalars `Î¸0, Ï€1, Ï€2`; do not cite it for region/year/occupation-varying access (cite the companion 1995/1999/2004 papers for that, with verification).
- **No occupation / no sector.** There is no occupation object; do not cite it for `loc4` or any occupation-as-access design, and there is correspondingly no NACE/ISCO conflation in it.
- **"Random opportunities" framing:** the paper's opportunity density is a **deterministic** density estimated by ML; the randomness is in the EV1 utility shocks. Consistent with my deterministic-opportunities stance â€” do not import a "random opportunities" reading.
- **Theory-paper boundary:** this is an empirical/methodological paper; it has no bearing on the Haydarâ€“Maniquet axiomatic characterisation, and nothing in it should be read as a theory contribution to the JMP.

---

## 14. Direct quotes worth citing
(Short verbatim excerpts; page numbers as printed. Use sparingly and attribute.)
- p. 593, on the correction: "consistent estimates of v(f(wh, I), h) can still be obtained when the true choice set B is replaced by S".
- p. 605, on the headline lesson: "the ability of a model to replicate observed outcomes is not very informative".
- p. 595, on the offered-hours density: peaks make it "more likely to find jobs with hours that accord with full-time and standard part-time positions".

---

## 15. Open questions and risks for my draft
- **Common vs individualised proposal.** This paper individualises *nothing* in its offered-hours/market proposal, so it cannot, by itself, justify my partly-individualised proposal (wage/occupation conditioned on `x_i`); I must lean on the proposal-individualisation audit and the companion papers, not this one.
- **Recovery â‰  prediction performance.** The paper's validation target is *out-of-sample prediction*, not *parameter recovery*; my certification claim is recovery-based. Cite carefully: it supports "in-sample fit is insufficient," but it is not itself a parameter-recovery proof (though Table A2 lets one inspect parameter dispersion across designs).
- **Integration node count.** Their true-model fit used 1,000 alternatives; my 101 (singles) is far thinner. The paper's finding that coarse sets degrade distribution tails is a flag for my thin-ESS singles households (cross-references my welfare-integration ESS gate).
- **Endogenous wage handling.** They estimate the wage equation jointly with Heckman selection; my pipeline treats the wage technology as an ability sub-block of `g`. The architectural difference must be stated so a referee does not read my ability channel as their wage equation.
- **No numerical-implementation detail.** Optimiser, starting values, and multistart are not reported [verify], so the paper cannot be cited for numerical-stability practice.

---

## 16. TL;DR for retrieval
Methodological/simulation paper establishing that, in a RUM labour-supply model with an explicit **hours/market opportunity density** and a Boxâ€“Cox **preference** utility, the sampling-of-alternatives estimator with the `âˆ’ln q` **proposal/prior correction** (McFadden 1978) is consistent, and that choice-set representation barely affects in-sample fit but strongly affects out-of-sample policy prediction â€” the precedent for my synthetic-recovery-over-fit standard and my `âˆ’log Ï€` correction. It carries **no welfare object, no inequality decomposition, no ability-as-opportunity channel, and no occupation**, so it informs only the **estimation/access** and **recovery-design** parts of my JMP, never the welfare (WÂ¹â€“Wâ¶) or three-way decomposition layers. The opportunity density is **deterministic** and estimated, consistent with my deterministic-opportunities framing; it is an empirical/methodological source with no connection to the Haydarâ€“Maniquet theory paper.
# Aaberge & Colombino 2012 â€” Accounting for family background when designing optimal income taxes: a microeconometric simulation analysis

> **Extraction note (read first).** The main article text relegates the
> microeconometric labour-supply model â€” its utility function, choice-set
> construction, opportunity/quantity-constraint mechanism, estimator, and
> estimates â€” to an **Electronic Supplementary Material (ESM)** that is *not*
> in front of me. Every claim below about the *structural model microstructure*
> (Sections 3, 4, 4b, 5, 8, 10) is therefore drawn only from the main text's
> brief characterisations and is flagged accordingly. I do **not** reconstruct
> the model from the companion Aabergeâ€“Colombinoâ€“StrÃ¸m (1999/2000) or Dagsvik
> (1994) papers, even where the main text cites them. Where the main text is
> silent, I write "ESM, not in main text â€” [verify against ESM]".

---

## 0. Metadata

- **BibTeX key:** AabergeColombino2012
- **Authors:** Rolf Aaberge (Statistics Norway); Ugo Colombino (Collegio Carlo Alberto / UniversitÃ  di Torino)
- **Year:** 2012 (received 8 Jan 2009; accepted 1 Jul 2010; published online 14 Sep 2010)
- **Outlet:** *Journal of Population Economics* 25(2):741â€“761
- **DOI:** 10.1007/s00148-010-0331-y
- **PDF filename:** Aaberge_Colombino_2012_Accounting_for_family_background_when_designing_optimal_income_taxes.pdf
- **Tier:** T1A
- **JMP block(s) served:**
  - **welfare** â€” the rank-dependent welfare functionals $W_k$ over equivalent income are the *closest precedent in the literature for a "menu of welfare functionals over a money-metric distribution"*, which is the shape of my Exercise A.
  - **normative-interpretation** â€” Roemer EOp / circumstances-vs-effort is a *responsibility-sensitive* welfare logic adjacent to (but **not** identical to) my access/ability/preference cut.
  - **decomposition** â€” provides a welfare-into-(mean Ã— inequality) factorisation $W_k = W_\infty(1-C_k^*)$ that is a *precedent in form* but is **not** a source-component (Shapley) decomposition.
  - **estimation** â€” supplies a structural-labour-supply-driven *policy-simulation* template (singles + couples, three group models), but the model microstructure is in the ESM and not usable from this file alone.
  - **data-infrastructure / motivation** â€” secondary; Italy 1993 SHIW, not transportable to my setting.

---

## 1. One-paragraph relevance to my JMP

This paper is the canonical demonstration, inside the Aabergeâ€“Colombino structural-labour-supply tradition I build on, that a *responsibility-sensitive* social objective can be evaluated on a money-metric (equivalent-income) distribution produced by a microeconometric model â€” and that the answer (how much redistribution the criterion favours) is an *empirical* question settled by simulation, not by theory. It speaks most directly to my **welfare** layer: its rank-dependent family $W_1, W_2, W_3, W_\infty$ (Bonferroni, Gini, an intermediate, utilitarian) is a precedent for treating *a menu of welfare functionals* rather than one number, which is the structural shape of my Exercise A (the $W^1$â€“$W^6$ measure menu). It also speaks to **normative-interpretation**: its circumstances/effort partition (Ã  la Roemer) is a responsibility cut analogous in spirit to my compensationâ€“responsibility spectrum. **Crucially, the analogy is partial and must be policed:** their responsibility cut is *between-type vs within-type* on an *exogenous circumstance* (father's education), evaluated by *rank within type* â€” it is **not** a structural decomposition of welfare inequality into **access / ability / preference**, and their "equality of opportunity" is Roemer-EOp, not my latent-jobs opportunity density. The paper is a precedent for *form and ethos*, not a source I can cite for my specific three-channel decomposition.

---

## 2. Data and setting

- **Country / year:** Italy, 1993.
- **Dataset:** Bank of Italy Survey of Household Income and Wealth (SHIW 1993) [p. 749].
- **Sample unit:** individuals nested in households; the *decision* unit is the household â€” single females, single males, and couples, each with a separately estimated labour-supply model [p. 749]. Welfare is then assigned at the *individual* level via an equivalised income (see Â§6) for decision-makers aged 18â€“54 [p. 750].
- **Sample size:** not stated in the main text [verify against ESM]. The sample is described as covering "approximately the entire labour force," persons 19â€“54 [pp. 743, 749]. No N is given.
- **Key variables:** gross income $y$; disposable income $x$; hours of work; the circumstance/type variable = **father's years of education**, partitioned into three types (<5 years; 5â€“8 years; >8 years) [p. 746]; equivalent income (see Â§6).
- **Budget-set construction:** disposable income is generated by *applying a parametric tax-transfer rule to gross income* (affine two-parameter and piecewise-linear three-parameter rules) under a constant-revenue and non-negative-income constraint; the model then re-optimises labour supply against the new budget [pp. 749â€“750, 750, 756]. The detailed 1993 tax rule is in the ESM [p. 744].

**Transport to my setting.** *Does not transport* as a data source. Italy 1993 SHIW â‰  my France pooled 2015â€“2017 EU-SILC/EUROMOD cross-section. Two features they *have* that I do **not**:
1. **A parental-background circumstance variable** (father's education) used to define Roemer types. I have **no** parental-background instrument in the engine-ready EUROMOD data; my "circumstances" are the structural access/ability channels, not an exogenous family-background type.
2. **Budget sets generated by counterfactual policy rules** they vary as the object of optimisation. My budget sets come from *the actual* EUROMOD policy at the 2016-real basis; I do **not** search over tax rules â€” my paper is a *decomposition*, not an optimal-tax exercise.
Features the paper shares with me at the *framework* level (singles + couples; structural labour supply; equivalent income) are genuine but live in the ESM, so this file does not give me the implementation.

---

## 3. Model and objects (map object-by-object to mine)

**Heavy caveat:** the model is in the ESM. The main text states only the following.

- **Choice set = my latent-jobs set?** The main text says utility functions **and choice sets** of the underlying model are *stochastic*, and that stochastic simulation is used to find each unit's optimal choice given a tax rule [p. 749]. This is consistent with the Aabergeâ€“Colombino RURO/latent-jobs lineage, but the main text does **not** describe the choice set's construction (grid vs sampled alternatives, size, job attributes). **Derived-by-analogy, not explicit:** that this is a latent-jobs set like mine. [verify against ESM]
- **Deterministic utility = my preference utility $v$?** The model has utility functions over (at least) income and, the authors note, *leisure is not yet valued in the welfare measure* â€” welfare equates income and well-being, with the value of leisure explicitly flagged as *ongoing/future work* [p. 754 fn. 8; p. 760]. So even though the *behavioural* model has a utility over consumption and leisure, the *welfare* object in this paper is **income-based, not preference-respecting equivalent income**. This is a first-order difference from my $W^1$â€“$W^6$.
- **Explicit opportunity / availability mechanism analogous to my $g$?** The main text says the model "accounts for quantity constraints on the distribution of hours" [p. 743] and that choice sets are stochastic [p. 749]. This is the *only* opportunity-mechanism signal in the main text. It is consistent with a job-availability / hours-availability density (my **access** channel), but the functional form, whether it separates **hours / wage(ability) / market / occupation**, and whether it varies with circumstances are **not in the main text**. [verify against ESM]
- **Budget map = my EUROMOD disposable income?** No. Their disposable income is produced by *parametric candidate tax rules* applied to gross income [pp. 749â€“750]; mine is the realised EUROMOD `ils_dispy`. The functional role differs: theirs is the policy lever being optimised; mine is fixed structure.
- **Job attribute in BOTH utility and opportunity?** **Cannot determine from the main text** â€” the model is in the ESM. The main text does not describe occupation or sector at all. No flag can be raised from this file; the question must be carried to the ESM. **Not-established here.**

**Object map verdict:** the *behavioural* model is in the same family as mine (structural labour supply, singles + couples, stochastic choice sets, hours quantity constraints), but **this file does not let me verify the object correspondence**, and the *welfare* object differs sharply (income, not preference-respecting equivalent income).

---

## 4. Estimation method

- **Likelihood / estimator:** **Not in the main text.** The labour-supply models for the three groups are described as "estimated on 1993 Italian data" [p. 749], with details in the ESM. No likelihood, estimator, or normalisation is stated in the main article. [verify against ESM]
- **Choice-set construction (grid vs sampled; size):** Not in the main text [verify against ESM].
- **Proposal / sampling density; prior/proposal correction:** Not mentioned in the main text. **Not-established here** â€” see Â§4b.
- **What the paper *does* compute (the simulation, not the estimation):** the *policy optimisation* is computational. A five-step loop [pp. 749â€“750]: (1) apply a candidate tax rule to gross incomes â†’ disposable incomes, re-deriving labour supply by **stochastic simulation** of the household models under constant total revenue and non-negative disposable income; (2) impute each decision-maker (18â€“54) an **equivalent income** = household disposable income / $\sqrt{\text{household size}}$; (3) build type-specific equivalent-income distributions $F_1, F_2, F_3$ by father's education; (4) compute $W_k$ for $k=1,2,3,\infty$; (5) iterate over tax-rule parameters to maximise $W_k$ subject to constant revenue.
- **Verdict (reusable for my RURO/JAX pipeline?):** **No, not from this file.** The *estimation* machinery I would want to compare against lives in the ESM. What *is* reusable is the **simulation-evaluation loop architecture** (re-solve labour supply under a counterfactual budget â†’ equivalise â†’ evaluate a welfare functional), which is a template my welfare/decomposition layer partially mirrors when it reprices reference packages through EUROMOD â€” but my paper does **not** optimise over policies, so even the loop is only a partial analogue.

---

## 4b. Proposal / sampling-of-alternatives correction  [extract even if brief]

**Not present in the main text.** The article does not discuss sampling of alternatives, importance sampling, a proposal density, or a McFadden-style log-prior correction; if such machinery exists it is in the ESM. **Not-established here.** I cannot relate this paper's proposal individualisation to my wage/occupation-individualised, hours/employment-common proposal from this file. Carry to ESM if the model details are needed; otherwise this paper is *silent* on my Â§4b concern.

---

## 5. Opportunity mechanism  [MOST IMPORTANT â€” be exhaustive; split by channel]

There are **two distinct "opportunity" notions** in this paper, and conflating them would be the central error a careless reader could make. I treat them separately.

### 5.1 The *normative* opportunity notion (Roemer EOp) â€” this is what the paper is *about*

This is **not** a structural opportunity *density over jobs*. It is a **partition of the population into types by an exogenous circumstance**, with the residual within-type variation attributed to *effort*:

- **Circumstance:** father's education, three types â€” <5 years, 5â€“8 years, >8 years [p. 746].
- **Effort proxy:** an individual's *rank (quantile) within their type's* equivalent-income distribution; two individuals at the same within-type quantile are deemed to have exerted the same effort [p. 746].
- **Pure-EOp objective (Roemer):** the average over quantiles of the *lowest* type-specific income at each quantile, $W_\infty = \int_0^1 \min_j F_j^{-1}(t)\, dt$ [p. 747, eq. (2.5)] â€” i.e. it cares only about the worst-off *type* at each effort level, ignoring within-(worst-type) inequality.
- **Their extension (the paper's own contribution):** a *family* of "extended EOp" functionals $W_k = \int_0^1 p_k(t)\, \min_j F_j^{-1}(t)\, dt$, $k=1,2,\dots$ [p. 747, eq. (2.6)], which re-introduce inequality aversion *within* the worst-off type via the rank-dependent weight $p_k(t)$, thereby nesting pure-EOp ($k=\infty$, flat weights) and adding within-worst-type concern as $k\downarrow 1$.

**Mapping to my three sub-objects:** this normative opportunity notion **does not map** onto my access / ability / preference channels. Father's education is an exogenous *circumstance type*, not a feasible-set object; effort = within-type rank, not preference. **Explicit-in-source that it is Roemer-EOp; not-established (indeed, false) that it is my structural opportunity decomposition.** Do not import their "EOp" as my "opportunity."

### 5.2 The *structural* opportunity notion (the labour-supply model) â€” peripheral here, in the ESM

The only structural-availability signal in the main text is "quantity constraints on the distribution of hours" [p. 743] plus "stochastic â€¦ choice sets" [p. 749].

- **access** (hours / participation / region / occupation offers): the *hours* quantity-constraint language is an **access**-type object in spirit, but its form is **not in the main text** [verify against ESM]. Region, year, occupation offers: **not mentioned**.
- **ability** (wage technology; returns to education/experience; residual productivity): **not in the main text** [verify against ESM]. Note: education appears in this paper *only* as the **circumstance type variable (father's education)**, never (in the main text) as a structural wage return. Do not read their father's-education type as my education-based ability channel â€” different object, different person (parent vs own).
- **occupation as availability:** **not mentioned in the main text at all.** No occupation/`loc4` analogue; no sector/industry conflation to flag (because the topic does not arise).

**Cost-of-omission statement:** because this paper's *structural* opportunity mechanism is opaque in the main text, the paper gives me **no usable functional form** for my access/ability split. Its value to my Â§5 is *conceptual contrast* â€” it shows a respected alternative way to make a welfare evaluation "opportunity-sensitive" (Roemer types) that is orthogonal to my latent-jobs density â€” which I should explicitly distinguish from in my identification/normative sections.

---

## 6. Welfare object â€” and its place on my $W^1$â€“$W^6$ map

- **Does it compute welfare?** Yes â€” it is the central object.
- **Money-metric?** It is an **income-based** welfare object over **equivalent income**, defined as **household disposable income $\div \sqrt{\text{household size}}$** [p. 750]. It is *money-metric in the trivial sense that the argument is income*, but it is **NOT preference-respecting equivalent income**: the value of leisure is explicitly **excluded** and flagged as future work [p. 754 fn. 8; p. 760]. This is the decisive difference from my object.
- **Equivalent income / CV / EV / inclusive value?** None of these in my technical sense. No compensating/equivalent variation; no log-sum/inclusive-value welfare core; welfare reads the *equivalised disposable income* of the simulated optimal choice. **Ex-post-in-income**, not ex-ante-in-utility. The fact that the *behavioural* choice was simulated stochastically does not make the *welfare* object an inclusive value â€” they evaluate realised equivalised income.
- **Universal vs constrained set:** the welfare functional is defined over the realised equivalent-income distribution under a given tax rule; the "constrained feasible set" question (my universal-vs-constrained reference) does not arise in their welfare object because they evaluate income, not utility over a feasible set.
- **Reference:** the EOp functionals use a **within-type-rank reference** (the $\min_j$ over types at each quantile $t$) â€” the worst-off *type* at the matched effort level â€” not a reference *price/preference/bundle* in my King-style sense.
- **Discrete-choice subtleties:** handled on the *behavioural* side by stochastic simulation of choices; **not** carried into the welfare object (no log-sum aggregation of welfare, no Hicksian/Marshallian distinction stated).

**Locate on my $W^1$â€“$W^6$ map.**

> **Explicit boundary flag (per task instruction):** this paper does **not** contain my $W^1$â€“$W^6$ family. Its $W_1, W_2, W_3, W_\infty$ are **rank-dependent inequality-aversion variants of one (extended-Roemer-EOp) functional over equivalent *income***; my $W^1$â€“$W^6$ are **six different references on a compensationâ€“responsibility spectrum over preference-respecting equivalent *utility-income***. The superscripts/subscripts coincide *notationally* and the *idea of a family indexed by a normative parameter* coincides, but the **objects are different** and the indices do **not** correspond. Do **not** write "Aabergeâ€“Colombino compute $W^1$â€“$W^6$." They compute a different family.

- Their **inequality-aversion** index $k$ â†” my measures' *inequality aversion* is a **different axis** from my *responsibility-stance* axis (Independence-of-$y$ / Independence-of-$A$). Their family moves aversion to within-(worst-type) inequality; my family moves the compensation/responsibility reference. If anything, their $k$-axis is analogous to the choice of inequality index *inside* one of my measures, not to the choice of measure.
- **Verdict:** **adaptable in form, incompatible in object.** Usable as a *precedent for "report a parametric family of welfare functionals, not one number, and let the data decide which matters"* (directly supports my Exercise-A framing). **Not** usable as a source for my equivalent-income construction, my reference set, or my three-channel cut.

---

## 6b. Inclusive value and money-metric inversion  [extract if the paper uses a log-sum or an EV/CV]

**N/A in substance.** The paper does **not** use an inclusive value / log-sum as the welfare core, and does **not** obtain welfare by inverting an own-utility map to a money figure. Welfare is realised equivalised disposable income from the simulated optimum. The expectation over preference/choice-set stochasticity enters the *behavioural simulation* [p. 749], not an analytic-in-shocks welfare inversion. There is therefore **nothing here to relate to my analytic-in-shocks, importance-sampling inversion**. (Stated explicitly so the absence is on record, not mistaken for an oversight.)

---

## 7. Inequality / decomposition content  [three-way where relevant]

- **Inequality index:** the rank-dependent **$C_k$ family** [p. 745, eqs. (2.2)â€“(2.4)]: $C_1$ = Bonferroni coefficient, $C_2$ = **Gini**, $C_3$ = a higher-order variant; with $W_k = \mu(1-C_k)$ for the EO functionals [p. 745] and $W_k^* = W_\infty(1-C_k^*)$ for the extended-EOp functionals over the mixture distribution $F^*(x)=\max_i F_i(x)$ [p. 748, eqs. (2.7)â€“(2.9)].
- **Decomposition rule:** a **welfare = mean Ã— (1 âˆ’ inequality)** factorisation, $W_k = W_\infty(1 - C_k^*)$ [p. 748, eq. (2.8)]. This is an **efficiency/equity factorisation of a *single* welfare number into a level component and an inequality component** â€” reported in their Tables 4, 8, 9 as $W_\infty$ alongside $C_1^*, C_2^*, C_3^*$. It is **NOT** a Shapley/Shorrocks **source-component** decomposition, and it does **not** attribute inequality to factors/channels.
- **Counterfactual construction:** their counterfactuals are **alternative tax rules** (affine and three-parameter), not equalisation of a source channel. What is "varied" is the policy; what is "held fixed" is revenue (constant-revenue constraint) and the estimated behavioural model. Nothing is "zeroed out" in the source-attribution sense I use.
- **Order-independence / path-independence / exhaustiveness:** their levelÃ—inequality split is exact by construction ($W=\mu(1-C)$), but the path-independence properties that matter for *my* Shapley exercise are **not** at issue here because there is no multi-factor attribution.
- **Verdict (reusable for my three-way Shapley split?):** **No.** This paper is **not even a two-way source decomposition** in my sense â€” it is a level/inequality factorisation of one welfare functional, plus a *menu of functionals* indexed by inequality aversion and by EO-vs-EOp. To become my three-way access/ability/preference Shapleyâ€“Shorrocks split it would have to be **entirely re-built**: introduce structural channels, define channel-equalisation counterfactuals, and apply Shapley averaging over equalisation orders â€” none of which is present. **Cite it for the *family-of-functionals* idea and the EOp-vs-EO contrast, not for decomposition method.**

---

## 8. Identification and the separation of preferences from opportunities  [STRICT]

**The main text offers essentially nothing on structural identification** â€” the model and its identification are in the ESM. What I can say honestly:

- **What separates tastes from constraints in *their* model:** **Not stated in the main text** [verify against ESM]. The "quantity constraints on hours" remark [p. 743] implies the model distinguishes desired hours from available hours, but the identification argument is not given here.
- **Ability vs access within the opportunity side:** **Not addressed.** Their paper does not make my ability/access distinction at all; their "opportunity" is the Roemer circumstance/effort cut (Â§5.1), whose identification rests on the *observability of the circumstance* (father's education) and the *assumption that within-type rank = effort* [p. 746] â€” an **assumption**, not an estimated separation. That assumption is the paper's identifying normative stance, and it is exactly the kind of move a referee would interrogate.
- **Transport to my France pooled cross-section:** their identifying device for the *normative* cut â€” an **observed exogenous circumstance** (parental education) â€” **I do not have** in the EUROMOD engine-ready data. Their device for the *structural* model is opaque here. So this paper gives me **no transportable identification argument** for my preference-vs-opportunity or access-vs-ability separation.
- **Synthetic-recovery / parametric-identification:** **not discussed** in the main text. My baseline's reliance on synthetic recovery (not in-sample fit) has **no counterpart** stated here.

**Use for my identification note:** as a *foil*. Their responsibility cut is identified by an **assumption on an observed circumstance + a rank-as-effort convention**; mine is identified by **functional-form / structural restrictions on an estimated opportunity density, certified by synthetic recovery**. Stating this contrast strengthens my defence against the "your decomposition is mechanical" referee by showing my cut is *structural and recovery-tested*, where a respected EOp precedent rests on an explicit normative convention. Do **not** soften this; the contrast is the point.

---

## 9. Key results and magnitudes

Reported numbers (Italy 1993; 1,000 ITL; Ã·1.93627 for â‰ˆEUR) [pp. 750â€“759]:

- **Headline qualitative finding:** the Equality-of-Outcome (EO) criterion does **not** call for more redistribution than the Equality-of-Opportunity (EOp) criterion â€” contrary to a common prior. In their simulations EO never calls for redistribution (a universal lump-sum tax is EO-optimal across the rule classes), while only the *extended* EOp criterion, with enough within-worst-type inequality aversion, calls for positive marginal rates/transfers [pp. 758, 760, abstract p. 741].
- **EOp-optimal affine (two-parameter) rules** [Table 2, p. 750]: for $k\ge 3$ the optimum is a **pure lump-sum tax** ($t=0$, $c<0$); for $k\le 2$ a **high marginal rate with a positive transfer** (e.g. $k=1$: $t=.774$, $c=11{,}500$; $k=2$: $t=.637$, $c=9{,}500$).
- **Mechanism for the counterintuitive lump-sum result:** the **labour supply of the most disadvantaged type (type 1) is highly responsive**; under the lump-sum rule (zero marginal rate) type-1 hours rise most in percentage terms (e.g. +13.37% for type 1 under EOp2(3)), so efficiency gains for the worst-off can dominate unless within-type inequality aversion is high [Table 5, p. 753; discussion pp. 753â€“754].
- **Inequality magnitudes (illustrative):** under the 1993 system, $C_1^*=.426$, $C_2^*$ (Gini) $=.302$, $C_3^*=.242$ [Table 4, p. 753]; the EOp-optimal $k=1$ affine rule compresses these sharply ($C_2^*\approx.127$) at a cost in $W_\infty$ [Table 4, p. 753].
- **Equityâ€“efficiency trade-off, made explicit** [Table 8, p. 757]: e.g. moving to the Gini-EOp-optimal three-parameter rule lowers $W_\infty$ from 22,231 to 18,508 but cuts the Gini from .403 to .253, with the welfare functional rising on net.

**Benchmark value for my paper:** their *direction* â€” that responsibility-sensitivity does **not** mechanically imply more compression than outcome-egalitarianism, because behavioural responses interact with the worst-off â€” is a **plausibility prior** for my own results: I should not assume that my opportunity-compensating measures ($W^4/W^6$) will mechanically show more inequality than full-responsibility ($W^3$). Their magnitudes are *not* a numerical benchmark for my opportunity shares (different country, year, object, and decomposition).

---

## 10. Estimators, theorems, or formal results

No theorems with proofs are stated in the main text (the formal welfare-functional results are attributed to Mehran 1976, Yaari 1988, Aaberge 2001/2007). The reusable *formal constructions* are:

1. **Rank-dependent (generalised-Gini) welfare functional.**
   $$ W \;=\; \int_0^1 p(t)\, F^{-1}(t)\, dt, \qquad p_k(t)=\begin{cases}-\log t, & k=1\\ \tfrac{k}{k-1}\big(1-t^{\,k-1}\big), & k=2,3,\dots\end{cases} $$
   [p. 744 eq. (2.1); p. 745 eq. (2.2)]. Associated inequality $C_k = 1 - W_k/\mu$ [p. 745 eq. (2.4)].
   - *Assumptions:* a distribution $F$ of (equivalent) income with mean $\mu$; positive weight function $p(t)$ on $[0,1]$ (Yaari 1988 dual / Atkinson 1970 normative justification).
   - *Technique:* weight low quantiles more as $k\downarrow$; $k=2$ gives Gini, $k\to\infty$ gives the mean (inequality-neutral).
   - **Reusability verdict for my welfare/decomposition layer: YES, as my inequality index inside a measure.** The generalised-Gini $C_k$ is a clean, axiomatically justified family I can use as the inequality functional $I(\Omega^k)$ on each of my $W^1$â€“$W^6$ distributions, and reporting across $k$ is a cheap robustness axis. **Maybe** for the welfare-functional framing of Exercise A. **Not** the source decomposition.

2. **Extended-EOp functional over the type-mixture distribution.**
   $$ W_k^{*} \;=\; \int_0^1 p_k(t)\,\min_j F_j^{-1}(t)\, dt, \qquad F^{*}(x)=\max_i F_i(x), \qquad W_k^{*}=W_\infty(1-C_k^{*}) $$
   [p. 747 eq. (2.6); p. 748 eqs. (2.7)â€“(2.9)].
   - *Assumptions:* types $j$ defined by an observed circumstance; within-type rank = effort.
   - **Reusability verdict: NO for my JMP as a welfare object** â€” it requires an observed circumstance/type variable I do not use, and it embeds the Roemer worst-off-type logic, which is not my compensationâ€“responsibility reference logic. Useful only as the *contrast object* in my normative-interpretation discussion.

---

## 11. Robustness and specification sensitivity

What they vary and what it teaches my robustness section:

- **Tax-rule class:** two-parameter affine vs three-parameter piecewise-linear [Tables 2/7]. Lesson: their headline (lump-sum EOp-optimality for $k\ge 3$) is *partly an artefact of the restricted two-parameter class* â€” the three-parameter class restores positive top rates even at higher $k$ [pp. 756â€“757]. **Transfer to me:** the *richness of the admissible set* changes the conclusion â€” analogous to my warning that the *reference set* / *measure menu* richness can change the apparent opportunity share; report the menu, do not over-read one measure.
- **Inequality-aversion parameter $k$:** $k\in\{1,2,3,\infty\}$ throughout. Lesson: results are *highly sensitive to $k$* [p. 750: "the optimal policy is very sensitive to the value of $k$"]. **Transfer:** I should report my decomposition under more than one inequality index ($C_2$ Gini plus at least one more), since the generalised-Gini aversion can move shares.
- **EO vs EOp criterion:** the *normative* axis (Section 4, Tables 9, 11). Lesson: the normative stance can flip the redistribution conclusion. **Transfer:** directly supports my Exercise-A thesis that the *stance* (my $W^k$ choice) is itself an object of interest, not a nuisance to be fixed.
- **Lump-sum feasible vs not feasible:** Section 5 (Tables 10, 11) re-optimises forbidding lump-sum taxes. Lesson: a single *implementability constraint* changes the optimum qualitatively. **Transfer:** my reference-coverage / EUROMOD-feasibility gate is the analogue â€” what is *feasible to evaluate* constrains what is reportable.
- **What they flag as missing (a robustness debt):** **leisure is not valued** in the welfare object; they state the policy prescriptions "might change" once leisure is valued [p. 754 fn. 8; p. 760]. **Transfer (important):** this is precisely the gap my **preference-respecting** equivalent income closes â€” I should cite this as the literature's own acknowledgement that income-only welfare is incomplete for labour-supply welfare analysis.
- **Sample-size / draw-count / starts / circumstance-partition sensitivity:** **Not in the main text** [verify against ESM]. So this paper gives me nothing on effective-sample-size or multistart stress-testing.

---

## 12. What I can cite this paper for

- That **EOp / responsibility-sensitivity does not mechanically imply more redistribution than outcome-egalitarianism**, and that the comparison is an *empirical* question resolved by microeconometric simulation [abstract p. 741; pp. 758, 760]. **(explicit-in-source)**
- That a **structural labour-supply model with stochastic choice sets and hours quantity constraints** can be used to evaluate responsibility-sensitive social objectives via simulation [pp. 743, 749]. **(explicit-in-source)**
- The **generalised-Gini / rank-dependent welfare family** $W_k$ and inequality family $C_k$ ($k=1$ Bonferroni, $k=2$ Gini, $k=3$, $k=\infty$ utilitarian) as an axiomatically grounded *menu of welfare functionals* over a money-metric distribution [pp. 744â€“745]. **(explicit-in-source)**
- That **equivalent income = household disposable income $/\sqrt{\text{household size}}$** is a standard equivalisation in this literature [p. 750]. **(explicit-in-source)** â€” though my unit is the household and intra-household equivalisation is deferred, so use as background.
- That **labour-supply responsiveness of the worst-off interacts with the optimal degree of redistribution** [Table 5, pp. 753â€“754]. **(explicit-in-source)** â€” supports my caution against assuming a monotone measureâ†’inequality relationship.
- As a **precedent in the Aabergeâ€“Colombino tradition** that my structural welfare programme extends, and as a **foil** whose responsibility cut (Roemer circumstance/effort on parental education) differs from my structural access/ability/preference cut.

---

## 13. What I should NOT cite this paper for  [overclaim risks]

- **Three-way (access/ability/preference) decomposition.** This paper has **no** source-component decomposition at all â€” only a levelÃ—inequality factorisation $W=W_\infty(1-C^*)$ and a *menu* of functionals. Do not attribute any channel decomposition to it. **(boundary flag: it is not even two-way in my sense)**
- **Preference-respecting equivalent income.** Its welfare object is **income-only**; leisure is explicitly excluded [p. 754 fn. 8]. Do not cite it for a King/Fleurbaey-style money-metric utility. **(ex-post / income object presented as my ex-ante preference-respecting object â€” do not)**
- **My $W^1$â€“$W^6$ family.** Their $W_1$â€“$W_\infty$ are **inequality-aversion variants of one extended-EOp income functional**, not my six compensationâ€“responsibility references. Notational coincidence only; **do not write that they compute $W^1$â€“$W^6$.** **(explicit boundary flag, per task)**
- **A structural opportunity *density* over latent jobs.** Their "opportunity" is Roemer circumstance/effort (parental education / within-type rank); their structural availability mechanism (hours quantity constraints) is opaque in the main text. Do not cite it as a latent-jobs opportunity mechanism analogous to my $g$. **(opportunity-notion conflation flag)**
- **Occupation/sector/industry.** The paper does not treat occupation, sector, or industry; there is no `loc4` analogue and no NACE content. Do not cite it on any occupation-as-access point. **(silence, not support)**
- **Random-opportunity framing.** N/A here â€” the paper does not frame opportunities as random; do not import any "RO" reading from it. My opportunities are deterministic regardless.
- **Identification of preferences vs opportunities.** The structural identification is in the ESM and not stated in the main text; do not cite the *article* for an identification argument. **(not-established here)**
- **Theory-paper boundary.** This is an *empirical/simulation* paper; it is unrelated to the companion **Haydarâ€“Maniquet** axiomatic paper. Never attribute the Haydarâ€“Maniquet axioms/characterisation/proofs to it, and never let its presence blur the JMP-vs-theory-paper boundary. The $W^1$â€“$W^6$ *characterisation* is Haydarâ€“Maniquet's, **not** Aabergeâ€“Colombino's. **(theory-paper boundary flag)**

---

## 14. Direct quotes worth citing

(Short, verbatim, page-numbered; for my own notes.)

1. "the EOp criterion does not necessarily imply less redistribution than the EO criterion" â€” p. 742.
2. "circumstances â€¦ attributes of the environment of the individual â€¦ 'beyond her control'" â€” p. 746.
3. "a model of labour supply that provides a simultaneous treatment of partners' decisions" â€” p. 743.
4. "the utility functions (and choice sets) of the underlying micro-econometric model(s) are stochastic" â€” p. 749.
5. "When accounting for the value of leisure â€¦ the policy prescriptions might change" â€” p. 754 (fn. 8).

---

## 15. Open questions and risks for my draft

- **Leisure-valuation gap (their admitted debt â†’ my contribution).** Their explicit caveat that income-only welfare may mislead once leisure is valued [p. 754 fn. 8; p. 760] is a *motivating hook* for my preference-respecting object â€” but it is also a *risk*: a referee may ask whether my preference-respecting welfare merely re-labels the same equity/efficiency tension they already flagged. I must show my decomposition delivers *new attribution* (access vs ability vs preference), not just a leisure-augmented level.
- **Responsibility-cut comparability.** Their cut (observed circumstance + rank-as-effort) is *transparent and assumption-light to state*; mine (structural channels, recovery-certified) is *richer but heavier to defend*. The draft should pre-empt "why not just use a Roemer circumstance partition?" â€” answer: I have no clean exogenous circumstance in EUROMOD, and the responsibility-relevant object here is the *feasible job set*, which is latent, not an observed type.
- **Menu-as-headline risk, corroborated.** Their $k$-sensitivity [p. 750] and EO-vs-EOp divergence support my Exercise-A bet that the *stance* matters â€” but their case also shows the bet can fail to "grab" (the menu can agree). This reinforces my welfare-spec build-order gate: observe the spread before claiming sensitivity is the result.
- **No inference content.** The paper reports no standard errors / bootstrap on the welfare numbers in the main text; it gives me no precedent for my cluster-robust per-component CIs. I cannot lean on it for inference design.
- **ESM dependence.** Anything I might want about their *estimator, choice set, opportunity density, or identification* requires the ESM. If those become load-bearing for positioning, pull the ESM (and the companion ACS 1999) as separate sources â€” do **not** infer them from this file.

---

## 16. TL;DR for retrieval

Aaberge & Colombino (2012, *J Popul Econ*) use a stochastic-choice-set structural labour-supply model (Italy 1993 SHIW; singles + couples) to find second-best optimal income-tax rules under an **extended Roemer EOp** criterion â€” a rank-dependent generalised-Gini *family* $W_1,\dots,W_\infty$ over **equivalent income** (leisure excluded), with types = father's education and effort = within-type rank â€” and find EOp need not imply more redistribution than EO. For my JMP it is a **welfare-layer and normative-interpretation** precedent (a *menu of welfare functionals*, and a responsibility-sensitive ethos) and a **foil** for my access/ability/preference cut; it is **not** a source for preference-respecting equivalent income, a latent-jobs opportunity density, my $W^1$â€“$W^6$ family, or any three-way Shapley decomposition, and its structural/identification microstructure lives in an ESM not present here.
# Bhattacharya 2015 â€” Nonparametric Welfare Analysis for Discrete Choice

> Extraction produced against `JMP_T1_exhaustive_extraction_prompt_v2.md`.
> Source of truth: the attached PDF (Econometrica 83(2), 617â€“649). Project
> anchors (`JMP_project_state_v1.md`, `JMP_welfare_spec_v5.md`) used only for
> relevance judgments. Page numbers refer to the journal pagination (617â€“649)
> printed on the PDF. Tags used below: **[explicit]** = stated in the source;
> **[analogy]** = derived by analogy to my JMP, not in the source;
> **[not-established]** = the source does not establish this; **[verify]** =
> metadata or detail I could not confirm from the PDF text.

---

## 0. Metadata

- **BibTeX key:** Bhattacharya2015 [verify â€” key not specified in source]
- **Authors:** Debopam Bhattacharya (Dept. of Economics, University of Oxford). [explicit, p. 649]
- **Year:** 2015 (manuscript received June 2014; final revision November 2014). [explicit, p. 649]
- **Outlet:** *Econometrica*, Vol. 83, No. 2 (March 2015), pp. 617â€“649. [explicit, p. 617]
- **DOI/URL:** 10.3982/ECTA12574. [explicit, p. 617]
- **PDF filename:** `Bhattacharya_2015_Nonparametric_Welfare_Analysis_for_Discrete_Choice.pdf`. [explicit, upload]
- **Tier:** T1A.
- **JMP blocks served:** welfare (money-metric EV/CV from discrete choice), identification (preference heterogeneity of unspecified dimension), estimation (the parametric MNL welfare integrator as a special case), motivation/defence (the "your decomposition is mechanical / driven by functional form" referee). It does **not** serve the opportunity-mechanism, decomposition, or normative-interpretation blocks directly. [analogy, on relevance]

---

## 1. One-paragraph relevance to my JMP

This is the canonical statement that money-metric welfare for discrete choice â€” the marginal distributions of equivalent variation (EV) and compensating variation (CV) under a price change â€” is point-identified as a closed-form functional of conditional choice probabilities, under arbitrary, unspecified-dimension preference heterogeneity and without specifying the utility functional form. [explicit, pp. 617â€“618] For my JMP it speaks almost entirely to the **preference** channel and to the welfare-object construction: it is the cleanest reference for the claim that my equivalent-income objects are *preference-respecting* and need not identify the full heterogeneity distribution to be well-defined, and it is my strongest defence against the referee who suspects my welfare numbers are artefacts of the Boxâ€“Cox functional form. Its negative result for ordered choice (and the link to Hausmanâ€“Newey set-identification for continuous choice) is the analytic backdrop for why a *discrete* unordered job menu with alternative-specific budgets is a favourable setting for welfare measurement. [explicit, pp. 617â€“618, 634] It says nothing about an opportunity mechanism, heterogeneous feasible sets, or a three-way decomposition; on those it is silent and must not be over-read.

---

## 2. Data and setting

**None.** The paper is purely theoretical/methodological; there is no empirical dataset, sample unit, or country. [explicit â€” the introduction frames the microdata setting abstractly (p. 617) and Â§2 onward is formal; the only computation is a worked multinomial-logit integrator (pp. 632â€“633)] The "setting" is an individual with observed income $Y$ and observed prices $P$ choosing a discrete good, with covariates suppressed for notational clarity ("the entire analysis should be thought of as implicitly conditioned on these observed covariates"). [explicit, p. 621]

**Transport to my France pooled 2015â€“2017 EUROMOD cross-section.** The *theory* transports: it is a single-cross-section, one-time-choice result and explicitly states this is the setup of all existing empirical welfare-analysis work it is aware of. [explicit, p. 634, "Sequential Choice"] What I do **not** have / what differs:

- The paper's welfare experiment is a **price change** for a good. My JMP has **no price change**: my welfare object is a *level* (an ex-ante equivalent income against a reference state), not a CV/EV for a counterfactual price movement. This is the single most important mapping caveat â€” see Â§6. [analogy]
- The paper requires **own-price and income variation** across observed units to trace the welfare CDF nonparametrically. [explicit, p. 631, "Computational Issues"] My budget variation comes from the EUROMOD tax-benefit map across alternatives, not from exogenous price variation; I do not attempt nonparametric identification.
- The paper assumes a **common, universal choice set** (same menu for every consumer). [explicit â€” Â§2.2 sets up a fixed alternative set $\{0,1,\dots,J\}$ common to all, p. 629] My JMP's defining feature is *heterogeneous feasible sets*; the paper has no analogue.
- No panel, no administrative match, no external instrument, no vacancy/offer data appears or is required (consistent with my own data constraints; the paper simply does not need them for its identification result). [explicit]

---

## 3. Model and objects (map object-by-object to mine)

| Their object | Their definition (source) | My object | Match? |
|---|---|---|---|
| Choice set $\{0,1,\dots,J\}$, alternative-specific prices $p_j$ | Mutually exclusive discrete alternatives, common to all consumers (p. 629) | latent-jobs set $\mathcal C_i$ | **Partial.** Both are unordered discrete menus; theirs is universal/common, mine is household-specific and feasibility-constrained. [analogy] |
| Deterministic-plus-heterogeneity utility $U_j(Y-p_j,\eta)$ | Continuous, strictly increasing in numeraire; $\eta$ of unknown dimension/distribution, arbitrary entry (Assumption 1, p. 622; Assumption 2, p. 630) | preference utility $v$ (Boxâ€“Cox in $c,\ell$, taste-shifters) | **Object-analogous, assumptions much weaker.** Theirs imposes only monotonicity+continuity in the numeraire; mine is a parametric Boxâ€“Cox. [explicit for theirs; analogy for the map] |
| Budget: $W + PQ = Y$, consumption $= Y - p_j$ | Numeraire after discrete purchase (p. 621) | EUROMOD disposable income $c_j = $ `ils_dispy_real` at alternative $j$ | **Analogous role, different map.** Theirs is linear price-subtraction; mine is the nonlinear tax-benefit transform. [analogy] |
| Opportunity / availability mechanism | **None.** Universal choice set; all welfare variation is preference heterogeneity. (p. 632, summary; Â§2.2 setup) | opportunity density $g$ (hours / wage-ability / market / occupation-access) | **No analogue in the source.** [explicit â€” the paper has no $g$] |

**Separation of hours / wage(ability) / market / occupation channels:** absent. The paper has no opportunity mechanism, hence no channel split. [explicit]

**Does any attribute enter BOTH utility and an opportunity mechanism?** Not applicable â€” there is no opportunity mechanism, so the double-entry hazard I track does not arise here. The paper's only "all else" object is the heterogeneity vector $\eta$ inside utility. [explicit]

**Key structural difference to flag for my draft:** the paper's welfare object is generated by *price variation on a fixed menu*; mine is generated by *menu variation across households at fixed policy*. The identification logic (slice the population by reservation price; sweep prices to trace the CDF) does not port to my setting, where I am not perturbing a price. [analogy]

---

## 4. Estimation method

The paper is **about identification, not estimation**; a full inference treatment is deferred to a companion (Bhattacharya and Lee 2014, unpublished at the time). [explicit, pp. 632â€“633, "Inference"]

- **Likelihood / estimator:** none for the main results. The identification result expresses welfare CDFs as functionals of the structural choice probability $\bar q(\cdot,\cdot)$ (the "average structural function" in the sense of Blundellâ€“Powell 2003). [explicit, p. 622] $\bar q$ is to be recovered by nonparametric regression of the buy indicator on price and income when these are independent of $\eta$ given covariates, or via control functions under endogeneity. [explicit, p. 622]
- **Choice-set construction:** fixed, common, finite menu; **no sampling of alternatives, no proposal density.** [explicit â€” Â§2.2]
- **Proposal / prior correction:** **none.** There is no sampling-of-alternatives step, so no $\log\pi$ correction exists or is needed. [explicit] (See Â§4b.)
- **Normalisation / scale:** in the parametric MNL example, utilities $U_j(a,\eta)=\beta_j a + \varepsilon_j$ with i.i.d. extreme-value $\varepsilon$ independent of price and income; the $\beta$'s are estimable by ML. [explicit, p. 632, eq. (23)] No explicit scale-normalisation discussion beyond the standard logit form.
- **Numerical method:** for the parametric case, the mean-welfare integral over the price interval is computed by averaging the estimated integrand over a uniform grid $r_k = p_{10} + \frac{k}{K+1}(p_{11}-p_{10})$. [explicit, pp. 632â€“633, eq. after (24)]
- **What pins preferences vs the opportunity mechanism:** not applicable â€” there is no opportunity mechanism to separate from preferences. The paper's separation problem is instead "welfare distribution vs heterogeneity distribution," and its result is that the former does not require the latter. [explicit, Remark 1 p. 627; Appendix example pp. 646â€“647]

**Verdict (reusable for my RURO/JAX pipeline?):** **No for the estimator** (there is none), **Yes for one downstream step** â€” the parametric MNL welfare integrator (eqs. 23â€“24, p. 632) is the textbook template for integrating a closed-form choice-probability expression over a price/parameter grid, and my analytic-in-shocks log-sum welfare core is a relative of it. But I do **not** reuse its nonparametric identification machinery, because I do not perturb a price and I do estimate a parametric structure. [analogy]

## 4b. Proposal / sampling-of-alternatives correction

**Not present.** The paper uses a fixed, common, fully enumerated choice set; there is no sampling of alternatives, no proposal density $\pi$, no individualised draw, and therefore no McFadden-style correction and no per-alternative $\log\text{prior}$. [explicit â€” confirmed by the absence of any sampling step in Â§Â§2.1â€“2.2 and by the direct enumeration in the MNL example, eq. (23)]

**Relation to my importance-sampling welfare integrator and proposal-individualisation concern:** the paper offers **no** guidance on the $-\log\pi$ correction, on partly-individualised proposals, or on effective-sample-size diagnostics, because it never samples alternatives. My proposal-correction obligations and my ESS finding are entirely outside this paper's scope; it should not be cited on them. [explicit absence â†’ not-established for my purposes]

---

## 5. Opportunity mechanism  [MOST IMPORTANT]

**There is no explicit opportunity mechanism.** The choice set is a fixed, universal menu identical for every consumer; feasibility, offer probabilities, reservation-wage/participation restrictions, and circumstance-varying availability are **not modelled**. All cross-individual variation in welfare arises from preference heterogeneity $\eta$, with prices and income observed and (conditionally) independent of $\eta$. [explicit â€” Â§2 setup; summary p. 632]

Mapping to my three sub-objects:

- **access** (hours / market-participation / region / year / occupation offers): **absent.** [explicit]
- **ability** (wage technology; returns to education/experience; residual dispersion): **absent.** [explicit]
- **occupation as availability vs something else:** not present; no occupation object, hence **no sector/industry conflation risk** to flag. [explicit]

**Functional form of the mechanism:** N/A.

**Cost of this omission for my access/ability/preference decomposition.** Because the paper holds the feasible set fixed and common, it cannot â€” even in principle â€” separate access or ability from preference; everything it calls "heterogeneity" lives inside utility ($\eta$) and is, in my taxonomy, **preference** (with the important caveat that the paper's $\eta$ is *unrestricted* and could in a richer reading absorb what I would call ability/access if those were folded into utility). The paper is therefore a model of the *limiting case my JMP argues against*: the universal-choice-set world in which opportunity differences are invisible and would be loaded entirely onto tastes. This makes it useful **as the foil** for sub-question 1 ("do models without constrained opportunities overstate preference heterogeneity?") â€” Bhattacharya formalises welfare in exactly the world where that overstatement is unavoidable because no opportunity object exists. [analogy â€” the paper does not itself make this framing; it is my use of it]

---

## 6. Welfare object â€” and its place on my $W^1$â€“$W^6$ map

**Does it compute welfare?** Yes. The objects are the **marginal distributions of EV and CV** (and their means) for a discrete *price change* $p_0 \to p_1$. [explicit, Theorems 1â€“2, pp. 626, 631]

- **Money-metric?** Yes â€” EV and CV are income-compensation measures (units of the numeraire). [explicit, p. 617]
- **Equivalent income / equivalent variation?** It is **Hicksian** EV/CV for a price change, *not* an equivalent-income level against a reference state. [explicit] This differs from my object, which is an equivalent-income *level* against a normative reference set. [analogy]
- **Compensating / equivalent variation?** Both, defined as the income $S$ solving the indifference equations (5)â€“(6) for binary choice and (15)â€“(16)/(17)â€“(18) for multinomial. [explicit, pp. 624â€“625, 630]
- **Universal vs constrained feasible set?** **Universal** common set. [explicit] My welfare object is over a **constrained, household-specific** set. This is a fundamental mismatch. [analogy]
- **Reference price / preference / bundle / set:** the reference is the *post-change* (or pre-change) price situation under the consumer's **own** preferences; there is no reference-preference swap and no reference *set* â€” the menu is fixed. [explicit]
- **Discrete-choice subtleties:** handled via the composite-outside-option reduction â€” multinomial welfare for a price change in alternative 1 is reduced to a binary problem against $U^*(p_{-1},y,\eta)=\max\{U_0,U_2,\dots,U_J\}$, then Theorem 1 is applied (Theorem 2, Assumption 2). [explicit, pp. 629â€“631] Marshallian vs Hicksian: average EV equals the change in average Marshallian consumer surplus *even without quasilinearity*; average CV $\ge$ average EV for a normal good. [explicit, Corollary 1 and implications, p. 628] Integration over unobserved heterogeneity is the population integral $\int \cdot\, dF(\eta)$, and crucially does **not** require $F$ to be known or identified. [explicit, Remark 1, p. 627]
- **Ex-ante vs ex-post:** the welfare object is **per-type then aggregated** â€” for each $\eta$ the individual EV/CV is a deterministic number (Lemmas 1â€“2), and the paper reports the *marginal distribution* of that number across $\eta$. [explicit, pp. 625â€“626] There is **no inclusive-value / expected-maximum (log-sum) welfare core** in the main results: the extreme-value shocks appear only in the parametric MNL *example* (eqs. 23â€“24), not in the identification theorems. This is the opposite of my **ex-ante log-sum** stance. [explicit; contrast is analogy]

**Locating the paper on my $W^1$â€“$W^6$ family map.** The paper does **not** contain, reference, or correspond to my $W^1$â€“$W^6$ family, and contains no Ind-$y$ / Ind-$A$ classification. [explicit absence â†’ **the source does NOT contain $W^1$â€“$W^6$**] Any correspondence is by analogy only: Bhattacharya's EV/CV use the consumer's *own* preferences and the *own* (universal) menu, so in spirit they sit at the **Full-Responsibility / own-everything** corner that my $W^2$/$W^3$ occupy â€” the consumer is evaluated against her own choice situation with no compensation of pay or set. But this is a loose analogy: his object is a *change* measure (a difference induced by a price move), not a *level* against a reference, so it is not literally any of my six. [analogy â€” explicitly flagged as not-established in the source]

**Verdict:** **Adaptable in spirit, not directly usable.** Usable as authority for "preference-respecting money-metric welfare is well-defined and computable without identifying the heterogeneity distribution." Not usable as a template for my ex-ante, reference-level, constrained-set equivalent income. [analogy]

## 6b. Inclusive value and money-metric inversion

- **Inclusive value (log-sum / expected maximum) as welfare core?** **No.** The identification results do not use a log-sum welfare core; welfare per type is obtained from the utility-indifference equations directly, then aggregated to a distribution. [explicit] The extreme-value structure enters only in the parametric MNL worked example (eq. 23), and even there the welfare *integral* is over the price grid, not an expected-maximum over shocks reported as the welfare number. [explicit, eqs. 23â€“24]
- **Money-metric by inversion of an own-utility map?** **Yes, conceptually, at the individual level.** The switcher's EV/CV is literally an inverse-utility solve: e.g. $S^{EV}=y-p_0-U_1^{-1}(U_0(y,\eta),\eta)$ for the switching type (Lemma 1, case ii), and the CV switcher solve $S^{CV}=U_0^{-1}(U_1(y-p_0,\eta),\eta)-y$ (Lemma 2, case ii). [explicit, p. 625] This one-dimensional inversion of an own-utility map is the **same kind of operation** as my bracketing root-solve of the own-utility map for $W^k$. [analogy] The difference: the paper inverts to recover a *price-change compensation*, then aggregates the closed form into choice probabilities; I invert to recover a *level* against a reference and integrate the shocks analytically via the log-sum.
- **Expectation over shocks analytic vs simulated?** In the nonparametric results there are no parametric shocks; the population integral over $\eta$ is collapsed analytically into choice probabilities $\bar q$ (no simulation). [explicit] In the MNL example the choice probability is the closed-form logit (analytic in the EV1 shocks), and only the price-grid integral is done numerically. [explicit, eqs. 23â€“24] This is **consistent in flavour** with my analytic-in-shocks importance-sampling inversion, and is a fair citation for "the expectation over the extreme-value shocks can be taken in closed form." [analogy]

---

## 7. Inequality / decomposition content

- **Inequality index:** **none.** The paper produces *welfare distributions* (CDFs of EV/CV) and their means, but applies **no** inequality index (no Gini, MLD, Theil, variance of logs, Atkinson). [explicit]
- **Decomposition rule:** **none.** There is no Shapley, Shorrocks, factor-component, subgroup, RIF, or regression decomposition. [explicit]
- **Counterfactual construction:** the only counterfactual is a *price change* $p_0\to p_1$; nothing is "equalised," "neutralised," or "zeroed out" across individuals in a decomposition sense. [explicit]
- **Order/path-independence/exhaustiveness:** N/A (no decomposition).

**Verdict (reusable for my three-way access/ability/preference Shapleyâ€“Shorrocks split?):** **No.** The paper supplies the *welfare distribution* that a decomposition would operate on, but contributes no decomposition machinery and is neither two-way nor three-way. To reach my three-channel split one would have to (i) replace the price-change CV/EV with my ex-ante reference-level equivalent income, (ii) introduce the opportunity object the paper lacks, and (iii) add the Shapleyâ€“Shorrocks counterfactual layer entirely from elsewhere (Shorrocks 2013 etc.). The paper is upstream of, and orthogonal to, the decomposition. [analogy]

---

## 8. Identification and the separation of preferences from opportunities  [STRICT]

**What the paper identifies and how.** The marginal distributions of EV/CV are point-identified as closed-form functionals of the conditional choice probabilities $\bar q(p,y)$ under a *single substantive assumption*: utilities are continuous and strictly increasing in the numeraire (Assumption 1 / Assumption 2). [explicit, pp. 622, 630] The identifying source is **own-price and income variation** that sweeps the population's reservation-price boundary: $\Pr\{S^{EV}\le a\}=1-\bar q(p_0+a,y)$ exploits that the fraction not buying at price $p_0+a$ is exactly the fraction with reservation price below $p_0+a$. [explicit, Theorem 1 + "Some Intuition," p. 626]

**Preferences vs opportunities:** the paper does **not** separate preferences from opportunities, because it has no opportunity object. What it *does* establish â€” and this is the load-bearing import for my identification note â€” is a different, stronger separation: **welfare distributions are identified without identifying the preference-heterogeneity distribution, or even its dimension.** [explicit, Remark 1 p. 627; Appendix worked example pp. 646â€“647, where two different $\eta_1$ distributions (uniform vs degenerate) produce identical choice probabilities and hence identical, point-identified welfare distributions, yet the dimension of $\eta$ is itself unidentified.]

**Ability vs access within the opportunity side:** N/A â€” no opportunity side. [explicit]

**Transport to my France pooled cross-section (no panel, no external instrument):** The reassuring transportable lesson is that **I do not need to identify my full heterogeneity distribution to have a well-defined, preference-respecting money-metric welfare object** â€” a direct shield for the "your welfare numbers are a functional-form artefact" referee. [analogy, grounded in explicit Remark 1 / Appendix] The non-transportable part: Bhattacharya's *nonparametric* identification needs continuous own-price variation that I do not have and do not invoke; my identification of the *structural* opportunity/preference split rests instead on parametric functional-form restrictions and is **certified by synthetic recovery, not in-sample fit** (per project state Â§3.7, Â§8). The honest statement for my draft is: Bhattacharya licenses the welfare-*object* well-definedness under unrestricted heterogeneity; it does **not** license my *structural separation* of access/ability/preference, which is a parametric identification claim the paper neither makes nor supports. [analogy]

**On the "mechanical decomposition" referee, with a caution.** The paper's Remark 3 (pp. 638â€“639) is a double-edged sword I must cite carefully: it shows that for *ordered* choice a parametric model would *appear* to point-identify the welfare distribution, but that this apparent identification is "driven entirely by functional form assumptions" and is "artificial." [explicit, p. 639] This is exactly the charge a referee could level at my parametric RURO decomposition. I can cite Bhattacharya to show I am *aware* of the functional-form-identification hazard and to motivate my synthetic-recovery certification as the answer; I must **not** cite him as having *cleared* parametric structural models of the charge â€” he does the opposite for the ordered case. [analogy â€” strict]

---

## 9. Key results and magnitudes

No empirical magnitudes (no data). The substantive results are analytic:

- **Theorem 1 (binary):** for a price rise $p_0\to p_1$, $\Pr\{S^{EV}\le a\}=1-\bar q(p_0+a,y)$ and $\Pr\{S^{CV}\le a\}=1-\bar q(p_0+a,y+a)$ on $[0,p_1-p_0]$. [explicit, p. 626]
- **Corollary 1:** $\mu^{EV}(y,p_0,p_1)=\int_{p_0}^{p_1}\bar q(p,y)\,dp$ = change in average Marshallian consumer surplus (no quasilinearity needed); $\mu^{CV}=\int_{p_0}^{p_1}\bar q(p,y+p-p_0)\,dp$. [explicit, p. 628]
- **Implications:** for a normal good, $E(S^{EV})\le E(S^{CV})$; deadweight-loss formulas for a per-unit tax follow. [explicit, p. 628]
- **Theorem 2 (unordered multinomial):** same CDF forms with $\bar q_1$ (composite outside option). [explicit, p. 631]
- **Negative result (ordered choice, $\ge 3$ alternatives, uniform unit price):** EV/CV distributions are **not** nonparametrically point-identified; linked to Hausmanâ€“Newey (2014) set-identification for continuous choice as a limiting case. [explicit, Â§3, pp. 634â€“639]
- **Appendix example:** heterogeneity dimension unidentified yet welfare distributions point-identified. [explicit, pp. 646â€“647]

Benchmarking value for my own opportunity-share / welfare-spread plausibility: **none** â€” no shares or spreads are reported. [explicit]

---

## 10. Estimators, theorems, or formal results

For each, statement (near-verbatim in LaTeX), assumptions, technique, reusability verdict.

**Assumption 1.** For each $\eta$, $U_0(a,\eta)$ and $U_1(a,\eta)$ are continuous and strictly increasing in $a$; inverses $U_j^{-1}(b,\eta)$ are uniquely defined. [explicit, p. 622]
*Technique/role:* the sole substantive restriction; guarantees the inverse-utility solves are well-defined. *Reusability:* **yes** â€” my Boxâ€“Cox utility satisfies continuity+monotonicity in consumption, so my one-dimensional inversion inherits the same well-definedness guarantee. [analogy]

**Lemma 1 (EV, three cases).** Under Assumption 1: (i) non-buyers at $p_0$ â†’ $S^{EV}=0$; (ii) switchers â†’ $S^{EV}=y-p_0-U_1^{-1}(U_0(y,\eta),\eta)$; (iii) buyers at both prices â†’ $S^{EV}=p_1-p_0$. [explicit, p. 625]
*Reusability:* the *form* (welfare is a piecewise inverse-utility object) is instructive; not directly portable (price-change object). [analogy]

**Lemma 2 (CV, three cases).** Symmetric, with $S^{CV}=U_0^{-1}(U_1(y-p_0,\eta),\eta)-y$ for the switching case. [explicit, p. 625] Same verdict.

**Theorem 1.** Statement as in Â§9. [explicit, p. 626]
*Technique (3â€“5 bullets):* (a) per-type welfare from Lemmas 1â€“2; (b) the event $\{S\le a\}$ maps to a no-purchase event at a shifted price/income; (c) aggregate over $F(\eta)$, which collapses to $\bar q$; (d) point masses at $0$ and $p_1-p_0$. *Reusability:* **maybe** for the welfare *integrator* idea (express welfare via choice probabilities), **no** for the price-change identification. [analogy]

**Theorem 2.** Multinomial extension via composite outside option $U^*=\max\{U_0,U_2,\dots,U_J\}$ under Assumption 2 (all $U_j$ continuous, strictly increasing). [explicit, pp. 630â€“631]
*Reusability:* the composite-max reduction is a clean device; my log-sum core already aggregates over the whole menu analytically, so I do not need it, but it is a citable precedent for handling the multinomial structure. [analogy]

**Corollary 1.** As in Â§9. [explicit, p. 628] *Reusability:* the Marshallian-surplus equivalence is a teaching point, not used in my pipeline. [analogy]

**Section 3 negative result + Remark 3.** Ordered-choice non-identification; parametric "identification" is functional-form artefact. [explicit, pp. 634â€“639] *Reusability:* **yes, as a cited caution** in my identification section (see Â§8). [analogy]

---

## 11. Robustness and specification sensitivity

The paper is analytic, so "robustness" is about identification boundaries rather than estimation stress-tests:

- **Monotonicity of the CDF:** requires $\bar q(p_0+a,y)$ (EV) and $\bar q(p_0+a,y+a)$ (CV) nonincreasing in $a$; these follow from Assumption 1 and can be imposed or tested after estimating an unrestricted $\bar q$. [explicit, pp. 627â€“628]
- **Endogenous income:** control functions recover $\bar q$; Remark 2 distinguishes the marginal welfare distribution at hypothetical income $y$ (the parameter of interest) from the conditional distribution for the subpopulation with realised income $y'$ (an ATE-vs-ATT analogy). [explicit, pp. 622, 633]
- **Parametric vs nonparametric reporting:** the author advises reporting both parametric (e.g. mixed logit) and nonparametric welfare numbers and examining sensitivity to smoothing. [explicit, p. 633]
- **Out-of-support prices / limited price variation:** if hypothetical prices lie outside the observed range, or $P_1$ varies too little, one must either go parametric or only *bound* mean EV/CV; the conclusions of Theorems 1â€“2 are unaffected, but $\bar q$ at out-of-range points cannot be obtained nonparametrically. [explicit, p. 631]

**What this informs in my work:** (i) the parametric-vs-checked discipline echoes my synthetic-recovery gate; (ii) the "limited variation â†’ only bounds" point is a useful analogue to my effective-sample-size concern (thin coverage â†’ degraded identification of the integrand), though the mechanism differs (their thinness is in observed price support; mine is in importance-sampling node coverage). [analogy] The paper does **not** vary choice-set size, number of draws/starts, opportunity-set definitions, circumstance partitions, or an ability/access boundary â€” none of those exist here. [explicit absence]

---

## 12. What I can cite this paper for

- That **money-metric welfare (EV/CV) for discrete choice is point-identified from choice probabilities under arbitrary, unspecified-dimension preference heterogeneity**, requiring only monotonicity+continuity of utility in the numeraire. [explicit, pp. 617â€“618, 622, Theorem 1]
- That **the preference-heterogeneity distribution need not be identified â€” nor even its dimension â€” for welfare distributions to be well-defined and point-identified** (Remark 1; Appendix example). [explicit, pp. 627, 646â€“647] *(This is the key citation for my "welfare object is preference-respecting and robust to not pinning down full heterogeneity" claim.)*
- That **average EV equals the change in average Marshallian consumer surplus even without quasilinear utility**, and average CV $\ge$ EV for a normal good (Corollary 1). [explicit, p. 628]
- That **welfare can be computed directly from choice probabilities without reconstructing expenditure functions / utility primitives**, including under a parametric MNL approximation (eqs. 23â€“24). [explicit, pp. 632, 640]
- As **methodological precedent and caution** that parametric welfare calculations can rest on functional-form-driven identification (Remark 3 / ordered-choice result) â€” used to motivate my synthetic-recovery certification. [explicit, pp. 638â€“640]
- For the **EV/CVâ€“asâ€“inverse-utility-solve** construction (Lemmas 1â€“2), as a relative of my own bracketing inversion. [explicit, p. 625]

---

## 13. What I should NOT cite this paper for  [overclaim risks]

- **Not** for any opportunity / access / ability mechanism, heterogeneous feasible sets, or rationing â€” the paper has a **universal common choice set** and no opportunity object. [explicit absence]
- **Not** for a **two-way or three-way decomposition** of welfare inequality â€” it has **no decomposition and no inequality index** at all. Do not present it as opportunity-vs-preference or access/ability/preference. [explicit absence]
- **Not** for an **ex-ante / inclusive-value (log-sum) welfare core** â€” its welfare object is a per-type price-change EV/CV aggregated to a distribution; the log-sum appears only in a parametric example, not as the welfare number. Do not read my ex-ante stance into it. [explicit]
- **Not** as containing or endorsing my **$W^1$â€“$W^6$ family** or any **Ind-$y$ / Ind-$A$** classification â€” it does not. The loose "Full-Responsibility corner" analogy is mine, not the source's; flag it as such. [**source does NOT contain $W^1$â€“$W^6$**]
- **Not** for a **reference-level equivalent income** â€” its object is a *price-change* compensation, not a level against a normative reference state/preference/set. [explicit]
- **Not** for **occupation/industry** anything; no occupation, no sector, no NACE/ISCO content. No `loc4`/`lindi` mapping. [explicit absence]
- **Not** for a **random-opportunity** reading â€” the paper has deterministic, common menus and stochastic *preferences*; its randomness is in $\eta$, not in opportunities. Consistent with my deterministic-opportunities stance, but do not cite it as evidence about opportunities at all. [explicit]
- **Not** to clear parametric structural decompositions of the "mechanical / functional-form" charge â€” Remark 3 cuts the other way for ordered choice. [explicit, p. 639]
- **Theory-paper boundary:** this is a welfare-*measurement* econometrics paper; it has nothing to do with the Haydarâ€“Maniquet axiomatic characterisation, and must never be enrolled to support axioms, characterisations, or proofs, nor read as a theory contribution of my JMP. [boundary]

---

## 14. Direct quotes worth citing

(Short, exact, with page numbers. Use sparingly.)

1. "the marginal distributions of EV and CV can be expressed as simple closed-form functionals of conditional choice probabilities" (abstract, p. 617).
2. "These results hold even when the distribution and dimension of unobserved heterogeneity are neither known nor identified" (abstract, p. 617).
3. "average EV for a price rise equals the change in average Marshallian consumer surplus" (abstract, p. 617).
4. "more numeraire is better" (gloss on strict monotonicity, p. 622).
5. "the identification result underlying this calculation is artificial in that it is driven entirely by functional form assumptions" (Remark 3, ordered choice, p. 639).
6. "identifiability of the heterogeneity distribution or even correct specification of its dimension is not a requirement for identifiability of welfare distributions" (Appendix, p. 647).

[All verbatim from the PDF; each under the quote-length limit. Quote 5 must be cited with the Â§8 caution, not as endorsement.]

---

## 15. Open questions and risks for my draft

- **Object mismatch risk.** My equivalent-income *level* against a reference set is not the same object as Bhattacharya's price-change EV/CV. If I cite him as authority for "money-metric welfare from discrete choice," a careful referee will note the object differs (change vs level; universal vs constrained set). I should cite him precisely for the *preference-respecting, heterogeneity-robust* property, not for the object form. [risk]
- **Inference is deferred in the source.** Bhattacharya defers full inference to Bhattacharyaâ€“Lee (2014); I cannot lean on this paper for standard errors on welfare distributions. My cluster-robust bootstrap is my own and is not supported by this paper. [risk â€” verify Bhattacharyaâ€“Lee status if I need an inference citation]
- **The functional-form caution (Remark 3) is a live referee weapon.** It strengthens my motivation for synthetic-recovery certification but also names the exact vulnerability of my parametric RURO; I must address it head-on rather than cite around it. [risk]
- **Nonparametric ideal vs my parametric reality.** The paper's nonparametric ideal needs price variation I lack; positioning must make clear I adopt its *welfare-well-definedness lesson* while operating parametrically with a different identification warrant (recovery, not in-sample fit). [risk]
- **No opportunity object.** The paper cannot speak to the central empirical bet of my JMP (that opportunity differences are large and compensation-relevant); it is upstream infrastructure only. Do not let its prominence crowd the opportunity-mechanism citations (Aabergeâ€“Colombinoâ€“StrÃ¸m, Dagsvik, Aabergeâ€“Colombino) in the positioning. [risk]

---

## 16. TL;DR for retrieval

Bhattacharya (2015, *Econometrica*) point-identifies the marginal distributions of EV/CV from a discrete *price change* as closed-form functionals of conditional choice probabilities, under arbitrary unspecified-dimension **preference** heterogeneity and only monotonicity+continuity of utility in the numeraire â€” the canonical authority that my preference-respecting money-metric welfare object is well-defined without identifying the heterogeneity distribution. It has **no opportunity mechanism, no inequality index, no decomposition, no $W^1$â€“$W^6$ family, and no inclusive-value welfare core**, so it informs only the **preference** channel and the welfare-object's robustness, never access/ability or the three-way split. Its ordered-choice negative result and Remark 3 are a double-edged citation: useful to motivate my synthetic-recovery certification against the functional-form-identification charge, but not a clearance of parametric structural decompositions.
# Beffy, Blundell, Bozio, Laroque & TÃ´ 2019 â€” Labour supply and taxation with restricted choices

> **Provenance note.** This summary is produced from the attached PDF (the accepted
> "Article in Press" version, HAL `halshs-01883898`), which is internally paginated
> **1â€“31**; the published article is *Journal of Econometrics* 211(1), **pp. 16â€“46**.
> All page citations below use the **in-press internal numbering (1â€“31)** visible in
> the PDF; add 15 to map to published pages approximately. Equation, table, and lemma
> numbers are as printed in the PDF. Tags used throughout: **[explicit]** = stated in
> the source; **[analogy]** = derived-by-analogy to my JMP, not in the source;
> **[not established]** = the source does not contain this; **[verify]** = metadata I
> could not confirm from the PDF.

---

## 0. Metadata

- **BibTeX key:** `BeffyBlundellBozioLaroqueTo2019` [verify â€” house convention].
- **Authors:** Magali Beffy (CREST), Richard Blundell (UCL/IFS), Antoine Bozio (PSE/IFS), Guy Laroque (UCL/IFS/Sciences-Po), Maxime TÃ´ (UCL/IFS). [explicit, p. 1]
- **Year:** 2019 (online 2018). [explicit]
- **Outlet:** *Journal of Econometrics* 211(1), pp. 16â€“46. [explicit, HAL cover]
- **DOI:** 10.1016/j.jeconom.2018.12.004. [explicit]
- **HAL Id:** halshs-01883898. **PDF filename:** `Beffy_et_al_2019_Labour_supply_and_taxation_with_restricted_choices.pdf`. License: CC BY (open access). [explicit]
- **Tier:** T1A.
- **JMP block(s) served:** **identification** (primary); **opportunity-mechanism â†’ access** (primary, hours channel only); **estimation** (secondary, identification logic and Monte-Carlo recovery); **motivation** (secondary). **Not** welfare, **not** decomposition, **not** ability (wage-technology) opportunity, **not** normative-interpretation. [analogy â€” relevance routing]

---

## 1. One-paragraph relevance to my JMP

This is the canonical structural restricted-choice labour-supply paper and the direct methodological ancestor of my JMP's **access** channel: it models observed hours as the joint product of preferences and an estimated **offer distribution over hours**, andâ€”uniquely useful for meâ€”it proves the conditions under which preferences and the offer distribution are *separately* identified. It speaks almost entirely to the **access** dimension (hours availability) and to the **identification** backbone (separating preferences from constraints), plus its Monte-Carlo work is a published precedent for my synthetic-recovery standard of evidence. It contains **no** welfare, equivalent-income, inclusive-value, or inequality/decomposition content, and **no** ability (wage-technology) or occupation opportunity objectâ€”so its relevance is concentrated in access + identification, and I must not lean on it for the welfare layer, the decomposition, or the ability/access cut.

---

## 2. Data and setting

- **Country / years:** United Kingdom, 1997â€“2002 (chosen deliberately to span major tax-credit/welfare reforms, generating budget-constraint variation). [explicit, p. 2, p. 11]
- **Dataset:** UK Family Expenditure Survey (FES); the complete nonlinear budget constraint per family from the IFS-Taxben microsimulation model. [explicit, p. 2, p. 11]
- **Sample unit:** the **woman** (single or married mother) within a household with children; spouse choices and family composition are treated as fixed exogenous inputs. [explicit, p. 3, p. 11]
- **Sample size:** â‰ˆ **10,575** women, spread fairly evenly across the six years. [explicit, p. 11, Table 1]
- **Key variables:** usual weekly hours, gross hourly wage, consumption expenditure, education (3 levels), number and age of children, cohabitation, London residence, year, birth-cohort (yob â‰· 1963). [explicit, Tables 1â€“3]
- **Budget-set construction:** full tax / tax-credit / welfare schedule (income support, family credit, rent rebate, local tax rebate) with large nonconvexities and flat segments (income support conditional on working < 16 h). [explicit, p. 4, Fig. 1]
- **Consumption** is used to make the static hours model life-cycle-consistent (Blundellâ€“Walker). [explicit, p. 3]

**Transport to my France pooled 2015â€“2017 EUROMOD cross-section â€” PARTIAL.**
- *Shared:* a cross-sectional micro sample with a **microsimulated nonlinear budget set** (IFS-Taxben â†” EUROMOD `ils_dispy`); identification leaning on **budget-constraint heterogeneity**; consumption anchored to disposable income (their FES consumption â†” my `ils_dispy`, 2016-real). [analogy]
- *Features I do NOT have / differences:* their sample is **women-with-children only** (not my three groups: single males, single females, and couples-as-joint-unit); their offers are **hours-only**; there is **no occupation, no panel, no external instrument, no vacancy/offer data**; and their identifying budget variation is partly **reform-driven** (1997â€“2002), which my pooled cross-section does not exploit as a designed reform instrument. [explicit on their side; analogy on the gap]

---

## 3. Model and objects (map object-by-object to mine)

- **Choice set.** A finite hours set $\mathcal{H}=\{h_1,\dots,h_I\}$; agents choose on a **random subset** (a small number of offered points), not the universal set. The paper focuses on the **two-offer** case: two i.i.d. offers drawn from offer distribution $g$, with non-work always available. [explicit, p. 4â€“5, eqs. (1)â€“(2)]
  - *Map to my latent-jobs set:* PARTIAL analogue. My RURO engine samples a large alternative set from a proposal $\pi$ and applies a McFadden-style $-\log\pi$ correction; Beffy et al. enumerate a 2-offer consideration set and the offer density $g$ enters the likelihood **combinatorially** ($g_i^2 + 2g_i\sum_{j\ne i}g_j p_{ij}$). The "latent feasible set" *idea* is shared; the mechanics differ. [analogy + explicit]
- **Deterministic utility $v$.** $u(c,h)=\dfrac{c^{1-\gamma}}{1-\gamma}+a\,\dfrac{(L-h)^{1-\phi}}{1-\phi}$, $L=100$, additively separable, with $\ln a = Z^a\beta^a+\sigma^a\varepsilon^a$ (leisure taste-shifter). [explicit, eqs. (13),(15)]
  - *Map to my preference utility $v$:* same role (consumption + leisure). **Difference:** additively-separable CRRA-type, **not Boxâ€“Cox** (my spec). Their taste-shifters (cohabiting, youngest-kid age, number of kids, cohort) â‰ˆ my demographic leisure shifters. [analogy]
- **Opportunity / availability mechanism analogous to my $g$:** YES, but **only one channel â€” hours.** $g(h\mid Z^o)$ is a discretised mixture of two truncated normals (modes part-time â‰ˆ 15 h, full-time â‰ˆ 38 h); the mixture weight $p_1(Z^o)$ depends on education / London / year in Model 3. [explicit, p. 12, Table 5]
  - **hours â†’** my **access** (hours availability). [explicit channel; analogy mapping]
  - **wage (ability):** present only as a reduced-form **wage equation** $\ln w = Z^w\beta^w+\sigma^w\varepsilon^w$ (returns to age, education, kids, London, year; dispersion $\sigma^w$)â€”but the wage is a **worker attribute feeding the budget $R(w,h)$**, *not* an offer/availability object. Maps to my **ability** content **by analogy only**, and the difference matters (see Â§5). [explicit; analogy]
  - **market / participation:** governed by **fixed costs of work** $b=Z^b\beta^b+\sigma^b\varepsilon^b$ (eq. (16)) and an always-available non-work optionâ€”**not** a separate market-offer probability. Differs from my market/employment-availability access sub-channel. [explicit]
  - **occupation:** **absent.** No ISCO / occupation / sector / industry variable at all. [explicit, by absence]
- **Budget map = my EUROMOD disposable income?** Their $R(w,h)$ = after-tax-and-benefit income from IFS-Taxben â‰ˆ my `ils_dispy` from EUROMOD. [analogy]
- **FLAG â€” any attribute in BOTH utility and opportunity?** No attribute enters *both* utility and the offer mechanism. But **education** enters **both** the wage equation (human-capital / ability-like) **and** the hours-offer mixture weight (access-like) in Model 3 [explicit, Table 5]. They treat this as an exclusion-restriction design (a covariate shifting offers), not as an identification hazard. *For me:* this is a useful **precedent that education legitimately straddles the ability/access boundary**â€”exactly the contested re-allocation I flag as a deferred robustness. [analogy]
- **No sector/industry conflation** to flag, because there is no occupation/sector object at all. [explicit, by absence]

---

## 4. Estimation method

- **Estimator:** maximum likelihood of the two-offer sample likelihood, with a **two-step control function** for consumption endogeneity (reduced-form consumption residual $\varepsilon^c$ added as a regressor in the utility/cost/wage equations; Blundellâ€“Powell). [explicit, p. 13]
- **Choice-set construction:** **not** a sampled-alternatives MNL over a fixed large grid; two offers drawn from $g$, with the $n$-offer generalisation noted to converge to the unrestricted model as $n\to\infty$. [explicit, p. 6]
- **Proposal / sampling density:** none in my sense (see Â§4b).
- **Prior/proposal correction ($-\log\pi$):** **not used.** No log-prior is subtracted from a choice index; the offer density $g$ enters the likelihood **directly** (so $g$ is simultaneously the structural object and a likelihood ingredient). My mandatory $-\log\pi$ has **no counterpart** here. [explicit, by construction of eq. (2)]
- **Normalisation / scale:** $V_I$ normalised to 0 (only utility *differences* identified); RUM with a differentiable CDF $F_{ij}$ of $\varepsilon_i-\varepsilon_j$. [explicit, p. 7]
- **Numerical method / starts:** ML; the Monte-Carlo uses **several starting values** including random starts. [explicit, Appendix C]
- **What pins preferences separately from the opportunity mechanism:** see Â§8.
- **Verdict â€” reusable for my RURO/JAX pipeline?** *Partly.* The 2-offer combinatorial likelihood is **not** portable as an estimator (my engine is sampled-MNL with an analytic log-sum). The **control-function** treatment of consumption endogeneity is a portable idea **only if** I later treat consumption as endogenousâ€”currently I lock $c=$ `ils_dispy`, so likely not needed. The genuinely reusable content is the **identification logic** of Â§8, not the estimator.

---

## 4b. Proposal / sampling-of-alternatives correction  [extract even if brief]

- Largely **N/A**: there is **no McFadden sampling-of-alternatives correction**.
- The object that plays the "what's available" role is $g(h\mid Z^o)$, which is **partly individualised**: the mixture **weight** $p_1$ depends on covariates (education, London, year in Model 3) while the component means/sds ($m_1,\sigma_1,m_2,\sigma_2$) are **common**. [explicit, Table 5]
- This is a loose parallel to my **partly-individualised proposal** (in my design, wage/occupation channels are individualised, hours/employment common). The directions differ: here the offer **weight** is individualised by covariates while the hours **modes** are common; in my proposal the wage **mean** is individualised while hours/employment are common. [analogy]
- **No per-alternative log-prior is carried** (no importance sampling). Relate to my IS welfare integrator: I sample-and-reweight with a per-row $-\log\pi$; they enumerate two offers and put $g$ straight into the likelihoodâ€”conceptually $g \leftrightarrow$ my $g$, but their $g$ is never a proposal to be corrected away. [explicit; analogy]

---

## 5. Opportunity mechanism  [MOST IMPORTANT â€” split by channel]

**Form.** An explicit offer distribution over **hours**. Two i.i.d. draws from $g$; the agent chooses the utility-maximising offered point or non-work; likelihood $\ell_{2i}=g_i^2+2g_i\sum_{j\ne i}g_j\,p_i(\{i,j\})$. [explicit, eq. (2)] $g$ is a discretised mixture of two truncated normals on $[0,66]$ with covariate-dependent weight $p_1(Z^o)$. [explicit, p. 12]

**access (hours / market / region / year / occupation offers):**
- **hours:** YES â€” the core object; twin-peaked offers, part-time mode â‰ˆ 15 h and full-time mode â‰ˆ 38 h. [explicit, Table 5, p. 15]
- **market / participation:** via **fixed costs** $b$, not a separate offer probability; non-work always feasible. [explicit]
- **region:** London enters the fixed cost $b$ and the wage equation; in Model 3 it is also a (statistically **insignificant**) offer-weight covariate. [explicit, p. 15]
- **year:** year dummies in the offer weight (Model 3, **insignificant**) and in the wage equation. [explicit, Tables 5â€“6]
- **occupation offers:** **ABSENT.** [explicit, by absence]

**ability (wage technology â€” returns to education/experience, residual productivity):**
- Present as a **wage equation** (returns to age, education, kids, London, year; dispersion $\sigma^w$), but **not** part of $g$; the wage is a worker attribute feeding $R(w,h)$. Maps to my **ability** sub-block **by analogy**, with the explicit caveat that here the wage technology is a *reduced-form wage equation, not an opportunity density*. [explicit; analogy]

**occupation as availability vs. something else:** N/A (absent); **no sector/industry conflation** to flag. [explicit, by absence]

**Does it vary with observable circumstances?** YES â€” the offer **weight** varies with **education** (more educated â†’ higher full-time-offer probability) and (insignificantly) London/year. [explicit, p. 15, Table 5] *Note:* education is placed in the **access** object here, whereas my baseline places education in **ability**; this is a concrete precedent for treating education on either side of the ability/access boundary. [analogy]

**Functional form:** mixture of two truncated normals, discretised to a pmf $g(h\mid Z^o)=p(h{+}1\mid Z^o)-p(h\mid Z^o)$. [explicit, p. 12]

**Cost of the omissions for my access/ability/preference decomposition.** Because offers are **hours-only**, the paper supports the **hours-access** channel and its identification, but provides **no** transportable content for wage(ability)-as-opportunity, occupation-as-access, or an explicit market-offer channel. Indeed, the paper's treatment of the wage as a *worker attribute* (not an opportunity object) is exactly the modelling choice my JMP departs from by folding the wage technology into $g$ (the ability sub-block). [analogy]

---

## 6. Welfare object â€” and its place on my $W^1$â€“$W^6$ map

- **Does the paper compute welfare?** **No.** [not established] There is no money-metric welfare, no equivalent income, no compensating/equivalent variation, no inclusive-value welfare object, and no reference-preference / reference-set construction. The empirical outputs are parameter estimates, model fit, rejection shares, elasticities, and behavioural **policy simulations** (employment, hours, a 10% wage increase). [explicit, Â§5]
- **Place on my $W^1$â€“$W^6$ map:** **none.** The paper cannot be located on the family map; it constructs no equivalent-income measure and takes no Ind-$y$/Ind-$A$ stance. [not established]
- **Verdict:** **incompatible** as a welfare source. Do not cite it for welfare, equivalent income, or any $W^k$.

---

## 6b. Inclusive value and money-metric inversion

- **N/A / [not established].** No log-sum/inclusive-value welfare core is computed and no own-utility map is inverted to money. The identification RUM (Â§3) uses a general $F_{ij}$, with IIA/logit handled as a special case in Appendix B (Lemma 3), but the **inclusive value is never used as a welfare object**, and the expectation over shocks is not taken as a welfare log-sum. [explicit; not established for welfare use]

---

## 7. Inequality / decomposition content  [three-way where relevant]

- **Inequality index:** none. [not established]
- **Decomposition rule:** none â€” the paper is **not** a decomposition paper (neither two-way opportunity/preference nor my three-way access/ability/preference). [not established]
- **Counterfactual construction present?** The paper **does** run structural counterfactual **simulations** â€” **constrained (two-offer) vs. unconstrained** employment and hours, and a 10% wage rise â€” but these are *behavioural* simulations, **not** welfare-inequality decompositions; nothing is "equalised/neutralised" in a welfare sense. [explicit, p. 19â€“21]
- **Verdict â€” reusable for my three-way Shapleyâ€“Shorrocks split (anchored on $W^3/W^5/W^1$)?** **No.** The only transferable *idea* is the **turn-restrictions-off counterfactual**, which loosely parallels my "equalise access" thought-experiment, but it is conducted on employment/hours (not a welfare distribution) and is **not Shapley-organised**. To serve my decomposition it would have to be re-expressed as an equalisation of a channel within a money-metric, recomputed through a welfare core, and Shapley-averaged â€” none of which the paper does. [analogy]

---

## 8. Identification and the separation of preferences from opportunities  [STRICT â€” the paper's core value to me]

The paper's central theoretical contribution is precisely my identification problem, stated cleanly for the hours-offer case.

- **Lemma 1** [explicit, p. 7]: if the offer distribution $g$ is **known**, preferences (the random utilities $V_i$) are **identified** â€” the system $\ell_i=g_i^2+2g_i\sum_{j\ne i}g_j F_{ij}(V_i-V_j)$ has at most a unique $V$ (proof via Galeâ€“Nikaido, dominant-diagonal Jacobian).
- **Lemma 2** [explicit, p. 8]: if the choice probabilities $p_{ij}$ are **known**, the offer distribution $g$ is **recovered** uniquely (Brouwer fixed point on a simplex map; uniqueness via dominant diagonal).
- **Joint problem:** **without restrictions, $g$ and the preferences are NOT separately identified** (Lemmas 1+2 together). [explicit, p. 8]
- **Three routes to joint identification:**
  1. **Parametric** (3.3.1) [explicit, p. 9]: restrict $g(\gamma)$ and $p(\beta)$ to finite parameters with $\dim[\beta:\gamma]\le I-1$, and require full column rank of $\Pi=[\partial Q/\partial\beta,\ \partial Q/\partial\gamma]$ (eqs. (7)â€“(12)). Flat budget segments give $\partial p_{ij}/\partial\beta=0$ for some pairs (those pairs inform $g$, not preferences).
  2. **Semi-parametric via exclusion restrictions** (3.3.2) [explicit, p. 9â€“10]: a covariate $Z$ (e.g. wage / other income) that shifts the **budget constraint $R$** without shifting the **offer distribution $g$**; identification requires enough variation in $Z$ (with discrete $Z$ over $K$ values: $(I-1)\times K$ likelihood contributions vs. $I-1+\dim(\beta)$ unknowns).
  3. **Nonparametric via dominated regions** (3.3.3) [explicit, p. 11]: where the nonlinear budget has flat/decreasing segments, dominated hours satisfy $p_{ij}=1$ regardless of $\beta$, so Lemma 2 recovers $g$ on that subpopulation, after which Lemma 1 recovers preferences on households facing increasing budgets.
- **Monte-Carlo recovery** (Appendix C, Tables 13â€“14) [explicit, p. 23â€“30]: with a **single** budget constraint, estimates are biased/imprecise (preference parameters especially, when the budget is near-linear); with **â‰¥ 2 distinct** budget constraints, recovery is well-behaved. Budget-constraint heterogeneity functions as the exclusion variable.

**Transport to my France pooled cross-section (no panel, no external instrument):**
- The **exclusion-restriction logic transports in spirit** [analogy]: EUROMOD's nonlinear tax-benefit schedule generates household-specific **budget-constraint heterogeneity** (via demographics, region, other income) that shifts $R$ without (by assumption) shifting the opportunity density â€” a legitimate identification source I share. *(That budget heterogeneity identifies the split is [explicit]; that EUROMOD supplies it for me is [analogy].)*
- The **dominated-regions** route also transports in principle (EUROMOD nonconvexities exist). [analogy]
- Crucially, my **certification is by synthetic recovery at production resolution**, which is the *same epistemic move* as their Monte-Carlo recovery. This is published support that (i) parametric RURO-type identification must be *demonstrated by recovery*, and (ii) **budget-constraint heterogeneity is what makes recovery succeed** â€” directly arming me against the "your separation is mechanical / functional-form-driven" referee. [analogy]
- **Honest caveat:** Beffy et al. identify a **hours-offer distribution vs. preferences**. They do **not** identify a wage- or occupation-offer distribution, so they provide **no transportable identification argument for my ability-vs-access split**. That finer cut rests on my own functional-form + synthetic-recovery argument, not on this paper. [explicit limitation; analogy on consequence]

---

## 9. Key results and magnitudes

- **Nonparametric rejection:** â‰ˆ **2.6%** of working women observed at strictly dominated hours; an additional **0.4%** would earn more out of work. [explicit, p. 16â€“17, Table 8]
- **Parametric rejection** at the Model-3 $\phi$: **7.9%** of working women violate the revealed-preference inequality. [explicit, p. 17â€“18, Tables 8â€“9]
- **Offer modes:** part-time â‰ˆ **15 h**, full-time â‰ˆ **38 h**; more educated women have higher full-time-offer probability; no significant location/year offer differences. [explicit, p. 15, Table 5]
- **Frisch elasticity (mean):** 0.58 (M1) / 0.59 (M2) / **0.30** (M3). **Marshallian (mean):** 0.58 / 0.48 / **0.20** (M3). [explicit, Table 10, p. 19] â€” accounting for unobserved-heterogeneity correlations and offer heterogeneity roughly **halves** the elasticities.
- **Employment:** **71%** unconstrained vs. **62.5%** constrained; mean hours **35.5** vs. **26.2**. [explicit, p. 19]
- **10% wage rise:** intensive margin **0.35** (unconstrained) vs. **0.16** (constrained); extensive **0.25** vs. **0.27**. [explicit, Table 11, p. 21]
- **Who is constrained:** poorer households, shorter hours, lower wages, more often lone mothers. [explicit, Table 9, p. 17â€“18; abstract]
- **Benchmark for me:** that estimated preferences/elasticities move *materially* once hours restrictions are modelled is direct evidence for my **sub-question 1** (unmodelled opportunity is absorbed into estimated tastes). The magnitudes (elasticities â‰ˆ halving; employment 71â†’62.5) give a plausibility range for "how much do restrictions matter," but on **UK women-with-children**, not France â€” use as order-of-magnitude only. [explicit numbers; analogy on benchmarking]

---

## 10. Estimators, theorems, or formal results

- **Lemma 1** â€” *Given $g$, at most one $V$ (with $V_I=0$) solves $\ell_i=g_i^2+2g_i\sum_{j\ne i}g_j F_{ij}(V_i-V_j)$.* Assumptions: $\ell,g$ in the positive simplex; $F_{ij}$ differentiable. Technique: (i) stack $I-1$ equations; (ii) show Jacobian is a dominant-diagonal matrix; (iii) invoke Galeâ€“Nikaido for univalence. **Reuse verdict:** the *identification logic* is reusable; the estimator is not (my likelihood is a sampled-MNL log-sum). [explicit]
- **Lemma 2** â€” *Given $p_{ij}$ (with $p_{ij}+p_{ji}=1$), a unique $g$ in the simplex solves $\ell_i=g_i^2+2g_i\sum_{j\ne i}g_j p_{ij}$.* Technique: Brouwer fixed point for existence + dominant-diagonal univalence for uniqueness. **Reuse:** logic reusable as the "recover offers given choices" half. [explicit]
- **Lemma 3** (Appendix B, IIA/logit special case) â€” analogous unique-solution result under IIA, $\ell_i=g_i^2+2g_ip_i\sum_{j\ne i}g_j/(p_i+p_j)$. **Reuse:** closest to my MNL setting (logit special case), but still 2-offer-structured; reusable as a conceptual bridge, not as my estimator. [explicit]
- **Rank condition** (eqs. (7)â€“(12)) â€” full column rank of $\Pi$ for joint parametric identification. **Reuse:** a *template* for arguing my parametric identification, but I rely on synthetic recovery rather than an explicit rank proof. [explicit; analogy on reuse]

---

## 11. Robustness and specification sensitivity

- **Number of offers:** the two-offer model is acknowledged restrictive; it converges to the standard unrestricted model as $n\to\infty$. [explicit, p. 6, p. 22] â†’ informs my **choice-set-size sensitivity** (101 singles / 901 couples).
- **Single vs. multiple budget constraints (Monte-Carlo):** a single budget constraint â†’ biased/weak recovery (preferences worst when the budget is near-linear); dominated regions â†’ precise $g$ but **less precise preferences**; combining constraints â†’ recovers both. [explicit, Tables 13â€“14, p. 23â€“30] â†’ informs my **recovery/stability tests** and the **effective-information** concern.
- **Three model variants** (M1 exogenous wage/consumption; M2 correlated unobservables; M3 covariates in the offer weight): **M3 fits the hours distribution best.** [explicit, p. 15â€“16, Fig. 2, Table 8] â†’ supports adding **circumstance covariates to the access channel**.
- **Identification trade-off:** dominated budget regions sharpen $g$ but blur preferences; monotone budgets sharpen preferences. [explicit, p. 9, p. 30] â†’ **corroborates** my reported standard-error asymmetry (tight opportunity block, wide preference block) as a *generic feature of this model class*, not a defect. [analogy]

---

## 12. What I can cite this paper for

- That a structural labour-supply model can **separate preferences from an estimated offer (opportunity) distribution**, with formal identification conditions (Lemmas 1â€“2, Â§3). [explicit]
- That **budget-constraint heterogeneity / nonlinear tax-benefit variation** is an identification source for the offer-vs-preference split, **demonstrated by Monte-Carlo recovery** (Â§3.3, Appendix C). [explicit]
- That observed **twin-peaked hours reflect hours-offer restrictions**, not preferences alone, with â‰ˆ 2.6% nonparametric and 7.9% parametric rejection of the unrestricted model (Â§2.2, Â§5.3). [explicit]
- That **accounting for hours restrictions materially changes estimated preferences/elasticities and counterfactual employment** (Â§5). [explicit] â€” support for my sub-question 1.
- As the canonical **consideration-set / restricted-choice antecedent** of my access channel and as motivation for modelling a household-specific feasible set (Intro, Â§2.3). [explicit]
- That **near-linear/monotone budget constraints weakly identify the offer distribution, while dominated regions weakly identify preferences** (Appendix C). [explicit]

---

## 13. What I should NOT cite this paper for  [overclaim risks]

- **No welfare content.** Do not cite for any welfare, equivalent-income, money-metric, CV/EV, or inclusive-value-as-welfare claim â€” the paper computes none.
- **No decomposition.** Do not cite for any inequality index or decomposition (two-way *or* three-way) â€” it is not a decomposition paper.
- **Hours-only opportunity.** Do not present its offer distribution as covering **wage/ability**, **occupation**, or **market** opportunity. Offers are hours-only; the wage is a worker attribute; occupation is absent.
- **Random-opportunity framing (boundary flag).** The paper uses a genuinely **random** offer-draw framing (choices made on a random subset of possible hours). My JMP treats opportunities as **deterministic feasible sets** (the "RO" in RURO is estimation machinery). Cite this paper as **random-consideration-set** and explicitly differentiate it from my deterministic stance; do not import its randomness as if it were mine.
- **Not a sampled-MNL-with-log-sum estimator.** It is a 2-offer combinatorial likelihood in which $g$ sits *inside* the likelihood; it has **no $-\log\pi$ proposal correction**. Do not describe it as my estimation machinery.
- **Theory-paper boundary.** Nothing here is the Haydarâ€“Maniquet axioms/characterisation. Do not attribute any $W^1$â€“$W^6$ reading or normative claim to this paper, and do not read this paper as a theory contribution.
- **Population caveat.** UK women-with-children, 1997â€“2002. Do not generalise its magnitudes to my French three-group sample without qualification.

---

## 14. Direct quotes worth citing

> **Note on reproduction.** I am keeping verbatim reproduction minimal. One short verbatim
> quote is given; the remaining entries are **page-located paraphrases** so you can pull
> the exact wording yourself from the open-access (CC-BY) PDF if you want a verbatim
> citation. This is deliberate, not an omission.

- **Verbatim (abstract, p. 1):** "observed hours reflect both the distribution of preferences and restrictions on choices."
- **Paraphrase, intro (p. 1â€“2):** the standard unrestricted-hours model has long been recognised as ill-suited to distinguish individual preferences from external (demand-side) constraints. [locator for verbatim pull]
- **Paraphrase, intro (p. 2):** their interpretation is rational choice from a set of job *packages* limited by the hours employers offer (a labour-supply analogue of the consideration set). [locator]
- **Paraphrase, Â§2.3.2 / conclusion (p. 6, p. 22):** as the number of offers grows the model converges to the standard unrestricted-choice model. [locator]
- **Paraphrase, Monte-Carlo conclusion (p. 31):** estimates are well-behaved when the simulated population faces two different budget constraints, and biased when it faces only one. [locator]

---

## 15. Open questions and risks for my draft

- **"What is your $Z$?"** Their identification leans on budget-constraint heterogeneity + dominated regions + an exclusion restriction shifting $R$ but not $g$. My pooled cross-section has no reform instrument, so I must **name the concrete EUROMOD shifters** (demographic / regional / other-income variation in the tax-benefit map) that play the role of their $Z$ â€” the referee will ask.
- **Ability-vs-access has no precedent here.** This paper identifies hours-offers vs preferences only; the identification of my finer **ability/access** cut is entirely my own burden (functional form + synthetic recovery) and cannot be propped up with this citation.
- **Random vs deterministic framing.** I must reconcile the lineage in prose: borrow the restricted-choice *machinery* and identification logic while making clear my opportunities are deterministic feasible sets, not random draws.
- **Weak preference identification under near-linear budgets.** Their Monte-Carlo warns that near-linear budgets weakly identify preferences. This **corroborates** my wide singles-preference block as a generic feature â€” but a referee could equally read it as a weak-identification risk; I should frame it as identification-with-imprecision and lean on synthetic recovery.
- **Consumption endogeneity.** They model it with a control function; I lock $c=$ `ils_dispy`, which removes that endogeneity channel. I should note this as a deliberate simplification (a channel they had to model that I sidestep), not pretend the issue is absent.

---

## 16. TL;DR for retrieval

Beffy, Blundell, Bozio, Laroque & TÃ´ (2019, *J. Econometrics*) estimate a structural labour-supply model in which observed hours reflect both preferences and an estimated **hours-offer distribution** $g$, and prove that preferences and $g$ are *separately* identified given budget-constraint heterogeneity, exclusion restrictions, and dominated regions â€” making this my primary citation for the **access** channel and for the **identification** backbone (and, via its Monte-Carlo recovery, for my synthetic-recovery standard). It is hours-only and contains **no ability/occupation opportunity object, no money-metric welfare, no inclusive value, and no inequality decomposition**, so it must not be cited for the welfare layer, the three-way decomposition, or the ability/access cut. Its **random-offer** framing must be explicitly differentiated from my **deterministic** feasible sets, and none of it touches the companion Haydarâ€“Maniquet theory paper.
# Bourguignon, Ferreira & MenÃ©ndez 2007 â€” Inequality of Opportunity in Brazil

> Extraction produced under `JMP_T1_exhaustive_extraction_prompt_v2.md`.
> Source of truth: the attached PDF (*Review of Income and Wealth*, Series 53,
> No. 4, December 2007, pp. 585â€“618). Page numbers cite the printed journal
> pagination. Relevance is anchored to `JMP_project_state_v1.md` and
> `JMP_welfare_spec_v5.md`; my project design is **not** imported into the
> reading of this paper. Throughout I distinguish **explicit-in-source**,
> **derived-by-analogy**, and **not-established**.

---

## 0. Metadata

- **BibTeX key:** bourguignon2007inequality [verify exact key against my .bib]
- **Authors:** FranÃ§ois Bourguignon (The World Bank); Francisco H. G. Ferreira (The World Bank, corresponding author); Marta MenÃ©ndez (UniversitÃ© Paris Dauphine and INRA, Paris-Jourdan). [explicit, p. 585]
- **Year:** 2007. [explicit]
- **Outlet:** *Review of Income and Wealth*, Series 53, Number 4, December 2007, pp. 585â€“618. [explicit, running heads]
- **DOI/URL:** [uncertain, needs verification â€” not printed on the PDF]
- **PDF filename:** `Bourguignon_et_al_2007_INEQUALITY_OF_OPPORTUNITY_IN_BRAZIL.pdf`
- **Tier:** T1A.
- **JMP block(s) served:** **decomposition** (primary); **opportunity-mechanism / normative-interpretation** (the circumstance/effort cut and its compensatory reading); **motivation** (a canonical magnitude benchmark for "opportunity share of inequality"). It does **not** serve the estimation, identification-of-preferences, welfare-construction, or data-infrastructure blocks for my design.

---

## 1. One-paragraph relevance to my JMP

This is the canonical reduced-form template for the object my decomposition layer reports: a **counterfactual-equalisation share of inequality attributable to factors beyond the individual's control**. It defines the opportunity share $\Theta_I = [I(F) - I(\tilde\Phi)]/I(F)$, where $\tilde\Phi$ is the earnings distribution simulated under equalised circumstances, and it further splits that share into a **direct** and an **indirect** component â€” a structure that prefigures the *anatomy* of my Shapley equalisation even though the mechanism is entirely different. For my **access** channel it is the closest classical antecedent (circumstances = factors outside individual control = the access/ability side of my cut); it has **nothing** to say about my **preference** channel, because it contains no utility function and no behavioural model â€” taste heterogeneity is silently absorbed into the residual. Its single most transportable methodological contribution is the **partial-identification / bounding** strategy (Monte-Carlo over admissible regressorâ€“residual correlations) that turns an un-identified omitted-variables problem into a reported interval; this is directly relevant to my defence against the "your decomposition is mechanical" referee, though my own identification rests on synthetic recovery rather than on their sign-restricted correlation bounds.

---

## 2. Data and setting

- **Country/year:** Brazil, 1996 (a single cross-section). [explicit, p. 591]
- **Dataset:** PNAD 1996 (*Pesquisa Nacional por Amostra de DomicÃ­lios*), the annual household survey of IBGE; 1996 is used because that wave carries a special supplement on parental education and father's occupation. [explicit, pp. 591â€“592]
- **Sample unit:** individuals (prime-age males who are household heads or spouses). [explicit, p. 591]
- **Sample size:** the full PNAD 1996 is upward of 330,000 individuals; after restricting to urban active males aged 26â€“60 reporting positive earnings the sample is 37,548, falling to **28,474** after dropping observations with missing parental education/occupation. [explicit, p. 591]
- **Cohort structure:** the sample is split into seven 5-year birth cohorts, 1936â€“40 through 1966â€“70, analysed separately. [explicit, p. 592]
- **Key variables:**
  - *Outcome:* log real hourly earnings from all occupations. [explicit, pp. 592, 602 table note]
  - *Circumstances $C$:* race (Black & mixed-race vs White & Asian); region of birth; mean parental schooling; motherâˆ’father schooling difference; father's occupational status (three regrouped levels: lower / medium / higher). [explicit, pp. 592â€“593, 596]
  - *"Efforts" $E$:* own years of schooling; a migration dummy; labour-market status (formal employee/employer, informal employee, self-employed). [explicit, pp. 593, 596â€“597]
- **Budget-set construction:** **N/A** â€” there is no budget set, no tax-benefit map, and no choice problem; the object is an earnings regression, not a labour-supply model.
- **Transport to my France pooled 2015â€“2017 EUROMOD cross-section:** the *cross-sectional, single-wave, no-panel* character transports well â€” like me, they have neither a panel nor an external instrument and must identify a counterfactual from a single cross-section. What I do NOT share, and what they exploit, is **observed family-background circumstances** (parental education, father's occupation) â€” my circumstances are labour-market-side (access/ability in $g$), not intergenerational. What they do NOT have, and I do: an estimated structural model, a preference object, an explicit feasible-set/opportunity density, and a money-metric welfare layer. [explicit on their side; the contrast is derived-by-analogy]

---

## 3. Model and objects (map object-by-object to mine)

- **Choice set vs my latent-jobs set:** **none.** There is no choice set and no latent-jobs object. [explicit â€” the model is a reduced-form earnings function]
- **Deterministic utility vs my preference utility $v$:** **none.** There is no utility function; "efforts" are *observed proxies*, deliberately kept in quotation marks because they are themselves shaped by circumstances and luck rather than derived from optimisation. [explicit, pp. 592â€“593] My preference channel has **no analogue** here.
- **Opportunity/availability mechanism vs my $g$:** **no density-over-alternatives mechanism.** "Opportunity" is operationalised as the **effect of exogenous circumstance variables on earnings**, in the Roemerian circumstance/effort tradition, not as a feasible-set or offer distribution. There is no separation into hours / wage(ability) / market-participation / occupation channels; the only internal split is **direct effect on earnings** vs **indirect effect through "effort" variables** (Â§4 below). [explicit, pp. 593â€“595]
- **Budget map vs my EUROMOD disposable income:** **N/A** (no budget map).
- **Job attribute entering BOTH utility and opportunity:** **N/A by construction** â€” there is no utility block, so the double-entry hazard my prompt flags cannot arise here. Worth noting for contrast: father's occupational status enters as a **circumstance**, and the individual's own labour-market status enters as an **"effort"**; occupation-type objects therefore appear on *both* sides of *their* circumstance/effort cut, but this is a parent-vs-own distinction, not a utility-vs-opportunity double entry. [explicit, pp. 592â€“593]
- **The core model equation (explicit, p. 593, eq. 2):**
$$ w_i = f\big(C_i,\; E_i(C_i, v_i),\; u_i\big), $$
with the log-linear empirical form (explicit, pp. 596â€“597, eqs. 5â€“6):
$$ \ln w_i = \alpha C_i + \beta E_i + u_i, \qquad E_i = H C_i + v_i. $$
Substituting gives the reduced form (explicit, p. 597, eqs. 9â€“10):
$$ \ln w_i = \psi C_i + \varepsilon_i, \qquad \psi = \alpha + \beta H,\; \varepsilon_i = \beta v_i + u_i. $$

---

## 4. Estimation method

- **Likelihood/estimator:** ordinary least squares on the log-earnings equation, run **separately by cohort**; both the "full" equation (7) with circumstances *and* efforts and the reduced form (10) with circumstances *only* are estimated by OLS. [explicit, pp. 596â€“597, 601]
- **Choice-set construction / grid / proposal density:** **N/A** â€” no discrete choice, no sampling of alternatives.
- **Prior/proposal correction ($-\log\pi$):** **N/A** â€” there is no choice index and no McFadden-type correction; the question does not arise.
- **Normalisation/scale:** standard OLS; dependent variable in logs; circumstance/effort regressors as described in Â§2.
- **Numerical method / starting values / multistart:** **N/A** (closed-form OLS).
- **What pins down "preferences" separately from "opportunities":** nothing, because there are no preferences in the model. What is separated is the **direct** circumstance effect (coefficients $\alpha$ in the full equation, holding efforts fixed) from the **total** circumstance effect (coefficients $\psi$ in the reduced form, letting efforts adjust); the indirect effect is the residual $\psi - \alpha = \beta H$. [explicit, pp. 596â€“597]
- **Verdict â€” reusable for my RURO/JAX pipeline?** **No** for the estimator itself (OLS earnings regression is not a structural discrete-choice estimator). **Yes, conceptually,** for the *counterfactual-construction logic*: simulate an equalised distribution, recompute the inequality index, take the proportional fall as the share. That logic survives transplant into my Shapley layer; the regression engine does not.

---

## 4b. Proposal / sampling-of-alternatives correction  [extract even if brief]

**N/A.** The paper has no sampling of alternatives, no proposal distribution, and no importance-sampling integrator. There is therefore nothing to relate to my proposal-individualisation concern. Recording this explicitly so the section co-indexes with T1 sources that *do* have a proposal correction: this source contributes **zero** to my 4b design.

---

## 5. Opportunity mechanism  [MOST IMPORTANT â€” be exhaustive; split by channel]

**Functional form of "opportunity."** Opportunity is *not* modelled as feasibility, availability, or an offer distribution. It is the **causal contribution of exogenous circumstance variables to earnings**, in Roemer's (1998) circumstance/effort partition. Equality of opportunity is defined distributionally: it would obtain if the earnings distribution were independent of circumstances, $F(w\mid C) = F(w)$. [explicit, pp. 593â€“595] Given the structural form (2), this requires both (i) circumstances have no direct effect on earnings conditional on efforts, and (ii) efforts are distributed independently of circumstances. [explicit, p. 595] The empirical strategy uses the **equality-of-circumstances benchmark** $C_i = \bar C\;\forall i$, which is sufficient (not necessary) for equality of opportunity, and constructs the counterfactual earnings distribution $\tilde\Phi(w)$ under that benchmark. [explicit, p. 595]

**Mapping to my three sub-objects:**

- **access** (hours / market-participation / region / year / occupation offers): **no direct analogue.** Their nearest objects are *region of birth* (a circumstance) and *labour-market status* (an "effort"). Region of birth is a circumstance that could be read as a coarse access proxy, but it is a *background* circumstance, not a feasible-set or local-labour-demand object. There is no hours availability, no participation margin, no occupation-offer distribution. [derived-by-analogy; the access reading is mine, not theirs]
- **ability** (wage technology â€” returns to education and experience, residual productivity): their **own schooling** is an "effort", not an ability/opportunity object, and there is no estimated wage technology in the structural sense â€” returns to schooling appear as an OLS coefficient on own years of schooling, not as an identified productivity primitive. *Parental* education and father's occupation are the circumstances that shift earnings, partly *through* own schooling (the indirect channel). So the closest thing to my "ability" content sits on their **effort** side, with its *circumstance-driven part* attributed to opportunity via the indirect effect. [explicit on the variables; the ability mapping is derived-by-analogy]
- **occupation as availability vs something else:** occupation appears **twice** and neither use is my access object. *Father's* occupational status is a **circumstance** (a determinant of opportunity); the individual's own **labour-market status** (formal/informal/self-employed) is an **"effort."** Both are realised positions, not offer/availability distributions. [explicit, pp. 592â€“593]
- **sector/industry conflation flag:** the paper does **not** use NACE/industry; "occupation" here is a sociological status classification (a nine-level scheme regrouped to three). [explicit, p. 593] No `loc4`/`lindi` conflation risk arises *in the source*; the discipline note for my draft is only that I must not describe their father's-occupation circumstance using my own occupation-as-access vocabulary.

**The internal channel split they DO have (direct vs indirect).** This is the structurally interesting part for me. The overall opportunity share captures *both* the direct effect of circumstances on earnings (the $\partial f/\partial C$ channel) and the indirect effect operating through circumstance-shaped efforts ($G(E\mid C)$). [explicit, pp. 595â€“596] The direct share is computed from the full equation (5'); the overall share from the reduced form (10); the indirect share is their difference. [explicit, pp. 596â€“597]

**Cost of the omission for my decomposition.** Because there is no explicit feasible-set mechanism, their framework cannot distinguish a worker with good circumstances in a depressed local market from one with the same circumstances in a thriving market â€” exactly the access variation my opportunity density exists to capture. Their "opportunity" is **background-circumstance opportunity**, not **labour-market-feasibility opportunity**. For my three-way cut, this source informs the *reporting form* of the share and the direct/indirect anatomy, but supplies no mechanism for the access or ability channels. [derived-by-analogy]

---

## 6. Welfare object â€” and its place on my $W^1$â€“$W^6$ map

- **Does the paper compute welfare?** **No.** The decomposed object is **observed earnings inequality** (a Theil index, with a Gini robustness check), not a welfare or equivalent-income object. [explicit, pp. 607â€“608]
- **Money-metric / equivalent income / EV / CV / log-sum:** none of these. [explicit â€” there is no preference map to invert]
- **Universal vs constrained set:** **N/A** (no choice set).
- **Reference price / preference / bundle / set:** the only "reference" is the **equality-of-circumstances benchmark** $\bar C$ used to build the counterfactual *earnings* distribution; it is a reference on the *circumstance vector*, not a reference preference or reference opportunity set. [explicit, p. 595]
- **Discrete-choice subtleties (log-sum, selection, Hicksian/Marshallian, integration over heterogeneity, ex-ante/ex-post):** **N/A** across the board.
- **Location on my $W^1$â€“$W^6$ map:** the paper contains **no** $W^1$â€“$W^6$ object and **no** Independence-of-$y$/Independence-of-$A$ construction; it must **not** be cited as containing them. The *only* legitimate connection is normative-spirit: its compensatory motivation (inequality from factors beyond individual control is "more objectionable") is the same ethical premise that animates the compensation end of my spectrum. That is a *motivational* alignment, not a measure correspondence. [explicit motivation, pp. 585â€“586; the non-correspondence is established]
- **Verdict:** **incompatible** as a welfare construction (there is none); **adaptable** only at the level of the counterfactual-share *reporting object*, which operates on an inequality index of an outcome, not on a welfare distribution.

---

## 6b. Inclusive value and money-metric inversion  [extract if the paper uses a log-sum or an EV/CV]

**N/A.** No inclusive value, no log-sum, no EV/CV, no one-dimensional own-utility inversion, no expectation over extreme-value shocks (analytic or simulated). The paper's counterfactual is constructed by re-evaluating a fitted OLS earnings equation under equalised circumstances, $\tilde w_i = \exp(\hat\psi \bar C + \hat\varepsilon_i)$, not by inverting a utility map. [explicit, p. 597] Contributes nothing to my analytic-in-shocks importance-sampling inversion.

---

## 7. Inequality / decomposition content  [three-way where relevant]

- **Inequality index:** Theil (headline); Gini reported as a robustness check (cohort-average opportunity share 13% under Gini vs 23% under Theil). [explicit, pp. 607â€“608]
- **Decomposition rule:** a **counterfactual-equalisation / regression-based** decomposition, not Shapley and not Shorrocks. The overall opportunity share is
$$ \Theta_I = \frac{I(F) - I(\tilde\Phi)}{I(F)}, $$
explicitly flagged as **index-contingent** (the subscript $I$). [explicit, p. 595, eq. 3] The direct/indirect sub-decomposition is
$$ \Theta_I^d = 1 - \frac{I(\tilde\Phi^d)}{I(F)}, \qquad \Theta_I^{\text{indirect}} = \Theta_I - \Theta_I^d. $$
[explicit, p. 596, eq. 4 â€” I have rewritten the printed expression in clean notation; verify against the source typographic form]
- **Counterfactual construction â€” what is equalised / neutralised / held fixed / zeroed:**
  - *Overall share:* equalise circumstances $C_i \to \bar C$ in the **reduced form**, so circumstances are neutralised both directly and through their effect on efforts; residual $\hat\varepsilon_i$ is held at its observed value. [explicit, p. 597]
  - *Direct share:* equalise circumstances in the **full equation** while holding observed efforts $E_i$ fixed; this zeroes the direct channel only. [explicit, p. 596]
  - *Individual-circumstance contributions:* equalise one circumstance at a time, holding the others at observed values. [explicit, pp. 611â€“612]
  - *Upper-bound thought experiment:* treat all observed "efforts" as circumstances (equalise everything observed), leaving only $u$ as genuine effort. [explicit, pp. 608â€“609]
- **Order-independence / path-independence / exhaustiveness:** **not addressed as such.** The decomposition is *not* claimed to be order-independent or exhaustive in the Shapley sense; the individual-circumstance equalisations are "controlling for all others" but the paper does **not** Shapley-average over orderings, so the single-circumstance contributions need not sum to the overall share. [explicit method, p. 611; the absence of a Shapley property is established by what the paper does not claim]
- **Verdict â€” reusable for my three-way access/ability/preference Shapleyâ€“Shorrocks split anchored on $W^3/W^5/W^1$?** **Partially, and only at the conceptual level.** The *share-of-inequality-from-equalising-X* object and the *direct-vs-indirect anatomy* transplant cleanly into my Shapley framing. But the decomposition here is **two-way at most** (circumstance vs residual, where the residual silently bundles effort, preference heterogeneity, luck, and measurement error) and is **regression-based, not Shapley**. To reach my three channels it would have to be extended by (i) replacing the OLS-counterfactual engine with the structural welfare object, (ii) splitting the opportunity side into access vs ability â€” which their data cannot do, since they have no wage-technology/feasible-set separation â€” and (iii) imposing Shapley order-averaging to obtain exhaustiveness, which they do not do. So the source is an **antecedent and a reporting template**, not a reusable estimator. [derived-by-analogy + established]

---

## 8. Identification and the separation of preferences from opportunities  [STRICT]

- **What identifies the share:** there is **no causal point-identification**. The residual $u$ (and $\varepsilon$) is acknowledged to be correlated with the regressors because of unobserved circumstances and efforts; an IV strategy is rejected as infeasible (no plausible exclusion restrictions for circumstance variables). [explicit, pp. 597â€“598] Instead the paper uses a **partial-identification / bounding** strategy: it treats the regressorâ€“residual correlation vector $\rho_{Xu}$ as unknown, draws it from a uniform distribution on $(-1,1)$, **discards draws** that violate (a) positive-semi-definiteness of the implied covariance matrix (equivalently $K \le 1$) and (b) four economically-motivated sign restrictions on key coefficients, and reports the resulting interval of bias-corrected coefficients as a **90% interval**. [explicit, pp. 598â€“600]
- **Preferences vs constraints:** the paper does **not** attempt this separation â€” it has no preference object. Its separation is **circumstance vs effort**, with effort itself partly circumstance-driven. The honest statement for my purposes: this source separates *background opportunity* from *everything else*, and the "everything else" includes the preference heterogeneity my paper exists to isolate. [explicit / established]
- **Ability vs access within the opportunity side:** **not done.** No internal split of the opportunity side into a pay/ability dimension and a feasible-set/access dimension exists here. [established]
- **Transport to my France pooled cross-section (no panel, no external instrument):** the *spirit* transports â€” both designs confront a single cross-section without instruments and must reason about an un-identified counterfactual. But their specific device (sign-restricted, PSD-constrained correlation bounds on an OLS earnings equation) is **not** my device; my baseline is certified by **synthetic recovery**, not by in-sample fit and not by their correlation-bound intervals. The transportable lesson is the *posture* â€” report a defensible interval rather than a falsely precise point â€” not the mechanism. [explicit on their side; the transport judgment is derived-by-analogy]
- **Referee defence ("your decomposition is mechanical"):** this paper is a useful citation that a respected literature *accepts a reduced-form, partially-identified opportunity share as informative* precisely because it is transparent about what it cannot identify. It does **not**, however, license any claim that the share is causal; it is explicitly a measure of the share *associated with observed circumstances*, conditional on maintained assumptions. Do not soften this when citing. [explicit, pp. 597â€“600, 614]

---

## 9. Key results and magnitudes

All magnitudes refer to **urban Brazilian males aged 26â€“60 with positive earnings, 1996**, by birth cohort unless stated. [explicit, p. 591]

- **Overall opportunity share (Theil):** five observed circumstances account for **10â€“37%** of within-cohort earnings inequality; **15â€“37%** excluding the youngest cohort; cross-cohort simple average of mean estimates â‰ˆ **23%**. [explicit, pp. 607, 614]
- **Worked cohort example (1941â€“45):** equalising circumstances reduces the Theil index from **0.997** to a counterfactual **0.632â€“0.675** (mean 0.656), i.e. a **32â€“37%** opportunity share. [explicit, p. 607]
- **Gini robustness:** cohort-average opportunity share â‰ˆ **13%** under the Gini (vs 23% under Theil) â€” a sizeable index-sensitivity. [explicit, p. 607]
- **Direct vs indirect split:** on average â‰ˆ **60%** of the circumstance effect operates **directly** on earnings (conditional on observed efforts), â‰ˆ **40%** indirectly through efforts; the direct-to-overall ratio averages â‰ˆ **61â€“62%** with a wide bounded interval (â‰ˆ **29â€“82%** excluding the youngest cohort). [explicit, pp. 608â€“609, 614]
- **Upper-bound thought experiment (all observed efforts treated as circumstances):** opportunity share averages â‰ˆ **36%**, bounded â‰ˆ **23â€“48%** across cohorts. [explicit, pp. 608â€“609]
- **Individual circumstances:** **parental education** is the dominant single circumstance across all cohorts; **father's occupation** second; **race** matters and is relatively more important for younger cohorts; **region of birth** contributes little once race and family background are controlled (â‰ˆ 1â€“2% of inequality). Parental schooling alone accounts for â‰ˆ 65â€“70% of the total observed-circumstance effect, rising to â‰ˆ 80% when father's occupation is added. [explicit, pp. 611â€“614]
- **Returns to own schooling (an "effort" coefficient):** â‰ˆ **9â€“12%** per year (bounds â‰ˆ 8â€“13%), lower than some prior Brazilian estimates, attributed to including parental-background controls. [explicit, p. 603]
- **Cross-cohort pattern:** weak evidence that the opportunity share declines for younger cohorts, but the authors caution that cohort, age, and period effects cannot be separated in a single cross-section, and that the youngest cohort's estimate is fragile (part-time incidence inflating residual variance). [explicit, pp. 610â€“611]

**Benchmarking value for me:** a 10â€“37% (central â‰ˆ 23%) circumstance share against *earnings* inequality is a coarse plausibility anchor for the magnitude of an opportunity share, but it is **not** directly comparable to my welfare-inequality opportunity surface â€” different outcome (earnings vs money-metric welfare), different circumstances (family background vs labour-market access/ability), different index treatment, and different decomposition rule. Use it as an order-of-magnitude sanity check only, with the non-comparability stated. [derived-by-analogy]

---

## 10. Estimators, theorems, or formal results

This is an applied paper; there are **no theorems**. The reusable formal objects are definitions/estimators:

1. **Overall opportunity share (p. 595, eq. 3).**
   - Statement: $\Theta_I := \dfrac{I(F) - I(\tilde\Phi)}{I(F)}$, with $\tilde\Phi$ the counterfactual earnings CDF under equalised circumstances.
   - Assumptions: a (possibly biased) reduced-form earnings model; an inequality index $I$; the equality-of-circumstances benchmark as the equalisation operator.
   - Technique: fit reduced form by OLS; simulate $\tilde w_i = \exp(\hat\psi\bar C + \hat\varepsilon_i)$; recompute $I$; take the proportional fall.
   - Reusability verdict: **maybe / conceptual yes** â€” the *form* of the share is reusable as my reporting object; the *engine* (OLS earnings) is replaced by my structural welfare object, and the *equalisation* is replaced by channel-equalisation in $g$ with Shapley averaging.

2. **Direct (partial) share (p. 596, eq. 4).**
   - Statement: $\Theta_I^d := 1 - \dfrac{I(\tilde\Phi^d)}{I(F)}$, with $\tilde\Phi^d$ the distribution that equalises circumstances in the earnings equation while holding observed efforts fixed.
   - Reusability verdict: **conceptual yes** â€” this is the antecedent of decomposing an opportunity effect into a piece that flows through the direct evaluation and a piece that flows through behaviourally-mediated channels; loosely analogous to my distinction between the direct evaluation channel and the attainment channel, though the mechanisms differ entirely. State the analogy as loose, not exact.

3. **Bias-bounding procedure (pp. 598â€“600).**
   - Statement: treat $\rho_{Xu}$ as unknown; the OLS bias is $B = (X'X)^{-1}\mathrm{cov}(X,u)$; draw $\rho_{Xu}\sim U(-1,1)$ componentwise; retain draws with $K \le 1$ (PSD of the implied covariance) and satisfying four sign restrictions; report a 90% interval over retained draws.
   - Reusability verdict: **no** for my pipeline (I use synthetic recovery and cluster-robust bootstrap), but a **citable precedent** for reporting an opportunity share as a defensible interval rather than a point.

---

## 11. Robustness and specification sensitivity

What they vary and what moves: [explicit unless noted]
- **Inequality index:** Theil â†’ Gini roughly halves the cohort-average share (23% â†’ 13%), establishing strong index-sensitivity of the opportunity share. (p. 607)
- **Circumstance partition:** single-circumstance equalisations show parental education dominant, region negligible. (pp. 611â€“612)
- **Effort reclassification:** treating efforts as circumstances raises the share to â‰ˆ 36% â€” an internal upper bound on the observed-variable share. (pp. 608â€“609)
- **Sample scope:** urban-only baseline; a joint urban+rural check raises shares modestly (â‰ˆ 2â€“19% relative, not percentage points, excluding the youngest cohort). (pp. 607â€“608)
- **Selection:** a Heckman correction was tried; the Mills ratio was insignificant and second-stage coefficients were similar, so OLS is retained for prime-age urban men. (p. 601, footnote)
- **Bias bounds:** the 90% intervals over admissible correlations are the principal robustness device throughout.

**Lessons for my recovery/stability and robustness sections:**
- **Index-sensitivity is first-order.** Their Theil-vs-Gini gap is a warning that my opportunity surface must report the index explicitly and probably show more than one index; do not headline a single number whose magnitude is half-driven by the index choice. [derived-by-analogy]
- **Single-factor contributions need not sum to the total** unless order-averaged â€” a direct argument for my Shapley exhaustiveness gate. [derived-by-analogy]
- **An internal upper-bound construction** (their "efforts-as-circumstances") is a cheap, interpretable way to bracket a share; my access-only vs access+ability bracket plays the analogous role. [derived-by-analogy]

---

## 12. What I can cite this paper for

- A **canonical, early operationalisation** of Roemer's circumstance/effort distinction into a measurable share of *outcome* inequality attributable to factors beyond individual control. [explicit]
- The **counterfactual-equalisation definition** of an opportunity share, $\Theta_I = [I(F)-I(\tilde\Phi)]/I(F)$, and its **explicit index-dependence**. [explicit, p. 595]
- The **direct/indirect anatomy** of an opportunity effect (effect on outcomes conditional on mediators, vs effect operating through mediators). [explicit, p. 596]
- A **partial-identification posture**: reporting a *bounded interval* for an opportunity share when the underlying parameters are not point-identified, rather than a falsely precise point. [explicit, pp. 598â€“600]
- **Magnitude benchmark:** that a small set of background circumstances can account for on the order of 10â€“37% (central â‰ˆ 23%, Theil) of earnings inequality in a high-inequality setting. [explicit, p. 614]
- The finding that **index choice (Theil vs Gini) materially changes the share**. [explicit, p. 607]

---

## 13. What I should NOT cite this paper for  [overclaim risks]

- **Two-way, not three-way.** Its cut is circumstance vs residual (effort + unobservables). It does **not** deliver an access / ability / preference three-way split; do not present it as a precedent for separating ability from access, nor for isolating preferences. [established]
- **No welfare object.** It decomposes *earnings inequality*, not money-metric welfare. Do not cite it as computing equivalent income, EV/CV, or any $W^1$â€“$W^6$-type object; it contains none. [established]
- **No Independence-of-$y$ / Independence-of-$A$ structure.** Do not attribute my measure taxonomy or its normative readings to this paper. [established]
- **Occupation-as-status, not occupation-as-access or sector.** Father's occupation is a sociological-status *circumstance*; own labour-market status is an *effort*. Neither is my `loc4` occupation-availability object, and neither is `lindi`/NACE industry. Do not let their "occupation" language migrate into my access vocabulary. [established]
- **No feasible-set / latent-jobs mechanism.** Do not cite it as modelling job opportunities, offers, hours availability, or local labour demand; its "opportunity" is background circumstance, not labour-market feasibility. [established]
- **No causal point identification.** Do not cite the shares as causal estimates; they are associations under maintained assumptions, with the bias bounds as the honest qualifier. [explicit, pp. 597â€“600]
- **Not Shapley / not order-independent.** Do not cite it for Shapley or Shorrocks exhaustiveness; the single-circumstance contributions are not order-averaged. [established]
- **Theory-paper boundary.** Irrelevant here in substance (this is not the Haydarâ€“Maniquet companion), but the general rule stands: never read this empirical IOp paper as supplying my axiomatic/normative *characterisation* â€” it supplies *motivation and a reporting template*, not foundations.

---

## 14. Direct quotes worth citing

Each quote is short and used once; page numbers from the printed journal.

1. On the ethical premise (quoting Peragine within the paper), p. 585: inequalities due to factors beyond individual responsibility are inequitable and to be compensated, whereas those due to personal responsibility are not [verify exact wording against p. 585 before quoting verbatim; paraphrase preferred].
2. On the measurement gap, p. 586: the authors note that empirical use of the opportunity concept has been rare because economists have lacked agreed ways to measure inequality of opportunity. [paraphrase; verify if a verbatim phrase is wanted]
3. On the headline magnitude, p. 614: five observed circumstances account for between 10 and 37 percent of within-cohort earnings inequality, with a cross-cohort mean near 23 percent. [paraphrase of the explicit result, p. 614]

> Note: I have deliberately kept these as paraphrase/short fragments and flagged the one near-verbatim fragment for verification, to respect quotation limits. Pull exact verbatim strings from the PDF at draft time if a direct quote is required.

---

## 15. Open questions and risks for my draft

- **Index-sensitivity contaminates the headline.** Their 23%-vs-13% Theil/Gini gap is a direct warning that an opportunity share is not a primitive but an index-conditional object. My opportunity surface must be reported with the index fixed and ideally shown across at least two indices; otherwise a referee will (rightly) attribute magnitude to the index. [derived-by-analogy]
- **The "residual = everything else" trap.** Their residual silently bundles preference heterogeneity, luck, and measurement error with genuine effort. My entire contribution is to *not* do this â€” to put preferences in an estimated block rather than the residual. The risk is the mirror image: that my *preference* component absorbs mis-specified opportunity, which is why the synthetic-recovery gate and the wide-but-identified preference standard errors matter. Cite this paper as the thing I improve upon, and be explicit that the improvement is *moving preference out of the residual*. [derived-by-analogy]
- **Causal humility.** Even with a structural model, my decomposition shares is conditional on the maintained opportunity-density specification; their candid bounding posture is a model for how to write the identification caveat without overclaiming. [explicit on their side]
- **Single-cross-section cohort/period/age confound.** Their inability to separate cohort, age, and period effects from one 1996 wave is a caution for any temporal reading of my pooled 2015â€“2017 sample; I pool three adjacent waves, so temporal interpretation must stay minimal. [explicit, pp. 610â€“611]

---

## 16. TL;DR for retrieval

Bourguignonâ€“Ferreiraâ€“MenÃ©ndez (2007) is the canonical reduced-form **decomposition** antecedent: it defines the opportunity share of *earnings* inequality as the proportional fall in a Theil/Gini index when observed background **circumstances** (race, region of birth, parental education, father's occupation) are equalised, and splits it into a **direct** wage effect (â‰ˆ60%) and an **indirect** effect through circumstance-shaped "efforts," reporting 10â€“37% (central â‰ˆ23%, Theil) for urban Brazilian men in 1996 under a sign-restricted partial-identification bounding scheme. For my JMP it informs only the **reporting form** of the opportunity share and the direct/indirect anatomy on the **access** side; it has **no preference object, no welfare/equivalent-income object, no feasible-set mechanism, no ability/access split, and no Shapley property**, so it is an antecedent and a magnitude benchmark, never a source for my three-way access/ability/preference Shapleyâ€“Shorrocks welfare decomposition or my $W^1$â€“$W^6$ family.
# Dagsvik, Jia, Kornstad & Thoresen 2014 â€” Theoretical and Practical Arguments for Modeling Labor Supply as a Choice among Latent Jobs

> **Extraction note.** This is a **survey / methodological-arguments** paper, not
> an empirical estimation paper. Its empirical figures are borrowed from Dagsvik
> & Jia (2012a). The primary technical derivations of the latent-jobs model live
> in **Dagsvik & StrÃ¸m (2006)** and **Dagsvik & Jia (2012a)**, to which this paper
> repeatedly defers; cite those for the machinery, this one for the *argument and
> interpretation*. Throughout I flag **[explicit]** (stated in this source),
> **[analogy]** (derived by mapping to the JMP), and **[not established]** (absent
> from this source). Pages cited from the running headers in the supplied PDF;
> ambiguous locations marked **[verify]**.

---

## 0. Metadata

- **BibTeX key:** `dagsvik_jia_kornstad_thoresen_2014`
- **Authors:** John K. Dagsvik (Statistics Norway and Ragnar Frisch Centre for Economic Research); Zhiyang Jia, Tom Kornstad, Thor O. Thoresen (Statistics Norway).
- **Year:** 2014 (Â© 2013).
- **Outlet:** *Journal of Economic Surveys*, Vol. 28, No. 1, pp. 134â€“151.
- **DOI:** 10.1111/joes.12003 [explicit, p.134].
- **PDF:** `Dagsvik_et_al__-_2014_-_THEORETICAL_AND_PRACTICAL_ARGUMENTS_FOR_MODELING_LABOR_SUPPLY_AS_A_CHOICE_AMONG_LATENT_JOBS.pdf`
- **Tier:** T1A (as filed). Qualifier: it is the *programmatic statement* of the latent-jobs research program rather than its technical core.
- **JMP block(s) it serves:** **model-foundation / motivation**; **estimation** (the latent-jobs likelihood form); **identification** (the preference-vs-opportunity separation result); **opportunity-mechanism â€” access** (hours availability $g(h)$ and total job availability $\theta$). It does **not** serve the **welfare** or **decomposition** blocks (no welfare measure, no inequality index, no decomposition is computed), and it speaks to **ability** only obliquely (a separately estimated qualifications-based wage equation, not an opportunity-density channel).

---

## 1. One-paragraph relevance to my JMP

This is the canonical theoretical justification for the object at the centre of my structural layer: it shows that the *ad hoc* part-time/full-time dummies of the conventional van Soest discrete-choice model can be re-read as an **explicit, structural opportunity term** $\log(\theta g(h))$ inside the choice index, i.e. that my opportunity-density terms ($\log h$, $\log\text{market}$) have a demand-side foundation rather than being a fitting device [explicit, pp.139â€“141]. It speaks directly to my **access** channel (the hours-opportunity distribution $g(h)$ and the total-job-availability scalar $\theta$, the latter linkable to the unemployment rate) and supplies the foundational **identification** result I must defend: preferences and the opportunity distribution are separable only up to an additive function of hours unless one imposes functional form (Boxâ€“Cox) or uses desired-hours data [explicit, p.143]. It does **not** separate **ability** from **access** within the opportunity object, computes **no** welfare measure, and contains **no** decomposition â€” so it anchors my estimation and identification prose, not my welfare or decomposition prose.

---

## 2. Data and setting

- This paper is a survey; it has no estimation dataset of its own. The empirical illustrations are **lifted from Dagsvik & Jia (2012a)**: **Norwegian married couples**, base year **1997**, Labour Force Survey data, with out-of-sample validation against 2006 LFS data and 2003 income-tax-return data [explicit, pp.144â€“145].
- **Sample unit in the illustration:** married couples (a joint decision unit) [explicit, p.144]. This matches my couples unit in spirit, but the figures are illustrative, not re-estimated here.
- **Key variables in the illustration:** annual hours of work discretised into eight intervals with positive-hours medians **260, 780, 1040, 1560, 1960, 2340, 2600** [explicit, p.144]; household disposable income (Figure 3) [explicit, p.146 [verify]].
- **Budget-set construction:** $C=f(hw,I)$, where $f(\cdot)$ maps gross income to after-tax household income and "can in principle capture all details of the tax and benefit system" [explicit, p.139, eq. (4)]. This is the same role my EUROMOD disposable-income map plays [analogy].
- **Transport to my France pooled 2015â€“2017 EUROMOD cross-section:** the *model* transports cleanly (static, discrete, tax-benefit budget). The *identification and validation strategy does not transport directly*: the paper's out-of-sample assessment exploits a **tax reform** (2006) and a second data source, and one of its two identification routes requires **desired/preferred-hours data** (Euwals & van Soest 1999; Bloemen 2008) [explicit, p.143]. I have **no panel, no desired-hours instrument, and no exploited reform**; I rely instead on functional form plus **synthetic recovery** (which this paper does not use). Features named here that I do **not** have: a tax-reform natural experiment for out-of-sample validation; desired-hours data; job-specific wage data of the Dagsvikâ€“Jia (2012a) "general case."

---

## 3. Model and objects (object-by-object map to mine)

- **Choice set = my latent-jobs set?** **Yes, conceptually [explicit].** The agent chooses among *jobs* $z=1,2,\dots$ (with $z=0$ the non-market alternative), each job carrying fixed job-specific hours $H(z)$ and non-pecuniary attributes; observed hours and income are those of the chosen job [explicit, pp.139â€“140, eq. (8)]. The choice sets $\{B(h)\}$ (available jobs with hours $h$) are latent to the researcher [explicit, p.140]. This is exactly my latent-jobs framing.
- **Deterministic utility = my preference utility $v$?** **Yes [explicit].** $U(C,h,z)=v(C,h)+\varepsilon(z)$ with $\varepsilon(z)$ iid Gumbel; $v(C,h)$ is the systematic preference term [explicit, p.139, eq. (8)]. The recommended functional form is **generalized Boxâ€“Cox in consumption and leisure with an interaction term** (eq. (15)) [explicit, p.143] â€” the same family as my preference block.
- **Explicit opportunity / availability mechanism analogous to my $g$?** **Yes, but only over hours and total count [explicit].** The number of available jobs at hours $h$ is $m(h)$; with $\theta=\sum_x m(x)$ and $g(h)=m(h)/\theta$, the term $\theta g(h)$ is the **opportunity measure** and $g(h)$ the **opportunity distribution** [explicit, p.141]. It enters the choice index additively as $\log(\theta g(h))$ (eq. (14)) [explicit, p.141].
  - **hours channel:** present, as $g(h)$ [explicit].
  - **market / participation channel:** present, as $\theta$ (total job availability; depends on education and a constant; linkable to the unemployment rate) and the single non-market alternative $m(0)=1$ [explicit, pp.140â€“141, 143; footnote 12 p.148].
  - **wage (ability) channel:** **not in the opportunity density of this exposition.** The baseline assumes the wage "only depends on individual qualifications and does not vary across jobs" [explicit, p.139]; wages are predicted from a **separately estimated wage equation** [explicit, p.144]. Job-specific wages are deferred to the cited Dagsvik & Jia (2012a) "more general case" [explicit, p.139].
  - **occupation channel:** **absent in the baseline** ("the jobs are latent and thus job characteristics do not appear") [explicit, p.144]. The cited Dagsvik & StrÃ¸m (2006) extension classifies jobs into **two observable sectors (public and private)** [explicit, p.144].
- **Budget map = my EUROMOD disposable income?** Functionally yes (eq. (4)); their $f$ is my EUROMOD map [analogy].
- **Does any job attribute enter BOTH utility and the opportunity mechanism?** **No [explicit].** Hours enter utility via $v(C,h)$ and availability via $g(h)$, but these are distinct objects whose **non-separability is the paper's central identification caveat** (Â§8), not a deliberate double-entry. They do not place wage or occupation in both blocks; in fact the baseline keeps occupation out of both. No identification-driven double-entry is asserted.

**Differences to record.** (i) Their opportunity object is **one-dimensional over hours** (plus the scalar $\theta$); my $g$ additionally carries a **wage/ability** sub-block and an **occupation** access sub-block, which are beyond this paper [explicit vs. JMP]. (ii) They use a **fixed finite hours grid $D$ with multiplicities $m(h)$**, not a **sampled** alternative set; consequently there is **no sampling-of-alternatives correction** in their likelihood (see Â§4b). (iii) Their "sector" (public/private) is an **institutional** partition â€” it is *neither* my occupation (`loc4`/ISCO) *nor* my industry (`lindi`/NACE); do not map it onto either.

---

## 4. Estimation method

- **Likelihood / estimator:** multinomial-logit-type choice probabilities derived from the iid-Gumbel RUM, with representative utilities $\{\psi(h)\}$ **weighted by job frequencies $\{m(h)\}$** (eqs. (10)â€“(11)) and re-expressed as $\exp(\psi(h)+\log(\theta g(h)))$ in the denominator-normalised form (eq. (14)) [explicit, pp.140â€“141]. Maximum likelihood, with the wage equation, choice probabilities, and opportunity measure specified jointly [explicit, p.144]. No GMM, no simulated argmax in the exposition.
- **Choice-set construction:** **fixed discrete grid** of hours points $D$ (the illustration uses eight intervals). Discretisation is argued to be inessential and arbitrarily refinable [explicit, pp.139, 144].
- **Proposal / sampling density:** **none** â€” the grid is fixed, not sampled (see Â§4b).
- **Prior/proposal correction ($-\log\pi$ subtracted from the choice index)?** **Not established / not present.** The additive term inside the index is the **structural** $\log(\theta g(h))$, not a nuisance sampling correction. It is always well defined for $g(h)>0$ [analogy]; the question of an importance-sampling prior does not arise here.
- **Normalisation / scale:** the summability constraint $\sum_h g(h)=1$ need **not** be imposed at estimation because $\theta g(h)$ enters jointly and the normalisation can be applied post-estimation [explicit, p.143]. Fixed cost can be folded into $\theta$ as $\theta\exp(c)$ (Cogan 1981) [explicit, p.141].
- **What pins preferences apart from the opportunity mechanism:** functional-form restrictions (Boxâ€“Cox, eq. (15)) â€” see Â§8. Without them the two are confounded up to an additive $d(h)$ [explicit, p.143].
- **Numerical method / starting values / multistart:** not discussed in this survey [not established]. (Boxâ€“Cox estimation difficulties are flagged â€” Â§11.)
- **Verdict â€” reusable for my RURO/JAX pipeline?** **Partly â€” as the structural template, not as a runnable recipe.** Reuse: the $\exp(\text{utility}+\log\text{opportunity})$ index structure (eq. (14)) is exactly my per-alternative value's structural backbone, **minus** my $-\log\pi$ correction (which my pipeline needs because I *sample* alternatives, whereas they use a fixed grid). Do **not** reuse: their fixed-grid construction in place of my sampled set; and there is no estimation code or numerical protocol to reuse here (it is in the cited companions).

## 4b. Proposal / sampling-of-alternatives correction  [extract even if brief]

**Not present in this paper.** Alternatives are a **fixed finite grid** of hours points with structural multiplicities $m(h)$; there is no random sampling of alternatives and therefore no McFadden-style sampling correction and no per-alternative log-prior [explicit, pp.139â€“141]. The additive log-term $\log(\theta g(h))$ that appears inside the choice index (eq. (14)) is a **structural opportunity weight** (the object of interest), **not** a proposal/prior correction â€” this is the single most important place a careless reader could conflate their model with my pipeline. Mapping to my design: their $\log(\theta g(h))$ is the analogue of my **structural** $[\log h + \log w + \log\text{market}]$ block, **not** of my $-\log\pi(j;x_i)$. My $-\log\pi$ exists only because I integrate over *sampled* draws; it has no counterpart here. Relation to my proposal-individualisation concern (wage/occupation individualised; hours/employment common): **not addressed** â€” the question is meaningless for a fixed grid [not established].

## 5. Opportunity mechanism  [MOST IMPORTANT â€” split by channel]

The mechanism is a **deterministic density over hours plus a total-availability scalar**, derived from latent job multiplicities. Formally: $B(h)$ is the set of available jobs with hours $h$; $m(h)=|B(h)|$; $m(0)=1$; $\theta=\sum_{x\in D} m(x)$; $g(h)=m(h)/\theta$; the **opportunity measure** is $\theta g(h)$ [explicit, pp.140â€“141]. The $\{m(h)\}$ are **sufficient statistics** for the latent choice sets under the iid-Gumbel assumption [explicit, p.141]. Equilibrium foundation: $\theta$ can be derived from a two-sided matching model (Dagsvik 2000; Dagsvik & Jia 2012b), but the paper uses a **reduced-form** representation [explicit, p.142] â€” as do I [analogy].

Mapping to my three sub-objects:

- **access (hours / market / region / year / occupation offers).**
  - *Hours availability:* **explicit and central** â€” $g(h)$. The standard empirical specification is **$g(h)$ uniform apart from peaks at part-time and full-time hours** [explicit, p.143], implemented as $\log(\theta g(h))$ **linear in length of schooling plus part-time and full-time dummies** [explicit, p.144]. This is the demand-side reinterpretation of van Soest's hours dummies â€” the foundation for treating my hours-availability terms as structural access rather than fitted taste.
  - *Market / participation:* **explicit** â€” $\theta$ (total job availability), allowed to depend on education and a constant, and linkable to the unemployment rate and business-cycle variation [explicit, pp.141, 143; footnote 12, p.148]. The non-market alternative is the single $z=0$ with $m(0)=1$.
  - *Region / year:* **not modelled** in this paper [not established]. (My access sub-block's regional, urbanisation, and year shifters are beyond it.)
  - *Occupation offers:* **not in the baseline** [explicit, p.144]. The cited two-sector (public/private) extension is institutional, not occupational.
- **ability (wage technology: returns to education/experience, residual productivity).** **Present but outside the opportunity density.** Wages depend on individual **qualifications** through a separately estimated wage equation, with random effects giving a **mixed multinomial logit** that also relaxes IIA (McFadden & Train 2000; used by Dagsvik & StrÃ¸m 2006, Dagsvik & Jia 2012a, Kornstad & Thoresen 2007) [explicit, pp.142, 144]. This is the closest object to my **ability** sub-block, but the paper does **not** fold it into $g$ as a job-availability channel, and does **not** separate ability from access *within* opportunity [explicit + not established]. My ability-in-$g$ design is therefore an **extension beyond** this source.
- **occupation as availability vs. something else.** In the baseline, occupation is **absent** (jobs latent, characteristics suppressed) [explicit, p.144]. In the cited extension it is an **observable sector (public/private)** entering as an additional discrete dimension [explicit, p.144]. **Flag:** their "sector" is an institutional split; it must **not** be mapped to my occupation-as-access (`loc4`, ISCO-type) nor to my reserved industry object (`lindi`, NACE). The paper does **not** conflate occupation with industry â€” it simply does not use either; the conflation risk is on the *reader's* side, not the source's.

**Functional form:** $g(h)$ piecewise-constant with PT/FT peaks; $\log(\theta g(h))$ linear in schooling and PT/FT dummies [explicit, pp.143â€“144]. **Deterministic** in the baseline ("So far we treat the terms $\{m(h)\}$ as deterministic") [explicit, p.140]; the paper *also* offers a **stochastic-choice-set** interpretation (Dagsvik 1994; Dagsvik & StrÃ¸m 2006; Dagsvik & Jia 2006; Dickensâ€“Lundberg) that accommodates unobserved heterogeneity in opportunities [explicit, pp.141â€“142] â€” which I do **not** adopt (my opportunities are deterministic). 

**Cost to my decomposition if the mechanism were omitted:** the source itself states the payoff â€” without an explicit $\log(\theta g(h))$, the PT/FT peaks would have to be absorbed into $v(C,h)+\gamma(h)$ as taste, making the model non-structural and policy simulation uninterpretable [explicit, pp.138â€“139]. That is precisely my motivation for putting access in $g$ rather than letting it masquerade as preference; this paper is the cleanest citation for that argument.

## 6. Welfare object â€” and its place on my $W^1$â€“$W^6$ map

**The paper computes no welfare measure. [explicit / not established]** It motivates structural modelling by noting that counterfactual policy effects "are at the core of discussions on welfare effects of policy changes" [explicit, p.136] and cites Chetty (2009) on sufficient statistics for welfare analysis [explicit, footnote 3, p.148], but it constructs **no** money-metric welfare, **no** equivalent income, **no** compensating/equivalent variation, and **no** inclusive-value welfare object. The only distributional output is a **descriptive** predicted disposable-income distribution for model assessment (Figure 3) [explicit, p.146 [verify]].

**Placement on my $W^1$â€“$W^6$ map:** **N/A.** The source does **not** contain $W^1$â€“$W^6$, does not use Independence-of-$y$ / Independence-of-$A$, and takes no compensationâ€“responsibility stance. Do not attribute any welfare-measure family to it. **Verdict: incompatible as a welfare source** (it is upstream of welfare â€” it supplies the structural utility/opportunity primitives the welfare layer consumes, nothing more).

## 6b. Inclusive value and money-metric inversion  [extract if used]

**Not established as a welfare construction.** The **log-sum denominator** appears in the choice probabilities (eqs. (10)â€“(14)) [explicit], and the expectation over the Gumbel shocks is taken **analytically** (this is what yields the closed-form MNL form) [explicit, by construction]. But the paper never elevates the log-sum to an **inclusive-value welfare** object and never performs a **money-metric inversion** (no one-dimensional solve to a money figure, no EV/CV). So: *analytic-in-shocks* â€” **yes, shared** [explicit, structurally]; *inclusive value as welfare core* â€” **not in this paper** [not established]; *inversion to money* â€” **absent** [not established]. My analytic-in-shocks, importance-sampling inversion shares only the analytic-expectation step with this source.

## 7. Inequality / decomposition content  [three-way where relevant]

**None. [explicit / not established]** No inequality index (no Gini/MLD/Theil/Atkinson), no decomposition rule (no Shapley/Shorrocks/factor/subgroup/RIF), no counterfactual equalisation. The disposable-income *distribution* in Figure 3 is a goodness-of-fit display, not an inequality analysis [explicit, p.146 [verify]]. **Verdict: not reusable for my three-way access/ability/preference Shapleyâ€“Shorrocks split.** The paper is silent on decomposition entirely; it is neither two-way nor three-way. To connect it to my decomposition would require building the entire welfare-and-decomposition layer *on top of* its structural model â€” which is exactly my contribution, not theirs.

## 8. Identification and the separation of preferences from opportunities  [STRICT]

This is the paper's most load-bearing contribution for me.

- **The confounding result [explicit, p.143].** For positive $h$, the choice index contains $\psi(h)+\log g(h)=v(f(hw,I),h)+\log g(h)$. Assuming the offered wage does **not** depend on hours and parameters are constant across the population, Dagsvik & Jia (2012a) show $v(C,h)$ is identified **only up to an additive term $d(h)$ depending on hours** â€” i.e. **preferences and the opportunity distribution are non-parametrically separable only up to an additive function of $h$.**
- **What restores full identification [explicit, p.143].** Either (i) **functional-form assumptions** â€” the Boxâ€“Cox form (eq. (15)), justified on invariance-principle grounds (Dagsvik & RÃ¸ine Hoff 2011; Dagsvik 2012), under which the model is identified; or (ii) **data on desired/preferred hours** (Euwals & van Soest 1999; Bloemen 2008).
- **Policy-simulation escape clause [explicit, p.143].** For counterfactuals that only change the budget $f$, one need **not** separate the hours-utility term from $g(h)$, because neither depends on $f$. (This does *not* help me: my decomposition *requires* the separation, since I equalise channels.)
- **Ability vs. access within opportunity:** **not addressed [not established].** The paper's identification argument is **preference vs. (hours) opportunity** only. It offers **no** argument separating a wage/ability sub-block from an access sub-block inside $g$. My three-way cut's ability/access boundary therefore cannot be supported by this paper; it rests on my own functional-form-plus-channel-assignment, and is exactly the part a "your decomposition is mechanical" referee will press.
- **Transport to my France pooled cross-section.** The functional-form route (i) **transports** â€” it is precisely my strategy (Boxâ€“Cox preferences). The desired-hours route (ii) does **not** â€” I have no desired-hours data. The paper's *assessment* standard is **out-of-sample prediction across a tax reform**, **not synthetic recovery** [explicit, pp.144â€“145]; so this paper does **not** license my synthetic-recovery certification â€” I must cite it for the *identification logic* (separation is parametric, not nonparametric) and source the recovery-as-evidence standard elsewhere. Honest net statement: **Dagsvik et al. establishes that preference/opportunity separation in latent-jobs models is inherently parametric and defensible on functional-form grounds; it does not, and cannot, certify the finer ability/access separation my decomposition needs.**

## 9. Key results and magnitudes

The paper reports **no estimated parameters of its own**; magnitudes are illustrative or borrowed.

- **Wage elasticities (borrowed from Dagsvik & Jia 2012a):** "of moderate magnitude, with married females more responsive than males," broadly in line with the literature; **no numerical values given here** [explicit, p.146]. The discrete-choice literature (including theirs) typically reports **gross** (pre-tax) wage elasticities, unlike the Hausman-type post-tax convention [explicit, p.146].
- **Illustrative logit elasticity arithmetic [explicit, p.147]:** for $P(w,X)=1/(1+\exp(-\alpha\log w - X\beta))$, the participation wage elasticity is $(1-P)\alpha$; at $P=0.6$ it is $0.4\alpha$, at $P=0.8$ it is $0.2\alpha$. This is a pedagogical point that **nonlinear models yield sample-dependent elasticities**, not an estimate.
- **Out-of-sample fit (Norway):** the 2006 tax reform cut the top marginal rate from **55.3% to 47.8%** [explicit, p.144]; the model's predicted **female** hours distribution for 2006 tracks the actual better than the 1997 baseline, while **male** responses are not well reproduced [explicit, pp.144â€“145]; the 2003 predicted disposable-income distribution matches the data closely [explicit, p.145].
- **Benchmarking value for me:** "females more responsive than males, both moderate" is a sanity band for my own elasticities **if** I compute them (currently deferred); there are **no opportunity-share or welfare-spread magnitudes** here to benchmark my decomposition against.

## 10. Estimators, theorems, or formal results

No numbered theorems. The reusable formal objects are the choice-probability derivations and the functional form.

1. **Latent-jobs choice probability (eq. (14)) [explicit, p.141].**
   $$\varphi(h)=\frac{\exp\!\big(\psi(h)+\log(\theta g(h))\big)}{\exp(\psi(0))+\sum_{x\in D}\exp\!\big(\psi(x)+\log(\theta g(x))\big)}.$$
   - Assumptions: iid Gumbel shocks $\varepsilon(z)$; $v(C,h)+\varepsilon(z)$ utility; fixed-hours jobs; $m(h)$ deterministic (baseline).
   - Technique: McFadden RUM â†’ MNL; sum over $z\in B(h)$ collapses the job-level probability (eq. (9)) into the hours-level probability via the multiplicity $m(h)$; $\{m(h)\}$ are sufficient statistics for the latent sets.
   - **Reusability: yes** â€” this *is* the structural form of my per-alternative value, minus the $-\log\pi$ sampling correction my pipeline adds.
2. **Boxâ€“Cox systematic utility (eq. (15)) [explicit, p.143].**
   $$v(C,h)=\gamma\frac{C^{\alpha}-1}{\alpha}+\delta\frac{(M-h)^{\beta}-1}{\beta}+\mu\frac{(C^{\alpha}-1)\big((M-h)^{\beta}-1\big)}{\alpha\beta}.$$
   - Assumptions: $\alpha<1,\beta<1,\gamma>0,\delta>0$, $\mu$ constrained â†’ strict concavity; $M$ = maximum feasible hours.
   - Technique: derived from qualitative-measurement / invariance axioms (Dagsvik & RÃ¸ine Hoff 2011; Dagsvik 2012); under it the model is identified.
   - **Reusability: yes** â€” same preference family as my utility block (consumption, leisure, interaction). Note my baseline carries demographic taste-shifters and gender that this generic form does not write out.
3. **Identification-up-to-$d(h)$ result [explicit, p.143].** Statement and assumptions as in Â§8. **Reusability: yes, as a cited identification primitive** for the preference/opportunity separation; **no** for ability/access separation.

## 11. Robustness and specification sensitivity

- **Boxâ€“Cox vs. quadratic [explicit, p.143]:** Boxâ€“Cox yields roughly the same fit as quadratic; quadratic can fail to be increasing in leisure; Boxâ€“Cox is harder to estimate (nonlinear in parameters). **Mastrogiacomo et al. (2011)** report estimation difficulties; **Blundell & Shepard (2012)** obtained an unacceptable estimate of one Boxâ€“Cox parameter. â†’ A direct warning for my own Boxâ€“Cox estimation; relevant to my pinned/at-bound parameters.
- **Number of discrete alternatives [explicit, pp.139, 144]:** discretisation is argued inessential and arbitrarily refinable; the discrete setting may even be the "true" one. â†’ Supports my fixed-resolution grids as defensible, not a mere approximation.
- **IIA relaxation [explicit, pp.142]:** nested MNL, random effects, or a random-effects wage equation (mixed MNL) relax IIA without ad hoc terms. â†’ Optionality for my robustness, though my baseline does not need it.
- **Elasticities sample-dependent in nonlinear models [explicit, pp.146â€“147].** â†’ Caution for any elasticity reporting I add.
- **Model assessment = out-of-sample prediction [explicit, pp.144â€“145].** Their stress test is predicting a different year / a reform, **not** synthetic recovery. â†’ My recovery-based certification is a *different* (and, for my no-reform setting, more available) standard; cite this for the limits of in-sample fit, not for recovery.

## 12. What I can cite this paper for

- That the conventional discrete-choice (van Soest) model's PT/FT **dummies can be reinterpreted as a structural opportunity term** $\log(\theta g(h))$ arising from demand-side job availability â€” the foundation for treating my access terms as structural rather than as fitted taste [pp.138â€“141].
- The **definitions** of the opportunity measure $\theta g(h)$ and opportunity distribution $g(h)$, with $\theta$ as total job availability (education-dependent, unemployment-linked) [pp.140â€“141].
- The **identification result** that preferences and the opportunity distribution separate only up to an additive $d(h)$ absent functional-form or desired-hours information, hence that **the separation is parametric** [p.143].
- That **Boxâ€“Cox** preferences are the invariance-justified, identification-securing functional form for this class of models [p.143].
- That the latent-jobs model **rationalises hours peaks structurally** and thereby keeps counterfactual simulation interpretable, where dummy-augmented conventional models do not [pp.138â€“139].
- That a **reduced-form** opportunity measure has an **equilibrium (two-sided matching)** foundation [p.142].
- General methodological cautions: Boxâ€“Cox estimation fragility; nonlinear elasticity sample-dependence; discretisation as inessential [pp.143, 146â€“147].

## 13. What I should NOT cite this paper for  [overclaim risks]

- **Any welfare measure.** It computes none; do **not** cite it for money-metric welfare, equivalent income, EV/CV, or inclusive-value welfare. **It does not contain $W^1$â€“$W^6$** or any compensationâ€“responsibility / Independence-of-$y$ / Independence-of-$A$ framing.
- **Any decomposition.** No inequality index, no Shapley/Shorrocks, no opportunity-vs-preference split â€” and certainly no **three-way access/ability/preference** split. Citing it for a decomposition (even two-way) would be an overclaim.
- **Ability/access separation within opportunity.** Its identification logic is preference-vs-(hours-)opportunity only. Do not read it as licensing my ability/access cut.
- **Occupation/sector language.** Its only occupational object is a cited **public/private institutional sector** extension. Do **not** present this as my **occupation-as-access** (`loc4`/ISCO), and do **not** let it drift into **industry** (`lindi`/NACE) language. The paper does not conflate the two; I must not introduce the conflation.
- **Random vs. deterministic opportunities.** The paper offers a **stochastic-choice-set** interpretation alongside the deterministic baseline. Map only the **deterministic** reading to my design; do not import the random-choice-set framing.
- **Synthetic-recovery certification.** Its assessment standard is out-of-sample prediction, not parameter recovery. Do not cite it as precedent for my recovery gate.
- **Theory-paper boundary.** This is empirical-methods literature; it has no bearing on the companion Haydarâ€“Maniquet axiomatic paper. Do not let any of its content migrate into the theory paper's territory, and do not read the JMP as a theory contribution because it cites this.

## 14. Direct quotes worth citing

To respect copyright I reproduce one short verbatim phrase and give page-anchored pointers for the rest (pull exact wording directly from the PDF at these locations):

- p.141, defining the central object (verbatim): "We shall call Î¸g(h) the opportunity measure and g(h) the opportunity distribution."
- p.141 [pointer]: the sentence stating that $\log g(h)+\log\theta$ in eq. (14) is an explicit representation of demand-side choice restrictions, no longer an ad hoc addition.
- p.143 [pointer]: the sentence stating preferences and the opportunity distribution can be separated only up to an additive term depending on $h$.
- p.143 [pointer]: the sentence that full identification requires functional-form assumptions (or desired-hours data).
- p.144 [pointer]: the sentence stating that in this version jobs are latent and job characteristics do not appear, with the public/private two-sector extension referenced to Dagsvik & StrÃ¸m (2006).
- p.140 [pointer]: the sentence treating $\{m(h)\}$ as deterministic ("So far we treat the terms $\{m(h)\}$ as deterministic").

## 15. Open questions and risks for my draft

- **The parametric-separation risk is inherited, not solved.** The paper is candid that separation rests on functional form; my decomposition inherits this, and the referee point ("the access/preference split is a functional-form artefact") is *not* answered by citing Dagsvik â€” it is *named* by it. My synthetic-recovery evidence is the load-bearing answer, and this paper does not supply it.
- **Ability/access has no identification anchor here.** My finer cut needs its own defence (channel assignment as an explicit normative-cum-functional assumption); I cannot lean on this source for it.
- **Validation-standard mismatch.** Their out-of-sample/reform standard is unavailable to me (no exploited reform, no panel); I must justify recovery-based certification on its own terms.
- **No welfare/decomposition scaffolding to borrow.** Everything downstream of the structural model â€” the inclusive-value welfare inversion, the $-\log\pi$ welfare integrator, the Shapley split â€” is mine to build; this paper ends exactly where my contribution begins.
- **Wage/ability modelling choice.** They keep wages in a separate qualifications equation (job-invariant in the baseline). My decision to carry wage returns *inside* $g$ as an ability channel is a deliberate departure I should flag against this baseline, citing Dagsvik & Jia (2012a)'s job-specific-wage general case as the closer precedent.

## 16. TL;DR for retrieval

Dagsvikâ€“Jiaâ€“Kornstadâ€“Thoresen (2014) is the programmatic survey that reinterprets van Soest's ad hoc hours dummies as a **structural opportunity term** $\log(\theta g(h))$ â€” supplying the foundation and citation for my **access** channel (hours availability $g(h)$, total job availability $\theta$) and for the **preference-vs-opportunity identification** result (separable only up to an additive $d(h)$ absent Boxâ€“Cox functional form or desired-hours data). It treats **ability** only as a separate qualifications-based wage equation (not an opportunity-density channel), keeps occupation latent (with a cited public/private *sector* extension that is neither my ISCO occupation nor NACE industry), and contains **no welfare measure, no $W^1$â€“$W^6$, and no decomposition** â€” it is strictly upstream of my welfare/decomposition layers and informs only my estimation and identification prose.
# Dagsvik & Jia 2016 â€” Labor Supply as a Choice Among Latent Jobs: Unobserved Heterogeneity and Identification

> Source of truth: the attached JSTOR PDF (J. Appl. Econ. 31(3): 487â€“506). The companion
> `.md` was used only for navigation. Page numbers refer to the journal pagination (487â€“506).
> Tags used below: **[explicit]** = stated in the paper; **[analogy]** = derived by mapping
> to my design, not asserted by the paper; **[not-established]** = the paper does not do this;
> **[verify]** = could not be confirmed from the provided PDF body (e.g. supplementary-appendix
> material).

---

## 0. Metadata

- **BibTeX key:** `dagsvik_jia_2016_latent_jobs`
- **Authors:** John K. Dagsvik (Statistics Norway; Frisch Centre); Zhiyang Jia (Statistics Norway).
- **Year:** 2016 (published online 6 January 2015; received 1 Oct 2012, revised 23 Sep 2014). [explicit, p.487]
- **Outlet:** *Journal of Applied Econometrics*, Vol. 31, No. 3, pp. 487â€“506. [explicit, p.487]
- **DOI / URL:** DOI 10.1002/jae.2428; JSTOR stable URL `https://www.jstor.org/stable/10.2307/26609622`. [explicit, p.487]
- **PDF filename:** `Dagsvik_and_Jia_-_2016_-_Labor_Supply_as_a_Choice_Among_Latent_Jobs...pdf`
- **Tier:** **T1A** (core â€” the canonical identification statement of the RURO/latent-jobs framework my estimation layer instantiates).
- **JMP blocks served:** **identification** (primary); **estimation**; **opportunity-mechanism (access + ability)**; **motivation**. It does **not** serve welfare, decomposition, or normative-interpretation directly.

---

## 1. One-paragraph relevance to my JMP

This is the foundational identification paper for the exact structural object my estimation layer instantiates: a choice probability that factorises into a deterministic preference utility $v(C,h)$ and an *opportunity measure* $\theta\,g_1(h)\,g_2(w\mid h)$ over latent jobs. [explicit, pp.489â€“490] It is the paper that establishes â€” formally, on cross-section data â€” *when* preferences can be separated from the opportunity mechanism, which is precisely the separation my access/ability/preference decomposition presupposes; without that separation the decomposition is mechanical, and this paper is my primary defence on that point. [explicit, Â§3, pp.492â€“494] It speaks directly to **two of my three channels**: the wage sub-block $g_2(w\mid h)$ and its individual-ability random effect $\eta$ map to my **ability** channel, and the hours/availability objects $g_1(h)$ and $\theta$ map to my **access** channel. [explicit for the objects, pp.489â€“491; channel-naming is [analogy]] It does **not** compute welfare, an inclusive-value welfare core, or any inequality decomposition, and it contains nothing resembling my $W^1$â€“$W^6$ family; it is upstream machinery, not a welfare or decomposition source. [not-established]

---

## 2. Data and setting

- **Country / year:** Norway, single cross-section, **Norwegian Labor Survey 1997**. [explicit, p.495]
- **Dataset / unit:** Married/cohabiting **couples**; the labour-supply model is a **joint** couple decision. [explicit, pp.487, 495]
- **Sample size:** Table I reports household counts by employment configuration â€” both spouses working **2,254**; only husband working **256**; only wife working **5** (no "neither working" row is shown in the table). [explicit, p.495] Total over the listed cells $\approx 2{,}515$ couples; whether a non-working-couple cell exists is [verify] (not shown in the provided body).
- **Key variables:** age, length of schooling (education), potential experience ($=$ age $-$ schooling $-7$), non-labour income, gross hourly wage rate, weekly hours of work, number of children (0â€“6 and 7â€“18). [explicit, Table I, p.495]
- **Budget-set construction:** disposable income via a net-of-tax function $C=f(hw,I)$, with $I$ non-labour income; $f$ is stated to be able in principle to capture the full tax/benefit system. [explicit, p.489]
- **Transport to my France pooled 2015â€“2017 EUROMOD cross-section:** *Partial.* The structural form transports cleanly (cross-section, discrete latent-jobs couples, parametric Boxâ€“Cox utility, opportunity density). What I have that they do not: an explicit microsimulated budget (EUROMOD `ils_dispy`) rather than an estimated net-of-tax function; pooled multiple waves (they have one year). What they have/use that bears on me: a **three-stage wage-equation estimation** to handle measurement error in hours ("division bias"), because they observe weekly hours only and infer the wage by division. [explicit, pp.495â€“496] **Features I do NOT have, named explicitly:** no panel, no administrative match, no external opportunity instrument, no vacancy/offer data â€” and the paper itself states that even panel or independent cross-sections do not, in general, solve the identification problem. [explicit, p.492]

---

## 3. Model and objects (object-by-object map to mine)

| Their object | Mine | Match? | Note |
|---|---|---|---|
| Latent job "packages" $(H(z),W(z),\text{attributes})$, worker-specific unobserved choice set | latent-jobs set $\mathcal C_i$ | **Yes** [explicit, pp.487â€“489] | Theirs is conceptually infinite (Poisson-scattered); mine is a finite sampled grid (singles 101, couples 901). |
| Deterministic utility $v(C,h)$, Boxâ€“Cox | preference utility $v_i(c,\ell)$, Boxâ€“Cox | **Yes** [explicit, eq.(8), p.493] | Both Boxâ€“Cox in consumption and leisure; globally concave. Theirs is over $C$ and $(1-h/M)$. |
| Opportunity measure $\theta\,g_1(h)\,g_2(w\mid h)$ | opportunity density $g(j;x_i)$ | **Yes** [explicit, p.489] | This is the central shared object; see Â§5. |
| $g_1(h)$ â€” offered-hours density | **access** (hours availability) | **Yes** [explicit] | Their $g_1$ is uniform with peaks at PT/FT. |
| $g_2(w\mid h)$, wage equation, random effect $\eta$ | **ability** (wage technology + residual $\sigma$) | **Yes** [explicit eq.(4),(9); channel name [analogy]] | $\eta$ is explicitly called individual *ability* (p.494). |
| $\theta$ â€” job-availability scalar (ratio of market to non-market opportunities) | **market/participation** availability term ($\log\text{market}$) | **Partial** [explicit p.489; mapping [analogy]] | $\theta$ also absorbs psychic cost of working ($\theta<1$). |
| Market vs non-market opportunities ($z>0$ / $z<0$) | market/participation channel | **Yes** [explicit, p.488] | The participation margin is a market-vs-non-market split. |
| Budget $C=f(hw,I)$ | EUROMOD `ils_dispy` | **Analogous** [explicit] | Their estimated net-of-tax function â†” my microsimulated income. |
| **Occupation / sector** | my `loc4` access object | **Absent in the estimated model** | See flag below. |

**Flag â€” occupation/sector.** The estimated empirical model contains **no occupation and no sector variable.** [explicit] The paper uses "sector" to mean *labour-market sector* (e.g. public health care, teaching) and invokes it only as informal *explanation* for gendered hours peaks, plus a footnote that a sector-specific model (as in Dagsvik & StrÃ¸m 2006) *could* yield explicit sector-specific opportunity measures. [explicit, p.497 fn.9; p.501] Two consequences for me: (i) this paper is **not** a precedent for an occupation-as-access layer being estimated â€” it is a precedent only for the *idea* that sector/occupation belongs in the opportunity measure if added; (ii) their "sector" language is closer to industry than to my ISCO-type `loc4` task categories, so I must not cite it as support for `loc4`-as-occupation, and must keep my `loc4`/`lindi` discipline intact when citing.

**Flag â€” does any attribute enter BOTH utility and opportunity?** **No.** [explicit] The wage and hours enter the opportunity measure $g_2(w\mid h)g_1(h)$ and enter utility only through $C=f(hw,I)$ and through $h$; the wage technology / ability is purely in the opportunity side, never in $v$. Crucially, **non-labour income $I$ enters only through consumption and does not affect the opportunity measure** â€” this exclusion is the load-bearing identification device (Assumption 3 / Theorem 2). [explicit, pp.492â€“493] This is consistent with my design (occupation and the wage return live in $g$ only, never in $v$).

---

## 4. Estimation method

- **Likelihood / estimator:** maximum likelihood on the closed-form choice probabilities (2a,b)/(3a,b). [explicit, p.496]
- **Choice-set construction:** a **fixed grid** of eight feasible annual hours per spouse â€” $\{0,\,208,\,624,\,1040,\,1456,\,1950,\,2340,\,2600\}$ â€” with the offered-wage dimension handled by **integration/summation** over the wage density, not by a sampled-alternative draw. [explicit, p.495] This is *full enumeration over a small grid*, **not** McFadden sampling-of-alternatives.
- **Proposal / sampling density:** **none** â€” there is no importance-sampling proposal because alternatives are enumerated; see Â§4b.
- **Prior/proposal correction ($-\log\pi$):** **absent**, by construction (no sampling). [explicit by absence] The opportunity density $g$ enters the likelihood as a *structural weight* on each enumerated alternative, not as a nuisance correction. This is the key contrast with my pipeline (see Â§4b).
- **Normalisation / scale:** $C_0$ is a known subsistence-consumption constant; $\theta$ enters multiplicatively on $v$, so it also soaks up the psychic cost of working (rationalising $\theta<1$). [explicit, pp.489â€“490] $\delta(h)$ / $g_1(h)$ separation is left unidentified for pure tax/wage simulation (kept fixed); see Â§8.
- **Division-bias handling (their numerical method of substance):** a **three-stage procedure** (after Dagsvik & StrÃ¸m 2004, 2006): (1) reduced-form participation probability; (2) wage-rate equations estimated with a selectivity correction using stage-1 results; (3) ML on the labour-supply model with stage-2 predicted wages inserted and the wage-equation errors integrated out. [explicit, p.496] Selection bias in the wage equations is reported negligible. [explicit, p.496]
- **Starting values / multistart:** not described in the provided body. [verify]
- **What pins preferences apart from opportunity:** the exclusion restriction on $I$, a parametric functional form (Boxâ€“Cox), and a normalisation on the offered-hours density (two hours points with equal $g_1$). [explicit, Assumptions 3, 5, 6; Theorem 4, p.493] â€” see Â§8.
- **Verdict â€” reusable for my RURO/JAX pipeline?** **Yes, structurally â€” with one decisive difference.** The likelihood object (utility $\times$ opportunity density, normalised over alternatives) is exactly mine. *Difference:* they **enumerate** a small grid and **integrate** the wage; I **sample** alternatives and therefore must carry the $-\log\pi$ correction that they do not need. Reuse the *factorisation and the role of $g$ as a structural weight*; do **not** import their estimation as evidence that a sampling correction is unnecessary â€” that is an artefact of enumeration. Their three-stage wage procedure is an alternative to my single-stage approach worth citing as a measurement-error precedent, not adopting.

---

## 4b. Proposal / sampling-of-alternatives correction  [extract even if brief]

**The paper has no sampling-of-alternatives step and therefore no McFadden-style proposal correction.** [explicit by construction] Alternatives are the eight fixed hours points; the offered-wage distribution is integrated analytically/numerically. The object that *plays the role* of a per-alternative weight is the **structural opportunity density** $\theta g_1(h)g_2(w\mid h)$ itself â€” but this is a structural primitive, not a nuisance proposal to be divided out. [explicit, pp.489â€“490]

Mapping to my concerns:
- **My $-\log\pi$** is a sampling nuisance correction; **their $g$-terms** ($\log g_1+\log g_2+\log\theta$) are the *structural* analogues of my $\log h_{ij}+\log w_{ij}+\log\text{market}_{ij}$. The clean lesson: when I sample, I must *both* keep the structural $g$-logs *and* subtract $\log\pi$; this paper isolates the structural logs in their pure (un-sampled) form, which is useful for verifying that my structural terms are specified correctly independent of the sampling correction. [analogy]
- **Proposal individualisation.** They consider $g_2(w\mid h;\eta)$ depending on individual covariates and a random effect $\eta$ (i.e. the wage channel is individual-specific), while keeping $g_1(h)$ common across observationally identical agents on the stated ground that hours restrictions are institutionally (union/negotiation) determined and not individual. [explicit, pp.490â€“491] This is a near-exact precedent for my proposal-individualisation split â€” **wage individualised, hours/employment common** â€” and I can cite it for that design choice. [explicit for their structural choice; my proposal-instrument analogy is [analogy]]

---

## 5. Opportunity mechanism  [MOST IMPORTANT â€” split by channel]

**Form.** The available jobs are a realisation of a **Poisson process** of taste shifters $\{\varepsilon(z)\}$ scattered on $(0,\infty)$ with non-homogeneous intensity $\propto \varepsilon^{-2}$ (market intensity scaled by $\theta$, non-market by $1$), with offered $(H(z),W(z))$ drawn independently on $D\times(0,\infty)$ according to $g_1(h)g_2(w\mid h)$. [explicit, Assumption 2, p.489] Dagsvik (1994) showed this $\varepsilon^{-2}$ intensity is the form required for the resulting job choice to satisfy IIA. [explicit, pp.489â€“490] The realised choice probability collapses to the closed form in Theorem 1 (eq. 2a,b): for $h>0$,
$$
\varphi(h,w\mid I)\;=\;\frac{v\big(f(hw,I),h\big)\,\theta\,g_1(h)\,g_2(w\mid h)}{v\big(f(0,I),0\big)\;+\;\theta\sum_{r\in D}\int_0^\infty v\big(f(ry,I),r\big)\,g_1(r)\,g_2(y\mid r)\,dy},
$$
with $\varphi(0,0\mid I)$ the no-work probability (numerator $v(f(0,I),0)$). [explicit, eq.(2a,b), p.490] When wages carry an individual random effect $\eta$, the probability is the same expression with $\theta(\eta)g_2(w\mid h;\eta)$ and an expectation $E_\eta[\cdot]$ taken over $\eta$, which **breaks IIA**. [explicit, eq.(3a,b), p.491]

**Channel map (the core of why this paper matters to me):**

- **ACCESS** = $g_1(h)$ and $\theta$.
  - $g_1(h)$ is the probability that a job with hours $h$ is available; empirically specified **uniform with peaks at part-time (1040 h/yr) and full-time (1950 h/yr)**, motivated as institutional hours regulation. [explicit, pp.489, 495] The paper notes this is *formally equivalent* to van Soest-style PT/FT dummies but with a structural (opportunity) rather than preference interpretation. [explicit, p.495]
  - $\theta$ ("job availability") is the ratio of available market to non-market opportunities; $\log\theta$ is specified **linear in length of schooling**; estimated $\theta<1$ for both genders; $\theta_F$ increases with schooling, $\theta_M$ not significant. [explicit, pp.489, 495, 497]
  - **What they do NOT have in access that I have:** region, urbanisation, year, and occupation offer shifters. Their access channel is hours-availability $+$ a schooling-shifted scalar $\theta$ only. [explicit by absence]
- **ABILITY** = the wage technology $g_2(w\mid h)$ and its random effect.
  - Offered log-wage equation $\log W(z)=\alpha+\psi(H(z))+\eta+\xi(z)$ [eq.(4)], with $\alpha$ a function of schooling, experience, experience$^2$, and a marriage dummy. [explicit, eq.(4) p.491; spec p.496]
  - The random effect $\eta$ (Model 2) is **explicitly interpreted as individual ability** affecting the opportunity measure: "$a+Xb+\eta$ â€¦ represent[s] the effect of observed and unobserved individual ability." [explicit, p.494]
  - $\xi(z)$ (Model 1) is *across-job* wage variation for a given agent. The two models are the two "extreme" stances: Model 1 = wage varies across jobs only ($\eta=0$); Model 2 = each agent faces one wage that varies across agents ($\xi=0$). [explicit, p.496]
  - This is a direct precedent for my ability sub-block (returns to education/experience $+$ residual dispersion $\sigma$). My $\sigma$ corresponds to their wage-equation residual variance (var of $\xi$ in M1, var of $\eta$ in M2). [explicit for theirs; correspondence [analogy]]
- **MARKET/PARTICIPATION** = the market-vs-non-market opportunity split and $\theta$. [explicit, pp.488â€“490]
- **OCCUPATION** = **not modelled** in the estimated opportunity mechanism; only referenced as a possible sector-specific extension. [explicit, p.497 fn.9] **No sector/industry conflation to flag in their estimation** because they estimate no such variable; but note their *informal* "sector" usage means industry-flavoured labour-market sectors, not my ISCO `loc4`.

**Does it vary with circumstances?** Yes, but narrowly: $\theta$ varies with schooling, and $g_2$ varies with schooling/experience and (in M2) with individual ability $\eta$; $g_1(h)$ is deliberately held common across observationally identical agents (institutional hours). [explicit, pp.490â€“491, 495]

**Cost of the omissions for my decomposition.** Because their access channel lacks region/urbanisation/year/occupation, their estimated "opportunity" is thinner than mine; their paper cannot, and does not, decompose welfare by access vs ability. I should cite it for the *existence and identification* of the access (hours, $\theta$) and ability (wage-$\eta$) sub-objects, not for any quantification of an access/ability split.

---

## 6. Welfare object â€” and its place on my $W^1$â€“$W^6$ map

**The paper computes no welfare object.** [not-established] It produces choice probabilities, expected hours ("labour supply curves"), wage elasticities, and a policy simulation of a change in the hours-opportunity distribution. There is **no money-metric welfare, no equivalent income, no compensating/equivalent variation, no inclusive-value welfare core, and no reference price/preference/bundle/set** in the sense my welfare layer requires. [not-established]

- It does **not** place anywhere on my $W^1$â€“$W^6$ family; **do not cite this paper as containing or supporting any $W^k$ measure.** Its closest relative â€” welfare effects of tax reforms â€” appears only in a *cited* reference (Aaberge, Dagsvik & StrÃ¸m 1995), not in this paper. [explicit, references p.502]
- The one welfare-adjacent operation is the **policy simulation** (Â§4.3, Appendix B): changing $g_1$ by removing the part-time peak and raising the full-time peak with $\theta_F$ fixed, then recomputing the realised labour-supply distribution. [explicit, pp.500â€“501, 505â€“506] This is a *behavioural* counterfactual on the opportunity density, not a welfare evaluation. It is, however, a clean precedent for the kind of access-shift counterfactual my decomposition equalises. [analogy]
- **Verdict:** **incompatible as a welfare source**; usable only as the structural-estimation foundation on which a welfare layer (mine) is later built. The welfare construction is entirely my (and the equivalent-income literature's) addition.

---

## 6b. Inclusive value and money-metric inversion  [extract if used]

**Not used.** [not-established] The paper does not use the log-sum / inclusive value as a welfare core and performs no money-metric inversion. The expectation over the extreme-value-type taste shifters is handled *analytically* in deriving the closed-form choice probabilities (Theorem 1), and the unobserved wage effect $\eta$ is integrated out (by simulation/numerical integration over $g_\eta$). [explicit, pp.490â€“491] So there is an analytic-in-taste-shocks derivation I can point to as the antecedent of my analytic-in-shocks log-sum â€” but the paper stops at choice probabilities and expected hours; it never forms a welfare inclusive value or inverts utility to money. My analytic-in-shocks importance-sampling inversion is my own construction, consistent in spirit but not present here.

---

## 7. Inequality / decomposition content  [three-way where relevant]

**None.** [not-established] No inequality index (Gini/MLD/Theil/Atkinson), no decomposition (Shapley/Shorrocks/factor/subgroup/RIF), no counterfactual equalisation of a distribution. The closest object is the *behavioural* hours-distribution simulation (Â§7-adjacent), which equalises nothing in a welfare sense. **It cannot be cited as a precedent for my three-way access/ability/preference Shapleyâ€“Shorrocks split.** To be extended to my decomposition it would need: (i) a welfare object built on top (the inclusive-value money metric); (ii) an inequality index over households; (iii) a Shapley equalisation protocol over the estimated $g$/$v$ blocks. All three are absent.

---

## 8. Identification and the separation of preferences from opportunities  [STRICT â€” the backbone]

This is the paper's central contribution and my primary identification citation. The problem is stated exactly as mine: observed behaviour reflects **both** preferences $v(C,h)$ **and** latent choice constraints (the opportunity measure $\theta g_1 g_2$), so standard multinomial/mixed-logit identification does **not** apply. [explicit, pp.492, 501] The results, in order:

- **Non-parametric ratio is identified, the split is not (Theorem 1 corollary).** $\varphi(h,w\mid I)/\varphi(0,0\mid I)=v(f(hw,I),h)\,\theta g_1(h)g_2(w\mid h)/v(f(0,I),0)$ is observable, but $v$ and $\theta g_1 g_2$ are not separately recoverable from it. [explicit, eq.(7), p.492]
- **Exclusion restriction (Assumption 3).** $v(C,h)$ is smooth and $I$ enters **only through consumption**, not the opportunity measure â€” i.e. non-labour income shifts $C$ while holding hours and wage fixed. [explicit, pp.492â€“493] This is the key economic exclusion; my analogue is that EUROMOD non-labour income enters only $c$, not $g$.
- **Theorem 2 (non-identification under exclusion alone).** Even with Assumption 3, the model is **non-parametrically unidentified**: $v(C,h)=\zeta(C)^{r}\lambda^{*}(C,h)\,\delta(h)$ with $\zeta,\lambda^{*}$ identified but $r$ an unknown constant and $\delta(h)$ an unknown function of hours. [explicit, p.493]
- **Theorem 3 (Assumption 4: offered wages âŸ‚ offered hours).** The offered-hours distribution is identified and $v(C,h)=\lambda(C,h)\delta(h)$ with $\lambda$ identified, **$\delta(h)$ still not**. For pure tax/wage counterfactuals one need not separate $\delta(h)$ from $g_1(h)$ as long as $g_1$ is held fixed. [explicit, pp.493] â€” *Important caveat for me: this "don't need to separate" licence applies to behavioural tax simulation, NOT to a welfare decomposition that attributes inequality to access vs preference; my object requires the separation their tax-simulation can dodge.*
- **Theorem 4 (full identification via functional form).** Under Assumptions 1â€“3, 5, 6 â€” a generalized **Boxâ€“Cox** $\log v$ (eq.8) plus a normalisation that two distinct hours points share the same offered-hours probability, $g_1(h_1)=g_1(h_2)$ â€” model (2a,b) is **identified**. [explicit, p.493] **This is parametric identification: the separation is bought with functional form + a normalisation, not with an instrument or panel.**
- **Theorem 5 (identification with a wage random effect / ability).** With unobserved wage heterogeneity (model 3a,b), identification needs an **exogenous covariate $X$ that affects the opportunity density / offered wage but not preferences** (Assumption 7: $\log W(z)=Xb+a+\eta+\xi(z)$, with $\theta$ constant or $\theta(a+Xb+\eta)$). Then $v$ is identified up to a multiplicative $h$-term, $\theta(\cdot)$ up to a constant, and the conditional offered-wage distribution is identified; adding Boxâ€“Cox (Assumption 6) gives full identification. [explicit, pp.494]

**Transport to my France pooled cross-section (honest assessment).**
- Their cross-section + Boxâ€“Cox + exclusion-of-$I$ + hours-normalisation route (**Theorem 4**) transports directly to me: I too rely on parametric Boxâ€“Cox and on non-labour income entering only consumption. My certification by **synthetic recovery** is the right standard precisely because identification here is *parametric*, not design-based â€” recovery on simulated data is the test of whether the functional-form identification actually bites at my sample size. [analogy; consistent with project state Â§3.6/Â§8]
- Their random-wage-effect route (**Theorem 5**) requires an **exogenous wage/opportunity shifter $X$ excluded from preferences**. My ability sub-block uses education and experience as the wage technology; for the Theorem-5 logic to support separating my ability channel, those must be credibly excluded from $v$ â€” which is exactly my design (education/experience are in $g$, not $v$). But I have **no external instrument** beyond functional form, and the paper is explicit that **panel or repeated cross-sections do not in general rescue identification** (only changes in the opportunity measure, not its level, become non-parametrically identifiable under fixed preferences). [explicit, p.492] So I cannot lean on my pooling of 2015â€“2017 as an identification gain; it is a precision/clustering matter, not an identification one.
- **Referee defence ("your decomposition is mechanical").** Cite Theorems 2â€“5 to establish that (a) the separation is a *known hard problem*, (b) it is *achievable* under stated parametric assumptions I satisfy, and (c) the honest standard is recovery under those assumptions â€” which is why I certify by synthetic recovery rather than in-sample fit. **Do not soften:** the identification is parametric and rests on the exclusion of $I$ from $g$, the exclusion of the wage shifter from $v$, the Boxâ€“Cox form, and an offered-hours normalisation.

---

## 9. Key results and magnitudes

All from the Norway 1997 married-couples sample; "M2" = their maintained Model 2 (individual wage heterogeneity).

- **Model selection.** Log-likelihood values $\approx 5309$ (M1) and $5243$ (M2) [sign reported as printed; magnitude is the likelihood-function value â€” [verify] sign]. McFadden $\rho^2 = 0.49$ (M1), $0.50$ (M2). [explicit, p.497]
- **Andrews $\chi^2$ goodness-of-fit (5 d.f., 6 cells):** M1 $=57.6$ (fails), M2 $=10.4$ (passes; 5% critical $=11.07$). M2 selected as maintained model. [explicit, pp.497â€“498]
- **Wage elasticities (aggregated, M2; Table II, p.499):**
  - Own-wage elasticity of the **probability of working, married women** $=0.333$ (text rounds to $0.33$); a 5% female wage rise raises the female participation share by $\approx 1.5\%$. [explicit, pp.499, 502/p.14 text]
  - Probability of working, **married men**: very small, $\approx 0.007$ (own), $0.010$ (men's wage). [explicit, Table II]
  - **Unconditional hours elasticity, women** $=0.618$ (M2, own-wage); **men** $\approx 0.022$ (own) to $0.080$ (men's wage). [explicit, Table II]
  - Cross-wage elasticity for women is **negative** and smaller than own-wage. Both-spouses-wage elasticity of female participation $=0.205$ (M2). [explicit, Table II; p.499]
- **Opportunity findings.** $\theta<1$ for both genders (interpreted as fewer interesting available jobs than non-market opportunities, and/or psychic cost of work). $\theta_F$ rises with schooling; $\theta_M$ insignificant. Number of children significantly raises women's marginal utility of leisure, not men's. [explicit, p.497]
- **Policy simulation.** Removing the female part-time peak and raising the full-time peak (with $\theta_F$ fixed) shifts women from PT to FT by roughly equal magnitudes; men's labour supply barely changes. [explicit, pp.500â€“501]
- **Benchmark value for me:** female participation own-wage elasticity $\approx 0.33$ and unconditional hours elasticity $\approx 0.6$, with near-zero male responses, are the order-of-magnitude sanity checks for my France estimates; large divergence would flag a specification problem. [analogy]

---

## 10. Estimators, theorems, or formal results

For each, statement (paraphrased; LaTeX for the math), assumptions, technique, reusability verdict.

- **Theorem 1 (closed-form choice probability).** Under Assumptions 1â€“2, the joint density of $(h,w)$ is the ratio in Â§5 (eq. 2a,b). Assumptions: separable random utility $U=v(C,h)\varepsilon(z)$; Poisson-scattered taste shifters with $\varepsilon^{-2}$ intensity; offered $(H,W)\sim g_1g_2$ independent of shifters. Technique: max-stable / extreme-value process algebra (Dagsvik 1994); the $\varepsilon^{-2}$ form yields IIA. **Reusable:** yes â€” this *is* my per-alternative structural weight, modulo my sampling correction. [explicit, p.490]
- **Theorem 2 (non-identification under exclusion).** $v(C,h)=\zeta(C)^{r}\lambda^{*}(C,h)\delta(h)$; $r,\delta(h)$ unidentified. Assumptions 1â€“3. Technique: log-differentiate the observable ratio in $I$, integrate over $C$ (Appendix A). **Reusable:** as the *negative* result I cite to justify parametric identification. [explicit, p.493]
- **Theorem 3 (partial identification under wageâŸ‚hours).** Offered-hours distribution identified; $v=\lambda\delta$, $\delta(h)$ unidentified. Assumptions 1â€“4. **Reusable:** yes, to delimit what is/ isn't free without functional form. [explicit, p.493]
- **Theorem 4 (parametric full identification).** Boxâ€“Cox $\log v$ (eq.8) $+$ $g_1(h_1)=g_1(h_2)$ $\Rightarrow$ model (2a,b) identified. Assumptions 1â€“3, 5, 6. **Reusable:** **yes â€” this is my identification citation.** [explicit, p.493]
- **Theorem 5 (identification with wage random effect).** With Assumption 7 (exogenous wage shifter $X$ excluded from preferences) $+$ moment bound (Assumption 8): $v$ identified up to an $h$-term, $\theta(\cdot)$ up to a constant, conditional offered-wage distribution identified; with Boxâ€“Cox, full identification. **Reusable:** yes for justifying the separability of my ability channel, conditional on excluding the wage shifter from $v$. [explicit, p.494]
- **Boxâ€“Cox utility (eq. 8).** $\log v(C,h)=\gamma_1\frac{C^{\alpha}-1}{\alpha}+\gamma_2\frac{(1-h/M)^{\beta}-1}{\beta}+\gamma_3\frac{(C^{\alpha}-1)}{\alpha}\frac{((1-h/M)^{\beta}-1)}{\beta}$ [explicit form, p.493; exact constant arrangement [verify] against the printed OCR]. Globally concave; justified by invariance principles (Dagsvik & StrÃ¸m 2006; Dagsvik & RÃ¸ine Hoff 2011). **Reusable:** yes â€” same family as my preference block.

---

## 11. Robustness and specification sensitivity

- **Wage-heterogeneity stance (their main robustness axis).** They estimate the two "extreme" cases â€” across-job wage variation (M1) vs individual wage heterogeneity / ability (M2) â€” and select M2 on fit. [explicit, pp.496â€“498] *Lesson for me:* the ability-vs-job-residual decomposition of wage variance is a real specification fork; my $\sigma$ inherits this ambiguity, and the M1/M2 contrast is the precedent for treating it as a robustness choice rather than a settled object. The authors decline to separate inter- vs intra-individual wage effects ($\xi+\eta$), judging it to hinge too much on functional form â€” directly relevant to how hard I can push the ability/access boundary. [explicit, p.496 fn.8]
- **Hours grid / cell aggregation.** Thin joint-hours cells force them to aggregate to six cells for goodness-of-fit; the eight-point grid is fixed. [explicit, p.497] *Lesson:* my 901/101 grids are far finer; their thin-cell problem is a caution about over-disaggregating couples.
- **Measurement error / division bias.** The negative observed wageâ€“hours correlation ($-0.22$ women, $-0.17$ men) is a measurement artefact handled by the three-stage procedure. [explicit, pp.495â€“496] *Lesson:* a stress test I should run if I ever construct wages by division; with EUROMOD income I sidestep it but should note it.
- **What they do NOT stress-test:** number of draws (no simulation draws â€” analytic), number of starts, alternative opportunity-set definitions, reference states (no welfare). [not-established] So this paper gives me *no* guidance on effective-sample-size or draw-growth stability â€” those concerns are specific to my importance-sampling layer and unaddressed here.

---

## 12. What I can cite this paper for

- The **RURO/latent-jobs factorisation** of labour supply into preference utility $\times$ opportunity measure, and the closed-form choice probability (Theorem 1). [explicit]
- The **formal identification problem** of separating preferences from the opportunity mechanism on cross-section data, and its resolution under exclusion + Boxâ€“Cox + an offered-hours normalisation (Theorems 2â€“5). This is my primary identification citation. [explicit]
- The terms **"opportunity measure"** ($\theta g_1 g_2$) and **"opportunity density"** ($g_1 g_2$), and $\theta$ as a **job-availability** scalar. [explicit, p.489]
- The design choice that the **wage channel is individualised while the hours channel is institutional/common** across observationally identical agents. [explicit, pp.490â€“491]
- The interpretation of a **wage random effect as individual ability** entering the opportunity measure (support for my ability channel). [explicit, p.494]
- That **non-labour income enters only consumption, not the opportunity measure** (the exclusion restriction). [explicit, pp.492â€“493]
- A **joint couples** latent-jobs labour-supply application as precedent. [explicit]
- Benchmark **female participation/hours elasticities** ($\approx 0.33$ / $\approx 0.6$) with negligible male responses. [explicit, Table II]
- That conventional discrete-choice (van Soest) **PT/FT preference dummies are formally equivalent to peaks in the opportunity density**, with the latter carrying a structural rationale. [explicit, p.495]

---

## 13. What I should NOT cite this paper for  [overclaim risks]

- **No welfare object.** Do not attribute any money-metric welfare, equivalent income, EV/CV, or inclusive-value welfare core to this paper. [not-established]
- **No $W^1$â€“$W^6$.** The compensationâ€“responsibility family is *not* here; it comes from the companion theory and the equivalent-income literature. [not-established]
- **No decomposition.** Do not cite for any inequality index or Shapley/Shorrocks split â€” and especially not for a three-way access/ability/preference decomposition. Its only "decomposition" of opportunity is conceptual, not an inequality decomposition. [not-established]
- **Two-way framing, not three-way.** Where the paper distinguishes sources it is *preferences vs opportunity (constraints)* â€” a **two-way** cut. My three-way access/ability/preference vocabulary is *my* refinement; when citing, say the paper separates preferences from the opportunity mechanism, and note that the access/ability sub-split is my extension. [explicit that it is two-way]
- **Occupation/sector.** Do not cite as support for an estimated occupation-as-access layer; the estimated model has no occupation and no sector. Their informal "sector" (health care, public sector) is industry-flavoured, not my ISCO `loc4`; do not let it license `loc4`/`lindi` slippage. [explicit by absence]
- **Random vs deterministic opportunities.** The paper treats opportunity sets as genuinely **stochastic** (Poisson-scattered, the "RO" is substantive). My design treats opportunities as **deterministic feasible sets** with "RO" as estimation machinery only. Do not import their random-opportunities interpretation as if it were mine. [explicit, Assumption 2]
- **Sampling correction.** Do not cite their enumeration-based estimation as evidence that a $-\log\pi$ proposal correction is dispensable; that is specific to fixed-grid enumeration. [explicit by construction]
- **Theory-paper boundary.** This is a Dagsvikâ€“Jia empirical/identification paper; it is unrelated to the Haydarâ€“Maniquet axiomatic theory paper. Never route any axiom, characterisation, or proof of the $W$-family through this citation, and never read this paper as a theory contribution to my JMP. [boundary]

---

## 14. Direct quotes worth citing

Short verbatim phrases for my own annotation (each kept brief; page numbers as printed):

- p.489 â€” "The parameter Î¸ is clearly a measure of job availability".
- p.489 â€” "the opportunity measure" / "the opportunity density" (their naming of $\theta g_1 g_2$ and $g_1 g_2$).
- p.492 â€” identification "arises from the fact that observed labor supply behavior is a result of both preferences â€¦ and latent job choice constraints".
- p.492 â€” on panel/cross-section data: "hard to see how this would help to solve the identification problem".
- p.494 â€” the wage intercept term is meant to "represent the effect of observed and unobserved individual ability".

(If a longer block is needed for a direct quotation in the draft, pull it from the PDF at the cited page rather than expanding these.)

---

## 15. Open questions and risks for my draft

- **Parametric identification is the whole game.** The paper makes unmistakable that the preference/opportunity separation is *not* design-identified on a cross-section; it is bought with Boxâ€“Cox + exclusions + a normalisation. My access/ability/preference decomposition inherits this â€” I must state plainly that the decomposition's credibility rests on those parametric assumptions and on synthetic recovery, not on an instrument I do not have. Risk: a referee reads the decomposition as data-identified; pre-empt it.
- **Ability vs across-job residual ($\eta$ vs $\xi$).** The authors refuse to separate inter- from intra-individual wage variation as "not theoretically sound" given the information. My ability channel ($\sigma$, returns to education/experience) sits on exactly this fault line; pushing the ability/access boundary too hard repeats the move they declined. Treat the ability/access re-allocation as a *named robustness* (project state Â§6.3), not a headline.
- **Hours channel as institutional/common.** Their justification for common $g_1(h)$ (union/negotiation-set hours) supports my "hours/employment common in the proposal" choice â€” but it also implies access heterogeneity I *do* model (region, occupation, year) is a stronger claim than theirs; I should be ready to defend that those access shifters are identified, given the paper warns even $g_1$'s level is delicate.
- **No guidance on integration error.** The paper is analytic/enumeration-based and says nothing about importance-sampling effective sample size or draw-growth stability â€” the live blockers in my singles welfare integral. This paper cannot reassure on that; it is orthogonal.
- **"Sector" temptation.** The paper's sector talk is a standing temptation to conflate occupation and industry. Discipline: cite only for the *idea* that occupation/sector belongs in $g$ if added, never as an estimated precedent, and keep `loc4` â‰  `lindi`.

---

## 16. TL;DR for retrieval

Dagsvik & Jia (2016, *JAE*) is the canonical identification paper for the latent-jobs/RURO factorisation â€” preference utility $v(C,h)$ times an opportunity measure $\theta g_1(h)g_2(w\mid h)$ â€” proving that on cross-section data preferences and opportunities are non-parametrically unseparable (Thms 2â€“3) but identified under a Boxâ€“Cox utility plus an offered-hours normalisation and the exclusion of non-labour income from the opportunity measure (Thms 4â€“5), with a wage random effect interpreted as individual **ability** entering $g$ (my ability channel) and $g_1(h)/\theta$ supplying my **access** channel. It is my primary **identification** and **opportunity-mechanism** citation and a benchmark for elasticities (female participation $\approx 0.33$), but it computes **no welfare, no inclusive-value money metric, and no decomposition**, contains nothing of the $W^1$â€“$W^6$ family, uses a **two-way** preference/opportunity cut and **genuinely stochastic** opportunity sets, and must never be read through the Haydarâ€“Maniquet theory boundary.
# Dagsvik & KarlstrÃ¶m 2005 â€” Compensating Variation and Hicksian Choice Probabilities in Random Utility Models that are Nonlinear in Income

## 0. Metadata
- **BibTeX key:** DagsvikKarlstrom2005 [verify exact key against project .bib]
- **Authors:** John K. Dagsvik (Statistics Norway and the Frisch Centre, Oslo); Anders KarlstrÃ¶m (Royal Institute of Technology, Stockholm).
- **Year:** 2005 (first version received August 2001; final version accepted February 2004).
- **Outlet:** *The Review of Economic Studies*, Vol. 72, No. 1 (Jan. 2005), pp. 57â€“76.
- **DOI/URL:** JSTOR stable URL https://www.jstor.org/stable/3700684 [no DOI printed on the supplied PDF â€” verify].
- **PDF filename:** `Dagsvik_KarlstrÃ¶m_2005_Compensating_Variation_and_Hicksian_Choice_Probabilities_in_Random_Utility.pdf`
- **Tier:** T1A.
- **JMP block(s) served:** welfare (primary); estimation / numerical-implementation of the welfare integrator (secondary, via the analytic-in-shocks expenditure-function machinery); normative-interpretation (only weakly â€” it supplies the *technique* for CV/EV in nonlinear-in-income RUMs, not a responsibility taxonomy). **Not** an opportunity-mechanism, identification, decomposition, or data-infrastructure source.

---

## 1. One-paragraph relevance to my JMP
This is the methodological backbone for converting a discrete-choice random-utility model that is **nonlinear in income** into a money-metric welfare figure â€” exactly my situation, since my Boxâ€“Cox utility $v_i(c,\ell)$ is nonlinear in consumption and the standard log-sum/linear-in-income CV shortcut therefore does **not** apply (explicit-in-source, p. 58: "when the utility function is nonlinear in income, no analogue to the log-sum approach exists"). The paper defines a random *expenditure function* $Y_B(\mathbf{w},u)=\min_{k\in B} Y_k(w_k,u-\varepsilon_k)$ and shows that money-metric welfare reduces to a **one-dimensional** problem in income for each alternative, then aggregated â€” which is precisely the structure of my money-metric inversion of attained utility $V_i$ to an equivalent income $\Omega_i$. It speaks to **all** my welfare measures uniformly (the inversion technique is measure-agnostic), but it is silent on the access/ability/preference channel cut: it has no opportunity mechanism, no inequality object, and no decomposition. Its contribution to my paper is *apparatus*, not *content*: the expenditure-function/Hicksian-choice-probability toolkit, the GEV closed forms (Corollary 5 / Examples), and the explicit warning that the linear-in-income log-sum welfare formula is invalid in my setting.

---

## 2. Data and setting
**N/A â€” this is a pure theory/methods paper.** There is no dataset, no country, no sample unit, and no estimation sample. The "setting" (their Â§2, p. 59) is an abstract consumer facing a feasible set $B\subseteq S=\{1,\dots,M\}$ of alternatives, each with attributes $w_j$ (including a price/user-cost component) and income $y$.

- **Transports to my France pooled 2015â€“2017 EUROMOD cross-section?** The *machinery* transports fully (it is data-free and holds for any GEV/MNL discrete-choice model nonlinear in income). The *application* does not transport, because there is nothing to transport â€” the paper provides formulae, not estimates.
- **Features I do NOT have that the paper presumes / exploits:** the paper is built around a **two-period price/attribute change** $(\mathbf{w}^0,y^0)\to(\mathbf{w},y^1)$ with the error terms $\{\varepsilon_j\}$ held fixed across the two regimes (explicit, p. 58). My JMP is a **single-cross-section level** welfare exercise, not a before/after reform-CV exercise; I have no policy counterfactual and (under the v5 design) no second regime. So the paper's headline objects (the *distribution* of CV across a policy change, compensated transition probabilities $i\to j$) are richer than what my baseline needs â€” I use the static expenditure-function/inversion core, not the two-period CV-distribution apparatus. This is a derived-by-analogy mapping, not explicit-in-source.

---

## 3. Model and objects (map object-by-object to mine)
Utility of alternative $j$: $U_j = v_j(w_j,y)+\varepsilon_j$ (eq. (1), p. 59), with $v_j(\cdot)$ continuous, decreasing in price, strictly increasing in income, possibly $j$-dependent; $\{\varepsilon_j\}$ have a joint CDF $F^B$ with continuous density (explicit-in-source).

- **Their choice set $B$ = my latent-jobs set $\mathcal{C}_i$?** **Derived-by-analogy.** Both are finite alternative sets entering a max-utility discrete choice. But their $B$ is a *given* feasible subset of a universal $S$; they treat $B$ as exogenous and do **not** model how $B$ is formed. My latent-jobs set is generated by an estimated opportunity density $g$. So the *object* maps, but the *mechanism that produces it* is absent here.
- **Their deterministic utility $v_j(w_j,y)$ = my preference utility $v$?** **Partially, explicit-in-source.** Their $v_j$ is the systematic utility nonlinear in income; my $v_i(c,\ell)$ is the analogous block. Caveat: their $v_j$ can absorb non-pecuniary attributes $a_j$ and a $j$-index, which in some of their examples plays a role analogous to an alternative-specific value. In my architecture those alternative-specific terms would live in the **opportunity density $g$**, not in $v$. So I must **not** import their "$v_j$ carries everything alternative-specific" convention â€” that would conflate my preference block with my access/ability blocks.
- **Explicit opportunity/availability mechanism analogous to my $g$?** **No â€” not-established / absent.** There is no density over alternatives representing feasibility, no offer probabilities, no participation restriction. $B$ is exogenously given. Consequently there is **no** separation of hours / wage(ability) / market / occupation channels. This is the central limitation for my purposes: the paper is about welfare *given* the choice set, not about the choice set's heterogeneity.
- **Their budget map = my EUROMOD disposable income?** **Derived-by-analogy only.** They use an abstract price/user-cost $w_{1j}$ entering $v_j(w_j,y)=\psi_j(y-w_{1j},w_{2j})$ (footnote 3, p. 58; Corollary 1, p. 63). My disposable-income map is the EUROMOD tax-benefit function $c_{ij}$. The paper's "price" abstraction subsumes my $c_{ij}$ as a special case but is not derived for a tax-benefit budget specifically.
- **Does any attribute enter BOTH utility and an opportunity mechanism?** **N/A â€” there is no opportunity mechanism**, so the double-entry flag cannot fire. (No identification justification is offered because the question does not arise in their framework.)

---

## 4. Estimation method
**Largely N/A â€” the paper is not an estimation paper.** It derives welfare formulae taking the random-utility model as already specified/estimated. There is no likelihood, no estimator, no choice-set-construction-by-sampling, no proposal density, and no prior/proposal correction in the paper.

- **Likelihood/estimator:** none.
- **Choice-set construction (fixed grid vs sampled alternatives; grid size):** they assume a **fixed, finite** feasible set $B=\{1,\dots,m\}$; no sampling of alternatives (explicit-in-source, Â§2).
- **Proposal/sampling density; prior/proposal correction; is $\log(\text{prior})$ subtracted from the choice index?** **Not present.** Because the set is fixed and exogenous, there is no McFadden-style sampling-of-alternatives correction anywhere in the paper. This is an important *negative* finding: the paper does **not** speak to my mandatory $-\log\pi(j)$ correction, and I must not cite it for that. (See Â§4b and Â§13.)
- **Normalisation/scale:** in the i.i. extreme-value specialisation (Â§7, p. 70) the standard MNL scale applies; the type-III EV with scale $\tau$ is noted in the Remark on p. 60 ($\tau U_j = v_j+\varepsilon_j$, $P(\varepsilon_j\le x)=\exp(-e^{-x})$).
- **Numerical method / starting values / multistart:** none â€” the contribution is *analytic* formulae plus, where closed forms are unavailable, a single one-dimensional (or low-dimensional) integral.
- **What pins down preferences vs the opportunity mechanism:** N/A â€” no opportunity mechanism, no estimation, so nothing is "pinned down" in the estimation sense.

**Verdict (reusable for my RURO/JAX pipeline?):** **Yes, for the welfare layer only â€” not for estimation.** The reusable step is the **expenditure-function inversion** $u=V_B(\mathbf{w},Y_B(\mathbf{w},u))$ (eq. (7), p. 60) computed alternative-by-alternative as a one-dimensional solve $Y_k(w_k,u-\varepsilon_k)$ (eq. (9), p. 61), and the analytic-in-shocks expectation in the GEV/MNL case (Corollary 5, eq. (20), p. 70). These map directly onto my "ex-ante attained utility $V_i$, then invert to money" core (welfare spec v5 Â§1.1). The estimation, sampling, and proposal-correction parts of my pipeline get **nothing** from this paper.

---

## 4b. Proposal / sampling-of-alternatives correction  [extract even if brief]
**Not-established / absent in the source.** The paper does not sample alternatives and does not carry any per-alternative log-prior. There is no covariate-dependent proposal mean, no occupation-conditioned draw, and no common-vs-individualised proposal distinction â€” because the feasible set is taken as a fixed exogenous primitive. 

Relation to my importance-sampling welfare integrator: the paper is **complementary but silent**. It establishes that, in the GEV/MNL case, the welfare expectation over the extreme-value shocks is **closed-form / analytic** (Corollary 5, p. 70), which is exactly the property my v5 integrator relies on ("analytic in the extreme-value shocks; no FrÃ©chet draws and no simulated argmax"). But the *separate* question of correcting for how the *alternatives themselves* are sampled (my $-\log\pi(j;x_i)$, partly individualised in wage and occupation, common in hours and employment) is **outside this paper's scope**. Do not attribute any proposal-correction result to Dagsvikâ€“KarlstrÃ¶m; cite McFadden's sampling-of-alternatives literature for that instead.

---

## 5. Opportunity mechanism  [MOST IMPORTANT â€” be exhaustive; split by channel]
**N/A â€” there is no explicit opportunity mechanism in this paper.** The feasible set $B$ is an exogenous, fixed, finite subset of the universal set $S$ (explicit-in-source, Â§2, p. 59). Availability of jobs, hours, wages, and occupations is **not** modelled as a density, as offer probabilities, or as a reservation-wage/participation restriction. The set does **not** vary with observable circumstances (region, education, demographic type, local labour market) â€” there are no covariates in the model at all beyond the alternative attributes $w_j$ and income $y$.

Mapping to my three sub-objects:
- **access** (hours / market-participation / region / year / occupation offers): **absent.**
- **ability** (wage technology â€” returns to education/experience, residual productivity): **absent.**
- **occupation as availability vs something else:** **absent**, hence no sector/industry conflation risk to flag (the paper never discusses occupation or industry).

One adjacency worth recording, but as **derived-by-analogy, not as an opportunity mechanism.** The paper shows how to handle a **changing choice set** across the two periods: removing an alternative is implemented by sending its price to infinity so $v_j\to-\infty$ (Remark, p. 67; Examples 2â€“3, pp. 71â€“72), and adding an alternative is the symmetric case (Example 2, eq. (24)â€“(26)). This is a *technical device for set changes under a policy*, not a model of *heterogeneous feasible sets across agents*. It could in principle be borrowed to represent "this job type is not in household $i$'s set" â€” but that is my $g$'s job, and the paper offers no estimation or probabilistic content for it.

**Cost of the omission for my decomposition:** because the paper has no opportunity mechanism, it cannot, on its own, support any access/ability/preference attribution. It supplies the welfare *evaluator* that sits *downstream* of my $g$; it does not supply $g$ and must not be cited as if it does.

---

## 6. Welfare object â€” and its place on my $W^1$â€“$W^6$ map
**Does the paper compute welfare? Yes â€” it derives the apparatus for compensating variation (CV) and equivalent variation (EV) in discrete choice.**

- **Money-metric? Equivalent income? CV/EV? Expected (log-sum) utility?** The welfare object is **compensating variation**, defined implicitly by $\max_j(v_j(w_j^0,y^0)+\varepsilon_j)=\max_j(v_j(w_j,y^1-\mathrm{cv})+\varepsilon_j)$ (p. 58), with $\mathrm{cv}=y^1-Y_B(\mathbf{w},V_B(\mathbf{w}^0,y^0))$ (p. 65). They emphasise (p. 73) that the EV derivation is "completely analogous." It is money-metric in the CV/EV sense. It is **not** an equivalent-income-with-reference-preference object of the King/Fleurbaeyâ€“Maniquet type; there is no reference preference and no responsibility taxonomy.
- **Universal vs constrained feasible set?** Defined over the agent's feasible set $B$ (which may differ across the two periods via the set-change device). It is a constrained-set object in the weak sense that $B$ can be any subset, but there is no normative reading of the set as "opportunity."
- **Reference price/preference/bundle/set:** the reference is the **initial utility level** $V_B(\mathbf{w}^0,y^0)$; welfare is measured relative to the agent's *own* utility at the initial attributes/income, holding the realised $\{\varepsilon_j\}$ fixed across regimes (explicit, p. 58). The reference is a *utility level under own preferences*, not an external reference preference.
- **Discrete-choice subtleties handled:** this is the paper's core strength. It handles (i) **log-sum aggregation** where utility is linear in income (acknowledged as the standard case, p. 58) and supplies the **replacement** when it is nonlinear; (ii) **selection / switching** â€” the chosen alternative can differ before vs after the change, which is precisely the analytic difficulty the random expenditure function resolves (p. 58, p. 64); (iii) **Hicksian vs Marshallian** â€” it defines *Hicksian (compensated) choice probabilities* $P^h_B(j,\mathbf{w},u)=P(J_B(\mathbf{w},Y_B(\mathbf{w},u))=j)$ (Definition 1, p. 62) and proves a discrete-choice **Shephard's-Lemma** analogue (Corollary 1, p. 63); (iv) **integration over unobserved heterogeneity** â€” only a one-dimensional integral is needed given $F^B$ (Theorem 2, p. 62); random coefficients handled in Â§5 (p. 68); (v) **ex-ante vs ex-post** â€” the framework is **ex-ante** in the sense that it integrates over $\{\varepsilon_j\}$ to produce *distributions* and *expectations* of CV (e.g. the mean-CV formula (20), p. 70), while also delivering the joint distribution with the realised initial/current choice.

**Locate on my $W^1$â€“$W^6$ map:** **Not on the map.** The paper's CV/EV is a **policy-change** welfare measure on a single preference with the *initial own-utility level* as reference. My $W^1$â€“$W^6$ are *level* equivalent-income measures distinguished by Independence-of-$\mathbf{y}$ / Independence-of-$A$ stances on responsibility. The paper has neither Ind-$\mathbf{y}$ nor Ind-$A$ content and does **not** correspond to any single $W^k$. The honest mapping is: Dagsvikâ€“KarlstrÃ¶m supply the **computational engine** (expenditure-function inversion, analytic-in-shocks expectation) that any of my $W^k$ inversions can be built on; they do **not** supply, and must not be cited for, the family or its normative readings (those are the companion Haydarâ€“Maniquet theory paper's content, imported as cited primitives).

**Verdict:** **Adaptable (engine), incompatible (object).** Directly usable as the nonlinear-in-income inversion/expectation machinery; incompatible as a normative welfare object or as my $W^k$ family.

---

## 6b. Inclusive value and money-metric inversion  [extract if the paper uses a log-sum or an EV/CV]
- **Does it use the inclusive value (log-sum)?** **Yes, but conditionally and as a contrast.** The paper states the log-sum is the right welfare core **only when utility is linear in income** (p. 58, p. 64: Roy's-identity duality "only when utility is linear in income"). Its whole point is the case where the log-sum **fails**. In the i.i.d. EV / MNL specialisation it nonetheless recovers closed-form expressions: Example 4 (p. 72) gives the linear-in-income case mean expenditure $EY_B(\mathbf{w},V_B(\mathbf{w}^0,y^0))=y^0+\frac1\gamma\log(\sum_k e^{-\gamma w_k^0+a_k^0})-\frac1\gamma\log(\sum_k e^{-\gamma w_k+a_k})$ (eq. (29)), i.e. a log-sum difference â€” confirming the standard formula as the linear special case.
- **Is welfare obtained by inverting an own-utility map to a money figure (1-D solve)?** **Yes â€” explicit-in-source and central.** $Y_k(w_k,u-\varepsilon_k)$ is defined by $v_k(w_k,Y_k(w_k,u-\varepsilon_k))+\varepsilon_k=u$ (eq. (9), p. 61); since $v_k$ is strictly increasing in income this is a **unique one-dimensional solve**, and $Y_B=\min_{k\in B} Y_k$ (eq. (10)). This is *exactly* my "invert attained utility to an equivalent income" step, done per-alternative then aggregated by the min. This is the single most directly reusable result in the paper.
- **Is the expectation over the extreme-value shocks taken analytically (no draws) or by simulation?** **Analytically, in the GEV/MNL case** â€” Corollary 5 (p. 70) and Example 1 (p. 70â€“71) give closed forms; eq. (20) gives mean expenditure as a one-dimensional integral with **no shock simulation**. The paper explicitly argues (citing McFadden 2001, Conclusion p. 73) that this analytic method "is to be preferred to using simulations." This **directly corroborates** my v5 decision to integrate $\varepsilon$ analytically (the log-sum is the closed-form expectation over $\varepsilon$) and to avoid FrÃ©chet draws / simulated argmax in the welfare layer.

Relation to my analytic-in-shocks, importance-sampling inversion: **strong, explicit-in-source for the analytic-in-$\varepsilon$ half; silent for the importance-sampling-over-alternatives half.** Dagsvikâ€“KarlstrÃ¶m justify the analytic expectation over shocks; they do **not** address sampling/weighting over a large alternative set (my IS over draws with weight $\hat g/\pi$), because their set is small and fixed.

---

## 7. Inequality / decomposition content  [three-way where relevant]
**N/A â€” there is no inequality index and no decomposition in this paper.** It computes individual-level (and population-mean, via Hammond 1990's weighted-population-mean welfare, mentioned p. 59) CV/EV objects, not a Gini/MLD/Theil/Atkinson index, and performs no factor/Shapley/Shorrocks/subgroup/RIF decomposition.

- **Counterfactual construction:** the only counterfactual is the **two-period attribute/price change** with $\{\varepsilon_j\}$ held fixed (p. 58). Nothing is "equalised," "neutralised," or "zeroed out" in the inequality-of-opportunity sense. The set-change device (price $\to\infty$) zeroes out an *alternative*, not a *circumstance*.
- **Order/path-independence/exhaustiveness:** N/A (no decomposition).

**Verdict (reusable for my three-way access/ability/preference Shapleyâ€“Shorrocks split anchored on $W^3$/$W^5$/$W^1$?):** **No.** The paper contributes **upstream** of the decomposition â€” it produces the money-metric welfare *values* that a Shapley decomposition would then operate on â€” but it supplies **zero** decomposition content. It is neither two-way nor three-way; it is non-decompositional. To reach my three-way split, everything in the decomposition layer must come from elsewhere (Shorrocks 2013; the IOp/Shapley literature); this paper is cited only for how the welfare numbers feeding the decomposition are computed.

---

## 8. Identification and the separation of preferences from opportunities  [STRICT]
**N/A for identification â€” the paper is not an identification paper.** It assumes the random-utility model (the systematic $v_j$ and the error CDF $F^B$) is **already known/specified**; it does not ask what identifies tastes vs constraints, and it has no opportunity side to separate from preferences. There is no exclusion restriction, no choice-set variation used for identification, no panel, no external opportunity shifter, and no synthetic-recovery argument.

The one assumption that bears on identification *of welfare effects* (not of the model) is the **fixed-$\varepsilon$ assumption**: the random terms are unchanged across the two regimes (p. 58). The paper is candid that this is "reasonable if the error terms characterize tastes" but "less reasonable if $\{\varepsilon_k\}$ also include unmeasured attributes of alternatives, which may be altered by policy" (p. 58) â€” citing Heckmanâ€“HonorÃ© (1990), McFadden (1999b), Carneiroâ€“Hansenâ€“Heckman (2001). 

**Transport to my France pooled cross-section (no panel, no external instrument):** the welfare *machinery* transports (it needs only $\hat\theta$ and the set, both of which I have). The fixed-$\varepsilon$ assumption is **not a binding concern for my baseline** because my v5 welfare object is a **single-cross-section level** computation, not a two-period reform-CV â€” there is no "after" regime in which $\varepsilon$ could change. If I ever add an EV/CV reform exercise (welfare spec v5 Â§1.1 lists EV/CV as secondary D3 objects for AC/JJT comparability), then the fixed-$\varepsilon$ caveat becomes live and I should cite this paper's discussion of it. This does **not** defend me against the "your decomposition is mechanical" referee â€” that defence rests on $g$'s identification and synthetic recovery, on which this paper is silent.

---

## 9. Key results and magnitudes
**No empirical magnitudes** â€” there are no elasticities, participation/hours effects, welfare-effect sizes, opportunity shares, or decomposition shares, because there is no data. The "results" are analytic formulae. The substantive deliverables, with units where they exist:

- **Distribution of the random expenditure function** (Theorem 1, eq. (12), p. 61): $P(Y_B(\mathbf{w},u)\le y)=1-F^B(u-v_1(w_1,y),\dots,u-v_m(w_m,y))$ â€” a CDF over the money metric.
- **Hicksian (compensated) choice probabilities** as a **one-dimensional integral** (Theorem 2, p. 62).
- **Discrete-choice Shephard's Lemma** (Corollary 1, p. 63): $\partial EY_B(\mathbf{w},u)/\partial w_{1j}=P^h_B(j,\mathbf{w},u)$ â€” the price-derivative of aggregate expenditure equals the fractional compensated demand (= Hicksian choice probability).
- **Closed-form mean expenditure / mean CV in the MNL case** (Corollary 5, eq. (20), p. 70) and nested-logit examples (Example 1, eqs. (22)â€“(23), p. 71).
- **Consistency check:** Example 4 (pp. 72â€“73) verifies that the general machinery reproduces the familiar linear-in-income log-sum mean-CV formula (eq. (29)) as a special case.

**Benchmarking value for my plausibility checks:** **low/indirect.** Because there are no numbers, the paper cannot tell me whether my opportunity share or welfare spread is plausible. Its benchmarking role is purely *formal* â€” it tells me the *correct closed form* my MNL welfare integrator should reduce to in the linear-in-income limit, which is a useful **unit-test target** (if I linearise $v$ in $c$, my integrator should reproduce eq. (29)).

---

## 10. Estimators, theorems, or formal results
For each, statement (in LaTeX, near-verbatim), assumptions, technique, reusability verdict.

**Theorem 1 (random expenditure function; p. 61).** $Y_B(\mathbf{w},u)$ is uniquely defined by (8), continuous in $(\mathbf{w},u)$, increasing in prices, strictly increasing in $u$; and
$$P(Y_B(\mathbf{w},u)\le y)=1-F^B\big(u-v_1(w_1,y),\dots,u-v_m(w_m,y)\big),\quad u\in\mathbb{R},\,y>0.$$
- *Assumptions:* $v_k$ continuous, decreasing in price, strictly increasing in income; $F^B$ has continuous density; $B$ finite.
- *Technique:* (i) per-alternative inverse $Y_k(w_k,u-\varepsilon_k)$ from monotonicity in income; (ii) expenditure = $\min_k Y_k$; (iii) translate the min-event into the utility-domain event and read off $F^B$.
- *Verdict:* **Yes â€” directly reusable.** This is the distributional backbone of my money-metric inversion.

**Theorem 2 (Hicksian choice probabilities; p. 62).**
$$P^h_B(j,\mathbf{w},u)=\int_0^\infty F^B_j\big(u-v_1(w_1,y),\dots,u-v_m(w_m,y)\big)\,v_j(w_j,dy),\quad u\in\mathbb{R}.$$
- *Assumptions:* as Theorem 1, plus differentiability of $F^B$ in component $j$.
- *Technique:* change of variable $u_j=v_j(w_j,y_j)$ introduces the Jacobian $v_j(w_j,dy)$; only a 1-D integral remains.
- *Verdict:* **Maybe â€” secondary.** Useful if I report compensated transition/choice probabilities; not needed for the level-welfare headline.

**Corollary 1 (discrete-choice Shephard's Lemma; p. 63).** With $v_j(w_j,y)=\psi_j(y-w_{1j},w_{2j})$ and finite expected expenditures,
$$\frac{\partial EY_B(\mathbf{w},u)}{\partial w_{1j}}=P^h_B(j,\mathbf{w},u).$$
- *Technique:* differentiate the mean-expenditure integral under the integral sign; use $\partial v_j/\partial w_{1j}=-\partial v_j/\partial y$.
- *Verdict:* **Maybe.** Conceptually important (it is the "aggregate/probabilistic Shephard's Lemma," p. 64); a useful sanity/derivative check, not a core computation for me.

**Theorems 3â€“4 and Corollaries 2â€“4 (two-period CV distribution and compensated transitions; pp. 64â€“69).** Joint distribution of $\big(Y_B(\mathbf{w},V_B(\mathbf{w}^0,y^0)),\,J_B(\mathbf{w}^0,y^0),\,J^*_B(\mathbf{w}^0,y^0,\mathbf{w})\big)$, with $\mathrm{cv}=y^1-Y_B(\mathbf{w},V_B(\mathbf{w}^0,y^0))$; the GEV specialisation (Corollary 3) needs **no integration**.
- *Verdict:* **No / deferred.** These power a *reform-CV* analysis (transitions $i\to j$ induced by a policy at fixed utility). My baseline is a level exercise; relevant only if I add the D3 EV/CV reform cross-check.

**Corollary 5 (i.i.d. EV / MNL specialisation; p. 70).** For $0<y<y_i(\mathbf{w}^0,y^0,w_i)$,
$$P\big(Y_B(\mathbf{w},V_B(\mathbf{w}^0,y^0))>y,\,J_B(\mathbf{w}^0,y^0)=i\big)=\frac{\exp(v_i(w_i^0,y^0))}{\sum_{k\in B}\exp\big(\max(v_k(w_k,y),v_k(w_k^0,y^0))\big)},$$
with the mean-expenditure integral (20).
- *Verdict:* **Yes â€” high value.** This is the MNL case I am in; the analytic-in-$\varepsilon$ closed form is the template for my welfare integrator and a unit-test target.

**Lemma 1 (moment identity; p. 63):** $\int_0^\infty x^\alpha\,dH(x)=\alpha\int_0^\infty x^{\alpha-1}(1-H(x))\,dx$. Utility: turns the expenditure CDF into expected expenditure/moments. *Verdict:* **Maybe** â€” handy if I compute welfare moments directly from the CDF.

---

## 11. Robustness and specification sensitivity
**N/A in the empirical sense** (no estimation to stress-test). The paper's "specification sensitivity" is *model-class* generality:
- It works for any $F^B$ with continuous density; specialises cleanly to **GEV** (Â§6, p. 68), **nested logit** (Example 1), **MNL** (Â§7), and **random-coefficient / mixed MNL** (Â§5, p. 68, where Theorem 3 holds conditional on $\beta$ then integrate over $f(\beta)$).
- The **choice-set-change** robustness (adding/removing alternatives via $\pm\infty$ prices; Examples 2â€“3) shows the formulae survive set changes â€” informative for my "is this job type in the set?" representation, but again as a *device*, not an estimated mechanism.

**What this tells my recovery/stability and robustness sections:** mainly a **numerical-correctness** message â€” in the GEV class the welfare expectation is closed-form (Corollary 3 "no integration is needed"), so where my integrator uses simulation I should be able to cross-check against the analytic GEV expression and treat divergence as a bug, not noise. It does **not** speak to effective-sample-size, draw counts, or circumstance partitions (my actual stress tests), because it has no sampling step.

---

## 12. What I can cite this paper for
Specific, attributable claims:
1. That in random-utility discrete choice **nonlinear in income**, the linear-in-income log-sum welfare formula does **not** apply, and a distinct expenditure-function approach is required (p. 58, p. 64). *(Use this to justify why I cannot use the naive log-sum CV in my Boxâ€“Cox setting.)*
2. The existence and uniqueness of a **random expenditure function** $Y_B(\mathbf{w},u)=\min_{k\in B}Y_k(w_k,u-\varepsilon_k)$, obtained by a **one-dimensional inversion per alternative** (eqs. (8)â€“(10), Theorem 1). *(Use to ground my "invert attained utility to equivalent income" step.)*
3. That in the **GEV/MNL** class the distribution and **mean of CV are available in closed form / by a one-dimensional integral, with the expectation over the extreme-value shocks taken analytically** (Corollaries 3â€“5; eq. (20)). *(Use to justify my analytic-in-$\varepsilon$ integrator and as a unit-test target.)*
4. The **discrete-choice (aggregate/probabilistic) Shephard's Lemma** (Corollary 1). *(Cite if I use the price-derivativeâ€“Hicksian-probability link.)*
5. That **EV is derived analogously to CV** in this framework (Conclusion, p. 73). *(Cite for the D3 EV/CV cross-check.)*
6. The methodological stance â€” following McFadden (2001) â€” that the **analytic expenditure-function method is preferable to simulation** for welfare in nonlinear-in-income RUMs (Conclusion, p. 73). *(Cite to defend the analytic design choice.)*

---

## 13. What I should NOT cite this paper for  [overclaim risks]
- **Not** for any **opportunity mechanism / feasible-set heterogeneity**: the set is exogenous and fixed; the paper has no $g$, no access/ability split, no offer probabilities. Do not present it as supporting my opportunity layer.
- **Not** for the **sampling-of-alternatives / proposal-prior correction** ($-\log\pi(j)$): absent here; cite McFadden's sampling literature instead.
- **Not** for any **inequality index or decomposition** (two-way *or* three-way): the paper is non-decompositional. Do not let it stand in for Shorrocks/Shapley content.
- **Not** for the **$W^1$â€“$W^6$ family or any Independence-of-$\mathbf{y}$/Independence-of-$A$ responsibility reading**: the paper has no responsibility taxonomy and no reference-preference equivalent income. Those are the **companion Haydarâ€“Maniquet theory paper's** content, imported by the JMP as cited primitives â€” **never attribute the family, the axioms, or the normative classification to Dagsvikâ€“KarlstrÃ¶m, and never read this paper as a theory contribution to my JMP.**
- **Boundary flags that apply:** (i) **two-way vs three-way** â€” N/A but worse: it is *non*-decompositional, so do not cite for decomposition at all; (ii) **ex-post/universal-set vs my constrained ex-ante object** â€” the paper's CV is a two-period reform object at fixed initial own-utility, **not** my single-cross-section level equivalent income; do not equate them; (iii) **"sectoral"/industry vs occupation-as-access** â€” N/A (paper never mentions occupation or industry), so no conflation to import; (iv) **random- vs deterministic-opportunity** â€” the paper's randomness is in *tastes* ($\varepsilon_j$), not in *opportunities*; it makes no claim that opportunities are random, consistent with my deterministic-opportunity framing, but it also makes no claim that they are deterministic â€” it simply has no opportunity object. Do not cite it either way on the opportunity-randomness question.

---

## 14. Direct quotes worth citing
(Short, exact, with page numbers. Reworded paraphrases preferred elsewhere; these are the few places exact wording matters.)
1. p. 58: "when the utility function is nonlinear in income, no analogue to the log-sum approach exists." *(The licence for using the expenditure-function method.)*
2. p. 62 (Definition 1): Hicksian choice probabilities $P^h_B(j,\mathbf{w},u)\equiv P(J_B(\mathbf{w},Y_B(\mathbf{w},u))=j)$ â€” "the probability of choosing $j\in B$ given that the utility level is given and equal to $u$."
3. p. 64: the Marshallian duality (Roy's identity) route "follow[s] from the mean indirect utility function â€¦ only when utility is linear in income." *(Sharp statement of the boundary of the standard method.)*
4. p. 73 (Conclusion): an "aggregate version of Shephard's Lemma holds under rather general conditions," and, citing McFadden (2001), the method "is to be preferred to using simulations."
5. p. 58: the fixed-error assumption "seems reasonable if the error terms characterize tastes [but] is less reasonable if $\{\varepsilon_k\}$ also include unmeasured attributes of alternatives, which may be altered by policy." *(The honest caveat to cite if I add a reform-CV exercise.)*

[All five verified against the supplied PDF text; if quoting in the draft, re-verify exact wording against the published typesetting, as the supplied scan has OCR noise.]

---

## 15. Open questions and risks for my draft
1. **Marginal vs total welfare.** The paper's CV is a *change* object (two-period). My headline is a *level* object (equivalent income of an attained situation). I must be explicit that I borrow the **inversion/expectation engine**, not the reform-CV object, so a referee does not read my levels as their CV. (Risk: object-mismatch overclaim â€” flagged in Â§13.)
2. **Fixed-$\varepsilon$ across regimes.** Live only if I add the D3 EV/CV reform cross-check; then their caveat (errors = tastes vs unmeasured alternative attributes) bears directly on whether my reform-CV is interpretable. Note in the robustness section if D3 is run.
3. **Large alternative sets.** Their closed forms assume a small fixed $B$ and exploit GEV structure with no sampling. My $\mathcal{C}_i$ is large (901 joint / 101 single) and I integrate by importance sampling over draws. Their analytic-in-$\varepsilon$ result justifies the *shock* integration but **not** the *alternative-set* sampling/weighting â€” the variance/ESS behaviour of my IS integrator (welfare spec v5 Â§6 gate) is **not** addressed by this paper and remains my own burden.
4. **Unit-test opportunity.** Their linear-in-income consistency check (Example 4, eq. (29)) is a concrete target: a linearised version of my integrator should reproduce the log-sum mean-CV. Worth building as a regression test for the welfare core.
5. **Numerical integration error.** The paper's claim that the GEV case needs "no integration" (Corollary 3) is a reminder that wherever I *do* integrate numerically, an analytic GEV cross-check should exist; absence of one is a code-smell.

---

## 16. TL;DR for retrieval
Dagsvik & KarlstrÃ¶m (2005, *REStud*) is the **welfare-engine** reference for discrete-choice random-utility models **nonlinear in income**: it builds a random expenditure function via per-alternative one-dimensional inversion of own utility ($Y_B=\min_k Y_k$), derives Hicksian/compensated choice probabilities and a discrete-choice Shephard's Lemma, and gives closed-form, **analytic-in-shocks** CV/EV distributions and means in the GEV/MNL class â€” directly grounding my money-metric inversion of attained utility $V_i$ to equivalent income and corroborating my analytic-$\varepsilon$ integrator. It speaks to **all** my welfare measures uniformly through the *evaluation* engine but to **none** of the access/ability/preference *channels*, because it has **no opportunity mechanism, no inequality/decomposition object, no proposal correction, and no $W^1$â€“$W^6$ family** (those are upstream/elsewhere and, for the family, the companion theory paper). Cite it for the nonlinear-in-income inversion and the closed-form MNL CV/EV; never cite it for opportunity, decomposition, or the responsibility taxonomy.
# Ferreira & Gignoux 2011 â€” The Measurement of Inequality of Opportunity: Theory and an Application to Latin America

> **Extraction status:** T1A exhaustive, per `JMP_T1_exhaustive_extraction_prompt_v2.md`.
> **Source of truth:** the attached PDF (journal pages 622â€“657). Page references below are journal pages.
> **Convention used throughout:** *explicit-in-source* = stated in the paper; *derived-by-analogy* = my mapping to the JMP, not in the paper; *not-established* = neither.
> The paper predates and is unaware of my framework; almost every mapping to RURO/latent-jobs, to money-metric welfare, and to the access/ability/preference cut is *derived-by-analogy*. I flag this explicitly rather than letting the prompt's vocabulary leak into claims about the source.

---

## 0. Metadata

- **BibTeX key:** `FerreiraGignoux2011`
- **Authors:** Francisco H. G. Ferreira (The World Bank; IZA); JÃ©rÃ©mie Gignoux (Paris School of Economics).
- **Year:** 2011.
- **Outlet:** *Review of Income and Wealth*, Series 57, Number 4 (December 2011), pp. 622â€“657.
- **DOI:** 10.1111/j.1475-4991.2011.00467.x (explicit-in-source, p. 622).
- **JEL codes:** D31, D63, J62 (explicit-in-source, p. 622).
- **PDF filename:** `FERREIRA_GIGNOUX_2011_THE_MEASUREMENT_OF_INEQUALITY_OF_OPPORTUNITY.pdf`.
- **Tier:** T1A.
- **JMP block(s) served:** *decomposition* (primary); *normative-interpretation* (secondary); *motivation* (secondary). Does **not** serve estimation, identification of preferences-vs-opportunities in the structural sense, the opportunity-mechanism (access/ability) layer, or data-infrastructure for France.

---

## 1. One-paragraph relevance to my JMP

This is the cleanest available template for the *decomposition* layer: it pins a relative inequality-of-opportunity ratio to the **mean log deviation** $E_0$ via Fosterâ€“Shneyerov path-independent decomposability, and proves that the between-group share is a **lower bound** on true opportunity inequality (pp. 631â€“632, 635â€“636). For my D2 layer it supplies (a) a defensible index choice and (b) a lower-bound argument I can borrow as a defence against the "your decomposition is mechanical" referee â€” but only with a sharp caveat, because their decomposition is **two-way** (between-type "opportunity" vs an "effort+luck" residual) and **subgroup-based**, not the **three-way {access, ability, preference} Shapleyâ€“Shorrocks** factor decomposition I run. On the channel map it speaks to nothing inside my opportunity density $g$: its "circumstances" sit upstream of all three of my channels and it separates none of them, and its advantage variable is reduced-form income/consumption, not a preference-respecting money-metric $V_i$. It is therefore a *measurement-and-decomposition* anchor and a *motivation* citation, and a precise statement of the gap my structural opportunity object is meant to fill.

---

## 2. Data and setting

**Country/year/datasets (explicit-in-source, pp. 637â€“638, Table 1).** Six nationally representative household surveys: Brazil PNAD 1996; Colombia ECV 2003; Ecuador ECV 2006; Guatemala ENCOVI 2000; Panama ENV 2003; Peru ENAHO 2001.

**Sample unit (explicit-in-source, pp. 637â€“638).** Individuals who are household heads or their spouses, aged 30â€“49, with positive income/consumption and complete circumstance information. The age and head/spouse restrictions are imposed for comparability and because in Brazil and Peru background information was only collected for these individuals.

**Sample sizes after exclusions (explicit-in-source, Table 1, p. 638):** Brazil 70,521; Colombia 17,979; Ecuador 10,719; Guatemala 5,988; Panama 4,556; Peru 13,621.

**Key variables (explicit-in-source, pp. 638â€“640, Tables 2â€“4).**
- *Advantage $y$:* household per capita income, and household per capita consumption expenditure where available (consumption absent for Brazil).
- *Circumstances $C$:* father's education, mother's education (each 3 categories), father's occupation (agricultural worker / other; missing for Colombia and Peru), ethnicity/race (2 categories), region of birth (3 categories, or urban/rural for Panama). Gender is used **only** in a separate labour-earnings specification, not in the household-advantage analysis (see Â§8).

**Budget-set construction:** N/A. There is no budget map, no tax-benefit system, no consumption-from-hours construction. Advantage is taken directly from the survey income/consumption aggregate.

**Transport to my France pooled 2015â€“2017 EUROMOD cross-section.**
- *Compatible features (derived-by-analogy):* a single cross-section per country with no panel; a household-level money advantage measure; a partition-into-groups logic that I can re-use over my own groupings.
- *Features I do NOT have that they rely on / features they lack that I have:* they have **intergenerational background circumstances** (parental education, father's occupation, ethnicity, birthplace) that EU-SILC/EUROMOD does not deliver in usable form for France; they have **no behavioural model, no labour-supply choice, no wages-as-offers, no occupation-as-availability, and no tax-benefit budget**, all of which I have. They have **no panel, no administrative match, no external instrument, and no vacancy/offer data** â€” the same instrument poverty I face, which is relevant to Â§8.

---

## 3. Model and objects (object-by-object)

The paper is a **measurement framework, not a behavioural or structural model** (explicit-in-source, Â§2). The object-by-object map is therefore mostly a list of absences; I state each explicitly because the absences are exactly what my structural layer supplies.

- **Their choice set vs my latent-jobs set $\mathcal{C}_i$:** none. There is no choice set, no alternatives, no discrete choice. *Not-established* in the source.
- **Their deterministic utility vs my preference utility $v$:** none. No utility function, no Boxâ€“Cox, no taste-shifters. Preferences are *not modelled at all*; whatever they would explain is absorbed into the residual (explicit-in-source, "Treatment of preferences" is empty by construction â€” see Â§7 of the source's own framing and p. 633).
- **An explicit opportunity / availability mechanism analogous to my $g$:** none in the structural sense. "Opportunity" is operationalised as a **partition of the population into Roemerian types** $T_k$ that are homogeneous in observed circumstances (explicit-in-source, p. 626). There is no density over feasible jobs, no hours availability, no wage-offer technology, no participation/market mechanism, and no occupation-as-availability object. It therefore does **not** separate hours / wage(ability) / market / occupation channels.
- **Their budget map vs my EUROMOD disposable income:** none. Advantage is the raw survey aggregate (pp. 638â€“639).
- **Does any job attribute enter BOTH utility and the opportunity mechanism?** N/A â€” there is neither a utility block nor an opportunity mechanism, so the double-counting hazard the prompt asks me to flag cannot arise here. Worth recording the contrast: their *circumstances* are by construction **exogenous and upstream**, never simultaneously a taste-shifter and an availability shifter, precisely because there is no behavioural layer for them to enter twice.

**Net:** the only object that maps to mine is the **advantage variable** $y$ â†” my money-metric welfare $W$/$V_i$, and even that map is loose: $y$ is reduced-form income/consumption, not a preference-respecting equivalent income.

---

## 4. Estimation method

**Likelihood and estimator (explicit-in-source, Â§3, pp. 632â€“636).** There is no likelihood. Two procedures estimate the *same* path-independent quantities:
1. **Non-parametric:** compute the between-group component of the MLD directly from type-cell means, i.e. $E_0(\{\mu_i^k\}) = \tfrac{1}{N}\sum_i \log(\mu/\mu_i^k)$ with $\mu$ the grand mean and $\mu_i^k$ the type mean assigned to $i$ (explicit-in-source, p. 632).
2. **Parametric:** OLS of log advantage on circumstances, $\ln y = C\psi + \varepsilon$; build a parametric *smoothed* distribution $\tilde\mu_i=\exp[C_i\hat\psi]$ (eq. 8) and a parametric *standardized* distribution $\tilde\nu_i=\exp[\bar C\hat\psi+\hat\varepsilon_i]$ (eq. 9), then form $E_0$-based IOL/IOR from the standardized estimates (eqs. 10â€², 11â€²) (explicit-in-source, pp. 633â€“634).

**Choice-set construction / fixed grid vs sampled alternatives / grid size:** N/A â€” no choice set, no grid, no alternatives.

**Proposal / sampling density; prior/proposal correction:** N/A. There is **no** $\log(\text{prior})$ correction because there is no sampling of alternatives. This is the central structural reason the paper cannot be reused as an estimator for my pipeline.

**Normalisation / scale / numerical method / starting values / multistart:** N/A beyond standard OLS. Bootstrap standard errors are computed accounting for sampling weights, stratification, and clustering (explicit-in-source, p. 643).

**What pins preferences separately from the opportunity mechanism:** nothing â€” preferences are not in the model. The "between vs within" split is a *definitional* allocation (between-type = opportunity; within-type = effort+luck+unobserved circumstances), not an identified behavioural separation. This is exactly the separation my structural model is built to earn rather than assume.

**Verdict (reusable for my RURO/JAX pipeline?):** **No** for the estimator. The estimation machinery (OLS + between-group $E_0$) is not a discrete-choice estimator and carries no proposal correction. **Yes, partially**, for the *downstream* decomposition: the between-group $E_0$ computation and the path-independence argument are directly reusable in D2 *as the index/decomposition rule*, applied to my welfare object instead of to income â€” but the **factor** structure I need (Shapley over access/ability/preference) is not what they implement (see Â§7).

---

## 4b. Proposal / sampling-of-alternatives correction

**N/A â€” extract recorded for completeness.** The paper performs no sampling of alternatives and therefore has no proposal density, no per-alternative log-prior, and no McFadden-style correction. There is no individualised-vs-common proposal distinction to map onto my importance-sampling welfare integrator (where wage and occupation are individualised and hours/employment are common, per welfare spec v5 Â§V5-1). The only faint analogue is the **parametric counterfactual construction** (eqs. 8â€“9, 12): replacing residuals or fixing circumstances to build smoothed/standardized distributions is a *re-weighting-by-construction* of the empirical distribution, conceptually adjacent to a counterfactual integrator but with no stochastic sampling and no importance weights. Treat as *derived-by-analogy only*; do not cite this paper for anything about sampling-of-alternatives corrections.

---

## 5. Opportunity mechanism  [MOST IMPORTANT]

**There is no explicit opportunity mechanism in the structural sense.** I state this plainly because it is the paper's defining limitation for my purposes and the precise location of my contribution.

**What plays the role of "opportunity" (explicit-in-source, Â§2, pp. 626â€“629):** the population is partitioned into Roemerian **types** $T_k$, homogeneous in observed predetermined circumstances. "Equality of opportunity" is operationalised, following van de Gaer (1993), by the **weak criterion** that *mean* advantage be equal across types (eq. 4), a weakening of Roemer's (1998) *strong* criterion of equal conditional distributions (eq. 3). Inequality of opportunity is then between-type inequality in the **smoothed distribution** $\{\mu_i^k\}$ (each individual replaced by their type mean) (explicit-in-source, p. 630). It is **not** a density over alternatives, **not** offer probabilities, and **not** a reservation-wage/participation restriction.

**Does it vary with observable circumstances?** Yes â€” that is the entire content: opportunity is *defined* by variation in mean advantage across circumstance cells (region of birth, parental education, father's occupation, ethnicity). But these are **background/origin circumstances**, not contemporaneous labour-market availability.

**Map to my three sub-objects (derived-by-analogy):**
- **access** (hours / market-participation / region / year / occupation offers): **not represented.** Region appears, but as *region of birth* (an origin circumstance), not as a local-labour-market access shifter. No hours availability, no participation mechanism, no occupation offers.
- **ability** (the wage technology â€” returns to own education and experience, residual productivity dispersion): **not represented.** Parental education is a circumstance; the *respondent's own* education-and-experience wage return â€” my ability block â€” is not a structural object here, and in the reduced form it is absorbed into the residual/effort term rather than modelled.
- **occupation as availability vs something else:** the paper uses **father's occupation** (agricultural worker / other) as a *background circumstance*, i.e. an intergenerational-origin variable. This is **not** my `loc4` occupation-as-access object, and it is **not** industry/sector either. **Flag:** do not let "father's occupation" be read as occupation-opportunity in my sense; it is a parental-origin circumstance. There is no sector/industry conflation in the source to flag, because there is no contemporaneous occupation or industry object at all.

**Functional form:** type means (non-parametric) or $\exp[C\hat\psi]$ from a log-linear OLS (parametric).

**Cost of the omission for my access/ability/preference decomposition (derived-by-analogy):** because the source has no feasible-set object, it cannot distinguish demand-side job availability (my *access*) from the wage-generating technology (my *ability*) from tastes (my *preference*); all three are either folded into the circumstance partition (if correlated with background) or dumped into the residual (if not). My structural opportunity density is precisely what makes the access/ability split *identifiable as a modelled object* rather than assumed via a partition. The paper's lower-bound logic (Â§8) is, in effect, a confession that an unmodelled opportunity object leaves opportunity inequality understated â€” which is the motivation for modelling it.

---

## 6. Welfare object â€” and its place on my $W^1$â€“$W^6$ map

**Does the paper compute welfare? No.** It computes **inequality indices** ($\theta_a$/IOL absolute, $\theta_r$/IOR relative), not a welfare function (explicit-in-source, pp. 630â€“632). There is:
- no money-metric welfare, no equivalent income, no King (1983)/Fleurbaey-style construction;
- no compensating/equivalent variation;
- no expected (log-sum / inclusive-value) utility;
- no reference price, reference preference, reference bundle, or reference set;
- no discrete-choice welfare subtleties (no log-sum aggregation, no Hicksian/Marshallian distinction, no integration over unobserved heterogeneity, no ex-ante/ex-post welfare integration). The *ex-ante vs ex-post* language **does** appear (pp. 628â€“629), but as a distinction between **inequality-of-opportunity criteria** (van de Gaer ex-ante / Checchiâ€“Peragine ex-post), **not** as a welfare-integration timing choice. Do not import their ex-ante/ex-post usage as if it were my ex-ante inclusive-value vs ex-post chosen-alternative distinction.

**Place on my $W^1$â€“$W^6$ map.** **None â€” the source contains no $W^1$â€“$W^6$ object and no equivalent-income measure of any kind.** Mapping the advantage variable $y$ onto the family is *derived-by-analogy at best*: raw income/consumption corresponds to no specific Independence-of-$y$ / Independence-of-$A$ stance, because it embeds no preference-respecting reference at all. If forced, $y$ is closest in spirit to a **pre-welfare outcome** that my measures evaluate, not to any member of the family. **Verdict: incompatible as a welfare object; adaptable only as the *target distribution* a decomposition is run on** â€” i.e. swap their $y$ for my $V_i$/$W^k$ and re-use the index, which is the use the original MD note already proposes.

---

## 6b. Inclusive value and money-metric inversion

**N/A.** The paper uses no inclusive value (no log-sum, no expected maximum), no EV/CV, and performs no money-metric inversion. There is no analytic-in-shocks vs simulation question because there are no extreme-value shocks and no discrete-choice structure. Nothing here maps to my analytic-in-shocks, importance-sampling inversion.

---

## 7. Inequality / decomposition content  [three-way where relevant]

**Inequality index (explicit-in-source, pp. 631â€“632).** **Mean log deviation $E_0$** (Theil-L; the $\alpha=0$ member of Generalized Entropy), uniquely selected by adding **Fosterâ€“Shneyerov (2000) path-independent decomposability** to the standard axioms (symmetry, transfer principle, scale invariance, population replication, additive decomposability). IOL $=\theta_a=E_0(\{\mu_i^k\})$ (eq. 5â€²); IOR $=\theta_r=E_0(\{\mu_i^k\})/E_0(y)$ (eq. 6â€²).

**Decomposition rule (explicit-in-source).** **Subgroup / between-group decomposition** of $E_0$ by population subgroups, where subgroups are circumstance types. The "opportunity" component is the **between-type** $E_0$ of the smoothed distribution; the "ethically acceptable" remainder is the **within-type** component (effort + luck + unobserved circumstances). This is a *Theil-L by-subgroup* decomposition, **not** a Shapley, **not** a Shorrocks factor decomposition, **not** RIF, **not** Owen-grouped.

**Counterfactual construction (explicit-in-source, pp. 630â€“634).**
- *Smoothed distribution* $\{\mu_i^k\}$: replace each individual's advantage with the **type mean** â€” eliminates all within-type inequality, isolating between-type (opportunity) inequality. (What is *neutralised*: within-type variation.)
- *Standardized distribution* $\{\nu_i^k\}$: rescale by $y_i^k\cdot\mu/\mu^k$ â€” eliminates all between-type inequality, isolating within-type. (What is *neutralised*: between-type variation.)
- *Partial / circumstance-specific shares* (eqs. 12â€“13): equalise **one** circumstance while holding the others at their actual values, yielding "partial IORs."

**Order-independence / path-independence / exhaustiveness (explicit-in-source, pp. 631â€“632).** Path-independent decomposability is the headline property and is what pins the index to $E_0$. For $\alpha\neq 0$ Generalized Entropy measures the two decomposition paths (smoothed vs standardized) do **not** coincide; for $E_0$ they do. This is the cleanest available statement that *the choice of index is not innocuous for a decomposition* â€” directly relevant to my Shapley-exhaustiveness gate (welfare spec v5 Â§6(a)), though the mechanism is different (mine is Shapley symmetry/efficiency; theirs is path-independence of a subgroup split).

**Verdict (reusable for my three-way access/ability/preference Shapleyâ€“Shorrocks split?).** **Partially â€” index yes, decomposition architecture no.**
- *Reusable:* $E_0$ as the inequality index; the path-independence justification; the lower-bound logic as a robustness/defence argument; the smoothed/standardized counterfactual logic as the *conceptual* model of "neutralise a source."
- *Not reusable as-is:* the decomposition is **two-way** (opportunity vs residual) and **subgroup-based** (types), whereas mine is **three-way** (access / ability / preference) and **factor-based** (Shapley equalisation of structural channels). To get from theirs to mine you would have to (i) replace circumstance *types* with structural *channels* in $g$ and $v$, (ii) replace the single between/within cut with sequential Shapley equalisations of three factors, and (iii) accept that the path-independence theorem that licenses their unique $E_0$ split does **not** transfer â€” Shapley order-independence is a different property earned by averaging over equalisation orders, not by Fosterâ€“Shneyerov path-independence. **State this explicitly in the draft so the referee does not read the $E_0$ choice as if it also licensed the three-way Shapley split.**

---

## 8. Identification and the separation of preferences from opportunities  [STRICT]

**What identifies tastes vs constraints â€” and ability vs access within opportunity?** *Nothing, in the structural sense, and the paper is candid about this.*
- There is **no causal identification** (explicit-in-source, the paper repeatedly disclaims causal interpretation; the reduced form $\ln y=C\psi+\varepsilon$ is interpreted as encompassing both direct circumstance effects and indirect effects through effort, pp. 633â€“634).
- The maintained assumption is that **observed circumstances are exogenous/predetermined** (explicit-in-source, p. 626 and Â§3). The opportunity/residual split is a **definitional allocation under this assumption**, not an identified behavioural decomposition.
- **Ability vs access is not separated** (derived-by-analogy): there is no wage technology and no feasible-set object, so the within-opportunity structure my JMP cares about simply does not exist here.
- **Preferences are not identified because they are not modelled.** The within-type residual is labelled "effort + luck (+ unobserved circumstances)", *not* "preferences." It is therefore wrong to read their residual as my *preference* channel; it is an undifferentiated remainder.

**The lower-bound result (explicit-in-source, Proposition and Corollary, pp. 635â€“636).** Adding any omitted circumstance refines the partition and **weakly increases** between-type inequality in the smoothed distribution (by a mean-preserving-spread / transfer-principle argument); the denominator $I(y)$ is invariant to $C$, so IOR is also a lower bound. Hence all estimates based on observed circumstances are **lower bounds** on true inequality of opportunity. This is the paper's identification-substitute: it does not identify the true share, only a floor.

**Transport to my France pooled cross-section (derived-by-analogy).** The honest reading is *cautionary, not enabling*. The paper demonstrates that **without a structural model you cannot separate opportunity from preference at all** â€” you can only bound an opportunity *share* under an exogeneity assumption on background circumstances I largely cannot even observe in EU-SILC/EUROMOD for France. My identification therefore cannot lean on their machinery; it must come from the **structural functional-form and choice-set restrictions** of the RURO model plus **synthetic-recovery certification** (project state v1 Â§8, principle 1), exactly because the reduced-form route is unavailable. What I *can* borrow is the **lower-bound rhetorical move** as a defence: even my structural opportunity share can be framed as conservative if some opportunity variation remains unmodelled. Do **not** soften the core point: this paper offers a *measurement* identification story (exogenous circumstances + lower bound), not a *behavioural* one, and the "your decomposition is mechanical" referee is answered in my paper by the structural model and synthetic recovery, not by anything in Ferreiraâ€“Gignoux.

**One concrete transferable identification caveat (explicit-in-source, pp. 639â€“640):** gender is excluded from the household-advantage circumstance set because **household headship and household formation involve choice**, so the head's gender is endogenous and including it would *invalidate the lower-bound claim*. This is a direct warning for my **couples-as-joint-unit** design and my gender-attribution rules (welfare spec v5, A1/A2/A3): household-level gender assignment is not a clean "circumstance," and any opportunity-share statement that conditions on the head's gender inherits an endogeneity that breaks a lower-bound interpretation. Carry this into the identification note.

---

## 9. Key results and magnitudes

All numbers explicit-in-source (Tables 6â€“9, pp. 643â€“648), lower-bound shares for the stated populations (heads/spouses aged 30â€“49). Income covers all six countries; consumption covers five (Brazil has no consumption data).

**Household per capita income â€” IOR (Table 6, Panel A):**
- Non-parametric: Brazil 0.329, Colombia 0.252, Ecuador 0.283, Guatemala 0.359, Panama 0.338, Peru 0.293.
- Parametric (standardized): Brazil 0.322, Colombia 0.232, Ecuador 0.259, Guatemala 0.335, Panama 0.301, Peru 0.279.
- Range (conclusion, p. 654): IOR â‰ˆ **0.23 (Colombia) to 0.34 (Guatemala)**; IOL â‰ˆ 0.13 (Colombia) to 0.22 (Brazil).

**Household per capita consumption â€” IOR (Table 6, Panel B):**
- Non-parametric: Colombia 0.265, Ecuador 0.346, Guatemala 0.532, Panama 0.409, Peru 0.351.
- Parametric: Colombia 0.247, Ecuador 0.326, Guatemala 0.514, Panama 0.377, Peru 0.339.
- Headline (abstract, p. 622; results, pp. 643â€“644): between **one quarter and one half** of consumption inequality is opportunity-related (â‰ˆ 0.25 to â‰ˆ 0.51 parametric; up to 0.53 non-parametric, Guatemala).

**Income vs consumption (explicit-in-source, pp. 647):** IOR is *higher* for consumption than income in all five countries, driven by *lower within-type (residual) inequality* in consumption; IOL levels are generally similar or slightly lower for consumption. Interpretation offered: income-based IOR may understate permanent-income opportunity inequality because transitory variance and measurement error inflate the within-type residual and are counted as "effort/luck."

**Parametric vs non-parametric agreement (explicit-in-source, p. 644):** differences never statistically significant; rank-correlation of IOL across methods 0.89 (income), 0.90 (consumption); parametric is the preferred lower bound at small sample sizes.

**Partial (circumstance-specific) IORs (Table 9, pp. 647â€“648):** family background dominates; **mother's education** is the single largest circumstance (consumption share â‰¥ 0.16 everywhere, up to 0.29 in Guatemala); father's education generally exceeds ethnicity and birth region. In the *labour-earnings* specification, the **gender** share (after controlling for other circumstances) is small â€” roughly 0.2% (Colombia) to 5.8% (Guatemala).

**Opportunity-deprivation profiles (Tables 10â€“11, Â§6, pp. 649â€“653):** the worst-off ~10% are sharply concentrated. In **three of six** countries (Brazil, Guatemala, Peru) the opportunity-deprived are **100% ethnic/racial minorities**; mother-without-education exceeds ~90% in every country; agricultural-father and specific birth regions dominate.

**Equivalence-scale robustness (Table 8, pp. 645â€“646):** Buhmann et al. (1988) scale, $a=0.5$ and $0.75$; IOL falls as scale economies rise; **IOR is stable for income and sometimes higher for consumption** (e.g. Guatemala consumption IOR â‰ˆ 0.54).

**Benchmark value for my own numbers (derived-by-analogy):** these are *outcome* (income/consumption) opportunity shares from *background circumstances*, not *welfare* opportunity shares from a *feasible-set* model. Use them only as a loose order-of-magnitude prior ("opportunity components of 20â€“50% of an outcome's inequality are not implausible in the broad literature"), **not** as a direct benchmark for my $V_i$-based access/ability shares, which are conceptually different objects.

---

## 10. Estimators, theorems, or formal results

**(R1) Scalar IO indices (eqs. 5â€², 6â€², p. 632; explicit-in-source).**
$$\theta_a = E_0(\{\mu_i^k\}), \qquad \theta_r = \frac{E_0(\{\mu_i^k\})}{E_0(y)}.$$
- *Assumptions:* $I(\cdot)$ satisfies symmetry, Pigouâ€“Dalton transfer, scale invariance, population replication, additive decomposability, **and** Fosterâ€“Shneyerov path-independent decomposability; the smoothed distribution is built on a circumstance partition.
- *Technique:* path-independence uniquely selects $E_0$ within Generalized Entropy; $\theta_a$ is then the between-group Theil-L component, $\theta_r$ its share.
- *Reusability verdict:* **Yes** for the decomposition layer's index choice, applied to my $V_i$/$W^k$ rather than to income. **No** as a stand-in for the Shapley factor split.

**(R2) Lower-bound Proposition and Corollary (pp. 635â€“636; explicit-in-source).** $\theta_a(\{y,C\})$ is a lower-bound estimator of true $\theta_a^*(\{y,C^*\})$, and $\theta_r$ likewise (denominator invariant to $C$).
- *Assumptions:* observed $C$ is a sub-vector of the true circumstance vector $C^*$; $I(\cdot)$ satisfies the transfer principle.
- *Technique (3â€“5 bullets):* (i) an unobserved circumstance refines each type cell; (ii) refining a cell replaces a within-cell zero-inequality block with a non-negative-inequality block of the same mean; (iii) this is achievable by mean-preserving spreads; (iv) by the transfer principle between-group inequality weakly rises; (v) the denominator $I(y)$ is unchanged, so the ratio is also a lower bound.
- *Reusability verdict:* **Maybe / rhetorical** â€” reusable as a *framing* argument that my structural opportunity share is conservative; **not** a theorem about my Shapley decomposition, and I must not present it as one.

**(R3) Roemer strong criterion â†’ van de Gaer weak criterion (eqs. 3â€“4, pp. 627â€“629; explicit-in-source).** Equality of opportunity weakened from equality of conditional distributions $F^k(y)=F^l(y)$ to equality of conditional means $\mu^k(y)=\mu^l(y)$.
- *Reusability verdict:* **No** for estimation; **useful** only for the normative-framing section if I discuss ex-ante valuation of opportunity sets by their mean.

No estimator, theorem, or formal result here is reusable for my **estimation** or **welfare-inversion** layers; R1 is the only one reusable for the **decomposition** layer, and only as the index, not the architecture.

---

## 11. Robustness and specification sensitivity

What they vary and what it tells me (explicit-in-source unless flagged):
- **Parametric vs non-parametric (pp. 643â€“644):** agree closely; supports robustness of the *level* of the share. *For me:* a cheap internal cross-check pattern, not a structural test.
- **Cell sparsity / number of types (pp. 633, 640â€“642, Table 5):** with $J=5$ circumstances and $K$ up to 108, two countries (Guatemala, Panama) have >25% of cells with <5 observations; sparse cells **inflate** non-parametric between-type inequality, biasing IO **upward**, which is why the parametric route is preferred at small $N$. *For me (derived-by-analogy):* a direct warning about partition coarseness and small-cell noise that maps onto my **effective-sample-size** concern in the welfare integral (welfare spec v5 Â§6(b)(ii): median ESS â‰ˆ 20/101 for singles) â€” different mechanism, same lesson: thin cells/weights manufacture spurious dispersion, so report ESS and stress-test against draw/partition refinement.
- **Equivalence scale (Table 8, pp. 645â€“646):** IOL sensitive, IOR stable/robust. *For me:* supports reporting a *ratio/share* as the more robust object than a *level* â€” relevant to whether my headline is an opportunity *share* or a *level*.
- **Income vs consumption advantage (p. 647):** the choice of advantage variable materially moves the IOR through the residual. *For me:* a precedent that the *welfare object* choice matters â€” which is exactly the v5 thesis that the $W^1$â€“$W^6$ menu spread is itself a result; cite as motivation that the advantage/welfare definition is not innocuous.
- **What they do NOT stress-test:** any opportunity-mechanism specification (there is none), any preference specification (none), any choice-set size or draw count (none). So this section gives me nothing on my recovery/stability gates beyond the partition-sparsity analogy.

---

## 12. What I can cite this paper for

Specific, attributable claims:
1. The relative inequality-of-opportunity ratio is the between-type share of total inequality, and under path-independent decomposability the index is uniquely the **mean log deviation** $E_0$ (pp. 631â€“632).
2. Inequality-of-opportunity measures based on observed circumstances are **lower bounds** on true inequality of opportunity (Proposition/Corollary, pp. 635â€“636).
3. Empirically, lower-bound opportunity shares are **large** â€” roughly one-fifth to one-third of income inequality and one-quarter to one-half of consumption inequality across six Latin American countries (Table 6; abstract).
4. **Family background** (parental education, father's occupation) is the dominant circumstance, with mother's education the single largest partial share (Table 9).
5. Opportunity-deprivation profiles concentrate the worst-off in ethnic minorities and low-parental-education origins (Tables 10â€“11) â€” a template for *worst-off-group* identification I could adapt over welfare-type groupings.
6. The ex-ante (van de Gaer, between-type) vs ex-post (Checchiâ€“Peragine, within-tranche) distinction in the **inequality-of-opportunity** literature (pp. 628â€“629) â€” for positioning, not for my welfare-integration timing.
7. The methodological point that household **headship/gender is endogenous** and cannot be treated as a clean circumstance for household advantage (pp. 639â€“640) â€” for my gender-attribution and couples-unit discussion.

---

## 13. What I should NOT cite this paper for  [overclaim risks]

- **Two-way, not three-way.** Their decomposition is opportunity vs an undifferentiated "effort+luck" residual. Do **not** cite it as support for a three-way {access, ability, preference} split, and do **not** equate their residual with my *preference* channel.
- **Subgroup, not factor/Shapley.** It is a between-/within-subgroup Theil-L decomposition. Do **not** cite it as a Shapleyâ€“Shorrocks factor decomposition, and do not let the path-independence theorem be read as licensing my Shapley split (different property, Â§7).
- **No welfare object.** It computes inequality indices, not welfare. Do **not** cite it for money-metric/equivalent-income welfare, for inclusive-value welfare, or for any $W^1$â€“$W^6$ measure â€” **the source contains no $W^1$â€“$W^6$ object and no equivalent income.** Do not present its income/consumption $y$ as my constrained ex-ante welfare object.
- **No opportunity mechanism.** Its "opportunity" is a circumstance partition, not a feasible set / opportunity density. Do **not** cite it for hours/wage/market availability, for *access* or *ability* as modelled channels, or for occupation-as-availability.
- **"Father's occupation" â‰  occupation/sector opportunity.** It is an intergenerational-origin circumstance. Do **not** read it as my `loc4` (ISCO occupation-as-access), and certainly not as industry/sector (`lindi`/NACE). The source has no contemporaneous occupation or industry object, so there is no sector/industry conflation to attribute â€” and none to borrow.
- **Lower bound â‰  identified true share.** Do not present their shares (or any I construct in their style) as the *true* opportunity share; they are explicitly floors.
- **Cross-country shares are not country rankings I endorse.** Consistent with my hard boundary, do not let citation of their cross-country table drift my JMP toward a ranking exercise.
- **Theory-paper boundary.** Nothing here is the companion Haydarâ€“Maniquet axiomatic paper; do not attribute any characterisation/uniqueness/proof to the JMP, and do not read the JMP as a theory contribution. (This paper *is* useful precisely as the empirical/measurement tradition the JMP sits in, not as theory.)
- **Deterministic-opportunities framing.** Not implicated either way â€” the source has no random/deterministic opportunity object â€” so do not cite it for the "opportunities are deterministic" stance.

---

## 14. Direct quotes worth citing

> **Copyright/extraction note.** The PDF is copyrighted (Wiley-Blackwell notice, final page). I therefore give **page-anchored paraphrases** rather than reproducing multiple verbatim strings, with a single short verbatim phrase where exact wording carries weight. Pull longer verbatim quotes yourself from the PDF if a referee response requires them.

1. **(short verbatim, p. 622)** The measure captures "between-group inequality when groups are defined exclusively on the basis of predetermined circumstances."
2. *(paraphrase, p. 622):* lower-bound opportunity shares range from roughly a quarter to a half of total consumption inequality across the six countries.
3. *(paraphrase, pp. 631â€“632):* adding path-independent decomposability to the standard axioms restricts the index uniquely to the mean log deviation.
4. *(paraphrase, pp. 635â€“636):* because any omitted circumstance refines the type partition and cannot lower between-group inequality, the estimates are lower bounds on true inequality of opportunity.
5. *(paraphrase, pp. 639â€“640):* because headship and household formation involve choice, the head's gender is not a valid circumstance for household-advantage opportunity measurement.
6. *(paraphrase, pp. 643â€“644):* parametric and non-parametric estimates are statistically indistinguishable, with the parametric route preferred as the conservative lower bound in small samples.

---

## 15. Open questions and risks for my draft

- **The residual is not "responsibility."** The paper's within-type remainder bundles effort, luck, and unobserved circumstances; it is not demonstrated to be responsibility-sensitive. My draft must be careful not to inherit this slippage: my *preference* channel is a modelled object, and whether it is "responsibility-relevant" is a normative stance read off the $W^k$ menu (welfare spec v5 Â§V3-3), not an identity with a statistical residual.
- **Lower bound vs structural share.** Their lower-bound floor is an artefact of *unmodelled* opportunity. My contribution is to *model* it â€” so I should frame my opportunity share as addressing the very incompleteness their bound concedes, while acknowledging my own residual unmodelled opportunity (a borrowed lower-bound caveat).
- **Index choice is not innocuous.** Their path-independence result warns that decomposition outputs depend on the index for $\alpha\neq 0$. My Shapley split needs its own exhaustiveness/order-independence guarantee (welfare spec v5 Â§6(a)); do not assume the $E_0$ uniqueness carries over.
- **Cell-sparsity â†” ESS.** The small-cell inflation problem is a clean analogue of my thin importance-sampling weights for singles; the risk that **sparse support manufactures spurious between-component dispersion** applies to both, and is a referee-visible threat to any opportunity-share number.
- **Gender/headship endogeneity** directly threatens any gender-conditioned opportunity statement in my couples analysis; resolve in the identification note before reporting gendered shares.
- **Advantage/welfare definition drives the share.** Their income-vs-consumption gap is empirical support for the v5 bet that the welfare-measure menu spread is itself a finding â€” but it also warns that a reader can move my headline by moving the welfare object, so the $W^1$â€“$W^6$ spread must be reported transparently, not buried.

---

## 16. TL;DR for retrieval

Ferreiraâ€“Gignoux (2011) is the canonical **measurement-and-decomposition** template: it defines absolute/relative inequality-of-opportunity indices as the **between-type share of the mean log deviation**, uniquely justified by path-independent decomposability, proves they are **lower bounds** on true opportunity inequality, and finds large lower-bound shares (â‰ˆ20â€“50% of income/consumption inequality) in six Latin American countries â€” serving my **decomposition** layer (index + lower-bound defence) and **motivation/normative-interpretation**, but **none** of my structural channels. It has **no welfare object** (no money-metric, no $W^1$â€“$W^6$, no inclusive value), **no opportunity mechanism** (circumstance *types*, not a feasible-set density), and a **two-way subgroup** decomposition (opportunity vs effort/luck residual) that is **not** my three-way {access, ability, preference} Shapleyâ€“Shorrocks split â€” so it anchors *how to measure and bound an opportunity share* while precisely locating the gap my structural opportunity density and money-metric welfare are built to fill.
# Jacquet, Jia & Thoresen 2026 â€” How Much Does Responsibility Matter in Fairness Measurement?

> Extraction produced under `JMP_T1_exhaustive_extraction_prompt_v2.md`.
> Source of truth: the attached CESifo WP 12418 PDF. Relevance anchored to
> `JMP_project_state_v1.md` and `JMP_welfare_spec_v5.md` only.
> Three-way **access / ability / preference** vocabulary used throughout; the
> source's own two-way **preference / circumstance** language is flagged as the
> source's, not adopted.
> Tags: **explicit-in-source** / **derived-by-analogy** / **not-established**;
> uncertain metadata marked `[verify]`.

---

## 0. Metadata

- **BibTeX key:** JacquetJiaThoresen2026 `[verify exact key against your .bib]`
- **Authors:** Laurence Jacquet (CY Cergy Paris UniversitÃ© and THEMA); Zhiyang Jia (Research Department, Statistics Norway); Thor O. Thoresen (Research Department, Statistics Norway; Norwegian Fiscal Studies, Department of Economics, University of Oslo).
- **Year / outlet:** 2026, CESifo Working Papers No. 12418, January 2026.
- **DOI/URL:** SSRN `https://ssrn.com/abstract=6112587`. No journal DOI yet (working paper).
- **PDF filename:** `Jacquet_et_al_2026_How_Much_Does_Responsibility_Matter_in_Fairness_Measurement.pdf`.
- **JEL:** H31, I31, J22, C25. **Keywords:** money metric utility, fairness, tax reform, structural labor supply model.
- **Tier:** T1A (core; this is the single closest cousin of the JMP â€” same estimator family, same money-metric apparatus, overlapping author set with the companion theory paper, and Maniquet appears in the acknowledgements).
- **JMP block(s) served:** estimation; welfare; normative-interpretation; opportunity-mechanism (**access only**); motivation. **Not** decomposition (no inequality decomposition is performed); **not** ability (no structural wage technology); **not** data-infrastructure for France (Norwegian register/survey merge).

**Boundary note carried from the start.** Maniquet is thanked in the acknowledgements; this paper is **not** the companion Haydarâ€“Maniquet theory paper and must never be cited as such. It is also not the JMP. It is the empirical paper whose method the JMP most directly extends and differentiates from.

---

## 1. One-paragraph relevance to my JMP

This is the empirical template the JMP is built against and must out-position: it estimates the same **latent-jobs / "job choice" model** (Dagsvik 1994; Dagsvik and Jia 2016) on a cross-section of couples, and it produces **money-metric** welfare figures by inverting the household's own utility to money (McFadden 1999 simulation). It speaks directly to the **preference** channel (its Boxâ€“Cox utility block = my $v$) and to the **access** channel (its $\log Q(h)$ hours-availability term and the education-scaled job-availability measure $\theta_F$ = my hours/access sub-block of $g$). It does **not** instantiate my **ability** channel â€” wages are taken as observed data, not modelled as a structural wage technology â€” and it performs **no inequality decomposition**: it compares two welfare-*change* measures (standard CV vs. a preference-neutralised CVcirc, with a Conditional-Equality cross-check) and reads off *where on the income distribution* they diverge. For my purposes its single most load-bearing contribution is the **reference-preference neutralisation device** (set taste-shifters to sample medians; impose a common error term) and the demonstration that, in a Norwegian reform, neutralising preference heterogeneity barely moves the welfare distribution except at the very top. It is the paper I cite for the estimator and the money-metric inversion, and the paper I must explicitly distinguish from on four axes: **level vs. change**, **two-measure comparison vs. Shapley decomposition**, **preference-neutralising reference vs. preference-respecting equivalent income**, and **bundled circumstances vs. an access/ability split**.

---

## 2. Data and setting

- **Country / unit:** Norway; **married couples** (with or without children), treated as **unitary** (harmonised joint decision over both spouses' labour supply, common budget). **Explicit-in-source.**
- **Year / dataset:** Cross-section, **2015**. Built by merging, on personal identification numbers, the **Labour Force Survey** (Statistics Norway 2024) and the **Income and Wealth Statistics of Households** (Statistics Norway 2019). The LFS supplies actual and formal working time for main/secondary jobs plus background variables including demographic characteristics and **occupation**; conditional on participation, respondents self-classify as self-employed or employee. **Explicit-in-source.**
- **Sample size:** **1,594 couples** (Table C2). **Explicit-in-source.** Summary statistics in Table C1.
- **Sample restrictions:** couples excluded if one adult has self-employment income > NOK 115,000 (2015 prices); excluded if weekly hours > 80 or wage outside NOK [70, 600] (2015 prices). A person "works" if â‰¥ 1 hour/week. Hours = formal hours in main + second job. Nominal hourly wage = labour income / total annual hours. **Explicit-in-source.**
- **Budget-set construction:** disposable income obtained via the **LOTTE** family of tax-benefit microsimulation models (Jia et al. 2024); piecewise-linear, possibly non-convex budget sets. **Explicit-in-source.**

**Transport to my setting.** Partial. Same broad object (couples, cross-section, microsimulated nonlinear budget), so the *estimator and welfare apparatus transport cleanly*. But the **data infrastructure does not transport**: this is an admin/survey **register merge with personal IDs**, not EUROMOD on EU-SILC. **Features I do not have that they rely on:** (i) a clean **employee/self-employed** self-report (they exclude high self-employment couples on it); (ii) **occupation in the data** as a usable background variable (they have it but, note Â§3, do **not** use it in the model); (iii) precise formal-vs-actual hours from an LFS. They have **no panel, no external opportunity instrument** either â€” so on the identification axis they are in the same cross-sectional boat as my France pooled 2015â€“2017 EUROMOD sample (Â§8).

---

## 3. Model and objects (mapped object-by-object to mine)

| My object | Theirs | Match? |
|---|---|---|
| Latent-jobs choice set $\mathcal C_i$ | Latent jobs $z=1,2,\dots$ market, $z=-1,-2,\dots$ non-market; set $B(h)$ of jobs at hours $h$, size $Q(h)$ unobserved | **Same family** (explicit). Theirs is a fixed discrete **hours grid** (56 couple alternatives), not sampled draws. |
| Preference utility $v$ (Boxâ€“Cox over $c,\ell$, demographic shifters, gender) | $u(C,h_F,h_M)$, Boxâ€“Cox in consumption and leisure with leisure shifters (age, children) and a leisure interaction $\alpha_{15}$ (Eq. 4.10) | **Direct match** (explicit). Their taste-shifters = my demographic shifters. |
| Opportunity density $g$ | $\log Q_F(h_F) + \log Q_M(h_M)$ in the indirect utility (Eq. 4.3); $Q(h)=\theta\,g(h)$, $g$ the **opportunity density of hours**; $\theta$ = relative size of the job set vs. non-work | **Partial match.** Theirs is an **access/hours** density only. |
| **access** sub-block (hours/employment/region/year/occupation) | hours-availability density $g(h)$ (uniform off-peak, with **part-time and full-time peaks**) + $\theta_F$ scaled by **education**: $\log\theta_F = \gamma_{F1}+\gamma_{F2}S$ (Eq. 4.5); $\theta_M$ normalised to 1 (males â‰ˆ all employed) | **access match** (explicit). No region/year/occupation in their access block. |
| **ability** sub-block (structural wage technology: returns to education/experience, residual $\sigma$) | **Absent.** Wages are **observed data** (income/hours), entering only the budget map $C=f(\cdot)$. A reference wage appears only in the **unimplemented** CVpref (Appendix D.2) | **No match.** This is my channel, not theirs (see Â§5, Â§13). |
| occupation as access (`loc4`) | Occupation is **in the data but not in the model** â€” not in utility, not in $g$, not in the wage | **No match.** They neither use occupation nor conflate it with industry. **Not-established** that occupation does anything structural here. |
| EUROMOD disposable income $c_{ij}$ | LOTTE disposable income $C=f(h_Fw_F,h_Mw_M,I)$ | **Functional match**, different microsimulator. |

**Does any attribute enter BOTH utility and the opportunity mechanism?** **No** (explicit). Hours enter both *as an argument* ($u$ depends on $h$; $g$ is a density over $h$), but this is the standard latent-jobs separation â€” preferences value the hours, the opportunity density governs their **availability** â€” not a double-loading of a covariate. Wage enters only the budget; occupation enters nothing. No identification-by-double-entry issue arises, and none is claimed.

**Key structural reading.** Their indirect utility (Eq. 4.3) cleanly splits into a **preference part** $u(\cdot)+\eta$ and a **circumstance part** $\log Q_F+\log Q_M$. In my vocabulary the circumstance part is **access only**; their "circumstances" therefore equal my **access**, *not* my access + ability, because the wage (my ability locus) is not inside their $g$. This is the single most important mapping fact in the paper for me.

---

## 4. Estimation method

- **Estimator:** Maximum Likelihood in a **conditional logit**, choice probability Eq. 4.4. Log-likelihood Eq. 4.11: $\sum_i \log\varphi(h_{iF},h_{iM}\mid w_{iF},w_{iM},I_i)$. **Explicit.**
- **Choice set:** **fixed discrete grid** â€” 56 couple alternatives = **7 male Ã— 8 female** options (males have 7 because there is no data support for a male non-market alternative). **Not** sampled alternatives. **Explicit.**
- **Proposal / sampling density:** **none** â€” there is no sampling-of-alternatives step (see Â§4b). **Explicit.**
- **What pins preferences vs. opportunities apart:** functional form + the observed **bunching at part-time/full-time hours peaks** (which identifies the opportunity density's shape) + the joint hours density $\varphi$; $\theta_F$ identified off **education** variation (Eq. 4.5); $\theta_M$ normalised to 1; $Q_F(0)=Q_M(0)=1$ normalisation. They defer to **Dagsvik and Jia (2016)** for the formal cross-sectional identification conditions. **Explicit.**
- **Numerics / starts / multistart:** not described in detail `[verify â€” no multistart or starting-value protocol stated in the main text]`.
- **Fit:** $N=1{,}594$; log-likelihood $-3070.9$; McFadden's $\rho^2=0.52$ (Table C2). **Explicit.**

**Verdict: reusable for my RURO/JAX pipeline? Partly.** The **likelihood and the indirect-utility decomposition (Eq. 4.3â€“4.4) are directly reusable** as the conceptual backbone (my model is the same family). **Not reusable as-is:** their *estimation* uses a small fixed grid with no proposal correction; my pipeline uses **sampled alternatives with a per-row $-\log\pi$ correction** at 901 (couples) / 101 (singles) resolution. Their grid approach is the older Dagsvikâ€“Jia implementation; my sampling-plus-correction is the scaling step they do not take. Reuse the model, not the choice-set machinery.

---

## 4b. Proposal / sampling-of-alternatives correction

**Not present in estimation.** Estimation is over a **complete fixed grid** of 56 alternatives, so there is no McFadden-style sampling correction and no $-\log\pi$ term in the likelihood. The structural analogue of an "opportunity weight" is the **estimated** $\log Q(h)=\log\theta + \log g(h)$ term, but this is a *model primitive jointly estimated with preferences*, **not** a sampling instrument to be divided out. **Explicit / derived-by-analogy.**

**On the welfare side, simulation enters but not as a proposal.** CV is computed by **drawing Gumbel error terms** $\{\eta_i^k(h)\}$ and solving Eq. (D.1) numerically per draw (McFadden 1999). These are **shock draws over a common grid**, not importance draws over an individualised proposal. There is therefore **no individualised proposal** here at all â€” neither wage-conditioned nor occupation-conditioned â€” because wages are fixed data and occupation is unused. **Explicit.**

**Relation to my proposal-individualisation concern.** Direct contrast, useful for my Â§5.3 audit: my proposal is **partly individualised** (wage mean $\mu_i=X_ib+\delta_{\text{occ}}[\text{loc4}_i]$ and occupation stratum condition on $x_i$; hours/employment common). JJT have **no proposal individualisation** because their two high-dispersion channels (wage, occupation) are simply not stochastic in their model. So they cannot illuminate the well-conditioning of importance sampling â€” they don't importance-sample â€” but they **do** confirm that the *welfare* expectation, when shocks are simulated, requires a per-draw one-dimensional solve. My analytic-in-shocks log-sum (Â§6b) is the efficiency improvement over exactly their D.1 simulation.

---

## 5. Opportunity mechanism  [most important â€” split by channel]

The mechanism is a **density over hours alternatives**, scaled by an aggregate availability measure. Explicitly (Eq. 4.3â€“4.5, Appendix B):

- The latent jobs $z$ at hours $h$ form a set $B(h)$ of unobserved size $Q(h)$. Taking the max over $B(h)$ of i.i.d. Gumbel taste shocks (Appendix B derivation) yields an indirect utility shifted by $\log Q(h)$ â€” i.e. **more available jobs at $h$ â‡’ higher choice value at $h$**. This is the entire opportunity channel.
- $Q(h)=\theta\, g(h)$ with $g(h)$ the **opportunity density of hours** (share of available jobs at $h$) and $\theta$ the **size of the market opportunity set relative to non-work**. Normalisations: $Q(0)=1$.
- $g(h)$ is **uniform for nonstandard hours with a part-time peak and a full-time peak**, matching the observed hours distribution. **Explicit.**

**Mapping to my three sub-objects.**
- **access (hours / participation / job availability):** **YES, this is the whole mechanism.** Hours availability via $g(h)$ with the two peaks; aggregate participation/availability via $\theta$. Females: $\log\theta_F=\gamma_{F1}+\gamma_{F2}S$ â€” **job availability rises with education** (their interpretation). Males: $\theta_M$ **not identified**, normalised to 1 (near-universal male employment). **Explicit.**
- **ability (wage technology):** **ABSENT from the mechanism.** Wages are observed and enter only the budget. There is **no** structural return to education/experience inside $g$, and **no** residual productivity dispersion $\sigma$. The closest object is the **reference wage** $\bar w$ of the **CVpref** alternative (Appendix D.2), where they explicitly reason that "abilities predominantly result from circumstances beyond the individual's control" and so a common reference wage neutralises ability-driven inequality â€” **but CVpref is defined and then left for future research, not implemented.** So ability exists here only as an *unexecuted* neutralisation, not as an estimated channel. **Explicit (that it is deferred).**
- **occupation:** treated as **nothing** â€” observed in data, absent from the model. **No** sector/industry conflation to flag, because occupation is simply unused.

**Functional form:** opportunity density piecewise-uniform with two estimated peak parameters per gender (Table C2: male full-time 2.8936, female full-time 1.5027, male part-time âˆ’0.1512, female part-time âˆ’0.0451), plus $\theta_F=\exp(\gamma_{F1}+\gamma_{F2}S)$ with $\gamma_{F1}=-2.9199$ and $\gamma_{F2}=0.1653$ (SE 0.389 â€” **the educationâ†’availability slope is statistically insignificant**; flag this, Â§9).

**What the omission of an ability channel costs my access/ability/preference decomposition.** A great deal, and this is exactly why my paper exists. By folding all of "circumstances" into **hours/job availability** and treating wages as data, JJT **cannot separate access from ability** â€” they have only a two-way preference/circumstance cut where "circumstance" = access. My added structural wage technology (occupation-conditioned wage draws, returns to education/experience, $\sigma$) is what lets the **ability** dimension exist as a distinct, estimable channel. Cite JJT as the paper that *bundles* the opportunity side; position my ability/access split as the resolution of that bundling.

---

## 6. Welfare object â€” and its place on my $W^1$â€“$W^6$ map

**What they compute.** Three objects, all **welfare *changes* of a tax reform**, not welfare levels:
1. **CV** â€” standard compensating variation: the income that equates max utility before and after the reform under the household's **own** preferences (Eq. 4.12; McFadden 1999). Money-metric, **own-preference-respecting**, defined over the **constrained** latent-job set (it carries the $\log Q$ terms â€” Eq. 4.12 explicitly includes $\log Q_{iF}+\log Q_{iM}$). CV is **stochastic** in the $\eta$ draws.
2. **CVcirc** â€” circumstance-CV: identical computation but with the **deterministic utility $\bar u$ and the random term $\bar\eta$ set to common reference values** (taste-shifters â€” gender, age, children â€” at sample medians; $\alpha_1$â€“$\alpha_4$ common), so "households differ only in circumstances" (Eq. 4.13, Appendix D.2). **Preference heterogeneity is neutralised.**
3. **$\Delta$CE** â€” change in the **Conditional Equality** criterion (Fleurbaey 2008): max **reference-preference** utility on a **hypothetical linear equivalent budget** (slope = wage, lump-sum tax $T$ as intercept), Eq. 3.2â€“3.3, following Carpantier and Sapata (2016); $\Delta\text{CE}=\text{CE}_1-\text{CE}_0$. Reference preferences again at medians.

**Discrete-choice subtleties handled:** CV is the **conditional indirect utility of the most-preferred job within the latent set** (so it is a *constrained-choice* CV); the $\eta$ terms are held fixed pre/post (the standard McFadden assumption), and because the pre- and post-maxima need not fall on the same alternative, CV does **not** collapse to a closed form and is obtained by simulation. **Ex-post element:** for CE they "do not exploit information about actual choices" â€” they draw shocks and assume the household picks the utility-maximising alternative â€” so the CE construction is itself an **ex-ante-by-simulation** object over the grid, though it conditions the equivalent budget on the household's own wage. **Explicit.**

**Locating the paper on my $W^1$â€“$W^6$ map.** Handle with care; the correspondence is **partial and derived-by-analogy**, and the level/change mismatch means *none of these is literally a $W^k$*.
- **Standard CV** respects own preferences **and** own circumstances (own wage, own $Q$) â€” "own everything." Its *stance* is closest to my **Full-Responsibility** corner ($W^2/W^3$): nothing is neutralised. **Derived-by-analogy**, with the caveat that it is a *change* and that all my $W^k$ read attained $V_i$ whereas CV reads a utility *difference*.
- **CVcirc / CE** neutralise **preferences** (set to a reference), leaving circumstances individual. This does **not** map to any single $W^k$, because my family holds **preferences as the responsibility object across all six** and varies *which circumstance dimension* (Ind-$y$ / pay vs. Ind-$A$ / set) is compensated. CVcirc varies the *preference* axis, which my menu does **not** traverse. The honest statement: **CVcirc/CE belong to the reference-preference / Conditional-Equality tradition, which is a different normative device from my preference-respecting equivalent-income family.** My $W^k$ use the household's **own** indifference map; CVcirc/CE substitute a **common reference** map. (`JMP_welfare_spec_v5.md` Â§1.1 is explicit that my $W^k$ invert the *own*-utility map "never by a closed-form shortcut that would bypass the household's preferences" â€” the exact opposite design choice from CVcirc.)
- **CVpref** (their unimplemented dual, Appendix D.2) neutralises **circumstances** instead (reference wage $\bar w$, reference opportunity $\bar Q$). *This* is the object whose **stance** is nearest my compensation corner / my $W^5$ (compensate the set; with reference wage, also compensate pay). But it is **not-established empirically** â€” defined, deferred, never computed.

**Verdict:** the **estimator and the CV inversion are directly adaptable**; the **CVcirc/CE objects are conceptually adjacent but normatively distinct** from my family (reference-preference vs. preference-respecting) and are **changes not levels**; treat them as the *contrast case*, not as instances of $W^1$â€“$W^6$.

---

## 6b. Inclusive value and money-metric inversion

- **Inclusive value:** Yes, partially and analytically â€” the $\log Q(h)$ terms in Eq. 4.3 are precisely the **expected-maximum (log-sum) over the latent jobs at a given hours point**, derived in Appendix B from the Gumbel max. So the inclusive value *within* an hours cell is closed-form. **Explicit.**
- **But welfare is obtained by simulation, not by a closed-form log-sum.** Because CV is **nonlinear in income**, no closed form exists (they cite Dagsvik and KarlstrÃ¶m 2005 for the distribution/moments); they **draw $K$ Gumbel vectors and solve a one-dimensional equation per draw** (Eq. D.1), then average. **Explicit.**
- **Money-metric inversion:** Yes â€” CV is a **one-dimensional solve** that equates pre- and post-reform maximised utility under own preferences (Eq. D.1); CE solves for the lump-sum tax $T$ (Eq. 3.2). Both are own-/reference-utility inversions to a money figure, **not** closed-form shortcuts that bypass preferences. **Explicit.**
- **Expectation over shocks: by simulation**, not analytic. **Explicit.**

**Relation to my integrator.** This is the cleanest single point of methodological differentiation. My welfare layer takes the **expectation over the extreme-value shocks analytically** (the ex-ante inclusive value is the closed-form expected maximum; `JMP_welfare_spec_v5.md` Â§1.1: "the welfare layer requires no shock draws and no simulated argmax"), and inverts by a one-dimensional bracketing root-solve on the **importance-sampled** log-sum. JJT do the inversion by **per-draw simulation over a fixed grid**. Same money-metric inversion logic; **my analytic-in-shocks + importance-sampling step is the efficiency and the ex-ante-access improvement over their D.1 simulation.** Cite D.1 as the simulation baseline I improve on.

---

## 7. Inequality / decomposition content  [three-way where relevant]

**There is no inequality index and no decomposition in this paper.** No Gini/MLD/Theil/Atkinson; no Shapley, Shorrocks, factor-component, subgroup, RIF, or Owen-grouped decomposition. **Explicit (by absence).**

What they do instead:
- Report **means and standard deviations** of the three welfare-change measures (Table 1): the SD is the only dispersion object, used informally to say preference-neutralisation "slightly reduces the spread" (5,458 â†’ 5,188 NOK under CV â†’ CVcirc).
- Report a **rank-transition matrix** across quintiles, CV vs. CVcirc (Table 2): 71â€“93% stay in the same quintile.
- Plot welfare effects **by income decile** (Figures 4â€“5) and identify the decile where CV and CVcirc diverge.

The conceptual cut is **two-way** and, in the source's own words, **preference vs. circumstance** â€” and it is operationalised as a **comparison of two measures**, not as an additive attribution. The "amount that responsibility matters" is *defined* as the gap between CV and CVcirc, not as a component share.

**Verdict: not reusable as a decomposition method.** To serve my **three-way access / ability / preference Shapleyâ€“Shorrocks** split (anchored on $W^3$ for total source-composition and the $W^5$/$W^1$ duals for the access/ability faces) it would need three extensions, each substantial: **(i)** move the object from welfare **change** to welfare **level**; **(ii)** replace the two-measure gap with a genuine **order-independent additive decomposition** of an inequality index; **(iii)** **split circumstances into access and ability**, which their model cannot do because ability (wages) is not a modelled channel. The paper is the *motivation* for a decomposition ("how much does responsibility/preference matter") executed by a cruder instrument; my decomposition is the instrument it lacks.

---

## 8. Identification and the separation of preferences from opportunities  [strict]

**What separates tastes from constraints.** The split rests entirely on **functional form + distributional assumptions + the shape of the observed hours distribution**:
- Preferences enter through the Boxâ€“Cox $u(\cdot)$ and its taste-shifters; constraints enter **only** through $\log Q(h)$. The two are separately identified because the opportunity density is pinned to the **bunching at part-time and full-time peaks** (a feature preferences alone, on a smooth Boxâ€“Cox, would not generate), while the smooth trade-off identifies tastes.
- $\theta_F$'s level and education slope are identified off cross-sectional **education** variation (Eq. 4.5); $\theta_M$ is **conceded non-identified** and normalised (a candid admission worth citing).
- They defer the formal conditions to **Dagsvik and Jia (2016)**: latent-jobs identification from **cross-sectional micro data** under the Gumbel/Luce structure. **Explicit.**

**Can they separate ability from access?** **No.** Within "circumstance" there is only access (hours/job availability); wages are data, so there is no ability sub-model to identify. The would-be ability neutralisation (CVpref reference wage) is deferred. **Explicit / not-established.**

**Transport to my France pooled cross-section.** **Yes, and this is the backbone of my identification defence.** JJT identify the preference/opportunity separation **without a panel and without an external instrument** â€” exactly my constraint â€” relying on parametric/functional-form identification plus the observed hours distribution. This is precisely the structure my baseline uses, and my baseline is additionally **certified by synthetic recovery** rather than in-sample fit. So I can write: *the separation of preferences from opportunities in a cross-section is established practice in this literature (Dagsvikâ€“Jia 2016; Jacquetâ€“Jiaâ€“Thoresen 2026); my contribution is (a) to push it to a three-way access/ability/preference split by adding a structural wage channel, and (b) to discipline the resulting specification by a synthetic-recovery gate rather than in-sample fit.* This is also my answer to the "your decomposition is mechanical" referee: the *same* parametric identification underwrites a published, peer-relevant CV/CVcirc exercise; what is new in mine is the channel split and the recovery certification, not the act of separating tastes from constraints in a cross-section. **Do not soften: the identification is parametric, and I should own that rather than overclaim nonparametric content.**

---

## 9. Key results and magnitudes

- **Average welfare effects (Table 1):** CV = **NOK 18,384** (SD 5,458); CVcirc = **NOK 18,677** (SD 5,188); $\Delta$CE = **0.356** (SD 0.108, different unit/scale). Neutralising preferences **raises** the mean slightly and **lowers** the SD by ~5%. **Explicit.**
- **Rank stability (Table 2):** 71â€“93% of households stay in the same income quintile across CV vs. CVcirc; bottom and top quintiles most stable (84.9% and 92.5%). **Explicit.**
- **Across the distribution (Figure 4):** CV and CVcirc track each other up through decile 9 (~NOK 25,000 gain at decile 9, where disposable income â‰ˆ NOK 1 million), then **drop in decile 10**; **decile 10 is the only group where the two diverge significantly.** **Explicit.**
- **Mechanism:** under CVcirc, women who initially had stronger leisure preferences are assigned **lower returns to leisure**, so **female labour supply rises across the distribution**; male labour supply is unchanged except in the top decile, where it **falls**. The top-decile welfare divergence is driven by **women's** re-optimised labour supply, where pre-reform female hours were low. **Explicit.**
- **$\Delta$CE robustness (Figure 5):** $\Delta$CE closely mirrors CVcirc across deciles 1â€“9; mild divergence at the top (smaller gains), interpreted as methodological noise. **Explicit.**
- **Estimation (Table C2):** $N=1{,}594$; logL $-3070.9$; $\rho^2=0.52$; consumption exponent $\alpha_1=0.6694$; female leisure exponent $\alpha_3=-1.1490$; male leisure exponent $\alpha_4=0.2309$ (SE 0.308 â€” **imprecise**); leisure interaction $\alpha_{15}=1.2111$ (SE 0.863 â€” **imprecise**); $\gamma_{F2}=0.1653$ (SE 0.389 â€” **educationâ†’availability insignificant**). **Explicit.**

**Benchmark for my plausibility checks.** The headline economic message â€” **neutralising preference heterogeneity barely changes the welfare distribution except at the very top** â€” is a (weak, change-based, single-reform, Norway) prior that the **preference channel contributes modestly** to welfare-effect dispersion, with action concentrated among high-income women's labour supply. If my France **level** decomposition returns a small preference component and a larger opportunity component overall, JJT is consistent corroboration; but it is a *change* in a different country, so it bounds plausibility only loosely. Their ~5% SD reduction from full preference-neutralisation is the closest single number to compare against my preference component â€” note that mine should be **larger in principle** because I decompose a *level* and split out *access*, but do not assert this until computed.

---

## 10. Estimators, theorems, or formal results

No theorems. Key formal objects (LaTeX near-verbatim; **explicit**), with reuse verdicts:

1. **Indirect utility with opportunity terms (Eq. 4.3):**
$$V(h_F,h_M,I)=u\big(f(h_Fw_F,h_Mw_M,I),h_F,h_M\big)+\log Q_F(h_F)+\log Q_M(h_M)+\eta_{h_F,h_M}.$$
*Technique:* max of i.i.d. Gumbel over $B(h)$ â‡’ a $\log Q$ shift, $\eta$ retains Gumbel (Appendix B). **Reuse: yes** â€” this is my model's core identity.

2. **Choice probability (Eq. 4.4):**
$$\varphi(h_F,h_M)=\frac{Q_F(h_F)Q_M(h_M)\exp\big(u(f(\cdot),h_F,h_M)\big)}{\sum_{x,y}Q_F(x)Q_M(y)\exp\big(u(f(\cdot),x,y)\big)}.$$
**Reuse: yes** as the likelihood kernel; my version replaces the full-grid sum with a sampled-alternatives sum plus $-\log\pi$.

3. **Opportunity scaling (Eq. 4.5):** $\log\theta_F=\gamma_{F1}+\gamma_{F2}S$. **Reuse: maybe** â€” an education-as-access shifter; relevant to my Â§6.3 "education-as-access" deferred robustness cut, but note its insignificance here.

4. **Boxâ€“Cox utility (Eq. 4.10)** in $(C-C_0)$ and leisure $L_F,L_M$ with a leisure interaction $\alpha_{15}$ and demographic shifters in $\beta_F,\beta_M$. **Reuse: yes** as a specification template (my preference block is the same family).

5. **CV definition (Eq. 4.12)** and **CVcirc (Eq. 4.13):** constrained-choice CV with $\log Q$ terms; CVcirc replaces $u_i,\eta_i$ by common $\bar u,\bar\eta$. **Reuse: yes as templates**, but for *changes*; my levels need the reference-package inversion, not a pre/post-reform difference.

6. **CE (Eq. 3.2â€“3.3):** lump-sum tax $T_i$ implicitly defined by $u(c_i,h_i;\gamma_i)=\max_h\{u(c,h;\gamma_i)\mid c\le w_ih-T_i\}$; then $\text{CE}_i=\max_h\{\bar u(c,h;\bar\gamma)\mid c\le w_ih-T_i\}$. **Reuse: maybe** â€” relevant to my secondary "ex-post chosen-alternative CE" cross-check (`JMP_welfare_spec_v5.md` D3), but their CE uses reference preferences whereas my correction-free CE cross-check is own-preference.

7. **CV simulation (Eq. D.1)** â€” per-draw one-dimensional solve over $\eta$. **Reuse: as the contrast** my analytic-in-shocks integrator replaces (Â§6b).

**Discrepancy to flag (`[verify]`).** The subsistence consumption $C_0$ is stated as **NOK 64,000** in the Â§4.2.3 text but **57,000** in Table C2; $L_0=5{,}110$ hours is consistent across both. Treat $C_0$ as `[verify]` before quoting a number.

---

## 11. Robustness and specification sensitivity

- **Reference-value sensitivity:** medians of taste-shifters replaced by **10th/90th-percentile** values â€” results "remain robust." **Explicit.** (Directly relevant to my reference-state robustness in the decomposition.)
- **CV aggregation:** two routes â€” per-individual mean across draws (their choice) vs. pooling all draws across observationally identical groups; they use the former. **Explicit.**
- **Choice-set size:** fixed at 56; **not varied.** No effective-sample-size / draw-count study (because estimation is not simulation-based). **Number of welfare draws $K$ not stated `[verify]`.**
- **Ability/access boundary:** **not stress-tested** â€” there is no ability channel; the CVpref reference-wage neutralisation that would probe it is **deferred to future research.** **Explicit.**

**What this tells me to stress-test.** (i) My reference-state choice (their 10th/90th-percentile check is the template I should replicate across measures). (ii) My **draw-count / ESS stability** â€” JJT give me *no* guidance here (they don't importance-sample), which underscores that my Â§6 welfare-integration gate and the ESS diagnostic are genuinely my own contribution, not borrowed. (iii) The **ability/access boundary** is exactly the axis they could not test; my education-as-access vs. ability re-allocation (`JMP_project_state_v1.md` Â§6.3) is the test they flagged-by-omission.

---

## 12. What I can cite this paper for

- The **latent-jobs / "job choice" model** as the vehicle that "intrinsically" separates preferences (tastes over leisure) from circumstances (job opportunities) (Dagsvik 1994; Dagsvik and Jia 2016), and that the opportunity term is $\log Q(h)$ entering indirect utility additively (Eq. 4.3).
- The **bunching-at-peaks** empirical justification for an opportunity density (most jobs offer full-time or part-time schedules).
- The **reference-preference neutralisation device**: set taste-modifying variables to sample medians and impose a common error term to construct a preference-neutralised welfare measure (CVcirc).
- The **McFadden (1999) simulation** for CV in discrete-choice models nonlinear in income, and the **constrained-choice** reading of CV (it carries $\log Q$).
- The **link between a reference-preference CV and the Conditional Equality criterion** (Fleurbaey 2008; Carpantier and Sapata 2016), and that the two deliver "remarkably close" distributions empirically.
- The **unitary-couples** joint-choice assumption over $(h_F,h_M)$ as standard in this literature.
- The empirical finding (Norway, bracket-tax reform) that **preference heterogeneity matters little for the welfare distribution except at the top**.
- The candid **non-identification of $\theta_M$** and its normalisation, as precedent for honest normalisation choices.
- Money-metric utility's "revival" in the fair-allocation literature, with their cite chain (Fleurbaey 2008; Fleurbaey and Maniquet 2011, 2018; Bosmansâ€“Decancqâ€“Ooghe 2018; Schleeâ€“Khan 2022) as a ready-made positioning paragraph.

---

## 13. What I should NOT cite this paper for  [overclaim risks]

- **Not** a three-way decomposition. It is a **two-measure comparison** along a **preference / circumstance** axis, and not even a formal additive decomposition. Never imply it decomposes inequality into access/ability/preference shares.
- **Not** a welfare **level** object. Everything here is a **welfare *change*** (CV of a tax reform). Do not present CV/CVcirc/$\Delta$CE as instances of my level equivalent-income family, and do not read their "spread reduction" as a level inequality result.
- **Not** an **access/ability** split. "Circumstance" here = **access (hours/job availability) only**; wages are data, ability is unmodelled, CVpref is deferred. Do not attribute a separate ability channel to this paper.
- **Not** an **occupation-as-access** result. Occupation is in the data but **unused** in the model. Do not cite for `loc4`/occupation opportunity, and do not say they "use occupation."
- **No industry/sector** content at all â€” so there is no sector/occupation conflation to inherit, but equally nothing to cite on industry.
- **Reference-preference â‰  preference-respecting.** CVcirc/CE substitute a **common reference** indifference map; my $W^1$â€“$W^6$ use the household's **own** map. Do not equate CVcirc with a preference-respecting equivalent income, and do not claim this paper computes my family.
- **Random-vs-deterministic:** the latent jobs are **latent** (count $Q(h)$ unobserved) but the opportunity sizes are **deterministic parameters**; the randomness is in the **taste shocks** $\eta$. This is **consistent** with my deterministic-opportunities stance â€” so cite it to *support* that framing, but do **not** describe their opportunities as "random."
- **Theory-paper boundary:** Maniquet is acknowledged, but this paper proves no axioms and characterises no welfare family. Never attribute the Haydarâ€“Maniquet axioms/characterisation to it, and never read it (or my JMP) as a theory contribution.
- **McFadden (1999)** is used here for **welfare simulation**, not for **sampling-of-alternatives in estimation**. Do not cite it via this paper as a sampling correction.

---

## 14. Direct quotes worth citing

Deliberately minimal; verify each against the PDF before use. Page numbers are the printed paper pages.

- On the model's central virtue (p. 1): the job choice model holds features that *"mirror the distinction between preferences and circumstances."*
- On the definition of when responsibility matters (p. 1): *"Responsibility matters whenever the two metrics display different values."*
- On the structural split of indirect utility (p. 10): the opportunity part *"represents the labor market opportunities facing the household."*
- On the headline empirical result (p. 19, summarising): preferences may *"not matter so much in fairness measurement, except at the very top."*

(If more quotation is needed, pull it directly from the PDF rather than from this file â€” I am keeping verbatim text minimal here on purpose.)

---

## 15. Open questions and risks for my draft

- **Simulation vs. analytic integration error.** Their CV is simulated over $K$ Gumbel draws with no stated $K$ or convergence diagnostic (`[verify]`). My analytic-in-shocks + ESS-gated importance sampling is the disciplined alternative â€” but it means *I* carry the burden of demonstrating integration adequacy (the Â§6 three-part gate), since this literature offers no off-the-shelf standard. Frame my ESS diagnostic as filling that gap.
- **Normative basis of the reference.** "Median preferences as the responsibility reference" is asserted, not derived; their 10th/90th-percentile robustness is reassuring but does not address *why* the median. My family-of-measures design sidesteps this by reporting a *spectrum* rather than committing to one reference â€” a defensible positioning move against the "arbitrary reference" critique.
- **Bundled circumstances.** Their inability to separate access from ability is the gap my paper fills, but it also warns me: **is the structural wage technology separately identified from preferences in a cross-section?** JJT avoid the question by not modelling wages; I cannot. This is the sharpest identification risk for my ability channel and must be defended (synthetic recovery of the wage block, not in-sample fit â€” consistent with my certification discipline).
- **External validity of "responsibility matters only at the top."** Reform-specific and Norway-specific (individual taxation, dual income tax). My France level decomposition need not replicate it; do not anchor expectations to it.
- **Change vs. level confusion is a live referee risk.** Because JJT is my nearest neighbour and is a *change* paper, a reader may assume my decomposition is also reform-based. The intro must state the level/change distinction early and explicitly.

---

## 16. TL;DR for retrieval

Jacquetâ€“Jiaâ€“Thoresen (2026) estimate the **same latent-jobs "job choice" model** (Dagsvikâ€“Jia) on 1,594 Norwegian couples and compute **money-metric welfare *changes*** of a bracket-tax reform â€” standard CV vs. a **preference-neutralised CVcirc** (taste-shifters at medians) plus a Conditional-Equality cross-check â€” finding preferences barely move the welfare distribution except in the top decile. For my JMP it is the **estimator-and-inversion template** and the source of the **reference-preference device**, speaking to my **preference** and **access** channels but offering **no ability channel** (wages are data; CVpref is deferred) and **no inequality decomposition** (a two-measure comparison, not a Shapley split). It is the paper I cite for cross-sectional preference/opportunity identification and money-metric CV, and the paper I must distinguish from on **level-vs-change**, **decomposition-vs-comparison**, **preference-respecting-vs-reference-preference**, and **access/ability split vs. bundled circumstance**.
# Shorrocks 1982 â€” Inequality Decomposition by Factor Components

## 0. Metadata
- **BibTeX key (suggested):** `shorrocks1982decomposition`
- **Author:** A. F. Shorrocks (London School of Economics; Queen's University)
- **Year:** 1982
- **Outlet:** *Econometrica*, Vol. 50, No. 1 (January 1982), pp. 193â€“211
- **URL:** JSTOR stable URL `https://www.jstor.org/stable/1912537` (explicit on PDF). DOI `10.2307/1912537` [verify â€” not printed on PDF]
- **PDF filename:** `Shorrocks_1982_Inequality_Decomposition_by_Factor_Components.pdf`
- **Tier:** T1A
- **JMP block(s) served:** **decomposition** (primary); **normative-interpretation** (the two "contribution" readings of Â§5, which formalise the counterfactual-neutralisation idea); **motivation** (foundational citation for additive factor decomposition). It does **not** serve estimation, identification, welfare, or opportunity-mechanism (access/ability) â€” the paper contains no choice model, no welfare object, and no opportunity structure.

## 1. One-paragraph relevance to my JMP
This is the foundational reference for **additive decomposition of an inequality index into the contributions of distinct components**, and it supplies the axiomatic backbone for the claim that a decomposition can be made *unique* and *index-independent*. It speaks to **Exercise B (the source decomposition)** rather than to any single channel: it is about *how* to allocate inequality to components, not about *which* components (access / ability / preference) are the right ones. Its central cautionary result â€” that without the right symmetry axioms the proportional contribution of a component can be driven to *any* value in $(-\infty,\infty)$ (the three-person example, eq. 30) â€” is precisely the "your decomposition is mechanical / arbitrary" referee threat my Â§8 must pre-empt, and it is the reason my decomposition must be pinned by exhaustiveness/order-independence axioms (Shapleyâ€“Shorrocks) rather than by a "natural" formula. **Crucial boundary:** the rule Shorrocks derives (cov$(Y^k,Y)/\sigma^2(Y)$) applies to **additive income sources** $Y=\sum_k Y^k$; my access/ability/preference channels are **not** additive money components but counterfactual neutralisations of structural blocks, so the cov-rule does **not** transport directly â€” the Shapley-value machinery (Shorrocks 2013) is the correct tool, and this 1982 paper is the additive special case / conceptual ancestor.

## 2. Data and setting
**N/A â€” no data, no empirical application, no country/year.** This is a purely methodological/theoretical paper in the theory of inequality measurement. Populations appear only as abstract income vectors $Y=(Y_1,\dots,Y_n)$ and as illustrative hypotheticals (notably a three-person population in the eq. 30 example). Income "sources" are abstract factor components $Y^k$ (the running examples named are earnings, investment income, and transfer payments). There is **no** budget-set construction, **no** microdata, **no** panel, **no** instrument, **no** vacancy/offer data. Nothing here transports as *setting* to my France pooled 2015â€“2017 EUROMOD cross-section; what transports is the **decomposition theory**, which is setting-free.

## 3. Model and objects (map object-by-object to mine)
There is **no structural/behavioural model** to map â€” no choice set, no deterministic utility $v$, no opportunity density $g$, no budget map. The single object is a partition of total income into factor components and an inequality index $I(Y)$.
- **Their factor components $Y^k$** vs **my channels:** their $Y^k$ are *additive* sub-vectors summing to total income, $Y=\sum_k Y^k$ (the decomposition is defined for "disjoint and exhaustive components of income," explicit-in-source, Â§3). My {access, ability, preference} are **not** additive income sub-vectors; they are structural blocks of the model whose effect on welfare inequality is isolated by *equalisation/neutralisation counterfactuals*, not by summing money pieces. **This is the single most important object-level mismatch** and the basis for several boundary flags below.
- **Their total $Y$** vs **my welfare vector $\Omega^k$:** their decomposed aggregate is the *income* distribution; my decomposed aggregate is a *money-metric equivalent-income* distribution $\Omega^k$ computed from attained utility $V_i$. Shorrocks's aggregate is observed income; mine is a constructed welfare object â€” so even the thing being decomposed differs in kind.
- **Opportunity / availability mechanism:** none. (Detailed in Â§5 below.)
- **Budget map = my EUROMOD disposable income?** No budget map at all.
- **Job attribute entering BOTH utility and opportunity?** N/A â€” no utility and no opportunity object exist here, so the double-counting flag does not arise. The analogue concern in *this* paper is whether components are disjoint and exhaustive (they are required to be).

## 4. Estimation method
**N/A.** No likelihood, no estimator, no choice-set construction, no numerical optimisation, no starting values. The paper derives decomposition *rules* (closed-form allocations of an index to components), not estimates. **Verdict: not reusable as an estimation method** (there is none); reusable only as the *decomposition* layer (see Â§7, Â§10).

## 4b. Proposal / sampling-of-alternatives correction
**N/A.** No alternatives are sampled; no proposal density; no $\log(\text{prior})$ correction. The paper has no choice-theoretic content whatsoever. Nothing here bears on my importance-sampling welfare integrator or my proposal-individualisation concern.

## 5. Opportunity mechanism  [MOST IMPORTANT â€” here: explicitly absent]
**There is no opportunity mechanism, by construction.** The paper takes the *realised* distributions of factor incomes $\{Y^k\}$ as given primitives and asks only how to allocate the inequality of their sum. There is no feasibility, no availability, no offer probability, no reservation wage, no participation restriction, and no dependence on circumstances (region, education, demographic type, local labour market).
- **access:** not modelled.
- **ability:** not modelled.
- **occupation as availability:** not modelled; no occupation object, hence **no risk of occupation/industry conflation** in this source.

Shorrocks himself flags the cost of this omission in his own terms (Â§5, concluding remarks, explicit-in-source): factor decomposition examines each component *separately* and **neglects feedback effects** on other sources (his example: a tax decomposition identifies the contribution of taxes to post-tax inequality but ignores taxes' effect on the *pre-tax* distribution). He states that evaluating such indirect effects would require specifying behavioural relationships, which factor decompositions deliberately avoid â€” and he calls this "both the strength and weakness" of the approach.

**What this omission costs my access/ability/preference decomposition (derived-by-analogy):** because Shorrocks's rule is purely statistical and behaviour-free, applying an *additive-component* logic to my channels would silently assume the channels are non-interacting additive money pieces with no general-equilibrium/behavioural feedback. My channels are behaviourally entangled (neutralising access changes attained utility and hence the chosen bundle, which is exactly a "feedback effect" Shorrocks excludes). This is the formal reason my decomposition needs the Shapley counterfactual construction (which handles interactions by symmetric averaging over orderings) rather than the 1982 covariance rule.

## 6. Welfare object â€” and its place on my $W^1$â€“$W^6$ map
**The paper computes no welfare object.** No money-metric, no equivalent income, no compensating/equivalent variation, no log-sum/inclusive value. It operates entirely on income distributions and inequality indices. There is **no** reference price, reference preference, reference bundle, or reference set, and no ex-ante/ex-post distinction (there is no choice and no uncertainty).

**Place on my $W^1$â€“$W^6$ map: none â€” do not claim this source contains $W^1$â€“$W^6$ or any Independence-of-$\mathbf{y}$ / Independence-of-$A$ stance.** It is index-and-component theory upstream of the welfare object. The one genuine point of contact is conceptual and lives in Â§5: Shorrocks's two interpretations of "the contribution of factor $k$" (below, Â§7) formalise the *neutralisation counterfactual* that my decomposition uses to isolate a channel â€” but this is a decomposition-construction idea, not a welfare measure. **Verdict: incompatible as a welfare object; usable only at the decomposition layer.**

## 6b. Inclusive value and money-metric inversion
**N/A.** No inclusive value, no log-sum, no EV/CV, no money-metric inversion, no expectation over shocks (analytic or simulated). The paper has no discrete-choice or random-utility content.

## 7. Inequality / decomposition content  [CORE OF THIS PAPER]
This is the section the paper exists for. All of the following is **explicit-in-source**.

**Indices covered.** Variance $\sigma^2$; squared coefficient of variation $I_2$; Gini $G$; the Generalized Entropy family $I_c$ (eq. 19), including Theil $I_1$ and $I_0$; and â€” via the weak-consistency extension of Â§4 â€” the Atkinson family.

**Decomposition family and the "natural" rule.** For additive components $Y=\sum_k Y^k$, the *natural* decomposition assigns to factor $k$ its own variance plus **half** of every interaction (covariance) term involving it, giving the contribution
$$ S_k^*(\sigma^2) \;=\; \mathrm{cov}(Y^k,\,Y), \qquad s_k^*(\sigma^2)=\frac{\mathrm{cov}(Y^k,Y)}{\sigma^2(Y)} $$
(eqs. 3â€“4). The same proportional contributions arise for $I_2$ (eqs. 6â€“7); a separate "natural" rule (the pseudo-Gini, eqs. 10â€“11) is given for the Gini and a pseudo-Theil for $I_1$ (eqs. 20â€“21).

**The non-uniqueness warning (the load-bearing result for my defence).** Theorem 1 (eqs. 13â€“14) shows that any index written in the quasi-separable weighted-sum form $I(Y)=\sum_i a_i(Y)Y_i$ admits a contribution $S(Y^k,Y)=\sum_i a_i(Y)Y_i^k$ â€” but the weights $a_i(Y)$ are **not unique**. Corollary 1 (eq. 27) characterises the *entire family* of admissible rules via arbitrary functions $\lambda_j(Y)$, and eq. 28 shows the proportional contributions can be made to match those of *any other* index. The three-person illustration (eq. 30) is the punchline: by choosing $\lambda_1$ freely, the proportional contribution of a factor "can be made to give any value between plus and minus infinity" â€” i.e. an unaxiomatised decomposition is empirically meaningless.

**The uniqueness theorem.** Adding **Assumption 6 (Two-Factor Symmetry)** to Assumptions 1â€“5 yields **Theorem 3 (eq. 31): a unique rule for every inequality index**,
$$ s_k(I)\;=\;\frac{S(Y^k,Y)}{I(Y)}\;=\;\frac{\mathrm{cov}(Y^k,Y)}{\sigma^2(Y)} \quad\text{for all } Y\neq\mu e, $$
with two consequences stated explicitly: (i) the decomposition rule is unique, and (ii) the *proportional* contributions are **independent of the inequality index chosen** (they coincide with the natural decomposition of the variance / $I_2$).

**Weakly consistent decompositions (Â§4).** Replacing additive consistency (Assumption 4) with a weaker aggregator condition (Assumption 4â€²) and invoking AczÃ©l's theorem gives Theorem 4: there is a monotonic transform $f$ (unique up to scale) such that transformed contributions sum to the transformed index. This extends the framework to indices that are monotonic transforms of the quasi-separable form, **including the Atkinson family** ($f(y)=(1-y)^{1-\varepsilon}$). Under a non-additive aggregator the *proportional* contributions need no longer sum to one or be index-invariant.

**Counterfactual construction (the two interpretations, Â§5 â€” directly relevant to my channel neutralisation).** Shorrocks formalises "the contribution of factor $k$" two ways:
- **(A) "pure" contribution** â€” inequality if factor $k$ were the *only* source of differences: $C_k^A = I\!\big(Y^k+(\mu-\mu_k)e\big)$ (eq. 39): hold $Y^k$, give everyone the *mean* of every other source.
- **(B) "eliminated" contribution** â€” the fall in inequality if factor $k$ differences were *removed*: $C_k^B = I(Y) - I\!\big(Y-Y^k+\mu_k e\big)$ (eq. 40): replace each $Y_i^k$ by its mean.

For the variance, the unique rule sits exactly between them: $S(Y^k,Y)=\mathrm{cov}(Y^k,Y)=\tfrac12(C_k^A+C_k^B)$. **(A) zeroes out all other sources; (B) zeroes out the target source** â€” and (B) is the formal sibling of my "equalise this channel and read the inequality fall" counterfactual. Shorrocks notes (A) ignores interactions while (B) loads *all* of factor $k$'s interactions onto $k$, and that in general neither $C^A$ nor $C^B$ alone yields a *consistent* (summing) decomposition except when components are uncorrelated.

**Verdict for my three-way Shapleyâ€“Shorrocks split (anchored on $W^3$/$W^5$/$W^1$).** **Reusable as foundational principle, not as formula.** Three transfers, one non-transfer:
1. **Transfers:** the *consistency/exhaustiveness* requirement (Assumption 4) and the *index-independence* property (Theorem 3) are exactly the disciplines I want â€” they justify (a) requiring my Shapley components to sum to $I(\Omega^k)$ and (b) reporting across Gini/Theil/Atkinson without re-qualifying every number.
2. **Transfer:** interpretation (B) (eq. 40) is the additive-world version of my channel-equalisation counterfactual.
3. **Transfer (as warning):** the eq. 30 $(-\infty,\infty)$ result is the citation that *motivates* axiomatic pinning of any decomposition.
4. **Does NOT transfer:** the closed-form rule $\mathrm{cov}(Y^k,Y)/\sigma^2(Y)$ itself, because (i) my channels are **not** additive income components, and (ii) the asymmetry between (A) and (B) when components interact is exactly what the **Shapley average over all orderings** resolves â€” which is the 2013 development, **not** present in this 1982 paper.

**This paper is a $K$-factor additive (income-source) decomposition.** It is neither a two-way opportunity/preference split nor a three-way access/ability/preference split, and it is **not** a Shapley-value paper. Extending it to my three channels requires (a) reconceiving the "components" as structural-block neutralisations and (b) replacing the half-the-covariance interaction split with the Shapley symmetric-orderings average.

## 8. Identification and the separation of preferences from opportunities  [STRICT]
**N/A in the structural-econometric sense** â€” there is no estimation, no tastes-vs-constraints identification problem, and nothing here addresses separating *ability* from *access*. The paper's "identification" is purely about *which allocation rule* is pinned down by which axioms, an algebraic question.

**Why it nonetheless belongs in my identification/defence note (derived-by-analogy, state as such):** the eq. 30 result is the cleanest existing statement that a decomposition with too few axioms is *not identified as a number* â€” its proportional contribution ranges over the whole real line. This is the formal precedent I cite when a referee charges that the access/ability/preference split is "mechanical" or "arbitrary": the answer is that the split is pinned by exhaustiveness + order-independence (Shapleyâ€“Shorrocks), exactly the kind of axiomatic discipline Shorrocks (1982) shows is *necessary* to obtain a unique, interpretable decomposition. **It does not, however, solve my structural identification** (preferences vs opportunities, or ability vs access) â€” that must come from functional form, the certified synthetic-recovery argument, and the opportunity-density structure, none of which this paper touches. Do not let this citation be read as identifying the *channels*; it only disciplines the *allocation* once channels are defined.

## 9. Key results and magnitudes
No empirical magnitudes (no data). The "results" are the theorems. The one quantitative illustration worth carrying is the **three-person example (eq. 30)**: with the Gini and a freely chosen $\lambda_1$, the proportional factor contribution spans the entire interval $(-\infty,\infty)$ â€” a qualitative "magnitude" that benchmarks *how badly* an unaxiomatised decomposition can behave, not any substantive share. Nothing here benchmarks the plausible size of my own opportunity share or welfare spread.

## 10. Estimators, theorems, or formal results
- **Theorem 1 (eqs. 13â€“14).** *Statement:* Assumptions 2â€“4 imply $S(Y^k,Y)=a(Y)\!\cdot\!Y^k=\sum_i a_i(Y)Y_i^k$ with $I(Y)=a(Y)\!\cdot\!Y$. *Assumptions:* continuity + symmetric treatment of factors (A2), independence of level of disaggregation (A3), consistent (additive) decomposition (A4). *Technique:* the additivity of A4 forces a Cauchy functional equation in the contribution map; its solution (AczÃ©l) is linear, i.e. a weighted sum of factor incomes. *Reusability:* **yes, as principle** â€” gives the quasi-separable contribution form and motivates the exhaustiveness requirement; not a formula I apply to non-additive channels.
- **Corollary 1 (eq. 27) + eq. 28.** *Statement:* the admissible decomposition rules form a large family indexed by arbitrary continuous $\lambda_j(Y)$; proportional contributions under one index can be reproduced under any other. *Technique:* characterise the solution space of the single linear restriction (14) via a basis of the homogeneous system (22)â€“(23). *Reusability:* **yes, as the non-uniqueness warning** (the motivation for axiomatic pinning).
- **Theorem 2 (eqs. 29).** *Statement:* population symmetry and the equal-factor normalisation (Assumption 5) constrain but do **not** uniquely pin the rule. *Reusability:* maybe â€” supports the claim that "reasonable but weak" axioms are insufficient; secondary.
- **Theorem 3 (eq. 31).** *Statement:* Assumptions 1â€“6 imply the **unique, index-independent** rule $s_k(I)=\mathrm{cov}(Y^k,Y)/\sigma^2(Y)$. *Assumptions:* A1â€“A5 plus **Two-Factor Symmetry (A6)**. *Technique:* A6 plus a permutation-matrix construction kills all free $\lambda_j$. *Reusability:* **yes, as principle** (index-independence justifies my across-index robustness reporting); **no, as formula** (covariance rule needs additive components).
- **Theorem 4 (eqs. 35â€“38).** *Statement:* under weak consistency (Assumption 4â€²) there is a monotonic $f$, unique up to scale, with transformed contributions summing to the transformed index; covers the Atkinson family. *Technique:* associativity of the aggregator $F$ + AczÃ©l's representation theorem. *Reusability:* **maybe** â€” relevant if I want to decompose an index (Atkinson) that is only a monotonic transform of a quasi-separable form; note proportional shares then lose index-invariance and additive summing.

## 11. Robustness and specification sensitivity
What the paper itself "stress-tests" is the **axiom set**: it shows step-by-step how adding axioms (A4 â†’ A5 â†’ A6, then the weakening A4 â†’ A4â€²) changes the admissible decomposition family from "the whole real line" to "unique." Two takeaways for my robustness section:
- **Index choice:** Theorem 3 says the *proportional* contributions are index-independent under A1â€“A6 â€” direct support for reporting my decomposition across **Gini / Theil / Atkinson** without expecting the *shares* to move for index-choice reasons alone (any movement I see is then attributable to the decomposition rule or the welfare measure, not the index). This is a useful internal consistency check.
- **Aggregation rule:** Â§4 warns that under a non-additive aggregator (e.g. multiplicative, $f=\log$), proportional shares need not sum to one â€” so if I ever decompose a non-additively-aggregable index I must report this explicitly. For my purposes the additive/exhaustive route (Shapley) is the safer default.
There is nothing here on choice-set size, number of draws, multistart, or opportunity-set definitions â€” those concerns are foreign to this paper.

## 12. What I can cite this paper for
- The **foundational principles of factor decomposition**: continuity, symmetric treatment of factors, independence of the level of disaggregation, and **consistency/exhaustiveness** (contributions sum to total inequality) â€” Assumptions 1â€“4.
- That a decomposition lacking sufficient symmetry axioms is **not pinned down** â€” the proportional contribution can take *any* value (eq. 30, three-person example). The motivation-for-axiomatics citation.
- That, with two-factor symmetry added, there is a **unique decomposition rule whose proportional contributions are independent of the inequality index** (Theorem 3, eq. 31) â€” support for cross-index robustness reporting.
- The **two formal readings of "a factor's contribution"** (the "only source" reading (A), eq. 39; the "eliminate the differences" reading (B), eq. 40) â€” the additive-world formalisation of channel-neutralisation counterfactuals.
- The honest statement that factor decompositions **neglect behavioural feedback between components** (Â§5, tax-incidence example) â€” useful when I caveat that my channel neutralisations are *accounting* counterfactuals, not general-equilibrium ones.
- The **weak-consistency extension to the Atkinson family** (Theorem 4), if I decompose an Atkinson index.

## 13. What I should NOT cite this paper for  [overclaim risks]
- **NOT a Shapley-value decomposition.** This 1982 paper is the *additive factor-component* rule (half-the-covariance interaction split); the Shapley-value / symmetric-orderings construction is **Shorrocks (2013)** (and the cooperative-game lineage), **not** here. Cite 2013 for the Shapley average, not 1982.
- **NOT a two-way *or* three-way opportunity/preference decomposition.** It decomposes by **additive income sources**, not by access / ability / preference. Do **not** describe its components as "opportunity vs preference."
- **NO welfare object.** It contains no money-metric, equivalent income, EV/CV, or inclusive value; do not present its $S(Y^k,Y)$ as a decomposition of *welfare* â€” my object is the inequality of $\Omega^k$, not of income.
- **Do NOT claim it contains $W^1$â€“$W^6$** or any Independence-of-$\mathbf{y}$ / Independence-of-$A$ stance â€” it has no responsibility/compensation content of any kind.
- **NO opportunity / access / occupation content**, hence no occupation-vs-industry issue arises; do not import any "sectoral"/availability language from it.
- **NO random-opportunity framing** (and none to "correct"); it is silent on opportunities entirely. Consistent with my deterministic-opportunities stance, but it makes no claim either way.
- The **cov$(Y^k,Y)/\sigma^2(Y)$ formula does not apply to my channels** â€” they are not additive money components. Citing the *formula* (rather than the *principle*) for a structural-block decomposition would be a misuse.
- **Theory-paper boundary:** this is an empirical-JMP citation for decomposition method; it has no bearing on, and must not be conflated with, the Haydarâ€“Maniquet axiomatic welfare-characterisation paper. Shorrocks's axioms are *inequality-decomposition* axioms, not the companion paper's *welfare-measure* axioms.

## 14. Direct quotes worth citing
To respect source copyright I keep verbatim quotation minimal and give precise locations so exact wording can be pulled from the PDF when drafting:
- On the central non-uniqueness danger, the three-person example concludes that a factor's proportional contribution can be made to take <em>any</em> value between plus and minus infinity (**p. 202, around eq. 30**) â€” the single most quotable line for the "decomposition needs axioms" point.
- On feedback effects being excluded, and this being "both the strength and weakness" of factor decomposition (**p. 210, final paragraph of Â§5**) â€” paraphrase or short exact pull when caveating accounting-vs-behavioural counterfactuals.
- On the index-independence payoff: that with Assumptions 1â€“6 no qualification by choice of index is needed (**p. 205, after Theorem 3**).
- Interpretations (A) and (B) of a factor's contribution (**p. 209, eqs. 39â€“40**) â€” cite by equation, no prose quote needed.

(*Verbatim strings deliberately not reproduced here; copy exact wording from the cited pages of the PDF for the manuscript.*)

## 15. Open questions and risks for my draft
- **Additivity is the hidden assumption.** Everything in this paper rests on $Y=\sum_k Y^k$. My channels are not additive money pieces, so I must be explicit in the draft that I borrow Shorrocks's *principles* (exhaustiveness, index-independence) while replacing his *construction* with the Shapley average â€” and cite 2013 for the latter. The risk is a referee conflating the two; pre-empt by stating the distinction once, clearly.
- **Interaction handling.** Shorrocks's (A)/(B) asymmetry under correlated components is exactly the path-dependence the Shapley average is designed to remove. My Â§8 should make the link: the eq. 30 indeterminacy and the (A)â‰ (B) gap are *the same problem*, and order-independence is the resolution. This strengthens the "not mechanical" defence.
- **Feedback / general equilibrium.** Shorrocks's own caveat (behavioural feedback ignored) applies to my channel neutralisations: equalising access changes attained utility and the chosen bundle. I should state that my decomposition is a *structural-accounting* counterfactual at the estimated $\hat\theta$, not a GE counterfactual, and that this is a deliberate, standard scope limit (citing Shorrocks's framing of strength-and-weakness).
- **Index choice for the headline.** Theorem 3's index-independence holds for *additive* components; under my non-additive Shapley split the index-invariance is not guaranteed by this theorem. I should *check empirically* that shares are stable across Gini/Theil/Atkinson rather than *assert* it from Shorrocks 1982 â€” and report the check.

## 16. TL;DR for retrieval
Foundational additive **factor-component** inequality decomposition: with continuity, symmetric factor treatment, disaggregation-independence, consistency, and **two-factor symmetry**, every inequality index has the **unique, index-independent** contribution rule $\mathrm{cov}(Y^k,Y)/\sigma^2(Y)$ (Theorem 3, eq. 31); without enough axioms the proportional contribution is **indeterminate** over $(-\infty,\infty)$ (eq. 30). Serves my **decomposition** block as the *principle* layer (exhaustiveness + index-independence + the (A)/(B) neutralisation readings, eqs. 39â€“40), **not** as a usable formula â€” my access/ability/preference channels are non-additive, so the Shapley-average construction (Shorrocks 2013) is required, and this paper carries **no welfare object, no opportunity mechanism, and no $W^1$â€“$W^6$ content**.
# Shorrocks 2013 â€” Decomposition Procedures for Distributional Analysis: A Unified Framework Based on the Shapley Value

## 0. Metadata
- **BibTeX key:** `Shorrocks2013` [verify exact key against your `.bib`]
- **Authors:** Anthony F. Shorrocks
- **Year:** 2013 (received 19 May 2011; accepted 26 May 2011; published online 7 January 2012; journal volume dated 2013)
- **Outlet:** *Journal of Economic Inequality*, vol. 11, no. 1, pp. 99â€“126
- **DOI/URL:** 10.1007/s10888-011-9214-z
- **PDF filename:** `Shorrocks_2013_Decomposition_procedures_for_distributional_analysis.pdf`
- **Tier:** T1A
- **JMP block(s) served:** decomposition (primary); methodological backbone of the three-way Shapleyâ€“Shorrocks split. It does *not* serve estimation, identification, opportunity-mechanism, welfare-object construction, data-infrastructure, or motivation directly â€” it is the attribution rule layered on top of whatever welfare object and channel partition the JMP supplies upstream.

## 1. One-paragraph relevance to my JMP
This is the foundational reference for the JMP's headline decomposition layer: it establishes the Shapley decomposition as the unique exact, symmetric, residual-free additive rule for attributing a distributional indicator $I = f(X_1,\dots,X_m)$ to its factors by averaging each factor's marginal contribution over all elimination orders. The JMP's three-way **access / ability / preference** Shapleyâ€“Shorrocks split *is* an instance of this rule with $m=3$ factors, where $I$ is the inequality of a money-metric welfare measure $\Omega^k$ and "removing" a factor means equalising the corresponding structural channel. The paper supplies the exhaustiveness/order-independence property that the welfare-spec Â§6 Shapley gate demands (components must sum exactly to $I(\Omega^k)$). It speaks to no single one of the three channels â€” it is channel-agnostic machinery â€” and it speaks to no specific welfare measure $W^1$â€“$W^6$; its bearing is entirely on *how the attribution is performed* once the channels and the indicator are defined upstream. The paper's most consequential warning for the JMP is its own Â§4 result that Shapley contributions are generally **not invariant to how factors are grouped** unless a separability condition holds, which directly governs whether the JMP may treat {access, ability} as a grouped "opportunity" primary factor.

## 2. Data and setting
N/A â€” the paper is **purely methodological**; it uses no microdata, no country, no sample, no estimation. Its illustrative applications (growthâ€“redistribution poverty change; subgroup poverty; subgroup inequality; source decomposition of inequality) are analytical, drawn from the prior decomposition literature (Dattâ€“Ravallion, Fosterâ€“Greerâ€“Thorbecke, Theil, Bourguignon, Shorrocks's own earlier work), not from a dataset. **Transport to my France pooled 2015â€“2017 EUROMOD cross-section:** the *rule* transports completely â€” it is dimensionless with respect to data and applies to any aggregate indicator $I=f(\cdot)$ â€” but the paper supplies no data-side guidance, no inference machinery beyond a remark that standard errors would "ideally" be computed by algorithm (Â§7), and no sample-design considerations. Features I have that the paper does not address: clustered/bootstrapped inference (the JMP's cluster-robust bootstrap on `idorighh` is mine to build; the paper only flags the desideratum), and the structural-model origin of the factors.

## 3. Model and objects (map object-by-object to mine)
The paper's "model" is the abstract structure $\langle K, F\rangle$: a factor index set $K=\{1,\dots,m\}$ and a set function $F(S)$ giving the value the indicator takes when factors outside $S$ have been "eliminated," with the normalisation $F(\varnothing)=0$ (explicit-in-source, Â§2). There is **no choice set, no utility function, no opportunity mechanism, no budget map** â€” none of my structural objects appear. The mapping to mine is therefore one of *interface*, not of shared primitives:
- My latent-jobs choice set / preference utility $v$ / opportunity density $g$ are all **upstream**; in this paper's terms they are inputs that determine the factor list $K$ and the elimination counterfactuals defining $F(S)$.
- My welfare measure's inequality $I(\Omega^k)$ is this paper's indicator $I=F(K)$.
- My three channels {access, ability, preference} are this paper's factors $X_1,X_2,X_3$.
- "Equalising channel $k$" (my counterfactual) is this paper's "eliminating factor $k$," i.e. moving from $F(S\cup\{k\})$ to $F(S)$.
No job attribute enters "both utility and the opportunity mechanism" *in this paper*, because the paper has neither â€” the double-counting flag is N/A here and must be policed in my structural spec, not here. **Critical caveat the paper forces onto my design:** the paper is explicit (Â§2, footnote 1) that when $F$ derives from an econometric model the normalisation $F(\varnothing)=0$ usually requires one factor to represent the unexplained residual, or $I$ to be renormalised to the "surplus due to the identified factors." My three-channel split must therefore confront whether equalising all three of {access, ability, preference} drives welfare inequality to exactly zero; if it does not, there is an implicit residual factor and the exhaustiveness gate must be interpreted against the renormalised surplus, not against raw $I(\Omega^k)$.

## 4. Estimation method
N/A as an estimator of structural parameters. The paper's "method" is the **construction of the attribution**, given $F$. The Shapley contribution is (explicit-in-source, Eq. 2.8â€“2.9)
$$
C^S_k(K,F) \;=\; \sum_{S\subseteq K\setminus\{k\}} \pi(|S|,|K\setminus\{k\}|)\,\Delta_k F(S)
\;=\; \mathbb{E}_{S\subseteq K\setminus\{k\}}\,\Delta_k F(S),
$$
with weights $\pi(s,m-1) = (m-1-s)!\,s!/m!$ and marginal effect $\Delta_k F(S) = F(S\cup\{k\}) - F(S)$. There is **no likelihood, no choice-set sampling, no proposal density, and no prior/proposal correction** in this paper â€” those belong to my estimation and welfare-integration layers and are *not* informed by Shorrocks. **Verdict: reusable for my decomposition layer â€” yes, directly.** With $m=3$ channels the rule requires evaluating $F$ on all $2^3=8$ subsets and forming the order-averaged marginals; the named step is "compute $I(\Omega^k)$ under each of the eight equalisation states and apply Eq. 2.9." The paper notes (Â§7, explicit-in-source) that for complex models the contributions will not have closed form and must be computed by algorithm, and that standard errors "ideally" be produced too â€” confirming my plan to compute the three-way split numerically with bootstrap CIs rather than analytically.

## 4b. Proposal / sampling-of-alternatives correction
N/A â€” the paper has no sampling of alternatives and no proposal/prior correction; these concepts do not appear and have no analogue in $\langle K, F\rangle$. My importance-sampling welfare integrator and the per-row `prior` correction are entirely outside this paper's scope and must be sourced from the discrete-choice / RURO literature, not here. Stated plainly so it is not silently imported: **Shorrocks 2013 contributes nothing to the proposal-individualisation question.**

## 5. Opportunity mechanism
N/A â€” **no explicit opportunity mechanism exists in this paper.** The paper models neither feasibility of jobs, nor offer probabilities, nor reservation wages, nor any density over alternatives; it does not vary anything with region, education, demographic type, or local labour market. "Opportunity" enters a Shapley decomposition *only if the analyst defines an opportunity factor upstream and specifies the counterfactual that removes it* â€” which is exactly the JMP's job, not Shorrocks's. Mapping to my three sub-objects:
- **access** (hours / participation / region / year / occupation offers): not modelled here; becomes a factor only by my construction.
- **ability** (wage technology; returns to education/experience; residual productivity): not modelled here; same.
- **occupation** (`loc4`): not modelled; the paper cannot and does not conflate occupation with industry/sector because it models neither â€” **no sector/industry language appears**, so there is no conflation to flag.
**What the omission costs my decomposition:** nothing at the rule level â€” the rule is built precisely to be agnostic about what the factors are. But the paper offers *no* help in (i) defining the access/ability/preference factors, (ii) defining their equalisation counterfactuals, or (iii) arguing those counterfactuals are economically meaningful. The paper itself is emphatic (Â§7 and throughout) that the rule is an attribution device, not a model, so the entire substantive opportunity content of the JMP is upstream of it.

## 6. Welfare object â€” and its place on my $W^1$â€“$W^6$ map
N/A as a welfare construction. The paper computes **no** welfare object â€” no money metric, no equivalent income, no EV/CV, no inclusive value, no reference price/preference/bundle/set. It is explicitly **normatively neutral about the choice of indicator** (derived-by-analogy from Â§2 and Â§7): the rule decomposes whatever aggregate distributional statistic the analyst supplies â€” a Fosterâ€“Greerâ€“Thorbecke poverty index, a Gini, a generalized-entropy/MLD index, a variance â€” without endorsing any. **Placement on my $W^1$â€“$W^6$ map:** none. The paper corresponds to no Independence-of-$y$ / Independence-of-$A$ stance, because it takes no stance on the welfare object at all; it sits one layer *above* the measure menu, as the operator that maps any chosen $\Omega^k$ to its factor contributions. **Verdict: the welfare object is not in this paper (incompatible-as-a-source-of-welfare-objects); the decomposition operator is directly usable on whichever $\Omega^k$ the welfare layer hands it.** Do **not** cite Shorrocks 2013 for anything about money-metric or equivalent-income welfare.

## 6b. Inclusive value and money-metric inversion
N/A â€” the paper uses no inclusive value, no log-sum, no EV/CV, and performs no money-metric inversion. There is no expectation over extreme-value shocks, analytic or simulated. My analytic-in-shocks, importance-sampling inversion is wholly outside this paper. (Stated to forestall overclaim: the "expectation" $\mathbb{E}_{S\subseteq K\setminus\{k\}}$ in Eq. 2.9 is an expectation over *factor-elimination subsets*, a combinatorial average â€” it is **not** an expectation over preference shocks or a log-sum and must never be conflated with my inclusive value $V_i$.)

## 7. Inequality / decomposition content  [the core of this paper]
**Indices the paper treats explicitly:** the Fosterâ€“Greerâ€“Thorbecke decomposable poverty family; the generalized-entropy class $E_c$ (including the mean logarithmic deviation $E_0$ and the Theil index $E_1$ as members); the Gini coefficient; the variance and squared coefficient of variation (for source decomposition). **Decomposition rule:** the **Shapley decomposition** (Eq. 2.8â€“2.9), defined as the expected marginal contribution of each factor over all $m!$ elimination orders; plus the two-stage **Owen** value (Eq. 4.6â€“4.8) for hierarchical/grouped factors. **Counterfactual construction:** a factor is "eliminated" by setting it to a neutralising value â€” e.g. growth eliminated by $G=0$, redistribution by $R=0$ (Â§3.1); between-group inequality eliminated by setting each relative subgroup mean $b_k=1$ (Â§5.1, with the explicit note in footnote 8 that $b_k=\beta>0$ is an alternative); a source eliminated either by zeroing it (the "levels" formulation $F(S)=I(\sum_{k\in S} y_k)$, Eq. 6.2) or by replacing it with its mean (the "differences" formulation $\tilde F(S)=I(\sum_{k\in S} y_k + \sum_{k\notin S}\mu_k e)$, Eq. 6.3). The Â§6 levels-vs-differences distinction is directly relevant to my equalisation design: equalising a channel to its mean (differences) vs zeroing it (levels) are different counterfactuals with different Shapley contributions, and an equally-distributed component contributes zero under the differences formulation but generally non-zero (and possibly negative) under levels.
**Properties established (explicit-in-source):** exact additivity $\sum_k C^S_k = F(K)$ (Eq. 2.7); symmetry/anonymity; order-independence (the average over all $m!$ paths is what removes path dependence, Â§2); and the characterisation (footnote 3, citing Young 1985) that Eq. 2.8 is the *only* symmetric and exact rule whose factor-$k$ contribution depends only on factor $k$'s own marginal-effect set.
**Verdict for my three-way access/ability/preference split: directly reusable.** With $m=3$ the rule is fully exhaustive and order-independent by construction, satisfying my Shapley exhaustiveness gate. The paper is not "two-way vs three-way" in any limiting sense â€” the rule is defined for arbitrary $m$ â€” so no extension is needed to go from its two-factor worked examples (growth/redistribution; within/between) to my three factors. The one genuine design decision the paper forces is **grouping**: if I ever report a two-level hierarchy (e.g. "opportunity = access + ability" as one primary factor, preference as the other), Â§4 warns that the within-opportunity split of access vs ability is sensitive to the grouping *unless* $F$ is separable over {access, ability} (Eq. 4.10), and that aggregation-consistency between the grouped "opportunity" contribution and the sum of its access+ability parts is guaranteed only via the **Owen two-stage** procedure (Prop. 2). This is exactly the welfare-spec concern that the {access, ability} bracket and the {preference} factor be reported jointly and not double-interpreted.

## 8. Identification and the separation of preferences from opportunities  [STRICT]
The paper offers **no identification content** in the structural sense and must not be read as supporting the separation of preferences from opportunities. It is explicit and repeated (Â§2, Â§7, and the concluding remarks) that the rule is an *attribution* device that operates **after** the analyst has (i) defined the factor list, (ii) defined the counterfactual that removes each factor, and (iii) chosen the indicator $I$ â€” all of which are "economic and normative, not mechanical." The credibility of any Shapley decomposition therefore rests entirely on those upstream choices, **not** on the rule. For my paper this is double-edged and must be stated honestly in the identification note: Shorrocks 2013 guarantees that *given* a credible access/ability/preference partition and credible equalisation counterfactuals, the attribution is exact, symmetric, and order-independent â€” but it provides **zero** defence against the "your decomposition is mechanical" referee, because that referee's target is precisely the upstream factor-and-counterfactual definitions that Shorrocks places outside his framework. The separation of preferences ($v$) from opportunities ($g$), and of ability from access *within* $g$, must be identified in my structural model (functional form, the wage-technology vs feasible-set distinction, synthetic-recovery certification) â€” Shorrocks contributes the exhaustiveness of the *split*, never the *identification* of the things being split. Do not soften this: a referee who concedes the Shapley rule still has every license to attack the channel definitions.

## 9. Key results and magnitudes
No empirical magnitudes â€” the paper reports **no elasticities, welfare effects, opportunity shares, or decomposition shares from data.** Its "results" are analytical equivalences (explicit-in-source): (i) for the growthâ€“redistribution poverty change, the Shapley contributions equal the Dattâ€“Ravallion components *averaged over base and final years*, eliminating their residual term $E$ (Â§3.1, Eq. 3.5â€“3.6); (ii) for a multivariate subgroup poverty decomposition with $n$ attributes, each factor receives exactly $1/n$ of its single-attribute contribution (Prop. 4, Eq. 4.21); (iii) for subgroup inequality with the generalized-entropy class, the Shapley split coincides with standard within/between practice **only** for the mean logarithmic deviation $E_0$, and differs for all other $E_c$ (Â§5.1, Eq. 5.10â€“5.11); (iv) for source decomposition, the Shapley split reproduces the "natural" covariance decomposition $C_k=\mathrm{cov}(y_k,y)$ **exactly for the variance** (Â§6, Eq. 6.10), partially for the squared coefficient of variation (Eq. 6.12), and not in closed form for other indices; (v) an equally-distributed income source receives a **negative** Shapley contribution under the levels formulation when the index is scale-invariant and strictly Schur-convex (Prop. 5). For benchmarking my own numbers: the only transferable quantitative lesson is the $1/n$ multivariate-attribution result and the $E_0$-only coincidence â€” both bear on which inequality index I choose, not on plausible magnitudes of an opportunity share.

## 10. Estimators, theorems, or formal results
For each formal result: statement (near-verbatim, LaTeX), assumptions, technique, reusability verdict.

- **Shapley decomposition rule (Eq. 2.8â€“2.9).** Statement: $C^S_k(K,F) = \sum_{S\subseteq K\setminus\{k\}} \frac{(m-1-|S|)!\,|S|!}{m!}\,\Delta_k F(S) = \mathbb{E}_{S\subseteq K\setminus\{k\}}\Delta_k F(S)$. Assumptions: $F:\{S\mid S\subseteq K\}\to\mathbb{R}$ with $F(\varnothing)=0$. Technique: (1) define order-specific marginal contributions; (2) average over all $m!$ elimination orders to remove path dependence; (3) collapse the average to a subset-weighted sum; (4) identify the weights with the Shapley value. **Reusable: yes** â€” this is the JMP's decomposition operator with $m=3$.
- **Exactness (Eq. 2.7).** Statement: $\sum_{k\in K} C^S_k = F(K) - F(\varnothing) = F(K)$. Assumption: $F(\varnothing)=0$. Technique: telescoping along any elimination path, preserved under averaging. **Reusable: yes** â€” this is the welfare-spec exhaustiveness gate ($\sum$ components $= I(\Omega^k)$).
- **Owen two-stage / hierarchical rule (Eq. 4.6â€“4.9).** Statement: allocate to primary factor $L$ its Shapley contribution in the aggregated model, then allocate $L$'s contribution among its constituents by an inner Shapley step; this is **always aggregation-consistent** (Eq. 4.9). Assumptions: a partition $A=\{L_j\}$ of $K$. Technique: nested Shapley averaging (outer over primary factors, inner over secondary). **Reusable: maybe** â€” only if I report a grouped "opportunity = access+ability" primary factor and need its parts to sum consistently; needed precisely when $F$ is **not** separable over the group.
- **Proposition 1â€“2 (separability).** Statement: if $F$ is separable over $L\subseteq K$ (Eq. 4.10: $\Delta_k F(S\cup T)=\Delta_k F(S)$ for $k\in L$), then grouping $L$ does not change contributions of factors outside $L$ (Prop. 1) and the Shapley and Owen decompositions **coincide** and are aggregation-consistent (Prop. 2). Technique: combinatorial lemmas (Appendix Lemmas 1â€“2). **Reusable: yes, as a diagnostic** â€” tells me whether my access/ability split can be reported either grouped or ungrouped without changing the numbers; if access and ability interact (non-separable), the grouped vs ungrouped reports will differ and Owen is required for consistency.
- **Proposition 3 (separable + sufficient).** Statement: if $F$ is separable over each primary factor and each is "sufficient," contributions reduce to $\frac{1}{|A|}M_k(K,F)$, the first-round marginal scaled by the number of primary factors. **Reusable: maybe** â€” gives the clean $1/n$ shortcut (Prop. 4) but its assumptions are unlikely to hold for an interacting structural welfare model; treat as a special-case sanity check, not the working case.
- **Proposition 5 (negative contribution of an equal component).** Statement: under scale-invariance and strict Schur-convexity, an income source distributed equally across the population gets a strictly negative Shapley contribution (levels formulation). **Reusable: as interpretation** â€” warns that a channel that compresses the welfare distribution can carry a negative contribution; relevant if a channel turns out equalising.

## 11. Robustness and specification sensitivity
The paper's own "robustness" content is methodological, and it maps cleanly onto my stress-tests. (1) **Index choice matters:** the Shapley split coincides with conventional within/between subgroup practice only for $E_0$ (MLD) among the entropy class, and with the natural covariance split only for the variance among source decompositions â€” so my reported decomposition shares can move with the inequality index even holding the channels fixed. *Implication:* report the three-way split for the Gini (welfare-spec baseline) but show at least one entropy index (MLD/Theil) as a robustness check, and expect the shares to shift. (2) **Counterfactual choice matters:** levels vs differences (Â§6), and the neutralising value used to "remove" a factor ($b_k=1$ vs $b_k=\beta$, footnote 8; zero vs mean for a source), change the contributions. *Implication:* my channel-equalisation counterfactual (equalise to mean? to a reference? to the access-/ability-equalised population distribution?) is a first-order specification choice that must be stated and stress-tested. (3) **Grouping matters** (Â§4): the access-vs-ability split inside a grouped "opportunity" factor is sensitive to grouping unless separability holds. The paper does **not** address number-of-draws, choice-set size, multistart, effective-sample-size, or circumstance partitions â€” those robustness axes are mine and get no guidance here.

## 12. What I can cite this paper for
- That the Shapley decomposition is the exact, symmetric, order-independent additive attribution rule for any indicator $I=f(X_1,\dots,X_m)$, computed as each factor's marginal contribution averaged over all elimination orders (Eq. 2.8â€“2.9, Eq. 2.7).
- That this rule unifies and, in benchmark cases, reproduces or improves upon the prior patchwork of poverty/inequality decomposition formulas (abstract; Â§7).
- That it eliminates the residual/interaction term required by ad hoc decompositions (the Dattâ€“Ravallion residual; the Gini interaction term) â€” Â§3.1, Â§5.2.
- That the Shapley split coincides with standard within/between practice **only** for the mean logarithmic deviation among entropy indices, and with the natural covariance decomposition **only** for the variance among source decompositions (Â§5.1, Â§6).
- That for grouped/hierarchical factors the **Owen** two-stage value delivers aggregation consistency, coinciding with Shapley under separability (Â§4, Prop. 2).
- That the rule is index- and model-agnostic and that its outputs depend on the analyst's upstream choice of factors, counterfactuals, and indicator (Â§2, Â§7) â€” useful as the honest caveat in my own decomposition section.
- That for complex models the contributions generally lack closed form and require algorithmic computation, ideally with standard errors (Â§7) â€” supports my numerical-plus-bootstrap implementation.

## 13. What I should NOT cite this paper for  [overclaim risks]
- **Not** a source for any welfare object: it computes no money-metric, equivalent-income, EV/CV, or inclusive-value welfare, and corresponds to **no** $W^1$â€“$W^6$ measure or Ind-$y$/Ind-$A$ stance. Do not attribute the welfare family or its normative readings to Shorrocks.
- **Not** an identification result: it does not identify or justify the separation of preferences from opportunities, or of ability from access. Citing it as support for the *credibility* of the access/ability/preference partition would be an overclaim â€” it explicitly places that work upstream and outside its scope.
- **Not** a structural or opportunity-mechanism paper: no choice set, no $g$, no offer probabilities. Do not read its set function $F(S)$ as a feasible-set or opportunity object.
- **Not** about occupation, industry, or sector â€” the paper models none of these; there is no `loc4`/`lindi` content and therefore no occupation-as-access claim to draw from it.
- **Boundary flags:** (a) two-way examples (growth/redistribution; within/between) are *illustrations*, not a limit â€” but do not cite a specific two-factor formula (e.g. Eq. 3.5) as if it were the three-way rule; cite the general Eq. 2.9 for the three-way split. (b) The combinatorial "expectation over subsets" in Eq. 2.9 must **never** be presented as an expectation over preference shocks or as my inclusive value. (c) "Random opportunities" framing is irrelevant here â€” the paper is deterministic set-function machinery; nothing in it bears on the deterministic-vs-random opportunities question.
- **Theory-paper boundary:** Shorrocks 2013 is decomposition methodology and belongs to the empirical JMP's decomposition layer. It is unrelated to the Haydarâ€“Maniquet axiomatic theory paper; do not let its "characterisation/axioms" language (which refers to characterisations of the Shapley *value*, not of welfare measures) be read as supporting the companion paper's measure characterisation, and do not read the JMP's use of it as a theory contribution.

## 14. Direct quotes worth citing
Short verbatim extracts with page numbers (each â‰¤ ~12 words; one per locus):
- p. 102: the objective is to assign contributions to each factor so that the total is the sum of factor contributions. [paraphrase-safe; verify exact wording if quoting]
- p. 103: the rule averages each factor's marginal impact over all elimination sequences. [paraphrase-safe; verify exact wording if quoting]
- p. 104: contributions "sum up to the amount" requiring explanation (exactness). [verify page/wording]
- p. 121 (Â§7): the procedure "can be applied to a wide range of problems which cannot be solved with existing techniques." [verify exact wording before quoting]

> **Note (honesty flag):** I have **not** lifted exact verbatim strings with certified page-precision from the PDF for Â§14; the loci above are paraphrase-safe pointers. Before any of these enters the draft as a quotation, open the PDF and confirm the exact words and page. Marked **[verify]**.

## 15. Open questions and risks for my draft
- **The $F(\varnothing)=0$ / residual problem (Â§2, fn 1).** If equalising all three channels does not drive welfare-measure inequality to exactly zero, there is an implicit residual factor and my exhaustiveness gate must be stated against the renormalised "surplus due to identified factors," not raw $I(\Omega^k)$. I must check this empirically and report it.
- **Counterfactual definition is a first-order choice the paper leaves to me.** Equalise each channel to its mean? to a reference distribution? The Shapley numbers depend on it; the welfare-spec's "what is equalised / held fixed / zeroed" must be pinned and stress-tested (cf. Â§6 levels-vs-differences).
- **Grouping / Owen decision (Â§4).** Whether to report "opportunity = access + ability" as a grouped primary factor, and if so whether to use Owen for aggregation consistency, hinges on separability of $F$ over {access, ability}. If access and ability interact in the welfare measure (plausible, since both enter $g$), grouped and ungrouped reports will differ â€” I must decide and disclose which I report.
- **Index sensitivity.** Shares may shift between Gini and entropy indices even with channels fixed; the robustness section must show this rather than report a single-index headline as if index-invariant.
- **Inference.** The paper flags but does not provide standard errors; the entire cluster-robust bootstrap apparatus is mine, and the welfare-spec's per-component CI asymmetry (tight opportunity, wide preference) is not something Shorrocks speaks to.

## 16. TL;DR for retrieval
Shorrocks 2013 is the canonical, data-free methodological source establishing the **Shapley decomposition** as the unique exact, symmetric, order-independent additive rule for attributing any distributional indicator to its factors, plus the **Owen** two-stage extension and separability conditions for grouped factors â€” it is the operator the JMP applies to its three-way **access / ability / preference** split of welfare-measure inequality, satisfying the exhaustiveness gate by construction. It supplies **no** welfare object, **no** opportunity mechanism, and **no** identification of the channels â€” all of which are upstream â€” so it must be cited for the *attribution machinery and its exactness/grouping properties only*, never for the credibility of the channel partition, the welfare family $W^1$â€“$W^6$, or anything structural. Its load-bearing warnings for my draft are the $F(\varnothing)=0$/residual normalisation, the counterfactual-definition dependence, the grouping/Owen sensitivity, and the index-dependence of the resulting shares.
# van Soest 1995 â€” Structural Models of Family Labor Supply: A Discrete Choice Approach

> **FILE/SOURCE MISMATCH NOTE (not part of the template).** This summary was
> requested under the save name `Aaberge_Colombino_2013.md`, but the attached
> PDF is **van Soest (1995)**, not Aaberge & Colombino (2013). Per the
> instruction that *the attached PDF is the source of truth* and the rule
> *do not invent claims*, this document summarises van Soest (1995) and is named
> accordingly. If an Aaberge & Colombino (2013) summary is wanted, attach that
> PDF. **Suggested correct path:** `JMP_literature/03_summaries/T1B/van_Soest_1995.md`
> (tier reassessed below).

## 0. Metadata
- **BibTeX key:** `vanSoest1995` [verify against library convention]
- **Authors:** Arthur van Soest (Tilburg University)
- **Year:** 1995
- **Outlet:** *The Journal of Human Resources*, Vol. 30, No. 1 (Winter 1995), pp. 63â€“88
- **DOI/URL:** JSTOR stable URL `https://www.jstor.org/stable/146191` (printed on source); DOI [verify, not printed]
- **PDF filename:** `Van_Soest_-_1995_-_Structural_Models_of_Family_Labor_Supply_A_Discrete_Choice_Approach.pdf`
- **Tier:** Filed by the user under **T1A**. **My assessment: T1B** â€” it is the foundational *estimation*/data-infrastructure ancestor of the discrete-choice family-labour-supply approach, but it contains no opportunity density, no welfare object, and no decomposition, so it does not serve the JMP's defining (welfare/decomposition/opportunity-mechanism) blocks directly.
- **JMP block(s) served:** **estimation** (primary: the discrete-choice MNL labour-supply backbone, the joint-couple decision unit, simulated ML for unobserved wages); **data-infrastructure** (Heckman-corrected wage imputation feeding a discretised budget map); **identification** (secondary, as a *cautionary* baseline for separating preferences from availability); **access** channel (precursor only, by analogy â€” the "hours-restrictions" device). **Not** welfare, **not** decomposition, **not** ability-as-a-welfare-object, **not** normative-interpretation.

## 1. One-paragraph relevance to my JMP
van Soest (1995) is the canonical statement of the **discrete-choice structural labour-supply model**, which is the estimation skeleton my RURO/latent-jobs pipeline inherits: a finite choice set over (income, leisure) packages, type-I extreme-value shocks, and a multinomial-logit choice probability that sidesteps budget-set nonconvexities (explicit-in-source, pp. 67â€“69). It speaks to my **preference** channel directly (his translog $U$ is the analog of my Boxâ€“Cox utility block $v$) and to my **access** channel only by analogy: his ad hoc "hours-restrictions" alternative-specific constants are an early, *non-circumstance-varying* device for missing part-time jobs, which is precisely the homogeneity assumption my circumstance-dependent access density is built to relax (pp. 71â€“72). His simulated-ML integration over an unobserved-wage density (his "ability" technology, a Heckman-corrected wage equation) is the methodological ancestor of my importance-sampling integrator over the wage channel (pp. 70â€“71). The paper computes **no welfare object and no inequality decomposition**, so for those layers it is a methodological prerequisite, not a usable template.

## 2. Data and setting
- **Country/year:** Netherlands, 1987 (explicit, p. 73).
- **Dataset:** Socio Economic Panel (SEP), wave drawn October 1987 by CBS (explicit, p. 73).
- **Sample unit:** two-adult families (husband + wife, both aged 16â€“65); a **unitary family** decision unit (explicit, pp. 73â€“74).
- **Sample size:** 2,859 families after dropping missing values; composition â€” 13.0% neither spouse works, 3.1% only wife, 49.7% only husband, 34.1% both (explicit, pp. 73â€“74). (Table 5 uses 2,826 observations for simulations.)
- **Key variables:** number/age of children, spouses' ages, education levels, child benefits, other family income, before-tax hourly wages, weekly hours, employment dummies (Table 2, p. 75).
- **Budget-set construction:** after-tax family income $y_j$ as a function of the spouses' hours, inverting the Dutch 1987 tax/premium system (eleven brackets, marginal rates 0â€“70%) plus a stylised benefits floor at ~50% of the family poverty line; before-tax wage assumed independent of hours (explicit, pp. 66â€“67, 74). The transferable tax-free allowance creates the canonical joint-filing nonconvexity (explicit, p. 66).
- **Transport to my France pooled 2015â€“2017 EUROMOD cross-section:** the *architecture* transports cleanly (discrete choice, tax-benefit budget map, couples as joint unit). Features I have that van Soest does **not** use: EUROMOD-computed `ils_dispy` as the budget map (he hand-codes a stylised 1987 system); pooled multi-year cross-section. Features **he** has that bear on mine: a single cross-section (no panel) â€” same limitation as mine. Features **neither** of us has: panel, administrative match, external opportunity instrument, vacancy/offer data (explicit absence in source; he estimates the availability device from hours data alone, p. 72).

## 3. Model and objects (object-by-object map to mine)
- **Choice set vs my latent-jobs set:** His choice set is a **fixed, common, finite grid** of $(y_j, l_{mj}, l_{fj})$ packages â€” $m = m_{\text{ind}}^2$ points, with $m_{\text{ind}}=5$ (25 alts, $IL=12$) or $m_{\text{ind}}=6$ (36 alts, $IL=10$), time endowment $TE=80$ h/week (explicit, p. 67). This is a **universal hours grid, identical across families** â€” *not* a household-specific feasible-job set. This is the single most important difference from my latent-jobs construction.
- **Deterministic utility vs my preference $v$:** His direct **translog** utility $U(v)=v'Av+b'v$ with $v=(\log y,\log l_m,\log l_f)'$ (eq. 1, p. 68); demographic taste-shifters enter through $\beta_i,\alpha_{ij}$ (eq. 2, p. 68). This **maps to my preference utility $v$** (explicit functional-form analog; mine is Boxâ€“Cox, his is translog â€” both checkable for monotonicity/quasi-concavity).
- **Opportunity / availability mechanism analogous to my $g$:** **None as a density.** The only availability device is a set of **alternative-specific constants** $\gamma_m(l_{mj}),\gamma_f(l_{fj})$ on part-time alternatives (eqs. 13â€“14, p. 72), interpreted as drawbacks/scarcity of part-time jobs. This is **not** a density over alternatives, **not** household-specific, and **explicitly assumed homogeneous across the labour market** (p. 72). Mapping to my four $g$-channels: **hours** â†” his $\gamma$ constants (crude, aggregate, deterministic â€” derived-by-analogy only); **wage (ability)** â†” handled outside the index, via the wage equation feeding the budget map (see Â§4b, Â§5); **market/participation** â†” not separately modelled (participation is just the $h=0$ alternative); **occupation** â†” **absent entirely** (see Â§5, Â§13).
- **Budget map vs my EUROMOD disposable income:** His $y_j$ = hand-coded Dutch 1987 tax-benefit map; mine = EUROMOD `ils_dispy` (2016-real). Same role, different engine.
- **Attribute entering BOTH utility and availability?** **No** â€” wage/occupation do not enter his utility-plus-availability index twice; the $\gamma$ constants enter the index, the wage enters only the budget map. So no double-entry to flag here. (This is the cleanliness my baseline also targets: occupation in $g$ only.)

## 4. Estimation method
- **Likelihood/estimator:** Multinomial logit choice probabilities (eq. 6, p. 69) from i.i.d. type-I EV shocks added to each alternative's utility (eq. 5, p. 68); estimated by **(simulated) maximum likelihood** (explicit, pp. 69â€“71).
- **Choice-set construction:** **Fixed full grid** (25 or 36 alternatives), **not** sampled alternatives (explicit, p. 67). There is therefore **no** sampling-of-alternatives correction and **no** per-alternative log-prior (see Â§4b).
- **Proposal/sampling density and $\log(\text{prior})$ subtraction:** **N/A** â€” no alternatives are sampled; the "simulation" in the paper is over *unobserved wages and random preferences*, not over the choice set.
- **Normalisation/scale:** The common EV variance $\pi^2/6$ is the scale normalisation, chosen instead of normalising a utility parameter so that the normalised parameter's sign is known a priori (explicit, p. 69).
- **Numerical method / draws:** Approximate (simulated) ML; integrals over the unobserved-wage density and random-preference density approximated by $R$ Monte Carlo draws, $R=5$ and $R=10$ (eqs. 11â€“12, 18, pp. 71, 73). Consistency requires $R\to\infty$ with $\sqrt{n}/R\to 0$ (explicit, p. 71). No multistart procedure described [verify].
- **What pins preferences vs the availability device:** the translog functional form plus the assumption that the $\gamma$ constants are alternative-specific and homogeneous across the labour market (see Â§8).
- **Verdict â€” reusable for my RURO/JAX pipeline?** **Partly, yes.** The MNL log-sum core (eqs. 5â€“6) and the simulated-integration step (eqs. 11â€“12) are reusable in spirit (my JAX engine already does the analytic-in-shocks log-sum and importance-sampling integration). His **fixed-grid** choice set is **not** reusable â€” my pipeline uses sampled alternatives with a $-\log\pi$ correction, which his framework lacks by construction. **Name the step:** reuse the MNL probability form and the simulated-ML-over-wage-density idea; replace the fixed grid with my sampled-alternatives + proposal correction.

## 4b. Proposal / sampling-of-alternatives correction
**N/A in the strict sense.** van Soest uses a **fixed, exhaustive grid** of 25â€“36 alternatives, so there is no proposal distribution, no McFadden-style correction, and no per-alternative log-prior (explicit, p. 67). The integration he *does* perform is over the **unobserved before-tax wage density** $p(W_{bm},W_{bf}\mid Z_m,Z_f)$ (eqs. 10â€“12, pp. 70â€“71), with draws from the Heckman-estimated wage equations. **Relation to my work:** this wage-density integration is the closest analog to my **wage-channel importance sampling**, and his proposal is **partly individualised** in the same sense mine is â€” the wage draws condition on individual characteristics $Z$ (education, age, region, minimum wage), while there is no analogous individualisation of an hours/employment offer mechanism (he has none). So his design supports, by precedent, my "wage/occupation individualised; hours/employment common" individualisation pattern â€” though for him the hours dimension is a fixed grid, not a common offer density (derived-by-analogy, not explicit).

## 5. Opportunity mechanism  [MOST IMPORTANT â€” split by channel]
**There is no explicit opportunity density.** The choice set is a universal common grid; the only availability content is the ad hoc hours-restrictions device. By channel:

- **access (hours / participation / region / occupation offers):**
  - *Hours availability:* represented by **alternative-specific constants** $\gamma_{sk}$ ($s=m,f$; $k=1,2,3$) on part-time alternatives (eqs. 13â€“14, p. 72), motivated by the basic model's strong **over-prediction of part-time work** (Table 3, p. 78). All $\gamma_{sk}$ estimated significantly negative (explicit, p. 78). **Functional form:** additive constants on specific hours cells; **deterministic**, not a density. **Crucially, assumed homogeneous across the labour market** â€” they "do not depend on wage rates, education level, family composition" (explicit, p. 72), i.e. the relative scarcity of part-time jobs is assumed **uncorrelated with circumstances**.
  - *Participation/market:* not separately modelled; non-participation is simply the $h=0$ alternative within the same grid.
  - *Region:* enters only the *wage equation* (DWEST, regional unemployment rate), not an availability mechanism over the choice set (explicit, Table A1, p. 85).
  - *Occupation offers:* **absent** (see below).
- **ability (wage technology):** a **Heckman selection-corrected log-wage equation** estimated separately for males and females, with returns to **education dummies, age (log age, log ageÂ²), the legal minimum wage, and the regional unemployment rate**, plus residual dispersion $\sigma(\eta)$ and a selection correlation $\rho$ (explicit, Table A1, p. 85). This is the analog of my **ability** sub-block (returns to education/experience + residual productivity dispersion), **but** it is used only to *impute and integrate over unobserved wages in the budget map*, **not** as a channel in a welfare or decomposition object (derived-by-analogy for the mapping; the welfare/decomposition use is not-established because the paper has no such layer).
- **occupation:** **not present** in any form â€” no ISCO/task variable, no `loc4` analog, no industry/NACE variable. There is therefore **no occupation-as-access object and no sector/industry conflation risk** to flag in this source.

**Cost of the omission for my access/ability/preference decomposition (stated plainly):** because the choice set is common and the hours-restriction constants are homogeneous across circumstances, the model has, by construction, **no between-household variation in access** â€” exactly the object my paper exists to measure. Adopting his device unchanged would mechanically **zero out the access component** of my decomposition. His framework is a baseline to *depart from*, not a source for the access channel.

## 6. Welfare object â€” and its place on my $W^1$â€“$W^6$ map
**The paper computes no welfare object.** No money-metric income, no equivalent income, no compensating/equivalent variation, no inclusive-value-as-welfare. Its post-estimation objects are **behavioural**: expected hours, elasticities, and tax/benefit **policy simulations** reported in hours and participation rates (Tables 4â€“5, pp. 80, 83). Reference price/preference/bundle/set: **N/A** (no welfare reference is constructed). Discrete-choice welfare subtleties (log-sum aggregation, Hicksian vs Marshallian, ex-ante vs ex-post): **not addressed**, because no welfare is computed.

**Location on my $W^1$â€“$W^6$ map:** **none.** The source does **not** contain $W^1$â€“$W^6$ or any compensationâ€“responsibility classification (explicitly absent). Any attempt to place it would be fabrication. **Verdict: incompatible as a welfare source** â€” it is upstream of the welfare layer.

## 6b. Inclusive value and money-metric inversion
- **Inclusive value as welfare core?** **No** (not-established). He never forms the log-sum as a welfare object.
- **Money-metric inversion (1-D solve)?** **No** (not-established).
- **Expectation over EV shocks â€” analytic or simulated?** For *choice probabilities and expected hours*, **analytic** â€” expected hours are a closed-form, continuously differentiable function of wages/income via the MNL probabilities (explicit, footnote 13, p. 80). Simulation in the paper is over *wages and random preferences*, not over the shocks.
- **Relation to my analytic-in-shocks, importance-sampling inversion:** his expected-hours object shares my **analytic-in-shocks** property, but he stops at *behaviour*; my contribution converts the same analytic log-sum into an **ex-ante money-metric** via a 1-D root-solve, which he does not do (derived-by-analogy for the analytic step; the inversion is mine, not his).

## 7. Inequality / decomposition content
**None.** No inequality index (Gini/MLD/Theil/Atkinson), no decomposition rule (Shapley/Shorrocks/RIF/subgroup), no counterfactual equalisation. **Verdict: not reusable for my three-way access/ability/preference Shapleyâ€“Shorrocks split**, and it is neither a two-way nor a three-way decomposition â€” it has **no** decomposition at all. To serve this layer it would have to be extended with the entire welfare *and* decomposition apparatus.

## 8. Identification and the separation of preferences from opportunities  [STRICT]
- **What separates tastes from the availability device:** (i) the **translog functional form** of $U$, which generates smooth indifference maps and cannot, by itself, reproduce the spikes/holes in the observed hours distribution; (ii) the **restriction that the $\gamma$ hours-restriction constants are alternative-specific and homogeneous across the labour market** â€” they are identified from the residual peaks (full-time mass) and troughs (part-time deficit) the smooth utility leaves unexplained (explicit reasoning, pp. 72, 78). So the preference/availability split rests on **functional form + a strong homogeneity restriction**, not on choice-set variation, a panel, or an external instrument.
- **ability vs access within the availability side:** the paper does **not** attempt this split; "ability" lives only in the wage equation and is not contrasted against an access object.
- **Transport to my France pooled cross-section (no panel, no external instrument):** the *mechanism of identification* transports â€” I, too, lack a panel/instrument and lean on functional form. **But the specific homogeneity restriction does not survive contact with my research question:** van Soest assumes availability is uncorrelated with circumstances; my access channel is defined by making availability **circumstance-dependent**. This is the cleanest statement of why his device cannot be borrowed and is, instead, the foil for my identification note.
- **Defence against the "your decomposition is mechanical" referee:** van Soest is useful here precisely as the *negative* example â€” it shows that a model which forces availability to be homogeneous will load all between-household variation onto preferences (his basic-vs-extended elasticity collapse is the symptom; see Â§9), which is the over-attribution my paper corrects. Do **not** soften this: his hours-restriction constants are *ad hoc* and discretization-dependent (his own characterisation, pp. 72, 83).
- **Synthetic-recovery / parametric identification:** the paper relies on in-sample fit and diagnostic tests (Andrews 1988 chi-square; LM/Wald/LR on the $\gamma$'s), **not** on synthetic recovery (explicit, pp. 76â€“78). My baseline's standard of evidence (synthetic recovery, not in-sample fit) is therefore *stricter* than his and should be flagged as a deliberate departure.

## 9. Key results and magnitudes
- **Aggregate own before-tax wage elasticities of labour supply:** **0.11 (males), 0.40 (females)** (abstract p. 63; policy-sim rows 4â€“5, Table 5, p. 83). Population: sample-average aggregate response to a 10% wage increase.
- **Average-family median own-wage elasticities** (Table 4, p. 80): basic model (Model I) $h_m=0.153$, $h_f=1.027$; with hours restrictions (Model II) $h_m=0.104$, $h_f=0.524$; with hours restrictions + wage prediction error (Model III, $R=10$) $h_m=0.076$, $h_f=0.472$. **Headline pattern:** adding the availability device **roughly halves the female own-wage elasticity** (explicit, pp. 81â€“83). Cross-wage elasticities small and negative; income elasticities very small.
- **Model fit:** the basic model **strongly over-predicts part-time work**; the $\gamma$ constants restore the marginal hours fit almost exactly (max marginal difference 0.29 pp), though a bivariate chi-square test still rejects (explicit, pp. 78â€“79).
- **Quasi-concavity:** violated at 0.8% (25 alts) / 6.3% (36 alts) of basic-model sample points, concentrated among high-income full-time-wife families; 99.9% concave under Model II (explicit, pp. 76, 78).
- **Wage-prediction-error and random-preference extensions:** small effects; $R=5$ vs $R=10$ "virtually identical"; random-preference standard deviations imprecise and not confirmed as important (explicit, p. 79).
- **Policy simulations** (Table 5, p. 83): abolishing the transferable tax-free allowance â†’ female labour supply **+4.2%**, male **âˆ’0.7%** (net hours **+0.4%**); full individualisation of taxes+benefits â†’ female labour supply **âˆ’7.1%**, two-earner households **âˆ’14.5%**.
- **Benchmark value for my work:** the **elasticity collapse when availability is added** is the directly relevant magnitude â€” it quantifies how much "preference responsiveness" in a no-availability model is actually availability, which is the over-attribution my decomposition targets.

## 10. Estimators, theorems, or formal results
This is an applied econometrics paper; it states estimators, not theorems.
1. **Discrete-choice (MNL) labour-supply estimator.** Statement: $\Pr[U_j>U_k\ \forall k\neq j]=\exp(U(y_j,l_{mj},l_{fj}))/\sum_{k}\exp(U(y_k,l_{mk},l_{fk}))$ (eq. 6, p. 69), with $U$ the translog (eq. 1) and i.i.d. EV(I) shocks (eq. 5). Assumptions: finite common choice set; i.i.d. type-I EV; IIA. Technique: ML on closed-form logit probabilities; budget-set shape is irrelevant to the probability (a stated advantage). **Reusability:** **yes** â€” this is the backbone my RURO factorisation generalises ($v$ + $\log g$ âˆ’ $\log\pi$).
2. **Hours-restrictions extension.** Statement: $U_j=U(\cdot)+\gamma_m(l_{mj})+\gamma_f(l_{fj})+\varepsilon_j$ (eqs. 13â€“14, p. 72), $\gamma_{sk}$ alternative-specific, homogeneous across the market. **Reusability:** **no, as-is** â€” adopt only as the explicit foil; my access channel must make these circumstance-dependent.
3. **Simulated ML over unobserved wages.** Statement: $L=\int F_{\text{job}}(W_{bm},W_{bf},X)\,p(W_{bm},W_{bf})\,dW$ approximated by $L_R=\frac1R\sum_r F_{\text{job}}(W_{bmr},W_{bfr},X)$ (eqs. 10â€“12, pp. 70â€“71), draws from the Heckman wage equation; consistent as $R\to\infty$, $\sqrt n/R\to0$. **Reusability:** **yes** â€” methodological ancestor of my wage-channel importance sampling; my contribution is to fold this into an opportunity *density* rather than a budget-map nuisance integral.
4. **Random-preferences extension.** Statement: random normal coefficients on the leisure log-terms $\beta_2,\beta_3$ (eqs. 15â€“18, p. 73), integrated by simulation. **Reusability:** **maybe** â€” relevant only if I revisit unobserved preference heterogeneity beyond the EV shocks; the source finds it adds little.
No propositions, lemmas, or theorem numbers to report.

## 11. Robustness and specification sensitivity
- **Choice-set granularity:** $m_{\text{ind}}=5$ (25 alts) vs $6$ (36 alts) â€” most parameters similar, elasticity confidence intervals overlap; discretisation introduces rounding error and a modest quasi-concavity difference (explicit, pp. 76, 80). *Lesson for me:* alternative-count sensitivity is real but second-order; worth a recovery check across grid sizes.
- **Number of draws:** $R=5$ vs $10$ "virtually identical" (explicit, p. 79). *Lesson:* small $R$ can suffice â€” relevant to my effective-sample-size concern, though my singles ESS problem is about *importance-sampling* coverage, which his fixed-grid design does not face.
- **Discretisation-dependence of the availability device:** the $\gamma$ parameterisation depends on the chosen $IL$/$m_{\text{ind}}$, so results across discretisations "can no longer be compared" (explicit, p. 72). *Lesson/warning:* any hours-availability parameterisation I tie to a specific alternative grid inherits this fragility â€” argue for a circumstance-parameterised (not cell-specific) form.
- **What breaks:** elasticities fall sharply with each added realism layer; the author cautions that "misspecification is still present" and that true elasticities may be even smaller (explicit, p. 84).

## 12. What I can cite this paper for
- The **discrete-choice / multinomial-logit structural labour-supply model** as the foundational approach that handles nonlinear taxes and budget-set nonconvexities without coherency restrictions (pp. 67â€“69).
- The **unitary-couple joint-decision** treatment with a single family utility over (income, both leisures) (pp. 63, 68).
- The empirical fact that **standard models over-predict part-time work**, motivating an explicit treatment of **limited job/hours availability** (pp. 71â€“72, 78) â€” useful motivation for my access channel.
- That **adding availability constraints substantially lowers estimated wage elasticities** (pp. 81â€“84) â€” the over-attribution-to-preferences point.
- **Simulated ML** for integrating over **unobserved wages of non-workers** via a Heckman-corrected wage equation (pp. 70â€“71).

## 13. What I should NOT cite this paper for  [overclaim risks]
- **Not** an opportunity-density / RURO / latent-jobs paper â€” its availability device is **ad hoc alternative-specific constants**, not a household-specific feasible-set density. Do not attribute a latent-jobs opportunity mechanism to it.
- **Not** a source for **circumstance-varying access** â€” it explicitly assumes hours restrictions are **homogeneous across the labour market** (p. 72), the opposite of my access object.
- **Not** a welfare / equivalent-income paper â€” do **not** cite for money-metric well-being under different feasible sets; it computes no welfare object.
- **No inequality or decomposition** â€” do not read any "opportunity vs preference" (two-way) *or* access/ability/preference (three-way) split into it; it has none.
- **No occupation/sector** â€” it has no ISCO/`loc4` analog and no NACE/`lindi`; do not cite for occupation-as-access, and note there is no sector/industry conflation to inherit.
- **Random-opportunity vs deterministic framing** â€” irrelevant here; its randomness is in *shocks and unobserved wages*, not in opportunities. Do not import any "random opportunities" reading.
- **Theory-paper boundary** â€” nothing in this source bears on $W^1$â€“$W^6$ or the Haydarâ€“Maniquet axioms/characterisation. Do not let it stand in for the theory paper, and do not read it as a theory contribution.
- **Intra-household** â€” it is a *unitary* family utility, explicitly setting aside collective/Pareto-efficient intra-household models (footnote 1, p. 64); do not cite for individual-within-couple welfare.

## 14. Direct quotes worth citing
*(short verbatim phrases, page-numbered, for retrieval indexing only)*
- "labor supply is treated as a discrete choice problem" (p. 64).
- "the lack of available part-time jobs" (p. 71).
- "hours restrictions are homogeneous across the labor market" (p. 72).
- "allowing for hours restrictions substantially reduces estimated own wage elasticities" (pp. 83â€“84).

## 15. Open questions and risks for my draft
- **The availability-homogeneity assumption is the crux.** van Soest's model demonstrates the failure mode my paper corrects (availability folded into a homogeneous constant), but it also shows how *little* identifying variation supports an availability device estimated from hours data alone (p. 72). Risk for my draft: a referee can ask whether my circumstance-dependent access is identified by more than functional form â€” I must point to my synthetic-recovery certification and the partly-individualised proposal, not to in-sample fit.
- **Discretisation-dependence (p. 72)** is a live warning for any hours-availability parameterisation tied to a specific alternative grid; argue for a circumstance-parameterised form and report grid-size recovery.
- **Elasticity attenuation under added realism (p. 84)** suggests my preference-component estimates (already wide per the project's standard-error asymmetry) will be sensitive to how richly access is modelled â€” relevant to the preference-component confidence-interval width in the decomposition.
- **No welfare/integration machinery here**, so this source offers no guidance on my binding open issue (singles importance-sampling coverage / EUROMOD reprice parity); that risk must be addressed from the welfare-spec and project-state lineage, not from van Soest.

## 16. TL;DR for retrieval
van Soest (1995) is the foundational **discrete-choice MNL family-labour-supply estimator** (translog utility = my **preference** block; fixed common hours grid; simulated ML over unobserved wages = ancestor of my wage/**ability**-channel integration), and it motivates an **access**-type device only through ad hoc, *circumstance-homogeneous* hours-restriction constants. It contains **no opportunity density, no occupation variable, no welfare object, and no decomposition**, so it serves my **estimation/data-infrastructure** blocks and stands as the explicit **foil** for my circumstance-dependent access channel â€” never as a source for welfare, the $W^1$â€“$W^6$ family, or the three-way Shapleyâ€“Shorrocks split.
