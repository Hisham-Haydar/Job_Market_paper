---
title: "Labor Supply as a Choice Among Latent Jobs: Unobserved Heterogeneity and Identification"
authors: [John K. Dagsvik, Zhiyang Jia]
year: 2016
shelf: "RURO / Latent Jobs / Constrained Labour Supply"
note_type: "JMP-linked"
---

## Why this paper matters for my JMP
This is the cleanest existing identification analysis of the latent-jobs model that sits at the centre of my France 2016 prototype. My JMP separates preferences from opportunities and then uses both to decompose welfare inequality; this paper tells me precisely what that separation can and cannot deliver from cross-sectional data, and which functional-form choices buy back identification when nonparametric identification fails. It is the paper a referee will most likely cite when asking whether my opportunity-vs-preference decomposition is anything more than an artefact of my parametric assumptions.

## What it tells me about opportunities vs preferences
The product $v(C,h)\cdot g_1(h)$ is identified, the individual factors are not. The unidentified piece $\delta(h)$ is precisely a function of hours that could be reallocated freely between the preference block and the opportunity block. Practically: any narrative that the preference share of inequality is "X%" rather than "Y%" only holds inside the maintained parametric family. This is a constraint I should state explicitly rather than hide. The paper also shows empirically that Model 2 (individual-specific wages) dominates Model 1 (job-specific wages) on Norwegian couples, which is directly informative for how I should specify wage heterogeneity in the France pipeline.

## What it tells me about welfare measurement
The paper does no welfare analysis but the identification result has a sharp welfare implication. Whenever the welfare object compares utility levels across individuals choosing different hours — which is exactly what an AEI-style money-metric measure does — the unidentified $\delta(h)$ enters. So my welfare layer is parametric in the same sense the preference block is parametric. This sets up a natural sensitivity check: report the decomposition under at least two parameterisations of $v(C,h)$ and show how much the opportunity share moves.

## What it tells me about decomposition
For tax/wage counterfactuals (variation in $C$ holding $h$ fixed), the non-identification of $\delta(h)$ is harmless. For my opportunity-equalisation counterfactual it bites: equalising $g_1(h)$ across region $\times$ education cells is precisely a counterfactual that changes which hours $h$ are chosen, and the welfare evaluation of the new choices uses the identified-only-up-to-$\delta(h)$ utility. So the Shapley share I attribute to opportunities is conditional on the parametric decomposition of $v(C,h)\cdot g_1(h)$ chosen at estimation.

## What it tells me about empirical design
Three concrete design lessons. (i) Use Box-Cox preferences and the regularity condition (Assumption 5) to anchor identification. (ii) Specify wage heterogeneity at the individual level rather than at the job level — Model 2 dominated empirically and is also more transparent for the welfare layer. (iii) The three-stage estimator (participation probability → Heckman wage equations → ML) is a sensible template, and division-bias measurement error in hours is something I should expect to live with rather than fully resolve.

## How I may cite it in the paper
As the identification reference for the RURO/latent-jobs model. Likely citations: in the model section when I introduce the multiplicative utility-opportunity structure, in the identification section to flag what is and is not nonparametrically identified, and in a robustness/limitations paragraph to justify why I report the decomposition under at least two parametric specifications.

## What limitation of this paper my JMP may address
The paper stops short of any welfare analysis and explicitly acknowledges that the welfare implications of its identification result are unexplored. My JMP closes that loop: I take the parametric resolution they propose (Box-Cox + regularity), inherit their non-identification caveat, and then show how the maintained specification translates into a money-metric welfare object and a Shapley decomposition of welfare inequality. The decomposition exercise also makes the cost of the non-identification visible and quantifiable — sensitivity of the opportunity share to the parametric form of $v(C,h)$ becomes a falsifiable, reportable number rather than a footnote.
