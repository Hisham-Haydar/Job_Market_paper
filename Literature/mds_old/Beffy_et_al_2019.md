---

title: "Labour supply and taxation with restricted choices"
authors: ["Magali Beffy", "Richard Blundell", "Antoine Bozio", "Guy Laroque", "Maxime Tô"]
year: 2019
outlet: "Journal of Econometrics"
country_or_context: "United Kingdom"
population: "Working-age mothers in the UK, including single mothers and married/cohabiting mothers"
data_period: "1997–2002 UK Family Expenditure Survey"
shelf: "restricted_choices_taxation_uk_mothers"
tags: ["labour supply", "restricted choices", "consideration set", "hours restrictions", "nonlinear budget constraints", "tax-benefit system", "fixed costs", "female labour supply", "UK", "identification"]
priority: "high"
read_status: "extracted"
------------------------

# Full citation

Beffy, Magali, Richard Blundell, Antoine Bozio, Guy Laroque, and Maxime Tô. 2019. “Labour supply and taxation with restricted choices.” *Journal of Econometrics* 211(1): 16–46. [https://doi.org/10.1016/j.jeconom.2018.12.004](https://doi.org/10.1016/j.jeconom.2018.12.004). 

# One-sentence contribution

The paper develops and estimates a structural labour-supply model in which women choose rationally from a restricted random set of hours offers, and shows how nonlinear tax-benefit schedules help identify both preferences and the distribution of feasible hours offers. 

# Why this paper matters

This paper matters because it provides one of the clearest modern formulations of labour supply with restricted hours choices. It does not merely add ad hoc hours dummies or fixed costs; it explicitly models the feasible set as a random subset of possible hours. That is a substantial advance over the unrestricted-hours framework when one wants to distinguish preferences from demand-side constraints. 

For your potential JMP, this paper is especially important because it is close to your agenda on opportunity sets and constrained choice. It is not a full RURO or latent-jobs model in the wage-hours-characteristics sense, but it is a serious and explicit restricted-choice model with formal identification results. It also uses nonlinear budget constraints as a source of identification, which is methodologically very useful for structural labour-supply work under taxes and transfers. 

# Core research question

How can one identify and estimate preferences and labour-supply behavior when individuals choose hours from a restricted and unobserved set of offers rather than from the full set of all feasible hours, especially in the presence of nonlinear tax and benefit schedules? 

# Economic setting and context

The empirical application concerns working-age mothers in the UK between 1997 and 2002. This is a period with important reforms to tax credits and welfare benefits, so the after-tax budget constraints faced by women vary in rich and policy-relevant ways. The paper exploits this institutional variation rather than treating the tax-benefit system as a background detail. 

The relevant policy environment is the UK tax, tax-credit, and welfare system, simulated in detail using IFS-Taxben. The paper emphasizes that nonlinearities and flat regions in budget constraints are not nuisances; they are economically informative because they create dominated hours ranges that should never be chosen under unrestricted optimization. The charts on page 5 illustrate this directly, showing budget constraints with flat segments and actual choices that fall in or near dominated regions. 

# Model / theoretical framework

The model class is a static structural labour-supply model with restricted choices over hours, embedded in an intertemporal/life-cycle-consistent setting. The woman chooses hours, employment, and implicitly consumption subject to nonlinear taxes, benefits, and fixed costs of work, but crucially does so over a restricted random subset of possible hours. 

The starting point is the standard unrestricted model with utility
[
E_t\int_t^T u_\tau(c_\tau,h_\tau),d\tau
]
subject to an intertemporal budget constraint with after-tax income (R(w,h)) and fixed costs of work (b). In the unrestricted model, the set (H) of possible hours is the positive line or a dense hours set. The paper then replaces this with a restricted-choice framework in which individuals choose from a random subset of hours. 

The key restricted-choice specification is a two-offer model. Each woman is assumed to face two independent hours offers: the observed one, if employed, and one alternative not chosen. The option of not working is always available. This is a constrained rational-choice model, closely related to the “consideration set” literature, but interpreted here as job packages restricted by the hours employers offer. 

The framework is positive rather than explicitly normative. It studies behaviour and identification, not welfare ranking or social choice. However, because it changes the behavioral foundation of labour supply under taxation, it is highly relevant for downstream welfare and optimal-tax analysis. 

# Key objects

The main objects are the preference parameters over consumption and leisure, the fixed cost of work, the wage equation, and the distribution of hours offers. The preference side is parameterized by
[
u(c,h)=\frac{c^{1-\gamma}}{1-\gamma}+\frac{(L-h)^{1-\phi}}{1-\phi}a,
]
where (a) governs the weight on leisure and depends on observables and unobserved heterogeneity. Fixed costs of work (b) also depend on observables and unobservables. 

The central opportunity object is the offer distribution over hours. In the theoretical sections, the offer probabilities are denoted (g_i). In the empirical model, offers are modeled as a mixture of two truncated normal distributions over hours, one concentrated around part-time and one around full-time work. This mixture is allowed to depend on observables such as education. 

The key choice object is an hours offer, not a full latent job with wage, hours, and amenities. Wage heterogeneity is modeled separately through a wage equation rather than directly inside the offer set. This distinction matters for your agenda: the paper is a restricted-hours model rather than a full latent-job opportunity model. 

# Data

The data are the UK Family Expenditure Survey (FES) for 1997–2002. The sample contains 10,575 women with children, including both lone mothers and married/cohabiting mothers. The survey provides detailed information on hours worked, earnings, education, demographic structure, and household consumption. 

The paper uses consumption from the FES to maintain consistency with a life-cycle framework and detailed tax-benefit simulation from IFS-Taxben to recover the full nonlinear budget constraint for each family. This is one of the paper’s major empirical strengths: it uses actual institutional nonlinearities rather than stylized budget sets. 

The descriptive tables show a sample with 63.2% of women in work overall, substantial educational heterogeneity, and strong variation in hours. Median usual hours are 26 per week and the median hourly wage is £5.85 in 1997 prices. Table 2 shows that non-workers are less educated, more likely to have more children, and less likely to be cohabiting. 

# Identification logic

This is one of the paper’s main contributions.

The paper first shows that with unrestricted hours choice, nonlinear budget constraints can imply sets of strictly dominated hours that should never be chosen by a rational agent with utility increasing in consumption and leisure. Observing individuals working at such hours therefore nonparametrically rejects the unrestricted choice model. This argument depends only on the shape of (R(w,h)), not on the full parametric utility specification. The examples on page 5 visualize this clearly: the blue horizontal lines mark hours ranges that are strictly dominated, while the red vertical lines show actual observed hours. 

The paper then establishes several identification results for the restricted-choice model. First, when the offer distribution is known, preferences can be identified. Second, when preferences are known, the offer distribution can be fully recovered. Third, with parametric restrictions on preferences and offers, identification is achieved when the Jacobian has full column rank. Fourth, with exclusion restrictions from the budget constraint, semi-parametric identification is possible. 

The crucial economic identification device is heterogeneity in budget constraints. Variation in wages, non-labour income, and tax-benefit nonlinearities changes the choice probabilities while leaving the offer distribution structurally separate. In particular, flat or decreasing segments of the budget constraint reveal the offer distribution more sharply because certain hours become dominated regardless of preferences. 

So the identification logic is exactly relevant to your interests: the paper exploits policy-induced budget-set shape to separate preferences from constraints. However, it separates preferences from a restricted set of hours offers, not from a full multidimensional opportunity set over jobs. 

# Estimation / empirical strategy

The empirical model is estimated by maximum likelihood. The authors first estimate a reduced-form consumption equation and then use a control-function approach so that consumption endogeneity can be accounted for in the labour-supply likelihood. The second-stage likelihood then combines wage, hours, and employment decisions conditional on consumption and the estimated error term from the first stage. 

The offer distribution is specified as a mixture of two truncated normals over hours, with means around part-time and full-time work. The preference side and fixed costs are parameterized with observed covariates and normally distributed unobserved heterogeneity. Three models are estimated: a baseline model, a version allowing correlation between wages, consumption, and preferences, and a richer version allowing observables to affect the offer distribution. 

The model is then evaluated through fit to employment, hours, wages, the joint distribution of hours and wages, the fraction of observations rejecting the unrestricted model, and through simulations of unconstrained versus constrained labour supply and wage elasticities. 

# Treatment of preferences

Preferences are modeled structurally over consumption and leisure, with heterogeneity in both the taste for leisure and fixed costs of work. The utility parameter (a) depends on family structure and unobserved heterogeneity, while the fixed cost (b) depends on observables such as cohabitation, children, and London residence. This allows substantial heterogeneity in both intensive and extensive margins. 

The estimates suggest, for example, that cohabiting women have a stronger preference for leisure but lower fixed costs of work, while younger children raise the preference for leisure and also affect fixed costs. These are not simply reduced-form associations; they are embedded in a structural utility-and-cost specification. 

But the paper is not about preference heterogeneity as a welfare object. Preferences are behavioral primitives only. There is no preference-respecting welfare evaluation, no equivalent income, and no attempt to derive welfare rankings across heterogeneous preferences. 

# Treatment of opportunities / constraints

This section is central for your agenda.

The paper models opportunities explicitly, but only along the hours dimension. Individuals do not choose from the full continuum of hours; instead, they choose from a random restricted subset of hours offers. This is a genuine constrained-choice framework, not a standard unrestricted hours model with an adjustment cost term layered on top. 

This is conceptually close to an opportunity-set model: the econometrician does not observe the available set directly, but infers the distribution of offers from the data and the tax-benefit environment. The paper repeatedly interprets these restricted sets as employer-provided job packages in hours space. 

However, the model’s opportunity side is one-dimensional. Offers are over hours only. Wages are modeled separately, not as jointly distributed components of job offers in the main empirical specification. The paper itself notes that a natural future extension would be to allow offers over wage-hours packages. This matters for your research direction: the paper is highly relevant as a restricted-choice labour-supply model, but it is not yet a full RURO or latent-job model with multidimensional job characteristics. 

# Welfare / normative object

None. The paper is positive and econometric. It does not construct equivalent income, compensating variation, money-metric utility, or any social welfare function. 

Its normative relevance is indirect but strong. If observed hours reflect both preferences and restricted opportunities, then any welfare or policy analysis built on unrestricted labour-supply models risks misinterpreting constrained choices as freely chosen outcomes. This is a foundational issue for any subsequent welfare analysis. 

# Main findings

First, the paper finds direct nonparametric evidence against the unrestricted-hours model. About 2.56% of working women are observed at hours belonging to strictly dominated ranges of their budget constraints. This is independent of the parametric utility specification and is shown both analytically and in the examples on page 5. 

Second, once the parametric utility structure is imposed, the rejection of the unrestricted model is much larger. Depending on the estimated (\phi), the share of working women whose observed hours violate the unrestricted model can be much higher; under the preferred specification, 7.93% of working women reject the unrestricted model. Table 8 and Figure 3 make this point. 

Third, the estimated offer distribution has a twin-peaked structure around part-time and full-time work. This is not imposed mechanically by the observed hours distribution; it is an estimated feature of the offer process. Table 5 and the fit in Figure 2 support this. 

Fourth, the constrained two-offer model fits the employment and hours distribution well, including the twin peaks in observed hours. Model 3, which allows observed heterogeneity in the offer distribution, provides the best fit among the three specifications. Table 7 and Figure 2 show this clearly. 

Fifth, constraints matter quantitatively. Simulating the economy without hours restrictions, the model predicts an employment rate of about 71%, compared with about 62.5% in the constrained two-offer case. So restrictions depress employment substantially relative to unconstrained labour supply. This is shown in Section 5.5.1 and Figure 6. 

Sixth, hours restrictions alter wage-response elasticities. Under the preferred specification, the average intensive-margin response to a 10% wage increase is about 0.35 in the unconstrained case but only 0.16 in the constrained two-offer case, while the extensive-margin response is slightly higher in the constrained case. Table 11 documents this. 

# Main limitations

A first limitation is that the offer set is only over hours. Wages are modeled separately rather than as attributes of offered jobs. This is explicitly less rich than a full latent-job or RURO model where opportunities are wage-hours-characteristics packages. 

A second limitation is that the empirical application uses a two-offer specification. This is analytically convenient and identifiable, but restrictive. The paper acknowledges that richer n-offer specifications are a natural extension. 

A third limitation is that the framework is not normative. It is highly informative for positive analysis and identification, but it does not itself tell you how welfare should be measured when people face restricted opportunities. 

A fourth limitation, relative to your agenda, is that the opportunity set is not a first-class welfare object; nor is it multidimensional. It captures employer-side restriction in hours offers, but not occupations, amenities, job quality, or equilibrium labour demand. 

# Relevance for my JMP

## possible use for framing

This paper is very useful for framing a JMP that argues observed labour supply is not simply revealed preference over a full feasible set. It provides a modern and rigorous statement of the restricted-choice problem and shows that nonlinear taxes can help detect and identify it. 

## possible use for model design

It is highly relevant for model design because it offers a clean restricted-choice framework that is more disciplined than ad hoc hours-constraint specifications. If your project aims to move from hours restrictions toward richer job opportunity sets, this paper is an excellent intermediate benchmark. 

## possible use for identification

This is perhaps the paper’s strongest contribution for your purposes. It shows how nonlinear budget constraints and exclusion restrictions can help identify preferences separately from opportunity constraints. The identification theorems and the semiparametric arguments are directly useful. 

## possible use for welfare measurement

Indirectly, the paper is very useful because it shows that unrestricted labour-supply models may misclassify constrained choices as chosen preferences. Any welfare metric built on such misclassified behavior may be misleading. But the paper itself does not provide the welfare solution. 

## possible use for cross-country comparison

The paper is UK-specific, but the methodology is highly relevant for cross-country work. Since tax-benefit nonlinearities differ across countries, the identification of restricted choice sets may also differ. This suggests a strong avenue for country-by-country estimation of constrained labour supply. 

# Research questions this paper inspires

How much of the cross-country variation in female labour supply elasticities is due to differences in restricted opportunity sets over hours rather than differences in preferences?

Can the two-offer hours model be extended to a multidimensional latent-job model in which offers consist jointly of wages, hours, and job characteristics?

Would welfare rankings of tax-benefit reforms change materially if labour supply were modeled with restricted offers rather than unrestricted hours choice?

How much of observed non-employment among low-income mothers reflects weak preferences for work versus missing acceptable job-hour offers? 

# Challenge to this paper

The strongest simplification is the reduction of opportunities to hours offers only. This is already a major advance over unrestricted-hours labour supply, but it still abstracts from the richer multidimensional nature of jobs. A future paper could challenge this by modeling the offer distribution over wage-hours-characteristics packages, so that preferences and opportunities are separated along more economically meaningful dimensions than hours alone. 

# Relation to Bargain et al. (2013)

This paper is related to Bargain et al. (2013) on the positive side but not on the normative side. Both rely on structural labour-supply modeling under taxation and both take seriously nonlinear budget constraints. But Bargain et al. (2013) uses estimated preferences for welfare comparison across countries, whereas Beffy et al. is focused on showing that those preferences may be misidentified if hours-choice restrictions are ignored. Relative to Bargain et al. (2013), this paper is stronger on the constrained-choice and identification side, but it does not proceed to welfare ranking. For your corpus, it is best read as a methodological foundation that can discipline later welfare work. 

# Relation to opportunities vs preferences

This paper clearly helps separate preferences from opportunities, though only in the restricted-hours dimension. Its main message is that observed hours reflect both preferences and the unobserved set of offered hours choices. Ignoring the latter leads to rejection of the unrestricted model and can distort elasticity estimates. This is strongly aligned with your agenda, even if the opportunity concept here is narrower than the latent-job or full opportunity-set concept you ultimately want. 

# Useful quotations / formulas

The core two-offer observed choice probability is
[
\ell_{2i}(Z,\beta)=g_i^2+2g_i\sum_{j\neq i}g_j,p_i({i,j},Z,\beta),
]
which is the most important formal expression in the paper for your agenda because it combines opportunity probabilities (g_i) with structural choice probabilities. 

The basic utility specification is
[
u(c,h)=\frac{c^{1-\gamma}}{1-\gamma}+\frac{(L-h)^{1-\phi}}{1-\phi}a,
]
with fixed costs of work and a nonlinear tax-benefit mapping (R(w,h)). This is the paper’s main positive behavioural specification. 

A short statement of the empirical contribution is that the paper finds women “working at hours of work that would be strictly dominated by other choices were a full range of hours choices to be available,” which provides direct evidence of restricted choice. 

# Suggested tags

#restricted_choices #labour_supply #hours_restrictions #consideration_set #nonlinear_budget_constraints #taxbenefit #female_labour_supply #identification #UK #structural_model

# My quick takeaway

If I only remember one thing from this paper for my JMP, what should it be? That nonlinear tax-benefit schedules can be used not only to identify labour-supply preferences, but also to reveal when observed hours are constrained choices from a restricted set of offers rather than free optimization over all hours.
