---

title: "The Sensitivity of Structural Labor Supply Estimations to Modeling Assumptions"
authors: ["Max Löffler", "Andreas Peichl", "Sebastian Siegloch"]
year: 2018
outlet: "ifo Working Paper No. 259"
country_or_context: "Methodological study using Germany and the United States"
population: "Working-age households in SOEP Germany and CPS United States, split into five labor-supply types: single men, single women, couples with only male flexible, couples with only female flexible, and couples with both partners flexible"
data_period: "SOEP 2008 wave with labor-market outcomes and tax-benefit system for 2007; March CPS 2007 for the U.S."
shelf: "structural_labor_supply_methodology"
tags: ["structural labor supply", "discrete choice", "model uncertainty", "wage imputation", "labor supply elasticities", "Germany", "United States", "microsimulation", "random utility"]
priority: "high"
read_status: "extracted"
------------------------

# Full citation

Löffler, Max, Andreas Peichl, and Sebastian Siegloch. 2018. “The Sensitivity of Structural Labor Supply Estimations to Modeling Assumptions.” *ifo Working Paper* No. 259. 

# One-sentence contribution

The paper conducts a controlled meta-analysis of structural discrete-choice labor-supply models by estimating 3,456 plausible model variants on the same data and shows that estimated elasticities are driven far more by wage-treatment choices than by most utility-function or heterogeneity assumptions. 

# Why this paper matters

This paper matters because it addresses a problem that is highly relevant for any structural labor-supply project: the extent to which estimated behavioral elasticities are genuinely data-driven rather than artifacts of the modeler’s specification choices. It is therefore not a substantive paper about one labor-market mechanism, but a methodological paper about the internal fragility of the structural estimates that many later welfare or policy analyses take as inputs. 

For your project, the paper is especially useful because it shows where sensitivity really lies inside standard structural labor-supply models. Its headline conclusion is that elasticities are not very sensitive to many widely discussed choices, such as the functional form of utility or most heterogeneity specifications, but are highly sensitive to wage imputation and the treatment of wage prediction error. That is directly relevant if you want to interpret estimated preferences separately from opportunity or wage-setting objects. 

# Core research question

How sensitive are labor-supply elasticities estimated from structural discrete-choice models to plausible alternative modeling assumptions, especially regarding utility specification, heterogeneity, choice-set constraints, and the treatment of wages? 

# Economic setting and context

The paper is methodological rather than policy-specific. Its empirical environment is built from German SOEP data and U.S. CPS data, but the substantive purpose is not to analyze Germany or the U.S. per se. Instead, these datasets are used as platforms for systematic robustness analysis of discrete-choice labor-supply estimation. 

The broader context is the long-standing disagreement over labor-supply elasticities, including differences between micro and macro estimates and disagreement even across studies using similar micro methods. The paper’s premise is that part of this variation may come from model specification choices rather than only from true behavioral differences across populations or institutions. 

# Model / theoretical framework

The model class is the standard structural discrete-choice labor-supply model. Individuals choose among a finite set of jobs or hours alternatives (j \in J_n), including non-participation, and maximize utility over disposable income and leisure:
[
\max_{j \in J_n} U(C_{nj},L_j,e_{nj}) = \max_{j \in J_n} U(f(w_{nj}h_j,I_n\mid x_{nj}),T-h_j,e_{nj}).
]
This is a random-utility representation of labor-supply choice, not a reduced-form participation equation. 

The paper decomposes utility into a systematic part and an idiosyncratic part:
[
U(C_{nj},L_j,e_{nj}\mid x_{nj},\beta_n,\gamma_j)
================================================

\phi(C_{nj},L_j\mid x_{nj},\beta_n,\gamma_j)+e_{nj}.
]
Choice probabilities then take the familiar logit or mixed-logit form, with job availability terms (g(j)) entering multiplicatively as weights on alternatives. The paper presents both the standard discrete-choice setup and a more general mixed-logit specification in which preferences, availability, and wage prediction are integrated over latent distributions. 

The framework is positive, not normative. It is a model of labor-supply choice used for policy simulation, not a social-choice or welfare-theoretic framework. The paper is explicit that it focuses on the estimation technology behind structural labor-supply elasticities. 

Opportunities or constraints are treated in a limited structural sense. The paper allows labor-market conditions ( \gamma_j ) to capture the availability of job types, fixed costs of work, search costs for part-time jobs, or hours rigidities, but in the baseline empirical implementation it follows the standard literature by using common discrete hours alternatives and variants with fixed costs or part-time restrictions. It does not estimate latent individual-specific job opportunity sets in the RURO sense. 

# Key objects

The main objects are the systematic utility function (v(C_{nj},L_j)), preference parameters ( \beta_n ), labor-market condition parameters ( \gamma_j ), wage rates ( w_{nj} ), the tax-benefit map (f(\cdot)), and the choice probabilities over discrete alternatives. 

A second central object is the wage-imputation procedure. The paper distinguishes three related choices: whether wages are estimated jointly or in a two-step procedure, whether predicted wages are used only for non-workers or for the full sample, and whether the wage prediction error is ignored, approximated with one draw, or integrated out. These are the key methodological objects driving the paper’s results. 

The main empirical outcome objects are the Akaike Information Criterion and simulated own-wage labor-supply elasticities, decomposed into extensive, intensive, and total responses. Table 4 on pages 15–18 is the central summary table for these results, and Figure 1 on page 16 shows the distribution of aggregated own-wage elasticities across model variants for four demographic groups. 

# Data

The baseline analysis uses the German SOEP, specifically the 2008 wave with labor-market outcomes referring to the preceding year and the 2007 tax-benefit system. The sample is restricted to working-age households and excludes those for whom flexible labor supply is not well defined, such as households in which all decision makers are self-employed, civil servants, or in military service, as well as certain multi-adult households. The estimation sample is then split into five labor-supply types. 

The German subsamples are 779 single-male households, 1,065 single-female households, 688 couples with flexible male only, 1,042 couples with flexible female only, and 3,099 couples with both partners flexible. Tax-benefit calculations rely on IZAΨMOD, with the German tax-benefit system approximated by a flexible second-degree polynomial to reduce computational burden. The paper reports that the approximation fits extremely well, with (R^2) above 99 percent for all groups except single women, for whom it is still 97 percent. 

As a robustness check, the authors also use U.S. CPS data and TAXSIM. This second dataset is not central to the conceptual argument, but it is important because the main sensitivity conclusions persist outside the German setting. Table A.1 reports the corresponding U.S. meta-regression results. 

# Identification logic

Identification is the standard structural identification of discrete-choice labor-supply models. Preferences are identified from variation in working hours, wages, non-labor income, household characteristics, and the nonlinearity of the tax-benefit function. The paper emphasizes that labor-market conditions ( \gamma_j ) can only be separately identified from preferences under specific functional-form assumptions. 

A key assumption is wage exogeneity with respect to preferences and labor-market conditions:
[
E(\beta_n w_{nj}\mid x_{nj})=0,
\qquad
E(\gamma_j w_{nj}\mid x_{nj})=0.
]
The paper is explicit that most of the literature assumes this, largely for tractability, and that this assumption is itself questionable. This point is highly relevant because it means that part of what is usually called “preference estimation” may depend critically on how wages are modeled. 

There is no quasi-experimental identification here. The paper is instead about controlled variation in modeling assumptions while holding the underlying data fixed. Its identification exercise is therefore methodological: isolate the marginal impact of model assumptions on fit and elasticities by systematically estimating all plausible combinations. 

# Estimation / empirical strategy

The empirical strategy is a controlled meta-analysis. The paper estimates 3,456 model variants per dataset, each corresponding to a different plausible combination of assumptions concerning utility form, observed heterogeneity, unobserved heterogeneity, welfare stigma, hours restrictions or fixed costs, Halton draws, wage imputation, and the handling of wage prediction errors. With five labor-supply groups, this yields 17,280 maximum-likelihood estimations per dataset before convergence losses. Table 3 on pages 12–13 documents the combinatorial design and the number of converged models. 

Estimation uses maximum simulated likelihood with Halton sequences. The general likelihood integrates over both preference heterogeneity and predicted-wage uncertainty. The authors then standardize outcomes within labor-supply groups and regress model fit and simulated elasticities on indicators for the underlying modeling assumptions. Thus the paper’s main regression results are “meta-regressions” over estimated models rather than individual-level outcome regressions. 

Elasticities are simulated by increasing own wages by 10 percent and aggregating the resulting labor-supply responses; the paper also checks robustness to 1 percent wage changes and to using means, medians, and other summaries. These robustness tables are in the appendix and confirm the main result that wage treatment dominates. 

# Treatment of preferences

Preferences are explicit in the model, but the paper’s main point is that many preference-side modeling choices do not alter simulated elasticities much. The authors vary the functional form of the systematic utility function across translog, quadratic, and Box-Cox specifications, and allow observed heterogeneity in preferences for leisure and consumption as well as random-coefficient forms of unobserved heterogeneity. 

Their substantive conclusion is that elasticities are largely robust to these preference-side choices. Utility-function changes sometimes affect statistical fit, and some heterogeneity specifications improve fit, but the implied labor-supply elasticities do not move nearly as much as when the wage process is handled differently. This is one of the paper’s strongest results. 

This does not mean preferences are unimportant economically. Rather, it means that, within the class of standard structural discrete-choice models, many alternative reasonable preference specifications deliver similar elasticity predictions. The paper therefore shifts attention away from the usual debates over translog versus Box-Cox and toward the wage side of the model. 

# Treatment of opportunities / constraints

The paper does not model opportunities explicitly as individual-specific feasible job sets. It remains within the conventional discrete-choice labor-supply tradition where individuals choose among a finite set of hours alternatives or jobs, and labor-market conditions enter through availability weights (g(j)), fixed costs, or hours restrictions. 

This is important for your project. The paper clearly recognizes the conceptual role of availability and cites the Aaberge-Dagsvik tradition in which feasible jobs and latent opportunities matter, but its own empirical analysis does not estimate a RURO-style opportunity process. Instead, it treats opportunities mainly through hours restrictions, fixed costs, and choice-set design choices. 

The paper therefore helps distinguish preference assumptions from wage-treatment assumptions much better than it distinguishes preference heterogeneity from opportunity heterogeneity. In your taxonomy, it is a model-uncertainty paper about standard structural labor-supply estimation, not a paper on opportunity sets (A) as such. 

# Welfare / normative object

The paper is positive with downstream welfare relevance, not directly normative. Its motivation is that labor-supply elasticities are central inputs into welfare analysis and optimal taxation, and it cites Eissa et al. and Diamond–Saez for this reason. But the paper itself does not define welfare, compensation, or responsibility objects. 

The most explicit normative connection appears in the conclusion, where the authors note that their findings matter for tax policy design because the optimal top marginal tax rate depends heavily on the elasticity one feeds into the formula. Using the Diamond–Saez calibration, an elasticity of 0.25 implies a top rate of 72.7 percent, whereas an elasticity of 0.65 implies 50.6 percent. This is not itself a normative theory, but it shows the policy stakes of model sensitivity. 

The paper does not help directly with responsibility for opportunities, compensation for opportunities, reference opportunity sets, or decomposition of inequality. Its welfare relevance is indirect: it disciplines the empirical credibility of structural inputs later used in welfare and tax analysis. 

# Main findings

The central finding is that estimated labor-supply elasticities are highly sensitive to wage treatment but much less sensitive to most other common modeling assumptions. The abstract states that plausible choices concerning the modeling of the wage distribution and the imputation of missing wages lead to point estimates between 0.2 and 0.65. 

More specifically, using predicted wages for the full sample instead of only for non-workers roughly doubles the average own-wage elasticity in the meta-analysis, from about 0.23 to 0.46. Ignoring wage prediction error when using full-sample predicted wages pushes the average elasticity to about 0.65, whereas integrating out the wage prediction error lowers it to about 0.35. These are the paper’s most important empirical results, stated in the introduction and discussed again in Section 4.2. 

By contrast, the functional form of utility, observed and unobserved preference heterogeneity, welfare stigma, and most hours-restriction choices have much smaller effects on the resulting elasticities, though fixed costs and part-time restrictions do affect statistical fit and tend to raise extensive-margin elasticities somewhat. Table 4 on pages 15–18 is the key source here. 

The graphical evidence on page 16 is also informative. Figure 1 shows the distribution of simulated total own-wage elasticities across converged model variants for singles and couples, and visually confirms wide dispersion even within the same demographic group. That figure illustrates the paper’s core claim that model variation alone can generate substantial elasticity dispersion. 

The U.S. robustness analysis in Table A.1 broadly confirms the message from Germany: wage-imputation choices still matter materially, even though some other coefficients differ in magnitude. This strengthens the claim that the result is not driven by one country alone. 

# Main limitations

The first limitation is that the paper studies sensitivity within the class of standard structural discrete-choice models, not across fundamentally different opportunity-set frameworks. So while it says a great deal about wage-treatment fragility, it says much less about whether the entire model class is misspecified from the viewpoint of latent jobs or demand-side opportunities. 

A second limitation is that the paper’s main exercise is internal rather than external. It shows how results move across model variants, but it does not establish which variant is closest to the truth. The authors themselves explicitly state that they cannot identify a uniquely true elasticity and that the choice between wage-imputation procedures depends partly on the researcher’s substantive interpretation of how workers perceive wages. 

A third limitation for your purposes is that the paper presumes wage exogeneity in most implementations and does not resolve the deeper problem of how wages, preferences, and opportunities are jointly generated. The conclusion itself suggests that future research should estimate preferences and wages jointly. 

A fourth limitation is normative scope. The paper is highly relevant for empirical inputs into welfare or optimal-tax analysis, but it does not itself provide a framework for deciding which elasticities should matter ethically, nor how opportunity-related heterogeneity ought to enter welfare comparisons. 

# Relevance for my JMP

## possible use for framing

This paper is very useful for framing a cautionary methodological paragraph in your JMP. It provides strong support for the claim that estimated structural labor-supply parameters are not mechanically credible just because the model is sophisticated. Some assumptions matter much more than others. 

## possible use for model design

It is useful for model design mainly as a warning. If your project uses a standard discrete-choice labor-supply model, this paper shows that wage imputation and wage-error treatment deserve much more careful attention than is typical in the literature. It is less informative about how to model opportunities explicitly. 

## possible use for identification

This is one of the paper’s strongest uses for your project. It shows where identification is fragile inside structural labor-supply models and why wage handling is not a minor implementation detail. It also gives a taxonomy of assumptions you can explicitly audit in your own model. 

## possible use for welfare measurement

Indirect but important. Since welfare and optimal-tax exercises often use labor-supply elasticities as inputs, the paper is highly relevant for assessing the robustness of welfare conclusions. It is not itself a welfare-measurement paper. 

## possible use for decomposition

Directly limited. The paper is not a decomposition paper in your sense. It decomposes sensitivity across modeling assumptions, not welfare or inequality into preferences, opportunities, and pay. 

## possible use for comparative application

Useful methodologically. Because the paper applies the same sensitivity logic to both Germany and the U.S., it suggests a template for checking whether your own results are robust across datasets or institutional settings. 

# Research questions this paper inspires

How sensitive are RURO or latent-job estimates to alternative wage-imputation procedures once wages are treated as job attributes rather than exogenous worker characteristics?

If one moves from standard discrete hours models to explicit opportunity-set models, does wage treatment remain the dominant source of sensitivity, or do opportunity-set assumptions become equally important?

Can one jointly estimate wages, preferences, and job opportunity sets in a way that reduces the exogeneity problem identified in this paper?

How do welfare rankings based on (W(z,R,A;y)) change when the estimated wage process is varied across plausible modeling assumptions?

Which wage-imputation procedure is most consistent with a model in which workers choose among latent jobs rather than choosing hours conditional on an exogenous or expected wage?

# Challenge to this paper

The main challenge is that the paper convincingly shows sensitivity but stops short of resolving it. Once wage-treatment choices are shown to shift elasticities dramatically, the natural next question is which procedure is structurally or behaviorally most defensible. The paper gives partial guidance, especially in favor of integrating out wage prediction errors, but it does not settle the deeper modeling problem of how wages should enter labor-supply choice in the first place. 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper studies standard structural discrete-choice labor-supply models in which utility depends on consumption and leisure, wages are key inputs, and labor-market conditions can be captured by availability weights, fixed costs, or hours restrictions. It is centrally concerned with how modeling assumptions affect estimated elasticities. 

[reasonable inference for my project] In your notation, the paper is closest to the (R) and (y) sides of the problem. It is highly relevant for how one models wages and preference heterogeneity, but much less helpful for modeling (A) as a true feasible job set. The labor-market condition term (g(j)) can be read as a reduced-form proxy for opportunity structure, but the paper does not operationalize (A) as an individual-specific set-valued object. 

[unclear from paper] It remains unclear from the paper how its availability terms, fixed costs, or hours restrictions should map into a normative feasible-set concept. It is also unclear how much of what is commonly estimated as “preference” in these models is really compensating for wage or opportunity misspecification. 

[reasonable inference for my project] In your taxonomy, the paper is closest to a critique of naive use of (y)-driven structural estimates and to a warning about empirical confounding between wages and preferences. It is not a paper on independence of (A), reference opportunity sets, laissez-faire evaluation, or explicit responsibility for opportunities. Its main value is methodological discipline before one builds welfare claims on top of structural estimates. 

# Relation to Bargain et al. (2013)

This paper is closely related to the broader Bargain-style literature on structural labor-supply estimation and cross-model comparison, even though it is not itself a welfare-comparison paper. It explicitly cites Bargain and Peichl and Bargain et al. as reference points for the importance of study characteristics and cross-country heterogeneity in estimated elasticities. Its specific contribution is narrower and more technical: to isolate the effect of modeling assumptions within the standard structural labor-supply class. 

For your purposes, it is best read as a methodological companion to the Bargain tradition. Where Bargain-type work often uses structural estimates for welfare or policy comparisons, Löffler–Peichl–Siegloch ask how robust those estimates are to the underlying implementation choices. That makes it a useful cautionary counterpart rather than a substitute. 

# Relation to opportunities vs preferences

This paper is only indirectly about opportunities versus preferences. It does not attempt to separate preference heterogeneity from feasible job-set heterogeneity in a substantive labor-market sense. Instead, it shows that what appears to be preference responsiveness can be heavily altered by wage modeling choices. 

That is still valuable for your project. Before one can cleanly distinguish opportunities from preferences, one must know whether the wage side of the model is stable and credibly handled. This paper shows that, in standard structural labor-supply models, wage treatment is a major source of variation and therefore a possible source of confounding in any later preference-versus-opportunity interpretation. 

# Useful quotations / formulas

The core static labor-supply problem is
[
\max_{j\in J_n} U\big(f(w_{nj}h_j,I_n\mid x_{nj}),T-h_j,e_{nj}\big).
]
This is the basic structural decision problem analyzed throughout the paper. 

The decomposition of utility into systematic and idiosyncratic parts is
[
U(C_{nj},L_j,e_{nj}\mid x_{nj},\beta_n,\gamma_j)
================================================

\phi(C_{nj},L_j\mid x_{nj},\beta_n,\gamma_j)+e_{nj}.
]
This is central because the whole sensitivity exercise concerns how assumptions about the systematic component and related objects affect the resulting elasticities. 

The generalized mixed-logit likelihood is
[
L =
\prod_{n=1}^N
\int
\int
\int
\frac{\exp(v_{ni}[\cdot\mid \hat w_{ni},\beta_n])g(i\mid \gamma_i)}
{\sum_{j\in J_n}\exp(v_{nj}[\cdot\mid \hat w_{nj},\beta_n])g(j\mid \gamma_j)}
, f(\beta_n,\gamma)f(\hat w_n), d\beta_n, d\gamma, d\hat w_n.
]
This formula is useful because it makes clear that wage prediction and its distribution enter the likelihood directly, which is exactly why wage-treatment assumptions matter so much. 

# Suggested tags

structural-labor-supply, model-sensitivity, wage-imputation, wage-prediction-error, discrete-choice, mixed-logit, labor-supply-elasticities, methodology

# My quick takeaway

This is a high-priority methodology paper for your corpus. Its main message is sharp: much of the variation in structural labor-supply elasticities comes not from the utility specification or standard heterogeneity choices, but from how the wage process is modeled and imputed. For your project, it is especially important as a warning against overinterpreting structural preference estimates before auditing the wage side of the model.
