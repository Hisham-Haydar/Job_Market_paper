---

title: "Inequality of Opportunity in Brazil"
authors: ["François Bourguignon", "Francisco H. G. Ferreira", "Marta Menéndez"]
year: 2007
outlet: "Review of Income and Wealth"
country_or_context: "Urban Brazil"
population: "Active urban males aged 26–60 with positive earnings"
data_period: "1996 cross-section (PNAD 1996), analyzed by seven 5-year birth cohorts"
shelf: "inequality_of_opportunity_decomposition"
tags: ["inequality of opportunity", "Roemer", "Brazil", "earnings inequality", "circumstances vs effort", "decomposition", "Theil", "family background"]
priority: "high"
read_status: "extracted"
------------------------

# Full citation

Bourguignon, François, Francisco H. G. Ferreira, and Marta Menéndez. 2007. “Inequality of Opportunity in Brazil.” *Review of Income and Wealth* 53(4). 

# One-sentence contribution

The paper proposes an empirical measure of the share of earnings inequality attributable to observed circumstances beyond individual control, and applies it to urban Brazil, finding that family background, race, and region of birth account for a substantial fraction of male earnings inequality. 

# Why this paper matters

This paper matters because it is one of the clearest empirical attempts to operationalize a Roemer-style distinction between circumstances and efforts, and then to quantify how much observed earnings inequality is due to unequal opportunities rather than to residual factors. It is therefore highly relevant for any project concerned with compensation versus responsibility, and with decomposition of inequality into ethically distinct sources. 

For your project specifically, its main value is not in structural labor supply or job-choice modeling, because it does neither. Its value lies in showing how one can move from a normative distinction—circumstances versus effort—to an empirical decomposition with counterfactual distributions, partial effects, and bounds under imperfect identification. That is directly useful for thinking about decomposition, but only indirectly useful for thinking about feasible job sets (A) in (W(z,R,A;y)). 

# Core research question

How much of observed earnings inequality can be attributed to unequal opportunities, understood as differences in exogenous circumstances such as family background, race, and region of birth, and how much of this effect operates directly on earnings versus indirectly through variables interpreted as efforts? 

# Economic setting and context

The paper studies male earnings inequality in urban Brazil in 1996, using the PNAD household survey. The authors focus on Brazil because it is one of the world’s most unequal countries, and because the 1996 survey includes unusually rich retrospective information on parental education and father’s occupation, which can be used to proxy family-background circumstances. 

The ethical and conceptual context is Roemer’s equality-of-opportunity framework. The paper adopts the distinction between “circumstances,” which are beyond the individual’s control, and “efforts,” which can be influenced by individual choice, and asks how much observed inequality can be traced to the former. This is explicit from the introduction. 

# Model / theoretical framework

The model class is an empirical decomposition model of earnings inequality, motivated by Roemer’s opportunity-egalitarian distinction between circumstances and efforts. It is not a structural choice model and not a labor-supply model. The basic economic object is an earnings function
[
w_i = f(C_i, E(C_i,v_i), u_i),
]
where (C_i) denotes circumstance variables, (E_i) denotes effort variables that may themselves depend on circumstances, and (u_i) is an unobserved residual component. This structure is stated explicitly in Section 4. 

The framework is positive in implementation but explicitly normative in motivation. The paper does not estimate a welfare function or a utility-maximization problem. Instead, it defines inequality of opportunity as the reduction in earnings inequality that would arise if differences in observed circumstances were eliminated. This is a counterfactual measurement exercise, not a behavioral theory of job choice. 

There is no feasible set, no opportunity set in the sense of a set of jobs, and no explicit modeling of constraints or choice sets. “Opportunities” here are proxied by background characteristics that shape life chances, not by individual-specific feasible menus. That distinction is crucial for your project. 

# Key objects

The main economic objects are current hourly earnings (w), circumstance variables (C), effort variables (E), the observed earnings distribution (F(w)), and the counterfactual earnings distribution (\Phi(w)) that would obtain if observed circumstances were equalized. The key decomposition measure is
[
\Theta_I = \frac{I(F)-I(\Phi)}{I(F)},
]
which is interpreted as the share of earnings inequality attributable to unequal opportunities, for a chosen inequality index (I). This appears in Section 4. 

The paper also defines a direct-effect decomposition using a counterfactual distribution (F^d(w^d)), obtained by equalizing circumstances only in the earnings equation while holding observed effort variables at their realized values. The difference between the overall and direct decompositions is then interpreted as the indirect effect of opportunities operating through effort variables. 

Observed circumstance variables are race, region of birth, father’s and mother’s education, and father’s occupational status. Observed effort variables are own schooling, a migration dummy, and labor-market status. These definitions are explicit in Sections 3 and 4. 

# Data

The data come from the 1996 PNAD household survey conducted by IBGE. The analysis is restricted to urban areas, active males aged 26–60, with positive earnings. The final sample contains 28,474 occupied men after exclusions for non-response and sample restrictions. The sample is divided into seven 5-year birth cohorts, from 1936–40 through 1966–70. These details are in Section 3 and Table 1. 

The dependent variable is real hourly earnings from all occupations. Circumstances include race, region of birth, parental schooling, and father’s occupation. Efforts include own years of schooling, migration status, and labor-market status. Table 1 on page 10 provides the cohort-level descriptive statistics, including mean earnings, schooling, parental background, migration, father’s occupational status, and labor-market status. 

# Identification logic

Identification is not causal in the modern quasi-experimental sense. The paper explicitly recognizes omitted-variable problems: many relevant circumstances and efforts are unobserved, and these are likely correlated with the observed regressors. As a result, OLS estimates of both the earnings equation and the reduced form may be biased. 

The authors do not claim to solve this with instruments, and they explain why a standard IV strategy is unlikely to be convincing in this setting. Instead, they use a partial-identification-style robustness exercise: they simulate a wide range of admissible correlations between regressors and residuals, impose positive semi-definiteness of the covariance matrix and a few sign restrictions, and then construct 90 percent confidence intervals for unbiased coefficients. This is the core identification strategy in Section 5. 

Concretely, they randomly draw correlation coefficients between regressors and the residual, discard draws that violate covariance-matrix admissibility or sign restrictions, generate a distribution of possible bias vectors, and use the surviving coefficient ranges to simulate counterfactual earnings distributions. Thus, the decomposition results are presented as intervals rather than point-identified causal effects. This is a major strength of the paper. 

# Estimation / empirical strategy

The empirical strategy combines log-linear earnings regressions with counterfactual distribution simulations. The “full” earnings equation includes both circumstances and effort variables. A reduced-form earnings equation includes only circumstances and is used to estimate the overall effect of opportunities. Separate effort equations are also estimated, although the main decompositions are ultimately implemented through the earnings equations rather than through a fully structural system. 

The direct-effect decomposition comes from the full earnings equation. The overall opportunity decomposition comes from the reduced form. For each admissible coefficient vector, the authors simulate counterfactual earnings distributions in which observed circumstances are equalized, compute inequality indices over those distributions, and compare them with the observed earnings inequality. The central results are reported mainly with the Theil index, with analogous Gini decompositions discussed more briefly. 

# Treatment of preferences

The paper does not model preferences in the sense of utility functions or heterogeneous tastes over labor, leisure, occupations, or consumption. “Effort” is not derived from an explicit choice-theoretic model, and the authors are careful to place the term in quotation marks because the variables classified as efforts may also reflect luck or circumstance. 

This is an important limitation for your purposes. The paper separates circumstances from observed effort proxies, but it does not separate circumstances from preferences. Therefore, it cannot help much with welfare measurement under heterogeneous preferences, except by analogy. 

# Treatment of opportunities / constraints

This section is central, and the paper is conceptually useful but not in the same sense as RURO or feasible-set models. It does not model opportunities as actual feasible job sets, latent jobs, hours restrictions, or demand-side constraints. It treats opportunities as circumstance variables that shape life chances: race, region of birth, parental education, and father’s occupation. 

So the paper does model opportunities explicitly, but only as exogenous background determinants of earnings. It does not model availability constraints implicitly through a budget set, nor does it assume a universal job-choice set because it is not a choice model. It also does not use latent jobs. Demand-side constraints are not modeled as such, although labor-market status appears among the observed “effort” variables and may partly reflect labor-market structure. 

The paper helps distinguish opportunity heterogeneity from a residual category containing effort, luck, and unobserved factors. It does not distinguish opportunity heterogeneity from preference heterogeneity, because preferences are not explicitly in the model. Thus, for your taxonomy, it separates observed opportunities from “other determinants,” but not opportunities from preferences in a structural sense. 

# Welfare / normative object

The paper is positive with explicit normative motivation. The normative object is not individual welfare but inequality of opportunity, defined as the share of observed earnings inequality attributable to exogenous circumstances. Earnings are the outcome metric; the decomposition is performed using inequality indices such as the Theil index and, secondarily, the Gini coefficient. 

This is clearly useful for thinking about responsibility versus compensation. The paper is explicit that inequalities due to factors beyond individual responsibility are inequitable and should be compensated, whereas inequalities due to personal responsibility are not to be compensated, citing Roemer and Peragine. That is one of its most direct points of contact with your research interests. 

The paper is also directly useful for decomposition of inequality. It provides an overall opportunity share, a direct effect, and an indirect effect through effort variables. What it does not provide is a well-being measure over bundles, preferences, feasible sets, and pay schedules, nor does it address reference opportunity sets. 

# Main findings

The central quantitative finding is that the five observed circumstances account for between 10 and 37 percent of the Theil index of male earnings inequality across cohorts in urban Brazil, with a simple average central estimate of about 23 percent. These are the headline results in the introduction, conclusion, and Table 5 on pages 24–25. 

The direct effect of circumstances on earnings, holding observed effort variables fixed, accounts on average for about 60 percent of the total opportunity effect. In other words, the effect of family background, race, and origin is not mainly mediated through schooling, migration, and labor-market status; a large part works directly through wage determination conditional on those observed efforts. This is reported in Table 5 and emphasized in the conclusion. 

Parental education is the most important individual circumstance variable. Table 6 and Figure 2 show that equalizing parental education produces the largest reduction in earnings inequality for every cohort. Father’s occupation is the second most important circumstance, while race also matters, especially for younger cohorts. Region of birth plays a smaller role once other background variables are controlled for. 

The paper also finds weak evidence that the share of inequality attributable to observed circumstances is lower for younger cohorts. Figure 1 on page 26 and the discussion on page 27 suggest a decline in the opportunity share from older to younger cohorts, although the authors are careful to note that cohort patterns cannot be cleanly interpreted as time trends. 

# Main limitations

The first limitation is conceptual for your purposes: opportunities are measured through observed background variables rather than through actual feasible sets. This paper is therefore much closer to the equality-of-opportunity literature in the Roemer tradition than to job-opportunity-set or RURO frameworks. It cannot tell you how opportunity sets (A) should be represented in a jobs-and-wellbeing model. 

A second limitation is that preferences are absent. The decomposition is between circumstances and a residual category containing observed efforts, unobserved efforts, luck, measurement error, and any omitted preference heterogeneity. This makes the decomposition ethically suggestive but economically coarse. 

A third limitation is identification. The paper is careful and sophisticated about bias, but it still does not achieve point identification of causal opportunity effects. The results are bounds under maintained assumptions about omitted-variable correlations and sign restrictions, not experimentally grounded causal estimates. 

A fourth limitation is the outcome metric. The object decomposed is current earnings inequality among active urban men. This excludes participation, household composition, non-labor income aggregation beyond the specific earnings measure, and any broader notion of well-being. It is therefore narrower than the type of welfare object you are ultimately interested in. 

# Relevance for my JMP

## possible use for framing

This paper is very useful for framing any argument that inequality should be decomposed into ethically distinct sources, especially sources linked to responsibility versus compensation. It gives a concrete empirical example of how Roemerian language can be taken to the data. 

## possible use for model design

It is not directly useful for structural model design in labor supply or job choice. But it is useful as a reminder that, if you want to empirically separate opportunity from other determinants, you need a transparent operationalization of “opportunities.” This paper operationalizes them as exogenous circumstances. Your own project would need a richer object if opportunities are to mean feasible job sets. 

## possible use for identification

It is useful as an example of bounded inference under omitted-variable concerns. The Monte Carlo construction of admissible unbiased coefficient intervals is methodologically interesting, especially in settings where clean instruments are unavailable and the point is decomposition rather than causal policy evaluation. 

## possible use for welfare measurement

Directly, limited. The paper measures opportunity shares in earnings inequality, not well-being. Indirectly, it is useful because it shows one way to define a counterfactual compensation-oriented metric from an observed distribution. 

## possible use for decomposition

This is one of the paper’s strongest uses for your project. It provides a decomposition into overall opportunity effects, direct effects, and indirect effects through effort proxies. That architecture could inspire later decompositions in a richer (W(z,R,A;y)) framework. 

## possible use for comparative application

Potentially useful. The cohort comparison suggests how one might compare opportunity shares across groups, generations, regions, or countries, even when the underlying object is not directly observed opportunity sets. 

# Research questions this paper inspires

How would the measured “opportunity share” of inequality change if opportunities were represented by estimated feasible job sets rather than by family-background circumstances?

Can one construct a decomposition of inequality in well-being (W(z,R,A;y)) into a background-circumstance component, a preference component, and a feasible-set component, analogously to this paper’s direct and indirect decomposition?

What conditions would justify treating own schooling, migration, and labor-market status as responsibility variables rather than as channels through which unequal opportunities continue to operate?

How sensitive are opportunity-share decompositions to the choice of outcome metric: hourly earnings, annual earnings, disposable income, equivalent income, or a broader well-being index?

Can a Roemer-style circumstances/effort distinction be integrated with a structural discrete-choice labor model so that one obtains both behavioral consistency and an ethically interpretable decomposition?

# Challenge to this paper

The main challenge is that the paper’s ethical language is sharper than its empirical categories. Calling schooling, migration, and labor-market status “efforts” is analytically convenient, but these are themselves shaped by social structure, institutions, and inherited constraints. The authors know this and qualify the terminology, but the decomposition still rests on a coarse mapping between responsibility and observables. For a more demanding fairness framework, that mapping may be too crude. 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper defines opportunities through exogenous circumstance variables such as race, parental background, and region of birth, and measures the share of earnings inequality attributable to those circumstances. It does not define opportunities as feasible job sets, nor does it introduce an individual well-being measure depending on realized bundle, preferences, feasible set, and pay schedule. 

[reasonable inference for my project] In your notation, the paper is much closer to treating “opportunities” as components of a background vector that shifts attainable outcomes than as the set (A) itself. One could loosely interpret the circumstances as determinants of the feasible set or of the pay schedule, but that would be an inference, not something the paper formally does. 

[unclear from paper] It is not clear how the paper’s framework would map into (R), because preferences are absent; nor how to map it exactly into (A), because feasible sets are not modeled. The relation to (y) is also indirect, since the outcome is observed earnings rather than a pay schedule over jobs. 

[reasonable inference for my project] In your taxonomy, the paper is closest to responsibility for opportunities, compensation for opportunities, and decomposition of inequality. It is not close to independence of (A), independence of (y), laissez-faire type evaluation, or reference opportunity sets. If anything, it presumes that background circumstances matter ethically and empirically and should not be neutralized by an independence principle. 

# Relation to Bargain et al. (2013)

[not central]

# Relation to opportunities vs preferences

This paper is directly about opportunities versus something like responsibility, but not about opportunities versus preferences. Its ethical distinction is between exogenous circumstances and observed effort proxies. Since preferences are not modeled, the paper cannot tell whether inequality arises because people value different bundles differently, because they face different feasible sets, or because they exert different effort conditional on common preferences. 

That said, it is highly relevant for your broader theme because it shows how an ethically motivated decomposition can be implemented even when only partial observables on background are available. It is therefore useful as a lower-dimensional empirical analogue of your more ambitious conceptual distinction between preferences and opportunities. 

# Useful quotations / formulas

The key decomposition measure is
[
\Theta_I = \frac{I(F)-I(\Phi)}{I(F)},
]
where (I(F)) is observed earnings inequality and (I(\Phi)) is inequality in the counterfactual distribution with equalized observed circumstances. This is the central formula in Section 4. 

The paper’s main structural representation is
[
w_i = f(C_i,E(C_i,v_i),u_i),
]
which is important because it allows circumstances to affect earnings both directly and indirectly through effort variables. 

A second useful formula is the direct-effect decomposition:
[
\Theta_I^d = \frac{I(F)-I(F^d)}{I(F)},
]
which isolates the direct impact of observed circumstances on earnings conditional on observed efforts. 

# Suggested tags

inequality-of-opportunity, Roemer, Brazil, earnings-inequality, circumstances-effort, parental-background, opportunity-decomposition, Theil-index, intergenerational-persistence

# My quick takeaway

This is one of the more relevant papers for your opportunity-decomposition interests, but not for your RURO or feasible-set interests. Its core contribution is to show how one can empirically measure a compensation-relevant component of inequality using observed circumstances, counterfactual distributions, and bounded inference under omitted-variable bias. For your project, it is especially valuable as a template for decomposition logic and for responsibility-versus-compensation framing. It is much less useful for modeling (A) as an actual opportunity set, or for handling heterogeneous preferences in a structural way.
