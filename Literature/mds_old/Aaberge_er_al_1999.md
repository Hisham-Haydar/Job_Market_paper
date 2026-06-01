---

title: "Labour Supply in Italy: An Empirical Analysis of Joint Household Decisions, with Taxes and Quantity Constraints"
authors: ["Rolf Aaberge", "Ugo Colombino", "Steinar Strøm"]
year: 1999
outlet: "Journal of Applied Econometrics"
country_or_context: "Italy"
population: "Married couples in Italy; households with self-employment income above 20% of gross household income excluded"
data_period: "1987 Survey of Household Income and Wealth (SHIW); policy simulations based on the 1987 Italian tax-benefit system"
shelf: "italy_joint_household_quantity_constraints"
tags: ["labour supply", "joint household decisions", "quantity constraints", "tax-benefit system", "random opportunities", "Italy", "married couples", "wage elasticities", "opportunity sets", "microsimulation"]
priority: "high"
read_status: "extracted"
------------------------

# Full citation

Aaberge, Rolf, Ugo Colombino, and Steinar Strøm. 1999. “Labour Supply in Italy: An Empirical Analysis of Joint Household Decisions, with Taxes and Quantity Constraints.” *Journal of Applied Econometrics* 14(4): 403–422. 

# One-sentence contribution

The paper estimates, on nationwide Italian microdata, a joint household labour supply model with exact tax rules and explicit quantity constraints on jobs/hours, and shows that male labour supply is inelastic, female labour supply is much more elastic—especially among poor households—and that replacing the 1987 tax system with a proportional tax yields only modest aggregate labour-supply effects. 

# Why this paper matters

This paper matters because it is one of the early structural labour-supply studies that treats the feasible set as constrained rather than assuming households freely choose any hours point on the budget set. It explicitly criticizes the standard Hausman approach for presuming excessive flexibility of work schedules and instead models jobs as offers with fixed hours, wages, and non-pecuniary attributes. 

For your JMP, the paper is especially important because it is directly about the distinction between preferences and opportunities. It allows opportunity sets to vary across individuals, introduces random opportunity sets and quantity constraints, estimates joint spousal decisions, and embeds the actual tax-benefit system exactly. This makes it a strong precursor to later RURO-style and opportunity-sensitive labour supply work. 

# Core research question

How do taxes affect labour supply and the distribution of income in Italy when married couples make joint labour-supply decisions in an environment with exact tax rules, hours restrictions, and heterogeneous opportunity sets? 

# Economic setting and context

The setting is Italy under the 1987 tax-benefit system. The paper uses the 1987 Survey of Household Income and Wealth and studies married couples, excluding households with substantial self-employment income because their decision problem is viewed as different and because hours for the self-employed are not observed. The institutional environment includes exact individual income-tax rules, tax credits, and family benefits. 

A key institutional point is that the Italian system is based on individual taxation of spouses, with detailed tax brackets, credits for dependent workers and family members, and means-related family benefits. The authors stress that earlier Italian labour-supply studies either used local samples, ignored taxes, or approximated the budget set more crudely; this paper is presented as the first Italian model that simultaneously handles both spouses’ choices, exact income taxes, and constraints on the distribution of hours using nationwide microdata. 

# Model / theoretical framework

The model is a static structural labour supply model with random utility and random opportunity sets, estimated for married couples. Individuals do not choose a continuous hours point freely; rather, they choose among market and non-market opportunities. Each job is characterized by fixed hours, a wage rate, and other non-pecuniary attributes. The budget constraint maps gross income into disposable income through the exact tax-benefit system. 

For a one-person household, the opportunity set is (B_i(h,w)) for jobs with hours (h) and wage (w), together with (B_i(0,0)) for non-market opportunities. Utility has the form
[
U_i(C,h,j)=v_i(C,h)\varepsilon_{ij},
]
with (\varepsilon_{ij}) capturing unobserved job-specific attributes known to the household but not the econometrician. The corresponding choice probabilities depend both on the structural utility term and on the distribution of feasible opportunities. 

The married-couple extension is joint: spouses’ hours and wages are chosen simultaneously, and the opportunity structure contains separate male and female margins plus joint terms. The framework is purely positive in the paper’s main objective; there is no explicit welfare metric such as equivalent income or a social welfare function. Policy analysis is performed through simulated labour supply and income distributions under alternative tax systems. 

# Key objects

The main structural objects are the deterministic utility component (v(C,h_F,h_M)), random taste shifters over job opportunities, the opportunity densities (g), and the market-opportunity parameters (g_{0F}) and (g_{0M}). These objects jointly determine observed participation, hours, and earnings choices. 

A second key object is the joint opportunity density over hours and wages. The model factorizes job opportunities into wage and hours components and specifies the hours opportunity density as uniform with a peak at full-time hours. For married couples, the joint choice probability depends on both spouses’ opportunities, allowing simultaneous household decisions under quantity constraints. 

The main outcome objects are participation rates, hours conditional on participation, unconditional hours, own-wage and cross-wage elasticities, gross earnings, gross household income, disposable income, and the Gini coefficient under counterfactual tax systems. 

# Data

The data come from the 1987 Survey of Household Income and Wealth (SHIW) conducted by the Bank of Italy. The authors use this survey because it was the first available nationwide dataset with both hours of work and income information at the individual level, allowing the construction of hourly wage rates and exact budget constraints. 

The estimation sample includes 2,953 married-couple households. Couples are retained if spouses are aged 20–68. Households with self-employment income above 20% of gross household income are excluded; for included households, any observed self-employment income is added to net household income and treated as exogenous. Sample means reported in Table I on page 10 show male participation at 96%, female participation at 40%, male annual hours at 1,995, female annual hours at 690, gross annual household income at 37,500 thousand lire, and disposable income at 27,900 thousand lire. 

The main variables are spouses’ hours, wages, gross earnings, disposable income, age, education, experience, region, local unemployment rates, and number of children below and above age six. Exact tax brackets, credits, and family benefits are coded into the budget constraint. 

# Identification logic

Identification is structural and partly parametric. The model’s choice probabilities depend on both the deterministic utility term and the opportunity densities, so separating preferences from opportunities is a central identification problem. The paper shows that identifying the preference term and the opportunity densities nonparametrically requires additional assumptions, especially on the distribution of offered hours. 

In the theory section, the paper argues that when the deterministic utility is separable in income and leisure, variation in fixed work costs can identify the income component (v_1(\cdot)) nonparametrically. But to separate the leisure term from the hours opportunity density, additional parametric restrictions are needed. Empirically, the authors impose a uniform-with-full-time-peak specification for hours opportunities and lognormal wage opportunity densities. 

Opportunity access is further parameterized using regional indicators and local gender-specific unemployment rates in (g_{0F}) and (g_{0M}). These do not come from the abstract model itself; the paper explicitly treats them as empirical instruments or proxies for demand-side conditions. This is important for your agenda because the paper is not just fitting preferences; it is also using labour-market environment variables to identify constraints on available opportunities. 

# Estimation / empirical strategy

The empirical strategy is simultaneous estimation of utility and opportunity-density parameters using a McFadden sampling-of-alternatives method. The continuous model is approximated by a discrete logit version in which the denominator of the likelihood is replaced by a sum over 70 random points in (\mathbb{R}^4). The authors state that this delivers results close to full-information maximum likelihood and found the procedure computationally efficient. 

The deterministic utility function is specified flexibly in household consumption and male and female leisure, with participation indicators, ages, and children entering the parameters. Opportunity densities are specified separately for hours and wages, with hours concentrated around full-time work and market-opportunity access depending on region and local unemployment. Wage offers are modeled as lognormal functions of schooling, experience, and region. 

Policy simulations then redraw opportunity points and random shocks, solve the household’s discrete choice problem under alternative tax systems, and compute mean labour supply, income, taxes, and inequality measures. The simulations are conducted under the assumption that opportunity densities remain fixed across tax reforms. 

# Treatment of preferences

Preferences are heterogeneous through both observed and unobserved components. The utility function differs by spouses’ leisure, ages, children, and participation status, and the random taste shifters capture unobserved job-specific utility components. This means the model does not interpret all heterogeneity as coming from opportunity sets alone. 

The paper is explicit that households have preferences over income, hours, and non-pecuniary job attributes, not merely over a continuous consumption-leisure bundle. In that sense, the preference domain is already richer than in standard labour-supply models. Still, the welfare use of preferences remains positive/behavioral; the paper does not construct a preference-respecting welfare comparison across households. 

# Treatment of opportunities / constraints

This is the paper’s most important section for your research agenda.

The paper models opportunities explicitly. Individuals and couples choose from sets of market and non-market opportunities, not from a frictionless continuous hours budget set. Jobs carry fixed hours and wages, and the opportunity sets may vary across individuals because of differences in skills, education, age, region, and labour-market conditions. 

The authors emphasize that the standard Hausman approach effectively assumes individuals can choose their optimum anywhere along the budget set, whereas in reality firms offer only a restricted set of contracts and hours schedules. Their model directly addresses this by specifying distributions of offered hours and wages. In empirical implementation, hours opportunities are uniform with a full-time peak; market access depends on region and local unemployment. 

This is not yet a full latent-jobs model with a rich vector of observed job characteristics, occupations, or explicit labour demand. The opportunity side is still relatively stylized. But the paper clearly treats opportunities as first-class structural objects and does not bury them inside preferences or measurement error. That makes it highly relevant for the opportunities-versus-preferences distinction. 

# Welfare / normative object

The paper does not construct an explicit welfare metric such as equivalent variation, money-metric utility, or a social welfare function. It is a positive labour-supply and tax-simulation paper focused on behavioural responses and income distributions under alternative tax regimes. 

Its policy evaluation is therefore indirect. The paper assesses tax systems through participation, hours, earnings, disposable income, and the Gini coefficient. It does not provide an explicit normative ranking of households based on welfare. Relative to your agenda, this is a limitation: the paper is strong on opportunities and labour supply, but weak on welfare measurement proper. 

# Main findings

First, male labour supply is rather inelastic, whereas female labour supply—especially participation—is much more elastic. Table IV on page 15 reports aggregate uncompensated female participation own-wage elasticity at 0.654 and aggregate uncompensated female unconditional-hours elasticity at 0.737, versus 0.046 and 0.053 for males. 

Second, cross-wage effects are strong and partly offset own-wage effects. The paper explicitly states that if all wages increase by 1%, men’s unconditional labour supply is almost unchanged and women’s increases only modestly. This is a central substantive result because it helps explain the weak aggregate effects of tax reforms. 

Third, wage elasticities decline sharply with household income. Table V on page 16 shows very large female own-wage elasticities among the poorest households—for example, an uncompensated participation elasticity of 2.837 and an uncompensated unconditional-hours elasticity of 3.441—while responses are close to zero among rich households. 

Fourth, replacing the 1987 tax system with a revenue-neutral proportional tax produces only modest aggregate labour-supply responses. Table VII on page 18 shows female participation falling slightly from 0.40 to 0.38, male participation remaining at 0.96, and only minor changes in annual hours and gross income. 

Fifth, a shift to proportional taxation increases after-tax inequality. Table VIII on page 19 shows disposable-income Gini rising from 0.238 under the 1987 rules to 0.247 under proportional taxation, while a more progressive counterfactual lowers it to 0.220. 

Sixth, stronger progression has only weak negative aggregate labour-supply effects, again because strong cross-effects and small own-wage responses among middle- and high-income households dominate the aggregate picture. 

# Main limitations

A first limitation is the maintained independence of offered hours and offered wages. The authors explicitly recognize this as a simplification and suggest that richer firm-level data would be needed to test or relax it. 

A second limitation is that the opportunity structure is stylized. Jobs are described mainly by hours, wages, and unobserved non-pecuniary attributes; richer observed job characteristics are not included. The conclusion section explicitly notes the need for more job attributes in future work. 

A third limitation is that policy simulations keep opportunity densities fixed. This means tax reforms affect choices holding the distribution of offered jobs constant. If labour demand or job availability respond to policy, the simulations miss that margin. 

A fourth limitation, relative to your research interests, is the absence of an explicit welfare metric. The paper can say much about behaviour and income inequality, but not directly about well-being once heterogeneous preferences and opportunities are taken seriously. 

# Relevance for my JMP

## possible use for framing

This paper is very useful for framing an argument that structural labour supply should be modeled as constrained job choice, not as unconstrained choice of hours along a budget line. It gives you a clear historical precedent for opportunity-sensitive labor-supply modelling. 

## possible use for model design

It is highly relevant for model design because it handles joint household decisions, exact tax rules, and quantity constraints simultaneously. If your project aims to build a richer job-opportunity or RURO-style model, this paper is a natural methodological ancestor. 

## possible use for identification

The paper is useful for identification because it shows that preference and opportunity components cannot be disentangled without additional structure, and that empirical proxies for labour-demand conditions can be embedded in the opportunity side. That is directly relevant to your plan to separate preferences from opportunities more rigorously. 

## possible use for welfare measurement

Indirectly, the paper is useful because it shows that behavioral tax-simulation results can be modest even in the presence of strong heterogeneity. But it also highlights a gap: without a welfare object, one cannot say much about the normative ranking of tax systems beyond income inequality and labour supply. 

## possible use for cross-country comparison

The paper is not cross-country, but it is valuable for comparison with Norway- and Sweden-based work by the same authors. It suggests that country differences in tax effects may reflect not just tax schedules and preferences, but also opportunity structures, cross-effects within households, and the income distribution of elasticities. 

# Research questions this paper inspires

How much of the cross-country difference in labour supply elasticities is due to differences in opportunity densities rather than preferences?

Would a richer latent-job model with observed occupation and job-quality characteristics overturn the paper’s conclusion that proportional taxation has only modest aggregate labour-supply effects in Italy?

How would welfare rankings of alternative tax systems change if this opportunity-sensitive behavioural model were combined with a preference-sensitive welfare metric?

Do strong spousal cross-effects remain as large once the opportunity side is modeled with richer labour-demand structure and endogenous job creation? 

# Challenge to this paper

The strongest simplification is that the paper moves decisively beyond free-hours choice but still keeps the opportunity side fairly reduced-form and fixed under policy change. That is enough to show that opportunities matter, but not enough to identify how the labour market would reallocate jobs when taxes change. A future paper could challenge this by endogenizing opportunity sets or estimating a richer latent-job distribution with observed job characteristics. 

# Relation to Bargain et al. (2013)

This paper is methodologically upstream of Bargain et al. (2013). Bargain et al. uses a structural labour-supply model to derive welfare rankings under heterogeneous preferences, but does not treat opportunities as explicitly as Aaberge, Colombino, and Strøm do here. Relative to Bargain et al. (2013), this paper is stronger on quantity constraints and opportunity sets, but weaker on explicit welfare evaluation and preference-sensitive normative comparison. 

# Relation to opportunities vs preferences

This paper clearly helps separate preferences from opportunities. Preferences enter through the utility function and random taste shifters, while opportunities enter through the distribution of feasible jobs and market-access parameters. The paper’s entire motivation is that free choice along the budget set is unrealistic because the available contracts themselves are constrained. For your agenda, it is one of the more directly useful papers in showing how opportunity heterogeneity can be modeled structurally rather than absorbed into tastes. 

# Useful quotations / formulas

The core one-person choice probability is
[
\varphi(h,w)=
\frac{\Psi(h,w)g_0g(h,w)}
{\Psi(0,0)+g_0\sum_{x>0}\sum_{y>0}\Psi(x,y)g(x,y)},
]
which makes behavior depend jointly on utility and on the density of feasible opportunities. This is the most important formula in the paper for your research direction. 

The unemployment interpretation is also useful:
[
p=(1-g_0),\hat\varphi(0,0),
]
so unemployment can be linked to too few market opportunities relative to a benchmark “fair environment.” This is a concise formalization of how opportunity scarcity enters the model. 

For married couples, the joint choice density depends on both spouses’ opportunity densities and joint job opportunities, which is why the model can generate substantial cross-wage effects. 

# Suggested tags

#labour_supply #joint_household_decisions #quantity_constraints #opportunity_sets #Italy #tax_benefit #random_utility #cross_wage_effects #married_couples #structural_model

# My quick takeaway

If I only remember one thing from this paper for my JMP, what should it be? That once labour supply is modeled as constrained joint choice over offered jobs rather than free hours choice, aggregate tax responses can look surprisingly small even when some groups—especially poor married women—are individually very elastic, because opportunity constraints and strong spousal cross-effects reshape the aggregate result. 
