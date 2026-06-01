---
title: "Empirical welfare analysis: when preferences matter"
authors: [Jean-Francois Carpantier, Cristina Sapata]
year: 2016
outlet: "Social Choice and Welfare, 46(3), 521--542"
country_or_context: "United States"
population: "Single adults (no children, unmarried/divorced/widowed/separated)"
data_period: "2004 (Cross-National Equivalent File, CNEF -- PSID component)"
shelf: "welfare measurement / equivalent income / conditional equality / egalitarian equivalence / individual preferences / discrete choice"
tags: [conditional-equality, egalitarian-equivalence, equivalent-income, individual-preferences, group-preferences, heterogeneity, Box-Cox-utility, conditional-logit, discrete-choice, labour-supply, welfare-criteria, Fleurbaey, worst-off, reference-preferences, reference-circumstances, CNEF, PSID]
priority: "high"
read_status: "extracted"
---

# Full citation

Carpantier, J.-F., & Sapata, C. (2016). Empirical welfare analysis: when preferences matter. *Social Choice and Welfare*, 46(3), 521--542.

# One-sentence contribution

Implements Fleurbaey's (2008) conditional equality and egalitarian equivalence welfare criteria using individual-level (not just group-level) preference information recovered from the discrepancy between predicted and revealed labour supply choices, showing that 18% of worst-off individuals are reclassified when individual preferences replace group-level predictions.

# Why this paper matters

This is one of the few papers that empirically implements both conditional equality (CE) and egalitarian equivalence (EE) welfare criteria from Fleurbaey (2008), and the first to introduce individual-level preference recovery into this framework. The finding that individual preferences substantially change the identity of the worst-off is directly relevant for any welfare analysis using equivalent incomes: it shows that group-level preference estimation (standard in structural labour supply models) may misidentify who should be the target of social policy. The paper also provides a systematic comparison of how different reference parameters (reference wages for EE, reference preferences for CE) affect welfare rankings.

# Core research question

How sensitive are the conditional equality and egalitarian equivalence welfare criteria to the use of individual-level versus group-level preferences, and how do different reference parameter choices affect the identification of the worst-off?

# Economic setting and context

Post-tax-and-transfer welfare analysis in the United States. The paper uses 2004 CNEF data (PSID component) on 914 single adults without children, aged 25--55. The institutional context is the US tax-benefit system, with budget constraints computed using a piecewise-linear tax schedule and transfer rules. The paper does not evaluate a specific reform but rather compares welfare rankings under different criteria and preference specifications.

# Model / theoretical framework

**Utility specification (Box-Cox):**
$$u(c, l; z) = \beta_c \frac{c^{\alpha_c} - 1}{\alpha_c} + \beta_l(z) \frac{(1-l)^{\alpha_l} - 1}{\alpha_l}$$
where $c$ = consumption, $l$ = labour supply (fraction of time), $z$ = socio-demographic characteristics, and $\beta_l(z) = \exp(\delta_0 + \delta_1 \cdot \text{age} + \delta_2 \cdot \text{age}^2 + \delta_3 \cdot \text{female})$.

**Discrete choice:** 8 alternatives: $h \in \{0, 10, 20, 30, 35, 40, 50, 60\}$ hours/week. Conditional logit (McFadden 1974) with additive iid extreme-value errors: $U_{ij} = u(c_{ij}, l_j; z_i) + \varepsilon_{ij}$.

**Two welfare criteria from Fleurbaey (2008):**

1. **Egalitarian Equivalence (EE):** Fix a reference circumstance $\tilde{y}$ (a wage rate). Find the budget set $B_{\tilde{y}}$ at the reference wage such that the individual is indifferent between $B_{\tilde{y}}$ and their actual situation. Welfare = equivalent income = the non-labour income shift needed to reach actual utility on $B_{\tilde{y}}$. Three variants:
   - **EE0 (zero-wage):** Reference wage = 0. Equivalent income = consumption at $h=0$ yielding current utility.
   - **EEm (min-wage):** Reference wage = minimum wage.
   - **EEw (wage):** Reference non-labour income = 0 (individual keeps own wage).

2. **Conditional Equality (CE):** Fix reference preferences $\tilde{\beta}_l$. Compute the maximum well-being $\hat{v}_i$ the individual would achieve on their actual budget set if they had reference preferences. Three variants:
   - **CE10:** $\tilde{\beta}_l = 10$ (strong taste for work).
   - **CE20:** $\tilde{\beta}_l = 20$ (moderate).
   - **CE70:** $\tilde{\beta}_l = 70$ (strong taste for leisure).

**Individual preference recovery:**
For each individual $i$, the group-level model predicts an optimal choice $j^*_i = \arg\max_j u(c_{ij}, l_j; z_i)$. When the actual choice $k_i \neq j^*_i$ (57% of sample), the paper infers individual-specific preference information from the conditional expectation:
$$E[\varepsilon_{ij} - \varepsilon_{ik} \mid \varepsilon_{ij} - \varepsilon_{ik} > u_{ik} - u_{ij}]$$
This truncated mean of the error difference provides individual-level taste information that shifts the deterministic utility, effectively recovering individual preferences from the discrepancy between predicted and revealed choice.

# Key objects

- **Equivalent income (EE criteria):** The non-labour income on the reference budget set that yields the same utility as the actual situation. Higher equivalent income = better off.
- **Conditional well-being (CE criteria):** The maximum utility on the actual budget set computed with reference preferences. Higher $\hat{v}_i$ = better off from the perspective of reference preferences.
- **Discrepancy rate:** 57% of individuals choose differently from the group-model prediction -- the source of individual preference information.
- **Worst-off reclassification rate:** 18% of worst-off individuals (bottom decile) are reclassified when individual preferences replace group preferences under EE0.

# Data

2004 Cross-National Equivalent File (CNEF), PSID component. 914 single adults (no children, unmarried/divorced/widowed/separated), aged 25--55. Variables: weekly hours, hourly wages, non-labour income, age, gender, education. Budget constraints computed using the US tax-benefit system (piecewise-linear schedule).

# Identification logic

**Preference parameters:** Identified from conditional logit on discrete labour supply choices. Variation in budget constraints (different wages, non-labour incomes, tax schedule kinks) identifies the utility parameters $\alpha_c$, $\alpha_l$, $\delta_0$--$\delta_3$.

**Individual preferences:** Identified from the discrepancy between the group-model optimal choice and the individual's revealed choice. When $k_i \neq j^*_i$, the direction and magnitude of the discrepancy identify individual taste shifters relative to the group prediction. The identifying assumption is that the errors $\varepsilon_{ij}$ are iid Type I extreme value, so the conditional expectation of the error difference given revealed choice has a closed-form expression.

# Estimation / empirical strategy

1. **Step 1:** Estimate conditional logit on $N = 914 \times 8 = 7312$ person-alternative observations. Obtain group-level parameters $\hat{\alpha}_c, \hat{\alpha}_l, \hat{\delta}_0, \hat{\delta}_1, \hat{\delta}_2, \hat{\delta}_3$.

2. **Step 2:** For each individual, compute group-predicted optimal $j^*_i$. If actual choice $k_i \neq j^*_i$, compute the conditional expectation of the error difference using the Gumbel distribution properties.

3. **Step 3:** Compute welfare indices (EE0, EEm, EEw, CE10, CE20, CE70) under both group and individual preferences for all 914 individuals.

4. **Step 4:** Compare welfare rankings, worst-off identification, and socio-demographic profiles of the worst-off across criteria and preference specifications.

# Treatment of preferences

**Central focus of the paper.** Preferences are heterogeneous across observable groups (age, gender) through the taste shifter $\beta_l(z)$. The key innovation is recovering additional individual-level preference heterogeneity from the logit residuals. The paper demonstrates that group-level preferences (standard in the literature) are insufficient: 57% of individuals reveal choices inconsistent with group predictions, and incorporating this information changes 18% of worst-off identifications.

The paper treats preferences as given (no preference formation or adaptation). Preferences are respected in the welfare evaluation: both CE and EE criteria incorporate individual preferences, though they differ in how preferences enter the evaluation (CE holds preferences fixed at a reference; EE holds circumstances fixed at a reference).

# Treatment of opportunities / constraints

Budget constraints are computed from wages, non-labour income, and the tax-benefit system. The paper does not model involuntary unemployment, demand-side constraints, or job availability. All individuals are assumed to freely choose among the 8 hours alternatives at their observed (or imputed) wage. The budget set $B_i$ is individual-specific due to different wages and non-labour incomes, but there is no explicit opportunity set in the RURO sense.

The CE criterion evaluates welfare on the actual budget set (compensating for circumstance differences), while the EE criterion evaluates welfare on a reference budget set (compensating for preference differences). Neither criterion addresses the possibility that the choice set itself may be constrained by demand-side factors.

# Welfare / normative object

Two families of welfare criteria, each with three reference-parameter variants:
- **EE (egalitarian equivalence):** Equivalent income at reference wage. Social objective: maximin over equivalent incomes.
- **CE (conditional equality):** Well-being with reference preferences on actual budget. Social objective: maximin over conditional well-being.

The paper does not aggregate into a single social welfare number but focuses on identifying the worst-off (bottom decile) and comparing rankings across criteria.

# Main findings

1. **Preference parameters (Table 2):** $\hat{\alpha}_c = 0.478$, $\hat{\alpha}_l = -6.254$. Age has a positive linear and negative quadratic effect on leisure preference. Female dummy ($\hat{\delta}_3 = 0.893$) implies women have higher taste for leisure. All coefficients significant.

2. **Discrepancy rate:** 57% of individuals choose differently from group prediction. This is the source of individual preference information. The discrepancy is not noise: it contains systematic individual taste information recoverable from the truncated error distribution.

3. **Worst-off reclassification (Table 3, Figures 9--11):** Under EE0 (zero-wage), 18% of worst-off individuals are reclassified when individual preferences replace group preferences. Under EEm and EEw, reclassification rates are lower but non-trivial. The Venn diagrams show substantial but incomplete overlap between worst-off sets across criteria.

4. **Stability of socio-demographic profiles (Table 4):** Despite individual reclassification, the average socio-demographic profile of the worst-off (age, gender, education, hours, wage) is relatively stable across criteria and preference specifications. Policy targeting at the group level would be similar; individual-level targeting would differ.

5. **Consistency across criteria:** EEm and EEw produce nearly identical worst-off rankings (only 1 exception). CE10 is close to EEm/EEw. EE0 identifies a distinct set of worst-off individuals. CE70 (strong leisure preference) also identifies a different set.

6. **The zero-wage criterion is special:** EE0 reduces to comparing consumption at zero hours (non-labour income + transfers), ignoring labour supply capacity. This captures a "right to leisure" perspective but may undervalue individuals with high earning capacity who choose to work.

# Main limitations

- No demand-side constraints or involuntary unemployment: all individuals assumed to freely choose hours.
- Wage imputation not discussed; selection into employment may bias preference estimates.
- The individual preference recovery method relies on the iid extreme-value distributional assumption for the errors. If errors are correlated across alternatives (nested logit, mixed logit), the conditional expectation formula changes.
- Only singles without children: excludes the household dimension where preference heterogeneity and intra-household allocation are most complex.
- The 8 discrete hours alternatives are coarse; individuals may face different choice sets in reality.
- No policy reform evaluation: the paper is purely about measurement, not policy design.

# Relevance for my JMP

## possible use for individual vs group preferences in welfare measurement
The paper's finding that 18% of worst-off are reclassified with individual preferences is directly relevant. My RURO framework estimates preferences at the individual level (through the random utility component), but the welfare analysis may aggregate to group-level preference parameters. This paper warns that such aggregation can substantially change welfare conclusions, especially for identifying the worst-off under maximin/leximin criteria.

## possible use for comparing CE and EE criteria
The systematic comparison of three EE and three CE variants with different reference parameters provides a practical template for sensitivity analysis in my welfare evaluation. The finding that EEm ≈ EEw but EE0 differs highlights the importance of the reference wage choice -- in my framework, this corresponds to the reference wage $\tilde{w}$ in the equivalent income $m_i(\tilde{w}, z_i)$.

## possible use for the discrepancy-based individual preference recovery
The method of recovering individual preferences from the gap between group prediction and revealed choice could be adapted for the RURO setting. In my framework, the discrepancy between the group-predicted optimal job and the actual job chosen could reflect both individual preference heterogeneity AND demand-side constraints (limited job offers). Disentangling these two sources of discrepancy is a key challenge that the Carpantier-Sapata method does not address but my RURO model potentially can.

# Research questions this paper inspires

1. In the RURO framework, how much of the discrepancy between predicted and actual labour supply is due to individual preference heterogeneity versus demand-side constraints (limited job availability)? The Carpantier-Sapata method attributes all discrepancy to preferences; the RURO model offers a structural decomposition.

2. How sensitive is the RURO welfare analysis to using individual-level versus group-level preferences? If 18% reclassification occurs even in a simple model without demand-side constraints, the reclassification rate may be higher in a richer model.

3. Does the choice of reference wage $\tilde{w}$ in equivalent income matter more or less than the choice between individual and group preferences? The paper suggests that the reference parameter choice and the preference specification choice can both change worst-off identification by 10--20%.

# Challenge to this paper

The paper attributes all discrepancy between predicted and actual choices to individual preference heterogeneity (unobserved taste differences captured by the logit errors). But in reality, discrepancies may arise from demand-side constraints: individuals may not be able to freely choose their preferred hours. The RURO framework explicitly models this by introducing an opportunity density $g(h, w)$ that restricts the feasible set. Under RURO, an individual choosing $h = 20$ when the group model predicts $h = 40$ might not have a stronger taste for leisure -- they might simply lack access to full-time jobs. The Carpantier-Sapata method would incorrectly attribute this to preferences, biasing the welfare analysis. This is especially problematic for conditional equality, where the "reference preferences" are applied to the actual budget set: if the budget set does not reflect the true opportunity set, the conditional well-being measure is computed on the wrong domain.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The paper implements $W(z, R, A; y)$ with $z$ = observed (hours, consumption) bundle, $R$ = estimated (and individually recovered) preferences, $A$ = budget set computed from wages and tax-benefit system, $y$ = US tax-benefit schedule. Both EE and CE criteria are special cases of the general well-being function.

[Reasonable inference for my project] The EE criteria correspond to equivalent income $m_i(\tilde{w}, z_i)$ in my framework: fixing a reference wage $\tilde{w}$ and finding the income that yields the same utility on the reference budget. The reference wage choices (0, minimum, own) correspond to different anchoring points for interpersonal comparisons. My framework should be explicit about this choice and its implications.

[Unclear from paper] How the individual preference recovery would interact with the RURO opportunity density. In my framework, the "discrepancy" between predicted and actual choices reflects both preference heterogeneity and opportunity constraints. The Carpantier-Sapata method cannot be directly imported without controlling for the opportunity set.

# Relation to Bargain et al. (2013)

The paper shares the same theoretical foundation (Fleurbaey 2008) and similar empirical methods (discrete-choice labour supply with Box-Cox utility, equivalent income computation) as Bargain et al. (2013). The key difference: Carpantier & Sapata add individual preference recovery, which Bargain et al. do not. The finding that individual preferences change 18% of worst-off identifications suggests that Bargain et al.'s group-level analysis may miss important individual-level welfare variation. However, Bargain et al. use a richer model (couples, children, multiple countries) and focus on policy reform evaluation rather than methodological comparison.

# Relation to opportunities vs preferences

This paper is entirely about preferences -- it does not address opportunity constraints. The CE criterion compensates for circumstance (wage) differences while holding preferences fixed; the EE criterion compensates for preference differences while holding circumstances fixed. But "circumstances" here means only wages and non-labour income, not the broader opportunity set (job availability, hours constraints, hiring discrimination) that the RURO model captures. The paper's framework implicitly assumes that the opportunity set is fully described by the budget constraint at the observed wage, which is precisely the assumption that my JMP challenges.

# Useful quotations / formulas

**On the role of individual preferences (p. 522):**
"In this paper, we [...] go one step further than group-level analysis by using a methodology to capture, on top of group preferences, individual preference elements."

**On discrepancy-based identification (p. 530):**
"Each individual makes a choice that reflects his own preferences. When the observed choice differs from the modeled optimal one, this discrepancy can be used to recover information on individual preferences that is not captured by the group-level model."

**On the reclassification result (p. 537):**
"The zero-wage egalitarian equivalent criterion is the most sensitive to the use of individual preferences: 18% of the worst-off are reclassified."

**On consistency of EE criteria (p. 538):**
"The min-wage and wage egalitarian-equivalent criteria lead to the same identification of the worst-off, with only one exception out of 91 individuals."

**Box-Cox utility formula (p. 528):**
$$u(c, l; z) = \beta_c \frac{c^{\alpha_c} - 1}{\alpha_c} + \beta_l(z) \frac{(1-l)^{\alpha_l} - 1}{\alpha_l}$$
with $\beta_l(z) = \exp(\delta_0 + \delta_1 \text{age} + \delta_2 \text{age}^2 + \delta_3 \text{female})$.

# Suggested tags

conditional-equality, egalitarian-equivalence, equivalent-income, individual-preferences, group-preferences, heterogeneity, Box-Cox-utility, conditional-logit, discrete-choice, labour-supply, welfare-criteria, Fleurbaey, worst-off, reference-preferences, reference-circumstances, CNEF, PSID, Carpantier, Sapata

# My quick takeaway

A methodologically important paper showing that individual-level preference recovery (from logit residuals) changes the identity of 18% of worst-off individuals relative to group-level estimates. For my JMP, this raises a critical question: in the RURO framework, how much of the "discrepancy" between predicted and actual choices is preferences vs. opportunity constraints? The paper's method attributes everything to preferences, which is exactly the identification problem my model addresses. The systematic comparison of CE and EE criteria with different reference parameters also provides a useful template for sensitivity analysis in my welfare evaluation.
