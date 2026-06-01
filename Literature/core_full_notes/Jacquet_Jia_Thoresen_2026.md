---
title: "How Much Does Responsibility Matter in Fairness Measurement?"
authors: [Laurence Jacquet, Zhiyang Jia, Thor O. Thoresen]
year: 2026
outlet: "CESifo Working Paper No. 12418"
shelf: "Responsibility / Fairness / Equality of opportunity"
note_type: "canonical"
---

## Full citation
Jacquet, L., Jia, Z., & Thoresen, T. O. (2026). How Much Does Responsibility Matter in Fairness Measurement? *CESifo Working Paper No. 12418*, January 2026.

## One-sentence contribution
Operationalises the responsibility-vs-circumstance distinction within the Dagsvik job-choice (RURO) labour-supply model by constructing a circumstance-only Compensating Variation (CV$^{\text{circ}}$) that holds preferences at a reference value while preserving each household's actual opportunity set, and shows on Norwegian data that the welfare ranking of a major bracket-tax reform is essentially unchanged across the bottom nine deciles but diverges materially at the very top.

## Core research question
How much does it matter empirically whether welfare measurement of a tax reform respects each household's idiosyncratic preferences (a responsibility-respecting standard) or instead neutralises preferences and lets only circumstance-driven variation drive the welfare comparison (a compensation-only standard) — and where in the income distribution does the distinction bite?

## Model / framework
Dagsvik (1994) / Dagsvik & Jia (2016) job-choice model for couples. Utility on a job is $U(C,h_F,h_M,z)=u(C,h_F,h_M)+\varepsilon(z)$ with iid extreme-value taste shocks. Indirect utility decomposes additively: $V=u(f(\cdot),h_F,h_M)+\log Q_F(h_F)+\log Q_M(h_M)+\eta$, with the first term capturing preferences ($R$) and the $\log Q$ terms capturing opportunities ($A$). Female opportunity scale $\log\theta_F=\gamma_{F1}+\gamma_{F2}S$ depends on schooling; male scale normalised to one. Box-Cox systematic utility with 15 parameters. Three welfare objects: standard CV (own preferences, own opportunities), CV$^{\text{circ}}$ (reference preferences $\bar\gamma$ at sample medians, own opportunities, common $\bar\eta$), and the change in Conditional Equality $\Delta CE$ following Fleurbaey (2008).

## Data
Norwegian Labour Force Survey 2015 merged with Income and Wealth Statistics, 1,594 married couples. Tax-benefit calculations via the LOTTE microsimulator. Self-employed, weekly hours above 80, and wages outside NOK [70, 600] excluded. Reform studied: the 2013–2019 Norwegian "bracket tax" episode that replaced the two-tier surtax with a multi-bracket system while generally lowering MTRs.

## Identification logic
Standard RURO identification with the additional structure required for the responsibility cut. Preferences identified from variation in hours conditional on budget constraints; the female opportunity measure $\theta_F$ identified from the residual hours variation, parametrised through education; male $\theta_M$ normalised. The separation of $R$ from $A$ relies on the additive indirect-utility decomposition. CV is computed for each household using its own estimated preferences; CV$^{\text{circ}}$ is computed using $\bar\gamma$ — the difference is then interpretable as the welfare contribution of preference heterogeneity holding circumstances fixed.

## Treatment of preferences
Preferences are treated as responsibility characteristics following Kaplow (2008) and Lockwood & Weinzierl (2015) — tastes, not needs. Rich observed heterogeneity through age (log and squared), number of children below/above 6, gender, plus a spousal leisure interaction. The error $\varepsilon(z)$ is interpreted as preference heterogeneity (the paper notes Roemer & Trannoy 2016's caveat that this is itself contestable).

## Treatment of opportunities / constraints
Opportunities are an explicit primitive. The latent job set $B(h)$ has $Q(h)$ jobs at each hours level; the total market opportunity scale $\theta=\sum_{h>0}Q(h)$ contrasts market against non-market alternatives. The female scale depends on education; the hours density $g(h)$ has peaks at full-time and part-time. CV$^{\text{circ}}$ keeps these intact while neutralising preferences — so the metric measures welfare-given-the-opportunity-set, exactly the responsibility-sensitive object the fairness literature requires.

## Welfare / normative object
Three measures. (i) Standard CV — money-metric utility, preserves own preferences and circumstances. (ii) CV$^{\text{circ}}$ — preferences set to $\bar\gamma$, circumstances kept; isolates circumstance-driven welfare variation. (iii) $\Delta CE$ — Fleurbaey (2008) Conditional Equality, evaluated on a hypothetical equivalent linear budget at reference preferences. CV and CV$^{\text{circ}}$ are computed by McFadden (1999) simulation with $K$ Gumbel draws per household.

## Main findings
(i) Average reform welfare effects are similar under CV (NOK 18,384) and CV$^{\text{circ}}$ (NOK 18,677); CV$^{\text{circ}}$ is slightly less dispersed. (ii) Across deciles 1–9 the two measures track closely — the reform is welfare-improving for the vast majority of Norwegian couples regardless of which standard is applied. (iii) At decile 10 the gap opens: CV$^{\text{circ}}$ records larger gains than CV, because high-income women have stronger leisure preferences that are neutralised under CV$^{\text{circ}}$. (iv) 71–93% of households remain in the same quintile when ranked by CV vs CV$^{\text{circ}}$. (v) $\Delta CE$ and CV$^{\text{circ}}$ deliver the same distributional pattern, confirming the responsibility-sensitive metrics are empirically aligned with one another.

## Main limitations
The opportunity measure is parametrised through education only (and normalised for men), so any cross-individual variation in opportunities not captured by schooling is silently booked as preferences. The $\bar\gamma$ choice (sample medians) is one defensible reference but could materially affect CV$^{\text{circ}}$. The error term $\varepsilon(z)$ is classified as a preference component but could equally be read as a circumstance under different normative axioms. The exercise is a two-way comparison rather than a full Shapley decomposition. Single cross-section, single country, single reform — the headline "responsibility matters mostly at the top" claim is conditional on all three.

## Quick takeaway
The closest existing implementation of a $W(z,R,A;y)$ welfare exercise within a structural RURO model. Its central methodological move — substitute reference preferences while keeping actual opportunities to construct CV$^{\text{circ}}$ — is the canonical responsibility-sensitive analogue of Bargain et al. (2013)'s preference-respecting Fleurbaey metrics, and its empirical headline (responsibility binds mostly at the top of the income distribution in Norway) is the benchmark any cross-country extension will need to engage with.
