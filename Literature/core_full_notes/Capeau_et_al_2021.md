---
title: "Nonparametric Welfare Analysis for Discrete Choice: Levels and Differences of Individual and Social Welfare"
authors: [Bart Capéau, Liebrecht De Sadeleer, Sebastiaan Maes, André Decoster]
year: 2021
outlet: "CESifo Working Paper No. 9071"
shelf: "Welfare measurement / Equivalent income / Money-metric"
note_type: "canonical"
---

## Full citation
Capéau, B., De Sadeleer, L., Maes, S., & Decoster, A. (2021). Nonparametric Welfare Analysis for Discrete Choice: Levels and Differences of Individual and Social Welfare. *CESifo Working Paper No. 9071*.

## One-sentence contribution
Extends the nonparametric welfare-identification programme from Bhattacharya (2015) to Fleurbaey-style nested opportunity set (NOS) welfare measures, showing that the joint distribution of welfare *levels* and *differences* — and therefore additively-separable social welfare — is identified from choice and transition probabilities alone, with a German SOEP application that finds ~15% of single females lose from a flat-tax + basic-income reform and that losers are disproportionately initially well-off.

## Core research question
Can the marginal, conditional, and joint distributions of NOS welfare levels (a class that nests money-metric utility and equivalent income), of welfare differences such as compensating variation, and of the social welfare functional that aggregates them, be nonparametrically identified from observed choice and transition probabilities in DC-RUMs with unrestricted unobserved preference heterogeneity?

## Model / framework
A DC-RUM with $n$ alternatives, a numeraire, and an arbitrary unobserved preference type $\omega$. Utility $U_c^\omega(y-p_c)$ is continuous and strictly increasing in the numeraire (A1), with $F(\omega)$ exogenous to $(\mathbf{p},y)$ (A2) and standard utility maximisation (A3). The NOS welfare measure $W^\omega(y-p_k,k)=\sup_\lambda\{\lambda\mid U_k^\omega(y-p_k)\ge\max_{(y',c)\in B_\lambda}U_c^\omega(y')\}$ uses a common nested family of opportunity sets and includes money-metric utility, Pazner ray utilities, and equivalent income as special cases. The pivotal Lemma 1 translates "welfare exceeds $w$" into "alternative $k$ is optimal at virtual prices $\tilde{\mathbf{p}}(w)$", which is what reduces welfare distributions to functionals of choice/transition probabilities.

## Data
German SOEP 2018, 1,922 single females under 60, hourly wages 4–90 EUR, asset income below 12,000 EUR/yr. Three discrete alternatives — non-working, part-time (5–32h/wk), full-time ($\ge$ 32h/wk) — with disposable incomes from a German tax-benefit calculator. Counterfactual: replace the progressive tax with a 42% flat rate plus an unconditional basic income (revenue-neutral on the full SOEP).

## Identification logic
Lemma 1 maps welfare events to choice events at virtual prices. Theorem 1 turns the marginal welfare CDF into a single-choice probability $P_k$ evaluated at virtual prices; Theorems 2–4 turn joint distributions of welfare levels and CV into transition probabilities $P_{i,j}$ at combinations of actual, post-reform, and virtual prices; Proposition 2 expresses any additively-separable social welfare functional as an integral of choice probabilities. With cross-sectional data only, transition probabilities are not point-identified but are bounded via Boole-Fréchet inequalities and a stochastic revealed-preference shape restriction (Proposition 3), giving sharp upper and lower envelopes for welfare distributions and SWF differences.

## Treatment of preferences
Maximally general: $\omega$ has arbitrary dimension and distribution. The paper deliberately does not recover preferences or their distribution — the welfare distributions are identified without recovering either. This is the core methodological contribution and the strongest possible robustness statement against parametric mis-specification of $v(C,h)$ in the labour-supply welfare literature.

## Treatment of opportunities / constraints
Not modelled empirically. The choice set $\{NW,PT,FT\}$ is treated as freely available to all individuals. Opportunities enter only as the family of nested *virtual* opportunity sets $B_\lambda$ used to define welfare — these are normative reference objects, not descriptions of demand-side rationing. The paper acknowledges that endogeneity of $(\mathbf{p},y)$ to $\omega$ would violate A2, and that real-world heterogeneity in actual choice sets is outside the framework.

## Welfare / normative object
Several layers. (i) Distribution of NOS welfare levels for individual ranking. (ii) Distribution of CV for distributional incidence of price changes. (iii) Joint distribution of levels and CV for "who-gains-where-on-the-distribution" analysis. (iv) Additively-separable social welfare functional with NOS welfare as the sub-utility.

## Main findings
(i) Theorems 1–4 deliver closed-form representations of welfare distributions as functionals of choice/transition probabilities. (ii) Proposition 2: SWF differences are integrals of choice probabilities at virtual prices. (iii) Proposition 3: cross-sectional Boole-Fréchet bounds on transition probabilities, sharpened by stochastic revealed preference. (iv) Empirically, ~25% of single females have deterministic welfare under MMU at actual reference prices. (v) High-wage full-time workers' welfare first-order dominates other groups, but lower wage quartiles are intermingled — unobserved preferences carry meaningful weight in welfare levels. (vi) The flat-tax + basic-income reform first-order dominates the baseline SWF, but ~15% lose, and losers are concentrated in the initially best-off third (13.1% loser rate vs 0.6% in the bottom third).

## Main limitations
Working paper. Empirical application uses only three alternatives, so the welfare distribution is necessarily coarse. Cross-sectional data deliver bounds rather than point identification of joint level-difference distributions. Estimation of choice probabilities uses semiparametric logits with shape-restriction penalties, so functional-form bias is not literally absent. No demand-side opportunity modelling — all choice variation attributed to preferences. Sensitivity to the choice of reference prices for MMU is not explored. The ordered-choice issue from Bhattacharya (2015) is acknowledged but not solved.

## Quick takeaway
The most general nonparametric welfare-identification result available for discrete choice — and the one that makes Fleurbaey-style welfare levels (not just differences) operational. For any RURO welfare exercise, this is the benchmark of what is identifiable without parametric structure on preferences or heterogeneity, and the empirical illustration provides a clean template for the joint level-difference distributional analysis of a tax reform.
