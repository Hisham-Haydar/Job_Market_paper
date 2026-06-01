---
title: "Decomposition procedures for distributional analysis: a unified framework based on the Shapley value"
authors: [Anthony F. Shorrocks]
year: 2013
outlet: "Journal of Economic Inequality, 11, 99--126"
country_or_context: "General methodological framework"
population: "Not applicable"
data_period: "Not applicable"
shelf: "decomposition methods / Shapley value / inequality / poverty / methodology"
tags: [Shapley-decomposition, inequality-decomposition, poverty-decomposition, multivariate-decomposition, hierarchical-decomposition, Owen-value, distributional-analysis, methodology, Shorrocks]
priority: "medium"
read_status: "extracted"
---

# Full citation

Shorrocks, A. F. (2013). Decomposition procedures for distributional analysis: a unified framework based on the Shapley value. *Journal of Economic Inequality*, 11, 99--126.

# One-sentence contribution

Provides a unified decomposition rule for poverty and inequality analysis by assigning to each factor its average marginal contribution across all possible elimination orders, yielding an exact additive decomposition formally equivalent to the Shapley value.

# Why this paper matters

This is the foundational paper for the Shapley-Owen-Shorrocks decomposition that Audoly et al. (2025) later popularise for structural models. For my JMP, it provides the theoretical grounding for decomposing welfare or inequality statistics into contributions of interacting factors (preferences, opportunities, pay schedules) in nonlinear settings.

# Core research question

How should one decompose an aggregate distributional indicator (poverty, inequality) into factor contributions in a way that is symmetric, exact, interpretable, and applicable to complex multivariate settings?

# Model / theoretical framework

**General decomposition:** $I = f(X_1, \ldots, X_m)$. Define $F(S)$ = value of indicator with only factors in $S$, $F(\emptyset) = 0$. The Shapley rule assigns:
$$C_k^S = \sum_{S \subseteq K \setminus \{k\}} \pi(|S|, |K \setminus \{k\}|) \cdot \Delta_k F(S)$$
where $\Delta_k F(S) = F(S \cup \{k\}) - F(S)$ and $\pi$ weights by $\frac{(m-|S|-1)! \cdot |S|!}{m!}$.

**Properties:** (i) Exact decomposition (contributions sum to total); (ii) Symmetry (order-invariant); (iii) Null-effect normalisation ($C_k = 0$ if factor $k$ never changes $f$); (iv) Linearity of the attribution operator.

**Hierarchical extension (Owen):** Groups of factors treated as players; two-stage decomposition (between groups, then within groups).

# Key objects

- Aggregate indicator $I$, contributory factors $X_k$, subset-value function $F(S)$.
- Shapley contributions $C_k^S$: expected marginal effect over all elimination paths.
- Hierarchical model $\langle K, A, F \rangle$: secondary factors grouped into primary factors.

# Applications covered

- Growth vs redistribution decomposition of poverty change (eliminates residual term).
- Subgroup decomposition of inequality (replicates standard results for MLD; improves for Gini).
- Inequality by income source (variance: reproduces covariance decomposition; other indices: depends on levels vs differences formulation).
- Hierarchical/multivariate decompositions with conditions for Owen-Shapley consistency.

# Treatment of preferences / opportunities / welfare

None modelled. The paper is a decomposition tool, not a behavioural or normative model. Preferences, opportunities, and welfare enter only if an analyst defines them as factors in an aggregate statistic upstream.

# Main findings

1. Shapley value provides a unified, exact, symmetric decomposition rule for distributional analysis.
2. Replicates conventional practice in benchmark cases (decomposable indices, variance by source).
3. Improves on existing methods by eliminating residual/interaction terms in nonlinear settings.
4. Owen extension handles grouped factors consistently under specified conditions.

# Main limitations

- Decomposition tool, not a model of labour supply, welfare, or opportunity sets.
- Results depend entirely on the analyst's factorisation and counterfactual definitions.
- Not causal identification; attributes within accounting identities or modelling choices.
- Does not tell the analyst how to define preferences, opportunities, or pay schedules as "factors."

# Relevance for my JMP

## possible use for welfare decomposition
The paper's primary use. If my framework produces an aggregate welfare or inequality statistic built from $W(z, R, A; y)$, the Shapley decomposition provides a principled way to attribute it across heterogeneity in $R$, $A$, $y$, and their interactions.

## possible use for grouped decomposition
The Owen extension for hierarchical factors is directly relevant for grouping model components (e.g., all demand-side parameters as "opportunities") and decomposing across groups.

# Research questions this paper inspires

1. Can inequality in equivalent incomes be decomposed into contributions of preference heterogeneity ($R$), opportunity-set heterogeneity ($A$), and pay-schedule variation ($y$) using the Shapley rule?

2. What is the most defensible counterfactual for "removing" opportunity heterogeneity in a RURO model?

# Challenge to this paper

The Shapley rule is formally elegant but substantively agnostic. The hard question is not the mechanics of order-invariant attribution but the economic meaning of "removing" a factor. For the RURO framework, what does it mean to set the opportunity density $g(h,w)$ to its "null" value? The decomposition is only as convincing as the upstream model.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] General decomposition for $I = f(X_1, \ldots, X_m)$; no mention of $W(z,R,A;y)$ or labour supply.

[Reasonable inference for my project] Directly useful once the framework produces an aggregate statistic to decompose across $R$, $A$, $y$.

[Unclear from paper] How to define $R$, $A$, $y$ as removable factors; how to choose null values; how to interpret contributions ethically.

# Relation to Bargain et al. (2013)

Not directly related. Could be applied to decompose cross-country differences in equivalent income inequality.

# Relation to opportunities vs preferences

Not substantively about this distinction. A tool for quantifying their relative contribution once a model has distinguished them.

# Useful quotations / formulas

**Shapley decomposition (eqs. 2.8--2.9):**
$$C_k^S = \sum_{S \subseteq K \setminus \{k\}} \frac{(m-|S|-1)! \cdot |S|!}{m!} [F(S \cup \{k\}) - F(S)]$$

# Suggested tags

Shapley-decomposition, inequality-decomposition, poverty-decomposition, multivariate-decomposition, hierarchical-decomposition, Owen-value, distributional-analysis, methodology, Shorrocks

# My quick takeaway

The foundational paper for Shapley-based decomposition of distributional statistics. For my JMP, it provides the theoretical grounding for decomposing welfare/inequality across interacting factors (preferences, opportunities, pay schedules) once the structural model has been built. The method is exact and symmetric but substantively agnostic -- the hard work is defining the factors and their counterfactual removal, which is the analyst's responsibility upstream.
