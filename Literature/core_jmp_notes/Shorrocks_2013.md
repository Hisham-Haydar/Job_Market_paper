---
title: "Decomposition Procedures for Distributional Analysis: A Unified Framework Based on the Shapley Value"
authors: [Anthony F. Shorrocks]
year: 2013
shelf: "Decomposition methods / Inequality of opportunity"
note_type: "JMP-linked"
---

## Why this paper matters for my JMP
This is the methodological backbone of the welfare-inequality decomposition that gives my JMP its quantitative headline. My core deliverable is a Shapley-Shorrocks decomposition of welfare inequality into preference, opportunity, wage, and non-labour-income components — and Shorrocks (2013) is the rule I am applying. It is also the methodological reference any referee will check to verify that my decomposition is exact, symmetric, and residual-free rather than ad hoc.

## What it tells me about opportunities vs preferences
Nothing directly — the paper is normatively neutral. But it gives me the formal apparatus to make the opportunity-vs-preference split *quantitative* once I have defined the underlying factors in my structural model. The hard substantive work (what does "removing opportunity heterogeneity" mean in a RURO model?) is upstream of the Shapley rule itself, and the paper is explicit about this division of labour. My JMP needs to be careful to defend the upstream factor definitions on economic grounds and let Shorrocks (2013) do the attribution mechanics.

## What it tells me about welfare measurement
Indirectly important. Once I have computed welfare levels under the $W(z,R,A;y)$ framework, the Shapley rule lets me decompose any inequality measure of those welfare levels — Gini, MLD, Atkinson, variance — into factor contributions. Importantly, the rule gives the same factor split for the variance regardless of which inequality index is chosen as the target, which means I can run a robustness check across several indices and present a unified narrative.

## What it tells me about decomposition
Three direct lessons. (i) Use the Shapley rule rather than any sequential or ad hoc procedure — the order-invariance is non-negotiable for credibility. (ii) Use the Owen hierarchical extension to group factors: my four primary factors (preferences, opportunities, wages, non-labour income) can each be decomposed further in a second stage if needed. (iii) Document all $2^m$ subset evaluations explicitly so the decomposition is fully reproducible — for $m=4$ this is 16 subset evaluations per household, which is computationally trivial.

## What it tells me about empirical design
Two practical lessons. (i) Define the null counterfactual for each factor with care — the Shapley contribution literally depends on what "$X_k$ removed" means. For my opportunity counterfactual, "remove opportunity heterogeneity" should mean equalising $g(h)$ and $\theta$ across cells in some interpretable way (e.g., to the population-mean opportunity distribution), not setting them to zero. (ii) Pre-register the factor list and the null counterfactuals in the appendix so the decomposition is not ex-post tuned — this is the strongest defence against the "results-depend-on-counterfactual" critique the paper itself flags.

## How I may cite it in the paper
As the methodological reference for the Shapley-Shorrocks rule. Likely citations: in the methods section to introduce the decomposition formula; in the implementation appendix to motivate the choice of the Shapley rule over ad hoc sequential decompositions; in the robustness section to justify reporting multiple inequality indices under the same factor split; and possibly in the limitations section to acknowledge that the decomposition is conditional on the analyst-defined null counterfactuals.

## What limitation of this paper my JMP may address
The paper itself is a tool, not a model — it does not define preferences, opportunities, or pay schedules as factors. My JMP supplies exactly that upstream definition: it takes the RURO structural model as the source of $R$ and $A$, the wage distribution as the source of pay heterogeneity, and the EUROMOD tax-benefit calculator as the source of $y$, and feeds those four factors into the Shapley rule. So my contribution complements Shorrocks's by populating the framework with economically-disciplined factors rather than leaving the choice to the analyst.
