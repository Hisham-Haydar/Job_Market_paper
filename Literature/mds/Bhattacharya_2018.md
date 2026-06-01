---

title: "Empirical welfare analysis for discrete choice: Some general results"
authors: ["Debopam Bhattacharya"]
year: 2018
outlet: "Quantitative Economics"
country_or_context: "General methodological framework with an empirical illustration on recreational fishing-mode choice"
population: "Consumers choosing among discrete alternatives; application uses 1,182 individuals choosing among fishing modes in Southern California"
data_period: "[unclear from paper]"
shelf: "welfare_methods_discrete_choice"
tags: ["discrete choice", "welfare analysis", "equivalent variation", "compensating variation", "multiple price changes", "new goods", "quality change", "nonexclusive choice", "nonparametric identification", "program evaluation"]
priority: "high"
read_status: "extracted"
------------------------

# Full citation

Bhattacharya, Debopam. 2018. “Empirical welfare analysis for discrete choice: Some general results.” *Quantitative Economics* 9: 571–615. 

# One-sentence contribution

The paper extends nonparametric welfare analysis for discrete choice beyond single-price changes by deriving identification results for simultaneous price changes, introduction or elimination of alternatives, quality changes, and nonexclusive choices, showing where Hicksian welfare is point-identified and where only bounds are available. 

# Why this paper matters

This paper matters because it moves from the relatively special setting of one-price-at-a-time welfare analysis to the more realistic settings that arise in empirical policy evaluation: multiple prices moving simultaneously, options entering or disappearing, characteristics changing, and choices not being mutually exclusive. It therefore has more direct empirical reach than the 2015 paper. 

For your research, the paper is useful primarily as a methodological reference on welfare measurement under heterogeneous preferences in discrete choice settings. It is not a paper about labour-supply opportunity sets, responsibility, or compensation in the Fleurbaey–Maniquet sense, but it is valuable for clarifying what can be identified from choice probabilities without parametric assumptions on heterogeneity. 

# Core research question

Under unrestricted preference heterogeneity and unrestricted income effects, what welfare objects can be identified from structural choice probabilities in practical multinomial discrete-choice environments involving multiple price changes, elimination or introduction of options, changes in characteristics, and nonexclusive choice? 

# Economic setting and context

The paper is methodological rather than tied to one substantive market. It is motivated by policy-evaluation contexts such as tuition subsidies, health-product subsidies, transportation choices, and similar interventions where discrete choices change because prices, availability, or attributes change. The author explicitly frames the contribution as a way to calculate compensated program effects, cash-equivalents, and deadweight loss, which are often missing in empirical work. 

The empirical illustration uses cross-sectional microdata on fishing-mode choice in Southern California, with 1,182 individuals choosing among beach, pier, private boat, and charter boat fishing modes. The data include the chosen option, prices, catch rates, and individual income. 

# Model / theoretical framework

The model class is nonparametric multinomial discrete choice with unrestricted unobserved heterogeneity. Utilities take the form (U_j(Y-P_j,\eta)) in the core price-change setup, where (\eta) has unknown dimension and unknown distribution. Structural choice probabilities are defined as the population probabilities of each alternative being utility-maximizing at a given price vector and income level. 

The agent chooses among discrete alternatives. In the main setup these alternatives are exclusive. The feasible set is therefore the finite menu of available alternatives together with the price vector they face. In the later extension on nonexclusive choice, the consumer can combine binary options, which induces composite choice possibilities. 

Opportunities or constraints are not modeled explicitly as latent job sets, offer distributions, or socially relevant feasible opportunity sets. The relevant constraint is the budget effect of prices on income available for the numeraire. The framework is positive with welfare applications: positive because it studies identification from choice behavior, and welfare-oriented because the objects of interest are EV, CV, and deadweight loss. It is not an explicitly normative theory of justice, responsibility, or opportunity compensation. 

# Key objects

The key behavioural objects are the structural choice probabilities
[
q_j(p,y)=\int 1!\left{U_j(y-p_j,\eta)\ge \max_{k\ne j} U_k(y-p_k,\eta)\right}, dF_\eta(\eta),
]
or their appropriate extensions with characteristics and nonexclusive choice. These are the objects from which welfare distributions are recovered or bounded. 

The key welfare objects are Hicksian equivalent variation and compensating variation corresponding to economic changes. The paper is very explicit that Hicksian welfare remains well-defined in the settings studied even when Marshallian consumer surplus becomes path-dependent. It also studies compensated program effects and deadweight loss in program-evaluation language. 

A further central object is the distinction between point identification and set identification of welfare distributions. Cases (a) multiple price changes and (b) elimination/introduction of an option yield point identification from choice probabilities, whereas (c) change in characteristics and (d) nonexclusive choice with multiple price changes generally do not. 

# Data

The theoretical results do not require a specific dataset beyond individual-level cross-sectional data on discrete choices, prices, income, and optionally characteristics. The paper discusses implementation through nonparametric or flexible semiparametric estimation of structural choice probabilities. 

The empirical illustration uses a publicly available fishing-choice dataset with 1,182 individuals. The alternatives are beach, pier, private boat, and charter boat fishing. The variables include a choice indicator for each option, price of each alternative, exogenous catch rates, and monthly income. Table 1 reports means, standard deviations, minima, and maxima for these variables. 

# Identification logic

The paper’s identification logic is to derive welfare distributions directly as functionals of structural choice probabilities, rather than to identify preference distributions first and then compute welfare from a parametrically specified utility model. This is the core methodological point. 

For simultaneous changes in multiple prices among exclusive alternatives, Theorem 1 shows that the EV and CV distributions are point-identified from structural choice probabilities under only continuity and strict monotonicity of utility in the numeraire. The paper also proves that Marshallian consumer surplus becomes path-dependent in this setting, so Hicksian welfare is the correct object. 

For elimination of an alternative, the paper formalizes the common heuristic that removing an alternative is analogous to raising its price to infinity, but then shows carefully what follows and where identification may require observation of demand at high prices. If elimination does not affect prices of remaining alternatives, mean EV and mean CV take different integral forms, and only one coincides with the common ad hoc expression used in applied work. 

For quality change, Theorem 2 shows that welfare distributions are not generally identified from structural choice probabilities. Bounds can be constructed, and point identification can be restored under extra structure such as weak separability. For nonexclusive alternatives, single price changes remain tractable, but multiple price changes are not point-identified from choice probabilities. 

# Estimation / empirical strategy

The paper is identification-focused, but it also discusses implementation. The recommended strategy is to estimate structural choice probabilities nonparametrically or with flexible series/sieve methods and then plug them into the derived welfare formulas or bounds. If data are modest in size, parametric approximations to choice probabilities can also be used, but the theoretical contribution is precisely to avoid relying on parametric utility or heterogeneity assumptions. 

In the empirical illustration, the author uses a partially linear specification for each choice probability, with a cubic in own price and income, plus controls for catch rates and competitors’ net-of-price income terms. These are interpreted as approximations to the true nonparametric choice probabilities. The paper then compares the resulting welfare estimates to log-sum estimates based on quasilinear-style assumptions. 

The implementation section also discusses endogeneity. Price endogeneity may be handled through control functions. A notable specific result is that, for a price increase, the EV distribution at realized income is not affected by income endogeneity in the same way as CV, and for a price decrease the roles reverse. This is a useful technical point for applied work. 

# Treatment of preferences

Preferences are completely heterogeneous in the main results. The dimension and distribution of heterogeneity are unrestricted, and the paper does not assume quasilinearity, additive separability, or a parametric random-coefficients structure. This is one of the paper’s principal advantages over log-sum and mixed-logit-style welfare calculations. 

The paper is explicit that its approach “does not require identification of preference distributions.” This means welfare identification is treated as conceptually distinct from fully recovering heterogeneity itself. That is a strong methodological message, and one that aligns with the broader Bhattacharya agenda from the 2015 paper. 

However, when the economic change is a quality change rather than a price change, unrestricted heterogeneity is no longer enough to point-identify welfare distributions from choice probabilities. In that setting, the paper shows the need for additional structure such as weak separability if one wants point identification. 

# Treatment of opportunities / constraints

The paper does not model opportunities explicitly in the sense of individual feasible job sets, latent opportunity densities, or socially relevant availability sets. The choice set is the menu of alternatives under study, and the relevant constraints operate through prices, income, and characteristics. 

It therefore does not treat opportunity heterogeneity in your sense. There is no analogue of an individual-specific feasible set (A_i), no demand-side rationing, no latent jobs, and no distinction between realized choice and unequal access to alternatives as a separate object. The closest notion of “availability” arises in the entry or elimination of an option, but this is still not an opportunity-set analysis in the RURO or jobs-and-wellbeing sense. 

Accordingly, the paper helps distinguish preference heterogeneity from welfare identification, but not preference heterogeneity from opportunity heterogeneity. It is strong on the former and largely silent on the latter. 

# Welfare / normative object

The welfare object is Hicksian money-metric welfare: EV and CV at the individual level, and the associated mean welfare change and deadweight loss at the aggregate level. The paper emphasizes Hicksian welfare because Marshallian consumer surplus becomes path-dependent under multiple simultaneous price changes. 

The paper is positive with welfare applications. It is not explicitly normative in the social-choice sense. It does not specify a social welfare function, does not discuss interpersonal comparability, and does not address responsibility for opportunities or compensation for unequal feasible sets. It is about measuring the private cash-equivalent value of economic changes to individuals. 

The paper is useful for thinking about welfare measurement under heterogeneous preferences and for calculating compensated program effects. It is not useful, except indirectly, for thinking about reference opportunity sets, responsibility for opportunities, or decomposition of inequality into opportunity and preference components. 

# Main findings

The first main finding is that simultaneous price changes of multiple exclusive alternatives admit point identification of EV and CV distributions from structural choice probabilities under very weak assumptions, even though Marshallian consumer surplus becomes path-dependent. This is the central substantive extension beyond Bhattacharya (2015). 

The second main finding is that the welfare effects of introducing or eliminating an alternative can also be characterized from structural choice probabilities. The paper formalizes when the common practice of integrating demand “to infinity” is valid and shows that it corresponds to mean EV, not generally mean CV, and only under specific price conditions for the other alternatives. 

The third main finding is that welfare from quality change is generally only set-identified, not point-identified, unless one imposes further restrictions such as weak separability. Similarly, with nonexclusive alternatives, single price changes are tractable but multiple simultaneous price changes are not point-identified from choice probabilities. 

The empirical illustration shows that the author’s nonparametric or flexible choice-probability-based estimates can differ materially from standard log-sum estimates. In the fishing application, the paper reports opposite income gradients in some cases and large differences in magnitudes. The figures on pages 24–27 visually show these contrasts, and Table 2 reports mean welfare losses and bootstrap confidence intervals at mean income. 

# Main limitations

The main limitation for your project is again the absence of an explicit opportunity-set object. The paper studies prices, menus, and characteristics, but not unequal feasible sets in the labour-market or axiomatic sense. This prevents direct use for your (W(z,R,A;y)) framework if (A) is meant to represent job opportunities or ability sets. 

A second limitation is that the welfare notion remains narrow. EV and CV are exact and important money-metric objects, but they are tied to specific economic changes and do not constitute a general well-being measure. The paper does not address interpersonal welfare comparison or fairness-sensitive evaluation. 

A third limitation is practical support. For elimination of an option, computing some welfare objects nonparametrically may require observing demand at very high prices. The paper itself notes that these prices may not be observed because firms have no incentive to operate where demand is zero, so practical computation may involve lower bounds or parametric extrapolation. 

A fourth limitation is decomposition. The paper is not a decomposition study of welfare inequality into opportunities, preferences, and related factors. It delivers identification results for welfare effects of economic changes, not a decomposition of observed inequality. 

# Relevance for my JMP

## possible use for framing

This paper is useful for framing the welfare-analysis side of your project. It shows that one can speak rigorously about welfare effects in discrete-choice environments under rich heterogeneity without committing to fully parametric random-coefficients models. That is helpful if you want to motivate a welfare layer on top of structural discrete choice. 

## possible use for model design

It is moderately useful for model design insofar as it clarifies which policy changes allow point identification of welfare from structural choice probabilities and which do not. In particular, it suggests that if your empirical framework involves changes that resemble simultaneous price shifts or entry/exit of options, there is more scope for robust welfare analysis than if it mainly involves changes in nonprice attributes. 

## possible use for identification

This is one of the paper’s strongest contributions for your JMP. It gives a clean map of identification regions: point identification for multiple price changes and option entry/exit; set identification for quality change and nonexclusive multiple-price settings; and a further role for weak separability if one wants point identification in quality-change problems. 

## possible use for welfare measurement

It is highly useful for welfare measurement if your target is money-metric welfare in discrete choice. It extends the 2015 results and is closer to realistic policy evaluation. It is much less useful if your target is a broad well-being measure depending on realized bundle, preferences, feasible set, and pay schedule. 

## possible use for decomposition

Directly, it offers little for decomposition of welfare or inequality into opportunities and preferences. Indirectly, it helps by clarifying that welfare identification can be pursued separately from preference-distribution identification, but that is not yet a decomposition result. 

## possible use for comparative application

The framework is general enough to be used comparatively across regions or countries if comparable choice-probability structures can be estimated. But the paper itself does not implement a cross-country or cross-region comparison. Its empirical application is only illustrative. 

# Research questions this paper inspires

How far can Bhattacharya-style welfare identification be extended from consumer-choice settings to labour-supply environments where the relevant alternatives are jobs with wages, hours, and nonpecuniary attributes?

If labour-supply reforms alter both wages and job availability, is there an analogue of the “multiple price change” theorem when the opportunity set itself changes?

Can one derive money-metric welfare bounds for changes in nonpecuniary job characteristics, analogous to the paper’s quality-change bounds, in a jobs-and-wellbeing framework?

What additional structure, analogous to weak separability, would restore point identification of welfare when labour-market reforms change job characteristics rather than only net returns?

Can the distinction between exclusive and nonexclusive discrete choice be used to think about multi-activity labour-market participation, such as combining formal work, informal work, and home production?

# Challenge to this paper

The main challenge is conceptual rather than technical. The paper provides powerful identification results for compensated welfare effects, but it leaves aside the normative question of whether those money-metric effects are the right welfare metric when individuals differ in feasible opportunities rather than only in preferences. In your research domain, that omission is substantial. 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper analyzes welfare effects of economic changes in multinomial discrete choice using EV and CV under unrestricted heterogeneity. Its objects are structural choice probabilities, cash-equivalent welfare changes, and bounds or point-identification results depending on the scenario. 

[reasonable inference for my project] A loose mapping to your notation is that the realized chosen alternative is part of (z), and the heterogeneous utility representation corresponds loosely to (R). The paper’s treatment of prices is closer to a standard consumer budget effect than to your pay schedule (y), and there is no explicit analogue of (A) as a feasible job set or ability set. 

[explicit in paper] The paper does not develop a well-being measure of the form (W(z,R,A;y)), does not state axioms for independence of (A) or (y), and does not analyze responsibility for opportunities or reference opportunity sets. Those concerns are outside its scope. 

[reasonable inference for my project] It is therefore not close to independence of (A), responsibility for opportunities, reference opportunity sets, or laissez-faire evaluation. It is somewhat closer to the decomposition theme only in the narrow sense that it separates welfare identification from preference-distribution identification. Overall, it is best viewed as a methodological welfare-measurement reference that could sit underneath a broader jobs-and-wellbeing framework, but cannot substitute for the opportunity-sensitive normative layer. 

[unclear from paper] Whether its formulas or bounding strategies can be adapted cleanly to a labour-supply setting with latent job opportunities is not worked out in the paper. 

# Relation to Bargain et al. (2013)

[not central].

# Relation to opportunities vs preferences

The paper is much closer to preferences than to opportunities. It is centrally about how welfare can be identified in discrete choice under unrestricted heterogeneity of preferences and income effects. It does not model unequal access to alternatives as an independent source of heterogeneity, except in the trivial menu sense that an option may enter or exit the choice set. 

Its main relevance for your opportunities-versus-preferences agenda is therefore indirect. It shows how far one can go in welfare measurement without having a theory of opportunities, and thus also shows what remains missing if one wants to analyze responsibility or compensation for unequal feasible sets. 

# Useful quotations / formulas

The central methodological message is already in the abstract: the paper covers simultaneous price change of multiple alternatives, introduction/elimination of an option, changes in characteristics, and choice among nonexclusive alternatives; Hicksian welfare remains well-defined, while point identification or set identification depends on the case. 

A core formula is the structural choice probability
[
q_j(p,y)=\int 1{U_j(y-p_j,\eta)\ge \max_{k\neq j}U_k(y-p_k,\eta)}, dF_\eta(\eta),
]
from which welfare distributions are recovered in the identified cases. 

Another important formula is the line-integral expression for Marshallian consumer surplus under multiple price change,
[
CS(L)=-\int_L \sum_{j=1}^J q_j(p,y), dp_j,
]
which the paper shows is path-dependent in general. This is why the Hicksian EV/CV objects are central. 

# Suggested tags

multinomial-choice-welfare, EV, CV, multiple-price-change, new-goods, option-elimination, quality-change, nonexclusive-choice, nonparametric-identification, deadweight-loss

# My quick takeaway

This is a strong methodological follow-up to the 2015 paper and is more useful for applied welfare analysis because it treats policy changes that actually occur in practice. For your JMP, it is valuable as a reference on what welfare can be recovered from discrete-choice probabilities under rich heterogeneity. But it remains a welfare-identification paper, not an opportunity-sensitive labour-supply paper. Its best use in your corpus is as a methodological building block for the welfare side of a broader framework, not as a direct source on feasible job sets, responsibility, or compensation.
