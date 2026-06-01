---

title: "Estimating and Simulating with a Random Utility Random Opportunity Model of Job Choice Presentation and Application to Belgium"
authors: ["Bart Capéau", "André Decoster", "Gijs Dekkers"]
year: 2016
outlet: "International Journal of Microsimulation"
country_or_context: "Belgium"
population: "Working-age singles and couples available for the labor market in Belgium; self-employed, disabled, retired, students, and mixed households with only one partner available are excluded"
data_period: "EU-SILC 2007"
shelf: "ruro_belgium_job_choice"
tags: ["RURO", "random utility random opportunity", "job choice", "labor supply", "opportunity sets", "Belgium", "EU-SILC", "microsimulation", "education", "wage offer distribution"]
priority: "high"
read_status: "extracted"
------------------------

# Full citation

Capéau, Bart, André Decoster, and Gijs Dekkers. 2016. “Estimating and Simulating with a Random Utility Random Opportunity Model of Job Choice: Presentation and Application to Belgium.” *International Journal of Microsimulation* 9(2): 144–191. 

# One-sentence contribution

The paper presents, estimates, and simulates a Random Utility Random Opportunity (RURO) model of job choice on Belgian data, with the explicit goal of decomposing observed labor market behavior into preference-side and opportunity-side determinants. 

# Why this paper matters

This paper matters because it is one of the clearest operational presentations of the RURO framework in an empirical microsimulation setting. It does not treat hours choice as free optimization over a common budget set; instead, it models job offers as stochastic packages of wages, hours, and non-pecuniary attributes, with individual heterogeneity in the availability of both market and non-market opportunities. 

For your JMP, this is one of the most relevant papers in the entire corpus. It is directly aligned with your agenda on structural labor supply, latent jobs, heterogeneous opportunities, and the distinction between preferences and opportunities. It is also especially useful because it is not only theoretical: it shows how to estimate the model, how to simulate behavior under counterfactuals, and how to interpret fitted preference and opportunity components separately. 

# Core research question

How can one estimate and simulate a labor supply model in which observed job choice reflects both heterogeneous preferences and heterogeneous opportunities, and what do the Belgian data reveal about the roles of education in leisure preferences, job offer intensity, and wage offer distributions? 

# Economic setting and context

The empirical context is Belgium, using EU-SILC 2007 and a detailed tax-benefit mapping through EUROMOD. The authors study labor market participation and labor supply under a static microsimulation framework in which gross wages and hours offers are transformed into disposable income by the Belgian tax-transfer system. 

The paper is motivated by the view that standard discrete-choice labor supply models, such as Van Soest-type models, leave inter-individual differences in available opportunities outside the model. RURO is proposed as a structural alternative in which labor market frictions, hours restrictions, and job availability are part of the behavioral environment rather than being buried in reduced-form dummies or in tastes. 

# Model / theoretical framework

The model class is a static Random Utility Random Opportunity model of job choice. Individuals choose the best element from a set of opportunities that contains both market opportunities (jobs) and non-market alternatives. The innovation relative to standard random utility labor supply models is that the opportunity set itself is stochastic and individually heterogeneous. 

The key choice object is a job offer, indexed by (j), which is a package containing hours (h), wage (w), and other non-pecuniary job attributes. Non-participation is represented by non-market alternatives indexed separately, with (h=0) and (w=0). The utility of alternative (z) is
[
U(C(z),H(z),z;x_V)=V(C(z),T-H(z);x_V)\cdot \varepsilon(z),
]
where (V) is the systematic utility component over disposable income and leisure, and (\varepsilon(z)) captures the utility effect of unobserved job or activity attributes. 

The feasible set is not a universal common menu. Job offers arrive according to an inhomogeneous spatial Poisson process, with densities over hours offers, wage offers, and non-pecuniary utility draws. Non-market opportunities are modeled analogously through an intensity function over non-market utility draws. The framework is positive rather than explicitly normative, though it is intended for policy microsimulation. 

# Key objects

The central economic objects are the systematic utility function (V(c,T-h;x_V)), the induced utility in wage-hours space (\Psi(w,h;x_V,x_f)), the random multiplicative utility shifter (\varepsilon(z)), the relative job-offer intensity (q), the wage offer density (g_1(w)), and the offered labor-time density (g_2(h)). These are the core structural objects generating observed choices. 

The most important opportunity objects are the job arrival intensity and the two offer distributions. The paper interprets (q) as the relative intensity of market opportunities versus non-market opportunities for a given individual. The wage offer distribution is assumed lognormal, while the hours-offer distribution is piecewise uniform with peaks around part-time, three-quarter-time, and full-time jobs. The diagram on page 17 illustrates this peak structure explicitly. 

The main empirical outcome objects are participation rates, hours worked, wage distributions of accepted jobs, estimated preference intensity for leisure relative to consumption, and simulated counterfactual labor market responses to educational shifts. 

# Data

The paper uses the Belgian EU-SILC 2007 data. After sample selection, the estimation is conducted on 1,457 couple households, 571 single females, and 449 single males. Only households whose relevant adults are available for the labor market are kept; self-employed and several other groups are excluded because hours and earnings are not suitable for the model or labor supply is not flexibly modeled. 

Gross-to-net income for observed and simulated alternatives is computed using EUROMOD. The paper supplements the survey with external age-sex-education-specific unemployment rates from Eurostat, which are used as proxies for opportunity-side conditions in the job-offer intensity equation. Table 2 on page 22 reports these unemployment rates by age, sex, and education. 

The descriptive statistics show substantial education and participation heterogeneity. In the selected sample, female participation is much lower than male participation, especially for singles, and low education is associated with much higher unemployment. These empirical patterns are one of the main motivations for separately examining preferences, job-offer intensity, and wage-offer distributions. 

# Identification logic

Identification relies on the RURO choice probability structure and on additional assumptions about the distributions of opportunities. A key identification condition is the assumed independence of the wage offer distribution from hours offers, (g_1(w\mid h)=g_1(w)). This allows the authors to identify the wage offer density separately from the hours distribution and the systematic utility term. 

The paper argues that (g_1(w)) can be identified from relative frequencies of observationally equivalent individuals choosing different wages conditional on hours, while the relative intensity parameter (q) can be identified by comparing workers and non-workers once utility is normalized appropriately. To help identify (q), the empirical application also adds an exclusion variable: a group-specific unemployment rate that is assumed to affect opportunities but not preferences directly. 

The crucial limitation is equally explicit: the utility function (\Psi(w,h)) and the offered-hours distribution (g_2(h)) are not separately nonparametrically identified. The paper therefore imposes functional-form assumptions, especially Box–Cox-type utility and a peaked piecewise-uniform hours-offer distribution. The authors are transparent that this part of the model is not fully nonparametrically pinned down. 

# Estimation / empirical strategy

The empirical strategy is full structural estimation of the RURO likelihood. Choice probabilities are derived from the joint stochastic structure of utilities and opportunities, yielding closed-form probabilities for jobs and non-market choices once the Fréchet/Poisson structure is imposed. For couples, the paper extends the model under a unitary decision framework. 

Because the full opportunity set is not observed, the paper samples a choice set of wage-hours alternatives from a prior distribution and then corrects the likelihood using the sampling density. Disposable income for each sampled alternative is computed using EUROMOD. This is a practical simulated-choice-set implementation of the model. 

After estimation, the paper uses simulation in two ways: first, to assess in-sample fit by comparing simulated and observed income, wage, and hours distributions; second, to evaluate counterfactuals, most notably a change in male educational attainment intended to reduce the educational gap relative to females. 

# Treatment of preferences

Preferences are modeled through Box–Cox-type utility functions over consumption and leisure. For couples, the unitary model also includes an interaction term between spouses’ leisure, allowing leisure complementarities or substitutabilities. Covariates such as age, children, education, and region shift the preference intensity for leisure relative to consumption. 

The paper explicitly studies how education affects the steepness of indifference curves. Figure 2 on pages 23–24 shows that higher education is associated with less intense preferences for leisure relative to consumption for women, while for men the effect is non-monotonic: both low- and high-educated men display less intense leisure preference than middle-educated men. 

This is a substantive preference result, but the authors do not treat preferences as the sole driver of labor market outcomes. The whole architecture of the paper is built to prevent precisely that conflation. 

# Treatment of opportunities / constraints

This is the core contribution of the paper.

The paper models opportunities explicitly and centrally. Jobs are not freely chosen points on a budget frontier; they are stochastic offers with specific wages, hours, and non-pecuniary attributes. Individuals differ in the intensity with which suitable job offers arrive, in the wage distribution of those offers, and in the hours regimes those offers embody. Non-market opportunities are also heterogeneous across individuals. 

This is a first-class opportunity-set model. The opportunity side is not reduced to fixed costs, rationing dummies, or a universal hours grid. Instead, the model decomposes observed labor market behavior into at least three channels: the relative intensity of leisure preferences, the intensity of suitable job offers (q), and the wage offer distribution (g_1(w)). This is stated explicitly in the discussion of the Belgian application and again in the simulation analysis. 

The limitation is not absence of opportunity modeling, but incomplete identification and partial equilibrium. The hours-offer distribution is imposed through a parametric peak structure, and the model is not a full matching or equilibrium labor market model. Frictions are taken as given rather than endogenized. Still, relative to your agenda, this is exactly the kind of paper that takes opportunities seriously as structural objects. 

# Welfare / normative object

There is no explicit welfare metric such as equivalent income, compensating variation, or a social welfare function. The paper is not a normative welfare-comparison paper. It is a positive structural model designed for simulation and policy analysis. 

Its normative relevance is indirect. The authors argue that RURO can be useful for evaluating tax-benefit reforms and for distinguishing whether policy effects run through preferences or through opportunities. But the evaluative object remains behavior and simulated labor supply, not a formal measure of well-being or social justice. 

# Main findings

First, the estimated model yields meaningful and distinct decompositions of labor market behavior into preferences and opportunities. Education affects all three main components: preferences for leisure, the intensity of suitable job offers, and the wage offer distribution. This is the paper’s central substantive message. 

Second, higher education shifts the wage offer distribution to the right. Figure 3 on page 24 shows that both higher education and more potential experience move the estimated wage offer density toward higher wages, though potential experience and education partly offset each other because higher education lowers potential experience at a given age. 

Third, the offered-hours distribution is sharply non-uniform and differs by gender. Figure 4 on page 26 shows that females receive relatively more part-time and fewer full-time job offers than males. This is a direct estimated opportunity-side result, not a preference inference. 

Fourth, the intensity of suitable job offers (q) generally rises with education, though the net effect differs by sex once age-education-specific unemployment rates are included. Figure 5 on page 27 shows a clearly stronger positive education effect for women than for men, while suitable job availability for men declines somewhat with age. 

Fifth, the model fits many distributions reasonably well, but not perfectly. Pages 28–31 show that simulated disposable income, wages, and hours distributions match the observed data fairly well overall, though there are systematic discrepancies such as overestimated non-participation in couples and some misfit around three-quarter-time and full-time peaks. 

Sixth, the reported aggregate wage elasticities are relatively large by micro-model standards. Table 4 on page 31 reports, for example, a total elasticity of 0.6445 for women in couples when the female wage offer distribution is shifted rightward by 10%, and 0.6877 for single females under the same experiment. The authors note that these are conceptually different from standard Marshallian wage elasticities because the experiment shifts the entire wage offer distribution of jobs rather than an exogenous individual wage. 

Seventh, the education counterfactual has only moderate aggregate effects, and these effects operate mainly through opportunities rather than preferences. Tables 6 and 7 on pages 34–35 show that bringing male educational attainment closer to female levels modestly raises male participation and hours, especially for single men, while effects on women are very small. The decomposition in Table 7 indicates that the larger part of the change comes through opportunities rather than preferences. 

# Main limitations

A first limitation is partial identification. The paper is explicit that the systematic utility function and the offered-hours distribution are not separately nonparametrically identified, so some of the opportunity-preference decomposition depends on functional-form assumptions. 

A second limitation is that the model is static. It does not model search dynamics, waiting, learning, or intertemporal labor supply responses. Opportunities are stochastic, but the model is not dynamic. 

A third limitation is that the framework is not a full equilibrium model. It is not a matching model and does not determine labor market frictions endogenously. The paper itself states this clearly in the conclusion. 

A fourth limitation, relative to your interests, is that the paper remains positive rather than welfare-theoretic. It gives you an excellent opportunity-sensitive behavioral model, but not yet an opportunity-sensitive welfare metric. 

A fifth limitation is data-related. Self-employed and some complex households are excluded, and the model relies on survey rather than matched employer-worker data. This matters for generality and perhaps for richer identification of offer processes. 

# Relevance for my JMP

## possible use for framing

This paper is a central framing reference if your JMP argues that labor supply should be modeled as job choice under heterogeneous opportunities rather than as hours choice under a common feasible set. It gives a clean conceptual statement of why wages, hours, and non-pecuniary job attributes should be part of the opportunity side. 

## possible use for model design

It is directly useful for model design. It offers a tractable RURO architecture with explicit objects for preferences, offer intensity, wage offer density, and hours-offer density, together with a practical estimation/simulation strategy using sampled choice sets and tax-benefit microsimulation. 

## possible use for identification

This paper is important for identification because it states very clearly what is and is not identified. In particular, it warns that utility and hours-offer densities are hard to separate without structure. This is highly relevant if you want to estimate opportunities and preferences jointly. 

## possible use for welfare measurement

Indirectly very useful. The paper does not provide a welfare metric, but it gives the positive decomposition your welfare project needs: differences in outcomes can be decomposed into preferences, offer intensity, and wage distributions. A later welfare layer could build on exactly that decomposition. 

## possible use for cross-country comparison

Potentially very useful. The Belgian application shows how one could estimate country-specific preference and opportunity components and then compare across institutional settings. This is directly relevant to your cross-country welfare and labor supply agenda. 

# Research questions this paper inspires

How much of the cross-country variation in labor supply elasticities is due to differences in job-offer intensity and wage-offer distributions rather than differences in preferences?

Can the RURO decomposition into preferences, offer intensity, and wage-offer distribution be linked to an explicit opportunity-sensitive welfare metric?

Would the conclusion that education affects labor market behavior mainly through opportunities survive in richer data with observed occupations, tasks, and job quality?

Can one integrate this RURO framework with a labor-demand or matching model so that the opportunity process is not taken as exogenous? 

# Challenge to this paper

The strongest unresolved issue is that the paper takes the decisive conceptual step of treating opportunities as structural objects, but it still relies on strong parametric structure and a static reduced-form opportunity process. A future paper could challenge this by preserving the RURO insight while making the offer process richer, more directly observed, and perhaps partially equilibrium-based. 

# Relation to Bargain et al. (2013)

The relation is strong on the structural-labor-supply side but different on the normative side. Bargain et al. (2013) uses structural labor supply estimation for welfare comparison under heterogeneous preferences, whereas this RURO paper emphasizes the decomposition of behavior into preferences and opportunities. Relative to Bargain et al. (2013), Capéau et al. is much stronger on explicit opportunity modeling and much weaker on welfare evaluation. For your purposes, the two are complementary: Bargain et al. helps on the welfare side, while this paper helps on the opportunity-sensitive behavioral side. 

# Relation to opportunities vs preferences

This paper is one of the clearest papers in your corpus for separating preferences from opportunities. That is its stated purpose. The model is explicitly designed to “understand individual heterogeneity in choice behaviour as a combined effect of differences in preferences and opportunities,” and the Belgian application operationalizes that idea through separate estimates of leisure-preference intensity, job-offer intensity, and wage-offer distributions. It does not fully solve the welfare-comparison problem, but on the positive behavioral side it is almost exactly the kind of separation your agenda requires. 

# Useful quotations / formulas

The core RURO utility specification is
[
U(C(z),H(z),z;x_V)=V(C(z),T-H(z);x_V)\cdot \varepsilon(z),
]
which is the paper’s defining behavioral equation. It combines a systematic consumption-leisure component with a multiplicative random component summarizing non-pecuniary attributes of jobs and activities. 

The single-agent job-choice probability is
[
\phi(w,h)=
\frac{\Psi(w,h),q,g_1(w),g_2(h)}
{\Psi(0,0)+\int_{r\in W}\int_{t\in H}\Psi(r,t),q,g_1(r),g_2(t),dt,dr},
]
with the non-market alternative probability given analogously by replacing the numerator with (\Psi(0,0)). This is the core expression that makes behavior jointly depend on preferences and opportunities. 

The diagram on page 17 is also important. It shows the piecewise-uniform peak distribution of offered labor-time regimes, with mass concentrated around part-time, three-quarter-time, and full-time jobs. This visual makes clear that the model is not treating the hours dimension as smooth or unrestricted. 

# Suggested tags

#RURO #job_choice #opportunity_sets #labor_supply #wage_offer_distribution #hours_restrictions #Belgium #microsimulation #preferences_vs_opportunities #latent_jobs

# My quick takeaway

If I only remember one thing from this paper for my JMP, what should it be? That a serious structural labor supply model can treat observed labor market outcomes as the joint result of preferences and heterogeneous job opportunities—and in this Belgian application, education matters more through opportunities than through preferences.
