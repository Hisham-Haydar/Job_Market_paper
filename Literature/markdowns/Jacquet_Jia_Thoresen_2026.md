---
title: "How Much Does Responsibility Matter in Fairness Measurement?"
authors: [Laurence Jacquet, Zhiyang Jia, Thor O. Thoresen]
year: 2026
outlet: "CESifo Working Paper No. 12418"
country_or_context: "Norway"
population: "Married couples (with or without children)"
data_period: "2015 cross-section (Labour Force Survey + Income and Wealth Statistics); reform period 2013-2019"
shelf: "responsibility_fairness_welfare"
tags: [compensating variation, fairness, responsibility, preferences, circumstances, job choice model, latent jobs, discrete choice, tax reform, microsimulation, Norway, RURO, conditional equality, reference preferences]
priority: "very high"
read_status: "extracted"
---

# Full citation

Jacquet, L., Z. Jia, and T. O. Thoresen (2026). "How Much Does Responsibility Matter in Fairness Measurement?" CESifo Working Paper No. 12418, January 2026.

# One-sentence contribution

The paper develops a new empirical method to measure the importance of individual responsibility in the distribution of welfare by comparing standard Compensating Variation (CV) with a "circumstance-only" CV (CV^circ) that neutralizes preference heterogeneity, using a structural job choice labor supply model estimated on Norwegian data.

# Why this paper matters

This paper is directly at the intersection of structural labor supply estimation, fairness measurement, and the responsibility-versus-circumstances distinction. It operationalizes the conceptual separation between preferences (responsibility) and circumstances (job opportunities) through the Dagsvik (1994) / Dagsvik and Jia (2016) job choice model, which intrinsically separates these two sources of heterogeneity. By constructing CV^circ --- a welfare metric that holds preferences fixed at a reference value while allowing only circumstance-driven heterogeneity --- it provides a concrete empirical test of how much responsibility matters for fairness assessments of tax reforms. The paper also implements the Conditional Equality (CE) criterion of Fleurbaey (2008) as a robustness check, connecting the structural labor supply literature to the normative fairness literature.

# Core research question

How much does it matter empirically whether welfare measurement of tax reforms accounts for individual responsibility (preference heterogeneity) versus circumstances (opportunity heterogeneity), and where in the income distribution does the distinction bite?

# Economic setting and context

The paper studies the Norwegian 2013--2019 "bracket tax" reform, which increased the number of brackets in the piecewise linear tax on labor income while generally reducing marginal tax rates. Norway uses a dual income tax system combining a low proportional rate on capital income and progressive rates on labor income. The reform replaced a two-tier surtax with a multi-bracket system. The analysis focuses on married couples under individual taxation.

# Model / theoretical framework

The model class is a structural discrete choice labor supply model --- specifically, the "job choice" model of Dagsvik (1994) and Dagsvik and Jia (2016). This is a Random Utility / Random Opportunity (RURO) model.

The agent (household) chooses a latent job characterized by hours of work and non-pecuniary attributes. The utility function takes the form:

$$U(C, h_F, h_M, z) = u(C, h_F, h_M) + \varepsilon(z)$$

where $u(\cdot)$ is a deterministic component capturing preferences over consumption and leisure, and $\varepsilon(z)$ is a stochastic taste-shifter for job-specific non-pecuniary attributes.

The feasible set is explicitly modeled. For each hours level $h$, individuals face a latent set of jobs $B(h)$ with $Q(h)$ available jobs. The total number of market opportunities relative to non-market opportunities is $\theta = \sum_{h>0} Q(h)$. For females, $\log \theta_F = \gamma_{F1} + \gamma_{F2} S$ where $S$ is years of schooling. For males, $\theta_M$ is normalized to one (near-universal employment).

The framework is both positive and normative. The positive part estimates preferences and opportunity measures. The normative part constructs three welfare metrics: CV, CV^circ, and $\Delta$CE.

The framework can be directly interpreted through $W(z, R, A; y)$-type objects. The indirect utility function decomposes as $V(h_F, h_M, I) = u(f(\cdot), h_F, h_M) + \log Q_F(h_F) + \log Q_M(h_M) + \eta$, where the first term reflects preferences $R$, the $\log Q$ terms reflect the feasible job set $A$, and the budget constraint through $f(\cdot)$ reflects the pay schedule $y$.

# Key objects

**CV (Compensating Variation):** The monetary transfer that equates pre- and post-reform maximized utility, preserving each household's own preferences and opportunity set.

**CV^circ (Circumstance-only CV):** CV computed under reference (common) preferences --- taste-modifying variables are set to sample median, and a common random utility component is used. Only circumstance heterogeneity (job opportunities, wages, non-labor income) remains.

**$\Delta$CE (change in Conditional Equality):** Welfare change measured by comparing CE levels before and after the reform, where CE is the maximum utility achievable on a hypothetical equivalent linear budget set evaluated with reference preferences $\bar{\gamma}$.

**$\theta$ (opportunity measure):** The relative size of the job opportunity set compared to non-market opportunities.

**$g(h)$ (opportunity density):** The share of available jobs at hours level $h$.

**Reference preferences $\bar{\gamma}$:** Common preference parameters obtained by setting taste-modifying variables (gender, age, number of children) to their sample medians.

# Data

Cross-sectional data for 2015 from the Norwegian Labour Force Survey merged with Income and Wealth Statistics of Households (Statistics Norway). The sample consists of 1,594 married couples. Self-employed couples and those with self-employment income above NOK 115,000 are excluded. Couples with weekly hours above 80 or wage rates outside NOK [70, 600] are excluded. The tax-benefit model from the LOTTE microsimulation family is used to transform gross income into disposable income.

# Identification logic

The job choice model is identified from cross-sectional variation in hours of work conditional on wages and non-labor income. The key identification features are: (1) the preference parameters are identified from variation in hours choices conditional on budget constraints; (2) the opportunity measure $\theta_F$ is identified from the residual variation in hours choices not explained by preferences, modeled as a function of education; (3) the separation between preferences and circumstances follows from the additive structure of the indirect utility: $u(\cdot)$ for preferences and $\log Q(\cdot)$ for circumstances.

The identification of CV versus CV^circ relies on: for CV, each household's own estimated preference parameters are used; for CV^circ, all households share the same reference preferences, so any remaining heterogeneity in welfare effects is attributable only to circumstances.

# Estimation / empirical strategy

The model is estimated by Maximum Likelihood within a Conditional Logit framework. Spouses choose among 56 possible combinations of job and non-market alternatives (7 discrete options for men, 8 for women). The deterministic utility adopts a Box-Cox specification (Equation 4.10 in the paper) with 15 parameters ($\alpha_1$ through $\alpha_{15}$) plus subsistence levels.

CV and CV^circ are computed via McFadden's (1999) simulation approach: for each household, $K$ sets of random utility error terms are drawn from the standard Gumbel distribution, and CV is obtained by numerically solving the equation that equates pre- and post-reform maximized utility for each draw. The mean across draws gives the household's CV estimate.

For the CE criterion, equivalent linear budget sets are constructed for each household, reference utility is computed, and $\Delta CE_i = CE_{1,i} - CE_{0,i}$ is obtained for each household.

# Treatment of preferences

Preferences are modeled with rich observed heterogeneity through taste-modifying variables in the Box-Cox utility specification. For females, preferences for leisure depend on age (log and squared), number of children (below 6, above 6). For males, similarly. There is also a leisure interaction term between spouses. The stochastic error $\varepsilon(z)$ captures unobserved preference heterogeneity across jobs.

Key finding: for women, age and number of children are significant regressors capturing heterogeneity of preferences for leisure. Being a woman and being with children is associated with greater leisure preference.

The paper explicitly distinguishes between preferences as "responsibility" characteristics (for which individuals are held accountable) and circumstances (which call for compensation). Preferences are treated as tastes, not needs, following Kaplow (2008) and Lockwood and Weinzierl (2015).

# Treatment of opportunities / constraints

This section is crucial and the paper handles it exceptionally well for the purposes of a $W(z, R, A; y)$ framework.

The paper **models opportunities explicitly** through the latent job set $B(h)$ with $Q(h)$ jobs available at each hours level. The opportunity measure $\theta$ captures the total market opportunity set relative to non-market alternatives. For females, $\theta_F$ depends on education. For males, it is normalized to one.

The paper **uses latent jobs** --- jobs are the fundamental choice variable, characterized by given hours, a wage rate, and non-pecuniary attributes. The number of latent jobs at each hours level is not observed and must be estimated jointly with preference parameters.

The paper **does not assume a universal choice set** --- the number of available jobs $Q(h)$ varies across individuals (through $\theta$) and across hours levels (through the opportunity density $g(h)$, which has peaks at full-time and part-time hours).

The paper **uses hours restrictions** implicitly through the opportunity density $g(h)$, which is uniform for non-standard hours but peaks at part-time and full-time.

The paper **does not ignore demand-side constraints** --- the opportunity measure $\theta$ and density $g(h)$ are precisely the demand-side constraints that enter the model.

The paper **explicitly distinguishes preference heterogeneity and opportunity heterogeneity**: this is the central contribution. The indirect utility decomposes additively into a preference component ($u + \eta$) and an opportunity component ($\log Q_F + \log Q_M$). CV captures both; CV^circ neutralizes the former; the difference isolates the role of preferences (responsibility).

# Welfare / normative object

The paper uses three welfare objects:

1. **CV (standard):** Money metric utility measuring the income transfer needed to restore pre-reform utility. Respects each household's actual preferences and circumstances.

2. **CV^circ (circumstance-only CV):** A modified CV where all households are assigned common reference preferences (median taste-modifying variables and common error term). Only circumstance-driven welfare differences remain. This is responsibility-sensitive.

3. **$\Delta$CE (Conditional Equality change):** Based on the CE criterion of Fleurbaey (2008) and empirically implemented following Carpantier and Sapata (2016). CE assigns welfare by maximizing reference-preference utility over a hypothetical equivalent linear budget set. $\Delta$CE = $CE_1 - CE_0$ measures welfare change between tax regimes.

The paper is **positive with explicit normative (fairness) applications**. It is explicitly normative in that it connects to the Conditional Equality criterion and the responsibility-sensitive egalitarian tradition (Fleurbaey 2008; Roemer and Trannoy 2016).

The paper is directly useful for thinking about:
- **Responsibility for opportunities:** The entire paper is built around this distinction. CV^circ holds individuals responsible for preferences but not for circumstances.
- **Compensation for opportunities:** By isolating circumstance-driven welfare effects, the paper shows where compensation for unequal opportunities would be most needed.
- **Actual opportunity sets versus reference opportunity sets:** The paper keeps actual opportunity sets ($Q$) throughout but replaces actual preferences with reference preferences ($\bar{\gamma}$).
- **Decomposition of inequality:** The comparison of CV and CV^circ across the income distribution is itself a decomposition of welfare effects into responsibility and circumstance components.

# Main findings

1. Average welfare effects of the bracket tax reform are similar under CV (NOK 18,384) and CV^circ (NOK 18,677), with CV^circ showing slightly lower dispersion (SD 5,188 vs 5,458).

2. CV and CV^circ follow the same pattern across income deciles 1 through 9: welfare first increases then drops sharply at decile 10.

3. The two metrics differ significantly **only at the very top** of the household income distribution (decile 10), where CV^circ shows larger welfare gains than CV. The mechanism is that high-income women have stronger leisure preferences, which are neutralized under CV^circ.

4. The transition matrix between CV and CV^circ quintile rankings shows 71--93% of households remain in the same quintile.

5. $\Delta$CE and CV^circ yield very similar distributional patterns, confirming that the two responsibility-sensitive approaches are empirically aligned.

6. The main conclusion is that, for this particular reform and country, **preferences may not matter much in fairness measurement, except at the very top of the income distribution**.

# Main limitations

**Identification limits:** The opportunity measure $\theta_F$ is identified only through education, which is a crude proxy. Male opportunities are not identified (normalized to one). The separation between preferences and circumstances rests on the additive structure of indirect utility, which is a strong functional form assumption.

**Treatment of opportunities:** While the model explicitly incorporates job opportunities, these are parametrically specified and depend only on education. Richer circumstance variables (e.g., region, sector, employer characteristics) could alter the opportunity measure substantially.

**Welfare interpretation:** The finding that "responsibility doesn't matter much" is specific to the Norwegian context and this particular reform. The authors explicitly note this may not hold for other countries or reforms. The result may also depend on the choice of reference preferences (median values).

**Choice-set assumptions:** The Gumbel distributional assumption for $\varepsilon(z)$ and the specific Box-Cox functional form may affect results. The paper uses 56 discrete alternatives for couples.

**Relevance for decomposition:** The paper does not perform a full decomposition of inequality into preferences, opportunities, and other factors. It compares two aggregate welfare measures rather than decomposing individual welfare.

**Integration with $W(z, R, A; y)$:** The paper is highly compatible with a $W(z, R, A; y)$ framework. The main limitation is that $A$ is modeled only through $\theta$ and $g(h)$, and $y$ is given by the tax-benefit system. A richer specification of $A$ (e.g., with occupation- or sector-specific constraints) would strengthen the connection.

# Relevance for my JMP

## possible use for framing

This paper provides a direct and contemporary framing for any JMP that seeks to connect structural labor supply models with fairness/responsibility considerations. The paper's central argument --- that the job choice model is "particularly well-suited for applied fairness analysis, as it accounts for the preference/circumstance distinction" --- is directly applicable. The comparison between CV and CV^circ can serve as a template for the kind of welfare analysis a JMP could extend.

## possible use for model design

The paper's use of the Dagsvik (1994) / Dagsvik and Jia (2016) job choice model, with its additive decomposition of indirect utility into preference and opportunity components, is directly relevant for model design. The indirect utility $V = u(\cdot) + \log Q_F + \log Q_M + \eta$ cleanly separates $R$ and $A$. The paper also shows how to construct CV^circ by substituting reference preferences, which provides a blueprint for constructing alternative welfare measures.

## possible use for identification

The identification strategy for $\theta_F$ (through education) and the normalization $\theta_M = 1$ are useful reference points, though limited. The paper's approach to computing CV via McFadden's simulation method (drawing $K$ Gumbel error terms) is a practical identification/computation strategy for welfare metrics in discrete choice models.

## possible use for welfare measurement

This is the paper's primary contribution to the JMP. CV^circ provides a concrete welfare object that can be interpreted as $W(z, \bar{R}, A; y)$ --- well-being evaluated at reference preferences but actual circumstances. The CE criterion provides an alternative fairness-sensitive welfare measure. Both can be implemented within a job choice model framework.

## possible use for decomposition

The paper implicitly decomposes welfare effects into a "preference component" (CV - CV^circ) and a "circumstance component" (CV^circ). This is a two-way decomposition rather than a full decomposition. A JMP could extend this by providing finer decompositions (e.g., separating opportunity heterogeneity from wage heterogeneity from non-labor income heterogeneity).

## possible use for comparative application

The paper notes that "this finding may not hold for other countries or other reforms," explicitly suggesting cross-country replication. The methodology is portable to any country with a structural labor supply model and a microsimulation tax-benefit calculator.

# Research questions this paper inspires

1. If one enriches the opportunity measure $\theta$ with occupation, sector, and regional variation (rather than education alone), does the preference/circumstance distinction become more pronounced across the income distribution?

2. Can one construct a full decomposition of CV into components attributable to preference heterogeneity, opportunity heterogeneity, wage heterogeneity, and non-labor income heterogeneity?

3. Does the finding that "responsibility matters only at the top" hold in countries with greater labor market segmentation or more heterogeneous opportunity sets?

4. How does the choice of reference preferences $\bar{\gamma}$ (median vs. other quantiles) affect the CV^circ welfare ranking, and can one construct bounds on the welfare effect that are robust to the reference choice?

5. Can the CV^pref alternative (neutralizing circumstances instead of preferences) be used to construct a complementary decomposition, and how does it relate to the $W(z, R, A; y)$ framework?

# Challenge to this paper

The paper's main finding --- that responsibility matters only at the top --- rests on a relatively parsimonious specification of opportunities (education only for women, normalized for men). If the true opportunity set is richer and more heterogeneous (varying by region, age, occupation, employer type), then the gap between CV and CV^circ could be larger across the entire distribution, not just at the top. In other words, the paper may understate the role of circumstances by using a thin opportunity measure, which mechanically compresses CV^circ toward CV. Additionally, the paper treats the stochastic error term $\varepsilon(z)$ as a preference/taste component, but Roemer and Trannoy (2016) note that the error term's classification as "effort" or "circumstance" is itself contentious.

# Relation to my jobs_and_wellbeing framework

This paper is arguably the closest existing work to a $W(z, R, A; y)$ framework. The indirect utility $V = u(f(\cdot), h_F, h_M) + \log Q_F(h_F) + \log Q_M(h_M) + \eta$ maps directly onto $W(z, R, A; y)$: the realized bundle $z = (C, h_F, h_M)$ is determined by the job choice; preferences $R$ are captured by $u(\cdot)$ and the random component $\eta$; the feasible job set $A$ is captured by $Q_F$ and $Q_M$; and the pay schedule $y$ is captured by the budget constraint function $f(\cdot)$ that incorporates the tax-benefit system. The paper's CV^circ is precisely $W(z, \bar{R}, A; y)$ --- well-being at reference preferences but actual opportunity sets and actual pay schedule. The difference CV - CV^circ isolates the welfare contribution of preference heterogeneity, which in this framework corresponds to the welfare sensitivity to $R$. The paper does not explore $W(z, R, \bar{A}; y)$ (reference opportunities), though the appendix mentions CV^pref as a related alternative.

The paper is closest to **responsibility for preferences** and **reference opportunity sets** (in the sense that it uses reference preferences $\bar{R}$ while keeping actual $A$). It is also directly related to the **compensation for opportunities** principle, since CV^circ measures what compensation each household deserves when preference differences are neutralized.

# Relation to Bargain et al. (2013)

This paper explicitly builds on Bargain et al. (2013). Bargain et al. (2013) is cited as a key reference for the use of discrete choice labor supply models in welfare analysis with heterogeneous preferences, but Bargain et al. use the conventional van Soest (1995) model that does not incorporate job opportunities. Jacquet, Jia, and Thoresen extend this by arguing that the Dagsvik job choice model is better suited for the preference/circumstance distinction because it explicitly models latent jobs and thus captures opportunity heterogeneity as a separate dimension from preference heterogeneity. This is a direct advancement: where Bargain et al. measure welfare with heterogeneous preferences but a universal (implicit) choice set, this paper measures welfare while explicitly separating the preference and opportunity components.

# Relation to opportunities vs preferences

This paper is centrally about the opportunities-versus-preferences distinction. The entire contribution is to operationalize this distinction within a structural labor supply model and measure its empirical importance for welfare assessment. The finding is that, in Norway, the distinction matters primarily at the very top of the income distribution. The paper shows that the job choice model's additive decomposition ($u$ for preferences, $\log Q$ for opportunities) provides a natural and empirically tractable way to separate the two sources of heterogeneity. This makes the paper a key methodological reference for any work that needs to distinguish opportunity-driven from preference-driven welfare differences.

# Useful quotations / formulas

**Indirect utility decomposition (Eq. 4.3):**
$$V(h_F, h_M, I) = u(f(h_F w_F, h_M w_M, I), h_F, h_M) + \log(Q_F(h_F)) + \log(Q_M(h_M)) + \eta_{h_F, h_M}$$

"the job choice model holds features that mirror the distinction between preferences and circumstances of the fairness literature" (p. 10)

**CV definition (Eq. 4.12):**
$$\max_{h_F, h_M} (u_i(f_0(\cdot)) + \log Q_{iF} + \log Q_{iM} + \eta_i) = \max_{h_F, h_M} (u_i(f_1(\cdot) + CV_i) + \log Q_{iF} + \log Q_{iM} + \eta_i)$$

**CV^circ definition (Eq. 4.13):**
$$\max_{h_F, h_M} (\bar{u}(f_0(\cdot)) + \log Q_{iF} + \log Q_{iM} + \bar{\eta}) = \max_{h_F, h_M} (\bar{u}(f_1(\cdot) + CV_i^{circ}) + \log Q_{iF} + \log Q_{iM} + \bar{\eta})$$

**CE definition (Eq. 3.3):**
$$CE_i = \bar{u}_i = \max_h \{\bar{u}(c, h; \bar{\gamma}) \mid c \leq w_i h - T_i\}$$

**Opportunity measure (Eq. 4.5):**
$$\log \theta_F = \gamma_{F1} + \gamma_{F2} S$$

"responsibility matters whenever the two metrics display different values" (p. 1, abstract)

"for the vast majority of Norwegian households, the reform resulted in significant welfare gains, regardless of whether preferences have been neutralized or not" (p. 19--20)

# Suggested tags

structural labor supply, job choice model, Dagsvik, compensating variation, fairness, responsibility, circumstances, preferences, CV^circ, conditional equality, reference preferences, discrete choice, latent jobs, RURO, tax reform, microsimulation, Norway, welfare measurement, opportunity heterogeneity, preference heterogeneity, decomposition

# My quick takeaway

This is the most directly relevant paper to a $W(z, R, A; y)$ framework that I have encountered. It operationalizes the separation between preferences and opportunities within the Dagsvik job choice model and measures the empirical importance of the distinction for welfare assessment. The finding that responsibility matters mostly at the top is striking but may be specific to the Norwegian context and the parsimonious opportunity specification. The methodology --- constructing CV^circ by imposing reference preferences while keeping actual opportunity sets --- is a clean and replicable strategy that any JMP in this area should engage with. The paper also provides a useful bridge between the structural labor supply literature and the normative fairness literature (Fleurbaey, Roemer, Maniquet). A natural extension would be to enrich the opportunity measure and apply the method cross-country.
