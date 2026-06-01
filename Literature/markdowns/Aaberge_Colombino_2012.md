---
title: "Accounting for Family Background when Designing Optimal Income Taxes: A Microeconometric Simulation Analysis"
authors: [Rolf Aaberge, Ugo Colombino]
year: 2012
outlet: "Journal of Population Economics, 25(3), 741--761"
country_or_context: "Italy"
population: "Married couples, single females, single males; ages 18--54"
data_period: "1993"
shelf: "structural labour supply / optimal taxation / equality of opportunity"
tags: [RURO, discrete-choice, optimal-taxation, EOp, EO, extended-EOp, Roemer, family-background, circumstances, types, Italy, microsimulation, lump-sum-tax, affine-tax, piecewise-linear]
priority: "high"
read_status: "extracted"
---

# Full citation

Aaberge, R., & Colombino, U. (2012). Accounting for Family Background when Designing Optimal Income Taxes: A Microeconometric Simulation Analysis. *Journal of Population Economics*, 25(3), 741--761.

# One-sentence contribution

Develops an extended Equality of Opportunity (EOp) criterion that accounts for income inequality both between and within circumstance types, applies it to Italian data using a structural RURO labour supply model, and finds that the EO criterion is paradoxically more "interventionist" (redistributive) than the EOp criterion — because EOp-optimal policies exploit the high labour supply elasticity of disadvantaged types via lump-sum taxes rather than marginal rate redistribution.

# Why this paper matters

This is the first paper to compute optimal income taxes under the Roemer (1998) Equality of Opportunity criterion using a structurally estimated microeconometric labour supply model with heterogeneous behavioural responses. It extends the pure EOp criterion ($\tilde{W}_\infty$) to a family of "extended EOp" criteria ($\tilde{W}_k$) that also penalize within-type inequality, bridging the gap between pure EOp and EO. The key empirical finding — that EOp favours lump-sum taxation while EO favours marginal rate redistribution — is surprising and driven by the high labour supply elasticity of the most disadvantaged type.

# Core research question

What is the optimal income tax-transfer rule under the Equality of Opportunity criterion (Roemer 1998), and how does it differ from the optimal rule under the conventional Equality of Outcome criterion? Does accounting for family background (circumstances) as a source of inequality lead to more or less redistribution through marginal tax rates?

# Economic setting and context

Italy 1993: progressive individual income tax with 7 brackets (10%--51%), low female participation (~40%), rigid labour market with few part-time opportunities, strong regional disparities (North vs. South). Family background (father's education) is a key predictor of economic outcomes. The paper uses the 1993 Bank of Italy SHIW data.

# Model / theoretical framework

**Positive model:** The RURO (Random Utility Random Opportunity) job-choice model of Dagsvik (1994), as estimated in Aaberge, Colombino & Strøm (1999) on Italian 1993 SHIW data. Three separate models are estimated: one for couples, one for single females, one for single males. The model accounts for joint household decisions, non-linear budget constraints, and quantity constraints on job availability.

**Normative framework:**

1. **EO (Equality of Outcome):** Standard rank-dependent SWF:
$$W_k = \int_0^1 p_k(t) F^{-1}(t) \, dt$$
where $F$ is the CDF of equivalent income (disposable household income divided by $\sqrt{\text{household size}}$) and $p_k(t)$ are weight functions indexed by inequality aversion $k$.

2. **Pure EOp (Roemer):**
$$\tilde{W}_\infty = \int_0^1 \min_j F_j^{-1}(t) \, dt$$
where $F_j^{-1}(t)$ is the quantile function of type $j$'s income distribution. This focuses only on the worst-off type at each quantile.

3. **Extended EOp (new):**
$$\tilde{W}_k = \int_0^1 p_k(t) \min_j F_j^{-1}(t) \, dt, \quad k = 1, 2, 3, \ldots$$
This combines between-type inequality (via $\min_j$) with within-type inequality aversion (via $p_k(t)$). The extended EOp can be decomposed as:
$$\tilde{W}_k = \tilde{W}_\infty(1 - \tilde{C}_k)$$
where $\tilde{C}_k$ is a measure of inequality for the mixture distribution $\tilde{F}(x) = \max_j F_j(x)$.

**Types (circumstances):** 3 types defined by father's education:
- Type 1: less than 5 years (most disadvantaged)
- Type 2: 5--8 years
- Type 3: more than 8 years (most advantaged)

**Framework:** Both positive (behavioural simulation) and normative (optimal tax design under EOp and EO criteria).

# Key objects

- **Extended EOp welfare function** $\tilde{W}_k = \int_0^1 p_k(t) \min_j F_j^{-1}(t) \, dt$: the paper's main theoretical contribution. Nests pure EOp ($k = \infty$) and approaches EO as types become homogeneous.
- **Inequality decomposition** $\tilde{W}_k = \tilde{W}_\infty(1 - \tilde{C}_k)$: separates the extended EOp into an efficiency component ($\tilde{W}_\infty$, mean of the worst-off type's distribution) and an inequality component ($\tilde{C}_k$, inequality within the worst-off distribution).
- **Affine tax rules:** $x = c + (1-t)y$ with lump-sum transfer $c$ and constant marginal rate $t$.
- **Three-parameter tax rules:** Two brackets with rates $t_1, t_2$ and a kink at mean income $\bar{y}$, plus transfer $c$.

# Data

1993 Bank of Italy Survey of Household Income and Wealth (SHIW93). Sample: singles and couples aged 18--54. Self-employed excluded (>20% of gross income from self-employment). Three separate models estimated for couples, single females, and single males. Income measured in 1,000 ITL (pre-Euro; divide by 1.93627 for Euro equivalent). Father's education used to define 3 circumstance types.

# Identification logic

Identification follows the standard RURO approach (Aaberge et al. 1999): utility parameters identified from non-linearities in the Italian tax-benefit function; opportunity density parameters identified from hours/wage distributions, participation rates, and regional unemployment variation. The type classification (father's education) is observed in the SHIW data and is used only for the normative evaluation, not for the positive model estimation — the same structural model applies to all types.

# Estimation / empirical strategy

1. **Structural estimation:** RURO labour supply models estimated by maximum likelihood on Italian 1993 SHIW data (estimates from Aaberge et al. 1999; details in the Electronic Supplementary Material).
2. **Type classification:** Individuals classified into 3 types by father's education.
3. **Equivalent income:** Disposable household income / $\sqrt{\text{household size}}$.
4. **Tax simulation:** For each candidate tax rule, simulate labour supply and compute the type-specific income distributions $F_1, F_2, F_3$.
5. **Welfare evaluation:** Compute $\tilde{W}_k$ for each $k$ and each candidate tax rule.
6. **Optimization:** Search over tax parameters $(c, t)$ or $(c, t_1, t_2)$ to maximize $\tilde{W}_k$ subject to revenue neutrality.

# Treatment of preferences

Preferences are modeled via the RURO framework with Box-Cox / exponential utility functions, taste-shifters for age, children, and household composition. In Italy, the marginal utility of consumption differs by employment status ($K_F, K_M$) to capture underground economy effects. Preferences are heterogeneous through observed demographics and random taste components $\varepsilon$ (Type I extreme value). The paper does not use a common welfare function for normative evaluation — instead it uses equivalent income (disposable income / $\sqrt{\text{household size}}$) as the welfare metric, avoiding the need for a reference preference ordering.

# Treatment of opportunities / constraints

Opportunity densities $p(h, w)$ with peaks at full-time hours (1846--2106 annual hours). Opportunity scale $g_0$ depends on region (North/South) and local unemployment. Italy has $g_0 < 1$ (rationing), rigid hours (full-time peak ~11--12x more prevalent than other hours), and strong regional disparities. **Crucially, opportunity densities are held fixed under counterfactual tax reforms** — only preferences respond to tax changes.

The paper does not explicitly model how father's education affects the opportunity set $A$. Types are defined by father's education for the normative criterion, but the positive model does not condition opportunity densities on parental background. The channel through which family background affects income runs through education, wages, and region (which do condition $g_0$), but this is not decomposed into a direct $A$-effect vs. an $R$-effect.

# Welfare / normative object

The paper's main normative contribution is the **extended EOp** family $\tilde{W}_k$:

$$\tilde{W}_k = \int_0^1 p_k(t) \min_j F_j^{-1}(t) \, dt$$

This criterion:
- For $k = \infty$: reduces to pure EOp ($\tilde{W}_\infty = \int \min_j F_j^{-1}(t) dt$) — only between-type inequality matters
- For finite $k$: also penalizes within-type inequality in the worst-off distribution
- For $k = 1$ (Bonferroni): maximum aversion to within-type inequality

The paper compares optimal taxes under EOp ($\tilde{W}_k$ for various $k$) vs. EO ($W_k$ for various $k$).

The paper uses **equivalent income** (not utility or a common welfare function) as the welfare metric. This means leisure is not valued in the welfare evaluation — a limitation the authors acknowledge (footnote 11: "inclusion of the value of leisure will be pursued in future work").

# Main findings

**Two-parameter (affine) optimal taxes (Table 2):**

| $k$ | MTR $t$ | Transfer $c$ (1000 ITL) |
|-----|---------|------------------------|
| 1 (Bonferroni) | 0.774 | 11,500 |
| 2 (Gini) | 0.637 | 9,500 |
| 3 | 0 | $-5,790$ |
| $\infty$ (utilitarian EOp) | 0 | $-5,790$ |

**Key finding:** For $k \geq 3$, the EOp-optimal affine tax is a **pure lump-sum tax** ($t = 0$, $c = -5,790$). Only when within-type inequality aversion is high ($k \leq 2$) do positive marginal tax rates emerge.

**Three-parameter optimal taxes (Table 7):**

| $k$ | $t_1$ | $t_2$ | $c$ (1000 ITL) |
|-----|--------|--------|----------------|
| 1 | 0.856 | 0.776 | 12,500 |
| 2 | 0.251 | 0.531 | 3,500 |
| 3 | 0 | 0.168 | $-3,500$ |
| $\infty$ | 0 | 0 | $-5,790$ |

**EOp vs. EO comparison (Tables 9, 11):**
- Under EO ($W_k$), the optimal tax is **always** a universal lump-sum tax ($t_1 = t_2 = 0$, positive $c$) when lump-sum taxes are feasible — regardless of inequality aversion $k$. This is the most "efficient" policy.
- Under EOp ($\tilde{W}_k$) with $k \leq 2$, the optimal policy involves positive marginal rates and larger transfers — more "redistributive."
- **Paradox:** "The EO criterion is more supportive of 'interventionist' (redistributive) policies than the EOp approach" is **reversed** — it is actually EOp with high within-type inequality aversion that prescribes higher marginal rates.

**Mechanism:** The most disadvantaged type (Type 1: low father's education) has the highest labour supply elasticity. Under the pure lump-sum tax, Type 1 individuals increase their labour supply by 13.37% (vs. +5.50% for Type 2 and +7.42% for Type 3). The efficiency gains from the lump-sum tax disproportionately benefit the worst-off type, making it EOp-optimal despite being disequalizing within types.

**Decomposition (Tables 4, 8):**
- Lump-sum tax (EOp3($\infty$)): highest efficiency ($\tilde{W}_\infty = 22,231$) but highest within-type inequality ($\tilde{C}_1 = 0.553$, $\tilde{C}_2 = 0.403$)
- EOp3(1): lower efficiency ($\tilde{W}_\infty = 15,393$) but much lower inequality ($\tilde{C}_1 = 0.176$, $\tilde{C}_2 = 0.116$)
- The trade-off between efficiency and within-type equality drives the sensitivity to $k$

**No-lump-sum-tax constraint (Tables 10--11):**
- When lump-sum taxes are not feasible, EOp and EO optimal rules converge more closely.
- Under EOp with $k = \infty$: flat tax at 31.3% with $c = 0$
- Under EO: same flat tax for $k \geq 2$; progressive for $k = 1$ (Bonferroni)

# Main limitations

- Welfare metric is equivalent income (disposable income / $\sqrt{n}$), not utility — leisure is not valued. Under the lump-sum tax, people work much more; if leisure has value, the lump-sum tax may be less desirable.
- Only 3 types defined by father's education — coarse classification may miss important circumstance variation.
- Father's education affects income through multiple channels (own education, wages, region, preferences) but the decomposition is not explicit.
- Opportunity densities held fixed under tax changes — partial equilibrium.
- Italian-specific results may not generalize (low participation, rigid hours, underground economy).
- The type classification does not condition the positive model — types enter only the normative criterion.
- Revenue neutrality at national level; regional effects not explored.

# Relevance for my JMP

## possible use for framing
The paper's key paradox — that EOp can be less redistributive than EO — provides a compelling motivation for carefully specifying the normative criterion. In my framework, the $W(z, R, A; y)$ measure makes the role of $A$ (feasible set) explicit, which should resolve this paradox by distinguishing between inequality due to $A$ (compensable) and inequality due to $R$ (responsibility).

## possible use for model design
The extended EOp criterion $\tilde{W}_k = \int p_k(t) \min_j F_j^{-1}(t) dt$ is a useful benchmark for my framework. The paper shows how to compute optimal taxes under this criterion using the RURO model — the same pipeline I can use for $W(z, R, A; y)$.

## possible use for identification
The paper uses father's education to define types (circumstances). In my framework, types correspond to different feasible sets $A$. The paper's finding that type classification matters for policy prescriptions motivates careful identification of $A$ in my framework.

## possible use for welfare measurement
The extended EOp family $\tilde{W}_k$ bridges EO and EOp by introducing within-type inequality aversion. My framework's $W(z, R, A; y)$ provides an alternative bridge — it is sensitive to both $A$ (like EOp) and $R$ (like EO), but through a different mechanism (the well-being measure itself rather than the aggregation rule).

## possible use for decomposition
The decomposition $\tilde{W}_k = \tilde{W}_\infty(1 - \tilde{C}_k)$ separates between-type effects (efficiency of the worst-off type) from within-type inequality. My framework could produce a richer decomposition by separating the contribution of $A$ from $R$ to both between-type and within-type inequality.

## possible use for comparative application
Italy provides a contrasting case to Norway (Aaberge & Colombino 2006, 2011, 2013): low participation, rigid hours, high elasticities for the disadvantaged. The finding that EOp favours lump-sum taxation in Italy (because disadvantaged types are very elastic) might reverse in Norway where elasticity patterns differ.

# Research questions this paper inspires

1. Does the paradox that EOp favours less redistribution than EO survive when leisure is included in the welfare metric? Under the lump-sum tax, Type 1 individuals work much more — if leisure matters, their welfare gain may be smaller.

2. How would the optimal taxes change if types were defined more finely (e.g., by father's education $\times$ region $\times$ gender) rather than just father's education?

3. In my framework, can $W(z, R, A; y)$ produce optimal taxes that avoid the EOp paradox by explicitly conditioning welfare on the feasible set $A$ rather than using a $\min_j$ operator over types?

4. Does the EOp vs. EO ranking of optimal policies depend on the country? In Norway (where the disadvantaged are less elastic than in Italy), would EOp be more redistributive than EO?

# Challenge to this paper

The paper's welfare metric — equivalent income (disposable income / $\sqrt{n}$) — ignores the value of leisure. This is particularly problematic for the key finding: the EOp-optimal lump-sum tax induces large labour supply increases among disadvantaged types (Table 5: Type 1 hours increase 13.37%). If leisure is valued, these individuals may not be better off despite higher income. The authors acknowledge this limitation (footnote 11) but do not address it. Additionally, the type classification by father's education is used only in the normative criterion, not in the positive model — the structural model treats all types identically in terms of preferences and opportunities. This means the paper cannot distinguish whether family background affects outcomes through preferences ($R$), opportunities ($A$), or both.

# Relation to my jobs_and_wellbeing framework

[Reasonable inference for my project] The extended EOp criterion $\tilde{W}_k = \int p_k(t) \min_j F_j^{-1}(t) dt$ evaluates welfare at the worst-off type for each effort quantile $t$. In my framework, types correspond to different feasible sets $A_j$, and the $\min_j$ operator implicitly compensates for differences in $A$. However, the paper's types are defined by father's education, which is a proxy for $A$ but also correlated with $R$ (preferences may differ by family background). My framework would handle this more cleanly by conditioning welfare directly on $A$, separating the $R$-component.

[Explicit in paper] The paper defines types by father's education (p. 746) and uses Roemer's (1998) framework where "differences in incomes within each type are assumed to be due to different degrees of effort" (p. 746). The extended EOp $\tilde{W}_k$ is explicitly introduced as a bridge between pure EOp and EO (eq. 2.6). The paper states: "the extended EOp welfare functions might be considered as a mixture of the pure EOp welfare function and the EO welfare functions" (p. 748).

[Unclear from paper] Whether the paper's welfare measure satisfies any of the axioms in my framework. Since the welfare metric is equivalent income (not utility-based), it does not directly correspond to any of my Measures 1--5. The $\min_j$ operator is a maximin over types, which is related to Full Compensation (compensate for differences in $A$), but the within-type inequality aversion ($p_k$) also partially compensates for effort differences, violating Full Responsibility. The paper does not discuss whether the extended EOp satisfies Independence of $\mathbf{y}$ or RAA.

The paper is closest to: **the EOp branch of the normative framework** — it operationalizes Roemer's theory with structural estimation, using types as proxies for circumstances ($A$). My framework replaces the $\min_j$ operator with a well-being measure that explicitly conditions on $A$.

# Relation to Bargain et al. (2013)

The paper shares the Italian SHIW data and RURO modelling framework with the broader Aaberge-Colombino literature that Bargain et al. (2013) build upon. However, Bargain et al. use heterogeneous preferences for welfare evaluation (computing equivalent income with individual utility functions), while this paper uses equivalent income without utility (disposable income / $\sqrt{n}$). Bargain et al. do not implement EOp criteria — they focus on EO with heterogeneous preferences. The extended EOp criterion $\tilde{W}_k$ developed here could be combined with Bargain et al.'s heterogeneous-preference welfare evaluation to produce a more complete framework. The finding that EOp favours less redistribution than EO challenges the presumption in Bargain et al. that accounting for preference heterogeneity necessarily leads to different policy conclusions.

# Relation to opportunities vs preferences

The paper treats family background (father's education) as a circumstance — something beyond individual control — and uses it to define types for the EOp criterion. However, the positive model does not separately identify how family background affects preferences ($R$) vs. opportunities ($A$). The structural model has the same preference and opportunity parameters for all types; types enter only through the normative criterion (the $\min_j$ operator). This means the paper cannot answer whether disadvantaged types have worse outcomes because they face fewer opportunities ($A$), because they have different preferences ($R$), or both. My framework, by explicitly modeling $A$ and $R$ as separate objects, could decompose the family background effect into these channels.

The paper's key empirical finding — that disadvantaged types have higher labour supply elasticity — is an interaction of $R$ and $A$: these individuals are at the extensive margin (low participation due to scarce opportunities and low wages), where elasticities are mechanically high. This suggests that the EOp-optimality of the lump-sum tax is driven by the opportunity structure ($A$) rather than by preferences ($R$).

# Useful quotations / formulas

**Extended EOp welfare function (eq. 2.6):**
$$\tilde{W}_k = \int_0^1 p_k(t) \min_j F_j^{-1}(t) \, dt, \quad k = 1, 2, \ldots$$

**Decomposition (eq. 2.8--2.9):**
$$\tilde{W}_k = \tilde{W}_\infty(1 - \tilde{C}_k)$$
$$\tilde{C}_k = 1 - \frac{\tilde{W}_k}{\tilde{W}_\infty}$$

**Pure EOp (eq. 2.5):**
$$\tilde{W}_\infty = \int_0^1 \min_j F_j^{-1}(t) \, dt$$

**Mixture distribution (eq. 2.7):**
$$\tilde{F}(x) = \max_j F_j(x)$$

**On the EOp paradox (p. 758):**
"It might appear paradoxical that, overall, EOp requires more redistribution (through marginal tax rates) than EO. However, the paradox is only apparent. EOp is motivated by a methodological position that focuses on inequality due to circumstances: but this position does not necessarily imply less redistribution — a consequence of EO and EOp being non-nested criteria."

**On the key mechanism (p. 753):**
"A possible explanation lies in the relatively high labour supply response of the least advantaged type... Since the EOp criterion requires the maximisation of a weighted average of the incomes of the least advantaged type, and since the labour supply of these individuals turns out to be very responsive to higher net wage rates, it follows that lower marginal tax rates... can in fact improve substantially the welfare of this group."

# Suggested tags

EOp, EO, extended-EOp, Roemer, optimal-taxation, family-background, circumstances, types, RURO, Italy, microsimulation, lump-sum-tax, affine-tax, rank-dependent-SWF, Bonferroni, Gini, within-type-inequality, labour-supply-elasticity

# My quick takeaway

This paper is essential for my JMP because it: (i) operationalizes Roemer's EOp criterion with a structural RURO model, providing a template for computing optimal taxes under responsibility-sensitive criteria; (ii) introduces the extended EOp family $\tilde{W}_k$ that bridges EO and EOp — a useful benchmark for my $W(z, R, A; y)$; and (iii) reveals the paradox that EOp can favour less redistribution than EO when the most disadvantaged type has the highest elasticity. For my framework, the key insight is that the $\min_j$ operator in EOp is a crude way to account for circumstances — it treats all within-type inequality as "effort" and all between-type inequality as "circumstance." My $W(z, R, A; y)$ provides a more nuanced approach by explicitly conditioning on the feasible set $A$, which could avoid the paradox and produce more defensible optimal tax prescriptions.
