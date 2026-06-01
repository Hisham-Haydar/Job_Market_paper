---
title: "Theoretical and Practical Arguments for Modeling Labor Supply as a Choice Among Latent Jobs"
authors: [John K. Dagsvik, Zhiyang Jia, Tom Kornstad, Thor O. Thoresen]
year: 2014
shelf: "RURO / Latent Jobs / Constrained Labour Supply"
note_type: "JMP-linked"
---

## Why this paper matters for my JMP
This is the framing manifesto behind the modelling choice at the heart of my France 2016 prototype. It gives me the citable theoretical defence of the latent-jobs structure I use, and — crucially — the formal bridge $\gamma(h)=\log\theta+\log g(h)$ that lets me reinterpret the conventional Van Soest dummy-augmented model as a special case of my framework where opportunities have been silently absorbed into preferences. Whenever a referee asks "why latent jobs rather than dummies?", this is the paper I cite.

## What it tells me about opportunities vs preferences
The paper's central interpretive move — that hours dummies $\gamma(h)$ are demand-side opportunity terms, not preference terms — is exactly the move my decomposition relies on. Without it, the Van Soest representation would book the part-time and full-time spikes as preferences, and any opportunity share of welfare inequality would mechanically collapse to zero. The paper also reminds me that the additive convention $v(C,h)+\gamma(h)$ implies non-monotone preferences in hours, which is normatively unattractive for any responsibility-sensitive welfare measure.

## What it tells me about welfare measurement
No welfare object is implemented, but the paper makes the right warning: any welfare measure built on the misidentified utility $v(C,h)+\gamma(h)$ will misclassify constrained outcomes as voluntary choices. This is exactly the misclassification my JMP is designed to avoid. It also points to Dagsvik & Karlström (2005) for matching-CV machinery, which is a useful cross-reference if I ever want to compute exact compensating variation rather than the AEI money-metric I currently use.

## What it tells me about decomposition
For pure tax/wage counterfactuals (variation in $C$ at fixed budget mapping), the latent-jobs structure and the dummy model deliver the same predictions, so the structural choice does not buy me anything mechanical. Where it buys something is in $A$-channel counterfactuals: equalising or reshaping $g(h)$ across cells is a counterfactual the dummy model literally cannot represent because the "preference" dummies are not portable across populations. My opportunity-equalisation Shapley component therefore lives or dies on this paper's structural reinterpretation.

## What it tells me about empirical design
Three concrete lessons. (i) Specify $g(h)$ flexibly with peaks at full-time and part-time and let $\theta$ depend on education and demographics — these are the moments the data identify well. (ii) Use Box-Cox systematic utility justified by the invariance axioms; this is the parametric form the latent-jobs literature has converged on. (iii) Be explicit that the wage elasticity scales with $(1-P)$, so when I report French elasticities and benchmark them against Norwegian or US numbers, I should adjust for the participation gap rather than treat raw elasticity differences as preference differences.

## How I may cite it in the paper
As the structural-interpretation reference for the RURO/latent-jobs framework, paired with Dagsvik & Jia (2016) for identification. Likely citations: in the model section when I introduce $g(h)$ and $\theta$, in a methodological footnote when I explain why I do not use additive hours dummies, and in the discussion when I motivate the $A$-channel counterfactuals as exercises that conventional discrete-choice models cannot perform.

## What limitation of this paper my JMP may address
The paper is a survey and explicitly states it does not improve fit, does not implement welfare, and freezes $g(h)$ in the short run. My JMP closes the welfare loop: I take the structural reinterpretation as given, layer on a money-metric welfare object, and produce a quantitative Shapley decomposition where the share attributable to $g(h)$ and $\theta$ becomes a reportable number. The out-of-sample prediction exercise the authors run for the 2006 Norwegian reform is also a template for the validation exercise I should run on a French reform episode.
