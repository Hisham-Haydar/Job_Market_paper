---
title: "Nonparametric Welfare Analysis for Discrete Choice"
authors: [Debopam Bhattacharya]
year: 2015
outlet: "Econometrica, 83(2), 617--649"
country_or_context: "Theoretical (no empirical application)"
population: "General consumers facing discrete choices"
data_period: "N/A"
shelf: "welfare measurement / nonparametric identification / discrete choice / CV and EV"
tags: [nonparametric, welfare, equivalent-variation, compensating-variation, discrete-choice, unobserved-heterogeneity, money-metric, consumer-surplus, identification, binary-choice, multinomial-choice, ordered-choice]
priority: "medium-high"
read_status: "extracted"
---

# Full citation

Bhattacharya, D. (2015). Nonparametric Welfare Analysis for Discrete Choice. *Econometrica*, 83(2), 617--649.

# One-sentence contribution

Shows that for binary and unordered multinomial discrete choice with unrestricted unobserved preference heterogeneity, the marginal distributions of equivalent variation (EV) and compensating variation (CV) from a price change are nonparametrically point-identified as simple closed-form functionals of conditional choice probabilities -- without specifying the functional form of utility, the dimension of heterogeneity, or the distribution of unobservables -- but that this result fails for ordered choice with uniform unit price.

# Why this paper matters

Previous welfare analysis for discrete choice either assumed quasilinear utility (Domencich and McFadden 1975), negligible income effects (Small and Rosen 1981), or parametric heterogeneity distributions (Herriges and Kling 1999; Dagsvik and Karlstrom 2005). This paper shows that for unordered multinomial choice, welfare distributions can be recovered from choice probabilities alone under essentially no restrictions on preferences or heterogeneity. This is a fundamental identification result: it establishes that parametric assumptions in applied welfare analysis are not needed for identification but only for computational convenience. The result provides a benchmark for evaluating the robustness of parametric welfare calculations in structural models.

# Core research question

Under what conditions can the marginal distributions of money-metric welfare (EV and CV) from a discrete price change be nonparametrically point-identified from observed choice probabilities, allowing for unrestricted unobserved heterogeneity in preferences?

# Economic setting and context

Purely theoretical. The setting is a consumer facing a discrete choice among $J + 1$ alternatives (including an outside option), with alternative-specific prices, total income $Y$, and vector-valued unobserved taste heterogeneity $\eta$ of unknown dimension and distribution. Examples include: buying vs. not buying a discrete good, choosing among transportation modes, choosing among brands, and -- relevant for labour supply -- choosing among discrete hours/job packages.

# Model / theoretical framework

**Binary choice (Section 2.1):**
Consumer with income $Y$ chooses between buying ($Q = 1$, price $P$) and not buying ($Q = 0$). Utility:
$$\begin{cases} U_1(Y - P, \eta) & \text{if 1 is chosen} \\ U_0(Y, \eta) & \text{if 0 is chosen} \end{cases}$$

**Assumption 1 (only substantive assumption):** For each $\eta$, $U_0(a, \eta)$ and $U_1(a, \eta)$ are continuous and strictly increasing in $a$ (more numeraire is better).

**Structural choice probability:**
$$\bar{q}(p, y) \equiv \Pr\{U_1(y - p, \eta) > U_0(y, \eta)\} = \int \mathbf{1}\{U_1(y - p, \eta) > U_0(y, \eta)\} dF(\eta)$$

**Welfare measures for price rise $p_0 \to p_1$:**
- **EV:** $S^{EV}$ solves $\max\{U_0(y - S, \eta), U_1(y - S - p_0, \eta)\} = \max\{U_0(y, \eta), U_1(y - p_1, \eta)\}$
- **CV:** $S^{CV}$ solves $\max\{U_0(y + S, \eta), U_1(y + S - p_1, \eta)\} = \max\{U_0(y, \eta), U_1(y - p_0, \eta)\}$

**Multinomial choice (Section 2.2):** Extended to $J + 1$ unordered alternatives by defining a composite outside option $U^*(p_{-1}, y, \eta) = \max\{U_0(y, \eta), U_2(y - p_2, \eta), \ldots, U_J(y - p_J, \eta)\}$ and reducing to binary choice.

**Ordered choice (Section 3):** Consumer buys 0, 1, or 2 units at uniform unit price $p$. Welfare distributions are NOT point-identified in this case.

# Key objects

- **$\bar{q}(p, y)$:** Structural (Marshallian) choice probability -- the probability of buying at price $p$ and income $y$, integrating over all types $\eta$.
- **$S^{EV}(y, p_0, p_1, \eta)$:** Equivalent variation for type $\eta$ at income $y$ from price change $p_0 \to p_1$.
- **$S^{CV}(y, p_0, p_1, \eta)$:** Compensating variation for type $\eta$.
- **Reservation price $t(y, \eta)$:** The price at which type $\eta$ is indifferent between buying and not at income $y$. EV equals $t(y, \eta) - p_0$ for "switchers."

# Data

No data used. The paper is purely theoretical (identification theory).

# Identification logic

**Key insight:** The EV for a price increase from $p_0$ to $p_1$ can take only three values for any type $\eta$: (i) $S^{EV} = 0$ for non-buyers (unaffected), (ii) $S^{EV} = t(y,\eta) - p_0$ for "switchers" (those who switch from buying to not buying), where $t$ is the reservation price, (iii) $S^{EV} = p_1 - p_0$ for those who buy at both prices. The CDF of EV is determined by the mass of each group, which depends only on choice probabilities $\bar{q}(\cdot, \cdot)$.

**Theorem 1 (main result for binary choice):**
$$\Pr\{S^{EV} \leq a\} = \begin{cases} 0 & a < 0 \\ 1 - \bar{q}(p_0 + a, y) & 0 \leq a < p_1 - p_0 \\ 1 & a \geq p_1 - p_0 \end{cases}$$

$$\Pr\{S^{CV} \leq a\} = \begin{cases} 0 & a < 0 \\ 1 - \bar{q}(p_0 + a, y + a) & 0 \leq a < p_1 - p_0 \\ 1 & a \geq p_1 - p_0 \end{cases}$$

**Corollary 1 (average welfare):**
$$E(EV) = \int_{p_0}^{p_1} \bar{q}(p, y) \, dp = \text{change in Marshallian consumer surplus}$$
$$E(CV) = \int_{p_0}^{p_1} \bar{q}(p, y + p - p_0) \, dp$$

The average EV equals the change in Marshallian consumer surplus even when utility is not quasilinear -- extending the classical DM75 result. For a normal good, $E(EV) \leq E(CV)$.

**Theorem 2 (multinomial):** Extends to $J + 1$ unordered alternatives by replacing $\bar{q}$ with $\tilde{q}_1(t, p_{-1}, y)$ (the choice probability for alternative 1 at own-price $t$, other prices $p_{-1}$, income $y$).

**Negative result for ordered choice (Section 3):** When unit price is uniform across all alternatives (buy 0, 1, or 2 units at price $p$ per unit), welfare distributions are NOT point-identified because the data do not contain observations where consumers face the specific price-income combinations needed. The identification failure is fundamental, not an artefact of functional form.

# Estimation / empirical strategy

No estimation. The paper provides closed-form expressions for welfare distributions in terms of choice probabilities, which can be estimated nonparametrically (e.g., Nadaraya-Watson) or via parametric models (e.g., logit, mixed logit). The paper provides a computational example using multinomial logit (eq. 23--24).

# Treatment of preferences

Preferences are allowed to be completely general: $\eta$ is vector-valued with unknown dimension and unknown distribution, entering utility in an arbitrary way. The only restriction is Assumption 1 (strict monotonicity in the numeraire). This is the paper's key contribution relative to the prior literature (DM75, SR81, DK05) which imposed quasilinearity, known heterogeneity dimension, or parametric distributions.

# Treatment of opportunities / constraints

Opportunities are not modelled. The framework assumes free choice among all alternatives at given prices -- there are no supply-side restrictions, rationing, or demand constraints. The choice set is assumed to be the full set $\{0, 1, \ldots, J\}$ for all consumers.

# Welfare / normative object

The paper identifies the **full distribution** of EV and CV (not just the mean), which is the most informative welfare object. The distribution allows computation of any functional: mean, median, quantiles, inequality measures, social welfare functions, etc. The welfare measures are money-metric (Hicksian) and satisfy standard properties. No aggregation into a SWF is performed.

# Main findings

1. **Binary and unordered multinomial:** EV and CV distributions are point-identified from choice probabilities alone, under essentially unrestricted heterogeneity (Theorems 1 and 2).

2. **Average EV = change in Marshallian consumer surplus** (Corollary 1, eq. 10). This extends the classical result beyond quasilinear utility.

3. **For normal goods:** $E(EV) \leq E(CV)$ -- the standard relationship from continuous demand theory carries over.

4. **Ordered choice (uniform unit price):** EV and CV distributions are NOT point-identified (Section 3). This is because a change in the per-unit price simultaneously changes the "price" of all quantities, preventing the variation needed to trace out the welfare distribution.

5. **Heterogeneity need not be identified:** The welfare distributions are point-identified even when the dimension and distribution of $\eta$ are not. The Appendix provides an explicit example where different heterogeneity distributions produce identical choice probabilities yet identical welfare distributions.

6. **Parametric computation:** For multinomial logit with $J + 1$ alternatives, average CV is given by eq. (24) -- a simple numerical integral of the logit choice probability.

# Main limitations

- No empirical application in this paper (see Bhattacharya 2018 for the empirical companion)
- Static, one-period framework -- dynamic/sequential discrete choices not covered
- Assumes free choice among all alternatives -- no demand-side restrictions or rationing
- Results require variation in prices and income in the data; if prices are uniform or income has limited variation, nonparametric estimation may not be feasible
- Ordered choice (which includes labour supply with discrete hours at a uniform wage) is the negative case -- welfare distributions are NOT identified

# Relevance for my JMP

## possible use for framing
The paper establishes the theoretical benchmark for welfare analysis in discrete choice models: under what conditions can welfare be identified without parametric assumptions? The negative result for ordered choice (Section 3) is directly relevant for labour supply, where hours are ordered and the "unit price" (wage) is uniform across hours levels. This means that nonparametric welfare identification in the labour supply context requires either (a) treating hours/job alternatives as unordered (as in the RURO model, where different jobs have different wages) or (b) imposing parametric structure.

## possible use for model design
The RURO model's treatment of jobs as unordered alternatives (each with its own wage) places the labour supply problem in the unordered multinomial framework where Bhattacharya's positive identification results apply. This provides a theoretical justification for the RURO approach over standard ordered-choice models (van Soest 1995): in the RURO framework, welfare distributions can in principle be identified nonparametrically, while in the standard model they cannot.

## possible use for identification
The paper's key equation -- $E(EV) = \int \bar{q}(p, y) dp$ -- provides a formula for computing average welfare from choice probabilities alone. In the labour supply context, this would correspond to computing the welfare effect of a tax change from the probability of choosing each job type as a function of the tax parameters. This connects to the Dagsvik-Karlstrom (2005) approach.

## possible use for decomposition
The paper does not decompose welfare into components. However, the distributional results (full CDF of EV and CV) could be used to compute inequality in welfare effects, connecting to the distributional analysis in $W(z, R, A; y)$.

# Research questions this paper inspires

1. Can the nonparametric identification results be extended to the RURO framework where alternatives are latent (unobserved) rather than observed? The RURO model has a continuum of unordered alternatives, which is the limit of the multinomial case.

2. The negative result for ordered choice suggests that labour supply models treating hours as ordered (van Soest 1995) cannot nonparametrically identify welfare distributions. Does the RURO framework's treatment of jobs as unordered resolve this problem?

3. Can the paper's approach be combined with the Fleurbaey welfare metrics from Bargain et al. (2013)? The Fleurbaey metrics are money-metric (like EV/CV) and could potentially be expressed as functionals of choice probabilities.

4. How does the welfare distribution change when the choice set is restricted (as in Beffy et al. 2019)? If individuals face only two offers instead of the full set, the welfare distribution should be computable from the restricted-choice model's probabilities.

# Challenge to this paper

The paper's most important result for labour supply applications is actually the *negative* one: for ordered choice (Section 3), welfare distributions are not point-identified. Since standard discrete-choice labour supply models (van Soest 1995) treat hours as ordered alternatives at a uniform wage, the implication is that nonparametric welfare analysis is not possible in these models without additional structure. The paper does not discuss this implication for the labour supply literature, and does not consider how demand-side restrictions (which break the ordering by offering different wages for different hours) might restore identification. In the RURO framework, where different jobs offer different wage-hours packages, the alternatives are effectively unordered, placing the problem back in the positive identification case -- but this connection is not made in the paper.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The paper provides nonparametric identification of money-metric welfare (EV and CV) in discrete choice settings. These welfare measures are directly related to the "rent" metric in Bargain et al. (2013) and to the equivalent income concept in the $W(z, R, A; y)$ framework.

[Reasonable inference for my project] The positive identification result for unordered choice and the negative result for ordered choice provide a theoretical argument for the RURO framework: by treating jobs as unordered alternatives (each with distinct wages), the RURO model falls into the category where welfare distributions can be nonparametrically identified. Standard ordered-hours models do not have this property.

[Unclear from paper] Whether the nonparametric identification extends to settings with supply-side restrictions (limited choice sets, as in Beffy et al. 2019) or with latent alternatives (as in the RURO model, where the set of available jobs is not directly observed). Also unclear: how the results relate to the preference-heterogeneity welfare metrics (Fleurbaey) rather than standard Hicksian welfare measures.

The paper is closest to: **nonparametric identification of welfare measures** and **theoretical foundations for welfare analysis in discrete choice labour supply models**.

# Relation to Bargain et al. (2013)

Bargain et al. (2013) compute three Fleurbaey welfare metrics that are money-metric (equivalent income). Bhattacharya (2015) shows that money-metric welfare (EV/CV) can be nonparametrically identified from choice probabilities in the unordered case. The connection suggests that Bargain et al.'s metrics might also be expressible as functionals of choice probabilities, potentially allowing nonparametric computation. However, the Fleurbaey metrics involve reference preferences/prices that differ from the standard EV/CV setup, so the exact connection is unclear.

# Relation to opportunities vs preferences

The paper does not address the opportunities-preferences distinction. All welfare variation arises from preference heterogeneity $\eta$ -- there is no modelling of heterogeneous opportunities. In the $W(z, R, A; y)$ framework, the welfare distribution would depend on both $R$ (captured by $\eta$) and $A$ (the feasible set). Extending Bhattacharya's results to settings with heterogeneous choice sets (different $A_i$ for different individuals) is an open question.

# Useful quotations / formulas

**Main result -- EV distribution (Theorem 1, eq. 7):**
$$\Pr\{S^{EV} \leq a\} = 1 - \bar{q}(p_0 + a, y) \quad \text{for } 0 \leq a < p_1 - p_0$$

**Average EV = Marshallian consumer surplus change (Corollary 1, eq. 10):**
$$\mu^{EV}(y, p_0, p_1) = \int_{p_0}^{p_1} \bar{q}(p, y) \, dp$$

**Average CV (eq. 11):**
$$\mu^{CV}(y, p_0, p_1) = \int_{p_0}^{p_1} \bar{q}(p, y + p - p_0) \, dp$$

**On the key insight (p. 640):**
"the conditional choice probabilities alone contain all the relevant information for nonparametric recovery of the resulting welfare distributions"

**On ordered choice failure (p. 639):**
"nonparametric point-identifiability of welfare distributions in the case of unordered multinomial choice and its failure in the ordered case is a fundamental difference that would not be apparent if one were to focus only on parametric models"

# Suggested tags

nonparametric, welfare-identification, equivalent-variation, compensating-variation, discrete-choice, money-metric, unobserved-heterogeneity, consumer-surplus, binary-choice, multinomial-choice, ordered-choice, Marshallian, Hicksian, identification

# My quick takeaway

This paper provides the theoretical foundation for welfare analysis in discrete choice models: welfare distributions are nonparametrically identified from choice probabilities for unordered alternatives but NOT for ordered alternatives at uniform price. For my JMP, the key implication is that the RURO framework -- where jobs are unordered alternatives with distinct wage-hours packages -- has a theoretical advantage for welfare analysis over standard ordered-hours models (van Soest 1995). The nonparametric identification of $E(EV)$ as the integral of choice probabilities provides a clean theoretical benchmark against which parametric welfare calculations (Bargain et al. 2013, Aaberge-Colombino) can be evaluated for robustness. The main gap for my purposes: the paper assumes free choice among all alternatives, ignoring demand-side restrictions that are central to the $A$ component of $W(z, R, A; y)$.
