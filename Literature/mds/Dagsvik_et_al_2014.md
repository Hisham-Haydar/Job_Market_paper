---

title: "Theoretical and Practical Arguments for Modeling Labor Supply as a Choice Among Latent Jobs"
authors: ["John K. Dagsvik", "Zhiyang Jia", "Tom Kornstad", "Thor O. Thoresen"]
year: 2014
outlet: "Journal of Economic Surveys"
country_or_context: "Methodological; general labor-supply framework with Norwegian empirical illustrations"
population: "General labor-supply setting; empirical illustrations use married couples in Norway"
data_period: "Model discussion is general; illustrations rely on a Norwegian model estimated on 1997 data with out-of-sample comparisons for 2003 and 2006"
shelf: "latent_jobs_labor_supply_methodology"
tags: ["latent jobs", "labor supply", "random utility", "discrete choice", "job choice", "hours restrictions", "opportunity sets", "Norway", "microsimulation", "structural labor supply"]
priority: "very high"
read_status: "extracted"
------------------------

# Full citation

Dagsvik, John K., Zhiyang Jia, Tom Kornstad, and Thor O. Thoresen. 2014. “Theoretical and Practical Arguments for Modeling Labor Supply as a Choice Among Latent Jobs.” *Journal of Economic Surveys* 28(1): 134–151. 

# One-sentence contribution

The paper argues that labor supply should be modeled as a choice among latent jobs rather than as a pure hours choice, because this allows structural separation between preferences over jobs and restrictions on available job opportunities, while retaining the practical advantages of discrete-choice labor-supply models for policy simulation. 

# Why this paper matters

This paper matters a great deal for your project because it is one of the clearest methodological statements that the standard labor-supply framework is incomplete when it ignores that workers choose among jobs, not directly along a frictionless hours continuum. The authors insist that part-time/full-time peaks and similar patterns are not well treated as mere preferences; they should instead be understood through the structure of available jobs. 

For your research direction, this is a core bridge paper between conventional structural labor-supply estimation and RURO/latent-opportunity thinking. It does not provide a normative well-being theory, but on the positive side it explicitly separates preferences from opportunity restrictions in a way that is unusually close to your (W(z,R,A;y)) agenda. 

# Core research question

Why should labor supply be modeled as a choice among latent jobs rather than as a direct choice of hours under a budget constraint, and what are the theoretical and practical advantages of doing so for structural estimation and policy simulation? 

# Economic setting and context

The paper is primarily methodological. Its main target is the theory and interpretation of static structural labor-supply models. The authors contrast three approaches: the standard continuous textbook model based on marginal calculus, the conventional discrete labor-supply model in the style of van Soest, and their own alternative job-choice model with latent job opportunities. 

The empirical illustrations are Norwegian. The article discusses a married-couples model estimated on 1997 Norwegian data and then used for out-of-sample comparisons for 2003 and 2006. These illustrations are supportive rather than central: the paper’s main contribution is conceptual and methodological, not a country-specific substantive result. 

# Model / theoretical framework

The model class is a structural random-utility labor-supply model in which the primitive choice object is a **job**, not a continuous or discrete hours point. A job is characterized by fixed job-specific hours, a wage, and nonpecuniary attributes. The worker is assumed to choose among latent available jobs and one nonmarket alternative. Utility takes the additive form
[
U(C,h,z)=v(C,h)+\varepsilon(z),
]
where (z) indexes jobs and (\varepsilon(z)) captures the utility of unobserved nonpecuniary job attributes. 

The budget side is standard at the level of income mapping:
[
C=f(hw,I),
]
where (w) is wage, (I) is nonlabor income, and (f(\cdot)) is the tax-benefit transformation from gross to disposable income. But unlike the conventional consumer-theory labor-supply model, observed hours and income are interpreted as outcomes attached to the chosen job. 

The feasible set is therefore not a universal common set of hours points. Instead, the worker faces latent sets (B(h)) of available jobs with hours (h), with cardinality (m(h)). These latent job counts summarize the opportunity side of the model. The probability of choosing hours (h) is then proportional to the representative utility of jobs with hours (h) times the number of such jobs available:
[
\varphi(h)=\frac{\exp(\psi(h))m(h)}{\exp(\psi(0))+\sum_{x\in D}\exp(\psi(x))m(x)}.
]
This is the key formal bridge between preferences and opportunities. 

The framework is positive rather than normative. It is built for structural estimation and policy simulation, not for fairness evaluation or welfare measurement in the axiomatic sense. 

# Key objects

The central preference object is the systematic utility term (v(C,h)), or equivalently (\psi(h)=v(f(hw,I),h)) after substitution of the budget mapping. The random term (\varepsilon(z)) captures job-specific nonpecuniary utility. 

The central opportunity objects are the latent job sets (B(h)), their cardinalities (m(h)), the total number of job opportunities (\theta=\sum_{x\in D}m(x)), and the normalized opportunity distribution (g(h)=m(h)/\theta). The quantity (\theta g(h)) is interpreted as the opportunity measure for jobs with hours (h). 

A third key object is the empirical representation of labor-supply choice probabilities:
[
\varphi(h)=\frac{\exp(\psi(h))g(h)\theta}{\exp(\psi(0))+\theta\sum_{x\in D}\exp(\psi(x))g(x)}.
]
This equation is central because it shows that observed hours are jointly determined by utility and job availability. 

# Data

The paper is not an empirical paper built around one estimation sample, but it does present empirical illustrations from Norway. The model discussed was estimated on Norwegian married-couple data for 1997, and then used to compare predicted and observed distributions for 2003 and 2006. The 2006 illustration is especially tied to a Norwegian tax reform that reduced the maximum marginal tax rate and changed dividend taxation. 

The *charts on article page 145* are informative here. Figure 1 compares predicted and observed annual-hours distributions for married men, while Figure 2 does the same for married women. The female distribution under the job-choice model appears to track the later data better than the naive prediction. Figure 3 on article page 146 compares predicted and observed disposable-income distributions for married couples and shows a reasonably close fit of the model relative to the naive benchmark. 

# Identification logic

Identification is structural and relies on functional-form and distributional assumptions. The paper is explicit that one cannot generally separate the utility term (v(C,h)) from the opportunity term (g(h)) nonparametrically without further restrictions, because they enter the choice probabilities through the sum (\psi(h)+\log g(h)). This is one of the most important identification points in the paper. 

To obtain identification, the authors recommend explicit functional-form assumptions for the utility representation. They emphasize generalized Box-Cox forms and provide theoretical arguments for such choices based on invariance principles. With these assumptions, the job-choice model becomes identified and estimable. 

The paper also notes that if one had data on desired hours, then one could identify preferences more directly. Without such data, identification of preferences versus opportunities depends on the structural restrictions embedded in the model. This means identification is strong but model-dependent, not quasi-experimental. 

# Estimation / empirical strategy

The empirical strategy is maximum-likelihood estimation of a discrete-choice model where the systematic utility function is parameterized and the opportunity measure is represented parsimoniously. A common practical specification is to assume that the opportunity distribution (g(h)) is roughly uniform apart from peaks at part-time and full-time hours. This yields a theoretically grounded interpretation of the dummy-variable practice often used in conventional discrete models. 

The authors stress that the model can be estimated in a way very similar to the modified van Soest-style framework, but with one crucial difference: the extra hours-specific terms now represent opportunity restrictions rather than ad hoc preference shifters. This is a major conceptual advantage, even when empirical fit is similar. 

The paper also discusses random effects and mixed-logit type extensions, especially through stochastic wage equations. These relax the strong IIA implications that follow from the simple iid extreme-value specification. 

# Treatment of preferences

Preferences are modeled explicitly through the deterministic utility term (v(C,h)) and the random nonpecuniary component (\varepsilon(z)). Importantly, the latter is interpreted as utility from unobserved job attributes rather than as pure noise over hours choices. This is a richer conception of preferences than the standard consumption-leisure framework. 

At the same time, the paper is very clear that the observed peaks at full-time and part-time work should not simply be read as preference peaks. The authors argue that treating them as such is structurally ad hoc unless one truly believes workers have discontinuously stronger tastes for those hours levels. Their preferred interpretation is that these peaks reflect institutional or demand-side restrictions in the availability of jobs. 

This means the paper is explicitly anti-reductionist with respect to preferences. Observed labor supply is not interpreted as the direct revelation of tastes over hours alone. 

# Treatment of opportunities / constraints

This is the core section for your project, and the paper is exceptionally relevant here. The whole model is built to represent **latent job opportunities**. Individuals face latent choice sets of jobs; jobs have fixed hours and nonpecuniary attributes; and hours restrictions are interpreted as restrictions on the set of jobs that are available to the worker. This is stated explicitly in the introduction and formalized in Section 3. 

The paper is also explicit about how this differs from the conventional discrete labor-supply model. In the standard discrete model, the worker still effectively chooses from a common finite set of hours points. In the latent-jobs model, the worker chooses among jobs, and the frequency of jobs with a given hours level matters. This is conceptually much closer to a feasible-opportunity-set approach. 

The opportunity side is represented by (m(h)), (g(h)), and (\theta). The paper interprets (\theta) as the total amount of available job opportunities and (g(h)) as the distribution of those opportunities across hours categories. It further discusses how these objects may be viewed as reduced forms of labor-market restrictions and, in related work, as objects linked to matching equilibrium. 

The paper therefore clearly helps distinguish preference heterogeneity from opportunity heterogeneity, though only within a structural-statistical framework. It does not observe actual individual job sets directly, but it makes them explicit latent objects of the model. This is one of the strongest papers in your corpus on that point. 

# Welfare / normative object

The paper is positive, not normative. It uses utility as a behavioral object and discusses welfare effects only in the loose policy-simulation sense common to structural labor-supply work. It does not define a money-metric welfare criterion, a social welfare function, a fairness principle, or an axiomatic well-being measure. 

Its relevance for your welfare project is therefore indirect. It gives a structurally interpretable empirical representation of opportunities and preferences. That is exactly the kind of positive model that could be paired with a separate normative well-being framework. But the normative layer is not developed here. 

The paper does briefly mention welfare effects of policy changes as part of the justification for structural models in general, but this remains generic. It is not a welfare-measurement paper. 

# Main findings

The first main finding is conceptual: the conventional discrete labor-supply model should be reinterpreted and extended as a model of choice among latent jobs, not merely as a practical approximation to a continuous-hours choice problem. This is the main thesis of the paper. 

The second main finding is that the common empirical practice of adding dummy variables for part-time and full-time hours can be given a structural interpretation. In the latent-jobs framework, such terms represent the availability of jobs at those hours levels rather than arbitrary preference peaks. This is a major practical and theoretical contribution. 

The third main finding is that the model offers a convenient platform for policy simulation not only for tax and wage changes, but also for reforms that affect the opportunity distribution of jobs itself. The paper specifically notes that one can simulate reforms that replace part-time positions with full-time positions by changing the opportunity distribution (g(h)). This is something the conventional model cannot interpret cleanly. 

The fourth main finding, based on the Norwegian illustrations, is that the job-choice model performs reasonably well out of sample. The *chart in Figure 2 on article page 145* suggests that for married women the model’s predicted distribution of annual hours tracks the later observed distribution more closely than the naive benchmark. The *chart in Figure 3 on article page 146* shows a reasonably close predicted disposable-income distribution for married couples. 

# Main limitations

The main limitation is that identification of preferences versus opportunities is only partial without strong structural assumptions. The paper is explicit that one cannot nonparametrically separate (v(C,h)) and (g(h)) in general. So although the framework conceptually distinguishes preferences and opportunities, the empirical separation remains model-dependent. 

A second limitation is that the model is still static and partial. It does not model dynamic labor supply, career progression, search, bargaining, or a fully explicit equilibrium determination of job opportunities in the paper itself. The authors mention matching and equilibrium interpretations only in relation to other work. 

A third limitation is normative. The paper gives no ethical theory of how latent opportunities should enter welfare evaluation. So it is highly relevant for the positive modeling of (A)-type objects, but not directly for responsibility, compensation, or reference opportunity sets. 

A fourth limitation is that job characteristics remain latent in the baseline exposition. This is analytically convenient, but for some applications one may want observable occupational, sectoral, or task attributes to enter more explicitly. The paper notes that such sectoral extensions are possible and cites related work. 

# Relevance for my JMP

## possible use for framing

This paper is extremely useful for framing. It gives a strong conceptual argument against interpreting labor supply as pure hours choice and supports the claim that one should think in terms of jobs and opportunity restrictions. That is a very strong opening reference for a project about opportunities versus preferences. 

## possible use for model design

This is the strongest relevance margin. The paper provides a direct template for modeling latent opportunity sets through the distribution of available jobs. It is one of the closest methodological sources to a RURO-style labor-supply/job-choice design. 

## possible use for identification

High relevance. The paper clearly explains what can and cannot be separately identified about preferences and opportunities, and why additional functional-form structure is needed. This is directly useful for your own identification strategy. 

## possible use for welfare measurement

Direct relevance is limited because the paper is not normative. Indirectly, it is highly relevant because any well-being framework that depends on feasible job opportunities needs a credible empirical way to represent those opportunities, and this paper provides exactly that. 

## possible use for decomposition

Moderate relevance in a positive sense. The paper does not decompose welfare inequality, but it does decompose observed labor-supply behavior conceptually into utility and opportunity components. That is a natural precursor to a later normative decomposition into (R), (A), and (y). 

## possible use for comparative application

High relevance. The framework is portable to many countries and institutional settings, especially where hours restrictions and job structure matter. The paper also notes that a version of this approach has been embedded in the model system used by Statistics Norway for policy analysis. 

# Research questions this paper inspires

Can a latent-job model like this be combined with a normative well-being measure (W(z,R,A;y)) so that the estimated opportunity objects (m(h)), (g(h)), and (\theta) become ethically relevant inputs rather than only behavioral shifters?

How robust is the empirical separation of (v(C,h)) and (g(h)) to alternative functional-form assumptions, and what kinds of auxiliary data would best strengthen identification?

Can the latent-job framework be extended from hours restrictions to multidimensional job packages including occupation, task content, job security, and nonpecuniary amenities observed by the analyst?

How would policy prescriptions change if reforms were evaluated not only through changes in the tax schedule (y), but also through changes in the opportunity distribution (g(h))?

Can one define an “aversion to lack of opportunities” concept in a latent-jobs framework analogous to preference heterogeneity over leisure and income?

# Challenge to this paper

The strongest challenge is that the paper argues persuasively for modeling opportunities explicitly, but its own empirical separation of opportunities and preferences remains dependent on strong structural assumptions. So while the conceptual advance is substantial, the empirical content of the distinction is not fully nonparametric or assumption-free. 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper treats labor supply as a choice among latent jobs and explicitly represents the availability of jobs with different hours through opportunity measures such as (m(h)), (g(h)), and (\theta). Preferences and opportunities are therefore separate structural objects in the model. 

[reasonable inference for my project] The mapping into your notation is quite natural. The realized bundle (z) corresponds to the job chosen and its associated disposable income and hours; (R) corresponds to the deterministic and stochastic preference structure over income, hours, and nonpecuniary job attributes; (A) corresponds to the latent set of available jobs, summarized statistically by (B(h)), (m(h)), (g(h)), and (\theta); and (y) corresponds to the wage and tax-benefit mapping entering disposable income through (f(hw,I)). supported by 

[explicit in paper] The paper is strongly about the importance of (A)-type objects on the positive side. It rejects the idea that observed labor supply should be modeled solely as unconstrained preference-based hours choice. 

[unclear from paper] The paper does not say how well-being should normatively depend on (A), does not define a welfare function (W(z,R,A;y)), and does not state axioms such as IIJ, IPIJ, Full Compensation, or Responsibility for Equal Pay. Those questions are outside its scope. 

[reasonable inference for my project] Relative to your framework, this paper is one of the strongest positive-model foundations available. It is especially useful for the empirical side of (A), while leaving open the normative side of how (A) should enter well-being measurement. supported by 

# Relation to Bargain et al. (2013)

This paper is related to the broader structural labor-supply and tax-benefit microsimulation literature that includes Bargain-type contributions, but it addresses a different bottleneck. Rather than focusing on welfare comparison under heterogeneous preferences, it focuses on the opportunity structure underlying labor-supply behavior. In that sense, it is more of a methodological precursor for enriching the positive side of those models than a direct counterpart on the welfare side. 

# Relation to opportunities vs preferences

This paper is directly about the opportunities-versus-preferences distinction. That is its defining contribution. Preferences are represented in utility; opportunities are represented by latent job availability; and observed hours are the result of both, not of either one alone. 

It is especially useful because it explains why conventional discrete models that fit hours peaks by adding dummy variables are structurally ambiguous: they can fit the data, but they do not tell us whether the peaks come from tastes or constraints. The latent-jobs model resolves that ambiguity by giving the hours-specific terms an opportunity interpretation. 

This makes the paper one of the clearest positive-model references in your corpus for separating preference heterogeneity from opportunity heterogeneity, even though the separation remains structurally rather than nonparametrically identified. 

# Useful quotations / formulas

The most important formula is the latent-job choice probability
[
\varphi(h)=\frac{\exp(\psi(h))m(h)}{\exp(\psi(0))+\sum_{x\in D}\exp(\psi(x))m(x)},
]
because it shows directly that the probability of observed hours (h) depends both on utility and on the number of available jobs with those hours. 

The equivalent representation
[
\varphi(h)=\frac{\exp(\psi(h))g(h)\theta}{\exp(\psi(0))+\theta\sum_{x\in D}\exp(\psi(x))g(x)}
]
is also central because it separates the total amount of opportunities (\theta) from their distribution across hours (g(h)). 

The *charts on article page 145* are especially useful visually: Figure 1 compares predicted and observed annual-hours distributions for married men, and Figure 2 does the same for married women, illustrating the out-of-sample performance of the model relative to a naive benchmark. 

# Suggested tags

latent-jobs, job-choice, labor-supply-methodology, opportunity-restrictions, hours-constraints, random-utility, structural-microsimulation, Norway, RURO-precursor

# My quick takeaway

This is one of the most important positive-model papers in your corpus. It does not solve the normative jobs-and-wellbeing problem, but it gives a very strong methodological foundation for treating observed labor supply as the outcome of both preferences and latent opportunities rather than as a direct hours choice. For your JMP, it is a core reference on how to model the (A)-side seriously.
