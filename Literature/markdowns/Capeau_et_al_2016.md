---
title: "Estimating and Simulating with a Random Utility Random Opportunity Model of Job Choice: Presentation and Application to Belgium"
authors: [Bart Capéau, André Decoster, Gijs Dekkers]
year: 2016
outlet: "International Journal of Microsimulation, 9(2), 144--191"
country_or_context: "Belgium"
population: "Working-age individuals: couples and singles (male and female)"
data_period: "2007 (EU-SILC cross-section)"
shelf: "RURO model / labour supply / job choice / microsimulation / Belgium"
tags: [RURO, random-utility, random-opportunity, Poisson, Fréchet, discrete-choice, labour-supply, job-offers, hours-restrictions, wage-offer-distribution, hours-offer-distribution, opportunity-density, Box-Cox, simulated-likelihood, EUROMOD, microsimulation, Belgium, EU-SILC, education-simulation, preferences-vs-opportunities]
priority: "high"
read_status: "extracted"
---

# Full citation

Capéau, B., Decoster, A., & Dekkers, G. (2016). Estimating and Simulating with a Random Utility Random Opportunity Model of Job Choice: Presentation and Application to Belgium. *International Journal of Microsimulation*, 9(2), 144--191.

# One-sentence contribution

Provides a self-contained exposition and first Belgian application of the RURO (Random Utility Random Opportunity) model of labour supply, estimating preferences, wage offer distributions, hours offer distributions, and job offer intensities separately on EU-SILC 2007 data for couples and singles, and demonstrates the model's ability to decompose the effects of education changes into preference and opportunity channels.

# Why this paper matters

Standard discrete-choice labour supply models (van Soest 1995) assume workers can freely choose any hours-wage combination along their budget constraint. The RURO model (Dagsvik 1994; Aaberge, Colombino, and Strøm 1999) relaxes this by treating labour supply as a choice among latent job offers that arrive via an inhomogeneous Poisson process -- each job is a (wage, hours) package drawn from an offer distribution that varies with individual characteristics. This paper is the first to apply the full RURO framework to Belgium, using EUROMOD for tax-benefit calculations, and to explicitly decompose policy simulation results into preference-driven and opportunity-driven components. It serves as a practical handbook for implementing RURO models in microsimulation contexts.

# Core research question

How can the RURO model be estimated on Belgian data, what are the estimated preference and opportunity parameters, and to what extent do changes in education affect labour supply through the preference channel versus the opportunity channel?

# Economic setting and context

Belgium 2007, a period of relatively stable labour market conditions before the financial crisis. The Belgian tax-benefit system features high marginal tax rates, extensive social transfers (unemployment benefits, social assistance, child benefits, education benefits, housing benefits), and pronounced institutional hours peaks at half-time (~20h), three-quarter time (~30h), and full-time (~38-40h). Female participation rates are substantially below male rates: 78.8% for coupled males vs. 77.5% for coupled females; 80.6% for single males vs. 69.5% for single females.

# Model / theoretical framework

**Total utility** for a job $z$ with wage $w$ and hours $h$:
$$U = V(C(z), T - H(z); \mathbf{x}_V) \cdot \varepsilon(z)$$
where $V$ is systematic utility (deterministic, depends on consumption $C$, leisure $T-H$, and observable characteristics $\mathbf{x}_V$), and $\varepsilon(z)$ is a random taste shifter capturing unobserved job attributes.

**Systematic utility** in $(w,h)$ space:
$$\Psi(w,h) := V(f(w,h;\mathbf{x}_f), T-h; \mathbf{x}_V)$$
where $f(w,h;\mathbf{x}_f)$ is the tax-benefit function mapping gross $(w,h)$ to net disposable income.

**Random opportunities -- inhomogeneous spatial Poisson process:**
- Job offers arrive as points in utility space. The intensity of job offers with utility exceeding $v$ is:
$$\lambda^1(v) = q / v^2$$
where $q$ is the relative intensity of suitable job offers (individual-specific).
- Non-market alternatives have intensity $\lambda^0(v) = 1/v^2$ (normalisation).

**Maximum utility** over all available alternatives follows a Fréchet distribution:
$$\Pr\{\max U \leq x\} = \exp\left[-\frac{\Psi(0,0) + \int\int \Psi(r,t) \cdot q \cdot g_1(r) \cdot g_2(t) \, dr \, dt}{x}\right]$$

**Choice probability** for a job at $(w,h)$:
$$\varphi(w,h) = \frac{\Psi(w,h) \cdot q \cdot g_1(w) \cdot g_2(h)}{\Psi(0,0) + \int\int \Psi(r,t) \cdot q \cdot g_1(r) \cdot g_2(t) \, dr \, dt}$$

**Non-participation probability:**
$$\varphi(0,0) = \frac{\Psi(0,0)}{\Psi(0,0) + \int\int \Psi(r,t) \cdot q \cdot g_1(r) \cdot g_2(t) \, dr \, dt}$$

**Couples extension (Appendix A2):** Both partners draw from independent Poisson processes. The household utility function $\Psi(w_1,h_1,w_2,h_2)$ depends on both spouses' wages and hours. The choice probability denominators include terms $A$, $B$, $C$ for the cases where only partner 1 works, only partner 2 works, and both work, respectively.

# Key objects

- **$\Psi(w,h)$:** Systematic utility -- the deterministic component of utility from a job at $(w,h)$, after applying the tax-benefit function.
- **$q$:** Relative intensity of suitable job offers -- individual-specific, captures the number of available jobs relative to non-market alternatives. Parameterised as $\ln q(\mathbf{x}_{opp}) = \boldsymbol{\eta}'_q \cdot \mathbf{x}_{opp}$.
- **$g_1(w)$:** Wage offer density -- lognormal with covariates (gender, experience, education, region).
- **$g_2(h)$:** Hours offer density -- piecewise uniform with $K=3$ peaks at institutional hours levels (half-time 18.5--20.5h, three-quarter time 29.5--30.5h, full-time 37.5--40.5h), gender-specific.
- **$\varepsilon(z)$:** Random taste shifter -- captures unobserved job attributes; generates the Fréchet distribution of maximum utility.
- **$\varphi(w,h)$:** Choice probability -- the probability that a person is observed at $(w,h)$.

# Data

Belgian EU-SILC 2007, cross-section. Sample selection: individuals aged 18--64, available for the labour market (not sick, in education, disabled, or (pre)retired), not self-employed. Mixed households (only one partner available) excluded. Households with working children still at home excluded.

**Final sample:** 1457 couple households, 571 single females, 449 single males.

**Descriptive statistics (Table 1):**
- Mean age: ~38--41 across groups
- Education: roughly 1/3 low, 1/3 middle, 1/3 high
- Participation: 68.12% single females, 78.84% coupled females, 79.40% coupled males, 93.20% single males
- Conditional hours/week: 35.88 (single F), 39.69 (single M), 32.50 (coupled F), 40.84 (coupled M)
- Mean hourly wage: 14.91 (single F), 15.20 (single M), 14.73 (coupled F), 16.25 (coupled M)
- Disposable income (EUR/month): 1567 (single F), 1588 (single M), 3143 (couples)

**External data:** Group-specific unemployment rates by age $\times$ sex $\times$ education from Eurostat (Table 2), used as exclusion restriction for the $q$-function.

# Identification logic

The RURO model's identification rests on the multiplicative separability of $\Psi$ and the offer density components in the choice probability:

1. **$\Psi(w,h) \cdot g_2(h)$ identified from hours ratios** (eq. 17): For a given wage $w$, the ratio $\varphi(w,h)/\varphi(w,h')$ identifies $\Psi(w,h) \cdot g_2(h) / [\Psi(w,h') \cdot g_2(h')]$.

2. **$g_1(w)$ identified from wage ratios** (eq. 18): For a given $h$, $\varphi(w,h)/\varphi(w',h)$ identifies $g_1(w)/g_1(w')$ up to the ratio $\Psi(w,h)/\Psi(w',h)$ -- but the wage enters $\Psi$ only through the tax-benefit function, so $\Psi$ can be computed once its parameters are known.

3. **$q$ identified from participation** (eq. 19): The ratio $\varphi(w,h)/\varphi(0,0)$ identifies $q \cdot g_1(w) \cdot g_2(h) \cdot \Psi(w,h)/\Psi(0,0)$.

**Critical non-identification result:** $\Psi(w,h)$ and $g_2(h)$ are NOT separately nonparametrically identified -- only their product $\Psi \cdot g_2$ is. This is why the paper imposes parametric functional forms for both.

**Exclusion restriction:** Group-specific unemployment rate enters $q$ (opportunities) but not $\Psi$ (preferences), helping separate the two.

# Estimation / empirical strategy

**Functional forms:**
- **Box-Cox utility (singles):**
$$\ln V = \beta_c \frac{c^{\alpha_c} - 1}{\alpha_c} + (\boldsymbol{\beta}'_h \mathbf{x}_V) \frac{((T-h)/T)^{\alpha_h} - 1}{\alpha_h}$$

- **Box-Cox utility (couples):** Separate consumption and leisure terms for each partner, plus a leisure interaction term $\beta_{h_1 h_2}$.

- **Hours density $g_2(h)$:** Piecewise uniform over 5 intervals: [1, 18.5), [18.5, 20.5], (20.5, 29.5), [29.5, 30.5], (30.5, 37.5), [37.5, 40.5], (40.5, 70]. Three peak parameters $\gamma_2, \gamma_3, \gamma_4$ (relative to base $\gamma_1$), gender-specific.

- **Wage density $g_1(w)$:** Lognormal with mean $\boldsymbol{\mu}'_w \mathbf{x}_w$ and standard deviation $\sigma_w$, gender-specific. Covariates: potential experience, experience$^2$, education dummies, gender.

- **Job offer intensity:** $\ln q(\mathbf{x}_{opp}) = \boldsymbol{\eta}'_q \mathbf{x}_{opp}$ with covariates: region, education, gender, number of children, group-specific unemployment rate.

**Estimation method:** Simulated maximum likelihood. For each individual, $S$ choice sets are sampled from a prior distribution $P(w,h)$ constructed from the empirical hours distribution and a fitted lognormal wage distribution (eq. 26). Each sampled alternative is weighted by the importance sampling ratio. The integral in the denominator of $\varphi$ is approximated by the sample average over $S$ draws.

**Tax-benefit calculations:** EUROMOD version F5.5, computing disposable income for each $(w,h)$ combination in the sampled choice set.

**Model specification (Table 3):** Region, education, age, children, gender enter preferences ($\mathbf{x}_V$). Region, education, gender, children, unemployment rate enter job offers ($\mathbf{x}_{opp}$). Gender, hours peaks enter hours density ($\mathbf{x}_h$). Gender, experience, education enter wages ($\mathbf{x}_w$).

# Treatment of preferences

Preferences are modelled via Box-Cox utility with rich covariate dependence. The leisure preference intensity $\boldsymbol{\beta}'_h \mathbf{x}_V$ depends on age (quadratic in log), children (three age categories), region, and education. Key findings:

- **Males:** Education effect on leisure preference is non-monotone -- both low and high education men have less intense leisure preferences than middle-education men (Figure 2).
- **Females:** Higher-educated women have less intense leisure preferences (steeper indifference curves).
- **Consumption exponent $\alpha_c$:** 0.610 for couples (t=11.96), 0.292 for single males (t=2.38), 0.049 for single females (t=0.33 -- near log utility).
- **Leisure exponents $\alpha_h$:** Large negative values (−8.35 for coupled males, −7.00 for coupled females, −5.44 for single males, −7.69 for single females), indicating strong curvature.
- **MRS** between consumption and leisure time: given by eq. (27) for singles, eq. (28) for couples.

# Treatment of opportunities / constraints

This is the distinctive feature of the RURO framework. Opportunities are explicitly modelled through three components:

1. **Wage offer distribution $g_1(w)$:** Lognormal, shifts right with education and experience (Figure 3). Higher education has two countervailing effects: direct positive shift and indirect negative through lower potential experience.

2. **Hours offer distribution $g_2(h)$:** Strongly gender-specific (Figure 4). Females receive more part-time and half-time offers; males receive predominantly full-time offers. Peak at 37.5--40.5h is dominant for males ($\gamma_4$ coefficients: 2.690 males, 2.206 females, both highly significant).

3. **Job offer intensity $q$:** Varies by education, region, gender, children, and unemployment rate (Figure 5). For males, a higher unemployment rate *increases* $q$ (coefficient 0.338, t=1.50), a counterintuitive result the authors note. For females, unemployment rate has a small negative effect (−0.072, t=−0.58). Education per se increases $q$, but for males the effect is attenuated by the unemployment rate channel.

**Key empirical pattern:** The impact of education on labour supply runs predominantly through the opportunity channel (wage offers, job intensity) rather than the preference channel (Table 7).

# Welfare / normative object

No welfare analysis is performed. The paper focuses on positive analysis: model fit, elasticities, and education simulation. However, the RURO framework's separate identification of preferences and opportunities is explicitly motivated as a tool for normative analysis: "it provides a tool to throw some light on the extent to which the impact of such reforms runs through preferences, or rather through the channel of modifying opportunities" (p. 179).

# Main findings

**1. Preferences (Section 5.1, Tables A1--A2, Figure 2):**
- Indifference curves are well-behaved (upward-sloping, convex) for all demographic groups
- Education effect on leisure preferences is non-monotone for males, monotonically decreasing for females
- Consumption exponent near zero for single females (close to log utility), around 0.6 for couples

**2. Opportunities (Section 5.2, Tables A3, Figures 3--5):**
- Wage offer distributions shift right with education and experience, are lognormal
- Hours offer distributions show strong institutional peaks, especially full-time for males
- Job offer intensity increases with education (direct effect) but the unemployment rate channel partly offsets this for males
- Job availability decreases slightly with age for males but not for females

**3. Model fit (Section 6.1, Figures 6--11):**
- Disposable income: well fitted for couples (simulated mean EUR 3070 vs. observed EUR 3143) and singles
- Wage distributions: good fit for females, slightly worse for males (more mass at lower/moderate wages)
- Hours distributions: peaks reasonably fitted; three-quarter time underestimated; non-participation slightly overestimated for couples
- Participation: close to observed for most groups

**4. Elasticities (Section 6.2, Table 4):**
- Total wage elasticity from 10% rightward shift of wage offer distribution:
  - Coupled females: 0.64 (own wage), −0.20 (cross, husband's wage)
  - Coupled males: −0.17 (own wage shift of female dist.), 0.33 (own)
  - Single females: 0.69
  - Single males: 0.46
- Intensive margin smaller than total: 0.22 coupled F, 0.13 coupled M, 0.13 single F, 0.09 single M
- Extensive margin (part in): 3.2% coupled F, 0.5% coupled M, 3.3% single F, 2.9% single M
- Elasticities are "rather large" compared to micro estimates but comparable to macro estimates, which is attributed to the RURO model's incorporation of frictions

**5. Education simulation (Section 7, Tables 5--7):**
- Expected education shifts (from MIDAS dynamic model) have small overall effects on participation and hours
- **Decomposition:** Education effects run predominantly through the opportunity channel (wage offers, job intensity) rather than through preferences
  - "Alt pref" (change education in preferences only, keep opportunities at baseline): almost no effect
  - "Alt opp" (change education in opportunities only, keep preferences at baseline): captures most of the total effect
- For single males: participation increases by 2+ percentage points through the opportunity channel
- For females: effects are smaller and sometimes slightly negative (lower education in counterfactual reduces experience, which offsets higher job intensity)

# Main limitations

- Static model -- no dynamics, no job search, no transitions
- Not a matching/equilibrium model -- frictions are exogenous (Poisson intensity), not endogenised through employer behaviour
- $\Psi(w,h)$ and $g_2(h)$ not separately nonparametrically identified -- the hours offer peaks could reflect preferences rather than offer constraints (footnote 17: "we cannot tell this to be wrong on purely empirical grounds")
- Counterintuitive sign on male unemployment rate in $q$-function (positive, though imprecise)
- Non-participation slightly overestimated
- No welfare analysis despite the framework's natural suitability for it
- Sample excludes self-employed, mixed households, and households with working children at home

# Relevance for my JMP

## possible use for framing
The paper provides a complete, self-contained exposition of the RURO model that can be cited as the methodological reference for RURO implementation in a microsimulation context. The explicit decomposition of education effects into preference and opportunity channels (Table 7) directly demonstrates the $R$ vs. $A$ decomposition that is central to $W(z, R, A; y)$.

## possible use for model design
The functional form choices -- Box-Cox utility, lognormal wage offers, piecewise uniform hours offers with institutional peaks, log-linear $q$-function with unemployment rate exclusion restriction -- provide a template for my own RURO specification. The couples extension (Appendix A2) shows how to handle joint household decisions. The simulated likelihood with importance sampling (eq. 23--26) is the estimation approach I would follow.

## possible use for identification
The identification discussion (Section 3.2) clearly states the non-identification of $\Psi$ and $g_2$ separately, which is the key identification challenge for any RURO model. The use of group-specific unemployment rates as an exclusion restriction for $q$ (entering opportunities but not preferences) provides a strategy that could be replicated with different data.

## possible use for welfare analysis
Although the paper does not compute welfare, its estimated RURO model is precisely the type of structural model from which $W(z, R, A; y)$ welfare metrics could be computed. The separate estimates of $R$ (utility parameters) and $A$ (offer distributions, job intensity) are the inputs needed for computing equivalent income or other Fleurbaey-type welfare measures.

## possible use for comparative application
The education simulation (Section 7) is a concrete policy exercise showing how the RURO model can be used for counterfactual analysis. The decomposition methodology (Table 7: "alt pref" vs. "alt opp") is directly applicable to decomposing welfare effects of any policy reform into preference and opportunity components.

# Research questions this paper inspires

1. The paper finds that education effects on labour supply run mainly through opportunities, not preferences. Does the same hold for tax-benefit reforms? If a tax cut increases labour supply, is it primarily because it changes incentives (preferences channel) or because it changes the set of "worthwhile" jobs (opportunity channel)?

2. The non-identification of $\Psi$ and $g_2$ is a fundamental limitation. Can additional data sources (desired hours, job satisfaction, stated preferences) help separate these? Bloemen (2008) shows that desired hours data can sharpen preference identification in a related framework.

3. The elasticities are larger than typical micro estimates. Is this because the RURO model captures responses that standard models miss (e.g., movements between different types of jobs), or because the functional form assumptions are too flexible?

4. Can the RURO framework be combined with Bhattacharya's (2015) nonparametric welfare identification results? Since jobs in the RURO model are unordered alternatives, Bhattacharya's positive identification result should apply -- but the alternatives are latent, not observed.

# Challenge to this paper

The central identification challenge -- that $\Psi(w,h)$ and $g_2(h)$ are not separately nonparametrically identified -- means that the paper's decomposition of education effects into "preference" and "opportunity" channels depends entirely on the parametric functional forms chosen (Box-Cox utility, piecewise uniform hours density). If the hours offer peaks at 20h, 30h, and 40h could equally well be explained by preference clustering at those hours (as in standard discrete-choice models), then the decomposition in Table 7 may be an artefact of the parameterisation rather than a genuine economic finding. The paper acknowledges this (footnote 17) but does not investigate robustness to alternative specifications. Moreover, the counterintuitive positive coefficient on unemployment rate in the male $q$-function raises questions about whether the exclusion restriction (unemployment rate enters opportunities but not preferences) is valid -- if unemployment reflects labour demand conditions that also affect preferences (e.g., through discouragement effects), the restriction fails.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The paper models labour supply as choice among latent jobs characterised by $(w,h)$ packages, with preferences ($V$) and opportunities ($q, g_1, g_2$) as separate primitives. This maps directly to $R$ (preferences) and $A$ (feasible set of jobs) in $W(z, R, A; y)$.

[Reasonable inference for my project] The education decomposition (Table 7) provides a template for decomposing welfare effects of any policy change into an $R$-channel and an $A$-channel. The finding that education effects run mainly through $A$ suggests that welfare evaluations attributing all labour supply variation to preferences (as in standard models) may be misleading.

[Unclear from paper] Whether the RURO model's estimated preference parameters are "deep" enough to serve as the $R$ in a Fleurbaey-type welfare measure. The multiplicative separability assumption ($U = V \cdot \varepsilon$) imposes that unobserved job attributes scale utility proportionally -- this may not be innocuous for welfare measurement. Also unclear: how robust the preference-opportunity decomposition is to alternative functional forms.

The paper is closest to: **RURO model implementation** and **preference-opportunity decomposition in labour supply**.

# Relation to Bargain et al. (2013)

Bargain et al. (2013) compute Fleurbaey welfare metrics using a standard discrete-choice model (van Soest 1995) that treats hours as ordered alternatives with free choice. Capéau et al. (2016) estimate a RURO model that explicitly models job offer restrictions. The RURO framework could in principle deliver Fleurbaey welfare metrics that account for opportunity heterogeneity ($A$) -- something Bargain et al. cannot do because their model does not distinguish preferences from opportunities. The wage elasticities in Capéau et al. (0.64 for coupled females) are larger than those typically found in standard discrete-choice models, which could affect welfare calculations.

# Relation to opportunities vs preferences

This paper is the most explicit existing demonstration of separating opportunities from preferences in a labour supply model. The education simulation (Table 7) shows:
- "Alt pref" (change preferences only): participation for coupled males goes from 90.87% to 90.94%, hours from 36.35 to 36.27 -- essentially no change
- "Alt opp" (change opportunities only): participation goes to 91.90%, hours to 36.78 -- meaningful increase
- The opportunity channel dominates

This decomposition is exactly the type of exercise that the $W(z, R, A; y)$ framework is designed to enable at the welfare level. The challenge is that the decomposition's credibility depends on the non-identification caveat: $\Psi$ and $g_2$ are jointly identified, so the "preference" and "opportunity" labels rest on the parametric specification.

# Useful quotations / formulas

**Choice probability (eq. 15):**
$$\varphi(w,h) = \frac{\Psi(w,h) \cdot q \cdot g_1(w) \cdot g_2(h)}{\Psi(0,0) + \int\int \Psi(r,t) \cdot q \cdot g_1(r) \cdot g_2(t) \, dr \, dt}$$

**Non-identification (Section 3.2, p. 156):**
"the product $\Psi \cdot g_2$ is identified by (17), but $\Psi$ and $g_2$ separately are not"

**On the decomposition (p. 179):**
"it provides a tool to throw some light on the extent to which the impact of such reforms runs through preferences, or rather through the channel of modifying opportunities"

**On the nature of RURO elasticities (p. 175):**
"the figures reported here are conceptually of a different nature, in that actually obtained wages in the present model are the result of choosing the most attractive job offer according to the persons' preferences. Therefore, a reaction to an exogenous change in that wage cannot be conceived of in the framework we used."

**On limitations (p. 179):**
"The model is essentially static. And it does not provide a complete equilibrium framework. It is not a matching model in which job offers are matched (or not) to suitable candidates. Frictions on the labour market are taken as given."

**Main education result (p. 179):**
"the already small change in labour market participation due to expected changes in education level, run predominantly through the channel of opportunities rather than through preferences."

**Box-Cox utility (eq. 20):**
$$\ln V = \beta_c \frac{c^{\alpha_c} - 1}{\alpha_c} + (\boldsymbol{\beta}'_h \mathbf{x}_V) \frac{((T-h)/T)^{\alpha_h} - 1}{\alpha_h}$$

**Wage offer intensity for males (Table A3):**
$\sigma_M = 0.264$ (t=60.63), constant $= 2.066$ (t=72.00), experience $= 2.297$ (t=9.41), experience$^2 = -3.110$ (t=−5.71)

**Hours peaks, females (Table A3):**
Half-time $\gamma_2 = 1.636$ (t=16.42), three-quarter $\gamma_3 = 1.804$ (t=16.69), full-time $\gamma_4 = 2.206$ (t=31.36)

**Hours peaks, males (Table A3):**
Half-time $\gamma_2 = 0.643$ (t=2.81), three-quarter $\gamma_3 = 0.862$ (t=4.55), full-time $\gamma_4 = 2.690$ (t=45.17)

# Suggested tags

RURO, random-utility, random-opportunity, Poisson-process, Fréchet, discrete-choice, labour-supply, job-offers, hours-restrictions, wage-offer-distribution, hours-offer-distribution, opportunity-density, Box-Cox, simulated-likelihood, EUROMOD, microsimulation, Belgium, EU-SILC, education, preferences-vs-opportunities, decomposition, couples, singles, elasticities

# My quick takeaway

This paper is the practical handbook for RURO estimation. Its key empirical contribution -- that education affects labour supply mainly through opportunities rather than preferences (Table 7) -- is a direct proof-of-concept for the $R$ vs. $A$ decomposition in $W(z, R, A; y)$. The main caveat is that this decomposition rests on parametric assumptions because $\Psi$ and $g_2$ are not separately nonparametrically identified. The functional form choices (Box-Cox utility, lognormal wages, piecewise uniform hours with institutional peaks, log-linear $q$ with unemployment rate exclusion) provide a concrete template for my own implementation. The elasticities (0.64 for coupled females) are larger than standard micro estimates, which the authors attribute to the RURO model capturing job-switching responses that standard models miss. The paper's limitation -- no welfare analysis despite having all the ingredients -- is precisely the gap my JMP would fill.
