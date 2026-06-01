---
title: "EUROMOD: The European Union Tax-Benefit Microsimulation Model"
authors: [Holly Sutherland, Francesco Figari]
year: 2013
outlet: "EUROMOD Working Paper No. EM8/13, ISER, University of Essex"
country_or_context: "EU-27 countries"
population: "All EU-27 populations (representative micro-data)"
data_period: "2005--2010 policy years (EU-SILC input data 2006--2008)"
shelf: "microsimulation / EUROMOD / tax-benefit systems / infrastructure / methodology"
tags: [EUROMOD, microsimulation, tax-benefit, EU-SILC, budget-constraint, disposable-income, policy-simulation, redistribution, work-incentives, labour-supply, effective-marginal-tax-rate, participation-tax-rate, cross-country, infrastructure]
priority: "low"
read_status: "extracted"
---

# Full citation

Sutherland, H., & Figari, F. (2013). EUROMOD: The European Union Tax-Benefit Microsimulation Model. EUROMOD Working Paper No. EM8/13, Institute for Social and Economic Research (ISER), University of Essex.

# One-sentence contribution

Provides a comprehensive overview of EUROMOD, the EU-wide static tax-benefit microsimulation model covering all 27 EU member states, describing its architecture, input data (EU-SILC), validation process, programming language, and recent applications in redistributive analysis, policy swapping, labour supply modelling, and crisis evaluation.

# Why this paper matters

EUROMOD is the computational infrastructure underlying most of the empirical papers in my literature (Bargain et al. 2013, Immervoll et al. 2007, Bargain & Orsini 2006, Capéau & Decoster 2016, etc.). This paper explains how budget constraints are computed, how tax-benefit rules are coded, how data are prepared, and what validation is performed. Understanding EUROMOD is essential for understanding the quality and limitations of the budget constraint calculations that feed into structural labour supply models and equivalent income computations.

# Core research question

What is the current state of EUROMOD, how does it work, and what are its recent applications and future directions?

# Economic setting and context

EUROMOD is a static microsimulation model: it computes household disposable income by applying tax-benefit rules to individual micro-data (primarily EU-SILC), without modelling behavioural responses. It covers income taxes (national and local), social insurance contributions, family benefits, housing benefits, social assistance, and other income-related benefits for all 27 EU member states. Instruments not simulated (due to data limitations) include contributory pensions, disability benefits, and most in-kind transfers.

# Model / theoretical framework

**Static arithmetic microsimulation:** Takes individual/household characteristics and market incomes as given, applies tax-benefit rules, computes disposable income. No behavioural response modelled within EUROMOD itself -- but EUROMOD outputs feed into structural labour supply models.

**Key capabilities:**
- Computes disposable income for each individual/household under current or counterfactual policy rules
- Calculates work incentive indicators: Effective Marginal Tax Rates (EMTRs), Replacement Rates, Participation Tax Rates
- Supports "policy swapping" (applying one country's tax-benefit system to another country's population)
- Can run on hypothetical family types (budget constraint charts)
- Produces micro-level output compatible with any statistical software

**Architecture:** C++ compiled code reads tax-benefit rules from a flexible modular system (Excel-based interface, with standalone .NET interface in development). No national rules are hard-wired in the code; all policy parameters are stored externally. The model uses standardised variable names across countries for comparability.

# Key objects

- **Policy spine:** The ordered sequence of tax-benefit functions applied to each individual, determining the order of simulation.
- **Income lists:** Aggregations of monetary variables used as input to tax-benefit algorithms.
- **Assessment units:** The group of people on which tax-benefit rules are applied (individual, family, household).
- **Uprating factors:** CPI, average earnings growth, or other indices used to bring income data from the survey reference year to the policy simulation year.
- **Non-take-up correction:** Random assignment of non-receipt to a fraction of entitled households, calibrated to administrative caseload statistics.
- **Tax evasion correction:** Splitting reported income into a declared and an evaded component (for countries like Bulgaria, Greece, Italy).

# Data

EU-SILC (European Union Statistics on Income and Living Conditions) from Eurostat. In some countries, national SILC versions or alternative surveys are used (e.g., FRS for UK). Data contain household demographics, labour market status, gross/net market income, and other income sources. Survey weights correct for non-response and sampling. When gross incomes are unavailable, a net-to-gross procedure is applied. Income reference period is typically the year before the survey year.

# Identification logic

Not applicable (microsimulation tool, not an estimation framework).

# Estimation / empirical strategy

Not applicable. EUROMOD is a simulation tool, not an estimation tool. It is validated by comparing aggregate outputs (total tax revenue, benefit expenditure, number of recipients, poverty rates, inequality measures) against administrative statistics and national microsimulation models.

# Treatment of preferences

EUROMOD does not model preferences. It is a static calculator that assumes fixed behaviour. When combined with structural labour supply models (as in Bargain et al. 2012c), preferences enter through the labour supply model, not through EUROMOD. EUROMOD provides the budget constraints that feed into utility maximisation.

# Treatment of opportunities / constraints

EUROMOD does not model labour market constraints or job availability. It computes what disposable income would be at each potential hours level (given the tax-benefit rules and the individual's wage), producing the budget constraint. Demand-side constraints (involuntary unemployment, hours restrictions) are not captured -- they must be modelled separately (e.g., in RURO models like Capéau & Decoster 2016).

# Welfare / normative object

No welfare criterion embedded in EUROMOD. It produces disposable income and work incentive indicators. Welfare analysis (inequality indices, equivalent income, social welfare functions) is performed downstream by researchers using EUROMOD outputs.

# Main findings

1. **Coverage:** EUROMOD covers all 27 EU member states with comparable methodology. Over 250 policy-data-country combinations have been validated.

2. **Applications in redistribution:** EUROMOD has been the primary tool for studying the redistributive effects of European tax-benefit systems (Immervoll et al. 2006, Paulus et al. 2010, Decoster et al. 2010).

3. **Policy swapping:** EUROMOD enables applying one country's tax-benefit system to another's population, distinguishing effects of policy structure from population characteristics (Levy et al. 2007, 2009; Figari et al. 2011b).

4. **Labour supply modelling:** EUROMOD increasingly provides budget constraints for structural discrete-choice labour supply models. Bargain et al. (2012c) used it for the first large-scale international comparison of labour supply elasticities across 17 European countries.

5. **Crisis evaluation:** EUROMOD was used to assess the cushioning effects of tax-benefit systems during the 2008 financial crisis (Figari et al. 2011c, Dolls et al. 2012a, 2012b).

6. **Work incentive indicators:** EUROMOD computes EMTRs and Participation Tax Rates that feed into optimal tax analyses (Immervoll et al. 2007, 2011).

7. **Limitations:** Static (no behavioural response), limited coverage of contributory benefits and pensions, baseline assumes full compliance and take-up (with optional corrections), cross-sectional data limits dynamic analysis.

# Main limitations

- Static: no behavioural responses to policy changes.
- Cannot simulate contributory benefits (pensions, some unemployment benefits) due to lack of contribution history data.
- Non-take-up and tax evasion corrections are crude (random assignment based on aggregate rates).
- Data quality varies across countries (net vs gross income, imputation of benefit components from harmonised aggregates).
- Cross-sectional: no dynamic modelling of life-cycle effects.
- Uprating from data year to policy year assumes unchanged individual characteristics.

# Relevance for my JMP

## possible use as computational infrastructure
If my JMP uses European data (e.g., Belgian EU-SILC as in Capéau & Decoster 2016), EUROMOD provides the budget constraint computation. Understanding EUROMOD's assumptions (full compliance, static, no demand-side constraints) is essential for interpreting the budget constraints in my structural labour supply and welfare analysis.

## possible use for understanding the data pipeline
The paper clarifies how gross incomes, net-to-gross procedures, uprating, and non-take-up corrections are handled in the empirical papers I cite. Any limitations in EUROMOD's budget constraint computation propagate into the structural models and welfare analysis that use its outputs.

# Research questions this paper inspires

1. How sensitive are equivalent income computations to the EUROMOD assumptions (full take-up, no tax evasion, static uprating)? If non-take-up is substantial (as in Belgium, France, Greece), the actual budget constraint differs from the EUROMOD-simulated one, affecting both preference estimation and welfare measurement.

# Challenge to this paper

EUROMOD is a static tool that assumes agents face the full legal budget constraint. In the RURO framework, agents face a restricted opportunity set -- they cannot freely choose any point on the budget constraint because not all (hours, wage) combinations are available. EUROMOD computes what disposable income *would be* at each hours level, but this is only relevant if the agent can actually access a job at those hours. The gap between the EUROMOD budget constraint and the RURO opportunity set is precisely the demand-side constraint that my JMP addresses.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] EUROMOD provides the pay schedule $y(h, w)$ -- the mapping from gross (hours, wage) combinations to disposable income after taxes and benefits -- which is an input to my framework's well-being function $W(z, R, A; y)$.

[Reasonable inference for my project] The quality of my welfare analysis depends on the accuracy of the EUROMOD budget constraint. Errors in the budget constraint (from non-take-up, tax evasion, data imputation) affect both preference estimation (through incorrect choice sets) and equivalent income computation (through incorrect reference budgets).

[Unclear from paper] Whether EUROMOD's budget constraint computation can be adapted to account for the RURO opportunity density -- e.g., by weighting each (hours, wage) point by the probability of it being available to the agent.

# Relation to Bargain et al. (2013)

Direct infrastructure dependency. Bargain et al. (2013) use EUROMOD to compute budget constraints for their structural labour supply model in multiple European countries. The paper notes that "Bargain et al. (2012c) provide the first large-scale international comparison of labor supply elasticities for 17 European countries" using EUROMOD. The quality and comparability of Bargain et al.'s results depend on EUROMOD's accuracy.

# Relation to opportunities vs preferences

EUROMOD is agnostic about both preferences and opportunities. It computes the budget constraint (the $y$ in my framework) but does not model preferences ($R$) or opportunities ($A$). The implicit assumption is that agents can access any point on the budget constraint, which is equivalent to assuming a perfectly elastic demand side. The RURO framework's contribution is precisely to relax this assumption by introducing the opportunity density $g(h, w)$ that restricts the feasible set.

# Useful quotations / formulas

**On EUROMOD as static (p. 4):**
"EUROMOD is a static model in the sense that the arithmetic simulation of taxes and benefits abstract from potential behavioural reactions of individuals and the socio-demographic characteristics of the population are assumed to be fixed over time."

**On labour supply applications (p. 15):**
"The static calculations produced by EUROMOD are increasingly used to derive the budget sets used in the structural discrete choice labour supply models which are a well-established and recognised modelling set up to predict the individual behavioural adjustments to policy changes."

**On open access (p. 5):**
"EUROMOD is unusual in that it is openly accessible. It is intended for academic and non-commercial policy-relevant analysis and it is in principle available for use by any researcher subject to permission to access the micro-data."

# Suggested tags

EUROMOD, microsimulation, tax-benefit, EU-SILC, budget-constraint, disposable-income, policy-simulation, redistribution, work-incentives, labour-supply, EMTR, participation-tax-rate, cross-country, infrastructure, Sutherland, Figari

# My quick takeaway

A reference paper on the EUROMOD infrastructure that underlies most empirical analyses in my literature. Key for understanding the budget constraint computation pipeline: EU-SILC data → gross income imputation → tax-benefit simulation → disposable income at each hours level → input to structural labour supply models. The main limitation for my JMP: EUROMOD assumes agents can access any point on the budget constraint, while the RURO model restricts the feasible set to jobs available through the opportunity density $g(h, w)$.
