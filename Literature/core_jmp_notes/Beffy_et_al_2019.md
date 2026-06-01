---
title: "Labour Supply and Taxation with Restricted Choices"
authors: [Magali Beffy, Richard Blundell, Antoine Bozio, Guy Laroque, Maxime Tô]
year: 2019
shelf: "RURO / Latent Jobs / Constrained Labour Supply"
note_type: "JMP-linked"
---

## Why this paper matters for my JMP
This is the strongest existing identification result for separating preferences from opportunities in a discrete-choice labour-supply model — and it does so without invoking the full RURO machinery I use, which makes it an essential robustness reference. The headline empirical finding (offer restrictions halve elasticities for UK mothers) is the most compelling outside-the-RURO evidence that the $A$ block in $W(z,R,A;y)$ is empirically first-order, not just theoretically interesting. If a referee prefers a less structural approach, this is the model they will compare mine against.

## What it tells me about opportunities vs preferences
Three things. First, the dominated-region argument is a clever non-RURO way to identify the opportunity block — variation in how the budget constraint is shaped serves as the exclusion restriction that variation in non-labour income serves in Dagsvik & Jia (2016). Second, the comparison of constrained vs unconstrained hours (26.2 vs 35.5) gives a clean numeric anchor for the size of the opportunity wedge — a useful benchmark for what "opportunity-equalised" hours might look like in my France counterfactual. Third, it shows that the opportunity block has observable correlates (education raises full-time offers), validating my plan to condition $g(h)$ on education.

## What it tells me about welfare measurement
The paper does not implement welfare, but it sketches exactly the welfare object I want: the money-metric gap between realised constrained utility and the unconstrained optimum. The fact that the women who fail the unrestricted-choice test are systematically poorer, lone, and lower-wage tells me the welfare cost of opportunity restrictions is correlated with circumstances — i.e., the opportunity-share contribution to welfare inequality is sign-predictable. This is a useful prior to bring to the France decomposition.

## What it tells me about decomposition
The 2× elasticity gap between unrestricted and two-offer specifications has a direct decomposition implication: roughly half of what naïve discrete-choice models book as a "preference response" to taxes is actually opportunity-driven. So in any tax-reform welfare decomposition, the preference share is overstated by something on the order of 50% if I use a Van-Soest-style model. That is the magnitude of the misclassification my JMP needs to correct.

## What it tells me about empirical design
Four lessons. (i) Use the budget-constraint dominated set as a diagnostic — flag observations in dominated regions and report the share. (ii) Allow opportunity-distribution covariates (education, household type, region) in $g(h)$ from the start — the paper finds these matter. (iii) Discipline the offer distribution with a parsimonious mixture rather than a fully nonparametric form. (iv) Estimate jointly with consumption and wage equations rather than sequentially — the control-function approach handles wage endogeneity cleanly.

## How I may cite it in the paper
As the leading non-RURO identification result for restricted-choice labour supply. Likely citations: in the framework section to motivate the opportunity primitive; in the identification section as a complementary identification source (budget non-linearities) to my own (functional-form-based identification of $v(C,h)\cdot g(h)$); in the empirical section as the benchmark for the magnitude of the elasticity bias from ignoring opportunities; and in the limitations section to acknowledge that my opportunity primitive carries wage information that theirs does not.

## What limitation of this paper my JMP may address
Three. (i) The two-offer restriction is arbitrary; my RURO opportunity scale $\theta$ implicitly estimates the effective number of offers. (ii) Their offer distribution is over hours only; mine is over (hours, wage) pairs, which matters for any welfare object that weights both income and time. (iii) They produce no welfare object despite the framework being well-designed for one — my JMP delivers exactly that object and a Shapley-Shorrocks decomposition built on top of it.
