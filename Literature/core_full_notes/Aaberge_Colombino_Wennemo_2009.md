---
title: "Evaluating Alternative Representations of the Choice Sets in Models of Labor Supply"
authors: [Rolf Aaberge, Ugo Colombino, Tom Wennemo]
year: 2009
outlet: "Journal of Economic Surveys, 23(3), 586–612"
shelf: "RURO / Latent Jobs / Constrained Labour Supply"
note_type: "canonical"
---

## Full citation
Aaberge, R., Colombino, U., & Wennemo, T. (2009). Evaluating Alternative Representations of the Choice Sets in Models of Labor Supply. *Journal of Economic Surveys*, 23(3), 586–612.

## One-sentence contribution
A controlled Monte-Carlo comparison of sixteen discrete-choice labour-supply specifications — crossing fixed vs sampled alternatives, six vs twenty-four points, and the inclusion of job and hours-peak dummies — that shows in-sample fit is essentially uninformative about model quality and that out-of-sample policy predictions are accurate only when the choice set explicitly carries opportunity-density features.

## Core research question
How sensitive are estimated labour-supply elasticities and tax-reform predictions to the specification of the discrete choice set, and which features of that specification — number of alternatives, fixed vs sampled draws, treatment of job availability — are responsible for accurate out-of-sample behaviour?

## Model / framework
The "true" data-generating process is a continuous RURO model on Norwegian women (Aaberge & Colombino 2006) with opportunity density $p(h,w)=p^0 g_1(h)g_2(w\mid h)$, where $g_1(h)$ has peaks at part-time and full-time hours. Sixteen alternative discrete-choice models are estimated on Monte-Carlo samples drawn from this true model, crossing four choice-set sizes (6 fixed, 24 fixed, 6 sampled, 24 sampled) with four treatments of job availability (no correction; job dummy $d_0$ alone; peaks dummies $d_1,d_2$ alone; both). All models share the same Box-Cox preference structure with extreme-value taste shocks, so the comparison isolates choice-set design.

## Data
Norwegian 1995 administrative + survey data, 1,842 married/cohabiting women aged 20–62. The true RURO is estimated once on this sample; 100 Monte-Carlo replicates of size 1,842 are then drawn from the estimated true model, and each candidate model is re-estimated on each replicate.

## Identification logic
The exercise inherits identification from the true RURO model. The diagnostic identification question is then operational: can simpler models recover the true model's out-of-sample predictions from in-sample data? In-sample fit is found to identify preferences across all sixteen specifications equally well; the opportunity component is identified only when the choice set carries explicit job-availability features ($d_0$ approximating $\log p^0$ and $d_1,d_2$ approximating the peaks in $g_1$).

## Treatment of preferences
Box-Cox utility in disposable income and leisure with age and child taste-shifters and Type-I extreme-value job-level shocks. Functional form is held identical across all sixteen variants so the experiment isolates choice-set effects rather than preference-form effects.

## Treatment of opportunities / constraints
The paper's centre of gravity. The true model has an opportunity scale $p^0<1$ (rationing), a hours density with two institutional peaks, and a log-normal conditional wage density. Candidate models approximate these with combinations of a job dummy (overall market vs non-market opportunity ratio) and peaks dummies (institutional bunching at part-time and full-time hours). Only specifications carrying both kinds of dummies recover the opportunity content of the true model.

## Welfare / normative object
None directly computed. The exercise is positive but the implications are explicitly normative: any welfare evaluation built on a model that mispredicts hours under the counterfactual cannot deliver credible welfare numbers under the same counterfactual.

## Main findings
(i) All sixteen models fit the 1995 baseline hours distribution similarly well. (ii) Under a revenue-neutral 25% flat-tax counterfactual, mean prediction errors range from 30–55% for specifications without opportunity-density features down to under 5% for the 24-sampled-alternatives specification with both job and peaks dummies. (iii) The interaction of "more alternatives" with "job dummy" matters more than either alone. (iv) The marginal value of peaks dummies exceeds that of the job dummy. (v) Sampled vs fixed alternatives matters less than the dummy structure once the latter is in place.

## Main limitations
The reference truth is itself a parametric RURO, not an external benchmark — the ranking of competing models is conditional on the RURO being correct. Only female labour supply is modelled; husbands are held fixed. Only one counterfactual (a flat tax) is examined. The Norwegian opportunity structure has unusually pronounced peaks, so quantitative magnitudes may not transfer cleanly to economies with smoother hours distributions. No welfare object is computed.

## Quick takeaway
The cleanest empirical demonstration that opportunity-density features are first-order for tax-reform predictions even when in-sample fit is indistinguishable. Any RURO-vs-Van-Soest comparison should cite this paper for the specific finding that "job dummy + peaks dummies + sampled alternatives" is the minimum specification that recovers the truth, and any welfare exercise that omits opportunity features should be expected to inherit the 30–55% bias seen in the labour-supply layer.
