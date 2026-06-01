---

title: "Evaluating Alternative Representations of the Choice Sets in Models of Labor Supply"
authors: ["R. Aaberge", "U. Colombino", "T. Wennemo"]
year: 2009
outlet: "Journal of Economic Surveys"
country_or_context: "Methodological paper using a Norwegian female labour-supply model for simulation"
population: "Married/cohabiting females aged 20–62 in Norway in the underlying estimated 'true' model"
data_period: "Underlying estimation sample from the 1995 Norwegian Survey of Level of Living; simulations benchmarked to the 1994 tax regime and a flat-tax reform"
shelf: "choice_set_representation_structural_labour_supply"
tags: ["structural labour supply", "discrete choice", "choice set specification", "random utility", "opportunity density", "sampled alternatives", "fixed alternatives", "prediction performance", "policy simulation", "Norway"]
priority: "very high"
read_status: "extracted"
------------------------

# Full citation

Aaberge, R., U. Colombino, and T. Wennemo. 2009. “Evaluating Alternative Representations of the Choice Sets in Models of Labor Supply.” *Journal of Economic Surveys* 23(3): 586–612. 

# One-sentence contribution

The paper shows, using Monte Carlo and large-sample simulation exercises, that in discrete-choice labour-supply models the way the choice set is represented—fixed versus sampled alternatives, and uniform versus heterogeneous availability of alternatives—has limited effect on in-sample fit but can materially affect out-of-sample policy predictions. 

# Why this paper matters

This paper matters because it targets a methodological issue that is central to structural labour-supply modeling but often treated as a technical detail: how the analyst represents the household’s feasible set inside a discrete-choice model. The authors argue that this issue matters especially for policy simulation, which is the main practical use of these models. 

For your project, the paper is highly relevant because it explicitly separates preferences from constraints and then asks how different empirical representations of the choice set affect prediction. That makes it directly useful for thinking about the empirical side of (A)-type objects, even though the paper does not formulate an explicit well-being measure (W(z,R,A;y)). 

# Core research question

How much do alternative empirical representations of the choice set in discrete-choice labour-supply models affect model fit and, more importantly, out-of-sample policy prediction performance? 

# Economic setting and context

The paper is methodological rather than a substantive country study. Its empirical core is a previously estimated model of married/cohabiting females’ labour supply in Norway, based on the 1995 Norwegian Survey of Level of Living, with ages restricted to 20–62. That model is treated as the “true” data-generating process for the simulation exercises. 

The policy context is tax reform evaluation. The paper’s motivation is that discrete-choice labour-supply models are commonly used to predict the effects of tax and welfare reforms, and therefore their adequacy should be judged not only by in-sample replication of observed behaviour but by their ability to predict post-reform outcomes. 

# Model / theoretical framework

The model class is a random-utility discrete-choice labour-supply model. In the basic formulation, the individual chooses among opportunities characterized by hours of work and possibly other job attributes, and utility is written as
[
U(f(wh,I),h,j)=v(f(wh,I),h)+\varepsilon(j),
]
with (f) the tax-transfer rule, (w) the wage rate, (h) hours, and (j) unobserved job or individual characteristics. Under the Type I extreme-value assumption, choice probabilities take a multinomial-logit form. 

A central theoretical issue is whether the analyst treats all alternatives as equally available or instead introduces an opportunity density (p(h)). The paper is explicit that many applications assume equal availability of all hour values, while other approaches allow for heterogeneous accessibility of alternatives through a density of opportunities that may differ across individuals. 

The framework is positive and methodological, not normative. The paper studies how different empirical representations of the feasible set affect prediction. It does not evaluate fairness axioms, responsibility, compensation, or interpersonal well-being directly. 

# Key objects

The main objects are the systematic utility function (v), the stochastic term (\varepsilon), the tax-transfer mapping (f), and the opportunity density (p(h)). The paper’s central conceptual distinction is between the preference component (v) and the opportunity-side component (p(h)) in the choice probability. 

A second key object is the representation of the choice set itself. The paper compares fixed alternatives versus sampled alternatives, 6 versus 24 alternatives, and models with or without a “job” dummy and “peaks” dummies that capture non-uniform availability of work opportunities. Table 1 summarizes the 16 model variants. 

The performance object is the relative prediction error, computed for participation, hours, and disposable income, both under the current tax regime and under a flat-tax reform. Tables 8 and 9 report the summary regressions explaining how modeling choices affect this prediction error. 

# Data

The underlying “true” model is estimated on 1,842 married/cohabiting females from the 1995 Norwegian Survey of Level of Living, with ages 20–62. Husbands’ behaviour and non-labour income are treated as exogenous in the simplified application used here. 

The paper then generates simulated samples from that estimated model. In the Monte Carlo exercise, 30 samples of 1,842 observations are drawn. In the second exercise, a larger sample of 11,052 observations is generated to focus on systematic differences across model specifications rather than sampling noise. 

# Identification logic

This is not an identification paper in the causal-inference sense. The paper does not use quasi-experimental variation. Its logic is instead methodological: treat one structurally estimated model as the data-generating process, estimate alternative models with different choice-set representations on simulated samples, and compare their prediction errors. 

Identification of the substantive behavioural parameters in the “true” model remains structural and parametric. The key paper-specific contribution is not new identification of preferences or constraints, but evaluation of specification error induced by alternative representations of the choice set. [explicit in paper] 

For your project, the important lesson is that in-sample fit is not an adequate validation criterion for structural models if the intended use is policy evaluation. The relevant test is out-of-sample predictive performance after reform. [reasonable inference for my project] supported by 

# Estimation / empirical strategy

The paper first defines a “true” model of female labour supply with a Box–Cox-style utility specification and a non-uniform opportunity density for hours, including peaks around part-time and full-time jobs. That model is estimated by maximum likelihood using sampled alternatives: the chosen value plus 999 sampled values from the empirical distribution of offered hours. Appendix A, especially Table A1, reports the estimated parameters. 

It then estimates 16 alternative models that vary along four dimensions: fixed versus sampled alternatives, 6 versus 24 alternatives, inclusion or exclusion of a job dummy, and inclusion or exclusion of peaks dummies. Table 1 lists these models, and Table A2 reports their estimated parameters. 

Prediction performance is assessed both in-sample under the 1994 tax system and out-of-sample under a revenue-neutral flat tax. For each model, participation rates, hours of work, and disposable income are predicted by income decile and compared with the values generated by the true model. The paper then regresses the log of the summary prediction error on indicators for the different specification choices. Tables 8 and 9 are central. 

# Treatment of preferences

Preferences are represented through the systematic utility function (v(f(wh,I),h)), with consumption, leisure, age, and children entering the specification. The paper keeps the preference specification fixed across the competing models in order to isolate the effect of alternative choice-set representations. This is methodologically important because the exercise is not about comparing different utility forms but about comparing different representations of opportunities. 

Thus, the paper treats preferences as stable structural primitives within the simulation design. It is not about normative treatment of heterogeneous preferences, but about how errors in representing the feasible set contaminate prediction even when preferences are correctly specified. [reasonable inference for my project] supported by 

# Treatment of opportunities / constraints

This is the core section for your purposes. The paper explicitly studies whether one should assume that all hour values are equally available or instead allow availability to vary across hours and across individuals through an opportunity density (p(h)). The authors stress that much of the literature assumes equal availability, while their own line of work allows individual-specific densities of opportunities. 

In the “true” model, the opportunity set is represented by a density in which market opportunities are distinguished from non-market opportunities and where full-time and part-time hours receive additional mass through peaks dummies. This implies that not all work-hour options are equally accessible, and the model is designed to reflect labour-market structure rather than pure unconstrained choice. 

The paper therefore models opportunities explicitly, though in a simplified one-dimensional hours form rather than as a full job-set object with multiple attributes. It clearly helps distinguish preference heterogeneity from opportunity heterogeneity on the positive side. It also directly addresses whether latent opportunity structure matters for policy simulation. 

However, the paper does not move to an explicit normative feasible-set framework. It studies the statistical and predictive role of the opportunity set, not its ethical role. It does not define actual set-valued (A_i) objects for welfare comparison. [explicit in paper / reasonable inference for my project] 

# Welfare / normative object

The paper is mainly positive and methodological. It is motivated by welfare and tax-policy evaluation, but it does not introduce an explicit welfare measure, social welfare function, or normative criterion in the paper itself. The performance metrics are participation, hours, and disposable income prediction errors. 

Accordingly, the paper is not explicitly normative. It does not treat responsibility for opportunities, compensation for opportunities, reference opportunity sets, or decomposition of inequality. Its contribution is upstream: it studies the empirical reliability of structural models that may later be used in welfare and policy analysis. 

# Main findings

The headline result, stated already in the abstract and confirmed by the simulations, is that alternative representations of the choice set have little impact on the fitting of observed values but a more substantial impact on out-of-sample prediction performance. This means that a model can look adequate in-sample while performing meaningfully worse in policy evaluation. 

The Monte Carlo results show that models based on sampled alternatives tend to outperform models based on fixed alternatives, especially for policy reform predictions. The paper also finds that prediction tends to be less precise in lower and upper income deciles, particularly for poorer choice-set representations. Tables 2–7 illustrate these patterns for participation, hours, and disposable income. 

The second simulation exercise sharpens the result. Under the current tax regime, evidence in favor of more sophisticated choice-set representations is present but not very strong. Under the flat-tax reform, the pattern is much clearer: using sampled alternatives and allowing for heterogeneous availability of alternatives significantly reduces the prediction error, particularly for hours of work and net income. Tables 8 and 9 are the key evidence. 

A particularly important substantive point is the authors’ conclusion that model adequacy should be judged by ability to predict the outcomes of policy changes, not merely by ability to replicate observed pre-reform outcomes. That is arguably the central methodological message of the paper. 

# Main limitations

A first limitation is that the simulation exercise is explicitly application-specific. The authors themselves note that the results are likely to be application-specific rather than fully general. The paper is therefore best used as strong methodological evidence, not as a universal theorem about all discrete-choice labour-supply models. 

A second limitation is that the opportunity side is simplified. The main simulation uses a female labour-supply model where the opportunity object is essentially a density over hours, not a richer multidimensional job space including wages and non-pecuniary job attributes. For your project, this means it is closer to a reduced RURO-type hours-opportunity model than to a full latent-job model. [reasonable inference for my project] supported by 

A third limitation is that the paper does not provide a welfare interpretation of why one representation of the feasible set is normatively preferable. It only shows which representations improve prediction. Thus it is very useful for empirical model design, but not for ethical analysis of opportunity sets. 

A fourth limitation is that decomposition is absent. The paper does not decompose differences in predicted outcomes into preference, opportunity, and pay-schedule channels in a formal sense; it studies overall model performance across alternative choice-set specifications. 

# Relevance for my JMP

## possible use for framing

This paper is one of the strongest methodological references for arguing that empirical treatment of feasible sets is not a secondary detail. If the project aims to say something about opportunities, then how the choice set is represented econometrically is central.

## possible use for model design

It is highly useful for model design. It directly supports using sampled alternatives rather than fixed grids, and it supports introducing heterogeneous opportunity densities rather than assuming equal availability of all options.

## possible use for identification

It is useful mainly as a validation paper. Its main lesson is that structural models should be assessed by out-of-sample policy prediction, not just by in-sample fit.

## possible use for welfare measurement

Directly, limited. The paper does not build a welfare metric. Indirectly, very useful, because any welfare analysis built on a structural labour-supply model will inherit specification error if the choice set is poorly represented.

## possible use for decomposition

Directly, limited. Indirectly, relevant, because it shows that poor empirical representation of (A)-type objects may contaminate any downstream attempt to decompose outcomes into preference and opportunity components.

## possible use for comparative application

Moderate. The paper itself is not comparative across countries, but the methodological lesson is portable to other contexts, especially tax-benefit microsimulation and latent-job labour-supply models.

# Research questions this paper inspires

1. How should one represent empirical feasible sets (A_i) in a structural labour-supply model if the ultimate goal is normative well-being measurement rather than only prediction?

2. Can a RURO-style model with multidimensional job packages replicate the paper’s result that choice-set representation matters little in-sample but substantially out-of-sample?

3. How much of the estimated heterogeneity usually attributed to preferences in discrete-choice labour-supply models is actually due to misspecification of opportunity availability?

4. Can one design validation exercises that test not only post-reform outcome prediction but also prediction of welfare measures built from (z), (R), (A), and (y)?

5. What empirical criteria should determine when fixed-alternative approximations are acceptable and when sampled-alternative representations are necessary?

# Challenge to this paper

The strongest challenge is that the paper convincingly shows the predictive importance of opportunity-set representation without fully opening the black box of what the opportunity set economically is. In this application it is largely a density over hours, augmented by job and peaks dummies. That is already informative, but for a project like yours it leaves open the next step: how to move from econometric convenience to an economically and normatively interpretable object (A). 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper distinguishes sharply between the preference component of utility and the representation of the choice set. Its whole purpose is to evaluate how alternative empirical representations of that choice set affect prediction. It therefore directly supports the idea that feasible opportunities should not simply be absorbed into preferences. 

[reasonable inference for my project] In your notation, the paper is closest to work on the empirical representation of (A). The realized bundle (z) is the observed labour-supply outcome and resulting disposable income; (R) is the systematic utility specification; (A) is approximated by the empirically represented choice set and its opportunity density; and (y) enters through the wage and tax-transfer mapping (f(wh,I)). This is not the paper’s own language, but it is a natural mapping. 

[unclear from paper] The paper does not define a well-being measure (W(z,R,A;y)), does not study axioms such as independence of (A) or independence of (y), and does not discuss reference opportunity sets, responsibility for opportunities, or IPIJ/IIJ-type conditions. Those issues lie outside its explicit scope. 

[reasonable inference for my project] In your taxonomy, the paper is strongly related to explicit modeling of opportunity sets and strongly opposed to any implicit independence-of-(A) stance at the empirical level. It is not about laissez-faire evaluation, responsibility for acquired ability, or decomposition of inequality in the normative sense. Its contribution is methodological: if (A) matters, then it must be represented carefully in the econometric model. 

# Relation to Bargain et al. (2013)

[not central]

# Relation to opportunities vs preferences

This paper is highly relevant to the opportunities-versus-preferences distinction on the positive side. It explicitly treats the representation of opportunities as separate from the representation of preferences and shows that this distinction matters for policy simulation. 

It is less useful on the normative side. The paper does not ask how welfare should treat inequalities arising from opportunities versus preferences. But it does establish an important prerequisite: if empirical models misrepresent opportunities, then any subsequent normative interpretation of behaviour will be on weak foundations. [reasonable inference for my project] supported by 

# Useful quotations / formulas

A central basic formula is the continuous multinomial-logit probability
[
\phi(h)=\frac{\exp(v(f(wh,I),h)),p(h)}{\int_B \exp(v(f(wx,I),x)),p(x),dx},
]
which makes the opportunity density (p(h)) an explicit component of choice, not a residual detail. 

The sampled-alternatives likelihood contribution is
[
\phi(h\mid S)=
\frac{\exp(v(f(wh,I),h)-\ln q(h))}
{\sum_{x\in S}\exp(v(f(wx,I),x)-\ln q(x))},
]
or, in the empirical true model, the same object augmented by the job and peaks dummies. This is central because it explains why sampled alternatives can remain consistent while fixed alternatives need not. 

The paper’s key substantive conclusion is that “the way the choice set is represented has little impact on the fitting of observed values, but a more significant and important impact on the out-of-sample prediction performance.” This is the core methodological takeaway. 

# Suggested tags

choice-set-specification, structural-labour-supply, discrete-choice, random-utility, sampled-alternatives, fixed-alternatives, opportunity-density, policy-prediction, Monte-Carlo, Norway

# My quick takeaway

This is a core methodological paper for your corpus. Its main value is not a new substantive labour-supply result, but a sharp demonstration that the empirical representation of the feasible set can matter greatly for policy prediction even when it seems to matter little for in-sample fit. For your JMP, it is especially useful as evidence that opportunity-set modeling is not a cosmetic econometric detail but a foundational component of any serious attempt to distinguish preferences from opportunities.
