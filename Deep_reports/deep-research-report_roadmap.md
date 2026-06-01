# Mapping your RURO–welfare corpus into a defensible job market paper direction

## Corpus coverage snapshot

Your primary file *Literature_collection.md* is already a coherent “spine” rather than a grab‑bag: it combines (i) a Scandinavian/Italian structural labor‑supply tradition that treats jobs as discrete packages and models quantity constraints, (ii) a more recent latent‑job / random‑opportunity identification thread, (iii) an explicit welfare/heterogeneous‑preferences thread (both normative and empirical), and (iv) a complementary microsimulation/tax‑benefit layer. The secondary inventory *LIT_deep-research-report.md* mostly supplements breadth and reminds you of adjacent bridge literatures, but the core identity of the corpus is clearly the opportunities‑as‑job‑limits paradigm.

Below is a targeted assessment, aligned with your supervisor’s guidance (opportunities underexplored; responsibility central; country rankings not the main question; decomposition promising; consistency across estimation, welfare evaluation, decomposition).

### RURO / latent jobs

Coverage is **strong and unusually well chosen**.

- The corpus contains the “job packages + opportunity density” approach for labor supply with nonlinear budgets and institutional constraints via **Aaberge–Colombino–Strøm (Italy, quantity constraints)** and related work. A canonical example is “Labour Supply in Italy: An Empirical Analysis of Joint Household Decisions, with Taxes and Quantity Constraints,” which explicitly frames labor supply as a discrete choice under imperfect markets and quantity constraints. citeturn2search8  
- It contains modern “latent jobs” thinking with explicit identification analysis (not just estimation). “Labor Supply as a Choice Among Latent Jobs: Unobserved Heterogeneity and Identification” is exactly in your comparative‑advantage zone. citeturn0search4  
- It includes an explicit warning that **choice‑set construction and availability assumptions matter especially for policy counterfactuals**, consistent with your supervisor’s “opportunities modeled as limits” emphasis. The choice‑set paper “Evaluating Alternative Representations of the Choice Sets in Models of Labor Supply” is the right anchor. citeturn2search2  
- It includes an “hours‑offers / restricted choices” identification route that is conceptually parallel to RURO and very useful if you want a paper that is methodologically crisp. In particular, “Labour supply and taxation with restricted choices” shows how observed hours can reflect both preferences and offers, and develops identification logic for recovering one when the other is known. citeturn2search13turn2search10  
- It has a rationing bridge: “Making work pay” in a rationed labor market sits exactly at the “policy under constrained opportunities” interface. citeturn0search5  

**What is missing inside this cluster:** your corpus has the key empirical/technical papers, but it is missing the single most useful “manifesto” that clarifies why latent jobs is not merely a convenient discretization and how it differs from both the conventional discrete-hours approach and continuous Hausman-style marginal calculus. That’s a nontrivial gap because it tightens your framing and helps you pre‑empt seminar objections. citeturn0search3turn0search1  

### Structural labor supply with opportunities

Coverage is **strong**, with two shortcomings that look like JMP opportunities rather than problems:

1. The corpus gives you excellent templates for structurally estimating labor supply under constraints and using the model for counterfactual tax reforms (Italy, Norway, cross-country evidence). For example, “Labor supply responses and welfare effects from replacing current tax rules by a flat tax: Empirical evidence from Italy, Norway and Sweden” explicitly treats welfare effects (not just hours or revenue) and highlights heterogeneity across the income distribution. citeturn3search1turn3search0  
2. It also contains a strong methodological warning that simulations are sensitive to the way the feasible set is represented (choice set vs availability). citeturn2search2  

**But** most of the classic structural reform papers, even when they incorporate job constraints, still tend to treat the labor-market opportunity structure as background/partial equilibrium in policy simulations; that creates room for a JMP that “takes opportunity constraints seriously” in the welfare and decomposition layers, without claiming general equilibrium.

### Opportunities versus preferences

Coverage is **strong conceptually**, but **uneven in how it becomes an empirical decomposition object**.

- On the positive/identification side, you have strong pillars: latent jobs identification citeturn0search4, restricted-offer identification citeturn2search13turn2search10, and RURO applied estimation separating offers/intensities from preferences in a concrete dataset (Belgium, EU‑SILC). citeturn8search6turn8search5  
- On the normative side, you have a direct bridge in the newest working-paper “How Much Does Responsibility Matter in Fairness Measurement?”, which explicitly proposes comparing standard compensating variation to a responsibility‑neutralized variant using a structural job choice model that distinguishes preferences from circumstances. citeturn13search1turn13search0  

**What is still undercovered:** the corpus does not yet have a “canonical” empirical inequality decomposition toolkit that is explicitly framed as *opportunities vs effort/preferences* and that can be repurposed for welfare inequality rather than earnings inequality.

### Welfare analysis and welfare metrics

Coverage is **strong on theory and increasingly strong on empirical welfare analysis**.

- The corpus includes preference‑heterogeneity‑aware welfare comparisons built on estimated discrete choice labor supply models, e.g., “Welfare, labor supply and heterogeneous preferences: evidence for Europe and the US,” which explicitly shows welfare rankings depend on the normative treatment of preference heterogeneity (and not only on demographics). citeturn12search1turn12search5  
- It includes beyond‑GDP welfare comparisons (useful as a *foil*—something you can cite and then explicitly not replicate as your main question). citeturn7search0turn7search5  
- You also have nonparametric welfare tools for discrete choice choices that can become a methodological “escape hatch” if you want to reduce parametric dependence in the welfare layer: Capéau et al. develop nonparametric identification of distributions of individual welfare/welfare differences from choice probabilities and adapt Fleurbaey (2009) style welfare measures to discrete choice. citeturn8search1turn8search2  

**Missing:** a small number of bridge pieces that are particularly aligned with the “responsibility for preferences, compensation for circumstances” stance in applied welfare analysis (see the missing list below).

### Inequality decomposition

Coverage is **the clearest weakness relative to your supervisor’s guidance**, and therefore the **clearest JMP opportunity**.

Your corpus discusses inequality aversion and fairness, but it does not yet look like it contains a standard, reusable decomposition machinery for:  
\[
\text{Inequality in opportunity‑sensitive well‑being} \quad \Rightarrow \quad 
\text{“opportunity component”} \;+\; \text{“preference/effort component”} \;+\; \text{residual/interaction}.
\]

Two missing pillars matter:

- You need an inequality decomposition rule that is order‑independent and interpretable for non‑linear aggregates; the Shapley approach is the standard fix. Shorrocks (2013) is the canonical reference for a unified Shapley-value decomposition framework in distributional analysis. citeturn10search1  
- You need empirical inequality‑of‑opportunity decompositions (circumstances vs effort) that you can explicitly adapt from earnings to opportunity‑sensitive welfare. Bourguignon–Ferreira–Menéndez (Brazil; Review of Income and Wealth) is a classic empirical decomposition of earnings inequality into an opportunity component (circumstances) plus residual, including direct and indirect channels through effort. citeturn10search2turn10search0  
- Ferreira–Gignoux (2011) provides an operational scalar measure of inequality of opportunity (between‑group inequality based on circumstances) and is widely used as a “lower bound” style empirical benchmark. citeturn10search5  

This is exactly where your JMP can produce something that does *not* look like “yet another welfare ranking paper,” but rather as a structural + normative + decomposition contribution.

### Microsimulation / tax-benefit policy evaluation

Coverage is **solid, and enough for a supporting skill signal**, but it is not yet the central story—consistent with your goal.

Your corpus includes the EU tax‑benefit infrastructure and one of the best entry points: EUROMOD’s overview paper (data, validation, scope, architecture). citeturn7search1turn7search4  

**Likely underrepresented:** a “flagship” cross-country EUROMOD policy experiment paper that you can cite as a bridge while emphasizing your differentiation (you will treat opportunity constraints structurally rather than only through calibrated elasticities). Immervoll–Kleven–Kreiner–Saez is a canonical example. citeturn14search3turn14search2  

### Cross-country / beyond-GDP applications

Coverage is **moderate and sufficient as context**, but it is also the area your supervisor is warning you not to turn into the main question.

- Jones–Klenow (2016) is the standard beyond‑GDP welfare statistic combining consumption, leisure, mortality, and inequality. citeturn7search0turn7search5  
- The Bargain et al. welfare‑ranking approach brings preference heterogeneity into cross-country welfare ranking using discrete choice labor supply estimation. citeturn12search1turn12search5  

These are excellent “comparison class / foil” references: they justify why cross‑country ranking is tempting but also why it can look derivative unless you add a novel decomposition or opportunity‑constraint angle.

## Strongest defensible literature gaps for a JMP

### What looks saturated or risky to position as the main contribution

A cross-country welfare ranking paper that “simply” adds another welfare metric or another set of countries is high risk:

- Beyond‑GDP welfare comparisons already have a canonical AER benchmark. citeturn7search0turn7search5  
- Preference‑heterogeneity‑aware welfare rankings via discrete choice labor supply already exist for Europe/US and emphasize normative sensitivity to heterogeneity. citeturn12search1turn12search5  

So, if your paper’s headline is “country rankings change once we …,” it will likely be read as incremental unless you deliver a genuinely new dimension (e.g., opportunity constraints as a first‑class object) and a decomposition that changes interpretation.

### Where the literature is genuinely promising and underexplored

The most defensible gap—aligned with supervisor guidance—is:

**A consistent pipeline that treats opportunities as limits in jobs in (i) estimation, (ii) well‑being evaluation, and (iii) inequality decomposition.**

Concretely:

1. **Estimation layer:** RURO/latent jobs models identify/estimate preferences and opportunity/offer structures rather than folding everything into tastes. citeturn0search4turn2search13turn2search10  
2. **Welfare layer:** responsibility‑sensitive welfare measures require explicit decisions about what differences warrant compensation and what differences warrant responsibility; recent work shows how to embed this distinction into money‑metric welfare changes using structural job choice. citeturn13search1turn13search0  
3. **Decomposition layer:** there is no “default standard” yet that takes a structurally modeled opportunity set and turns it into a decomposed welfare‑inequality object with an order‑independent attribution rule—Shapley decomposition is the natural candidate. citeturn10search1turn10search0turn10search5  

This is the gap where you can most plausibly claim a real scientific contribution rather than “application only.”

### My candid assessment

If your JMP can *credibly* deliver a decomposition of welfare inequality into (at least) “opportunity-set inequality” and “preference/effort inequality,” with a welfare metric that is defensible under responsibility-sensitive reasoning, then you will have:

- a clear structural contribution (estimating opportunity sets in a RURO/latent jobs framework),
- a clear welfare economics contribution (explicitly stating and operationalizing a responsibility/compensation stance),
- and a clear applied contribution (showing the decomposition meaningfully changes what we think drives inequality and what policies do).

That combination is rare enough to be compelling in job market seminars.

## Missing or underrepresented papers to add

The items below are **only** papers that appear central to your stated JMP direction *and* are likely **not yet sufficiently represented** in your primary corpus. I group them by how critical they are to the “opportunities → welfare → decomposition” JMP arc.

### Core missing papers

- **Theoretical And Practical Arguments For Modeling Labor Supply As A Choice Among Latent Jobs** — entity["people","John K. Dagsvik","labor economist"]; entity["people","Zhiyang Jia","econometrician"]; entity["people","Tom Kornstad","statistics norway"]; entity["people","Thor O. Thoresen","public economist"] — 2014 — entity["organization","Journal of Economic Surveys","academic journal"] — [latent jobs / framing] citeturn0search3turn0search1  
- **Inequality Of Opportunity In Brazil** — entity["people","François Bourguignon","development economist"]; entity["people","Francisco H. G. Ferreira","world bank economist"]; entity["people","Marta Menéndez","economist"] — 2007 — entity["organization","Review of Income and Wealth","academic journal"] — [inequality decomposition / opportunities] citeturn10search2turn10search0  
- **The Measurement Of Inequality Of Opportunity: Theory And An Application To Latin America** — Ferreira; entity["people","Jérémie Gignoux","economist"] — 2011 — Review of Income and Wealth — [inequality of opportunity / measurement] citeturn10search5  
- **Decomposition procedures for distributional analysis: a unified framework based on the Shapley value** — entity["people","Anthony Shorrocks","economist"] — 2013 — entity["organization","Journal of Economic Inequality","academic journal"] — [Shapley / decomposition] citeturn10search1  
- **Optimal Income Taxation Theory and Principles of Fairness** — entity["people","Marc Fleurbaey","economist"]; François Maniquet — 2018 — Journal of Economic Literature — [normative bridge / fairness] citeturn8search0turn8search4  
- **Generalized Social Marginal Welfare Weights for Optimal Tax Theory** — entity["people","Emmanuel Saez","public finance economist"]; entity["people","Stefanie Stantcheva","economist"] — 2016 — entity["organization","American Economic Review","academic journal"] — [normative weights / policy evaluation] citeturn1search0turn1search4  

### Useful extensions

- **De Gustibus non est Taxandum: Heterogeneity in preferences and optimal redistribution** — entity["people","Benjamin B. Lockwood","economist"]; entity["people","Matthew Weinzierl","economist"] — 2015 — entity["organization","Journal of Public Economics","academic journal"] — [responsibility vs preferences / optimal tax] citeturn1search5turn1search1  
- **Optimal Income Transfer Programs: Intensive versus Extensive Labor Supply Responses** — Saez — 2002 — entity["organization","Quarterly Journal of Economics","academic journal"] — [policy design / extensive margin] citeturn11search1turn11search0  
- **Negative Marginal Tax Rates and Heterogeneity** — entity["people","Philippe Choné","economist"]; entity["people","Guy Laroque","economist"] — 2010 — American Economic Review — [heterogeneity / optimal tax link] citeturn11search2turn11search10  
- **Welfare reform in European countries: a microsimulation analysis** — entity["people","Herwig Immervoll","economist"]; entity["people","Henrik Jacobsen Kleven","economist"]; entity["people","Claus Thustrup Kreiner","economist"]; Saez — 2007 — Economic Journal — [EUROMOD / bridge] citeturn14search3turn14search2  
- **Getting tired of work, or re-tiring in absence of decent job opportunities? Some insights from an estimated Random Utility/Random Opportunity model on Belgian data** — entity["people","Bart Capéau","economist"]; Decoster — 2016 — EUROMOD Working Paper — [RURO applied / prefs vs opps] citeturn8search7turn8search5  
- **The Sensitivity of Structural Labor Supply Estimations to Modeling Assumptions** — entity["people","Max Löffler","economist"]; entity["people","Andreas Peichl","economist"]; entity["people","Sebastian Siegloch","economist"] — 2018 — entity["organization","IZA Discussion Paper","working paper series"] — [robustness / wage treatment] citeturn12search0turn12search6  
- **Empirical welfare analysis: when preferences matter** — entity["people","Jean-François Carpantier","economist"]; entity["people","Christelle Sapata","economist"] — 2016 — Social Choice and Welfare — [empirical fairness metrics] citeturn14search8turn14search9  
- **Valuing Alternative Work Arrangements** — entity["people","Alexandre Mas","economist"]; entity["people","Amanda Pallais","economist"] — 2017 — American Economic Review — [job amenities / discrete choice] citeturn1search2turn1search13  

### Possible blind spots

- **Generalized Social Marginal Welfare Weights Imply Inconsistent Comparisons of Tax Policies** — entity["people","Itai Sher","economist"] — 2024 — American Economic Review — [normative critique / caution] citeturn1search12  
- **A Practitioner’s Note on the Shapley-Owen-Shorrocks Decomposition** — entity["people","Richard Audoly","economist"]; entity["people","Rory McGee","economist"]; entity["people","Sergio Ocampo","economist"]; entity["people","Gonzalo Paz-Pardo","economist"] — 2025 — entity["organization","Federal Reserve Bank of New York Staff Reports","working paper series"] — [implementation aid / Shapley] citeturn10search10  
- **Inequality of Opportunity, Income Inequality and Economic Mobility: Some International Comparisons** — entity["people","Paolo Brunori","economist"]; Ferreira; entity["people","Vito Peragine","economist"] — 2013 — ECINEQ Working Paper / IZA DP / World Bank WP versions — [international IOp benchmarking / cautionary foil] citeturn9search0turn9search4  

## Mapping literature to JMP components

I interpret “strong enough for a JMP” as: you can write a credible introduction + model + prototype empirical section that survives a skeptical seminar *without* requiring a second paper’s worth of new theory.

### RURO / opportunity-set estimation

Supported strongly in your corpus by (i) job-package structural models with quantity constraints (Italy and beyond), citeturn2search8turn3search1 (ii) explicit choice-set/availability sensitivity analysis, citeturn2search2 (iii) latent-job identification analysis, citeturn0search4 and (iv) restricted-choice identification that lets you talk precisely about offers vs preferences. citeturn2search13turn2search10  

Most important missing paper: Dagsvik et al. (2014) manifesto to sharpen framing. citeturn0search3  

**Verdict:** **Strong enough**, and likely your most defensible core.

### Separating preferences from opportunities

Strong empirical/identification supports exist:

- Latent jobs identification discussion: citeturn0search4  
- Offers vs preferences identification in restricted choice sets: citeturn2search13  
- Applied RURO separating preference and opportunity heterogeneity (Belgium; EU‑SILC): citeturn8search6turn8search5  

Missing: again, Dagsvik et al. (2014) for “why this is not just discretization.” citeturn0search3  

**Verdict:** **Strong enough**, and (crucially) gives you a “scientific contribution” angle if you show how much “taste heterogeneity” shrinks once opportunity heterogeneity is modeled.

### Welfare analysis under heterogeneous preferences

Strong supports:

- Empirical welfare comparisons retaining preference heterogeneity using discrete choice labor supply estimation: citeturn12search1turn12search5  
- Nonparametric welfare analysis for discrete choice to reduce parametric dependence: citeturn8search1  

Missing/underrepresented: empirical implementations of fairness criteria (conditional equality / egalitarian equivalence) relying on individual preferences. citeturn14search8turn14search9  

**Verdict:** **Strong enough**, provided you keep the welfare object tightly tied to your structural model and avoid trying to “solve all interpersonal comparability” debates.

### Inequality decomposition

Supported weakly inside the current corpus (as far as your stated supervisor direction requires). The missing literature is extremely standard and easy to plug in:

- Shapley decomposition framework: citeturn10search1  
- Circumstances/effort opportunity decomposition in earnings: citeturn10search2  
- Scalar inequality‑of‑opportunity measurement benchmark: citeturn10search5  

**Verdict:** **Not yet strong enough as-is**, but **becomes strong** once you add 3–4 core references and define your decomposition object cleanly.

### Responsibility / compensation ideas in empirical work

Your corpus is already pointed in the right direction if it includes the new responsibility‑measurement working paper, which operationalizes a “responsibility-neutralized” welfare-change metric and explicitly uses a structural job-choice model to do so. citeturn13search1turn13search0  

Missing: preference heterogeneity in optimal redistribution framed explicitly as responsibility vs compensation (as in Lockwood–Weinzierl). citeturn1search5  

**Verdict:** **Promising but should be focused**: your JMP should not become “a general philosophy of responsibility,” but responsibility should be the normative justification for *your chosen welfare metric and decomposition.*

### Cross-country application

Your corpus has:

- Beyond GDP benchmark: citeturn7search0  
- Preference‑heterogeneity welfare rankings across Europe/US using harmonized microdata: citeturn12search1  

**Verdict:** **Strong enough as secondary motivation or robustness**, but **risky as the headline** (likely to look incremental).

### Regional / within-country application

This is the area I suspect is **underbuilt** in the corpus relative to the opportunity‑constraints story—but it is also where your JMP can be most original *without* requiring cross-country comparability.

A within-country design lets you interpret “opportunities” as **local labor-market job sets** (region × education/skill × demographic constraints) and gives you an intuitive decomposition story: “How much welfare inequality is due to unequal local job opportunities vs preference/effort heterogeneity?”

**Verdict:** **Scientifically promising**, but you will need to choose a dataset where job opportunities can be credibly proxied (EU‑SILC region + sector + hours brackets; matched employer‑employee data; or job‑ads/vacancy data).

### Microsimulation extension

You have EUROMOD infrastructure coverage. citeturn7search1  
A useful missing bridge is a flagship EUROMOD policy experiment paper (Immervoll et al.). citeturn14search3  

**Verdict:** **Strong enough as a supporting skill signal**, but I recommend keeping it as a second-stage extension after you have the opportunity‑sensitive welfare/decomposition core working.

### Optimal-tax or policy-design extension

Your corpus has fairness and tax foundations; adding the following makes it credible as an extension:

- Generalized welfare weights (connects fairness to implementable policy evaluation): citeturn1search0  
- Preference heterogeneity and redistribution: citeturn1search5  
- Extensive vs intensive margin transfer design intuition (EITC vs NIT): citeturn11search0  

**Verdict:** **Feasible as a short extension**, but do not let it dominate the JMP unless you have a clean new theorem or a very sharp sufficient-statistics bridge.

## Best feasible JMP directions

### Direction one

**Core question:** *How much of observed welfare inequality (in a labor-supply setting) is attributable to unequal job opportunities rather than preference heterogeneity, once labor supply is modeled as choice among latent jobs?*

**Contribution logic:**  
You (i) estimate a RURO/latent-jobs structural model, citeturn0search4turn2search8 (ii) define an opportunity‑sensitive money‑metric welfare measure that clarifies responsibility/compensation treatment, citeturn13search1turn1search5 and (iii) decompose welfare inequality into opportunity vs preference components using an order‑independent Shapley decomposition. citeturn10search1  

**Why it signals your skills well:** this direction screams structural estimation + identification + welfare economics + inequality measurement, without becoming “just microsimulation.”

**First empirical prototype:** replicate an existing RURO application setting (Belgium EU‑SILC is an existence proof), estimate preference and opportunity parameters, compute baseline money‑metric welfare, then run a decomposition where the “opportunity distribution” is equalized across some circumstance groups (regions, education types, age groups) and compute the implied reduction in welfare inequality. citeturn8search6turn8search5turn10search1  

**Main literatures addressed:** latent jobs / constrained labor supply citeturn0search4turn2search13, empirical welfare under heterogeneity citeturn12search1turn8search1, inequality of opportunity decomposition citeturn10search2turn10search5.

### Direction two

**Core question:** *Do policy evaluations (e.g., in-work benefits or tax reforms) change meaningfully when welfare changes are computed under a responsibility-sensitive metric that “neutralizes” preference heterogeneity but keeps opportunity constraints explicit?*

**Contribution logic:**  
You exploit the distinction between standard compensating variation and a responsibility-adjusted welfare metric computed from a structural job-choice model, then show that the distribution of winners/losers and the implied policy desirability differ when opportunity constraints are treated consistently. citeturn13search1turn0search5  

**Why it signals skills:** shows you can do structural counterfactuals and normative evaluation, but still stay empirically grounded in a real reform setting.

**First empirical prototype:** take a single reform environment (e.g., a tax schedule change), compute standard CV and responsibility-adjusted CV (or equivalent money-metric objects) by simulation from the estimated model, and highlight where differences concentrate (top tail, constrained groups, etc.). citeturn13search1turn3search3  

**Main literatures:** fairness measurement in public economics citeturn1search0turn8search0, constrained labor supply policy evaluation citeturn0search5turn3search3.

### Direction three

**Core question:** *Can we empirically show that “preference heterogeneity” in labor supply is overstated because standard models misattribute opportunity/offer heterogeneity (hours offers, job amenities) to tastes—and what does that imply for welfare and inequality evaluations?*

**Contribution logic:**  
You build an empirical demonstration that the estimated distribution of tastes (e.g., for leisure vs consumption) changes substantially after introducing a realistic offer distribution, and that welfare conclusions are sensitive to those modeling assumptions. citeturn2search13turn12search0  

**Why it signals skills:** strong econometrics/identification credibility; pre-empts “black box” critiques of structural models by being explicitly about robustness and misattribution.

**First empirical prototype:** implement a restricted-offers model (like Beffy et al. or RURO), test alternative offer distributions (or alternative opportunity heterogeneity parameterizations), and quantify how welfare inequality changes. citeturn2search13turn12search0  

**Main literatures:** identification of offers and preferences citeturn2search13turn0search4, robustness of structural estimation citeturn12search0.

### Preferred direction

**Preferred:** **Direction one** (opportunity-sensitive welfare inequality decomposition).  
It aligns perfectly with the supervisor guidance (decomposition due to opportunities; responsibility central; avoid headline country-rankings) and creates a distinctive JMP identity.

### Narrower fallback

**Fallback:** an explicitly “Belgium-style” RURO application that decomposes welfare inequality by age/education/region and uses Shapley decomposition plus a responsibility-sensitive welfare metric as the normative backbone. This is narrower because it relies on an existing estimation and focuses your novelty on the welfare + decomposition layer. citeturn8search6turn10search1turn13search1  

### Direction to avoid

**Avoid:** a JMP whose headline is **cross-country welfare ranking changes**. The literature already has strong anchors (beyond GDP welfare statistic; welfare rankings with heterogeneous preferences from labor-supply estimation), so you risk looking like a competent but incremental extension unless you add a deep decomposition/identification novelty. citeturn7search0turn12search1  

## Short roadmap, priority rereads, and missing-papers block

### Short 7–10 day roadmap

**Day 1–2: Pin down the “product definition” of the JMP.**  
Write a one-page memo with: (i) the welfare object you will measure (money-metric; baseline vs responsibility-adjusted), (ii) the decomposition target (inequality index of welfare; what groups define “circumstances”), and (iii) the minimal RURO estimation needed for a prototype.

**Day 3–4: Decide the decomposition and normative stance concretely.**  
Commit to (a) an inequality index (e.g., variance of log welfare, Gini of welfare, or Atkinson of welfare) and (b) an attribution rule (Shapley). This step is where the JMP becomes “a scientific contribution” rather than “an application.” citeturn10search1turn10search2turn10search5  

**Day 5: Build the first welfare-object computation pipeline.**  
Even with placeholder parameters, create the code skeleton: simulate job-choice probabilities, compute money-metric welfare (baseline and opportunity-equalized counterfactual), then compute inequality and a first-pass decomposition.

**Day 6–7: Prototype “opportunity equalization” counterfactuals.**  
Implement at least two clean counterfactuals:  
- equalize offer intensities/distribution across circumstance groups;  
- equalize only wage-offer distribution vs only hours-offer distribution.  
This gives you immediate “seminar slides” showing what dimension of opportunities matters.

**Day 8–10: Stress test and seminar-proof the identification story.**  
Draft a short “identification and interpretation” note that explains, in words and in equations, how your model separates preferences from opportunities and what assumptions are doing the work; cite the key identification papers and robustness references. citeturn0search4turn2search13turn12search0  

### Papers to revisit first

These are the 5–10 papers I would reopen *immediately* because they map one-to-one to your preferred JMP direction:

- “Labor Supply as a Choice Among Latent Jobs: Unobserved Heterogeneity and Identification” citeturn0search4  
- “Labour Supply in Italy: An Empirical Analysis of Joint Household Decisions, with Taxes and Quantity Constraints” citeturn2search8  
- “Evaluating Alternative Representations of the Choice Sets in Models of Labor Supply” citeturn2search2  
- “Labour supply and taxation with restricted choices” citeturn2search13  
- “Welfare, labor supply and heterogeneous preferences: evidence for Europe and the US” citeturn12search1  
- “Nonparametric Welfare Analysis for Discrete Choice: Levels and Differences of Individual and Social Welfare” citeturn8search1  
- “How Much Does Responsibility Matter in Fairness Measurement?” citeturn13search1  
- EUROMOD overview (as infrastructure) citeturn7search1  

### Missing Papers to Add

```markdown
## Missing Papers to Add

### Core missing papers
- Theoretical And Practical Arguments For Modeling Labor Supply As A Choice Among Latent Jobs — John K. Dagsvik; Zhiyang Jia; Tom Kornstad; Thor O. Thoresen — 2014 — Journal of Economic Surveys — [latent jobs / framing]
- Inequality Of Opportunity In Brazil — François Bourguignon; Francisco H. G. Ferreira; Marta Menéndez — 2007 — Review of Income and Wealth — [inequality decomposition / opportunities]
- The Measurement Of Inequality Of Opportunity: Theory And An Application To Latin America — Francisco H. G. Ferreira; Jérémie Gignoux — 2011 — Review of Income and Wealth — [inequality of opportunity / measurement]
- Decomposition procedures for distributional analysis: a unified framework based on the Shapley value — Anthony Shorrocks — 2013 — Journal of Economic Inequality — [Shapley / decomposition]
- Optimal Income Taxation Theory and Principles of Fairness — Marc Fleurbaey; François Maniquet — 2018 — Journal of Economic Literature — [normative bridge / fairness]
- Generalized Social Marginal Welfare Weights for Optimal Tax Theory — Emmanuel Saez; Stefanie Stantcheva — 2016 — American Economic Review — [normative weights / policy evaluation]

### Useful extensions
- De Gustibus non est Taxandum: Heterogeneity in preferences and optimal redistribution — Benjamin B. Lockwood; Matthew Weinzierl — 2015 — Journal of Public Economics — [responsibility vs preferences / optimal tax]
- Optimal Income Transfer Programs: Intensive versus Extensive Labor Supply Responses — Emmanuel Saez — 2002 — Quarterly Journal of Economics — [policy design / extensive margin]
- Negative Marginal Tax Rates and Heterogeneity — Philippe Choné; Guy Laroque — 2010 — American Economic Review — [heterogeneity / optimal tax link]
- Welfare reform in European countries: a microsimulation analysis — Herwig Immervoll; Henrik Jacobsen Kleven; Claus Thustrup Kreiner; Emmanuel Saez — 2007 — Economic Journal — [EUROMOD / bridge]
- Getting tired of work, or re-tiring in absence of decent job opportunities? — André Decoster; Bart Capéau — 2016 — EUROMOD Working Paper — [RURO applied / prefs vs opps]
- The Sensitivity of Structural Labor Supply Estimations to Modeling Assumptions — Max Löffler; Andreas Peichl; Sebastian Siegloch — 2018 — IZA Discussion Paper 11425 — [robustness / wage treatment]
- Empirical welfare analysis: when preferences matter — Jean-François Carpantier; Christelle Sapata — 2016 — Social Choice and Welfare — [empirical fairness metrics]
- Valuing Alternative Work Arrangements — Alexandre Mas; Amanda Pallais — 2017 — American Economic Review — [job amenities / discrete choice]

### Possible blind spots
- Generalized Social Marginal Welfare Weights Imply Inconsistent Comparisons of Tax Policies — Itai Sher — 2024 — American Economic Review — [normative critique / caution]
- A Practitioner’s Note on the Shapley-Owen-Shorrocks Decomposition — Richard Audoly; Rory McGee; Sergio Ocampo; Gonzalo Paz-Pardo — 2025 — Federal Reserve Bank of New York Staff Reports — [implementation aid / Shapley]
- Inequality of Opportunity, Income Inequality and Economic Mobility: Some International Comparisons — Paolo Brunori; Francisco H. G. Ferreira; Vito Peragine — 2013 — ECINEQ WP / IZA DP / World Bank WP versions — [international IOp benchmarking / foil]
```