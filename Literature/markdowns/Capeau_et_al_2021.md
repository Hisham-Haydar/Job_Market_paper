---
title: "Nonparametric Welfare Analysis for Discrete Choice: Levels and Differences of Individual and Social Welfare"
authors: [Bart Capéau, Liebrecht De Sadeleer, Sebastiaan Maes, André Decoster]
year: 2021
outlet: "CESifo Working Paper No. 9071"
country_or_context: "Germany (empirical application); theoretical (identification results)"
population: "Single females (empirical application)"
data_period: "2018 (German SOEP)"
shelf: "welfare measurement / nonparametric identification / discrete choice / Fleurbaey / NOS measures / social welfare"
tags: [nonparametric, welfare, money-metric-utility, NOS-measures, Fleurbaey, discrete-choice, equivalent-variation, compensating-variation, social-welfare, welfare-levels, welfare-differences, joint-distribution, transition-probabilities, choice-probabilities, unobserved-heterogeneity, labour-supply, flat-tax, Germany, SOEP]
priority: "high"
read_status: "extracted"
---

# Full citation

Capéau, B., De Sadeleer, L., Maes, S., & Decoster, A. (2021). Nonparametric Welfare Analysis for Discrete Choice: Levels and Differences of Individual and Social Welfare. *CESifo Working Paper No. 9071*.

# One-sentence contribution

Adapts Fleurbaey's nested opportunity set (NOS) welfare measures to discrete choice random utility models (DC-RUMs), proves that the full distribution of welfare levels, welfare differences, and their joint distribution can be nonparametrically identified from choice and transition probabilities alone -- without parametric assumptions on preferences or the distribution of unobserved heterogeneity -- and demonstrates the approach empirically on German single females' labour supply, evaluating a flat tax reform.

# Why this paper matters

Prior nonparametric welfare analysis for discrete choice (Bhattacharya 2015, 2018) focused on welfare *differences* (CV, EV) from price changes. This paper extends the analysis to welfare *levels* -- the distribution of individual well-being in any given situation -- using the Fleurbaey NOS class of welfare measures (which includes money metric utilities as a special case). This is critical because: (1) welfare levels allow ranking individuals by well-being, identifying who is poor; (2) levels enable computation of social welfare functions; (3) the *joint* distribution of levels and differences reveals whether winners from a reform were initially well-off or poor. The paper also provides Boole-Fréchet bounds for transition probabilities from cross-sectional data, making the results implementable without panel data.

# Core research question

Can the distributions of individual welfare levels, welfare differences, and their joint distribution be nonparametrically identified from choice and transition probabilities in DC-RUMs with unrestricted unobserved preference heterogeneity? And can these results be used for social welfare analysis?

# Economic setting and context

**Theoretical:** General DC-RUM setting with $n$ alternatives, a numeraire, and unrestricted unobserved preference heterogeneity $\omega$. Utility $U_c^\omega(y - p_c)$ for alternative $c$ at price $p_c$ and income $y$, strictly increasing in the numeraire $y - p_c$.

**Empirical:** German single females, SOEP 2018, choosing among three alternatives: non-working (NW), part-time (PT), full-time (FT). Tax reform: replacing the progressive German income tax with a 42% basic income flat tax.

# Model / theoretical framework

**Preferences:** Individual of type $\omega \in \Omega$ has utility $U_c^\omega(y - p_c)$ for choosing alternative $c$ at price $p_c$ and income $y$. Preferences are unrestricted: $\omega$ can be of any dimension, distributed according to unknown $F(\omega)$.

**Assumptions:**
- **A1 (Monotonicity):** $U_c^\omega$ is continuous and strictly increasing in the numeraire for all $\omega, c$. Plus regularity conditions (R1: price ordering, R2: no ties).
- **A2 (Exogeneity):** Distribution $F(\omega)$ is independent of $(\mathbf{p}, y)$.
- **A3 (RUM):** Individual $\omega$ chooses $i$ iff $U_i^\omega(y - p_i) \geq \max_{c \neq i} U_c^\omega(y - p_c)$.

**NOS welfare measures (Fleurbaey 2009):** A family of nested opportunity sets $\{B_\lambda\}_{\lambda \in \Lambda}$, common to all individuals, is used to define:
$$W^\omega(y - p_k, k) = \max_\lambda \left\{\lambda \mid U_k^\omega(y - p_k) \geq \max_{(y',c) \in B_\lambda} U_c^\omega(y')\right\}$$

The welfare level is the size of the largest opportunity set such that bundle $k$ (at its price) is weakly preferred to everything in $B_\lambda$. This class includes:
- **Money metric utilities (MMU):** $B_\lambda = \{(y',c) \mid y' \leq y - \lambda + p_c^{ref}\}$ -- equivalent to expenditure function evaluation at reference prices $\mathbf{p}^{ref}$.
- **Pazner ray utilities:** $B_\lambda = \{(y',c) \mid y' = \alpha \mathbf{b}^{ref}, \alpha \leq \lambda\}$.
- **Equivalent income:** minimal amount of a numeraire to achieve the same utility under reference values for other dimensions.

**Key Lemma (Lemma 1):** $\{\omega \mid w \leq W^\omega(y-p_k,k)\} = \{\omega \mid U_k^\omega(y-p_k) \geq \max_c U_c^\omega(y - \tilde{p}_c(w))\}$ -- welfare being at least $w$ is equivalent to $k$ being optimal at virtual prices $\tilde{\mathbf{p}}(w)$. This translates welfare events into choice events, enabling nonparametric identification.

# Key objects

- **$W^\omega(y-p_k,k)$:** NOS welfare measure for type $\omega$ evaluated at alternative $k$ with price $p_k$ and income $y$.
- **$P_i(\mathbf{p},y)$:** (Marshallian) choice probability for alternative $i$ at prices $\mathbf{p}$ and income $y$.
- **$P_{i,j}(\mathbf{p},\mathbf{p}',y)$:** Transition probability -- probability that $i$ is optimal at $(\mathbf{p},y)$ and $j$ is optimal at $(\mathbf{p}',y)$.
- **$\tilde{p}_c(\lambda)$:** Virtual prices -- mapping from the NOS index $\lambda$ to prices for alternative $c$.
- **$MMU_{\mathbf{p}^{ref}}^\omega(y-p_k,k)$:** Money metric utility evaluated at reference prices $\mathbf{p}^{ref}$.
- **$CV^\omega$:** Compensating variation -- implicitly defined by $\max_c U_c^\omega(y-p_c) = \max_c U_c^\omega(y-p_c'-CV^\omega)$.
- **$F_W(w \mid \mathbf{p},y)$:** Conditional CDF of welfare given prices and income.
- **$SWF$:** Social welfare function $= \int\int h(w) \, dF_W(w \mid \mathbf{p},y) \, dG(\mathbf{p},y)$.

# Data

**Empirical application:** German Socio-Economic Panel (SOEP), 2018 wave. Sample: 1,922 single females available for the labour market, aged below 60, hourly wages EUR 4--90, yearly asset income below EUR 12,000.

Three alternatives: NW (hours < 5/week), PT (5 $\leq$ hours < 32), FT (hours $\geq$ 32). Disposable income calculated via a German tax-benefit calculator.

Exogenous income $y = d_{FT}$ (disposable income when working full-time). Prices: $p_{NW} = d_{FT} - d_{NW}$, $p_{PT} = d_{FT} - d_{PT}$, $p_{FT} = 0$.

Reference prices for MMU: $p_c^{ref} = \text{med}(d_{FT} - d_c)$ for $c \in \{NW, PT\}$, $p_{FT}^{ref} = 0$.

# Identification logic

**Welfare levels (Theorem 1):** The joint distribution of welfare $W$ in option $k$ and the choice of $j$ at prices $\mathbf{p}'$:
$$\Pr_\omega[w \leq W^\omega(y-p_k,k), j = J^\omega(\mathbf{p}',y)] = P_{j,k}\big(\mathbf{p}', (p_k, \tilde{\mathbf{p}}_{-k}(w)), y\big) \cdot \mathbb{I}[p_k \leq \tilde{p}_k(w)]$$

By Lemma 1, $W \geq w$ is equivalent to $k$ being optimal at virtual prices $\tilde{\mathbf{p}}(w)$. So the distribution of welfare is obtained by evaluating transition probabilities at actual and virtual prices. This requires only choice/transition probabilities -- no parametric structure.

**Welfare differences (Theorem 2--3):** The joint distribution of welfare levels before and after a price change, and the distribution of CV, are expressed as transition probabilities evaluated at initial, final, and virtual prices.

**Joint distribution of levels and CV (Theorem 4):** $\Pr[w \leq MMU, CV^\omega \leq z] = P_{i,j}(\min(\mathbf{p}, \mathbf{p}' + \min(z,y-w)), \mathbf{p}', y) \cdot \mathbb{I}[\cdots]$

**Social welfare (Proposition 2, eq. 35):**
$$F_W(w \mid \mathbf{p},y) = 1 - \sum_k P_k\big(\min(\mathbf{p}, \tilde{\mathbf{p}}(w)), y\big) \mathbb{I}[p_k \leq \tilde{p}_k(w)]$$

All results expressed as functionals of choice and transition probabilities, hence nonparametrically identified.

**Cross-sectional bounds (Proposition 3):** When only cross-sectional data are available (no panel), Boole-Fréchet inequalities + stochastic revealed preference yield bounds on transition probabilities:
$$P_{i,i}^L = \max\{P_i(\mathbf{p},y) + P_i(\mathbf{p}',y) - 1, P_i((\max\{p_i,p_i'\}, \min\{\mathbf{p}_{-i},\mathbf{p}'_{-i}\}),y)\}$$
$$P_{i,i}^U = \min\{P_i(\mathbf{p},y), P_i(\mathbf{p}',y)\}$$

**Shape restrictions (Proposition 4):** $\partial P_i / \partial p_i \leq 0$ and $\partial P_i / \partial p_j \geq 0$ for $j \neq i$ -- own-price decreasing, cross-price increasing.

**Key result for MMU (Corollary 2):** When reference prices equal actual prices and $k$ is optimal, $MMU^\omega_{\mathbf{p}'}(y-p'_k,k) = y$ -- welfare is deterministic and equals exogenous income. This means ~25% of the sample has exactly determinable welfare.

# Estimation / empirical strategy

**Semiparametric estimation of choice probabilities:** Flexible binary logit models for $P_{PT}$ and $P_{FT}$ with cubic polynomials in disposable income of all three alternatives plus demographic covariates (age, education, children, region). $P_{NW}$ is the complement. Penalty function imposed to ensure shape restrictions (Proposition 4).

**Welfare computation:** All distributions computed using eq. (16)--(18) and (27)--(32) with estimated choice probabilities evaluated at actual and virtual prices. Transition probabilities approximated using Boole-Fréchet bounds (cross-sectional data only).

**Tax reform:** Replace progressive German tax with 42% flat rate (revenue-neutral for full SOEP sample). Remove means test for social assistance, making it a basic income.

# Treatment of preferences

Preferences are completely unrestricted: $\omega$ is of arbitrary dimension and distribution, entering utility in any way subject to monotonicity in the numeraire (A1). The paper explicitly does *not* recover preferences -- it shows that welfare distributions can be identified without recovering either deterministic preferences or the distribution of unobserved heterogeneity. This is the central methodological contribution.

# Treatment of opportunities / constraints

Opportunities are modelled implicitly through the family of nested opportunity sets $(B_\lambda)_{\lambda \in \Lambda}$. These are virtual/hypothetical constructs used to *define* welfare, not descriptions of actual constraints. The paper does not model labour demand restrictions, job offer processes, or hours constraints -- it treats the discrete choice set $\{NW, PT, FT\}$ as given and free.

# Welfare / normative object

The paper's central object. Several layers:

1. **Individual welfare levels:** Distribution of $W^\omega$ for any given $(\mathbf{p},y)$ -- allows ranking individuals by well-being.

2. **Individual welfare differences:** Distribution of $CV^\omega$ or changes in NOS measures from price changes.

3. **Joint distribution:** $\Pr[W_0 \leq w, CV \leq z]$ -- reveals whether gainers from reform were initially well-off or poor.

4. **Social welfare:** $SWF = \int\int h(w) \, dF_W(w \mid \mathbf{p},y) \, dG(\mathbf{p},y)$ with NOS measures as the well-being metric. All NOS-based SWFs satisfy interpersonal comparability principles (Fleurbaey and Maniquet 2017, 2018).

5. **Empirical findings:**
   - ~25% of single females have deterministic welfare (step-function distribution)
   - High-wage FT workers' welfare first-order dominates other groups
   - Lower three wage quartiles are intermingled -- unobserved preferences matter greatly
   - Reform (flat tax + basic income) first-order dominates baseline in aggregate
   - But ~15% lose -- predominantly the initially well-off
   - Bottom two-thirds gain: 98% advance, ~half gain up to EUR 200/month
   - Over 40% of the initially best-off third are losers

# Main findings

**Theoretical:**
1. The marginal, conditional, and joint distributions of NOS welfare levels are functionals of choice probabilities (Theorem 1, Corollary 1)
2. The joint distribution of welfare levels and differences (including CV) is a functional of transition probabilities (Theorems 2--4)
3. Social welfare for any additively separable SWF can be computed from choice probabilities alone (Proposition 2, eq. 34--36)
4. Transition probabilities can be bounded from cross-sectional data using Boole-Fréchet inequalities and stochastic revealed preference (Proposition 3)
5. All results generalise Bhattacharya (2015), Dagsvik and Karlström (2005), and de Palma and Kilani (2011) to unrestricted heterogeneity and NOS welfare measures

**Empirical:**
6. High-wage individuals' welfare distribution first-order dominates lower wage groups (Figure 6)
7. Within lower wage quartiles, welfare distributions by choice are intermingled -- unobserved preference heterogeneity matters (Figure 5)
8. Flat tax reform first-order dominates baseline for the population (Figure 7)
9. ~15% of single females lose from reform; losers are disproportionately initially well-off (Table 1: 13.1% of best-off third vs. 0.6% of worst-off third)
10. Among bottom two-thirds of baseline welfare, 98% gain; approximately half gain up to EUR 200/month

# Main limitations

- Working paper (not yet published in a journal as of 2021)
- Empirical application uses only three discrete alternatives (NW, PT, FT) -- coarse
- Cross-sectional data: transition probabilities are bounded, not point-identified (Proposition 3)
- Semiparametric estimation may introduce functional form bias despite the nonparametric theory
- Revenue neutrality of reform is for full SOEP, not for the single-female subsample
- No demand-side restrictions or opportunity heterogeneity -- all labour supply variation attributed to preferences
- Sensitivity to reference prices not explored (acknowledged as future work)
- Ordered choice / outside good issue: identification requires relative price variation across alternatives, which is limited when alternatives are ordered (acknowledged in Section 5)

# Relevance for my JMP

## possible use for framing
This paper bridges the Fleurbaey welfare measurement literature and the nonparametric identification literature for discrete choice. It shows that NOS welfare measures (including equivalent income, which is central to $W(z,R,A;y)$) can be nonparametrically identified from choice probabilities. This provides the welfare-measurement foundation for my JMP.

## possible use for model design
The NOS welfare framework is exactly the class of welfare measures I need for $W(z,R,A;y)$. The paper shows how to implement these measures in discrete choice settings without parametric assumptions. However, my JMP uses a RURO model (with explicit opportunity densities), not a standard DC-RUM -- the question is whether the nonparametric identification results extend to the RURO setting where alternatives are latent.

## possible use for identification
The key identification results (Theorems 1--4) show how welfare distributions map to choice/transition probabilities. In the RURO framework, the "choice probabilities" are functions of both preferences $\Psi$ and opportunities $(q, g_1, g_2)$ -- so the nonparametric results would identify welfare distributions that reflect *both* preference and opportunity heterogeneity. Separating the two channels would require the additional RURO structure.

## possible use for welfare analysis
The joint distribution of welfare levels and CV (Theorem 4) enables exactly the kind of distributional analysis I want: who gains, who loses, and are the gainers initially well-off or poor? The winners-and-losers analysis (Table 1, Figure 8) is a template for my own policy evaluation.

## possible use for social welfare
The SWF construction (Proposition 2, eq. 34--36) shows how to aggregate individual welfare into social welfare using NOS measures and choice probabilities. This provides a rigorous way to evaluate tax-benefit reforms in terms of social welfare without specifying utility functions.

# Research questions this paper inspires

1. Can the nonparametric identification results be extended to the RURO framework where the choice set is latent (continuum of $(w,h)$ jobs)? The RURO model's Fréchet-distributed maximum utility might admit closed-form welfare distributions.

2. The paper treats alternatives as exogenously given. In the RURO model, the feasible set $A$ varies across individuals. How does heterogeneity in $A$ affect the welfare distribution? The NOS measures use a *common* family of opportunity sets -- but actual opportunity sets differ.

3. The joint distribution of MMU and CV (Theorem 4) could be decomposed into a preference-driven component and an opportunity-driven component in the RURO framework. Has this been done?

4. The paper's finding that unobserved preferences matter greatly for welfare levels (lower three quartiles intermingled in Figure 5) suggests that money-metric welfare differs substantially from income. Does this hold in a RURO model where opportunity heterogeneity is also present?

# Challenge to this paper

The paper's key assumption -- A2, that unobserved preference heterogeneity $F(\omega)$ is independent of $(\mathbf{p},y)$ -- is strong in the labour supply context. If workers with different preferences sort into different labour market segments (e.g., high-leisure-preference workers choose occupations with more part-time options), then the budget set $(\mathbf{p},y)$ is endogenous to $\omega$, violating A2. The paper acknowledges this and suggests a control function approach but does not implement it. In the RURO framework, this endogeneity is partly addressed by modelling opportunity heterogeneity explicitly -- but the RURO model has its own identification challenges ($\Psi$ and $g_2$ not separately identified). The empirical application's use of only three alternatives (NW, PT, FT) is also limiting: with so few alternatives, the welfare distributions may be too coarse to capture the heterogeneity that matters for policy.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The NOS welfare measures are exactly the Fleurbaey-type measures used in $W(z,R,A;y)$. The paper explicitly cites Fleurbaey (2006, 2007, 2009), Fleurbaey and Maniquet (2017, 2018), and Decancq et al. (2015) and shows how to implement their welfare concepts nonparametrically.

[Reasonable inference for my project] The paper provides the welfare-measurement side of the $W(z,R,A;y)$ framework: how to go from choice probabilities to welfare distributions. Combining this with the RURO model (which provides the preference-opportunity decomposition) would yield a complete framework for welfare analysis that separates $R$ from $A$. The nonparametric identification results for welfare levels (not just differences) are particularly relevant, as they allow ranking individuals by well-being in any policy scenario.

[Unclear from paper] Whether the NOS welfare measures can be extended to settings with heterogeneous opportunity sets (different $A_i$ for different individuals), as in the RURO model. The paper assumes a common choice set $\mathcal{C}$ -- but in the RURO framework, each individual faces a different realisation of job offers. Also unclear: how the welfare results interact with the Bhattacharya (2015) negative result for ordered choice -- the paper's three-alternative setting (NW, PT, FT) is effectively ordered by hours, but the prices differ across alternatives (due to the nonlinear tax system), so the ordered-choice problem may not bite.

The paper is closest to: **nonparametric identification of Fleurbaey welfare measures in discrete choice** and **distributional welfare analysis of tax reforms**.

# Relation to Bargain et al. (2013)

Bargain et al. (2013) compute three Fleurbaey welfare metrics using a parametric discrete-choice model (van Soest 1995). Capéau et al. (2021) show that the *distribution* of such metrics can be identified nonparametrically from choice probabilities, without the parametric assumptions Bargain et al. impose. This means that Bargain et al.'s welfare rankings could in principle be checked for robustness: do the rankings survive when parametric assumptions are relaxed? The paper's finding that unobserved preference heterogeneity matters greatly for welfare levels (Figure 5) suggests that Bargain et al.'s assumption of a specific heterogeneity distribution (e.g., through logit error terms) may materially affect their welfare results.

# Relation to opportunities vs preferences

The paper does not model opportunity heterogeneity -- it attributes all choice variation to preference heterogeneity $\omega$. The NOS welfare measures use virtual/hypothetical opportunity sets $(B_\lambda)$ to define welfare, but these are not actual opportunity constraints. In the $W(z,R,A;y)$ framework, actual opportunity sets $A$ vary across individuals (some face more job offers than others). The question is whether the NOS welfare measure should be defined relative to common virtual opportunity sets (as in this paper) or relative to individual-specific actual opportunity sets. The former enables interpersonal comparability; the latter reflects actual constraints. This tension is central to the Fleurbaey framework and to my JMP.

# Useful quotations / formulas

**NOS welfare measure (eq. 10):**
$$W^\omega(y-p_k,k) = \sup_\lambda \left\{\lambda \mid U_k^\omega(y-p_k) \geq \max_{(y',c) \in B_\lambda} U_c^\omega(y')\right\}$$

**Key Lemma (Lemma 1, p. 13):**
$$\{\omega \mid w \leq W^\omega(y-p_k,k)\} = \{\omega \mid U_k^\omega(y-p_k) \geq \max_c U_c^\omega(y - \tilde{p}_c(w))\}$$

**Welfare distribution (Theorem 1, eq. 14):**
$$\Pr_\omega[w \leq W^\omega(y-p_k,k), j = J^\omega(\mathbf{p}',y)] = P_{j,k}\big(\mathbf{p}', (p_k, \tilde{\mathbf{p}}_{-k}(w)), y\big) \mathbb{I}[p_k \leq \tilde{p}_k(w)]$$

**Marginal welfare distribution (eq. 17):**
$$\Pr_\omega[w \leq W^\omega(y-p_k,k)] = P_k\big((p_k, \tilde{\mathbf{p}}_{-k}(w)), y\big) \mathbb{I}[p_k \leq \tilde{p}_k(w)]$$

**CV distribution (eq. 27, = Bhattacharya 2015 main result):**
$$\Pr_\omega[CV^\omega \leq z] = \sum_i P_i(\min(\mathbf{p}, \mathbf{p}'+z), y) \mathbb{I}[p_i \leq p_i'+z]$$

**Social welfare CDF (Proposition 2, eq. 35):**
$$F_W(w \mid \mathbf{p},y) = 1 - \sum_k P_k\big(\min(\mathbf{p}, \tilde{\mathbf{p}}(w)), y\big) \mathbb{I}[p_k \leq \tilde{p}_k(w)]$$

**SWF change (eq. 36):**
$$SWF' - SWF = \int\int h(w) \, d\big(F_W(w \mid \mathbf{p}+\Delta\mathbf{p},y) - F_W(w \mid \mathbf{p},y)\big) \, dG(\mathbf{p},y)$$

**On welfare levels (p. 3):**
"Characterising these levels is of first-order importance to applied welfare analysis for at least three reasons. First, knowledge on these levels enables researchers to rank individuals according to their well-being in any given situation [...] Second, in aggregating welfare levels across individuals, overall social welfare can be calculated [...] Third, joint knowledge on levels and differences of welfare enables the investigation of the association between individuals' gains or losses from a price change and their position in terms of initial welfare."

**On unobserved preferences mattering (p. 31):**
"This suggests that, besides wages, both systematic and unobserved preference differences do play an important role in assessing the welfare level of an individual."

**MMU deterministic result (Corollary 2, p. 18):**
"Both the MMU in the optimal bundle and the MMU in bundle $k$, conditional on $k$ being optimal, are, therefore, deterministic and equal the initial exogenous income $y$ when reference equal actual prices."

# Suggested tags

nonparametric, welfare-levels, welfare-differences, NOS-measures, Fleurbaey, money-metric-utility, discrete-choice, DC-RUM, CV, EV, joint-distribution, transition-probabilities, choice-probabilities, social-welfare, Boole-Fréchet-bounds, revealed-preference, unobserved-heterogeneity, labour-supply, flat-tax, Germany, SOEP, interpersonal-comparability, equivalent-income

# My quick takeaway

This paper is the theoretical workhorse for welfare measurement in my JMP. It shows that the full distribution of Fleurbaey-type NOS welfare measures -- including welfare *levels*, not just differences -- can be nonparametrically identified from choice probabilities in discrete choice models. The key insight (Lemma 1) is that "welfare $\geq w$" translates to "optimal choice at virtual prices," so all welfare distributions become functionals of (counterfactual) choice probabilities. The empirical application demonstrates the power of the approach: the joint distribution of welfare levels and CV reveals that 15% lose from a progressive-to-flat reform, and losers are disproportionately initially well-off. For my JMP, the main question is how to extend these results to the RURO setting where: (a) alternatives are latent (not observed), (b) the choice set varies across individuals (opportunity heterogeneity $A$), and (c) the welfare measure should ideally reflect both preference and opportunity channels. The paper's assumption of a common, exogenous choice set is the key limitation for my purposes.
