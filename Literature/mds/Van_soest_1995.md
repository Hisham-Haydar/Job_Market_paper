---

title: "Structural Models of Family Labor Supply: A Discrete Choice Approach"
authors: ["Arthur van Soest"]
year: 1995
outlet: "The Journal of Human Resources"
country_or_context: "Netherlands"
population: "Two-adult households in the Netherlands; estimation sample of 2,859 families from 1987 cross-section data"
data_period: "1987"
shelf: "structural_family_labour_supply_discrete_choice"
tags: ["structural labour supply", "discrete choice", "family labour supply", "hours restrictions", "Dutch tax-benefit system", "random preferences", "wage prediction errors", "policy simulation"]
priority: "very high"
read_status: "extracted"
------------------------

# Full citation

van Soest, Arthur. 1995. “Structural Models of Family Labor Supply: A Discrete Choice Approach.” *The Journal of Human Resources* 30(1): 63–88. 

# One-sentence contribution

The paper develops a static structural discrete-choice model of joint labour supply of spouses, explicitly incorporating the Dutch tax-benefit system, hours restrictions, random preferences, and unobserved wages of nonworkers, and shows that allowing for hours restrictions substantially lowers estimated labour-supply elasticities. 

# Why this paper matters

This paper matters because it is one of the foundational papers replacing the continuous-hours family labour-supply model with a discrete-choice framework that can handle nonlinear taxes, joint filing, fixed costs, unemployment assistance, and other nonconvex budget-set features without losing tractability. For your literature map, it is a key methodological reference on structural labour-supply estimation. 

It also matters because it is one of the early papers that explicitly tries to deal with two empirical frictions often central in later labour-supply work: unobserved wages of nonworkers and hours restrictions. It therefore sits at an important junction between standard neoclassical labour supply and more constrained-choice approaches, even if it does not yet model opportunities as explicit job sets. 

# Core research question

How can one estimate a fully structural model of the labour supply of husbands and wives when tax-benefit rules are nonlinear, wages are unobserved for nonworkers, and the observed concentration of hours suggests that workers face restrictions on available hours choices? 

# Economic setting and context

The paper is set in the Netherlands and is motivated by the Dutch policy debate on raising labour-force participation, especially among married women, during the late 1980s and early 1990s. Section II emphasizes low female participation relative to other EC countries, the policy concern with increasing female employment, and the relevance of the Dutch tax-benefit system for spousal work incentives. Table 1 on page 65 summarizes the participation comparison. 

The policy discussion is concrete. The paper focuses especially on the Dutch transferability of the tax-free allowance between spouses and on stylized unemployment assistance. This is therefore not a purely methodological exercise detached from policy; it is a structural model built to simulate tax-benefit reforms affecting family labour supply. 

# Model / theoretical framework

The model class is a static neoclassical structural family labour-supply model cast as a discrete-choice problem. Family utility depends on the husband’s leisure, the wife’s leisure, and family income. Instead of treating hours as continuous, the paper assumes that each family chooses from a finite set of income-leisure bundles, with hours for each spouse restricted to a discrete grid. In the empirical implementation, this yields 25 or 36 alternatives. Sections III and V define this setup. 

The deterministic utility specification is a direct translog utility function in ((\log y,\log l_m,\log l_f)), where (y) is family after-tax income and (l_m,l_f) are male and female leisure. Observed heterogeneity enters through demographic shifters in the utility parameters, and a multinomial-logit-type extreme-value shock is added to each alternative’s utility. Equation (1), equation (2), and equation (5) are the core formal statements. 

The framework is positive, not normative. Agents choose the preferred discrete hours-income alternative given wages, nonlabour income, and tax-benefit rules. The model is fully structural in the sense that policy simulations are performed directly on the estimated behavioural structure, but the paper does not define a welfare criterion or fairness principle. 

On feasible sets, the paper does not model explicit individualized opportunity sets or latent job menus. The baseline choice set is a common discrete grid of hours combinations translated into income-leisure bundles through the tax-benefit system. Hours restrictions are added later in a reduced-form way through alternative-specific utility penalties for part-time work, not through an estimated distribution of actual job offers. This is crucial for locating the paper relative to your project. 

# Key objects

The main behavioural objects are the family utility function (U(v)=v'Av+b'v), the discrete set of male and female hours combinations, the induced after-tax family income (y_j) for each hours pair, and the choice probabilities over alternatives. Equations (1), (5), and (6) are the core objects. 

A second key object is the wage process. Since wages are unobserved for nonworkers, the paper estimates male and female wage equations with selection correction and then integrates over the implied wage distribution when wages are missing. Equations (7)–(12) in Section IV.A formalize this. 

A third key object is the hours-restrictions term. To fit the observed hours distribution, the paper augments utility with alternative-specific constants for part-time hours of husbands and wives. Equations (13) and (14) define these reduced-form “hours restriction” parameters. 

# Data

The data come from the Dutch Socio-Economic Panel, October 1987 wave. The estimation sample includes two-adult households with both partners aged 16–65. After removing a small number of missing-value cases, 2,859 families remain. Of these, 13.0% have neither spouse employed, 3.1% have only the wife working, 49.7% have only the husband working, and 34.1% have both spouses working. Pages 73–74 provide the sample description. 

Table 2 on page 75 gives the main sample statistics. Mean weekly hours are 35.42 for husbands and 9.68 for wives when nonworkers are included. Mean before-tax hourly wages are 26.71 Dutch guilders for employed men and 18.46 for employed women. Other family income is negatively correlated with both male and female hours and participation. 

# Identification logic

Identification is structural and heavily parametric. Preferences are identified from observed hours choices over the discrete budget set induced by wages, other income, and the Dutch tax-benefit rules. The paper relies on the translog utility specification, the extreme-value error structure, and the selected demographic shifters to recover behavioural parameters. 

A concrete identification challenge concerns nonworkers’ wages. The paper explicitly criticizes the usual practice of plugging in wage predictions for nonworkers as if they were observed without error, and instead integrates over the distribution implied by estimated wage equations. This is one of the paper’s clearest identification contributions. Section IV.A is central here. 

A second identification issue concerns hours restrictions. The paper is explicit that these are inferred indirectly from the mismatch between the standard model and the observed hours distribution. There is no direct information on actual job offers or constraints, so hours restrictions are only partially and indirectly identified. This is why the paper describes its treatment of restrictions as ad hoc. 

Random preferences are also difficult to identify. When explicit random preference terms are added, the estimates barely change and the additional variance terms are imprecise. The paper therefore does not find strong evidence that this extension is empirically important. Section V.B discusses this. 

# Estimation / empirical strategy

The core estimation method is maximum likelihood for the basic model and smooth simulated maximum likelihood for extensions involving unobserved wages and random preferences. The discrete-choice probabilities are multinomial-logit probabilities conditional on wages and preference shocks. When wages are missing, the likelihood is integrated over wage distributions and approximated by simulation draws. Sections III, IV.A, and IV.C provide the formal setup. 

The paper estimates four main model classes. Model I is the basic discrete-choice translog model. Model II adds hours restrictions. Model III adds both hours restrictions and wage-prediction-error integration. Model IV further adds random preferences. Table A2 reports the parameter estimates for all of these. 

The model is then evaluated in three ways: by checking monotonicity and quasi-concavity ex post, by comparing actual and predicted marginal frequencies of hours choices, and by computing elasticities and policy simulations. Table 3 shows the failure of the basic model to match the hours distribution, while Table 5 summarizes policy simulations. Figures 1 and 2 illustrate the shapes of estimated indifference curves for different family types. 

# Treatment of preferences

Preferences are treated explicitly and structurally. Utility is defined over family income and both spouses’ leisure, with observed heterogeneity through the number of children, the presence of young children, and age variables. This allows the paper to recover how family composition shifts labour-supply behaviour. 

The estimated preference structure implies the standard result that wives’ labour supply is more responsive than husbands’ labour supply. The indifference curves in Figure 1 and the elasticity calculations in Table 4 reflect this. The paper also notes that family composition affects female labour supply more strongly than male labour supply. 

However, the stochastic part of preferences is limited in the basic model because the multinomial-logit errors cannot be interpreted as genuine random preferences. That is why the paper later adds explicit random preference terms in (\beta_2) and (\beta_3). Empirically, though, this extension changes little. 

# Treatment of opportunities / constraints

This section is crucial for your purposes. The paper does not model opportunities explicitly as individualized feasible job sets, latent job offers, or wages-hours packages drawn from an opportunity distribution. All households face the same discretized grid of hours options in the core model. 

The paper does, however, take constraints more seriously than a pure unconstrained continuous-hours model. Its main empirical finding is that the standard discrete-choice model strongly overpredicts part-time work and underpredicts nonparticipation and standard full-time hours. Table 3 on page 78 shows this clearly. To deal with this, the paper introduces negative utility shifters for part-time alternatives, interpreted as reduced-form hours restrictions, search costs, or unattractive job characteristics. Section IV.B is explicit on this. 

So the paper treats availability constraints only implicitly. It does not assume a universal continuous choice set, but it still does not model actual opportunity heterogeneity in a rich way. It helps distinguish preference estimation from reduced-form hours scarcity, but not preferences from explicit feasible sets (A_i). This distinction should be kept very clear. 

# Welfare / normative object

The paper is purely positive with policy simulations. It does not construct an individual welfare metric, equivalent income, or social welfare function. It also does not discuss responsibility, compensation, or fairness. 

Its relevance for welfare analysis is indirect. Because it produces structurally estimated labour-supply responses under tax-benefit rules, it can serve as an input into policy analysis. But the paper itself does not define how policy changes should be normatively evaluated. 

It is also not a decomposition paper. It does not decompose inequality or welfare into preferences, opportunities, and pay schedules. At most, it isolates the empirical importance of hours restrictions relative to standard preference-based labour-supply modelling. 

# Main findings

The first main finding is methodological: the basic discrete-choice model fits the observed hours distribution poorly, especially by strongly overpredicting part-time work for both sexes. Table 3 on page 78 documents this starkly. This is the main empirical reason the paper introduces hours restrictions. 

The second main finding is that allowing for hours restrictions substantially improves the fit and reduces estimated labour-supply elasticities. This is the paper’s central substantive message. Table 4 shows that the wife’s own wage elasticity falls from 1.027 in the basic model to 0.524 once hours restrictions are added, while the husband’s falls from 0.153 to 0.104. 

The third main finding is that accounting for wage prediction errors matters much less than hours restrictions. Moving from Model II to Model III reduces elasticities somewhat further, but the change is modest relative to the large shift induced by hours restrictions. Random preferences matter even less empirically. Section V.B and Table 4 make this point clearly. 

The fourth main finding is the headline aggregate elasticity result from the preferred general model: own before-tax wage elasticities of aggregate labour supply are about 0.11 for males and 0.40 for females, with much smaller cross-wage elasticities. This is stated in the introduction and is consistent with the policy simulations. 

The fifth main finding is policy-relevant. Abolishing the transferability of the tax-free allowance increases female labour supply by 4.2% and reduces male labour supply by 0.7%, implying more two-earner households and only a small increase in total hours. Table 5, row 6, is the key source. A stylized move to separate taxes and benefits reduces female labour supply by 7.1%. 

# Main limitations

A first limitation is the treatment of opportunities. Hours restrictions are modeled ad hoc through alternative-specific constants, not through observed or latent job offer sets. The paper itself recognizes this. This is important for your project because the paper is still weak on explicit opportunity modeling. 

A second limitation is staticity. The paper explicitly notes that the model is static and cannot be made consistent with two-stage budgeting in a life-cycle framework because expenditure data are unavailable. Page 67, footnote 5, states this clearly. 

A third limitation is the exogeneity of before-tax wages inside the labour-supply model. Wage prediction errors are handled, but the paper explicitly does not allow for wage endogeneity. Section IV.A says this directly. 

A fourth limitation is discretization. Although computationally convenient, the model uses coarse hours categories and therefore introduces rounding error and leaves some sample information unused. The conclusion acknowledges this directly. 

A fifth limitation is that the preferred model still fails some specification tests. Even after adding hours restrictions, the model can still be rejected by chi-squared diagnostics when male and female hours are considered jointly. Section V.B notes this. 

# Relevance for my JMP

## possible use for framing

This paper is very useful for framing the structural-estimation side of your JMP. It is a canonical reference for why discrete-choice labour-supply models became attractive in the presence of nonlinear taxes and benefits.

## possible use for model design

It is highly useful for model design if your empirical structure remains in the consumption-leisure tradition. It is especially useful for thinking about discrete alternatives, nonconvex budget sets, and joint spousal labour supply.

## possible use for identification

It is useful because it explicitly confronts two standard identification problems: unobserved wages of nonworkers and mismatch between observed hours and unconstrained-choice predictions. It is therefore a strong methodological reference.

## possible use for welfare measurement

Directly limited. The paper does not construct a welfare metric. Indirectly useful, because it gives a way to generate behaviourally grounded counterfactual choices under alternative tax-benefit systems.

## possible use for decomposition

Very limited directly. It does not decompose inequality or welfare into (R), (A), and (y). Indirectly, it shows that reduced-form constraints can materially alter what would otherwise be attributed to preferences.

## possible use for comparative application

Limited directly, since it is a Dutch single-country paper. Strong indirectly, because the modelling strategy became a template for a large comparative labour-supply literature.

# Research questions this paper inspires

1. Can the paper’s discrete choice set over hours-income bundles be extended to a richer job-choice model in which feasible job sets (A_i) vary across households?

2. How much of the “hours restrictions” term is really capturing scarce jobs, search frictions, or nonpecuniary job characteristics rather than pure hours availability?

3. What happens to the paper’s elasticities if before-tax wages are made endogenous to hours, job type, or opportunity structure rather than only treated with prediction-error correction?

4. Can the family labour-supply model be integrated with an explicit well-being measure (W(z,R,A;y)) so that policy simulations are evaluated normatively rather than only behaviourally?

5. How robust are the policy conclusions once one replaces reduced-form hours restrictions by an explicit latent-job or RURO-style opportunity model?

# Challenge to this paper

The paper’s main weakness, relative to your research agenda, is that it solves the tractability problem before it solves the opportunity-set problem. It greatly improves on continuous-hours labour-supply models and recognizes hours restrictions, but it still treats those restrictions in an ad hoc reduced-form way rather than as actual heterogeneous feasible sets. So it is a major methodological step, but not yet a model that cleanly separates preferences from opportunities. 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper models realized labour supply as a discrete choice over income-leisure bundles generated by the tax-benefit system, with preferences over family income and both spouses’ leisure. It also recognizes that observed hours may be constrained, but captures this through hours-restriction parameters rather than through explicit job sets. 

[reasonable inference for my project] In your notation, the realized bundle (z) is closest to the chosen family income-leisure bundle. Preferences (R) correspond to the translog utility ordering, with some observed heterogeneity and optional random preference terms. The pay schedule (y) is represented through before-tax wages combined with the Dutch tax-benefit mapping into after-tax family income. The feasible set (A) is not explicit; at most it is approximated by the common discrete hours grid plus reduced-form hours restrictions. 

[unclear from paper] The paper does not define a well-being measure (W(z,R,A;y)), does not distinguish actual versus reference opportunity sets, and does not analyze axioms such as independence of (A), IIJ, IPIJ, independence of (y), or responsibility for opportunities. These issues are outside its formal scope. 

[reasonable inference for my project] In your taxonomy, the paper is closest to the structural labour-supply and heterogeneous-preferences side of the project, with a limited concession to constrained opportunities via hours restrictions. It is not close to reference opportunity sets or laissez-faire evaluation. It is also not close to a full opportunity-sensitive framework, because (A) is not modeled as an explicit object. 

# Relation to Bargain et al. (2013)

This paper is strongly relevant as a methodological precursor. Bargain et al. (2013) estimate discrete-choice labour-supply models and then construct welfare comparisons under heterogeneous preferences. van Soest (1995) is one of the foundational papers that established the tractable discrete-choice labour-supply framework on which much of that later literature relies. The difference is that van Soest is purely behavioural and methodological, whereas Bargain et al. adds the welfare-measurement layer. [reasonable inference for my project] supported by 

# Relation to opportunities vs preferences

This paper is more useful for preferences and budget-set modeling than for opportunities. It shows clearly that what looks like preference-based hours choice in a standard model may in fact reflect reduced-form hours restrictions. That is an important caution. 

But it does not provide a genuine opportunity-set model. So for your project it should be read as an intermediate paper: more realistic than unconstrained continuous-hours labour supply, but still far from an explicit (A)-based jobs model. 

# Useful quotations / formulas

The core utility specification is
[
U(v)=v'Av+b'v,
]
with (v=(\log y,\log l_m,\log l_f)'). This is equation (1) and the backbone of the model. 

The discrete-choice probability is
[
\Pr[U_j>U_k\ \forall k\neq j]
=============================

\frac{\exp(U(y_j,l_{mj},l_{fj}))}{\sum_{k=1}^m \exp(U(y_k,l_{mk},l_{fk}))},
]
equation (6). This is the key formal statement that turns the model into a tractable structural discrete-choice labour-supply framework. 

The hours-restriction extension is
[
U_j = U(c_j,l_{mj},l_{fj})+\gamma_m(l_{mj})+\gamma_f(l_{fj})+\varepsilon_j,
]
with negative part-time constants. Equations (13) and (14) are crucial because they are the paper’s main device for capturing constrained hours. 

Table 4 is the most important results table for elasticities, and Table 5 is the key table for policy simulation. Table 3 is central for diagnosing the failure of the basic model. Figures 1 and 2 are useful because they show how estimated indifference curves shift by family type and by partner’s hours. 

# Suggested tags

van-soest-1995, structural-labour-supply, discrete-choice, family-labour-supply, Dutch-tax-benefit-system, hours-restrictions, wage-prediction-errors, random-preferences, policy-simulation

# My quick takeaway

This is a foundational methodological paper for the structural labour-supply side of your corpus. Its strongest contribution is not opportunity-sensitive welfare measurement, but the establishment of a tractable discrete-choice family labour-supply framework that handles nonlinear tax-benefit rules and recognizes that unconstrained hours choice fits the data poorly. For your JMP, it is especially useful as a benchmark on the (R)- and (y)-side of the problem, and as an early warning that reduced-form constraints can materially change estimated behavioural responses without yet giving you a full model of (A).
