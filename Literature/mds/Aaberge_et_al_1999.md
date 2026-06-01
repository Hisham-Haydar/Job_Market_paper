---

title: "Labour Supply in Italy: An Empirical Analysis of Joint Household Decisions, with Taxes and Quantity Constraints"
authors: ["Rolf Aaberge", "Ugo Colombino", "Steinar Strøm"]
year: 1999
outlet: "Journal of Applied Econometrics"
country_or_context: "Italy"
population: "Married couples in Italy; husbands and wives aged 20–68; households with self-employment income above 20% of gross household income excluded"
data_period: "1987"
shelf: "structural_labour_supply_quantity_constraints"
tags: ["structural labour supply", "joint household decisions", "quantity constraints", "random utility", "opportunity sets", "Italy", "tax simulation", "hours restrictions"]
priority: "very high"
read_status: "extracted"
------------------------

# Full citation

Aaberge, Rolf, Ugo Colombino, and Steinar Strøm. 1999. “Labour Supply in Italy: An Empirical Analysis of Joint Household Decisions, with Taxes and Quantity Constraints.” *Journal of Applied Econometrics* 14(4): 403–422. 

# One-sentence contribution

The paper develops and estimates for Italy a joint household labour-supply model in which couples choose among jobs characterized by hours, wages, and non-pecuniary attributes under exact tax rules and quantity constraints, and it shows that female labour supply is much more elastic than male labour supply, especially in poor households. 

# Why this paper matters

This paper matters because it is an early and important precursor of the Aaberge–Colombino line that later becomes central for RURO-type modelling. It moves beyond the Hausman framework by allowing non-convex budget sets, quantity constraints, joint household decisions, and heterogeneous opportunity sets. For your research direction, that is especially important because the paper explicitly refuses the universal flexible-hours choice set and instead models labour supply as constrained by the distribution of available jobs. 

It is also valuable because it is one of the clearest early empirical papers that tries to separate preferences from opportunities on the positive side. Preferences enter through the deterministic utility component; opportunities enter through the distribution of jobs by hours and wages and through household-specific availability parameters. That is not yet your normative (W(z,R,A;y)) framework, but it is very close to the empirical architecture needed for it. 

# Core research question

How do taxes affect joint household labour supply in Italy when one explicitly accounts for non-convex budget sets, quantity constraints, heterogeneous job opportunities, and simultaneous labour-supply decisions of husbands and wives? 

# Economic setting and context

The paper studies Italy using the 1987 Survey of Household Income and Wealth conducted by the Bank of Italy. The authors emphasize that this was the first nationwide Italian survey available to them with both income and hours information sufficient to compute wages and estimate a structural model of labour supply with taxes. They position the paper against earlier Italian studies that either used local samples, ignored taxes, ignored non-convexities, or modeled only wives’ labour supply rather than joint decisions. 

The policy context is the 1987 Italian tax and benefit system. The paper models the exact individual-based income tax schedule and family benefits, and then simulates revenue-neutral reforms toward proportional taxation and toward increased progression. The applied focus is therefore clearly tax reform under realistic institutional constraints rather than abstract labour-supply estimation alone. 

# Model / theoretical framework

The model class is a structural random-utility labour-supply model with quantity constraints and random opportunity sets. A household faces a set of market and non-market opportunities. Each market opportunity is characterized by fixed hours of work, a wage rate, and other job characteristics; non-market opportunities have zero hours and zero wage. Utility over an opportunity takes the multiplicative form
[
U_i(C,h,j)=v_i(C,h)\varepsilon_{ij},
]
where (v_i) is the deterministic component and (\varepsilon_{ij}) is a random taste shifter. The household chooses the opportunity that maximizes utility subject to the tax-based budget constraint (C=f(wh,I)). 

The feasible set is not universal and is not assumed to contain arbitrary hours choices. Instead, the paper models the opportunity set through the number or density of available jobs of each type. Jobs are indexed by hours and wages, and the probability of choosing a job depends jointly on the deterministic utility of that job and on the relative number of such opportunities. This is the central formal device through which quantity constraints and labour-demand-side restrictions enter the model. 

The framework is positive rather than normative. It is designed to explain labour-supply choices and to simulate the effects of alternative tax systems on labour supply and the income distribution. The paper does not build a social welfare function, does not discuss fairness axioms, and does not provide a responsibility-sensitive welfare evaluation. 

# Key objects

The key positive objects are the household utility function (U_i(C,h,j)), its deterministic component (v_i(C,h)), the tax function (f(\cdot)), and the opportunity objects (g(h,w)) and (g_0), which summarize the distribution and relative abundance of feasible market opportunities versus non-market opportunities. In the couple version, the opportunity density extends to ((h_F,h_M,w_F,w_M)). 

A central conceptual object is the distinction between the preference term and the opportunity term in the labour-supply density. The choice probability is proportional to the utility term (\Psi_i(h,w)) times the opportunity term (g_i(h,w)), scaled by the relative number of market opportunities (g_{0i}). That decomposition is one of the main reasons this paper is so relevant to your agenda. 

# Data

The data come from the 1987 Bank of Italy Survey of Household Income and Wealth. The sample consists of 2,953 married-couple households after excluding households in which self-employment income exceeds 20% of gross household income. For included households, self-employment income is added to net household income and treated as exogenous. Husbands’ and wives’ ages are restricted to 20–68. Table I reports the main sample statistics. 

Table I shows, among other things, a male participation rate of 96% and female participation rate of 40%, mean annual hours of 1,995 for men and 690 for women, mean hourly wages of 12.0 thousand lire for men and 4.3 thousand lire for women, and mean disposable household income of 27.9 million lire. These descriptive facts matter because the whole elasticity structure is estimated around this institutional and demographic environment. 

# Identification logic

The paper is unusually explicit about identification. It shows, within the theoretical model, that the non-participation probability under a benchmark “fair environment” and the observed unemployment and participation rates can identify the relative abundance of market opportunities (g_0) nonparametrically. It also shows that, under separability of the deterministic utility component in income and leisure, variation in fixed costs of work can identify the income-utility component (v_1(\cdot)) nonparametrically, and that once (v_1) is identified, the conditional wage density (g_1(w\mid h)) can also be identified. 

However, identification is only partly nonparametric. The paper is explicit that the decomposition of (v_2(h)) and the hours opportunity density (g_2(h)) cannot be achieved nonparametrically without additional institutional or firm-specific information, so parametric assumptions are imposed. In the empirical implementation, offered hours are assumed uniformly distributed except for a peak at full-time hours, and wages are assumed lognormal with means depending on education, experience, and region. 

Thus the paper combines a formal identification argument with a strongly parametric estimation strategy. There is no quasi-experimental identification. The main sources of identification are the structural form of the model, the tax schedule, participation and unemployment variation, demographic covariates, and parametric assumptions on wage and hours opportunity densities. [reasonable inference for my project] 

# Estimation / empirical strategy

The empirical strategy is maximum-likelihood estimation of the joint labour-supply model for couples. Because exact evaluation of the continuous likelihood is computationally costly, the paper uses the McFadden sampling-of-alternatives procedure. The continuous logit model is approximated by a discrete logit version where the integral in the denominator is replaced by a sum over 70 random points with appropriate weights. The authors report that even 10 random points gave results close to those obtained with 70. 

The deterministic part of utility is specified flexibly in consumption and male and female leisure, allowing demographic interactions with age and children. Opportunity densities are specified separately for hours and wages, with hours densities featuring a full-time peak and wage densities depending on education, experience, and region. Female and male opportunity densities are also allowed to depend on local unemployment and whether the household lives in northern rather than southern/central Italy. Tables II and III report the main parameter estimates. 

# Treatment of preferences

Preferences are modeled explicitly through the deterministic utility component. The systematic utility function depends on household consumption, male leisure, female leisure, age of both spouses, and the number of children below and above age six. The functional form is flexible and non-separable in consumption and leisure because participation indicators enter the consumption term, partly to capture the possibility of non-reported income in the underground economy. 

Preference heterogeneity is present, but mostly through observed covariates and random taste shifters attached to opportunities. The model is not built around ethically meaningful heterogeneity in preferences; it is built to explain behaviour. The paper does not use preferences for welfare evaluation, and it does not ask whether preference differences should be respected or neutralized normatively. 

# Treatment of opportunities / constraints

This is the most important section for your research direction. The paper models opportunities explicitly. Individuals do not choose any hours level freely along a budget line. They choose among available jobs, and the number and characteristics of these jobs may vary across individuals. Jobs are characterized by hours, wages, and non-pecuniary attributes, and opportunity sets may differ because of skills, education, age, and local labour-market conditions. 

The paper therefore does not assume a universal choice set. It also does not reduce opportunities to a single exogenous wage rate. Both hours restrictions and wage opportunities are modeled. This is much closer to a latent job-opportunity framework than to a standard labour-supply model. In your terminology, the paper helps distinguish preference heterogeneity from opportunity heterogeneity on the positive side. [reasonable inference for my project] 

The paper interprets unemployment as relative excess non-participation compared with a benchmark “fair environment” in which market and non-market opportunities are equally numerous. Opportunity scarcity is thus a formal part of the model. The paper also explicitly says that involuntary unemployment or limited labour-market attachment can be understood as too few or too poor market opportunities. 

At the same time, opportunities are not observed set-valued objects. They are inferred through densities and relative counts. So the paper is highly relevant for modelling feasible sets statistically, but it does not yet provide actual observed (A_i) sets in the strong sense of your jobs-and-wellbeing project. 

# Welfare / normative object

The paper is mainly positive with some distributional applications. It reports labour-supply effects, gross and disposable income changes, and Gini coefficients under alternative tax systems, but it does not define individual welfare through a common welfare function and does not aggregate welfare through an explicit social welfare criterion. 

This means the paper is not directly useful for responsibility for opportunities, compensation for opportunities, or reference opportunity sets at the normative level. It is also not a decomposition paper in the sense of decomposing inequality into opportunities and preferences. Its value for those questions is indirect: it provides a model architecture that distinguishes preferences and opportunities behaviourally. [reasonable inference for my project] 

# Main findings

The central empirical finding is that male labour supply is rather inelastic while female labour supply, especially participation, is much more elastic. Table IV reports aggregate uncompensated own-wage elasticities of 0.053 for male unconditional hours and 0.737 for female unconditional hours, with strong negative cross-wage effects that offset much of the own-wage response. When all wages rise by 1%, male unconditional labour supply is nearly unchanged and female labour supply rises only modestly once cross-effects are taken into account. 

A second major finding is that elasticities depend strongly on household income. Table V shows that the largest labour-supply responses are found for women in the poorest households. For the poorest 10% of households, the female uncompensated elasticity of participation with respect to own wage is 2.837, while for the richest 10% it is only 0.031. The paper highlights sharply declining wage elasticities with household income. 

A third finding is that tax reforms produce only modest aggregate labour-supply responses. Table VII shows that replacing the 1987 progressive tax system with a revenue-neutral proportional tax slightly lowers female participation and hours and slightly raises male hours, while a more progressive system slightly lowers both male and female labour supply. Table VIII shows that proportional taxation increases disposable-income inequality by about 4%, whereas increased progression reduces it by about 7.6%. 

# Main limitations

A first limitation is that the opportunity structure is only partially observed and partly imposed parametrically. In particular, the independence of offered hours and wages is assumed, and the distribution of offered hours is modeled as uniform with a full-time peak. The authors themselves state that testing the independence assumption would require better firm-level or institutional information. 

A second limitation is that the model is not used with an explicit welfare metric. Policy evaluation is limited to labour-supply outcomes, income levels, and Gini coefficients. For your project, that means the paper is strong on the positive modelling of (R) and latent (A), but weak on the evaluative side of (W(z,R,A;y)). [reasonable inference for my project] 

A third limitation is the age and sample scope. The paper studies married couples only, excludes most self-employment-heavy households, and uses 1987 Italian data. These restrictions are reasonable for estimation, but they limit the generality of the substantive findings. 

A fourth limitation is that job attributes beyond hours and wages are left largely latent in the random taste shifter. The authors themselves note that richer data on job attributes, firm-specific hours-setting, and institutional information would improve the analysis. 

# Relevance for my JMP

## possible use for framing

This is a very strong paper for framing the empirical side of your project because it explicitly rejects the idea that labour supply should be modeled as unconstrained choice along a budget set. It shows how job opportunities and hours restrictions can be made central.

## possible use for model design

It is highly useful for model design. The paper gives an early operational template for representing job opportunities by distributions over hours and wages, and for estimating joint household decisions under taxes and quantity constraints.

## possible use for identification

It is useful because it contains an explicit identification discussion, including which components are theoretically identifiable and which require parametric assumptions. That is uncommon and valuable.

## possible use for welfare measurement

Directly, it is limited. The paper does not construct an individual welfare measure or social welfare function. Indirectly, it helps by providing the kind of behavioural model that a later welfare analysis could sit on top of.

## possible use for decomposition

Directly, very limited. It does not decompose inequality into preferences and opportunities. Indirectly, it is useful because it already separates the behavioural contribution of preferences from the contribution of opportunity densities.

## possible use for comparative application

It is useful as an Italian benchmark and as an early comparative counterpart to later Norway and Sweden papers by the same authors. It can help you trace how the modelling strategy evolves across countries and applications.

# Research questions this paper inspires

1. Can the opportunity-density objects (g_0) and (g(h,w)) be translated into an explicit feasible-set object (A_i) suitable for normative well-being analysis?

2. How much of the measured female labour-supply elasticity in poor households reflects preferences versus scarce or poor job opportunities?

3. What changes in conclusions would arise if actual observed job characteristics were incorporated instead of leaving most non-pecuniary features in the random taste shifter?

4. Can one build a decomposition in which tax reforms affect welfare through three distinct channels: preferences, opportunity sets, and pay schedules?

5. How should one normatively evaluate labour-market scarcity when unemployment is modeled as deficient access to market opportunities relative to a benchmark “fair environment”?

# Challenge to this paper

The strongest challenge is that the paper’s positive treatment of opportunity is ahead of its normative treatment. It develops a powerful way of modeling scarce and heterogeneous job opportunities, but it does not tell us how those opportunity differences should count in welfare assessment. From your perspective, this leaves open the key ethical question even while the behavioural architecture is already highly relevant. 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper clearly separates realized labour-supply outcomes from the opportunity side of the problem. Households choose among jobs, and the opportunity set varies across households through the relative abundance and characteristics of available jobs. Choices therefore depend on both preferences and opportunities. 

[reasonable inference for my project] A natural mapping into your notation is the following. The realized bundle (z) corresponds to the chosen income–hours job bundle. Preferences (R) correspond to the deterministic utility component (v_i(C,h)) together with the stochastic taste shifters. The feasible set (A) is not directly observed, but it is represented statistically by (g_0), (g(h,w)), and their couple analogues. The pay schedule (y) is partly the wage distribution across jobs and partly the tax function (f) that maps gross income into disposable income. 

[unclear from paper] The paper does not define individual well-being as (W(z,R,A;y)), does not analyze independence of (A), independence of (y), IIJ, IPIJ, or responsibility for opportunities. It also does not distinguish actual from reference opportunity sets in a normative sense. 

[reasonable inference for my project] In your taxonomy, this paper is close to the theme of opportunity heterogeneity and explicitly not close to independence of (A). If anything, it insists that (A)-type variation matters for observed behaviour. It is also not close to laissez-faire or responsibility-sensitive evaluation, because it remains mainly a positive econometric paper. 

# Relation to Bargain et al. (2013)

[not central]

# Relation to opportunities vs preferences

This paper is highly relevant to the opportunities-versus-preferences distinction on the positive side. It does not collapse all observed heterogeneity into preferences. Instead, it explicitly models labour-supply outcomes as the result of both utility differences and differences in the opportunity set, including hours restrictions and job availability. 

But it does not turn that distinction into a normative theory. It does not ask which inequalities are due to bad opportunities and should therefore be compensated, nor whether preferences over infeasible jobs should be ignored. So it is best read as an empirical precursor to your framework rather than as a direct answer to the ethical problem. 

# Useful quotations / formulas

A central formula is the labour-supply density for singles:
[
\varphi_i(h,w)=\frac{\Psi_i(h,w)g_{0i}g_i(h,w)}{\Psi_i(0,0)+g_{0i}\sum_x\sum_y \Psi_i(x,y)g_i(x,y)},
]
for ((h,w)>0). This is the paper’s clearest formal statement that observed choices depend jointly on deterministic utility and available opportunities. 

The couple analogue is:
[
\varphi(h_F,h_M,w_F,w_M)=\frac{\Psi(h_F,h_M,w_F,w_M)g_0,g(h_F,h_M,w_F,w_M)}{D},
]
with (D) integrating over joint opportunities for both spouses. This is central because it puts joint household decisions and opportunity constraints in one formal structure. 

The paper’s theoretical unemployment interpretation is also important:
[
p=(1-g_0),\tilde{\varphi}(0,0),
]
linking unemployment to deficient access to market opportunities relative to a benchmark “fair environment.” 

# Suggested tags

structural-labour-supply, Italy, joint-household-decisions, quantity-constraints, random-opportunities, hours-restrictions, tax-simulation, opportunity-sets, Aaberge-Colombino-Strom

# My quick takeaway

This is one of the most important early empirical papers for your corpus. It does not provide a normative well-being theory, but it does something you need before that: it formalizes labour supply as choice from heterogeneous and constrained job opportunities rather than as free hours choice on a budget line. For your JMP, it is especially valuable as an empirical ancestor of RURO-style thinking and as a concrete example of how opportunity heterogeneity can be modeled separately from preferences.
