---
title: "Labour Supply in Italy: An Empirical Analysis of Joint Household Decisions, with Taxes and Quantity Constraints"
authors: [Rolf Aaberge, Ugo Colombino, Steinar Strøm]
year: 1999
shelf: "RURO / Latent Jobs / Constrained Labour Supply"
note_type: "JMP-linked"
---

## Why this paper matters for my JMP
This is the canonical demonstration that the RURO/latent-jobs machinery survives translation to a high-unemployment European labour market — exactly the setting my France 2016 prototype lives in. It is the closest historical analogue to my exercise: couples, non-convex tax-benefit budget set, identification of an opportunity scale parameter, regional heterogeneity in opportunities, and a tax-reform simulation grounded in the estimated structural model. The methodological choices the authors had to make in 1999 are essentially the choices I am making for France in 2026.

## What it tells me about opportunities vs preferences
The paper operationalises my $W(z,R,A;y)$ split in a clean way: $v(C,h)$ is the preferences block, $g_0$ and $g(h,w)$ are the opportunity block, and the structural unemployment equation $\rho=(1-g_0)\varphi(0,0)$ gives a quantitative measure of how much of observed non-participation is opportunity-driven rather than preference-driven. This is exactly the kind of decomposition I want for France, with regional/educational variation in $g_0$ playing the role that the North/South cut plays here.

## What it tells me about welfare measurement
The paper does not compute a welfare object — it stops at the disposable-income Gini for the policy comparison. That is the gap my JMP fills. But the comparison of three revenue-neutral tax regimes is a useful template: report distributional outcomes under several explicit counterfactuals and let the welfare measure aggregate them. The authors' finding that the flat tax raises the Gini while leaving aggregate labour supply nearly unchanged previews the Bargain et al. (2013) money-metric exercise I will lean on more heavily.

## What it tells me about decomposition
The North/South $g_0$ gap is a worked example of a circumstance-driven opportunity wedge — and it is large enough (significant Northern coefficient, $t=6.5$ for women) to drive a material slice of any opportunity-vs-preference decomposition. For my France pipeline, this validates building the opportunity Shapley component on geographic + education cells rather than relying solely on demographic shifters inside $v$. The cross-spouse elasticity finding (own-wage effects are largely neutralised by cross-effects) also warns me that any decomposition done at the individual rather than household level will mis-attribute income variation.

## What it tells me about empirical design
Five concrete lessons. (i) Estimate $g_0$ jointly with preferences and discipline it with the unemployment rate — do not normalise it away. (ii) Allow the marginal utility of consumption to differ by employment status when the country has a meaningful informal sector (relevant for some EU robustness checks). (iii) Use a uniform hours density with peaks rather than a fully flexible $g(h)$ — identification is fragile. (iv) Estimate spouses jointly; cross-effects are first-order and a unitary household objective is a defensible default. (v) Run the Hausman comparison as a robustness exercise — the 60% gap in female hours elasticity is a citable benchmark for the size of the bias my framework corrects.

## How I may cite it in the paper
As the empirical workhorse of the RURO literature alongside Aaberge & Colombino (2018) and Aaberge, Colombino & Wennemo (2009). Likely citations: in the model section as the canonical couples extension of Dagsvik (1994); in the empirical-design section as the precedent for identifying an opportunity scale parameter from unemployment data; in the decomposition section as the precedent for region-conditioned opportunity heterogeneity; and in the elasticity-discussion section as the reference for the Hausman-vs-RURO bias.

## What limitation of this paper my JMP may address
Three. (i) No welfare measurement — my JMP layers a money-metric welfare object on the same structural primitives. (ii) The opportunity decomposition is ad hoc (North/South + local unemployment ratio) rather than a formal Shapley-Shorrocks split — my JMP delivers an order-independent decomposition of welfare inequality. (iii) The paper does not engage with the responsibility cut between $R$ and $A$, treating the gender gap in elasticities as a pure modelling output rather than a normative object — my JMP makes that responsibility cut explicit and reports the welfare-inequality consequence of choosing it differently.
