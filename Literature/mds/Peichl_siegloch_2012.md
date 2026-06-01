---

title: "Accounting for labor demand effects in structural labor supply models"
authors: ["Andreas Peichl", "Sebastian Siegloch"]
year: 2012
outlet: "Labour Economics"
country_or_context: "Germany"
population: "German households in SOEP 2009/2010 for labor supply; German establishments and employees in LIAB 1996-2007 for labor demand; policy simulation focuses on employable benefit recipients under a workfare reform"
data_period: "Labor supply estimated on SOEP 2009 (using 2010 wave); labor demand estimated on LIAB 1996-2007"
shelf: "labor_supply_demand_interaction_structural_microsimulation"
tags: ["labor supply", "labor demand", "structural microsimulation", "partial equilibrium", "workfare", "Germany", "discrete choice labor supply", "linked employer-employee data"]
priority: "very high"
read_status: "extracted"
------------------------

# Full citation

Peichl, Andreas, and Sebastian Siegloch. 2012. “Accounting for labor demand effects in structural labor supply models.” *Labour Economics* 19(2): 129–138. 

# One-sentence contribution

The paper proposes a practical way to incorporate labor demand into structural discrete-choice labor supply simulations by iterating estimated labor supply responses with micro-estimated labor demand elasticities until a partial labor-market equilibrium is reached, and shows for a German workfare reform that demand effects offset about 25% of the positive labor-supply effect. 

# Why this paper matters

This paper matters because it addresses a major weakness of standard structural labor supply simulations: they typically treat labor demand as perfectly elastic, so predicted supply shifts are interpreted as employment shifts. The paper argues that this is generally incorrect and that labor-market outcomes inferred from supply-only models are biased if labor demand is finite. 

For your research direction, the paper is especially valuable as a bridge between structural labor supply estimation and an explicit, though still parsimonious, treatment of demand-side constraints. It does not build a RURO model or an axiomatic welfare framework, but it is one of the clearest attempts to move beyond the universal-demand assumption inside microsimulation. That makes it highly relevant for any project concerned with separating preferences from opportunities or constraints in labor-market outcomes. 

# Core research question

How can structural labor supply models used for policy evaluation be extended in a straightforward way to account for labor demand effects, and how much does ignoring those effects bias simulated labor-market outcomes of policy reforms such as workfare in Germany? 

# Economic setting and context

The paper is set in Germany and studies the labor-market effects of a counterfactual workfare reform. The policy requires employable individuals in benefit-receiving households to fulfill a full-time work requirement, or the remaining hours needed to reach full-time if they already work part-time. All other tax-benefit rules are kept unchanged. 

The institutional context is a standard tax-benefit microsimulation setting, but the contribution is methodological. The authors emphasize that many ex-ante policy evaluations focus only on labor supply and therefore implicitly assume perfectly elastic labor demand. Their proposed remedy is a partial-equilibrium micro-level integration of labor demand and labor supply. 

# Model / theoretical framework

The model class is a linked structural labor supply–labor demand microsimulation model solved by iteration to a partial labor-market equilibrium. On the supply side, the authors estimate a standard discrete-choice random-utility model of labor supply in the tradition of van Soest (1995) and Blundell et al. (2000). On the demand side, they estimate labor demand elasticities from a structural translog cost function using linked employer–employee data. The two sides are then iterated through wage adjustments until hours and wages converge. 

What the agent chooses on the supply side is a discrete hours category. For couples there are 49 joint choices, generated from seven hours categories for each spouse: 0, 10, 20, 30, 40, 50, and 60 weekly hours. Utility depends on household consumption, female and male hours, squared and interaction terms, and fixed costs of work represented by part-time dummies. Equation (1) on page 131 gives the translog utility specification. 

The feasible set is not modeled as an explicit set of jobs or job offers. On the supply side, the model remains a standard discrete-hours choice model, so the household is evaluated over a fixed grid of hours categories with disposable income computed by tax-benefit simulation. Demand-side constraints enter only indirectly through wage adjustments and employment offsets induced by estimated labor demand elasticities. Thus, opportunities are not modeled as explicit heterogeneous feasible sets (A_i), but neither are they ignored altogether: the paper introduces firm-side behavior as a market-level constraint on the translation of supply shifts into employment. [reasonable inference for my project] supported by 

The framework is positive and simulation-based, not normative. Welfare enters only in the sense of utility-maximizing labor supply decisions, not as a separate social or individual welfare measure. 

# Key objects

The central supply-side object is the direct translog utility function over consumption and hours, shown in Equation (1). Household disposable income is computed using the IZAΨMOD tax-benefit calculator, which maps gross earnings into net income under the German tax-transfer system. 

The central demand-side object is the translog cost function in Equation (2), from which cost-share equations are derived using Shephard’s lemma. These yield own- and cross-wage labor demand elasticities by skill group through Equations (5) and (6). 

A third key object is the iteration algorithm linking the two models. For each skill and household-type cell, the reform-induced net-income change first generates a labor supply response; the induced hours change then implies a wage adjustment through the labor demand elasticity; the new wage feeds back into the supply model; and the process repeats until the relative change in working hours is below 0.1%. Figure 1 on page 133 is the key diagram explaining this logic. 

# Data

The labor supply model is estimated on the 2010 wave of the German Socio-Economic Panel, containing information for 2009. The authors observe around 25,000 individuals in more than 12,000 households and use information on gross wages, job type, government transfers, working time, household composition, age, and education. The IZAΨMOD calculator is used to compute net income under January 2009 rules. 

The labor demand model uses the LIAB linked employer–employee dataset from the IAB, combining administrative employee records with the IAB Establishment Panel. The final panel covers 1996-2007 and includes 4,073 establishments observed on average 3.3 times, giving 13,451 establishment-year observations and between 1.6 and 2.0 million workers per year. The paper excludes some industries, including mining, agriculture, finance, and the public sector. 

Skill groups are defined consistently across the supply and demand sides: high-skilled workers hold a university, polytechnical, or college degree; medium-skilled workers have completed vocational training or obtained the Abitur; low-skilled workers have neither. This common skill partition is essential for the labor supply–demand linkage. 

# Identification logic

Identification is structural on both sides. On the supply side, the paper relies on a standard discrete-choice labor supply model with net incomes calculated under the full tax-benefit schedule. The authors emphasize that accounting for tax-benefit nonlinearities creates variation in net wages across households with similar gross wages, and that spatial and household-specific institutional variation also helps identify preference parameters. They further use predicted wages for all individuals to reduce endogeneity concerns. 

On the demand side, identification comes from estimating a translog cost function and the associated factor-share equations using rich linked employer–employee microdata. Labor demand elasticities are recovered from the estimated translog parameters. The demand system is estimated by SUR, exploiting variation across firms, skill shares, wages, output, industries, and time. 

The combined model is not identified as one unified equilibrium system. Instead, the two structural models are estimated separately and then linked through an iteration procedure. The paper is explicit that this requires restrictive assumptions, most notably constant labor demand elasticities during the iteration, perfect competition, no wage rigidities, and no demand-side shift from the reform itself. This is a practically useful but partial-equilibrium identification strategy rather than a full equilibrium identification of market interactions. [reasonable inference for my project] supported by 

# Estimation / empirical strategy

The labor supply side is estimated as a discrete-choice conditional logit model with a translog utility specification. The model uses seven discrete hours categories and calibrates the random utility component by drawing Extreme Value Type-I errors consistent with observed choices. Disposable income for every alternative is computed using IZAΨMOD. 

The labor demand side is estimated from a translog cost function. The authors derive factor-share equations for three labor inputs—high-, medium-, and low-skilled labor—and estimate them by seemingly unrelated regression, using the restrictions implied by linear homogeneity and symmetry. Table 6 in the appendix reports the estimated coefficients and confirms that the demand model satisfies positivity, quasi-concavity, and adding-up conditions. 

The two estimated models are then linked by an iterative algorithm. For each skill/household-type cell: net incomes are recalculated under the reform; labor supply is simulated; wages are adjusted using labor demand elasticities; labor supply is re-simulated at the new wage; and the process continues until convergence. Table 3 on page 135 opens this “black box” by showing the sequence of hours and wage changes across iterations. Figure 1 on page 133 is the conceptual diagram of the mechanism, and Figure 2 on page 136 illustrates how higher absolute labor demand elasticities imply smaller wage adjustments for a given supply shift. 

# Treatment of preferences

Preferences are modeled explicitly on the labor supply side through a translog utility function over consumption and hours, with heterogeneity through taste shifters such as age, age squared, presence of children, and region. Fixed costs of work are represented through part-time dummies. The model is fully structural in the standard discrete-choice labor supply sense. 

However, the paper’s contribution is precisely that preferences are not treated as the sole determinant of employment changes. Pure supply-side models would implicitly interpret the reform-induced supply shift as an employment shift. Peichl and Siegloch argue that this is generally wrong because demand-side firm behavior must also be taken into account. So the paper is explicitly against a pure-preference interpretation of labor-market outcomes. 

This is an important point for your project. The paper still does not model opportunities as individual feasible sets, but it does reject the reduction of observed labor-market effects to preferences alone. [reasonable inference for my project] supported by 

# Treatment of opportunities / constraints

This is the key section for your interests. The paper does not model opportunities explicitly as heterogeneous job sets, latent offers, or RURO-type feasible sets. It does not assign each individual a set (A_i) of available jobs. The supply model itself remains a standard discrete-hours choice model with a common hours grid. 

Nonetheless, the paper is centrally about constraints neglected by standard labor supply models. Its core claim is that even if labor supply responds positively to a reform, employment need not respond one-for-one because labor demand is finite. This means that the market does not passively accommodate households’ preferred hours choices. On page 129, the paper states that studies focusing only on supply “implicitly assume perfectly elastic labor demand,” and that eventual employment effects equal labor supply effects only under that assumption. 

Thus, the paper introduces an important form of opportunity restriction at the market level: firm demand constrains the realization of supply shifts into jobs. This is not the same as modeling individual opportunity sets, but it is directly relevant for the preferences-versus-opportunities distinction because it shows that demand-side conditions can materially alter labor-market outcomes. The paper finds that this demand channel offsets about 25% of the positive labor supply effect of the workfare reform. Table 2 on page 134 is the key evidence. 

So the paper helps distinguish preference heterogeneity from at least one class of constraints: demand-side labor-market restrictions. It does not, however, identify heterogeneous opportunities at the individual level. It is therefore more relevant for “market constraints matter” than for “individual feasible sets are estimated.” [reasonable inference for my project] supported by 

# Welfare / normative object

The paper is overwhelmingly positive rather than normative. Utility is used as a behavioral object in the structural labor supply model, but there is no explicit social welfare function, money-metric welfare measure, equivalent variation, or fairness criterion. 

Its policy relevance comes from improving the accuracy of ex-ante employment and budget predictions, not from developing a welfare theory. The workfare application does include fiscal effects, but the evaluation is couched in terms of employment, government budget, and feasibility rather than normative well-being. 

For your project, this means the paper is not directly useful for responsibility for opportunities, compensation for opportunities, or reference opportunity sets. Its usefulness is upstream: it shows that any welfare or fairness analysis of labor-market reforms should be cautious about interpreting supply-side simulations as realized labor-market opportunities. [reasonable inference for my project] supported by 

# Main findings

The first main empirical finding is that German labor demand elasticities are finite and economically meaningful. Table 1 on page 132 reports own-wage elasticities of about −0.56 for high-skilled workers, −0.37 for medium-skilled workers, and −1.05 for low-skilled workers. This immediately rejects the pure labor-supply assumption of perfectly elastic demand. 

The second main finding is that the counterfactual workfare reform induces a large positive labor supply effect in the supply-only simulation, around 1.5 million full-time equivalents. Table 2 on page 134 shows that all household types and skill groups have positive labor supply responses. 

The third and central finding is that labor demand offsets roughly 25% of that positive supply effect. Table 2 reports an overall labor demand effect of about −377,000 full-time equivalents relative to the pure labor-supply result, yielding an offset ratio of about −25.3%. This is the paper’s headline result and is also stated in the abstract. 

The fourth finding is that these offsets differ across household types, skill groups, and gender. Women exhibit stronger countervailing demand effects than men, and medium-skilled groups show particularly large relative offsets. The text on page 134 explains this pattern in terms of differences in labor supply elasticities and labor demand elasticities. 

The fifth finding is that the demand–supply iteration converges and behaves in line with theory. Table 3 on page 135 displays the alternating wage and hours adjustments across iterations, and Figure 2 on page 136 explains why larger absolute labor demand elasticities imply smaller offsetting effects and quicker convergence. 

The sixth finding is fiscal. Even after accounting for labor demand restrictions, the workfare reform increases the government budget. Table 4 on page 135 reports a budget effect of €31.7 billion after labor supply responses only and €27.7 billion after adding labor demand, before subtracting workfare administration costs; after those costs, the total effect remains positive at about €10.5 billion. 

The seventh finding is robustness. Page 136 reports that alternative reform simulations and elasticity scenarios produce qualitatively similar results: labor demand consistently acts as a stabilizer, dampening both positive and negative labor supply shifts, and the relative magnitude of demand offsets is typically between 15% and 35%. 

# Main limitations

A first limitation is that the model is partial equilibrium. The authors explicitly state that they abstract from changes in output prices, consumption, and other general equilibrium effects. They also do not model intertemporal adjustments. This is a deliberate simplification, but it limits the scope of the policy evaluation. 

A second limitation is that labor demand effects enter only through wage adjustments and skill-cell demand elasticities. The paper does not model individual job-offer probabilities, hours offers, or explicit rationing at the person level. As a result, the opportunity side remains aggregate and market-level rather than individual-specific. [reasonable inference for my project] supported by 

A third limitation is the reliance on restrictive assumptions for the iteration procedure: constant labor demand elasticities, perfect competition, no wage rigidities, and no demand-curve shift due to the policy reform. The authors acknowledge these assumptions explicitly on pages 133 and 136. 

A fourth limitation is that the supply model remains a standard discrete-hours model. So while the paper adds demand-side behavior, it does not solve the deeper problem of modeling joint wage-hours-job opportunities at the individual level. [reasonable inference for my project] supported by 

A fifth limitation is normative. The paper has no explicit welfare metric or fairness framework, so it cannot by itself be integrated into a responsibility-sensitive analysis of opportunities without substantial additional structure. 

# Relevance for my JMP

## possible use for framing

This paper is highly useful for framing the point that structural labor supply models are incomplete if they ignore labor demand. It supports a strong claim that labor-market outcomes should not be interpreted solely through supply-side preferences. 

## possible use for model design

It is useful for model design if your empirical strategy remains partly structural and policy-simulation oriented. In particular, it provides a template for augmenting a labor supply model with a demand module without building a full CGE model. 

## possible use for identification

Moderate to high relevance. The paper is valuable as an example of how separately estimated structural supply and demand components can be combined on microdata. It also shows the precise assumptions under which such a linkage is credible. 

## possible use for welfare measurement

Direct relevance is limited. The paper is not about welfare measurement. Indirectly, it is useful because any welfare analysis of labor-market reforms that ignores demand-side constraints risks mismeasuring the realized outcomes that should enter welfare evaluation. [reasonable inference for my project] supported by 

## possible use for decomposition

Moderate relevance in a positive sense. The paper does not decompose welfare inequality into preferences and opportunities, but it does decompose labor-market reform effects into a supply-side component and a demand-side offset. That is conceptually useful for any later decomposition of realized outcomes into different structural forces. [reasonable inference for my project] supported by 

## possible use for comparative application

The application is German, but the methodology is portable to other countries with a discrete-choice labor supply model, a tax-benefit calculator, and linked employer–employee data for labor demand estimation. 

# Research questions this paper inspires

Can a RURO or latent-job model be combined with a micro-estimated labor demand module so that both individual opportunity sets and market-level demand restrictions jointly determine labor outcomes?

How much of the discrepancy between predicted labor supply effects and realized employment effects can be attributed to demand elasticities versus explicit rationing or job-offer heterogeneity?

Can structural policy simulations be decomposed into preference-driven supply shifts, demand-side wage adjustments, and changes in individual feasible opportunity sets?

How would a responsibility-sensitive welfare analysis change if market-level labor demand restrictions were treated as ethically relevant opportunity constraints rather than merely as equilibrium adjustments?

Can the iterative supply–demand linkage in this paper be extended to richer job packages including occupation, sector, and nonpecuniary job attributes rather than only hours and wages?

# Challenge to this paper

The main challenge is that the paper improves structural labor supply simulation without rethinking the opportunity structure at the individual level. It convincingly shows that labor demand matters, but the mechanism remains a market-level wage adjustment rather than a full model of heterogeneous job availability. So it corrects one important bias in supply-only models, but it does not yet provide a truly opportunity-sensitive labor-market model. 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper’s central claim is that labor-market outcomes cannot be inferred correctly from labor supply behavior alone because labor demand is finite and must be modeled. It therefore insists that realized employment effects differ from pure labor supply effects. 

[reasonable inference for my project] In your notation, the paper is useful mainly for the link between realized outcomes (z) and the pay schedule / market environment (y). It shows that the translation from preferences into realized labor-market bundles is mediated by firm-side demand conditions. supported by 

[unclear from paper] There is no explicit individual feasible set (A_i), no normative well-being measure (W(z,R,A;y)), and no distinction between actual and reference opportunity sets. The paper does not study fairness, compensation, or responsibility. 

[reasonable inference for my project] Relative to your framework, this paper is best seen as a partial correction to opportunity neglect. It is not a full theory of (A), but it is clearly anti–independence-of-demand conditions in a positive sense: market constraints materially affect realized outcomes and therefore should not be suppressed when thinking about opportunities. supported by 

# Relation to Bargain et al. (2013)

This paper is closely related to the broader structural labor supply and tax-benefit microsimulation literature in which Bargain and coauthors operate, but its distinctive contribution is to add labor demand to that framework. Relative to benchmark labor-supply welfare simulations, its novelty lies in showing that supply-side responses may materially overstate employment effects when demand is not perfectly elastic. [reasonable inference for my project] supported by 

# Relation to opportunities vs preferences

This paper is important for the opportunities-versus-preferences distinction in a specific and limited way. It does not model individual opportunity sets, but it clearly argues that labor-market outcomes are not just preference revelations from the supply side. They are also shaped by employer demand and equilibrium wage adjustments. 

So the paper should not be read as a full opportunity-set paper, but it is a strong warning against treating labor supply estimates as if they directly revealed realized opportunities or employment outcomes. For your project, that warning is valuable. It says that even before building a full (A_i)-model, one must not ignore the market-side constraints that intervene between preferences and realized bundles. [reasonable inference for my project] supported by 

# Useful quotations / formulas

The key conceptual statement is already in the abstract: demand effects “offset about 25% of the positive labor supply effect of the policy reform.” This is the cleanest summary of the paper’s main empirical message. 

Equation (1) on page 131 gives the structural labor supply utility specification, while Equations (2)–(6) on pages 131–132 define the translog labor demand side and the resulting own- and cross-wage elasticities. These are the paper’s core structural formulas. 

Figure 1 on page 133 is especially useful: it graphically shows how a positive labor supply shift initially moves employment from (E_A) to (E_B), but once demand is downward sloping, wage adjustments and further supply responses push the economy to a new equilibrium (Z) with a smaller employment increase than the supply-only prediction. 

Table 2 on page 134 and Table 3 on page 135 are the most important empirical displays. Table 2 shows the size of labor-demand offsets by household type, skill, and gender. Table 3 shows the detailed convergence path of hours and wage changes across iterations. 

# Suggested tags

labor-demand-effects, structural-labor-supply, partial-equilibrium-microsimulation, workfare, linked-employer-employee-data, Germany, demand-side-constraints, policy-simulation

# My quick takeaway

This is a high-priority methodological paper for your corpus. It does not provide a RURO model or an axiomatic well-being framework, but it makes an important corrective point: structural labor supply simulations that ignore labor demand can substantially overstate employment effects. For your JMP, the main value of the paper is as a disciplined reminder that realized labor-market outcomes reflect not only preferences and tax incentives, but also market-side constraints.
