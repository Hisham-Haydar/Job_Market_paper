---
title: "Theoretical and Practical Arguments for Modeling Labor Supply as a Choice Among Latent Jobs"
authors: [John K. Dagsvik, Zhiyang Jia, Tom Kornstad, Thor O. Thoresen]
year: 2014
outlet: "Journal of Economic Surveys, 28(1), 134–151"
shelf: "RURO / Latent Jobs / Constrained Labour Supply"
note_type: "canonical"
---

## Full citation
Dagsvik, J. K., Jia, Z., Kornstad, T., & Thoresen, T. O. (2014). Theoretical and Practical Arguments for Modeling Labor Supply as a Choice Among Latent Jobs. *Journal of Economic Surveys*, 28(1), 134–151.

## One-sentence contribution
A unified survey-style defence of the latent-jobs framework: it shows that the ad hoc hours dummies in the conventional discrete-choice model (Van Soest 1995) have an exact structural reinterpretation as the log of an opportunity measure plus a log opportunity distribution, and argues on this basis that the latent-jobs model is the theoretically appropriate baseline for labour-supply analysis.

## Core research question
How should the discrete-choice labour-supply framework be extended from a discretisation of the standard consumer problem to a structural model of job choice that explicitly distinguishes preferences over consumption and leisure from demand-side restrictions on the set of available jobs?

## Model / framework
Compares three nested approaches: (i) the Hausman continuous labour-supply equation; (ii) the conventional discrete-choice model with ad hoc hours dummies $\gamma(h)$; (iii) the job-choice model where utility is $U(C,h,z)=v(C,h)+\varepsilon(z)$ with i.i.d. extreme-value job-level taste shocks and the choice set contains $m(h)$ latent jobs at each hours level. Defining $\theta=\sum_h m(h)$ and $g(h)=m(h)/\theta$, the choice probability becomes a logit in $\psi(h)+\log\theta+\log g(h)$ (eq. 14) — formally identical to the dummy-augmented Van Soest model with the explicit identification $\gamma(h)=\log\theta+\log g(h)$. Box-Cox systematic utility is justified by invariance axioms.

## Data
The paper is a survey rather than an empirical study. Empirical illustrations use Norwegian Labour Force Survey 1997 (estimation) and 2003 tax-return / 2006 Labour Force Survey data for out-of-sample validation across a tax reform that cut the top marginal rate from 55.3% to 47.8%.

## Identification logic
Without functional-form restrictions only the sum $\psi(h)+\log g(h)$ is identified — preferences and opportunities are confounded. Two routes restore separation: parametric structure on $v(C,h)$ (the Box-Cox specification with invariance) or external information on desired hours (Euwals & van Soest 1999; Bloemen 2008). For tax/wage counterfactuals one does not actually need the separation, because only the income component of $v$ enters changes in the budget constraint.

## Treatment of preferences
$v(C,h)$ is treated as a true structural utility. The paper's central interpretive claim is that the convention of letting $\gamma(h)$ enter additively with $v(C,h)$ — and then calling the sum "preferences" — implies non-monotone preferences over hours, which is implausible. Reassigning $\gamma(h)$ to opportunities preserves a well-behaved $v(C,h)$.

## Treatment of opportunities / constraints
Opportunities are first-class. They consist of (i) an opportunity measure $\theta$ (total available jobs, allowed to depend on education and demographics, and interpretable as containing fixed costs of work) and (ii) an opportunity distribution $g(h)$ (fraction of available jobs at each hours level, typically uniform with peaks at full-time and part-time). $\theta$ in principle has a two-sided matching microfoundation but the survey treats it as exogenous in the short run.

## Welfare / normative object
None directly. But the paper makes the welfare-relevant point that conflating $g(h)$ with preferences via $\gamma(h)$ implies any welfare measure built on the misidentified utility will misclassify constrained outcomes as voluntary choices. References Dagsvik & Karlström (2005) for the matching CV machinery.

## Main findings
(i) The dummy-augmented Van Soest model and the latent-jobs model are *observationally equivalent* in their reduced form but interpretively distinct. (ii) The latent-jobs model provides a structural rationale for hours peaks. (iii) The framework can simulate demand-side counterfactuals (e.g. removing part-time positions) that the conventional model cannot. (iv) Out-of-sample, the model predicts the post-reform 2006 hours distribution well for women, less well for men. (v) Wage elasticities are not constant — they scale with $(1-P)$, so cross-country elasticity differences may partly be a mechanical consequence of differences in participation rates rather than of preferences or opportunities.

## Main limitations
A survey paper, not an empirical contribution; the authors explicitly state the alternative model "will in general not provide better fit." $g(h)$ is held fixed in the short run, so equilibrium responses of opportunities to large reforms are ignored. IIA is maintained. Nonparametric identification of preferences vs opportunities fails. No welfare analysis is implemented.

## Quick takeaway
The framing manifesto for RURO/latent-jobs labour supply. Its central, citable result is the equivalence $\gamma(h)=\log\theta+\log g(h)$, which gives any future RURO welfare or decomposition exercise a clean reinterpretation of the dummy-augmented conventional model as a special case where opportunities have been silently absorbed into preferences.
