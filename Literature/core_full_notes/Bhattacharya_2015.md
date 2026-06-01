---
title: "Nonparametric Welfare Analysis for Discrete Choice"
authors: [Debopam Bhattacharya]
year: 2015
outlet: "Econometrica, 83(2), 617–649"
shelf: "Welfare measurement / Equivalent income / Money-metric"
note_type: "canonical"
---

## Full citation
Bhattacharya, D. (2015). Nonparametric Welfare Analysis for Discrete Choice. *Econometrica*, 83(2), 617–649.

## One-sentence contribution
Establishes that for binary and unordered multinomial discrete choice with arbitrary unobserved preference heterogeneity, the marginal distributions of equivalent and compensating variation from a price change are point-identified as closed-form functionals of conditional choice probabilities — but the same identification fails for ordered choice at a uniform unit price.

## Core research question
Under what conditions on the structure of the discrete-choice problem can the entire distribution of money-metric welfare (EV and CV) from a discrete price change be recovered nonparametrically from observed choice probabilities, without specifying the functional form of utility, the dimension of the heterogeneity vector, or its distribution?

## Model / framework
A consumer with income $Y$ chooses among $J+1$ alternatives at known prices and receives utility $U_j(Y-p_j,\eta)$ that is continuous and strictly increasing in the numeraire (the only substantive assumption). Under a price change $p_0\to p_1$ for alternative $j$, EV takes one of three values per type $\eta$: zero (non-buyers at both prices), $t(y,\eta)-p_0$ for switchers (where $t$ is the reservation price), or $p_1-p_0$ for inframarginal buyers. Aggregating, the EV CDF is $\Pr\{S^{EV}\le a\}=1-\bar q(p_0+a,y)$ on $[0,p_1-p_0]$, and the CV CDF is the same expression with $y$ replaced by $y+a$. Section 3 shows that for ordered choice at a uniform unit price the analogous identification fails because price variation does not generate the orthogonal coverage required to trace the welfare distribution.

## Data
None. The paper is purely theoretical, with a brief computational example using multinomial logit.

## Identification logic
The trick is to slice the population by reservation price: changes in the price-income pair sweep out exactly the boundary types whose welfare equals the local price increment. Because choice probabilities $\bar q(p,y)$ identify the mass of switchers between every pair of (price, income) pairs, they identify the entire welfare CDF. The result requires variation in own price and income but not in the structure of $U$ or in the heterogeneity distribution. The negative ordered-choice result follows because uniform per-unit pricing collapses the price grid that the unordered case relies on.

## Treatment of preferences
Maximally general. Heterogeneity vector $\eta$ has unknown dimension, unknown distribution, and enters utility in an arbitrary way. The only restriction is local non-satiation in the numeraire. This is strictly weaker than the quasilinear-utility assumption (Domencich & McFadden 1975), the no-income-effects approximation (Small & Rosen 1981), or the parametric heterogeneity assumed by Herriges & Kling (1999) and Dagsvik & Karlström (2005).

## Treatment of opportunities / constraints
Not modelled. The choice set is assumed to be the same full menu for every consumer; no rationing, no demand-side restrictions, no heterogeneous feasible sets. Welfare variation arises entirely from preference heterogeneity.

## Welfare / normative object
The full marginal distributions of EV and CV — strictly more informative than the mean. Mean welfare follows as a corollary: $E(EV)=\int_{p_0}^{p_1}\bar q(p,y)\,dp$ (the change in Marshallian consumer surplus, generalised beyond quasilinear utility) and $E(CV)=\int_{p_0}^{p_1}\bar q(p,y+p-p_0)\,dp$. For normal goods $E(EV)\le E(CV)$. Distributions can be aggregated into any social welfare functional, but the paper does not aggregate.

## Main findings
(i) Theorem 1: closed-form EV and CV CDFs from binary choice probabilities. (ii) Theorem 2: extension to unordered multinomial via composite outside option. (iii) Corollary 1: average EV equals the change in Marshallian consumer surplus regardless of income effects. (iv) Section 3 (negative): for ordered choice at a uniform unit price, welfare distributions are not point-identified. (v) Appendix: distinct heterogeneity distributions can produce identical choice probabilities yet still imply identical welfare distributions — heterogeneity itself need not be identified.

## Main limitations
Static one-period framework. Assumes free choice — no rationing, no restricted choice sets. Requires substantial price and income variation in the data, which may be unavailable. The negative ordered-choice result directly bites for the most common labour-supply discretisation (van Soest hours grid at a single wage). No empirical application; the companion empirical paper is Bhattacharya (2018).

## Quick takeaway
The benchmark identification result for nonparametric welfare analysis in discrete choice. The positive result vindicates frameworks that treat alternatives as unordered (each with its own price/wage) — including RURO — as theoretically capable of nonparametric welfare identification. The negative result is the hidden cost of ordered-hours discrete-choice labour-supply models: any welfare object computed from them carries identification only via the maintained parametric form.
