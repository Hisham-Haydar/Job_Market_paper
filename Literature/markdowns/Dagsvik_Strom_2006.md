---
title: "Sectoral Labour Supply, Choice Restrictions and Functional Form"
authors: [John K. Dagsvik, Steinar Strøm]
year: 2006
outlet: "Journal of Applied Econometrics, 21(6), 803--826"
country_or_context: "Norway"
population: "Married women (with husband's labour supply taken as given)"
data_period: "1994"
shelf: "RURO model / sectoral labour supply / functional form justification / opportunity density"
tags: [RURO, labour-supply, discrete-choice, Poisson-process, opportunity-density, sectoral-choice, public-sector, private-sector, functional-form, psychophysics, Box-Cox, IIA, married-women, Norway, elasticities, identification]
priority: "high"
read_status: "extracted"
---

# Full citation

Dagsvik, J. K., & Strøm, S. (2006). Sectoral Labour Supply, Choice Restrictions and Functional Form. *Journal of Applied Econometrics*, 21(6), 803--826.

# One-sentence contribution

Develops the theoretical foundations of the RURO (Random Utility, Random Opportunity) labour supply model -- including the Poisson process representation of latent job opportunities, the IIA-based derivation of the $\varepsilon^{-2}$ intensity measure, a psychophysics-based justification for the Box-Cox functional form of systematic utility, and a sectoral extension -- and applies the framework to Norwegian married women's choice between public sector, private sector, and non-participation.

# Why this paper matters

This is the key methodological paper for the RURO framework as applied to labour supply. While Dagsvik (1994) provided the general theoretical framework, this paper translates it into a practical labour supply model with: (1) explicit theoretical justification for the multiplicatively separable utility $U = v(C,h) \cdot \varepsilon(z)$, (2) psychophysical invariance arguments that pin down the Box-Cox functional form for $v(C,h)$, (3) extension to multiple sectors with sector-specific opportunity densities, and (4) empirical demonstration that the opportunity density (not just preferences) explains the observed clustering of hours at part-time and full-time levels. The paper shows that ignoring the opportunity structure biases preference parameter estimates and misattributes institutional constraints to taste heterogeneity.

# Core research question

How can labour supply be modelled when workers choose from latent, individual-specific sets of job opportunities characterised by hours, wages, and non-pecuniary attributes -- and what functional form restrictions on preferences and opportunity densities are justified by theoretical principles?

# Economic setting and context

Norway, 1994. Married women choose between not working, working in the public sector, and working in the private sector. The public sector is more unionised, has more regulated hours, higher job security, and more education-intensive jobs (health, education). The private sector is more heterogeneous and less unionised. The Norwegian tax system creates non-convex budget sets. 92% of married women participate in the labour market, with roughly equal splits between public (49.2%) and private (42.8%) sector employment.

# Model / theoretical framework

**Assumption 1 (multiplicative separability):**
$$U(C, h, z) = v(C, h) \cdot \varepsilon(z)$$
where $v(\cdot)$ is deterministic and $\varepsilon(z)$ is a random taste-shifter for job-type $z$.

**Budget constraint:** $C = f(hw, I)$ where $f(\cdot)$ transforms gross income into after-tax household income, $I$ is non-labour income (including husband's income). Shorthand: $\psi(h, w; I) \equiv v(f(hw, I), h)$.

**Assumption 2 (Poisson process for opportunities):**
The triples $\{(H(z), W(z), \varepsilon(z))\}$ in the opportunity set $\wp$ are realisations from a non-homogeneous Poisson process on $[0, \bar{h}] \times [0, \infty) \times (0, \infty)$. Taste-shifters $\{\varepsilon(z)\}$ are distributed independently of $\{(H(z), W(z))\}$. Different agents face independent realisations.

**Assumption 3 (intensity measure):**
$$d\lambda(h, w, \varepsilon) = \begin{cases} \theta_1 \, g(h, w) \, \varepsilon^{-2} \, dh \, dw \, d\varepsilon & \text{when } h > 0, w > 0, \varepsilon > 0 \\ (1 - \theta_1) \, \varepsilon^{-2} \, d\varepsilon & \text{when } h = w = 0, \varepsilon > 0 \end{cases}$$
where $g(h,w)$ is the opportunity density and $\theta_1 \in (0,1)$ is the fraction of feasible opportunities that are market opportunities.

The $\varepsilon^{-2}$ structure follows from the IIA assumption (Dagsvik 1994). The parameter $\theta = \theta_1 / (1 - \theta_1)$ is the ratio of mean feasible market to non-market opportunities.

**Theorem 1 (choice probabilities):**
$$\varphi(h, w; I) = \frac{\psi(h, w; I) \, g(h, w) \, \theta}{\psi(0, 0; I) + \theta \iint_D \psi(x, y; I) \, g(x, y) \, dx \, dy}$$
for $h > 0, w > 0$, and
$$\varphi(0, 0; I) = \frac{\psi(0, 0; I)}{\psi(0, 0; I) + \theta \iint_D \psi(x, y; I) \, g(x, y) \, dx \, dy}$$

**Sectoral extension (Section 2.4):** With $m$ sectors, utility becomes $U(C, h, j, z) = v(C, h) \, \mu_j \, \varepsilon_j(z)$ where $\mu_j > 0$ captures average preference for sector $j$. Sector-specific opportunity densities $g_j(h, w)$ and intensities $\theta_{1j}$ yield:
$$\varphi_j(h, w; I) = \frac{\psi(h, w; I) \, \mu_j \theta_j \, g_j(h, w)}{\psi(0, 0; I) + \sum_{k=1}^m \mu_k \theta_k \iint_D \psi(x, y; I) \, g_k(x, y) \, dx \, dy}$$

**Functional form justification (Section 2.3):**

**Assumption 4 (consumption invariance):** If the fraction preferring $(C_1, L_1)$ over $(C_2, L_2)$ is $\leq$ the fraction preferring $(C_1^*, L_1)$ over $(C_2^*, L_2)$, then the same holds when consumption levels are rescaled by any $r > 0$.

**Assumption 5 (leisure invariance):** Analogous for rescaling leisure levels.

**Theorem 2:** Under Assumptions 4 and 5:
$$\log v(C, h) = \beta_1 \frac{C^{\alpha_1} - 1}{\alpha_1} + \beta_2 \frac{L^{\alpha_2} - 1}{\alpha_2} + \beta_3 \frac{(C^{\alpha_1} - 1)(L^{\alpha_2} - 1)}{\alpha_1 \alpha_2}$$
where $\alpha_j < 1$, $\beta_j > 0$, $C$ is consumption minus subsistence, $L$ is leisure minus subsistence. This is the Box-Cox form. Special cases: $\alpha_1 = \alpha_2 = \beta_3 = 0$ gives Stone-Geary $\log v = \beta_1 \log C + \beta_2 \log L$.

# Key objects

- **$g(h, w)$ / $g_j(h, w)$:** Opportunity density -- the average fraction of feasible jobs with hours $\in (h, h+dh)$ and wage $\in (w, w+dw)$. Sector-specific in the extended model.
- **$\theta_1$ / $\theta_{1j}$:** Fraction of feasible opportunities that are market (sector $j$) opportunities.
- **$\theta = \theta_1/(1-\theta_1)$:** Ratio of market to non-market opportunities.
- **$b_j = \mu_j \theta_j$:** Composite parameter combining sector preference and opportunity intensity. $\log b_j = f_{j1} + f_{j2} S$ (education-dependent).
- **$\psi(h, w; I)$:** Systematic utility evaluated at hours $h$, wage $w$, non-labour income $I$.
- **$v_2(h) \cdot g_2(h)$:** The product of the hours component of systematic utility and the hours offer density -- only this product is nonparametrically identified (eq. 2.11).
- **$g_{j2}(h)$:** Hours offer density for sector $j$ -- piecewise uniform with peaks at full-time (1950 annual hours) and part-time (1040 annual hours).

# Data

"Survey of Income and Wealth, 1994" merged with "Level of Living Conditions, 1995" (Statistics Norway). Sample: 824 married women aged 25--64 (with husbands). None self-employed, none on disability. Wage rates: annual wage income / hours worked (excluding rates above NOK 350 or below NOK 40). Wage equation estimated on larger sample including single women (691 public, 580 private). Tax system fully modelled. 7 hours intervals per sector (medians: 420 to 2808 annual hours).

**Summary statistics (Table 1):**
- Not working: 66 women (8.0%), mean education 11.0 years
- Public sector: 405 (49.2%), mean education 12.4 years, mean hours 1641, mean wage NOK 104.30/hr
- Private sector: 353 (42.8%), mean education 10.9 years, mean hours 1570, mean wage NOK 100.56/hr

# Identification logic

From eq. (2.11): $\psi(h, w; I) \cdot g(h, w) = v_1(f(hw, I)) \cdot v_2(h) \cdot g_1(w|h) \cdot g_2(h)$. The product $v_1(C)$ and $g_1(w|h)$ are nonparametrically identified (Dagsvik and Strøm 1997). The product $v_2(h) \cdot g_2(h)$ is identified but $v_2$ and $g_2$ are NOT separately identifiable without functional form assumptions. This is the fundamental identification limitation of the RURO model (later formalised in Dagsvik and Jia 2016, Theorem 2).

Key quote: "However, it is important to be aware of the fact that if the purpose is to carry out policy simulations for which the distribution of offered hours is kept fixed, it is not necessary to identify $v_2(h)$ and $g_2(h)$, separately" (p. 11).

For sectoral models, sector-specific $b_j$ parameters are identified from sectoral participation rates conditional on education and other covariates.

# Estimation / empirical strategy

1. **Wage equations** (Table 2): Heckman two-stage selection correction. Log wage regressed on experience, experience², education, and $\log P_j$ (selection term). Sector-specific equations. $R^2$ low (0.14 public, 0.08 private) -- motivates random effects in structural model.

2. **Random effects on wages:** $\bar{w}_j = w_j^* \eta_j$ where $\log \eta_j \sim N(0, \sigma_j)$, $j = 1, 2$. Mean wage approximation: $\int \psi(h, y; I) g_{j1}(y) dy \approx \psi(h, \bar{w}_j; I)$.

3. **Structural model** (Table 3): ML estimation of eqs. (4.5)--(4.6), with expectations over random effects computed by simulation ($M = 50$ draws). Parameters: $\alpha_1, \alpha_2$ (Box-Cox exponents), $\alpha_2$ (scale), $\alpha_4$--$\alpha_8$ (leisure taste-shifters: age, children), $\alpha_9$ (interaction), $f_{j1}, f_{j2}$ (opportunity parameters), hours peaks.

4. **Hours discretisation:** 7 intervals per sector, medians from 420 to 2808 annual hours.

# Treatment of preferences

Preferences are modelled through the deterministic component $v(C, h)$ with Box-Cox functional form justified by psychophysical invariance (Theorem 2). Leisure preferences depend on age (convex, minimum around 31--32), number of young children (0--6), and older children (7--17). The interaction term $\alpha_9$ between consumption and leisure is insignificant ($t = -1.4$), so additive separability in consumption and leisure cannot be rejected.

Key finding: the consumption exponent $\alpha_1 = 0.64$ is significantly different from zero, meaning agents care about absolute consumption levels (not just relative). The leisure exponent $\alpha_3 = -0.53$ is not significantly different from zero at 5%, so log-linearity in leisure cannot be rejected.

**Comparison with uniform hours (Table 5):** When offered hours are forced to be uniformly distributed, the leisure exponent becomes $\alpha_3 = -1.88$ (significant, $t = -5.1$) and all leisure taste parameters are scaled down. This demonstrates that ignoring the hours offer distribution biases preference estimates: "if offered hours are not uniformly distributed, which there are good reason to believe, then a change in this institutional constraint will be considered wrongly to yield a shift in preferences" (p. 25).

# Treatment of opportunities / constraints

This is the paper's central innovation. Opportunities are modelled through:

1. **Sector-specific opportunity densities** $g_j(h, w) = g_{j1}(w) \cdot g_{j2}(h)$ (hours and wages independent within sector).

2. **Hours offer density** $g_{j2}(h)$: Piecewise uniform with peaks at full-time (1950 hrs) and part-time (1040 hrs). Full-time peak larger in public sector ($\log$ ratio 1.58, $t = 11.4$) than private (1.06, $t = 7.8$). Part-time peak present in both sectors (public: 0.68, $t = 4.6$; private: 0.80, $t = 5.1$).

3. **Sector-specific opportunity intensity** $b_j = \mu_j \theta_j$: Education increases public sector opportunities ($f_{12} = 0.22$, $t = 2.7$) but decreases private sector opportunities ($f_{22} = -0.33$, $t = -3.0$). This confirms that higher education opens more public sector jobs (universities, health) while potentially "overqualifying" women for private sector positions.

4. **Non-market opportunities:** Captured by the $(1 - \theta_1)$ term in the intensity measure. The non-working option has zero hours and wages but heterogeneous non-pecuniary value through $\varepsilon(z)$.

# Welfare / normative object

No explicit welfare analysis. The paper focuses on positive analysis (choice probabilities, elasticities). Welfare implications are discussed only indirectly through the observation that ignoring opportunity constraints leads to biased preference estimates, which would contaminate welfare calculations.

# Main findings

**Preference estimates (Table 3):**
- Box-Cox consumption exponent $\alpha_1 = 0.64$ (significant): quasi-concave utility
- Leisure exponent $\alpha_3 = -0.53$ (insignificant at 5%): log-linearity in leisure not rejected
- Consumption-leisure interaction $\alpha_9 = -0.12$ (insignificant): additive separability not rejected
- Marginal utility of leisure depends on age (convex, minimum ~32 years) and children (positive effect)

**Opportunity density estimates (Table 3):**
- Full-time peak larger in public sector (log ratio 1.58) than private (1.06)
- Part-time peak in both sectors (public 0.68, private 0.80)
- Education increases public sector opportunities, decreases private sector opportunities

**Model fit (Table 4):** Good fit to participation and sectoral allocation (predicted: 7.9% not working vs. observed 8.0%; public 48.3% vs. 49.2%; private 43.8% vs. 42.8%). McFadden $\rho^2 = 0.21$.

**Aggregate elasticities (Table 6):**
- Overall wage elasticity of participation: 0.26 (both sectors)
- Overall unconditional hours elasticity: 0.61 (both sectors)
- Strong inter-sector substitution: 1% public wage increase → 1.47% increase in public participation but 1.32% decrease in private participation (net: 0.15%)
- Conditional hours elasticity: 0.34 (public + private)

**Comparison: RURO vs. uniform hours (Table 5):**
- Uniform hours model has worse fit (log likelihood $-1862.0$ vs. $-1760.9$)
- Leisure preference parameters are systematically biased under uniform hours assumption
- Key lesson: hours clustering is due to institutional constraints (opportunity density peaks), not strong preferences for specific hours levels

# Main limitations

- Only married women's labour supply (husband's supply taken as given)
- Two sectors only (public vs. private); finer sectoral disaggregation not attempted
- $v_2(h)$ and $g_2(h)$ not separately identified -- functional form assumptions needed
- Wage offer distribution $g_{j1}(w)$ not estimated; replaced by mean wage approximation with random effects
- No welfare analysis; only positive (choice/elasticity) results
- Single cross-section (1994); no panel dimension for dynamics
- IIA assumed at individual level; cannot be tested without stated preference data

# Relevance for my JMP

## possible use for framing
This is the foundational methodological paper for the RURO approach that my JMP builds on. The key insight -- that observed hours clustering reflects opportunity constraints, not just preferences -- directly motivates the $A$-component of $W(z, R, A; y)$. The paper's demonstration that ignoring opportunity structure biases preference estimates provides the empirical case for separating $R$ from $A$.

## possible use for model design
The full model specification is here: Poisson process for opportunities, IIA-based $\varepsilon^{-2}$ intensity, Box-Cox utility from psychophysical invariance, sectoral extension, piecewise uniform hours density with institutional peaks, random effects on wages. This is the template that Capéau et al. (2016) and other RURO applications follow.

## possible use for identification
The paper explicitly states the fundamental identification limitation: $v_2(h) \cdot g_2(h)$ is identified but the components are not separable without functional form. This is the limitation that Dagsvik and Jia (2016) later formalise. For policy simulations where the hours distribution is held fixed, this non-identification is harmless. But for welfare analysis (where $v_2$ matters independently), it is a serious concern.

## possible use for elasticities benchmark
Table 6 provides sector-specific elasticities for Norwegian married women that can be compared with the Bargain-Peichl (2016) meta-analysis benchmarks: overall wage elasticity 0.61 (unconditional hours) is in the upper range for 1990s estimates, consistent with the meta-analysis findings for that period.

# Research questions this paper inspires

1. How do the biased preference estimates under uniform hours affect welfare calculations? If $v_2(h)$ absorbs the effect of $g_2(h)$ when hours offers are assumed uniform, welfare measures computed from the biased $v_2$ will confound preference-based welfare with opportunity structure.

2. Can the sectoral extension be further disaggregated (e.g., by industry or occupation) to capture finer variation in opportunity densities? This would provide a richer $A$-component for $W(z, R, A; y)$.

3. The inter-sector substitution elasticities are large (1.47 for own-sector, -1.32 for cross-sector). What are the welfare implications of sector-specific wage changes when workers reallocate across sectors?

4. Can the psychophysical invariance argument (Theorem 2) be extended to justify functional forms for the opportunity density, not just the utility function?

# Challenge to this paper

The paper's most important theoretical contribution -- the psychophysical justification for Box-Cox utility (Theorem 2) -- rests on Assumptions 4 and 5 (scale invariance of preference rankings). These assumptions are plausible in the absence of satiation but may fail for high consumption/leisure levels where satiation effects become relevant. More fundamentally, the assumptions concern the *aggregate* preference ranking $\tilde{\varphi}$ (the fraction of the population preferring one bundle to another), which mixes individual-level preference heterogeneity with the distribution of unobserved taste-shifters. The invariance may hold for the representative agent but fail for specific subpopulations with different taste distributions. The paper also does not address whether the same invariance principles could justify alternative functional forms if the underlying preference heterogeneity distribution is non-standard. Finally, the mean wage approximation (eq. 4.3) used in estimation may be poor when the wage offer distribution has high variance, which the low $R^2$ of the wage equations (0.08--0.14) suggests is the case.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The paper provides the formal model of how workers choose among latent job opportunities characterised by hours, wages, and non-pecuniary attributes. The opportunity density $g_j(h,w)$ is the formal representation of the $A$-component in $W(z, R, A; y)$, and the systematic utility $v(C, h)$ corresponds to $R$.

[Reasonable inference for my project] The paper's demonstration that preference estimates are biased when the opportunity structure is ignored (Table 5 comparison) implies that welfare calculations based on standard discrete-choice models (van Soest 1995) will confound $R$ and $A$ effects. The $W(z, R, A; y)$ framework's explicit separation avoids this problem.

[Unclear from paper] How to extend the welfare analysis. The paper computes no welfare measures, and the non-identification of $v_2(h)$ separately from $g_2(h)$ means that preference-based welfare measures like CV (Dagsvik and Karlström 2005) cannot be computed without the maintained functional form assumptions. The sensitivity of welfare to these assumptions is an open question.

The paper is closest to: **foundational methodology for the RURO model** and **demonstration that opportunity structure matters for preference estimation in labour supply**.

# Relation to Bargain et al. (2013)

Bargain et al. (2013) compute welfare metrics in a standard discrete-choice model (van Soest type) that assumes uniform hours availability. Dagsvik and Strøm (2006) show that this assumption biases preference estimates. The implication is that Bargain et al.'s welfare metrics may be computed from biased preference parameters -- the $R$-component of their welfare measures confounds genuine preferences with opportunity constraints. Applying Bargain et al.'s welfare metrics to a RURO model (as partially done in Capéau et al. 2021) would produce different welfare rankings if the opportunity density is non-uniform.

# Relation to opportunities vs preferences

This paper is *the* key reference for the opportunities vs. preferences distinction. The central message is that the observed distribution of hours and sector choices reflects both preference heterogeneity ($v(C,h)$ and $\varepsilon(z)$) and opportunity heterogeneity ($g_j(h,w)$ and $\theta_j$). Standard models that ignore opportunity heterogeneity attribute all variation to preferences, leading to: (1) biased utility parameters (Table 5), (2) incorrect elasticities, and (3) potentially misleading welfare conclusions. The RURO framework's explicit separation allows both channels to be estimated and their contributions to labour supply behaviour and welfare to be disentangled.

# Useful quotations / formulas

**Choice probability (Theorem 1, eq. 2.9):**
$$\varphi(h, w; I) = \frac{\psi(h, w; I) \, g(h, w) \, \theta}{\psi(0, 0; I) + \theta \iint_D \psi(x, y; I) \, g(x, y) \, dx \, dy}$$

**Sectoral choice probability (eq. 2.17):**
$$\varphi_j(h, w; I) = \frac{\psi(h, w; I) \, \mu_j \theta_j \, g_j(h, w)}{\psi(0, 0; I) + \sum_{k=1}^m \mu_k \theta_k \iint_D \psi(x, y; I) \, g_k(x, y) \, dx \, dy}$$

**Box-Cox utility (Theorem 2, eq. 2.13):**
$$\log v(C, h) = \beta_1 \frac{C^{\alpha_1} - 1}{\alpha_1} + \beta_2 \frac{L^{\alpha_2} - 1}{\alpha_2} + \beta_3 \frac{(C^{\alpha_1} - 1)(L^{\alpha_2} - 1)}{\alpha_1 \alpha_2}$$

**On opportunity density interpretation (p. 9):**
"$g(h, w) \, dh \, dw$ [can be interpreted] as the fraction of jobs with hours and wage rates within $(h, h + dh) \times (w, w + dw)$ that -- on average -- are *feasible* to the agent."

**On hours clustering (p. 25):**
"through parametric identification our model implies that observed concentration of hours of work around part-time and full-time work arise because there are institutional constraints in the labor market rather than because individuals have strong preferences for full-time and part-time hours of work"

**On bias from ignoring opportunities (p. 25--26):**
"if offered hours are not uniformly distributed, which there are good reason to believe, then a change in this institutional constraint will be considered wrongly to yield a shift in preferences in labor supply models that assume uniformly distributed offered hours"

**On IIA being less restrictive than standard theory (Appendix A, p. 29):**
"the conventional theory yields restrictions that are similar to IIA and appear even more restrictive than IIA"

# Suggested tags

RURO, labour-supply, discrete-choice, Poisson-process, opportunity-density, sectoral-choice, public-sector, private-sector, functional-form, psychophysics, Box-Cox, Stone-Geary, IIA, invariance, married-women, Norway, elasticities, identification, non-identification, hours-clustering, institutional-constraints, Hausman-model, van-Soest

# My quick takeaway

This is the foundational RURO methodology paper. It provides: (1) the Poisson process representation of latent opportunities with IIA-derived $\varepsilon^{-2}$ intensity, (2) the psychophysics-based justification for Box-Cox utility, (3) the sectoral extension with sector-specific opportunity densities and taste parameters, and (4) the crucial empirical demonstration that ignoring opportunity structure (assuming uniform hours) biases preference estimates. For my JMP, the paper provides both the model template and the core motivation: observed labour supply reflects the interaction of preferences ($R$) and opportunities ($A$), and separating them matters for both positive analysis (elasticities) and normative analysis (welfare). The overall unconditional hours elasticity of 0.61 and the large inter-sector substitution effects highlight that sector choice is an important margin that standard one-sector models miss. The main limitation for welfare analysis is the non-identification of $v_2(h)$ from $g_2(h)$ -- a problem that requires functional form assumptions to resolve and that Dagsvik and Jia (2016) later analyse formally.
