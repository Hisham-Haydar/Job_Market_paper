---

title: "EUROMOD: The European Union tax-benefit microsimulation model"
authors: ["Holly Sutherland", "Francesco Figari"]
year: 2013
outlet: "EUROMOD Working Paper No. EM8/13"
country_or_context: "European Union (EU-27 in the version described)"
population: "Individuals and households in representative national micro-data for EU member states"
data_period: "Policy systems up to 2010 in the public version described; input data mainly based on EU-SILC from roughly 2006–2008, depending on country and release"
shelf: "euromod_microsimulation_infrastructure"
tags: ["EUROMOD", "microsimulation", "tax-benefit systems", "Europe", "static model", "policy simulation", "redistribution", "work incentives", "input data", "validation"]
priority: "very high"
read_status: "extracted"
------------------------

# Full citation

Sutherland, Holly, and Francesco Figari. 2013. *EUROMOD: The European Union tax-benefit microsimulation model*. EUROMOD Working Paper No. EM8/13. 

# One-sentence contribution

The paper provides a systematic overview of EUROMOD as a harmonized, static, cross-country tax-benefit microsimulation infrastructure for the EU, explaining its policy scope, data, validation, programming architecture, and major applications in redistribution, work incentives, labour supply, and crisis analysis. 

# Why this paper matters

This paper matters because EUROMOD is one of the main empirical infrastructures behind a large share of European tax-benefit, labour-supply, and policy-distribution research. For your research program, it is not a theory paper about well-being, opportunities, or structural job choice, but it is a key supporting empirical tool. 

It is especially important because it states very clearly what EUROMOD is and is not. It is a static arithmetic simulator of tax liabilities and benefit entitlements, based on representative micro-data and detailed policy rules. Behavioural responses, dynamic life-cycle processes, and explicit opportunity sets are outside the core model, though EUROMOD outputs can be used as inputs to labour-supply and other behavioural models. 

# Core research question

The paper does not address a single substantive policy question. Its core aim is to explain the current state of the art of EUROMOD: why it was built, how it is organised, what it simulates, what data it uses, how it is validated, and what kinds of research it enables. 

# Economic setting and context

The setting is the European Union as a comparative policy space. EUROMOD is designed to simulate taxes and cash benefits for all member states within one common framework, making country-by-country analyses comparable and allowing EU-wide analysis, policy swapping, and common-shock simulations. Pages 4–7 are especially important for this rationale. 

The model is also positioned as research infrastructure rather than a single project-specific model. The paper stresses its relevance both for national analysis and for EU-level analysis, including cross-country comparisons, the study of common reforms, and the assessment of EU-level fiscal ideas. It also emphasizes its open accessibility for academic and non-commercial research. 

# Model / theoretical framework

The model class is a static tax-benefit microsimulation model. EUROMOD simulates individual and household tax liabilities and cash-benefit entitlements under the legal rules in force in each member state, using nationally representative micro-data. It is “static” in the explicit sense that arithmetic simulations abstract from behavioural responses and keep socio-demographic characteristics fixed. 

What agents “choose” is not modeled inside EUROMOD itself. EUROMOD takes individual and household circumstances in the input data and applies policy rules to them. It therefore produces after-tax, after-transfer income and related indicators, but it does not estimate a behavioural model of labor supply, job search, or household decision-making. 

The framework is positive and policy-analytic, not normative in the axiomatic sense. It can be used to study redistribution, work incentives, and the immediate effects of reforms, but it does not define a welfare criterion or a social ordering function. The paper explicitly notes that EUROMOD can inform more sophisticated behavioural or macro models, rather than replacing them. 

If one asks about feasible sets, the answer is clear: EUROMOD does not model feasible job sets or opportunity sets explicitly. It can compute disposable income for hypothetical families across different work situations and can generate budget constraints, but it does not itself represent a set-valued labor-market opportunity object. 

# Key objects

The key object is the tax-benefit simulation engine itself: a harmonized multi-country framework that applies policy rules to micro-data and stores the results at micro level for later statistical analysis. This is the core infrastructure object described throughout Sections 1–4. 

A second key object is household disposable income as simulated under alternative policy rules. EUROMOD aims to simulate as much as possible of taxes and cash benefits affecting disposable income, including income taxes, social contributions, family benefits, housing benefits, social assistance, and other income-related benefits. Some contributory benefits and pensions are instead taken from the data because the information needed for simulation is unavailable. Pages 7–9 are central here. 

A third key object is the set of work-incentive indicators produced by the model, especially effective marginal tax rates, replacement rates, and participation tax rates. These are not labour-supply parameters, but they are direct policy-to-budget-set objects and are often used as the first step toward behavioural analysis. 

A fourth key object is the input database architecture. EUROMOD largely relies on EU-SILC, supplemented in some countries by national SILC versions or other national surveys, with standardized variable definitions and naming conventions that facilitate cross-country work. Pages 9–11 describe this architecture. 

# Data

Most EUROMOD input data are derived from EU-SILC, though some countries use national SILC versions directly or combine them with other national sources when they contain richer variables. The paper notes that the current public version described, F6.0, covers EU-27 policy systems up to 2010 and uses several alternative micro-datasets mainly starting from 2006 up to 2008. 

The input database contains individual-level information on household demography, labour-market characteristics, market income, pensions, public transfers, and other private incomes, along with survey weights. If gross values are missing or unsatisfactory, net-to-gross procedures are used. These practical data issues are discussed on pages 9–10. 

The paper is also explicit about EU-SILC limitations: weak coverage of financial income, difficulties in matching asset-based means tests, annual aggregation of income, and the need to reconstruct certain benefit components from harmonized categories. This is important for any user who might otherwise overinterpret the model’s precision. 

# Identification logic

There is no causal identification strategy in the econometric sense, because EUROMOD is not estimating behavioural parameters. Its logic is institutional and arithmetic: combine detailed legal rules with representative micro-data to infer taxes, transfers, disposable income, and related indicators. 

The closest analogue to identification is validation. Baseline systems are validated at both micro and macro level. Simulated benefit expenditures, recipient counts, tax revenues, payer counts, and the resulting income distribution are compared with external administrative statistics, national models, and input-data distributions. Country reports document these exercises. Pages 10–12 are central on this point. 

A second important logical layer concerns assumptions about compliance and take-up. By default, EUROMOD baseline simulations do not comprehensively model benefit non-take-up or tax evasion, so legal rules are effectively assumed to be respected. The paper explicitly states this and also explains the limited corrections included for some countries. This is essential for interpreting simulation outputs correctly. 

# Estimation / empirical strategy

There is no estimation strategy in the usual structural or reduced-form sense. EUROMOD is a simulation platform. The “empirical strategy” of the paper is descriptive and infrastructural: explain the construction of the model, its data, its validation, and the research uses to which it has been put. 

Operationally, the model reads tax-benefit rules through a dedicated tax-benefit programming language, applies them to standardized micro-data, and produces output data at the micro level. It is implemented in C++, while the user interface in the public version described is built in Microsoft Excel. Pages 12–13 explain this architecture. 

The paper also emphasizes that EUROMOD can be run on hypothetical families rather than only observed samples. This is an important empirical feature because it allows users to derive budget constraints and compare how national systems treat stylized household types under different work situations. 

# Treatment of preferences

Preferences are not estimated or modeled explicitly within EUROMOD. The model does not infer utility parameters, choice probabilities, or heterogeneous tastes. This should be stated very clearly. 

However, the paper explicitly notes that EUROMOD has been used as the basis for labour-supply models, and it cites work using EUROMOD-generated budget sets to estimate labour-supply responses. So preferences are outside the core model but can be brought in through external models layered on top of EUROMOD outputs. 

For your project, this means EUROMOD is best seen as a policy-income calculator or budget-set generator, not as a preference-recovery model. It can support a model of (R), but it does not itself provide one. [reasonable inference for my project] supported by 

# Treatment of opportunities / constraints

This paper is not about opportunities in the feasible-set sense. EUROMOD does not model job availability, occupational menus, hours offers, rationing, or latent opportunity distributions. It simulates tax-benefit consequences conditional on observed or hypothetical household characteristics. 

The closest it comes to opportunity structure is through budget constraints for hypothetical families and work-incentive indicators. In other words, it maps policy rules into net-income schedules across work situations. This is highly useful, but it is not the same as modeling actual feasible opportunity sets (A). 

The paper therefore helps with one piece of your broader framework: the disposable-income consequences of policy under alternative earnings or hours assumptions. It does not help directly with distinguishing preference heterogeneity from opportunity heterogeneity, nor with modeling jobs as constrained sets. [reasonable inference for my project] supported by 

# Welfare / normative object

EUROMOD is not itself a welfare model. It does not define individual well-being, equivalent income, fairness criteria, or social welfare functions. The paper is explicit that EUROMOD is a static model of taxes, transfers, incomes, and incentives. 

Its normative relevance is indirect. Because it simulates how policy rules translate gross market situations into disposable incomes, it is a major empirical tool for later welfare, poverty, redistribution, and reform analysis. But the evaluative metric must come from elsewhere. 

The paper is therefore best classified as positive policy infrastructure with broad applicability to normative questions, not as a normative contribution in itself. 

# Main findings

The paper’s main “findings” are infrastructural rather than causal. First, EUROMOD is presented as a unique pan-European microsimulation model covering all EU countries in a common framework, with flexibility sufficient for consistent cross-country comparison, transferability of policy components, and multiple-user access. Pages 4–6 emphasize this as the core achievement. 

Second, the paper shows that EUROMOD has become a large and mature research infrastructure with extensive policy scope, detailed validation, standardized data architecture, and many country-policy-data combinations. At the time of writing, the public release described covers EU-27 systems up to 2010 and offers more than 250 validated policy-data-country combinations. Pages 8–11 summarize this scope. 

Third, the paper documents a wide application range: redistribution analysis, policy swapping, tax-design work, work-incentive analysis, labour-supply modeling, crisis analysis, EU-level fiscal policy, and web-based public simulation tools. Section 5 is essentially a map of the research fields enabled by EUROMOD. 

Fourth, the paper is clear on both strengths and limitations. EUROMOD is strong on static ex ante distributional and budget analysis; weaker on behavioural responses, non-cash incomes, life-cycle policies such as contributory pensions, and real-world deviations from legal rules such as non-take-up and tax evasion. Pages 16–19 are especially useful here. 

# Main limitations

A first limitation is staticity. EUROMOD abstracts from behavioural responses and keeps population characteristics fixed. This is central and explicit. As a result, it is not itself a labor-supply, search, or dynamic policy model. 

A second limitation is data quality. EU-SILC and related surveys may be weak on financial income, assets, monthly timing, and the detailed information needed for some means tests or for full simulation of contributory benefits and pensions. 

A third limitation is incomplete modeling of non-take-up and evasion. Baseline simulations generally assume legal rules are respected, although simple corrections are applied in selected countries. This can generate overestimation of some taxes and benefits relative to observed outcomes. 

A fourth limitation, relative to your project, is conceptual: EUROMOD does not model feasible job sets, wages as job offers, latent opportunities, or heterogeneous preferences. So it is an excellent supporting infrastructure for (y)- and net-income calculations, but not a full model of (R) or (A). [reasonable inference for my project] supported by 

# Relevance for my JMP

## possible use for framing

This paper is very useful for framing the empirical-support layer of your JMP. It makes clear that a serious jobs-and-wellbeing or labor-supply project often needs a separate tax-benefit engine underneath the behavioral or normative model.

## possible use for model design

It is highly useful for model design whenever disposable income, budget constraints, or reform counterfactuals must be computed consistently. It is especially useful if your eventual empirical work remains European and policy-sensitive.

## possible use for identification

Directly, limited. EUROMOD does not identify behavioural parameters. Indirectly, strong: it helps isolate the policy mapping from gross to net incomes, which can then be treated as known in later identification work.

## possible use for welfare measurement

Directly limited, since EUROMOD is not itself a welfare measure. Indirectly very useful because any welfare or distributional measure that depends on disposable income under actual or hypothetical policy rules can use EUROMOD as the income engine.

## possible use for decomposition

Moderately useful. It does not decompose inequality into preferences, opportunities, and pay schedules, but it does allow one to isolate the contribution of taxes and transfers relative to market incomes in a standardized way.

## possible use for comparative application

This is one of its strongest uses. EUROMOD is explicitly built for cross-country comparative work and for policy swapping, common-reform, and EU-level analyses.

# Research questions this paper inspires

How can a jobs-and-wellbeing framework (W(z,R,A;y)) incorporate EUROMOD as the net-income mapping while keeping (R) and (A) modeled separately?

Can EUROMOD-generated budget constraints be combined with RURO-style or latent-job models so that policy-sensitive disposable income enters an explicit opportunity-set framework?

How much of measured cross-country welfare inequality changes once one replaces income-only EUROMOD outputs with opportunity-sensitive well-being measures built on top of them?

Can one use EUROMOD to decompose policy effects into direct arithmetic effects and behavioural/opportunity-set effects when the latter are modeled externally?

What is the right way to integrate benefit non-take-up, tax evasion, and constrained job opportunities jointly in an extended European microsimulation framework?

# Challenge to this paper

The strongest challenge is that the paper presents a very powerful policy-simulation engine, but precisely because it is an engine, it leaves many substantive questions open. EUROMOD can tell us how legal tax-benefit rules map observed circumstances into disposable income, but not how those circumstances were generated, whether they were chosen, or what they mean for well-being or justice. For your project, this means EUROMOD is indispensable infrastructure but not a substitute for a model of preferences, opportunities, or welfare. 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] EUROMOD is a static microsimulation model that maps observed or hypothetical household characteristics and gross incomes into taxes, benefits, disposable incomes, and work-incentive indicators under detailed policy rules. It can also generate budget constraints for hypothetical families and is often used as the base for labour-supply models. 

[reasonable inference for my project] In your notation, EUROMOD is most naturally related to the pay-schedule / tax-benefit mapping side of the framework, that is, the transformation from pretax earnings and household circumstances into disposable resources. It can therefore be a powerful empirical component for the (y)-side and for the realized income component of (z). 

[unclear from paper] The paper does not define a well-being measure (W(z,R,A;y)), does not model preferences (R), does not model feasible job sets (A), and does not discuss axioms such as independence of (A), IIJ, IPIJ, responsibility for opportunities, or reference opportunity sets. These questions are outside its scope. 

[reasonable inference for my project] EUROMOD is not close to independence of (y); rather, it is precisely a detailed model of how policy shapes net income. It is also not a model of (A), except in the weak sense that it can be used to calculate net-income consequences for hypothetical work states. Its main value for your framework is infrastructural: it can supply the policy-sensitive monetary mapping needed underneath a richer jobs-and-wellbeing model. 

# Relation to Bargain et al. (2013)

This paper is directly relevant as background infrastructure for the Bargain line of research. It explicitly notes that EUROMOD has been extensively used as the basis for labour-supply models and cites Bargain et al. (2012c) among the examples. Relative to Bargain et al. (2013), EUROMOD does not provide the welfare metric or the estimated heterogeneous preferences; it provides the harmonized tax-benefit and budget-set environment on top of which such work can be built. So the relation is foundational and empirical rather than conceptual. 

# Relation to opportunities vs preferences

This paper is much weaker on opportunities and preferences than on policy mechanics. It does not model opportunity sets, and it does not estimate preferences. It therefore does not resolve the opportunities-versus-preferences distinction. 

But it is still relevant because it isolates the policy component of the environment. In your broader research program, that is useful: if one wants to separate preferences, opportunities, and policy-induced net incomes, EUROMOD can help identify the last component cleanly while leaving the first two to other models. 

# Useful quotations / formulas

A central formulation appears on page 4: EUROMOD is “static” in that its arithmetic simulations abstract from behavioural reactions and hold socio-demographic characteristics fixed. This is one of the most important conceptual clarifications in the paper. 

The work-incentive indicators listed on page 8 are also central: Effective Marginal Tax Rates, Replacement Rates, and Participation Tax Rates. These are among the main outputs relevant for later labour-supply analysis. 

The discussion on pages 10–12 is especially useful because it explains validation and the assumptions on non-take-up and tax evasion. For practical use of EUROMOD, this is as important as the headline description of the model itself. 

# Suggested tags

EUROMOD, tax-benefit-microsimulation, Europe, static-model, policy-simulation, redistribution, work-incentives, validation, EU-SILC, empirical-infrastructure

# My quick takeaway

This is a core infrastructure paper for the empirical side of your project. It does not contribute directly to your theory of well-being or to the modeling of feasible job sets, but it explains the main European tax-benefit engine that can sit underneath labour-supply, reform, and welfare analysis. For your JMP, its main value is practical and architectural: it clarifies exactly what EUROMOD can provide, what it cannot provide, and where it fits in a broader (W(z,R,A;y))-type research design.
