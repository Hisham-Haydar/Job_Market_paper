I inspected the additional files together with the project-state and welfare-spec files. The important conclusion is this:

You should **not restart with a broad literature search as the first step**. You already have a large, partly organized JMP corpus: an 85-entry BibTeX file, a combined extracted literature file, a folder/PDF structure, several deep-research reports, and two transcripts showing how the theory-paper library was built. The correct next move is to **rebuild the JMP library from the existing corpus first**, then run **one targeted gap-audit Deep Research** to check what is missing.

The theory-paper workflow is useful as a template, but the JMP extraction prompt must be structurally different. The theory prompt was about axioms, characterizations, W³/W⁵, and proof reuse. The JMP prompt must instead extract material for:

```text
latent jobs / RURO / constrained opportunities
→ estimation and identification
→ wage-offer and occupation-opportunity structure
→ money-metric welfare W¹–W⁶
→ inclusive-value / proposal-corrected welfare
→ Shapley decomposition into access / ability / preference
→ inference, simulation, bootstrap, and implementation
```

The most important deliverable now should be:

```text
docs/JMP_literature_extraction_protocol_v1.md
```

This should become the canonical extraction prompt for every paper you summarize for the JMP.

---

## 1. What I found from the uploaded files

`JMP_project_state_v1.md` is now much more than a topic note. It fixes the empirical and methodological identity of the paper: opportunity-sensitive decomposition of money-metric well-being inequality in a latent-jobs structural labour-supply model. It clearly separates preferences, ability, and access, and it makes the opportunity density (g(j;x_i,\theta^{opp})) the scientific novelty.

`JMP_welfare_spec_v5.md` is the binding welfare-design document. It says the welfare object is not a single measure but a family (W^1,\dots,W^6), all computed from proposal-corrected ex-ante attained utility / inclusive value and then inverted into money-metric welfare. It also fixes the decomposition logic: Shapley–Shorrocks over access, ability, and preference, with reporting as a surface over measures and components.

`JMP_lit_collection.bib` already has a strong core: Aaberge–Colombino, Dagsvik, Bargain, Capéau, Bhattacharya, Fleurbaey, Decancq, Hufe, Roemer, Shorrocks, Sutherland–Figari, microsimulation, and equality-of-opportunity references. This is enough to begin extraction. It is not enough to avoid a targeted gap check later.

`full_literaterature.md` is a very large combined extracted corpus. It is useful as a searchable backup, but it should **not** replace per-paper summaries. It appears too noisy to use directly as the main library object.

`all_Literature_structure.md` is effectively a file tree / PDF location record, but it appears encoded with null characters. It should be cleaned by script and converted into a PDF inventory.

`deep-research-report_update.md`, `LIT_deep-research-report.md`, `deep-research-report_roadmap.md`, and `JMP_gap_check_v1.md` are synthesis aids. They should not be treated as source truth. Their role is to help tier the corpus and identify missing papers.

`Chat_gpt_lite.md` and `Claude_lit.md` show the theory-paper workflow. The transferable part is the pipeline: discovery → audit → PDF collection → exhaustive markdown summaries → indexes → writing bank. The non-transferable part is the extraction orientation: the JMP is empirical/structural/welfare-decomposition, not pure axiomatic characterization.

---

## 2. Revised strategy

Do **four phases**, not a broad restart.

```text
Phase 0 — Local corpus normalization
Phase 1 — JMP tiering and source inventory
Phase 2 — Targeted gap audit with Deep Research / Claude Research
Phase 3 — Exhaustive paper extraction and indexing
```

The first Deep Research run should come **after** the local inventory, not before. Otherwise the research model will rediscover papers you already have and waste time.

---

# Phase 0 — Local corpus normalization

Tool: **Claude Code Sonnet**.

Files to place in the workspace:

```text
JMP_lit_collection.bib
all_Literature_structure.md
full_literaterature.md
JMP_project_state_v1.md
JMP_welfare_spec_v5.md
deep-research-report_update.md
JMP_gap_check_v1.md
LIT_deep-research-report.md
deep-research-report_roadmap.md
```

Expected outputs:

```text
JMP_literature/00_admin/JMP_existing_corpus_inventory_v1.csv
JMP_literature/00_admin/JMP_existing_bibtex_audit_v1.md
JMP_literature/00_admin/JMP_pdf_inventory_v1.csv
JMP_literature/00_admin/JMP_literature_rebuild_decision_log_v1.md
```

Prompt:

```text
Work locally in my JMP literature workspace.

This is Phase 0 of rebuilding the literature library for my economics JMP.

Read:
- JMP_lit_collection.bib
- all_Literature_structure.md
- full_literaterature.md
- JMP_project_state_v1.md
- JMP_welfare_spec_v5.md
- deep-research-report_update.md
- JMP_gap_check_v1.md
- LIT_deep-research-report.md
- deep-research-report_roadmap.md

Task:
Create a clean inventory of the existing JMP literature corpus. Do not summarize papers yet. Do not run external searches.

Create:
1. JMP_literature/00_admin/JMP_existing_corpus_inventory_v1.csv
2. JMP_literature/00_admin/JMP_existing_bibtex_audit_v1.md
3. JMP_literature/00_admin/JMP_pdf_inventory_v1.csv
4. JMP_literature/00_admin/JMP_literature_rebuild_decision_log_v1.md

The corpus inventory CSV must include:
- source_id
- bibtex_key
- author_year
- title
- authors
- year
- publication_type
- journal_or_source
- DOI_or_URL
- has_bibtex
- has_pdf
- appears_in_full_literature_md
- appears_in_deep_research_reports
- likely_JMP_bucket
- preliminary_tier
- notes
- metadata_problems

Use these JMP buckets:
- latent_jobs_RURO_opportunity_sets
- structural_labor_supply
- wage_offer_occupation_distribution
- couples_joint_labor_supply
- random_utility_welfare
- money_metric_equivalent_income
- responsibility_equality_of_opportunity
- Shapley_decomposition_inequality
- microsimulation_tax_benefit
- simulation_inference_bootstrap
- motivation_positioning
- not_central_or_background

The BibTeX audit must identify:
- duplicate or near-duplicate entries;
- missing years;
- missing titles;
- missing DOI/URL;
- entries that look irrelevant for the JMP;
- entries that look essential but lack PDFs.

The PDF inventory must clean the folder/path listing, including any encoding issues, and map PDF filenames to likely BibTeX entries.

Do not invent metadata. Use [verify] where uncertain.
Do not confuse this JMP with the separate theory paper.
Do not summarize papers yet.
```

Save the result as a **corpus audit**, not a concept note.

---

# Phase 1 — JMP tiering and source inventory

Tool: **Claude Project chat** or **ChatGPT Thinking**.

Files to attach:

```text
JMP_existing_corpus_inventory_v1.csv
JMP_existing_bibtex_audit_v1.md
JMP_pdf_inventory_v1.csv
JMP_project_state_v1.md
JMP_welfare_spec_v5.md
JMP_gap_check_v1.md
deep-research-report_roadmap.md
```

Expected outputs:

```text
JMP_literature/00_admin/JMP_literature_tiers_v1.md
JMP_literature/00_admin/JMP_literature_tiers_v1.csv
JMP_literature/00_admin/JMP_first_summary_batch_v1.md
```

Prompt:

```text
This is for my economics JMP literature library.

The JMP studies unequal job opportunities and well-being inequality in a latent-jobs structural labour-supply model. It estimates opportunity heterogeneity, computes a family of money-metric welfare measures W¹–W⁶, and later decomposes inequality into access, ability, and preference using Shapley–Shorrocks.

Read:
- JMP_existing_corpus_inventory_v1.csv
- JMP_existing_bibtex_audit_v1.md
- JMP_pdf_inventory_v1.csv
- JMP_project_state_v1.md
- JMP_welfare_spec_v5.md
- JMP_gap_check_v1.md
- deep-research-report_roadmap.md

Task:
Tier the existing literature corpus for the JMP.

Create:
1. JMP_literature/00_admin/JMP_literature_tiers_v1.md
2. JMP_literature/00_admin/JMP_literature_tiers_v1.csv
3. JMP_literature/00_admin/JMP_first_summary_batch_v1.md

Tier definitions:
T1 = must summarize exhaustively because the paper directly supports the JMP's model, welfare object, decomposition, identification, or main contribution.
T2 = summarize selectively because it supports a specific section or robustness.
T3 = citation/background only.
DEFER = possibly useful later but not now.
REJECT = not useful for this JMP.

For each source, assign:
- tier;
- priority rank;
- JMP component;
- why it matters;
- what I can cite it for;
- what I should not cite it for;
- whether to collect PDF immediately;
- whether to summarize now.

JMP components:
- model_latent_jobs
- opportunity_density
- wage_ability
- occupation_access
- couples_joint_choice
- welfare_inclusive_value
- money_metric_equivalent_income
- W1_W6_normative_family
- responsibility_and_opportunity
- Shapley_decomposition
- microsimulation_EUROMOD
- inference_bootstrap_simulation
- numerical_estimation

The first-summary batch should include:
- first 12 T1 papers;
- next 8 T1/T2 papers;
- reason for each.
Do not over-center beyond-GDP/country-ranking sources.
Do not over-center pure optimal taxation unless directly needed.
Do not mix the separate theory paper into this JMP library.
```

My likely first-summary batch, before seeing the normalized inventory, would be:

```text
1. Dagsvik et al. 2014 — latent jobs / labour supply as choice among latent jobs
2. Dagsvik and Jia 2016 — latent jobs, unobserved heterogeneity, identification
3. Dagsvik and Strøm 2006 — sectoral labour supply and choice restrictions
4. Aaberge et al. 2009 — alternative representations of choice sets
5. Aaberge and Colombino 2013 — microeconometric labour supply and optimal taxes
6. Bargain et al. 2013 — welfare, labour supply, heterogeneous preferences
7. Capéau et al. 2015 / 2016 — RURO / random opportunities
8. Bhattacharya 2018 — empirical welfare analysis for discrete choice
9. Capéau et al. 2021 — nonparametric welfare analysis for discrete choice
10. Hufe et al. 2022 — measuring unfair inequality
11. Shorrocks 2013 or 1982 — decomposition procedures
12. Sutherland and Figari 2013 — EUROMOD / tax-benefit microsimulation
```

Additions likely needed after gap audit:

```text
- de Palma and Kilani on welfare / EV-CV in random utility
- Small and Rosen on applied welfare in discrete choice
- McFadden / Train background only for log-sum and random utility, not as core JMP novelty
- papers on simulation error / sampling of alternatives / importance sampling if not already in the corpus
```

---

# Phase 2 — Targeted gap audit

Only after Phase 1.

Tool: **ChatGPT Deep Research** first, then optionally **Claude Research Mode** as adversarial audit.

This should be targeted. Do not ask for a broad literature review.

Save as:

```text
JMP_literature/01_discovery_reports/DR03_JMP_targeted_gap_audit_v1.md
```

Prompt:

```text
ROLE
You are a literature-gap auditor for an economics job market paper.

PROJECT
The JMP studies unequal job opportunities and well-being inequality in a latent-jobs structural labour-supply model. It estimates an opportunity density over latent jobs, computes money-metric welfare measures W¹–W⁶ from proposal-corrected ex-ante inclusive value, and decomposes welfare inequality into access, ability, and preference using Shapley–Shorrocks.

INPUTS
I will provide:
- project state memo;
- welfare specification memo;
- current source inventory;
- current tiering table.

TASK
Do not produce a broad literature review. Audit the current corpus for missing or under-covered sources that are necessary for this specific JMP.

Audit the following areas:
1. latent jobs / RURO / random opportunity sets;
2. structural labour supply with constrained opportunities;
3. wage-offer distributions and occupation-conditioned wage draws;
4. couples labour supply and joint choice sets;
5. random utility welfare, inclusive value, compensating variation, equivalent variation;
6. money-metric welfare and equivalent income;
7. responsibility-sensitive welfare and equality of opportunity;
8. Shapley / Shorrocks inequality decomposition;
9. tax-benefit microsimulation / EUROMOD structural labour supply;
10. simulation error, sampling of alternatives, importance sampling, bootstrap inference.

OUTPUT
Use exactly these sections:

1. Audit verdict
2. Current corpus strengths
3. Missing Tier 1 papers
4. Missing Tier 2 papers
5. Sources currently over-weighted
6. Sources that should be demoted or treated as background
7. Missing methods papers for estimation/inference
8. Missing welfare papers for inclusive value / money metric
9. Missing decomposition papers
10. Missing couples / joint-choice papers
11. Revised first-summary batch
12. Exact sources to add to Zotero
13. Exact sources to search for manually
14. Final action list

RULES
- Do not invent references.
- If uncertain, mark [uncertain, verify].
- Do not confuse this JMP with the separate theory paper.
- Do not recommend broad beyond-GDP sources unless directly useful.
- Do not recommend pure optimal-tax papers unless they support the structural labour-supply or welfare layer.
```

---

# Phase 3 — Exhaustive JMP paper extraction

This is the most important part.

Save the prompt below as:

```text
JMP_literature/06_prompts/JMP_T1_exhaustive_extraction_prompt_v1.md
```

Use it for every Tier 1 paper. It is deliberately long and retrieval-oriented.

```text
ROLE

You are an expert research assistant in structural labour economics, discrete-choice labour-supply estimation, random utility welfare analysis, welfare economics, equality of opportunity, and inequality decomposition.

TASK

Produce an exhaustive, retrieval-oriented Markdown summary of the attached paper for my economics job market paper.

My JMP is titled, provisionally:

“Unequal Job Opportunities and Well-Being Inequality: A Latent-Jobs Structural Decomposition.”

The goal is to lose no information relevant to my JMP. The summary must help me later write the literature review, model section, welfare section, decomposition section, and empirical implementation section. It must also help me avoid overclaiming.

Use the attached JMP project-state memo and welfare-spec memo only to understand my project, notation, and extraction needs. Do not summarize those memos.

MY JMP MODEL

The empirical object is a latent-jobs / RURO-type structural labour-supply model.

A household or individual \(i\) faces a sampled choice set of job alternatives \(j\in \mathcal C_i\). Each alternative contains consumption, leisure, hours, wage, occupation, region/access variables, and tax-benefit outcomes.

The estimated per-alternative value has the form

\[
V_{ij}
=
u_i(c_{ij},\ell_{ij};\theta^{pref})
+
\log g(j;x_i,\theta^{opp})
-
\log \pi(j;x_i),
\]

where:

- \(u_i(\cdot)\) is deterministic utility / preferences;
- \(g(j;x_i,\theta^{opp})\) is the opportunity density;
- \(\pi(j;x_i)\) is the proposal distribution used to sample alternatives;
- \(-\log\pi\) is the mandatory sampling-of-alternatives / proposal correction;
- the inclusive value is

\[
IV_i = \log\sum_{j\in\mathcal C_i}\exp(V_{ij}).
\]

The opportunity density is split into:

1. **ability / wage technology**:
   wage returns to education and experience, residual wage dispersion;

2. **access / market opportunity**:
   participation availability, hours availability, region, unemployment/access variables, year, occupation availability.

The decomposition cut is:

- preference \(=\theta^{pref}\);
- ability \(=\) wage technology / education-experience productivity;
- access \(=\) non-wage opportunity environment: market, hours, region, unemployment, occupation availability.

The welfare layer computes a household-level, money-metric, preference-respecting family \(W^1,\dots,W^6\). All measures read attained utility through the inclusive value \(IV_i\), then invert it into a money metric using a measure-specific reference. The measures span a compensation–responsibility spectrum over pay and opportunity sets. Welfare inequality is later decomposed by Shapley–Shorrocks equalisation of access, ability, and preference.

OUTPUT — use exactly this structure:

# Author Year — Title

## 0. Metadata

Include:
- full citation;
- BibTeX key if available;
- authors;
- year;
- journal / working paper series / book;
- DOI / URL;
- PDF filename;
- priority tier;
- JMP literature bucket(s);
- JMP component(s):
  model / estimation / opportunities / wage ability / occupation access / couples / welfare / W1-W6 / decomposition / inference / microsimulation / writing motivation.

If any item is uncertain, write “[uncertain, needs verification]”.

## 1. One-paragraph relevance to my JMP

Explain exactly why this paper matters for my JMP. Be specific. Do not say merely “related to labour supply” or “related to welfare.”

## 2. Research question and contribution

State:
- the paper’s research question;
- its main contribution;
- what gap it claims to fill;
- how close it is to my JMP.

Classify closeness:
- direct predecessor;
- close comparator;
- supporting method;
- background only;
- potential referee comparison;
- not central.

## 3. Model objects and mapping to my JMP

Define the paper’s objects:
- decision-maker;
- alternatives;
- choice set;
- utility;
- budget set;
- constraints;
- wages;
- hours;
- occupations/sectors;
- household/couple structure;
- random shocks;
- heterogeneity;
- welfare object.

Map each object to my JMP:

| Paper object | Meaning in source | JMP analogue | Same / different / absent | Notes |
|---|---|---|---|---|

Be explicit about differences.

## 4. Choice-set / opportunity-set structure

Extract everything about:
- feasible sets;
- opportunity sets;
- latent jobs;
- choice restrictions;
- rationing;
- random opportunity sets;
- random utility random opportunities;
- offer probabilities;
- job availability;
- hours restrictions;
- sector/occupation restrictions;
- unemployment or demand-side access;
- regional opportunity variation.

Answer:
- Does the paper distinguish preferences from opportunities?
- Does it estimate opportunity heterogeneity?
- Does it treat opportunities as a modelling device or as an object of welfare analysis?
- Does it have anything analogous to \(g(j;x_i,\theta^{opp})\)?
- Does it have anything analogous to \(-\log \pi(j;x_i)\)?

Classify each claim:
- explicit in source;
- derived by analogy;
- not established.

## 5. Preference specification

Extract:
- utility function;
- deterministic utility;
- random utility shocks;
- curvature;
- Box-Cox / translog / quadratic / other;
- preference heterogeneity;
- demographic taste shifters;
- treatment of consumption and leisure;
- treatment of children/time;
- treatment of gender and couples.

Map to my preference block \(u_i(c,\ell;\theta^{pref})\).

State whether the paper risks attributing opportunity differences to preferences, or whether it avoids that.

## 6. Wage-offer / ability structure

Extract everything about:
- wage equations;
- Mincer terms;
- education;
- experience;
- residual wage dispersion;
- gender-specific wage equations;
- occupation-conditioned wages;
- selection into work;
- wage imputation;
- wage-offer density;
- unobserved productivity.

Map to my ability block.

Answer:
- Can I cite this paper for treating wage opportunities as part of the structural opportunity environment?
- Can I cite it for gender-specific wage offers?
- Can I cite it for occupation-conditioned wage distributions?
- What should I not cite it for?

## 7. Occupation, sector, and job characteristics

Extract:
- whether the paper models occupation, sector, task type, job characteristics, contracts, part-time/full-time, or hours packages;
- whether occupation enters utility, opportunity, wage, or all of these;
- whether occupation is treated as a preference object or an availability object;
- whether it conditions wage offers on occupation;
- whether it treats occupation as part of the feasible job.

Map carefully to my design:
- `loc4` enters opportunity/access, not utility;
- W1 wage draws condition on occupation;
- occupation availability enters through gender-specific opportunity terms.

Flag any double-counting risk discussed or implied.

## 8. Couples and household structure

If relevant, extract:
- unit of analysis;
- singles/couples split;
- joint utility;
- household budget;
- joint labour supply;
- male/female roles;
- whether the couple choice set is a product of partners’ options or a diagonal/joint draw;
- how intra-household welfare is handled;
- equivalence scales, if any.

Map to my NC pilot and pooled model:
- household-level welfare unit;
- joint utility for couples;
- product choice-set issue;
- partner-specific disposable income columns;
- gender-specific leisure and opportunity parameters.

If the paper does not model couples, write “N/A” and explain whether this limits its relevance.

## 9. Estimation method

Extract:
- likelihood;
- simulated likelihood;
- sampling of alternatives;
- importance sampling;
- correction terms;
- maximum likelihood;
- mixed logit / latent class / RURO;
- identification arguments;
- computational methods;
- solver / optimizer;
- standard errors;
- bootstrap;
- simulation error handling.

Write formulas where possible.

Map to my estimation:
\[
P_{ij}
=
\frac{\exp(V_{ij})}
{\sum_{k\in\mathcal C_i}\exp(V_{ik})}.
\]

Answer:
- Does the paper estimate preferences and opportunities jointly?
- Does it correct for sampled alternatives?
- Does it discuss proposal draws or simulation draws?
- Does it provide identification restrictions useful for my access / ability / preference decomposition?

## 10. Welfare analysis

Extract:
- compensating variation;
- equivalent variation;
- equivalent income;
- inclusive value / expected maximum utility;
- social welfare;
- money-metric utility;
- welfare under heterogeneous preferences;
- welfare under random utility;
- welfare under different opportunity sets;
- ex-ante vs ex-post welfare;
- analytical integration over shocks.

Map to my welfare object:
\[
IV_i = \log\sum_j \exp(V_{ij}),
\]
then \(W_i^k\) is obtained by money-metric inversion at measure-specific references.

Answer:
- Does the paper support the use of inclusive value as attained utility?
- Does it support money-metric inversion?
- Does it handle heterogeneous preferences?
- Does it respect or neutralize preferences?
- Does it treat opportunity sets as welfare-relevant?
- Does it discuss welfare under constrained choice sets?

Classify:
- explicit in source;
- derived by analogy;
- not established.

## 11. Relation to \(W^1,\dots,W^6\)

My JMP computes a family \(W^1,\dots,W^6\) spanning responsibility for pay and responsibility for opportunity sets.

For this paper, answer:
- Does it correspond to any one measure \(W^k\)?
- Does it support the general idea of a measure family?
- Does it use a single welfare metric?
- Does it neutralize preferences, opportunities, wages, or circumstances?
- Does it help justify comparing welfare measures across responsibility stances?

Use this table:

| JMP measure/family aspect | Supported by source? | Explicit / analogy / absent | Notes |
|---|---|---|---|
| Ex-ante attained utility | | | |
| Money-metric inversion | | | |
| Own preferences respected | | | |
| Reference preferences | | | |
| Responsibility for pay | | | |
| Responsibility for opportunity set | | | |
| Family / menu of welfare objects | | | |

Be strict. Do not claim support for W¹–W⁶ unless the source really supports it.

## 12. Responsibility, compensation, and equality of opportunity

Extract:
- responsibility-sensitive welfare;
- equality of opportunity;
- circumstances vs effort;
- preference neutrality;
- compensation principles;
- fair income / equivalent income;
- unfair inequality;
- opportunity sets as compensable objects.

Map to my decomposition:
- access = non-responsibility channel;
- ability = contested channel;
- preference = responsibility or reference-preference channel.

Answer:
- Can I cite this source for the normative idea that opportunities are compensation-relevant?
- Can I cite it for separating preferences from circumstances?
- Can I cite it for a responsibility-sensitive empirical welfare measure?
- What should I not cite it for?

## 13. Inequality decomposition

Extract:
- inequality index;
- decomposition by factors/sources;
- Shapley decomposition;
- Shorrocks decomposition;
- opportunity/circumstance decomposition;
- counterfactual equalisation;
- path/order dependence;
- exact decomposition;
- residual terms.

Map to my decomposition:
\[
I(\Omega^k)
=
\phi^{access}_k
+
\phi^{ability}_k
+
\phi^{preference}_k,
\]
where \(\phi\) are Shapley components over equalisation orderings.

Answer:
- Does the paper use Shapley / Shorrocks?
- Does it decompose welfare or income?
- Does it decompose opportunities, preferences, or circumstances?
- Does it justify order-independent decomposition?
- Does it warn against interpreting components causally?

## 14. Microsimulation and policy simulation

Extract:
- tax-benefit microsimulation;
- EUROMOD;
- policy reform simulation;
- disposable income construction;
- budget constraints;
- behavioural vs non-behavioural simulation;
- reform welfare incidence.

Map to my empirical pipeline:
- EUROMOD disposable income;
- structural labour-supply alternatives;
- policy counterfactuals;
- microsimulation as supporting skill, not core identity.

If irrelevant, write “N/A”.

## 15. Inference, uncertainty, and numerical implementation

Extract:
- standard errors;
- bootstrap;
- cluster bootstrap;
- simulation error;
- draw stability;
- effective sample size;
- numerical integration;
- optimization;
- Hessian issues;
- boundary parameters;
- active constraints;
- robustness to draw count;
- computational scaling.

Map to my current issues:
- JAX estimator;
- CONOPT oracle;
- simulation consistency;
- 900 vs 1600 alternatives;
- active-bound `beta_l0_m`;
- bootstrap for welfare/decomposition.

## 16. Main equations

List the paper’s key equations with notation. For each equation, add:

- paper equation number if available;
- meaning;
- JMP analogue;
- whether directly reusable.

If equation numbers are unavailable, write “[equation number unavailable]”.

## 17. Main results

Summarize:
- theoretical results;
- empirical estimates;
- welfare results;
- decomposition results;
- policy results;
- identification results.

Only include what is useful for my JMP. Do not summarize unrelated findings.

## 18. Examples, tables, and figures useful for my JMP

List:
- tables to revisit;
- figures to cite or imitate;
- numerical patterns;
- examples;
- counterexamples;
- diagnostics.

Include page/table/figure numbers if available. If unavailable, write “[verify]”.

## 19. What I can cite this paper for

Give precise citation uses, such as:

- latent jobs / constrained opportunity sets;
- sampled alternatives / proposal correction;
- welfare in random utility;
- heterogeneous preferences and welfare;
- equivalent income;
- equality of opportunity;
- Shapley decomposition;
- microsimulation;
- couples labour supply;
- wage-offer modelling;
- simulation/inference.

Each citation use must be specific.

## 20. What I should not cite this paper for

Prevent overclaiming. Include:
- things the paper does not do;
- things only analogically related;
- claims that require another source;
- points that are my contribution, not theirs.

## 21. Relationship to my contribution

Explain how this source positions my JMP relative to the literature.

Use this table:

| Contribution dimension | What source already does | What my JMP adds |
|---|---|---|
| Latent jobs / constrained opportunities | | |
| Opportunity vs preference separation | | |
| Welfare under heterogeneous opportunities | | |
| W¹–W⁶ responsibility surface | | |
| Shapley access/ability/preference decomposition | | |
| Empirical implementation / EUROMOD | | |
| Inference / computation | | |

## 22. Relationship to closest competitors

If the paper is a close competitor, answer:
- What would a referee say is similar?
- What is genuinely different?
- Is my novelty incremental or substantial relative to this source?
- What sentence should I use to distinguish my JMP?

If not a close competitor, write “N/A”.

## 23. Implementation lessons for my code and pipeline

Extract lessons for:
- data construction;
- wage draws;
- choice-set sampling;
- opportunity density;
- proposal correction;
- EUROMOD integration;
- welfare computation;
- decomposition;
- inference;
- numerical optimization.

## 24. Direct quotations or passages to revisit

Provide 3–7 short quotes or paraphrased passages with page numbers if available.

Rules:
- Do not quote long passages.
- If exact page numbers are unavailable, write “[page unavailable, verify]”.
- If quoting from OCR text, mark “[OCR, verify]”.

## 25. Open questions for my JMP

List questions this paper raises for:
- model specification;
- welfare measurement;
- decomposition;
- estimation;
- inference;
- positioning;
- robustness.

## 26. Final retrieval summary

Write:
- 3-sentence dense summary;
- 5 retrieval keywords;
- 3 “cite-for” bullets;
- 3 “do-not-cite-for” bullets.

## 27. Final extraction table

Create a compact table:

| Object / claim | Source treatment | JMP analogue | Citation use | Warning |
|---|---|---|---|---|

STRICT RULES

1. Do not invent claims, theorem numbers, page numbers, equations, or DOIs.
2. If uncertain, write “[uncertain, needs verification]”.
3. Always distinguish:
   - explicit in source;
   - derived by analogy;
   - not established.
4. Do not confuse this empirical JMP with my separate theory paper.
5. Do not treat W¹–W⁶ as if the source contains them unless it does.
6. Do not overclaim that a source models opportunity sets unless it really does.
7. Do not overclaim that a source performs decomposition unless it really does.
8. If a section does not apply, write “N/A — [brief reason]”.
9. Use LaTeX for mathematical notation.
10. Keep the output retrieval-oriented, not polished prose.
11. Be exhaustive for relevance, but do not summarize irrelevant material.
```

---

# Phase 4 — Build indexes after summaries

Only after you have at least 12–20 extracted summaries.

Tool: **Claude Code Sonnet**.

Expected outputs:

```text
JMP_literature/04_indexes/INDEX_01_master_bibliography.md
JMP_literature/04_indexes/INDEX_02_latent_jobs_and_opportunities.md
JMP_literature/04_indexes/INDEX_03_welfare_and_money_metric.md
JMP_literature/04_indexes/INDEX_04_responsibility_and_equality_of_opportunity.md
JMP_literature/04_indexes/INDEX_05_decomposition.md
JMP_literature/04_indexes/INDEX_06_microsimulation_and_estimation.md
JMP_literature/04_indexes/INDEX_07_inference_and_computation.md
JMP_literature/04_indexes/INDEX_08_writing_bank.md
```

Prompt:

```text
Work locally in JMP_literature.

Read:
- all summaries in 03_summaries/
- 00_admin/JMP_literature_tiers_v1.csv
- JMP_project_state_v1.md
- JMP_welfare_spec_v5.md

Task:
Build retrieval indexes for writing the JMP.

Create:
1. INDEX_01_master_bibliography.md
2. INDEX_02_latent_jobs_and_opportunities.md
3. INDEX_03_welfare_and_money_metric.md
4. INDEX_04_responsibility_and_equality_of_opportunity.md
5. INDEX_05_decomposition.md
6. INDEX_06_microsimulation_and_estimation.md
7. INDEX_07_inference_and_computation.md
8. INDEX_08_writing_bank.md

Rules:
- Organize by claim, not only by author.
- Every claim must list supporting sources.
- Mark each source support as:
  explicit / analogy / background / weak.
- Add “do not overclaim” warnings.
- Do not invent citations.
- Keep the JMP separate from the theory paper.

INDEX_08_writing_bank must include paragraph skeletons for:
1. latent jobs as the empirical unit;
2. opportunity heterogeneity versus preference heterogeneity;
3. why occupation belongs in the opportunity layer;
4. why money-metric welfare must read feasible sets;
5. why W¹–W⁶ is a responsibility-sensitivity surface;
6. why Shapley access/ability/preference decomposition is appropriate;
7. why microsimulation is supporting infrastructure, not the paper’s identity;
8. why the paper is not a country-ranking exercise;
9. why the paper is not merely another structural labour-supply application.
```

---

## Final recommended immediate sequence

Do this next:

```text
1. Claude Code Sonnet:
   run Phase 0 local corpus normalization.

2. Claude Project / ChatGPT Thinking:
   run Phase 1 tiering.

3. ChatGPT Deep Research:
   run only the targeted Phase 2 gap audit.

4. Then summarize the first 12 T1 papers using the extraction prompt above.
```

Do not run Deep Research first. The uploaded corpus is already too rich to ignore. The correct first move is to transform what you already have into a disciplined JMP inventory.

Save this answer as:

```text
JMP_literature_rebuild_plan_v2.md
```

Category: **working library-rebuild plan**.
