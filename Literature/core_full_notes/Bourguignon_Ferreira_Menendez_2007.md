---
title: "Inequality of Opportunity in Brazil"
authors: [François Bourguignon, Francisco H. G. Ferreira, Marta Menéndez]
year: 2007
outlet: "Review of Income and Wealth, 53(4)"
shelf: "Decomposition methods / Inequality of opportunity"
note_type: "canonical"
---

## Full citation
Bourguignon, F., Ferreira, F. H. G., & Menéndez, M. (2007). Inequality of Opportunity in Brazil. *Review of Income and Wealth*, 53(4).

## One-sentence contribution
Operationalises Roemer's circumstance-vs-effort distinction on Brazilian male earnings data via a counterfactual-based decomposition that equalises observed circumstances and recomputes inequality, finding that five exogenous circumstance variables account for 10–37% of the Theil index of urban male earnings inequality across cohorts, with roughly 60% of that effect operating directly on wages rather than through observed effort proxies.

## Core research question
What share of observed male earnings inequality in urban Brazil can be attributed to exogenous circumstances (race, region of birth, parental education, father's occupation) versus "effort," and how much of the circumstance effect operates directly on wages rather than indirectly through circumstance-influenced effort variables such as schooling, migration, and labour-market status?

## Model / framework
A reduced-form earnings function $w_i=f(C_i,E(C_i,v_i),u_i)$ where $C_i$ are circumstance variables, $E_i$ are "effort" variables themselves shaped by $C_i$ (effort in quotation marks because they are not derived from optimisation), and $u_i$ is an unobserved residual. The opportunity share is defined as $\Theta_I=[I(F)-I(\Phi)]/I(F)$, with $I(\Phi)$ the inequality of the counterfactual distribution that equalises observed circumstances. A direct-effect decomposition $\Theta_I^d=[I(F)-I(F^d)]/I(F)$ separates the part of the circumstance effect that operates conditional on observed efforts. There is no utility function, no labour-supply model, and no explicit feasible-set object.

## Data
PNAD 1996 household survey from IBGE, restricted to urban males aged 26–60 with positive earnings — 28,474 observations across seven five-year birth cohorts (1936–1940 through 1966–1970). Outcome: real hourly earnings.

## Identification logic
The decomposition is not point-identified causally because the residual $u$ may be correlated with the regressors. The paper deploys a partial-identification strategy: a Monte Carlo procedure draws admissible correlations between regressors and residuals subject to positive-semi-definiteness and sign restrictions, constructs the implied unbiased coefficient estimates, and reports 90% confidence intervals across the admissible set. Results are presented as bounds rather than point estimates — a methodological strength relative to the rest of the IOp literature.

## Treatment of preferences
None. There is no utility function and no behavioural model. The "effort" variables are observed proxies, not optimisation outputs — the authors place the term in quotation marks throughout because schooling, migration, and labour-market status are themselves shaped by circumstances and luck. Preference heterogeneity is invisibly bundled into the residual.

## Treatment of opportunities / constraints
Opportunities are operationalised through observed background circumstances — the Roemerian rather than the RURO conception. There is no representation of feasible job sets, latent offers, hours restrictions, or local labour-demand variation. A worker with "good" parental circumstances facing a depressed local market is indistinguishable in the data from a worker with the same circumstances facing a thriving market.

## Welfare / normative object
None directly. The decomposed object is observed earnings inequality (Theil, with Gini robustness). Normative motivation is compensatory in spirit — earnings inequalities driven by circumstances beyond individual control are flagged as unfair — but there is no explicit welfare measure that combines bundles, preferences, feasible sets, and tax schedules.

## Main findings
(i) Five observed circumstances explain 10–37% of the Theil index of male earnings inequality across cohorts, with a simple average of about 23%. (ii) About 60% of that opportunity effect operates directly on wages conditional on observed effort, rather than through schooling/migration/labour-market-status channels. (iii) Parental education is the most important individual circumstance variable; father's occupation second; race matters more for younger cohorts. (iv) Weak evidence of a declining opportunity share for younger cohorts, but cohort effects cannot be cleanly separated from time effects. (v) Bounded inference produces coherent confidence intervals around all of these magnitudes.

## Main limitations
Opportunities are proxied by observed background variables rather than represented as feasible sets — a worker with bad local job availability is not flagged as opportunity-deprived if their parental circumstances are good. The "effort" residual contains preference heterogeneity, luck, measurement error, and unobserved circumstances, mixed indistinguishably. Outcome is current earnings of active men only — excludes participation, household composition, non-labour income, and broader well-being. Identification is bounded rather than point.

## Quick takeaway
The benchmark empirical demonstration of Roemerian opportunity decomposition on a developing-country dataset, with admirable methodological discipline (partial identification via Monte Carlo). Its central limitation — that "opportunities" are observed background characteristics rather than feasible sets — is exactly the gap that a structural RURO-based opportunity primitive can close, and the direct/indirect architecture is a useful template for richer multi-channel decompositions.
