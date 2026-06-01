---

title: "Empirical Optimal Income Taxation: A Microeconometric Application to Norway"
authors: ["Rolf Aaberge", "Ugo Colombino"]
year: 2011
outlet: "ChilD Working Paper No. 16/2011"
country_or_context: "Norway"
population: "Single females, single males, and married/cohabiting couples; individuals aged 20–62; self-employed and permanent disability recipients excluded"
data_period: "1994 estimation data; 2001 used for out-of-sample prediction"
shelf: "optimal_taxation_structural_labour_supply"
tags: ["optimal taxation", "structural labour supply", "random utility", "microsimulation", "latent opportunities", "quantity constraints", "interpersonal comparability", "Norway"]
priority: "very high"
read_status: "extracted"
------------------------

# Full citation

Aaberge, Rolf, and Ugo Colombino. 2011. *Empirical Optimal Income Taxation: A Microeconometric Application to Norway*. ChilD Working Paper No. 16/2011. 

# One-sentence contribution

The paper uses a structural random-utility labour-supply model with heterogeneous preferences and heterogeneous job opportunities to compute optimal income-tax schedules for Norway directly by simulation, rather than by plugging empirical elasticities into analytical optimal-tax formulas. 

# Why this paper matters

This paper matters because it is very close to the kind of bridge your project needs between positive labour-supply modelling and normative welfare evaluation. The authors explicitly reject the standard approach of taking analytical optimal-tax formulas and calibrating them with external estimates, and instead use the estimated microeconometric model itself as the computational engine for tax design. That gives the paper a high level of internal consistency between behavioural assumptions and policy simulation. 

It also matters because the paper models job opportunities explicitly through an opportunity density (p(h,w,s)), so the choice environment is not reduced to a universal hours grid with one exogenous wage per worker. At the same time, it separates behavioural utility from the welfare function used by the social planner, which is directly relevant for your own concern with the distinction between actual preferences and normative well-being measurement. 

# Core research question

How can one identify empirically optimal income-tax rules, under alternative inequality-averse social welfare criteria and a fixed public-budget constraint, by using a flexible microeconometric model of household labour supply that allows heterogeneous preferences and heterogeneous job opportunities? 

# Economic setting and context

The setting is Norway. The model is estimated on detailed Norwegian household data for 1994, and the behavioural sample includes 1,842 couples, 309 single females, and 312 single males. The out-of-sample validation uses 2001 outcomes predicted from the model estimated on 1994 data. The policy problem is the design of personal income taxation while keeping total net tax revenue fixed and leaving the main 1994 transfer structure unchanged. Tables 4.3 and 5.1 are central for the tax-rule comparison, while Tables 3.4 and 3.5 report the within-sample and out-of-sample prediction exercises. 

# Model / theoretical framework

The model is a structural random-utility labour-supply model that extends the standard multinomial logit framework. For a single household, the agent chooses among jobs characterized by wage (w), hours (h), observed job characteristics (s), and unobserved match characteristics (j), subject to the budget constraint (c=f(wh,I)), where (I) is exogenous non-labour income and (f) is the tax rule. The feasible environment is denoted (B), the set of available opportunities, including non-market opportunities with (w=0) and (h=0). The model is positive at the behavioural level and normative at the tax-design level. 

A central feature is that the feasible set is not treated as identical across individuals. Instead, because the analyst does not observe the entire opportunity set (B), the paper represents it through a probability density (p(h,w,s)) over available jobs. This allows the number and characteristics of available jobs to differ across agents, including differences in offered hours, wages, and sector. The paper is explicit that the model can accommodate quantity constraints and involuntary unemployment in the sense that some agents may face very poor or empty market-opportunity sets. 

For couples, the model allows joint labour-supply decisions and spouse interaction. The paper also stresses that exact tax rules can be inserted directly into the model, so there is no need to simplify non-convex budget sets into differentiable textbook objects. That is important for tax simulation but also for any later attempt to map the framework into a richer (W(z,R,A;y))-style setting. 

# Key objects

The main positive objects are the household-specific utility function (U), its systematic part (v), the random component (\varepsilon), the opportunity density (p(h,w,s)), the tax rule (f), and the realised choice ((c,h,s,j)). The choice density is proportional to the systematic attractiveness of a job times its availability, which is the key formal device used to integrate preferences and opportunities in the econometric model. 

The main welfare objects are the common individual welfare function (V(y,h)), where (y) is equivalent after-tax income and (h) maps into leisure, and the rank-dependent social welfare functions (W_i), which differ by their degree of inequality aversion. The policy object is a 9-parameter piecewise-linear tax rule with exemption level, four marginal tax rates, three kink points, and a lump-sum transfer or tax. Table 5.1 reports the resulting optimal parameters. 

# Data

The data come from the 1995 Norwegian Survey of Level of Living, with detailed income information from tax records. The estimation sample is restricted to individuals aged 20 to 62. Self-employed individuals and those receiving permanent disability benefits are excluded. The sample contains 1,842 couples, 309 single females, and 312 single males. Table 2.1 on page 14 reports participation, hours, gross income, taxes, and disposable income by family type and income decile. 

The paper also performs an out-of-sample prediction exercise using the 2002 Norwegian Survey of Level of Living to predict choices under the 2001 tax regime. Tables 3.4 and 3.5 on page 24 compare observed and predicted decile incomes for 1994 and 2001 respectively. 

# Identification logic

Identification is structural and mainly parametric. The model is estimated by maximum likelihood from the choice densities implied by the random-utility specification and the opportunity densities. The crucial identifying assumptions are the Type III extreme-value distribution for the stochastic component, the parametric specification of preferences, the parametric wage-offer distributions, and the parametric opportunity densities for jobs, hours, and sectors. There is no quasi-experimental source of identification. [reasonable inference for my project] 

The paper’s identification strategy therefore does not separately observe true feasible sets or directly observe effort. It infers opportunity structure statistically through (p(h,w,s)), and it infers behavioural responses from the fitted structural model. This is strong on internal coherence and weak on design-based identification. [reasonable inference for my project] 

The paper partly addresses external validity by showing that the estimated model predicts the 2001 disposable-income distribution rather well. That is not a formal identification result, but it is an important credibility check for the simulation exercise the paper ultimately performs. 

# Estimation / empirical strategy

The empirical strategy is to estimate a microeconometric labour-supply model with 78 parameters capturing heterogeneity in preferences and opportunities. The paper estimates separate preference structures for single females, single males, and couples, while allowing the opportunity densities to differ by gender and sector. In practice, the continuous opportunity set is approximated by a sampled set of alternatives following the McFadden procedure; each household’s observed choice is combined with 199 sampled alternatives, and the resulting discrete approximation is used for estimation. 

After estimation, the authors compute wage and non-labour-income elasticities by stochastic simulation. They then solve the optimal-tax problem by iterating over a class of 9-parameter tax schedules. For each candidate tax rule, they simulate household choices, convert household income into equivalent individual income, evaluate each individual using the common welfare function, aggregate with a rank-dependent social welfare function, and search for the tax rule that maximizes social welfare subject to constant total tax revenue. The paper states that each optimization requires the evaluation of approximately 200,000 tax-transfer rules. 

# Treatment of preferences

Preferences are explicitly heterogeneous in the behavioural model. The paper allows observed and unobserved heterogeneity in tastes, different preference structures across singles and couples, and spouse interaction in the couple utility function. The functional form is flexible enough to generate backward-bending labour supply, and the paper explicitly interprets some weakly negative wage responses in the middle of the single-person income distribution as cases where income effects dominate substitution effects. Tables 2.3 and 2.4 report the preference parameter estimates, and Table 3.1 reports the resulting heterogeneity in wage elasticities. 

However, the paper is equally explicit that these estimated utility functions are not suitable as interpersonally comparable welfare functions. The social planner therefore does not use the behavioural utility functions directly for welfare evaluation. Instead, a separate common individual welfare function is imposed. This separation between behavioural preferences and normative evaluation is one of the paper’s most important conceptual moves. 

# Treatment of opportunities / constraints

This is one of the paper’s strongest contributions for your purposes. The paper models opportunities explicitly, though not as directly observed individual feasible sets. The opportunity set (B) is represented through a probability density (p(h,w,s)), and the choice probability is proportional to utility attractiveness times availability. This means that labour-supply behaviour depends not only on tastes and the budget set but also on the statistical distribution of available jobs. The paper is explicit that the number and characteristics of opportunities may differ across individuals and that the framework is compatible with quantity constraints and involuntary unemployment. 

The paper therefore does not assume a universal identical choice set. Nor does it restrict the agent to choosing only hours while wage is fixed at the individual level. Jobs differ by wage, hours, and sector, and households may respond to tax changes by moving to jobs with different hours, wages, and non-pecuniary characteristics. That is much closer to latent-jobs or RURO-style logic than standard hours-choice labour-supply models. [reasonable inference for my project] 

At the same time, the paper does not explicitly construct individual feasible sets (A_i) in a set-theoretic sense. Opportunity heterogeneity is latent and statistical. The paper helps distinguish both preference heterogeneity and opportunity heterogeneity on the positive side, but it does not produce a direct normative treatment of actual feasible sets as such. It also does not use reference opportunity sets. 

# Welfare / normative object

The paper is positive with explicit welfare applications. The normative object is a common individual welfare function
[
V(y,h)=\left(\frac{y^{\gamma_1}-1}{\gamma_1}\right)+\left(\frac{L^{\gamma_3}-1}{\gamma_3}\right),
]
where (y) is equivalent after-tax income and (L) is leisure. For singles, (y) is disposable income; for married or cohabiting individuals, household disposable income is divided by (\sqrt{2}). The function is used only for welfare evaluation, not for simulating behaviour. Table 4.1 on pages 26–27 reports the parameter estimates. 

The social planner then aggregates these individual welfare levels using rank-dependent social welfare functions (W_i), with different values of (i) corresponding to different inequality-aversion profiles. The paper interprets these welfare criteria in terms of equally distributed equivalent welfare and discusses the Bonferroni, Gini, and utilitarian cases. Table 4.2 on page 29 reports the weight profiles. 

The paper is explicitly normative in that it adopts a planner’s welfare metric and inequality-averse aggregation rule. It is not a responsibility-versus-compensation paper in the strong Roemer/Fleurbaey-Maniquet sense. It does not explicitly ask whether inequality due to opportunities should be compensated while inequality due to effort should be treated as legitimate. Nor does it construct a reference opportunity set. So it is useful for welfare measurement and interpersonal comparability, but not for a direct theory of responsibility for opportunities. 

On decomposition, the paper does not provide a decomposition of inequality into preferences, opportunities, pay schedules, and other factors. It is not a decomposition paper in your intended sense. Its value lies instead in the architecture needed before such a decomposition could be attempted. 

# Main findings

The main substantive finding is that all optimal tax schedules are progressive, with monotonically increasing marginal tax rates. Compared to the 1994 Norwegian tax system, the optimal rules imply a lower average tax rate, lower marginal rates on low and average incomes, and higher marginal rates on sufficiently high incomes. Under the constraint imposed in the paper, the top optimal marginal tax rate is 75 percent above roughly 700,000 NOK and applies to only about 1.8 percent of taxpayers. Table 5.1 on page 33 contains the main optimal-tax results. 

The behavioural mechanism is that labour-supply elasticities decline sharply with income, and married women in particular are much more elastic than married men. Table 3.1 on pages 20–21 and the discussion on page 21 emphasize that low-income households are much more responsive than high-income households. This pattern helps explain why the model generates low marginal tax rates at the bottom and middle and higher rates at the top. 

The paper also finds that all optimal tax rules would generate a strong majority of winners relative to the 1994 system. Table 5.5 on page 39 reports winner shares by gender, family type, and decile. Singles women in the top two deciles are the main group that would not support the optimal rules, because the actual 1994 system contained child-related deductions that are removed in the optimized class of tax schedules. 

Finally, the out-of-sample prediction exercise is quite successful. On page 24, Table 3.5 shows that the model reproduces the 2001 income distribution reasonably closely across couples, single females, and single males. This materially strengthens the empirical credibility of the simulation approach. 

# Main limitations

The first limitation is identification. The model is behaviourally rich, but identification is structural and parametric rather than quasi-experimental. The paper does not separately identify preferences and opportunities in a nonparametric or institutionally grounded causal sense. [reasonable inference for my project] 

The second limitation is the treatment of opportunities. The paper explicitly models opportunity heterogeneity, which is an important strength, but only through a latent density (p(h,w,s)). It does not observe or normatively evaluate actual feasible job sets. Therefore it is highly relevant to your project as an empirical precursor, but it cannot be directly imported into a rigorous (W(z,R,A;y)) framework without additional conceptual work. [reasonable inference for my project] 

The third limitation concerns welfare interpretation. The common welfare function solves the interpersonal-comparability problem operationally, but it is imposed rather than axiomatized in a responsibility-sensitive framework. The paper therefore sidesteps, rather than solves, deeper normative questions about what should count as compensated disadvantage and what should count as legitimate heterogeneity. 

The fourth limitation is that the paper does not fully capture broader taxable-income responses. The authors explicitly note that households may respond through dimensions other than hours, such as wage, job quality, and other characteristics, but the model is not fully consistent with the broader “effort-taxable income” approach. This matters especially for top-bracket taxation. 

The fifth limitation is that the paper does not provide a decomposition of welfare inequality into opportunities, preferences, and pay schedules. For your decomposition agenda, it is therefore a model-architecture paper rather than a direct solution. 

# Relevance for my JMP

## possible use for framing

This paper is highly useful for framing the empirical side of a jobs-and-wellbeing project. It shows that one can build a structural model where realized choices are generated by heterogeneous preferences and heterogeneous opportunities, and then impose a separate normative welfare criterion for policy evaluation. That positive/normative split is directly relevant for your project.

## possible use for model design

It is especially useful for model design because it does not collapse labour supply into a choice over hours at a fixed wage. Instead, it treats jobs as multidimensional packages and represents job availability statistically. That is conceptually close to the latent-jobs and RURO direction.

## possible use for identification

It is useful mainly as a template for internally consistent structural identification and counterfactual policy simulation. It is less useful if your main concern is design-based identification of the separate causal effect of preferences or opportunities.

## possible use for welfare measurement

It is very useful here. The paper explicitly refuses to aggregate heterogeneous behavioural utilities as if they were comparable and instead introduces a common welfare function. That is directly relevant to your own attempt to distinguish welfare measurement from revealed preference.

## possible use for decomposition

Directly, it offers little. It does not decompose inequality into opportunity and preference components. Indirectly, it suggests a path: estimate behaviour with latent opportunity densities, impose a separate welfare metric, and then compare counterfactual distributions under alternative normalizations.

## possible use for comparative application

The paper itself is Norway-specific, but the authors explicitly note that similar exercises across many economies could eventually reveal broader regularities linking economic fundamentals to optimal tax rules. So the architecture is portable even if the results are country-specific.

# Research questions this paper inspires

1. Can the latent opportunity density (p(h,w,s)) be translated into an explicit feasible-set object (A_i) that is normatively interpretable in an individual well-being measure (W(z,R,A;y))?

2. How can one separate preference heterogeneity from opportunity heterogeneity in a structural labour-supply model strongly enough to support a decomposition of welfare inequality?

3. If a planner uses a common welfare function instead of behavioural utilities, what axioms would justify that welfare metric in a jobs-and-wellbeing framework?

4. How sensitive are optimal-tax results to the representation of the top-end opportunity set once broader taxable-income responses, mobility, and job-search margins are introduced?

# Challenge to this paper

The main challenge is conceptual. The paper is excellent at combining behavioural richness with policy computation, but its normative move is relatively ad hoc: once heterogeneous preferences make interpersonal comparison difficult, it introduces a common welfare function. That is operationally sensible, but it is not yet a full theory of why that common function is the right ethical object for evaluating people with different opportunities and different preferences. 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper models realized labour-market outcomes as the result of heterogeneous preferences and heterogeneous opportunities, and it uses a separate common welfare function for normative evaluation. It therefore already contains a separation between behaviour-generating utility and welfare-measuring utility. 

[reasonable inference for my project] A natural translation into your notation is that (z) corresponds to the realized post-tax bundle, mainly disposable income plus hours/leisure and job characteristics; (R) corresponds to the heterogeneous behavioural preferences; (A) corresponds not to an observed feasible set but to a latent opportunity structure represented by (p(h,w,s)); and (y) corresponds partly to wage offers embodied in jobs and partly to the tax mapping from gross to net income. This is not the paper’s own notation, but it is a reasonable way to map it into your framework. 

[unclear from paper] The paper does not define individual well-being as (W(z,R,A;y)), does not analyze axioms such as independence of (A), independence of (y), or responsibility for preferred jobs, and does not construct a reference opportunity set. It also does not directly address whether one should hold persons responsible for some components of (A) or only for effort conditional on (A). 

[reasonable inference for my project] In your taxonomy, this paper is closest to the themes of decomposition of welfare-relevant heterogeneity, reference-based welfare evaluation, and empirical modelling of opportunity heterogeneity. It is not close to independence of (A); if anything, it assumes opportunity variation is behaviourally central. It is not close to independence of (y) either. It is also not laissez-faire in the evaluative sense, because actual preferences generate choices but a separate common welfare metric generates normative assessment. 

# Relation to Bargain et al. (2013)

[not central]

# Relation to opportunities vs preferences

This paper is very useful on the positive side of the opportunities-versus-preferences distinction. It does not simply treat all heterogeneity as taste heterogeneity. Instead, it explicitly allows heterogeneity in both behavioural preferences and job opportunities, and it makes opportunity availability enter the choice density directly. 

On the normative side, however, it does not develop a full fairness theory separating what should be compensated from what should be respected. It solves interpersonal comparability through a common welfare function, but it does not turn the opportunities-versus-preferences distinction into a full individual well-being theory. So its main usefulness for your project is structural and architectural rather than axiomatic. 

# Useful quotations / formulas

A central behavioural formula is the choice density
[
\phi(h,w,s)=
\frac{v(f(wh,I),h,s),p(h,w,s)}
{\iiint_B v(f(xy,I),y,z),p(x,y,z),dx,dy,dz},
]
because it makes clear that observed choices reflect both utility attractiveness and availability of opportunities. 

A central welfare formula is the common individual welfare function
[
V(y,h)=
\left(\frac{y^{\gamma_1}-1}{\gamma_1}\right)
+
\left(\frac{L^{\gamma_3}-1}{\gamma_3}\right),
]
used only for social evaluation and not for behavioural simulation. 

A central policy object is the 9-parameter piecewise-linear tax rule with exemption level (E), marginal rates ((\tau_1,\tau_2,\tau_3,\tau_4)), bracket cutoffs ((Z_1,Z_2,Z_3)), and lump-sum term (T). Table 5.1 on page 33 gives the optimized values for the main welfare criteria. 

# Suggested tags

optimal-taxation, structural-labour-supply, random-utility, latent-opportunities, quantity-constraints, microsimulation, interpersonal-comparability, welfare-measurement, Norway, Aaberge-Colombino

# My quick takeaway

This is a core paper for your corpus. It does not solve your jobs-and-wellbeing problem at the axiomatic level, but it gives one of the clearest empirical structures in which preferences, opportunities, and tax rules are treated jointly without collapsing welfare evaluation into revealed behaviour. For your JMP, its main value is as a bridge from structural labour-supply modelling with latent opportunities to a more explicit and normatively rigorous (W(z,R,A;y)) framework.
