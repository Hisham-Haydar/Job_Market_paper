---
title: "Theoretical and Practical Arguments for Modeling Labor Supply as a Choice Among Latent Jobs"
authors: [John K. Dagsvik, Zhiyang Jia, Tom Kornstad, Thor O. Thoresen]
year: 2014
outlet: "Journal of Economic Surveys, 28(1), 134--151"
country_or_context: "Norway (empirical illustrations); general (theoretical framework)"
population: "Married couples (Norwegian Labour Force Survey and tax register data)"
data_period: "1997 (estimation), 2003/2006 (out-of-sample validation)"
shelf: "job choice / latent jobs / discrete choice / labour supply / opportunity measure / hours restrictions / RURO"
tags: [job-choice, latent-jobs, discrete-choice, labour-supply, opportunity-measure, opportunity-distribution, hours-restrictions, demand-side, Box-Cox, invariance, IIA, identification, Norway, policy-simulation, structural, Dagsvik, survey]
priority: "high"
read_status: "extracted"
---

# Full citation

Dagsvik, J. K., Jia, Z., Kornstad, T., & Thoresen, T. O. (2014). Theoretical and Practical Arguments for Modeling Labor Supply as a Choice Among Latent Jobs. *Journal of Economic Surveys*, 28(1), 134--151.

# One-sentence contribution

Provides a unified exposition and defense of the "job choice" model of labour supply -- where individuals choose among latent jobs characterised by fixed hours, wages, and nonpecuniary attributes, subject to demand-side restrictions on the available choice set -- contrasting it with both the standard textbook (Hausman) approach and the conventional discrete-choice (Van Soest) approach, and demonstrating that the job choice framework provides a structural rationale for the ad hoc dummy variables used in conventional discrete-choice models to fit peaks at part-time and full-time hours.

# Why this paper matters

This is the key survey paper that makes the case for the latent jobs / job choice framework as a theoretically superior alternative to both the Hausman continuous approach and the Van Soest conventional discrete-choice approach. It clarifies a crucial point: the conventional discrete-choice model's practice of adding dummy variables $\gamma(h)$ to the utility function to fit peaks at standard hours is *ad hoc* and lacks structural interpretation, whereas the job choice model provides a demand-side explanation for these peaks through the opportunity distribution $g(h)$. This paper is the methodological manifesto for the RURO approach used in Aaberge-Colombino and Capéau et al.

# Core research question

How can the discrete-choice modelling framework be extended from a simple discretisation of the standard consumer-choice problem to a structurally founded model of job choice that accounts for preferences over job attributes and demand-side restrictions on available jobs?

# Economic setting and context

The paper is primarily theoretical/methodological, with empirical illustrations from Norway. The Norwegian context features: high female participation but with substantial part-time work, unionised wage-setting, and regulated working hours -- all features that make demand-side hours restrictions empirically relevant.

The paper responds to criticisms of discrete-choice models (e.g., Keane 2011; Blundell et al. 2007; Heim 2009) who view them as "a somewhat crude approximate approach that makes estimation problems manageable" (p. 135). Dagsvik et al. argue the opposite: discreteness is not a computational shortcut but reflects the actual structure of labour markets where jobs come in discrete packages.

# Model / theoretical framework

**1. Standard textbook approach (Section 2.1):** Linear labour supply function:

$$h = \alpha + \beta \tilde{w}(h) + X\gamma + \delta \tilde{I}(h) + \varepsilon \quad \text{(eq. 1)}$$

where $\tilde{w}(h)$ is the marginal wage, $\tilde{I}(h)$ is virtual nonlabour income. Three weaknesses: (i) intractable with nonconvex budget sets, (ii) not robust to functional form and distributional assumptions, (iii) silent about job attributes and demand-side restrictions.

**2. Conventional discrete-choice model (Section 2.2):** Utility $U(C, h) = v(C, h) + \eta(C, h)$ where $\eta$ has extreme value distribution. Choice probability:

$$p(h) = \frac{\exp(\psi(h))}{\exp(\psi(0)) + \sum_{x \in D} \exp(\psi(x))} \quad \text{(eq. 6)}$$

where $\psi(h) = v(f(hw, I), h)$. This model cannot fit peaks at standard hours, so researchers add ad hoc dummies $\gamma(h)$:

$$p(h) = \frac{\exp(\psi(h) + \gamma(h))}{\exp(\psi(0)) + \sum_{x \in D} \exp(\psi(x) + \gamma(x))} \quad \text{(eq. 7)}$$

The paper's key critique: interpreting $v(C, h) + \gamma(h)$ as "true" utility implies non-monotone utility in hours, which is implausible. The peaks are more plausibly due to institutional hours restrictions, not preferences.

**3. The job choice model (Section 3):** Jobs are the fundamental choice unit, characterised by fixed hours $H(z)$, wages, and nonpecuniary attributes. Utility:

$$U(C, h, z) = v(C, h) + \varepsilon(z) \quad \text{(eq. 8)}$$

where $\varepsilon(z)$ captures unobservable nonpecuniary attributes of job $z$, iid extreme value. The agent's choice set $B(h)$ contains $m(h)$ available jobs with hours $h$. The choice probability of working $h$ hours is:

$$\varphi(h) = \frac{\exp(\psi(h)) m(h)}{\exp(\psi(0)) + \sum_{x \in D} \exp(\psi(x)) m(x)} \quad \text{(eq. 10)}$$

Define $\theta = \sum_x m(x)$ (total jobs) and $g(h) = m(h)/\theta$ (opportunity distribution):

$$\varphi(h) = \frac{\exp(\psi(h)) g(h) \theta}{\exp(\psi(0)) + \theta \sum_{x \in D} \exp(\psi(x)) g(x)} \quad \text{(eq. 12)}$$

**Critical equivalence (eq. 14):** The job choice model can be rewritten as:

$$\varphi(h) = \frac{\exp(\psi(h) + \log(\theta g(h)))}{\exp(\psi(0)) + \sum_{x \in D} \exp(\psi(x) + \log(\theta g(x)))}$$

This has the same structure as the conventional model with dummies (eq. 7), but now $\log g(h) + \log \theta$ replaces $\gamma(h)$. The crucial difference: $\log g(h)$ has a structural interpretation as the demand-side opportunity distribution, not an ad hoc utility term.

**Functional form for $v(C, h)$ (eq. 15):** Generalised Box-Cox:

$$v(C, h) = \frac{\gamma(C^\alpha - 1)}{\alpha} + \frac{\delta((M-h)^\beta - 1)}{\beta} + \frac{\mu(C^\alpha - 1)((M-h)^\beta - 1)}{\alpha\beta}$$

justified by invariance axioms (Dagsvik and Røine Hoff 2011; Dagsvik 2012).

# Key objects

- **Opportunity measure $\theta$:** Total number of available jobs. Can depend on education and other demographics. Interpretable as including fixed costs of work (Cogan 1981): $\theta \exp(c)$ where $c$ is disutility of fixed costs.
- **Opportunity distribution $g(h)$:** Fraction of available jobs offering hours $h$. If $g(h)$ is large at full-time and part-time, the model generates peaks at these hours without ad hoc dummies.
- **$\{m(h)\}$ as sufficient statistics (p. 141):** The numbers of available latent jobs at each hours level are sufficient statistics for the choice sets. This is a consequence of the iid extreme value assumption on $\varepsilon(z)$.
- **Nonpecuniary attributes $\varepsilon(z)$:** Job-specific utility components capturing working conditions, location, tasks, etc. These are the reason individuals don't all choose the same hours point -- heterogeneity in job attributes drives within-hours-category variation.

# Data

Empirical illustrations use:
- **Norwegian Labour Force Survey** (estimation, 1997): married couples.
- **Income tax return data** (2003): out-of-sample income distribution validation.
- **Labour Force Survey** (2006): out-of-sample hours distribution validation after a major tax reform (marginal rate reduced from 55.3% to 47.8%).

8 discrete hours intervals with medians at 260, 780, 1040, 1560, 1960, 2340, 2600 annual hours.

# Identification logic

**Nonparametric identification (p. 143):** Without parametric functional form assumptions, one can only identify $\psi(h) + \log g(h)$ -- preferences and opportunities are not separately identified from hours-of-work data alone. Separation requires either:
- Functional form assumptions on $v(C, h)$ (parametric identification)
- Data on desired hours (Euwals and van Soest 1999; Bloemen 2008)

For policy simulations involving changes in the budget constraint (tax reforms), the paper notes that one does *not* need to separate $v_2(h)$ (the hours component of utility) from $g(h)$, because neither depends on the budget constraint function $f$. Only the income component of utility needs to be identified for tax reform simulation.

**Opportunity distribution specification:** In applications, $g(h)$ is assumed uniform apart from peaks at full-time and part-time hours (captured by dummies). $\log(\theta g(h))$ specified as $\log \theta + \log g(h)$ where $\log \theta$ is linear in education, and $\log g(h)$ includes part-time and full-time dummies.

# Estimation / empirical strategy

1. Wage equation estimated to predict wages for non-workers
2. Budget constraint computed via tax-benefit rules at each discrete hours point
3. ML estimation of the job choice model with Box-Cox utility (eq. 15), opportunity measure $\theta$ (function of education), and opportunity distribution $g(h)$ (with PT/FT dummies)
4. Out-of-sample validation: predict hours distribution for 2006 (after tax reform) using 1997 parameters -- compare with actual 2006 data
5. Out-of-sample validation: predict income distribution for 2003 using tax return data -- compare with actual

# Treatment of preferences

Utility $v(C, h)$ is the systematic component of preferences over consumption and hours, with Box-Cox functional form (eq. 15) justified by invariance axioms. Nonpecuniary job attributes enter through $\varepsilon(z)$, which is iid extreme value across jobs. The paper explicitly separates preferences ($v(C, h)$) from opportunities ($g(h), \theta$) -- this is the defining feature of the job choice model relative to the conventional discrete-choice model.

Key conceptual point: in the conventional model, the dummies $\gamma(h)$ are absorbed into "preferences" (modified utility $v + \gamma$), conflating demand-side restrictions with tastes. The job choice model resolves this by attributing peaks to $g(h)$ (demand) rather than $\gamma(h)$ (preferences).

# Treatment of opportunities / constraints

This is the paper's central contribution. Opportunities are explicitly modelled through:
- **$B(h)$:** the set of available jobs offering hours $h$ (latent, unobserved)
- **$m(h) = |B(h)|$:** the number of available jobs at hours $h$
- **$\theta = \sum_h m(h)$:** total number of available jobs (opportunity measure)
- **$g(h) = m(h)/\theta$:** the opportunity distribution (fraction of jobs at each hours level)

The opportunity set is individual-specific through $\theta$ (which depends on education and demographics) but $g(h)$ is typically assumed common across individuals. The opportunity set reflects demand-side constraints: institutional hours regulations, employer preferences, union agreements, etc.

The paper notes that $\theta$ can be interpreted through a two-sided matching equilibrium (Dagsvik 2000; Dagsvik and Jia 2012b), where it depends on firm utilities (cost/production functions). However, the equilibrium derivation is beyond the scope of this survey.

# Welfare / normative object

No welfare analysis. The paper is about positive modelling (labour supply prediction and policy simulation). However, the separation of preferences from opportunities is crucial for welfare analysis: if peaks at standard hours reflect constraints ($g(h)$) rather than preferences ($v$), welfare calculations that treat observed choices as preference-optimal will be wrong. The paper references Dagsvik and Karlström (2005) on compensating variation in the job choice framework.

# Main findings

1. **The conventional discrete-choice model's ad hoc dummies have a structural interpretation** as the log opportunity distribution $\log g(h)$ plus the log opportunity measure $\log \theta$. Equation (14) shows formal equivalence, but the job choice model gives $\gamma(h)$ a demand-side interpretation rather than a preference interpretation.

2. **The job choice model provides a theoretical rationale for peaks at standard hours.** Peaks at full-time and part-time hours reflect the distribution of available jobs ($g(h)$ concentrated at these points), not non-monotone preferences for specific hours levels.

3. **The job choice model enables simulation of demand-side reforms** -- e.g., replacing part-time positions with full-time positions -- that the conventional model cannot simulate because it lacks explicit demand-side structure.

4. **Out-of-sample performance (Figures 1--3):** The job choice model predicts the 2006 post-reform hours distribution for married women well, and the 2003 income distribution for married couples well. For married men, the model over-predicts the shift to higher hours after the tax reform.

5. **Wage elasticities are moderate** and consistent with the broader literature. Married women are more responsive than married men. Elasticities are nonlinear: the same model produces very different elasticities at different participation rates ($0.4\alpha$ at $P = 0.6$ vs. $0.2\alpha$ at $P = 0.8$).

6. **The paper is explicitly theoretical, not empirical:** "Note that the point we make here is a theoretical one, and consequently, the alternative approach we propose will in general not provide better fit to the data than the conventional modified discrete labor supply model" (p. 135). The value is interpretive and structural, not in fit.

# Main limitations

- No new empirical results (survey/exposition paper)
- Opportunity distribution $g(h)$ assumed fixed in the short run -- no equilibrium determination
- IIA property maintained (from iid $\varepsilon(z)$), though relaxable via nested logit or random effects
- Nonparametric identification of preferences vs. opportunities is impossible without additional data (desired hours) or functional form assumptions
- No welfare analysis (though the framework enables it)
- Norwegian empirical illustrations may not generalise to other institutional contexts
- Job-specific wages not treated in the simplified version presented here (wages depend only on qualifications, not job type)

# Relevance for my JMP

## possible use as the methodological manifesto for the RURO approach
This paper is the definitive argument for why the job choice / latent jobs framework is preferable to the conventional Van Soest discrete-choice model. For my JMP, it provides the theoretical motivation: the conventional model conflates preferences and opportunities through ad hoc dummies, while the job choice model separates them. Since my welfare analysis (equivalent income in the RURO framework) requires this separation -- welfare depends on whether non-participation is voluntary ($R$) or involuntary ($A$) -- the job choice framework is not just theoretically cleaner but *necessary* for the welfare question I ask.

## possible use for the identification challenge
The paper is transparent about the identification problem: $\psi(h) + \log g(h)$ is identified, but $\psi(h)$ and $\log g(h)$ are not separately identified without functional form assumptions. This is the central methodological challenge for my JMP. The paper suggests two solutions: (i) parametric functional form for $v(C, h)$ (Box-Cox with invariance axioms), or (ii) desired hours data. I should discuss which approach I follow and why.

## possible use for the equivalence result (eq. 14)
The formal equivalence between the job choice model (eq. 12) and the conventional model with dummies (eq. 7) is a key result. It means that existing Van Soest estimates with dummies can be *reinterpreted* through the job choice lens: the estimated $\gamma(h)$ can be decomposed into $\log \theta + \log g(h)$, providing a post-hoc demand-side interpretation. This is useful for connecting my RURO results to the existing literature.

## possible use for the policy simulation advantage
The paper demonstrates that the job choice model can simulate demand-side reforms (replacing part-time with full-time jobs) that the conventional model cannot. For my JMP, this capability is important if I want to simulate reforms that change the opportunity set (e.g., subsidised job creation, public employment programmes) rather than just the tax-benefit schedule.

# Research questions this paper inspires

1. The paper establishes that $\psi(h) + \log g(h)$ is nonparametrically identified but the components are not. In the RURO welfare analysis, how sensitive are equivalent income estimates to different decompositions of $\gamma(h)$ into preference vs. opportunity components? If the welfare ranking of reforms depends on this decomposition, the identification problem is welfare-relevant.

2. The paper treats $g(h)$ as fixed in the short run. But if a tax reform increases the return to part-time work, won't employers create more part-time jobs? The equilibrium response of $g(h)$ to tax reforms is not modelled. How important is this for welfare analysis?

3. The elasticity nonlinearity result (p. 147) -- wage elasticity equals $(1 - P(w,X))\alpha$, so it's twice as large at 60% participation as at 80% participation -- has implications for cross-country comparisons. Countries with lower female participation would mechanically show higher elasticities even with identical structural parameters. Can the RURO framework disentangle whether cross-country elasticity differences reflect preferences, opportunities, or this mechanical nonlinearity?

# Challenge to this paper

The paper argues that peaks at standard hours should be attributed to demand-side restrictions ($g(h)$) rather than preferences ($\gamma(h)$). While this is plausible, the argument is fundamentally untestable without external information: the paper itself demonstrates that preferences and opportunities are not separately identified from hours data alone (p. 143). The theoretical appeal of the demand-side interpretation does not constitute evidence for it. One could equally argue that social norms, coordination with school hours, or habit formation create genuine preference peaks at standard hours. The paper's claim rests on *plausibility*, not identification -- and it candidly acknowledges this: "the alternative approach we propose will in general not provide better fit to the data" (p. 135).

More importantly, the equilibrium determination of $g(h)$ is deferred to other work (Dagsvik 2000; Dagsvik and Jia 2012b), but for policy simulation this is critical. If a tax reform changes incentives, $g(h)$ should respond through employer adjustments. Treating $g(h)$ as fixed while simulating large tax reforms is inconsistent with the equilibrium interpretation that the paper itself invokes.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The paper provides the formal structure for the $A$ component in $W(z, R, A; y)$. The opportunity set $A$ corresponds to $\{B(h)\}_{h \in D}$, parametrised by $\theta$ (total opportunities) and $g(h)$ (opportunity distribution). Preferences $R$ correspond to $v(C, h)$. The realised bundle $z$ is determined by the choice among available jobs, integrating both $R$ and $A$. The tax-benefit schedule $y$ enters through the budget constraint $C = f(hw, I)$.

[Reasonable inference for my project] The equivalence result (eq. 14) implies that the conventional Van Soest model with dummies is a *reduced form* of the job choice model, where $\gamma(h) = \log \theta + \log g(h)$. This means existing Van Soest estimates from the literature (e.g., Bargain et al. 2013; Bargain & Orsini 2006) can be reinterpreted through the job choice lens. However, *welfare analysis* requires the decomposition into $v$ and $g$ because welfare depends on whether observed choices reflect preferences or constraints.

[Unclear from paper] How the opportunity distribution $g(h)$ interacts with the tax-benefit schedule $y$ in equilibrium. The paper treats $g(h)$ as exogenous to $y$, but in general equilibrium, tax reforms affect employer decisions about job creation and hours offerings. The $W(z, R, A; y)$ framework should in principle allow $A$ to depend on $y$, but this is not operationalised.

# Relation to Bargain et al. (2013)

Bargain et al. (2013) use the conventional Van Soest discrete-choice model with ad hoc dummies for hours peaks. Dagsvik et al. (2014) provide the theoretical foundation for reinterpreting those dummies as the opportunity distribution $g(h)$. The welfare analysis in Bargain et al. treats observed choices as preference-optimal (all non-participation is voluntary), which this paper suggests is wrong: some of the hours distribution reflects demand-side constraints. If Bargain et al. (2013) were re-estimated with the job choice framework, the equivalent income calculations would differ because: (i) some non-participants would be classified as constrained (lower welfare than the preference-optimal model implies), and (ii) the welfare gain from tax reforms that move people into work would be larger (because entering employment relaxes a binding constraint, not just changes an optimally chosen leisure allocation).

# Relation to opportunities vs preferences

This is the paper's central theme. The conventional discrete-choice model conflates opportunities and preferences by absorbing demand-side effects ($g(h)$) into the utility function via ad hoc dummies ($\gamma(h)$). The job choice model separates them: $v(C, h)$ captures preferences, $g(h)$ and $\theta$ capture opportunities. The paper demonstrates that this separation is theoretically motivated (job attributes, hours regulations, employer constraints) but empirically challenging (nonparametric non-identification).

The paper's position is clear: "it seems more plausible to interpret the peaks found in the data as resulting from restrictions on hours of work" (p. 139) rather than as preference peaks. This is the foundational assumption for the RURO framework and for the welfare interpretation in my JMP.

# Useful quotations / formulas

**On the ad hoc nature of conventional dummies (p. 139):**
"The ad hoc practice of introducing dummy variables to improve the fit of the discrete choice labor supply model to improve the fit to the data has the unfortunate implication that the model will no longer be structural. As a consequence, it will be problematic how counterfactual policy simulations should be interpreted."

**On the structural interpretation (p. 141):**
"$\log g(h) + \log \theta$ in (14) is no longer a term that is added in an *ad hoc* manner but is given an explicit representation of choice restrictions that stem from the demand side of the labor market."

**On the theoretical (not empirical) nature of the contribution (p. 135):**
"Note that the point we make here is a theoretical one, and consequently, the alternative approach we propose will in general not provide better fit to the data than the conventional modified discrete labor supply model."

**On hours peaks and institutional regulations (p. 135):**
"Although one cannot rule out that workers may have stronger preferences for full-time and part-time hours of work... it seems more reasonable to assert that observed peaks at full-time and part-time hours are, to a great extent due to institutional regulations."

**On identification (p. 143):**
"If the offered wage depends on hours of work one cannot achieve identification in the nonparametric case without further assumptions... one can only separate preferences and the opportunity distribution up to an additive term depending on $h$."

**On the job choice model enabling demand-side simulations (p. 145):**
"Within our framework one can readily simulate the effect of this reform on labor supply by changing the opportunity distribution of hours... the conventional discrete choice framework cannot simulate the effect of this type of reform because the quantitative choice restrictions are not explicitly represented in the model."

# Suggested tags

job-choice, latent-jobs, discrete-choice, opportunity-measure, opportunity-distribution, demand-side, hours-restrictions, identification, Box-Cox, invariance, IIA, structural, ad-hoc-dummies, Van-Soest, Hausman, Norway, policy-simulation, Dagsvik, survey, RURO

# My quick takeaway

The theoretical manifesto for the job choice / latent jobs approach to labour supply modelling. The key insight: the conventional Van Soest model's practice of adding dummy variables $\gamma(h)$ to fit peaks at standard hours is ad hoc and conflates demand-side restrictions with preferences. The job choice model provides a structural interpretation: $\gamma(h) = \log \theta + \log g(h)$, where $g(h)$ is the opportunity distribution (demand-side) and $\theta$ is the opportunity measure (total jobs). For my JMP, this separation is essential: welfare analysis via equivalent income requires knowing whether non-participation is voluntary (preference) or involuntary (opportunity constraint). The paper is candid about the identification challenge -- preferences and opportunities are not separately identified from hours data alone -- which is a central methodological issue I must address.
