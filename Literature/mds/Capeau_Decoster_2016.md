---

title: "Getting tired of work, or re-tiring in absence of decent job opportunities? Some insights from an estimated Random Utility/Random Opportunity model on Belgian data"
authors: ["Bart Capéau", "André Decoster"]
year: 2016
outlet: "EUROMOD Working Paper No. EM4/16"
country_or_context: "Belgium"
population: "Single males, single females, and heterosexual couples aged 16–64 available for the labour market; employees and job-available nonworkers; excluding self-employed, early retired, disabled, students, and mixed couples with only one partner available"
data_period: "EU-SILC Belgium 2007"
shelf: "RURO_latent_jobs_opportunities_preferences"
tags: ["RURO", "random utility random opportunity", "latent jobs", "labour supply", "job offers", "opportunities", "preferences", "ageing", "Belgium", "EUROMOD"]
priority: "high"
read_status: "extracted"
------------------------

# Full citation

Capéau, Bart, and André Decoster. 2016. “Getting tired of work, or re-tiring in absence of decent job opportunities? Some insights from an estimated Random Utility/Random Opportunity model on Belgian data.” *EUROMOD Working Paper* EM4/16. 

# One-sentence contribution

The paper estimates a Random Utility/Random Opportunity (RURO) model on Belgian EU-SILC 2007 data to separate age differences in labour-market behaviour into preference effects and opportunity effects, and concludes that declining opportunities with age are at least as important as changing preferences in explaining lower elderly participation, with opportunities working mainly through the extensive margin.

# Why this paper matters

This paper matters because it addresses exactly the distinction that many structural labour-supply models leave blurred: whether lower labour supply is driven by tastes or by the set of jobs actually available to the individual. Its central contribution is to estimate a model in which wages and hours are job attributes and job availability is itself heterogeneous across people, instead of treating individuals as choosing hours freely at an exogenously fixed wage.

For your project, the paper is especially important because it is one of the clearest applied attempts to operationalize the separation between preferences and opportunities. It is therefore directly relevant for RURO, latent jobs, feasible job sets, and for any future attempt to construct a welfare object that should not confound tastes with job availability. Its value is strongest for model design and for the conceptual treatment of opportunities; it is weaker for explicit normative theory.

# Core research question

To what extent is the lower labour-market participation of older individuals due to changing preferences for leisure or non-work, and to what extent is it due to a decline in decent job opportunities available to them?

# Economic setting and context

The paper studies Belgian labour-market behaviour using a cross-section from EU-SILC 2007. The authors deliberately do not model the retirement decision as such. Instead, they exclude early leavers and other individuals not available for the labour market, and focus on the participation and hours choices of those still available for work. This is a narrower but cleaner question than the standard retirement literature based on pension wealth and dynamic retirement choice.

The empirical motivation is visible already in the descriptive comparison between ages 30–49 and 50–64. Participation drops materially in every subgroup: from 96% to 84% for males in couples, from 85% to 54% for females in couples, from 85% to 62% for single males, and from 73% to 58% for single females; mean weekly labour time also falls sharply. This descriptive gap is the phenomenon the RURO model is designed to explain.

# Model / theoretical framework

The model class is a structural discrete job-choice model of the Random Utility/Random Opportunity type. Individuals choose among job offers and non-market alternatives. A job is not just a point on a budget line. It is a package containing a wage (w), labour time (h), and other non-pecuniary attributes (s). The model therefore extends classical discrete labour-supply models from “hours choice at a given wage” to “choice among jobs and non-market options.” 

Preferences are modeled through a systematic utility component over disposable income and leisure, multiplied by a random term capturing the valuation of non-pecuniary job or leisure attributes:
[
U(C(z),H(z),s(z);x^V)=V(C(z),T-H(z);x^V)\cdot \varepsilon(s(z)).
]
Using the gross-to-net map (c=f(w,h;x^f)), this induces a utility representation in the wage-hours space:
[
\Psi(w,h;x^V,x^f)=V(f(w,h;x^f),T-h;x^V).
]
This is central because the model is structurally built around job packages rather than around a conventional continuous labour-supply schedule. 

Opportunities are modeled explicitly through a stochastic job-arrival process. Jobs arrive according to an inhomogeneous spatial Poisson process. The opportunity side has three main components: a wage-offer density (g_1(w)), a labour-time-offer density (g_2(h)), and a job-offer intensity term linked to personal characteristics. Non-market alternatives are also given an availability structure. The relative intensity of market to non-market opportunities is summarized by
[
q(x^q)=\frac{\pi_1(x^q)}{\pi_0(x^q)}.
]
This is a genuine opportunity-side object, not a preference parameter. 

The framework is positive, not normative. It is designed to explain observed behaviour and to simulate counterfactual labour-market outcomes under different opportunity and preference profiles. It does not propose a welfare ordering over persons or a fairness criterion.

# Key objects

The main economic objects are the systematic utility function (V(c,T-h;x^V)), the induced wage-hours utility (\Psi(w,h;x^V,x^f)), the random multiplicative taste term (\varepsilon(s)), the wage-offer density (g_1(w;x^{g1})), the hours-offer density (g_2(h;x^{g2})), and the relative job-offer intensity (q(x^q)). These jointly determine the likelihood of choosing a particular job or the non-market alternative. 

The central choice density for singles is
[
\phi(w,h)=\frac{q(x^q)\Psi(w,h)g_1(w)g_2(h)}{\Psi(0,0)+q(x^q)\int_W\int_H \Psi(s,t)g_1(s)g_2(t),dt,ds},
]
with the corresponding non-market choice probability
[
\phi(0,0)=\frac{\Psi(0,0)}{\Psi(0,0)+q(x^q)\int_W\int_H \Psi(s,t)g_1(s)g_2(t),dt,ds}.
]
These expressions make the decomposition between attractiveness and availability completely explicit. 

A further key object is the counterfactual decomposition used in Section 7: one counterfactual equalizes age-related opportunities, the other equalizes age-related preferences. That decomposition is the main empirical device used to compare the role of (R)-type and (A)-type heterogeneity.

# Data

The estimation uses Belgian EU-SILC 2007. Net incomes for the choice sets are computed with EUROMOD version F5.5. The estimation sample contains 1,457 couples, 571 single females, and 449 single males. The data preparation excludes the self-employed, early retirees, disabled persons, students, and households with labour-supply complications outside the model’s scope, such as couples where only one partner is labour-market available or households with working children still living with parents. 

Observed covariates used across model components include age, education, region, children, sex, potential experience, and a type-specific unemployment rate constructed externally by age-sex-education group. Table 1 reports descriptive statistics for the estimation sample, and Table 2 reports the group-specific unemployment rates used as opportunity-side information. 

# Identification logic

Identification is partly structural and partly parametric. The paper is unusually explicit that some components are non-parametrically identified while others are not. The main identification idea is that observed differences across wages, hours, participation, and covariates can separately discipline the wage-offer distribution, the relative intensity of job offers, and preferences. The relative intensity (q(x^q)) is identified from the comparison between workers and nonworkers once the rest of the choice density is specified. 

A crucial identification restriction is that the wage-offer distribution is independent of hours conditional on covariates, (g_1(w\mid h;x^{g1})=g_1(w;x^{g1})). The authors also state clearly that the utility function (\Psi(w,h)) and the hours-offer density (g_2(h)) are not separately non-parametrically identified. They therefore rely on functional-form assumptions, especially Box-Cox preferences and a piecewise-uniform peak structure for offered hours. This is a real identifying limitation, not a minor technical detail. 

The paper adds an exclusion-style variable on the opportunity side: type-specific unemployment by age-sex-education group enters the (q)-function and is intended to proxy job availability rather than preferences. This helps the empirical separation between preference and opportunity factors, although the paper itself notes the need for better exogenous variation in job availability in future work.

# Estimation / empirical strategy

Estimation is by maximum likelihood using sampled latent choice sets. Because the full opportunity set is unobserved and potentially very large, the authors sample alternatives in wage-hours space from a prior distribution and then correct the likelihood accordingly. The paper explains this in detail through importance sampling with replacement and through the simulated likelihood construction. 

Parametrically, wages are assumed lognormally distributed, labour-time offers follow a piecewise-uniform distribution with peaks around standard part-time and full-time regimes, and the relative opportunity intensity is log-linear in covariates. Preferences are of Box-Cox type, with separate specifications for singles and couples and an interaction term for spouses’ leisure in the couples model. These assumptions are not ancillary; they are integral to estimation and interpretation. 

The empirical strategy then proceeds in two stages conceptually. First, estimate the RURO structure. Second, simulate behavioural outcomes and counterfactuals, including age-equalized opportunities and age-equalized preferences. The fit of the model is evaluated by comparing observed and simulated distributions of disposable income, wages, and labour time regimes.

# Treatment of preferences

Preferences are modeled explicitly and flexibly, though still parametrically. The systematic part of utility depends on disposable income and leisure, with preference shifters such as age, education, region, and children. Non-pecuniary job and leisure characteristics that are not observed by the econometrician enter through multiplicative random utility terms. This gives the model richer preference heterogeneity than standard discrete hours models, but not fully arbitrary heterogeneity. 

The age effect on preferences is one of the paper’s main findings, but it is not monotone across all groups. For females in couples and single males, the intensity of preference for leisure increases with age over the relevant sample range. For single females and males in couples, the age profile is non-monotonic, with minimum leisure-intensity around ages 37 and 36 respectively. This matters because the paper’s headline is not simply “older people prefer leisure more”; the preference channel is heterogeneous and sometimes nonlinear. 

# Treatment of opportunities / constraints

This is the paper’s most important section for your purposes. The paper models opportunities explicitly. It does not assume a universal choice set with only wages and taxes differing across persons. Instead, opportunities are latent, stochastic, and person-specific. The key objects are job-offer intensity, the wage-offer density, the labour-time-offer density, and the relative availability of market versus non-market alternatives. This is a direct attempt to formalize feasible opportunities rather than to leave them implicit. 

The paper also models hours restrictions explicitly through the offer distribution (g_2(h)). This is a major departure from traditional discrete-choice labour-supply models in which hours categories are simply imposed as the choice grid. Here, hours restrictions come from the job arrival process itself. The paper is explicit that this is one of the reasons RURO is especially apt for the research question.

Demand-side constraints are therefore not ignored, but neither are they fully structural in general-equilibrium or search-theoretic form. They are captured reduced-form through the stochastic job-offer process and the opportunity-intensity function (q(x^q)). This is much stronger than assuming a common opportunity set, but weaker than modeling firms, vacancies, search, and matching explicitly.

The paper helps distinguish both preference heterogeneity and opportunity heterogeneity. That is precisely its point. Among the papers relevant to your project, this is one of the clearest empirical examples where the distinction is not only discussed conceptually but also implemented quantitatively.

# Welfare / normative object

The paper is primarily positive, not explicitly normative. It does not define a welfare criterion for comparing allocations across persons, nor does it derive optimal taxes or compensation principles from the estimated model. Its counterfactuals are behavioural and descriptive in purpose: they isolate how age differences in participation and hours would change if opportunities or preferences were equalized.

Still, the paper is clearly useful for welfare work in an indirect sense. In the conclusion, the authors explicitly say that structural models like RURO are “obvious candidates as suppliers of essential information for normative analyses” and that they plan to construct welfare measures building on this type of framework. That is an explicit bridge toward welfare analysis, though not yet a welfare contribution in this paper itself. 

For your specific interests, the paper is useful for thinking about compensation for opportunity deficits, because it isolates opportunity-side shortfalls from taste-side differences. But it does not itself say whether opportunity deficits should be compensated, or how. Likewise, it helps with decomposition of behaviour into preferences and opportunities, but not with a formal decomposition of inequality or well-being.

# Main findings

The paper’s core finding is that age-related declines in opportunities are at least as important as age-related changes in preferences in explaining lower labour-market participation among older workers. This conclusion appears already in the abstract and is restated in the conclusion.

Empirically, the estimated job-offer intensity has an inverted-U relationship with age, peaking around age 30 and then declining sharply. After age 50, the availability of suitable jobs is substantially lower than for younger groups, with the decline somewhat stronger for women. Region also matters: opportunity intensity is lower in Wallonia and especially Brussels than in Flanders. These are central opportunity-side results, shown in Figure 6 and summarized in the conclusion. 

On the preference side, the age profile is more mixed. The paper finds monotonic age-related steepening of leisure preference for females in couples and single males, but non-monotonic profiles for single females and males in couples, with minimum leisure-intensity around ages 37 and 36 respectively. Thus the preference channel is present, but it is not uniformly increasing with age across all groups. 

The counterfactuals in Table 9 are especially important. Equalizing age-related opportunities raises overall participation from 82.0% in the baseline to 88.9%, whereas equalizing age-related preferences raises it only to 84.6%. By contrast, the preference counterfactual has a stronger effect on conditional hours: average hours conditional on participation rise from 36.4 to 38.3, whereas the opportunity counterfactual has almost no positive effect on conditional hours and even a slight overall decline. The paper interprets this as evidence that opportunities matter mainly on the extensive margin, while preferences matter more on the intensive margin.

# Main limitations

The first limitation is identification. The paper is transparent that the utility function and the hours-offer distribution are not separately non-parametrically identified, so the interpretation of estimated hours restrictions partly rests on functional form. For your purposes, this means the opportunity object is modeled, but not fully pinned down independently of preference assumptions. 

A second limitation is that the paper is static. It explicitly excludes retirement dynamics, early exit, disability transitions, schooling, and forward-looking behaviour. This is defensible for the stated question, but it means the model cannot capture life-cycle incentives or dynamic job-search effects, both of which matter for older workers. 

A third limitation is the fixed-stock-of-capacities normalization. Under the model’s interpretation, raising market opportunity intensity can reduce the availability of non-market alternatives. The paper itself shows that improving job opportunities is therefore not guaranteed to be Pareto-improving, because some individuals may lose valued non-market options. This is conceptually interesting but normatively awkward, and it matters for how one maps the model into opportunity-based welfare analysis. 

A fourth limitation is that job demand is modeled reduced-form through offer intensities and not through a richer equilibrium, search, or matching structure. The paper therefore distinguishes opportunities from preferences better than standard labour-supply models, but still does not provide a complete model of opportunity formation.

# Relevance for my JMP

## possible use for framing

This paper is highly useful for framing a project around the central question “are observed labour-market outcomes driven by tastes or by the feasible set of jobs?” It gives you a direct empirical template for making that distinction operational rather than merely rhetorical.

## possible use for model design

This is one of the paper’s strongest uses. It provides a concrete design for treating jobs as packages ((w,h,s)), for letting opportunity sets be latent and stochastic, and for allowing both wage offers and hours offers to vary across persons. If your model design aims to move beyond fixed wages and freely chosen hours, this paper is directly relevant. 

## possible use for identification

The paper is also useful here because it is explicit about what does and does not identify. The use of type-specific unemployment on the opportunity side, together with structural restrictions such as wage-offer independence from hours, gives you a practical identification roadmap, while also showing where functional form is doing heavy lifting.

## possible use for welfare measurement

Directly, limited, because this paper does not construct welfare measures. Indirectly, substantial, because it isolates the preference and opportunity objects that a later welfare measure would want to treat differently. The explicit statement in the conclusion that the framework should feed into welfare analysis is particularly relevant. 

## possible use for decomposition

Highly relevant. The age counterfactuals are effectively a decomposition of behavioural age gradients into preference and opportunity components. It is not an inequality decomposition, but it is a decomposition logic you could adapt.

## possible use for comparative application

Potentially high. The authors themselves suggest that better identification of opportunity intensity could come from cross-country or over-time variation. That is directly relevant if your project later extends beyond one country or one institutional environment. 

# Research questions this paper inspires

How would the estimated contribution of opportunities versus preferences change if the opportunity process were defined over occupation-specific job cells rather than only over wage-hours packages?

Can one construct a welfare measure (W(z,R,A;y)) that treats the RURO-estimated opportunity component as morally distinct from the preference component, and what axioms would such a measure satisfy?

How sensitive is the estimated opportunity effect to the fixed-capacities normalization (\pi_0(x^q)+\pi_1(x^q)=1), and what changes if market opportunities expand without shrinking non-market opportunities?

Can exogenous regional, temporal, or policy variation in vacancies improve the identification of (q(x^q)) and separate labour-demand opportunity shocks from age-related preference shifts?

How should one classify hours restrictions generated by (g_2(h)): as opportunity constraints, institutional rationing, or partly as reduced-form reflections of preferences?

# Challenge to this paper

The paper’s main conceptual vulnerability is that it obtains its preference-opportunity decomposition within a normalization where increasing job opportunities partly crowds out non-market opportunities. That is internally coherent, but it makes the opportunity object less clean than it first appears, because some “opportunity improvement” is mechanically tied to a loss elsewhere. For a project interested in compensation for job opportunities, that normalization deserves scrutiny before the model is used normatively.

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper distinguishes preference factors from opportunity factors inside an estimated RURO model. Opportunities are modeled through the latent arrival intensity of job offers, wage-offer densities, and hours-offer densities, while preferences are modeled through a systematic utility function plus random valuation of non-pecuniary attributes. 

[reasonable inference for my project] In your notation, the paper comes unusually close to separating (R) and (A). The realized bundle (z) corresponds to the chosen job or non-market alternative and its associated disposable income and labour time. The preference object (R) is approximated by the estimated systematic utility and random taste component. The feasible-set object (A) is not observed directly, but the latent opportunity process is clearly intended as an empirical proxy for the availability structure behind (A).

[unclear from paper] The paper does not define a well-being measure (W(z,R,A;y)), nor does it specify how the latent opportunity process should be mapped into a set-valued object (A) for normative analysis. It is also unclear how much of the estimated opportunity process should be interpreted as employer-side constraints, institutional hours restrictions, or other non-preference frictions.

[reasonable inference for my project] In your taxonomy, this paper is closest to decomposition of preferences versus opportunities and to the rejection of independence from opportunities. It is not naturally a paper about independence of (A) or independence of (y), and it is not a laissez-faire or reference-opportunity-set paper. It is best read as a positive empirical foundation for a later opportunity-sensitive welfare framework.

# Relation to Bargain et al. (2013)

[reasonable inference for my project] This paper is closely related to the broad structural labour-supply tradition to which Bargain-type work belongs, but it departs from the usual setup in one decisive respect: wages and hours are treated as attributes of latent job offers rather than as exogenous wages combined with chosen hours. That makes it especially relevant if one sees standard structural labour-supply models as potentially confounding preferences with opportunities. The relation is therefore complementary: Bargain-type models are strong on tax-benefit structural evaluation, while Capéau–Decoster are stronger on explicit opportunity heterogeneity. 

# Relation to opportunities vs preferences

This paper is directly about opportunities versus preferences. Indeed, that distinction is not just part of the motivation; it is the organizing principle of the empirical exercise. The central counterfactual comparison explicitly asks what would happen if age differences in opportunities were removed versus if age differences in preferences were removed.

For your project, that makes this paper especially valuable. Many labour-supply papers speak loosely about preferences and constraints, but this one builds the distinction into the model and shows empirically that the opportunity component can be quantitatively large. It is therefore one of the most directly relevant papers in your corpus for the opportunities-versus-preferences agenda. 

# Useful quotations / formulas

A central utility formula is
[
U(C(z),H(z),s(z);x^V)=V(C(z),T-H(z);x^V)\cdot \varepsilon(s(z)).
]
This is the core decomposition of systematic utility and random valuation of non-pecuniary attributes. 

The relative opportunity intensity is
[
q(x^q)=\frac{\pi_1(x^q)}{\pi_0(x^q)}.
]
This is one of the paper’s most important objects because it captures the balance between market and non-market opportunities. 

The single-person job-choice density is
[
\phi(w,h)=\frac{q(x^q)\Psi(w,h)g_1(w)g_2(h)}{\Psi(0,0)+q(x^q)\int_W\int_H \Psi(s,t)g_1(s)g_2(t),dt,ds}.
]
This formula is especially useful because it shows that choice probabilities are proportional to attractiveness weighted by availability. 

# Suggested tags

RURO, latent-job-opportunities, preferences-vs-opportunities, ageing, Belgium, EU-SILC, EUROMOD, structural-labour-supply, hours-restrictions, job-arrival-process

# My quick takeaway

This is one of the most relevant papers in your corpus for the preferences-versus-opportunities question. Its core contribution is not simply that opportunities matter, but that it builds a structural empirical framework in which opportunities and preferences are distinct objects and then shows that, for ageing and participation in Belgium, the opportunity channel is at least as important as the preference channel. For your project, it is especially valuable as a model-design and decomposition paper; its main limitation is that the move from latent opportunities to a normatively usable feasible-set object remains incomplete.
