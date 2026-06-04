# Bargain, Decoster, Dolls, Neumann, Peichl & Siegloch 2013 — Welfare, labor supply and heterogeneous preferences: evidence for Europe and the US

> Retrieval-oriented T1A summary for *"Unequal Job Opportunities and Well-Being
> Inequality: A Latent-Jobs Structural Decomposition"* (Haydar 2026). Source of
> truth: the attached PDF. Page numbers refer to the journal pagination
> (789–817) as printed on the PDF pages. Convention: **explicit-in-source** =
> stated in the paper; **derived-by-analogy** = my mapping to the JMP, not the
> paper's claim; **not-established** = the paper does not do this.

---

## 0. Metadata

- **BibTeX key:** `Bargain_et_al_2013`
- **Authors:** Olivier Bargain; André Decoster; Mathias Dolls; Dirk Neumann; Andreas Peichl; Sebastian Siegloch.
- **Year:** 2013 (received 3 Nov 2011; accepted 8 Oct 2012; published online 19 Oct 2012).
- **Outlet:** *Social Choice and Welfare*, vol. 41, pp. 789–817. Issue number 41(4) [verify — only the volume and page range are printed on the PDF].
- **DOI:** 10.1007/s00355-012-0707-x (p. 789).
- **PDF filename:** `Bargain_et_al_2013_Welfare__labor_supply_and_heterogeneous_preferences.pdf`
- **Tier:** T1A.
- **JMP block(s) served:** welfare (primary); estimation; normative-interpretation; data-infrastructure; motivation. **Does not** serve opportunity-mechanism (access/ability) or decomposition design in my sense — see §5, §7, §13.

---

## 1. One-paragraph relevance to my JMP

This is the canonical empirical statement of the preference-respecting,
money-metric **equivalent-income** welfare programme on EUROMOD discrete-choice
labour supply, and my welfare layer is the same construction lineage (King 1983;
Fleurbaey 2006, 2008): a single estimated Box–Cox preference, a *menu* of
money-metric references, and the spread across the menu as the object of
interest. It speaks directly to my **preference** channel and to the welfare
object's computational core (deterministic-utility indifference curves, expected
utility over the random-utility distribution, tangency-search inversion). Its
normative menu — "rent", "rent + reference wage", "wage" — is a
compensation–responsibility spectrum, but the axis is **responsibility for
work preferences (willingness-to-work)**, which is near-orthogonal to my
Independence-of-pay / Independence-of-access axis; the three metrics are
therefore *not* my $W^1$–$W^6$ and must not be presented as such (§6, §13). Its
load-bearing relevance for the JMP's *motivation* is its own concession that the
model omits demand-side opportunity constraints and that estimated
country-specific "preferences" plausibly absorb opportunity/institutional
differences — precisely the conflation my opportunity layer exists to undo.

---

## 2. Data and setting

- **Countries/years:** 11 European countries (AT, BE, DK, FI, FR, GE/DE, IE, NL, PT, SW, UK) plus the US (p. 790, fn. 1). EU microdata are tied to tax-benefit systems for **1998 or 2001** (p. 800); the US uses **2006 IPUMS-CPS** data covering income **year 2005** (p. 800). France in their data is a single cross-section circa **2001** (Table 1, p. 802).
- **Dataset:** harmonised household surveys combined with national tax-benefit simulation, as described in Bargain et al. (2012) for the EU; IPUMS-CPS for the US (p. 800). [The specific EU survey per country is listed in the Acknowledgements, p. 815: ECHP / EU-SILC and national equivalents; FR is the INSEE EBF — explicit-in-source.]
- **Sample unit:** "unitary" household; **couples treated as a single decision maker**, with the analysis modelling **married women's** labour supply and **husbands' hours held fixed** (p. 798). Sample restricted to households where husbands work $\geq 30$ h/week, women aged 18–59 and available for the market (p. 800).
- **Sample size:** **42,975 households** pooled across countries (Table 1 note, p. 802).
- **Key variables:** household net income, non-labour income (incl. husband's earnings), female hourly wage, female weekly hours, participation (Table 1, p. 802). Taste-shifters $z_i$: ages of both spouses, woman's education, children <3 / 3–6 / 7–12, region (p. 799, eq. 6).
- **Budget set:** net income $c_{ij}=f(w_i h_{ij}, I_i, x_i)$ computed at each discrete hours point by **EUROMOD** (EU) and **TAXSIM** (US) (p. 800). Female wages **predicted for all observations** with a standard selection-bias correction (p. 800).
- **Discretisation:** $J=7$ hours categories — non-participation, two part-time, two full-time, two over-time, spanning 0–60 h/week in steps of 10 h (p. 800).

**Transport to my France pooled 2015–2017 EUROMOD cross-section.** Strong on the
welfare-and-budget machinery: same EUROMOD disposable-income budget construction,
same Box–Cox discrete-choice family, and France is one of their countries (FR
2001). Weak on unit and scope: they are **married women, couples-as-unitary with
the husband fixed**, a single cross-section per country; my baseline is **three
groups (single males, single females, couples as a *joint* two-decider unit),
pooled across 2015/2016/2017**. Features they do **not** have, and that I also
do not have (so no advantage transfers): panel, administrative match, external
opportunity instrument, vacancy/offer data. Their cross-country dimension is
irrelevant to my within-France design.

---

## 3. Model and objects (object-by-object map to mine)

- **Choice set.** Fixed, **common** grid of $J=7$ hours alternatives (p. 800). This is **not** my latent-jobs set: it is a universal hours grid, not a household-specific feasible-job distribution. *(not-established: any household-specific feasible set.)*
- **Deterministic utility = my preference utility $v$.** Box–Cox over consumption and leisure (p. 798, eq. 5):
$$
u_i\big(c_{ij},\,T-h_{ij}\big)=\beta_c\,\frac{c_{ij}^{\alpha_c}-1}{\alpha_c}+\beta_{li}\,\frac{(T-h_{ij})^{\alpha_l}-1}{\alpha_l}.
$$
  Same functional family as my preference block; monotonicity/concavity hold under $\beta_c,\beta_{li}>0$, $\alpha_c,\alpha_l<1$ (p. 799), which is exactly why they (and I) use Box–Cox for tangency-based welfare. **Explicit-in-source.**
- **Random utility.** $V_{ij}=u_i(c_{ij},T-h_{ij})+\varepsilon_{ij}$ with i.i.d. EV-I shocks, giving conditional-logit choice probabilities (p. 798–799, eq. 4). My RURO per-alternative value adds opportunity-density terms and a proposal correction that this model does **not** contain (see §4, §5).
- **Opportunity / availability mechanism analogous to my $g$.** **None.** There is no opportunity density, no offer probabilities, no participation/hours-availability sub-block, no occupation channel. Opportunities enter *only* through the budget (wages + tax-benefit). They state plainly that they "do not model potential demand side restrictions on the labor market nor fixed costs of work" (p. 799). **Explicit-in-source (the absence is stated).**
- **Budget map = my EUROMOD disposable income.** Yes, in spirit: $c_{ij}=f(\cdot)$ via EUROMOD/TAXSIM = my `ils_dispy`-based consumption. **Explicit-in-source.**
- **Heterogeneity.** Country-specific deep parameters $(\alpha_c,\alpha_l,\beta_c,\beta_{l0})$ estimated separately per country; within-country household heterogeneity only through the leisure intercept $\beta_{li}=\beta_{l0}+\beta_{lz}z_i$ (p. 799, eq. 6). All systematic between-household variation is loaded into the **preference** block. **Explicit-in-source.**
- **Does any job attribute enter BOTH utility and the opportunity mechanism?** N/A — there is no opportunity mechanism, so the both-sides flag cannot fire. The structurally relevant observation for me is the *converse*: everything (including whatever is truly opportunity-driven) is absorbed into utility, by construction. **Derived-by-analogy (the implication for my taxonomy).**

---

## 4. Estimation method

- **Likelihood/estimator.** Conditional-logit maximum likelihood (McFadden 1974); EV-I shocks deliver closed-form logistic choice probabilities; estimated **separately by country** (p. 799). **Explicit-in-source.**
- **Choice-set construction.** Fixed common grid of $J=7$ alternatives — **not** sampled alternatives, no fixed-grid-of-draws (p. 800). **Explicit-in-source.**
- **Proposal/sampling density; prior/proposal correction.** **None** — because the grid is enumerated, not sampled, there is no McFadden sampling-of-alternatives correction and **no $\log(\text{prior})$ term**. **Explicit-in-source (by construction of the enumerated grid).** This is a first-order contrast with my RURO engine (§4b).
- **Normalisation/scale.** Standard logit scale via the EV-I assumption; consumption scale carried by $\beta_c$ (estimated, not normalised to 1 here — contrast with my `beta_c=1`). **Explicit-in-source.**
- **Numerical method / starting values / multistart.** Not detailed in the printed text [verify — likely in Bargain et al. 2011/2012 companions]. **Not-established here.**
- **What pins preferences separately from the opportunity mechanism.** Nothing — there is no opportunity mechanism to separate from. Preferences are identified from observed choices over nonlinear tax-benefit budgets (van Soest logic; see §8). **Explicit-in-source.**

**Verdict (reuse for my RURO/JAX pipeline):** *partial / how* — the
**estimator is too thin** (a pure hours-grid conditional logit with no $g$ and no
proposal correction is the model my design departs from). What is reusable is the
**utility block** (Box–Cox specification and its tangency-friendly properties)
and the **welfare-computation steps** (§6, §6b), not the estimation architecture.

---

## 4b. Proposal / sampling-of-alternatives correction

**Not applicable / not present.** The model enumerates a common $J=7$ hours grid,
so there is no proposal distribution, no per-alternative log-prior, and no
McFadden correction (p. 800). There is consequently nothing to "individualise":
the only individualised input is the **predicted female wage** (Heckman-corrected,
p. 800), which feeds the *budget*, not a sampling proposal. **Relevance to my
importance-sampling welfare integrator:** none as a method to import; the value is
as the **null model** — it shows that the standard equivalent-income welfare
literature operates with *no* proposal correction at all because it never samples
a feasible set, which is exactly the machinery my ex-ante constrained-set object
adds and must defend. **Explicit-in-source (absence); derived-by-analogy (the
contrast).**

---

## 5. Opportunity mechanism  [MOST IMPORTANT]

**There is no explicit opportunity mechanism.** Stated exhaustively, channel by
channel against my three sub-objects:

- **access (hours / market-participation / region / year / occupation offers).** **Absent.** The hours set is a common universal grid; there is no offer probability, no participation restriction beyond the sample-selection rules, no region/year/local-labour-market variation in *feasibility*. Region enters only as a *taste-shifter* inside $\beta_{li}$ (p. 799), i.e. on the **preference** side, not as access. **Explicit-in-source.**
- **ability (wage technology: returns to education/experience, residual productivity $\sigma$).** **Not present as an opportunity object.** Wages are *imputed* once via a Heckman-corrected wage equation and then enter the budget as a fixed input (p. 800). There is no structural wage-return sub-block inside an opportunity density and no residual-productivity dispersion parameter analogous to my $\sigma$. So my **ability** channel has no counterpart here. **Explicit-in-source (wages are an imputation input); derived-by-analogy (the absence of an ability *opportunity* object).**
- **occupation.** **Not modelled at all** — no occupation, no sector/industry. There is therefore **no sector/occupation conflation to flag**, and equally no occupation-as-access content to borrow. **Explicit-in-source (absence).**

**Functional form of the (non-)mechanism:** opportunities are encoded entirely by
the budget $c_{ij}=f(w_ih_{ij},I_i,x_i)$ and the common hours grid. The paper is
candid about the omission and names it as future work: it flags **demand-side
constraints, fixed costs of work, and "country-specific choice opportunities"**
as needed extensions left undone (pp. 799, 826). **Explicit-in-source.**

**Cost to my access/ability/preference decomposition if I inherited this design.**
Total: the decomposition would be impossible. With no $g$, every opportunity
difference is folded into the estimated preference parameters, so an
"opportunity vs preference" (let alone three-way) split cannot be formed — the
opportunity content would be mechanically zero and the preference content would
be inflated by exactly the absorbed access/ability variation. This is the
identification gap my opportunity layer is built to close, and Bargain et al. is
the cleanest citable instance of the gap. **Derived-by-analogy (consequence for
my design); the underlying absorption concern is explicit-in-source (pp. 799,
826).**

---

## 6. Welfare object — and its place on my $W^1$–$W^6$ map

**Yes, the paper computes welfare:** individual-level, **money-metric**,
preference-respecting **equivalent income**, defined over the
**consumption–leisure** space and evaluated on the *deterministic* utility (so
indifference curves are well-behaved). Three metrics (p. 795, eqs. 1–3):

- **"wage" metric** — minimum hypothetical net wage delivering utility $u$ at **zero** virtual non-labour income:
$$
\nu_i^{W}(u,\mu_r=0)=\min_{\tilde w_i}\big[\tilde w_i \mid v_i(\tilde w_i,\mu_r=0)\ge u\big]. \quad (\text{eq. 1})
$$
- **"rent + reference wage" metric** — virtual non-labour income (expenditure function) at a **reference wage** $w_r$:
$$
\nu_i^{RW}(u,w_r)=e_i(u,w_r)=\min_{\mu_i}\big[c_i-w_r h_i \mid u_i(c_i,h_i)\ge u\big]. \quad (\text{eq. 2})
$$
- **"rent" metric** — consumption at zero hours (IC intercept with the ordinate), $w_r=h_r=0$:
$$
\nu_i^{R}(u,h_r=0)=c_i(u,0)=\min_{c_i}\big[c_i \mid u_i(c_i,0)\ge u\big]. \quad (\text{eq. 3})
$$

- **Universal vs constrained set.** Defined on each household's own indifference curve over the **common** consumption–leisure space; there is **no constrained-feasible-set** object, because there is no opportunity set in the model. **Explicit-in-source.**
- **References used.** A reference virtual wage and/or virtual non-labour income. The "rent + reference wage" metric uses reference wages at **p25/p50/p75 of the pooled wage distribution** (Tables 3–4, pp. 807–808); "wage" sets $\mu_r=0$; "rent" sets $w_r=0$. **Explicit-in-source.**
- **Discrete-choice subtleties.** Handled by computing an **expected** welfare base over EV-I draws and then deriving deterministic ICs from it (full detail in §6b); the chosen-alternative selection is via per-draw argmax; integration over unobserved heterogeneity is by simulation, not analytically. **Explicit-in-source.**
- **Ex-ante vs ex-post.** The welfare base is the **simulated expected deterministic utility of the *chosen* alternative** (p. 801), i.e. an expected-realised-utility object — **not** my analytic ex-ante log-sum inclusive value over a feasible set. **Explicit-in-source.**

**Place on my $W^1$–$W^6$ map.** The paper **does not contain $W^1$–$W^6$** and
makes no Independence-of-$\mathbf{y}$ / Independence-of-$A$ classification.
*(not-established.)* Its three metrics span a compensation–responsibility
spectrum on a **different axis**: responsibility for **work preferences /
willingness-to-work**. The "rent" metric compensates most for low
willingness-to-work (favours the work-averse, p. 796); the "wage" metric holds
individuals **maximally responsible** for willingness-to-work (p. 797, fn. 7);
"rent + reference wage" is intermediate. This is the *preference-axis* analogue
of a compensation–responsibility spectrum — near-**orthogonal** to my
access/pay axis, in the same way JJT vary the preference axis (welfare spec §1.3).
Concretely: **all** my $W^1$–$W^6$ hold preferences *respected* and vary the
*opportunity* treatment (pay vs access), a dimension Bargain et al. do not have;
**their** three metrics hold the (absent) opportunity treatment fixed and vary
the *preference-responsibility* treatment, a dimension my family collapses by
respecting preferences throughout. So no single $W^k$ corresponds to a Bargain
metric. **Derived-by-analogy (the axis comparison); explicit-in-source (their
metrics' own responsibility readings, pp. 796–797).**

**Verdict:** the **construction** (Box–Cox ICs; rent analytic intercept; tangency
search for rent+RW and wage) is **directly adaptable** to my welfare core; the
**normative classification is incompatible with my $W$-map** and must be cited
only as the *preference-responsibility* precedent, never as my access/ability
menu.

---

## 6b. Inclusive value and money-metric inversion

- **Inclusive value (log-sum)?** **No.** The welfare base is **not** the log-sum expected maximum. They draw $r=1,\dots,R$ EV-I shocks, take the **argmax alternative per draw**, record the **deterministic** utility of that alternative $u^{\max}_r$, and average: $\bar u=\tfrac1R\sum_r u^{\max}_r$, the "expected optimal utility", from which ICs are derived (p. 801). This is $\mathbb E[u(\text{chosen bundle})]$, deliberately stripping $\varepsilon$ from the welfare base — distinct from my analytic $\log\sum_j\exp(\cdot)$ inclusive value (which would retain the shock expectation). **Explicit-in-source.**
- **Expectation analytic or simulated?** **Simulated** (R draws), not analytic. Direct contrast with my **analytic-in-shocks** log-sum, which uses no Fréchet/EV draws and no simulated argmax. **Explicit-in-source.**
- **Money-metric inversion.** The "rent" metric has a **closed-form** solution (set $h=0$ in the IC, read off consumption — the ordinate intercept). The "rent + reference wage" and "wage" metrics have **no analytic solution** under Box–Cox and are obtained by a **numerical tangency search**, incrementing hours from 0 to $T$ in steps of **0.01 h/week** along the IC until the MRS matches the reference (p. 801). This is a one-dimensional solve along the own-preference IC — the same shape as my **1-D bracketing root-solve** of the own-utility map, and importantly it does **not** bypass the household's own preferences. **Explicit-in-source.**

**Relevance:** the inversion step is reusable almost verbatim; the **expectation
step is not** — I should cite Bargain et al. for the equivalent-income inversion
and explicitly distinguish my analytic inclusive value from their simulated
expected-chosen-utility base (this difference is the substance of my welfare
spec guardrail "stochastic-choice analogue, stated").

---

## 7. Inequality / decomposition content

- **Inequality index.** **None of Gini/MLD/Theil/variance-of-logs/Atkinson.** The welfare comparison is **ordinal**: average **percentile rank** position by country in the pooled distribution, rank correlations, and CDF comparisons (Fig. 2 p. 805; Tables 3–4 pp. 807–808). No cardinal inequality index is decomposed. **Explicit-in-source.**
- **Decomposition rule.** A **two-scenario counterfactual swap**, not Shapley/Shorrocks. Holding individual **budgets and observed $(c,h)$ fixed** and **without re-estimation**, they switch on heterogeneity from one source at a time — country-specific **preference parameters** vs **socio-demographic composition** — and read off how the percentile rankings move (§5.3, pp. 810–812; Tables 5–6). **Explicit-in-source.**
- **Counterfactual construction.** Start from a **reference household** (median-MRS); introduce either demographic heterogeneity only (Table 6a) or preference-parameter heterogeneity only (Table 6b); recompute metrics and ranks. What is equalised: preferences set to the reference; what is varied: one source. **Explicit-in-source.**
- **Order-independence / path-independence / exhaustiveness.** **Not addressed** — it is a scenario comparison, not a Shapley average over orderings; no exhaustiveness identity is imposed. **Not-established.**

**Verdict (reuse for my three-way access/ability/preference Shapley–Shorrocks
split):** **not reusable as a decomposition method.** Two structural mismatches:
(i) it is **two-way**, and **both** sources (preference parameters, demographics)
live **inside my single preference channel** — it says nothing about access or
ability; (ii) it decomposes **ordinal reranking**, not a cardinal inequality
index, and is **not** Shapley. To reach my three-way split I would need an
opportunity object they lack **and** a Shorrocks index decomposition they do not
perform. What *does* carry over conceptually is the **"hold budgets and observed
choices fixed, swap one source at a time"** counterfactual logic; my Shapley
equalisation generalises that logic (averaging over orderings, summing to
$I(\Omega^k)$). **Derived-by-analogy.**

---

## 8. Identification and the separation of preferences from opportunities  [STRICT]

- **What identifies tastes.** Observed labour-supply choices over **known, nonlinear** tax-benefit budget constraints (van Soest 1995 logic). The tax-benefit system's nonlinearities and discontinuities generate **variation in net wages for the same gross wage** across households with different circumstances; this cross-sectional variation is the identifying source (p. 800, fn. 11). No panel, no external instrument. **Explicit-in-source.**
- **Separation of preferences from opportunities.** **Not attempted, and conceded as a limitation.** Because there is no opportunity object, identification of "preferences" is *conditional* on the common hours grid being the true feasible set. The paper explicitly warns that country-specific "preferences" may capture cross-country differences in **opportunities/institutions** (childcare, part-time availability, demand-side restrictions) (pp. 799, 826). So their "preference" estimates are, on their own admission, potentially **contaminated by access**. **Explicit-in-source.**
- **Ability vs access *within* opportunity.** N/A — no opportunity side to subdivide. **Not-established.**
- **Transport to my France pooled cross-section.** The **van Soest tax-benefit identification of preferences transports** (I use the same EUROMOD-budget nonlinearity). What does **not** transport — because they never attempt it — is the harder task my paper owns: identifying the **opportunity density separately from preferences without a panel or external instrument**. **My defence against the "your decomposition is mechanical" referee cannot lean on Bargain et al.**; they are the exhibit of *not* separating, and the burden falls on my **synthetic-recovery certification** (project state §3.6). They identify off cross-sectional tax-benefit variation, **not** synthetic recovery. **Explicit-in-source (their identification); derived-by-analogy (the transport judgement).**

---

## 9. Key results and magnitudes

- **MRS heterogeneity (Table 2, p. 804).** Full-sample mean MRS between consumption and hours $=8.7$ PPP-USD/h at the mean bundle; range from **Portugal 3.7** and **Finland 3.8** (low willingness-to-work compensation) to **Ireland 17.6**, **Austria 13.2**, **Germany 13.2**, **Netherlands 13.2** (high); **France 9.5**. A near **5× spread** across countries. Units: 2001 PPP-USD per hour. **Explicit-in-source.**
- **Metric-dependent reranking (Table 3, p. 807).** Average percentile position shifts between the "rent" and "wage" metrics of **at least 15 percentage points for 7 of 12 countries** (abstract; Table 3 col. 8). Examples: **Ireland +27.4**, **Austria +19.7**, **Netherlands +17.2**, **Germany +14.5** (up); **Finland −20.4**, **Sweden −18.2**, **Denmark −16.7** (down). The **US** falls from income rank **63.3** to "wage" **56.7**; **Ireland** rises from **53.1** (income) to **73.9** ("wage"). **Explicit-in-source.**
- **Source of the reranking (§5.3, Tables 5–6, pp. 810–812).** **Country-specific preference parameters**, **not** demographic composition, drive the metric-dependent reranking (Table 6b mirrors the full result; Table 6a shows demographics alone move ranks little). France is a partial exception where demographics matter more (p. 812, fn. 24). **Explicit-in-source.**

**Benchmark value for my paper.** The *existence of a large across-measure spread*
(tens of percentile points) is encouraging for my welfare spec §5.2 expectation
that my own six-measure family will spread materially — but the **mechanism
differs**: their spread is **preference-driven across countries**; mine would be
**access/ability-driven within France**. I therefore use this only as *a priori*
reason to expect spread, **not** as a numerical benchmark for my opportunity
share or welfare gap. **Derived-by-analogy.**

---

## 10. Estimators, theorems, or formal results

The paper proves no theorems; it **applies** Fleurbaey's axiomatic results (cited,
not re-derived). The formal objects worth importing:

- **Three welfare metrics** (eqs. 1–3, p. 795) — restated in §6 above. *Assumptions:* well-behaved (continuous, increasing, quasi-concave) $u$; nonlinear budgets; tangency conditions. *Technique:* indirect utility / expenditure function on the deterministic IC; reference wage or reference non-labour income fixes the metric. **Verdict:** **reusable** as the inversion targets of my welfare core, with the normative-axis caveat of §6.
- **Box–Cox deterministic utility** (eq. 5, p. 798) — *Verdict:* **reusable**; it is already my preference family.
- **Random-utility / conditional-logit choice probability** (eq. 4 + EV-I, pp. 798–799). *Verdict:* **partial** — my RURO adds the opportunity-density and proposal-correction terms this lacks.
- **Taste-shifter parameterisation** $\beta_{li}=\beta_{l0}+\beta_{lz}z_i$ (eq. 6, p. 799). *Verdict:* **reusable** as the demographic-shifter form on the preference block.

No estimator is novel; all are standard MLE/numerical-inversion. **Explicit-in-source.**

---

## 11. Robustness and specification sensitivity

From §5.4 (pp. 812–814), with full detail deferred to Bargain et al. (2011):

- **Functional form.** Box–Cox vs **constrained quadratic** utility (with monotonicity/concavity imposed): MRS "very similar" (p. 813). Informs my preference-form robustness.
- **Choice-set size.** $J=7$ vs **13 categories** (5 h steps): estimation results robust (p. 813, fn. 25). Informs my grid-resolution / effective-sample-size concern — though note their grid is enumerated, so this is *not* evidence about importance-sampling node counts.
- **Welfare-metric computation.** Three handlings of the random component — baseline (expected utility over draws), (1) metrics per draw then average the *metrics*, (2) probability-weighted sum over discrete categories — leave the **orderings almost unaffected** (p. 813). Mild comfort that the welfare base choice is not knife-edge; **but** it does not speak to my analytic-log-sum-vs-simulated-argmax gap, which is a different object, nor to my ESS degeneracy for singles.
- **Reference household.** p10/p50/p90 of the MRS distribution as alternative references: levels move, **core results unchanged** (pp. 813–814). Direct precedent for my required **reference-preference sensitivity** report.

**What to stress-test in my paper, prompted by this:** preference functional form;
choice-set/integration resolution; the welfare-base/expectation method; and the
reference-preference choice. **Explicit-in-source.**

---

## 12. What I can cite this paper for

- The **canonical empirical implementation** of preference-respecting, money-metric **equivalent-income** welfare on EUROMOD discrete-choice labour supply (King/Fleurbaey lineage).
- The **three metric formulas** ("rent", "rent + reference wage", "wage") and their per-metric responsibility readings on the **willingness-to-work** axis (pp. 795–797, eqs. 1–3).
- The empirical fact that the **normative treatment of preference heterogeneity materially moves welfare rankings** ($\geq 15$ pp for 7/12 countries) (abstract; Table 3, p. 807).
- The **Box–Cox discrete-choice labour-supply specification** with demographic taste-shifters as a standard, welfare-suitable form (eqs. 5–6, pp. 798–799).
- The explicit **acknowledgement that standard models omit demand-side opportunity constraints**, and that estimated "preferences" may **absorb opportunity/institutional differences** — my motivation citation (pp. 799, 826).
- The **expected-utility-over-the-random-utility-distribution** approach to welfare in a logit model, and its **robustness** to the computation method and reference household (pp. 801, 813–814).
- The **counterfactual-swap** logic for attributing reranking to preference parameters vs demographic composition, holding budgets and observed choices fixed (§5.3).

---

## 13. What I should NOT cite this paper for  [overclaim risks]

- **NOT a three-way (or even opportunity-vs-preference) decomposition.** Its §5.3 decomposition is **two-way and entirely within my preference channel** (preference parameters vs demographics); it isolates **no access or ability** component.
- **NOT my $W^1$–$W^6$ family.** It contains **three** metrics on a **responsibility-for-preferences** axis, **not** the Independence-of-pay / Independence-of-access axis. Do **not** claim it contains, characterises, or instantiates any $W^k$.
- **NOT an ex-ante inclusive-value (log-sum) welfare object.** Its welfare base is the **simulated expected deterministic utility of the chosen alternative**, not the analytic log-sum over a feasible set. Do not present it as my constrained ex-ante object.
- **NOT an opportunity model.** No opportunity density, no access/ability object, no latent jobs, no offer probabilities. Do not cite for opportunity-mechanism design.
- **NOT a cardinal inequality decomposition.** Its inequality content is **ordinal percentile reranking**; there is no Gini/Theil/Atkinson and no Shorrocks decomposition.
- **"sectoral"/industry language.** It has **no occupation or sector object at all** — so do not attribute any occupation-as-access (or industry/NACE) content to it, in either direction.
- **random-opportunity framing.** N/A — there is no opportunity randomness; do not read any "RO" content into it. (Opportunities in my design are deterministic anyway.)
- **theory-paper boundary.** It grounds its metrics in **Fleurbaey (2006, 2008)** and **Fleurbaey–Maniquet (2006)** — a *different* reference set. Do **not** attribute the companion **Haydar–Maniquet** axioms/characterisation/proofs to it, and do not let its presence in my welfare citations blur into the theory paper.
- **Sample boundary.** Married women, couples-as-unitary with **husbands' hours fixed**, single cross-section. Do not cite it for singles, for joint two-decider couples (my unit), or for pooled multi-year estimation.

---

## 14. Direct quotes worth citing

1. (Abstract, p. 790) "The resulting welfare rankings clearly depend on the normative treatment of preference heterogeneity with alternative metrics."
2. (p. 795) "The key feature of the metrics introduced above is that they fully respect preferences: all metrics increase when the individual moves to a bundle on a higher indifference curve of her own preference ordering."
3. (p. 796) "First, the 'rent' metric asks for the amount of (hypothetical) net income which would be enough to remain equally well off compared to the initial situation if one did no longer have to earn it."
4. (p. 797, fn. 7) "The 'wage' metric might thus be interpreted as holding individuals maximally responsible for their willingness-to-work."
5. (p. 799) "This particularly implies that we do not model potential demand side restrictions on the labor market nor fixed costs of work."
6. (p. 801) "This 'expected optimal utility' $\bar u$ is used to empirically derive individual indifference curves."
7. (p. 826) "Here, a specific and additionally demanding requirement in the present context would have been to determine country-specific choice opportunities."

---

## 15. Open questions and risks for my draft

- **The contamination they concede is the claim I must prove I undo.** They state that "preferences" may absorb opportunities (pp. 799, 826). A referee will ask whether my opportunity layer *genuinely* re-allocates that variation or merely **relabels** preference heterogeneity as access. My answer must be the **synthetic-recovery** certification (project state §3.6) and the standard-error asymmetry (opportunity tightly estimated, preference wide, §3.8) — not an appeal to Bargain et al.
- **My welfare base differs from theirs and I must defend "ex-ante".** Their simulated expected-chosen-utility vs my analytic log-sum inclusive value: I must name the realised-bundle-vs-inclusive-value gap explicitly (welfare spec guardrail 2) and justify the ex-ante stance as the only one that can carry the access channel (project state §2.3).
- **Integration error is a different beast for me.** Their robustness shows the *expectation method* barely moves orderings, but they **enumerate** the grid; my importance-sampling **ESS degeneracy for singles** (project state §7.1) has no analogue in their setting and cannot borrow comfort from their result.
- **Reference-preference sensitivity is mandatory, not optional.** Their results are robust to the reference household; my family computation must report the analogous **reference-preference sensitivity** for the preference-equalisation step of the decomposition.
- **Do not import their magnitude as my benchmark.** Their large spread is *cross-country preference-driven*; mine is *within-France access/ability-driven*. Borrowing "$\geq 15$ pp" as an expectation for my opportunity share would be a category error.

---

## 16. TL;DR for retrieval

Bargain et al. (2013) is the canonical EUROMOD discrete-choice implementation of
**preference-respecting money-metric equivalent income**, computing three
metrics ("rent" / "rent + reference wage" / "wage") that span a
compensation–responsibility spectrum on the **preference (willingness-to-work)**
axis — informing my **preference** channel and my welfare-inversion core
(Box–Cox ICs, rent analytic intercept, tangency search), but **not** my
$W^1$–$W^6$ access/ability menu. It has **no opportunity mechanism** (no $g$, no
access/ability object, common hours grid) and explicitly concedes that estimated
"preferences" may absorb omitted opportunity constraints — making it the primary
**motivation** citation for my opportunity layer. Its §5.3 "decomposition" is a
**two-way preference-vs-demographics counterfactual swap on ordinal ranks**, not
a cardinal three-way Shapley–Shorrocks split, so it informs the
hold-fixed-and-swap *logic* but supplies neither the channels nor the method.
