---

title: "A model of labour supply with job offer restrictions"
authors: ["Hans G. Bloemen"]
year: 1992
outlet: "CentER Discussion Paper No. 9239"
country_or_context: "The Netherlands"
population: "Married women"
data_period: "1985 OSA sample"
shelf: "job_offer_restrictions_labor_supply"
tags: ["labour supply", "job offers", "hours restrictions", "wage offer distribution", "job search", "involuntary unemployment", "discrete hours", "Netherlands", "structural model", "accepted offers"]
priority: "high"
read_status: "extracted"
------------------------

# Full citation

Bloemen, Hans G. 1992. *A Model of Labour Supply with Job Offer Restrictions*. CentER Discussion Paper No. 9239, Tilburg University, October 1992. 

# One-sentence contribution

The paper formulates and estimates a static structural labour-supply model in which individuals choose from randomly arriving job offers with both a wage and an hours component, thereby linking hours-restriction models to job-search-style wage offer models. 

# Why this paper matters

This paper matters because it directly attacks a central weakness of the standard neo-classical labour-supply model: the assumption that individuals can freely choose optimal hours at a given wage. Bloemen instead treats the feasible set as a set of job offers, so labour supply is constrained by what the market offers, not only by preferences and the budget set. 

For your potential JMP, the paper is useful because it is an early attempt to separate labour-supply behaviour from the opportunity side of the labour market. It does so in a still relatively simple way—jobs are summarized by wage and hours only—but the conceptual move is very close to your interest in opportunity sets, latent jobs, and the distinction between preferences and constraints. 

# Core research question

How should labour supply be modeled when individuals are restricted by the random set of job offers they receive, each offer containing both a wage and an hours component, and what does such a model imply empirically for observed hours distributions and labour-force participation? 

# Economic setting and context

The empirical application is to married women in the Netherlands using OSA data from 1985. The paper is motivated by dissatisfaction with the standard labour-supply model and by evidence from the hours-restrictions literature that workers cannot generally choose arbitrary hours. It also aims to bridge that literature with job-search theory, where wages are random offers but hours restrictions are usually absent. 

The policy/institutional context enters mainly through taxes and labour-market restrictions. The paper first estimates a version with a linear budget constraint and then extends the model by allowing wages to depend on hours, interpreting this hours dependence largely as capturing the tax system. The model is not designed as a full tax-benefit microsimulation, but taxes matter for the mapping from gross wage-hours offers into effective returns. 

# Model / theoretical framework

The model is a static structural labour-supply model with job offer restrictions. It is not a standard free-hours model. The individual receives a random number of job offers, each characterized by a wage and a weekly number of working hours, and chooses the offered wage-hours package yielding the highest utility. If all offered jobs yield lower utility than non-work, the individual is observed as non-working. 

The number of job offers is Poisson-distributed with parameter (\lambda). Hours are drawn from a discrete offer distribution over (m) hours categories, while wages conditional on hours are assumed lognormal. Only accepted offers are observed, so the observed wage distribution is endogenous to the acceptance rule and must be estimated jointly with labour supply. 

The utility function is Hausman-style:
[
u(h,y)=-\ln(\gamma-\beta h)-\frac{\beta(h-X\delta-\varepsilon-\theta y)}{\gamma-\beta h},
]
with disposable income (y), hours (h), observed covariates (X), and unobserved taste heterogeneity (\varepsilon). The framework is purely positive. There is no welfare-ranking object, no equivalent income, and no social welfare function. 

# Key objects

The main objects are the utility parameters, the Poisson parameter governing the number of job offers, the discrete hours-offer probabilities, and the wage-offer distribution conditional on hours. A job offer is explicitly a two-dimensional object: wage plus hours. 

A second key object is the reservation comparison between the best received job and non-work. This is how non-participation and involuntary unemployment arise in the model. Non-work can occur either because no job arrives or because all arriving jobs generate less utility than non-work. 

Empirically, the paper also treats the dependence of the average number of job offers on observed characteristics as a central object. This matters because earlier hours-restriction papers often kept the number of offers fixed across individuals, whereas Bloemen tests whether offer arrival differs systematically by age and education. 

# Data

The data come from the Organization for Strategic Labourmarket Research (OSA). The estimation sample contains 849 married women observed in 1985. The paper groups weekly working hours into discrete categories, using four-hour intervals up to 60 hours, with some pooling restrictions for sparsely populated cells. 

The variables entering the model include labour-force participation, weekly working hours, wages, family size, number of children below age six, age, and education indicators. In the wage equation, age terms and education dummies approximate the earnings profile and human capital. In the offer-arrival equation, age and education-type/level variables enter the Poisson parameter. 

The data are cross-sectional. This is important for interpretation because the paper repeatedly notes that the model is fully static: all job offers are assumed to arrive at one point in time, and there is no sequential search or duration margin. 

# Identification logic

Identification is structural and relatively demanding. Since only accepted wage-hours offers are observed, the wage-offer distribution cannot be estimated independently in a first stage without inconsistency. All parameters of the wage-offer process and labour-supply process must be estimated simultaneously. 

The model relies on parametric structure for both the utility function and the offer process. Hours offers are discrete with probabilities (p_\ell), wages conditional on hours are lognormal, and the number of offers is Poisson. Identification therefore comes from how accepted offers, non-participation, and the observed hours distribution jointly restrict the underlying preference and offer parameters. 

A major empirical message of the paper is that once the Poisson parameter is allowed to vary with individual characteristics, the estimated utility function becomes very flat. Bloemen interprets this as evidence that the available cross-sectional data provide too little information to separately recover a sensible underlying preference structure once richer heterogeneity in opportunities is allowed. This is a very important identification warning for your agenda. 

# Estimation / empirical strategy

The paper estimates the model by maximum likelihood. Separate likelihood contributions are derived for working and non-working individuals. For workers, the likelihood conditions on observing the accepted wage-hours package and integrates over the unobserved taste shock. For non-workers, the likelihood integrates the probability that either no offer arrives or all offers fall below the reservation utility of non-work. 

Several specifications are estimated. The baseline assumes a linear budget constraint and a constant Poisson parameter. A second version lets the Poisson parameter depend on individual characteristics. A third version allows the wage equation to depend on hours, interpreted mainly as capturing the tax system. The paper then simulates hours distributions from the estimated models and compares them to the empirical distribution, both informally and through Andrews’ chi-square diagnostic test. 

# Treatment of preferences

Preferences are modeled through a parametric utility function over income and hours plus a normal random taste shock. Family size and young children enter through observed preference shifters affecting the reservation utility of working. In the baseline model these variables have strong effects on labour-force participation. 

However, the paper’s deeper contribution is not about rich preference heterogeneity. It is almost the opposite: it shows that once the opportunity side is allowed to vary more flexibly across individuals, the data may cease to be informative enough to pin down preferences cleanly. In that sense the paper is a caution against over-interpreting estimated labour-supply preferences when the opportunity side is underspecified. 

The paper is not preference-respecting in any normative sense. Preferences are purely behavioral objects here. 

# Treatment of opportunities / constraints

This is the paper’s core contribution.

The paper models opportunities explicitly as job offers. Individuals do not choose arbitrary hours at an exogenous wage; they choose among a random set of wage-hours packages. This makes opportunity restrictions the primitive source of labour-market constraint. Involuntary unemployment can arise because no offer arrives or because no acceptable offer arrives. 

Relative to the hours-restrictions literature, Bloemen adds an independent wage-offer effect: jobs differ not only by hours but also by wages. Relative to standard job-search theory, he adds hours as an explicit job component. This is the paper’s main bridging contribution. 

For your research direction, the paper is strongly relevant because it does not treat the feasible set as universal. But its opportunity model remains relatively narrow: jobs are characterized only by wage and hours. There are no occupations, tasks, amenities, sectors, or richer latent job characteristics. So it is an early opportunity-set model, but not yet a full latent-jobs framework in the richer Dagsvik/Aaberge sense. 

# Welfare / normative object

None. The paper does not evaluate welfare using equivalent variation, money-metric utility, social welfare functions, or fairness criteria. It is a positive structural labour-supply paper. 

Its relevance for welfare economics is indirect: it changes the behavioural foundation on which any later welfare or policy analysis would be based, because labour-supply behavior is interpreted as constrained acceptance of offered jobs rather than free choice of hours. 

# Main findings

First, the model reproduces participation and several peaks in the hours distribution reasonably well in simulation. In the baseline model, the simulated frequencies track non-participation and the peaks around 20, 32, and 40 hours fairly closely. This is visible in Table 3.2 and the associated graphs on page 14. 

Second, desired hours under the unconstrained utility problem look very different from observed hours. In the baseline model, desired participation is higher than actual participation, and the distribution of desired hours lacks the observed peaks. The paper interprets this as evidence of hours restrictions and involuntary unemployment. This comparison is reported in Table 3.2 and Figures 3.1–3.2 on page 14. 

Third, allowing the number of job offers to depend on individual characteristics is strongly supported statistically. The likelihood-ratio test rejects the hypothesis of a common Poisson parameter. Age lowers the average number of offers, and some education-type indicators increase it. This is one of the paper’s clearest empirical results. 

Fourth, once that richer offer-arrival heterogeneity is introduced, the estimated utility function becomes almost flat and the desired-hours distribution becomes implausibly diffuse, with a large mass above 60 hours. The paper interprets this as a failure of the available data to identify the underlying preference structure well. This is a very important negative result, not a minor technical detail. 

Fifth, adding hours terms to the wage equation is significant and changes interpretation. In that specification, the low observed frequency of hours above 40 is explained less by low offer probabilities and more by a low marginal increase in income relative to the marginal utility of leisure at high hours. This is reported in Table 3.5, Table 3.6, and the discussion on pages 10–11 and 18. 

Sixth, despite decent visual fit in some simulations, formal Andrews chi-square tests reject all three model specifications under all three partitions of the hours distribution. The paper is explicit that visual matching of hours peaks is not enough. This is shown in Table 3.7 on page 19. 

# Main limitations

A first limitation is that the model is static. All job offers are assumed to arrive at once, and acceptance is immediate. The paper itself argues that a sequential search model with duration data would be preferable for interpretation and identification. 

A second limitation is that the job offer space is thin. Offers vary only in wage and hours, with no richer non-pecuniary job characteristics, sectors, occupations, or working conditions. This is a major simplification relative to your latent-jobs agenda. 

A third limitation is identification. The paper shows that once the number of offers becomes individual-specific, the utility function is no longer well recovered from the available data. This means the model is informative about constraints, but much less informative about preferences than one might initially think. 

A fourth limitation is that the model fails formal goodness-of-fit tests. So although it is conceptually important, it should not be treated as an empirically definitive solution. 

# Relevance for my JMP

## possible use for framing

This paper is very useful for framing a JMP that argues labour supply should be modeled as constrained job acceptance rather than free hours choice. It gives a clean conceptual link between the hours-restrictions literature and the wage-offer/job-search literature. 

## possible use for model design

It is useful as a simple precursor to a latent-jobs framework. The idea that each job offer is a wage-hours package is directly relevant if you want to build a richer model where jobs also differ by sector, occupation, or amenities. 

## possible use for identification

This is where the paper is particularly valuable. It shows that richer modeling of opportunities does not automatically improve identification of preferences; it can actually expose how little the data tell you about preferences once opportunity heterogeneity is admitted. That is a major lesson for your project. 

## possible use for welfare measurement

Indirectly relevant. It shows that any welfare analysis based on standard labour-supply models risks confusing desired labour supply with feasible labour supply. But the paper itself offers no welfare metric. 

## possible use for cross-country comparison

The paper is not cross-country, but it suggests that cross-country differences in labour supply may partly reflect differences in offer distributions, not only differences in preferences or tax schedules. That is directly useful for your broader agenda. 

# Research questions this paper inspires

How much of the cross-country variation in estimated labour-supply elasticities is actually variation in the distribution of job offers rather than variation in preferences?

Can one extend Bloemen’s wage-hours offer framework to richer latent jobs with occupation, sector, and non-pecuniary characteristics without losing identification?

What kinds of panel or duration data are needed to identify preferences and opportunity distributions jointly in a sequential job-offer model?

How would welfare comparisons change if observed non-participation were partly driven by missing acceptable offers rather than by taste for leisure alone? 

# Challenge to this paper

The strongest simplifying assumption is the static treatment of the offer process. Once job offers are the primitive constraint, it is hard to avoid the conclusion that timing, waiting, and future offers matter. Bloemen himself recognizes this and points toward sequential search as the natural next step. A future paper could therefore challenge the model by retaining the offer-based structure while introducing dynamic search and richer job characteristics. 

# Relation to Bargain et al. (2013)

The relation is indirect but important. Bargain et al. (2013) uses structural labour-supply estimation for welfare ranking under heterogeneous preferences, whereas Bloemen is concerned with modeling the constrained job-offer environment that generates observed labour-supply choices. Relative to Bargain et al. (2013), this paper is much stronger on explicit opportunity restrictions and much weaker on normative analysis. For your purposes, it is a behavioral foundation paper rather than a welfare-comparison paper. 

# Relation to opportunities vs preferences

This paper clearly pushes in the direction of separating opportunities from preferences. The basic explanatory object is the job-offer distribution, not a universal feasible set. At the same time, the paper shows that once opportunities are modeled more richly, preferences become harder to recover from the data. That makes it highly relevant to your agenda: it supports the opportunities side conceptually, but also warns that empirical separation of preferences and opportunities is difficult with standard cross-sectional data alone. 

# Useful quotations / formulas

The basic job-offer mechanism is that the number of offers is Poisson:
[
p(n)=\frac{e^{-\lambda}\lambda^n}{n!}, \qquad n=0,1,\ldots
]
and a job offer is a draw of both wage and hours from a joint offer distribution. This is the paper’s core departure from standard labour-supply models. 

The discrete hours-offer distribution is
[
P(h=h_\ell)=p_\ell,\qquad \ell=1,\ldots,m,
]
while the wage offer conditional on hours is lognormal:
[
\ln w = x^\prime \eta + v, \qquad v\sim N(0,\sigma_v^2).
]
These are the two key offer-side components. 

A short statement of the paper’s central conclusion is on page 12: once the Poisson parameter depends on relevant characteristics, “the utility function becomes a flat and approximately uniform random function,” suggesting that the data contain too little information to recover preferences well. 

# Suggested tags

#job_offer_restrictions #labor_supply #hours_restrictions #wage_offers #involuntary_unemployment #structural_model #Netherlands #accepted_offers #identification #job_search_link

# My quick takeaway

If I only remember one thing from this paper for my JMP, what should it be? That modelling labour supply through job offers is a major step toward separating preferences from opportunities, but it also reveals a hard econometric truth: once the opportunity side becomes more realistic, standard cross-sectional labour-supply data may no longer identify preferences cleanly.
