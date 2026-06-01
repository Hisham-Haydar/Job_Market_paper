---
title: "Structural Labour Supply Models and Microsimulation"
authors: [Rolf Aaberge, Ugo Colombino]
year: 2018
shelf: "Welfare measurement / Equivalent income / Money-metric"
note_type: "JMP-linked"
---

## Why this paper matters for my JMP
This is the methodological survey that defines the playing field my JMP enters. It sets out the canonical RURO + microsimulation pipeline I am implementing for France 2016, and — crucially — it identifies the unresolved welfare-evaluation tension my JMP is designed to resolve: common utility (interpersonally comparable but ignores preference heterogeneity) vs Fleurbaey preference-respecting (respects heterogeneity but indexing-dilemma). Whenever I want to motivate why my $W(z,R,A;y)$ framework is needed rather than just one more application of an existing welfare metric, this is the paper I cite as the official statement of the open problem.

## What it tells me about opportunities vs preferences
The paper gives the cleanest written articulation of why the RURO is the right vehicle for an opportunity-vs-preference decomposition: the structural interpretation of the dummy coefficients ($\gamma_0=\ln J+A_0$, $\gamma_\ell=\ln(J_\ell/J)+A_\ell$) means the opportunity block is policy-invariant in a way that the DC dummies are not. It also gives me the Colombino (2013) iterative-equilibrium argument I will need when a referee asks whether my opportunity counterfactuals are partial-equilibrium artefacts — the framework supports endogenous reshaping of $p(w,h)$ in response to large reforms.

## What it tells me about welfare measurement
The key passage for me is the explicit acknowledgment that the common utility function $V(y,h)$ "by definition contains interpersonal comparability of both welfare levels and welfare differences" — meaning it achieves comparability by assumption, not by argument. That is exactly the methodological move I want to avoid. The paper's honest "no clear winner" between common utility and Fleurbaey is the gap my framework targets: I want a welfare object that is interpersonally comparable in the same way King (1983) equivalent income is, but conditions on the opportunity set so that "comparability" is not a euphemism for "ignoring $A$".

## What it tells me about decomposition
The paper does not implement decomposition exercises directly, but it surveys the rank-dependent SWF family (Weymark/Yaari) which is the natural target for any inequality decomposition I want to do. It also flags the Norwegian elasticity-decline result over 1979–2011 as a potential decomposition target — a useful analogue: that decline can be re-read as an opportunity-set expansion (the female extensive margin saturated), which is exactly the kind of $A$-channel attribution my Shapley exercise is designed to make quantitatively.

## What it tells me about empirical design
Five concrete lessons. (i) Adopt the McFadden (1978)/Ben-Akiva-Lerman (1985) importance sampling for the alternatives — it is the standard. (ii) Specify $p(w,h)=p_1 g_1(h)g_2(w)$ explicitly rather than via dummies, to keep the opportunity primitive visible for downstream welfare. (iii) Take an explicit stance on the $\varepsilon$ interpretation (RUM vs optimisation error) since it determines whether $\varepsilon$ enters welfare. (iv) For the optimal-tax extension, follow the iterative microsimulation approach of equation (16) rather than analytical Mirrlees. (v) When elasticities are reported, distinguish between extensive/intensive and historical/current to allow comparison with the Norwegian time series.

## How I may cite it in the paper
As the canonical methodological survey of the entire structural-labour-supply + microsimulation + social-welfare-evaluation pipeline. Likely citations: in the introduction as the statement of the unresolved welfare-evaluation tension; in the model section as the source of the unified DC/RURO formalism; in the welfare-framework section as the source of the common-utility-vs-Fleurbaey contrast my framework navigates; and in the optimal-tax / extension section as the methodological reference for any computational optimum-tax exercise built on top of the welfare layer.

## What limitation of this paper my JMP may address
The paper presents the common utility function and the Fleurbaey preference-respecting approach as a stark binary and concludes there is no clear winner. My JMP introduces a third option — the $W(z,R,A;y)$ framework — that conditions welfare on both preferences and opportunities, using the responsibility cut to decide which preference differences the social planner should respect and the opportunity primitive to decide which differences should be compensated. This dissolves the binary the paper leaves open and gives a constructive welfare object that is interpersonally comparable without assuming preferences are homogeneous.
