---
title: "Structural Labor Supply Models and Wage Exogeneity"
authors: [Max Löffler, Andreas Peichl, Sebastian Siegloch]
year: 2014
outlet: "SOEPpapers on Multidisciplinary Panel Data Research, No. 675 (DIW Berlin)"
country_or_context: "Germany (main), USA (robustness)"
population: "Single men, single women, couples (five demographic subgroups)"
data_period: "2007 (SOEP wave 2008; CPS 2007 for US robustness)"
shelf: "labour supply elasticities / sensitivity analysis / wage endogeneity / discrete choice"
tags: [labour-supply, elasticities, discrete-choice, wage-exogeneity, wage-endogeneity, sensitivity-analysis, meta-analysis, structural-model, functional-form, translog, Box-Cox, quadratic, wage-imputation, prediction-error, mixed-logit, Germany, USA, SOEP, optimal-taxation]
priority: "medium-high"
read_status: "extracted"
---

# Full citation

Löffler, M., Peichl, A., & Siegloch, S. (2014). Structural Labor Supply Models and Wage Exogeneity. *SOEPpapers on Multidisciplinary Panel Data Research*, No. 675, DIW Berlin.

# One-sentence contribution

Estimates 3,456 structural discrete-choice labour supply models (all plausible combinations of modelling assumptions) on the same German data, demonstrating that elasticities are robust to functional form, preference heterogeneity, and hours restrictions, but are extremely sensitive to the treatment of wages -- in particular, the standard assumption that wages are exogenous to preferences biases elasticities downward by more than half (0.25 vs. 0.6 when correlation is allowed).

# Why this paper matters

The paper provides the first systematic, controlled sensitivity analysis of structural discrete-choice labour supply models. By estimating thousands of model variants on the same data, it isolates which modelling choices matter and which do not. The key finding -- that wage treatment dominates all other specification choices -- has profound implications for the reliability of labour supply elasticities used in optimal tax analysis. Diamond and Saez (2011) use an elasticity of 0.25 (standard model) to derive an optimal top rate of 72.7%; the paper's preferred estimate of 0.6 reduces this to 52.6%, close to observed rates.

# Core research question

Which modelling assumptions in structural discrete-choice labour supply models affect estimated elasticities, and how does the standard assumption of wage exogeneity (independence between preferences and wages) bias the results?

# Economic setting and context

Germany, 2007 tax-benefit system. The analysis covers five demographic subgroups: single men (779), single women (1,065), couples with flexible male only (688), couples with flexible female only (1,042), and couples with both partners flexible (3,099). The German tax system features joint taxation for couples (income splitting), a complex benefit system, and social insurance contributions -- all captured by the IZA¥MOD microsimulation model. US robustness check uses CPS 2007 with NBER TAXSIM.

# Model / theoretical framework

**Standard discrete-choice model:** Individual $n$ maximises utility over $j \in J_n$ alternatives:
$$\max_j U(C_{nj}, L_j, \epsilon_{nj}) = \max_{j \in J_n} U(f\{w_{nj}h_j | x_{nj}, I_n\}, T - h_j, \epsilon_{nj})$$

**Systematic utility:**
$$U(C_{nj}, L_j | x_{nj}, \beta_n, \gamma_n) = \varphi(C_{nj}, L_j | x_{nj}, \beta_n, \gamma_n) + \epsilon_{nj}$$

With i.i.d. extreme value $\epsilon_{nj}$, the choice probability is:
$$P(U_{ni} > U_{nj}, \forall j \neq i | x_n, \beta_n, \gamma_n) = \frac{\exp(\varphi\{C_{ni}, L_i | x_{ni}, \beta_n, \gamma_n\}) \cdot g(i | x_{ni}, \gamma_n)}{\sum_{s \in J_n} \exp(\varphi\{C_{ns}, L_s | x_{ns}, \beta_n, \gamma_n\}) \cdot g(s | x_{ns}, \gamma_n)}$$

where $g(j)$ captures availability of hours alternatives (fixed costs, hours restrictions).

**Standard exogeneity assumption:**
$$\text{Corr}(\beta_n, w_{nj} | x_{nj}) = 0 \qquad \text{Corr}(\gamma_n, w_{nj} | x_{nj}) = 0$$

**Flexible model (Section 5):** Relaxes exogeneity by estimating preferences and log-wage equation jointly:
$$\ln(SL) = \sum_{n \in E} \ln\left(\frac{1}{R} \sum_r \frac{\exp(v_{ni}\{\cdot | \hat{w}_{ni}^{(r)}, \beta_n^{(r)}\}) \cdot g(i | \gamma_n^{(r)})}{\sum_j \exp(v_{nj}\{\cdot | \hat{w}_{nj}^{(r)}, \beta_n^{(r)}\}) \cdot g(j | \gamma_n^{(r)})}\right) + \ldots$$

Allows: (1) hours-dependent wages (part-time penalty), (2) correlation between consumption preferences and wages ($\rho_{C,\ln W}$), (3) correlation between leisure preferences and wages ($\rho_{L,\ln W}$). Estimated via full information maximum likelihood with Halton draws.

# Key objects

- **3,456 model specifications:** All combinations of: 3 utility functions (translog, quadratic, Box-Cox) × 2 welfare stigma options × 3 hours restrictions × 3 Halton draw counts × 5 observed heterogeneity options × 5 unobserved heterogeneity options × 2 wage imputation samples × 3 prediction error treatments.
- **16,730 converged estimation results** (across 5 demographic groups).
- **Meta-regression (Table 4):** Regresses standardised AIC and elasticities on modelling assumption dummies.
- **$\rho_{C,\ln W}$:** Correlation between consumption preferences and log wages. Estimated at $-0.717^{***}$ (Model 5): higher wages correlate with lower preference for consumption.
- **$\rho_{L,\ln W}$:** Correlation between leisure preferences and log wages. Estimated at $0.511^{***}$ (Model 5): higher wages correlate with higher preference for leisure.

# Data

**German SOEP** (Socio-Economic Panel), wave 2008, incomes from 2007. ~24,000 individuals in ~11,000 households. After exclusions (self-employed, civil servants, military, <17 or >65, multi-adult households with >2 adults), five subsamples totalling ~6,673 households.

**US CPS** (March Current Population Survey, 2007) via IPUMS-CPS, with NBER TAXSIM for tax calculations. Used for robustness check only.

**Tax-benefit microsimulation:** IZA¥MOD v3.0.0, approximated by second-degree polynomial in gross earnings and household characteristics ($R^2 > 0.99$ for most subgroups).

**Choice set:** 7 hours alternatives per individual (0, 10, 20, 30, 40, 50, 60 hours/week). Couples: $7^2 = 49$ alternatives.

# Identification logic

Standard discrete-choice identification: variation in $h_j$, $w_{nj}$, $I_n$, $x_{nj}$ and the nonlinearity of $f(\cdot)$ identify preference parameters $\beta_n$ and opportunity parameters $\gamma_n$.

For the flexible model (Section 5): identification of correlation between preferences and wages uses the observed wage equation residual for employed workers (subset $E$) and the multivariate normal distribution of $(\beta_n, \gamma_n, \epsilon_{w,n})$. Correlation parameters $\rho_{C,\ln W}$ and $\rho_{L,\ln W}$ are identified from the systematic relationship between wage residuals and labour supply choices conditional on observables.

# Estimation / empirical strategy

**Part 1 (Sections 3--4): Controlled meta-analysis.**
- Estimate 3,456 model specifications on each of 5 demographic subgroups (17,280 planned; 16,730 converged)
- Standardise AIC and elasticities within each labour supply group
- Meta-regression (Table 4): regress standardised outcomes on assumption dummies
- Elasticities computed by simulating 10% own-wage increase and aggregating individual responses

**Part 2 (Section 5): Flexible joint estimation.**
- 5 nested models of increasing flexibility (Table 5):
  - Model (1): Standard two-step, wages exogenous
  - Model (2): Joint estimation of preferences and wages
  - Model (3): + hours-dependent wages (part-time/overtime dummies)
  - Model (4): + correlation $\rho_{C,\ln W}$
  - Model (5): + correlation $\rho_{L,\ln W}$
- Estimated on single females only (computational constraints)
- Up to 4,000 Halton draws; results stable from 50 draws

# Treatment of preferences

Preferences over consumption and leisure modelled through $\varphi(C, L)$ with three functional forms tested: translog, quadratic, Box-Cox. Observed heterogeneity: interaction of preference parameters with age, children, etc. Unobserved heterogeneity: random coefficients (multivariate normal on consumption and/or leisure preference parameters), optionally with correlation between consumption and leisure preferences.

Key finding: the choice of functional form (translog vs. quadratic vs. Box-Cox), observed heterogeneity, and unobserved heterogeneity have minimal impact on estimated elasticities (Table 4). This contrasts sharply with the wage treatment, which dominates.

# Treatment of opportunities / constraints

Opportunities modelled through $g(j | x_{nj}, \gamma_n)$: fixed costs of working, part-time restrictions (hours < 20 less available), welfare stigma. These are the standard ad hoc approaches in the van Soest (1995) tradition. The paper notes that the RURO framework (Aaberge et al. 1995) provides a more structural interpretation of these constraints but does not implement it.

Fixed costs and part-time restrictions significantly improve fit and increase extensive-margin elasticities (Table 4). This is consistent with the RURO interpretation: jobs with very few hours are harder to find, so extensive-margin responses concentrate at part-time/full-time.

# Welfare / normative object

No direct welfare analysis. The paper discusses implications for optimal taxation: the Diamond-Saez (2011) optimal top rate formula $\tau = \frac{1}{1 + a \cdot e}$ yields 72.7% with $e = 0.25$ (restrictive model) but 52.6% with $e = 0.6$ (flexible model). The finding that wage exogeneity biases elasticities downward suggests that optimal tax rates derived from standard models may be too high.

# Main findings

**Part 1: Sensitivity to modelling assumptions (Table 4):**

1. **Functional form:** Quadratic slightly worse fit than translog; Box-Cox insignificant. Neither significantly affects elasticities.

2. **Welfare stigma:** Improves fit significantly but no effect on elasticities.

3. **Hours restrictions / fixed costs:** Significantly improve fit. Fixed costs increase extensive-margin elasticities ($+0.238^{***}$) and total elasticities ($+0.238^{***}$). Part-time restrictions similar effect.

4. **Observed heterogeneity:** Improves fit for single males; small effects on elasticities for some groups.

5. **Unobserved heterogeneity:** Minimal effect on both fit and elasticities. Random coefficients add computational cost but little value.

6. **Wage imputation -- CRITICAL finding:**
   - Using predicted wages for full sample (vs. non-workers only), without correcting prediction error: **more than doubles estimated elasticities** (extensive $+2.121^{***}$ to $+2.240^{***}$ across groups)
   - Full sample with prediction error integrated out: also significantly inflates elasticities ($+1.385^{***}$ to $+1.406^{***}$)
   - Adding a single random draw partly offsets the full-sample effect

**Part 2: Joint estimation results (Table 5, single females):**

7. **Hours-dependent wages (Model 3):** Part-time work pays ~7% less than full-time (significant at 5%). Overtime pay slightly lower (insignificant). Confirms inverted U-shaped wage-hours profile.

8. **Wage-preference correlation (Models 4--5):**
   - $\rho_{C,\ln W} = -0.717^{***}$: higher wages strongly negatively correlated with consumption preferences
   - $\rho_{L,\ln W} = +0.511^{***}$: higher wages positively correlated with leisure preferences
   - Interpretation: unobserved ability raises wages but also raises preference for leisure (backward-bending supply)

9. **Elasticity effect:** Total elasticity increases from 0.20 (Model 1) to 0.63 (Model 5). More than doubled. Extensive margin drives most of the increase (0.17 → 0.58).

10. **Model fit:** Models 3--5 outperform Models 1--2 on all criteria (AIC, BIC, pseudo-$R^2$, log-likelihood).

# Main limitations

- Working paper (not peer-reviewed journal version); results should be treated as preliminary
- Flexible model (Section 5) estimated only for single females -- computational constraints prevent extension to couples
- The identification of $\rho_{C,\ln W}$ and $\rho_{L,\ln W}$ relies on functional form (multivariate normality); the correlations are not nonparametrically identified
- Meta-regression standard errors are not bootstrapped (likely understated)
- Does not address the RURO distinction between preferences and opportunities: the "wage-preference correlation" could partly reflect opportunity heterogeneity (e.g., high-ability workers facing different job sets)
- Static model; no lifecycle or dynamic considerations
- Tax system approximated by polynomial (though $R^2 > 0.99$)

# Relevance for my JMP

## possible use for framing
The paper demonstrates that the treatment of wages is the most consequential modelling choice in structural labour supply -- more important than functional form, heterogeneity, or hours restrictions. This motivates the RURO framework's explicit modelling of the wage offer distribution $g_1(w)$ as part of the opportunity density, rather than treating wages as exogenous individual characteristics.

## possible use for model design
The finding that $\rho_{C,\ln W} < 0$ and $\rho_{L,\ln W} > 0$ suggests that unobserved ability affects both wages and preferences. In the RURO framework, this correlation is partly captured by the opportunity density (higher-ability workers face more/better job offers) rather than by preference-wage correlation. The $W(z, R, A; y)$ framework can separate these channels: ability affects $A$ (more opportunities) and potentially $R$ (different preferences), and the welfare implications differ.

## possible use for identification
The paper's finding that wage prediction errors matter enormously for elasticities is relevant for RURO estimation, where the wage offer distribution $g_1(w)$ is estimated as part of the structural model. The RURO approach of estimating wages simultaneously within the structural model (as in Aaberge et al. 1995) may avoid the bias documented here, providing a structural rationale for joint estimation.

## possible use for comparative benchmarks
The paper's range of elasticities (0.2 to 0.6 for single women, depending on specification) provides a benchmark for evaluating RURO-based estimates. If RURO estimates fall in the upper range (because they account for opportunity heterogeneity), this is consistent with the paper's finding that more flexible models produce higher elasticities.

# Research questions this paper inspires

1. Does the RURO framework's simultaneous estimation of wages and preferences automatically resolve the wage exogeneity problem documented here? In the RURO model, wages are drawn from the opportunity distribution and are therefore structurally linked to preferences through the choice mechanism. Is this sufficient to account for the correlation?

2. How much of the estimated $\rho_{C,\ln W}$ and $\rho_{L,\ln W}$ reflects genuine preference-wage correlation vs. opportunity heterogeneity? In a RURO model, workers with different abilities face different opportunity sets ($A$), which could produce apparent preference-wage correlation even if preferences ($R$) are independent of ability.

3. The paper finds that elasticities double from 0.25 to 0.6 when allowing for correlation. Is this increase consistent with macroeconomic elasticities (Chetty et al. 2011)? If so, the micro-macro gap may be partly due to model specification errors in standard micro studies, not just frictions.

4. The paper tests functional form (translog vs. Box-Cox vs. quadratic) but not the RURO-justified Box-Cox from Dagsvik and Strøm (2006). Does the psychophysics-justified Box-Cox with opportunity density produce different results than the ad hoc Box-Cox tested here?

# Challenge to this paper

The paper's main finding -- that wage-preference correlation doubles elasticities -- is important but potentially confounds two distinct mechanisms. First, there may be genuine feedback between ability, wages, and preferences (as the paper models). Second, the apparent correlation may reflect misspecification of the opportunity structure: if high-wage workers face different job sets (more full-time options, fewer part-time), this creates a spurious correlation between wages and labour supply choices that is not about preferences but about opportunities. The RURO framework distinguishes these channels: the opportunity density $g(h,w)$ captures the hours-wage profile of available jobs, while preferences $v(C,h)$ capture pure tastes. By not separating these, the paper cannot determine whether the "preference-wage correlation" reflects genuine preference heterogeneity or opportunity heterogeneity -- a distinction that matters critically for welfare analysis.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The paper documents that the standard exogeneity assumption in discrete-choice models biases elasticities downward. This directly affects welfare calculations: if elasticities are understated, the welfare cost of taxation is understated and optimal tax rates are overstated.

[Reasonable inference for my project] The $W(z, R, A; y)$ framework separates preferences ($R$) from opportunities ($A$). The "wage-preference correlation" documented here may partly reflect $A$-heterogeneity (workers with different abilities face different opportunity sets) rather than pure $R$-wage correlation. If so, the RURO model's explicit opportunity density may resolve part of the exogeneity problem structurally, without needing the flexible correlation approach proposed here.

[Unclear from paper] Whether the elasticity increase from allowing correlation (0.25 → 0.6) would persist in a RURO model that separately estimates opportunity densities. If the opportunity density captures the hours-wage profile, the "residual" preference-wage correlation may be smaller, and the elasticity increase less dramatic.

The paper is closest to: **methodological sensitivity analysis of structural labour supply models** and **motivation for joint estimation of wages and preferences (as in RURO)**.

# Relation to Bargain et al. (2013)

Bargain et al. (2013) use a standard two-step estimation procedure with wages treated as exogenous. This paper shows that this procedure may bias preference estimates and produce elasticities that are too low. Since Bargain et al.'s welfare metrics depend on estimated preferences, the welfare rankings could be sensitive to the wage treatment. The paper does not compute welfare metrics, but the implication is clear: welfare calculations based on biased preferences may misrank individuals or policy reforms.

# Relation to opportunities vs preferences

The paper's key finding -- significant correlation between wages and both consumption and leisure preferences -- has a natural interpretation in the opportunities vs. preferences framework. What the paper calls "preference-wage correlation" could partly reflect opportunity heterogeneity: workers with higher unobserved ability face both higher wages and different job opportunity sets (e.g., more full-time positions available to skilled workers). The standard model attributes all this variation to preferences because it has no opportunity channel. The RURO framework, by explicitly modelling opportunity densities, can absorb part of this correlation structurally. This suggests that the "true" preference-wage correlation may be smaller than $\rho_{C,\ln W} = -0.717$ once opportunities are properly accounted for.

# Useful quotations / formulas

**On the key finding (p. 2--3):**
"In our preferred model, estimated labor supply elasticities are more than twice as high compared to conventional models assuming zero correlation between work preferences and wages (0.6 instead of 0.25)."

**On wage treatment being key (p. 19):**
"Most previous robustness checks have thus concentrated on issues of secondary order. Instead, more attention should be paid to the wage imputation and the handling of wage prediction errors."

**On optimal tax implications (p. 25):**
"Diamond and Saez (2011) use an elasticity of 0.25 [...] This leads to an optimal top marginal tax rate of $\tau = \frac{1}{1+1.5 \times 0.25} = 72.7\%$. However, an elasticity of 0.6, as found in our most flexible model, reduces the optimal tax rate to 52.6%, bringing it closer to actually observed values."

**On the mechanism (p. 20):**
"the less productive worker has now a higher preference for consumption, whereas preferences of the more productive worker stay constant. As the less productive worker now values consumption and income more, it follows that his labor supply elasticity increases."

**Exogeneity assumption (eq. 5):**
$$\text{Corr}(\beta_n, w_{nj} | x_{nj}) = 0 \qquad \text{Corr}(\gamma_n, w_{nj} | x_{nj}) = 0$$

**Estimated correlations (Table 5, Model 5):**
$$\rho_{C,\ln W} = -0.717^{***} \qquad \rho_{L,\ln W} = +0.511^{***}$$

# Suggested tags

labour-supply, elasticities, discrete-choice, wage-exogeneity, wage-endogeneity, sensitivity-analysis, controlled-meta-analysis, functional-form, translog, Box-Cox, quadratic, wage-imputation, prediction-error, mixed-logit, random-coefficients, fixed-costs, hours-restrictions, optimal-taxation, Diamond-Saez, Germany, SOEP, USA, CPS, joint-estimation, preference-wage-correlation

# My quick takeaway

This paper is the definitive sensitivity analysis for structural discrete-choice labour supply models. The punchline is simple: functional form, heterogeneity specification, and hours restrictions don't matter much for elasticities; the treatment of wages matters enormously. The standard assumption that wages are exogenous to preferences biases elasticities downward by a factor of 2--3 (0.25 → 0.6 for single women). For my JMP, the key insight is that the RURO framework's simultaneous estimation of wage offers and preferences may structurally address part of this problem: by modelling the wage offer distribution as part of the opportunity density, the RURO approach avoids treating wages as exogenous individual characteristics. The "preference-wage correlation" documented here ($\rho_{C,\ln W} = -0.72$, $\rho_{L,\ln W} = +0.51$) may partly reflect opportunity heterogeneity rather than genuine preference-wage dependence -- a distinction that matters for welfare analysis because $A$-driven correlation affects the feasible set, not well-being conditional on the feasible set.
