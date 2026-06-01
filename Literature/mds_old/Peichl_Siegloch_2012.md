---

title: "Accounting for labor demand effects in structural labor supply models"
authors: ["Andreas Peichl", "Sebastian Siegloch"]
year: 2012
outlet: "Labour Economics"
country_or_context: "Germany"
population: "Working-age individuals and couples in Germany in the labor supply model; firms and employees in German linked employer–employee administrative data in the labor demand model"
data_period: "Labor supply side: SOEP 2010 wave with information for 2009; labor demand side: LIAB establishment-year panel, 1996–2007"
shelf: "labor_supply_demand_link"
tags: ["labor supply", "labor demand", "partial equilibrium", "structural model", "workfare", "Germany", "microsimulation", "linked employer-employee data", "wage adjustment", "policy evaluation"]
priority: "high"
read_status: "extracted"
------------------------

# Full citation

Peichl, Andreas, and Sebastian Siegloch. 2012. “Accounting for labor demand effects in structural labor supply models.” *Labour Economics* 19(1): 129–138. 

# One-sentence contribution

The paper proposes a practical way to extend structural labor supply microsimulation by adding estimated labor demand reactions at the microdata level, and shows in a German workfare simulation that ignoring demand offsets overstates employment gains by about 25%. 

# Why this paper matters

This paper matters because most structural labor supply simulations treat labor demand as perfectly elastic, so labor supply shifts are read directly as employment effects. Peichl and Siegloch argue that this is generally false and provide a concrete correction: estimate labor demand for different worker types from linked employer–employee data, then iterate wage and labor supply adjustments until a partial labor market equilibrium is reached. 

For your potential JMP, the paper is important methodologically. It is not a latent-jobs or RURO paper, but it is a serious attempt to stop interpreting labor supply responses in isolation from firm behavior. In your terms, it helps separate household-side preference responses from market-side employment feasibility, although it does so through estimated labor demand rather than through explicit individual opportunity sets. 

# Core research question

How can one incorporate labor demand reactions into structural labor supply models in a tractable microdata-based way, and how much do these demand reactions change the predicted labor market effects of a policy reform such as workfare in Germany? 

# Economic setting and context

The application is Germany. The paper uses a standard tax-benefit microsimulation labor supply setup for German households and combines it with labor demand estimates from linked employer–employee administrative data for German establishments. The policy experiment is a workfare reform under which employable benefit recipients are required to work full time in community jobs to receive transfers. 

The broader context is ex ante policy evaluation. The authors position the paper against a large literature in which labor supply models are used to infer employment effects under the implicit assumption of perfectly elastic labor demand. They argue that this assumption is empirically implausible because labor demand elasticities are finite and therefore wage adjustments must mediate the final employment effect. 

# Model / theoretical framework

The framework combines two structural models. On the household side, the paper uses a static structural discrete-choice labor supply model in the van Soest–Blundell tradition, estimated on German household microdata. On the firm side, it estimates a translog labor demand system from linked employer–employee data, deriving own- and cross-wage elasticities for three skill groups. The two models are then linked by an iterative wage-adjustment procedure until partial labor market equilibrium is reached. 

On the labor supply side, couples choose among 49 joint hours combinations, coming from seven hours categories for each spouse: 0, 10, 20, 30, 40, 50, and 60 hours. Utility is translog in household consumption and spouses’ worked hours, with part-time dummies interpreted as fixed costs of work. On the labor demand side, firms minimize costs given output, with labor inputs distinguished by skill group. 

The framework is positive and policy-evaluative, not directly normative. It studies employment and fiscal effects of policy reforms. There is no welfare ranking, no social welfare function, and no fair-allocation criterion. 

# Key objects

The main household-side objects are discrete labor supply choices, the translog utility function over consumption and worked hours, and labor supply changes by household type, gender, and skill group. The paper distinguishes single men, single women, men in couples, and women in couples, and further splits workers by skill. 

The key firm-side objects are the translog cost function, cost shares, and own- and cross-wage labor demand elasticities for high-, medium-, and low-skilled labor. The estimated own-wage elasticities are about -0.56 for high-skilled, -0.37 for medium-skilled, and -1.05 for low-skilled workers. These are central because they determine how strongly wages adjust to labor supply shifts. 

The central equilibrium object is the iterative demand–supply link. A policy reform first shifts labor supply; then wages adjust according to estimated labor demand; then labor supply is recomputed at the new wages; and the process repeats until changes become negligible. This iterative loop is the core contribution of the paper. The diagram on page 5 illustrates this logic graphically, with labor demand acting as a stabilizer that partly offsets initial labor supply shifts. 

# Data

The labor supply model uses the 2010 wave of the German Socio-Economic Panel (SOEP), containing information for 2009. The paper observes about 25,000 individuals in more than 12,000 households and uses data on gross wages, job type, government transfers, working time, household composition, age, and education. These are translated into net incomes using the IZA tax-benefit calculator IZAΨMOD under January 2009 policy rules. 

The labor demand model uses LIAB linked employer–employee data from the IAB. The worker component comes from the administrative employment register; the firm component is the IAB Establishment Panel. The final panel covers 1996–2007 and contains 13,451 establishment-year observations from 4,073 establishments, with between 1.6 and 2.0 million workers per year. The analysis excludes agriculture, mining, finance, and the public sector, mainly because output or labor supply treatment differs there. 

This is therefore a combined microdata exercise: household survey data for labor supply and linked administrative employer–employee data for labor demand. That is one of the main empirical strengths of the paper. 

# Identification logic

Identification on the labor supply side comes from the standard structural microsimulation logic: nonlinearities and non-convexities in the German tax-benefit system create variation in net wages and disposable incomes across otherwise similar households. The paper also uses predicted wages rather than observed wages for all individuals, partly to reduce bias from wage endogeneity. 

Identification on the labor demand side comes from the translog cost-share system estimated on linked firm-worker data. Variation in observed wages and output across establishments, combined with the structure of the translog system, identifies skill-specific own- and cross-wage demand elasticities. The paper imposes standard curvature and homogeneity restrictions and checks monotonicity, quasi-concavity, and adding-up conditions; the specification passes these tests. Table 6 in the appendix reports 100% satisfaction of strict quasi-concavity and adding-up in the estimated model. 

The key identification step of the paper as a whole is not a single econometric theorem but a structural linkage argument: supply responses alone do not identify employment effects unless labor demand is perfectly elastic. By explicitly estimating labor demand elasticities, the paper identifies the wage adjustment margin that mediates between supply shifts and final employment changes. 

# Estimation / empirical strategy

The household labor supply model is a standard random utility discrete-choice model with a translog utility specification. Couples choose among 49 combinations of hours. Net incomes are computed with IZAΨMOD. The paper calibrates the random utility component using Extreme Value Type-I errors so that observed choices maximize utility. 

The labor demand model is estimated from a translog cost function and the associated cost-share equations for three skill types, using seemingly unrelated regression on LIAB data. The estimated system is then used to derive own- and cross-wage labor demand elasticities. 

The main empirical strategy is then simulation. The authors implement the workfare reform, calculate the initial labor supply shift, compute wage adjustments implied by the labor demand elasticities, feed those wages back into the labor supply model, and iterate until convergence. Table 3 on page 7 shows the iteration process numerically for each household-type/skill cell, with alternating hours and wage adjustments that shrink as the model converges. 

# Treatment of preferences

Preferences are modeled on the household side only. The utility function is translog in consumption and worked hours, with parameters varying by age, children, region, and other observables. Part-time work enters via dummy variables interpreted as fixed costs of work. 

The paper is not about heterogeneous preferences in the normative sense. Preferences are purely behavioral primitives driving labor supply choices. The main conceptual contribution is not to enrich tastes but to show that policy-induced labor supply changes should not be read as employment changes when firms respond along the demand side. 

Relative to your agenda, this means the paper sharpens the separation between preference-driven household responses and market-clearing outcomes, but it does not separately study heterogeneous preferences versus heterogeneous opportunities at the individual job-set level. 

# Treatment of opportunities / constraints

This section is crucial for your interests.

The paper does not model opportunities as latent job sets or random opportunity densities in the RURO sense. Instead, it accounts for constraints through a different channel: firm labor demand. Individuals choose labor supply in the usual discrete-hours way, but the final employment outcome depends on whether firms absorb the additional labor supply at unchanged wages or whether wages adjust downward and partially undo the initial supply shift. 

So the paper treats labor demand as the main omitted constraint in standard structural labor supply models. It is explicit that pure labor supply models implicitly assume perfectly elastic labor demand, and that this is precisely the source of bias in predicted employment outcomes. In that sense, the paper separates household preferences from market feasibility better than the standard model. 

However, opportunities are still not first-class micro objects. The model does not describe which jobs are available to whom, how hours offers are restricted, or how job quality differs across workers. For your agenda, this is an important limitation: the paper adds market-clearing labor demand, not individual opportunity sets. 

# Welfare / normative object

None. The paper does not construct equivalent income, compensating variation, or a social welfare function. Its evaluation criteria are employment and fiscal outcomes under alternative policy rules. 

The paper is therefore purely positive with policy-application consequences. It is highly relevant for policy design, but not directly a welfare-economics paper in the sense of your JMP agenda. 

# Main findings

First, the paper finds finite and economically meaningful labor demand elasticities. The estimated own-wage elasticities are about -0.56 for high-skilled, -0.37 for medium-skilled, and -1.05 for low-skilled workers. This is the central empirical premise for rejecting the perfectly elastic labor demand assumption. 

Second, when the workfare reform is simulated without labor demand effects, labor supply rises by about 1.49 million full-time equivalents. Once labor demand is incorporated, this increase falls by about 377,000 FTE, so the final effect is closer to 1.11 million jobs. Demand effects therefore offset about 25% of the positive labor supply effect. 

Third, labor demand acts as a stabilizer more generally. The paper states that in additional robustness checks, if a reform reduces labor supply, demand adjustments work in the opposite direction as well and make the overall employment effect less negative. So the stabilizing role is not specific to workfare. 

Fourth, the magnitude of the offset depends on the size of labor demand elasticities. The higher the absolute value of the demand elasticity, the smaller the countervailing demand effect for a given labor supply shift, and the quicker the model converges. The chart on page 8 illustrates this graphically with low- and high-elasticity demand curves. 

Fifth, the workfare reform remains fiscally feasible even after demand effects are accounted for. The gross budget gain falls from about €31.7 billion after pure labor supply adjustments to about €27.7 billion after also accounting for labor demand. After subtracting estimated workfare program costs, the net gain remains positive. 

# Main limitations

A first limitation is that the framework is partial equilibrium. It models wage and employment adjustments in the labor market but ignores broader general equilibrium channels such as consumption, prices, output-market adjustment, and intertemporal responses. The authors state this explicitly. 

A second limitation is that the labor market is effectively assumed perfectly competitive in the linking step. The paper notes that it does not model wage rigidities, unions, efficiency wages, or search frictions, although it suggests these would be natural future extensions. 

A third limitation, relative to your interests, is that the constraint side is firm labor demand by skill cell, not individual opportunity sets. The model therefore captures market-level feasibility but not worker-level job-offer heterogeneity. 

A fourth limitation is that labor demand is assumed not to shift in response to the reform. The demand curve itself is held fixed while wages move along it. This is reasonable for a pure labor supply reform, but still restrictive. 

A fifth limitation is that the labor supply side remains a conventional discrete-hours model. So the paper corrects one major omission of standard structural labor supply analysis, but not all of them. 

# Relevance for my JMP

## possible use for framing

This paper is very useful for framing a project that argues structural labor supply analysis is incomplete if it ignores firm behavior. It gives you a precise language: pure labor supply models identify supply shifts, not final employment effects. 

## possible use for model design

It is useful as a modular design template. You could think of your own project as combining three layers: preferences, opportunities, and market equilibrium. This paper helps with the market-equilibrium layer by showing how to append labor demand to a labor supply microsimulation. 

## possible use for identification

The paper is valuable because it demonstrates that employment effects require separate identification of labor demand elasticities. For your agenda, this is a reminder that separating preferences from opportunities may still be insufficient if one ignores equilibrium demand responses. 

## possible use for welfare measurement

Indirectly useful. Any welfare or optimal-tax analysis using labor supply responses as behavioral primitives may misstate policy effects if labor demand offsets are ignored. The paper does not solve the welfare problem, but it improves the positive model that welfare analysis would sit on. 

## possible use for cross-country comparison

Potentially very useful. One natural extension of your agenda would be to ask whether cross-country differences in employment or welfare effects of tax-benefit reforms are driven not only by preferences and opportunities, but also by country-specific labor demand elasticities. 

# Research questions this paper inspires

How much of the cross-country variation in estimated reform effects is due to differences in labor demand elasticities rather than differences in preferences or tax systems?

Can a latent-job or RURO model be linked to a labor demand module of this kind, so that both worker opportunity sets and firm responses are modeled explicitly?

How much do opportunity-sensitive welfare comparisons change once one moves from pure labor supply responses to demand-adjusted employment outcomes?

Would optimal tax prescriptions change materially if one combined a structural household labor supply model, explicit opportunity sets, and skill-specific labor demand responses in one integrated framework? 

# Challenge to this paper

The strongest omission is that the paper corrects standard structural labor supply models at the market level but not at the individual opportunity-set level. It recognizes that employment effects depend on demand, but it still assumes household labor supply is chosen from a conventional discrete-hours menu. A future paper could challenge this by integrating three things simultaneously: household preferences, heterogeneous job opportunities, and firm labor demand. 

# Relation to Bargain et al. (2013)

[not central].

# Relation to opportunities vs preferences

This paper helps separate market demand constraints from household preference responses, but it does not separate preferences from individual opportunity sets in the RURO/latent-jobs sense. It therefore moves part of the way toward your agenda. It says: even if you know household preferences, employment outcomes still depend on firm-side labor demand. But it does not yet say which jobs are available to which workers. So it is best read as a complementary equilibrium extension, not as a substitute for opportunity-set modeling. 

# Useful quotations / formulas

The central household-side utility is a translog specification over consumption and spouses’ worked hours:
[
U_{ij}
======

\alpha_{ci}\ln c_{ij}
+
\alpha_{h_i^f}\ln h_{ij}^f
+
\alpha_{h_i^m}\ln h_{ij}^m
+\cdots
]
with part-time dummies added as fixed costs of work. This is the labor supply backbone. 

The central labor demand object is the translog cost function and its implied cost-share equations. The paper computes own-wage elasticities as
[
\mu_{ii}^{TL}
=============

\frac{\alpha_{ii}-\hat S_i+\hat S_i\hat S_i}{\hat S_i},
]
and cross-wage elasticities as
[
\mu_{ij}^{TL}
=============

\frac{\alpha_{ij}+\hat S_i\hat S_j}{\hat S_i}.
]
These formulas generate the skill-specific demand responses that drive the demand–supply link. 

The key substantive empirical claim is that demand effects “offset about 25% of the positive labor supply effect of the policy reform.” That is the main takeaway from the workfare application. 

# Suggested tags

#labor_supply #labor_demand #structural_model #partial_equilibrium #microsimulation #linked_employer_employee_data #Germany #workfare #wage_adjustment #policy_evaluation

# My quick takeaway

If I only remember one thing from this paper for my JMP, what should it be? That even a well-specified structural labor supply model is not enough to infer employment effects from policy reform: firm labor demand can undo a substantial share of the initial supply response, so serious policy analysis needs at least one equilibrium layer beyond household behavior.
