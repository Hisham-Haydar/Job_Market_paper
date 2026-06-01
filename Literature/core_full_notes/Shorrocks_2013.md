---
title: "Decomposition Procedures for Distributional Analysis: A Unified Framework Based on the Shapley Value"
authors: [Anthony F. Shorrocks]
year: 2013
outlet: "Journal of Economic Inequality, 11, 99–126"
shelf: "Decomposition methods / Inequality of opportunity"
note_type: "canonical"
---

## Full citation
Shorrocks, A. F. (2013). Decomposition Procedures for Distributional Analysis: A Unified Framework Based on the Shapley Value. *Journal of Economic Inequality*, 11, 99–126.

## One-sentence contribution
Establishes that the Shapley value — assigning to each factor its average marginal contribution across all elimination orders — provides an exact, symmetric, order-independent additive decomposition rule that unifies the patchwork of poverty- and inequality-decomposition formulas in the prior literature, and extends naturally to grouped factors via the Owen value.

## Core research question
How should one decompose a distributional indicator $I=f(X_1,\ldots,X_m)$ into additive contributions from each factor in a way that is exact (contributions sum to the total), symmetric across factors, free of arbitrary residual or interaction terms, and applicable when the underlying function $f$ is nonlinear?

## Model / framework
For an indicator $I=f(X_1,\ldots,X_m)$, define the subset-value function $F(S)$ as the value of $I$ when only factors in $S$ are "active" (with $F(\varnothing)=0$ as a normalisation). The Shapley contribution of factor $k$ is the weighted average over all subsets $S\subseteq K\setminus\{k\}$ of the marginal effect $\Delta_k F(S)=F(S\cup\{k\})-F(S)$, with weights $\pi(|S|,|K\setminus\{k\}|)=(m-|S|-1)!|S|!/m!$. The decomposition satisfies (i) exact additivity, (ii) symmetry / order invariance, (iii) null-effect normalisation (a factor that never moves $f$ gets contribution zero), and (iv) linearity of the attribution operator. The hierarchical Owen extension treats grouped factors as primary players in a two-stage decomposition (between groups, then within groups), with consistency conditions identified in the paper.

## Data
None — the paper is purely methodological.

## Identification logic
Not an identification paper. The Shapley rule is an attribution rule once the analyst has defined the factor list, the counterfactuals that "remove" each factor, and the indicator $I$. Identification of the factors themselves is upstream of the decomposition.

## Treatment of preferences
None modelled. Preferences enter only if an analyst defines them as a factor in $f$ upstream.

## Treatment of opportunities / constraints
None modelled. Opportunities enter only if an analyst defines them as a factor.

## Welfare / normative object
None directly. The decomposition rule is normatively neutral about the choice of indicator: it can decompose poverty headcounts, Gini coefficients, mean log deviations, or any other aggregate distributional statistic the analyst supplies.

## Main findings
(i) The Shapley rule reproduces conventional decompositions in benchmark cases — e.g., the Datt-Ravallion growth-vs-redistribution decomposition without the residual term, and Shorrocks's own (1982) MLD subgroup decomposition. (ii) For Gini and other non-decomposable indices, the Shapley rule supplies an exact additive split where ad hoc rules previously left a residual. (iii) For source decomposition of inequality the Shapley split coincides with the natural variance-of-source decomposition for the variance, and provides a defensible analogue for other indices. (iv) The Owen extension handles grouped factors consistently under stated regularity conditions.

## Main limitations
The paper supplies a rule, not a model. Its outputs depend entirely on the analyst's choice of factor list and on the counterfactual definition that "removes" each factor — choices that are economic and normative, not mechanical. Causal interpretation requires those upstream choices to be defensible. The rule does not tell the analyst what should count as a primary vs secondary factor, nor whether a given indicator $I$ is the right normative summary statistic.

## Quick takeaway
The methodological reference for any decomposition exercise that needs an exact, symmetric, residual-free additive split into factor contributions in a nonlinear setting. The substantive economic and normative work — defining factors, defining their null counterfactuals, choosing $I$ — is upstream of the rule itself, and the credibility of any Shapley decomposition lives or dies on those upstream choices.
