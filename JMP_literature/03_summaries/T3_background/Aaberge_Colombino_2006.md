# Aaberge & Colombino 2006 — Designing Optimal Taxes with a Microeconometric Model of Household Labour Supply

> **Extraction note (read first).**
> - **Source of truth:** the attached PDF, Statistics Norway *Discussion Papers* No. 475 (Sept. 2006). All section/equation/table references below are to that document; **no page numbers are cited** (the source is referenced by its own section/eq/table numbering, which is explicit in text).
> - **Template used:** `JMP_T2_focused_extraction_prompt_v2.md`. The exhaustive `JMP_T1_exhaustive_extraction_prompt_v2.md` was **not attached**, so I could not "use it exactly." I have populated the full T2 skeleton (sections 0,1,2,5,6,7,8,9,12,13,16) at T1A depth. The T1-only sections (3,4,10,11,14,15) are listed at the end as `[T1-only — rerun with the real T1 prompt]`, with pointers to the source material that would fill them, so the rerun is cheap.
> - **Filename correction:** requested as `Aaberge_et_al_2009.md`; the attached PDF is **Aaberge & Colombino (2006), DP475**, not the 2009 Wennemo choice-set paper (which already has a file in the project). Saved as `Aaberge_Colombino_2006.md`. Intended repo path: `JMP_literature/03_summaries/T1A/Aaberge_Colombino_2006.md`.
> - **Vocabulary:** I use **access / ability / preference** in my own analysis; where I report what the *source* does I use its own two-factor language (*preferences / opportunities*) and its own Roemerian *Equality-of-Outcome / Equality-of-Opportunity* (EO/EOp) language, flagging the obsolete framing.
> - **W-namespace warning, stated up front:** this paper contains a family it calls $W_1, W_2, W_3, W_\infty$ — these are **rank-dependent social welfare functions** (single-series Ginis: $W_1$ Bonferroni, $W_2$ Gini, $W_\infty$ utilitarian), an *inequality-aggregation* family. They are **not** the JMP's $W^1$–$W^6$ equivalent-income measure family. The paper does **not** contain the JMP's $W^1$–$W^6$. See §6 and §13.

---

## 0. Metadata

- **Suggested BibTeX key:** `aaberge_colombino_2006_optimaltaxes`
- **Authors:** Rolf Aaberge (Statistics Norway, Research Dept.); Ugo Colombino (Dipartimento di Economia, Torino).
- **Year / outlet:** 2006, Statistics Norway *Discussion Papers* No. 475, Research Department, Oslo (working paper / discussion paper).
- **Handle (explicit in source):** `https://hdl.handle.net/10419/192457` (EconStor). No DOI in source.
- **Likely journal version:** Aaberge & Colombino, *Scandinavian Journal of Economics* (≈2013), "Using a microeconometric model of household labour supply to design optimal income taxes." **[verify — not in source; do not cite a DOI without checking]**
- **PDF filename:** `Aaberge_Colombino_2006_Designing_Optimal_Taxes_with_a_Microeconometric_Model_of_Household_Labour_Supply.pdf`
- **Tier:** T1A.
- **JMP blocks served:** estimation (the RURO/latent-jobs estimator lineage); opportunity-mechanism (the offered-hours / offered-wage / sector opportunity densities → maps onto access vs ability); welfare (a common, opportunity-aware individual welfare function — a *precedent*, not the JMP's equivalent income); decomposition / normative-interpretation (Roemer EO vs EOp, a *different* opportunity construct); motivation.
- **JEL (source):** H21, H31, J22.

---

## 1. One-paragraph relevance to my JMP

This is a direct ancestor of the JMP's structural layer: it is the Aaberge–Colombino–Strøm (1999) RURO/latent-jobs estimator — choice over *jobs* (packages of hours $h$, wage $w$, and sector $s$), with utility weighted by an estimated **opportunity density** $p(h,w,s)$ — applied here to Norwegian singles and couples with 78 parameters. Its opportunity density is **already factorised** into an offered-**wage** sub-density (lognormal in own education and experience → my **ability** channel, the Independence-of-$\mathbf{y}$ dimension) and offered-**hours** plus **sector** plus **market-vs-non-market** sub-densities (→ my **access** channel, the Independence-of-$A$ dimension), which makes it a clean citation that the access/ability split is *operational* inside the offer mechanism, not an invention of the JMP. It also runs a welfare layer (a *common*, opportunity-aware individual welfare function) and an opportunity-sensitive normative criterion (Roemer EOp), but **both differ in kind from the JMP's objects** — the welfare object is a common-utility comparability device rather than a preference-respecting equivalent income, and "opportunity" in its EOp criterion means **family-background circumstances**, not the feasible-job-set content the JMP attributes. So it anchors my *estimator* and my *opportunity-mechanism* sections strongly, my *welfare* and *decomposition* sections only as contrast.

---

## 2. Data, setting, and model in brief

- **Country / data:** Norway; the 1995 Survey of Level of Living, income year 1994. **[verify — internal inconsistency in source: the abstract says "1994," the conclusions and Appendix say "1995"; most consistent reading is survey 1995 / tax rule and incomes 1994].**
- **Unit:** decision unit is the household — single females, single males, and married/cohabiting **couples making joint labour-supply decisions** (the couple is the joint unit, as in my baseline).
- **Age window:** estimation restricted to ages **18–54** (to exclude retirement, per Appendix A); the welfare-function estimation and the optimal-tax simulation use ages **20–62** (Table 4.1, §6). **[verify — the 18–54 vs 20–62 mismatch is in the source as written].**
- **Core model:** a discrete-choice random-utility labour-supply model, "an extension of the standard multinomial logit," in the Aaberge–Dagsvik–Strøm / Aaberge–Colombino–Strøm (1999) tradition (explicit in §2 fn 3). Agents choose among **jobs** characterised by $(w,h,j)$, not merely among hours; for a given agent wages may differ job to job. Behaviour is a comparison of *utility levels* across a continuum/large set of latent jobs, with an estimated density of opportunities. Estimated by simultaneous maximum likelihood across the three groups.
- **Feature I do not have:** the EOp layer uses **father's years of schooling** as a circumstance/type variable (3 types). My French pooled EUROMOD cross-section has no comparable parental-background circumstance, so the paper's *EOp* exercise does not transport even though its *estimator* does. (Conversely, the paper has no occupation/ISCO offer layer; its only "sector" variable is public-vs-private — see §5.)

---

## 5. Opportunity mechanism

**Explicit in source.** The set $B$ of opportunities available to a household includes non-market opportunities (a "job" with $w=0,h=0$). Because the analyst does not observe $B$, it is represented by a density $p(h,w,j)$ of job *types*, interpreted as the relative frequency/availability of jobs of type $(h,w,j)$ in the choice set (§2, eq (2.4) and its discussion). The choice density (eq (2.4)) is the systematic utility $v$ **weighted by availability** $p$, normalised over the feasible set — i.e. "relative attractiveness weighted by availability," which is structurally the JMP's `u + log g − log π` integrand with $p$ playing the role of the offer density $g$.

The opportunity density is specified (Appendix A, eq (A3)) for singles as
$$
p(h,w,s) \;=\;
\begin{cases}
p_0\, g_{1s}(h)\, g_{2s}(w)\, g_3(s), & h>0,\\[2pt]
1-p_0, & h=0,
\end{cases}
$$
with $p_0$ the proportion of **market** opportunities, and the three conditional densities:

- $g_{1s}(h)$ — **offered hours** density (eq (A7)): uniform over hours except multiplicative peaks at **part-time (18–20 weekly hours)** and **full-time (37–40)**, parameters $\pi$ varying by gender.
- $g_{2s}(w)$ — **offered wage** density (eq (A9)): **lognormal**, $\log w = \beta_0 + \beta_1\,\mathrm{Exp} + \beta_2\,\mathrm{Exp}^2 + \beta_3\,\mathrm{Ed} + \sigma\eta$, $\eta\sim N(0,1)$, with experience $\mathrm{Exp}=\text{age}-\text{schooling}-5$; parameters vary by gender **and by sector**.
- $g_3(s)$ — **sector** density (eq (A8)): public vs private, parameters $\mu$ by gender.

For couples the same architecture is specified jointly over $(h_M,h_F,w_M,w_F,s_M,s_F)$ with separate market/non-market proportions $p_0^M,p_0^F$ (eqs (A10)–(A19)).

**Mapping to access / ability (derived-by-analogy; the source uses two-factor "preferences/opportunities" and does not name access/ability).**
- $g_2$ (offered-wage technology in own education/experience and residual $\sigma$) $\to$ **ability** — exactly the Independence-of-$\mathbf{y}$ / pay dimension of the JMP cut.
- $g_1$ (offered hours), $g_3$ (sector), and $p_0$ (market vs non-market) $\to$ **access** — the Independence-of-$A$ / feasible-set dimension.
- Systematic utility $v$ $\to$ **preference**.

So the AC opportunity density is *already* split into one pay sub-density and several feasibility sub-densities; the JMP's three-way structural-to-normative map (preference $=v$; ability+access $=g$, cut $g$ in two) is the *same partition*, re-labelled and re-purposed for a welfare decomposition rather than for tax simulation.

**Boundary flag — "sector" here is public/private, not ISCO and not NACE.** The paper's $s$ is a **public-vs-private employment-sector** dummy. It is **neither** the JMP's occupation offer layer (`loc4`/ISCO, which I treat as *access*) **nor** the reserved industry variable (`lindi`/NACE). Do not cite this paper's "sector" as occupation or as industry. In JMP vocabulary a public/private offered-job split is best read as a further *access* sub-block.

---

## 6. Welfare object

**What the paper computes (explicit in source, §4).** Because estimated preferences are heterogeneous and the sample mixes singles and couples, the paper confronts interpersonal comparability and resolves it with a **common individual welfare function** $V$ (eq (4.1)): all individuals are treated as singles, $V$ is allowed to vary with age and number of children, and couples' disposable income is divided by $\sqrt{2}$ for scale economies, with each partner assigned the resulting income (eq (4.2)). Crucially, $V$ is **estimated with the same opportunity-weighted density** (eq (2.4) with $v$ replaced by $V$), inserting the previously estimated offered-hours and offered-wage distributions for $p$ — so the welfare object is **opportunity-aware**: the proportion of the population at a given $(c,L)$ is the welfare value of $(c,L)$ weighted by how available that income–leisure combination is.

**Money-metric vs other.** $V$ is a **common-utility** comparability device, not a money-metric / equivalent income in the King (1983) / Fleurbaey sense. It is *not* the JMP's preference-respecting equivalent income, and it is *not* converted to an income/subsidy against a reference. The paper cites Fleurbaey & Maniquet (2006), "Fair Income Tax," and Boadway et al. (2002) in fn 5 precisely on the comparability-under-heterogeneous-leisure-preferences problem — a useful citation hook for my §2.1, but the paper does **not** adopt the equivalent-income solution.

**Constrained vs universal; ex-ante vs ex-post.** Welfare is computed **ex-post** on the *simulated chosen* pair $(c,h)$ under each tax rule (§6, step 3: "apply to the chosen $(c,h)$ the common utility function"), not on an ex-ante inclusive value / log-sum. It is opportunity-*aware* in estimation of $V$ (offered densities enter), but the per-person welfare number is read off a realised bundle, not off the JMP's $V_i=\log\sum\exp(\cdot)$. This is the AC/JJT "ex-post chosen-alternative" form that my welfare memo lists as a **secondary, correction-free cross-check (D3)**, not as the headline ex-ante object.

**Where it sits on my $W^1$–$W^6$ map.** **Not established / N/A.** The paper does not have an Independence-of-$\mathbf{y}$/Independence-of-$A$ stance and does not span a compensation–responsibility spectrum at the *measure* level. The closest correspondence is conceptual only: a common-utility welfare function evaluated on realised bundles is nearest to a **Full-Responsibility, ex-post** reading, but this is an analogy, not a placement on the characterised family. **Do not claim this paper instantiates any $W^k$.**

---

## 7. Inequality / decomposition content

**Inequality / SWF family (explicit in source, §5).** Aggregation uses a family of **rank-dependent social welfare functions** $W_k$ (eq (5.1)–(5.2)) of Mehran (1976)/Yaari (1988) type, with associated inequality measures $I_k$ (eq (5.4)): $I_1$ Bonferroni, $I_2$ Gini; $W_1$ Bonferroni, $W_2$ Gini, $W_3$ an intermediate, $W_\infty$ utilitarian (inequality-neutral). Inequality aversion **decreases in $k$**. These are "illfare-ranked single-series Ginis" (Donaldson–Weymark 1980). **This $W_k$ is an inequality-aggregation family and shares only a letter with my $W^1$–$W^6$ equivalent-income family — see §13.**

**Opportunity content (explicit in source, §5).** The normative novelty is **Equality of Opportunity (EOp)** in the sense of Roemer (1998): outcomes are the joint product of *circumstances* (beyond control) and *effort* (own responsibility). **Circumstances/types are defined by father's years of education** (Type 1 $<5$, Type 2 $5$–$8$, Type 3 $>8$); **effort is proxied by the within-type quantile/rank** of the welfare distribution. The EOp criterion maximises (a weighted version of) the across-type minimum at each effort quantile; the paper introduces an **extended EOp family** $\tilde W_k$ (eq (5.6)) and a mixture distribution $\tilde F$ (eq (5.7)) of the worst-off type-segments, decomposed analogously to $W_k$ (eq (5.8)–(5.9)). EO (Equality of Outcome) is the special case ignoring the type structure.

**Counterfactual construction / order properties.** The "decomposition" here is the EOp construction (across-type minimum / mixture of worst-off segments), **not** a Shapley–Shorrocks attribution and **not** order-independent-by-construction in the Shapley sense. There is no exhaustive components-sum-to-total identity of the JMP type.

**Reusable for my three-way access/ability/preference Shapley split?** **Indirectly, as lineage and contrast, not as method.** (i) The paper's responsibility cut is **circumstances (family background) vs effort**, a *different* opportunity referent from the JMP's **job-set access/ability vs preference**; it is two-way and Roemerian, not three-way and structural. (ii) To get to the JMP's split you would *not* extend this EOp construction; you would instead Shapley-equalise the **structural** blocks ($g_2$ ability, $g_1/g_3/p_0$ access, $v$ preference) that this paper *estimates but does not decompose*. So the citable contribution is: this paper supplies the **estimated opportunity sub-densities** that a three-way decomposition needs, and a **precedent for treating opportunity as compensation-relevant and effort/preference as responsibility-relevant**, while leaving the structural Shapley attribution itself unaddressed.

---

## 8. Identification and separation of preferences from opportunities

**What identifies tastes vs constraints here (explicit-in-source mechanism; the cleanly-stated exclusion is derived-by-reading).** Preferences ($v$) and opportunities ($p$) are separated by **functional-form and covariate exclusion** inside a jointly estimated MNL-type likelihood:
- The **offered-wage** density $g_2$ depends on **own education and experience** (eq (A9)); these enter *opportunity*, not the systematic utility $v$ (eq (A2)). Education/experience shifting *offered pay* but not *tastes* is the exclusion that pins the **ability** channel apart from preference.
- The **offered-hours** density $g_1$ carries **part-time/full-time peaks** (eq (A7)); concentration of observed hours at those peaks beyond what tastes-over-leisure would generate identifies the **access** (hours-availability) channel.
- The **sector** density $g_3$ and **market proportion** $p_0$ absorb participation/sectoral availability.
- Pooling **singles and couples** in one simultaneous likelihood (the opportunity densities are shared across marital status — Appendix A) adds cross-group restrictions that help identify the offer side.

**Transport to my France pooled cross-section (no panel, no external instrument).** The **estimator transports directly** — this is the lineage of my RURO baseline, and identification rests on the same within-cross-section functional-form + exclusion logic rather than on panel variation or instruments, which is exactly my setting. Two honest caveats: (i) separation of *ability* (returns in $g_2$) from *preference* leans on the maintained exclusion that education/experience are offer-side, not taste-side — the same assumption my ability/access cut depends on, so this paper is support for the assumption's standard-ness, not independent proof of it; (ii) the paper's *EOp* identification (father's education types) does **not** transport, as that variable is absent from my data. So cite for **estimator identification**, not for **circumstance-based EOp identification**.

---

## 9. Key results and magnitudes

- **Model size:** **78 parameters** capturing heterogeneity in preferences and in opportunities across singles and couples (abstract, §2, §7).
- **Labour-supply elasticities (Table 3.2, aggregate, own-wage, unconditional total hours):** married females $\approx$ **0.52**, married males $\approx$ **0.39**, single females $\approx$ **0.02**, single males $\approx$ **0.02**. Headline behavioural facts: married women far more elastic than married men; **low-income households much more elastic than high-income** (Table 3.1; §3); backward-bending supply for singles in the middle deciles.
- **Optimal-tax findings (§6, Tables 6.2–6.6):** within a 6-parameter piecewise-linear rule and **fixed total net revenue**, every optimal rule implies an **average tax rate below the 1994 rule**, with **lower marginal rates on low/average income and higher marginal rates on high income**; more egalitarian SWF $\Rightarrow$ more progressive rule. Unconstrained, the **top marginal rate is $100\%$** above $\approx$ **NOK 700,000 (1994) $\approx$ €87,000**; a second exercise caps $\tau_3 \le 0.60$. **EO and EOp optimal rules are very similar** (EOp even marginally more progressive in places) — a notable null on the EO-vs-EOp distinction at the policy-rule level.

---

## 12. What I can cite this paper for

1. **Estimator lineage and legitimacy of the RURO/latent-jobs design** — choice over jobs $(h,w,s)$, utility weighted by an estimated opportunity density, in the Aaberge–Colombino–Strøm tradition; the structural backbone of my baseline.
2. **The opportunity density is *factorised* into a pay sub-density and feasibility sub-densities** — i.e. that separating offered **wages** (ability) from offered **hours/sector/market** (access) is standard practice inside the offer mechanism, not a JMP innovation (eqs (A3),(A7)–(A9)).
3. **Welfare can be made opportunity-aware** by estimating the welfare function with the same offer-weighted density (§4) — precedent for "welfare under different feasible sets," while being explicit that AC use a *common-utility* device, not equivalent income.
4. **Responsibility-sensitive normative framing has standing in this literature** — opportunity (circumstances) as compensation-relevant, effort as responsibility-relevant (Roemer EOp, §5) — motivation for my compensation–responsibility spectrum.
5. **The rank-dependent / single-series-Gini SWF family** ($W_1$ Bonferroni, $W_2$ Gini, $W_\infty$ utilitarian; $I_1,I_2$) as an inequality-aggregation toolkit (§5) — usable as an inequality index citation, kept terminologically separate from my $W^1$–$W^6$.
6. **Empirical regularities** for sanity-checking my French estimates: married-women > married-men elasticity, low-income > high-income elasticity.

---

## 13. What I should NOT cite this paper for (overclaim risks)

1. **$W^1$–$W^6$ namespace collision.** The paper's $W_1,W_2,W_3,W_\infty$ are **rank-dependent SWFs / single-series Ginis**, *not* the JMP's equivalent-income measure family. Never imply this paper contains, characterises, or instantiates my $W^1$–$W^6$. (It does not.)
2. **Two-way, not three-way; and a *different* two-way.** Its responsibility cut is **circumstances (father's education) vs effort**, Roemerian — not **opportunity vs preference** and not **access/ability/preference**. Do not present it as a two-factor opportunity/preference decomposition that "just needs extending" to three channels; the channel it splits is family background, a different object.
3. **Sector $\ne$ occupation $\ne$ industry.** Its $s$ is **public/private**; do not cite it as ISCO occupation (`loc4`) or as NACE industry (`lindi`). In my map a public/private offer split is *access*, but it is not my occupation layer.
4. **Welfare object mismatch.** It is **common-utility, ex-post on the chosen bundle**, *not* preference-respecting ex-ante equivalent income. Do not cite it as a money-metric equivalent-income computation or as an ex-ante inclusive-value welfare object; at most it is precedent for my **D3 secondary** ex-post CE cross-check.
5. **No Shapley–Shorrocks.** Do not attribute an order-independent, exhaustive components-sum-to-total decomposition to this paper.
6. **Deterministic-opportunities boundary.** The JMP treats opportunities as **deterministic**; do not import any "random opportunities" reading from the RURO label here.
7. **Theory-paper boundary.** This is an empirical AC paper; it is unrelated to the Haydar–Maniquet theory paper. Never route any normative characterisation/proof through it, and never let "Aaberge–Colombino welfare function" stand in for the companion paper's axiomatic $W^1$–$W^6$.
8. **Data-year and age-window precision.** Report the 1994/1995 data year and the 18–54 vs 20–62 windows as flagged `[verify]`, not as settled facts, given the internal inconsistencies in the source.

---

## 16. TL;DR for retrieval

Aaberge & Colombino (2006, Statistics Norway DP475) estimate a 78-parameter RURO/latent-jobs household labour-supply model on Norwegian 1994/95 data (singles + couples, joint), in which an estimated **opportunity density factorises into an offered-wage sub-density in own education/experience (= my *ability* channel) and offered-hours/sector/market sub-densities (= my *access* channel)**, then use it to simulate **optimal piecewise-linear taxes** under fixed revenue, finding lower average rates with higher top-end marginal rates and near-identical EO and EOp optima. For the JMP it is **estimator-lineage T1A** — strong support for the structural backbone and for the access/ability factorisation of the offer mechanism — but its **welfare object is common-utility/ex-post (not equivalent income)**, its **$W_k$ are single-series-Gini SWFs (not my $W^1$–$W^6$)**, and its **"opportunity" is Roemerian family-background circumstances (not feasible-job-set access/ability)**, so it must not be cited as a money-metric equivalent-income decomposition or as a three-way opportunity/preference split.

---

## [T1-only sections — rerun with `JMP_T1_exhaustive_extraction_prompt_v2.md` (not attached)]

These section numbers are referenced by the T2 template as belonging to the fuller T1 template, but I do not have the T1 prompt and will not invent its required structure. Source material that would populate them, for a cheap rerun:

- **§3 (full model / equation inventory):** §2 eqs (2.1)–(2.4); Appendix A eqs (A1)–(A9) singles, (A10)–(A19) couples; Type-III extreme-value error (eq (2.3)).
- **§4 (estimation details):** simultaneous ML, likelihood = product of densities over single-F / single-M / couples; ages 18–54; parameter tables A1 (singles utility), A2 (couples utility), A3 (job/hours/wage densities), A4 (incomes & labour supply under the current rule).
- **§10 (robustness / specification variants):** unconstrained vs $\tau_3\le 0.60$ exercises (Tables 6.2 vs 6.3); EO vs EOp (Tables 6.2–6.6); inequality-aversion sweep over $k=1,2,3,\infty$.
- **§11 (limitations):** common-utility comparability device rather than equivalent income; circumstance variable limited to father's education; ex-post welfare read on simulated bundles; static cross-section.
- **§14 (related-literature positioning):** Mirrlees (1971), Saez (2001), Laroque (2005); Roemer (1998), Roemer et al. (2003); Aaberge–Colombino–Strøm (1999, 2000); Fleurbaey–Maniquet (2006); Dagsvik (1994); Ben-Akiva–Watanatada (1981).
- **§15 (data infrastructure):** 1995 Survey of Level of Living; Norwegian 1994 tax rule (Table 6.1); 6-parameter piecewise-linear optimal-rule class (eq (6.1)).
