# JMP DR03 Index Update Report — v1

**Date:** 2026-06-04
**Scope:** Surgical v2 index updates following the five accepted DR03 summaries.

No summaries were produced in this session. No existing summaries were edited.
No v1 index files were overwritten. No BibTeX was edited. No external searches
were run.

---

## 1. Index update verdict

**PASSED WITH WARNINGS.**

All four authorized index updates (INDEX 02, 06, 07, 08 v2) have been written
as `_v2` files. v1 files are preserved unchanged. Every new claim carries an
explicit `[explicit]` / `[analogy]` / `[background]` tag and a `Do not
overclaim:` line consistent with the v1 style and the update plan.

The warnings are:
1. **Bloemen 2000 citation warning** (medium priority) — all new claims citing
   Bloemen 2000 carry the `[DP version; journal pages TBC]` flag and instruct
   against using DP page numbers in the manuscript. This warning propagates
   through INDEX 02 v2, INDEX 06 v2, and INDEX 08 v2 §16. It does not block
   index use; it must be resolved before final manuscript page citations.
2. **Löffler 2014 version note** (low priority) — SOEPpapers 675 vs IZA DP
   8281 discrepancy is noted in INDEX 06 v2. The content is version-stable.
3. **Four conditional sources remain gated** — no entry added for Magnac-Robin,
   Dagsvik-Strøm-Locatelli, Crede/Grammatikos, Sun-Leung in any index.

---

## 2. Files inspected

| File | Purpose |
|---|---|
| `JMP_DR03_index_update_plan_v1.md` | Authorised section edits, triggers, sequencing, prohibited changes |
| `JMP_DR03_added_summaries_QC_report_v1.md` | Acceptance verdict and metadata warnings |
| `JMP_DR03_added_summaries_acceptance_list_v1.csv` | 5 accepted summaries, per-source status |
| `JMP_DR03_added_summaries_repair_queue_v1.csv` | 5 repairs (none blocking) |
| `JMP_DR03_verification_log_v1.md` | 4 conditional sources still unresolved |
| `INDEX_02_latent_jobs_and_opportunities_v1.md` | Full v1 content carried forward |
| `INDEX_06_microsimulation_and_estimation_v1.md` | Full v1 content carried forward |
| `INDEX_07_inference_and_computation_v1.md` | Full v1 content carried forward |
| `INDEX_08_writing_bank_v1.md` | Full v1 content carried forward |
| `T1A/Bloemen_2000_job_offer_restrictions.md` | §§5, 8, 12, 13 load-bearing |
| `T1A/Bloemen_2008_job_search_hours.md` | §§5, 8, 12, 13 load-bearing |
| `T2/Cameron_Miller_2015_cluster_robust.md` | §§5, 6, 7, 12, 13 load-bearing |
| `T1B/Bloemen_2010_collective_household.md` | §§1, 5, 6, 7, 12, 13 load-bearing |
| `T2/Loffler_et_al_2014_wage_exogeneity.md` | §§5, 8, 9, 12, 13 load-bearing |

---

## 3. Summaries accepted for indexing

All five mandatory DR03 summaries were confirmed accepted by
`JMP_DR03_added_summaries_QC_report_v1.md` before this index update was written.

| Priority | Summary | Tier | Acceptance status |
|---|---|---|---|
| 1 | `Bloemen_2000_job_offer_restrictions.md` | T1A | ACCEPTED WITH METADATA REPAIR |
| 2 | `Bloemen_2008_job_search_hours.md` | T1A | ACCEPTED WITH MINOR METADATA NOTE |
| 3 | `Cameron_Miller_2015_cluster_robust.md` | T2 | ACCEPTED WITH MINOR METADATA NOTE |
| 4 | `Bloemen_2010_collective_household.md` | T1B | ACCEPTED WITH MINOR METADATA NOTE |
| 5 | `Loffler_et_al_2014_wage_exogeneity.md` | T2 | ACCEPTED WITH MINOR VERSION/OUTLET NOTE |

No conditional source was accepted. No prohibited background source was indexed.

---

## 4. Indexes updated

| Index | v2 file | Sections modified | Trigger |
|---|---|---|---|
| **INDEX 02** | `INDEX_02_latent_jobs_and_opportunities_v2.md` | Latent Jobs (+1 claim); Random Opportunities (+1 claim); Constrained Choice Sets (+1 claim); Identification — new section (+1 claim) | Bloemen 2000 + Bloemen 2008 both accepted |
| **INDEX 06** | `INDEX_06_microsimulation_and_estimation_v2.md` | RURO Estimation (+1 claim); Couples/Singles (+1 claim); Wage-Offer Modelling (+2 claims) | Bloemen 2000 + 2008 + 2010 + Löffler 2014 all accepted |
| **INDEX 07** | `INDEX_07_inference_and_computation_v2.md` | Bootstrap (expanded claim + C&M added as source); Standard Errors (C&M added as source); Simulated Likelihood (Train 2009 reference note added) | Cameron & Miller 2015 accepted |
| **INDEX 08** | `INDEX_08_writing_bank_v2.md` | §§11–16 added (six new paragraph skeletons) | All five accepted |

---

## 5. Indexes not updated

| Index | Reason |
|---|---|
| INDEX 00 (T1A/T1B status register) | Tier promotions of Bloemen 2000/2008 to T1A documented; physical update to be made alongside the tier CSV update. Not touched in this session per plan. |
| INDEX 01 (Master bibliography) | Requires bib entries for Bloemen 2010 and Cameron-Miller 2015 to be added to the base `.bib` first. Not updated. |
| INDEX 03 (Welfare and money-metric) | No changes authorized per update plan. |
| INDEX 04 (Responsibility and EOP) | No changes authorized per update plan. |
| INDEX 05 (Decomposition) | No changes authorized. Sun-Leung 2019 remains gated. |

---

## 6. Claims added

### INDEX 02 — four new claims

**Claim I-02-A** (Latent Jobs section):
The restricted-wage-hours-offer structure is the search-theoretic antecedent of
the JMP opportunity layer.
Sources: Bloemen 2000 [explicit, DP version]; Bloemen 2008 [explicit, *JoLE*].

**Claim I-02-B** (Random Opportunities section):
The hours-offer distribution in a job-search model is a structural precursor to
the RURO opportunity density; hours availability is determined by what employers
offer, not by worker preferences.
Sources: Bloemen 2008 [explicit]; Bloemen 2000 [explicit].

**Claim I-02-C** (Constrained Choice Sets section):
Constrained wage-and-hours offers are modeled explicitly in the job-search
tradition; omitting the offer side inflates estimated preference heterogeneity.
Sources: Bloemen 2000 [explicit]; Bloemen 2008 [explicit].

**Claim I-02-D** (Identification — new section):
In a single cross-section, making the opportunity mechanism richly covariate-
dependent can collapse preference identification; parametric structure and
recovery certification are the key identification discipline.
Sources: Bloemen 2000 [explicit]; Bloemen 2008 [explicit]; Dagsvik & Jia 2016
[explicit]; Beffy et al. 2019 [explicit]; JMP project state v1 [explicit].

---

### INDEX 06 — four new claims

**Claim I-06-A** (RURO Estimation section):
The job-offer-restriction tradition pre-dates and substantiates the latent-jobs
framing; it models labor supply as choice among restricted (wage, hours) packages.
Sources: Bloemen 2000 [explicit]; Bloemen 2008 [explicit].

**Claim I-06-B** (Couples/Singles section):
A collective household model with non-participation provides a structural contrast
to the JMP's unitary assumption; the additive-constant non-identification in such
models justifies deferring intra-household distribution.
Sources: Bloemen 2010 [explicit background contrast; *Economic Journal* 120(543)].

**Claim I-06-C** (Wage-Offer Modelling section):
Wage-preference independence is a maintained assumption; it is testable and
elasticity estimates are highly sensitive to it. Misspecified wage treatment can
roughly double labor-supply elasticities.
Sources: Löffler et al. 2014 [explicit; IZA DP 8281]; JMP project state v1 [explicit].

**Claim I-06-D** (Wage-Offer Modelling section):
Hours-and-wage offers are the structural objects behind the access channel; the
hours-offer distribution is a demand-side object distinct from desired hours,
concentrated at institutional standard hours.
Sources: Bloemen 2000 [explicit]; Bloemen 2008 [explicit].

---

### INDEX 07 — expansions to two existing claims + one reference note

**Expanded claim I-07-A** (Bootstrap section):
Cameron & Miller 2015 added as authoritative practitioner anchor for cluster-
robust variance and cluster bootstrap.

**Expanded claim I-07-B** (Standard Errors section):
Cameron & Miller 2015 added as explicit source for cluster-robust SE
justification with ≈9,657 `idorighh` clusters.

**Reference note I-07-C** (Simulated Likelihood section):
Train (2009) added as a one-line methods reference for quasi-random integration
and SML; not a welfare or decomposition source.

---

### INDEX 08 — six new paragraph skeletons (§§11–16)

**§11:** Why observed labour-supply choices may be constrained by job offers
(Sources: Bloemen 2008 [explicit]; Bloemen 2000 [explicit, DP])

**§12:** Why hours packages are not merely free continuous choices — magnitudes
from Bloemen 2008 (40h offer concentration, overemployed share) and Bloemen 2000
(involuntary non-participation gap)
(Sources: Bloemen 2008 [explicit]; Bloemen 2000 [explicit, DP])

**§13:** Why constrained offers support modelling opportunity separately from
preferences — identification and preference-inflation lessons
(Sources: Bloemen 2008 [explicit]; Bloemen 2000 [explicit, DP])

**§14:** Why wage exogeneity matters for the ability channel — Löffler et al.
elasticity-sensitivity meta-analysis
(Sources: Löffler et al. 2014 [explicit]; JMP project state v1 [explicit])

**§15:** Why cluster-robust inference is required — Cameron & Miller 2015 as
the practitioner anchor for ≈9,657-cluster many-clusters inference
(Sources: Cameron & Miller 2015 [explicit])

**§16:** Internal citation guide for Bloemen 2000 with the DP-version warning
(in-text form, reference form, prohibitions, action required)

---

## 7. Overclaim warnings added

Every new claim in every v2 index carries a `Do not overclaim:` line. The
standing overclaim prohibitions applied in each index:

| Prohibition | Applied to |
|---|---|
| Bloemen 2000/2008 do not contain W^1–W^6, money-metric welfare, proposal correction, or decomposition | INDEX 02 v2 (3 claims), INDEX 06 v2 (2 claims), INDEX 08 v2 (§§11, 12, 13) |
| Bloemen's offers are stochastic (Poisson); JMP feasible sets are deterministic | INDEX 02 v2 (2 claims), INDEX 08 v2 (§11) |
| Bloemen 2010 is a contrast source; do not cite as JMP household model or for W^1–W^6 | INDEX 06 v2 (1 claim) |
| Preference-vs-sharing-rule ≠ access/ability/preference three-way decomposition | INDEX 06 v2 (1 claim) |
| Löffler et al. is not a RURO/latent-jobs paper; not a welfare/decomposition source | INDEX 06 v2 (1 claim), INDEX 08 v2 (§14) |
| Löffler et al. ~0.2→~0.6 elasticity result is single-female Germany/SOEP only | INDEX 06 v2 (1 claim), INDEX 08 v2 (§14) |
| Cameron & Miller is not structural labor-supply or welfare | INDEX 07 v2 (2 claims), INDEX 08 v2 (§15) |
| Cameron & Miller "multiway clustering" ≠ JMP's three-channel decomposition | INDEX 07 v2 (1 claim), INDEX 08 v2 (§15) |
| Cameron & Miller few-clusters apparatus is not required for ≈9,657 clusters | INDEX 07 v2 (1 claim), INDEX 08 v2 (§15) |
| Bloemen 2008 education-type/sector covariate is neither loc4 nor lindi | INDEX 02 v2 (1 claim) |
| Bloemen 2000 DP page numbers must not be used as final manuscript references | INDEX 02 v2 (all claims), INDEX 06 v2 (all Bloemen 2000 references), INDEX 08 v2 (§§11–13, §16) |

---

## 8. Citation metadata warnings carried forward

| Warning | Source | Indexes affected |
|---|---|---|
| **MEDIUM: DP vs journal version** — PDF is 1992 CentER DP 9239; target is *Labour Economics* 7(3):297–312 (2000). Do not use DP page numbers in manuscript. | Bloemen 2000 | INDEX 02 v2, INDEX 06 v2, INDEX 08 v2 |
| **LOW: bibkey** — `Bloemen2000` used informally; reconcile with `bloemenModelLabourSupply2000` | Bloemen 2000 | — (not shown in indexes; internal only) |
| **LOW: bibkey** — `Bloemen2008` informal; reconcile with `bloemenJobSearchHours2008` | Bloemen 2008 | — |
| **LOW: bibkey** — `Bloemen2010` informal; reconcile with `bloemenCollectiveHousehold2010` | Bloemen 2010 | — |
| **LOW: bibkey** — `cameron_miller_2015_cluster_robust` is snake_case; reconcile with `cameronMillerClusterRobust2015` | Cameron & Miller 2015 | — |
| **LOW: outlet** — SOEPpapers 675 vs IZA DP 8281; same paper, two circulations | Löffler 2014 | INDEX 06 v2 (noted in version header) |

---

## 9. Conditional sources excluded

The following four sources remain at `unresolved` in
`JMP_DR03_verification_log_v1.md` and were not indexed:

| Source | Index that would receive it | Status |
|---|---|---|
| Magnac & Robin 2014 | INDEX 06 Wage-Offer Modelling v3 (future) | unresolved |
| Dagsvik Strøm & Locatelli 2021 | INDEX 03 v2 discrete compensated effects (future) | unresolved |
| Sun & Leung 2019 | INDEX 05 v2 interaction note (future) | unresolved |
| Crede / Grammatikos 2022 | INDEX 07 v3 Simulation Error (future) | unresolved |

No entry was added for any of these sources. No placeholder, stub, or pending
note was left in any v2 index for these sources.

---

## 10. What was not done

- **No v1 files were overwritten.** All four index files exist at both v1 and v2.
- **No summaries were produced.** All five DR03 summaries were written in a
  prior session; this session only reads them for indexing.
- **INDEX 00 not updated.** The T1A/T1B status register records Bloemen 2000 and
  Bloemen 2008 as T3 at v1. The physical edits (T3→T1A for both; new entries for
  Bloemen 2010 T1B and Cameron-Miller 2015 T2) have not been made. Apply when
  the tier CSV update is done.
- **INDEX 01 not updated.** The master bibliography cannot be updated until bib
  entries for `bloemenCollectiveHousehold2010` and `cameronMillerClusterRobust2015`
  are added to the base `.bib`.
- **No BibTeX entries added.** The two new sources (Bloemen 2010, Cameron-Miller
  2015) still require `.bib` entries before bibliography or INDEX 01 updates.
- **No tier CSV update made.** Bloemen 2000 and 2008 are T1A in the control
  files but the physical `JMP_literature_tiers_expanded_v1.csv` still reflects
  the pre-DR03 state. Apply after bib entries are confirmed.
- **No §9 verification run.** The four conditional sources remain unresolved.
- **Bloemen 2000 DP/journal repair not executed.** Requires acquiring the
  *Labour Economics* 7(3):297–312 (2000) PDF and re-running the MD extraction.
  Repair queue row R01 (`JMP_DR03_added_summaries_repair_queue_v1.csv`).

---

## 11. Whether literature-review skeleton may proceed

**Yes, conditionally.**

The literature-review skeleton may now be drafted using:
- INDEX 02 v2 (latent jobs, random opportunities, constrained choice sets,
  identification)
- INDEX 06 v2 (structural labor supply, RURO estimation, budget-set, couples
  contrast, wage-offer modelling)
- INDEX 07 v2 (simulated likelihood, sampled alternatives, bootstrap, standard
  errors, simulation error)
- INDEX 08 v2 (all 16 paragraph skeletons)

All five accepted DR03 summaries are indexed. The Bloemen 2000 `[DP version;
journal pages TBC]` flag must be carried into the draft for any Bloemen 2000
page reference or direct quote; do not finalize manuscript citations for Bloemen
2000 until the journal version is confirmed.

The four conditional sources (Magnac-Robin, Dagsvik-Strøm-Locatelli,
Crede/Grammatikos, Sun-Leung) cannot be used in the draft until the
verification log clears them.

INDEX 01 (master bibliography) is not updated; the draft should not list Bloemen
2010 or Cameron-Miller 2015 in a printed bibliography until their bib entries are
confirmed in the base `.bib`.

---

## 12. Immediate next action

1. **Add bib entries** for `bloemenCollectiveHousehold2010` (Economic Journal
   120(543):183–214, DOI `10.1111/j.1468-0297.2009.02292.x`) and
   `cameronMillerClusterRobust2015` (JHR 50(2):317–372) in the base `.bib`.
   Then write **INDEX 01 v2** (master bibliography update).

2. **Apply tier CSV update** — promote Bloemen 2000 and Bloemen 2008 from T3 to
   T1A; add Bloemen 2010 as T1B (new); add Cameron-Miller 2015 as T2 (new);
   apply Löffler 2014 promotion from T3 to T2. Then write **INDEX 00 v2**
   (T1A/T1B status register).

3. **Resolve Bloemen 2000 version** (Repair R01 in the repair queue) — locate
   *Labour Economics* 7(3):297–312 (2000), update PDF, re-extract, update §0 and
   §14 of the summary. Update `[DP version; journal pages TBC]` flags in
   INDEX 02 v2, INDEX 06 v2, and INDEX 08 v2 §16 once confirmed.

4. **Run §9 verification** for the four conditional sources (Magnac-Robin,
   Dagsvik-Strøm-Locatelli, Crede/Grammatikos, Sun-Leung) — manual lookup via
   publisher websites, DOI, Econlit, SSRN. Record outcomes in
   `JMP_DR03_verification_log_v1.md`.

5. **Begin literature-review skeleton draft** — all indexes are now available
   at v2. Use INDEX 08 v2 §§1–16 as the paragraph skeleton template.

---

**INDEX UPDATE STATUS: PASSED WITH WARNINGS**

All four authorized index updates are written. The Bloemen 2000 DP/journal
version warning propagates into the indexes and must be resolved before final
manuscript page citations; it does not block drafting. Four conditional sources
remain gated.
