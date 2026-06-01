---
title: "Structural Labour Supply Models and Microsimulation"
authors: [Rolf Aaberge, Ugo Colombino]
year: 2018
outlet: "International Journal of Microsimulation, 11(1), 162–197"
shelf: "Welfare measurement / Equivalent income / Money-metric"
note_type: "canonical"
---

## Full citation
Aaberge, R., & Colombino, U. (2018). Structural Labour Supply Models and Microsimulation. *International Journal of Microsimulation*, 11(1), 162–197.

## One-sentence contribution
The authoritative survey of structural labour-supply models — the conventional Discrete Choice (Van Soest) model and the Random Utility Random Opportunities (RURO) model — and their integration with tax-benefit microsimulation, with explicit treatment of the interpersonal-comparability problem in welfare evaluation, the choice between a common welfare function and Fleurbaey-style preference-respecting metrics, and the computational optimal-taxation problem.

## Core research question
How should structural labour-supply models be specified, estimated, and embedded in microsimulation pipelines for both positive policy evaluation and normative social-welfare analysis, and what trade-offs face the analyst choosing between a common welfare function (which assumes interpersonal comparability) and preference-respecting welfare metrics (which preserve heterogeneity but face the indexing dilemma)?

## Model / framework
Surveys two model classes side by side. (i) Discrete Choice with optional dummy refinements: $P(h)\propto\exp\{v(f(wh,I),h)\}\,\exp\{\gamma(h)\}$. (ii) RURO: $\varphi(w,h)\propto\exp\{v(f(wh,I),h)\}\,p(w,h)$ with $p(w,h)=p_1 g_1(h)g_2(w)$ for $h>0$. Establishes that DC is the special case of RURO when wages are fixed and the opportunity density is uniform, and gives the structural reinterpretation of DC dummies as opportunity terms ($\gamma_0=\ln J+A_0$, $\gamma_\ell=\ln(J_\ell/J)+A_\ell$). Welfare layer covers (a) a common utility function $V(y,h)$ used as the social planner's index, (b) the King (1983) equivalent income, and (c) the Fleurbaey preference-respecting class. The optimal-tax problem $\max_\vartheta W(U_1,\ldots,U_N)$ subject to incentive-compatibility and revenue constraints is solved by iterative microsimulation rather than analytically.

## Data
None new — the survey draws on Italian SHIW (1987, 1993), Norwegian administrative tax data (1979–2011), Swedish HINK (1981), and the cumulative empirical literature.

## Identification logic
Discusses identification at survey level. Preferences identified from tax-function non-linearities; opportunity-density parameters identified from the joint hours-wage distribution and participation rates; structural vs reduced-form interpretation of dummy coefficients drives the policy-invariance properties needed for ex-ante simulation. Argues forcefully that no observational design can identify policy-invariant parameters without a structural model (Marschak/Lucas).

## Treatment of preferences
Surveys two interpretations of the random component $\varepsilon$: as unobserved job attributes inside utility (the RUM/RURO interpretation) or as optimisation error outside utility (the conventional DC interpretation). The interpretation matters for welfare evaluation because the first includes $\varepsilon$ in welfare and the second excludes it. Heterogeneity flexibility runs from observed taste-shifters through Mixed Logit random parameters.

## Treatment of opportunities / constraints
Central. The paper argues that the RURO's structural representation of opportunities $p(w,h)$ is the key advantage for ex-ante policy simulation, because the DC dummies are reduced-form and may not be policy-invariant — a tax reform changes the labour demand and hence the opportunity density. The Colombino (2013) iterative equilibrium procedure exploiting the structural interpretation of the dummies is the recommended fix when the analyst wants to simulate not just labour supply but the joint equilibrium with reshaped opportunities.

## Welfare / normative object
Three approaches surveyed. (i) Common utility function $V(y,h)$ — same functional form as individual utility but homogeneous parameters; achieves interpersonal comparability by assumption. (ii) King (1983) equivalent income at reference characteristics and reference budget. (iii) Fleurbaey-Maniquet preference-respecting metrics — flagged as "promising" but acknowledged to be sensitive to the chosen reference, citing the Decoster & Haan (2015) work-loving-vs-work-averse critique. Both primal Atkinson SWFs and dual rank-dependent (Weymark/Yaari) SWFs are surveyed as aggregators.

## Main findings
(i) DC is a special case of RURO; RURO's "dummies" have a structural opportunity interpretation that DC's do not. (ii) Choice-set specification has dramatic out-of-sample consequences (citing Aaberge, Colombino & Wennemo 2009). (iii) Norwegian total labour-supply elasticity declined from positive to near zero between 1979 and 2011, mostly because the female extensive margin saturated. (iv) Computational optimal taxes generated by RURO + microsimulation deliver monotonically rising MTRs and a negative bottom MTR (in-work credit), in contrast to the U-shape predicted by analytical Mirrlees/Saez under restrictive assumptions. (v) The common-utility vs preference-respecting tension in welfare evaluation is not resolved by the paper — both have honest weaknesses.

## Main limitations
A survey, not a new empirical contribution. Dynamic and collective/bargaining models are mentioned but not developed. General-equilibrium and labour-demand effects are flagged but not synthesised in detail. The fundamental tension between the common-utility approach and preference-respecting welfare measures is acknowledged but not adjudicated.

## Quick takeaway
The reference survey for the entire RURO + microsimulation + social-welfare-evaluation pipeline. Its most important interpretive move is to position the common-utility function and the Fleurbaey preference-respecting metrics as competing rather than complementary approaches with no clear winner — exactly the unresolved tension that a $W(z,R,A;y)$ framework conditioning welfare on both preferences and opportunities is designed to resolve.
