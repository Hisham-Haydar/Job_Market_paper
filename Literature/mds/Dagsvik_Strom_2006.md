---

title: "Sectoral labour supply, choice restrictions and functional form"
authors: ["John K. Dagsvik", "Steinar Strøm"]
year: 2006
outlet: "Journal of Applied Econometrics"
country_or_context: "Norway"
population: "Married women in Norway; data source includes married couples and cohabiting couples with common children"
data_period: "Core labour-supply estimation uses 1994 Norwegian data, merged with a 1995 living-conditions survey"
shelf: "latent_jobs_sectoral_labour_supply"
tags: ["latent jobs", "sectoral labour supply", "choice restrictions", "hours constraints", "non-pecuniary job attributes", "functional form", "Norway", "structural labour supply", "opportunity heterogeneity"]
priority: "very high"
read_status: "extracted"
------------------------

# Full citation

Dagsvik, John K., and Steinar Strøm. 2006. “Sectoral labour supply, choice restrictions and functional form.” *Journal of Applied Econometrics* 21(6): 803–826. The preprint notes that the earlier title was “Analyzing labor supply behavior with latent job opportunity sets and institutional choice constraints.” 

# One-sentence contribution

The paper develops a structural labour-supply framework in which individuals choose among latent job opportunities characterized by sector, wage, hours, and non-pecuniary attributes, and uses it to estimate sectoral labour supply for married women in Norway. 

# Why this paper matters

This paper is highly important for your project because it is one of the clearest early formulations of labour supply as choice over latent job packages rather than direct choice over leisure and disposable income. It explicitly introduces unobserved heterogeneity in opportunities, not only in tastes, and therefore moves much closer to your (A)-type object than standard labour-supply models do. 

It also matters because the authors explicitly discuss the confounding between preferences and opportunity restrictions, and because they try to justify utility functional form using invariance principles rather than purely ad hoc convenience. That combination—latent opportunities plus theoretical attention to structural form—is unusually relevant for your JMP. 

# Core research question

How can labour-supply behaviour be modeled when workers choose among latent job opportunities with sector-specific wages, fixed hours, and non-pecuniary job attributes, under complicated budget constraints and institutional hours restrictions? 

# Economic setting and context

The paper is motivated by features of real labour markets that standard models abstract from: jobs differ in non-pecuniary content, hours are often fixed by the job, and labour markets impose quantity constraints and institutional restrictions on hours. The authors emphasize that these aspects are especially relevant in unionized and regulated labour markets. 

The empirical application is to married women in Norway in 1994, choosing whether to work and, if so, whether to work in the public or private sector. The public/private distinction is substantively important because the sectors differ in wages, regulation, job security, and the nature of tasks. 

# Model / theoretical framework

The model class is a structural random-utility labour-supply model with latent job opportunity sets. The key departure from the traditional labour-supply model is that the worker does not choose hours and consumption directly from a universal feasible set. Instead, labour supply is the outcome of choosing from a latent set of jobs, where each job is characterized by hours, wage, sector, and non-pecuniary job attributes. 

In the one-person setup, utility is written as (U(C,h,z)=v(C,h)\varepsilon(z)), where (z) indexes market and non-market opportunities, (C=f(hw,I)) is after-tax household income, and (\varepsilon(z)) captures unobserved taste shifters and latent job-type attributes. The economic budget set is therefore only one part of the environment; the other part is the latent opportunity set. 

The feasible set is modeled explicitly through a Poisson-process representation of latent job opportunities. A job opportunity has fixed hours and wages, and the intensity measure generates an opportunity density over hours and wages. In the sectoral extension, the model assigns sector-specific opportunity densities and sector-specific pure preference weights. 

The framework is positive rather than normative. Its aim is to model observed labour-supply and sector choice under restrictions and unobserved heterogeneity. The paper does mention that the framework is suitable for estimating uncompensated and compensated labour-supply elasticities, but it does not develop a normative welfare theory. 

# Key objects

The main objects are the deterministic utility component (v(C,h)), the random taste/job shifter (\varepsilon(z)), the tax-benefit mapping (f(hw,I)), the opportunity density over jobs, and the sector-specific opportunity parameters (b_j=\mu_j\theta_j). In the multisectoral extension, (\mu_j) captures average sector-specific preference for sector (j), while (\theta_j) captures the relative availability of sector-(j) jobs. 

A central object is the opportunity density. In the one-sector version it is (\theta g(h,w)); in the sectoral version it becomes sector-specific through (g_j(h,w)) and (b_j). This object is the paper’s closest empirical analogue to an opportunity-set representation. 

Another key object is the product (v_2(h)g_2(h)), which the authors show is what is nonparametrically identified from observed behaviour when offered hours are not assumed uniform. This is important because it makes explicit where preference and opportunity terms are entangled. 

# Data

The labour-supply estimation uses a merged Norwegian sample from the “Survey of Income and Wealth, 1994” and the “Level of Living Conditions, 1995.” The sample includes married couples and cohabiting couples with common children, with spouses aged 25–64, excluding the self-employed and those on disability or related benefits. 

The final sample used to estimate the labour-supply model contains 824 married women. The wage equations are estimated on a larger sample because wage information for single women is also used there. Table 1 reports descriptive statistics by not working, public sector, and private sector. 

# Identification logic

Identification is structural and partly parametric. The paper is explicit that, without additional assumptions, one can identify only the product of the preference component over hours and the opportunity density over hours. In particular, under multiplicative separability, (v_2(h)) and (g_2(h)) cannot generally be disentangled nonparametrically from observed labour-supply outcomes. 

The paper states that if preferences are multiplicatively separable in consumption and hours and fixed costs of working are observed, then (v_1(C)) and the wage-offer density can be nonparametrically identified, but (v_2(h)) and (g_2(h)) remain confounded unless additional assumptions are imposed. Their solution in the empirical application is to impose functional-form structure on utility and a parametric structure on the opportunity distribution of hours. 

Identification therefore relies on a combination of: structural assumptions on the stochastic choice environment, invariance-motivated functional form for utility, independent random effects in sectoral opportunity densities, and first-stage wage equations. This is not quasi-experimental identification; it is a maintained-structure approach. [reasonable inference for my project] supported by 

# Estimation / empirical strategy

The empirical model focuses on married women who can choose between not working, public-sector work, and private-sector work. Offered hours are discretized into seven intervals in each sector, with explicit part-time and full-time peaks in the offered-hours distribution. The peaks are interpreted as institutional constraints rather than preference spikes. 

The wage equations are estimated first, using a selection-corrected approach. The structural labour-supply model is then estimated by maximum likelihood, with random effects introduced in the opportunity densities to account for unobserved heterogeneity. Expectations in the choice probabilities are computed by simulation. 

The model fit is evaluated by comparing observed and predicted aggregates. Table 4 reports that the model reproduces choice probabilities and sector-specific hours well, and the reported McFadden (\rho^2) is 0.21. 

# Treatment of preferences

Preferences are modeled as preferences over consumption, hours, and sector/job-specific non-pecuniary attributes. This is a stronger treatment of preferences than in standard labour-supply models because the worker may value the type of work or sector itself, not only income and leisure. 

The deterministic part of utility is given a Box–Cox-type functional form motivated by invariance arguments drawn from psychophysics and measurement theory. The paper derives a class of admissible functional forms from assumptions about meaningfulness under rescaling of consumption and leisure. This is a distinctive theoretical feature of the paper. 

At the same time, the paper is careful that observed concentrations of hours at part-time and full-time cannot automatically be interpreted as preference peaks. It argues that these peaks may instead reflect institutional choice constraints, which is a central difference from much of the previous literature. 

# Treatment of opportunities / constraints

This section is the core reason the paper is so relevant for your project. The framework explicitly models latent, individual-specific opportunity sets of jobs. Jobs differ by fixed hours, sector-specific wages, and non-pecuniary attributes, and the distribution of available jobs varies across individuals. The paper states explicitly that there are two sources of unobserved heterogeneity: tastes and opportunities. 

The model also treats institutional quantity constraints seriously. Offered hours are not assumed to be uniformly available; instead, the offered-hours distribution has peaks at part-time and full-time. These peaks are interpreted as reflecting regulation, union bargaining, and labour-market institutions rather than pure taste for specific hours. 

This means the paper does model opportunities explicitly, although in a latent probabilistic way rather than as an observed set-valued correspondence (A_i). It helps distinguish preference heterogeneity from opportunity heterogeneity conceptually and structurally, even though the two are not fully separated nonparametrically in estimation. 

It also clearly rejects the assumption of a universal common choice set. In its sectoral setting, different women face different sector-specific opportunity densities, and education shifts those opportunity densities, especially in the public sector. 

# Welfare / normative object

The paper is primarily positive. It does not construct an individual welfare measure, social welfare function, or responsibility-sensitive criterion. Its stated welfare-related contribution is that the framework provides a flexible way to estimate uncompensated and compensated labour-supply elasticities in the presence of random utilities and complex budget sets. 

There is therefore no explicit treatment of responsibility for opportunities, compensation for unequal opportunities, or reference opportunity sets. The paper is useful for those questions only indirectly, because it gives a positive representation of unequal opportunities that a later welfare analysis could build on. [reasonable inference for my project] supported by 

The paper does not provide a decomposition of inequality into preferences and opportunities, but it is unusually close to such a decomposition architecture because it insists on modeling both objects separately in the behavioural structure. [reasonable inference for my project] supported by 

# Main findings

The main theoretical finding is that labour supply can be modeled coherently as choice among latent job opportunities, and that this framework can accommodate both complicated non-convex budget sets and institutional restrictions on hours. The paper also argues that invariance principles can meaningfully narrow the admissible functional forms for utility. 

Empirically, the model fits Norwegian data on married women reasonably well. Table 4 shows that predicted probabilities of not working, public-sector work, and private-sector work are close to the observed fractions, and predicted sector-specific annual hours are also close to observed averages. 

The estimates imply that higher education raises public-sector job opportunities and reduces private-sector opportunities, conditional on the maintained specification. The paper interprets this as evidence that higher-educated women have more feasible jobs in the public sector. 

The full-time peak in offered hours is estimated to be more pronounced in the public sector than in the private sector, consistent with the idea that the public sector is more regulated and unionized. 

The wage-elasticity results in Table 6 show that overall labour-supply responses are modest, but inter-sector mobility responses are much larger. A 1 percent wage increase in one sector generates substantial movement into that sector and out of the other, while overall participation changes only slightly. 

# Main limitations

A first limitation is that the empirical application does not use the full richness of the theoretical framework. The only observed non-pecuniary job attribute is sector; other job characteristics remain latent. This limits how far the paper can go empirically in mapping actual opportunity sets. 

A second limitation is identification. The paper is explicit that certain preference and opportunity components are confounded nonparametrically, especially (v_2(h)) and (g_2(h)). The empirical separation therefore depends on parametric assumptions about functional form and about the offered-hours distribution. 

A third limitation is that the paper abandons full estimation of the offered wage density because of practical difficulties. Instead it works with subjective mean offered wages and first-stage wage equations. This is operationally sensible, but it means the opportunity side is only partially modeled in practice. 

A fourth limitation is that the framework is not an equilibrium model. The estimated model is used for simulations conditional on the opportunity density, but the paper is explicit that it does not model how opportunity densities themselves are generated in equilibrium. 

# Relevance for my JMP

## possible use for framing

This paper is one of the strongest framing references for arguing that labour supply should be analyzed as job choice under latent opportunity constraints rather than as unconstrained choice over leisure and income. It also supports the claim that observed hours concentrations need not be interpreted as pure preference phenomena. 

## possible use for model design

It is extremely useful for model design. It gives a concrete architecture with latent jobs, sector-specific opportunity densities, fixed hours by job, and non-pecuniary job attributes. For any RURO-adjacent structural labour-supply model, this paper is close to foundational. 

## possible use for identification

It is useful because it makes explicit where identification is difficult: preference over hours and opportunity over hours are entangled without extra assumptions. That is directly relevant if your project aims to separate (R) from (A) empirically. 

## possible use for welfare measurement

Direct use is limited because the paper does not define a well-being measure. Indirectly, it is highly useful because it provides a positive model in which both preferences and opportunities are represented distinctly enough to feed a later welfare measure (W(z,R,A;y)). [reasonable inference for my project] supported by 

## possible use for decomposition

The paper does not perform a formal decomposition, but it is one of the most promising empirical foundations for one. In particular, it suggests how one could attribute part of observed labour-supply differences to sectoral opportunity densities and part to preferences, subject to identification limits. [reasonable inference for my project] supported by 

## possible use for comparative application

The paper is Norway-specific in application, but the framework is portable to other institutional contexts with sectoral labour markets, regulated hours, and tax-benefit complexity. It is especially relevant for countries with strong unions or public-sector labour-market segmentation. [reasonable inference for my project] supported by 

# Research questions this paper inspires

Can a latent sectoral opportunity density be translated into a normatively meaningful feasible-set object (A_i) for a jobs-and-wellbeing measure?

How much of the observed public/private sector sorting of married women is due to sector-specific opportunities versus sector-specific tastes?

Can the confounding between (v_2(h)) and (g_2(h)) be weakened by adding desired-hours data, vacancy data, or administrative employer-side data?

What changes in labour-supply and welfare decomposition arise when institutional peaks in offered hours are treated as opportunity constraints rather than as preference peaks?

Can one define responsibility-sensitive welfare criteria that compensate for sectoral opportunity restrictions but not necessarily for preference differences across sectors?

# Challenge to this paper

The strongest challenge is that, although the framework is conceptually very rich on opportunities, the empirical implementation still requires strong structure and only partially observes the opportunity side. In particular, once sector is the only observed qualitative job attribute and wage-offer densities are simplified, one may worry that some opportunity variation is still absorbed into taste or residual terms. That does not undermine the framework, but it does limit how literally one should interpret the estimated opportunity distribution as the true feasible set. [reasonable inference for my project] supported by 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] This paper is unusually close to your framework because it treats labour supply as resulting from choice among latent jobs rather than direct choice over hours and income. It explicitly models both unobserved tastes and unobserved opportunities, and it allows job attributes to include sector, wages, hours, and non-pecuniary content. 

[reasonable inference for my project] A natural mapping is that the realized sector-hours-income outcome corresponds to the realized bundle (z); the deterministic and random utility components correspond to (R); the latent job opportunity set and its density correspond to (A); and the sector-specific wage/tax system enters through the pay side (y). The mapping is not exact because the paper uses probabilistic opportunity densities rather than literal observed feasible sets. supported by 

[explicit in paper] The paper does not define a welfare measure (W(z,R,A;y)), does not impose axioms on the role of opportunities, and does not address responsibility or compensation directly. Those questions are not part of its stated agenda. 

[reasonable inference for my project] In your taxonomy, the paper is very far from independence of (A): its entire point is that (A)-type restrictions matter for observed labour supply. It is also not close to laissez-faire evaluation, because it is not an evaluative paper at all. Its real value is as one of the strongest positive micro-foundations for taking (A) seriously in a later well-being framework. supported by 

[unclear from paper] It is unclear how the estimated opportunity densities should be normatively interpreted—whether as actual feasible sets, reduced-form proxies for them, or equilibrium outcomes that should themselves be morally neutralized. The paper does not address that. 

# Relation to Bargain et al. (2013)

This paper is best viewed as a methodological precursor rather than a direct substitute. It is closer to the positive structural side of the labour-supply-and-welfare literature: it enriches the behavioural model by introducing latent jobs, sectoral choice restrictions, and non-pecuniary job attributes. For your purposes, its main relation to the later welfare-comparison literature is that it supplies a richer opportunity-sensitive behavioural base on top of which welfare comparisons could later be built. [reasonable inference for my project]

# Relation to opportunities vs preferences

This paper is one of the strongest in your corpus on the opportunities-versus-preferences distinction. It explicitly states that there are two sources of unobserved heterogeneity—tastes and opportunities—and it builds the labour-supply model around that distinction. 

At the same time, it also shows why the distinction is empirically difficult: some opportunity and preference components remain entangled without additional assumptions. This makes the paper especially valuable for your project, because it is not merely conceptually aligned with your concern; it demonstrates the practical econometric difficulty of separating the two. 

# Useful quotations / formulas

A central formula is the probability density of realized hours and wages:
[
\varphi(h,w;I)=\frac{\theta g(h,w)\psi(h,w;I)}{\psi(0,0;I)+\theta\int!!\int_D \psi(x,y;I)g(x,y),dx,dy},
]
for positive (h) and (w). This is the key expression linking preferences and opportunities. 

The sectoral extension replaces this with sector-specific opportunity densities and parameters (b_j=\mu_j\theta_j), which is the main empirical object in the two-sector application. 

The utility functional form derived from invariance arguments is a Box–Cox-type specification of the form
[
\log v(C,h)=\beta_1\frac{C^{\alpha_1}-1}{\alpha_1}+\beta_2\frac{L^{\alpha_2}-1}{\alpha_2}+\beta_3\frac{(C^{\alpha_1}-1)(L^{\alpha_2}-1)}{\alpha_1\alpha_2},
]
in the theorem-level presentation. This is one of the paper’s most distinctive theoretical contributions. 

The key empirical results are in Table 4 for fit and Table 6 for wage elasticities. Table 6 is especially useful because it shows that weak aggregate labour-supply responses mask much stronger inter-sector mobility responses. 

# Suggested tags

latent-job-opportunities, sectoral-labour-supply, choice-restrictions, opportunity-density, nonpecuniary-job-attributes, public-private-sector, functional-form-invariance, Norway

# My quick takeaway

This is one of the most important papers for your JMP. It does not solve the welfare problem, but it provides a rigorous positive structure in which labour supply depends on both preferences and unequal opportunities, with explicit sectoral and institutional constraints. It is especially valuable because it does not simply assert that opportunities matter; it shows how to model them, where identification becomes difficult, and why standard preference-only interpretations of observed hours patterns can be misleading. For your project, this is very close to a positive foundation for the (A)-dimension in (W(z,R,A;y)).
