---

title: "Microsimulation as a tool for evaluating redistribution policies"
authors: ["François Bourguignon", "Amedeo Spadaro"]
year: 2006
outlet: "Journal of Economic Inequality"
country_or_context: "Methodological / multi-country applications"
population: "Not a single empirical sample; methodological review covering individuals and households in microsimulation models"
data_period: "[not central; paper is a methodological survey drawing on prior applications]"
shelf: "microsimulation_redistribution_welfare"
tags: ["microsimulation", "redistribution", "tax-benefit systems", "poverty", "inequality", "social welfare analysis", "behavioral microsimulation", "micro-macro models"]
priority: "high"
read_status: "extracted"
------------------------

# Full citation

Bourguignon, François, and Amedeo Spadaro. 2006. “Microsimulation as a tool for evaluating redistribution policies.” *Journal of Economic Inequality* 4: 77-106. 

# One-sentence contribution

The paper provides a methodological synthesis of microsimulation for redistribution analysis, distinguishing arithmetical from behavioural models, clarifying their theoretical foundations, and discussing how they can be used for tax incidence, poverty, inequality, and social welfare evaluation. 

# Why this paper matters

This paper matters because it is not merely a survey of applications; it is an attempt to organize microsimulation methods conceptually around budget constraints, behavioural responses, welfare metrics, and social evaluation. For your project, that makes it valuable as a map of the empirical and normative terrain linking tax-benefit modelling, labour supply, and welfare analysis. 

It is especially relevant because it explicitly separates arithmetical microsimulation, where behaviour is held fixed, from behavioural microsimulation, where labour supply or other decisions respond to policy changes. This distinction is directly useful for your research because it clarifies when one is evaluating outcomes under unchanged feasible behaviour and when one is attributing effects to preference-driven or constraint-driven behavioural responses. 

# Core research question

How should microsimulation techniques be understood and used as tools for evaluating redistribution policies, especially with respect to tax incidence, poverty, inequality, behavioural responses, and social welfare analysis? 

# Economic setting and context

The paper is methodological rather than country-specific. Its object is the class of microsimulation models used for redistribution analysis. The authors discuss a wide range of settings, including direct and indirect taxation, social assistance, labour supply, conditional cash transfers, pensions, and dynamic policy evaluation. They also discuss applications in both developed and developing countries, and at both national and cross-country levels. 

The context is the increasing use of micro-data and computing power in public economics. The authors emphasize that microsimulation arose as a response to the inadequacy of “representative agent” approaches when redistribution and heterogeneity matter, and they present microsimulation as the natural tool for identifying winners, losers, and aggregate budget effects of reforms. 

# Model / theoretical framework

The paper does not present one single structural model. Rather, it presents a taxonomy of microsimulation models. The common structure of these models is said to comprise three elements: a micro-dataset describing individuals or households, the policy rules that define their budget constraints, and, where relevant, a behavioural model governing their response. Section 2 is explicit on this taxonomy. 

The authors distinguish arithmetical microsimulation models from behavioural microsimulation models. Arithmetical models apply a change in the tax-benefit system to observed agents while holding behaviour fixed. Behavioural models add structural or semi-structural representations of responses such as labour supply, savings, or household composition. They further distinguish static from dynamic models, and partial equilibrium from general equilibrium models. 

In the behavioural labour-supply case, the paper sets out a standard continuous labour-supply model in which an agent chooses consumption and labour to maximize utility subject to a tax-benefit-induced budget constraint, and then discusses discrete-choice alternatives in which labour supply takes a finite number of values and the chosen alternative is the one with highest utility. Equations (7)–(14) summarize these structures. 

The framework is both positive and normative. It is positive because it models behaviour and budget constraints. It is normative because it also discusses welfare metrics, equivalent-variation logic, money-metric utility, social welfare functions, and optimal redistribution exercises. This dual character is one of the paper’s strongest features. 

# Key objects

The key positive objects are the micro-dataset, the tax-benefit or “net tax” schedule (NT(\cdot)), the budget constraint, and the behavioural decision rule. In the continuous labour-supply setup, the key equation is the household optimization problem subject to the tax-benefit schedule, leading to a labour-supply function of wages, non-labour income, household characteristics, and preference parameters. Equations (7)–(10) are the core objects for this part. 

The key normative objects are the indirect utility function (V_i(p,y_i)), the equivalent variation or welfare-income metric (\Delta y_i^*), and the social welfare function (SWF(\theta)). Equations (1)–(6) provide the envelope-theorem justification for arithmetical microsimulation in welfare terms, while Equations (15)–(17) define social welfare and money-metric utility in the behavioural case. These are the paper’s central theoretical objects for welfare analysis. 

# Data

The paper does not rely on a single dataset. It is a methodological survey drawing on many applications, including Euromod-type European tax-benefit models, labour-supply applications in several countries, and studies of conditional cash-transfer programs in developing countries. The data object is therefore generic: household-level micro-data containing incomes, socio-demographic characteristics, and variables necessary to reconstruct tax liabilities, benefit entitlements, or behavioural equations. 

The important point for your purposes is that the authors treat the micro-dataset as foundational. Microsimulation requires detailed household heterogeneity precisely because the goal is to identify the winners and losers of redistribution reforms and to evaluate their aggregate budgetary and welfare consequences. 

# Identification logic

This is not an identification paper in the narrow econometric sense. It does not derive identification theorems for parameters from exclusion restrictions or support conditions. Instead, its logic is conceptual and methodological: policy evaluation becomes possible because the analyst combines observed heterogeneity in the micro-data with explicit policy rules and, in behavioural models, an estimated or calibrated behavioural response model. 

For arithmetical microsimulation, the key theoretical justification is the envelope theorem. The authors show that, for marginal reforms and under perfect-market assumptions, the welfare effect of a price or tax change can be measured by applying the new prices to the initial consumption bundle. Equations (1)–(6) are the key theoretical justification. This is not identification of preferences, but it does justify the welfare interpretation of first-round incidence calculations. 

For behavioural microsimulation, the implicit identification logic is standard structural estimation or calibration. The behavioural rule is estimated from cross-sectional variation in wages, non-labour income, household characteristics, and the tax-benefit schedule, and then used for counterfactual simulation. The authors are explicit that this relies on strong assumptions, including the assumption that cross-sectional income effects proxy for the policy-induced income effects relevant for simulation. They flag this as an important limitation. 

Thus, identification is mainly parametric or structural in the behavioural case, and welfare-theoretic rather than econometric in the arithmetical case. [reasonable inference for my project] supported by 

# Estimation / empirical strategy

The paper is not itself an empirical estimation study, but it gives a clear account of the empirical strategy underlying behavioural microsimulation. The basic sequence is: specify a behavioural model, estimate or calibrate it on micro-data, then simulate alternative tax-benefit systems by changing the policy parameters while holding estimated preference parameters fixed and computing new choices and welfare levels. Equations (7)–(11) describe this standard approach for continuous labour supply. 

The paper then stresses the practical importance of discrete-choice labour-supply models, where labour supply takes finitely many values and each alternative has an associated utility level. The chosen alternative is the one with highest utility, and the tax-benefit system enters through the disposable income attached to each alternative. Equations (12)–(14) summarize this. This part is especially useful because it shows why discrete-choice models became attractive for behavioural microsimulation: they relax some functional-form restrictions while remaining easy to simulate. 

The authors also discuss calibrated models, where some behavioural parameters are imposed rather than estimated, and pseudo-residuals or idiosyncratic terms are backed out so that predicted choices under the status quo match observed choices. This is useful when the analyst wants behavioural realism without a full structural estimation exercise. 

# Treatment of preferences

Preferences are central in the behavioural part of the paper. In the continuous labour-supply framework, preferences are represented by a utility function over consumption, labour, and household characteristics, with common parameters and idiosyncratic terms. In the discrete-choice framework, the utility attached to each labour-supply alternative depends on wages, disposable income, observed characteristics, common parameters, and alternative-specific idiosyncratic terms. 

The paper treats preference heterogeneity pragmatically rather than axiomatically. It allows for idiosyncratic terms, which generate unobserved heterogeneity in behaviour and in responses to reforms. This is discussed explicitly around the discrete-choice model. The authors note that otherwise identical agents can respond differently to the same reform because their idiosyncratic preference terms differ. 

At the same time, the authors are quite clear that these behavioural models are only as credible as the assumptions used to estimate or calibrate them. They stress that strong assumptions remain, particularly the equivalence between cross-sectional income effects and policy-induced income effects. This is one of the paper’s most useful warnings. 

# Treatment of opportunities / constraints

This section is crucial for your project, and the paper is mixed in its usefulness. The paper absolutely emphasizes budget constraints and tax-benefit rules. In both arithmetical and behavioural microsimulation, the central “constraint” is the budget set defined by taxes, benefits, wages, and non-labour income. In that sense, constraints are modeled explicitly. 

However, the paper does not generally model opportunities as feasible job sets in the RURO sense. It does not analyse latent job availability, hours offers, occupation sets, or employer-side restrictions as a core object. The standard labour-supply setup is one where individuals choose labour supply conditional on wages and the tax-benefit system, not one where the feasible set (A) is itself heterogeneous and central. 

There are some partial openings toward opportunity-sensitive modelling. The paper notes that behavioural responses may concern labour supply, savings, or household composition, and later discusses imperfect labour markets and rationing in the context of linking microsimulation and general equilibrium or macro models. But this is an extension, not the standard core. The main framework does not separate preference heterogeneity from opportunity-set heterogeneity in the sense of jobs-and-wellbeing or RURO. 

So the paper helps with one class of constraints, namely budget constraints, but not with feasible job sets as distinct opportunity objects. That distinction is important for your project and the paper does not resolve it. 

# Welfare / normative object

This is one of the strongest parts of the paper. The authors explicitly justify arithmetical microsimulation using standard consumer theory and the equivalent variation or income-metric welfare change. They show that, for marginal reforms and under standard assumptions, the welfare effect of a price change can be measured by the cost of the initial consumption bundle under the new prices. Equations (1)–(6) provide this justification. 

They then extend the discussion to behavioural models and define a social welfare function over indirect utilities or money-metric utilities. Equations (15)–(17) define social welfare in a way that permits comparative evaluation of tax-benefit systems and links microsimulation to optimal redistribution analysis. This is one of the paper’s clearest bridges from behavioural microsimulation to applied public-economics welfare analysis. 

The paper also discusses how behavioural microsimulation can be used for applied optimal-tax analysis, for “inverse optimum” exercises that reveal the social preferences implicit in existing systems, and for comparative welfare evaluation of alternative tax-benefit structures. This material is especially valuable for your corpus because it shows how positive tax-benefit models and normative welfare criteria can be combined. 

What the paper does not do is develop a responsibility-sensitive welfare theory. It discusses social welfare, equity-efficiency trade-offs, and money-metric comparisons, but it does not explicitly treat compensation for opportunities, responsibility for opportunity sets, or reference opportunity sets. Those are outside its framework. 

# Main findings

Because this is a survey paper, the “findings” are methodological rather than a single empirical result. The first main finding is that microsimulation is powerful because it fully exploits household heterogeneity. It identifies winners and losers of reforms with much greater precision than representative-agent or “typical-case” approaches and also permits accurate budget-cost calculations. This is emphasized in the introduction and in the discussion of arithmetical models. 

The second main finding is that arithmetical microsimulation has a serious theoretical justification in welfare terms. The authors show that holding behaviour fixed is not simply ad hoc rigidity; for marginal reforms under standard assumptions, it is fully consistent with the envelope theorem and welfare-income measurement. This is a very important clarification. 

The third main finding is that behavioural microsimulation permits explicit analysis of the equity-efficiency trade-off and thereby connects microsimulation to applied optimal redistribution theory. Once labour-supply or consumption behaviour is modeled, one can evaluate not only disposable-income changes but also behavioural feedback on budgets and welfare. The discussion of labour-supply models and social welfare analysis is central here. 

The fourth main finding is forward-looking: the authors argue that the future of microsimulation lies in deeper behavioural modelling, dynamic models, and links to macro or general-equilibrium frameworks. The final section on extensions is explicit about this trajectory. 

# Main limitations

The first limitation is that the paper is broad and synthetic rather than analytically narrow. It does not derive detailed econometric identification results or propose one unified empirical framework. For a researcher wanting a ready-made estimation blueprint, it is more of a conceptual guide than a directly implementable model. 

The second limitation, crucial for your project, is that the paper’s central notion of “constraint” is the budget set, not the feasible job set. Labour-market opportunities in the sense of latent job availability, employer rationing, or opportunity sets (A) are largely absent from the baseline models. That makes the paper much more informative about (y)-type objects and tax-benefit constraints than about opportunity-set heterogeneity. 

The third limitation is that behavioural microsimulation relies on strong assumptions, and the authors explicitly say so. These include the behavioural specification itself, the equivalence between cross-sectional and policy-induced income effects, and the difficulty of testing the structural assumptions underlying simulation. This caution is one of the paper’s strengths, but it remains a limitation of the approach. 

A fourth limitation is that the welfare framework remains within standard public-economics social welfare analysis. It does not engage with axiomatic fairness theory of the kind you are developing. So although it is useful for social welfare and redistribution, it is not yet a theory of fair compensation for unequal opportunities. 

# Relevance for my JMP

## possible use for framing

This paper is highly useful for framing because it shows how microsimulation fits into the broader public-economics toolkit. It can help motivate why one needs micro-level heterogeneity, why representative-agent reasoning is insufficient for redistribution analysis, and why positive and normative analysis are often combined in practice. 

## possible use for model design

It is useful for model design if part of your empirical strategy involves tax-benefit microsimulation, labour-supply responses, or social-welfare comparisons. In particular, the paper gives a clean taxonomy of arithmetical versus behavioural versus dynamic versus micro-macro integrated approaches. That taxonomy can help you situate your own empirical design. 

## possible use for identification

Its use for identification is indirect. It does not provide the kind of formal identification results found in econometric theory papers, but it is useful in clarifying what data, behavioural assumptions, and policy variation are doing in a microsimulation exercise. It is therefore valuable as a conceptual identification map, especially for structural tax-benefit modelling. [reasonable inference for my project] supported by 

## possible use for welfare measurement

Very high relevance. The paper is one of the stronger survey-style references on how microsimulation can be linked to welfare-income metrics, social welfare functions, and applied optimal redistribution analysis. It is especially useful if you want to explain how one gets from behavioural simulation to welfare comparison without immediately invoking axiomatic fairness theory. 

## possible use for decomposition

Moderate relevance. The paper is about policy evaluation, not decomposition of inequality into preferences and opportunities. Still, it is useful because it distinguishes first-round incidence, behavioural effects, and aggregate fiscal feedback, which are themselves decompositions of policy impact. It does not, however, give the decomposition you want into (R), (A), and (y). 

## possible use for comparative application

High relevance. The paper discusses several cross-country and policy-comparison applications and gives strong support for comparative tax-benefit simulation across countries or systems. This is useful if your later work wants to compare welfare consequences of different institutional designs under a common framework. 

# Research questions this paper inspires

Can one extend standard behavioural microsimulation by replacing the universal labour-supply choice set with heterogeneous feasible job sets (A_i), so that behavioural and welfare analysis jointly reflect opportunity inequality?

How would a money-metric social welfare analysis change if the benchmark object were not only disposable income under a tax-benefit schedule, but also the size or quality of an individual’s feasible opportunity set?

Can microsimulation outputs be decomposed into components attributable to tax-benefit rules, preferences, and opportunity-set heterogeneity, rather than only first-round and behavioural feedback effects?

What would an “inverse optimum” exercise reveal if existing tax-benefit systems were evaluated under a fairness criterion that compensates unequal opportunities but respects responsibility for preferences?

Can discrete-choice labour-supply microsimulation be embedded in a RURO model where labour supply and job availability are jointly determined?

# Challenge to this paper

The main challenge is conceptual. Microsimulation as presented here is powerful for evaluating redistribution policies, but it takes as given the standard public-economics frame in which the main individual constraint is the budget set. For projects concerned with fairness of opportunities, that frame may be too narrow because it treats labour-market access and job availability as peripheral rather than central. 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper offers a broad framework for policy evaluation in which individual welfare effects are computed from changes in budget constraints and, in behavioural models, from the responses of agents to those changes. It is therefore directly relevant to the general question of how to connect individual-level data, behavioural structure, and social welfare evaluation. 

[reasonable inference for my project] In your notation, the paper is strongest on the (y)-side and on the welfare-aggregation side. It shows how policy changes alter disposable incomes and budget constraints, and how one may evaluate those changes through money-metric welfare or social welfare functions. This makes it useful for thinking about the normative treatment of realized bundles (z) and pay/tax schedules (y). supported by 

[unclear from paper] There is no explicit (W(z,R,A;y)) formulation, no formal feasible job set (A), and no treatment of the axiomatic role of opportunities as distinct from disposable-income possibilities. The paper does not analyse whether welfare should be independent of (A), sensitive to (A), or compensate for differences in (A). 

[reasonable inference for my project] The paper is therefore closer to social-welfare evaluation of tax-benefit systems than to an opportunity-sensitive jobs-and-wellbeing framework. It can serve as a bridge between your empirical/public-economics side and your axiomatic side, but not as a substitute for the latter. It is closer to decomposition of policy effects and money-metric welfare than to responsibility for opportunities, reference opportunity sets, or laissez-faire well-being evaluation. supported by 

# Relation to Bargain et al. (2013)

This paper is clearly relevant to the same general literature on labour supply, taxation, and welfare evaluation, but it operates at a broader methodological level. Relative to benchmark work such as Bargain et al. on welfare comparisons under heterogeneous preferences and labour-supply microsimulation, Bourguignon-Spadaro is more of a synthetic guide to the field and to its normative extensions than a focused empirical contribution. It is useful for situating Bargain-type work inside the wider microsimulation and redistribution literature. [reasonable inference for my project] supported by 

# Relation to opportunities vs preferences

The paper mainly discusses preferences and budget constraints, not opportunities in the sense of feasible job sets. Behavioural models distinguish observed heterogeneity, common parameters, and idiosyncratic preference terms, but they generally take the choice set as the budget-feasible set generated by wages and taxes. 

This means the paper is informative for the preferences-versus-budget-constraint distinction, but not for the preferences-versus-opportunities distinction as you define it. It is thus very useful for understanding one source of welfare differences, namely policy-shaped budget sets, while leaving open the more fundamental question of unequal job opportunities. [reasonable inference for my project] supported by 

# Useful quotations / formulas

The most important formula for the welfare justification of arithmetical microsimulation is the equivalent welfare-income change:
[
\Delta y_i^* = \sum_j x_{ij}\Delta p_j,
]
which shows that, for marginal price or tax changes under the usual assumptions, the welfare change can be measured by pricing the initial bundle at new prices. This is the paper’s main theoretical defence of first-round incidence analysis. 

For behavioural microsimulation, the key continuous setup is the household optimization problem under a net-tax schedule:
[
\max u(c_i,L_i;z_i,\beta,\varepsilon_i)
\quad \text{s.t.} \quad
c_i \le y_i^0 + w_iL_i + NT(w_iL_i,L_i,y_i^0,z_i;\theta),
]
which is then used to derive labour-supply reactions to policy reforms. 

For normative analysis, the key aggregation device is the social welfare function:
[
SWF(\theta)=\sum_i G!\left[V(w_i,y_i^0,z_i,\beta,\varepsilon_i;\theta)\right],
]
or equivalently its money-metric version. This is the paper’s main bridge to applied optimal redistribution theory. 

# Suggested tags

microsimulation, redistribution, tax-benefit-analysis, labor-supply-microsimulation, behavioral-microsimulation, social-welfare-analysis, money-metric-utility, applied-optimal-taxation

# My quick takeaway

This is a high-value synthesis paper for your corpus. It is not a paper about job opportunity sets, RURO, or opportunity-sensitive fairness, so it should not be treated as directly solving your (W(z,R,A;y)) problem. But it is extremely useful for understanding how public economists connect micro-data, budget constraints, behavioural responses, and social welfare analysis in practice. For your JMP, it is best read as a bridge paper linking structural microsimulation and normative evaluation on the (z)- and (y)-side, while leaving the (A)-side largely open.
