---

title: "Structural Labour Supply Models and Microsimulation"
authors: ["Rolf Aaberge", "Ugo Colombino"]
year: 2018
outlet: "International Journal of Microsimulation"
country_or_context: "Methodological survey with applications and references spanning Europe and the United States"
population: "Not a single empirical sample; reviews labour supply models for singles, couples, lone mothers, immigrant groups, and other populations studied in the literature"
data_period: "Survey article; discusses studies from earlier decades through 2018 rather than one common dataset"
shelf: "structural_labour_supply_microsimulation_survey"
tags: ["labour supply", "microsimulation", "discrete choice", "RURO", "opportunity sets", "optimal taxation", "welfare evaluation", "structural models", "tax-benefit reforms", "policy simulation"]
priority: "high"
read_status: "extracted"
------------------------

# Full citation

Aaberge, Rolf, and Ugo Colombino. 2018. “Structural Labour Supply Models and Microsimulation.” *International Journal of Microsimulation* 11(1): 162–197. 

# One-sentence contribution

The paper surveys how structural labor supply models—especially discrete choice and random utility–random opportunities models—can be embedded in microsimulation for tax-benefit reform analysis, welfare evaluation, and empirical optimal taxation. 

# Why this paper matters

This paper matters because it is not just a generic review of labor supply estimation; it is a structured methodological map of how labor supply models are used in behavioral microsimulation and how that link affects policy analysis, welfare evaluation, and optimal tax design. It is especially valuable because it treats the modeling of opportunities, not only preferences, as central to simulation credibility. 

For your potential JMP, this is a very important orientation paper. It explicitly distinguishes the discrete choice model from the RURO model, explains why opportunity sets matter, discusses how welfare evaluation becomes problematic under heterogeneous preferences, and shows how these issues feed directly into tax-benefit simulation and optimal-tax design. 

# Core research question

How should labor supply responses be modeled and used in microsimulation when the goal is to evaluate tax-benefit reforms, welfare changes, and socially optimal tax systems under heterogeneous preferences and heterogeneous opportunities? 

# Economic setting and context

The paper is a methodological survey rather than an application to one country or one reform. Its context is the development of behavioral microsimulation for tax-benefit analysis, with repeated reference to work from Norway, Sweden, Italy, the UK, Germany, the US, and broader European cross-country settings. 

The institutional setting throughout is tax-benefit policy analysis. The paper is motivated by the increasing policy interest in reforms whose effects depend on nonlinear and non-convex budget sets, heterogeneous preferences, and heterogeneous opportunities. It also places labor supply models within a larger microsimulation tradition originating with Orcutt, but emphasizes that the actual take-off of behavioral microsimulation came later and was tightly linked to tax-benefit reform analysis. 

# Model / theoretical framework

The paper is a survey of model classes, not a single estimated model. The two main frameworks are the discrete choice labor supply model and the random utility–random opportunities (RURO) model. It also discusses dynamic programming models, non-unitary household models, and the taxable-income approach as important related strands. 

The discrete choice model represents the budget set by a finite set of discrete alternatives, usually indexed by hours of work. Utility is written as (v(f(wh,I),h)+\varepsilon), where the random term is often given either a random-utility interpretation or an optimization-error interpretation. In this approach, the opportunity set is typically fixed and imputed by the analyst. 

The RURO model is more directly opportunity-sensitive. Utility is stochastic from the outset and households choose among opportunities or jobs defined by wages, hours, and other characteristics. The analyst does not know the exact opportunity set, so the choice environment is represented through an opportunity density (p(w,h)) or (p(w,h,s)). This makes the model explicitly about both preferences and opportunities. 

The framework is both positive and normative in the survey’s overall scope. On the positive side, it studies structural labor supply behavior. On the normative side, it discusses welfare evaluation, social welfare functions, and computational optimal taxation based on these labor supply models. 

# Key objects

The paper’s main objects are utility functions over disposable income and leisure, labor supply choices at extensive and intensive margins, job opportunity sets or densities, wage and hours distributions, and labor supply elasticities. In the microsimulation context, these objects are used to generate predicted post-reform choices and distributions. 

A second central set of objects is normative: common utility functions for interpersonal comparability, preference-respecting welfare metrics, primal and dual social welfare functions, inequality indices, and computational optimal tax rules. The paper explicitly connects individual welfare measurement to social evaluation of reform outcomes. 

A third key object is the tax-transfer rule itself. In the optimal-tax section, the policy object is a tax-benefit function parameterized for computational search, rather than a closed-form analytical solution. 

# Data

This is not a primary empirical paper with one dataset. It is a review article that synthesizes empirical and methodological literature. It discusses, among others, Norwegian studies from 1979, 1986, 1994, 2006, and 2011; Swedish and Italian applications; harmonized Europe–US cross-country work; and policy simulations for the UK, Germany, and other countries. 

Because the article is a survey, there is no single sample restriction, no single dependent variable, and no single data structure. Instead, it summarizes how different structural labor supply studies use survey, administrative, or harmonized tax-benefit microdata within microsimulation settings. 

# Identification logic

The paper’s identification contribution is conceptual rather than tied to one design. It argues that ex ante policy evaluation requires structural, policy-invariant parameters and that data alone—whether observational, experimental, or quasi-experimental—are insufficient unless embedded in a structural model. This is a very explicit Marschak/Lucas-style defense of structural modeling. 

For discrete choice and RURO models, identification comes from the structural relationship between preferences, budget constraints, and choice opportunities. In RURO especially, the paper stresses that the analyst must separately model opportunity densities rather than forcing all observed heterogeneity into preferences. 

The paper also argues that model evaluation should place substantial weight on out-of-sample prediction and external validation rather than on in-sample fit alone. It reports that available out-of-sample evidence is limited but broadly reassuring, and that flexible a-theoretical models may fit in-sample better but perform worse out of sample. 

# Estimation / empirical strategy

Because this is a survey, it does not estimate one model itself. Instead, it presents the main estimation logics behind the discrete choice and RURO traditions. In the discrete choice model, the usual result is a multinomial/conditional logit probability of choosing an hours alternative, sometimes refined with dummies or fixed-cost terms to improve fit. 

In the RURO model, estimation is based on a choice density where systematic utility is weighted by the density of available opportunities. The paper presents both continuous and discrete versions, as well as sampled-alternative methods that reweight probabilities when the opportunity set is simulated rather than fully observed. 

For policy simulation, the paper distinguishes two main procedures: computing expected choices from estimated choice probabilities, or simulating full alternative-specific utilities and selecting the utility-maximizing alternative under each policy regime. It emphasizes that the simulated pre-reform system should also be used as the baseline for comparison. 

# Treatment of preferences

Preferences are central throughout the paper, but the treatment differs by framework. In the discrete choice model, the literature often focuses on flexible deterministic utility specifications and may treat the random term as optimization error rather than as part of true utility. The survey suggests that, in practice, this approach often treats (v(f(wh,I),h)) as the true preference object and (\varepsilon) as noise. 

In RURO, preferences are also central, but they are not the only driver of behavior. Utility is stochastic and job-specific, and the paper emphasizes that choices reflect both utility and the availability of opportunities. This is a more balanced treatment of preferences and constraints. 

On the normative side, the paper is explicit that heterogeneous estimated utilities are not automatically suitable for interpersonal welfare comparison. It therefore reviews common-utility approaches and also discusses alternative preference-respecting welfare metrics associated with Fleurbaey, Maniquet, Piacquadio, Bargain et al., and Decoster–Haan. 

# Treatment of opportunities / constraints

This section is crucial for your agenda, and the paper is unusually helpful here.

The paper sharply distinguishes the discrete choice model from the RURO model in terms of opportunities. In the standard discrete choice model, the opportunity set is usually fixed by the analyst and given to every household in a mechanically similar way. This means opportunities are present, but often in a highly stylized and weakly individualized form. 

In RURO, opportunities are first-class objects. Households choose among jobs defined by hours, wages, and possibly other characteristics, and the analyst represents the opportunity set via an opportunity density. The number and type of jobs matter. This makes labor supply depend on both preferences and the distribution of available jobs. 

The paper is also clear that opportunity modeling matters for unemployment, underemployment, and constrained choices. It discusses involuntary unemployment as possibly arising from unattractive or sparse opportunity sets and treats this as conceptually distinct from pure taste heterogeneity. 

Relative to your research interests, this is one of the paper’s strongest contributions: it explicitly argues that structural policy analysis in labor supply requires modeling opportunities, not only preferences, and it treats RURO as especially suitable for that purpose. 

# Welfare / normative object

The paper is not itself a welfare application, but it devotes a substantial section to welfare evaluation. It reviews common-utility approaches, preference-respecting welfare metrics, and social welfare aggregation through both primal and dual approaches. 

A key normative object is the common utility function used to evaluate bundles generated by heterogeneous actual preferences. The paper explains this as a device for interpersonal comparability, distinct from the actual utility functions that generate behavior. It also reviews preference-respecting alternatives but warns that the choice of welfare metric can materially affect results, depending on how willingness-to-work is valued. 

The paper is therefore both positive and explicitly normative. It does not merely mention welfare as an afterthought; it treats welfare evaluation and optimal income taxation as core extensions of structural labor supply microsimulation. 

# Main findings

First, the paper argues that ex ante policy evaluation requires structural models. This is one of its clearest methodological positions: reduced-form evidence, however useful, is not sufficient by itself for general policy simulation. 

Second, it identifies discrete choice and RURO as the two main labor supply approaches for microsimulation, but treats RURO as more satisfactory when heterogeneous opportunities and richer job choice are important. 

Third, it argues that the treatment of opportunities can materially affect policy simulation. Opportunity densities, sampled choice sets, and equilibrium feedbacks are not minor details but part of the economic content of the model. 

Fourth, the paper emphasizes that labor supply elasticities have changed over time and that modern elasticities are lower than in earlier decades, especially because of changing participation patterns and income effects. It uses Norwegian evidence and refers to broader Europe–US work to support this point. 

Fifth, it argues that computational optimal-tax methods based on structural microsimulation can generate qualitatively different results from standard theory-based formula exercises, in part because they allow more realistic preferences, opportunity sets, couples, and nonlinearities. 

Sixth, the paper presents microsimulation as especially useful for exploring alternative social welfare criteria and for comparing policies such as in-work benefits, basic income variants, flat taxes, and optimal tax schedules. 

# Main limitations

The main limitation is that this is a survey article, not a single empirical contribution. It organizes and interprets a literature rather than estimating one new model or delivering one new dataset-based identification result. That makes it highly valuable for framing and method selection, but less useful as direct empirical evidence on one concrete policy setting. 

A second limitation, relative to your interests, is that the paper is broad rather than deep on any one welfare criterion. It reviews common-utility and preference-respecting approaches, but does not itself resolve the normative tensions between them. 

A third limitation is that the opportunity-set discussion, while very strong conceptually, remains mostly within the wage-hours-job-density framework of RURO. It does not fully move to richer latent-job spaces with occupation, task content, amenities, or formal demand-side matching structures. 

A fourth limitation is that dynamic, non-unitary, and taxable-income approaches are reviewed but not integrated into one unified operational framework. The paper acknowledges the trade-off between realism and tractability. 

# Relevance for my JMP

## possible use for framing

This paper is excellent for framing a JMP at the intersection of structural labor supply, opportunities, welfare, and tax-benefit simulation. It gives you a clear language for saying that credible policy analysis requires a structural approach and that the relevant structure concerns both preferences and opportunities. 

## possible use for model design

It is especially useful for model design because it compares the discrete choice and RURO paradigms directly. If your project aims to move beyond fixed hours menus toward latent jobs or opportunity-sensitive welfare analysis, the RURO discussion provides a direct conceptual bridge. 

## possible use for identification

For identification, the paper is useful as a methodological argument rather than as an empirical design template. It supports the position that policy-invariant primitives are needed for ex ante reform analysis and that out-of-sample predictive performance is a key credibility check. 

## possible use for welfare measurement

This paper is highly useful here because it lays out the tension between common-utility welfare evaluation and preference-respecting welfare metrics. It also explicitly notes that preference-respecting metrics can differ sharply depending on how willingness-to-work is normatively treated. 

## possible use for cross-country comparison

The survey is useful for cross-country work because it repeatedly stresses that labor supply elasticities, participation behavior, and opportunity structures differ across countries and over time. It therefore supports a cautious approach to transporting results across institutional environments. 

# Research questions this paper inspires

How much of the apparent cross-country heterogeneity in labor supply preferences is actually heterogeneity in opportunity densities or job availability?

Can one build a cross-country RURO model with richer latent jobs over wages, hours, and job characteristics, and then use it for welfare comparison beyond GDP?

What welfare metric is most appropriate when one wants simultaneously to respect heterogeneous preferences and to avoid conflating preferences with constrained opportunities?

How sensitive are optimal tax schedules to replacing a fixed discrete-hours choice set with an explicit random-opportunities structure?

Can the common-utility and preference-respecting welfare approaches be reconciled inside one opportunity-sensitive structural labor supply framework? 

# Challenge to this paper

The strongest unresolved issue in the paper is normative rather than econometric. It convincingly argues that opportunities should be modeled explicitly and that structural labor supply microsimulation can handle far richer environments than formula-based theory. But at the welfare stage, it leaves open the most difficult question for your agenda: how to evaluate individuals when both preferences and opportunities differ, without either collapsing preferences into a common utility function or allowing welfare comparisons to depend too strongly on willingness-to-work. 

# Relation to Bargain et al. (2013)

This paper explicitly cites Bargain et al. (2013) as an example of the application of preference-respecting welfare metrics in labor supply analysis, alongside Decoster and Haan (2015). It notes, however, that the results of such welfare analyses can depend significantly on the chosen metric and on how much weight is placed on willingness-to-work. So the relation is close and substantive: Bargain et al. (2013) is treated here as part of the key literature on welfare evaluation under heterogeneous preferences, but also as part of a literature whose normative choices are consequential and contestable. 

# Relation to opportunities vs preferences

This paper strongly supports the idea that one should distinguish preferences from opportunities. That distinction is most explicit in the contrast between the discrete choice model, where opportunity sets are often fixed and stylized, and the RURO model, where opportunity densities are structural objects. For your agenda, the paper is valuable because it treats the conflation of tastes and opportunities as a genuine modeling problem rather than as a minor technical issue. 

# Useful quotations / formulas

The key discrete choice probability is
[
P(h)=\frac{\exp(v(f(wh,I),h))}{\sum_{y=0}^{T}\exp(v(f(wy,I),y))}.
]
This is the benchmark fixed-opportunity-set representation discussed in the survey. 

The central RURO choice density is
[
\varphi(w,h)=
\frac{\exp(v(f(wh,I),h)),p(w,h)}
{\int_{(x,y)\in B}\exp(v(f(xy,I),y)),p(x,y),dx,dy},
]
or its discrete analogue. This is the single most important formula in the paper for your research interests because it makes job availability enter choice probabilities explicitly. 

The paper’s general computational optimal-tax problem is summarized as a social planner choosing policy parameters (\vartheta) to maximize a social welfare function subject to household utility maximization and the public budget constraint. This is the survey’s key bridge between structural labor supply modeling and normative tax design. 

# Suggested tags

#labour_supply #microsimulation #discrete_choice #RURO #opportunity_sets #welfare_evaluation #optimal_taxation #structural_models #choice_set #tax_benefit

# My quick takeaway

If I only remember one thing from this paper for my JMP, it should be this: the decisive methodological divide is not just between structural and reduced-form work, but between models that treat labor supply as choice from a fixed hours menu and models that treat it as choice from heterogeneous opportunities—and that divide matters directly for welfare analysis and optimal policy design. 
