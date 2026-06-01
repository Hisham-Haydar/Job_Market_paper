---
title: "Job Search, Hours Restrictions, and Desired Hours of Work"
authors: [Hans G. Bloemen]
year: 2008
outlet: "Journal of Labor Economics, 26(1), 137--179"
country_or_context: "Netherlands"
population: "Male individuals, unemployed and employed"
data_period: "1985--1989 (Dutch Socio-Economic Panel)"
shelf: "labour supply / job search / hours restrictions / desired hours / identification"
tags: [job-search, hours-restrictions, desired-hours, wage-hours-package, offer-distribution, reservation-wage, unemployment-duration, identification, preferences-vs-opportunities, Netherlands, men, overemployment, policy-simulation, Hausman-utility]
priority: "high"
read_status: "extracted"
---

# Full citation

Bloemen, H. G. (2008). Job Search, Hours Restrictions, and Desired Hours of Work. *Journal of Labor Economics*, 26(1), 137--179.

# One-sentence contribution

Develops a dynamic job search model in which job offers consist of both a wage rate and a discrete hours level drawn from a joint offer distribution, using subjective data on desired working hours to separately identify preferences from the hours offer distribution, and showing that without desired hours data the base model is overparameterised -- preferences appear flat and cannot be distinguished from offer restrictions.

# Why this paper matters

This paper addresses the central identification problem in models with demand-side restrictions: observed working hours reflect both preferences and offer availability, and these cannot be separated using observed hours alone. Bloemen's solution -- using subjective data on desired hours as an additional data source -- is one of the few credible approaches to this identification challenge. The paper provides the dynamic (search-theoretic) counterpart to the static model in Bloemen (2000), adding unemployment duration data and forward-looking behaviour, which substantially enriches both the identification and the policy implications.

# Core research question

Can subjective information on desired working hours be used to separately identify preferences for hours from the hours offer distribution in a structural job search model? How does this separation affect the model's predictions for policy simulations (benefit cuts, changes in standard working week)?

# Economic setting and context

Netherlands, 1985--1989. Male workers and unemployed individuals from the Dutch Socio-Economic Panel (SEP). The Dutch labour market features a strong concentration of hours at 40 hours/week (~67% of workers), with a substantial minority (25.3%) reporting being overemployed (wanting fewer hours) and only 6.1% underemployed. The policy context includes debates about reducing the standard working week and cutting unemployment benefits.

# Model / theoretical framework

**Dynamic job search with hours restrictions:**

Unemployed individuals receive job offers at rate $\lambda(v)$, where $v$ is unobserved heterogeneity in the arrival rate. Each offer is a pair $(w, h)$ from a joint distribution $f(w, h) = f(w) p_l$, where wages are continuous (lognormal) and hours are discrete with $L = 21$ categories (4, 8, ..., 84 hours/week).

**Utility:** Hausman (1980) specification:
$$u(y, h; \epsilon) = -\ln(\gamma - \beta h) - \frac{\beta(h - X\alpha - \epsilon - \beta y)}{\gamma - \beta h}, \quad \beta < 0, \gamma > 0 \quad \text{(eq. 5)}$$

**Optimal (desired) hours:** Linear labour supply function:
$$h^*(w, \mu) = \mu\beta + w\gamma + X\alpha + \epsilon \quad \text{(eq. 6)}$$

**Reservation utility property (Appendix A):** The model has a reservation utility level $\bar{u}(q) = \rho V(q)$ where $V(q)$ is the value of search. All offers $(w, h)$ with utility exceeding $\bar{u}$ are accepted. Equivalently, for each hours level $h_l$, there is a hours-dependent reservation wage $\xi(h_l, \bar{u}(q); \epsilon)$: offers with $w > \xi_l$ are accepted for hours level $l$.

**Key insight:** The reservation wage is U-shaped in hours, reaching its minimum at optimal hours $h^*$. Individuals accept offers with non-optimal hours only if the wage compensates sufficiently.

**Escape rate from unemployment:**
$$\theta(q) = \lambda(v) \sum_{l=1}^{L} p_l \bar{F}(\xi_l(q)) \quad \text{(eq. 4)}$$
where $\bar{F}(\cdot) = 1 - F(\cdot)$ is the survival function of offered wages.

**Three model variants for desired hours:**

1. **Base model:** No desired hours data used. Observed hours = accepted offer hours. Overparameterised -- preferences and offer probabilities are both identified from observed hours alone.

2. **Optimal desired hours model:** Desired hours $\tilde{h}$ linked to optimal hours $h^*$ via: $\ln \tilde{h} = \ln h^* + \nu$, $\nu \sim N(0, \sigma_\nu^2)$ (eq. 7). Imposes a tight link between subjective reports and the model's optimal hours.

3. **Hours satisfaction model (preferred):** Distinguishes "satisfaction" from "optimality." If $|h - h^* - \omega| \leq \bar{c}$, worker reports being satisfied (desired = observed). If $|h - h^* - \omega| > \bar{c}$, worker reports desired hours $\tilde{h} = h^* \exp(\nu)$ (eq. 8). The parameter $\bar{c}$ captures the tolerance band around optimality.

# Key objects

- **$p_l = P(h = h_l)$:** Hours offer probabilities. Peak at 40 hours: $p_{40} = 0.57$ (hours satisfaction model, Table 6). Substantial probability mass also at 48h (0.068), 52h (0.068).
- **$\xi_l(q)$:** Hours-dependent reservation wage. U-shaped in hours, minimum at 36--40 hours (Figure 2).
- **$\bar{c}$:** Satisfaction tolerance parameter. Estimated at 16.3 (s.e. 0.6) in hours satisfaction model (Table 2). Workers tolerate a gap of ~16 hours between actual and optimal before reporting dissatisfaction.
- **$\sigma_\epsilon$:** Variance of random preferences. Base model: 13.9; Optimal desired hours: 8.3; Hours satisfaction: 9.8 (Table 2). Decreases substantially when desired hours data is used.
- **$\sigma_v$:** Variance of unobserved heterogeneity in arrival rate. Base model: 0.26; desired hours models: 0.14 (insignificant) (Table 3).

# Data

**Source:** Dutch Socio-Economic Panel (SEP), Statistics Netherlands, October 1985 to April 1989 (biannual, 3.5 years).

**Samples:**
- **Entire sample:** $n = 5{,}320$ male individuals, younger than 65
- **Employed:** $n = 3{,}962$ with observed hours and wages; 3,216 with desired hours information
- **Unemployment spells:** $n = 573$ (297 ending in employment, 191 with after-spell wage-hours observed, 189 with desired hours)
- **Employment spells:** $n = 4{,}747$ for layoff rate estimation

**Key descriptives (Table 1):**
- Mean observed hours: 40.6 (s.d. 8.7)
- Mean desired hours: 39.0 (s.d. 8.1)
- Mean difference (observed - desired): 1.7 hours
- 68.6% satisfied with current hours; 25.3% overemployed; 6.1% underemployed
- Mean weekly earnings: 535.3 guilders
- Mean unemployment duration: 14.2 months (median 6)

# Identification logic

**Five sets of structural parameters:** (1) utility function, (2) hours offer probabilities $p_l$, (3) wage offer distribution, (4) job offer arrival rate $\lambda(v)$, (5) layoff rate $\delta$.

**Without desired hours (base model):** Arrival rate and layoff rate identified from unemployment duration and job tenure data. Wage distribution from accepted wages (truncated by reservation wage). But **preferences ($\beta, \gamma, \alpha, \sigma_\epsilon$) and offer probabilities ($p_l$) are both identified from observed hours alone** (eq. 15):
$$f(h_l) = \int \frac{p_l \bar{F}(\xi_l(q))}{\sum_{j=1}^{L} p_j \bar{F}(\xi_j(q))} g(q, \Sigma) dq \quad \text{(eq. 15)}$$

This means "changes in offer probabilities and preference parameters both may act to fit the distribution of observed working hours" (p. 149). Identification relies on the nonlinear functional form of the search model, but "a change in the preference parameters accompanied by a suitable change in the offer probabilities may lead to little variation" in observed hours -- the model is practically overparameterised.

**With desired hours:** Desired hours $\tilde{h}$ provide direct information on optimal hours $h^*$, which "pin down" preferences. Given preferences, offer probabilities are then identified from observed hours via eq. (15). The desired hours data thus resolve the identification problem by providing a separate window into preferences.

**Exclusion restriction:** Household characteristics (family size, marital status) enter only utility, not the arrival rate. This helps separate preference effects from arrival rate effects. Age enters both, so its identification "leans on the imposed structure and functional form" in the base model.

# Estimation / empirical strategy

**Simulated maximum likelihood (SSML)** with $R = 30$ replications to handle the two-dimensional integration over unobserved heterogeneity $q = (\epsilon, v)$. Likelihood contributions:
- **Unemployed** (no after-spell info): $f_u(t_u) = \int \theta(q) \exp\{-\theta(q) t_u\} g(q, \Sigma) dq$ (eq. 10)
- **Unemployed with after-spell wage-hours-desired hours:** eq. (11), includes wage density, hours probability, reservation wage condition, and desired hours density
- **Employed:** wage, hours, desired hours, conditional on job tenure; layoff rate from job tenure distribution
- Stock sample observations conditioned on backward recurrence times (Appendix B)

# Treatment of preferences

Hausman (1980) linear labour supply with a single random taste parameter $\epsilon \sim N(0, \sigma_\epsilon^2)$. Individual characteristics ($X$: family size, marital status, age dummies) shift preferences. The key finding is about **identifiability**: without desired hours, preferences appear relatively flat ($\sigma_\epsilon = 13.9$, reservation wage nearly flat in hours); with desired hours, preferences are more sharply identified ($\sigma_\epsilon = 8.3$--$9.8$, reservation wage clearly U-shaped with minimum at 36--40 hours).

The hours satisfaction model makes an important conceptual distinction: "satisfaction" $\neq$ "optimality." Workers may tolerate a gap of $\bar{c} \approx 16$ hours between observed and optimal hours and still report satisfaction. This is more realistic than equating desired hours directly to the model's optimal hours.

# Treatment of opportunities / constraints

Demand-side modelled through:
1. **Job offer arrival rate $\lambda(v)$:** Depends on education, age, region, education sector, and unobserved heterogeneity $v$. Parameterised as $\lambda(v) = \exp(\kappa_u' z_u + v)$.
2. **Hours offer distribution $p_l$:** Discrete probabilities, common across individuals. Strong peak at 40h ($p_{40} = 0.57$ in preferred model). Models with desired hours shift probability mass from below-40 to above-40 hours compared to base model.
3. **Wage offer distribution:** Lognormal, dependent on age, education. Variance $\tau$ and measurement error $\sigma_w$ estimated.
4. **Layoff rate $\delta$:** Depends on age, education, region, sector. Decreases with age; highest for lowest education.

# Welfare / normative object

No formal welfare analysis. Policy simulations assess effects on:
- Distribution of accepted working hours
- Unemployment hazard rate
- Reservation wages

# Main findings

**Identification and model comparison:**
1. **Base model (no desired hours):** Preferences appear flat. Reservation wage as a function of hours is nearly flat for a working week of 40+ hours (Figure 2, dash-dot line). Optimal hours implied at 48--60 hours -- implying underemployment, which contradicts the survey evidence (25.3% overemployed, only 6.1% underemployed). The base model fits observed hours best ($\chi^2 = 17.9$, $p = 0.21$) but **only because it is overparameterised** -- preferences absorb offer distribution features.

2. **Models with desired hours:** Preferences sharply identified. Reservation wage clearly U-shaped with minimum at 36--40 hours (Figure 2). Models correctly predict overemployment. But formal goodness-of-fit rejected ($\chi^2 = 264$ and 225) because the parametric model constrains the hours distribution at the individual level.

3. **Hours satisfaction model (preferred):** $\bar{c} = 16.3$ -- workers tolerate substantial hours deviations before reporting dissatisfaction. Predicted desired hours peak at 40h with 41.5% probability (Table 8), capturing the observed peak. Predicts overemployment correctly.

**Hours offer distribution (Table 6):**
- Base model: higher probabilities below 40h ($p_{20} = 0.067$, $p_{32} = 0.034$, $p_{40} = 0.55$)
- Hours satisfaction model: higher probabilities above 40h ($p_{48} = 0.068$, $p_{52} = 0.068$, $p_{40} = 0.57$). The models with desired hours assign more mass above 40h because preferences now explain why few people work those hours (they don't want to), freeing the offer distribution to show that such jobs are actually available.

**Policy simulations (hours satisfaction model):**

4. **5% benefit cut (Table 10):** Small impact on accepted hours distribution. Full-time (40h) frequency drops by 1.3pp, part-time (20h) increases by 0.5pp. Lower benefits make part-time jobs (with lower weekly income) relatively more acceptable.

5. **Shorter standard working week (40h→36h, Table 11):** Shifting offer probability from 40h to 36h reduces part-time work by ~0.7pp at 20h -- part-time preferring workers find 36h more acceptable and switch to full-time. Unemployment hazard increases by 2.2%.

6. **Offer distribution = desired hours distribution:** If offers matched desires, unemployment hazard increases by 1.3%, but the increase is smaller than the working-week reduction because increased selectivity partially offsets the better match.

**Benefit elasticity of unemployment duration:** 0.35 (base model), 0.35 (optimal desired hours), 0.50 (hours satisfaction). The hours satisfaction model shows higher sensitivity because individuals are more willing to accept non-optimal hours jobs, making unemployment duration more responsive to benefit changes.

# Main limitations

- Hausman (1980) utility is restrictive (linear labour supply)
- Linear budget constraint -- taxes ignored (acknowledged, p. 141 fn. 10)
- Stationary model: no duration dependence in hazard (residual analysis reveals neglected negative duration dependence, Figure 3)
- Hours offer distribution assumed common across individuals (no variation by education, region, etc.)
- "Satisfaction" tolerance parameter $\bar{c}$ is constant across individuals
- Male workers only; female labour supply with higher part-time rates would be more informative
- Formal goodness-of-fit test rejected for models with desired hours
- No general equilibrium effects in policy simulations

# Relevance for my JMP

## possible use for framing
This paper provides the clearest empirical demonstration that subjective data (desired hours) is essential for separately identifying preferences from opportunity restrictions in labour supply models. The "overparameterisation paradox" -- the base model fits observed hours best but gets preferences wrong -- is a powerful cautionary tale for the $W(z, R, A; y)$ framework: fitting observed outcomes well does not mean that the model correctly identifies the underlying $R$ and $A$ components.

## possible use for model design
The hours-dependent reservation wage (Figure 2) provides a concrete interpretation of the $A$ component in $W(z, R, A; y)$: the opportunity cost of demand-side restrictions equals the wage premium required to accept a job with non-optimal hours. The U-shaped reservation wage means that workers far from their optimal hours demand much higher compensation, which is a direct measure of the welfare cost of hours restrictions.

## possible use for identification
The paper's identification strategy -- using desired hours to pin down preferences, then identifying offer distribution from observed hours residually -- is directly applicable to the RURO framework. If desired hours or satisfaction data are available, they can serve as an additional moment condition to separately identify $R$ from $A$. The paper shows that this approach works empirically, reducing $\sigma_\epsilon$ from 13.9 to 8.3--9.8.

## possible use for policy simulation
The policy simulation results (benefit cuts shift accepted hours toward part-time; shorter working week reduces part-time) demonstrate how the model can evaluate welfare effects of demand-side policy changes. In the $W(z, R, A; y)$ framework, these correspond to changes in $A$ (offer distribution) while holding $R$ (preferences) fixed.

# Research questions this paper inspires

1. The paper uses desired hours for men. For women (especially married women with higher part-time rates), the separation between preferences and offer restrictions should be even more important. Can the approach be applied to the female labour supply context where the RURO model is typically estimated?

2. The tolerance parameter $\bar{c} = 16.3$ suggests workers accept large hours deviations as "satisfactory." Does this mean that the welfare cost of hours restrictions is small for most workers (within the tolerance band), or does the tolerance reflect adaptation/rationalisation rather than genuine indifference?

3. Can the identification improvement from desired hours data be combined with the RURO framework's continuous opportunity density? Desired hours would provide information on the "preference ray" in $(h, w)$ space, while the RURO opportunity density would model the available alternatives.

4. The paper shows that the base model predicts underemployment while the data shows overemployment. For the RURO framework, does ignoring demand-side restrictions (as in standard discrete-choice models) systematically bias the direction of hours mismatch?

# Challenge to this paper

The paper's key innovation -- using desired hours to identify preferences -- rests on the assumption that desired hours responses reflect true preferences (up to measurement error or a satisfaction tolerance). But desired hours may themselves be shaped by perceptions of what is available: a worker who has never seen a 30-hour job may not report 30 hours as desired, even if it would be optimal. If desired hours are "contaminated" by awareness of the offer distribution, they do not provide a clean window into preferences, and the identification strategy breaks down. The paper acknowledges this indirectly by distinguishing "satisfaction" from "optimality" (the $\bar{c}$ parameter), but does not address the deeper question of whether desired hours are adaptive or anchored to available options. In the $W(z, R, A; y)$ framework, this is the question of whether reported preferences $R$ are genuinely "pre-market" or already shaped by $A$.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The paper directly models the demand-side component $A$ (job offer distribution $f(w,h) = f(w)p_l$) and preferences $R$ (utility function parameters), and shows that separating them requires additional data (desired hours) beyond observed choices. This is exactly the identification challenge in $W(z, R, A; y)$.

[Reasonable inference for my project] The overparameterisation result implies that standard discrete-choice labour supply models (which use observed hours to estimate preferences) may be estimating a mixture of $R$ and $A$, not $R$ alone. If Bargain et al. (2013)'s preference estimates absorb some offer-distribution features, the Fleurbaey welfare metrics could be biased. The RURO framework, by explicitly modelling the opportunity density, partially addresses this -- but Bloemen's results suggest that without additional data (like desired hours or satisfaction reports), even RURO may face identification challenges.

[Unclear from paper] Whether the dynamic structure of the search model (forward-looking behaviour, reservation utility) provides additional identification power compared to the static RURO model. The search model uses unemployment duration and job tenure data, which are not typically available in the cross-sectional data used for RURO estimation.

The paper is closest to: **identification of preferences vs. opportunities using subjective data** and **dynamic job search with hours restrictions**.

# Relation to Bargain et al. (2013)

Bargain et al. (2013) estimate preferences from observed choices in a standard discrete-choice framework without demand-side restrictions. Bloemen (2008) shows that this approach (the "base model") produces flat preferences that predict underemployment -- the opposite of what survey data shows (overemployment). If Bargain et al.'s Box-Cox utility estimates similarly absorb offer-distribution features, their Fleurbaey welfare metrics could be computing welfare from "contaminated" preferences. The paper motivates using desired hours or satisfaction data alongside Bargain et al.'s framework to verify whether the estimated preferences are genuinely reflecting $R$ rather than a mixture of $R$ and $A$.

# Relation to opportunities vs preferences

This paper is centrally about the opportunities-preferences distinction and provides the strongest empirical evidence for why the distinction matters. Three key results:

1. **Without desired hours (base model):** Preferences appear flat, offer probabilities absorb preference features, model predicts underemployment (wrong direction).
2. **With desired hours:** Preferences are sharply identified, offer distribution has different shape (more mass above 40h), model correctly predicts overemployment.
3. **Policy implications differ:** The hours satisfaction model shows higher benefit elasticity of unemployment duration (0.50 vs. 0.35) because it correctly identifies that workers dislike deviation from optimal hours, making them more responsive to changes in the value of continued search.

# Useful quotations / formulas

**On the identification problem (p. 149):**
"changes in offer probabilities and preference parameters both may act to fit the distribution of observed working hours. It is the particular structure of the search model and the nonlinear way in which preference parameters and offer probabilities enter (15) that allow for the parametric identification of the two if only information on working hours is available."

**On the overparameterisation paradox (p. 167):**
"The results show that the base model fits the observed distribution of working hours well, both by inspection of the simulated distribution function and according to a goodness of fit test. In the estimation of the base model the information on desired hours is not incorporated. Therefore the model is overparameterized: supply side parameters (preferences) and demand side parameters (hours offer distribution) are both retrieved using observed hours only."

**On the value of desired hours (p. 173):**
"The base specification suggests that preferences are relatively flat: this is shown by the shape of the distribution of optimal hours generated by the model as well as by the shape of the reservation wage rate as a function of hours, which does not have a pronounced minimum."

**Reservation utility equation (eq. 3):**
$$\bar{u}(q) = u(b + \mu, 0; \epsilon) + \frac{\lambda(v)}{\rho + \delta} \sum_{l=1}^{L} p_l \int_{\xi(h_l, \bar{u}(q); \epsilon)}^{\infty} [u(wh_l + \mu, h_l; \epsilon) - \bar{u}(q)] f(w) dw$$

**Escape rate (eq. 4):**
$$\theta(q) = \lambda(v) \sum_{l=1}^{L} p_l \bar{F}(\xi_l(q))$$

# Suggested tags

job-search, hours-restrictions, desired-hours, wage-hours-package, offer-distribution, reservation-wage, reservation-utility, unemployment-duration, identification, preferences-vs-opportunities, overparameterisation, overemployment, Netherlands, men, Hausman-utility, subjective-data, policy-simulation, benefit-elasticity, working-week

# My quick takeaway

This is the most important paper in my literature for demonstrating *why* separating preferences from opportunities matters empirically. The "overparameterisation paradox" -- the model without desired hours fits observed hours *best* but gets preferences *wrong* (predicting underemployment when workers are actually overemployed) -- is a devastating critique of any model that estimates preferences from observed choices alone without accounting for demand-side restrictions. For my JMP, this means: (1) the standard discrete-choice welfare metrics (Bargain et al. 2013) may be based on "contaminated" preferences that absorb offer-distribution features; (2) the RURO framework is on the right track by separating preferences from opportunities, but may face similar identification challenges without additional data; (3) desired hours or satisfaction data can provide the key additional moment condition needed to separately identify $R$ and $A$ in $W(z, R, A; y)$. The policy simulations also show that once preferences and opportunities are correctly separated, the model can evaluate demand-side policy changes (shorter working week, different offer distributions) that are invisible to standard preference-only models.
