---
title: "Do More Equal Slices Shrink the Cake? An Empirical Investigation of Tax-Transfer Reform Proposals in Italy"
authors: [Rolf Aaberge, Ugo Colombino, Steinar Strøm]
year: 2004
outlet: "Journal of Population Economics, 17(4), 767--785"
country_or_context: "Italy"
population: "Married couples, ages 18--54"
data_period: "1993"
shelf: "structural labour supply / tax reform / welfare evaluation"
tags: [RURO, discrete-choice, tax-reform, Italy, equivalent-income, social-welfare, efficiency-equality, NIT, workfare, microsimulation]
priority: "high"
read_status: "extracted"
---

# Full citation

Aaberge, R., Colombino, U., & Strøm, S. (2004). Do More Equal Slices Shrink the Cake? An Empirical Investigation of Tax-Transfer Reform Proposals in Italy. *Journal of Population Economics*, 17(4), 767--785.

# One-sentence contribution

Uses a structural RURO job-choice model estimated on Italian data to evaluate three tax-transfer reforms (flat tax, negative income tax, workfare) and shows that NIT and workfare can simultaneously improve both efficiency and equality — overcoming the conventional trade-off — because the largest behavioural responses come from poor households with high elasticities.

# Why this paper matters

This paper is one of the first to combine structural discrete-choice labour supply modelling with a rigorous **social welfare evaluation** that decomposes the proportionate social gain into an efficiency effect and an equality effect. It demonstrates that the conventional expectation — that flatter taxes help the rich more — is misleading when opportunity constraints and heterogeneous elasticities are properly accounted for.

# Core research question

Can the Italian tax-transfer system be reformed to simultaneously improve efficiency (bigger cake) and equality (more equal slices)? Specifically, what are the welfare effects of replacing the 1993 progressive tax with (i) a flat tax, (ii) a negative income tax (NIT), or (iii) a workfare (WF) scheme?

# Economic setting and context

Italy 1993: progressive individual income tax with 7 brackets (10%--51%), combined with a patchwork of family benefits and allowances that are widely regarded as inefficient and poorly targeted. Political debate between centre-right (flat tax) and centre-left (guaranteed income / social dividend) proposals.

# Model / theoretical framework

The paper uses the **Dagsvik (1994) RURO job-choice model** as estimated in Aaberge et al. (1999, 2000) on Italian SHIW 1993 data. This is both a positive (behavioural simulation) and normative (social welfare evaluation) exercise.

**What the agent chooses:** A married couple chooses a "job package" from a choice set $\Omega_i$ containing opportunities characterized by $(h_F, h_M, w_F, w_M, z)$ — hours and wages for each spouse plus unobserved job attributes.

**Feasible set:** The choice set is explicitly modeled through opportunity densities $p_i(h_F, h_M, w_F, w_M)$ that vary across households by gender, region, education, and local unemployment. Not all hours-wage combinations are equally available; full-time jobs are more prevalent than part-time (especially in Italy). The parameter $p^0_{ij}$ captures the fraction of feasible market opportunities relative to non-market ones, and $p^0 < 1$ implies rationing.

**Framework:** Both positive (predicting labour supply responses) and normative (evaluating welfare via equivalent income and social welfare functions).

# Key objects

- **Equivalent income** $y^k_i$: the exogenous income that would give a reference household S (facing reference choice set $\Omega_S$ and reference tax $R^S$) the same utility level as household $i$ attains under tax regime $k$ with its own choice set $\Omega_i$. Formally: $V_i(\Omega_i, m_i, R^k) = V_S(\Omega_S, y^k_i, R^S)$ (eq. 2.3--2.5).
- **Comparable Welfare Gain (CWG):** $CWG_i = y^1_i - y^0_i$ — the difference in equivalent incomes under the reform vs. the status quo.
- **Proportionate social gain:** $\xi_b = W_{b,1}/W_{b,0}$ — the ratio of social welfare under the reform to social welfare under the status quo, decomposed into efficiency ($\xi_\infty = \mu_1/\mu_0$) and equality ($(1-C_{b,1})/(1-C_{b,0})$) components (eq. 2.10--2.11).
- **Rank-dependent social welfare:** $W_{b,k} = \int_0^1 p_b(t) F_k^{-1}(t) dt$ with weight functions parameterized by inequality aversion $b$ (eq. 2.7--2.8).

# Data

1993 Bank of Italy Survey of Household Income and Wealth (SHIW93). Sample: 2,160 married couples, ages 18--54. Self-employed excluded (>20% of gross income from self-employment). Model estimated on the same data (estimates taken from Aaberge et al. 2000).

# Identification logic

Identification follows the standard RURO approach: the utility function is identified from variation in the tax-benefit function $f(\cdot)$ across income levels and household types (exploiting the non-linearities in the budget set), while the opportunity densities are identified from observed hours/wage distributions and the unemployment rate $\rho = (1-g_0)\varphi(0,0)$. The model is estimated by maximum likelihood using the McFadden (1978) procedure with 70 random draws per household. Identification is parametric; the Box-Cox utility form provides flexibility but imposes smoothness.

# Estimation / empirical strategy

Pre-estimated model from Aaberge et al. (1999, 2000). Simulations are performed by drawing random hours, wages, and taste shocks for each household and solving the utility maximization problem under each tax regime. Revenue-neutrality is imposed: the marginal tax rate under each reform is determined endogenously to match 1993 total tax revenue. Revenue-neutral rates: 18.4% (FT), 28.4% (NIT), 27.3% (WF).

# Treatment of preferences

Preferences are modeled via a Box-Cox utility function (eq. A.2) with taste-shifters for household size, age, and children. The functional form is flexible and does not impose a priori any specific pattern of supply elasticity with respect to income or wage. Preferences are heterogeneous both through observed demographics and through the random taste component $\varepsilon$ (Type I extreme value). The paper does not use a common/reference utility function for welfare evaluation — instead it uses equivalent income defined via a reference household.

# Treatment of opportunities / constraints

**This section is crucial.**

The paper **explicitly models opportunities** through the opportunity density $p_i(h_F, h_M, w_F, w_M)$, decomposed as:
- Conditional density of hours: uniform with a peak at full-time (for both genders in Italy, reflecting rigidity)
- Conditional density of wages: log-normal with education, experience, and region effects
- Scale parameter $p^0_{ij}$: proportion of market vs. non-market opportunities, modeled as logistic in region and local unemployment

The paper explicitly states (p. 775, 778--779) that the opportunity structure is crucial for explaining the simulation results:
- Part-time jobs are scarce in Italy, so the relevant margin for many women is between non-participation and full-time work
- This means that reforms that increase the net wage on full-time jobs (even if the entrance MTR rises) can still increase participation
- The interaction of reforms with quantity constraints explains why NIT and WF do not create "poverty traps"

The paper **does** help distinguish preference heterogeneity (through the utility parameters and random $\varepsilon$) from opportunity heterogeneity (through the $p^0$ and $g(\cdot)$ parameters). However, it does not decompose welfare into preference vs. opportunity components in the Fleurbaey-Maniquet sense.

# Welfare / normative object

The paper is **positive with explicit welfare applications**. The normative evaluation uses:

1. **Equivalent income** (King 1983 generalized): money-metric utility defined via a reference household, reference choice set, and reference tax system. The reference tax system is the flat tax (computationally convenient because $\partial f/\partial y$ is constant).

2. **Rank-dependent social welfare functions** with the Aaberge (2000) family of inequality measures $C_{b,k}$, which nests the Gini ($b=2$) and Bonferroni ($b=1$) as special cases.

3. **Proportionate social gain** $\xi_b = (\mu_1/\mu_0) \cdot (1-C_{b,1})/(1-C_{b,0})$ — decomposed into efficiency and equality effects.

The paper **does not** address responsibility vs. compensation explicitly. It does not distinguish between opportunity-driven and preference-driven components of welfare inequality. However, the use of a reference household and reference choice set for interpersonal comparability is conceptually close to the conditional equality approach.

# Main findings

**Elasticities (Table 1):** Female own-wage unconditional hours elasticity: 4.44 (poorest decile) to 0.06 (richest decile). Male: 0.32 to 0.06. Cross-elasticities are large and positive for poor women (0.82 in decile 1), explaining why male wage increases also boost female participation.

**Labour supply (Table 2):** All reforms increase total gross income. Female participation in poorest deciles increases under all reforms (even NIT and WF, contrary to poverty-trap expectations). Male labour supply barely changes. The largest contribution to the "bigger cake" comes from poor and middle-class households.

**Welfare distribution (Table 3):**
- FT: 51.8% winners; mean CWG = ITL 3,105; but FT is disequalising — poorest decile has negative mean CWG
- NIT: 55.0% winners; mean CWG = ITL 1,643; poorest decile has positive mean CWG (ITL 3,039) — equalising
- WF: 55.6% winners; mean CWG = ITL 1,724; poorest has positive CWG (ITL 2,750) — equalising

**Efficiency vs. equality (Tables 4--5):**
- All reforms are efficient ($\xi_\infty > 1$): efficiency gains of 2.1% (FT), 0.8% (NIT), 1.1% (WF)
- FT is disequalising (equality ratio < 1 for all $b$)
- NIT and WF are both efficient AND equalising — they overcome the efficiency-equality trade-off
- Under the Gini SWF ($b=2$): proportionate social gain is 0.9% (FT), 1.5% (NIT), 1.6% (WF)

**Key mechanism:** The benefits come from "unexpected directions" — the largest labour supply responses are from poor women (high elasticity), not from rich households. The reforms lower average tax rates and guarantee basic income, inducing participation among women who were previously at the extensive margin.

# Main limitations

- The model is estimated on 1993 Italian data; institutional features (especially the benefit system) have changed since then.
- Partial equilibrium: opportunity densities are held fixed under the reforms. If reforms increase participation substantially, $g_0$ and wage distributions might change.
- The welfare evaluation uses equivalent income with a reference household — the choice of reference household matters in principle (though the paper reports robustness to three different reference households).
- No explicit decomposition of welfare inequality into opportunity vs. preference components.
- The "poverty trap" non-result depends on the opportunity structure (scarcity of part-time) which is specific to Italy; the result might not hold in countries with flexible hours.
- Revenue-neutrality is imposed at the national level but the regional effects are not explored.

# Relevance for my JMP

## possible use for framing
The paper's key insight — that "more equal slices" need not shrink the cake — directly supports the argument that a properly designed tax-transfer system can improve welfare along both efficiency and equity dimensions. This is relevant when motivating why the $W(z,R,A;y)$ framework should be used for optimal policy design.

## possible use for model design
The RURO model with opportunity densities $p(h,w)$ and scale $p^0$ is the same class of model underlying your framework. The Italian specification (with rationing, regional variation, underground economy adjustments) shows how the model can be adapted to different institutional contexts.

## possible use for identification
The paper's identification strategy (exploiting non-linearities in the tax function, using unemployment rates to identify $g_0$) is directly transferable to your setting. The Box-Cox utility specification nests multiple functional forms.

## possible use for welfare measurement
The equivalent income approach (King 1983) with a reference household and reference tax system is a bridge between the Aaberge-Colombino literature and the Fleurbaey-Maniquet approach. In your framework, using a reference preference $\bar{R}$ for interpersonal comparability is conceptually parallel.

## possible use for decomposition
The decomposition $\xi_b = (\mu_1/\mu_0) \cdot (1-C_{b,1})/(1-C_{b,0})$ into efficiency and equality components is useful but **does not** separate opportunity-driven from preference-driven inequality. Your framework could extend this by decomposing the equality effect further into components attributable to $A$ vs. $R$.

## possible use for comparative application
Italy serves as a contrasting case to Norway: low female participation, rigid hours, high unemployment, underground economy. Cross-country variation in the efficiency-equality trade-off is driven by differences in $A$ (opportunity densities).

# Research questions this paper inspires

1. Can the decomposition $\xi_b = \text{efficiency} \times \text{equality}$ be further refined into $\text{equality}_{A}$ (opportunity-driven) and $\text{equality}_{R}$ (preference-driven) components using the $W(z,R,A;y)$ framework?

2. When NIT and WF overcome the efficiency-equality trade-off, is this because they primarily compensate for opportunity deficits ($A$) or for preference heterogeneity ($R$)?

3. How sensitive is the "poverty trap non-result" to the structure of the opportunity set? Would it hold in a country with flexible part-time availability (e.g., Norway)?

4. Could the equivalent income measure used here be replaced by a $W(z,R,A;y)$-based measure that explicitly separates responsibility from compensation?

# Challenge to this paper

The welfare evaluation uses equivalent income relative to a reference household, but does not distinguish whether welfare differences arise from differences in opportunities (which the individual does not control) or from differences in preferences (for which the individual may be held responsible). Two households with the same equivalent income could have very different levels of well-being in a framework that accounts for opportunity sets. The paper's normative conclusions — that NIT and WF are "equalising" — might be qualified if some of the inequality reduction comes from compensating individuals for their preference choices rather than for their opportunity deficits.

# Relation to my jobs_and_wellbeing framework

[Reasonable inference for my project] The paper's equivalent income measure $y^k_i$ is defined via a reference household with reference choice set $\Omega_S$ and reference tax rule $R^S$. This is conceptually close to Measure 5 (Reference Ability LF) in my `jobs_and_wellbeing.md` framework, where well-being is evaluated relative to a reference ability set $\bar{A}$. The key difference is that the paper's reference includes a reference *tax system* as well, not just a reference opportunity set. The paper satisfies something close to Independence of $A$ (since welfare is evaluated at the reference choice set $\Omega_S$), but it does not satisfy Independence of $\mathbf{y}$ (since the equivalent income depends on the tax rule, which depends on $\mathbf{y}$). The paper does not address responsibility for acquired ability (RAA) or Full Responsibility as defined in my framework. The efficiency-equality decomposition ($\xi_b$) could be enriched by my framework's distinction between compensation for $A$ and responsibility for $R$.

[Explicit in paper] The paper uses a reference household and reference choice set for interpersonal comparability (p. 770, eq. 2.3--2.5). The paper models opportunity sets explicitly through $p_i(h,w)$ and $p^0_{ij}$.

[Unclear from paper] Whether the paper's welfare measure is invariant to changes in $A$ when evaluated at the reference $\Omega_S$ — this depends on whether the reference household's utility level changes when $A$ changes.

The paper is closest to: **reference opportunity sets** and **decomposition of inequality** (efficiency vs. equality, but not opportunity vs. preference).

# Relation to Bargain et al. (2013)

The paper shares the same RURO modelling framework that Bargain et al. (2013) later use for welfare evaluation under heterogeneous preferences. However, this paper does not address the Fleurbaey-Maniquet distinction between preference-driven and opportunity-driven welfare differences. The equivalent income approach used here is a predecessor to the more refined welfare measures in Bargain et al., which explicitly impose a reference preference ordering for interpersonal comparability. The finding that poor households' behavioural responses drive the welfare gains is consistent with Bargain et al.'s emphasis on the importance of preference heterogeneity for welfare conclusions.

# Relation to opportunities vs preferences

The paper **models both** opportunity heterogeneity (through $p^0$ and $g(\cdot)$) and preference heterogeneity (through utility parameters and $\varepsilon$), but **does not decompose** welfare effects into components attributable to each. The key finding — that the largest responses come from poor women — is driven by the interaction of high elasticities (preference-related) with the structure of available jobs (opportunity-related). The paper does not attempt to say whether the poor benefit more from NIT/WF because their opportunity sets improve or because their preferences are better accommodated.

# Useful quotations / formulas

**Proportionate social gain decomposition:**
$$\xi_b = \frac{W_{b,1}}{W_{b,0}} = \frac{\mu_1}{\mu_0} \cdot \frac{1 - C_{b,1}}{1 - C_{b,0}}$$
(eq. 2.10)

**On opportunity constraints and poverty traps (p. 775):** "Note that a traditional model, where different job type availability is not taken into account, could not have captured such an effect."

**On the direction of reform benefits (p. 778):** "The benefits from the reforms seem to come from an unexpected direction... the largest response to the reforms in terms of hours comes from households belonging to low and average income deciles."

# Suggested tags

structural-labour-supply, RURO, Italy, tax-reform, flat-tax, NIT, workfare, equivalent-income, social-welfare, efficiency-equality-tradeoff, microsimulation, opportunity-density, King-1983, rank-dependent-SWF, Aaberge-inequality

# My quick takeaway

This paper shows that the efficiency-equality trade-off can be overcome in Italy by combining a flat marginal rate with guaranteed income (NIT) or workfare. The crucial mechanism is that the largest behavioural responses come from poor women whose high elasticities interact with the job opportunity structure. For my JMP, the paper is valuable as (i) an application of the RURO model with explicit opportunity constraints, (ii) a demonstration that welfare evaluation with equivalent income and reference households can yield nuanced policy conclusions, and (iii) motivation for extending the efficiency-equality decomposition to separate opportunity-driven from preference-driven inequality components — which is exactly what the $W(z,R,A;y)$ framework aims to do.
