---
title: "Inequality of Opportunity in Brazil"
authors: [François Bourguignon, Francisco H. G. Ferreira, Marta Menéndez]
year: 2007
shelf: "Decomposition methods / Inequality of opportunity"
note_type: "JMP-linked"
---

## Why this paper matters for my JMP
This is the empirical-style template for the inequality-of-opportunity literature my decomposition exercise plugs into, and the cleanest example of how *not* to measure opportunities for my purposes. The paper proxies opportunities with observed background variables (race, parental education, region of birth) — exactly the reduced-form approach my structural RURO framework supersedes by modelling opportunities as actual feasible job sets. So this paper is at once the literature my decomposition speaks to and the limitation my framework addresses.

## What it tells me about opportunities vs preferences
The paper makes the conceptual cut between circumstances (compensable) and effort (not compensable) but does not separate effort from preferences — the residual mixes them indistinguishably. This is the silent-conflation problem on the inequality-of-opportunity side, mirroring the same problem in Bargain et al. (2013) on the welfare-measurement side. My JMP fills both gaps simultaneously: structural preferences from RURO, structural opportunities from the opportunity density, and the residual much smaller because both are explicitly modelled.

## What it tells me about welfare measurement
None directly — the paper decomposes earnings inequality, not welfare inequality. But the methodological lesson transfers: any welfare object I decompose should also be decomposed by an *equalisation* counterfactual rather than a regression-coefficient interpretation. The Bourguignon-Ferreira-Menéndez "compute inequality on the equalised-circumstance counterfactual distribution" approach is exactly what the Shapley rule generalises when extended to multiple factors.

## What it tells me about decomposition
Three lessons. (i) The direct/indirect-effect decomposition (60% of circumstance effect operates directly on wages, 40% through effort proxies) is a useful conceptual template — my structural decomposition should distinguish opportunity effects that operate *through* labour-supply choices (extensive margin) from those that operate directly on the wage given the choice (intensive margin). (ii) Reporting bounds rather than point estimates via Monte Carlo over admissible coefficient configurations is a defensible identification strategy when instruments are absent — useful for my parametric-form sensitivity analysis. (iii) The 23% headline number for circumstance share is a benchmark to compare against my opportunity-share number for France; if mine is much higher, that is itself informative about how much the structural opportunity primitive captures that circumstance proxies miss.

## What it tells me about empirical design
Two practical lessons. (i) Be explicit about which observed variables are circumstances and which are responsibility variables — the line is normative and the paper is admirably transparent that schooling-as-effort is contestable. (ii) Run the decomposition cohort by cohort (or in my case, region/education cell by cell) to expose heterogeneity in the opportunity share rather than collapse to a single national number — the cohort-by-cohort tabulation is one of the paper's most informative outputs.

## How I may cite it in the paper
As the canonical empirical reference for circumstance-based inequality-of-opportunity decomposition. Likely citations: in the literature section as the leading reduced-form approach to opportunity inequality; in the methodological section as the precedent for the equalised-counterfactual decomposition strategy; in the discussion as the comparator number for the share of inequality attributable to opportunities; and in the limitations section as the precursor whose conflation of effort with preferences my framework dissolves.

## What limitation of this paper my JMP may address
The most important one. The paper proxies opportunities with observable background characteristics and bundles preferences indistinguishably into the residual. My JMP replaces the proxy with a structural opportunity primitive (RURO $g(h,w)$ and $\theta$) and the residual with structural preferences from the same model. The result is a decomposition that attributes inequality not just to "circumstances vs effort" but to the four economically meaningful primitives — preferences, opportunities, wages, and non-labour income — within a unified Shapley-Shorrocks framework. This is a substantive advance: where the paper can attribute 23% to "circumstances", my JMP can attribute that share more finely and defensibly across the channels economic theory actually identifies.
