---
title: "A Model of Labour Supply with Job Offer Restrictions"
authors: [Hans G. Bloemen]
year: 2000
outlet: "CentER Discussion Paper No. 9239, Tilburg University (October 1992); published in Labour Economics, 7(3), 297--312 (2000)"
country_or_context: "Netherlands"
population: "849 married women"
data_period: "1985 (OSA cross-section)"
shelf: "labour supply / demand-side restrictions / job offers / hours restrictions / discrete hours"
tags: [labour-supply, job-offers, hours-restrictions, demand-side, Poisson, discrete-hours, wage-hours-package, married-women, Netherlands, Hausman-utility, hours-distribution, simulation, involuntary-unemployment]
priority: "medium-high"
read_status: "extracted"
---

# Full citation

Bloemen, H. G. (2000). A Model of Labour Supply with Job Offer Restrictions. *Labour Economics*, 7(3), 297--312. [CentER Discussion Paper No. 9239, Tilburg University, October 1992.]

# One-sentence contribution

Formulates a static labour supply model in which individuals receive a Poisson-distributed random number of job offers -- each consisting of a wage and a discrete hours level drawn from a joint distribution $f(w, h)$ -- and choose the utility-maximising package (or non-participation), finding that the model reproduces empirical hours peaks at 20, 32, and 40 hours but that when the Poisson parameter $\lambda$ is made individual-specific (age, education), the preference parameters become essentially unidentifiable because demand-side restrictions dominate observed behaviour.

# Why this paper matters

This is one of the earliest papers to model labour supply with explicit demand-side job offer restrictions where a job is a wage-hours *package* (not just a wage or just hours). It bridges the gap between the static hours-restrictions literature (Dickens and Lundberg 1985; Tummers and Woittiez 1991; Van Soest, Woittiez and Kapteyn 1990) and dynamic job search models (Mortensen 1986; Bloemen 1992). The key finding -- that once $\lambda$ depends on individual characteristics, preferences cannot be identified separately from offer distributions -- foreshadows the identification challenges addressed by later RURO models (Dagsvik 1994; Dagsvik and Jia 2016) and Beffy et al. (2019).

# Core research question

Can a labour supply model with explicit job offer restrictions (random number of wage-hours packages from a joint offer distribution) reproduce the empirical distribution of working hours, and can preference parameters be separately identified from offer distribution parameters?

# Economic setting and context

Netherlands, 1985. Married women with high non-participation rates (61%). Data from the Organisation for Strategic Labourmarket Research (OSA). Hours distribution shows characteristic peaks at 20, 32, and 40 hours per week. The model is motivated by the recognition that the standard neoclassical model (Heckman 1974, Hausman 1980) assumes free choice of hours, which is inconsistent with observed hours clustering.

# Model / theoretical framework

**Job offers:** An individual receives $n$ job offers, where $n \sim \text{Poisson}(\lambda)$. Each offer is a pair $(w, h)$ drawn from a joint distribution $f(w, h)$.

**Hours distribution:** Discrete, with $m = 15$ categories at $h_l = 4l$, $l = 1, \ldots, 15$ (i.e., 4, 8, 12, ..., 60 hours/week). Probabilities $P(h = h_l) = p_l$ are estimated as free parameters (with some equality restrictions for low-frequency categories).

**Wage distribution:** Log-normal, conditional on hours category:
$$\ln w = x'\eta + v, \quad v \sim N(0, \sigma_v^2) \quad \text{(eq. 2.3--2.4)}$$
where $x$ includes age (log(age/17) and its square) and education dummies. The subindex $l$ indicates possible dependence on $h_l$ (via hours terms in the extended specification).

**Joint offer density:**
$$f(w, h_l) = \frac{1}{\sqrt{2\pi}} \frac{1}{\sigma_v w} \exp\left\{-\frac{1}{2\sigma_v^2}[\ln w - \eta' x_l]^2\right\} p_l \quad \text{(eq. 2.6)}$$

**Utility:** Hausman (1980) specification, linear in income and wage:
$$u(h, y) = -\ln(\gamma - \beta h) - \frac{\beta(h - X\delta - e - \beta y)}{\gamma - \beta h} \quad \text{(eq. 2.8)}$$
where $\beta < 0$, $\gamma > 0$, $y = wh + \mu$ (disposable income), $e \sim N(0, \sigma_e^2)$ is unobserved taste heterogeneity.

**Desired hours** (unconstrained optimum under linear budget):
$$h^* = \beta\mu + \gamma w + X\delta + e \quad \text{(eq. 3.5)}$$
with $h = \max(h^*, 0)$.

**Decision:** Individual compares all $n$ offers, selects the one yielding highest utility, and compares it against reservation utility $u_0 = u(0, \mu)$. Non-participation if $n = 0$ (no offers) or all offers yield $u < u_0$.

**Number of offers (extended model):**
$$\lambda_i = \exp(\theta' z_i) \quad \text{(eq. 3.6)}$$
where $z_i$ includes age, education sector, and education level.

**Hours-dependent wages (extended model):**
$$\ln w = \eta' x + \tau_1 h + \tau_2 h^2 + v \quad \text{(eq. 3.7)}$$
interpreted as capturing the progressive tax system: net wage rate $w = (1 - \tau(h)) w_G$ where $\tau(h)$ is the marginal tax rate.

# Key objects

- **$\lambda$:** Poisson parameter governing the average number of job offers. Basic model: $\lambda = 36.7$ (Table 3.1). With individual characteristics: $\lambda_i = \exp(\theta' z_i)$ (Table 3.3).
- **$p_l$:** Discrete hours offer probabilities. Peaks at $h = 20$ ($p_5 = 0.137$), $h = 32$ ($p_8 = 0.117$), $h = 40$ ($p_{10} = 0.232$) in basic model (Table 3.1).
- **$f(w, h)$:** Joint wage-hours offer density.
- **$\sigma_e$:** Standard deviation of random preference parameter. Basic model: 32.6 (Table 3.1); with individual-specific $\lambda$: 248.7 (Table 3.3) -- essentially flat utility.
- **Desired hours distribution:** The distribution of $h^*$ from unconstrained optimization -- much flatter than empirical distribution, no peaks.

# Data

**Source:** Organisation for Strategic Labourmarket Research (OSA), Netherlands, 1985 cross-section.

**Sample:** 849 married women.

**Key statistics:**
- Non-participation rate: 61.0%
- Hours distribution for workers: peaks at 20h (5.2%), 32h (5.0%), 40h (10.1%)
- Hours grouped into 15 categories of 4 hours each (4, 8, ..., 60)

# Identification logic

The model is identified from the joint variation in observed wage-hours packages and non-participation. The likelihood contribution for a working individual with observed $(w_*, h_{l_*})$ involves:
1. The probability that among $n$ offers, this one yields highest utility
2. The wage density evaluated at $w_*$
3. The hours probability $p_{l_*}$
4. The Poisson probability of drawing $n$ offers
5. Integration over the unobserved preference parameter $e$

The non-working likelihood contribution involves the probability that either $n = 0$ or all $n$ offers are rejected ($\Pr(h = 0 | e, n) = [P(0|e)]^n$, summed over all $n$).

**Identification challenge (key finding):** When $\lambda$ depends on individual characteristics (age, education), the same observables that shift preferences also shift offer arrival rates. The preference parameters $(\beta, \gamma, \delta)$ become poorly identified: $\sigma_e$ explodes from 32.6 to 248.7 (Table 3.3), making the utility function "flat and approximately uniform random" (p. 12). This means the data cannot separately identify demand-side restrictions from preference-driven choices once both are allowed to depend on the same observables.

# Estimation / empirical strategy

**Maximum likelihood estimation.** Three specifications:

1. **Basic model (Table 3.1):** Linear budget constraint, constant $\lambda$, hours-independent wages. 15 hours offer probabilities $p_l$ (with equality restrictions), Poisson $\lambda$, lognormal wage parameters, Hausman utility parameters.

2. **Individual-specific $\lambda$ (Table 3.3):** $\lambda_i = \exp(\theta' z_i)$ with age and education. LR test strongly rejects constant $\lambda$ ($\chi^2 = 83.58$, critical 14.07 at 5%).

3. **Hours-dependent wages (Table 3.5):** $\ln w = \eta'x + \tau_1 h + \tau_2 h^2 + v$. LR test rejects $\tau_1 = \tau_2 = 0$ ($\chi^2 = 16.6$, critical 5.99).

**Simulation experiments:** For each individual, draw $e$, $n$, then $n$ wage-hours pairs. Compare with non-work utility. Repeat 10 times, compare simulated hours frequencies with empirical. Andrews (1988) chi-square test for distributional equivalence.

# Treatment of preferences

Hausman (1980) linear labour supply specification. Preferences are parameterised by $(\beta, \gamma, \delta, \sigma_e)$ with a single unobserved taste parameter $e \sim N(0, \sigma_e^2)$. The key finding is that preference identification is fragile: when demand-side parameters ($\lambda$) are enriched with individual characteristics, preference parameters blow up. The paper concludes: "the parameters of the underlying utility specification cannot be traced down anymore. That is, the utility function becomes a flat and approximately uniform random function" (p. 12). This is an early and stark demonstration of the preference-opportunity identification problem.

# Treatment of opportunities / constraints

The demand side is modelled through two channels:
1. **Number of offers ($\lambda$):** Poisson-distributed, possibly individual-specific. Controls extensive margin (involuntary unemployment when $n = 0$).
2. **Hours offer distribution ($p_l$):** Discrete probabilities determining which hours levels are available. Controls intensive margin (hours restrictions).
3. **Wage offer distribution:** Log-normal, possibly hours-dependent. Controls wage variation across offers.

The model allows for involuntary unemployment (probability $\exp(-\lambda)$ of receiving no offers). Desired participation (0.473--0.527) exceeds observed participation (0.390), suggesting involuntary unemployment of 8--14 percentage points (Table 3.2, 3.4).

# Welfare / normative object

No welfare analysis is performed. The paper is entirely positive: estimating the structural model and testing its fit.

# Main findings

1. **Basic model ($\lambda$ constant):** $\hat{\lambda} = 36.7$ (large but imprecise, s.e. = 32.3). Simulated hours match empirical peaks at 20, 32, 40 hours well (Table 3.2, Figure 3.1). Desired hours distribution is much flatter -- no peaks (Figure 3.2). This confirms that observed hours clustering is driven by offer restrictions, not preferences.

2. **Individual-specific $\lambda$:** LR test strongly rejects constant $\lambda$. Age has negative significant effect on $\lambda$; semi-technical/semi-commercial education has positive effect; higher education has higher $\lambda$ than lower. But utility parameters become unidentifiable ($\sigma_e = 248.7$, Table 3.3). The desired hours distribution becomes nearly uniform (Figure 3.4, last column of Table 3.4 with 45% probability mass above 60 hours).

3. **Hours-dependent wages:** $\tau_1 > 0$ (insignificant), $\tau_2 < 0$ (significant). Consistent with progressive taxation interpretation. Low empirical frequencies above 40 hours are explained by low marginal returns (taxes) rather than low offer probabilities -- offer probabilities for high hours actually increase (Table 3.5 vs. 3.1).

4. **Model fit:** Simulated hours match empirical distribution visually (Figures 3.1, 3.3). But Andrews chi-square test formally rejects all specifications (Table 3.7).

5. **Key negative result:** "if the parameter $\lambda$ is made dependent on relevant individual characteristics, preferences seem to play no role anymore. This may of course be the result of the fact that demand side restrictions play such an important role on the labour market that they fully determine the behaviour of individuals" (p. 9). Alternative explanation: with $\lambda$ individual-specific, "there is simply not enough information in the data set to trace down the underlying preference structure" (p. 9).

# Main limitations

- Discussion paper quality -- relatively brief, no robustness checks beyond three specifications
- Hausman (1980) utility is restrictive and known to be fragile
- Static model: no dynamics, no search over time
- No tax system modelling in basic specification; only reduced-form hours terms in extended specification
- Andrews test rejects all specifications -- model does not formally fit the data
- Poisson parameter $\lambda$ is difficult to interpret in a static model with no time dimension
- Single unobserved taste parameter $e$ -- limited preference heterogeneity
- No covariates in the hours offer distribution $p_l$

# Relevance for my JMP

## possible use for framing
This paper provides an early, clear demonstration of the fundamental identification problem in separating preferences from opportunities: once the number of job offers depends on individual characteristics (the same observables that shift preferences), the utility parameters become unidentifiable. This is exactly the identification challenge that the RURO framework must address, and it motivates the need for exclusion restrictions or structural assumptions that separate $R$ from $A$ in $W(z, R, A; y)$.

## possible use for model design
The paper's model is a direct precursor to the RURO framework: job offers are wage-hours packages $(w, h)$ drawn from a joint distribution, and individuals choose the best available package. The key differences with RURO are: (i) Bloemen uses a discrete hours distribution with free probabilities $p_l$, while RURO uses a continuous density $p(h, w)$; (ii) Bloemen separates the number of offers ($\lambda$) from the offer distribution, while RURO integrates both into a single opportunity measure; (iii) Bloemen uses Hausman utility, while RURO typically uses Box-Cox or other flexible forms.

## possible use for identification
The paper's negative result -- that preferences become flat when $\lambda$ is individual-specific -- is a warning for any model that tries to separate preferences from opportunities using the same observables. In the $W(z, R, A; y)$ framework, this suggests that identifying $R$ separately from $A$ requires either exclusion restrictions (variables that shift $A$ but not $R$, or vice versa) or parametric/structural assumptions that constrain how $R$ and $A$ interact.

## possible use for empirical benchmarks
The hours offer probabilities $p_l$ (Tables 3.1, 3.3, 3.5) provide early estimates of the demand-side hours distribution for Dutch married women. The peaks at 20, 32, and 40 hours can be compared with later estimates from Beffy et al. (2019) for the UK and from RURO models.

# Research questions this paper inspires

1. The paper shows that $\lambda$ individual-specific destroys preference identification. Does the RURO framework, which parameterises the opportunity density $p(h,w)$ differently (as a continuous density rather than a Poisson count times discrete probabilities), avoid this identification failure?

2. Can exclusion restrictions resolve the identification problem? For example, local labour market conditions (unemployment rate, industry composition) might shift $\lambda$ or $p_l$ without shifting preferences. This is the approach taken by Beffy et al. (2019) with budget constraint exclusion restrictions.

3. The paper finds desired participation (47--53%) exceeds observed participation (39%), implying ~8--14% involuntary unemployment among married women. How does this compare with estimates from RURO models and from Beffy et al. (2019)?

4. The hours-dependent wage result (significant $\tau_2 < 0$) is interpreted as tax effects. Could it also reflect employer-side hours premia/penalties? In the RURO framework with a joint $(h, w)$ density, this would be captured by the shape of the offer distribution rather than by a wage equation.

# Challenge to this paper

The paper's key negative result -- that preferences become unidentifiable when $\lambda$ is individual-specific -- may be an artefact of the Hausman utility specification rather than a fundamental identification impossibility. The Hausman utility function has limited flexibility (linear labour supply), and the single random taste parameter $e$ may not provide enough heterogeneity to separately identify preferences from offer rates. More flexible utility specifications (Box-Cox, random coefficients) combined with richer data (panel data, desired hours data, institutional variation) might resolve the identification problem. Indeed, later work by Beffy et al. (2019) achieves separate identification of preferences and offer distributions using budget constraint exclusion restrictions -- but with a simpler demand-side structure (two offers) than Bloemen's Poisson model. The fundamental question remains whether the richer Poisson/$\lambda$-individual model can be identified with appropriate instruments.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The paper directly models the demand-side component $A$ of $W(z, R, A; y)$: job offers are wage-hours packages from a distribution $f(w, h)$, and the number of available packages is stochastic (Poisson). The individual's realised bundle $z = (h_*, w_*)$ is the best available offer, not the unconstrained optimum.

[Reasonable inference for my project] The paper's negative identification result is a cautionary tale for the $W(z, R, A; y)$ framework: if $R$ and $A$ cannot be separately identified from observed choices, then the decomposition of well-being into preference-driven and opportunity-driven components is not feasible without additional structure. The RURO model's solution -- using a specific functional form for the opportunity density combined with an extreme value preference error -- is one approach, but the Bloemen result suggests that identification should be formally verified rather than assumed.

[Unclear from paper] Whether the identification failure would persist with richer data (panel, multiple time periods with policy variation) or with the specific functional form assumptions of the RURO model (e.g., the multiplicative structure of the Dagsvik 1994 model where opportunity density enters as a scaling factor in choice probabilities).

The paper is closest to: **early modelling of demand-side job offer restrictions** and **identification challenges in separating preferences from opportunities**.

# Relation to Bargain et al. (2013)

Bargain et al. (2013) estimate preferences using a standard discrete-choice model without demand-side restrictions, assuming free choice among all hours levels. Bloemen (2000) shows that ignoring demand-side restrictions produces a fundamentally different hours distribution (desired hours are flat; observed hours have peaks). If Bargain et al.'s preference estimates absorb some of the demand-side structure (because the model attributes hours clustering to preferences), then their Fleurbaey welfare metrics may be biased. Specifically, the preference parameters that generate peaks at standard hours levels may reflect offer availability rather than genuine taste for those hours.

# Relation to opportunities vs preferences

This paper is centrally about the opportunities-preferences distinction. The key insight is that once both are allowed to depend on the same observables, they become inseparable. The paper demonstrates this empirically: when $\lambda$ is constant, preferences are estimated with reasonable precision; when $\lambda$ varies with age and education, preferences become flat. This is the fundamental identification challenge for the $W(z, R, A; y)$ framework and motivates the need for exclusion restrictions, functional form assumptions, or additional data sources to separately identify $R$ and $A$.

# Useful quotations / formulas

**Joint offer density (eq. 2.6):**
$$f(w, h_l) = \frac{1}{\sqrt{2\pi}} \frac{1}{\sigma_v w} \exp\left\{-\frac{1}{2\sigma_v^2}[\ln w - \eta' x_l]^2\right\} p_l$$

**Likelihood contribution for a worker (eq. 2.17):**
$$l(w_*, h_{l_*} | e) = \lambda \exp\{-\lambda[1 - P(w_*, h_{l_*} | e)]\} k(w_*, \eta' x, \sigma_v) p_{l_*}$$
subject to $u(h_{l_*}, w_* h_{l_*} + \mu) > u_0$.

**On the identification failure (p. 9):**
"if the parameter $\lambda$ is made dependent on relevant individual characteristics, preferences seem to play no role anymore. This may of course be the result of the fact that demand side restrictions play such an important role on the labour market that they fully determine the behaviour of individuals."

**On desired vs. observed hours (p. 9):**
"Although the simulated hours distribution in this type of model fits the labour supply data better than in the neoclassical model, as argued in Van Soest, Woittiez and Kapteyn (1990), this is mainly the result of the discrete specification of the hours offer distribution."

**Desired participation vs. observed (Table 3.2):**
Observed participation: 0.390; Desired participation: 0.473; Simulated: 0.609.
Suggesting ~8% involuntary non-participation.

# Suggested tags

labour-supply, job-offers, hours-restrictions, demand-side, Poisson, discrete-hours, wage-hours-package, married-women, Netherlands, Hausman-utility, identification-failure, preferences-vs-opportunities, involuntary-unemployment, hours-distribution, simulation, offer-distribution

# My quick takeaway

This paper is an important early contribution to modelling demand-side restrictions in labour supply, and its negative identification result is the single most important finding for my JMP's methodology: when both preferences and job offer rates depend on the same individual characteristics, preferences become unidentifiable. The utility function "becomes flat" (σ_e explodes) because the data cannot distinguish whether a woman works 20 hours because she prefers part-time or because that is the only offer she received. This is exactly the $R$-vs-$A$ identification problem in $W(z, R, A; y)$. The RURO framework's solution involves specific functional form assumptions (extreme value errors, multiplicative opportunity density) that constrain how $R$ and $A$ interact -- but Bloemen's result warns that these assumptions are doing heavy lifting and should be carefully scrutinised. The paper also provides early evidence that demand-side restrictions are quantitatively important: desired hours are flat while observed hours peak at 20, 32, 40 -- the peaks are demand-driven, not preference-driven.
