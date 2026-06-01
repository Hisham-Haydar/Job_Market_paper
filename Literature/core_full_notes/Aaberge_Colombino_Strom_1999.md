---
title: "Labour Supply in Italy: An Empirical Analysis of Joint Household Decisions, with Taxes and Quantity Constraints"
authors: [Rolf Aaberge, Ugo Colombino, Steinar Strøm]
year: 1999
outlet: "Journal of Applied Econometrics, 14(4), 403–422"
shelf: "RURO / Latent Jobs / Constrained Labour Supply"
note_type: "canonical"
---

## Full citation
Aaberge, R., Colombino, U., & Strøm, S. (1999). Labour Supply in Italy: An Empirical Analysis of Joint Household Decisions, with Taxes and Quantity Constraints. *Journal of Applied Econometrics*, 14(4), 403–422.

## One-sentence contribution
The first application of the Dagsvik (1994) job-choice framework to Italian data, jointly modelling spouses' labour supply over a fully non-convex tax-benefit budget set with explicit quantity constraints, and showing that the conventional Hausman approach overstates female unconditional hours elasticities by roughly sixty percent because it ignores opportunity rationing.

## Core research question
What are the labour supply elasticities and the distributional and behavioural effects of tax reforms in Italy when the model jointly accounts for (i) couples' joint decisions, (ii) the exact non-convex Italian budget set, and (iii) quantity constraints captured by an opportunity scale parameter $g_0$ that allows for involuntary non-participation?

## Model / framework
RURO model with multiplicative utility $U_i(C,h,j)=v_i(C,h)\,\varepsilon_{ij}$ and i.i.d. extreme-value job-level shocks. Each agent has a market opportunity set with conditional density $g_i(h,w)$ and a non-market option, with the relative scale $g_{0i}$ measuring market vs non-market availability. The choice probability is $\varphi_i(h,w)\propto\Psi_i(h,w)\,g_{0i}\,g_i(h,w)$ for $h>0$ where $\Psi_i(h,w)=v_i(f(wh,I),h)$. Systematic utility uses Box-Cox-style leisure terms with demographic shifters and a consumption term where the marginal utility of consumption is allowed to differ by employment status (capturing underground-economy income). Hours density is uniform with an estimated full-time peak $\theta_k=\exp(\alpha)$.

## Data
Bank of Italy Survey of Household Income and Wealth, 1987. 2,953 married couples, both spouses 20–68, excluding heavily self-employed. Italian 1987 tax-benefit system with eight progressive brackets (12%–62%) modelled exactly.

## Identification logic
Two pieces. First, $g_0$ is identified non-parametrically from the unemployment rate via $\rho=(1-g_0)\varphi(0,0)$: the gap between observed non-participation and what the model would predict in a "fair environment" with $g_0=1$ pins down the opportunity scarcity. Second, conditional on separability $v(C,h)=v_1(C)v_2(h)$, the marginal utility of income $v_1$ is identified from variation in the tax function with respect to fixed costs of work, after which the wage opportunity density $g_1(w\mid h)$ is identified from the residual variation. Cross-region variation in $g_0$ (North vs South) and in unemployment rates pins down its determinants.

## Treatment of preferences
Box-Cox in leisure for each spouse with quadratic-in-log-age and child-presence shifters; consumption enters via an exponential term whose level is allowed to differ by joint employment status, intentionally capturing the role of unreported income in Italy. Estimated utility is strictly concave in consumption and leisure for both genders.

## Treatment of opportunities / constraints
Opportunities are first-class. The hours opportunity density $g_2(h)$ is uniform with a full-time peak estimated at $\theta_F\approx 11$, $\theta_M\approx 12$ — full-time jobs are about an order of magnitude more prevalent than part-time slots. The opportunity scale $\log g_{0F}$ depends on a Northern-region indicator and the local female unemployment-to-employment ratio, and similarly for males. Estimates deliver $g_0<1$ for both genders, formal evidence of rationing, with significantly more female opportunities in the North.

## Welfare / normative object
None directly. Distributional impact of counterfactual tax regimes is summarised through the Gini coefficient on disposable income, but no money-metric or compensating-variation welfare object is computed.

## Main findings
(i) Aggregate uncomp. hours elasticities: 0.05 male, 0.74 female, the latter driven mainly by participation (0.65). (ii) Female elasticity falls from 3.44 in the poorest decile to 0.04 in the richest; the male elasticity turns negative (–0.04) at the top. (iii) The Hausman approach overstates the female unconditional hours elasticity by ~60% (1.18 vs 0.74) because it ignores opportunity rationing. (iv) A revenue-neutral flat tax at 26.3% raises the disposable-income Gini from 0.238 to 0.247 with negligible behavioural response; greater progression lowers it to 0.220 with a small drop in female participation. (v) Strong cross-spouse wage effects largely neutralise the partial-equilibrium own-wage responses.

## Main limitations
Static, single cross-section; no dynamic or life-cycle extensive margin. Wage opportunities and hours opportunities are assumed independent. The household objective is a unitary utility — no intra-household bargaining. The "underground economy" channel is captured only through a status-dependent consumption coefficient. No formal welfare measurement and no responsibility cut on $g_0$.

## Quick takeaway
The benchmark application showing that the RURO framework can be operationalised in a high-unemployment Southern European setting with strong opportunity heterogeneity, and that ignoring opportunity scarcity meaningfully biases the labour-supply elasticities that drive tax-reform evaluations. The structural identification of $g_0$ from the unemployment rate is a citable template for any RURO model that wants to put rationing on a quantitative footing.
