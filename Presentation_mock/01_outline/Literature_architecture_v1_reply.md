Below is a presentation-oriented literature architecture tailored to a job market talk in structural labor supply and welfare analysis. The emphasis is on named benchmarks, explicit differentiation, and committee-facing clarity rather than bibliographic breadth.

---

1. MAIN FIELD POSITIONING

Your paper sits at the intersection of four identifiable literatures:

1. Structural discrete labor supply with nonlinear budget sets
   (static structural estimation of preferences under tax-benefit systems)

2. Welfare and inequality measurement in structural models
   (money-metric utility, equivalent variation, welfare-based inequality)

3. Equality of opportunity and ex-ante/ex-post decomposition
   (Roemer-type frameworks; inequality of opportunity measurement)

4. Latent jobs / job-type heterogeneity and restricted opportunity sets
   (search frictions, job offer constraints, discrete opportunity sets)

The distinctive feature of your paper is that it connects (1) and (2) to (3) through (4): you structurally estimate preferences and job opportunities, then decompose welfare inequality into opportunity-sensitive components within a latent-jobs RURO framework.

---

2. NAMED PAPER BENCHMARKS

Strand 1: Structural Discrete Labor Supply

Van Soest (1995, JHR)
They estimate a discrete-choice labor supply model with nonlinear budget constraints and fixed costs.
You embed a similar structural labor supply core but extend it to latent job opportunity sets and move from behavioral elasticities to welfare decomposition.

Blundell, Duncan, McCrae & Meghir (2000, Econometrica)
They estimate female labor supply responses to tax reform using structural discrete choice.
You use a structurally estimated model not primarily to simulate elasticities, but to construct money-metric welfare and decompose inequality by opportunity sets.

Aaberge, Colombino & Strøm (2000, JPubE; 2004, JHR)
They estimate structural labor supply models and simulate tax reforms using discrete choice with nonlinear budgets.
You adopt a similar computational architecture but introduce an explicit opportunity-sensitive welfare decomposition that separates preferences from constraints.

Keane & Moffitt (1998, IER)
They structurally model welfare participation and labor supply with discrete alternatives.
You differ by focusing on latent job-type heterogeneity and welfare inequality across opportunity sets rather than program participation per se.

Strand 2: Welfare and Inequality in Structural Models

Aaberge & Colombino (2013, JPubE)
They derive measures of social welfare and inequality based on structurally estimated utility functions.
You go further by decomposing welfare inequality into preference heterogeneity versus opportunity heterogeneity components.

Bourguignon & Spadaro (2012, JPubE)
They evaluate tax reforms using structural microsimulation and welfare metrics.
You extend this logic from reform evaluation to a decomposition of observed welfare inequality conditional on latent job opportunity sets.

Blundell, Pistaferri & Saporta-Eksten (2016, AER)
They use structural life-cycle models to analyze insurance and welfare implications of income risk.
You remain static but introduce opportunity-sensitive welfare decomposition under discrete job constraints rather than income risk shocks.

Strand 3: Equality of Opportunity

Roemer (1998, 2004)
He formalizes equality of opportunity as compensation for circumstances versus effort.
You operationalize a structurally grounded analogue where job opportunity sets function as circumstance-type constraints within a utility-consistent welfare metric.

Fleurbaey & Schokkaert (2009, EJ)
They link welfare economics and responsibility-sensitive egalitarianism.
You bring this normative framework into a structurally estimated labor supply model with explicit monetary welfare measures.

Checchi & Peragine (2010, JPubE)
They empirically measure inequality of opportunity using income partitions.
You replace reduced-form income partitions with structural welfare levels derived from utility maximization under latent job sets.

Strand 4: Latent Jobs / Restricted Opportunity Sets

Dagsvik (1994, 2002)
He models labor supply with random utility over job opportunities and choice sets.
You build on this logic but use the structure to decompose welfare inequality across latent job sets rather than only estimate labor supply behavior.

Eckstein & van den Berg (2007, JEL)
They survey equilibrium search models with wage posting and job heterogeneity.
You do not model equilibrium search, but you incorporate heterogeneity in job availability as an exogenous opportunity structure entering welfare decomposition.

Bontemps, Robin & van den Berg (2000, RESTUD)
They estimate wage offer distributions in search models.
You abstract from equilibrium wage posting but similarly treat wage offers as draws from latent opportunity distributions that shape feasible utility levels.

---

3. WHAT THEY DO / WHAT I DO MATRIX

Literature strand: Structural discrete labor supply
Benchmark papers: Van Soest (1995); Blundell et al. (2000); Aaberge et al. (2004)
What they do: Estimate discrete labor supply models under nonlinear budget constraints to recover elasticities and simulate tax reforms.
What I do: Use a similar structural backbone but augment it with latent job opportunity sets and move from behavioral elasticities to opportunity-sensitive welfare inequality decomposition.

Literature strand: Structural welfare analysis
Benchmark papers: Aaberge & Colombino (2013); Bourguignon & Spadaro (2012)
What they do: Compute welfare effects of tax reforms using money-metric utility within structural microsimulation.
What I do: Decompose observed welfare inequality into preference-driven versus opportunity-driven components using structurally estimated utility.

Literature strand: Equality of opportunity
Benchmark papers: Roemer (1998); Checchi & Peragine (2010); Fleurbaey & Schokkaert (2009)
What they do: Decompose income inequality into effort and circumstance components using reduced-form partitions.
What I do: Implement an opportunity-sensitive decomposition in a structural utility framework where opportunity sets are inferred from latent job availability.

Literature strand: Latent job heterogeneity / search
Benchmark papers: Dagsvik (2002); Bontemps et al. (2000); Eckstein & van den Berg (2007)
What they do: Model wage offers and job heterogeneity within search or random utility frameworks.
What I do: Embed latent job heterogeneity into a static RURO labor supply model and trace its welfare inequality implications.

---

4. WHY ECONOMISTS SHOULD CARE

The economic problem is that observed income inequality conflates three distinct objects: heterogeneity in preferences, heterogeneity in wages/productivity, and heterogeneity in job opportunities. Standard inequality measures rank outcomes but do not isolate whether dispersion arises from constrained choice sets or from heterogeneous tastes over leisure and consumption.

This distinction matters for welfare analysis and policy. If welfare inequality is primarily driven by opportunity constraints (restricted job sets, low-quality offers), then redistribution alone is insufficient; policies targeting job access or matching efficiency become first-order. If it is driven by preference heterogeneity, compensatory policy has a different normative status.

Decomposition is more informative than ranking because social evaluation depends on the source of inequality. A Gini coefficient on income cannot tell whether two individuals with identical preferences face systematically different opportunity sets. An opportunity-sensitive welfare decomposition identifies how much inequality is structurally attributable to constrained choice sets versus preference dispersion, thereby aligning positive structural modeling with normative evaluation.

---

5. IDENTIFICATION IN TWO SENTENCES

The identification challenge is to separately recover preference heterogeneity and latent job opportunity sets from observed discrete labor supply choices under nonlinear budget constraints. The paper addresses this by exploiting variation in tax schedules and wage realizations to discipline utility curvature while using cross-sectional variation in accepted hours-wage bundles to infer the distribution of latent job types that rationalizes observed choice probabilities within the RURO structure.

---

6. PRESENTATION-SPECIFIC OUTPUTS

Paper in a Nutshell – Slide Draft

Title: Opportunity-Sensitive Welfare Inequality in a Latent-Jobs Labor Supply Model

• Estimate a structural discrete labor supply model with nonlinear taxes and latent job types
• Recover individual money-metric welfare levels
• Decompose welfare inequality into:
– Preference heterogeneity
– Wage/productivity heterogeneity
– Job opportunity heterogeneity
• Quantify how much inequality is due to constrained opportunity sets
• Implication: inequality of welfare is not isomorphic to inequality of income

What the Literature Has Done – Slide Draft

Structural labor supply (Van Soest 1995; Blundell et al. 2000):
→ Estimate elasticities and simulate tax reforms.

Structural welfare analysis (Aaberge & Colombino 2013):
→ Compute welfare gains from policy changes.

Equality of opportunity (Roemer 1998; Checchi & Peragine 2010):
→ Decompose income inequality into effort vs circumstance.

Search and latent jobs (Dagsvik 2002; Bontemps et al. 2000):
→ Model heterogeneity in wage offers and job availability.

Missing link:
No paper integrates latent job opportunity sets into a structural labor supply model to decompose welfare inequality into opportunity-sensitive components.

What I Add – Slide Draft

1. A RURO structural labor supply model with latent job types.
2. Money-metric welfare at the individual level.
3. A decomposition of welfare inequality into:
   – Preferences
   – Wages
   – Opportunity sets
4. A bridge between equality-of-opportunity theory and structural microsimulation.
5. Quantitative evidence on how much inequality is “opportunity-driven.”

Backup Literature Map – Slide Draft

Quadrant 1: Structural labor supply
Van Soest (1995); Blundell et al. (2000); Aaberge et al. (2004)

Quadrant 2: Welfare-based evaluation
Aaberge & Colombino (2013); Bourguignon & Spadaro (2012)

Quadrant 3: Equality of opportunity
Roemer (1998); Fleurbaey & Schokkaert (2009); Checchi & Peragine (2010)

Quadrant 4: Job heterogeneity / search
Dagsvik (2002); Bontemps et al. (2000); Eckstein & van den Berg (2007)

Your location:
At the intersection of all four — using structural labor supply to operationalize equality-of-opportunity concepts through latent job opportunity sets and welfare decomposition.

This architecture should allow you to present yourself clearly as a structural labor economist contributing to welfare analysis and opportunity-sensitive inequality measurement, rather than as someone assembling adjacent ideas.
