---
title: "Welfare, Labor Supply and Heterogeneous Preferences: Evidence for Europe and the US"
authors: [Olivier Bargain, André Decoster, Mathias Dolls, Dirk Neumann, Andreas Peichl, Sebastian Siegloch]
year: 2013
outlet: "Social Choice and Welfare, 41(4), 789–817"
shelf: "Welfare measurement / Equivalent income / Money-metric"
note_type: "canonical"
---

## Full citation
Bargain, O., Decoster, A., Dolls, M., Neumann, D., Peichl, A., & Siegloch, S. (2013). Welfare, Labor Supply and Heterogeneous Preferences: Evidence for Europe and the US. *Social Choice and Welfare*, 41(4), 789–817.

## One-sentence contribution
Operationalises three Fleurbaey-style welfare metrics — "wage" (full responsibility for preferences), "rent + reference wage" (intermediate), and "rent" (full compensation for preferences) — on harmonised micro-data and tax-benefit simulators for twelve countries, and shows that the choice between compensation and liberal-reward axioms shifts cross-country welfare rankings by tens of percentile points and is driven primarily by country-specific preference parameters rather than by demographic composition.

## Core research question
How do cross-country welfare rankings of married women's households change when one moves from income-based comparisons to leisure-inclusive welfare metrics that take different normative positions on the responsibility individuals should bear for their consumption-leisure preferences?

## Model / framework
Country-specific Box-Cox discrete-choice labour-supply model in seven hours categories with extreme-value taste shocks: $u_i(c,T-h)=\beta_c(c^{\alpha_c}-1)/\alpha_c+\beta_{li}((T-h)^{\alpha_l}-1)/\alpha_l$, $\beta_{li}=\beta_{l0}+\beta_{lz}z_i$. Three welfare metrics from Fleurbaey (2006, 2008): the "wage" metric $v_i^W$ (minimum hypothetical wage at zero non-labour income that delivers utility $u$), the "rent + reference wage" metric $v_i^{RW}$ (expenditure function evaluated at a reference wage $w^r$ taken at p25/p50/p75 of the pooled wage distribution), and the "rent" metric $v_i^R$ (consumption at zero hours that delivers $u$). The latter two are limit cases of the first.

## Data
Harmonised household micro-data for 12 countries circa 2001 (EU-SILC, ECHP, GSOEP, IPUMS-CPS). Tax-benefit rules simulated by EUROMOD v.D16 for European countries and TAXSIM v.9 for the US. Sample is married women with working-age partners; husbands' hours are fixed; non-worker wages are imputed via Heckman selection.

## Identification logic
Preference parameters are identified country-by-country from observed labour-supply choices over known tax-benefit budget constraints — the standard van Soest identification. Welfare metrics are then computed deterministically from the estimated indifference curves; no further identification assumptions are required. The decomposition exercise (Section 5.3) identifies the relative roles of demographic composition and country-specific preference parameters by counterfactually swapping each across countries.

## Treatment of preferences
Preferences are the central object. Heterogeneity is allowed across two dimensions: observed taste-shifters $z_i$ (age, education, children) entering $\beta_{li}$, and country-specific deep parameters $(\alpha_c,\alpha_l,\beta_c,\beta_{l0})$. The paper does not adjudicate which metric is normatively correct; it documents that the choice has first-order empirical consequences. MRS at a common bundle ranges from 3.7 PPP-USD/h (Portugal) to 17.6 (Ireland), a near 5× spread.

## Treatment of opportunities / constraints
Opportunities enter only through the budget constraint and the wage rate. There is no explicit modelling of opportunity densities, job availability, rationing, fixed costs of work, childcare provision, or part-time availability. The paper acknowledges this as a key limitation: country-specific "preferences" partly absorb country-specific opportunity constraints.

## Welfare / normative object
Three individual-level money-metric welfare measures, all ordinal and respecting the compensation principle for individuals with identical preferences. They differ in their treatment of the liberal-reward principle. No social welfare function is applied — the paper deliberately stops at interpersonal comparisons because aggregation requires further normative choices (the Fleurbaey-style indexing dilemma).

## Main findings
(i) Income rankings differ markedly from preference-respecting welfare rankings: the US drops from a percentile rank of 63.3 (income) to 60.9 ("wage") and 62.4 ("rent"); Ireland rises from 53.1 to 58.2 ("wage"); Finland drops from 29.7 to 24.1 ("rent"). (ii) For seven of twelve countries the rent-vs-wage gap exceeds 3 percentile points. (iii) The decomposition shows that country-specific preference parameters, not demographic composition, drive the metric-dependent reranking. (iv) Cross-country MRS varies by a factor of nearly five at a common bundle, identifying which countries are flagged as "work-loving" vs "work-averse". (v) Robustness to Box-Cox vs quadratic utility, to alternative reference households, and to alternative aggregation rules within the metric is high.

## Main limitations
No demand-side opportunity modelling — involuntary unemployment, hours rationing, and fixed costs are absorbed into the preference block. Sample restricted to married women; men and singles excluded. No SWF aggregation. Static, no life-cycle. Most consequentially, country-specific "preferences" almost certainly capture cross-country differences in opportunities (childcare, part-time availability, institutions), so the central finding cannot cleanly be attributed to genuine taste differences.

## Quick takeaway
The leading empirical demonstration that the normative choice between compensation-principle and liberal-reward welfare metrics has first-order consequences for cross-country welfare rankings, and the paper any responsibility-sensitive welfare exercise will cite for the menu of money-metric formulas it makes operational. Its most important caveat — that the model conflates $R$ and $A$ — is exactly the gap a RURO-based welfare exercise can close.
