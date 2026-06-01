---

title: "Designing Optimal Taxes with a Microeconometric Model of Household Labour Supply"
authors: ["Rolf Aaberge", "Ugo Colombino"]
year: 2006
outlet: "Statistics Norway, Discussion Papers No. 475"
country_or_context: "Norway"
population: "Singles and married/cohabiting couples in Norwegian microdata; age coverage is partly unclear from paper"
data_period: "1994"
shelf: "optimal_taxation_structural_labour_supply_eop"
tags: ["optimal taxation", "structural labour supply", "random utility", "latent opportunities", "quantity constraints", "microsimulation", "equality of opportunity", "equality of outcome", "Norway"]
priority: "very high"
read_status: "extracted"
------------------------

# Full citation

Aaberge, Rolf, and Ugo Colombino. 2006. *Designing Optimal Taxes with a Microeconometric Model of Household Labour Supply*. Discussion Papers No. 475, Statistics Norway, Research Department. 

# One-sentence contribution

The paper develops a structural random-utility labour-supply model with heterogeneous preferences and heterogeneous job opportunities, and uses it directly as the computational device for optimal tax design under fixed revenue, comparing both equality-of-outcome and equality-of-opportunity social criteria.

# Why this paper matters

This paper matters because it is not only a structural labour-supply paper but also an unusually explicit attempt to connect positive microeconometric modelling with normative tax design. Instead of estimating elasticities and then inserting them into external optimal-tax formulas, it uses the estimated model itself to search over tax schedules. That internal consistency is highly relevant for any project that wants to keep together behaviour, constraints, and welfare evaluation.

It also matters for your research because the paper treats opportunities on two distinct levels. In the positive labour-supply model, opportunities are represented through a density of available jobs, so choice sets are heterogeneous and latent rather than universal. In the normative part, the paper separately introduces Roemer-style equality of opportunity, where circumstances and effort are distinguished. These two levels are not the same object, but their coexistence is precisely what makes the paper important for your (W(z,R,A;y)) agenda.

# Core research question

Can optimal income-tax schedules be designed empirically by maximizing social welfare over a class of tax rules using a flexible structural model of household labour supply, and how do the resulting schedules differ under equality-of-outcome and equality-of-opportunity criteria?

# Economic setting and context

The paper studies Norway, using household microdata for 1994 and holding fixed the contemporaneous transfer, income-support, and social-assistance system while varying the personal income-tax schedule. The exercise is explicitly application-specific rather than intended as a universally valid closed-form result.

The empirical environment includes both single individuals and couples, and the authors emphasize that joint household decisions, quantity constraints, and detailed tax rules matter for tax design. The paper is therefore located in the structural public-economics tradition rather than in reduced-form policy evaluation. 

# Model / theoretical framework

The model class is a structural random-utility labour-supply model that extends the standard multinomial logit framework. For a single person, the agent chooses among jobs characterized by hours (h), wage (w), and other job or match characteristics (j), subject to the budget constraint (c=f(wh,I)), where (I) is exogenous non-labour income and (f) is the tax rule. The choice set (B) includes market and non-market opportunities. 

A central feature is that the feasible opportunity set is not treated as a universal deterministic menu. Instead, because the analyst does not observe the full set (B), the paper represents it through a probability density (p(h,w,j)) over available opportunities. This allows the relative availability of jobs with different hours, wages, and other characteristics to differ across individuals. Quantity constraints are therefore not just an afterthought; they are part of the model architecture. 

The framework is both positive and normative. Positively, it models behavioural choices under heterogeneous preferences and heterogeneous opportunities. Normatively, it introduces a common individual welfare function and then aggregates welfare via either equality-of-outcome or equality-of-opportunity social criteria. The optimal-tax problem is solved computationally over a class of piecewise-linear tax schedules.

# Key objects

The main positive objects are the household-specific utility functions, the stochastic random-utility component, the disposable-income mapping (f), and the opportunity density (p(h,w,j)). The choice density combines systematic utility and availability, so realized choice depends jointly on preferences and opportunities. 

The main normative objects are the common individual welfare function (V), the rank-dependent equality-of-outcome social welfare functions (W_k), and the equality-of-opportunity counterparts (\widetilde{W}_k). The EOp criterion relies on a partition of individuals into circumstance types and interprets within-type rank as effort. 

The main policy object is a 6-parameter piecewise-linear income-tax rule with exemption level (E), three marginal tax rates ((\tau_1,\tau_2,\tau_3)), and two bracket thresholds ((Z_1,Z_2)). 

# Data

The paper uses Norwegian household microdata for 1994. The abstract states that the model is based on Norwegian household data for 1994. The appendix says estimation uses the 1995 Survey of Level of Living, which appears to be the survey source containing 1994 income information.

There is some ambiguity about age coverage. Section 6 states that the simulation exercise concerns single females, single males, and couples between ages 20 and 62, whereas the appendix says the estimation sample is restricted to ages 18 to 54. This should be treated as [unclear from paper] unless checked against the longer companion version. 

# Identification logic

Identification is structural and mainly parametric. The model is estimated by maximum likelihood using the random-utility choice density implied by the utility specification, the opportunity density, and the extreme-value assumption for the stochastic utility component. Wage offers are modelled parametrically, and hours opportunities are also given a parametric structure. 

The paper does not rely on quasi-experimental variation. Instead, it relies on functional-form assumptions, exclusion and structure embedded in wage, hours, and opportunity densities, and on observed variation in household characteristics and choices. This is a strong structural-identification strategy rather than a design-based one. [reasonable inference for my project] supported by 

Identification of welfare-relevant opportunity differences is partial and indirect. On the positive side, opportunities are inferred through estimated opportunity densities. On the normative side, equality of opportunity is operationalized through father’s education rather than through observed feasible job sets. So the paper identifies neither actual opportunity sets nor a clean decomposition of welfare into preference and opportunity components in your sense. [reasonable inference for my project] supported by

# Estimation / empirical strategy

The empirical strategy is to estimate separate structural utility functions for single females, single males, and couples, together with common opportunity-density components for jobs, hours, and wages. The full model contains 78 parameters capturing heterogeneity in preferences and opportunities. Estimation is by maximum likelihood.

After estimation, the authors compute wage and non-labour-income elasticities by stochastic simulation. These are not the final policy objects but diagnostic summaries of behavioural responses. They then simulate the effects of alternative tax rules, impute equivalent income, compute individual welfare with the common welfare function, aggregate through (W_k) or (\widetilde{W}_k), and iterate over tax parameters until social welfare is maximized subject to constant total tax revenue.

The optimization is performed in two versions: one unconstrained, which yields a 100 percent top marginal tax rate, and one constrained version imposing (\tau_3 \leq 0.6). Tables 6.2 and 6.3 on page 21 are the main tax-rule result tables. The figures on pages 25–26 graph the optimal EO schedules against the current rule. 

# Treatment of preferences

Preferences are heterogeneous in the behavioural model. The paper estimates different utility functions for single females, single males, and couples, and allows utility to depend on consumption, leisure, age, sector, and family composition. Thus, the behavioural side is explicitly preference-heterogeneous.

However, the paper is equally explicit that heterogeneous behavioural utility functions cannot simply be treated as interpersonally comparable welfare functions. To solve this, it imposes a common individual welfare function (V), estimated separately for social evaluation. This is analytically important because it separates behaviour-generating preferences from the normative welfare metric.

# Treatment of opportunities / constraints

This is one of the paper’s strongest sections for your purposes. The paper models opportunities explicitly on the positive side through the density (p(h,w,j)) of available jobs. The analyst does not observe the full opportunity set (B), so opportunities are represented probabilistically. This allows job availability to differ across individuals and allows for quantity constraints and hours restrictions in the labour market. 

The paper therefore does not assume a universal identical choice set. Nor does it reduce labour supply to a choice over hours alone. Agents choose job packages, and jobs differ in wage rates as well as other characteristics. In this sense, the paper is much closer to a latent-opportunity or RURO-type empirical logic than to standard deterministic hours-grid labour-supply models. [reasonable inference for my project] supported by 

At the same time, the paper’s normative equality-of-opportunity concept is not based on actual feasible job sets. Instead, “circumstances” are defined by father’s years of education, and within-type rank is interpreted as effort. So the paper has two distinct opportunity notions: a positive opportunity-density notion in the labour-supply model, and a normative circumstances notion in the EOp evaluation. They should not be conflated. 

Hence the paper helps distinguish both preference heterogeneity and opportunity heterogeneity, but only partially and on different conceptual layers. It does not deliver a unified observed feasible-set object (A). It also does not isolate demand-side constraints in a fully nonparametric way; they enter through latent opportunity densities.

# Welfare / normative object

The paper is explicitly normative in its tax-design stage. The individual welfare object is a common welfare function (V(c,h,s)), adjusted for age, children, and public-sector work, with couples’ income divided by (\sqrt{2}) to allow interpersonal comparability across heterogeneous households. The function is increasing and concave in income and leisure. Table 4.1 on page 14 reports the estimated parameters. 

Social aggregation under equality of outcome uses the rank-dependent family (W_k=\int_0^1 p_k(t)F^{-1}(t)dt), where (k) indexes inequality aversion. Under equality of opportunity, the paper adopts and extends Roemer’s criterion. Circumstances are defined by father’s education; effort is proxied by rank within the type-specific welfare distribution; and the paper defines generalized EOp welfare functions (\widetilde{W}_k) that allow varying weight profiles, rather than only the pure Roemer mean-of-the-worst-distribution criterion. 

This is directly relevant for thinking about responsibility versus compensation. The paper explicitly states that the planner may want to correct inequality due to opportunities or circumstances beyond control, but not inequality due to effort. That is an explicit compensation-versus-responsibility distinction. However, it is not framed in terms of feasible job sets (A), and it does not use reference opportunity sets. 

For decomposition, the paper is relevant but only in a specific Roemerian sense. It does not decompose inequality into preferences, actual opportunity sets, and pay schedules in your intended (W(z,R,A;y)) sense. But it does operationalize a decomposition of welfare differences into circumstance-related versus effort-related components through type distributions and rank. 

# Main findings

The core policy finding is that the computed optimal tax rules are more progressive than the 1994 Norwegian schedule. Under both EO and EOp criteria, the optimal rules imply lower marginal tax rates on low and average income levels and higher rates on sufficiently high incomes, while also delivering a lower average tax rate than the current system.

A striking result is that, in the unconstrained optimization, the top marginal tax rate always becomes 100 percent. Even when the authors impose the practical restriction (\tau_3 \le 0.6), the general qualitative pattern remains: relatively low bottom and middle rates, higher top rates, and substantial gross-income expansion through labour-supply responses. Tables 6.2 and 6.3 on page 21 are the key numerical summaries. 

The behavioural mechanism is that labour supply is much more elastic for low-income households than for high-income households, and married women are more elastic than married men. Table 3.1 on pages 8–9 and Table 3.2 on page 10 are central here. The paper draws from these elasticities the implication that efficiency arguments do not necessarily support flattening the marginal-tax profile or lowering top rates. 

The welfare comparison between EO and EOp is also important. The paper finds that the corresponding optimal tax rules are very similar, and even suggests that EOp can imply slightly more progressive taxation in the empirical implementation. This is notable because EOp is often interpreted as less interventionist than EO. 

# Main limitations

A first limitation is that the paper uses two different opportunity concepts without integrating them into a single explicit welfare framework. On the behavioural side, opportunities are latent job densities; on the normative side, opportunities are circumstances proxied by father’s education. This is interesting, but also conceptually fragmented. [reasonable inference for my project] supported by

A second limitation is that equality of opportunity is operationalized through only one observed circumstance variable, father’s education. That is a narrow proxy for opportunity, and it is far from an explicit feasible-set representation. For your project, this means the paper is suggestive for compensation theory but not a direct empirical implementation of opportunity sets (A). 

A third limitation is identification. The model is structurally rich but strongly parametric, and there is no external causal design. The credibility of counterfactual tax simulations depends on the maintained assumptions about utility, opportunity densities, wage offers, and shock structure. [reasonable inference for my project] supported by 

A fourth limitation is the realism of the top-rate result. The unconstrained optimum produces a 100 percent top marginal tax rate, which the authors themselves treat as impractical and therefore also analyze under a 60 percent cap. This indicates that the result is partly driven by model structure and missing margins of response. 

A fifth limitation is that the paper does not produce a decomposition of inequality into preferences, opportunities, and pay schedules in a way directly usable for your individual well-being project. It remains a social-welfare/tax-design paper rather than an individual-measure axiomatic paper. [reasonable inference for my project] supported by 

# Relevance for my JMP

## possible use for framing

This paper is very useful for framing a bridge between structural labour-supply estimation and fairness-based policy evaluation. It shows that one can keep a rich behavioural model and still impose an explicitly responsibility-sensitive social criterion.

## possible use for model design

It is highly useful for model design because it represents opportunities as latent job densities rather than collapsing the problem into one wage per person and a universal hours menu. That feature is close to the kind of latent-job modelling that is relevant for RURO-style work. 

## possible use for identification

It is useful mainly as an example of structural identification under internally consistent behavioural and policy simulation assumptions. It is less useful if your goal is external causal identification of preferences or opportunity effects. [reasonable inference for my project] supported by 

## possible use for welfare measurement

This is one of the strongest uses. The paper explicitly separates behavioural utility from the planner’s welfare metric and therefore avoids the naive aggregation of heterogeneous utilities. That is directly relevant for your concern with interpersonal comparability and the construction of welfare measures.

## possible use for decomposition

Directly, the paper offers a Roemer-type decomposition into circumstances and effort, not a decomposition into (R), (A), and (y). Indirectly, however, it suggests that a future decomposition could be built by combining its behavioural opportunity-density logic with your more explicit opportunity-set framework. [reasonable inference for my project] supported by

## possible use for comparative application

As an application, it is Norway-specific. But the conceptual template is portable: estimate a structural model with heterogeneous preferences and constraints, impose a welfare criterion, and search computationally over tax schedules. The same architecture could be adapted to other countries or to comparative microsimulation settings.

# Research questions this paper inspires

1. How can a latent-opportunity labour-supply model with density (p(h,w,j)) be reformulated so that the opportunity object becomes an explicit feasible set (A) suitable for normative analysis?

2. Can a Roemer-style responsibility/compensation distinction be embedded in an individual well-being measure (W(z,R,A;y)) rather than only in a social welfare criterion over distributions?

3. How sensitive are optimal tax results to alternative empirical definitions of “circumstances,” and what happens if circumstances are proxied by estimated opportunity sets rather than family background?

4. Can one separate preference heterogeneity from opportunity heterogeneity empirically in a way that is strong enough to support decomposition of welfare inequality into (R)-driven and (A)-driven components?

5. Is the similarity between EO-optimal and EOp-optimal tax rules a robust structural result, or is it specific to this Norwegian specification and this narrow operationalization of circumstances?

# Challenge to this paper

The main challenge is that its positive and normative treatments of “opportunity” are not unified. The labour-supply model’s opportunity concept is a latent density of available jobs, while the equality-of-opportunity criterion is built from father’s education and within-type welfare ranks. Those are both defensible modelling choices, but they are not the same object, and the paper does not provide a theory that links them.

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper clearly distinguishes realized choices from the opportunity side of the problem in the behavioural model by introducing a latent opportunity density (p(h,w,j)), and it separately distinguishes behavioural preferences from welfare evaluation by estimating a common welfare function (V). It also explicitly introduces a responsibility-sensitive social criterion through the EO/EOp distinction.

[reasonable inference for my project] A natural translation into your notation is as follows. The realized bundle (z) would correspond to the chosen post-tax income–hours/job package. Preferences (R) correspond to the heterogeneous household utility functions. The feasible set (A) is not directly observed, but the paper’s (p(h,w,j)) is a latent statistical representation of opportunity availability. The pay schedule (y) corresponds partly to wage offers embedded in jobs and partly to the tax rule mapping gross income into disposable income. supported by

[unclear from paper] The paper does not define an individual well-being measure (W(z,R,A;y)), does not study axioms such as independence of (A) or independence of (y), and does not ask whether welfare should be invariant to preferences over infeasible jobs. It also does not distinguish actual opportunity sets from reference opportunity sets in the manner of your current project.

[reasonable inference for my project] In your taxonomy, the paper is closest to responsibility for opportunities and decomposition of inequality into ethically relevant and irrelevant sources, but only at the social-evaluation level. It is not close to independence of (A); if anything, it insists that opportunities matter behaviourally. It is not close to independence of (y) either, because tax and wage mappings are central. It is not a laissez-faire evaluation. It is better read as a precursor for responsibility-sensitive empirical welfare analysis with latent opportunities. supported by

# Relation to Bargain et al. (2013)

[not central]

# Relation to opportunities vs preferences

This paper is highly relevant here because it does not simply treat all heterogeneity as preference heterogeneity. It explicitly allows both preferences and opportunities to vary across decision units. That is already a major conceptual advance over many structural labour-supply models.

But it stops short of giving a unified empirical or normative theory of opportunities versus preferences. Behavioural opportunities are latent job densities, while normative opportunity disadvantage is proxied by parental education. Thus, the paper is best viewed as a strong empirical bridge paper rather than a final conceptual solution.

# Useful quotations / formulas

The key behavioural formula is the choice density
[
\varphi(h,w,j)=\frac{v(f(wh,I),h,j),p(h,w,j)}{\iiint_B v(f(xy,I),y,z),p(x,y,z),dx,dy,dz},
]
which shows directly that realized choices reflect both attractiveness and availability. 

The key individual welfare formula is
[
\log V(c,h,s)=\frac{c^{\gamma_1}-1}{\gamma_1}+\frac{L^{\gamma_3}-1}{\gamma_3}+\text{demographic and sector terms},
]
with couples’ disposable income adjusted by (\sqrt{2}) for interpersonal comparability. 

The key EO and EOp social criteria are
[
W_k=\int_0^1 p_k(t)F^{-1}(t),dt
\quad\text{and}\quad
\widetilde{W}_k=\int_0^1 p_k(t)\min_j F_j^{-1}(t),dt.
]
These formulas capture the paper’s central normative distinction between equality of outcome and equality of opportunity. 

# Suggested tags

optimal-taxation, structural-labour-supply, random-utility, latent-opportunities, quantity-constraints, equality-of-opportunity, Roemer, equality-of-outcome, microsimulation, Norway

# My quick takeaway

This is a very important paper for your corpus. It is more relevant than a standard optimal-tax paper because it combines three elements that are usually separated: structural labour-supply estimation, explicit latent opportunity modelling, and responsibility-sensitive welfare evaluation. It does not yet give you a (W(z,R,A;y)) framework, and its opportunity concept is split between behavioural job densities and Roemer-style circumstances. But precisely for that reason, it is a valuable intermediate paper: it shows how far one can go empirically before the full axiomatic integration you are trying to develop.
