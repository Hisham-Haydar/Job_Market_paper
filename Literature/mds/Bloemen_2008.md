---

title: "Job Search, Hours Restrictions, and Desired Hours of Work"
authors: ["Hans G. Bloemen"]
year: 2008
outlet: "Journal of Labor Economics"
country_or_context: "Netherlands"
population: "Male individuals younger than 65 observed in unemployment or employment spells in the Dutch Socio-Economic Panel"
data_period: "October 1985 to April 1989"
shelf: "structural_job_search_hours_restrictions_desired_hours"
tags: ["job search", "hours restrictions", "desired hours", "structural labour supply", "reservation utility", "reservation wage-hours schedule", "Netherlands", "latent job offers", "unemployment duration"]
priority: "very high"
read_status: "extracted"
------------------------

# Full citation

Bloemen, Hans G. 2008. “Job Search, Hours Restrictions, and Desired Hours of Work.” *Journal of Labor Economics* 26(1): 137–179. 

# One-sentence contribution

The paper estimates a structural job-search model in which job offers arrive as wage-hours packages and uses subjective information on desired hours to separate preferred hours from offered hours, then applies the model to policy simulations on benefits and working-time reforms. 

# Why this paper matters

This paper matters because it directly addresses a core identification problem in the labour-supply-with-restrictions literature: observed hours combine preferences and employer-side constraints, and without extra information it is very difficult to disentangle them. Bloemen’s key move is to embed hours restrictions inside a structural search model and to use survey data on desired hours as an additional identifying source. 

For your project, this is highly relevant because the paper is explicitly about the gap between realized labour-market outcomes and the underlying opportunity environment. It is not a normative well-being paper, but it is one of the more directly useful empirical papers for thinking about how actual job opportunities constrain the realized bundle. 

# Core research question

How can one estimate a structural job-search model in which jobs differ not only by wages but also by fixed working hours, and what can subjective information on desired hours contribute to identifying preferences separately from hours offers? 

# Economic setting and context

The empirical setting is the Netherlands in the second half of the 1980s. The paper uses the Dutch Socio-Economic Panel and focuses on men younger than 65 who are observed in employment or unemployment between October 1985 and April 1989. 

The context is methodological and structural. The paper is motivated by limits of both the neoclassical labour-supply model and the standard empirical job-search model. The former treats observed hours as if they were chosen freely; the latter usually ignores hours as a job characteristic. Bloemen’s project is to merge these literatures. 

# Model / theoretical framework

The model class is a structural job-search model with hours restrictions. Unemployed individuals receive job offers according to a stochastic arrival process. Each offer contains both an hourly wage and a fixed weekly number of hours, drawn from a joint wage-hours offer distribution. The individual compares the value of search to the value of accepting a given wage-hours package. 

The agent does not choose hours freely from a budget set. Instead, the feasible opportunities are the wage-hours packages that happen to arrive. This is central. The paper therefore models opportunities explicitly on the positive side, though in latent distributional form rather than as a directly observed feasible-set object. 

The framework is purely positive, with policy simulations. It is not a normative social-choice or well-being framework. It studies unemployment duration, reservation wages as a function of hours, accepted hours, and policy responses, not justice or welfare rankings. 

# Key objects

The key behavioral objects are the utility function over net income and hours, the job-offer arrival rate, the layoff rate, and the joint wage-hours offer distribution. The arrival rate includes unobserved heterogeneity, and the hours offer distribution is discrete. 

A central theoretical object is the reservation utility level. Equivalently, for each offered hours level there is a reservation wage, so the reservation wage is a function of hours. The paper emphasizes that the reservation wage reaches a minimum at optimal hours, which gives the model a clear preference-based interpretation of hours mismatch. Figure 2 is the key visual summary. 

The other crucial object is desired hours. The paper uses survey responses on whether workers are satisfied with current hours and, if not, how many hours they would prefer. This is the main extra source of information used to separate optimal hours from offered hours. 

# Data

The data come from the Dutch Socio-Economic Panel, using waves from October 1985 through April 1989. The sample contains 573 unemployment-spell observations, of which 297 end in a transition to employment. For 191 of the previously unemployed, accepted wages and hours are observed after the spell, and for 189 of these there is information on desired hours. 

The employment side contains 4,747 employment-duration observations, 252 transitions into unemployment, 3,771 observations with wage-hours data, and 3,216 observations with subjective desired-hours information. These sample counts are important because the paper exploits both unemployment and employment durations, not only cross-sectional hours data. Table 1 on pages 152–153 is the main descriptive source. 

The mean observed working week is 40.6 hours, mean desired hours are 39.0, and among workers with both observed and desired hours 68.6% report satisfaction, 25.3% report overemployment, and 6.1% want to work more. This asymmetry is central for the empirical interpretation. Table 1 is crucial here. 

# Identification logic

Identification is structural, but stronger than in the earlier static hours-restrictions literature because unemployment-duration data are added and desired-hours data are used explicitly. The arrival rate and layoff rate are identified from unemployment and employment durations; the wage-offer distribution is identified from observed wages; and desired-hours information is used to help distinguish preferences over hours from the hours offer distribution. 

The paper is very explicit that without desired-hours information identification of preferences versus offered hours is weak. Equation (15) and the surrounding discussion show that observed hours alone can be fitted by many combinations of preference parameters and hours-offer probabilities. Desired hours help “pin down” preferences so that offered hours can then be recovered more credibly. 

This is one of the most important methodological results for your agenda. The paper is not merely estimating a richer model; it is explicitly diagnosing the identification problem generated by mixing (R)-type preferences and (A)-type constraints in observed hours. [reasonable inference for my project] supported by 

# Estimation / empirical strategy

The model is estimated by smooth simulated maximum likelihood. The likelihood combines unemployment duration, accepted wage-hours offers after unemployment, job tenure for the employed, and desired-hours information when available. Numerical integration is required over unobserved heterogeneity and latent accepted wages, which is why simulation-based estimation is used. 

Three model variants are estimated. The base model ignores desired hours in estimation. The “optimal desired hours model” treats desired hours as optimal hours up to measurement error. The “hours satisfaction model” exploits the wording of the questionnaire more directly by allowing workers to report satisfaction even when observed and optimal hours differ by a limited amount. This third model is the author’s preferred specification. 

The paper then uses these estimated models for residual analysis, simulation of observed and optimal hours distributions, goodness-of-fit testing for observed hours, and counterfactual policy simulations. Figures 1–3 and Tables 7–11 are the most important outputs for these purposes. 

# Treatment of preferences

Preferences are modeled through a Hausman-type utility function over net income and hours. Household composition variables such as family size and marital status enter utility, which is already an expansion relative to standard empirical job-search models where utility is often effectively reduced to the wage. 

The core contribution, however, is not just to estimate preferences but to show how badly they can be misidentified if desired-hours information is ignored. The base model fits observed hours well but implies a very flat preference structure over hours and predicts underemployment on average. The models that use desired hours imply a clearer concentration of optimal hours in the 32–44 range and a pronounced minimum of the reservation wage schedule around standard full-time hours. 

The hours satisfaction model is especially interesting because it weakens the mechanical identification of desired hours with exact optimality. This allows the paper to separate “satisfaction” from “optimality,” which is both empirically and conceptually important. 

# Treatment of opportunities / constraints

This is the paper’s main strength for your research direction. Opportunities are modeled explicitly as a distribution of job offers. Jobs differ in wages and fixed hours. The unemployed cannot choose any preferred hours directly; they can only accept or reject the wage-hours offers that arrive. 

Thus the paper does not assume a universal choice set and does not collapse labour supply to a wage-conditioned continuous hours choice. It is much closer to an explicit opportunity-set framework, though again in latent probabilistic form. This makes it far more useful for your (A)-side concerns than standard discrete-hours labour-supply papers. [reasonable inference for my project] supported by 

Still, the opportunity object is not a directly observed feasible-set (A_i). It is represented by the joint wage-hours offer distribution and the arrival process. The model is therefore highly relevant for empirical opportunity heterogeneity, but it stops short of a set-theoretic or normative treatment of opportunities. 

# Welfare / normative object

The paper is not an explicit welfare paper. It does not construct equivalent variation, equivalent income, or a social welfare function. It does not address fairness axioms, responsibility, or compensation in any formal sense. 

Its relevance for welfare analysis is indirect but important. By showing that observed hours are shaped by offer restrictions and that desired hours add identifying information about underlying preferences, the paper helps prevent a naive reading of realized labour supply as direct welfare revelation. This is a strong positive precondition for any later well-being analysis. [reasonable inference for my project] supported by 

The paper does not help directly with decomposition of inequality into opportunities and preferences, but it gives one of the clearest empirical frameworks in which such a decomposition could in principle be attempted later. 

# Main findings

The first major finding is that information on desired hours materially changes the inferred preference structure. The base model fits observed hours very well, but it generates very flat optimal-hours distributions and fails to reproduce the survey evidence that most dissatisfied workers are overemployed. By contrast, the models using desired hours place optimal hours mainly in the 32–44 range. Tables 8–9 and the discussion in Section IV.D are central here. 

The second major finding is that the hours satisfaction model performs better than the simpler optimal desired hours model in reproducing the distribution of desired hours. In particular, it explains a large share of the empirical peak in desired hours at 40 hours per week. This is one of the strongest practical arguments for distinguishing “satisfaction” from “exact optimality.” 

The third major finding is that the reservation wage schedule as a function of hours is informative. The base model produces a relatively flat reservation-wage-hours profile, whereas the desired-hours models show a pronounced minimum around 36–40 hours. Figure 2 on page 162 is the key visual evidence. 

The fourth major finding concerns policy. A 5% cut in benefits does not drastically alter accepted hours, but it shifts acceptance slightly toward part-time jobs. Changing the standard working week from about 40 to about 36 hours raises the unemployment hazard and reduces part-time work, because 36-hour jobs become more acceptable to workers who prefer somewhat shorter hours than the existing standard. Tables 10 and 11 on pages 169–171 contain these results. 

A fifth finding is that making the offer distribution more similar to desired hours raises the unemployment hazard, but by less than simply shifting the standard working week downward. The paper interprets this through the value of search: if desirable hours are more likely to arrive, some workers also become more selective about mismatched offers. 

# Main limitations

A first limitation is stationarity. The structural search model is stationary, and the residual analysis shows neglected negative duration dependence. Figure 3 and the discussion in Section IV.C make clear that the models fit shorter durations better than longer ones. 

A second limitation is the goodness-of-fit result for observed hours. The base model passes the formal fit test for observed hours, but the desired-hours models do not. The author interprets this as the consequence of giving up overparameterized flexibility once desired-hours information is used to identify preferences more credibly. This is informative, but still a limitation for full empirical fit. 

A third limitation, relative to your project, is that opportunities remain probabilistic rather than explicit feasible sets. The paper models job offers very well empirically, but it does not deliver a directly observed (A_i) or a normative opportunity object. 

A fourth limitation is scope. The empirical analysis uses Dutch men only, in a particular institutional period, and assumes no general-equilibrium response of firms to policy changes. The policy simulations are therefore partial-equilibrium comparative statics. 

# Relevance for my JMP

## possible use for framing

This paper is highly useful for framing because it states clearly that realized hours are jointly determined by preferences and the structure of job offers. That is one of the core messages your JMP needs.

## possible use for model design

It is very useful for model design. It provides a concrete way to combine job search, hours restrictions, desired-hours data, and a latent offer distribution in one structural framework.

## possible use for identification

This is one of its strongest uses. The paper gives a very clear account of why hours-offer probabilities and preferred hours are hard to disentangle and how subjective desired-hours information can help.

## possible use for welfare measurement

Directly limited, since no well-being measure is defined. Indirectly very useful, because the paper clarifies which parts of the realized bundle are constraint-driven and which parts are preference-driven.

## possible use for decomposition

Moderately useful. It does not perform an (R/A/y) decomposition, but it builds precisely the kind of empirical structure needed before such a decomposition could be attempted.

## possible use for comparative application

Limited directly, since it is a Dutch application, but the framework is portable to any setting with hours mismatch and search frictions.

# Research questions this paper inspires

1. Can Bloemen’s latent wage-hours offer distribution be translated into an explicit feasible-set object (A_i) suitable for an individual well-being measure (W(z,R,A;y))?

2. How much of measured overemployment or underemployment is due to offer restrictions rather than preferences, once desired-hours data are combined with job-search data?

3. Can the hours satisfaction approach be extended to a richer job space with occupation or nonpecuniary job characteristics in addition to wages and hours?

4. How would the policy conclusions change in a nonstationary search model with duration dependence and changing offer distributions?

5. Can desired-hours information be used not only to identify preferences versus offers, but also to decompose welfare inequality into components attributable to (R), (A), and (y)?

# Challenge to this paper

The strongest challenge is that the paper solves an important identification problem while still leaning on a relatively restrictive search structure. Desired-hours data clearly improve the separation of preferred from offered hours, but the model remains stationary, partial-equilibrium, and tied to a particular functional form. For your project, this means it is a very strong empirical building block, but not yet a fully general empirical representation of opportunities. 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper distinguishes sharply between realized hours, desired hours, optimal hours, and offered hours. Realized outcomes arise from a search process over wage-hours job offers, not from unconstrained choice, and desired-hours data are used to recover preferences more credibly. 

[reasonable inference for my project] In your notation, the realized bundle (z) corresponds to the accepted wage-hours-income package. Preferences (R) are represented by the utility function over income and hours, partly identified through desired-hours responses. The feasible set (A) is not observed, but it is represented probabilistically by the arrival process and the joint wage-hours offer distribution. The pay schedule (y) is mainly the wage component of offers together with benefits and nonlabor income. 

[unclear from paper] The paper does not define an individual well-being measure (W(z,R,A;y)), does not distinguish actual from reference opportunity sets, and does not study axioms such as independence of (A), independence of (y), IIJ, IPIJ, or responsibility for opportunities. Those issues are outside its explicit formal scope. 

[reasonable inference for my project] In your taxonomy, the paper is very close to explicit modelling of (A)-type opportunity constraints and very far from an empirical independence-of-(A) stance. It is also not laissez-faire in the evaluative sense, because it is not an evaluative paper at all. Its main contribution for your framework is methodological: it gives one of the clearest empirical strategies for separating preferred hours from offered hours in a search environment. 

# Relation to Bargain et al. (2013)

This paper is complementary rather than central. Bargain et al. (2013) studies welfare comparisons under heterogeneous preferences in the consumption-leisure space. Bloemen (2008) is much weaker on welfare measurement but much stronger on identifying hours constraints and search-driven opportunity restrictions. In that sense, Bargain et al. is the stronger reference on the (R)-side of normative evaluation, while Bloemen is the stronger reference on the positive empirical treatment of (A)-like constraints. [reasonable inference for my project] supported by 

# Relation to opportunities vs preferences

This paper is one of the most useful in your corpus for the opportunities-versus-preferences distinction on the positive side. It shows directly that observed hours cannot be read as preference revelation when workers face a restricted distribution of wage-hours offers. 

It also shows that desired-hours information can materially improve the empirical disentangling of these two sources. That makes it a particularly strong bridge paper for your project: it is not yet a full opportunity-sensitive well-being theory, but it addresses exactly the empirical confusion that such a theory must overcome. 

# Useful quotations / formulas

A central theoretical formula is the reservation utility equation
[
\bar u(q)=u(b+m,0;e)+\frac{\lambda(v)}{r+\delta}\sum_{l=1}^L p_l\int_{y(h_l,\bar u(q);e)}^\infty [u(wh_l+m,h_l;e)-\bar u(q)]f(w),dw,
]
which makes explicit how the gains of search depend on the wage-hours offer distribution. 

A second central object is the hazard out of unemployment
[
\nu(q)=\lambda(v)\sum_{l=1}^L p_l \bar F(y_l(q)),
]
which shows how search duration depends jointly on offer arrival and acceptance thresholds. 

Figure 2 on page 162 is especially important. It shows the reservation wage as a function of hours for the different model variants and visually demonstrates that the base model implies much flatter hours preferences than the models using desired-hours information. 

# Suggested tags

job-search, hours-restrictions, desired-hours, reservation-wage-schedule, structural-unemployment-duration, latent-job-offers, overemployment, underemployment, Netherlands, Bloemen-2008

# My quick takeaway

This is a core paper for the empirical side of your jobs-and-wellbeing agenda. It does not provide a normative (W(z,R,A;y)) theory, but it does something you need before that: it gives a serious structural method for separating preferred hours from offered hours when jobs arrive as constrained wage-hours packages. Its biggest value for your JMP is methodological and conceptual: it shows that hours mismatch is not noise around optimal labor supply but evidence about the opportunity structure itself.
