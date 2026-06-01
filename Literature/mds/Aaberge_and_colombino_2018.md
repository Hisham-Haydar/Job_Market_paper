---

title: "Structural Labour Supply Models and Microsimulation"
authors: ["Rolf Aaberge", "Ugo Colombino"]
year: 2018
outlet: "International Journal of Microsimulation"
country_or_context: "Methodological review with cross-country applications; substantial discussion of Norway, Italy, Sweden, Europe, the UK, and the US"
population: "Not a single estimation sample; survey of structural labour-supply applications for singles, couples, immigrants, single mothers, and broader working-age populations"
data_period: "Review article covering studies through 2018; illustrative evidence includes Norwegian data for 1979, 1986, 1994, 2006, and 2011"
shelf: "methodological_survey_structural_labour_supply_microsimulation"
tags: ["structural labour supply", "microsimulation", "discrete choice", "RURO", "random utility", "opportunity sets", "optimal taxation", "social welfare", "policy simulation", "review paper"]
priority: "very high"
read_status: "extracted"
------------------------

# Full citation

Aaberge, Rolf, and Ugo Colombino. 2018. “Structural Labour Supply Models and Microsimulation.” *International Journal of Microsimulation* 11(1): 162–197. 

# One-sentence contribution

The paper is a methodological survey that argues for structurally estimated labour-supply models in behavioural microsimulation, compares discrete-choice and random-utility–random-opportunities approaches, and explains how such models can be combined with welfare criteria to evaluate reforms and compute optimal tax-benefit systems. 

# Why this paper matters

This paper matters because it is one of the clearest overview pieces connecting structural labour-supply econometrics, behavioural microsimulation, social welfare evaluation, and empirical optimal taxation in one framework. It is not just a survey of techniques; it also defends a particular architecture in which household behaviour is structurally modeled, policy reforms are simulated computationally, and resulting outcomes are evaluated with explicit welfare criteria. 

For your project, it is especially valuable because it directly discusses the distinction between discrete-choice models and RURO models, the representation of opportunity sets, the role of heterogeneous preferences and opportunities, and the need to separate behavioural utility from welfare evaluation. It does not formulate a (W(z,R,A;y)) framework, but it is very close to the empirical and conceptual terrain in which such a framework would operate. 

# Core research question

How should labour supply be modeled within behavioural microsimulation for policy analysis, and what are the strengths, limitations, and welfare applications of the main structural approaches, especially the discrete-choice model and the random-utility–random-opportunities model? 

# Economic setting and context

This is a methodological review rather than a single-country empirical application. The paper surveys the evolution of behavioural microsimulation, the rise of structural labour-supply modelling from the mid-1990s onward, and the use of such models for tax-benefit reform analysis, in-work benefits, basic income schemes, flat taxes, and optimal taxation. It repeatedly draws illustrative evidence from Norway, Italy, Sweden, Europe, the UK, and the US. 

The context is explicitly public economics and microsimulation. The paper is concerned with settings where tax and benefit reforms create non-convex, heterogeneous, and policy-sensitive opportunity sets, and where reduced-form or purely non-behavioural exercises may be insufficient for ex ante policy evaluation. 

# Model / theoretical framework

The paper is a review of model classes rather than the presentation of one new estimated model. Its main theoretical distinction is between two labour-supply modelling approaches: the discrete-choice model and the random-utility–random-opportunities model. It also briefly discusses stochastic dynamic programming, non-unitary household models, and the taxable-income approach as alternative or complementary strands. 

In the discrete-choice model, the agent chooses among a finite set of hours or jobs, typically with an individual-specific fixed wage and a random term added to utility. The paper notes that this model is often interpreted in two different ways: either as classic random utility with unobserved utility components, or as a model with measurement or optimization error. This distinction matters for simulation and welfare interpretation. 

In the RURO model, the agent chooses among jobs characterized by hours, wages, and other job or match characteristics. The analyst does not observe the full opportunity set, so it is represented statistically through an opportunity density (p(w,h)) or (p(w,h,j)). This means that choices reflect both utility and the density of available opportunities. In that sense, the framework models opportunities explicitly, albeit as latent statistical objects rather than observed feasible sets. 

The framework is both positive and normative. Positively, the paper defends structural modelling of labour supply under heterogeneous preferences and heterogeneous opportunities. Normatively, it explains how behavioural microsimulation can be combined with common individual welfare functions and social welfare functions to evaluate reforms and identify socially optimal tax systems. 

# Key objects

The main positive objects are the utility function (U), the systematic utility component (v), the random utility component (\varepsilon), the tax-transfer rule (f), and the opportunity density (p(w,h)) or (p(w,h,j)). The paper emphasizes that in RURO, the density of opportunities is not a nuisance term but a central structural object because it represents the labour-demand side and the distribution of jobs available to households. 

The main normative objects are the common individual welfare function (V(y,h)), money-metric or preference-respecting welfare metrics, and social welfare functions of the primal or dual/rank-dependent type. The paper also formulates the computational optimal-tax problem as a maximization of social welfare subject to incentive-compatibility and budget constraints. 

# Data

Because this is a survey paper, it does not rely on one dataset. Instead, it reviews a large literature and uses illustrative empirical evidence from previous applications. It specifically refers to Norwegian evidence for 1979, 1986, 1994, 2006, and 2011 when discussing the evolution of labour-supply elasticities, and it cites applications for Sweden, Italy, the UK, Europe more broadly, and the US. 

The paper therefore does not have one unified empirical sample, one country, or one data period. Any attempt to treat it as a single empirical study would be misleading. [explicit in paper] 

# Identification logic

The paper is not itself an identification paper, but it takes a clear methodological position. It argues that ex ante policy evaluation requires structural models because one must identify policy-invariant primitives or parameters, whether the model is parametric or nonparametric, utility-based or agent-based, and whether the data are observational or experimental. This is one of the paper’s strongest explicit claims. 

The identification logic defended in the paper is therefore structural rather than design-based. It does not deny the value of reduced-form or experimental evidence, but argues that such evidence by itself is insufficient for ex ante evaluation unless embedded in a structural framework that identifies policy-invariant parameters. The paper also shifts attention from pure identification debates toward external validation and out-of-sample prediction as pragmatic criteria for evaluating structural models. 

This means that, for your purposes, the paper is more useful as a methodological defense of structural modelling than as a source of a specific identification strategy for separating (R), (A), and (y). [reasonable inference for my project] 

# Estimation / empirical strategy

The paper does not estimate one model in the article. Instead, it presents the structure of the main model classes and discusses how they are estimated and used in microsimulation. For discrete-choice models, it reviews the standard multinomial/conditional logit setup with optional “dummies refinement” or monetary cost adjustments. For RURO, it shows how the opportunity density can be factorized and estimated jointly with preferences, and how sampled choice sets can be used in practice. 

A major emphasis is on simulation rather than estimation alone. The paper distinguishes different procedures for producing policy predictions, discusses comparative statics versus short-run interpretations, and explains how equilibrium adjustments can be handled differently in DC and RURO models. In RURO, because opportunity densities already reflect the labour-demand side, policy simulation may require updating the density of available jobs to reflect new equilibrium conditions. 

# Treatment of preferences

The paper treats preference heterogeneity as central to structural labour-supply modelling. It explicitly notes that structural models are needed when preferences and opportunities are heterogeneous, and it surveys frameworks in which heterogeneity enters via random parameters, flexible functional forms, or household-specific utility structures. It also discusses the interpretation of the random term in DC models and how that interpretation affects whether the deterministic part of utility should be viewed as the “true” utility. 

At the same time, the paper is very careful not to equate behavioural utility with welfare. In the welfare section, it emphasizes the problems of interpersonal comparability and explains why estimated utility functions should not simply be aggregated for social evaluation. Instead, it reviews the use of common utility functions and alternative welfare metrics. This explicit separation between behavioural preferences and normative welfare evaluation is one of the paper’s most important features for your project. 

# Treatment of opportunities / constraints

This section is where the paper is most directly useful for your agenda. It repeatedly emphasizes that structural labour-supply models are especially needed when policies create complicated and non-convex opportunity sets and when opportunities are heterogeneous across households. The RURO model is presented precisely as a model in which the opportunity set is unknown to the analyst and represented by a probability density over jobs. 

The paper clearly states that RURO differs from standard DC models because the agent does not merely choose hours at a fixed wage. Instead, the household chooses among jobs that differ in hours, wage rates, and possibly additional characteristics, while the opportunity density captures the number or relative frequency of different jobs in the choice set. This is an explicit modelling of opportunities, although in latent density form. 

The paper also discusses quantity constraints, involuntary unemployment, and the representation of the labour-demand side. In RURO, involuntary unemployment can be represented by an empty or very poor market opportunity set. This is analytically important because it means that the opportunity object is not just a reduced-form residual but part of the model’s substantive interpretation. 

However, the paper does not move to a normative treatment of actual feasible sets. It does not define individual opportunity sets (A_i) as ethical objects or reference sets. It instead explains how latent opportunities are modeled positively in behavioural microsimulation. Thus, it helps distinguish opportunity heterogeneity from preference heterogeneity on the positive side, but not yet on the normative side of your project. 

# Welfare / normative object

The paper is not purely positive. A full section is devoted to social evaluation of policy reforms and empirical optimal taxation. It reviews the common-utility-function approach of Deaton-Muellbauer and Hammond, explains why interpersonal comparisons based directly on estimated behavioural utility functions are problematic, and presents a common individual welfare function (V(y,h)) defined over equivalent income and leisure. It also reviews alternative preference-respecting welfare metrics. 

At the social level, the paper reviews both primal and dual social welfare functions. It presents Atkinson-style primal welfare and Yaari/Weymark/Aaberge-style rank-dependent dual welfare functions, and explains how these may be used to rank policy reforms or define optimal tax problems. It therefore provides a clear methodological map from behavioural microsimulation to normative policy evaluation. 

This is directly relevant to your work on well-being measurement. The paper does not itself take a stand on responsibility for opportunities, compensation, or reference opportunity sets in an axiomatic way. But it does explain the available tools for moving from labour-supply choices to individual welfare and then to social evaluation, which is an indispensable intermediate step for your framework. [reasonable inference for my project] 

On decomposition, the paper does not provide a formal decomposition of inequality into preferences, opportunities, and pay schedules. It does, however, review the ingredients that such a decomposition would need: structural models of choices, explicit modelling of opportunities, and welfare metrics that do not collapse directly into revealed utility. [reasonable inference for my project] 

# Main findings

Because this is a survey paper, its “findings” are mainly methodological syntheses. First, it argues that RUM/RURO models currently offer the best compromise between sophistication and tractability for behavioural microsimulation. They can accommodate complicated tax rules, heterogeneous preferences, heterogeneous opportunities, and joint household decisions without the analytic rigidity of older approaches. 

Second, it argues that ex ante policy evaluation requires structural models. This is one of the most explicit claims in the paper: experimental or reduced-form evidence may be valuable, but it is not sufficient by itself for evaluating policies not yet implemented. The paper therefore provides a direct defense of structural modelling against anti-structural objections. 

Third, the paper emphasizes that labour-supply elasticities have evolved over time and vary systematically across groups. Using earlier Norwegian work as illustration, it notes that overall labour-supply responses have declined over time, that low-income individuals remain more responsive than high-income individuals, and that the labour-supply behaviour of women and men has become more similar, although important heterogeneity remains, especially for some immigrant groups. 

Fourth, in the optimal-tax discussion the paper stresses that computational microsimulation approaches can generate results quite different from those suggested by analytical Mirrlees/Saez-style exercises. In particular, it highlights results from the authors’ earlier work in which optimal tax systems are progressively increasing, sometimes feature negative bottom marginal rates, and differ sharply from the classic picture of high phase-out rates at the bottom and flatter top structures. 

# Main limitations

The first limitation is that the paper is a survey, not a single internally estimated and tested empirical model. It synthesizes many contributions and takes clear positions, but it does not itself resolve empirical disputes about which model class performs best in all settings. [explicit in paper] 

The second limitation, from your perspective, is normative. Although the paper reviews welfare evaluation and emphasizes the distinction between behavioural utility and welfare, it does not provide an axiomatic treatment of opportunities, responsibility, compensation, or reference opportunity sets. It remains at the level of methodological review and applied social-evaluation tools. [reasonable inference for my project] 

A third limitation is that the paper defends RURO as a positive model of opportunities but does not translate that opportunity object into a normatively explicit feasible-set framework. Thus, it is very helpful for modelling (A) empirically as a latent job distribution, but not for determining how (A) should enter a well-being measure. [reasonable inference for my project] 

A fourth limitation is that decomposition is mostly programmatic rather than implemented. The paper indicates how welfare functions and structural labour-supply models can be combined, but it does not itself deliver a decomposition of observed welfare inequality into preference, opportunity, and pay-schedule components. [explicit in paper / reasonable inference for my project] 

# Relevance for my JMP

## possible use for framing

This is one of the best framing papers for your empirical side. It gives a compact but intellectually serious justification for why a jobs-and-wellbeing project should use structural modelling, why opportunities should not be collapsed into preferences, and why welfare evaluation requires a separate normative layer.

## possible use for model design

It is highly useful for model design. The paper’s comparison of DC and RURO, especially its insistence that RURO explicitly models job opportunities and not only hours choice, is directly relevant to your interest in latent jobs and feasible job sets.

## possible use for identification

It is useful mainly as a methodological position paper. It does not provide a new identification design, but it clarifies why ex ante policy evaluation needs policy-invariant primitives and why validation and out-of-sample prediction matter for structural work.

## possible use for welfare measurement

It is very useful here. The discussion of common utility functions, preference-respecting metrics, and primal versus dual social welfare functions is directly relevant to the bridge from behavioural labour-supply estimation to well-being measurement.

## possible use for decomposition

Directly, it is limited. Indirectly, it is highly useful because it identifies the ingredients needed for decomposition: separate modelling of preferences and opportunities, non-trivial welfare metrics, and simulation-based counterfactual analysis.

## possible use for comparative application

It is useful because it surveys evidence and applications across several countries and policy types. That makes it a strong reference for situating your own project within a broad comparative and methodological literature.

# Research questions this paper inspires

How can the latent opportunity density in RURO be converted into an explicit individual feasible-set object (A) suitable for normative analysis rather than only positive estimation?

What welfare metric is most defensible when preferences are heterogeneous and labour-market opportunities are unequally distributed?

Can one build a decomposition of welfare inequality into components driven by preferences (R), opportunity sets (A), and pay schedules (y) using a RURO-style behavioural microsimulation model?

When do structural RURO models materially outperform simpler discrete-choice models in policy evaluation, and when is the extra complexity unnecessary?

How should equilibrium feedback in RURO models be incorporated when policy reforms change not only choices but also the density of available jobs?

# Challenge to this paper

The paper’s strongest challenge is that its positive modelling insights run ahead of its normative integration. It convincingly shows how opportunities can be modeled statistically through RURO and why structural models are needed for policy simulation, but it leaves open the hardest question for your project: how exactly should those modeled opportunities enter an ethically defensible individual well-being measure? 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper distinguishes sharply between behavioural utility used to simulate labour-supply choices and welfare functions used for social evaluation. It also emphasizes that opportunities can be heterogeneous and explicitly modeled, especially in RURO, through the density of available jobs. These two points make it directly relevant to a framework in which realized outcomes, preferences, and opportunities should not be conflated. 

[reasonable inference for my project] In your notation, the paper’s positive side maps naturally into (z), (R), (A), and (y): (z) is the realized post-tax job bundle, (R) is the household’s behavioural preference structure, (A) is approximated by the latent opportunity set or opportunity density of jobs, and (y) is the pay schedule combined with the tax-transfer rule. This mapping is not stated by the paper, but it is a reasonable and useful translation. 

[unclear from paper] The paper does not define a well-being measure (W(z,R,A;y)), does not study axioms such as independence of (A) or independence of (y), and does not discuss reference opportunity sets, IIJ, IPIJ, or responsibility for preferred jobs in your sense. Those are outside its explicit scope. 

[reasonable inference for my project] In your taxonomy, the paper is closest to the themes of explicit opportunity modelling, decomposition readiness, and the distinction between behavioural preferences and evaluative welfare metrics. It is not close to independence of (A); quite the contrary, it insists that opportunities matter behaviourally. It is also not close to laissez-faire evaluation, because it explicitly endorses distinct social welfare criteria for policy assessment. 

# Relation to Bargain et al. (2013)

This paper directly discusses Bargain et al. (2013) in the welfare section as an application of preference-respecting welfare metrics in labour-supply analysis. It presents that literature as a promising alternative to the common-utility approach, while also noting that different preference-respecting metrics can materially affect welfare conclusions depending on how they treat willingness to work. So Bargain et al. is central here, not peripheral, but as part of the welfare-evaluation debate rather than the opportunity-modelling debate. 

# Relation to opportunities vs preferences

This paper is one of the most useful methodological references for the opportunities-versus-preferences distinction on the positive side. RURO is explicitly presented as a model in which labour supply depends on both preferences and the density of available opportunities, whereas simpler DC models tend to be more restrictive in how they represent the opportunity side. 

On the normative side, however, the paper remains intermediate rather than definitive. It explains how welfare evaluation can be layered on top of behavioural models, but it does not fully theorize which inequalities should be attributed to preferences and which to opportunities, nor how that distinction should be encoded in an individual well-being measure. It is therefore a bridge paper rather than a final solution to the opportunities-versus-preferences problem. 

# Useful quotations / formulas

A central RURO choice-density formula is
[
\varphi(w,h)=
\frac{\exp(v(f(wh,I),h)),p(w,h)}
{\int!!\int_B \exp(v(f(xy,I),y)),p(x,y),dx,dy},
]
or its discrete analogue. This is central because it shows that observed choices are driven jointly by attractiveness and availability. 

A central welfare formula is the common individual welfare function
[
V(y,h)=
\left(\frac{y^{\gamma_1}-1}{\gamma_1}\right)\gamma_2
+
\left(\frac{L^{\gamma_3}-1}{\gamma_3}\right)\gamma_4,
]
with (L=1-h/8736), used as a common evaluative object rather than a behavioural utility function. 

A central optimal-tax formulation is the computational planner’s problem in which social welfare is maximized over tax-rule parameters subject to incentive compatibility of household choices and a public budget constraint. This is important because it summarizes the paper’s vision of empirical optimal taxation as an embedded microsimulation problem rather than a purely analytical formula exercise. 

# Suggested tags

structural-labour-supply, microsimulation, RURO, discrete-choice, opportunity-sets, welfare-evaluation, optimal-taxation, behavioural-policy-analysis, methodological-survey, Aaberge-Colombino

# My quick takeaway

This is a core methodological paper for your corpus. Its main value is not a new empirical result but a clear synthesis of why structural labour-supply models matter, why RURO is especially relevant when opportunities are heterogeneous, and why welfare evaluation must be kept distinct from behavioural utility. For your JMP, it is one of the best bridge papers linking latent-job empirical modelling to the later normative problem of defining well-being as a function of realized bundle, preferences, opportunities, and pay schedules.
