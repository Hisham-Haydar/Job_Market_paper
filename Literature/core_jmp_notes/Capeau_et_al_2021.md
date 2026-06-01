---
title: "Nonparametric Welfare Analysis for Discrete Choice: Levels and Differences of Individual and Social Welfare"
authors: [Bart Capéau, Liebrecht De Sadeleer, Sebastiaan Maes, André Decoster]
year: 2021
shelf: "Welfare measurement / Equivalent income / Money-metric"
note_type: "JMP-linked"
---

## Why this paper matters for my JMP
This is the paper that makes Fleurbaey welfare *levels* — not just differences — operational from choice probabilities. My JMP needs welfare levels to do an inequality decomposition (rank individuals on a money-metric scale and decompose the inequality of those levels), and Capéau et al. give the cleanest existing identification machinery for that object. It is also the natural generalisation of Bhattacharya (2015) and the natural complement to Bargain et al. (2013): it tells me which parts of my parametric welfare layer are identification-essential and which are just functional-form convenience.

## What it tells me about opportunities vs preferences
The paper deliberately attributes all choice variation to preferences and bypasses opportunities entirely — its NOS sets are normative virtual objects, not actual constraints. This is exactly the gap my JMP fills. But the empirical finding that lower wage quartiles are intermingled in welfare-level dominance ranks (i.e., unobserved preferences move welfare levels meaningfully) sets an important upper bound on how far an opportunity-side decomposition can push: if preferences genuinely carry this much within-wage-group welfare-level dispersion, the opportunity share will not be the whole story.

## What it tells me about welfare measurement
Three direct lessons. (i) Use the joint distribution of welfare levels and CV — the "who gains where on the baseline distribution" object is exactly the policy-evaluation table I want for any French reform counterfactual, and Theorem 4 gives the closed form. (ii) The MMU-equals-income result for ~25% of the sample is a useful deterministic check — anyone whose actual reference prices match the chosen reference prices has a known welfare level, which is a sanity test for my pipeline. (iii) Use NOS measures more general than MMU; the Pazner ray and equivalent-income variants are also identified and may be normatively preferable for the responsibility-sensitive cut my JMP cares about.

## What it tells me about decomposition
The SWF representation (Proposition 2) gives me a formal route to decompose differences in social welfare across counterfactuals into integrals of differences in choice probabilities. This is the analytic counterpart of the Shapley decomposition I want to do at the inequality level: I can write any SWF change as a sum of "choice-probability differences at virtual prices" and partition those by the source of the policy change. The paper itself does not Shapley-decompose, but it provides the additive structure that makes a Shapley exercise on top of it well-defined.

## What it tells me about empirical design
Five lessons. (i) Estimate choice probabilities semiparametrically with shape restrictions (own-price decreasing, cross-price increasing) — this is robust without being arbitrary. (ii) When only cross-sectional data are available, use Boole-Fréchet bounds for transition probabilities and report intervals rather than point estimates for joint-distribution objects. (iii) Take reference prices for MMU at sample medians of price differentials — defensible and replicable. (iv) Report welfare levels by wage-quartile and by chosen alternative, as in Figure 5–6 — a clear way to display the heterogeneity. (v) Run the deterministic-welfare check (Corollary 2): the share of the sample with $MMU=y$ is a hard accuracy benchmark for the estimated choice probabilities.

## How I may cite it in the paper
As the welfare-identification reference for NOS measures and as the methodological route from choice probabilities to welfare distributions. Likely citations: in the welfare-framework section as the source of the NOS welfare-level definition; in the methods section for the closed-form CDF representations of welfare levels and CV; in the empirical section as the precedent for the joint level-difference reform analysis; and in the limitations section as the precursor that flagged but did not address opportunity heterogeneity in the choice set.

## What limitation of this paper my JMP may address
The most important one is the assumption of a common, exogenous choice set — the paper attributes all choice variation to preferences and treats $\{NW,PT,FT\}$ as freely available to all single females. My JMP layers the same NOS welfare machinery on a RURO model where the opportunity set varies across individuals via $\theta$ and $g(h)$, so the welfare levels I identify reflect the realised opportunity constraint rather than a counterfactual unrestricted choice. This means the welfare-inequality decomposition I produce can attribute shares to opportunities, while Capéau et al.'s framework would book the same variation as preferences. The cross-sectional-only setting (bounds rather than point identification of joint distributions) is an additional limitation my single-cross-section France pipeline shares — I should adopt their Boole-Fréchet bounding strategy directly.
