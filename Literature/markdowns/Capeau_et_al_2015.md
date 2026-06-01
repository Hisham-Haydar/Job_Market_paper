---
title: "Estimating and Simulating with a Random Utility Random Opportunity Model of Job Choice: Presentation and Application to Belgium"
authors: [Bart Capéau, André Decoster, Gijs Dekkers]
year: 2016
outlet: "International Journal of Microsimulation, 9(2), 144--191"
country_or_context: "Belgium"
population: "Belgian private-household population; estimation on couples, single females, single males available for the labour market"
data_period: "EU-SILC 2007"
shelf: "RURO / job choice / latent jobs / opportunity heterogeneity / discrete choice labour supply / microsimulation"
tags: [RURO, random-utility-random-opportunity, job-choice, latent-jobs, opportunity-heterogeneity, discrete-choice-labour-supply, Belgium, microsimulation, wage-offer-distribution, hours-offer-distribution, Box-Cox-utility, Poisson-job-arrival, education, Capeau, Decoster, Dekkers]
priority: "very high"
read_status: "extracted"
---

# Full citation

Capéau, B., Decoster, A., & Dekkers, G. (2016). Estimating and simulating with a random utility random opportunity model of job choice: Presentation and application to Belgium. *International Journal of Microsimulation*, 9(2), 144--191.

# One-sentence contribution

Presents, estimates, and simulates a RURO model of job choice in which observed labour-market behaviour is jointly driven by heterogeneous preferences (Box-Cox utility over consumption and leisure) and heterogeneous stochastic job opportunities (inhomogeneous Poisson arrival of wage-hours packages), using Belgian EU-SILC 2007 data.

# Why this paper matters

This is one of the most directly relevant papers for my JMP because it provides a full empirical implementation of the RURO framework -- the class of models that structurally separates preferences from opportunities in labour supply. Unlike standard discrete-hours models that collapse all behavioural variation into preferences, this paper models job offers as stochastic arrivals with individual-specific intensity and wage-hours distributions. The resulting positive model is the natural empirical platform on which a normative $W(z,R,A;y)$ welfare measure can be built.

# Core research question

How can one estimate and simulate a labour-supply/job-choice model in which heterogeneity in observed choices reflects both preference differences and differences in available job opportunities, and what does such a model imply about education, participation, wages, and hours in Belgium?

# Model / theoretical framework

**Random Utility Random Opportunity (RURO) model.** Individuals choose the best available alternative from a stochastic set of market and non-market options.

**Preference side:** Total utility from alternative $z$:
$$U(C(z), H(z), z; x^V) = V(C(z), T - H(z); x^V) \cdot \varepsilon(z)$$
Systematic part $V$ is Box-Cox in disposable income and leisure (singles):
$$\ln V(c, T-h; x^V) = \beta_c \frac{c^{\alpha_c} - 1}{\alpha_c} + \beta_h' x^V \frac{((T-h)/T)^{\alpha_h} - 1}{\alpha_h}$$
Multiplicative random term $\varepsilon(z)$ captures unobserved nonpecuniary job attributes. Couples: unitary model with spouse-specific leisure terms and interaction.

**Opportunity side:** Jobs arrive via inhomogeneous spatial Poisson process. Three components:
- $q$: relative intensity of market over non-market opportunities (job-offer abundance)
- $g_1(w)$: wage-offer density
- $g_2(h)$: labour-time-offer density (piecemeal-uniform with peaks at part-time, 3/4-time, full-time)

**Choice probability:** Probability of choosing job $(w,h)$:
$$\phi(w,h) = \frac{\Psi(w,h) \cdot q \cdot g_1(w) g_2(h)}{\Psi(0,0) + \int\!\!\int \Psi(r,t) \cdot q \cdot g_1(r) g_2(t) \, dt \, dr}$$
where $\Psi(w,h)$ is the induced utility function over wage-hours packages. This formula shows directly how observed choices are the joint product of attractiveness (preferences) and availability (opportunities).

**Exclusion restriction:** Group-specific unemployment rate enters $q$ but not preferences.

# Key objects

- Induced utility $\Psi(w,h; x^V, x^f)$: preference valuation of a wage-hours package.
- Job-offer intensity $q$: central measure of market opportunity abundance.
- Wage-offer density $g_1(w)$: distribution of offered wages; shifts rightward with education.
- Labour-time-offer density $g_2(h)$: distribution of offered hours regimes; women receive more part-time, fewer full-time offers (Figure 4).
- Non-market alternatives: also stochastic, with own intensity structure (not a single homogeneous "leisure" point).

# Data

Belgian EU-SILC 2007. 6,348 households, 15,493 individuals. Estimation samples: 1,457 couples, 571 single females, 449 single males (labour-market-available, excluding self-employed and mixed households). Disposable income computed via EUROMOD. External type-specific unemployment rates by age, sex, and education proxy job availability.

# Identification logic

**Sequential nonparametric identification (pp. 157--158):**
1. Comparing observationally equivalent workers at different hours but same wage identifies the composite $\Psi(w,h) g_2(h)$.
2. Comparing workers at same hours but different wages identifies $g_1(w)$ (normalised to integrate to one).
3. Comparing workers and nonworkers identifies $q$ after normalising $\Psi(0,0)$.

**Key limitation:** $\Psi(w,h)$ and $g_2(h)$ are NOT separately nonparametrically identified. Resolution: functional form (Box-Cox utility + piecemeal-uniform hours density) and exclusion restriction (unemployment rate enters $q$ only).

# Estimation / empirical strategy

Simulated maximum likelihood. For each individual, sample alternative wage-hours pairs from a prior density $P(w,h)$, always including the observed choice. Likelihood reformulated conditional on sampled choice set. Disposable income computed via EUROMOD for each sampled alternative. Simulation used for fit assessment, elasticities, and education counterfactuals.

# Treatment of preferences

Explicitly modelled via Box-Cox utility with observable heterogeneity ($x^V$) and multiplicative random term. Education affects leisure preference intensity but not monotonically for all groups. For females, higher education reduces relative preference for leisure; for males, both low and high education can imply lower leisure intensity than middle education (Figure 2).

# Treatment of opportunities / constraints

**This is the paper's central contribution.** Opportunities are modelled explicitly as stochastic job arrivals with individual-specific intensity ($q$), wage distribution ($g_1$), and hours distribution ($g_2$). This is NOT a universal-choice-set model: available jobs differ across individuals. Non-market alternatives are also heterogeneous.

Key empirical findings on the opportunity side:
- Education shifts $g_1(w)$ rightward (Figure 3).
- Women receive more part-time and fewer full-time offers than men (Figure 4).
- Net effect of education on job-offer intensity $q$ differs by gender (Figure 5).
- The education counterfactual shows that participation differences between genders operate predominantly through opportunities rather than preferences (p. 179).

The paper helps distinguish both preference heterogeneity and opportunity heterogeneity. However, opportunities remain latent stochastic objects, not directly observed feasible sets $A_i$ in the axiomatic sense.

# Welfare / normative object

Essentially positive. No social welfare function, equivalent income, or fairness principle. The paper estimates a behavioural model and uses it for simulation, not normative evaluation. Its relevance for welfare is indirect but substantial: it provides the empirical structure in which opportunity heterogeneity is not forced into preferences, which is precisely the kind of positive model that could feed a normative $W(z,R,A;y)$ analysis.

# Main findings

1. RURO can be estimated on Belgian data, yielding a meaningful separation between preference intensity, job-offer intensity, and wage-offer distributions.
2. Education shifts wage-offer distribution rightward; education and experience interact on the opportunity side.
3. Education affects job-offer intensity $q$ differently by gender: clearly positive for women, more muted for men.
4. Labour-time-offer distribution has strong peaks at part-time, 3/4-time, and full-time, differing by gender.
5. Model fit is mixed but respectable: female wages and single-female participation fitted well; non-participation overestimated in some groups.
6. Wage-shift elasticities differ across margins: rightward female wage shift raises female labour supply strongly and can reduce male supply within couples.
7. Counterfactual where male education catches up with female: modest aggregate effects, concentrated among men aged 30--45, running predominantly through opportunities rather than preferences.

# Main limitations

- Static, not a full equilibrium framework; frictions taken as given.
- $\Psi(w,h)$ and $g_2(h)$ not separately nonparametrically identified: empirical separation of preferences and hours opportunities depends on functional form.
- Opportunities remain latent stochastic objects, not directly observed or normatively evaluated.
- Unitary couple assumption: no intra-household bargaining.
- Fit issues: overestimates non-participation in some subgroups.
- Not a decomposition paper in the welfare-economics sense: separates channels behaviourally but produces no normative decomposition into $R$, $A$, $y$.

# Relevance for my JMP

## possible use for empirical platform
This is the most directly relevant paper for the empirical side of my JMP. It provides a concrete RURO architecture that can serve as the positive model on which $W(z,R,A;y)$ is built. The mapping is natural: $z$ = realised job; $R$ = systematic + random preferences; $A$ = latent stochastic opportunity set from Poisson arrival; $y$ = gross-to-net mapping via EUROMOD + wage-offer distribution.

## possible use for identification strategy
The sequential identification logic (composite → wage density → opportunity intensity) is directly relevant for my own empirical design. The exclusion restriction (unemployment rate enters $q$ only) is a template.

## possible use for the preference-opportunity decomposition
The education counterfactual showing that participation gaps operate "predominantly through opportunities" motivates the normative question: if opportunity differences drive much of observed labour market inequality, shouldn't welfare measurement and policy account for this?

# Research questions this paper inspires

1. Can $W(z,R,A;y)$ be computed from a RURO model where $A$ is the estimated latent opportunity set, rather than treated as observed or universal?

2. How robust is the preference-opportunity separation to alternative functional forms for $g_2(h)$ and $\Psi(w,h)$?

3. Can the stochastic opportunity intensity $q$ be decomposed into circumstance-attributable and residual components, embedded in a responsibility-sensitive welfare analysis?

# Challenge to this paper

The model's empirical distinction between preferences and opportunities is not fully nonparametric. Because $\Psi(w,h)$ and $g_2(h)$ are not separately identified without functional form, some of what appears as "opportunity" may reflect specification choices. The paper is valuable precisely because it is explicit about this, but the limitation remains. For my JMP, this motivates investigating how sensitive welfare conclusions are to alternative RURO specifications.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] Jobs are packages of wages, hours, and nonpecuniary attributes; availability is individual-specific and stochastic; choices reflect joint preference-opportunity interaction. Directly models the positive ingredients of $W(z,R,A;y)$.

[Reasonable inference for my project] The mapping to my notation: $z$ = realised job; $R$ = Box-Cox utility + random taste; $A$ = latent Poisson opportunity set; $y$ = gross-to-net mapping + $g_1(w)$. Strongly anti-independence-of-$A$ in positive sense.

[Unclear from paper] Does not state or test normative axioms (IIJ, IPIJ, Full Compensation). Does not ask how well-being should normatively depend on $A$; asks how behaviour empirically depends on $A$-like latent opportunities.

# Relation to Bargain et al. (2013)

Not directly related, but complementary. Bargain et al. estimate preferences and compute equivalent incomes under a universal-choice-set assumption. This paper relaxes that assumption by introducing opportunity heterogeneity. Combining the two -- RURO-estimated opportunities with equivalent income welfare evaluation -- is essentially the architecture of my JMP.

# Relation to opportunities vs preferences

This paper is directly about the opportunities-versus-preferences distinction -- that is its central contribution. It argues that standard models confound the two by treating wages as exogenous individual traits and leaving job availability outside the model. RURO makes both explicit and provides a joint rather than one-sided model.

# Useful quotations / formulas

**Choice probability:**
$$\phi(w,h) = \frac{\Psi(w,h) \cdot q \cdot g_1(w) g_2(h)}{\Psi(0,0) + \int\!\!\int \Psi(r,t) \cdot q \cdot g_1(r) g_2(t) \, dt \, dr}$$

**Opportunity intensity:** $\lambda_1(\upsilon) = q / \upsilon^2$, governing the intensity of jobs yielding utility multiplier $\upsilon$.

**Key empirical finding (p. 179):** Education counterfactual effects on participation run "predominantly through opportunities rather than preferences."

# Suggested tags

RURO, random-utility-random-opportunity, job-choice, latent-jobs, opportunity-heterogeneity, discrete-choice-labour-supply, Belgium, microsimulation, wage-offer-distribution, hours-offer-distribution, Box-Cox-utility, Poisson-job-arrival, education, Capeau, Decoster, Dekkers

# My quick takeaway

The closest empirical paper to the positive side of my JMP. It provides a full RURO implementation that structurally separates preferences from opportunities in labour supply, estimated on Belgian data with EUROMOD integration. The key finding -- that participation gaps operate predominantly through opportunities -- directly motivates the normative question my framework addresses: if opportunity differences drive much of labour market inequality, welfare measurement must account for $A$ explicitly rather than absorbing it into preferences. The paper does not itself compute welfare, but it provides the empirical platform on which $W(z,R,A;y)$ can be built.
