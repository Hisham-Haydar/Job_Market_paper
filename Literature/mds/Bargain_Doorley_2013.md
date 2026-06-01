---

title: "Putting Structure on the RD Design: Social Transfers and Youth Inactivity in France"
authors: ["Olivier Bargain", "Karina Doorley"]
year: 2013
outlet: "IZA Discussion Paper No. 7508"
country_or_context: "France"
population: "Childless single individuals aged 20–30 in France; special focus on high-school dropouts"
data_period: "Main analysis: 1999 French Census; wages from pooled 1997–2001 French Labor Force Survey; external-validity checks with Census 2004–2011"
shelf: "structural_labor_supply_rd_identification"
tags: ["regression discontinuity", "structural labor supply", "social assistance", "youth inactivity", "France", "RMI", "RSA", "eligibility discontinuity", "external validity", "counterfactual policy simulation"]
priority: "very high"
read_status: "extracted"
------------------------

# Full citation

Bargain, Olivier, and Karina Doorley. 2013. *Putting Structure on the RD Design: Social Transfers and Youth Inactivity in France*. IZA Discussion Paper No. 7508. 

# One-sentence contribution

The paper combines a regression-discontinuity design with a structural participation model to identify the employment effect of age-conditioned social assistance in France and to simulate counterfactual youth-welfare reforms that the reduced-form RD design alone cannot address. 

# Why this paper matters

This paper matters because it is not just another labor-supply application: its methodological point is to reconcile internal validity from a natural experiment with external validity from a structural model. The authors explicitly frame the paper as an attempt to “put structure” on an RD design so that credible local causal evidence can be used for ex ante policy analysis. 

For your project, the paper is especially useful for identification strategy. It gives a concrete example of how one can use a quasi-experimental discontinuity to identify a behavioral model, then use that model to extrapolate away from the threshold and simulate counterfactual policies. It is much less useful for normative well-being measurement itself, but highly relevant for the empirical problem of moving from credible causal variation to structural counterfactuals. 

# Core research question

Can one combine a regression-discontinuity design and a structural labor-supply model to identify the causal employment effect of French social assistance eligibility at age 25 and then use that identified model to predict counterfactual youth-welfare reforms, including the extension of welfare to the under-25s and the introduction of in-work benefits? 

# Economic setting and context

The institutional setting is the French minimum-income system before and after the 2009 reform. Before 2009, the main social assistance program was the *Revenu Minimum d’Insertion* (RMI), a last-resort transfer available to French residents aged at least 25, unless younger individuals had dependent children. For childless singles under 25, the age condition created a sharp discontinuity in eligibility. 

The policy relevance is immediate. The paper is motivated by high youth unemployment and youth poverty in France, and by the question whether extending welfare to the under-25s would create an inactivity trap. It also studies the 2009 *Revenu de Solidarité Active* (RSA), which added an in-work benefit component by reducing the withdrawal rate and thereby potentially restoring work incentives. 

# Model / theoretical framework

The paper combines two frameworks. First, it uses a sharp regression-discontinuity design based on the fact that childless single individuals become eligible for RMI at age 25. Second, it embeds that discontinuity in a static structural labor-supply model in which individuals choose whether to participate based on financial incentives to work. 

The structural model is deliberately simple at the behavioral margin studied. The general setup is a discrete-choice labor-supply model over hours and consumption, but for the empirical core the authors focus on the participation margin only. Individuals compare utility when not working with utility when working full-time, where disposable income depends on wages, age, and the tax-benefit system, and where fixed costs or search costs of work are allowed to vary with age and other characteristics. 

The framework is positive, not normative. It is designed to estimate participation responses and simulate reforms, not to define a social welfare function or a fairness criterion. The paper does not evaluate justice, compensation, or responsibility; it studies labor-supply behavior under institutional eligibility rules. 

On feasible sets, the paper does not model explicit job opportunity sets. The choice environment is narrower: the key margin is participation versus non-participation, with age-based eligibility affecting out-of-work income and therefore the net gain from working. Labor-market frictions appear only indirectly through fixed costs, search costs, or non-employment residuals. 

# Key objects

The central policy object is disposable income as a function of earnings and age, (C(E;A)). Under the pre-2009 system, this includes housing subsidies and, for those aged at least 25, the RMI transfer with a taper rate on earnings. The age threshold directly shifts out-of-work disposable income and therefore the gain from participation. 

The key reduced-form object is the RD treatment effect at age 25, interpreted as the discontinuous effect of eligibility for RMI on employment. The key structural object is the latent participation propensity
[
Y_i^* = a_i + g_i\delta(A_i) + b_{1i}C(w_iH_1,A_i) - b_{0i}C(0,A_i) + \varepsilon_i,
]
which makes employment depend on in-work and out-of-work disposable income. 

A second crucial object is the counterfactual policy scenario. The paper simulates four particularly important ones: replacing RMI by RSA, abolishing RMI, extending RMI to the under-25s, and extending RSA to the under-25s. Figures 5–8 on pages 27–31 summarize these counterfactual employment profiles visually. 

# Data

The main source for both the RD analysis and the structural estimation is the 1999 French Census, using a 1/4 public sample of the population. This very large dataset is necessary because RD estimation around age thresholds requires large cell sizes, especially once the sample is restricted to childless single individuals aged 20–30. 

Because the Census does not contain labor income or benefit receipt, wage imputation is performed using the French Labor Force Survey, mainly pooled over 1997–2001. The authors estimate wage equations on the LFS and predict wages into the Census; they also check robustness with a matching-based wage imputation procedure. Table 1 on page 11 shows that Census and LFS samples are broadly comparable in demographics, education, and simulated disposable income. Figures B.1 and B.2 in the appendix compare actual, predicted, and matched wage distributions. 

For external-validity checks around the 2009 RSA reform, the authors also use later Census data, especially pooled years 2004–2008 for the pre-reform period and 2010–2011 for the post-reform period. 

# Identification logic

The identification logic is the paper’s strongest feature. The reduced-form treatment effect is identified by a sharp RD design exploiting the fact that childless singles below age 25 are not eligible for RMI while otherwise similar individuals just above age 25 are. Under local continuity of potential outcomes in age, any discontinuity in employment at the threshold can be attributed to eligibility. 

The structural model is then identified using the same discontinuity plus an additional exclusion restriction: the marginal utility of consumption is assumed not to vary with age. Age is allowed to affect participation through a smooth function, through wages, and through the tax-benefit schedule, but not through the coefficient on consumption itself. This restriction is what allows extrapolation away from the threshold. 

This is a strong and explicit identification strategy. It is substantially more transparent than a standard structural labor-supply model identified only from tax-benefit nonlinearities and demographic variation. At the same time, external validity still depends on the maintained structural assumptions, especially the exclusion restriction and the static participation framework. [reasonable inference for my project] supported by 

# Estimation / empirical strategy

The empirical strategy proceeds in layers. The authors first estimate reduced-form RD specifications of employment on age, age polynomials or splines, and the age-25 eligibility indicator. They check robustness to alternative age specifications, narrower windows around the threshold, and placebo groups not affected by the discontinuity. Figures 1 and 2 on page 20 are central: Figure 1 shows a visible drop in employment at age 25 for high-school dropouts, while Figure 2 shows no corresponding discontinuity in placebo years before or just after RMI introduction. 

They then estimate a structural participation model by simulated maximum likelihood, with wages first imputed from the labor force survey using a Heckman-style wage equation and, alternatively, matching. The model is estimated on Census data and validated by how well it reproduces the observed discontinuity and age-employment profiles. Tables 2 and 3 compare RD and structural estimates of the RMI effect; Figures 3 and 4 on pages 24–25 compare actual and predicted employment profiles by age. 

Finally, they use the estimated model for counterfactual simulation. Figures 5–8 on pages 27–31 are especially important: they show predicted employment profiles under the RSA reform, under abolition of RMI, under extension of RMI to the under-25s, and under extension of RSA to the under-25s. 

# Treatment of preferences

Preferences enter through a static participation utility model in which individuals compare utility from work and non-work as a function of disposable income and age-related taste shifters. The model also includes unobserved heterogeneity in the coefficient on in-work income. 

However, the paper’s real emphasis is not on preference heterogeneity as an end in itself. Preferences are a behavioral ingredient needed to map the RD discontinuity into a structural participation model. The paper does not ask normative questions about whether preference differences should be respected, compensated, or held fixed. 

An important empirical point is that the model allows low attachment to the labor market to differ by education group, especially for high-school dropouts. In practice, this is interpreted as higher participation costs or search costs for the least educated, rather than only lower wages. This matters for the predicted heterogeneity in policy responses. 

# Treatment of opportunities / constraints

This section is important for your broader research agenda. The paper does not model explicit feasible job sets or latent job distributions. There is no RURO-type opportunity density and no direct representation of a set (A_i) of feasible jobs. 

Still, the paper is not a pure unconstrained labor-supply model either. Constraints enter through at least three channels: the age-based eligibility rule, the minimum wage floor in wage imputation, and reduced-form participation or search costs that partly absorb labor-market rationing and weak labor-market attachment. The authors explicitly acknowledge that non-employment can reflect low gains to work, high preference for leisure, productivity below the minimum wage, or “other” non-employment such as frictional or cyclical unemployment. 

So the paper helps distinguish financial incentives from observed employment outcomes, but it does not separate preferences from opportunities in a clean feasible-set sense. It is much more about incentive-based participation under quasi-experimental identification than about opportunity sets as such. 

# Welfare / normative object

The paper is not a welfare-evaluation paper in the normative sense. It does not construct an individual welfare metric, an equivalent-income measure, or a social welfare function. It does not compare policies using welfare weights or inequality aversion. 

The closest thing to a normative issue is the policy-design question: whether extending social assistance to young people creates inactivity traps and whether adding an in-work component can offset them. This is policy-relevant, but it is not yet a formal treatment of responsibility, compensation, or opportunity-sensitive welfare. 

Hence the paper is best classified as purely positive with policy simulation, not as an explicitly normative contribution. 

# Main findings

The headline result is that eligibility for the pre-2009 French RMI at age 25 reduces employment among childless singles, especially among high-school dropouts. The abstract reports a drop of between 5 and 9% in the employment rate of young high-school dropouts, and the main RD estimates imply a discontinuity of around 3.9 percentage points for that group. Table 2 is central here. 

The structural model reproduces the local RD effect reasonably well. Table 2 shows that for high-school dropouts the RD estimate and the structural model both imply roughly a 3.9 percentage point employment effect in the cubic-age specification. This is one of the paper’s key validation results. 

The model also predicts that replacing RMI with RSA restores work incentives. Figure 5 on page 27 shows that the RSA reform raises employment for the over-25s relative to the pre-reform system, especially among high-school dropouts. Table 5 shows that the policy change from RMI to RSA increases employment by about 3 percentage points for high-school dropouts in the preferred specifications, and the ex post RD evidence around the actual reform is broadly consistent with that prediction. 

A further substantive result is that simply extending RMI to the under-25s would likely reduce participation among vulnerable youth. Figure 7 on page 30 shows a clear simulated employment drop for high-school dropouts under such an extension. By contrast, Figure 8 on page 31 shows that extending RSA to the under-25s would have little or no significant negative employment effect, because the in-work component offsets the inactivity trap. 

# Main limitations

A first limitation is that the model is deliberately narrow. It focuses on participation rather than a richer labor-supply or job-choice problem. This is appropriate for the discontinuity studied, but it rules out analysis of within-employment margins, job quality, and richer opportunity sets. 

A second limitation is the strong exclusion restriction needed for extrapolation: the marginal utility of consumption is assumed not to vary with age. This is clearly stated and defended, but it remains a substantive assumption rather than something directly verified. 

A third limitation is the treatment of opportunities. The model does not explicitly distinguish low productivity, rationing, search frictions, and true preferences in a fully structural way. Some of these are absorbed into fixed costs or residual non-employment. For your (W(z,R,A;y)) interests, that means the paper remains weak on explicit (A). [reasonable inference for my project] supported by 

A fourth limitation is that welfare analysis is absent. The paper can say whether reforms raise or lower employment, but not whether they improve well-being once income, leisure, and constraints are jointly valued. 

# Relevance for my JMP

## possible use for framing

This paper is highly useful for framing the methodological problem of combining internal validity and external validity. It gives a clean example of how a credible local design can discipline a structural model rather than compete with it.

## possible use for model design

It is useful for model design if your empirical work needs to identify a structural participation or labor-supply model from a discontinuity or other sharp institutional rule. The paper is especially relevant if you want stepwise identification rather than relying only on global functional form.

## possible use for identification

This is the strongest use. The paper offers a template for quasi-experimentally anchored structural estimation. In your research program, this is highly relevant whenever you want credible behavioral parameters before moving to decomposition or welfare analysis.

## possible use for welfare measurement

Directly, it is limited. The paper does not construct a welfare measure. Indirectly, it is useful because it shows how to obtain a behaviorally credible model that could later sit underneath a welfare framework.

## possible use for decomposition

Directly, very limited. It does not decompose outcomes into preferences, opportunities, and pay schedules. Indirectly, it is useful because it separates local causal policy effects from structural mechanisms and highlights the importance of identifying the participation margin cleanly.

## possible use for comparative application

Limited directly, since this is a France-specific paper. But the design logic is portable to any setting with age-based or threshold-based social-policy eligibility rules.

# Research questions this paper inspires

How can a quasi-experimental discontinuity be used to identify a richer labor-supply model in which feasible job sets (A_i) are explicit rather than absorbed into participation costs?

Can one extend the paper’s RD-plus-structure strategy to estimate a model where young workers choose among jobs with different wages, hours, and occupations rather than simply work versus non-work?

If a structural model is identified from a local discontinuity, what additional restrictions are minimally necessary to extrapolate from local policy effects to opportunity-sensitive well-being measures (W(z,R,A;y))?

How would the paper’s policy conclusions change if reform evaluation were conducted in terms of well-being rather than employment alone?

Can one use similar age-based discontinuities to identify not only labor-supply responses but also components of opportunity scarcity or demand-side rationing?

# Challenge to this paper

The strongest challenge is that the paper solves the identification problem more successfully than the interpretation problem. It gives a persuasive way to identify a structural participation response from an RD design, but it still leaves ambiguous what exactly lies behind non-employment: tastes, search costs, rationing, low productivity, or weak opportunities. For your project, that matters because the empirical credibility is high while the conceptual separation of (R) and (A) remains incomplete. 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper models realized labor-market status as the result of participation choices under age-conditioned financial incentives. It explicitly studies how the tax-benefit system shifts the gain from working versus not working, and it uses a quasi-experimental discontinuity to identify this behavioral response. 

[reasonable inference for my project] In your notation, the realized bundle (z) is very reduced here: essentially employment status and disposable income under a given rule. Preferences (R) are represented by the static participation utility parameters and unobserved heterogeneity. The pay schedule (y) enters through wages and the age-dependent tax-benefit mapping (C(E;A)). The feasible set (A) is not explicit; at most it is proxied indirectly by participation costs, search frictions, and the minimum-wage-related rationing logic. 

[unclear from paper] The paper does not define an individual well-being measure (W(z,R,A;y)), does not distinguish actual from reference opportunity sets, and does not study axioms such as independence of (A), independence of (y), or responsibility for opportunities. These issues are outside its explicit scope. 

[reasonable inference for my project] In your taxonomy, the paper is closest to empirical identification of (R)-driven and incentive-driven behavior under (y), not to explicit treatment of (A). It is not close to independence of (A), but mainly because (A) is not modeled explicitly. It is also not a laissez-faire or responsibility-sensitive evaluation. Its main contribution to your framework is methodological: credible identification for a structural behavioral layer that could later feed into a richer jobs-and-wellbeing model. 

# Relation to Bargain et al. (2013)

This paper is related to Bargain et al. (2013) mainly through the labor-supply side, not the welfare-measurement side. Bargain et al. (2013) is about welfare comparison under heterogeneous preferences in the consumption-leisure space, whereas this paper is about identifying a structural participation model from a regression-discontinuity design and then simulating policy reforms. The present paper is therefore methodologically complementary: it is much stronger on quasi-experimental identification, much weaker on welfare metrics, and narrower in its behavioral margin. [reasonable inference for my project] supported by

# Relation to opportunities vs preferences

This paper is more helpful for identifying incentive effects than for separating opportunities from preferences. It shows that some observed inactivity among vulnerable youth is responsive to age-conditioned welfare eligibility and to the presence or absence of in-work benefits. That is informative about the role of incentives. 

But it does not provide a clean opportunity-set framework. Non-employment may reflect low productivity, weak attachment, search costs, or labor-market rationing, and these are not fully separated. So the paper is best read as a bridge from causal participation effects to structural modeling, not as a resolution of the opportunities-versus-preferences problem. 

# Useful quotations / formulas

A central reduced-form equation is the RD specification
[
Y_i^*=\alpha_i+\gamma_i\delta(A_i)+\beta_i I(A_i\geq \bar A)+\varepsilon_i,
]
which captures the employment discontinuity at age 25. This is the core causal-identification device. 

A central structural equation is the participation propensity
[
Y_i^* = a_i + g_i\delta(A_i) + b_{1i}C(w_iH_1,A_i) - b_{0i}C(0,A_i) + \varepsilon_i.
]
This is crucial because it makes explicit the behavioral interpretation of the RD effect as a response to financial gains from work. 

The charts on pages 27, 30, and 31 are especially useful. Figure 5 shows that RSA raises predicted employment relative to RMI for the over-25s, especially among high-school dropouts; Figure 7 shows that extending RMI to the under-25s reduces predicted employment for high-school dropouts; and Figure 8 shows that extending RSA to the under-25s largely avoids that disincentive effect. 

# Suggested tags

regression-discontinuity, structural-labor-supply, France, RMI, RSA, youth-inactivity, eligibility-threshold, external-validity, quasi-experimental-identification, participation-model

# My quick takeaway

This is a very useful paper for the empirical-methods side of your corpus. Its main value is not a theory of welfare or opportunities, but a rigorous demonstration that a structural participation model can be credibly anchored in a sharp institutional discontinuity and then used for counterfactual policy simulation. For your JMP, it is especially valuable as a methodological bridge between reduced-form credibility and structural counterfactual analysis.
