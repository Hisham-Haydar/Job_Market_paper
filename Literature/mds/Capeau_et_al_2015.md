---

title: "Estimating and Simulating with a Random Utility Random Opportunity Model of Job Choice: Presentation and Application to Belgium"
authors: ["Bart Capéau", "André Decoster", "Gijs Dekkers"]
year: 2016
outlet: "International Journal of Microsimulation"
country_or_context: "Belgium"
population: "Belgian private-household population, with estimation on selected subsamples of labour-market-available couples, single females, and single males"
data_period: "EU-SILC 2007"
shelf: "ruro_job_choice_opportunities"
tags: ["RURO", "random utility random opportunity", "job choice", "latent jobs", "opportunity heterogeneity", "discrete choice labour supply", "Belgium", "microsimulation"]
priority: "very high"
read_status: "extracted"
------------------------

# Full citation

Capéau, Bart, André Decoster, and Gijs Dekkers. 2016. “Estimating and Simulating with a Random Utility Random Opportunity Model of Job Choice: Presentation and Application to Belgium.” *International Journal of Microsimulation* 9(2): 144-191. 

# One-sentence contribution

The paper presents, estimates, and simulates a RURO model of job choice in which observed labour-market behaviour is jointly driven by heterogeneous preferences and heterogeneous stochastic job opportunities, using Belgian EU-SILC 2007 data. 

# Why this paper matters

This paper matters greatly for your project because it is one of the clearest empirical papers that does not collapse labour-supply behaviour into preferences alone. Instead, it explicitly models job choice as depending on both preferences and opportunities, with job offers arriving stochastically and differing in wages, hours, and unobserved nonpecuniary attributes. That is much closer to your preferred separation between preferences and feasible opportunities than standard discrete-hours labour-supply models. 

It is also especially useful because it is not just conceptual. It gives a full estimated likelihood, a simulation strategy, empirical results on education effects through preferences and opportunities, and a counterfactual exercise. So it is relevant not only for framing but also for model design. 

# Core research question

How can one estimate and simulate a labour-supply/job-choice model in which heterogeneity in observed choices reflects both differences in preferences and differences in available job opportunities, and what does such a model imply in Belgian data about education, participation, wages, and hours? 

# Economic setting and context

The application is to Belgium using EU-SILC 2007. The empirical focus is labour-market participation and labour supply under job-choice frictions, with special attention to differences by education and gender. The paper highlights large unemployment gradients by education, especially among low-educated women and men, and uses the RURO framework to decompose these patterns into preference intensity, job-offer intensity, and wage-offer differences. 

The data are drawn from the Belgian private-household population. The estimation sample excludes people not available for the labour market, the self-employed, and certain mixed or ambiguous household types. The final estimation sample contains 1,457 couples, 571 single females, and 449 single males. This is stated in the data section on pages 163-164. 

# Model / theoretical framework

The model class is a Random Utility Random Opportunity model of job choice. The core conceptual move is that individuals choose among available activities, some of which are jobs and some of which are non-market alternatives. Jobs are treated as packages including wages, labour-time regimes, and other job attributes. Opportunities are not fixed and common across agents; they arise from an individual-specific stochastic process of job offers. 

The agent chooses the best available alternative. On the preference side, total utility from alternative (z) is
[
U(C(z),H(z),z;x^V)=V(C(z),T-H(z);x^V),\varepsilon(z),
]
where the systematic part (V) depends on disposable income and leisure, and the multiplicative random term captures unobserved nonpecuniary job or activity attributes. This is a random-utility model, but one embedded in a richer opportunity structure than standard labour-supply models. 

On the opportunity side, job offers differ by wages and hours, and arrive according to an inhomogeneous spatial Poisson process. The model specifies a wage-offer density (g_1(w)), a labour-time-offer density (g_2(h)), and an opportunity-intensity term (q) measuring the relative abundance of market opportunities. Non-market alternatives are also stochastic, with their own intensity structure. Pages 151-155 are the core theoretical exposition. 

The framework is positive rather than normative. It is designed to explain and simulate job choice and labour-market participation, not to evaluate justice or welfare through an explicit ethical criterion. Still, it is a structurally opportunity-sensitive positive model. 

# Key objects

The central economic objects are the systematic utility function (V(c,T-h;x^V)), the induced utility function over wage-hours packages (\Psi(w,h;x^V,x^f)), the random multiplicative taste term (\varepsilon(z)), the job-offer intensity (q), the wage-offer density (g_1(w)), and the labour-time-offer density (g_2(h)). These are the objects through which preferences and opportunities are separated. 

Another key object is the likelihood of observing a chosen job offer:
[
\phi(w,h)=\frac{\Psi(w,h),q,g_1(w)g_2(h)}{\Psi(0,0)+\int!!\int \Psi(r,t),q,g_1(r)g_2(t),dt,dr},
]
with the analogous expression for choosing a non-market alternative. This formula is important because it shows directly how preferences and opportunities jointly determine observed choices. 

The simulation objects are also central: sampled wage-hours choice sets, Fréchet draws for the random terms, and the resulting simulated optimal choices. The paper uses these for fit assessment, elasticities, and education counterfactuals. 

# Data

The model is estimated on Belgian EU-SILC 2007. The full dataset contains 6,348 households and 15,493 individuals and is representative of the Belgian private-household population, excluding collective households and institutions. The final estimation samples are selected from labour-market-available couples, single women, and single men. 

The final estimation sample consists of 1,457 couples, 571 single females, and 449 single males. Gross household labour income, taxes, social security contributions, and transfers are combined with EUROMOD calculations to obtain disposable income. The paper also uses external type-specific unemployment rates by age, sex, and education as a proxy for job availability. This is all in the data section on pages 163-165 and in Tables 1 and 2. 

# Identification logic

Identification is partly nonparametric and partly parametric. The paper explicitly discusses nonparametric identification on pages 157-158. The main logic is sequential. First, comparing observationally equivalent individuals who work different hours at the same wage identifies the composite object (\Psi(w,h)g_2(h)). Second, comparing individuals working the same hours at different wages identifies the wage-offer density (g_1(w)), since (g_1) must integrate to one. Third, comparing workers and nonworkers identifies (q) after normalizing (\Psi(0,0)). 

The key identification limitation is also explicit: (\Psi(w,h)) and (g_2(h)) are not separately nonparametrically identified. The paper resolves this by imposing functional form, notably Box-Cox utility on the preference side and a piecemeal-uniform labour-time-offer density with peaks around part-time, three-quarter-time, and full-time jobs. 

An exclusion restriction is introduced for the opportunity side: a group-specific unemployment rate enters (q) but is assumed not to affect individual preferences directly. The authors are explicit that this is meant to improve identification of opportunities relative to preferences. 

So identification is not quasi-experimental. It is structural, grounded in the specific RURO likelihood, support comparisons across observed wage-hours combinations, normalization, and exclusion restrictions. This is rigorous but model-dependent. [reasonable inference for my project] supported by 

# Estimation / empirical strategy

The estimation strategy is simulated maximum likelihood. Because the econometrician does not observe the full set of wage offers and labour-time regimes, the paper samples alternative wage-hours pairs from a prior density (P(w,h)), always including the observed choice in the sampled set. The likelihood is then reformulated conditional on the sampled choice set. Pages 160-163 provide the estimation and sampling details. 

Disposable income is not given a closed-form parametric specification. Instead, for each sampled wage-hours alternative, disposable income is calculated using Belgian tax rules as implemented in EUROMOD, combined with SILC household information. That makes the model particularly relevant for microsimulation-based labour-supply analysis. 

The model is then used for simulation in three ways: to assess fit, to compute elasticities, and to evaluate a counterfactual education scenario in which male educational attainment catches up with that of females. Pages 163-176 develop these exercises. 

# Treatment of preferences

Preferences are modeled explicitly through the systematic utility function over disposable income and leisure, plus a random multiplicative term capturing unobserved job or leisure attributes. The systematic part is Box-Cox. For singles,
[
\ln V(c,T-h;x^V)=\beta_c \frac{c^{\alpha_c}-1}{\alpha_c} + \beta_h'x^V \frac{((T-h)/T)^{\alpha_h}-1}{\alpha_h},
]
and for couples the model allows spouse-specific leisure terms and a leisure-interaction term under a unitary framework. Pages 158-159 present these functional forms. 

Preference heterogeneity is therefore partly observable, through (x^V), and partly unobservable, through the multiplicative random term (\varepsilon(z)). The random term absorbs unobserved nonpecuniary attributes of jobs and non-market activities. This is a richer treatment of tastes than a pure consumption-leisure model, though the nonpecuniary part is not separately observed. 

Substantively, the paper finds that education affects the intensity of preference for leisure relative to consumption, but not in a uniformly monotonic way for all groups. Figure 2 on page 167 shows that for males, both low and high education can imply lower leisure intensity than middle education, whereas for females higher education reduces the relative intensity of preference for leisure more clearly. 

# Treatment of opportunities / constraints

This is the most important section for your project, and the paper is exceptionally useful here. Opportunities are modeled explicitly. The set of available job alternatives is not assumed universal, nor summarized only by an exogenous wage. Instead, the availability of suitable jobs is the outcome of a stochastic job-arrival process. Job offers are packages of wages, hours regimes, and other attributes, and individuals differ in both observed and unobserved opportunity sets. Pages 146-155 are central on this point. 

The paper also treats non-market alternatives as heterogeneous and individually specific. This is important because the outside option is not a single homogeneous “leisure” point; it is itself an opportunity domain with varying intensity and attractiveness. That is a significant conceptual improvement over many labour-supply models. 

The opportunity side is parameterized through (q), (g_1(w)), and (g_2(h)). The term (q) measures the relative intensity of market over non-market opportunities; (g_1(w)) is the wage-offer density; and (g_2(h)) is the density of offered labour-time regimes. Figure 4 on page 169 shows that the estimated labour-time-offer distribution differs by gender, with women receiving relatively more part-time and fewer full-time offers. Figure 5 on page 170 shows the interaction between education, age-specific unemployment, and job-offer intensity. 

This paper therefore helps distinguish both preference heterogeneity and opportunity heterogeneity. That is its main contribution. However, opportunities are still latent stochastic offer structures rather than directly observed feasible sets (A_i) in the axiomatic sense. So it is very close to your opportunity-set concerns, but not identical to an explicit set-valued normative framework. 

# Welfare / normative object

The paper is essentially positive. It estimates a behavioural model of job choice and uses it for simulation of participation, hours, wages, and education counterfactuals. It does not define a social welfare function, money-metric utility criterion, equivalent variation, or fairness principle. 

There is therefore no explicit welfare object beyond utility as a behavioural construct. The paper does not evaluate redistribution in normative terms, and it does not ask whether unequal job opportunities should be compensated or whether individuals are responsible for them. 

Its relevance for your welfare work is indirect but substantial. It gives an empirical structure in which opportunity heterogeneity is not forced into preferences. That is precisely the kind of positive model that could later feed a normative (W(z,R,A;y))-type analysis. [reasonable inference for my project] supported by 

# Main findings

The first main finding is conceptual and empirical at once: the RURO framework can be estimated on Belgian data and yields a meaningful separation between preference intensity, job-offer intensity, and wage-offer distributions as drivers of labour-market outcomes. This is explicit in the abstract, introduction, and Sections 5-7. 

Second, education shifts the wage-offer distribution to the right. Figure 3 on page 168 shows that higher education is associated with higher wage offers, while potential experience also shifts the offer distribution rightward up to a point. The paper is explicit that education and experience interact on the opportunity side. 

Third, education affects the intensity of suitable job offers, but the net effect differs by gender because education and the group-specific unemployment proxy interact differently. Figure 5 on page 170 shows that for women the net effect of high education on suitable job-offer intensity is clearly positive, whereas for men the positive direct education effect is partly offset by the unemployment component and becomes more muted. 

Fourth, the estimated labour-time-offer distribution exhibits strong peaks around part-time, three-quarter-time, and full-time jobs, and these peaks differ by gender. Figure 4 on page 169 is central here. This is substantively important because it confirms that labour-time opportunities are not uniform. 

Fifth, the model’s fit is mixed but respectable. The paper reports that female wages and single-female participation are fitted relatively well, while non-participation is overestimated in some groups, especially among couples and single males. Pages 171-174 and Figures 6-11 provide the evidence. 

Sixth, the wage-shift elasticities are nontrivial and differ across margins. Table 4 on page 174 reports total and intensive effects and entries/exits. For example, a rightward shift of the female wage distribution raises female labour supply strongly and can reduce male labour supply within couples; a shift in the male wage distribution raises male labour supply and can lower female labour supply in couples. 

Seventh, the counterfactual in which male educational attainment catches up with female educational attainment has only modest aggregate effects on labour-market participation, concentrated mainly among men. Pages 175-179 and Tables 6-7 show that the effect is strongest for men aged roughly 30-45 and runs predominantly through opportunities rather than preferences. The conclusion on page 179 is explicit on this. 

# Main limitations

A first limitation is explicitly acknowledged by the authors: the model is static and not a full equilibrium framework. It is not a matching model and does not endogenize labour-market frictions through a complete equilibrium mechanism; frictions are taken as given. The conclusion on page 179 states this directly. 

A second limitation is identification. The utility function (\Psi(w,h)) and the labour-time-offer density (g_2(h)) are not separately nonparametrically identified, so the empirical separation of preferences and hours-offer opportunities depends on functional-form assumptions. This is a substantive econometric limitation, not a mere technical detail. 

A third limitation is that opportunities remain latent stochastic objects, not observed feasible sets. The model is therefore extremely useful for empirical separation of opportunities and preferences, but it does not directly observe or normatively evaluate actual opportunity sets. [reasonable inference for my project] supported by 

A fourth limitation is the unitary-couple assumption. For couples, the paper assumes a unitary household model, even though spouses’ leisure is separately modeled. That may be restrictive if intra-household bargaining matters. 

A fifth limitation is the fit. The model fits some distributions well but overestimates non-participation in some subgroups and does not fully match all labour-time peaks. The fit is good enough to be useful, but not strong enough to eliminate concern about specification. Pages 171-174 show this clearly. 

A sixth limitation, from your perspective, is that the paper is not a decomposition paper in the welfare-economics sense. It separates preference and opportunity channels within a behavioural model, but it does not produce a normative decomposition of inequality or well-being into (R), (A), and (y). 

# Relevance for my JMP

## possible use for framing

This paper is one of the strongest framing references for the proposition that observed labour-market outcomes should be understood as the joint result of preferences and opportunities. It provides a direct rebuttal to models that treat opportunity heterogeneity as negligible or as fully embedded in wages. 

## possible use for model design

Very high relevance. The paper offers a concrete empirical architecture for modelling jobs as wage-hours packages plus unobserved nonpecuniary attributes, with stochastic opportunity arrival and non-market alternatives. This is extremely close to the sort of RURO/job-set empirical design you have been considering. 

## possible use for identification

High relevance. The identification discussion is directly useful for thinking about what can and cannot be separately learned about preferences, wage offers, and hours opportunities from labour-market data. The use of exclusion restrictions through type-specific unemployment is also informative for your own identification thinking. 

## possible use for welfare measurement

Directly limited, because the paper is not normative. Indirectly, it is highly useful because a welfare measure that depends on feasible job opportunities needs a credible empirical representation of those opportunities. This paper supplies exactly that kind of structure. [reasonable inference for my project] supported by 

## possible use for decomposition

Moderate to high relevance in a positive sense. The paper does not give a welfare decomposition, but it does offer a behavioural decomposition intuition: unemployment and participation gaps can be traced to differences in leisure preference intensity, job-offer intensity, and wage-offer distributions. That is a very useful precursor to a more explicitly normative decomposition. 

## possible use for comparative application

The application is Belgian, but the framework is portable. Any setting with micro-data, tax-benefit microsimulation, and plausible measures or proxies for opportunity differences could in principle estimate a related RURO model. The model is therefore relevant for cross-country comparative work as a template rather than only as a Belgian case study. [reasonable inference for my project] supported by 

# Research questions this paper inspires

Can one construct an individual well-being measure (W(z,R,A;y)) in which (A) is estimated from a RURO job-arrival process rather than treated as observed or universal?

How robust is the empirical separation of preferences and opportunities in RURO models to alternative functional forms for (g_2(h)) and for the systematic utility function (\Psi(w,h))?

Can the stochastic opportunity intensity (q) be decomposed into components attributable to education, labour demand conditions, and other circumstances, and then embedded in a responsibility-sensitive welfare analysis?

How would optimal tax or transfer design change if the planner compensated low (q)-individuals differently from high (q)-individuals, rather than treating all non-employment as a preference outcome?

Can a RURO model be extended from wage-hours packages to richer job vectors including occupation, task content, and nonpecuniary job amenities observable to the analyst?

# Challenge to this paper

The central challenge is that the model’s empirical distinction between preferences and opportunities is not fully nonparametric. Because (\Psi(w,h)) and (g_2(h)) are not separately identified without structure, some of what appears as “opportunity” may still reflect functional-form choices rather than pure empirical evidence. The paper is valuable precisely because it is explicit about this, but the limitation remains serious. 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper directly treats job choice as depending on both preferences and opportunities. Jobs are packages of wages, labour time regimes, and other attributes, and the availability of suitable jobs is individually specific and stochastic. This is explicit throughout the introduction and model sections. 

[reasonable inference for my project] In your notation, the mapping is unusually natural: (z) corresponds to the realized chosen activity or job package; (R) corresponds to the systematic and random preference structure over disposable income, leisure, and nonpecuniary attributes; (A) corresponds to the latent stochastic opportunity set generated by the job-arrival process and the availability of non-market alternatives; and (y) corresponds to the income/pay schedule embedded in the gross-to-net mapping (f(w,h;x^f)) and in the wage-offer distribution. This is not the paper’s notation, but it is a close conceptual translation. supported by 

[explicit in paper] The paper is strongly anti–independence-of-(A) in any positive sense: opportunity variation is central to explaining choices. It is also clearly not independence of (y), because wages and taxes enter through job packages and disposable income. 

[unclear from paper] The paper does not state or test normative axioms such as Full Compensation, IIJ, IPIJ, Responsibility for Equal Pay, or reference opportunity-set principles. It does not ask how well-being should normatively depend on (A); it asks how behaviour empirically depends on (A)-like latent opportunities. 

[reasonable inference for my project] For your framework, this paper is closest to the empirical modeling of opportunity-sensitive well-being ingredients rather than to the normative characterization of well-being measures. It is especially close to your interests in RURO, latent jobs, and separating opportunity heterogeneity from preference heterogeneity. supported by 

# Relation to Bargain et al. (2013)

[not central].

# Relation to opportunities vs preferences

This paper is directly about the opportunities-versus-preferences distinction. That is its central value. It argues that classical labour-supply models confound the two by treating wages as exogenous individual traits and by leaving the availability of job alternatives outside the model, whereas RURO makes both parts explicit. 

The opportunity side is not merely “hours restrictions.” It includes the stochastic availability of job packages and the intensity with which suitable jobs arrive. That is stronger than much of the restricted-hours literature and much closer to the kind of opportunity heterogeneity that matters for your project. 

At the same time, the paper does not reduce everything to opportunities. Preferences remain central, are flexibly parameterized, and affect simulated behaviour. This is precisely why the paper is so useful: it is an explicit joint model rather than a one-sided correction. 

# Useful quotations / formulas

The most important behavioural formula is the likelihood of choosing a job offer:
[
\phi(w,h)=\frac{\Psi(w,h),q,g_1(w)g_2(h)}{\Psi(0,0)+\int!!\int \Psi(r,t),q,g_1(r)g_2(t),dt,dr}.
]
This formula shows directly that observed choice probabilities are the product of attractiveness and availability. 

The key opportunity formula is
[
\lambda_1(\upsilon)=\frac{q}{\upsilon^2},
]
which governs the intensity with which jobs yielding utility multiplier (\upsilon) arrive to an individual. The term (q) is the paper’s central measure of market opportunity intensity. 

The key preference formula for singles is the Box-Cox specification on page 158, because it is the basis for all comparative statements about the intensity of preference for leisure relative to consumption. 

Figure 4 on page 169 is also important: it shows visually that women are estimated to receive relatively more part-time and fewer full-time job offers than men. That figure encapsulates the empirical opportunity-side contribution of the paper. 

# Suggested tags

RURO, job-choice, latent-opportunity-sets, stochastic-job-offers, discrete-choice-labour-supply, Belgium, education-and-participation, wage-offer-distribution, hours-offer-distribution

# My quick takeaway

This is one of the most relevant papers in your corpus for the empirical side of your JMP. It does not provide an axiomatic well-being measure, but it gives an unusually explicit and structurally grounded way of separating preferences from opportunities in labour-market behaviour. If your project aims to move from empirical job opportunities to a normative (W(z,R,A;y)) framework, this paper is not peripheral support; it is close to a core bridge.
