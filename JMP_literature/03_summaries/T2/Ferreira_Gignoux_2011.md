# Ferreira & Gignoux 2011 — The Measurement of Inequality of Opportunity: Theory and an Application to Latin America

> **Extraction status:** T1A exhaustive, per `JMP_T1_exhaustive_extraction_prompt_v2.md`.
> **Source of truth:** the attached PDF (journal pages 622–657). Page references below are journal pages.
> **Convention used throughout:** *explicit-in-source* = stated in the paper; *derived-by-analogy* = my mapping to the JMP, not in the paper; *not-established* = neither.
> The paper predates and is unaware of my framework; almost every mapping to RURO/latent-jobs, to money-metric welfare, and to the access/ability/preference cut is *derived-by-analogy*. I flag this explicitly rather than letting the prompt's vocabulary leak into claims about the source.

---

## 0. Metadata

- **BibTeX key:** `FerreiraGignoux2011`
- **Authors:** Francisco H. G. Ferreira (The World Bank; IZA); Jérémie Gignoux (Paris School of Economics).
- **Year:** 2011.
- **Outlet:** *Review of Income and Wealth*, Series 57, Number 4 (December 2011), pp. 622–657.
- **DOI:** 10.1111/j.1475-4991.2011.00467.x (explicit-in-source, p. 622).
- **JEL codes:** D31, D63, J62 (explicit-in-source, p. 622).
- **PDF filename:** `FERREIRA_GIGNOUX_2011_THE_MEASUREMENT_OF_INEQUALITY_OF_OPPORTUNITY.pdf`.
- **Tier:** T1A.
- **JMP block(s) served:** *decomposition* (primary); *normative-interpretation* (secondary); *motivation* (secondary). Does **not** serve estimation, identification of preferences-vs-opportunities in the structural sense, the opportunity-mechanism (access/ability) layer, or data-infrastructure for France.

---

## 1. One-paragraph relevance to my JMP

This is the cleanest available template for the *decomposition* layer: it pins a relative inequality-of-opportunity ratio to the **mean log deviation** $E_0$ via Foster–Shneyerov path-independent decomposability, and proves that the between-group share is a **lower bound** on true opportunity inequality (pp. 631–632, 635–636). For my D2 layer it supplies (a) a defensible index choice and (b) a lower-bound argument I can borrow as a defence against the "your decomposition is mechanical" referee — but only with a sharp caveat, because their decomposition is **two-way** (between-type "opportunity" vs an "effort+luck" residual) and **subgroup-based**, not the **three-way {access, ability, preference} Shapley–Shorrocks** factor decomposition I run. On the channel map it speaks to nothing inside my opportunity density $g$: its "circumstances" sit upstream of all three of my channels and it separates none of them, and its advantage variable is reduced-form income/consumption, not a preference-respecting money-metric $V_i$. It is therefore a *measurement-and-decomposition* anchor and a *motivation* citation, and a precise statement of the gap my structural opportunity object is meant to fill.

---

## 2. Data and setting

**Country/year/datasets (explicit-in-source, pp. 637–638, Table 1).** Six nationally representative household surveys: Brazil PNAD 1996; Colombia ECV 2003; Ecuador ECV 2006; Guatemala ENCOVI 2000; Panama ENV 2003; Peru ENAHO 2001.

**Sample unit (explicit-in-source, pp. 637–638).** Individuals who are household heads or their spouses, aged 30–49, with positive income/consumption and complete circumstance information. The age and head/spouse restrictions are imposed for comparability and because in Brazil and Peru background information was only collected for these individuals.

**Sample sizes after exclusions (explicit-in-source, Table 1, p. 638):** Brazil 70,521; Colombia 17,979; Ecuador 10,719; Guatemala 5,988; Panama 4,556; Peru 13,621.

**Key variables (explicit-in-source, pp. 638–640, Tables 2–4).**
- *Advantage $y$:* household per capita income, and household per capita consumption expenditure where available (consumption absent for Brazil).
- *Circumstances $C$:* father's education, mother's education (each 3 categories), father's occupation (agricultural worker / other; missing for Colombia and Peru), ethnicity/race (2 categories), region of birth (3 categories, or urban/rural for Panama). Gender is used **only** in a separate labour-earnings specification, not in the household-advantage analysis (see §8).

**Budget-set construction:** N/A. There is no budget map, no tax-benefit system, no consumption-from-hours construction. Advantage is taken directly from the survey income/consumption aggregate.

**Transport to my France pooled 2015–2017 EUROMOD cross-section.**
- *Compatible features (derived-by-analogy):* a single cross-section per country with no panel; a household-level money advantage measure; a partition-into-groups logic that I can re-use over my own groupings.
- *Features I do NOT have that they rely on / features they lack that I have:* they have **intergenerational background circumstances** (parental education, father's occupation, ethnicity, birthplace) that EU-SILC/EUROMOD does not deliver in usable form for France; they have **no behavioural model, no labour-supply choice, no wages-as-offers, no occupation-as-availability, and no tax-benefit budget**, all of which I have. They have **no panel, no administrative match, no external instrument, and no vacancy/offer data** — the same instrument poverty I face, which is relevant to §8.

---

## 3. Model and objects (object-by-object)

The paper is a **measurement framework, not a behavioural or structural model** (explicit-in-source, §2). The object-by-object map is therefore mostly a list of absences; I state each explicitly because the absences are exactly what my structural layer supplies.

- **Their choice set vs my latent-jobs set $\mathcal{C}_i$:** none. There is no choice set, no alternatives, no discrete choice. *Not-established* in the source.
- **Their deterministic utility vs my preference utility $v$:** none. No utility function, no Box–Cox, no taste-shifters. Preferences are *not modelled at all*; whatever they would explain is absorbed into the residual (explicit-in-source, "Treatment of preferences" is empty by construction — see §7 of the source's own framing and p. 633).
- **An explicit opportunity / availability mechanism analogous to my $g$:** none in the structural sense. "Opportunity" is operationalised as a **partition of the population into Roemerian types** $T_k$ that are homogeneous in observed circumstances (explicit-in-source, p. 626). There is no density over feasible jobs, no hours availability, no wage-offer technology, no participation/market mechanism, and no occupation-as-availability object. It therefore does **not** separate hours / wage(ability) / market / occupation channels.
- **Their budget map vs my EUROMOD disposable income:** none. Advantage is the raw survey aggregate (pp. 638–639).
- **Does any job attribute enter BOTH utility and the opportunity mechanism?** N/A — there is neither a utility block nor an opportunity mechanism, so the double-counting hazard the prompt asks me to flag cannot arise here. Worth recording the contrast: their *circumstances* are by construction **exogenous and upstream**, never simultaneously a taste-shifter and an availability shifter, precisely because there is no behavioural layer for them to enter twice.

**Net:** the only object that maps to mine is the **advantage variable** $y$ ↔ my money-metric welfare $W$/$V_i$, and even that map is loose: $y$ is reduced-form income/consumption, not a preference-respecting equivalent income.

---

## 4. Estimation method

**Likelihood and estimator (explicit-in-source, §3, pp. 632–636).** There is no likelihood. Two procedures estimate the *same* path-independent quantities:
1. **Non-parametric:** compute the between-group component of the MLD directly from type-cell means, i.e. $E_0(\{\mu_i^k\}) = \tfrac{1}{N}\sum_i \log(\mu/\mu_i^k)$ with $\mu$ the grand mean and $\mu_i^k$ the type mean assigned to $i$ (explicit-in-source, p. 632).
2. **Parametric:** OLS of log advantage on circumstances, $\ln y = C\psi + \varepsilon$; build a parametric *smoothed* distribution $\tilde\mu_i=\exp[C_i\hat\psi]$ (eq. 8) and a parametric *standardized* distribution $\tilde\nu_i=\exp[\bar C\hat\psi+\hat\varepsilon_i]$ (eq. 9), then form $E_0$-based IOL/IOR from the standardized estimates (eqs. 10′, 11′) (explicit-in-source, pp. 633–634).

**Choice-set construction / fixed grid vs sampled alternatives / grid size:** N/A — no choice set, no grid, no alternatives.

**Proposal / sampling density; prior/proposal correction:** N/A. There is **no** $\log(\text{prior})$ correction because there is no sampling of alternatives. This is the central structural reason the paper cannot be reused as an estimator for my pipeline.

**Normalisation / scale / numerical method / starting values / multistart:** N/A beyond standard OLS. Bootstrap standard errors are computed accounting for sampling weights, stratification, and clustering (explicit-in-source, p. 643).

**What pins preferences separately from the opportunity mechanism:** nothing — preferences are not in the model. The "between vs within" split is a *definitional* allocation (between-type = opportunity; within-type = effort+luck+unobserved circumstances), not an identified behavioural separation. This is exactly the separation my structural model is built to earn rather than assume.

**Verdict (reusable for my RURO/JAX pipeline?):** **No** for the estimator. The estimation machinery (OLS + between-group $E_0$) is not a discrete-choice estimator and carries no proposal correction. **Yes, partially**, for the *downstream* decomposition: the between-group $E_0$ computation and the path-independence argument are directly reusable in D2 *as the index/decomposition rule*, applied to my welfare object instead of to income — but the **factor** structure I need (Shapley over access/ability/preference) is not what they implement (see §7).

---

## 4b. Proposal / sampling-of-alternatives correction

**N/A — extract recorded for completeness.** The paper performs no sampling of alternatives and therefore has no proposal density, no per-alternative log-prior, and no McFadden-style correction. There is no individualised-vs-common proposal distinction to map onto my importance-sampling welfare integrator (where wage and occupation are individualised and hours/employment are common, per welfare spec v5 §V5-1). The only faint analogue is the **parametric counterfactual construction** (eqs. 8–9, 12): replacing residuals or fixing circumstances to build smoothed/standardized distributions is a *re-weighting-by-construction* of the empirical distribution, conceptually adjacent to a counterfactual integrator but with no stochastic sampling and no importance weights. Treat as *derived-by-analogy only*; do not cite this paper for anything about sampling-of-alternatives corrections.

---

## 5. Opportunity mechanism  [MOST IMPORTANT]

**There is no explicit opportunity mechanism in the structural sense.** I state this plainly because it is the paper's defining limitation for my purposes and the precise location of my contribution.

**What plays the role of "opportunity" (explicit-in-source, §2, pp. 626–629):** the population is partitioned into Roemerian **types** $T_k$, homogeneous in observed predetermined circumstances. "Equality of opportunity" is operationalised, following van de Gaer (1993), by the **weak criterion** that *mean* advantage be equal across types (eq. 4), a weakening of Roemer's (1998) *strong* criterion of equal conditional distributions (eq. 3). Inequality of opportunity is then between-type inequality in the **smoothed distribution** $\{\mu_i^k\}$ (each individual replaced by their type mean) (explicit-in-source, p. 630). It is **not** a density over alternatives, **not** offer probabilities, and **not** a reservation-wage/participation restriction.

**Does it vary with observable circumstances?** Yes — that is the entire content: opportunity is *defined* by variation in mean advantage across circumstance cells (region of birth, parental education, father's occupation, ethnicity). But these are **background/origin circumstances**, not contemporaneous labour-market availability.

**Map to my three sub-objects (derived-by-analogy):**
- **access** (hours / market-participation / region / year / occupation offers): **not represented.** Region appears, but as *region of birth* (an origin circumstance), not as a local-labour-market access shifter. No hours availability, no participation mechanism, no occupation offers.
- **ability** (the wage technology — returns to own education and experience, residual productivity dispersion): **not represented.** Parental education is a circumstance; the *respondent's own* education-and-experience wage return — my ability block — is not a structural object here, and in the reduced form it is absorbed into the residual/effort term rather than modelled.
- **occupation as availability vs something else:** the paper uses **father's occupation** (agricultural worker / other) as a *background circumstance*, i.e. an intergenerational-origin variable. This is **not** my `loc4` occupation-as-access object, and it is **not** industry/sector either. **Flag:** do not let "father's occupation" be read as occupation-opportunity in my sense; it is a parental-origin circumstance. There is no sector/industry conflation in the source to flag, because there is no contemporaneous occupation or industry object at all.

**Functional form:** type means (non-parametric) or $\exp[C\hat\psi]$ from a log-linear OLS (parametric).

**Cost of the omission for my access/ability/preference decomposition (derived-by-analogy):** because the source has no feasible-set object, it cannot distinguish demand-side job availability (my *access*) from the wage-generating technology (my *ability*) from tastes (my *preference*); all three are either folded into the circumstance partition (if correlated with background) or dumped into the residual (if not). My structural opportunity density is precisely what makes the access/ability split *identifiable as a modelled object* rather than assumed via a partition. The paper's lower-bound logic (§8) is, in effect, a confession that an unmodelled opportunity object leaves opportunity inequality understated — which is the motivation for modelling it.

---

## 6. Welfare object — and its place on my $W^1$–$W^6$ map

**Does the paper compute welfare? No.** It computes **inequality indices** ($\theta_a$/IOL absolute, $\theta_r$/IOR relative), not a welfare function (explicit-in-source, pp. 630–632). There is:
- no money-metric welfare, no equivalent income, no King (1983)/Fleurbaey-style construction;
- no compensating/equivalent variation;
- no expected (log-sum / inclusive-value) utility;
- no reference price, reference preference, reference bundle, or reference set;
- no discrete-choice welfare subtleties (no log-sum aggregation, no Hicksian/Marshallian distinction, no integration over unobserved heterogeneity, no ex-ante/ex-post welfare integration). The *ex-ante vs ex-post* language **does** appear (pp. 628–629), but as a distinction between **inequality-of-opportunity criteria** (van de Gaer ex-ante / Checchi–Peragine ex-post), **not** as a welfare-integration timing choice. Do not import their ex-ante/ex-post usage as if it were my ex-ante inclusive-value vs ex-post chosen-alternative distinction.

**Place on my $W^1$–$W^6$ map.** **None — the source contains no $W^1$–$W^6$ object and no equivalent-income measure of any kind.** Mapping the advantage variable $y$ onto the family is *derived-by-analogy at best*: raw income/consumption corresponds to no specific Independence-of-$y$ / Independence-of-$A$ stance, because it embeds no preference-respecting reference at all. If forced, $y$ is closest in spirit to a **pre-welfare outcome** that my measures evaluate, not to any member of the family. **Verdict: incompatible as a welfare object; adaptable only as the *target distribution* a decomposition is run on** — i.e. swap their $y$ for my $V_i$/$W^k$ and re-use the index, which is the use the original MD note already proposes.

---

## 6b. Inclusive value and money-metric inversion

**N/A.** The paper uses no inclusive value (no log-sum, no expected maximum), no EV/CV, and performs no money-metric inversion. There is no analytic-in-shocks vs simulation question because there are no extreme-value shocks and no discrete-choice structure. Nothing here maps to my analytic-in-shocks, importance-sampling inversion.

---

## 7. Inequality / decomposition content  [three-way where relevant]

**Inequality index (explicit-in-source, pp. 631–632).** **Mean log deviation $E_0$** (Theil-L; the $\alpha=0$ member of Generalized Entropy), uniquely selected by adding **Foster–Shneyerov (2000) path-independent decomposability** to the standard axioms (symmetry, transfer principle, scale invariance, population replication, additive decomposability). IOL $=\theta_a=E_0(\{\mu_i^k\})$ (eq. 5′); IOR $=\theta_r=E_0(\{\mu_i^k\})/E_0(y)$ (eq. 6′).

**Decomposition rule (explicit-in-source).** **Subgroup / between-group decomposition** of $E_0$ by population subgroups, where subgroups are circumstance types. The "opportunity" component is the **between-type** $E_0$ of the smoothed distribution; the "ethically acceptable" remainder is the **within-type** component (effort + luck + unobserved circumstances). This is a *Theil-L by-subgroup* decomposition, **not** a Shapley, **not** a Shorrocks factor decomposition, **not** RIF, **not** Owen-grouped.

**Counterfactual construction (explicit-in-source, pp. 630–634).**
- *Smoothed distribution* $\{\mu_i^k\}$: replace each individual's advantage with the **type mean** — eliminates all within-type inequality, isolating between-type (opportunity) inequality. (What is *neutralised*: within-type variation.)
- *Standardized distribution* $\{\nu_i^k\}$: rescale by $y_i^k\cdot\mu/\mu^k$ — eliminates all between-type inequality, isolating within-type. (What is *neutralised*: between-type variation.)
- *Partial / circumstance-specific shares* (eqs. 12–13): equalise **one** circumstance while holding the others at their actual values, yielding "partial IORs."

**Order-independence / path-independence / exhaustiveness (explicit-in-source, pp. 631–632).** Path-independent decomposability is the headline property and is what pins the index to $E_0$. For $\alpha\neq 0$ Generalized Entropy measures the two decomposition paths (smoothed vs standardized) do **not** coincide; for $E_0$ they do. This is the cleanest available statement that *the choice of index is not innocuous for a decomposition* — directly relevant to my Shapley-exhaustiveness gate (welfare spec v5 §6(a)), though the mechanism is different (mine is Shapley symmetry/efficiency; theirs is path-independence of a subgroup split).

**Verdict (reusable for my three-way access/ability/preference Shapley–Shorrocks split?).** **Partially — index yes, decomposition architecture no.**
- *Reusable:* $E_0$ as the inequality index; the path-independence justification; the lower-bound logic as a robustness/defence argument; the smoothed/standardized counterfactual logic as the *conceptual* model of "neutralise a source."
- *Not reusable as-is:* the decomposition is **two-way** (opportunity vs residual) and **subgroup-based** (types), whereas mine is **three-way** (access / ability / preference) and **factor-based** (Shapley equalisation of structural channels). To get from theirs to mine you would have to (i) replace circumstance *types* with structural *channels* in $g$ and $v$, (ii) replace the single between/within cut with sequential Shapley equalisations of three factors, and (iii) accept that the path-independence theorem that licenses their unique $E_0$ split does **not** transfer — Shapley order-independence is a different property earned by averaging over equalisation orders, not by Foster–Shneyerov path-independence. **State this explicitly in the draft so the referee does not read the $E_0$ choice as if it also licensed the three-way Shapley split.**

---

## 8. Identification and the separation of preferences from opportunities  [STRICT]

**What identifies tastes vs constraints — and ability vs access within opportunity?** *Nothing, in the structural sense, and the paper is candid about this.*
- There is **no causal identification** (explicit-in-source, the paper repeatedly disclaims causal interpretation; the reduced form $\ln y=C\psi+\varepsilon$ is interpreted as encompassing both direct circumstance effects and indirect effects through effort, pp. 633–634).
- The maintained assumption is that **observed circumstances are exogenous/predetermined** (explicit-in-source, p. 626 and §3). The opportunity/residual split is a **definitional allocation under this assumption**, not an identified behavioural decomposition.
- **Ability vs access is not separated** (derived-by-analogy): there is no wage technology and no feasible-set object, so the within-opportunity structure my JMP cares about simply does not exist here.
- **Preferences are not identified because they are not modelled.** The within-type residual is labelled "effort + luck (+ unobserved circumstances)", *not* "preferences." It is therefore wrong to read their residual as my *preference* channel; it is an undifferentiated remainder.

**The lower-bound result (explicit-in-source, Proposition and Corollary, pp. 635–636).** Adding any omitted circumstance refines the partition and **weakly increases** between-type inequality in the smoothed distribution (by a mean-preserving-spread / transfer-principle argument); the denominator $I(y)$ is invariant to $C$, so IOR is also a lower bound. Hence all estimates based on observed circumstances are **lower bounds** on true inequality of opportunity. This is the paper's identification-substitute: it does not identify the true share, only a floor.

**Transport to my France pooled cross-section (derived-by-analogy).** The honest reading is *cautionary, not enabling*. The paper demonstrates that **without a structural model you cannot separate opportunity from preference at all** — you can only bound an opportunity *share* under an exogeneity assumption on background circumstances I largely cannot even observe in EU-SILC/EUROMOD for France. My identification therefore cannot lean on their machinery; it must come from the **structural functional-form and choice-set restrictions** of the RURO model plus **synthetic-recovery certification** (project state v1 §8, principle 1), exactly because the reduced-form route is unavailable. What I *can* borrow is the **lower-bound rhetorical move** as a defence: even my structural opportunity share can be framed as conservative if some opportunity variation remains unmodelled. Do **not** soften the core point: this paper offers a *measurement* identification story (exogenous circumstances + lower bound), not a *behavioural* one, and the "your decomposition is mechanical" referee is answered in my paper by the structural model and synthetic recovery, not by anything in Ferreira–Gignoux.

**One concrete transferable identification caveat (explicit-in-source, pp. 639–640):** gender is excluded from the household-advantage circumstance set because **household headship and household formation involve choice**, so the head's gender is endogenous and including it would *invalidate the lower-bound claim*. This is a direct warning for my **couples-as-joint-unit** design and my gender-attribution rules (welfare spec v5, A1/A2/A3): household-level gender assignment is not a clean "circumstance," and any opportunity-share statement that conditions on the head's gender inherits an endogeneity that breaks a lower-bound interpretation. Carry this into the identification note.

---

## 9. Key results and magnitudes

All numbers explicit-in-source (Tables 6–9, pp. 643–648), lower-bound shares for the stated populations (heads/spouses aged 30–49). Income covers all six countries; consumption covers five (Brazil has no consumption data).

**Household per capita income — IOR (Table 6, Panel A):**
- Non-parametric: Brazil 0.329, Colombia 0.252, Ecuador 0.283, Guatemala 0.359, Panama 0.338, Peru 0.293.
- Parametric (standardized): Brazil 0.322, Colombia 0.232, Ecuador 0.259, Guatemala 0.335, Panama 0.301, Peru 0.279.
- Range (conclusion, p. 654): IOR ≈ **0.23 (Colombia) to 0.34 (Guatemala)**; IOL ≈ 0.13 (Colombia) to 0.22 (Brazil).

**Household per capita consumption — IOR (Table 6, Panel B):**
- Non-parametric: Colombia 0.265, Ecuador 0.346, Guatemala 0.532, Panama 0.409, Peru 0.351.
- Parametric: Colombia 0.247, Ecuador 0.326, Guatemala 0.514, Panama 0.377, Peru 0.339.
- Headline (abstract, p. 622; results, pp. 643–644): between **one quarter and one half** of consumption inequality is opportunity-related (≈ 0.25 to ≈ 0.51 parametric; up to 0.53 non-parametric, Guatemala).

**Income vs consumption (explicit-in-source, pp. 647):** IOR is *higher* for consumption than income in all five countries, driven by *lower within-type (residual) inequality* in consumption; IOL levels are generally similar or slightly lower for consumption. Interpretation offered: income-based IOR may understate permanent-income opportunity inequality because transitory variance and measurement error inflate the within-type residual and are counted as "effort/luck."

**Parametric vs non-parametric agreement (explicit-in-source, p. 644):** differences never statistically significant; rank-correlation of IOL across methods 0.89 (income), 0.90 (consumption); parametric is the preferred lower bound at small sample sizes.

**Partial (circumstance-specific) IORs (Table 9, pp. 647–648):** family background dominates; **mother's education** is the single largest circumstance (consumption share ≥ 0.16 everywhere, up to 0.29 in Guatemala); father's education generally exceeds ethnicity and birth region. In the *labour-earnings* specification, the **gender** share (after controlling for other circumstances) is small — roughly 0.2% (Colombia) to 5.8% (Guatemala).

**Opportunity-deprivation profiles (Tables 10–11, §6, pp. 649–653):** the worst-off ~10% are sharply concentrated. In **three of six** countries (Brazil, Guatemala, Peru) the opportunity-deprived are **100% ethnic/racial minorities**; mother-without-education exceeds ~90% in every country; agricultural-father and specific birth regions dominate.

**Equivalence-scale robustness (Table 8, pp. 645–646):** Buhmann et al. (1988) scale, $a=0.5$ and $0.75$; IOL falls as scale economies rise; **IOR is stable for income and sometimes higher for consumption** (e.g. Guatemala consumption IOR ≈ 0.54).

**Benchmark value for my own numbers (derived-by-analogy):** these are *outcome* (income/consumption) opportunity shares from *background circumstances*, not *welfare* opportunity shares from a *feasible-set* model. Use them only as a loose order-of-magnitude prior ("opportunity components of 20–50% of an outcome's inequality are not implausible in the broad literature"), **not** as a direct benchmark for my $V_i$-based access/ability shares, which are conceptually different objects.

---

## 10. Estimators, theorems, or formal results

**(R1) Scalar IO indices (eqs. 5′, 6′, p. 632; explicit-in-source).**
$$\theta_a = E_0(\{\mu_i^k\}), \qquad \theta_r = \frac{E_0(\{\mu_i^k\})}{E_0(y)}.$$
- *Assumptions:* $I(\cdot)$ satisfies symmetry, Pigou–Dalton transfer, scale invariance, population replication, additive decomposability, **and** Foster–Shneyerov path-independent decomposability; the smoothed distribution is built on a circumstance partition.
- *Technique:* path-independence uniquely selects $E_0$ within Generalized Entropy; $\theta_a$ is then the between-group Theil-L component, $\theta_r$ its share.
- *Reusability verdict:* **Yes** for the decomposition layer's index choice, applied to my $V_i$/$W^k$ rather than to income. **No** as a stand-in for the Shapley factor split.

**(R2) Lower-bound Proposition and Corollary (pp. 635–636; explicit-in-source).** $\theta_a(\{y,C\})$ is a lower-bound estimator of true $\theta_a^*(\{y,C^*\})$, and $\theta_r$ likewise (denominator invariant to $C$).
- *Assumptions:* observed $C$ is a sub-vector of the true circumstance vector $C^*$; $I(\cdot)$ satisfies the transfer principle.
- *Technique (3–5 bullets):* (i) an unobserved circumstance refines each type cell; (ii) refining a cell replaces a within-cell zero-inequality block with a non-negative-inequality block of the same mean; (iii) this is achievable by mean-preserving spreads; (iv) by the transfer principle between-group inequality weakly rises; (v) the denominator $I(y)$ is unchanged, so the ratio is also a lower bound.
- *Reusability verdict:* **Maybe / rhetorical** — reusable as a *framing* argument that my structural opportunity share is conservative; **not** a theorem about my Shapley decomposition, and I must not present it as one.

**(R3) Roemer strong criterion → van de Gaer weak criterion (eqs. 3–4, pp. 627–629; explicit-in-source).** Equality of opportunity weakened from equality of conditional distributions $F^k(y)=F^l(y)$ to equality of conditional means $\mu^k(y)=\mu^l(y)$.
- *Reusability verdict:* **No** for estimation; **useful** only for the normative-framing section if I discuss ex-ante valuation of opportunity sets by their mean.

No estimator, theorem, or formal result here is reusable for my **estimation** or **welfare-inversion** layers; R1 is the only one reusable for the **decomposition** layer, and only as the index, not the architecture.

---

## 11. Robustness and specification sensitivity

What they vary and what it tells me (explicit-in-source unless flagged):
- **Parametric vs non-parametric (pp. 643–644):** agree closely; supports robustness of the *level* of the share. *For me:* a cheap internal cross-check pattern, not a structural test.
- **Cell sparsity / number of types (pp. 633, 640–642, Table 5):** with $J=5$ circumstances and $K$ up to 108, two countries (Guatemala, Panama) have >25% of cells with <5 observations; sparse cells **inflate** non-parametric between-type inequality, biasing IO **upward**, which is why the parametric route is preferred at small $N$. *For me (derived-by-analogy):* a direct warning about partition coarseness and small-cell noise that maps onto my **effective-sample-size** concern in the welfare integral (welfare spec v5 §6(b)(ii): median ESS ≈ 20/101 for singles) — different mechanism, same lesson: thin cells/weights manufacture spurious dispersion, so report ESS and stress-test against draw/partition refinement.
- **Equivalence scale (Table 8, pp. 645–646):** IOL sensitive, IOR stable/robust. *For me:* supports reporting a *ratio/share* as the more robust object than a *level* — relevant to whether my headline is an opportunity *share* or a *level*.
- **Income vs consumption advantage (p. 647):** the choice of advantage variable materially moves the IOR through the residual. *For me:* a precedent that the *welfare object* choice matters — which is exactly the v5 thesis that the $W^1$–$W^6$ menu spread is itself a result; cite as motivation that the advantage/welfare definition is not innocuous.
- **What they do NOT stress-test:** any opportunity-mechanism specification (there is none), any preference specification (none), any choice-set size or draw count (none). So this section gives me nothing on my recovery/stability gates beyond the partition-sparsity analogy.

---

## 12. What I can cite this paper for

Specific, attributable claims:
1. The relative inequality-of-opportunity ratio is the between-type share of total inequality, and under path-independent decomposability the index is uniquely the **mean log deviation** $E_0$ (pp. 631–632).
2. Inequality-of-opportunity measures based on observed circumstances are **lower bounds** on true inequality of opportunity (Proposition/Corollary, pp. 635–636).
3. Empirically, lower-bound opportunity shares are **large** — roughly one-fifth to one-third of income inequality and one-quarter to one-half of consumption inequality across six Latin American countries (Table 6; abstract).
4. **Family background** (parental education, father's occupation) is the dominant circumstance, with mother's education the single largest partial share (Table 9).
5. Opportunity-deprivation profiles concentrate the worst-off in ethnic minorities and low-parental-education origins (Tables 10–11) — a template for *worst-off-group* identification I could adapt over welfare-type groupings.
6. The ex-ante (van de Gaer, between-type) vs ex-post (Checchi–Peragine, within-tranche) distinction in the **inequality-of-opportunity** literature (pp. 628–629) — for positioning, not for my welfare-integration timing.
7. The methodological point that household **headship/gender is endogenous** and cannot be treated as a clean circumstance for household advantage (pp. 639–640) — for my gender-attribution and couples-unit discussion.

---

## 13. What I should NOT cite this paper for  [overclaim risks]

- **Two-way, not three-way.** Their decomposition is opportunity vs an undifferentiated "effort+luck" residual. Do **not** cite it as support for a three-way {access, ability, preference} split, and do **not** equate their residual with my *preference* channel.
- **Subgroup, not factor/Shapley.** It is a between-/within-subgroup Theil-L decomposition. Do **not** cite it as a Shapley–Shorrocks factor decomposition, and do not let the path-independence theorem be read as licensing my Shapley split (different property, §7).
- **No welfare object.** It computes inequality indices, not welfare. Do **not** cite it for money-metric/equivalent-income welfare, for inclusive-value welfare, or for any $W^1$–$W^6$ measure — **the source contains no $W^1$–$W^6$ object and no equivalent income.** Do not present its income/consumption $y$ as my constrained ex-ante welfare object.
- **No opportunity mechanism.** Its "opportunity" is a circumstance partition, not a feasible set / opportunity density. Do **not** cite it for hours/wage/market availability, for *access* or *ability* as modelled channels, or for occupation-as-availability.
- **"Father's occupation" ≠ occupation/sector opportunity.** It is an intergenerational-origin circumstance. Do **not** read it as my `loc4` (ISCO occupation-as-access), and certainly not as industry/sector (`lindi`/NACE). The source has no contemporaneous occupation or industry object, so there is no sector/industry conflation to attribute — and none to borrow.
- **Lower bound ≠ identified true share.** Do not present their shares (or any I construct in their style) as the *true* opportunity share; they are explicitly floors.
- **Cross-country shares are not country rankings I endorse.** Consistent with my hard boundary, do not let citation of their cross-country table drift my JMP toward a ranking exercise.
- **Theory-paper boundary.** Nothing here is the companion Haydar–Maniquet axiomatic paper; do not attribute any characterisation/uniqueness/proof to the JMP, and do not read the JMP as a theory contribution. (This paper *is* useful precisely as the empirical/measurement tradition the JMP sits in, not as theory.)
- **Deterministic-opportunities framing.** Not implicated either way — the source has no random/deterministic opportunity object — so do not cite it for the "opportunities are deterministic" stance.

---

## 14. Direct quotes worth citing

> **Copyright/extraction note.** The PDF is copyrighted (Wiley-Blackwell notice, final page). I therefore give **page-anchored paraphrases** rather than reproducing multiple verbatim strings, with a single short verbatim phrase where exact wording carries weight. Pull longer verbatim quotes yourself from the PDF if a referee response requires them.

1. **(short verbatim, p. 622)** The measure captures "between-group inequality when groups are defined exclusively on the basis of predetermined circumstances."
2. *(paraphrase, p. 622):* lower-bound opportunity shares range from roughly a quarter to a half of total consumption inequality across the six countries.
3. *(paraphrase, pp. 631–632):* adding path-independent decomposability to the standard axioms restricts the index uniquely to the mean log deviation.
4. *(paraphrase, pp. 635–636):* because any omitted circumstance refines the type partition and cannot lower between-group inequality, the estimates are lower bounds on true inequality of opportunity.
5. *(paraphrase, pp. 639–640):* because headship and household formation involve choice, the head's gender is not a valid circumstance for household-advantage opportunity measurement.
6. *(paraphrase, pp. 643–644):* parametric and non-parametric estimates are statistically indistinguishable, with the parametric route preferred as the conservative lower bound in small samples.

---

## 15. Open questions and risks for my draft

- **The residual is not "responsibility."** The paper's within-type remainder bundles effort, luck, and unobserved circumstances; it is not demonstrated to be responsibility-sensitive. My draft must be careful not to inherit this slippage: my *preference* channel is a modelled object, and whether it is "responsibility-relevant" is a normative stance read off the $W^k$ menu (welfare spec v5 §V3-3), not an identity with a statistical residual.
- **Lower bound vs structural share.** Their lower-bound floor is an artefact of *unmodelled* opportunity. My contribution is to *model* it — so I should frame my opportunity share as addressing the very incompleteness their bound concedes, while acknowledging my own residual unmodelled opportunity (a borrowed lower-bound caveat).
- **Index choice is not innocuous.** Their path-independence result warns that decomposition outputs depend on the index for $\alpha\neq 0$. My Shapley split needs its own exhaustiveness/order-independence guarantee (welfare spec v5 §6(a)); do not assume the $E_0$ uniqueness carries over.
- **Cell-sparsity ↔ ESS.** The small-cell inflation problem is a clean analogue of my thin importance-sampling weights for singles; the risk that **sparse support manufactures spurious between-component dispersion** applies to both, and is a referee-visible threat to any opportunity-share number.
- **Gender/headship endogeneity** directly threatens any gender-conditioned opportunity statement in my couples analysis; resolve in the identification note before reporting gendered shares.
- **Advantage/welfare definition drives the share.** Their income-vs-consumption gap is empirical support for the v5 bet that the welfare-measure menu spread is itself a finding — but it also warns that a reader can move my headline by moving the welfare object, so the $W^1$–$W^6$ spread must be reported transparently, not buried.

---

## 16. TL;DR for retrieval

Ferreira–Gignoux (2011) is the canonical **measurement-and-decomposition** template: it defines absolute/relative inequality-of-opportunity indices as the **between-type share of the mean log deviation**, uniquely justified by path-independent decomposability, proves they are **lower bounds** on true opportunity inequality, and finds large lower-bound shares (≈20–50% of income/consumption inequality) in six Latin American countries — serving my **decomposition** layer (index + lower-bound defence) and **motivation/normative-interpretation**, but **none** of my structural channels. It has **no welfare object** (no money-metric, no $W^1$–$W^6$, no inclusive value), **no opportunity mechanism** (circumstance *types*, not a feasible-set density), and a **two-way subgroup** decomposition (opportunity vs effort/luck residual) that is **not** my three-way {access, ability, preference} Shapley–Shorrocks split — so it anchors *how to measure and bound an opportunity share* while precisely locating the gap my structural opportunity density and money-metric welfare are built to fill.
