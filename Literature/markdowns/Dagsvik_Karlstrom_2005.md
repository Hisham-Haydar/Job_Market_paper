---
title: "Compensating Variation and Hicksian Choice Probabilities in Random Utility Models that are Nonlinear in Income"
authors: [John K. Dagsvik, Anders Karlström]
year: 2005
outlet: "Review of Economic Studies, 72(1), 57--76"
country_or_context: "Theoretical (with numerical examples)"
population: "General consumers facing discrete choices"
data_period: "N/A"
shelf: "welfare measurement / compensating variation / Hicksian demand / discrete choice / random utility"
tags: [compensating-variation, Hicksian-choice-probabilities, random-expenditure-function, discrete-choice, nonlinear-income, GEV, nested-logit, logsum, welfare, money-metric, Shephard-lemma]
priority: "high"
read_status: "extracted"
---

# Full citation

Dagsvik, J. K., & Karlström, A. (2005). Compensating Variation and Hicksian Choice Probabilities in Random Utility Models that are Nonlinear in Income. *Review of Economic Studies*, 72(1), 57--76.

# One-sentence contribution

Derives closed-form expressions for the distribution of the random expenditure function, Hicksian (compensated) choice probabilities, and the distribution of compensating variation (CV) in discrete-choice random utility models where utility is nonlinear in income -- extending the logsum welfare formula to the general nonlinear case and establishing a Shephard's Lemma for aggregate discrete-choice expenditure.

# Why this paper matters

The standard welfare measure in discrete choice -- the logsum formula (Small and Rosen 1981, Williams 1977) -- requires utility to be linear in income (quasilinear preferences), which rules out income effects. Many important applications (labour supply, housing, health insurance) involve nonlinear budget sets where income effects are substantial. This paper provides the general theory for computing welfare (CV distributions) in these nonlinear settings, extending Hicksian demand theory to discrete choice with random utility. It is the theoretical foundation for welfare analysis in structural discrete-choice labour supply models (van Soest 1995, Aaberge-Colombino), where utility is typically nonlinear in consumption/income.

# Core research question

How can compensating variation and Hicksian (compensated) choice probabilities be defined, computed, and characterized in discrete-choice random utility models where the deterministic utility component is nonlinear in income?

# Economic setting and context

Purely theoretical. The setting is a consumer choosing among $m$ discrete alternatives indexed $j \in B = \{1, \ldots, m\}$, where alternative $j$ has quality attribute $w_j$ and the consumer has total income $y$. Utility for alternative $j$ is $U_j = v_j(w_j, y) + \varepsilon_j$, where $v_j$ is the deterministic component (nonlinear in $y$) and $\varepsilon_j$ is a random taste shock. The paper covers general joint distributions of $(\varepsilon_1, \ldots, \varepsilon_m)$, with special results for GEV and i.i.d. extreme value cases.

# Model / theoretical framework

**Utility:** For alternative $j \in B$:
$$U_j = v_j(w_j, y) + \varepsilon_j$$
where $v_j(w_j, y)$ is continuous and strictly increasing in $y$, and $(\varepsilon_1, \ldots, \varepsilon_m)$ has joint CDF $F(\varepsilon_1, \ldots, \varepsilon_m)$.

**Marshallian choice:** The consumer chooses $J_B(w, y) = \arg\max_{j \in B} U_j$, achieving indirect utility $V_B(w, y) = \max_{j \in B} U_j$.

**Marshallian choice probability:**
$$P_B(j, w, y) = \Pr\{J_B(w, y) = j\} = \int F_j^B(v_j - v_1, \ldots, v_j - v_m) \, dv_j$$
where $F_j^B$ is $(-1)^{m-1}$ times the mixed partial derivative of $F$ w.r.t. all arguments except $j$.

**Random expenditure function (Definition 1):**
$$Y_B(w, u) = \min_{k \in B} Y_k(w_k, u - \varepsilon_k)$$
where $Y_k(w_k, \cdot) = v_k^{-1}(w_k, \cdot)$ is the income needed to achieve utility level $u - \varepsilon_k$ from alternative $k$. This is the minimum income needed to achieve utility level $u$ across all alternatives, given the random taste vector.

**Hicksian choice probability (Definition 2):**
$$P_B^h(j, w, u) = \Pr\{J_B(w, Y_B(w, u)) = j\}$$
The probability of choosing $j$ when income is set to the expenditure function level -- i.e., compensated demand.

# Key objects

- **$V_B(w, y)$:** Random indirect utility (maximum utility achievable at prices $w$, income $y$).
- **$Y_B(w, u)$:** Random expenditure function (minimum income to achieve utility $u$ at prices $w$). Satisfies $Y_B(w, V_B(w, y)) = y$ and $V_B(w, Y_B(w, u)) = u$.
- **$P_B^h(j, w, u)$:** Hicksian choice probability -- compensated demand analogue in discrete choice.
- **$EY_B(w, u) = E[Y_B(w, u)]$:** Expected expenditure function.
- **CV:** $CV = y^1 - Y_B(w, V_B(w^0, y^0))$ -- the income adjustment needed at new prices $w$ to maintain old utility $V_B(w^0, y^0)$.

# Data

No data. Numerical examples use hypothetical parameter values for nested logit models.

# Identification logic

Not applicable (theoretical paper). The paper shows that all welfare objects (CV distribution, Hicksian probabilities, expected expenditure) are computable from knowledge of $v_j(w_j, y)$ and $F(\varepsilon)$ -- the same primitives that determine Marshallian choice probabilities. In applied work, these primitives are estimated from observed choices, and the paper's formulas then deliver welfare measures.

# Estimation / empirical strategy

No estimation. The paper derives analytical formulas. Section 8 provides four worked examples:

1. **Nested logit (4 alternatives):** Numerical computation of CV distribution, Hicksian probabilities, and mean/variance of expenditure for a hypothetical quality improvement scenario.

2. **Introduction of a new alternative:** CV from expanding the choice set from $B$ to $B \cup \{k\}$.

3. **Removal of an alternative:** CV from shrinking the choice set.

4. **Linear utility (logsum recovery):** When $v_j = \alpha_j + \gamma y$ (quasilinear), mean CV reduces to:
$$E[CV] = y^0 + \frac{1}{\gamma} \log \sum_{k \in B} e^{v_k(w_k^0)} - \frac{1}{\gamma} \log \sum_{k \in B} e^{v_k(w_k)}$$
recovering the standard logsum formula.

# Treatment of preferences

Preferences are represented by $v_j(w_j, y) + \varepsilon_j$ with $\varepsilon$ capturing unobserved taste heterogeneity. The framework is completely general regarding the functional form of $v_j$ (only monotonicity in $y$ required) and the distribution of $\varepsilon$ (any absolutely continuous joint CDF). Income effects are fully permitted -- this is the paper's key advance over the logsum approach.

# Treatment of opportunities / constraints

The choice set $B$ is exogenous and known. No supply-side restrictions or opportunity densities are modelled. The framework assumes all alternatives in $B$ are available to all consumers.

# Welfare / normative object

**Compensating variation (CV):** The income adjustment at new prices that maintains old utility:
$$CV = y^1 - Y_B(w, V_B(w^0, y^0))$$

The paper derives:
- The **full distribution** of CV (not just the mean), via Corollary 2
- The **joint distribution** of CV with initial and compensated choices (Theorem 4)
- **Moments** of the expenditure function (Lemma 1, eqs. 17--18)

The welfare measure is money-metric (Hicksian), individual-level, and accounts for income effects.

# Main findings

**Theorem 1 (distribution of expenditure function):**
$$\Pr\{Y_B(w, u) \leq y\} = 1 - F^B(u - v_1(w_1, y), \ldots, u - v_m(w_m, y))$$
where $F^B(\varepsilon_1, \ldots, \varepsilon_m) = \Pr\{\varepsilon_1 \leq \varepsilon_1, \ldots, \varepsilon_m \leq \varepsilon_m\}$ is the joint survivor function of the $\varepsilon$'s evaluated at $u - v_j$.

**Theorem 2 (Hicksian choice probabilities):**
$$P_B^h(j, w, u) = \int F_j^B(u - v_1(w_1, y), \ldots, u - v_m(w_m, y)) \, v_j(w_j, dy)$$
This is the discrete-choice analogue of Hicksian demand.

**Corollary 1 (Shephard's Lemma):**
$$\frac{\partial EY_B(w, u)}{\partial w_{1j}} = P_B^h(j, w, u)$$
where $w_{1j}$ is a scalar component of $w_j$ entering $v_j$ with unit coefficient. The Hicksian choice probability is the derivative of expected expenditure with respect to quality -- exactly paralleling continuous Shephard's Lemma.

**Theorem 3 (joint distribution of expenditure and initial choice):**
$$\Pr\{Y_B(w, V_B(w^0, y^0)) \leq y, \, J_B(w^0, y^0) = j\} = \int_0^{v_j^0} F_j^B(u - v_1, \ldots, u - v_m) \, du$$
evaluated at $v_k = v_k(w_k, y)$ for $k \neq j$ and $v_j = v_j(w_j^0, y^0)$, where $v_j^0 = v_j(w_j^0, y^0)$.

**Corollary 2 (CV distribution conditional on initial choice):**
The distribution of CV conditional on initial choice $j$ follows directly from Theorem 3.

**Theorem 4 (joint with compensated choice):**
Extends to the joint distribution of expenditure, initial choice, and compensated choice $J_B^*(w^0, y^0, w) = J_B(w, Y_B(w, V_B(w^0, y^0)))$.

**Special cases:**
- **GEV (Corollary 3):** Explicit density formulas for GEV class models (nested logit, multinomial logit).
- **i.i.d. extreme value (Corollary 5):** Hicksian probability $= \frac{e^{v_j(w_j, y)}}{\sum_k e^{v_k(w_k, y)}} v_j'(w_j, y)$, which is Marshallian probability times marginal utility of income at the expenditure-function income level.
- **Linear utility (Example 4):** Mean CV reduces to the logsum formula, confirming this as a special case of the general theory.

# Main limitations

- Purely theoretical: no empirical application demonstrating the practical importance of the nonlinear extension
- Assumes the choice set $B$ is fixed and known (no latent alternatives, no demand-side restrictions)
- Random taste shocks $\varepsilon_j$ must be independent of income $y$ (no income-dependent heteroskedasticity)
- Computation requires numerical integration for all but the simplest cases (i.i.d. extreme value)
- Does not address nonparametric identification: assumes $v_j$ and $F$ are known (estimated in a prior step)
- Does not connect to labour supply models where "prices" are tax-benefit schedules rather than simple commodity prices

# Relevance for my JMP

## possible use for framing
The paper provides the theoretical foundation for computing money-metric welfare in discrete-choice models with nonlinear income effects -- precisely the setting of structural labour supply models. The Hicksian choice probability concept is the discrete-choice analogue of compensated labour supply, and the CV distribution is the welfare object that the $W(z, R, A; y)$ framework seeks to extend beyond money-metric measures.

## possible use for model design
The paper's framework can be applied directly to the RURO model: once preferences $v_j(w_j, y)$ and the distribution of $\varepsilon$ are estimated, the formulas in Theorems 1--4 deliver CV distributions for any policy change. The key extension needed for RURO is to handle the latent choice set (random $B$) rather than a fixed choice set -- this is addressed in Dagsvik and Karlström's own discussion (p. 73) and in Capéau et al. (2021).

## possible use for identification
Corollary 1 (Shephard's Lemma) provides a testable restriction: the derivative of expected expenditure with respect to a quality attribute equals the Hicksian choice probability. This could be used to test the internal consistency of structural labour supply estimates.

## possible use for welfare computation
The CV formulas provide the money-metric welfare benchmark against which the $W(z, R, A; y)$ framework's richer welfare measures can be compared. In particular, the CV captures only preference-based welfare ($R$-component) and does not account for opportunity restrictions ($A$-component). The difference between CV-based welfare and $W$-based welfare isolates the contribution of opportunity heterogeneity to well-being.

# Research questions this paper inspires

1. How do the CV distributions from the nonlinear formulas compare to logsum-based welfare in typical labour supply applications? If income effects are large (as expected for low-income workers), the logsum may substantially misbehave.

2. Can the Hicksian choice probability formulas be extended to the RURO setting where the choice set $B$ is random (drawn from an opportunity distribution)? This would require integrating over the random choice set.

3. The paper's CV is a money-metric welfare measure. How does it relate to the Fleurbaey-Maniquet equivalent income measures used in Bargain et al. (2013) and Capéau et al. (2021)? Is there a formal mapping between CV and NOS welfare?

4. Can the joint distribution of CV and initial choice (Theorem 3) be used to identify "winners" and "losers" from a policy reform by demographic group, without specifying a social welfare function?

# Challenge to this paper

The paper assumes a fixed, known choice set $B$ -- all consumers can access all alternatives. In labour supply applications, this is a strong assumption: workers face heterogeneous opportunity sets (different available jobs, hours constraints, hiring probabilities). The RURO model addresses this by making $B$ random with an estimated opportunity distribution. Extending the CV formulas to random $B$ is conceptually straightforward (condition on $B$ and integrate) but practically challenging because the opportunity set is latent. The paper also treats utility as additively separable in $v_j$ and $\varepsilon_j$, which excludes random coefficients on income -- a restriction that may matter for heterogeneous income effects. Section 5 discusses the random coefficients extension but provides no closed-form results.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The paper provides the money-metric welfare theory (CV distributions) for discrete-choice models with nonlinear income. The CV is a preference-based welfare measure that captures the $R$-component of $W(z, R, A; y)$.

[Reasonable inference for my project] The CV formulas, applied to a RURO model, would give the welfare effect of a tax-benefit reform holding the opportunity distribution fixed. Comparing this CV to the full $W(z, R, A; y)$ change (which also accounts for opportunity-set changes) would isolate the $A$-component's contribution to welfare. This decomposition is exactly what the $W$ framework is designed to deliver.

[Unclear from paper] How to extend the CV formulas to settings where the opportunity set $A$ is heterogeneous and potentially affected by policy. The paper's framework treats the choice set as exogenous, while in the $W(z, R, A; y)$ framework, $A$ is an endogenous component of well-being that may respond to policy.

The paper is closest to: **theoretical foundation for money-metric welfare in discrete-choice labour supply models** and **benchmark for preference-based welfare against which opportunity-inclusive measures can be compared**.

# Relation to Bargain et al. (2013)

Bargain et al. (2013) compute Fleurbaey welfare metrics (NOS measures) that go beyond standard CV by incorporating reference preferences and fairness considerations. Dagsvik and Karlström (2005) provide the standard Hicksian CV theory that Bargain et al.'s measures extend. The key difference: CV measures welfare relative to the individual's own preferences, while NOS measures evaluate welfare relative to reference preferences -- allowing interpersonal comparisons. The formal connection is that both are money-metric: CV answers "how much income at new prices gives old utility?" while NOS answers "how much income at reference prices gives current utility with reference preferences?" Capéau et al. (2021) make this connection explicit by showing both are computable from choice probabilities.

# Relation to opportunities vs preferences

The paper is purely preference-based: welfare depends only on $v_j(w_j, y)$ and $\varepsilon_j$, with no role for opportunity heterogeneity. The CV is defined over a fixed choice set $B$, so all welfare variation comes from taste heterogeneity ($\varepsilon$) and price/income changes -- not from differences in available alternatives. In the $W(z, R, A; y)$ framework, this corresponds to fixing $A$ (full choice set) and measuring welfare from $R$ alone. The paper's CV would understate welfare losses for individuals with restricted opportunity sets (small $A$) and overstate welfare gains for those who cannot access the theoretically available alternatives.

# Useful quotations / formulas

**Random expenditure function (Definition 1, eq. 3):**
$$Y_B(w, u) = \min_{k \in B} Y_k(w_k, u - \varepsilon_k)$$

**Distribution of expenditure (Theorem 1, eq. 5):**
$$\Pr\{Y_B(w, u) \leq y\} = 1 - F^B(u - v_1(w_1, y), \ldots, u - v_m(w_m, y))$$

**Hicksian choice probability (Theorem 2, eq. 7):**
$$P_B^h(j, w, u) = \int F_j^B(u - v_1(w_1, y), \ldots, u - v_m(w_m, y)) \, v_j(w_j, dy)$$

**Shephard's Lemma (Corollary 1, eq. 9):**
$$\frac{\partial EY_B}{\partial w_{1j}} = P_B^h(j, w, u)$$

**CV distribution (from Corollary 2):**
$$\Pr\{CV \leq c \mid J_B(w^0, y^0) = j\} = \frac{\Pr\{Y_B(w, V_B(w^0, y^0)) \leq y^1 - c, \, J_B(w^0, y^0) = j\}}{P_B(j, w^0, y^0)}$$

**Linear utility recovery of logsum (Example 4, p. 73):**
$$E[CV] = y^0 + \frac{1}{\gamma} \log \sum_{k \in B} e^{v_k(w_k^0)} - \frac{1}{\gamma} \log \sum_{k \in B} e^{v_k(w_k)}$$

**On the key contribution (p. 57):**
"Our paper generalizes the standard logsum formula to the case in which utility is nonlinear in income"

**On Shephard's Lemma (p. 63):**
"We may think of Corollary 1 as a discrete choice version of Shephard's Lemma"

# Suggested tags

compensating-variation, Hicksian-choice-probabilities, random-expenditure-function, discrete-choice, nonlinear-income, GEV, nested-logit, i.i.d.-extreme-value, logsum, Shephard-lemma, welfare-distribution, money-metric, income-effects, random-utility

# My quick takeaway

This paper provides the complete Hicksian demand/expenditure theory for discrete choice with nonlinear income -- extending the logsum welfare formula to the empirically relevant case where utility is nonlinear in income (income effects present). The key results are: (1) the random expenditure function $Y_B(w,u)$ has a tractable distribution (Theorem 1), (2) Hicksian choice probabilities satisfy a Shephard's Lemma (Corollary 1), (3) the full distribution of CV -- not just the mean -- is computable (Theorems 3--4), and (4) the logsum is recovered as a special case. For my JMP, this is the money-metric welfare benchmark: it gives the CV from tax-benefit reforms in standard discrete-choice models. The $W(z, R, A; y)$ framework extends beyond this by incorporating opportunity heterogeneity ($A$) and reference-preference welfare measures (Fleurbaey/NOS), but Dagsvik-Karlström CV remains the natural comparison point. The main gap: the paper assumes a fixed choice set, so extending to RURO (random opportunity set) requires additional integration over latent $B$.
