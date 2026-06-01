---
title: "Nonparametric Welfare Analysis for Discrete Choice"
authors: [Debopam Bhattacharya]
year: 2015
shelf: "Welfare measurement / Equivalent income / Money-metric"
note_type: "JMP-linked"
---

## Why this paper matters for my JMP
This is the theoretical benchmark against which my parametric welfare layer needs to be honest. Bhattacharya proves that money-metric welfare is nonparametrically identified in unordered discrete choice but NOT in ordered discrete choice — exactly the dividing line between the RURO framework I use (jobs are unordered alternatives, each with its own (h,w) package) and the conventional ordered-hours Van Soest framework. So this paper gives me a clean theoretical reason to prefer my modelling choice on welfare-identification grounds, independent of the labour-supply prediction reasons in Aaberge, Colombino & Wennemo (2009).

## What it tells me about opportunities vs preferences
The paper itself does not engage with the $R$-vs-$A$ split — all welfare variation in its setup arises from preference heterogeneity. But the asymmetry it documents (unordered identifies, ordered does not) is the welfare-side analogue of the asymmetry Beffy et al. (2019) document on the labour-supply side. Both point to the same lesson: the empirical content of $A$ is exposed only when the choice set is allowed to be non-trivial. For my decomposition, that means the parametric resolution of the Dagsvik & Jia (2016) non-identification ($\delta(h)$) is the binding constraint on welfare identification, not the lack of nonparametric tools.

## What it tells me about welfare measurement
Three things. (i) Use the FULL distribution of EV/CV, not just the mean — the closed-form CDF makes this almost free. (ii) The mean-EV-equals-Marshallian-consumer-surplus result generalises beyond quasilinear utility, so I can compute aggregate welfare effects of tax counterfactuals from choice probabilities directly without needing to integrate utility differences. (iii) For my France pipeline I should report welfare CDFs (e.g., quantiles of EV by education or region), not just means — this exploits the paper's strongest result and gives the welfare-inequality decomposition more empirical content.

## What it tells me about decomposition
Indirectly important. The paper shows that the full welfare distribution is identified, which means quantile-based decompositions and inequality functionals (Gini of EV, Atkinson of EV) are well-defined objects. So my Shapley decomposition can in principle be done not just on aggregate welfare but on welfare inequality at every quantile of the distribution. That is a richer decomposition target than the income-quantile decompositions that Bourguignon-Ferreira-Menéndez and Ferreira-Gignoux deploy in the inequality-of-opportunity literature.

## What it tells me about empirical design
Two lessons. (i) When estimating choice probabilities for the welfare layer, use a flexible enough specification (e.g., mixed logit at the household level) so the welfare CDF inherits the flexibility, even if the underlying RURO has parametric structure for identification. (ii) Treat the wage variation across (h,w) job packages as the "price variation" Bhattacharya needs — this is what places my model in the unordered-multinomial case and lets me cite his identification result.

## How I may cite it in the paper
As the theoretical benchmark for welfare identification in discrete choice. Likely citations: in the welfare-framework section to motivate why a money-metric approach is well-defined for my model class; in the methods section as the source of the closed-form CDF representation if I report welfare distributions; and in the discussion section as the result that distinguishes the RURO welfare layer from a Van-Soest-with-ordered-hours welfare layer at the level of identification.

## What limitation of this paper my JMP may address
The most important one for me is that Bhattacharya assumes free choice — no demand-side restrictions, no opportunity heterogeneity. My JMP layers welfare measurement on top of a model that treats opportunities as a primitive, so the welfare object I compute is welfare-given-the-opportunity-set, which is the empirically relevant quantity in a constrained labour market. The paper sketches this gap explicitly but does not fill it; a RURO-based welfare analysis is the natural way to extend Bhattacharya's nonparametric machinery to environments where the choice set itself varies across individuals.
