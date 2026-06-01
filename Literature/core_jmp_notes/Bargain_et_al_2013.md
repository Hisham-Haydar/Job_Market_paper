---
title: "Welfare, Labor Supply and Heterogeneous Preferences: Evidence for Europe and the US"
authors: [Olivier Bargain, André Decoster, Mathias Dolls, Dirk Neumann, Andreas Peichl, Sebastian Siegloch]
year: 2013
shelf: "Welfare measurement / Equivalent income / Money-metric"
note_type: "JMP-linked"
---

## Why this paper matters for my JMP
This is the empirical template for the welfare layer I am putting on top of my France 2016 RURO model. It defines the menu of preference-respecting money-metric welfare measures (rent, wage, rent + reference wage), shows that the choice among them has first-order consequences for rankings, and runs the harmonised microsimulation pipeline whose downstream version I am building. It is also the cleanest illustration of the central problem my JMP is designed to solve: that without an explicit opportunity primitive, "preferences" silently absorb opportunities and welfare rankings cannot tell the two apart.

## What it tells me about opportunities vs preferences
The paper makes the silent-conflation problem concrete. It explicitly acknowledges (p. 814–815) that country-specific preference parameters likely embed country-specific opportunity constraints — childcare, part-time availability, institutions — and concedes the framework cannot resolve which is which. This is exactly the gap my RURO-based France implementation closes. The paper also gives me a numeric anchor for how large the unresolved opportunity content might be: country-specific "preferences" account for ~85% of cross-country reranking, an upper bound on what a richer opportunity model could relabel as $A$.

## What it tells me about welfare measurement
Three direct lessons. (i) Use the $v^{RW}$ family rather than collapsing to either extreme — varying $w^r$ across p25/p50/p75 of the wage distribution is a clean way to display the responsibility-spectrum without taking a stand. (ii) Computing welfare metrics by expectation over taste draws is preferable to evaluating at point estimates. (iii) Robustness to Box-Cox vs quadratic utility is high in their data, which suggests the welfare layer is reasonably insensitive to the specific functional form of $v(C,h)$ — a useful prior for the parametric-form sensitivity I will need to report given the Dagsvik & Jia (2016) non-identification result.

## What it tells me about decomposition
The paper's Section 5.3 decomposition (counterfactually swapping demographics vs preference parameters across countries) is a methodological precursor to the Shapley-Shorrocks decomposition I want to do. It shows exactly the kind of additive split between two channels that Shapley generalises with order-independence. The paper's finding that demographics contribute almost nothing relative to deep parameters is the result that I will need to qualify by introducing a third (opportunity) channel.

## What it tells me about empirical design
Three lessons for the France pipeline. (i) Restrict the sample to a comparable demographic core (married women) for the headline results, then expand. (ii) Use a discrete grid of seven hours categories at minimum. (iii) Estimate country-specific preference parameters rather than imposing pooled coefficients — the cross-country MRS spread of ~5× is too large to absorb into demographic shifters. For me this translates to letting French preference parameters vary across regions and education cells rather than imposing a single parameter vector.

## How I may cite it in the paper
As the canonical empirical implementation of the Fleurbaey welfare metrics. Likely citations: in the welfare-framework section as the source of the $v^W$, $v^{RW}$, $v^R$ definitions; in the literature section as the leading demonstration that the metric choice changes welfare rankings; in the limitations section as the precursor that explicitly acknowledged the missing opportunity block; and in the discussion section as the natural cross-country comparator if I extend the France pipeline to a multi-country exercise.

## What limitation of this paper my JMP may address
The most important one. The paper computes preference-respecting welfare metrics on a model that does not separate preferences from opportunities, so the resulting cross-country reranking is necessarily contaminated. My JMP layers the same Fleurbaey welfare machinery on top of a RURO model where $R$ and $A$ are separately identified (modulo the parametric resolution from Dagsvik & Jia 2016), so the welfare-inequality decomposition can attribute shares to opportunities rather than booking them silently as preferences. The paper's own decomposition can be read as an upper bound on the opportunity share that my JMP makes visible.
