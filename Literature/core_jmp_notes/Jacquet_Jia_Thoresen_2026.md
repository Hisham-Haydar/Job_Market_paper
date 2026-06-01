---
title: "How Much Does Responsibility Matter in Fairness Measurement?"
authors: [Laurence Jacquet, Zhiyang Jia, Thor O. Thoresen]
year: 2026
shelf: "Responsibility / Fairness / Equality of opportunity"
note_type: "JMP-linked"
---

## Why this paper matters for my JMP
This is the existing paper closest to what my JMP is doing. It implements the responsibility cut in a RURO model, constructs a circumstance-only welfare object, and evaluates a real tax reform with it. The methodological footprint is essentially the one I am extending to France 2016. So this is both my closest competitor — anyone reading my JMP will ask "what's new beyond Jacquet-Jia-Thoresen?" — and my most direct methodological precedent. My JMP needs to define its contribution sharply against this paper.

## What it tells me about opportunities vs preferences
The paper gives the cleanest worked example of the additive decomposition $V=u+\log Q_F+\log Q_M+\eta$ that licenses the $R/A$ split inside RURO. It also delivers the empirical headline I need to engage with: in Norway 2015, conditioning on opportunities while neutralising preferences leaves welfare rankings essentially unchanged in deciles 1–9 and only diverges at the top. That is a strong "responsibility-matters-little" result that my France pipeline either replicates (in which case the result generalises) or refutes (in which case I have a comparative-finding contribution).

## What it tells me about welfare measurement
The CV$^{\text{circ}}$ construction is exactly the welfare object I want to build for France. Lessons: (i) compute it via McFadden (1999) simulation with $K$ Gumbel draws per household, not via a closed form; (ii) take $\bar\gamma$ at sample medians rather than at any one reference person; (iii) verify alignment between CV$^{\text{circ}}$ and Fleurbaey's $\Delta CE$ as a cross-method robustness check — this paper finds them empirically aligned, which is reassuring. The paper does not implement CV$^{\text{pref}}$ (neutralising opportunities while keeping preferences), but mentions it as the natural complementary object. That is a clean opening for my JMP — completing the $2\times 2$ of (own/reference) preferences × (own/reference) opportunities is something this paper notably does not do.

## What it tells me about decomposition
The paper does a two-way comparison (CV vs CV$^{\text{circ}}$) but not a Shapley decomposition. It treats the difference between the two as the welfare contribution of preference heterogeneity. My JMP can extend this by adding the third channel (wage / non-labour income) and using a Shapley-Shorrocks decomposition for order-independence. The paper's own implicit decomposition into "preferences" and "circumstances" is best read as a special case of the four-way decomposition my framework produces.

## What it tells me about empirical design
Five lessons. (i) Estimate via Conditional Logit ML on the joint household choice set (here 56 alternatives = 7 male × 8 female). (ii) Box-Cox systematic utility with ~15 parameters is feasible at sample sizes around 1,500–2,500 couples — this is the order of magnitude my France SRCV sample sits at. (iii) Identify the female opportunity measure through schooling at minimum; for France I should add region and possibly sector. (iv) Normalise the male opportunity measure to one only if male participation is near-universal — for France this is a defensible call for prime-age men but maybe not for older cohorts. (v) Exclude self-employment and extreme wage outliers consistently with the Norwegian sample selection.

## How I may cite it in the paper
As the canonical existing implementation of CV$^{\text{circ}}$ inside a RURO model. Likely citations: in the introduction as the closest existing methodological precedent; in the model section as the source of the additive RURO indirect-utility decomposition; in the welfare-framework section as the source of CV$^{\text{circ}}$; in the empirical-results section as the Norwegian benchmark for the "where in the distribution does responsibility bite" question; and in the limitations section as the precedent that does not extend to a full Shapley decomposition or to opportunity-side neutralisation.

## What limitation of this paper my JMP may address
Three. (i) The opportunity measure depends on schooling only; my France pipeline can enrich it with region and education jointly, which the paper itself flags as a productive direction and which may flip the headline result. (ii) The two-way comparison stops short of a four-way Shapley decomposition over preferences, opportunities, wages, and non-labour income — my JMP delivers exactly that. (iii) The CV$^{\text{pref}}$ counterpart (neutralising opportunities) is mentioned but not constructed; my framework completes the $2\times 2$, which is normatively important because the responsibility cut and the compensation cut are dual objects, not the same one viewed twice.
