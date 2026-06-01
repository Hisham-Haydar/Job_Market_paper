---
title: "Labour Supply and Taxation with Restricted Choices"
authors: [Magali Beffy, Richard Blundell, Antoine Bozio, Guy Laroque, Maxime Tô]
year: 2019
outlet: "Journal of Econometrics, 211(1), 16–46"
shelf: "RURO / Latent Jobs / Constrained Labour Supply"
note_type: "canonical"
---

## Full citation
Beffy, M., Blundell, R., Bozio, A., Laroque, G., & Tô, M. (2019). Labour Supply and Taxation with Restricted Choices. *Journal of Econometrics*, 211(1), 16–46.

## One-sentence contribution
A "two-offer" structural labour-supply model in which each woman chooses among exactly two randomly drawn hours offers and the offer distribution is identified separately from preferences using non-linearities in the budget constraint, with the empirical finding that ignoring offer restrictions roughly doubles estimated Frisch and Marshallian elasticities for UK mothers.

## Core research question
Can preferences and the distribution of hours offers be separately identified when individuals face restricted choice sets, and what does that separation imply for estimated elasticities, predicted employment, and the response of women's labour supply to a major welfare-reform episode?

## Model / framework
Life-cycle CRRA utility $u(c,h)=c^{1-\gamma}/(1-\gamma)+a(L-h)^{1-\phi}/(1-\phi)$ with fixed costs of work $b$. Each agent receives two i.i.d. hours offers from a discrete distribution $g=(g_1,\ldots,g_I)$ and picks the offer (or non-participation) with the highest indirect utility. Choice probabilities take the closed form $\ell_i=g_i^2+2g_i\sum_{j\neq i}g_j p_i(\{i,j\})$. The dominated set $H^W$ — hours ranges where the budget function $S(w,h)=\sup_{x\le h}R(w,x)$ is flat — provides a nonparametric rejection device: any choices observed there must reflect offer restrictions, not preferences. The $n$-offer generalisation converges to the unrestricted discrete-choice model as $n\to\infty$.

## Data
UK Family Expenditure Survey 1997–2002, 10,575 women with children (single or married mothers). Tax-benefit rules simulated through IFS-Taxben — Working Families' Tax Credit, Income Support, Family Credit, rent and local-tax rebates produce highly non-convex budget sets. Median hourly wage £5.85; median usual hours 26/week; ~37% non-employment.

## Identification logic
Three sequential results. (i) Lemma 1: with $g$ known, preference utilities are uniquely identified from observed choice shares via a system whose Jacobian is dominant-diagonal (Gale-Nikaido). (ii) Lemma 2: with preferences known, $g$ is uniquely recovered from the same system with roles reversed. (iii) Joint identification under three conditions — a parametric dimension count, semi-parametric exclusion restrictions from cross-sectional budget-constraint heterogeneity (e.g. spouse income shifts $R$ but not $g$), and nonparametric identification of $g$ from observed choices in dominated regions of the budget set.

## Treatment of preferences
CRRA in consumption and leisure with observed shifters (cohabiting, age of youngest child, birth cohort) and unobserved normal taste shock. The framework deliberately purges preferences of demand-side contamination: estimated $\phi$ rises sharply once offer restrictions are introduced, indicating that part of what conventional models read as a strong taste for leisure is actually offer rationing.

## Treatment of opportunities / constraints
The offer distribution $g(h\mid Z^o)$ is the explicit opportunity primitive — a mixture of two truncated normals with means at ~15 and ~38 hours, mixture weight $p_1$ allowed to depend on education, location, and year. More-educated women receive proportionally more full-time offers. The constrained-vs-unconstrained gap is large: predicted employment 62.5% vs 71%, average hours 26.2 vs 35.5. Women rejecting the unrestricted-choice model are disproportionately lone, young, low-wage, and high-fertility.

## Welfare / normative object
None directly. The framework is purely positive but the building blocks for a welfare exercise are present: the gap between constrained realised utility and the unconstrained optimum is an individual-level money-metric cost of the offer restriction.

## Main findings
(i) 2.6% of working women observed at strictly dominated hours; 7.9% fail the parametric revealed-preference inequality. (ii) Mixture means of the offer distribution at $m_1\approx 15$ and $m_2\approx 38$ hours. (iii) Adding offer restrictions halves estimated elasticities — Frisch falls from ~0.58 to ~0.30, Marshallian from ~0.58 to ~0.20. (iv) Removing all hours restrictions in simulation raises mean hours by ~9 and employment by ~9 percentage points. (v) Women who fail the unrestricted model are economically poorer households on average.

## Main limitations
The "two" in "two-offer" is unmotivated by data — the $n$-offer generalisation is sketched but not estimated. The offer distribution is over hours only, not over (hours, wage) pairs, so wage rationing is invisible. Offers are independent of preferences (no sorting). Sample is restricted to women with children; men and childless women are excluded. Static framework applied across a period of major welfare reform. No welfare object is constructed.

## Quick takeaway
The cleanest formal identification result for separating preferences from opportunities in a discrete-choice labour-supply model, with budget-set non-linearities playing the role of an exclusion restriction. The empirical headline — accounting for offer restrictions roughly halves elasticities — is the strongest single piece of evidence that conflating $R$ and $A$ has first-order quantitative consequences for the policy elasticities that drive tax-reform welfare numbers.
