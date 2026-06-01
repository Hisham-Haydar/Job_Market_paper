---

title: "Empirical welfare analysis: when preferences matter"
authors: ["Jean-François Carpantier", "Christelle Sapata"]
year: 2016
outlet: "Social Choice and Welfare"
country_or_context: "United States"
population: "Single adults without children, aged 20–65, not self-employed, retired, or fully in education, working at least 20 hours per week"
data_period: "2004 U.S. micro data from the CNEF"
shelf: "welfare_measurement_responsibility_preferences"
tags: ["egalitarian equivalence", "conditional equality", "Fleurbaey", "heterogeneous preferences", "labor supply", "discrete choice", "responsibility", "compensation", "United States", "empirical welfare analysis"]
priority: "high"
read_status: "extracted"
------------------------

# Full citation

Carpantier, Jean-François, and Christelle Sapata. 2016. “Empirical welfare analysis: when preferences matter.” *Social Choice and Welfare* 46: 521–542. 

# One-sentence contribution

The paper empirically implements Fleurbaey’s conditional equality and egalitarian equivalence criteria in a labor-supply setting, and its main contribution is to move beyond group-level preference heterogeneity by partially recovering individual-specific preferences from discrepancies between predicted and revealed labor-supply choices. 

# Why this paper matters

This paper matters because it sits directly at the intersection of structural labor-supply estimation and responsibility-sensitive welfare theory. Unlike standard structural labor-supply papers that stop at behavioral elasticities or policy simulation, it uses an estimated labor-supply model to construct interpersonal welfare comparisons under heterogeneous preferences. 

For your project, it is especially relevant on the welfare-measurement side. It does not model feasible job sets explicitly, but it is one of the clearer empirical papers showing how a structural labor-supply model can be used to operationalize fairness criteria that distinguish compensation from responsibility and that take preference heterogeneity seriously rather than treating it as a nuisance. 

# Core research question

How do responsibility-sensitive welfare criteria—specifically conditional equality and egalitarian equivalence—rank individuals in a labor-supply setting with heterogeneous preferences, and how much does the identification of the worst-off change when one accounts for individual-specific preferences rather than only socio-demographic group preferences? 

# Economic setting and context

The paper studies U.S. singles without children using a 2004 micro dataset. The substantive setting is not labor-supply policy design as such, but empirical welfare comparison in a consumption-leisure framework where individuals differ in wages, non-labor income, and preferences for leisure. 

The normative context is the theory of fair social orderings developed by Fleurbaey and Maniquet. The paper is explicitly motivated by the tension between compensation for circumstances and neutrality with respect to responsibility factors, and it takes the incompatibility of full compensation and full responsibility as a starting point. Pages 1–3 are especially clear on this point. 

# Model / theoretical framework

The model class is a static structural discrete-choice labor-supply model used as an empirical vehicle for welfare comparison. Individuals choose a bundle ((c,l)) of net income and labor supply by maximizing utility subject to a budget constraint:
[
(c_i,l_i)=\arg\max {v(c,l;z_i)\mid c\le f(I_i,w_i l)}.
]
Here (z_i) captures heterogeneous preferences, (I_i) is non-labor income, (w_i) is the wage, and (f(\cdot)) is the tax-benefit transformation from gross to net income. 

In the estimated model, the individual chooses among discrete hours alternatives, from 20 to 55 hours per week. State-specific utility is
[
v_{ij}=u(c_{ij},l_{ij};z_i)+\varepsilon_{ij},
]
with a deterministic Cox–Box utility component and a stochastic term assumed i.i.d. type-I extreme value, leading to a conditional logit model. The deterministic utility is
[
u(c_{ij},l_{ij};z_i)=\beta_c \frac{c_{ij}^{\alpha_c}-1}{\alpha_c}+\beta_l(z_i)\frac{(1-l_{ij})^{\alpha_l}-1}{\alpha_l},
]
where preference heterogeneity enters through (\beta_l(z_i)). 

The framework is both positive and normative. It is positive because it estimates labor-supply preferences from revealed choices. It is normative because those estimated preferences are then used to implement conditional equality and egalitarian equivalence criteria. There is no explicit feasible job set, no latent job-offer process, and no demand-side model of opportunities. Opportunities enter indirectly through the budget set, especially through wages and non-labor income. 

# Key objects

The main economic objects are the utility function (v(c,l;z_i)), the budget constraint (c\le f(I_i,w_i l)), the taste-shifter vector (z_i), and the discrete hours alternatives. The two sources of welfare in the empirical model are net income and leisure, giving the standard consumption-leisure trade-off. 

The crucial normative objects are the conditional equality criterion and the egalitarian equivalence criterion. Conditional equality fixes a reference responsibility variable—here, a reference preference for leisure—and compares the welfare individuals could achieve under equivalent budget sets. Egalitarian equivalence fixes a reference circumstance—here operationalized through reference wage or reference non-labor income sets—and asks what reference resources are needed for individuals to attain their current welfare given their actual preferences. Pages 4–8 contain the formal definitions, and Figures 2–5 graphically illustrate them. 

A further key object is the paper’s extension for individual preferences. The authors exploit the difference between the model’s group-level optimal choice and the individual’s revealed choice to recover information about the latent utility shocks. Equation (21) and the discussion around Figure 6 on page 12 are central here. 

# Data

The empirical application uses the Cross National Equivalent File for 2005 with information on incomes in 2004. The sample is restricted to U.S. singles without children, aged 20–65, not self-employed, not retired, not fully in education, and working at least 20 hours per week. Individuals with capital income above 10% of labor income are excluded because net capital income cannot be properly computed. The final sample contains 914 individuals. 

Table 1 reports the descriptive statistics. The sample is 46.3% women and 53.7% men. By education, 8.4% have less than high school, 34.7% have high school, and 56.9% have more than high school. The average working week is 41.2 hours, and the average annual net wage is $31,745. Figure 7 on page 14 shows the concentration of hours around standard full-time values. 

# Identification logic

Identification is structural and largely parametric. Preferences are identified from observed hours choices across discrete alternatives, together with wages, non-labor income, and the nonlinear tax function used to generate alternative net-income points. The stochastic utility term is assumed i.i.d. type-I extreme value, which gives the conditional logit choice probabilities. 

The paper’s distinctive identification move is not about causal policy variation but about preference refinement. It exploits the revealed-choice restriction that the chosen alternative must have higher total utility than unchosen alternatives. When the deterministic part fails to predict the actual choice, that discrepancy identifies bounds on differences in latent utility shocks. The authors then numerically compute conditional expectations of these latent differences to refine the estimated individual indifference curves. This is the core logic in Section 4. 

Identification is therefore not weak in the sense of being purely descriptive, but it remains heavily assumption-dependent. The functional form of utility is Cox–Box, hours are discretized, the wage rate is assumed constant across hours, and the stochastic term distribution is fixed. The paper itself does not claim causal identification of preference primitives in a reduced-form sense. 

# Estimation / empirical strategy

The empirical strategy has two stages. First, the authors estimate a static structural discrete-choice labor-supply model by conditional logit. They discretize hours into eight alternatives, construct net incomes for each hours level using the OECD *Taxing Wages 2005* information, and estimate the deterministic utility parameters and leisure taste shifters. 

Second, they use the estimated utility structure to implement the welfare criteria. For conditional equality, they vary the reference preference for leisure. For egalitarian equivalence, they consider three reference sets: zero-wage egalitarian equivalence, minimum-wage egalitarian equivalence, and wage egalitarian equivalence. They then identify the worst-off as the 10% of individuals most legitimate to receive a redistributive transfer and compare classifications across criteria. 

Their methodological extension adds individual preference information by replacing the usual zero expectation of latent utility differences with estimated conditional expectations derived from revealed-choice discrepancies. Figure 6 on page 12 illustrates this refinement graphically. 

# Treatment of preferences

Preferences are central in this paper. The authors explicitly reject the idea that welfare comparison can ignore heterogeneous preferences when welfare is multidimensional. In the estimated utility function, heterogeneity enters through the leisure-preference coefficient (\beta_l(z_i)), with socio-demographic taste shifters based on gender, age, education, and ethnicity. 

The main empirical novelty is that the paper does not stop at group-level preferences. It argues that averaging preferences within socio-demographic groups is too coarse and potentially disrespectful of individual choices. The discrepancy between the group-predicted optimum and the revealed individual choice is used to partially recover individual-specific preferences from the latent stochastic component. This is precisely the paper’s stated contribution on pages 2–3 and 10–12. 

Table 2 shows that, in the preferred specification, age and gender significantly affect the preference for leisure, while education and ethnicity are not robustly significant once the specification is simplified. The authors finally keep a preferred model that relies mainly on age and gender. 

# Treatment of opportunities / constraints

This section is crucial for your framework, and the paper is only partially aligned with it. It does not model opportunities as feasible job sets, latent job offers, hours restrictions imposed by employers, or demand-side rationing. There is no explicit (A)-type opportunity set. 

Instead, “circumstances” enter through the budget set, especially wages and non-labor income. In the egalitarian-equivalence implementation, the wage is explicitly used as a proxy for circumstances, following Bargain et al. (2013) and Decoster and Haan (2015). This is much narrower than an opportunity-set framework. The relevant page is 3, where the authors state that they take the wage as a proxy for circumstances and then define zero-wage, minimum-wage, and wage egalitarian equivalence criteria. 

So the paper helps distinguish preference heterogeneity from budget-set heterogeneity, but not preference heterogeneity from true feasible-set heterogeneity. It is therefore useful for responsibility versus compensation in a labor-supply framework, but much less useful for explicit opportunity-set modeling. 

# Welfare / normative object

The paper is explicitly normative. Its whole purpose is to implement responsibility-sensitive welfare criteria in an empirical setting. The welfare objects are not reduced-form inequality indices but welfare rankings generated by conditional equality and egalitarian equivalence. 

Conditional equality fully respects neutrality with respect to responsibility factors and only partially compensates for circumstances. Egalitarian equivalence fully compensates for the chosen reference circumstances and only partially respects neutrality. The paper is very clear on the ethical trade-off: one cannot simultaneously satisfy full compensation and full responsibility in general, so one must choose a fairness criterion that privileges one principle. Pages 1–3 set out this normative logic explicitly. 

This is directly useful for thinking about responsibility for opportunities and compensation. However, the “opportunities” in this paper are circumstances represented through wages and non-labor income, not actual feasible job opportunities. The paper also does not provide a decomposition of inequality into preferences, opportunities, and other factors in the sense of a Shapley-type or axiomatic decomposition. 

# Main findings

The main empirical finding is that accounting for individual preferences changes the identification of the worst-off in a nontrivial way. The abstract states that up to 18% of the worst-off are no longer categorized as worst-off once the empirical approach accounts for individual preferences. This headline result is confirmed in Section 5.3 and in Figure 9 on page 19. 

A second key result is that the model based only on socio-demographic group variables leaves substantial unexplained choice heterogeneity. The authors report that 57% of individuals made a labor-supply choice different from the one predicted by the group-level optimum. This is exactly the empirical motivation for refining preferences at the individual level. The result is stated at the end of Section 5.2 on page 16. 

For conditional equality, the identification of the worst-off is quite stable when the reference preference for leisure is chosen within a reasonable empirical range. But the classification becomes less stable with extreme reference values. Figure 8 on page 17 illustrates this sensitivity, and Table 3 shows that higher reference preference for leisure shifts the worst-off toward higher-wage, lower-hours individuals. 

For egalitarian equivalence, minimum-wage and wage egalitarian equivalence are very similar, while zero-wage egalitarian equivalence is much more specific. Figure 10 on page 19 shows that minimum-wage and wage egalitarian equivalence identify almost the same worst-off individuals, whereas zero-wage egalitarian equivalence singles out an additional set of individuals. Table 5 on page 20 shows that the zero-wage criterion identifies worst-off individuals with somewhat higher wages and slightly lower working hours than the other egalitarian-equivalence criteria. 

The comparison across criteria in Figure 11 on page 20 shows substantial consistency between conditional equality with a moderate reference preference and the minimum-wage or wage egalitarian-equivalence criteria. The more extreme versions—especially conditional equality with a very high leisure preference and zero-wage egalitarian equivalence—are more distinct. 

# Main limitations

The first limitation is that opportunities are modeled very narrowly. Circumstances are represented through wages and non-labor income, not through feasible job sets, labor-demand constraints, or actual opportunity menus. For your framework, this is a major conceptual limitation. 

A second limitation is that the sample is highly restricted. The paper studies only singles without children who work at least 20 hours per week. It therefore excludes nonworkers, very low-hours workers, households with children, and couples, all of which are central for broader welfare and labor-supply analysis. The restriction is partly data-driven because transfers and net incomes are less well observed outside this sample. 

A third limitation is that the structural model is static and fairly parsimonious. Hours are discretized, the wage is assumed constant across hours, capital income is largely excluded, and the tax schedule is built from OECD tax information rather than a detailed microsimulation model. These are reasonable simplifications for the paper’s purpose but they limit external validity. 

A fourth limitation is that the recovery of individual preferences remains partial and assumption-dependent. The refinement relies on the conditional logit structure and on interpreting discrepancies between predicted and revealed choices as preference-relevant rather than measurement or modeling error. The authors recognize this when discussing what the unexplained part of choices may reflect. 

# Relevance for my JMP

## possible use for framing

This paper is very useful for framing a project that wants to argue that interpersonal welfare comparisons cannot simply rely on outcomes when preferences are heterogeneous. It gives a concrete empirical illustration of how fairness criteria change the identification of the worst-off once preferences are taken seriously. 

## possible use for model design

It is useful for model design if your project needs a structural labor-supply component that feeds into welfare measurement. In particular, it shows one way to use a discrete-choice labor-supply model to infer welfare-relevant preference heterogeneity. It is less useful for modeling job opportunities or feasible sets. 

## possible use for identification

The paper is useful as an example of preference refinement from revealed-choice discrepancies. That is an interesting identification strategy within a random-utility labor-supply model, even if it is not causal identification in the reduced-form sense. 

## possible use for welfare measurement

This is one of its strongest uses for your JMP. The paper directly operationalizes fairness criteria in an empirical setting and shows how the welfare ranking of individuals changes once preference heterogeneity is incorporated more carefully. 

## possible use for decomposition

Limited directly. The paper does not decompose inequality into preferences and opportunities formally. But it does separate group-level versus individual-level preference treatment, and it compares the ranking implications of different normative criteria. 

## possible use for comparative application

Potentially useful, though the paper itself is not cross-country. Since it explicitly builds on Bargain et al. and Decoster–Haan, it can be read as part of a broader empirical welfare-comparison agenda across institutional settings. 

# Research questions this paper inspires

Can one replace the wage proxy for circumstances with an explicit feasible job set (A) and then define an egalitarian-equivalence criterion over (W(z,R,A;y))?

How does the identification of the worst-off change when individual preferences are recovered from a RURO model rather than from a standard discrete-hours labor-supply model?

What ethical interpretation should be given to discrepancies between predicted and revealed choices: true individual preferences, noise, constraints, or incomplete information?

Can one design a responsibility-sensitive welfare criterion that simultaneously distinguishes preferences (R), feasible opportunities (A), and pay schedules (y), rather than collapsing circumstances into the wage alone?

How robust are conditional equality and egalitarian-equivalence rankings to richer tax-benefit modeling, dynamic labor-supply choices, and broader household structures?

# Challenge to this paper

The central challenge is conceptual. The paper argues that preferences matter and that group-level averaging misses important individual variation. That is persuasive. But on the circumstance side it uses the wage as a proxy, which is much less satisfactory. If wages partly reflect effort, preferences, discrimination, job opportunities, or luck, then the ethical interpretation of the resulting egalitarian-equivalence rankings remains contestable. 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper uses a structural labor-supply model to implement responsibility-sensitive welfare criteria in a consumption-leisure space with heterogeneous preferences. Preferences are explicit and are first estimated at the socio-demographic group level, then partially individualized using revealed-choice discrepancies. 

[reasonable inference for my project] In your notation, the realized bundle (z) corresponds fairly closely to the chosen net-income/labor-supply bundle. The preference object (R) is also explicit, and this is the paper’s strongest point of contact with your framework. But (A) is not modeled as a feasible job set. What plays the role of circumstances or opportunities is mainly the budget set, especially wages and non-labor income. 

[unclear from paper] It is unclear how to map the paper’s “circumstances” into a genuine feasible-set object (A). It is also unclear whether the wage should be interpreted as part of (y), part of circumstances, or partly as an outcome of opportunities and preferences together. The paper deliberately does not resolve these distinctions. 

[reasonable inference for my project] In your taxonomy, the paper is closest to responsibility versus compensation, reference-sensitive welfare evaluation, and heterogeneous preferences. It is not a paper about independence of (A), independence of (y), laissez-faire evaluation, or explicit opportunity-set analysis. Its strongest value for your framework is on the (R)-side and on empirical welfare ranking, not on the (A)-side. 

# Relation to Bargain et al. (2013)

This paper is directly related to Bargain et al. (2013). It explicitly positions itself as an extension of the empirical welfare-analysis approach developed by Bargain et al. and by Decoster and Haan. The main difference is that Bargain et al. capture preferences at the socio-demographic group level, whereas Carpantier and Sapata attempt to recover additional individual-specific preference information from discrepancies between group-level predicted choices and revealed individual choices. 

So the relation is not peripheral but central. In substantive terms, the paper’s contribution is to refine the preference side of the Bargain-style welfare exercise, not to change the underlying labor-supply structure or the broad responsibility-sensitive framework. 

# Relation to opportunities vs preferences

This paper is very much about preferences, but only indirectly about opportunities. Its strongest contribution is to show that welfare rankings are sensitive to how one models heterogeneous preferences and that group-level preference proxies may be too coarse. 

On the opportunity side, the paper is much thinner. Circumstances are largely proxied by wages and non-labor income rather than by actual feasible options. So the paper helps you think rigorously about preferences versus compensation, but it does not yet provide the richer opportunities-versus-preferences separation that your (W(z,R,A;y)) project requires. 

# Useful quotations / formulas

The basic behavioral problem is
[
(c_i,l_i)=\arg\max {v(c,l;z_i)\mid c\le f(I_i,w_i l)}.
]
This is the paper’s core structural setup. 

The estimated deterministic utility is
[
u(c_{ij},l_{ij};z_i)=\beta_c \frac{c_{ij}^{\alpha_c}-1}{\alpha_c}+\beta_l(z_i)\frac{(1-l_{ij})^{\alpha_l}-1}{\alpha_l}.
]
This is central because the entire empirical welfare exercise depends on this preference representation. 

The key individual-preference refinement is
[
E(\varepsilon_{ij}-\varepsilon_{ik}\mid \varepsilon_{ij}-\varepsilon_{ik}>u_{ik}-u_{ij}),
]
which the authors compute numerically and then use to improve the individual indifference curve. This is the paper’s main methodological innovation. 

# Suggested tags

empirical-welfare-analysis, conditional-equality, egalitarian-equivalence, Fleurbaey, heterogeneous-preferences, discrete-labor-supply, responsibility-sensitive-welfare, worst-off-identification

# My quick takeaway

This is a very useful paper for the welfare-measurement side of your corpus. Its main contribution is not to model opportunities well, but to show that empirical welfare rankings based on responsibility-sensitive criteria can materially change once one takes individual preferences more seriously than standard group-based approaches do. For your project, it is especially relevant as a bridge from structural labor-supply estimation to fairness-based interpersonal comparison.
