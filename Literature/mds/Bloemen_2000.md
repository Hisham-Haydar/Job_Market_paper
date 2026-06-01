---

title: "A Model of Labour Supply with Job Offer Restrictions"
authors: ["Hans G. Bloemen"]
year: 1992
outlet: "CentER Discussion Paper No. 9239"
country_or_context: "Netherlands"
population: "Married women in the Netherlands; estimation sample of 849 married women"
data_period: "1985"
shelf: "job_offer_restrictions_structural_labour_supply"
tags: ["structural labour supply", "job offer restrictions", "hours restrictions", "wage offer distribution", "involuntary unemployment", "Netherlands", "search-labour supply link", "latent opportunities"]
priority: "very high"
read_status: "extracted"
------------------------

# Full citation

Bloemen, Hans G. 1992. *A Model of Labour Supply with Job Offer Restrictions*. CentER Discussion Paper No. 9239, Tilburg University. 

# One-sentence contribution

The paper formulates and estimates a static labour-supply model in which individuals choose from a random set of job offers characterized jointly by wages and hours, thereby linking hours-restriction labour-supply models to job-search models with wage offers. 

# Why this paper matters

This paper matters because it is unusually explicit about the opportunity side of labour supply. It rejects the standard neo-classical assumption that workers can freely choose their optimal hours at a fixed wage, and instead models labour supply as constrained by the actual wage-hours job offers that arrive to the individual. That makes it highly relevant for any project trying to distinguish preferences from opportunities in observed labour-market outcomes. 

It also matters because it sits conceptually between two literatures that are often separated: static labour-supply models with hours restrictions and dynamic job-search models with wage offers. The paper’s own abstract states this bridging role very clearly. For your corpus, this makes it one of the more important early papers on the positive modelling of latent job opportunities. 

# Core research question

How can one model labour supply when individuals are constrained by randomly arriving job offers that differ both in wage rates and in hours, and what can be learned empirically from such a model using Dutch data on married women? 

# Economic setting and context

The empirical setting is the Netherlands, using data on married women from 1985 supplied by the Organization for Strategic Labourmarket Research (OSA). The paper is motivated by dissatisfaction with standard labour-supply models in which workers can always choose their preferred hours at a fixed wage. It builds directly on the hours-restrictions literature of Dickens and Lundberg, Tummers and Woittiez, and Van Soest, Woittiez, and Kapteyn, while adding an independent wage-offer component. 

The paper is clearly a methodological and structural-econometric contribution rather than a policy-evaluation or welfare paper. Its emphasis is on modeling the labour market as a constrained opportunity environment and on estimating the resulting behavioural model. 

# Model / theoretical framework

The model class is a static structural labour-supply model with job-offer restrictions. Individuals receive a random number of job offers. Each offer consists of two characteristics: a wage component and an hours component. The worker compares the utility yielded by all received wage-hours packages and either accepts the one yielding the highest utility or does not work if all offers are worse than non-employment. This allows involuntary unemployment because the individual may receive no offer at all, or only unattractive offers. 

The feasible set is therefore modeled explicitly, though statistically rather than as an observed set-valued object. The number of job offers is assumed Poisson, and job offers are drawn from a joint wage-hours offer distribution (f(w,h)). Hours are discrete and wages are conditionally lognormal given hours. This is much closer to a latent-opportunity model than to a standard continuous-hours labor-supply model. 

The framework is purely positive. The paper does not define a welfare function, does not aggregate welfare socially, and does not offer a normative theory of compensation or responsibility. Its purpose is to explain labour-market outcomes when opportunities are restricted. 

# Key objects

The main economic objects are the utility function (u(h,y)), the Poisson-distributed number of job offers with parameter (\lambda), the discrete hours-offer distribution over categories (h_\ell), and the wage-offer distribution conditional on hours. Equations (2.1)–(2.9) set up these objects formally. 

A central object is the job-offer density (f(w,h)), which combines the probability of receiving a given hours offer with the conditional density of wages at that hours level. Another central object is the reservation comparison between the best offered job and the utility of non-work. This is the mechanism that generates both participation and accepted wage-hours outcomes. 

The paper also introduces an extended object that is especially relevant for your interests: the Poisson parameter (\lambda_i=\exp(\beta'z_i)), allowing the number of job offers to vary with individual characteristics. This is the paper’s main device for opportunity heterogeneity across individuals. 

# Data

The model is estimated on a sample of 849 married women in 1985 from the Dutch OSA dataset. The hours variable is discretized into categories of four weekly hours each, up to 60 hours, with grouped probabilities for low-frequency categories. This discretization is essential to the empirical implementation. 

The explanatory variables in the utility specification include a constant, log family size, and a dummy for children younger than six. The wage-offer equation includes a constant, age terms, and education dummies. In the specification with heterogeneous offer intensity, the Poisson parameter also depends on age and education variables. These empirical design choices are described on pages 7–10. 

# Identification logic

Identification is structural and strongly parametric. Because only accepted wage-hours offers are observed, the observed wage distribution is endogenous to the model structure. The paper explicitly states that this prevents a two-step procedure in which wage-offer parameters are estimated separately. Instead, all model parameters must be estimated simultaneously. This is an important identification point. 

Identification of opportunities comes from the assumed structure of the offer process: a Poisson number of offers, a discrete hours-offer distribution, and a conditional lognormal wage-offer distribution. Identification of preferences comes from accepted choices relative to non-participation under those maintained assumptions. The paper is transparent that the model is highly dependent on structure, not on quasi-experimental variation. 

A particularly important result is that once the Poisson offer parameter is allowed to depend on individual characteristics, the data no longer pin down the utility parameters in a sensible way: the underlying utility function becomes essentially flat and approximately uniform random. The paper interprets this as evidence that the available cross-section contains too little information to recover preferences once opportunity heterogeneity is modeled more flexibly. This is one of the most relevant points for your project. 

# Estimation / empirical strategy

The paper estimates the model by maximum likelihood. Separate likelihood contributions are derived for working and non-working individuals, conditional first on the random taste term and then integrating over it. Equations (2.16)–(2.23) are the core likelihood expressions. 

Three main specifications are estimated. First, a baseline model with a linear budget constraint and a constant Poisson offer parameter. Second, a model in which the Poisson offer parameter varies with individual characteristics. Third, a model with hours-dependent wages, interpreted mainly as a reduced-form way to capture the tax system by allowing net wages to vary with hours. The main parameter tables are Table 3.1 on page 13, Table 3.3 on page 15, and Table 3.5 on page 17. 

The paper then performs simulation exercises comparing empirical and model-generated hours distributions, and finally applies Andrews’ chi-square diagnostic test to compare observed and simulated distributions formally. The simulated distributions are shown in Tables 3.2, 3.4, and 3.6 and the corresponding charts on pages 14, 16, and 18. The Andrews test results are reported in Table 3.7 on page 19. 

# Treatment of preferences

Preferences are modeled through a Hausman-type utility function over hours and income, with an unobserved random taste term (e). Family size and the presence of young children shift utility through the reservation utility level. In the baseline model, these parameters are estimated sensibly and imply that larger families and young children raise the attractiveness of non-work. Table 3.1 on page 13 contains these estimates. 

However, the paper’s most striking finding on preferences is negative rather than positive. Once the offer-arrival parameter is allowed to depend on individual characteristics, the estimated utility function becomes nearly flat and preferences are no longer credibly identified. The paper explicitly states that this suggests the available data contain too little information to recover the utility structure once opportunity heterogeneity is modeled in this richer way. 

This makes the paper especially relevant for your framework: it is an early warning that what looks identifiable in a standard labour-supply model may become weakly identified once one tries to model opportunities seriously. 

# Treatment of opportunities / constraints

This is the core contribution of the paper. Opportunities are modeled explicitly. Individuals do not choose freely from a universal hours set. Instead, they receive a random number of job offers, and each offer contains both a wage and an hours component. The individual chooses from among these offers. This is a direct attempt to model constrained feasible opportunities on the positive side. 

The model therefore does not assume a universal choice set. It also does not treat wages as fixed at the individual level. Both wages and hours vary across offers. The paper further allows the expected number of offers to depend on individual characteristics, thereby introducing heterogeneity in opportunity intensity. This is highly relevant to latent-job and RURO-style reasoning. [reasonable inference for my project] supported by 

The paper also allows involuntary unemployment in an explicit way: non-employment can arise because no offers arrive, or because all offers yield lower utility than not working. This is more informative than a standard corner-solution model. But the opportunity object remains statistical rather than observed. It is not an explicit set (A_i) in the strong sense of your current framework. 

# Welfare / normative object

The paper does not evaluate welfare normatively. It does not construct equivalent variation, equivalent income, a common welfare function, or a social welfare function. It is therefore best classified as purely positive. 

Still, the paper matters indirectly for welfare analysis because it changes the interpretation of observed labour-market outcomes. If hours and wages are constrained by offer restrictions, then observed non-employment or observed hours cannot simply be read as pure preference revelation. This is a positive prerequisite for any later well-being analysis. [reasonable inference for my project] supported by 

The paper does not help directly with responsibility for opportunities, compensation for opportunities, reference opportunity sets, or decomposition of inequality. Its contribution is upstream: it provides a behavioural architecture in which such questions could later be asked more meaningfully. 

# Main findings

The first main finding is conceptual: allowing job offers to vary jointly in wages and hours yields a richer and more realistic labour-supply model than hours-restrictions models or standard wage-only search models alone. The paper explicitly presents itself as a bridge between these literatures. 

The second main finding is empirical: making the Poisson offer parameter depend on individual characteristics significantly improves fit, as shown by a likelihood-ratio statistic of 83.58 compared with the relevant critical value reported on page 8. But this richer opportunity specification severely destabilizes preference estimation, producing a nearly flat utility function. This is arguably the paper’s most important substantive result. 

The third main finding is that introducing hours into the wage equation is statistically significant and changes the interpretation of the hours distribution. In the baseline model, low frequencies above 40 hours are explained by low offer probabilities. In the hours-dependent wage model, these low frequencies are instead explained mainly by a low marginal increase in income from additional hours relative to the marginal utility of leisure. The paper interprets this hours dependence largely as capturing the tax system. Pages 10–11 and Table 3.5 are central here. 

A fourth finding is methodological. The model predicts participation and some peaks in the hours distribution reasonably well in the simulation exercises, especially the peaks at 20, 32, and 40 hours shown in the charts on pages 14, 16, and 18. But all three main specifications are formally rejected by Andrews’ chi-square diagnostic tests reported in Table 3.7 on page 19. The paper is therefore transparent that the model improves on standard approaches without fully fitting the data. 

# Main limitations

A first limitation is identification. The paper itself concludes that once opportunity intensity is made individual-specific, the utility structure cannot be sensibly traced down with the available data. This is a serious limitation and also one of the paper’s most informative results. 

A second limitation is staticity. All offers arrive at a point in time, the choice is immediate, and no future offers are considered. The author explicitly argues in the conclusion that the next step should be a sequential search model with unemployment-duration data. This limitation matters because the interpretation of the Poisson arrival parameter is otherwise unclear. 

A third limitation is fit. Although the simulated hours distributions capture participation and several peaks, the formal chi-square tests reject equality between simulated and observed distributions for all main specifications. So the model is substantively valuable but not empirically definitive. 

A fourth limitation, relative to your project, is normative absence. The paper does not move from opportunity modeling to well-being measurement, fairness, or decomposition. It remains a positive model of constrained choice. 

# Relevance for my JMP

## possible use for framing

This paper is very useful for framing the empirical side of your project because it states sharply that labour supply should be modeled as constrained by job offers rather than as unconstrained hours choice on a budget line.

## possible use for model design

It is highly useful for model design. It provides an early template for treating jobs as wage-hours packages and for allowing both the number and composition of offers to vary across individuals.

## possible use for identification

It is especially useful here. The paper shows that once opportunities are modeled more seriously, preference identification becomes much harder. That is an important caution for your own estimation strategy.

## possible use for welfare measurement

Directly limited. The paper offers no welfare paper offers no welfare measure. Indirectly important, because it prevents the misreading of observed labour supply as free preference revelation.

## possible use for decomposition

Directly limited. It does not decompose outcomes into preferences and opportunities. Indirectly strong, because it explicitly structures the data-generating process into utility and offer components and shows where the empirical separation breaks down.

## possible use for comparative application

Limited directly, since it is a Dutch application to married women only. But conceptually it can be compared fruitfully to the later Aaberge–Colombino line and to RURO-style work.

# Research questions this paper inspires

1. Can the paper’s statistical job-offer object be translated into an explicit feasible-set object (A_i) that can enter an individual well-being measure (W(z,R,A;y))?

2. What additional data—especially duration data, rejected offers, or vacancy information—are needed to identify both preferences and opportunity heterogeneity simultaneously?

3. How much of what standard labour-supply models interpret as preferences is actually driven by heterogeneity in offer arrival rates and job-offer composition?

4. Can a dynamic search version of this model produce a cleaner decomposition between preferences, opportunities, and wages than the static version here?

5. How should one normatively evaluate involuntary unemployment when non-employment results from zero or unattractive offers rather than from chosen leisure?

# Challenge to this paper

The strongest challenge is that the paper succeeds conceptually before it succeeds econometrically. It provides a very useful positive theory of labour supply under offer restrictions, but the richer the opportunity side becomes, the less the data seem able to recover the underlying preference structure. For your project, that is both a limitation and a lesson: modeling (A) seriously may force a major rethinking of what can be learned about (R) from stand. fileciteturn24file0

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper clearly distinguishes realized labour-market outcomes from the opportunity environment that generated them. Individuals receive a random number of job offers, each characterized by wages and hours, and then choose the best available package or non-work. This is directly relevant to any framework in which realized bundle and feasible opportuni. fileciteturn24file0

[reasonable inference for my project] In your notation, the realized bundle (z) corresponds to the accepted wage-hours-income package or to non-employment. Preferences (R) correspond to the utility function over hours and income with heterogeneity through the random taste term. The feasible set (A) is not observed directly, but it is represented statistically by the Poisson number of offers and the joint wage-hours offer distribution. The pay schedule (y) enters through the wage component of offers and, in the extended model, partly through the hours-dependent net wage specification int. fileciteturn24file0

[unclear from paper] The paper does not define a well-being measure (W(z,R,A;y)), does not distinguish actual from reference opportunity sets, and does not study axioms such as independence of (A), independence of (y), IIJ, IPIJ, or responsibility for opportunities. Those are outs. fileciteturn24file0

[reasonable inference for my project] In your taxonomy, this paper is strongly related to the explicit modelling of (A)-type opportunity heterogeneity and strongly not related to independence of (A). It is also not close to laissez-faire or responsibility-sensitive evaluation, because it remains a positive econometric paper. Its main contribution to your framework is to supply a very early empirical architecture for modeling latent . fileciteturn24file0

# Relation to Bargain et al. (2013)

[not central]

# Relation to opportunities vs preferences

This paper is one of the most relevant positive papers in your corpus for the opportunities-versus-preferences distinction. It does not collapse behaviour into preferences alone. It explicitly models job opportunities as random and heterogeneous, with both wag. fileciteturn24file0

At the same time, it also shows how difficult the empirical separation becomes once opportunities are modeled seriously. The flattening of the utility function in the richer offer-intensity specification is a concrete indication that the (R) versus opportunity separation is empirically demanding, not merely . fileciteturn24file0

# Useful quotations / formulas

A central formula is the Poisson offer-arrival structure
[
p(n)=\exp(-\lambda)\frac{\lambda^n}{n!},
]
which determines the random number of job offers received by the worker. This is the paper’s basic opportuni. fileciteturn24file0

A second central object is the utility function
[
u(h,y)=-\ln(\gamma-\beta h)-\frac{\beta(h-X\delta-e-\beta y)}{\gamma-\beta h},
]
which yields a linear labour-supply function under a linear budget constraint. This is the prefer. fileciteturn24file0

The most informative empirical tables are Table 3.3 on page 15, which shows the strong improvement from allowing (\lambda) to vary with characteristics but the associated instability in preference estimation, and Table 3.7 on page 19, which shows that all main specifications are rejected by Andrews’ chi-s. fileciteturn24file0

# Suggested tags

job-offer-restrictions, structural-labour-supply, latent-opportunities, hours-restrictions, wage-offers, involuntary-unemployment, Netherlands, married-women, Bloemen-1992

# My quick takeaway

This is a high-priority paper for the opportunity side of your corpus. It is not a welfare paper, and it does not yet give you an explicit (W(z,R,A;y)) object. But it is one of the clearest early attempts to model labour supply as constrained choice over latent wage-hours opportunities rather than as free choice of hours. Its most valuable lesson for your JMP is not only conceptual but empirical: once opportunities are modeled seriously, the clean recovery of preferences becomes much more difficult.
