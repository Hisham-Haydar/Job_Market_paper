---
title: "Empirical Welfare Analysis for Discrete Choice: Some General Results"
authors: [Debopam Bhattacharya]
year: 2018
outlet: "Quantitative Economics, 9(2), 571--615"
country_or_context: "Theoretical + empirical illustration (Southern California fishing)"
population: "General consumers facing discrete choices; empirical: 1182 recreational fishers"
data_period: "Cross-section (Herriges and Kling 1999 / Kling and Thomson 1996 data)"
shelf: "welfare measurement / nonparametric identification / discrete choice / CV and EV / empirical application"
tags: [nonparametric, welfare, compensating-variation, equivalent-variation, discrete-choice, multiple-price-change, elimination-of-alternatives, quality-change, nonexclusive-choice, endogeneity, income-effects, path-dependence, bounds, fishing, logsum, consumer-surplus]
priority: "medium-high"
read_status: "extracted"
---

# Full citation

Bhattacharya, D. (2018). Empirical Welfare Analysis for Discrete Choice: Some General Results. *Quantitative Economics*, 9(2), 571--615.

# One-sentence contribution

Extends Bhattacharya (2015) to four practically important scenarios -- simultaneous multiple price changes, elimination/introduction of alternatives, quality/characteristics changes, and nonexclusive choice -- showing that EV/CV distributions remain nonparametrically point-identified from choice probabilities for (a) and (b), but only bounded for (c) and (d), and provides the first empirical implementation using fishing mode choice data, finding that nonparametric welfare estimates differ substantially from logsum-based estimates (about 2x larger, increasing rather than decreasing with income).

# Why this paper matters

Bhattacharya (2015) established nonparametric identification of welfare distributions for single price changes in unordered discrete choice. But most real policy questions involve simultaneous changes in multiple prices (tax reforms), elimination or introduction of alternatives (banning products, new market entry), or changes in quality/characteristics. This paper shows which of these extensions preserve point identification and which do not, and demonstrates empirically that the nonparametric approach yields qualitatively different welfare estimates from standard logsum methods -- particularly in the income-gradient of welfare, which determines the progressivity of policy evaluation.

# Core research question

Can the nonparametric welfare identification results of Bhattacharya (2015) be extended to simultaneous multiple price changes, elimination/introduction of alternatives, quality changes, and nonexclusive choice? Where point identification fails, what bounds can be constructed?

# Economic setting and context

The theoretical framework is general: a consumer facing discrete choice among $J + 1$ alternatives with unrestricted unobserved preference heterogeneity $\eta$. The empirical application uses data on recreational fishing mode choice in Southern California (Herriges and Kling 1999; Kling and Thomson 1996): 1,182 individuals choosing among 4 modes (beach, pier, private boat, charter boat), with individual income, mode-specific prices (transportation costs), and exogenous catch rates.

# Model / theoretical framework

**Setup (same as Bhattacharya 2015):** Consumer with income $Y$, facing $J + 1$ exclusive alternatives at prices $\mathbf{p} = (p_1, \ldots, p_J)$ (alternative 0 is numeraire with price 0). Utility from alternative $j$: $U_j(y - p_j, \eta)$, strictly increasing in the numeraire argument (Assumption 1). Structural choice probability: $q_j(\mathbf{p}, y) = \Pr\{\text{alternative } j \text{ is chosen at prices } \mathbf{p}, \text{income } y\}$.

**Four extensions:**

1. **Multiple simultaneous price changes (Section 2.1, Theorem 1):** Prices change from $\mathbf{p}_0$ to $\mathbf{p}_1$ with $p_{j1} \geq p_{j0}$ for all $j$ (all prices weakly increase). EV and CV distributions are point-identified as closed-form functionals of choice probabilities.

2. **Elimination of alternatives (Section 2.2, Corollaries 1--2):** Welfare from removing the $J+1$th alternative. The EV distribution for elimination equals the limit of the EV distribution as the eliminated good's price goes to infinity. Formally justified by dominated convergence.

3. **Quality/characteristics changes (Section 3.1, Theorem 2):** When alternative characteristics $x$ change alongside prices, welfare distributions are NOT point-identified from choice probabilities. Bounds via Frechet inequalities are constructible. Weak separability ($U_1 = V_1(h_1(y-p, x), \eta)$) restores point identification (Proposition 2).

4. **Nonexclusive choice (Section 3.2, Theorem 3):** When consumers can buy multiple goods simultaneously, single price change welfare is identified (reduces to binary by grouping all bundles containing the good vs. those not). Multiple simultaneous price changes: NOT identified. Bounds constructible (eqs. 24--25).

**Additional results:**
- **Marshallian CS path-dependence (Appendix, Proposition 1):** For multiple simultaneous price changes, Marshallian consumer surplus is path-dependent -- different integration paths yield different values. Hicksian welfare (EV/CV) remains well-defined.
- **Endogeneity (Section 4.1):** For price increases, income-conditioned EV uses observable (not counterfactual) choice probabilities, so income endogeneity is irrelevant. For CV, the opposite holds. For price decreases, the roles reverse.

# Key objects

- **$q_j(\mathbf{p}, y)$:** Structural choice probability for alternative $j$ at price vector $\mathbf{p}$ and income $y$.
- **EV distribution for multiple price changes (Theorem 1, eq. 8):** Piecewise expression involving sums of choice probabilities evaluated at shifted price-income combinations, with breakpoints at the ordered price changes $p_{l1} - p_{l0}$.
- **Average EV for elimination (Corollary 1, eq. 17):** $E(EV) = \int_0^\infty q_{J+1}(p_1, \ldots, p_J, p_{J+1,0} + a, y) \, da$.
- **Logsum formula (eq. 31):** Standard parametric welfare measure based on conditional logit with constant marginal utility of income $|\alpha|$.
- **Bounds for quality change (Proposition 3, eq. 44):** Frechet-type bounds on $\Pr(S \leq a)$ expressed as max/min of choice probabilities over income values.

# Data

**Empirical illustration (Section 5):** Cross-section of 1,182 recreational fishers in Southern California from Kling and Thomson (1996), previously analysed by Herriges and Kling (1999).

- **Alternatives:** 4 fishing modes -- beach (11% share), pier (15%), private boat (35%), charter boat (38%)
- **Variables:** Individual monthly income (mean $5,250, sd $2,958); mode-specific prices reflecting transportation costs (means: beach $103, pier $103, private $55, charter $84); exogenous catch rates (fish per hour, means: beach 0.24, pier 0.16, private 0.17, charter 0.63)
- **Table 1:** Summary statistics for all variables

# Identification logic

**Multiple price changes (Theorem 1):** The key insight extends Bhattacharya (2015): for each type $\eta$, the EV from simultaneous price increases can take finitely many values determined by which alternatives the consumer switches away from. The mass of each group equals a sum of choice probabilities at specific price-income combinations. The proof (Appendix) shows that $\Pr(EV \leq a)$ decomposes into probabilities involving choice among alternatives at new prices vs. alternatives at old prices shifted by $a$, which equals observable choice probabilities.

**Elimination (Corollaries 1--2):** Formally justified by taking the eliminated good's price to infinity and applying dominated convergence. The "raising price to infinity" heuristic works exactly for average EV (eq. 17) but NOT for average CV or when substitute prices change simultaneously.

**Quality change failure (Theorem 2):** Constructed counterexample with $U_1(y - p, x, \eta) = y - p + x\eta_1$ and $U_0(y, \eta) = (1 - \eta_0)y$. Two different distributions $G_1, G_2$ of $\eta_1$ with the same mean produce identical choice probabilities (eq. 41) but different welfare distributions (eq. 43). Thus $\Pr(S = 0)$ is not identified.

**Nonexclusive failure (Theorem 3):** Multiple simultaneous price changes in nonexclusive setting cannot be decomposed into binary comparisons because each good appears in multiple bundles.

# Estimation / empirical strategy

**Partially linear sieve specification (eq. 29):**
$$q_j(\mathbf{p}, y, x) = h_j(y - p_j) + x'\beta_j + (y\mathbf{1}_{-j} - \mathbf{p}_{-j})'\gamma_j$$
where $h_j(\cdot, \cdot)$ is a cubic in income and own price, $x$ is catch rates, and $y\mathbf{1}_{-j} - \mathbf{p}_{-j}$ captures income net of other alternatives' prices. This is a series/sieve approximation to the true nonparametric choice probabilities.

**Three empirical exercises:**
1. **Multiple price change:** $\mathbf{p}_0 = (140, 140, 60, 12) \to \mathbf{p}_1 = (40, 40, 60, 72)$. Beach/pier prices fall by 100, charter rises by 60, private unchanged. Average CV computed via eq. (30).
2. **Eliminate alternative:** Remove private boat or charter boat. Average CV via eq. (32) = $\int_0^\infty q_4(\cdot) da$.
3. **Quality change:** Decrease beach catch rate from 4th quartile (0.53) to 1st quartile (0.06). Bounds on CV via Proposition 2.

**Comparison:** All exercises compared against logsum estimates (eq. 31) from constrained multinomial logit with constant marginal utility of income.

# Treatment of preferences

Preferences are completely unrestricted: $\eta$ has unknown dimension and distribution, entering utility arbitrarily. The only restriction is Assumption 1 (strict monotonicity in numeraire). No functional form assumed for utility. The empirical specification (eq. 29) is a nonparametric approximation -- a sieve -- not a structural utility function.

# Treatment of opportunities / constraints

No supply-side restrictions or demand constraints modelled. All alternatives are assumed available to all consumers. The elimination exercise (removing private or charter option) is a thought experiment about reducing the choice set exogenously, not about modelling endogenous supply restrictions.

# Welfare / normative object

**Full distributions of EV and CV** (where identified) or **bounds on distributions** (where not). The paper focuses on average CV across exercises, reported as functions of income (Figures 1--4) and at mean income (Table 2). No aggregation into social welfare functions.

# Main findings

**Theoretical:**
1. **Multiple price changes:** EV/CV distributions point-identified from choice probabilities (Theorem 1). Marshallian CS is path-dependent for simultaneous changes (Appendix), but Hicksian measures are not.
2. **Elimination:** EV distribution identified via price-to-infinity limit (Corollary 1). Average EV for elimination = $\int_0^\infty q_{J+1}(\cdot) da$. CV for elimination identified similarly (Corollary 2).
3. **Quality change:** NOT identified (Theorem 2, counterexample). Bounds constructible via Frechet inequalities (Proposition 3). Weak separability restores identification (Proposition 2).
4. **Nonexclusive choice:** Single price change identified; multiple NOT identified (Theorem 3). Bounds via eqs. (24--25).
5. **Endogeneity:** For price increases, EV conditioned on realized income uses observable choice probs -- no endogeneity correction needed. CV requires counterfactual probs. Roles reverse for price decreases.
6. **Iterating single price changes does NOT work:** Cannot compute welfare from simultaneous changes by sequentially applying Bhattacharya (2015) Theorem 2, because individual CV from step 1 is unknown (only its distribution is identified), so income in step 2 is unknown.

**Empirical (Section 5, Figures 1--4, Table 2):**
1. **Multiple price change:** Nonparametric average CV ≈ $42.57 (95% CI: $40.0--$43.1) vs. logsum $19.21. Nonparametric estimate is ~2.2x larger.
2. **Eliminate private boat:** Nonparametric CV ≈ $536.37 (CI: $292--$705) vs. logsum $1,212.4. Nonparametric is less than half the logsum estimate.
3. **Eliminate charter:** Nonparametric CV ≈ $588.16 (CI: $582--$592) vs. logsum $280.29. Nonparametric is ~2.1x larger.
4. **Quality change (catch rate):** Nonparametric bounds: lower ≈ 0, upper ≈ $7.50. Logsum ≈ $4.68. Logsum lies within bounds.
5. **Income gradient:** Logsum estimates *decrease* with income; nonparametric estimates *increase* with income (Figure 1). This reversal arises because the logsum formula treats income as a demographic covariate rather than as part of the budget constraint ($y - p_j$). The income-gradient difference determines whether a policy is assessed as progressive or regressive.
6. **Elimination comparison (Figure 3):** Eliminating either option costs ~10% of mean monthly income (~$530--590). Logsum implies much larger difference between eliminating private vs. charter; nonparametric implies similar losses.

# Main limitations

- Empirical application is illustrative only (fishing, not a high-stakes policy context)
- Sieve approximation (cubic) may not capture all nonlinearities; robustness to quadratic/linear spline noted but not extensively tested
- Bounds for quality change are wide (lower bound near zero) -- may be uninformative in practice
- Independence between budget sets and preferences assumed (no selection on income)
- Price endogeneity discussion is conceptual; no instruments implemented
- Integral for elimination CV truncated at highest observed price (lower bound on true CV)
- Static, one-period framework

# Relevance for my JMP

## possible use for framing
The paper provides the empirical companion to Bhattacharya (2015). The finding that nonparametric and logsum welfare estimates differ by factors of 2+ and have opposite income gradients is a powerful motivation for avoiding restrictive parametric assumptions in welfare analysis. For my JMP, this supports the argument that welfare conclusions from standard discrete-choice labour supply models (which use logsum-type formulas) may be sensitive to the functional form of utility -- and that the RURO framework, by allowing richer preference heterogeneity, can produce more robust welfare estimates.

## possible use for model design
The elimination-of-alternatives result (Corollaries 1--2) is directly relevant for thinking about welfare effects of demand-side restrictions in the RURO framework. If some jobs become unavailable (smaller $A$), the welfare loss can in principle be computed as the CV from eliminating those alternatives -- provided the alternatives are unordered (which they are in RURO).

## possible use for identification
The endogeneity result (Section 4.1) has a direct analogue in labour supply: if wages are endogenous but the welfare question is about the EV from a wage increase, then conditioning on realized income suffices for EV computation. This could simplify welfare analysis in the RURO framework where wage endogeneity is a concern.

## possible use for welfare comparison
The paper's demonstration that logsum-based and nonparametric welfare estimates differ in income-gradient (progressive vs. regressive) is crucial for the $W(z, R, A; y)$ framework. The Fleurbaey welfare metrics in Bargain et al. (2013) are computed from parametric utility functions -- if these have the wrong income gradient (as the logsum does in this application), the distributional welfare conclusions could be reversed.

# Research questions this paper inspires

1. Do the nonparametric welfare results extend to the RURO framework where the choice set itself is latent and individual-specific? The RURO model has a continuum of unordered alternatives with individual-specific availability -- this is between the "free choice" case (where Theorem 1 applies) and the "elimination" case (Corollaries 1--2).

2. The quality-change result (Theorem 2: NOT identified) is relevant for thinking about amenity changes in the RURO framework. If job amenities change (not just wages), welfare distributions are not identified from choice probabilities alone -- but weak separability restores identification. Does the RURO utility specification satisfy weak separability?

3. The income-gradient reversal between nonparametric and logsum estimates has direct implications for the Bargain et al. (2013) welfare metrics. If the Box-Cox utility used there produces logsum-type income gradients, the cross-country welfare rankings could be artefacts of functional form. Can this be tested?

4. Can the bounds for quality change (Proposition 3) be applied to evaluate welfare effects of changes in job amenities (working conditions, flexibility) in the labour supply context?

# Challenge to this paper

The empirical illustration, while informative, uses a dataset (fishing mode choice) that is far from the policy-relevant applications the theoretical results are designed for. The fishing data have only 4 alternatives, low stakes ($100-scale prices against $5,000 monthly income), and no dynamic considerations. The key empirical finding -- that nonparametric estimates differ from logsum by 2x with opposite income gradients -- could be specific to this dataset's features (small number of alternatives, specific price/income ranges). The paper acknowledges this: "It is not obviously possible to conclude empirically whether our estimates are more accurate than the logsum ones" (p. 598). A more convincing demonstration would apply the methods to a setting with higher stakes and more alternatives, such as health insurance choice or mode of transportation -- or indeed labour supply, where the welfare stakes are an order of magnitude larger.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The paper provides nonparametric welfare formulas for elimination of alternatives (Corollaries 1--2), which directly map to the $A$ component of $W(z, R, A; y)$: restricting the feasible set $A$ by removing alternatives is exactly the elimination scenario. The welfare cost of a smaller $A$ can be computed from choice probabilities without specifying the utility function.

[Reasonable inference for my project] The income-gradient result (nonparametric CV increases with income while logsum CV decreases) is relevant for the distributional analysis in $W(z, R, A; y)$. If welfare metrics based on parametric utility (like those in Bargain et al. 2013) produce incorrect income gradients, then the cross-country welfare rankings and the decomposition into $R$-driven vs. $A$-driven inequality could be reversed. The RURO model's richer preference specification may avoid this bias.

[Unclear from paper] Whether the nonparametric approach can handle the RURO model's latent choice set (where the set of available jobs varies across individuals and is not directly observed). The paper assumes all alternatives are available to all consumers -- the identification results may not directly apply when the choice set is individual-specific and unobserved. Also unclear: how to handle the continuous approximation in RURO (continuum of job types) vs. the finite-alternatives setting here.

The paper is closest to: **empirical implementation of nonparametric welfare analysis** and **comparison of parametric vs. nonparametric welfare estimates in discrete choice**.

# Relation to Bargain et al. (2013)

Bargain et al. (2013) compute Fleurbaey welfare metrics using parametric (Box-Cox) utility estimated via discrete-choice models. Bhattacharya (2018) shows that such parametric welfare estimates can differ dramatically from nonparametric ones -- by factors of 2+, with opposite income gradients. This raises the question of whether Bargain et al.'s cross-country welfare rankings are robust to relaxing the Box-Cox functional form. If the income gradient of welfare is wrong (as the logsum example suggests), then the assessment of which countries provide higher well-being to their workers could be reversed. The paper's results suggest that parametric welfare calculations should at minimum be benchmarked against nonparametric estimates.

# Relation to opportunities vs preferences

The paper does not address the opportunities-preferences distinction. All variation in welfare outcomes arises from preference heterogeneity $\eta$ -- there is no modelling of heterogeneous opportunity sets. However, the elimination-of-alternatives results (Corollaries 1--2) provide a framework for evaluating the welfare cost of restricted opportunities: if some individuals face smaller choice sets (fewer available jobs in the RURO context), the welfare loss from each missing alternative can be computed. The challenge is that in the RURO framework, the restricted choice set is individual-specific and latent, whereas in this paper it is common and known.

# Useful quotations / formulas

**Average EV for elimination (Corollary 1, eq. 17):**
$$E(EV) = \int_0^\infty q_{J+1}(p_1, \ldots, p_J, p_{J+1,0} + a, y) \, da$$

**CV distribution for multiple price changes (eq. 30, applied to 4 alternatives):**
$$\Pr(CV \leq a) = \begin{cases} 0 & a < -100 \\ (q_1 + q_2)(40 - a, 40 - a, 60, 12, y, x) & -100 \leq a < 0 \\ 1 - q_4(40, 40, 60, 12 + a, y + a, x) & 0 \leq a < 60 \\ 1 & a \geq 60 \end{cases}$$

**On the income-gradient reversal (p. 593--594):**
"Evidently, the logsum estimates are small, and decrease with income, whereas our CV estimates imply larger (about 2 times) welfare losses which increase with income."

**On logsum vs. nonparametric (p. 593):**
"The substantive difference in functional forms between (29), (30), and (31) is in how price and income appear in them. The logsum formula is based on the constant marginal utility of income, and thus requires price coefficients to be identical across alternatives."

**Key empirical comparison (Table 2, at mean income $4,000/month):**
| Exercise | Cubic approx. | 95% CI | LogSum |
|---|---|---|---|
| Multiple price change | $42.57 | $40.0--43.1 | $19.21 |
| Eliminate private boat | $536.37 | $292--705 | $1,212.4 |
| Eliminate charter | $588.16 | $582--592 | $280.29 |
| Decrease catch rate | $7.05 | $4.55--11.91 | $4.68 |

**On the approach's advantages (p. 598--599):**
"our estimates correspond to a theoretically consistent utility structure, do not impose constant marginal utility of income, and are not based on specific distributional assumptions, they should be viewed as more robust on theoretical grounds"

**On practical applications (p. 599):**
"our methods can be used in program evaluation studies to calculate 'compensated' program effects, that is, the program's value to the subjects themselves, measured in terms of its cash equivalent, and the associated deadweight loss"

# Suggested tags

nonparametric, welfare-identification, compensating-variation, equivalent-variation, discrete-choice, multiple-price-change, elimination-of-alternatives, quality-change, nonexclusive-choice, endogeneity, income-effects, path-dependence, Marshallian, Hicksian, bounds, logsum, sieve-estimation, fishing, empirical-welfare

# My quick takeaway

This paper delivers the empirical payoff of Bhattacharya (2015): nonparametric welfare formulas applied to real data produce estimates that differ from standard logsum formulas by factors of 2+ with *opposite* income gradients. The income-gradient reversal is the most important finding for my JMP: it means that the standard parametric approach (which underlies Bargain et al. 2013's welfare metrics) could be getting the distributional incidence of policy changes wrong -- assessing a policy as progressive when it is actually regressive, or vice versa. The elimination-of-alternatives results provide a theoretical framework for evaluating welfare costs of restricted choice sets ($A$ in $W(z, R, A; y)$), though extending this to the RURO model's latent, individual-specific choice sets remains an open question. The negative results for quality change and nonexclusive choice are also important: they define the boundaries of what nonparametric welfare analysis can achieve and where parametric structure (or at least weak separability) is unavoidable.
