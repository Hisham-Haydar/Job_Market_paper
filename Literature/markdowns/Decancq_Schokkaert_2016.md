---
title: "Beyond GDP: Using Equivalent Incomes to Measure Well-Being in Europe"
authors: [Koen Decancq, Erik Schokkaert]
year: 2016
outlet: "Social Indicators Research, 126, 21--55"
country_or_context: "18 European countries"
population: "General population (ESS respondents)"
data_period: "2008 and 2010 (European Social Survey waves 4 and 5)"
shelf: "welfare measurement / beyond GDP / equivalent income / life satisfaction / cross-country / inequality"
tags: [equivalent-income, beyond-GDP, life-satisfaction, preferences, multidimensional-wellbeing, health, unemployment, social-interactions, safety, inequality, S-Gini, Box-Cox, Europe, ESS, cross-country, Decancq, Schokkaert]
priority: "medium-high"
read_status: "extracted"
---

# Full citation

Decancq, K., & Schokkaert, E. (2016). Beyond GDP: Using Equivalent Incomes to Measure Well-Being in Europe. *Social Indicators Research*, 126, 21--55.

# One-sentence contribution

Proposes and implements a five-principle framework for measuring well-being beyond GDP -- individualistic, accounting for cumulative deprivation, respecting individual preferences, avoiding physical-condition neglect, and incorporating inequality aversion -- operationalised via equivalent incomes computed from life-satisfaction regressions on European Social Survey data for 18 countries in 2008 and 2010, showing that including non-income dimensions and inequality dramatically changes cross-country welfare rankings and growth assessments.

# Why this paper matters

This paper bridges the theoretical concept of equivalent income (Fleurbaey 2009, Fleurbaey & Maniquet 2011) and its empirical implementation using widely available survey data. It demonstrates that equivalent incomes can be computed from life-satisfaction regressions without structural labour supply models, making the approach accessible for large-scale cross-country comparisons. The paper is directly relevant to the JMP because it shows how the equivalent-income metric works in practice and what choices (reference values, preference estimation, inequality aversion) drive the results.

# Core research question

Can equivalent incomes be computed using life-satisfaction data to produce a coherent, preference-respecting, inequality-sensitive measure of well-being across European countries, and how does this measure differ from GDP per capita in levels and growth?

# Economic setting and context

18 European countries observed in 2008 (pre-/early crisis) and 2010 (post-crisis). The paper covers the financial crisis period, providing a test of whether equivalent incomes capture the welfare impact of the crisis differently from income alone.

# Model / theoretical framework

**Five principles for a well-being measure:**
1. **Focus on individual well-being** -- the measure should be individualistic
2. **Accounting for cumulative deprivation** -- aggregate row-by-row (individual level) before column-by-column (dimension level) to capture correlation of disadvantages
3. **Respect for individual preferences** -- use individual-specific weights for dimensions, not imposed weights
4. **Avoidance of physical-condition neglect** -- happiness/satisfaction should not be the sole metric due to adaptation
5. **Inequality aversion** -- the social welfare function should be distribution-sensitive

**Equivalent income definition:** The hypothetical income that, combined with the best possible value on all non-income dimensions ($\bar{x}$), would place the individual in a situation equally good as their actual situation:

$$y_i^* = y_i \exp\left(\frac{\beta + \gamma' z_i}{\mu + \pi' z_i}(f(x_i) - f(\bar{x}))\right)$$

where $y_i$ = actual income, $x_i$ = non-income dimensions, $z_i$ = personal characteristics affecting preferences, $f(\cdot)$ = Box-Cox transformation, $\beta, \gamma, \mu, \pi$ are estimated from the life-satisfaction regression.

**Life-satisfaction regression (eq. 3):**

$$S_i = \alpha + (\mu + \pi' z_i) \ln y_i + (\beta + \gamma' z_i)' f(x_i) + \delta' z_i + \varepsilon_i$$

Ordered logit estimation. The interaction terms $\pi' z_i$ and $\gamma' z_i$ allow heterogeneous preferences across demographic groups.

**Box-Cox transformation (eq. 4):**

$$f(v_i) = \frac{v_i^\tau - 1}{\tau}$$

Captures decreasing returns in each non-income dimension. $\tau$ estimated: health ($\tau = 0.62$), social interactions ($\tau = 0.34$), safety ($\tau = 0.95$), unemployment (binary).

**Social welfare (eq. 1):**

$$SW = M(1 - I_\rho)$$

where $M$ = mean equivalent income, $I_\rho$ = S-Gini inequality index with bottom-sensitivity parameter $\rho$. $\rho = 1$: utilitarian (no inequality aversion); $\rho = 2$: Gini; $\rho = 5$: strong bottom-sensitivity; $\rho \to \infty$: Rawlsian.

# Key objects

- **Equivalent income $y_i^*$:** Always $\leq y_i$ (since non-income dimensions are below their best possible values). The gap $y_i - y_i^*$ = willingness-to-pay for reaching perfect non-income conditions.
- **Life-satisfaction regression coefficients ($\mu, \beta, \gamma, \pi$):** Determine the weights on income and non-income dimensions in equivalent income. Estimated from ordered logit on pooled ESS data ($N = 52{,}137$).
- **S-Gini inequality index $I_\rho$:** Inequality in equivalent incomes, with $\rho$ controlling bottom-sensitivity.
- **Non-income dimensions (Table 4):** Health (self-reported, 1--5), unemployment (binary), social interactions (frequency of meeting friends, 1--7), safety (feeling safe walking alone at night, 1--4).
- **Reference values $\bar{x}$:** Best possible: very good health, employed, meet friends daily, feel very safe.

# Data

European Social Survey (ESS), waves 4 (2008) and 5 (2010). 18 countries: Belgium, Switzerland, Czech Republic, Germany, Denmark, Estonia, Spain, Finland, France, Great Britain, Greece, Hungary, Netherlands, Norway, Poland, Russia, Sweden, Slovenia. $N \approx 52{,}000$ pooled. Income measured as household income decile (uprated to PPP-adjusted monetary values using OECD Real Net National Income).

# Identification logic

Preferences are identified from the life-satisfaction regression: the relative weight individuals place on income vs. non-income dimensions is revealed by how these dimensions correlate with life satisfaction, conditional on personal characteristics ($z_i$). The interaction terms ($\pi' z_i$, $\gamma' z_i$) identify group-level preference heterogeneity (by age, gender, education). The approach assumes that the relative importance individuals report in their satisfaction responses reflects their true preferences (even though satisfaction levels may be distorted by adaptation).

Key identification assumption: satisfaction levels may be subject to aspiration effects (captured by $\delta' z_i$), but the relative importance of different dimensions is not. This is why equivalent incomes are immune to aspiration effects by construction: the $z_i$ terms in the denominator and numerator cancel out (eq. 5).

# Estimation / empirical strategy

1. Pool ESS data across 18 countries and both waves ($N = 52{,}137$)
2. Estimate ordered logit of life satisfaction on $\ln y_i$, Box-Cox transformed non-income dimensions, interaction terms, and controls ($z_i$: age, gender, education, marital status, religion, urban, ethnic minority, country and time dummies)
3. Compute equivalent income $y_i^*$ for each individual using eq. (5)
4. Compute mean, inequality, and social welfare ($SW = M(1 - I_\rho)$) for each country-year
5. Decompose contributions of each dimension to the gap between income and equivalent income (Table 8)
6. Compare growth rates in income vs. equivalent income vs. social welfare (Table 12)

# Treatment of preferences

Preferences are estimated from life-satisfaction regressions, not from structural choice models. This is a key methodological choice: the paper uses stated preferences (satisfaction responses) rather than revealed preferences (labour supply choices). The advantage is generality (covers health, safety, social interactions -- not just labour supply). The limitation is that it can only capture group-level preference heterogeneity (by demographic characteristics $z_i$), not individual-level heterogeneity.

The paper explicitly notes three methods for estimating preferences for equivalent incomes: (1) revealed preferences from labour market choices (Bargain et al. 2013), (2) stated preferences / contingent valuation (Fleurbaey et al. 2013), (3) life-satisfaction regressions (this paper). Each has strengths and weaknesses.

Key result on preferences: women and higher-educated individuals have a higher coefficient on income ($\mu + \pi' z_i$). Women care less about unemployment and safety than men. Young people care less about health.

# Treatment of opportunities / constraints

Not explicitly modelled. Unemployment enters as a non-income dimension of well-being, but there is no distinction between voluntary and involuntary unemployment, no job availability, no opportunity density. The equivalent income captures the welfare cost of being unemployed (relative to being employed), but does not decompose this cost into preference-driven and opportunity-driven components.

# Welfare / normative object

Social welfare = $SW = M(1 - I_\rho)$ where $M$ = mean equivalent income and $I_\rho$ = S-Gini inequality index. The parameter $\rho$ captures the degree of inequality aversion / bottom-sensitivity. The paper presents results for $\rho = 1$ (utilitarian), $\rho = 2$ (Gini), $\rho = 5$ (strong bottom-sensitivity).

# Main findings

1. **Equivalent incomes change country rankings substantially (Table 7).** Germany drops from rank 7 to 12 in average equivalent income (worse health self-reports). Denmark improves from rank 6 to 2. Norway stays at the top.

2. **Health is the most important non-income dimension (Table 8).** Health reduces average equivalent income by 61--91% relative to actual income. Social interactions reduce it by 33--57%. Safety: 19--44%. Unemployment: 1--4%. Total non-income effect: 72--94% reduction.

3. **Inequality in equivalent incomes is much higher than in monetary incomes (Table 9).** For all countries, the Gini of equivalent incomes exceeds the Gini of monetary incomes. This is cumulative deprivation: those with low income also tend to have worse health, more unemployment, less social interaction, and less safety.

4. **Growth in well-being differs markedly from income growth during the financial crisis (Table 12).** Most countries experienced negative equivalent-income growth even when income growth was positive or small. Greece's social welfare growth was $-25\%$ with bottom-sensitivity ($\rho = 5$), reflecting the severe impact of the crisis on the worst-off. Switzerland had the best performance.

5. **Distribution-sensitivity matters (Tables 10--12).** Introducing inequality aversion ($\rho > 1$) changes both the level ranking and the growth ranking. Countries with high inequality in equivalent incomes (e.g., Great Britain, Russia) do worse with higher $\rho$; Scandinavian countries do better.

6. **Preference heterogeneity matters.** Women and higher-educated individuals weight income more heavily. Young people weight health less. These group-level differences affect equivalent incomes through the interaction terms in eq. (5).

# Main limitations

- Life-satisfaction-based preference estimation captures only group-level heterogeneity, not individual-level
- Self-assessed health may be subject to cross-country differences in reporting style
- ESS income data are crude (deciles, not continuous)
- No panel data → cannot control for individual fixed effects (personality traits)
- Subjective variables (health, safety) may be endogenous with life satisfaction
- No labour supply modelling, no distinction between voluntary and involuntary unemployment
- Reference values ($\bar{x}$) chosen as "best possible" -- other choices would affect levels (though not rankings within a given reference)
- No structural model of how policies affect outcomes

# Relevance for my JMP

## possible use for welfare metric comparison
The paper demonstrates an alternative way to compute equivalent incomes -- from life-satisfaction regressions rather than from structural labour supply models. For my JMP, this provides a useful comparison: are the equivalent incomes from the RURO structural model consistent with those from life-satisfaction data? If both approaches yield similar welfare rankings, this cross-validates the welfare metric. If they diverge, the divergence may reveal where structural assumptions matter most.

## possible use for the role of non-income dimensions
The paper shows that health, social interactions, and safety matter enormously for equivalent incomes (Table 8: health alone reduces equivalent income by 61--91%). In the RURO framework, the key non-income dimensions are job availability ($A$) and leisure/hours. The paper's finding that unemployment has a relatively small average effect on equivalent income (1--4%) but a very large effect on the unemployed subpopulation is relevant: the RURO framework's explicit modelling of involuntary non-participation may capture welfare effects that are averaged away in population-level measures.

## possible use for the five principles
The five principles provide a checklist for evaluating the JMP's welfare metric: (1) individualistic -- yes (individual equivalent incomes from RURO); (2) cumulative deprivation -- yes (individual-level aggregation); (3) respect for preferences -- yes (individual preferences $v(C, T-h)$ from RURO); (4) avoidance of physical-condition neglect -- yes (equivalent income, not satisfaction); (5) inequality aversion -- yes (can apply maximin/leximin to equivalent incomes). The RURO-based metric satisfies all five principles.

# Research questions this paper inspires

1. Can the life-satisfaction approach and the structural labour supply approach to equivalent incomes be reconciled? The life-satisfaction approach estimates willingness-to-pay for health, safety, etc. from satisfaction regressions. The structural approach estimates willingness-to-pay for leisure/job characteristics from choice behaviour. Are these consistent?

2. The paper finds that unemployment has a small average effect but a large effect on the unemployed. In the RURO framework, what is the equivalent-income cost of reduced opportunity density $g(h,w)$? Is it comparable to the unemployment coefficient in the satisfaction regression?

3. The paper's preference heterogeneity is at the group level (by demographics). The RURO framework provides individual-level preference heterogeneity (via the structural utility parameters). Does this finer heterogeneity change welfare rankings?

# Challenge to this paper

The paper's use of life-satisfaction regressions to estimate preferences has a fundamental limitation: it cannot distinguish between the effect of a life dimension on satisfaction (which may reflect adaptation) and its effect on welfare (which should reflect deep preferences). The paper argues that the relative importance of dimensions in satisfaction regressions reflects true preferences even if satisfaction levels are distorted by adaptation. But this assumption is untestable: if adaptation affects the relative importance of dimensions (not just the level of satisfaction), the preference estimates and hence the equivalent incomes will be biased. The structural approach (Bargain et al. 2013, RURO) avoids this by estimating preferences from revealed behaviour (labour supply choices), which is less susceptible to adaptation bias -- though it introduces its own assumption that choices reflect preferences rather than constraints.

Moreover, the paper's treatment of unemployment as a non-income dimension of well-being conflates voluntary and involuntary unemployment. The equivalent-income cost of unemployment is assumed to be the same whether the individual chose not to work or was unable to find a job. The RURO framework distinguishes these cases through the opportunity density $g(h,w)$.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The paper computes equivalent incomes $y_i^*$ -- the income at reference non-income conditions that yields the same well-being as the actual situation. In $W(z, R, A; y)$ terms: $y_i^*$ is the income at reference $\bar{A}$ (best employment) and reference non-income dimensions ($\bar{x}$) that makes $i$ as well off as under actual $(z_i, R_i, A_i, y_i)$. The paper captures $z$ (outcomes), $R$ (preferences from satisfaction), and $y$ (income), but not $A$ (opportunity set) separately.

[Reasonable inference for my project] The paper's equivalent income can be decomposed as: $\ln y_i^* = \ln y_i + \frac{\beta + \gamma' z_i}{\mu + \pi' z_i}(f(x_i) - f(\bar{x}))$. In the RURO framework, an analogous decomposition would be: $\ln y_i^* = \ln y_i + \text{WTP for leisure gap} + \text{WTP for opportunity gap}$, where the leisure WTP comes from preferences $v(C, T-h)$ and the opportunity WTP comes from the opportunity density $g(h,w)$. The RURO decomposition provides the $R$-$A$ separation that the satisfaction-based approach cannot.

[Unclear from paper] Whether the satisfaction-based preference estimates are consistent with structural estimates from labour supply models. The paper notes three methods for estimating preferences (p. 36) and acknowledges that "it would certainly be advisable to compare the results obtained with each of them" (p. 52).

# Relation to Bargain et al. (2013)

The paper explicitly cites Bargain et al. (2013) as using revealed preferences from labour market data to compute equivalent incomes. The two approaches are complementary: Bargain et al. estimate preferences from labour supply choices (structural model), while Decancq-Schokkaert estimate preferences from life-satisfaction regressions (reduced-form). The structural approach is more rigorous for the labour supply dimension but limited to income-leisure trade-offs. The satisfaction approach can incorporate health, safety, social interactions -- dimensions that the labour supply model does not cover. My JMP focuses on the labour supply dimension (RURO), but the Decancq-Schokkaert approach could extend the welfare metric to include non-labour dimensions.

# Relation to opportunities vs preferences

The paper does not distinguish opportunities from preferences. Unemployment enters as a non-income outcome, not as a constraint. The equivalent income measures the welfare cost of unemployment regardless of whether it is voluntary or involuntary. In the RURO framework, the welfare cost of involuntary unemployment (limited $g(h,w)$) is conceptually different from the welfare cost of choosing not to work (preferences $v(C, T-h)$). The satisfaction-based approach cannot make this distinction because it observes outcomes, not the choice set.

# Useful quotations / formulas

**Equivalent income definition (p. 35):**
"The equivalent income of an individual is the hypothetical income that, if combined with the best possible value on all non-income dimensions, would place the individual in a situation that he/she finds equally good as his/her actual situation."

**On respecting preferences (Principle 3, p. 29):**
"The weighting scheme applied to construct the measure of individual well-being should respect the individual ideas about what is a good life."

**On physical-condition neglect (Principle 4, p. 30):**
"Happiness (or subjective life satisfaction) may be one of the important dimensions of life, but it should not be seen as an encompassing measure of individual well-being."

**On cumulative deprivation (p. 28):**
"If one cares about cumulative deprivation, one has to summarize the information in Table 2 row-by-row rather than column-by-column."

**Key formula (eq. 5):**
$$y_i^* = y_i \exp\left(\frac{\beta + \gamma' z_i}{\mu + \pi' z_i}(f(x_i) - f(\bar{x}))\right)$$

**Social welfare (eq. 1):**
$$SW = M(1 - I_\rho)$$

# Suggested tags

equivalent-income, beyond-GDP, life-satisfaction, preferences, multidimensional-wellbeing, health, unemployment, social-interactions, safety, inequality, S-Gini, Box-Cox, cumulative-deprivation, Europe, ESS, cross-country, financial-crisis, social-welfare, Decancq, Schokkaert

# My quick takeaway

An accessible and empirically rich implementation of the equivalent-income approach to measuring well-being across Europe. The paper demonstrates that non-income dimensions (especially health and social interactions) dramatically reduce equivalent incomes relative to monetary incomes, and that inequality in equivalent incomes is much higher than income inequality due to cumulative deprivation. For my JMP, the paper provides: (1) a useful comparison method -- equivalent incomes from satisfaction regressions vs. from structural labour supply models; (2) a five-principle checklist that the RURO-based welfare metric satisfies; (3) evidence that the labour supply dimension (unemployment) has a relatively small population-average effect on equivalent income but a very large effect on the affected individuals -- motivating the RURO framework's explicit modelling of the opportunity set. The key gap the RURO framework fills relative to this paper: structural decomposition of equivalent-income differences into preferences ($R$) and opportunities ($A$), and the distinction between voluntary and involuntary non-employment.
