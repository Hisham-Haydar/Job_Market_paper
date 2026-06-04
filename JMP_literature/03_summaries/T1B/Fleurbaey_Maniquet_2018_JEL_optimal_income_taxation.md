# Fleurbaey and Maniquet 2018 — Optimal Income Taxation Theory and Principles of Fairness

## 0. Metadata
- **BibTeX key:** FleurbaeyManiquet2018JEL [verify exact key against your .bib]
- **Authors:** Marc Fleurbaey (Princeton University); François Maniquet (CORE, Université catholique de Louvain).
- **Year:** 2018.
- **Outlet:** *Journal of Economic Literature*, Vol. 56, No. 3 (September 2018), pp. 1029–1079.
- **DOI/URL:** https://doi.org/10.1257/jel.20171238 (JSTOR stable URL https://www.jstor.org/stable/10.2307/26494239).
- **PDF filename:** `Fleurbaey_and_Maniquet_-_2018_-_Optimal_Income_Taxation_Theory_and_Principles_of_Fairness.pdf`.
- **Tier:** T1B.
- **JEL codes (explicit in source):** D63, H21, H24, J24.
- **JMP block(s) served:** welfare (money-metric construction and reference choice); normative-interpretation (compensation vs responsibility, libertarian vs egalitarian-equivalent readings); decomposition (only loosely — the source has no inequality-decomposition machinery; it speaks to *what* normative cut a decomposition would operationalise). It does **not** serve estimation, identification, opportunity-mechanism, or data-infrastructure.

**Boundary note (carried through this summary).** This is a *survey of optimal income-taxation theory*. It is **not** the companion Haydar–Maniquet axiomatic theory paper, and it is **not** your empirical JMP. It is, however, the published source that grounds the *money-metric / equivalent-income family* logic your welfare layer relies on. Where I map its objects onto your $W^1$–$W^6$ family, that mapping is **derived-by-analogy** and flagged as such; the paper does **not** contain a $W^1$–$W^6$ classification.

---

## 1. One-paragraph relevance to my JMP
This is the canonical published statement of how fairness principles select among *utility representations* — specifically money-metric utilities $m_i(w,z_i)$ — rather than among social welfare weights, and of how the *choice of reference* (reference wage $\tilde w$, reference labour $\tilde\ell$) encodes a normative position on a compensation–laissez-faire spectrum (explicit in source, §5, §8). That spectrum is the direct conceptual ancestor of your **preference**-vs-opportunity normative cut and of the across-measure spectrum your welfare family is built to traverse: the paper's "compensate unequal skills" vs "let individuals own their skills (laissez-faire/libertarian)" axis maps onto your **ability** (Independence-of-pay) dimension, and its choice of *reference wage* is the lever your ability/access references turn (derived-by-analogy). It speaks most directly to your **ability** channel and to the *reference-choice* logic underneath every $W^k$; it speaks to **access** only indirectly (through the reference-set choice in the public-goods/"implicit budget" extensions). It is a theory survey with one illustrative US calibration, no household microdata estimation, no opportunity density, and no inequality decomposition — so its role for you is normative grounding and citable definitions, not method transport.

## 2. Data and setting
No empirical estimation in the paper's main contribution; it is a theory review. The one quantitative illustration is a **calibration "to resemble the US population"** (explicit, §9.2): 300 household types, wages lognormal with parameters $(\mu,\sigma)=(2.2,0.6)$ chosen to fit 2014 US census pretax-income quintiles under a flat 30% tax; a household treated as 1.66 adults, individual minimum wage \$15,000/yr → household minimum \$25,000; quasi-linear preferences $c - a_i\ell^{1+1/\varepsilon}$ with three $a_i$ values producing 45% full-time / 43% part-time / 12% low-hours at status quo; $\varepsilon=0.5$, status-quo average elasticity 0.26; sixteen tax brackets, max income 500. A separate figure (Figure 6) evaluates the **2013 US income tax for a couple with two children**, budget from the OECD Tax–Benefit Calculator (explicit, §9.1 footnote 49).

**Transport to my France pooled 2015–2017 EUROMOD cross-section:** does **not** transport as a data/estimation setting — it is a calibrated theoretical illustration, not microdata estimation, and uses quasi-linear preferences rather than your Box–Cox block. What transports is the *welfare-construction logic*, not data. Features the paper uses that you do **not** have and do **not** need (it is theoretical): a planner's tax instrument $T(\cdot)$, incentive-compatibility constraints, and a single-good labour–consumption space with a scalar productivity $w_i$. Features you have that it does **not**: an estimated opportunity density, multidimensional access (region, year, occupation), and a discrete latent-jobs choice set. The paper's "agent faces wage $w_i$ and chooses $\ell$ freely on a budget" is a *continuous* labour-supply primitive, **not** your discrete sampled-alternatives latent-jobs set (explicit difference).

## 3. Model and objects (map object-by-object to mine)
- **Choice set.** Theirs: continuous $(\ell,c)$ with $0\le\ell\le1$, $c\ge0$, agent maximises $U_i$ on budget $c=y-T(y)$, $y=w_i\ell$ (explicit, §2). Mine: discrete sampled latent-jobs set $\mathcal C_i$. **Not the same object** — continuous budget vs sampled discrete alternatives.
- **Deterministic utility.** Theirs: $U_i(\ell,c)$, continuous, quasi-concave, nonincreasing in $\ell$, increasing in $c$ (explicit, §2). Maps to my preference utility $v$ in *role* (the preference-respecting core), but mine is Box–Cox over consumption/leisure/children-time with demographic shifters; theirs is general in §2 and quasi-linear $c-a_i\ell^{1+1/\varepsilon}$ in the §9 calibration. Correspondence is **by-analogy at the level of "ordinal preferences over labour–consumption"**, exact functional form differs.
- **Opportunity / availability mechanism analogous to my $g$.** **Not present.** The paper has no probabilistic opportunity density, no offer/availability mechanism, no separation of hours / wage(ability) / market / occupation availability channels. Heterogeneity enters only through a scalar productivity $w_i$ and preferences $U_i$ (explicit, §2). The closest analogue to your *ability* dimension is the scalar wage $w_i$ entering the budget; there is **no** analogue to your *access* dimension (hours/employment/region/year/occupation availability). This omission is exactly the gap your opportunity layer fills (derived-by-analogy; not-established in source).
- **Budget map.** Theirs: $c=y-T(y)$, an analytic tax function (explicit). Mine: EUROMOD-simulated disposable income at each alternative. Different construction; same role (the consumption a labour choice yields).
- **Does any job attribute enter BOTH utility and an opportunity mechanism?** Not applicable — there is no opportunity mechanism, so no double-entry risk arises in the source. (Your discipline of keeping occupation out of utility has no counterpart here because the paper has no occupation variable at all.)

## 4. Estimation method
**Not applicable as an estimator.** The paper derives optimal-tax formulas and evaluates reforms; it does not estimate a structural model from microdata. The §9 illustration computes optimal *piecewise-linear* taxes (16 brackets) for a calibrated population, noting that with many agents at full-time the first-order Mirrleesian formula (their eq. labelled (3), the Jacquet–Lehmann form) cannot be applied, so they optimise piecewise-linear taxes directly (explicit, §9.2 and footnote 54).

- **Choice-set construction / sampled alternatives / proposal density:** **none** — continuous model, no sampling of alternatives, no importance sampling.
- **Prior/proposal ($-\log\pi$) correction:** **not present** and not applicable (no discrete sampled choice set). Do **not** cite this paper for anything about the sampling-of-alternatives correction.
- **Normalisation / scale / what pins preferences vs opportunities:** the paper's central methodological claim is orthogonal to estimation — it is that the *utility representation* (the money-metric index) must be *chosen on ethical grounds*, because least-concave (Atkinson) calibration is defined only up to scaling once preferences are heterogeneous (explicit, §3). There is no "separate preferences from opportunities" identification problem in the source because there is no opportunity mechanism to separate from.
- **Verdict — reusable for my RURO/JAX pipeline?** **No** for estimation machinery. **Yes, conceptually**, for the welfare layer's *reference-choice* step: the money-metric definition and the reference-wage/reference-labour parameterisation are directly reusable as the normative scaffolding for choosing each $W^k$'s reference (name the step: the one-dimensional own-utility inversion to a money figure is exactly their "implicit budget at reference wage $w$" construction).

## 4b. Proposal / sampling-of-alternatives correction
**N/A.** Continuous model; no sampling of alternatives, no proposal density, no McFadden-style correction, no per-alternative log-prior. Nothing in this paper bears on your importance-sampling integrator or your proposal-individualisation concern.

## 5. Opportunity mechanism  [MOST IMPORTANT — but largely absent here]
**There is no explicit opportunity mechanism in this paper.** Feasibility of jobs/hours/wages/occupations is **not** modelled as a density, offer probability, or participation restriction. The model is a standard Mirrleesian one in which:
- each agent has a **scalar productivity $w_i$** (the wage when working full time) and chooses labour freely on the tax-induced budget (explicit, §2);
- there is a labour bound $0\le\ell\le1$ (explicit, §2), which matters for the money-metric definitions but is not an availability constraint in your sense.

Mapping to my three sub-objects:
- **access** (hours / market-participation / region / year / occupation offers): **no analogue.** The agent can choose any $\ell\in[0,1]$; there is no restricted feasible set, no regional/temporal/occupational availability. (not-established in source)
- **ability** (wage technology, returns to education/experience, residual dispersion): the scalar $w_i$ is the *only* productivity object; it is **exogenous and one-dimensional**, with **no** Mincer-type returns to education/experience and **no** residual productivity dispersion parameter. The paper's compensation-vs-laissez-faire debate is *about* whether inequality in $w_i$ should be compensated — which is the normative content of your **ability** dimension — but the source does not *model* how $w_i$ is generated. (Mapping of the *normative stance* to your ability channel is derived-by-analogy; the *mechanism* is not-established.)
- **occupation as availability vs something else:** **no occupation variable.** No sector/industry either. There is therefore **no** conflation risk in the source, and nothing here licenses any "occupation-as-access" claim — that is your construct, not theirs.

**What the omission costs my access/ability/preference decomposition:** the paper cannot supply any access-side content; it is purely a preference-vs-ability (compensation-vs-responsibility-for-skill) source. Use it to ground the **ability/preference** boundary and the responsibility framing, **not** the access channel.

## 6. Welfare object — and its place on my $W^1$–$W^6$ map
**Yes, the paper computes welfare**, and this is its core relevance. The central object is the **money-metric utility** $m_i(w,z_i)$, attributed to Samuelson (1974) (explicit, §5.2):
$$
m_i(w,z_i)=\min\{t\in\mathbb R \mid \exists(\ell,c)\in X,\; c=t+w\ell,\; U_i(\ell,c)\ge U_i(z_i)\},
$$
i.e. the lump-sum transfer (negative = tax) leaving agent $i$ indifferent between her bundle $z_i$ and freely working at reference wage $w$ (explicit, §5.2). Key properties stated in source:
- once $w$ is fixed, $m_i(w,\cdot)$ is a **numerical representation of $i$'s own preferences** (explicit, §5.2 and its footnote on nestedness) — i.e. it is *preference-respecting*, exactly your requirement.
- the **reference wage $w$ need not be the agent's actual wage** (explicit, §5.2). This is the lever.

It is **money-metric** (yes), an **equivalent-income–type** object (the "implicit budget at reference wage $w$" is the budget that would give $i$ utility $U_i(z_i)$; explicit, §5.2). Defined over a **reference budget**, not over a constrained feasible set in your sense — the reference is a *wage-and-lump-sum* budget, parameterised by $w$ (and, in the generalisation, by reference labour $\tilde\ell$ and reference preferences). The paper is a **first-best / second-best deterministic** model, so the discrete-choice subtleties (log-sum aggregation, selection of chosen alternative, integration over EV shocks, ex-ante vs ex-post) **do not arise** — there are no random utility shocks and no inclusive value. (This is a major structural difference from your object; see §6b.)

Two reference choices generate the spectrum (explicit, §5, §8):
- **$m_i(\tilde w, z_i)$ with a common reference wage $\tilde w$** = the *reference-wage egalitarian-equivalent* family (Pazner–Schmeidler egalitarian-equivalence; explicit, §5.4 and footnote 25). With $\tilde w$ common across agents, this **compensates skill inequality** among same-preference agents.
- **$m_i(w_i, z_i)$ at the agent's own wage** = the **libertarian** index, which lets skilled agents keep their advantage (explicit, §5.2, §5.5, §8.1.2).
- a **convex combination** $\tilde w_i=\lambda\tilde w+(1-\lambda)w_i$ and a **reference-labour** generalisation $m_i(\tilde w_i,z_i)+\tilde w_i\tilde\ell$ (the Kolm (2004) index) span the intermediate cases (explicit, §8.1.2–§8.1.3).

**Locating the paper on my $W^1$–$W^6$ map (derived-by-analogy; the paper does NOT contain $W^1$–$W^6$):**
- The paper's **egalitarian-equivalent** index $m_i(\tilde w,z_i)$ (common reference wage, compensate skill) corresponds in *spirit* to the **Independence-of-pay / compensate-pay** stance — i.e. the side your $W^5$ (compensate the set, responsible for pay) and $W^1$ (compensate pay) duals separate. The single-parameter $\tilde w$ in the source does **not** separate access from ability the way your two-axis (Ind-$y$, Ind-$A$) menu does, because the source has no access dimension; so the correspondence is to the **ability/pay** axis only.
- The paper's **libertarian** index $m_i(w_i,z_i)$ (+$w_i\tilde\ell$) corresponds in spirit to your **Full-Responsibility** end (own your pay/skill) — i.e. the stance behind your $W^2$/$W^3$.
- The paper's **$\lambda$-intermediate and $\tilde\ell$-intermediate** indices correspond to the *interior* of your compensation–responsibility spectrum.

**Crucial caveats on this mapping.** (a) The paper's spectrum is **one-dimensional** (compensate-skill ↔ own-skill, tuned by $\tilde w$, $\lambda$, $\tilde\ell$); your family is **two-dimensional** (Ind-$y$ × Ind-$A$), because you add an access axis the source lacks. (b) The paper's object is **deterministic and ex-post-free** (no shocks, no set), whereas your $W^k$ are **ex-ante inclusive-value** objects reading attained utility $V_i$ over a feasible set. So the source grounds the *reference-choice normative logic* but **not** the ex-ante/inclusive-value construction. **Verdict: adaptable (for the reference-choice and responsibility-framing layer), incompatible (as a literal welfare object), because the source is deterministic-continuous and single-axis.**

## 6b. Inclusive value and money-metric inversion
- **Inclusive value (log-sum / expected maximum):** **not used.** The paper has no random-utility shocks; welfare is the deterministic money-metric $m_i$, obtained by a **one-dimensional construction** (find the lump-sum $t$ equating $U_i$ on the reference budget to $U_i(z_i)$) — explicit, §5.2. This *one-dimensional inversion of the own-utility map* is structurally the same kind of operation as your one-dimensional bracketing root-solve, and is the legitimate citable precedent for "invert own utility to a money figure, do not use a closed-form shortcut that bypasses the household's preferences." (derived-by-analogy for the *inversion step*; explicit that $m_i$ represents own preferences.)
- **Expectation over shocks analytic vs simulated:** **N/A** — there are no shocks in the model.
- **Relation to my analytic-in-shocks importance-sampling inversion:** the *inversion-to-money* idea transports; the *expectation-over-shocks* and *integration-over-a-set* parts have no counterpart here. Cite for the inversion principle; do **not** cite for anything about inclusive value or shock integration.

## 7. Inequality / decomposition content
- **Inequality index:** the paper uses **maximin / leximin** social-ordering functions applied to the well-being indices $m_i(\tilde w_i,z_i)+\tilde w_i\tilde\ell$ (explicit, §5, §6, §9), and discusses general inequality-averse social welfare functions $W(\cdot)$ and weighted-utilitarian $\sum_i\alpha_i U_i$. It does **not** use Gini / MLD / Theil / Atkinson indices, and does **not** report an inequality *number* for a population.
- **Decomposition rule:** **none.** There is **no Shapley, Shorrocks, factor-component, RIF, or subgroup decomposition** in this paper. Do **not** cite it for any decomposition method. (not-established in source)
- **Counterfactual construction:** the paper's "what is equalised / held responsible" logic is encoded in the *reference choice* (which inequalities the index treats as compensable), not in a counterfactual decomposition. The relevant normative content: a common reference wage $\tilde w$ → compensate skill inequality; own wage $w_i$ → hold agents responsible for skill (explicit, §8).
- **Order/path-independence/exhaustiveness:** **N/A** — no decomposition, so no Shapley properties discussed.
- **Verdict — reusable for my three-way access/ability/preference Shapley–Shorrocks split?** **No** as a decomposition method. **Yes** as the *normative justification* for *which* cut a decomposition should make and *why* anchoring matters: the paper establishes that the compensate/responsibilise distinction is a *choice of utility index*, which is precisely why your decomposition is measure-dependent and must be anchored on non-pre-absorbing measures. The paper is at most a **two-way** (compensation vs responsibility-for-skill) normative source, and it covers only your **ability/preference** boundary — it says nothing about **access**, so it cannot be extended to your third channel from its own content; you would supply the access axis entirely from elsewhere.

## 8. Identification and the separation of preferences from opportunities  [STRICT]
The paper's "identification" is **normative-philosophical, not econometric.** It does **not** identify tastes vs constraints from data; it argues that *once* preferences and skills are known (assumed observable in the theory), the ethical question is which utility *representation* to use (explicit, §3, §8). Concretely:
- It establishes that with **heterogeneous preferences**, least-concave (Atkinson) calibration is defined only up to a scaling factor and is therefore not directly comparable — so additional **ethical** assumptions are needed to fix interpersonal comparisons (explicit, §3). This is the source's core "identification" point: *interpersonal comparability is a normative choice, not a measurement.*
- It does **not** offer an exclusion restriction, choice-set variation, panel argument, or external opportunity shifter. There is no empirical identification of an opportunity mechanism because there is no opportunity mechanism.

**Transport to my France pooled cross-section (no panel, no external instrument):** the paper offers **no** econometric identification strategy you can borrow. What it does give you — and this is load-bearing for your defence against the "your decomposition is mechanical" referee — is the *principled* statement that the compensation/responsibility boundary is a **normative choice of utility index**, not a fact to be read off the data. That reframes the referee challenge: the decomposition's *anchor* is an explicit ethical stance (citable to this paper), not an arbitrary modelling convenience. It does **not**, however, defend the *separation of access from preferences in the data* — that identification burden is yours and is not addressed here. The paper relies on assumed-observable preferences/skills, **not** on synthetic-recovery or parametric-identification arguments (so it does not speak to your synthetic-recovery certification standard).

## 9. Key results and magnitudes
Headline analytical results (explicit in source):
- **Money-metric → laissez-faire optimality.** With $G=0$ and own-wage money-metric $m_i(w_i,z_i)$, the laissez-faire allocation achieves $m_i=0$ for all $i$ and any redistribution makes some $m_i<0$; under an inequality-averse (incl. maximin) $W$, laissez-faire is among the best feasible allocations (explicit, §5.2). With a fixed budget $G$, the same ordering recommends an equal poll tax $G/n$ (explicit, §5.2).
- **Zero marginal tax on low incomes under the $m_i(w_{\min},z_i)$ maximin criterion**, with Saez's formula and zero weight above $w_{\min}$ (explicit, §7; eqs. on $T'(y)$).
- **Weighted utilitarianism cannot generally mimic fair indices** — Pareto weights $\alpha_i$ would have to depend on the whole population profile and on the allocation being evaluated, so they cannot be guessed before solving and cannot reliably rank suboptimal allocations (explicit, §6).
- **§9 calibration (US-like):** utilitarian optimal marginal-rate patterns shift from inverted-U → declining → U-shaped (Diamond 1998) as inequality aversion $\rho$ rises (explicit, Figure 7). Egalitarian-equivalent and libertarian optimal taxes shown in Figure 8 for various $\tilde w$ and $\tilde\ell$. The 2013 US tax (couple, two children) resembles a libertarian criterion with $\tilde\ell\approx0.4$ (explicit, §9.1, Figure 6); the threshold $\tilde\ell=0.439$ is where priority flips between top and low incomes (explicit, §9.1).

**Benchmarking value for my numbers:** **limited and indirect.** These are theoretical/optimal-tax magnitudes, not welfare-inequality shares or opportunity shares, so they do **not** benchmark your opportunity share or welfare spread. Do not import any number here as a plausibility check on your decomposition.

## 10. Estimators, theorems, or formal results
The paper is a survey and states no labelled theorems with proofs; it presents *constructions* and *results from the fair-social-ordering literature*. Reusable formal objects:

1. **Money-metric utility (Samuelson 1974), as stated in §5.2:**
   $$m_i(w,z_i)=\min\{t\in\mathbb R\mid \exists(\ell,c)\in X,\;c=t+w\ell,\;U_i(\ell,c)\ge U_i(z_i)\}.$$
   *Assumptions:* $U_i$ continuous, quasi-concave, nonincreasing in $\ell$, increasing in $c$; labour bound $\ell\in[0,1]$. *Technique:* nestedness of $\{c\le t+w\ell\}$ in $t$ ⇒ $m_i(w,\cdot)$ represents $i$'s preferences. *Reusability verdict:* **Yes** — this is the citable definition for your equivalent-income inversion; reuse for the welfare-layer reference-budget step.

2. **Generalised index (Kolm 2004), §8.1.2:** $m_i(\tilde w_i,z_i)+\tilde w_i\tilde\ell$ with $\tilde w_i=\lambda\tilde w+(1-\lambda)w_i$. *Role:* parameterises the compensation–laissez-faire spectrum by $(\lambda,\tilde\ell)$. *Reusability verdict:* **Maybe/adaptable** — it is the one-axis analogue of your reference choices; cite to justify that "reference wage + reference labour" is a principled, literature-grounded parameterisation, but note your two-axis menu generalises it.

3. **Reference-wage egalitarian-equivalent social ordering, §5.4:** $\min_{i} m_i(\tilde w,z_i)$, with the special pairwise-compensation / pairwise-laissez-faire properties and the recommendation $\tilde w=w_{\min}$ (justified by participation-constraint and endogeneity arguments, §8.1.4). *Reusability verdict:* **Yes** for normative grounding of a reference-wage choice; **No** as an estimator.

4. **Income-weighting / Saez reform result with zero weights above $w_{\min}$, §7.** *Reusability:* **No** for your JMP (it is optimal-tax, not welfare-measurement), beyond citing the general point that maximin concentrates positive weight on the worst-off index value.

(No theorem numbers exist to cite; do not invent any.)

## 11. Robustness and specification sensitivity
What the paper varies (explicit, §8–§9):
- **Reference wage $\tilde w$** (low → favours work-averse agents; high → favours hardworking; $\tilde w=w_{\min}$ singled out for participation-constraint and endogeneity reasons).
- **Reference labour $\tilde\ell$** (0 = pure libertarianism; →1 = "slavery of the talented", penalising the more productive — explicit, §9.2, citing Dworkin 1981b).
- **$\lambda$** (0 = libertarian, 1 = egalitarian-equivalent).
- **Inequality aversion $\rho$** in the utilitarian SWF (Figure 7).
- **Choice of cardinalisation** for utilitarian comparisons (intercept utilities $c-a_i\ell^{1+1/\varepsilon}$).

**What this tells me to stress-test:** the paper's central robustness lesson — that welfare *rankings and optimal policy move materially with the reference choice* — is exactly the empirical bet behind your family-as-headline thesis. It motivates reporting the **across-measure spread** as a first-class object and stress-testing the **reference-wage / reference-set choice** in your welfare family. It does **not** speak to choice-set size, number of draws/starts, effective-sample-size, or circumstance partitions (those are estimation-side concerns absent here).

## 12. What I can cite this paper for
- The **definition of money-metric / equivalent-income utility** $m_i(w,z_i)$ and the fact that, with $w$ fixed, it is a **preference-respecting** numerical representation of the agent's own preferences (§5.2). [explicit]
- That the **reference wage** is a free normative parameter that need not equal the agent's actual wage (§5.2). [explicit]
- That **fairness principles operate by selecting the utility index** (the scaling/representation), which keeps them compatible with the Pareto principle, rather than by weighting given utilities (§5.1, §6). [explicit]
- The **compensation vs laissez-faire (libertarian)** distinction as the normative axis underlying reference choice, with the egalitarian-equivalent ($\tilde w$ common) vs libertarian ($w_i$ own) endpoints (§5.2–§5.4, §8). [explicit] — use to ground your **ability/preference** (Independence-of-pay) cut.
- That **weighted utilitarianism / Pareto weights cannot transparently encode fairness** and cannot in general mimic fair money-metric orderings (§6). [explicit] — supports preferring an explicit equivalent-income family over weighted-SWF approaches.
- **Roemer's equality-of-opportunity** circumstance/effort partition and its money-metric reading (§5.3, §5.5). [explicit] — citable for the responsibility framing, with care (see §13).
- The **four ethical choices** guiding utility-index selection (subjective vs ordinal; compensate skill vs own skill; prioritise skill-inequality vs equal tax treatment; favour high vs low work-aversion) (§8.1). [explicit] — a clean menu to cite when motivating your reference choices.
- That **reference-choice materially shifts welfare/policy conclusions** (the whole §8–§9 spectrum). [explicit] — motivation for the family-as-headline design.

## 13. What I should NOT cite this paper for  [overclaim risks]
- **NOT a three-way (access/ability/preference) decomposition** — it has **no decomposition at all**, and its normative axis is **two-way at most** (compensate-skill vs own-skill). It is silent on **access**. Do not attribute any access-channel content to it.
- **NOT an inequality-decomposition or Shapley/Shorrocks source.** No factor decomposition, no inequality index numbers.
- **NOT an ex-ante / inclusive-value welfare source.** Its money-metric is **deterministic and ex-post-free**; do not present its $m_i$ as if it were your ex-ante inclusive-value object over a constrained feasible set. (Your $W^k$ read attained utility $V_i$ over a set; the source's $m_i$ reads a single bundle $z_i$.)
- **NOT a random-opportunity source and NOT an opportunity-mechanism source.** No opportunity density, no offer probabilities, no feasible-set restriction. Consistent with your deterministic-opportunities framing, but the source simply has no opportunity object to cite.
- **NOT a source containing your $W^1$–$W^6$ family.** The six-measure, two-axis (Ind-$y$ × Ind-$A$) classification is your companion Haydar–Maniquet theory paper's construct, not this 2018 JEL paper's. Cite the *money-metric and reference-choice primitives* here; cite $W^1$–$W^6$ to the companion paper only.
- **NOT a sampling-of-alternatives / $-\log\pi$ correction source.** Continuous model; nothing on proposal correction or importance sampling.
- **NOT an estimation/identification source.** No microdata estimation, no econometric identification of preferences vs opportunities; its "identification" is the normative claim that interpersonal comparability is a value choice.
- **NO "sector"/"industry" or "occupation" content** to import — the model has no occupation or industry variable, so it cannot support any occupation-as-access (or any sector) claim.
- **Theory-paper boundary:** do not attribute the companion Haydar–Maniquet axioms, characterisation, or proofs to this survey, and do not read this survey as itself supplying your JMP's normative characterisation. It is the *published primitive* (money-metric + compensation/laissez-faire spectrum); the characterisation of your specific family is elsewhere.

## 14. Direct quotes worth citing
[Short verbatim quotes with page numbers; each kept brief.]
- p. 1037: "the traditional concept of money-metric utilities is convenient and surprisingly versatile" — on money-metric flexibility. [verify page; appears in §3 closing]
- p. 1042 (§5.2): money-metric is "the lump-sum transfer (negative if it is a tax) that leaves agent $i$ indifferent". [verify exact page]
- p. 1038 (§4, footnote 11): "compensation reflects the goal of eliminating the inequalities due to all causes other than preferences." [verify page]
- p. 1049 (§5.4): the money-metric "respects individual preferences while using an objective measuring rod to compare individual situations." [verify exact page]
- p. 1049 (§5.4, footnote, quoting Deaton 1980): welfare measurement should be "fundamentally based on opportunities rather than on their untestable consequences." [verify page]
- p. 1073 (§10): "individual utility indexes are malleable tools that can incorporate many of the fairness considerations". [verify page]

*(All page numbers above are flagged [verify] against the PDF pagination 1029–1079; quote them only after confirming the exact printed page, as the PDF interleaves two-column text.)*

## 15. Open questions and risks for my draft
- **Single-axis vs two-axis gap.** The source's spectrum is tuned by scalar $\tilde w$, $\lambda$, $\tilde\ell$; your family adds an *access* axis with no counterpart here. Risk: a referee may say your normative scaffolding is "just Fleurbaey–Maniquet money-metric." You must articulate clearly that the **access dimension (Ind-$A$) is your addition**, not in the source, and is what the opportunity layer earns.
- **Deterministic vs ex-ante.** The source's money-metric reads a realised bundle; your object is ex-ante over a set. You should state explicitly that you adopt the *reference-choice logic* from this literature but compute it on an inclusive-value attained utility — and that the access channel enters *through attainment* under every measure (your §5.1 point), which has no analogue here.
- **Preference-respecting inversion is well-grounded** (this paper) — but the *uniqueness/ comparability* concerns the source raises (least-concave defined only up to scaling under heterogeneous preferences, §3) are a live risk for *your* interpersonal comparisons too; ensure your reference choice pins comparability the way $\tilde w$ does here.
- **Responsibility-for-preferences caveat.** The source notes (§5.3, §5.4) the uneasy route of treating preferences as possibly "distorted" and using *ideal* preferences (dropping Pareto). Your design treats preferences as preference-respecting; flag that you deliberately do **not** take the ideal-preferences route, and cite this paper for why that route is contested.

## 16. TL;DR for retrieval
Fleurbaey–Maniquet (2018, *JEL*) is the published normative grounding for your **welfare layer's reference-choice logic and the ability/preference (compensation-vs-responsibility) axis**: it defines money-metric / equivalent-income utility $m_i(w,z_i)$ as a preference-respecting representation whose **reference wage encodes whether skill inequality is compensated (egalitarian-equivalent, common $\tilde w$) or owned (libertarian, own $w_i$)**, and argues fairness must select the utility *index* rather than weight given utilities. It has **no opportunity density, no access channel, no inclusive value, no sampling correction, and no inequality decomposition**, so cite it for the money-metric primitive and the responsibility framing — **never** for access content, ex-ante construction, or your $W^1$–$W^6$ family (which belong to the companion theory paper and your own design).
