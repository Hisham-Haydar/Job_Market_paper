---

title: "Welfare Reform in European Countries: A Microsimulation Analysis"
authors: ["Herwig Immervoll", "Henrik Jacobsen Kleven", "Claus Thustrup Kreiner", "Emmanuel Saez"]
year: 2007
outlet: "The Economic Journal"
country_or_context: "15 pre-enlargement European Union countries"
population: "Working-age individuals aged 18–59; simulations use full-year workers for earnings deciles and OECD Labour Force participation data for non-workers"
data_period: "1998 tax-benefit systems and microdata; some aggregate tax inputs from OECD 1998 sources"
shelf: "microsimulation_labor_supply_welfare_reform"
tags: ["microsimulation", "EUROMOD", "welfare reform", "in-work benefits", "EITC", "negative income tax", "extensive margin", "intensive margin", "Europe", "equity-efficiency trade-off"]
priority: "high"
read_status: "extracted"
------------------------

# Full citation

Immervoll, Herwig, Henrik Jacobsen Kleven, Claus Thustrup Kreiner, and Emmanuel Saez. 2007. “Welfare Reform in European Countries: A Microsimulation Analysis.” *The Economic Journal* 117(516): 1–44. 

# One-sentence contribution

The paper uses a labor-supply model with both intensive and extensive responses, combined with the EUROMOD microsimulation model, to compare traditional welfare expansion with in-work benefits across 15 EU countries, concluding that in-work benefits are typically much more attractive than expanding traditional welfare. 

# Why this paper matters

This paper matters because it is one of the clearest cross-country attempts to connect optimal-tax logic, empirical labor-supply elasticities, and realistic tax-benefit systems using full microsimulation. It does not remain at the level of theoretical sign results. Instead, it asks how the equity-efficiency trade-off actually looks in existing European systems once one accounts for participation tax rates, marginal effective tax rates, and institutional detail country by country. 

For your project, its main value is threefold. First, it is directly relevant for structural labor-supply analysis with both extensive and intensive margins. Second, it provides a practical bridge between theory and empirical policy evaluation through EUROMOD. Third, it is useful for thinking about how policy design interacts with opportunity-like objects, not because it models feasible job sets explicitly, but because it operationalizes the budget constraints and work incentives individuals face in different institutional environments. That last point is an inference for your project rather than an explicit claim of the paper. 

# Core research question

How do two stylized welfare reforms—an expansion of traditional welfare through a universal demogrant and an in-work benefit targeted to workers—compare in terms of efficiency and the equity-efficiency trade-off across European countries once labor supply responds along both the intensive and extensive margins? 

# Economic setting and context

The paper studies the 15 pre-enlargement EU countries under their 1998 tax-benefit systems. The policy background is the European debate over whether low-income support should continue to rely mainly on traditional out-of-work transfers or whether it should be reoriented toward in-work support, following developments such as the U.S. EITC and the UK Working Families Tax Credit. Pages 3–5 frame this as a shift from the “old debate” about the *size* of welfare programs to the “new debate” about the *shape* of redistribution and work incentives. 

The empirical context is that European countries already had substantial means-tested and categorical support at the bottom, often generating high participation tax rates. Table 1 on page 2 shows that social benefits make up a very large fraction of disposable income in the bottom deciles in all countries, often above 50 percent and in some cases much higher. This institutional background is central to the paper’s conclusion that expanding traditional welfare is often unattractive at the margin. 

# Model / theoretical framework

The model class is a static labor-supply model with both intensive and extensive margins, embedded in a microsimulation evaluation of existing tax-benefit systems. Individuals are divided into demographic-earnings groups. Within each group, individuals share the same productivity and preferences but differ in a fixed cost of work (q), which generates smooth participation responses at the group level. Utility is quasi-linear:
[
u_j(c,l,q)= c - v_j(l) - q \mathbf{1}(l>0).
]
This specification eliminates income effects and makes welfare aggregation straightforward. 

The agent chooses labor supply (l) to maximize disposable income net of labor disutility and fixed work cost. Conditional on participation, hours satisfy the standard marginal condition depending on the net-of-tax wage. Participation occurs if the utility gain from working relative to not working exceeds the fixed cost. The paper then defines an intensive elasticity (e_j) for hours conditional on work and an extensive elasticity (\eta_j) for participation with respect to the gain from work. These are the core behavioral objects. Pages 6–9 develop this structure formally. 

The framework is positive with welfare evaluation. Positive behavior is the labor-supply response to taxes and transfers. Normative evaluation is not done through a fully specified social welfare function over all individuals. Instead, following Browning and Johnson, the paper measures the equity-efficiency trade-off by the ratio of welfare losses for losers to welfare gains for gainers under revenue-neutral reforms. This is a pragmatic policy-evaluation criterion rather than an axiomatic welfare theory. 

# Key objects

The main economic objects are the marginal tax rate (z_j), the participation tax rate (a_j), the intensive elasticity (e_j), the participation elasticity (\eta_j), and group employment (E_j). Marginal tax rates are computed by increasing earnings by 3 percent and measuring the change in net taxes and benefits; participation tax rates are computed by setting earnings to zero and measuring the implied loss of disposable income relative to actual earnings. These definitions are given on pages 15–16. 

The central welfare object is the equity-efficiency trade-off
[
\Psi = \frac{dL}{dG},
]
where (dL) is the aggregate welfare loss of losers and (dG) is the aggregate welfare gain of gainers from a small revenue-neutral reform. A value of (\Psi=1) means no equity-efficiency conflict; (\Psi>1) means redistribution is distortionary; (\Psi<1) means redistribution can improve efficiency. This is defined on pages 9–10 and then specialized to the two reforms. 

A second important object is the mechanical-versus-behavioral revenue decomposition. The paper defines (D) as the fraction of the mechanical revenue effect lost because of behavioral responses. For the working-poor policy, the corresponding object (D_w) may even be negative, implying a net positive fiscal feedback from increased participation. This is central to the paper’s results on efficiency. 

# Data

The empirical implementation uses EUROMOD, which combines country-specific but partly harmonized microdata with detailed tax-benefit calculators for all relevant 1998 tax and transfer rules in the 15 EU countries. The model includes income taxes, employee and employer social security contributions, means-tested and universal benefits, housing benefits, family benefits, unemployment benefits, and consumption taxes. Pages 14–21 and Tables A1–A3 summarize the institutional detail. 

For the main simulations, the sample used to construct earnings deciles is individuals aged 18–59 who worked the full year and had positive annual earnings. Pensioners, early retirees, disability recipients, students, and part-year workers are excluded. Deciles are based on pre-tax individual earnings including employer social contributions. Non-working populations and unemployment-benefit coverage are incorporated using OECD Labour Force Statistics. This is all described on pages 15–16 and in Table A3. 

# Identification logic

There is no causal identification strategy in the paper in the quasi-experimental sense. The analysis is a calibrated policy simulation built from institutional tax-benefit rules, observed earnings distributions, and externally chosen elasticity parameters motivated by the empirical literature. The identification of reform effects therefore comes from the combination of statutory policy variation encoded in EUROMOD and assumed labor-supply elasticities, not from exogenous policy shocks exploited econometrically within the paper. 

The crucial assumptions are that labor-supply responses can be summarized by the chosen intensive and extensive elasticities, that the static model with fixed work costs is a reasonable approximation for welfare reform questions, and that the chosen demographic-decile grouping captures the relevant heterogeneity for simulation purposes. The authors are explicit that this is a “first step” and that results can be updated as the empirical literature improves. 

# Estimation / empirical strategy

The empirical strategy is microsimulation plus elasticity-based calibration. EUROMOD is first used to compute effective marginal tax rates and participation tax rates by country and by earnings decile. Figure 1 on page 17 reports marginal tax rates, and Figure 2 on page 18 reports participation tax rates. These figures are central because the working-poor reform becomes attractive precisely where participation tax rates at the bottom are high. 

The paper then evaluates two infinitesimal revenue-neutral reforms. The first is a demogrant reform: a uniform transfer to all financed by a uniform increase in marginal tax rates on earnings. The second is a working-poor reform: a transfer only to workers, again financed by a uniform increase in marginal tax rates. Closed-form expressions for the efficiency cost and the equity-efficiency trade-off are derived for each reform, and then country-specific simulations are reported in Tables 2–6. 

# Treatment of preferences

Preferences enter in a simplified structural way through (v_j(l)), differing across groups, and through the fixed cost of work (q), which varies within groups. This generates both intensive and extensive responses, but the model does not estimate a rich utility function from observed choices. Instead, it calibrates elasticities based on prior studies. 

The paper therefore does not provide an explicit treatment of heterogeneous preferences in the welfare-economics sense you are interested in. Preference heterogeneity is operationalized only to the extent necessary to produce elastic labor supply along the two margins. There is no independent welfare comparison across heterogeneous tastes beyond the quasi-linear aggregation used for reform evaluation. 

# Treatment of opportunities / constraints

This section is important, and the paper is useful but not in the RURO sense. It does not model opportunities as actual feasible job sets, latent job offers, or demand-side rationing. There is no individual-specific set (A) of available jobs. The “opportunity structure” in the paper is instead encoded in observed tax-benefit rules and the resulting budget constraints, especially the participation tax rate and marginal effective tax rate. 

The paper does model non-convexities explicitly through fixed costs of work and through the institutional structure of taxes and benefits. These include means-tested benefits, housing benefits, unemployment benefits, social assistance phase-outs, in-work benefits, and tax discontinuities. In that sense it captures *institutional constraints* very well, but not *feasible opportunity sets* in the broader job-opportunity sense. Pages 5–8 and 19–21 are explicit on this. 

So the paper helps distinguish intensive and extensive behavioral margins and demonstrates how institutional constraints shape them. It does not help distinguish preference heterogeneity from opportunity heterogeneity in a structural job-choice sense, and it does not estimate latent opportunities. 

# Welfare / normative object

The paper is positive with welfare applications. Its welfare object is the equity-efficiency trade-off from a marginal reform, measured as the ratio of welfare losses among losers to welfare gains among gainers. This is not an explicit optimal-tax solution based on a fully specified social welfare function, nor is it a direct well-being measure of the form (W(z,R,A;y)). It is a practical reform-evaluation metric. 

The paper is directly relevant to responsibility versus compensation only in a limited way. It distinguishes between redistribution to the poor and redistribution to the working poor, and it explicitly notes that a conservative government might value the working poor more than the non-working poor, while a Rawlsian planner might do the opposite. But these are interpretive remarks rather than a developed fairness theory. Pages 35–36 make this explicit. 

The paper is also not a decomposition paper in your sense. It does not decompose inequality into opportunities, preferences, and related components. Rather, it decomposes the revenue effect of reforms into mechanical and behavioral parts and studies how those parts differ under two policy designs. 

# Main findings

The main substantive result is that expanding traditional welfare through a demogrant is typically undesirable in Europe unless redistributive tastes are extreme, because existing systems already create high participation tax rates at the bottom. In the benchmark simulations, redistributing one additional euro to the poor through the demogrant reform often costs the rich between 2 and 4 euros in welfare in many countries, and much more in some Nordic countries. Table 2(a) on pages 26–28 is the key source. 

By contrast, redistribution to the working poor through an in-work benefit is much more attractive. In many countries the efficiency loss is very small, and in some cases the reform improves aggregate efficiency because stronger participation responses raise revenue. In the benchmark scenario, Denmark, Ireland, France, Portugal, and Spain have (\Psi<1) for the working-poor policy, meaning that one euro transferred to the working poor costs the rich less than one euro in welfare. Table 2(a) is again central. 

The cross-country mechanism is clear from Figures 1 and 2. Countries with especially high participation tax rates at the bottom, such as Denmark, Ireland, and France, gain more from shifting toward in-work support. The paper explicitly notes on pages 28–29 that high participation tax rates in bottom deciles, combined with high participation elasticities there, make working-poor policies relatively more attractive. 

The results are robust to several sensitivity analyses. Table 3 shows that only modest average participation elasticities are needed to make the working-poor policy more attractive than the demogrant policy in almost all countries, often around 0.05–0.10 and never above 0.20 in panel (a). Table 4 shows that larger intensive elasticities worsen both policies, but do not change the relative superiority of the working-poor policy in most countries. Tables 5 and 6 show that the qualitative ranking is robust to excluding unemployment benefits and to concentrating participation elasticities on married women and lone parents. 

The paper also finds that the working-poor policy is politically more feasible in a self-interested-voter sense. Table 7 shows that, under the benchmark scenario, a majority would support the working-poor reform in most countries, while the demogrant reform would command a majority only in Spain and Italy. This is an important but secondary result. 

# Main limitations

The first limitation is that the paper does not model feasible job sets or labor-demand constraints explicitly. Non-employment is treated through fixed costs and participation elasticities, not through latent opportunities or observed job availability. This matters for your project because the distinction between preferences and opportunities remains unresolved at the structural level. 

A second limitation is the static framework. The paper explicitly excludes part-year work, retirement, disability transitions, education decisions, and dynamic human-capital effects. The authors acknowledge that in-work benefits may matter partly because work builds future earnings capacity, but this is not modeled. Pages 36–37 discuss this. 

A third limitation is that labor-market imperfections are outside the core model. The discussion section notes that involuntary unemployment, segmented labor markets, minimum wages, bargaining, and externalities could alter the welfare assessment. The authors argue that many of these extensions would likely strengthen the case for in-work benefits, but this is not shown within the model itself. 

A fourth limitation is normative. The equity-efficiency trade-off measure is practical but thinner than a full welfare criterion. It tells us how costly redistribution is, but not how much society should value the recipients. The paper itself notes that very strong Rawlsian redistributive preferences could still justify more traditional welfare. 

# Relevance for my JMP

## possible use for framing

This paper is highly useful for framing a project at the interface of labor supply, welfare design, and microsimulation. It shows clearly that the old question “how large should welfare be?” is distinct from the newer question “who should receive the marginal euro of redistribution?” and that the answer depends heavily on participation incentives. 

## possible use for model design

It is useful for model design if your JMP includes a structural labor-supply component or policy simulations. In particular, the way it embeds both extensive and intensive margins into a tractable grouped model is very relevant. It is less useful if your project requires explicit modeling of job sets or opportunity sets (A). 

## possible use for identification

Directly, limited. The paper does not estimate elasticities internally. Indirectly, very useful, because it shows which objects must be measured accurately for policy evaluation: participation tax rates, marginal effective tax rates, and the distribution of extensive elasticities across the earnings distribution. 

## possible use for welfare measurement

Moderately useful. It does not give you a well-being measure, but it gives a concrete way to evaluate reforms using money-metric welfare changes and a transparent trade-off criterion. It is especially useful if your empirical work culminates in simulated reform comparisons rather than in an axiomatic welfare ranking. 

## possible use for decomposition

Indirectly useful. The paper does not decompose inequality into preferences, opportunities, and policy factors. But it does decompose reform effects into mechanical and behavioral components and identifies how participation tax rates at the bottom interact with extensive elasticities. That is a decomposition of reform mechanisms, not of welfare inequality. 

## possible use for comparative application

Very useful. This is one of the strongest features of the paper. It performs the same analysis across 15 countries under harmonized logic, making it a valuable model for comparative policy applications or cross-country extensions of your work. 

# Research questions this paper inspires

How would the ranking of demogrant versus in-work benefits change if participation responses were driven by estimated feasible job sets rather than reduced-form fixed costs of work?

Can one integrate EUROMOD-style microsimulation with a (W(z,R,A;y))-type welfare measure so that reform evaluation depends not only on disposable income but also on feasible opportunities?

How sensitive are working-poor reforms to the ethical valuation of non-workers versus workers when non-employment reflects a mix of preferences, constraints, and job scarcity?

Can the mechanical-versus-behavioral decomposition used here be extended into a decomposition of well-being inequality into tax-benefit structure, preferences, and opportunity constraints?

Would a dynamic model with human-capital accumulation, stigma, and involuntary unemployment strengthen or weaken the conclusion that in-work benefits dominate traditional welfare expansion?

# Challenge to this paper

The central challenge is that the paper’s strongest empirical conclusion rests on a reduced-form treatment of the extensive margin. High participation elasticities make in-work benefits look attractive, but the model does not explain whether nonparticipation is due to preferences, fixed work costs, institutional traps, or lack of job opportunities. For a project concerned with fairness and opportunities, that matters because the ethical interpretation of the reform depends on why people are out of work in the first place. 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper models labor-supply behavior with intensive and extensive margins and evaluates reforms using disposable-income changes and microsimulated tax-benefit rules. It does not define well-being as (W(z,R,A;y)), and it does not model feasible job sets (A). 

[reasonable inference for my project] The paper is nevertheless close to your framework on the institutional side. The realized bundle (z) is approximated by employment status, hours, earnings, and disposable income under a rich tax-benefit system. The pay schedule (y) is effectively the observed earnings process together with tax-benefit transformations. What is missing is an explicit separation between preferences (R) and feasible set (A). The fixed cost of work (q) compresses several possible sources of nonparticipation into one reduced-form object. 

[unclear from paper] It is unclear whether the participation elasticity should be interpreted as preference heterogeneity, opportunity heterogeneity, labor-demand constraints, stigma, or child-care costs. The paper allows these interpretations informally but does not separate them empirically or normatively. 

[reasonable inference for my project] In your taxonomy, the paper is closest to practical policy evaluation under heterogeneous behavioral responses and to the contrast between redistribution to non-workers and redistribution to the working poor. It is not close to independence of (A), independence of (y), reference opportunity sets, or axiomatic responsibility for opportunities. Its main relevance is as a microsimulation bridge from labor-supply theory to comparative reform evaluation. 

# Relation to Bargain et al. (2013)

This paper is closely related to the broader structural tax-benefit and welfare literature associated with Bargain and related authors, though it is more focused on comparative microsimulation and reform ranking than on the construction of individual welfare metrics under preference heterogeneity. It shares the general concern with integrating labor-supply responses, tax-benefit institutions, and welfare evaluation, but its normative criterion is the Browning–Johnson trade-off rather than a richer individual welfare measure. [reasonable inference for my project] supported by 

In that sense, it is complementary to Bargain-type work. Bargain-style analyses can help think about individual welfare measurement under heterogeneous preferences, while Immervoll et al. provide the comparative institutional and microsimulation machinery showing how such welfare analysis could be embedded in actual European policy systems. [reasonable inference for my project] supported by 

# Relation to opportunities vs preferences

The paper is stronger on constraints than on opportunities, and stronger on behavior than on preferences. It captures how taxes and benefits shape the gain from work, and therefore how institutions influence labor-force participation. That is very useful for understanding the incentive environment facing individuals. 

But it does not cleanly separate preferences from opportunities. The fixed cost of work (q) is allowed to reflect monetary costs, commuting, stigma, or distaste for work, which mixes preference-like and opportunity-like components. Thus, the paper helps with reduced-form participation incentives, not with a rigorous opportunity-versus-preference decomposition. 

# Useful quotations / formulas

The extensive-margin threshold is
[
q_j = c_j - c_0 - v_j(l_j),
]
which determines who in group (j) enters work. This is the central link between budget constraints and participation. 

The participation elasticity is defined as
[
\eta_j
======

\frac{c_j-c_0}{F_j(q_j)}
\frac{\partial F_j}{\partial (c_j-c_0)}
=======================================

\frac{(c_j-c_0)f_j(q_j)}{F_j(q_j)}.
]
This is important because it is the main margin on which the paper’s results turn. 

For the welfare criterion, the key formula is
[
\Psi = \frac{dL}{dG},
]
the welfare loss of losers relative to the welfare gain of gainers from a small revenue-neutral reform. This is the paper’s main evaluative statistic. 

# Suggested tags

EUROMOD, welfare-reform, in-work-benefits, working-poor, demogrant, extensive-margin, participation-tax-rate, marginal-effective-tax-rate, Europe, microsimulation

# My quick takeaway

This is a very important paper for the empirical-policy side of your corpus. Its central message is that once participation responses matter and existing European systems already impose high participation tax rates at the bottom, expanding traditional welfare becomes very costly while in-work benefits often become highly attractive. For your project, it is especially useful as a comparative microsimulation template and as a reminder that institutional budget constraints matter enormously. Its limitation is that it remains reduced-form on the key distinction you care about most: whether nonparticipation reflects preferences, opportunities, or constrained job availability.
