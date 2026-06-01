---
title: "Evaluating Alternative Representations of the Choice Sets in Models of Labor Supply"
authors: [Rolf Aaberge, Ugo Colombino, Tom Wennemo]
year: 2009
shelf: "RURO / Latent Jobs / Constrained Labour Supply"
note_type: "JMP-linked"
---

## Why this paper matters for my JMP
This is the empirical case for not running my JMP on a stripped-down Van Soest specification. The headline finding — that prediction errors under a flat-tax counterfactual run 30–55% in models without opportunity dummies and collapse to under 5% with the right dummies — is exactly the kind of evidence I need to defend the structural cost of my approach. It also validates the specific design choice in my France pipeline: 24 (or thereabouts) sampled wage-vigintile × hours alternatives plus opportunity features, rather than a sparse fixed grid.

## What it tells me about opportunities vs preferences
The paper provides a striking asymmetric identification result: preferences are recoverable from in-sample data under almost any choice-set design, but opportunities are not. That maps directly onto my $W(z,R,A;y)$ framework — it implies that the $A$-block in my decomposition is the empirically fragile piece and demands the strongest specification discipline. It also makes a concrete suggestion: the job-availability dummy approximates $\log p^0$ and the peaks dummies approximate $g_1(h)$, so my opportunity block can be parametrised parsimoniously rather than fully nonparametrically.

## What it tells me about welfare measurement
The paper does not compute welfare, but its negative result transfers directly. If a model mis-predicts the post-reform hours distribution by 30–55%, then any money-metric welfare object built on that model will misallocate utility across constrained vs voluntary outcomes by a similar order of magnitude. So the cost of choice-set misspecification is not a second-order econometric inconvenience for me — it is first-order for the welfare numbers my JMP reports. This is the strongest existing argument for why a welfare-and-opportunity decomposition cannot be done credibly inside a conventional Van Soest model.

## What it tells me about decomposition
Two implications. (i) The preference-vs-opportunity Shapley split I want to compute is asymmetric in identification: the opportunity share is the harder one to nail down empirically, so its sensitivity to specification is what I should stress-test. (ii) The "interaction of more alternatives with the job dummy" matters more than either alone, which suggests I should not skimp on either margin in my France implementation — sparse alternatives + opportunity dummies, or rich alternatives without dummies, both fail.

## What it tells me about empirical design
Five concrete lessons for the France 2016 pipeline. (i) Use sampled rather than fixed alternatives. (ii) Aim for ~24 alternatives per agent rather than the 6–8 typical of Van Soest applications. (iii) Include a job/participation dummy AND hours-peak dummies. (iv) Do not over-trust in-sample fit as a model-selection criterion — report out-of-sample policy-prediction stability. (v) Run a Monte-Carlo robustness exercise from my own estimated model and report how the welfare decomposition shifts under leaner specifications.

## How I may cite it in the paper
As the methodological backstop for my choice-set design. Likely citations: in the empirical-implementation section as the reference for the sampled-alternatives + dummies specification; in the robustness section as the precedent for Monte-Carlo evaluation of choice-set sensitivity; and in the limitations section as the source of the warning that opportunity-block identification is fragile and depends on the maintained parametric form.

## What limitation of this paper my JMP may address
The paper is purely about labour-supply prediction, not welfare — its central claim about opportunities mattering for policy is asserted but never quantified in welfare units. My JMP closes that gap: I take the paper's "use the dummies" prescription, build an opportunity-aware model, and translate the resulting predictions into a money-metric welfare-inequality decomposition. The Monte-Carlo design also gives me a template for the robustness exercise that the paper itself does not cross to welfare measurement.
