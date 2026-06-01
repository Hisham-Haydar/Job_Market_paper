
---

title: "Sectoral labour supply, choice restrictions and functional form"
authors: ["John K. Dagsvik", "Steinar Strøm"]
year: 2006
outlet: "Journal of Applied Econometrics"
country_or_context: "Norway"
population: "Married women in Norway, with sector choice between public and private employment; husband's labor supply treated as given in the empirical application"
data_period: "1994 Norwegian income/tax environment; labor supply sample from merged 1994–1995 Norwegian survey data"
shelf: "sectoral_labour_supply_choice_restrictions"
tags: ["sectoral labor supply", "latent jobs", "choice restrictions", "opportunity sets", "public vs private sector", "non-pecuniary job attributes", "functional form", "labor supply elasticities", "Norway", "structural model"]
priority: "high"
read_status: "extracted"
------------------------

# Full citation

Dagsvik, John K., and Steinar Strøm. 2006. “Sectoral labour supply, choice restrictions and functional form.” *Journal of Applied Econometrics* 21(6): 803–826. DOI: 10.1002/jae.866. 

# One-sentence contribution

The paper develops and estimates a structural labor supply model in which married women choose among latent sector-specific jobs with fixed hours, sector-specific wages, and non-pecuniary attributes, and uses this framework to study labor supply, sector choice, and wage elasticities under institutional hours restrictions. 

# Why this paper matters

This paper matters because it is one of the clearest early statements of the latent-jobs view of labor supply within applied econometrics. It argues that labor supply is better understood as job choice under quantity constraints than as free choice over a smooth consumption-leisure set, and it embeds this in a tractable empirical model with taxes, sectoral wages, and institutional peaks at part-time and full-time hours. 

For your JMP, the paper is highly relevant because it is explicitly about the distinction between preferences and opportunities. It models unobserved heterogeneity both in tastes and in job opportunities, allows sector-specific job attributes, and treats observed clustering of hours as potentially arising from constraints rather than from preferences alone. It is therefore very close to your opportunity-set and latent-job agenda. 

# Core research question

How can labor supply be modeled when workers choose among latent sector-specific jobs characterized by hours, wages, and non-pecuniary job attributes, and what does such a model imply empirically for sector choice, labor supply elasticities, and the interpretation of observed hour concentrations in Norway? 

# Economic setting and context

The empirical setting is Norway in the mid-1990s. The application studies married women choosing between the public and private sector, with the husband’s labor supply treated as exogenous. The paper emphasizes that public and private jobs differ not only in wages but also in job security, working conditions, unionization, work organization, and the availability of part-time and full-time contracts. 

The institutional environment matters centrally. The Norwegian tax and transfer system creates nonlinear and potentially non-convex budget sets, while unionization and sectoral regulation shape hours availability. The paper specifically interprets peaks at part-time and full-time hours as reflecting institutional restrictions and negotiation outcomes rather than only tastes. 

# Model / theoretical framework

The model is a static structural labor supply model in which the fundamental choice object is a job. Jobs are latent alternatives characterized by offered wage rate, offered hours, sector, and non-pecuniary job attributes. The model is therefore not a conventional continuous labor supply model and not merely a finite-hours discrete-choice model; it is a latent opportunity-set/job-choice framework. 

Utility takes multiplicative random-utility form. In the single-agent exposition,
[
U(C,h,z)=v(C,h)\varepsilon(z),
]
where (v(C,h)) is the systematic utility component and (\varepsilon(z)) captures unobserved taste shifters related to latent job attributes. Disposable income is determined by the exact tax-transfer mapping (C=f(hw,I)). 

The feasible set is an individual-specific latent set of job opportunities. This is the crucial departure from standard labor supply. Choice constraints are represented through an opportunity density over jobs, with separate sector-specific opportunity densities in the empirical model. The framework is purely positive in this paper; it does not construct a welfare ranking or social welfare function. 

# Key objects

The central structural objects are the deterministic utility function (v(C,h)), the job-specific taste shifters (\varepsilon(z)), and the opportunity density over feasible jobs. In the sectoral extension, sector-specific opportunity densities (g_j(h,w)) and job-availability terms (b_j) summarize how many public- and private-sector jobs are effectively available to the agent. 

The main behavioral objects are sectoral participation probabilities, annual hours in public and private employment, sectoral and aggregate labor supply elasticities, and sectoral wage responses. The empirical application also focuses on full-time and part-time peaks in offered hours as objects of independent economic meaning rather than as merely reduced-form dummies. 

A key theoretical object is the decomposition (v_2(h)g_2(h)), which the paper shows is what can be nonparametrically recovered when offered-hours constraints are present. This point matters because it says that the hours preference term and the offered-hours distribution are not separately identified without extra structure. 

# Data

The labor supply application uses a merged Norwegian sample based on the “Survey of Income and Wealth, 1994” and “Level of Living Conditions, 1995.” The estimation sample for the labor supply model consists of 824 married or cohabiting women with common children, aged 25–64, whose spouses are neither self-employed nor on disability or similar benefits. 

The data distinguish non-working women, women in the public sector, and women in the private sector. Table 1 reports 66 non-workers, 405 public-sector workers, and 353 private-sector workers. Mean annual hours are about 1,641 in the public sector and 1,570 in the private sector; mean observed wage rates are about NOK 104.3 in the public sector and NOK 100.6 in the private sector. 

The model uses detailed after-tax disposable household income and observed hours from main and side jobs. Wage equations are estimated on a larger sample, including single women, because the labor supply model itself applies only to married women while wage estimation benefits from broader support. 

# Identification logic

Identification is structural and partly parametric. The paper explicitly notes that, nonparametrically, only the product of the leisure-preference component and the offered-hours distribution can generally be identified. In particular, (v_2(h)) and (g_2(h)) cannot be separated without additional assumptions. 

The identifying strategy therefore uses functional-form restrictions. The systematic utility function is restricted using invariance arguments from psychophysics, yielding a Box–Cox–type specification. On the opportunity side, sectoral offered-hours distributions are assumed uniform except for peaks at part-time and full-time hours, and sectoral wages are introduced through estimated wage equations plus random effects. 

This is central for your agenda: the paper does not simply assume that observed full-time and part-time bunching reveals preferences. It says that without extra assumptions one cannot disentangle preference for particular hours from institutional or organizational concentration of job offers at those hours. That is one of the paper’s main identification lessons. 

# Estimation / empirical strategy

The paper estimates a sectoral choice/labor supply model for married women choosing between non-participation, public-sector work, and private-sector work. Offered hours are discretized into seven intervals per sector, with full-time corresponding to the interval centered at 1,950 annual hours and part-time to the interval centered at 1,040 hours. 

The wage equations are estimated first, using experience, experience squared, education, and a selection correction term derived from reduced-form sectoral participation probabilities. In the structural model, unobserved heterogeneity in the wage opportunity densities is handled through random effects, and the remaining parameters are estimated by maximum likelihood with simulated expectations. 

The empirical model is then used to generate sector-specific and aggregate uncompensated wage elasticities. The paper also compares the preferred specification, in which offered hours have institutional peaks, to an alternative specification with uniformly distributed offered hours in order to show how much of the observed hours concentration is being attributed to opportunity restrictions versus preferences. 

# Treatment of preferences

Preferences are modeled over consumption and leisure, with additional latent job/sector attributes entering through the random taste shifters. The paper’s central substantive point is that people may care about job type and sectoral characteristics, not only about hours and income. This is one reason why labor supply should be modeled as job choice. 

The deterministic utility specification is justified through invariance arguments rather than chosen only for convenience. The resulting functional form is a generalized Box–Cox specification in consumption and leisure, with age and children shifting the marginal utility of leisure. In the empirical estimates, the marginal utility of leisure depends strongly on age and children, while the interaction between consumption and leisure is not significant. 

At the same time, the paper is careful not to treat observed clustering of hours as preference evidence by default. This is important. A model that assumes uniform offered hours necessarily interprets peaks as preference for those hours. The paper argues that this is often implausible in a unionized and institutionally regulated labor market. 

# Treatment of opportunities / constraints

This is the most important section for your research interests.

The paper models opportunities explicitly. The agent faces a latent individual-specific set of feasible jobs, and jobs differ by hours, wages, sector, and non-pecuniary attributes. Thus labor supply is not free choice over a common hours grid. There are two distinct sources of unobserved heterogeneity: tastes and opportunities. 

The empirical opportunity distributions are sector-specific. Offered hours are assumed uniform except for part-time and full-time peaks, with sectoral differences in those peaks. In particular, the full-time peak is estimated to be more pronounced in the public sector than in the private sector, consistent with the authors’ interpretation of stronger institutional regulation in the public sector. 

This makes the paper highly relevant to the opportunities-versus-preferences distinction. It explicitly argues that if offered hours are not uniformly distributed, then a model that imposes uniform offered hours will falsely treat institutional constraints as preferences. That is almost exactly the concern behind your agenda. The limitation is that opportunities are modeled in relatively low-dimensional reduced form: sector, hours, and wage, rather than a richer latent-job distribution with explicit occupation, task, or amenity vectors. 

# Welfare / normative object

None in the direct sense. The paper does not construct a welfare measure, equivalent income, compensating variation, or social welfare function. It is a positive structural labor supply paper focused on modeling behavior under taxes and choice restrictions. 

Its policy relevance is indirect. By changing the behavioral model of labor supply, it changes the foundation on which one would later compute welfare effects or reform responses. But the paper itself stops at sector choice, participation, hours, and elasticities. 

# Main findings

First, the model fits the Norwegian data reasonably well. Table 4 shows predicted and observed aggregates for non-participation, public-sector work, and private-sector work are close, and the reported McFadden pseudo-(R^2) is 0.21. 

Second, the estimates imply that highly educated women face more public-sector opportunities and fewer private-sector opportunities, conditional on wages. This is captured through the estimated sector-specific opportunity parameters (b_1) and (b_2). 

Third, the public sector exhibits a more pronounced full-time peak in the opportunity distribution than the private sector. The paper interprets this as consistent with stronger regulation and unionization in the public sector. 

Fourth, overall female labor supply elasticities are moderate, but sectoral mobility is much stronger. Table 6 shows that a 1% wage increase in the public sector raises the probability of public-sector work by about 1.47% while reducing private-sector participation by about 1.32%; similarly strong but opposite substitution appears for private-sector wage increases. This is one of the paper’s most important substantive findings. 

Fifth, aggregate overall responses look small partly because inter-sectoral substitution offsets them. The paper’s conclusion explicitly emphasizes that weak overall female labor supply responses conceal much stronger mobility across sectors. 

Sixth, when offered hours are instead assumed uniformly distributed, the estimated leisure-side parameters change substantially while the consumption-side parameters remain similar. The paper interprets this as evidence that treating hour peaks as preferences rather than as constraints materially alters the structural interpretation. 

# Main limitations

A first limitation is that the empirical application does not exploit the full latent-job framework. The only observed non-pecuniary job attribute used is sector. Other job attributes remain latent and are absorbed into random taste shifters. 

A second limitation is that the model estimates only the marginal density of chosen hours and sector because the authors abandon full specification of the wage-offer density (g_1^j(w)) in the application. This simplifies estimation but means the full job-offer structure is not recovered. 

A third limitation is that the application treats the husband’s labor supply as given. The paper notes that the framework can be extended to couples jointly, and an appendix sketches that extension, but the estimated empirical model is still one-sided. 

A fourth limitation, relative to your broader agenda, is that the opportunity side is reduced-form and partial-equilibrium. It is sector-specific and hours-specific, but not a richer market-equilibrium or occupation/task-level opportunity process. 

# Relevance for my JMP

## possible use for framing

This paper is excellent for framing a JMP that argues labor supply should be modeled as constrained job choice rather than free hours choice. It gives both the conceptual and empirical case for that claim. 

## possible use for model design

It is highly useful for model design because it shows how to incorporate sector-specific wages, part-time/full-time opportunity peaks, and latent non-pecuniary job attributes in one coherent framework. It is a natural precursor if you want to move toward a richer RURO or latent-job model. 

## possible use for identification

This paper is especially useful for identification because it makes clear that hours bunching cannot be read as preferences without assumptions on the offered-hours distribution. That is a direct warning against conflating opportunity constraints with tastes. 

## possible use for welfare measurement

Indirectly useful. It does not provide a welfare criterion, but it shows that any later welfare analysis based on standard labor supply estimates may be misspecified if it ignores sectoral choice restrictions and non-uniform offered hours. 

## possible use for cross-country comparison

The paper is not cross-country, but it suggests a clear cross-country research direction: estimate country-specific sectoral/job opportunity distributions and test how much of apparent preference heterogeneity is actually institutional heterogeneity in available jobs and offered hours. 

# Research questions this paper inspires

How much of the cross-country variation in female labor supply elasticities is due to differences in sector-specific opportunity densities rather than differences in preferences? 

Would a richer latent-job model with observed occupations and tasks change the paper’s result that overall labor supply responses mask large inter-sector mobility? 

Can one combine this sectoral latent-job framework with a welfare metric that distinguishes welfare losses from poor opportunities from welfare differences due to preferences? 

How sensitive are optimal tax or transfer simulations to assuming uniform offered hours when actual labor markets exhibit strong institutional peaks at part-time and full-time work? 

# Challenge to this paper

The strongest simplifying move is that the opportunity side is still represented by reduced-form sectoral densities with stylized full-time and part-time peaks. That is already far better than a frictionless hours-choice model, but it leaves open the richer question of how occupations, tasks, working conditions, and firm-side demand jointly generate those opportunity distributions. A future paper could challenge this by moving from sector-specific opportunity densities to a richer latent-job distribution with observed job characteristics and perhaps an explicit equilibrium component. 

# Relation to Bargain et al. (2013)

This paper is methodologically upstream of Bargain et al. (2013). Bargain et al. uses structural labor supply estimation to derive welfare rankings under heterogeneous preferences, while Dagsvik and Strøm focus on the behavioral model itself and insist that sectoral and institutional opportunity restrictions must be modeled explicitly. Relative to Bargain et al. (2013), this paper is much stronger on the opportunity-set side and much weaker on the normative side, since it does not proceed to welfare comparison. For your corpus, it is a foundational behavioral paper that helps diagnose what later welfare papers may be missing. 

# Relation to opportunities vs preferences

This paper is strongly on the side of separating opportunities from preferences. Its core empirical message is that observed full-time and part-time peaks should not automatically be interpreted as preferences, because they may instead reflect institutional choice restrictions and non-uniform job availability. At the same time, the paper also shows that this separation is not automatic: without additional assumptions, preference for hours and offered-hours opportunities are entangled. That combination of ambition and caution makes it highly relevant to your agenda. 

# Useful quotations / formulas

The core utility specification is
[
U(C,h,z)=v(C,h)\varepsilon(z),
]
with jobs indexed by (z) and characterized by wages, hours, and non-pecuniary attributes. This is the paper’s central behavioral object. 

The key sectoral choice density is
[
\varphi_j(h,w;I)=
\frac{\psi_j(h,w;I),\mu_j\theta_j g_j(h,w)}
{\psi(0,0;I)+\sum_k \mu_k\theta_k \int!!\int \psi_k(x,y;I)g_k(x,y),dx,dy},
]
for (j=1,2). This formula shows directly that sectoral labor supply depends jointly on preferences and sector-specific opportunity densities. 

A concise statement of the paper’s most important methodological point is that if offered hours are not uniformly distributed, then a model assuming uniform offered hours will interpret institutional constraints as preferences. That is the essential lesson of the comparison reported around Table 5. 

# Suggested tags

#sectoral_labor_supply #latentjobs #choice_restrictions #opportunity_sets #public_private_sector #functional_form #hours_constraints #structural_model #Norway #labor_supply_elasticities

# My quick takeaway

If I only remember one thing from this paper for my JMP, what should it be? That weak aggregate labor supply responses can conceal strong movement across constrained job opportunities, and that unless sectoral and hours restrictions are modeled explicitly, structural labor supply estimates may misread institutional opportunity structure as household preference.
