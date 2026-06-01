---

title: "Accounting for family background when designing optimal income taxes: a microeconometric simulation analysis"
authors: ["Rolf Aaberge", "Ugo Colombino"]
year: 2012
outlet: "Journal of Population Economics"
country_or_context: "Italy"
population: "Single females, single males, and couples in Italy; approximately the labour force aged 19–54"
data_period: "1993"
shelf: "equality_of_opportunity_optimal_taxation"
tags: ["equality of opportunity", "equality of outcome", "optimal taxation", "structural labour supply", "microsimulation", "family background", "Italy", "Roemer", "opportunity vs effort"]
priority: "very high"
read_status: "extracted"
------------------------

# Full citation

Aaberge, Rolf, and Ugo Colombino. 2012. “Accounting for family background when designing optimal income taxes: a microeconometric simulation analysis.” *Journal of Population Economics* 25: 741–761. 

# One-sentence contribution

The paper develops an extended Roemer-style equality-of-opportunity criterion and uses a microeconometric labour-supply model for Italy to identify second-best optimal income tax-transfer rules that depend only on income while accounting normatively for family background. 

# Why this paper matters

This paper matters because it is one of the clearest attempts to connect structural labour-supply microsimulation with a responsibility-sensitive normative criterion. Unlike standard optimal-tax papers that optimize an equality-of-outcome social welfare function, this paper asks how tax design changes once family background is treated as a circumstance beyond individual control. 

For your project, the paper is especially valuable because it keeps separate three layers that are often conflated: observed outcomes, the positive behavioural model generating those outcomes, and the normative criterion used to evaluate them. It is not an individual well-being paper in your exact (W(z,R,A;y)) sense, but it is directly relevant to the compensation-versus-responsibility problem and to the question of how opportunity-related inequality can be embedded in policy evaluation. 

# Core research question

What income tax-transfer rule is optimal, within second-best rules that depend only on income, when the social objective is equality of opportunity defined with respect to family background rather than equality of outcome? 

# Economic setting and context

The empirical application is Italy, using 1993 data from the Bank of Italy Survey of Household Income and Wealth. The paper considers single females, single males, and couples aged 19–54, and uses estimated labour-supply models to simulate behavioural responses to alternative tax-transfer rules. The comparison is between equality-of-opportunity and equality-of-outcome tax design, with family background proxied by father’s education. 

The policy environment is explicitly second-best. The authors do not allow the tax rule to depend on type or circumstances, even though types are observable in the data. The tax-transfer rule is constrained to depend only on income, just as in standard Mirrleesian second-best taxation. That restriction is central to the interpretation of the results. 

# Model / theoretical framework

The paper combines a normative EOp/EO framework with a positive microeconometric labour-supply model. The labour-supply model is not rederived in the article itself because it is described in the electronic supplementary material, but the paper states clearly that it is a relatively sophisticated household labour-supply model that treats singles and couples, models partners’ decisions jointly, and accounts for quantity constraints on hours. 

The agent chooses labour supply under alternative tax rules, and the model is used as a simulation engine for counterfactual tax design. The normative exercise is not to estimate preferences from scratch within the paper, but to use the estimated model to simulate how disposable incomes and labour supply would change under alternative rules. Equivalent incomes are then constructed and evaluated by EOp or EO criteria. 

Opportunities are modeled explicitly in the normative sense of Roemerian “circumstances,” not in the sense of observed feasible job sets. Types are defined by father’s education, and rank within the type-specific income distribution is interpreted as effort. Thus, the paper is normative and positive, but its “opportunity” concept is circumstance-based rather than feasible-set-based. It also uses a labour-supply model with quantity constraints, so constraints enter positively, but the normative object is still not an explicit set (A). 

# Key objects

The main normative objects are the EO rank-dependent social welfare functions (W_k), the pure EOp welfare function (\widetilde{W}_\infty), and the extended EOp welfare functions (\widetilde{W}_k). The EO functions aggregate the full income distribution, while the EOp functions focus on the worst-off type distribution defined pointwise across effort ranks. 

The key type object is family background, proxied by father’s education. Individuals are partitioned into three types: less than 5 years of paternal education, 5–8 years, and more than 8 years. Within-type rank is used as the effort measure. 

The key policy objects are two-parameter affine tax rules and three-parameter tax rules. In the affine case, the rule is a constant marginal tax rate plus a universal lump-sum transfer or tax. In the three-parameter case, the rule has a lump-sum component and two marginal tax rates separated by a kink at average individual gross income. 

# Data

The paper uses the 1993 Bank of Italy Survey of Household Income and Wealth. The sample includes single females, single males, and couples aged 19–54, and is intended to cover approximately the labour force. The paper itself does not provide the full underlying estimation details in the main text; those are delegated to the electronic supplementary material. 

Father’s education is the key circumstance variable used to define EOp types. Disposable household income is transformed into adult-equivalent income by dividing by the square root of household size before building type-specific income distributions. 

# Identification logic

Identification is mainly structural and simulation-based. The paper does not rely on quasi-experimental variation in the modern causal-inference sense. Instead, it relies on an estimated microeconometric labour-supply model and then simulates behavioural responses under counterfactual tax rules. The crucial assumptions are therefore those embedded in the estimated household labour-supply model and in the normative partition of individuals into types by father’s education. [reasonable inference for my project] 

Normative identification of opportunity disadvantage is also narrow. The paper identifies “circumstances” with one observed background variable, father’s education. This is coherent within Roemer’s framework, but it is not a full identification of all relevant opportunity components, nor does it identify feasible opportunity sets in your sense. [reasonable inference for my project] 

# Estimation / empirical strategy

The empirical strategy is to estimate labour-supply behaviour using a household microeconometric model and then search computationally over tax-rule parameter spaces. For each candidate tax rule, the model simulates labour-supply responses, converts household disposable income into equivalent income, builds type-specific income distributions, computes the chosen EOp or EO social objective, and iterates until the objective is maximized under a constant-revenue constraint. 

The paper first studies two-parameter affine tax rules in order to remain comparable with Roemer et al. (2003), and then studies a more flexible three-parameter class. This comparison is methodologically important because some of the striking results, especially the optimality of a pure lump-sum tax under some EOp criteria, are shown to depend partly on the class of tax rules being searched over. Tables 2, 3, and 7 are central here. 

# Treatment of preferences

The paper does not center its contribution on preference heterogeneity as an object of direct welfare decomposition. Preferences enter through the underlying microeconometric labour-supply model, which is rich enough to simulate heterogeneous labour-supply responses across singles and couples. The main text repeatedly emphasizes heterogeneous labour-supply behaviour and notes that these heterogeneous responses are crucial in shaping the optimal tax rules. 

However, the normative analysis is not preference-based in the sense of taking heterogeneous utility functions as the welfare object. Instead, the paper evaluates tax systems through distributions of adult-equivalent income under EO or EOp criteria. In other words, preference heterogeneity matters behaviourally, but the welfare metric used in the main analysis is income-based, not a direct well-being measure over consumption and leisure. 

# Treatment of opportunities / constraints

Normatively, opportunities are treated as “circumstances” beyond individual control, operationalized by paternal education. This is the paper’s central opportunity concept. Individuals are divided into three types by family background, and EOp seeks to reduce differences attributable to those circumstances while treating within-type rank as effort. 

Positively, the paper also uses a labour-supply model that accounts for quantity constraints on hours and jointly models partners’ decisions. This means the empirical model does contain constrained opportunities in the labour-market sense. But the article does not make those labour-market opportunities the normative object. It is therefore important not to confuse the paper’s positive treatment of labour-market constraints with its normative treatment of opportunity as family background. 

The paper helps distinguish opportunity heterogeneity from effort heterogeneity in a Roemerian sense. It does not, however, distinguish preference heterogeneity from opportunity heterogeneity in the stronger (R) versus (A) sense you are interested in, nor does it model actual feasible job sets explicitly as normative objects. 

# Welfare / normative object

The paper is explicitly normative. Its main normative contribution is the development of an extended EOp criterion that lies between pure EOp and more conventional EO. The pure EOp criterion focuses on the average income of the worst-off type-specific rank distribution:
[
\widetilde{W}_\infty=\int_0^1 \min_j F_j^{-1}(t),dt.
]
The extended EOp criterion instead applies the same family of inequality-averse rank weights used under EO:
[
\widetilde{W}_k=\int_0^1 p_k(t)\min_j F_j^{-1}(t),dt.
]
This allows concern for inequality within the worst-off distribution as well as between types. 

Under EO, the paper uses the rank-dependent welfare functions
[
W=\int_0^1 p(t)F^{-1}(t),dt,
]
with the familiar Bonferroni-, Gini-, and utilitarian-type cases. The paper is explicit that EO ignores the source of inequality, whereas EOp distinguishes inequality due to circumstances from inequality due to effort. 

This is directly useful for thinking about responsibility versus compensation. The paper explicitly says that bad outcomes associated with lack of effort are less legitimate targets of redistribution than bad outcomes attributable to circumstances. That is an explicit compensation/responsibility distinction. However, the object is income distribution by type, not an individual well-being measure over realised bundle, preferences, opportunity set, and pay schedule. 

# Main findings

The paper’s central empirical finding is that EOp does not mechanically imply less redistribution than EO. In fact, in the simulations presented, EO often supports the pure lump-sum tax, whereas the extended EOp criterion can imply more redistributive tax structures with positive marginal rates and transfers, especially when the planner places substantial weight on inequality within the worst-off distribution. The paper is explicit that its results do not conform to the common expectation that EO is always more interventionist than EOp. 

For two-parameter affine tax rules, the EOp-optimal rule depends strongly on the value of (k). When (k \geq 3), the optimal rule is a pure lump-sum tax with zero marginal tax rate. When (k \leq 2), the optimal rule involves a high marginal tax rate and a positive lump-sum transfer. Tables 2 and 3 on pages 750–751 summarize these results, and Figs. 1–3 illustrate the associated type distributions and revenue-constant rule sets. 

For three-parameter tax rules, the pattern becomes richer. The pure lump-sum tax remains EOp-optimal under pure EOp ((k=\infty)), but for lower (k) the optimal rule includes positive marginal tax rates, and in some cases a strongly redistributive structure. Table 7 is the key summary. The paper interprets these results as evidence that heterogeneous labour-supply responses of disadvantaged groups are crucial for optimal-tax design under EOp. 

When the EO criterion is applied, the universal lump-sum tax is always optimal within the tax-rule classes studied. Table 9 shows that this is driven by large efficiency gains that dominate the associated disequalizing effects in the EO objective. This is one of the most important comparative findings in the paper. 

# Main limitations

A first limitation is that the opportunity concept is narrow. The paper equates circumstances with father’s education, which is reasonable as a proxy for family background but clearly incomplete as a measure of opportunity. For your project, this means the paper is relevant to compensation for background circumstances, but it is not yet a broad theory of opportunities. 

A second limitation is that welfare is income-based. The paper itself notes in the conclusion that policy prescriptions might change if the value of leisure were included in the measurement of individual welfare, especially because some tax rules generate large labour-supply responses. This is a major limitation from the standpoint of labour-supply welfare analysis. 

A third limitation is that the paper does not construct actual feasible opportunity sets. It works with type-specific income distributions and simulated labour-supply responses, not with explicit job-set objects (A). This is important for your framework, because the paper’s opportunity object is social-background-based rather than set-based. [reasonable inference for my project] 

A fourth limitation is that some striking results, especially the optimality of the pure lump-sum tax, depend on the class of tax rules searched over and on the income-based welfare metric. The paper itself partly addresses this by moving from two-parameter to three-parameter rules, but the general point remains. 

A fifth limitation is that the decomposition is only into type-related versus within-type inequality under EOp. It does not decompose inequality into preferences, opportunities, pay schedules, and effort in the richer structural sense you are interested in. 

# Relevance for my JMP

## possible use for framing

This paper is highly useful for framing the compensation-versus-responsibility part of your JMP. It gives a concrete example of how a policy evaluation can be made sensitive to background circumstances without letting the tax rule directly depend on those circumstances.

## possible use for model design

It is moderately useful for model design. The underlying microeconometric model includes joint household labour supply and quantity constraints, which is relevant. But the main design lesson is normative rather than econometric: one can overlay a responsibility-sensitive welfare criterion on top of a labour-supply simulation model.

## possible use for identification

It is of limited use for causal identification. The paper is structural and simulation-based, not quasi-experimental. Its more important lesson is how to operationalize an opportunity-sensitive social criterion in a second-best tax environment.

## possible use for welfare measurement

It is very useful here. The paper shows how one can move from pure EO to an intermediate criterion that partly compensates for background circumstances and partly respects within-type differences. That is directly relevant for designing intermediate well-being measures or axioms.

## possible use for decomposition

It is useful as a partial decomposition template. The paper decomposes inequality into between-type and within-worst-off-type components under EOp. This is not your (R/A/y) decomposition, but it is a serious normative decomposition of disadvantage sources.

## possible use for comparative application

It is useful comparatively because it extends Roemer et al. (2003) and explicitly contrasts its Italian microsimulation results with earlier simpler calibrated results. That makes it a good comparative reference point for how modelling detail affects normative prescriptions.

# Research questions this paper inspires

1. Can a Roemer-style circumstance/effort distinction be translated from type-specific income distributions into an individual well-being framework (W(z,R,A;y))?

2. How would the paper’s EOp prescriptions change if welfare were measured over income and leisure rather than over equivalent income alone?

3. Can family background be interpreted empirically as a determinant of feasible job sets (A), rather than merely as a type-defining circumstance?

4. Under what conditions does an extended EOp criterion imply more redistribution than EO, and when does the opposite occur?

5. Can one build a structural decomposition in which background circumstances affect both preferences (R) and opportunities (A), while the welfare criterion compensates only the latter?

# Challenge to this paper

The strongest challenge is that the paper’s opportunity concept is ethically sharp but economically thin. It identifies family background as a circumstance and uses it to define types, but it does not show how that background concretely maps into the opportunity sets individuals face in the labour market. As a result, the normative distinction between circumstance and effort is clearer than the economic mechanism linking background to actual feasible options. 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper is centrally about responsibility versus compensation. It treats family background as a circumstance beyond individual control and builds a social criterion that aims to correct inequality attributable to those circumstances rather than to effort. It also remains second-best by restricting tax rules to depend only on income. 

[reasonable inference for my project] In your notation, the paper is much closer to a framework that gives ethical weight to parts of (A) than to one that is independent of (A). However, its “opportunity” object is not an actual feasible job set. It is a type-defining background circumstance that shapes the normative comparison across people. Thus, it is useful for the ethical logic of compensation, but not yet for the explicit modelling of (A) as a job set. 

[reasonable inference for my project] The paper could be related to (W(z,R,A;y)) as follows. The realised bundle (z) is proxied by equivalent disposable income after behavioural adjustment. Preferences (R) are embedded in the underlying labour-supply model but are not the primary normative object. The feasible set (A) is not explicit, but family background can be interpreted as one determinant of opportunity conditions. The pay schedule (y) enters through the tax-transfer rule and the labour-income process. 

[unclear from paper] The paper does not define an individual well-being measure (W(z,R,A;y)), does not analyze independence of (A) or independence of (y), does not distinguish actual from reference opportunity sets, and does not ask whether individuals should be held responsible for preferences over infeasible jobs. Those are outside its explicit scope. 

[reasonable inference for my project] In your taxonomy, the paper is closest to responsibility for opportunities, compensation for background circumstances, and a primitive decomposition of inequality sources. It is not close to laissez-faire evaluation, not close to independence of (A), and only indirectly related to reference opportunity sets. 

# Relation to Bargain et al. (2013)

This paper is relevant to the same broad literature on structural labour supply, tax design, and welfare evaluation, but its distinctive contribution is the explicit use of an equality-of-opportunity criterion rather than the more usual equality-of-outcome framework. Relative to the benchmark welfare-and-labour-supply literature, its novelty lies less in labour-supply econometrics itself and more in the normative criterion imposed on top of the microsimulation exercise. In that sense, it is complementary to the Bargain-style welfare-and-labour-supply literature rather than a direct substitute for it. [reasonable inference for my project] 

# Relation to opportunities vs preferences

This paper is more useful for opportunities than for preferences. It does not principally ask how heterogeneous preferences should be treated normatively. Instead, it asks how redistribution should respond to inequality generated by background circumstances versus effort. That makes it directly relevant to the “opportunities” side of your agenda. 

But the opportunity notion remains type-based and circumstance-based, not feasible-set-based. So the paper is best read as a normative bridge from background-inequality models toward your more explicit jobs-and-wellbeing framework, not as a finished treatment of opportunities versus preferences. 

# Useful quotations / formulas

The key EO welfare function is
[
W=\int_0^1 p(t)F^{-1}(t),dt.
]
This is the benchmark equality-of-outcome object against which the paper contrasts EOp. 

The key pure EOp object is
[
\widetilde{W}_\infty=\int_0^1 \min_j F_j^{-1}(t),dt,
]
which averages the lowest type-specific income at each effort rank. 

The main theoretical innovation is the extended EOp criterion
[
\widetilde{W}_k=\int_0^1 p_k(t)\min_j F_j^{-1}(t),dt,
]
which adds inequality aversion within the worst-off type distribution. 

# Suggested tags

equality-of-opportunity, Roemer, family-background, optimal-taxation, structural-labour-supply, microsimulation, compensation-vs-responsibility, Italy, EO-vs-EOp

# My quick takeaway

This is a high-priority paper for the normative side of your corpus. It is not a jobs-as-feasible-sets paper, and it does not directly speak the language of (W(z,R,A;y)). But it is one of the most relevant papers for understanding how a responsibility-sensitive criterion can change optimal-tax prescriptions once background circumstances are treated as ethically compensable. For your JMP, it is especially useful as a bridge from Roemer-style circumstance/effort distinctions toward a more explicit opportunity-set-based theory of well-being.
