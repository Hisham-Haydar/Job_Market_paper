---

title: "In-work policies in Europe: Killing two birds with one stone?"
authors: ["Olivier Bargain", "Kristian Orsini"]
year: 2006
outlet: "Labour Economics"
country_or_context: "Finland, France, and Germany"
population: "Women in couples and single women aged 25–64 available for the labor market; male labor supply in couples treated as fixed"
data_period: "1998 policy environment; Finland 1998 data, Germany 1998 data, France 1994 household budget data inflated to 1998"
shelf: "in_work_policies_structural_labour_supply"
tags: ["in-work benefits", "structural labor supply", "microsimulation", "Europe", "poverty traps", "family-based tax credits", "individualized wage subsidies", "female labor supply", "redistribution", "EUROMOD"]
priority: "very high"
read_status: "extracted"
------------------------

# Full citation

Bargain, Olivier, and Kristian Orsini. 2006. “In-work policies in Europe: Killing two birds with one stone?” *Labour Economics* 13(6): 667–697. 

# One-sentence contribution

The paper compares, for Finland, France, and Germany, a family-income-tested in-work tax credit and a purely individualized low-wage subsidy using EUROMOD plus structural female labor-supply models, and finds that the individualized policy generally dominates on employment while both reforms have only limited differences in poverty reduction. 

# Why this paper matters

This paper matters because it directly studies one of the core design problems in tax-benefit reform: whether one can jointly improve redistribution and labor-market inclusion through in-work transfers, and how the answer depends on whether the policy is household-based or individualized. It is not merely descriptive; it uses structural behavioral microsimulation to compare reforms on both employment and poverty grounds. 

For your project, the paper is especially useful as a bridge between structural labor-supply estimation and policy design. It is less useful for explicit opportunity-set analysis, but it is important for understanding how labor-supply responses, family structure, and tax-benefit design interact in a comparative microsimulation environment. 

# Core research question

Can in-work transfer policies simultaneously reduce poverty and increase social inclusion in continental European welfare states, and how do the answers differ when the policy is means-tested on household income versus individualized on workers’ own low wages? 

# Economic setting and context

The paper studies Finland, France, and Germany, three countries described as facing inactivity traps because generous social assistance creates weak financial returns to work for low-wage households. The policy background is the broader European debate over “making work pay” reforms in contexts where social assistance may discourage labor-market participation. 

The comparative setting is central. The authors explicitly exploit cross-country heterogeneity in pre-reform tax-benefit systems, earnings distributions, and labor-supply elasticities in order to understand why the same stylized reforms may work differently across countries. Pages 3–4 and Table 1 are especially important for the institutional background. 

# Model / theoretical framework

The model class is a structural discrete-choice labor-supply model combined with tax-benefit microsimulation. Female adults choose among a small discrete set of weekly hours alternatives, while household disposable income for each alternative is computed by EUROMOD under the actual system and under each reform scenario. Utility depends on hours, disposable income, and observed household characteristics, plus an extreme-value random term. Equations (1) and (2) on pages 12–13 present the core framework. 

The framework is positive with policy-evaluation applications. Positively, it models labor-supply responses of women to changes in tax-benefit schedules. The evaluation criterion is not a welfare-theoretic one in the strong sense, but a pragmatic policy comparison based on employment transitions and poverty outcomes. The authors explicitly state that they compare reforms using two policy goals: poverty reduction and social inclusion measured by transitions into work. 

The choice set is not modeled as a heterogeneous job-opportunity set. Rather, women choose among non-participation, part-time, and full-time work. The paper explicitly acknowledges that it does not model the demand side, life-cycle aspects, or domestic production, and that rationing may partly be absorbed by fixed costs or educational effects. This is therefore a standard structural discrete-hours framework, not a RURO or latent-job model. 

# Key objects

The key policy objects are two stylized reforms. The first is a working tax credit (WTC) means-tested on family income and modeled after the British WFTC, extended to childless singles and couples. The second is an individualized low-wage subsidy (LWS) that increases hourly wages up to a country-specific reference wage and then phases out with higher wage rates. Section 3 and the formulas on pages 6–8 define these reforms precisely. 

The key behavioral objects are female labor-supply choices, household disposable income under alternative tax-benefit systems, and structural labor-supply elasticities. The paper emphasizes participation responses more than hours responses, though both margins are simulated. Table 4 on page 19 reports own-wage elasticities for women in couples and single women by country. 

The key evaluative objects are poverty reduction and social inclusion. Poverty is measured by changes in headcount below fixed poverty lines at 40, 50, and 60% of median equivalized disposable income. Social inclusion is measured as net transitions into work. Tables 5–7 are the core result tables for responses, costs, and poverty effects. 

# Data

The paper uses harmonized microdata integrated in EUROMOD. Finland relies on the 1998 Income Distribution Survey, Germany on the 1998 GSOEP, and France on the 1994 Household Budget Survey inflated to 1998 monetary values. EUROMOD computes taxes, social contributions, and transfers for each household under baseline and reform scenarios. 

For labor-supply estimation, the analysis is restricted to households with adults aged 25–64 available for the labor market. Disabled, retired, full-time students, self-employed, farmers, and certain “extreme” households are excluded. The estimations focus on women in couples and single women; male labor supply is treated as fixed. Table 2 on page 11 reports the resulting sample composition and key descriptive statistics. 

# Identification logic

Identification is structural and mainly parametric. The model uses variation in nonlinear tax-benefit rules, wages, household composition, and demographic taste shifters to identify labor-supply preferences. The authors are explicit that the model is not nonparametrically identified and that identification relies on functional-form restrictions, interaction terms, and the nonlinearity of the tax-benefit rules. 

The paper does not use quasi-experimental variation. Instead, it follows the standard structural discrete-choice tradition: predict wages for non-participants, compute disposable income for each hours alternative with EUROMOD, estimate preferences by maximum likelihood, and then simulate reform responses. This is internally coherent for ex ante policy simulation, but it does not provide causal identification in the reduced-form sense. [reasonable inference for my project] supported by 

Identification is weak with respect to opportunities. The authors explicitly note that the approach does not model the demand side and that rationing in hours or participation may influence the estimates, with fixed costs or education effects partly absorbing such constraints. This is an important limitation for any interpretation that would try to separate preferences from opportunity constraints. 

# Estimation / empirical strategy

The empirical strategy has three layers. First, the authors simulate actual tax-benefit systems and stylized reforms using EUROMOD. Second, they estimate country-specific structural labor-supply models for women in couples and single women. Third, they use the estimated models to simulate post-reform transitions, fiscal cost, and poverty effects under the WTC and LWS. 

The discretization is intentionally simple: non-participation, part-time work, and full-time work. Female wages are computed from data or predicted for non-participants using a standard wage equation with Heckman correction. Labor-supply elasticities are then computed numerically by simulating wage increases. Sections 4 and 5 are the core methodological sections. 

The paper is especially strong in connecting behavioral results to reform design. Page 8, Figure 2 visually compares how the WTC and LWS alter budget constraints for a Finnish single woman and a German couple, showing that the WTC creates large gains to work but also high phase-out EMTRs, while the LWS lowers EMTRs more uniformly. 

# Treatment of preferences

Preferences are represented by a quadratic utility function in disposable income and hours, with observed heterogeneity through age, children, and region, plus fixed costs of work and an extreme-value stochastic term. The authors explicitly estimate these preferences separately for women in couples and single women in each country. Equations (1) and (2), together with Tables 8 and 9 in the appendix, describe this structure. 

At the same time, the paper is cautious about interpretation. It explicitly warns that because the model omits the demand side, life-cycle considerations, and domestic production, the estimated “consumption-leisure preferences” should not be interpreted too literally. The paper even states that it refrains from welfare analysis because of this lack of robustness in the interpretation of the utility model. This is an unusually important admission. 

Thus, preference heterogeneity is behaviorally central, but the paper itself does not treat estimated preferences as a normatively robust object. This makes it relevant for your project as a warning about over-interpreting structural preference estimates when opportunity constraints are only implicitly handled. [reasonable inference for my project] supported by 

# Treatment of opportunities / constraints

The paper does not model opportunities explicitly as feasible job sets. Women choose among a discrete set of hours levels, not among jobs with different wages, hours, and non-pecuniary characteristics. There is no latent job density, no explicit opportunity set (A_i), and no direct account of differential job availability. 

However, the paper is not blind to constraints. It explicitly notes that continental European labor markets are characterized by institutional and demand-side rigidities, that actual hours distributions are concentrated around a few work-hour bundles, and that rationing in hours or in participation may significantly influence the results. Figure 3 on page 13 shows the observed concentration of hours around non-participation and full-time work, which the authors use to justify the discrete-choice setup. 

Still, these constraints remain implicit. They enter, at best, through fixed costs of work, educational effects, or the shape of the observed hours distribution. So the paper helps distinguish financial incentives from labor-supply behavior, but it does not help much with a rigorous distinction between preference heterogeneity and opportunity heterogeneity in your stronger (R) versus (A) sense. 

# Welfare / normative object

The paper is not explicitly normative in the welfare-theory sense. It does not construct an individual welfare measure, equivalent income, or social welfare function for reform ranking. Instead, it adopts pragmatic policy criteria: poverty reduction and social inclusion. 

This is important because the paper explicitly states that it avoids welfare analysis given the fragile interpretation of the estimated utility functions when demand-side constraints and other omitted factors are present. That is analytically significant for your research: the authors themselves do not treat their structural utility model as a robust normative object. 

The closest thing to a normative trade-off here is the efficiency-equity tension in the design of in-work benefits: household-based policies target poorer families better but discourage secondary earners; individualized policies are less tightly targeted but create stronger work incentives. This is a policy-design trade-off, not a well-being theory. 

# Main findings

The main employment finding is that the household-based WTC generally has negative net effects on female employment in all three countries. Positive participation effects for single women are offset, and more than offset, by negative participation effects for married women with working partners. The effect is especially strong in France. Table 5 on pages 20–21 is the key source. 

By contrast, the individualized low-wage subsidy yields positive net employment effects, especially in France and Germany. Table 5 shows that the LWS increases employment of both single women and married women, so that total female employment rises under the individualized design. Finland shows smaller gains because estimated labor-supply elasticities are smaller. 

The poverty results are more nuanced. Table 7 on page 25 shows that both reforms reduce poverty, but the WTC and LWS are often closer than one might expect. In France, both substantially reduce poverty at the 50% median-income line; in Germany, the WTC does slightly better once behavioral responses are included; in Finland, both effects are modest. The paper’s important substantive claim is that the individualized subsidy can achieve poverty reduction not dramatically inferior to the family-based tax credit while performing much better on employment. 

The cost-efficiency comparison is also important. Table 6 on pages 22–23 shows that once behavioral responses are accounted for, the WTC becomes more expensive than its pre-response budget because it reduces work in key groups, while the LWS becomes cheaper than its pre-response cost because it raises employment. The paper interprets this as further support for the individualized scheme in continental European settings. 

# Main limitations

A first limitation is the treatment of opportunities. The paper openly states that it does not explicitly model the demand side, rationing, life-cycle considerations, or domestic production. For your purposes, this is the single most important limitation: the model is structurally rich on tax-benefit incentives but thin on opportunity sets. 

A second limitation is that male labor supply is fixed, single men are effectively excluded from the behavioral analysis, and unemployed job seekers are largely treated outside the model. This simplifies the exercise but narrows the behavioral margins that reforms can affect. 

A third limitation is normative. The paper explicitly refrains from welfare analysis because the interpretation of the utility model is not sufficiently robust. This is methodologically honest, but it means the paper cannot directly speak to welfare measurement, responsibility, or compensation questions. 

A fourth limitation is that the findings are strongly shaped by the stylized design of the two benchmark reforms. The paper itself notes that better policy design might, in principle, target lone mothers while avoiding discouragement of secondary earners. Hence the results should be read as a comparison of two broad policy families, not as a theorem about all possible in-work instruments. 

# Relevance for my JMP

## possible use for framing

This paper is very useful for framing the policy-design problem in labor-supply microsimulation. It shows that “making work pay” reforms cannot be evaluated only on poverty grounds or only on employment grounds; the family unit of assessment is central.

## possible use for model design

It is moderately useful for model design if your empirical framework stays within structural discrete labor supply and tax-benefit microsimulation. It is not useful for explicit job-opportunity-set modeling.

## possible use for identification

It is of limited use for identification in the quasi-experimental sense. Its value lies more in showing how to do disciplined structural simulation than in providing a strong identification strategy for preferences or opportunities.

## possible use for welfare measurement

Directly, limited. The paper is explicit that it does not provide robust welfare analysis. Indirectly, it is very useful as a cautionary example: one should not too quickly treat estimated structural utility as a normatively reliable welfare metric.

## possible use for decomposition

It is moderately useful in a loose sense. It does not decompose welfare into opportunities, preferences, and pay schedules, but it does separate redistribution and employment effects and links cross-country differences to tax-benefit systems, income distributions, and elasticities.

## possible use for comparative application

This is one of the paper’s strongest uses. It is a genuinely comparative European application with a harmonized model and reform framework across three countries. That makes it valuable for any comparative policy project.

# Research questions this paper inspires

1. Can the paper’s comparative microsimulation framework be extended from discrete hours choices to a latent-job model with explicit feasible job sets (A_i)?

2. Under what conditions does an individualized in-work transfer dominate a family-income-tested transfer once welfare is measured over both income and leisure rather than poverty and employment only?

3. How much of the observed difference between France, Germany, and Finland is due to tax-benefit design versus preference heterogeneity versus unmodeled opportunity constraints?

4. Can one design a hybrid in-work policy that preserves the poverty-targeting advantages of the WTC while avoiding the discouragement of secondary earners?

5. How would the paper’s conclusions change if non-employment and part-time work were modeled with explicit rationing or demand-side constraints rather than fixed costs alone?

# Challenge to this paper

The strongest challenge is that the paper’s policy conclusions are drawn from a behavioral model whose own welfare interpretation the authors do not fully trust. That is not a flaw in honesty; it is the correct methodological stance. But it means the paper is strongest as a positive comparative simulation of employment and poverty effects, and weaker as a basis for deeper claims about well-being, fairness, or optimal design. 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper models women’s labor-supply choices under different tax-benefit systems and compares reforms using poverty and employment outcomes. It explicitly does not model the demand side or use the estimated utility model for welfare analysis. 

[reasonable inference for my project] In your notation, the realized bundle (z) is essentially the chosen hours/income combination under each tax-benefit regime. Preferences (R) are represented by the estimated quadratic utility over disposable income and hours, but the paper itself cautions against giving these preferences a strong normative interpretation. The pay schedule (y) enters through gross wages and the tax-benefit mapping computed by EUROMOD. The feasible set (A) is largely absent as an explicit object; at most it is indirectly reflected in fixed costs and in the limited hours-choice discretization. 

[unclear from paper] The paper does not define a well-being measure (W(z,R,A;y)), does not analyze actual versus reference opportunity sets, and does not study axioms such as independence of (A), independence of (y), responsibility for opportunities, or compensation for opportunity disadvantage. These are outside its explicit scope. 

[reasonable inference for my project] In your taxonomy, the paper is closest to the relation between (R), (y), and comparative policy outcomes, but not to explicit treatment of (A). It is not close to independence of (A), but mainly because (A) is not modeled. It is also not a laissez-faire or reference-opportunity-set paper. Its main use for your framework is as a comparative tax-benefit microsimulation benchmark and as a warning about over-interpreting structural preference estimates when opportunity constraints remain implicit. 

# Relation to Bargain et al. (2013)

This paper is related to Bargain et al. (2013) mainly through the shared concern with structural labor-supply estimation and normative policy interpretation, but the two papers diverge sharply on the welfare object. Bargain et al. (2013) uses estimated preferences to construct alternative individual welfare metrics in the consumption-leisure space. The present paper explicitly refuses to do that, because it doubts the robustness of the preference interpretation once demand-side constraints and other omitted factors are acknowledged. In that sense, this 2006 paper is an instructive precursor: it shows the empirical promise of the labor-supply framework but also its normative limits. [reasonable inference for my project] supported by

# Relation to opportunities vs preferences

This paper is materially more useful for preferences and tax-benefit incentives than for opportunities. It studies how estimated female labor-supply responses differ across countries and interact with reform design, but it does not model opportunities as explicit feasible job sets. 

At the same time, the paper is valuable because it openly acknowledges that what appears as preference heterogeneity may partly reflect omitted constraints. That makes it an important cautionary reference for your project: if (A) is not modeled, one should be careful about giving (R) too much empirical or normative weight. 

# Useful quotations / formulas

The core behavioral probability is the conditional logit formula
[
P_{ik}=
\frac{\exp U(H_k,C_{ik},Z_i)}
{\sum_{j=1}^{J}\exp U(H_j,C_{ij},Z_i)},
]
which is the basis for the structural labor-supply simulation. Equation (1) on page 12 is central. 

The paper’s key policy message is visible in *Figure 2 on page 8*: the WTC sharply raises net gains at entry into work but also creates steep phase-out segments, whereas the LWS lowers EMTRs more uniformly. This figure is one of the clearest visual summaries of why the two reforms generate different participation responses. 

The most important substantive table is *Table 5 on pages 20–21*. It shows that the WTC raises participation of single women but lowers participation of married women enough to produce a negative net female employment effect, whereas the individualized LWS yields positive net employment effects in France and Germany. 

# Suggested tags

in-work-benefits, working-tax-credit, low-wage-subsidy, structural-labor-supply, EUROMOD, comparative-microsimulation, poverty-traps, female-employment, Europe, Bargain-Orsini

# My quick takeaway

This is a high-priority paper for the comparative policy-simulation side of your corpus. It does not solve your jobs-and-wellbeing problem, and it is weak on explicit opportunity sets, but it is very valuable for showing how structural labor-supply microsimulation can be used to study the design trade-off between family-based and individualized in-work policies. Its most useful lesson for your JMP is methodological and conceptual: employment and poverty effects can diverge across policy designs, and one should be very cautious about treating estimated labor-supply utility as a welfare object when opportunity constraints remain implicit.
