# JMP T1 Exhaustive Extraction Prompt (v2)

> **Use for:** T1A and T1B (core) papers. For supporting/background papers use
> `JMP_T2_focused_extraction_prompt_v2.md`. The lean v1 prompt (`summary_T1.md`)
> is retained as a fallback only.
> **What changed from v1 (`summary_T1.md`):** the decomposition is now
> **three-way access / ability / preference** (not two-factor opportunity vs
> preference); the welfare object is the **family $W^1$–$W^6$** on the
> compensation–responsibility spectrum; new mandatory sections force the
> inclusive value, money-metric inversion, the proposal/prior correction,
> couples joint choice, occupation-conditioned wage draws, and
> inference/numerical implementation; the empirical-JMP vs theory-paper boundary
> is made explicit. Section numbers are kept stable and non-contiguous so T1 and
> T2 summaries co-index.

---

ROLE
You are an expert research assistant in structural labour-supply econometrics,
discrete-choice random-utility models (RURO / latent jobs), money-metric and
equivalent-income welfare measurement, and the inequality-of-opportunity /
Shapley–Shorrocks decomposition literature.

TASK
Produce an exhaustive, retrieval-oriented Markdown summary of the attached paper,
for use in my empirical job market paper *"Unequal Job Opportunities and
Well-Being Inequality: A Latent-Jobs Structural Decomposition"* (Haydar 2026).
Lose no information relevant to my work. Use the project anchor below ONLY to
judge relevance — do **not** summarize my project, and do **not** import my
design into the paper you are reading.

MY PROJECT — anchor every "relevance" judgment to this (current as of welfare
spec v5 + project state v1; supersedes the older two-factor framing):

- **Research question.** How much of inequality in money-metric well-being is
  driven by unequal **job opportunities** rather than by heterogeneous
  **preferences**, once labour supply is modelled as a choice among latent jobs?
- **Structural model (RURO / latent jobs).** Choice probability factorises as
  preference utility $v$ times an opportunity density $g$. On a sampled set of
  alternatives the per-alternative value is
  `u_ij + log h_ij + log w_ij + log market_ij − log π(j;x_i)`, where the
  `log h / log w / log market` terms are the opportunity-density channels and
  `−log π` is the **mandatory sampling-of-alternatives (proposal/prior)
  correction**. The household inclusive value is the log-sum.
- **The three structural→normative channels (THIS REPLACES the old two-factor
  cut).**
  - **preference** = the utility block $v$ (Box–Cox over consumption, leisure,
    children-time; demographic taste-shifters; gender).
  - **ability** = the wage-technology sub-block of $g$ (returns to own education
    and experience; residual productivity dispersion $\sigma$). This is the
    **Independence-of-$y$ / pay** dimension.
  - **access** = the rest of $g$ (employment/hours availability; region;
    urbanisation; year; gender-specific occupation offers). This is the
    **Independence-of-$A$ / feasible-set** dimension.
  "Opportunity" = **access + ability** (upper bound); **access alone** is the
  lower bound.
- **Estimation.** France, pooled EU-SILC 2015–2017 via EUROMOD (`ils_dispy`,
  2016-real basis); three groups (single males, single females, couples);
  couples are a **joint** decision unit (901 joint alternatives; singles 101).
  Certified 47-parameter pooled baseline; certification is by **synthetic
  recovery**, not in-sample fit.
- **Welfare object — a FAMILY, not one measure.** Ex-ante, household-level,
  money-metric, preference-respecting equivalent income, computed as the
  characterised family $W^1,\dots,W^6$ spanning a **compensation–responsibility
  spectrum**, classified by Independence-of-$y$ (pay/ability) and
  Independence-of-$A$ (access):
  - $W^2,W^3$ = Full Responsibility (own everything);
  - $W^1$ = compensate pay, responsible for the set (Ind-$y$, not Ind-$A$);
  - $W^5$ = compensate the set, responsible for pay (Ind-$A$, not Ind-$y$);
  - $W^4,W^6$ = Full Compensation (compensate both).
  All six read attained utility $V_i$, so unequal access lowers welfare under
  **every** measure through attainment; the Ind-$y$/Ind-$A$ properties bite only
  in the *direct* evaluation channel.
- **Headline contribution.** A **three-way** access/ability/preference
  Shapley–Shorrocks decomposition of welfare inequality, anchored on
  non-pre-absorbing measures (Full-Responsibility $W^3$ for total
  source-composition; the one-sided duals $W^5$/$W^1$ for the access/ability
  dimensions), reported as an opportunity **surface** over (measure × channel).
- **Hard boundaries.**
  - NOT a country-ranking or beyond-GDP-ranking paper.
  - NOT the separate axiomatic theory paper (Haydar–Maniquet). That paper
    *characterises* $W^1$–$W^6$; the JMP **imports the measures and their
    normative readings as cited primitives and re-derives nothing**.
  - **Opportunities are deterministic** (the "random opportunities" framing is
    removed); the "RO" in RURO is estimation machinery, not a claim that
    opportunities are random.
  - **Occupation** (`loc4`, ISCO-type, four task categories) is an
    **access/opportunity** object in $g$ only — never utility, never the
    structural wage return. It must **never** be called industry or sector;
    industry (`lindi`, NACE) is reserved and deferred to robustness.

OUTPUT — use exactly this structure (keep the numbering; write "N/A" if a section
genuinely does not apply; never pad):

# Author Year — Title

## 0. Metadata
BibTeX key, authors, year, outlet, DOI/URL, PDF filename, tier (T1A/T1B), and
which JMP block(s) it serves: estimation / identification / welfare /
decomposition / opportunity-mechanism (access / ability) / normative-interpretation /
data-infrastructure / motivation.

## 1. One-paragraph relevance to my JMP
Three to five sentences: why this paper matters for *my* paper specifically, and
which of the three channels (access / ability / preference) or which welfare
measure(s) it speaks to.

## 2. Data and setting
Country, year(s), dataset, sample unit (individuals / couples / households),
sample size, key variables, budget-set construction. State explicitly whether the
setting transports to my **France pooled 2015–2017 EUROMOD cross-section**, and
name any feature I do NOT have (panel, administrative match, external instrument,
vacancy/offer data).

## 3. Model and objects (map object-by-object to mine)
Is their choice set = my latent-jobs set? their deterministic utility = my
preference utility $v$? Do they have an explicit opportunity / availability
mechanism analogous to my $g$, and if so does it separate **hours**, **wage
(ability)**, **market/participation**, and **occupation** channels? Their budget
map = my EUROMOD disposable income? Note every difference. **Flag immediately if
any job attribute enters BOTH utility and the opportunity mechanism**, and
whether they justify it on identification grounds.

## 4. Estimation method
Likelihood and estimator; choice-set construction (fixed grid vs sampled
alternatives; grid size); proposal / sampling density; **prior/proposal
correction** — is $\log(\text{prior})$ subtracted from the choice index, and is
it always well defined? Normalisation and scale; numerical method; starting
values / multistart; what pins down preferences separately from the opportunity
mechanism. **Verdict: reusable for my RURO/JAX pipeline? (yes / no / how —
name the step).**

## 4b. Proposal / sampling-of-alternatives correction  [extract even if brief]
Exactly how alternatives are sampled and corrected. Is the proposal **partly
individualised** (e.g. a covariate-dependent wage mean, occupation-conditioned
draws) or common across units? Is the correction McFadden-style? Does each drawn
alternative carry its own log-prior? Relate to my importance-sampling welfare
integrator and my proposal-individualisation concern (wage/occupation
individualised; hours/employment common).

## 5. Opportunity mechanism  [MOST IMPORTANT — be exhaustive; split by channel]
Exactly how feasibility/availability of jobs, hours, wages, and occupations is
modelled. Is it a density over alternatives? offer probabilities? a
reservation-wage / participation restriction? Does it vary with observable
circumstances (region, education, demographic type, local labour market)? **Map
to my three sub-objects explicitly:**
- **access** (hours / market-participation / region / year / occupation offers);
- **ability** (the wage technology: returns to education and experience, residual
  productivity);
- whether **occupation** is treated as availability (like my `loc4` access
  object) or as something else — and flag any sector/industry conflation.
State the functional form. If there is **no** explicit opportunity mechanism
(a common universal choice set), say so plainly and state what that omission
would cost my access/ability/preference decomposition.

## 6. Welfare object — and its place on my $W^1$–$W^6$ map
Does the paper compute welfare? If so: money-metric? equivalent income?
compensating/equivalent variation? expected (log-sum / inclusive-value) utility?
Defined over a **universal** set or a **constrained feasible** set? What
reference price / reference preference / reference bundle / reference set is used?
How are the discrete-choice subtleties handled — log-sum aggregation, selection
of the chosen alternative, Hicksian vs Marshallian, integration over unobserved
heterogeneity, **ex-ante vs ex-post**? **Then locate the paper on my family map:**
which of $W^1$–$W^6$ (or which Ind-$y$ / Ind-$A$ stance) does its construction
correspond to, if any? Verdict: directly usable / adaptable / incompatible, and
why.

## 6b. Inclusive value and money-metric inversion  [extract if the paper uses a log-sum or an EV/CV]
Does the paper use the **inclusive value** (expected maximum / log-sum) as the
welfare core? Is welfare obtained by **inverting** an own-utility map to a money
figure (a one-dimensional solve), or by a closed-form shortcut that bypasses the
household's own preferences? Is the expectation over the extreme-value shocks
taken **analytically** (no shock draws) or by simulation? Relate to my analytic-
in-shocks, importance-sampling inversion.

## 7. Inequality / decomposition content  [three-way where relevant]
Inequality index (Gini / MLD / Theil / variance of logs / Atkinson).
Decomposition rule (Shapley, Shorrocks, factor-component, subgroup,
regression-based, RIF, Owen-grouped). Counterfactual construction: **what is
equalised, what is neutralised, what is held fixed, what is "zeroed out."**
Order-independence / path-independence / exhaustiveness properties. **Verdict:
reusable for my three-way access/ability/preference Shapley–Shorrocks split
(anchored on $W^3$ / $W^5$ / $W^1$)?** If the paper is two-way (e.g.
opportunity vs preference, or compensate vs reward), say so and state exactly how
it would have to be extended to three channels.

## 8. Identification and the separation of preferences from opportunities  [STRICT]
What identifies tastes vs constraints — and, where possible, **ability vs access**
within the opportunity side? Name the exact source: functional-form restriction,
exclusion restriction, choice-set variation, panel/repeated choices, an external
opportunity shifter (local unemployment, vacancies), distributional assumptions
on unobservables. State honestly whether it transports to my France pooled
cross-section, where I have **no panel and (currently) no external instrument**.
This is the backbone of my identification note and my defence against the
"your decomposition is mechanical" referee — do not soften it. If the paper
relies on synthetic-recovery / parametric-identification arguments, note them
(my baseline is certified by synthetic recovery, not in-sample fit).

## 9. Key results and magnitudes
Headline numbers: elasticities, participation/hours effects, welfare-effect
magnitudes, opportunity-share / unfair-share findings, decomposition shares,
across-measure spread. Anything that benchmarks whether my own opportunity share
or welfare spread is plausible. Report numbers with units and the population they
refer to.

## 10. Estimators, theorems, or formal results
For each formal result/estimator: statement (near-verbatim, in LaTeX),
assumptions, technique in 3–5 bullets, and a verdict on reusability for my
estimation / welfare-inversion / decomposition layer (yes / no / maybe + how).

## 11. Robustness and specification sensitivity
What they vary and what breaks: choice-set size, number of draws, number of
starts, alternative opportunity-set definitions, circumstance partitions,
reference-state / reference-preference choices, ability/access boundary. This
informs my recovery/stability tests, my effective-sample-size concern, and my
robustness section — extract anything that tells me what to stress-test.

## 12. What I can cite this paper for
Specific, attributable claims I can support with this paper.

## 13. What I should NOT cite this paper for  [overclaim risks]
Claims this paper does NOT establish that a careless reader might attribute to it.
**Always include the relevant boundary flags where they apply:**
- two-way (not three-way) decomposition;
- ex-post or universal-set welfare presented as my constrained ex-ante object;
- "sectoral"/industry language vs my occupation-as-access object;
- random-opportunity framing vs my deterministic feasible sets;
- **theory-paper boundary**: never attribute the companion Haydar–Maniquet
  axioms/characterisation/proofs to the JMP, and never read the JMP as a theory
  contribution.

## 14. Direct quotes worth citing
3–7 short, exact verbatim quotes with page numbers.

## 15. Open questions and risks for my draft
What this paper leaves unresolved that bears on my paper; where it raises a risk
I must address (identification, inference, integration error, normative framing).

## 16. TL;DR for retrieval
Three dense sentences for later indexing, naming the channel(s) and welfare
stance the paper informs.

RULES
- Do not invent claims, theorem numbers, estimates, elasticities, or DOIs. If any
  metadata is uncertain, write "[uncertain, needs verification]".
- Throughout, distinguish **explicit-in-source** from **derived-by-analogy** from
  **not-established**.
- Use the **three-way access / ability / preference** vocabulary; do not lapse
  into the obsolete two-factor "opportunity vs preference" framing except to note
  that a source uses it.
- Keep **occupation (ISCO / `loc4`)** strictly separate from
  **industry / sector (NACE / `lindi`)**; if the paper itself conflates them,
  flag the conflation explicitly.
- Treat opportunities as **deterministic** when mapping to my design.
- Respect the **empirical-JMP vs theory-paper boundary** in every relevance and
  citation judgment.
- Use LaTeX for all mathematics. No praise, no filler. If a section does not
  apply, write "N/A".
