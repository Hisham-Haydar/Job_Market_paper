---

title: "Nonparametric Welfare Analysis for Discrete Choice: Levels and Differences of Individual and Social Welfare"
authors: ["Bart Capéau", "Liebrecht De Sadeleer", "Sebastiaan Maes", "André Decoster"]
year: 2021
outlet: "CESifo Working Paper No. 9071"
country_or_context: "General methodological paper with an empirical application to Germany"
population: "General discrete-choice framework; empirical application uses single females in Germany"
data_period: "Empirical application: German SOEP 2018 wave"
shelf: "nonparametric_discrete_choice_welfare"
tags: ["discrete choice", "welfare analysis", "nonparametric", "money metric utility", "social welfare", "labor supply", "heterogeneous preferences", "choice probabilities", "transition probabilities", "Germany"]
priority: "high"
read_status: "extracted"
------------------------

# Full citation

Capéau, Bart, Liebrecht De Sadeleer, Sebastiaan Maes, and André Decoster. 2021. *Nonparametric Welfare Analysis for Discrete Choice: Levels and Differences of Individual and Social Welfare*. CESifo Working Paper No. 9071, May 2021. 

# One-sentence contribution

The paper develops a nonparametric welfare-analysis framework for discrete-choice random utility models that identifies distributions of individual welfare, welfare changes, and social welfare without imposing strong parametric assumptions on preferences or on unobserved preference heterogeneity. 

# Why this paper matters

This paper matters because it targets a central weakness of much empirical welfare analysis: welfare calculations in discrete-choice settings are often built on restrictive parametric utility assumptions, while unobserved preference heterogeneity is either tightly parameterized or partially ignored. Capéau et al. instead ask what welfare objects can be recovered directly from choice probabilities and transition probabilities, allowing essentially unrestricted unobserved heterogeneity. 

For your JMP, this paper is especially important on the welfare-measurement side. It is not primarily a labor-supply identification paper and not an opportunities paper, but it gives a rigorous bridge from discrete choice behavior to individual and social welfare comparisons under heterogeneous preferences. That is highly relevant if your project eventually needs a welfare layer that is less parametric than the standard structural labor-supply literature. 

# Core research question

How can one conduct individual and social welfare analysis in discrete-choice models while allowing for unrestricted unobserved preference heterogeneity and avoiding strong parametric assumptions, and what welfare conclusions emerge in a labor-supply application to German single females? 

# Economic setting and context

The paper is mostly methodological. Its general setting is a discrete-choice random utility model with a finite set of alternatives and a numeraire. Welfare is studied both at the individual level and at the social level, with particular attention to money-metric measures, welfare differences after price changes, and aggregation across persons. 

The empirical illustration revisits the standard leisure-consumption trade-off in labor supply using German SOEP microdata. Single females choose among three labor-supply states: non-work, part-time work, and full-time work. The policy experiment replaces the current nonlinear German income tax schedule with a revenue-neutral basic-income flat-tax reform. 

# Model / theoretical framework

The model class is a discrete-choice random utility model with unrestricted unobserved preference heterogeneity. Preferences are represented by utility functions (U_c^\omega(y-p_c)), where (c) indexes discrete alternatives, (y) is exogenous income, (p_c) is the price of alternative (c), and (\omega) indexes unobserved preference types. The paper assumes utility is continuous and strictly increasing in the numeraire and that the distribution of preference types is independent of budget sets. 

The paper’s main theoretical innovation is to adapt the class of nested opportunity set (NOS) welfare measures, associated with Fleurbaey’s framework, to discrete choice. In this setting, individual welfare is measured by the largest member of a common family of nested opportunity sets that is still weakly dominated by the person’s actual situation according to her own preferences. Because preferences are random from the econometrician’s viewpoint, these welfare measures become random variables. 

The framework is explicitly normative as well as positive. It is positive in that it starts from observed discrete choices and their associated probabilities. It is normative in that it studies individual welfare levels, welfare differences such as compensating variation and equivalent variation, and social welfare constructed from individual welfare distributions. 

# Key objects

The main objects are choice probabilities (P_i(p,y)), transition probabilities (P_{i,j}(p,p',y)), nested opportunity set welfare measures, money metric utilities (MMUs), compensating variation (CV), equivalent variation (EV), and additively separable social welfare functions. These are the core welfare-theoretic and econometric objects of the paper. 

A central theoretical object is the distribution of welfare itself, not just its mean. The paper emphasizes that once preferences are heterogeneous and unobserved, welfare levels and welfare changes are random variables. Hence the relevant outcome is a welfare distribution, possibly conditional on observed choices, not a single deterministic welfare number. 

In the application, key empirical objects are the welfare distributions of single females by wage quartile and labor-supply status, the welfare distribution under the baseline tax schedule and under the reform, and the joint distribution of baseline welfare with welfare gains and losses from the reform. Figures 5–8 and Table 1 summarize these. 

# Data

There are two layers. The theoretical contribution is not tied to a specific dataset. The empirical application uses microdata from the 2018 wave of the German Socio-Economic Panel (SOEP). The estimation sample is restricted to single females available to the labor market and below age 60, with additional trimming of wage and asset-income outliers and deletion of missing-hours observations. The final subsample contains 1,922 single females. Appendix Table 2 reports the descriptive statistics. 

The labor-supply alternatives are non-work, part-time employment, and full-time employment. Disposable income for each alternative is simulated using a tax-benefit calculator under the German baseline system and under the reform. Missing wages for non-workers are imputed using a Heckman-type selection model. The estimated choice probabilities depend on disposable incomes across alternatives and demographic variables such as age, education, children, and East Germany. 

The empirical data are therefore cross-sectional household microdata combined with tax-benefit simulation. The broader theoretical results, however, are designed to apply generally to cross-sectional and panel data environments with sufficient price and income variation. 

# Identification logic

This is the heart of the paper.

The paper’s main identification insight is that statements about welfare levels can be translated into statements about optimal choice under counterfactual “virtual” prices. Once this equivalence is established, distributions of welfare can be written as functionals of observable choice probabilities. Thus marginal distributions of NOS welfare measures are identified nonparametrically from cross-sectional data, while joint distributions involving welfare before and after price changes are identified from transition probabilities, which in turn require panel data. 

For welfare differences such as CV and EV, the logic is analogous. Their distributions are written as functionals of uncompensated choice probabilities or transition probabilities evaluated at appropriately shifted price vectors. This extends earlier exact welfare results in discrete choice to the case of essentially unrestricted unobserved heterogeneity. 

The key identifying assumptions are strong but transparent. Budget sets must be exogenous with respect to unobserved preference types; utility must be strictly increasing in the numeraire; and, for transition-based welfare comparisons, the unobserved preference type must remain unchanged across the price change. When only cross-sectional data are available, transition probabilities are no longer point identified, but the paper shows they can be bounded using Boole-Fréchet inequalities and stochastic revealed-preference restrictions. 

# Estimation / empirical strategy

The paper is primarily analytic rather than estimation-heavy in the theory sections. The main econometric strategy is to express welfare objects as functionals of choice probabilities and transition probabilities, and then estimate those probabilities nonparametrically. The authors discuss kernel and series methods in general, while emphasizing that the welfare objects themselves, rather than primitive utilities, are the main targets of identification. 

In the empirical application, the choice probabilities for part-time and full-time work are estimated semiparametrically through flexible binary logit specifications with cubic polynomials in disposable incomes for all three alternatives and a linear index in demographics. The non-work probability is the complement. Shape restrictions implied by rationality and monotonicity are imposed through a penalty function. Appendix C.2 explains this implementation in detail, and Appendix Table 3 reports the estimates. 

Welfare distributions are then computed by plugging these estimated choice probabilities into the nonparametric formulas for MMU distributions, social welfare, and joint distributions of baseline welfare with welfare changes under the tax reform. Some objects, especially the joint distribution of baseline welfare and welfare gains, are approximated numerically because the relevant expressions involve derivatives and integrals of probability objects. 

# Treatment of preferences

Preferences are modeled in a deliberately flexible way. The authors allow unrestricted unobserved heterogeneity in preferences across individuals, represented by the type (\omega). This is one of the paper’s defining strengths relative to standard parametric DC-RUM applications. Welfare is therefore not a deterministic scalar for the econometrician, but a random variable induced by unobserved preference heterogeneity. 

The paper is careful not to estimate deterministic utility functions as primitives. Instead, it works directly with choice probabilities and with welfare objects that are functions of the combined utility-and-heterogeneity structure. This is conceptually important: the goal is not to recover one preferred parametric utility specification, but to recover welfare distributions under weaker assumptions. 

At the same time, the paper is not about responsibility-sensitive welfare or explicit normative judgments over heterogeneous preferences in the Fleurbaey-Maniquet axiomatic sense beyond the use of NOS measures. Preferences are heterogeneous and respected by the welfare measure, but the paper does not develop a new fairness axiomatics. 

# Treatment of opportunities / constraints

This section is crucial for your agenda, and the answer is mixed.

The paper does not model opportunities explicitly in the RURO, latent-jobs, or opportunity-set sense that is central to your work. The discrete choice set is taken as given, and the analysis asks how welfare can be measured given that behavioral environment. Hence the paper is largely silent on whether the alternatives available to an individual are themselves constrained, rationed, or heterogeneous across persons in a structural way. 

The “nested opportunity sets” in the paper are welfare-comparison devices, not actual labor-market opportunity sets. They are normative constructs used to cardinalize preferences, not empirical objects describing feasible jobs or actual choice availability. This distinction is essential. The paper is about welfare measurement, not about identifying market opportunities. 

This matters directly for your research direction. The framework can measure welfare very flexibly once a discrete-choice model is given, but it does not solve the preferences-versus-opportunities problem. If the underlying DC-RUM already absorbs opportunity constraints into utility or into observed choice probabilities, the welfare objects derived here inherit that conflation. 

# Welfare / normative object

The welfare objects are nested opportunity set measures, with money metric utilities as the leading example. The paper studies levels of individual welfare, welfare differences such as CV and EV, and social welfare obtained by aggregating individual welfare levels through additively separable Bergson-Samuelson-type social welfare functions. 

This is therefore an explicitly normative paper. It is not merely positive with welfare applications. Its core purpose is to provide a less parametric framework for welfare analysis in discrete-choice settings, including both individual well-being measurement and social aggregation. 

The normative stance is preference-based and money-metric compatible. It is closely linked to Fleurbaey’s NOS framework and to Samuelson’s MMU tradition, but adapted to discrete choice and to unobserved heterogeneity. The result is a welfare apparatus that is richer than the standard expected-CV or expected-logsum approach. 

# Main findings

First, the paper shows that distributions of NOS welfare measures in discrete-choice models can be recovered nonparametrically from observed choice probabilities. This is the main theoretical result. It implies that individual welfare levels need not be computed from a tightly parameterized utility model. 

Second, the paper derives nonparametric expressions not only for marginal welfare distributions, but also for joint distributions of welfare levels and welfare differences, and for social welfare. This extends the scope of welfare analysis from average changes to full distributional analysis. 

Third, with only cross-sectional data, transition probabilities are not point identified, but the paper shows they can be bounded using Boole-Fréchet inequalities and stochastic revealed-preference inequalities. This is an important practical contribution because many empirical settings do not have panel data. 

Fourth, in the German labor-supply application, about 25% of the single females have a conditional MMU distribution that degenerates to a step function, meaning that welfare can be determined exactly for those individuals given their observables and chosen alternative. This is stated in the application discussion on pages 29–31 and illustrated by the individual welfare distributions in Figure 4 on page 30. 

Fifth, the grouped welfare distributions reveal strong interaction between wages, chosen labor-supply state, and unobserved preferences. Figure 5 on page 31 shows that, among high-wage women, the welfare distribution of those choosing full-time work tends to dominate that of part-time and non-workers, whereas for low-wage women the reverse ordering tends to hold. The authors interpret this as evidence that wages and preferences jointly matter for welfare rankings. 

Sixth, at the broader group level, the welfare distribution of the highest wage quartile tends to first-order dominate that of the lower wage quartiles, while the bottom three quartiles are more intermingled. Figure 6 on page 32 emphasizes that high wages matter a great deal, but are not the whole story. 

Seventh, the flat-tax basic-income reform produces a welfare distribution that first-order dominates the baseline distribution in the sample of single females. Figure 7 on page 33 shows this directly, and the text notes that this implies all social welfare functions in their class rank the reform above the baseline. 

Eighth, first-order dominance does not imply universal gains. The paper finds that about 15% of single females lose from the reform, and that losers are disproportionately concentrated among those initially well-off. Figure 8 and Table 1 on page 34 show that roughly 90% of losers belong to the initially best-off third, while almost 98% of the bottom two-thirds gain from the reform. 

# Main limitations

A first limitation, relative to your core research interests, is that the framework takes the discrete choice environment as given. It does not model heterogeneous opportunity sets, job availability, labor demand constraints, latent jobs, or rationing as structural objects. 

A second limitation is the exogeneity assumption on prices and income. The paper notes that this is strong and suggests control-function approaches as a way to handle some forms of endogeneity, but the baseline theory still relies on exogenous budget sets. 

A third limitation is that point identification of joint welfare distributions requires panel-data-type transition information. With only cross-sectional data, one generally gets bounds rather than sharp identification. This is methodologically honest, but empirically restrictive. 

A fourth limitation is that the empirical application uses a coarse three-choice labor-supply model for single females only. This is useful for illustration, but much simpler than the richer labor-supply environments often studied in structural public economics. 

A fifth limitation is that empirical welfare estimates remain sensitive to the chosen welfare metric and the reference prices used in that metric. The authors themselves highlight this as a future research issue in the conclusion. 

# Relevance for my JMP

## possible use for framing

This paper is highly useful for framing a JMP that wants to move beyond parametric welfare analysis in discrete-choice settings. It gives you a strong methodological argument for why welfare comparisons should not be tied mechanically to one parametric utility model. 

## possible use for model design

It is useful if your project ends with a discrete-choice model and you need a welfare layer on top of it. In particular, the NOS/MMU machinery could be a candidate welfare layer for an estimated labor-supply or job-choice model. 

## possible use for identification

This paper is valuable because it shows that some welfare objects are identifiable directly from choice probabilities and transition probabilities, without separate identification of the full underlying utility structure. That is a methodological gain. 

## possible use for welfare measurement

This is the paper’s strongest relevance for your JMP. It provides tools for measuring levels of well-being, not just changes, and for studying the joint distribution of baseline welfare with reform gains and losses. This is especially useful if your project wants to ask whether reforms benefit those who were initially badly off. 

## possible use for cross-country comparison

Potentially very useful. Because the framework is not tied to one country or one parametric utility model, it could in principle be used to compare welfare distributions across countries once comparable discrete-choice probabilities are available. But the paper itself does not solve the comparability problem across different opportunity structures. 

# Research questions this paper inspires

Can a nonparametric welfare layer of this type be combined with a RURO or latent-jobs labor-supply model so that welfare is measured after preferences and opportunities have been separated more carefully?

How much do welfare rankings of tax-benefit reforms change when one moves from parametric structural labor-supply welfare calculations to nonparametric NOS/MMU-based calculations?

Can one construct opportunity-sensitive welfare measures for discrete choice that preserve the nonparametric identification logic of this paper while treating feasible job sets as endogenous or heterogeneous?

In cross-country labor-supply applications, does nonparametric welfare analysis reduce the sensitivity of conclusions to parametric taste assumptions, or do cross-country differences in opportunity sets remain the dominant issue? 

# Challenge to this paper

The strongest omission is that the paper solves a welfare-measurement problem while largely bracketing the opportunity-set problem. Its welfare objects are impressive once a discrete-choice environment is given, but the environment itself may already conflate heterogeneous preferences with heterogeneous opportunities. A future paper could challenge this by embedding the Capéau et al. nonparametric welfare machinery inside a structural model that explicitly separates the opportunity side from the preference side. 

# Relation to Bargain et al. (2013)

This paper is highly relevant to Bargain et al. (2013), but from a different direction. Bargain et al. uses a parametric structural labor-supply model to derive welfare comparisons under heterogeneous preferences, whereas Capéau et al. focuses on the nonparametric identification of welfare levels and welfare changes in discrete-choice settings with unrestricted unobserved heterogeneity. Relative to Bargain et al., this paper is much stronger on methodological robustness in welfare measurement and much weaker on labor-supply structure and institutional detail. For your corpus, the two are complementary: Bargain et al. is closer to the standard structural welfare application, while this paper is closer to a methodological critique and extension of how such welfare analysis should be done. 

# Relation to opportunities vs preferences

This paper does not itself separate preferences from opportunities in the way your agenda requires. It allows very rich preference heterogeneity, but it takes the discrete choice environment as given. Therefore it mainly refines welfare analysis conditional on an underlying model, rather than refining the underlying behavioral model itself. It can help you once you have a model that adequately separates preferences from opportunities, but on its own it risks inheriting any conflation already built into the choice probabilities. 

# Useful quotations / formulas

A central formula is the distributional representation of welfare through transition probabilities:
[
\Pr_\omega!\left[w \leq W^\omega(y-p_k,k),; j = J^\omega(p',y)\right]
=====================================================================

P_{j,k}!\left(p', (p_k,\tilde p_{-k}(w)), y\right)\mathbf{1}[p_k \le \tilde p_k(w)].
]
This is the paper’s key identification device: a welfare statement is translated into a choice statement at virtual prices. 

For MMUs, the relevant object is
[
MMU^\omega_{p^{ref}}(y-p_k,k)
=============================

\max_\lambda \left{\lambda \mid U^\omega_k(y-p_k)\ge \max_c U^\omega_c(\lambda-p^{ref}_c)\right},
]
which generalizes the expenditure-function logic of money-metric utility to the discrete-choice, heterogeneous-preference setting. 

The empirical application’s Figure 7 on page 33 is also especially useful: it shows the reform welfare distribution first-order dominating the baseline welfare distribution for the sample of single females. Figure 8 and Table 1 on page 34 then make the more subtle point that losers still exist and are concentrated among those initially well-off. 

# Suggested tags

#nonparametric #discrete_choice #welfare_measurement #MMU #social_welfare #heterogeneous_preferences #choice_probabilities #transition_probabilities #labor_supply #Germany

# My quick takeaway

If I only remember one thing from this paper for my JMP, what should it be? That discrete-choice welfare analysis does not have to rest on tight parametric preference assumptions: one can recover rich distributions of individual and social welfare from choice behavior itself, but only conditional on an underlying choice environment that may still need much better treatment of opportunities.
