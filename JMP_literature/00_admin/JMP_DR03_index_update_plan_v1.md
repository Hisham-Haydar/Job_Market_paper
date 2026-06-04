# JMP DR03 Index Update Plan — v1

**Date:** 2026-06-04
**Source:** `JMP_DR03_assimilation_decision_v1.md` §13; verified against
`INDEX_02`, `INDEX_06`, `INDEX_07` v1 content.

**Rule:** Create a `_v2` file for each touched index; do not overwrite v1.
Indexes not listed here remain at v1 and are not touched.

---

## General principles

- Every new entry added to an index must carry an explicit
  **`[explicit]` / `[analogy]` / `[not-established]`** tag, consistent with
  existing v1 style.
- Every new entry must be followed by a `**Do not overclaim:**` line recording
  the boundary of the source's valid use.
- A summary must be **accepted** before the source is referenced in an index.
  Do not add a citation to an index for a source that is still in the summary
  queue and unwritten.
- Verification-gated sources (Magnac-Robin; Dagsvik-Strøm-Locatelli;
  Crede/Grammatikos; Sun-Leung) must not appear in any index at any version
  until the `JMP_DR03_verification_log_v1.md` §9 check explicitly clears them.

---

## INDEX 02 — Latent Jobs and Opportunities (→ v2)

**Trigger:** Bloemen 2000 summary accepted + Bloemen 2008 summary accepted.
Both must be complete before writing INDEX 02 v2.

### Section: "Latent Jobs"
Add at the end of the existing bullet list:
```
- **Claim:** The restricted-wage-hours-offer structure is the search-theoretic
  antecedent of the JMP opportunity layer: feasible jobs are defined as
  (wage, hours) pairs drawn from an offer distribution, not as points on a
  common grid.
  **Sources:** Bloemen 2000 [explicit job-offer-restriction model]; Bloemen 2008
  [explicit joint wage-and-hours offer search model].
  **Do not overclaim:** Bloemen 2000/2008 model feasible-job offers but contain
  no money-metric welfare object, no W^1-W^6 family, no proposal correction,
  and no access/ability/preference decomposition. Use as model-class motivation
  only.
```

### Section: "Random Opportunities"
Add at the end of the existing bullet list:
```
- **Claim:** The hours-offer distribution in a job-search model is a structural
  precursor to the RURO opportunity density: hours availability is determined by
  what employers offer, not by worker preferences over a common grid.
  **Sources:** Bloemen 2008 [explicit hours-offer distribution in job search];
  Bloemen 2000 [explicit wage-hours offer restrictions].
  **Do not overclaim:** The search-model offer distribution is not the same object
  as the JMP's g(j;x_i) opportunity density; the connection is by analogy (model
  class), not by isomorphism.
```

### Section: "Constrained Choice Sets"
Add at the end of the existing bullet list:
```
- **Claim:** Constrained wage-and-hours offers are modeled explicitly in the
  job-search tradition; this gives a published precedent for the feasibility
  constraint that the JMP embeds in the access channel.
  **Sources:** Bloemen 2000 [explicit]; Bloemen 2008 [explicit].
  **Do not overclaim:** Bloemen 2000/2008 do not contain the JMP's
  welfare/opportunity decomposition; they are precedents for the model structure,
  not for the normative framework.
```

**No other INDEX 02 sections are modified.**

---

## INDEX 06 — Microsimulation and Estimation (→ v2)

**Trigger:** Three sequential triggers, each enabling one addition:
1. Bloemen 2000 + Bloemen 2008 summaries accepted → add to "RURO Estimation"
   and "Wage-Offer Modelling".
2. Bloemen 2010 summary accepted → add to "Couples / Singles".
3. Löffler et al. 2014 summary accepted → add to "Wage-Offer Modelling".

These additions should be written together in a single v2, gated on the four
summaries that actually touch INDEX 06: Bloemen 2000, Bloemen 2008,
Bloemen 2010, and Loffler et al. 2014. Cameron & Miller 2015 does not touch
INDEX 06 and is not a dependency for INDEX 06 v2.

### Section: "RURO Estimation"
After the existing second bullet, add:
```
- **Claim:** The job-offer-restriction tradition (Bloemen line) pre-dates and
  substantiates the latent-jobs framing: it models labor supply as choice among
  restricted (wage, hours) packages rather than over a common hours grid.
  **Sources:** Bloemen 2000 [explicit restricted-offer labor-supply model];
  Bloemen 2008 [explicit job-search with wage-and-hours offers].
  **Do not overclaim:** The Bloemen line does not contain RURO's opportunity-
  density estimation, the JMP welfare object, or the proposal/sampling correction.
  It supports the model-class motivation paragraph, not the estimation section.
```

### Section: "Wage-Offer Modelling"
After the existing second bullet, add:
```
- **Claim:** Wage-preference independence is a maintained assumption of RURO and
  related structural models; it is testable and estimates are sensitive to it.
  **Sources:** Loffler et al. 2014 [explicit wage-exogeneity caution; sensitivity
  of labor-supply and welfare estimates to the assumption]; JMP project state v1
  [explicit: ability channel depends on separability of wage technology].
  **Do not overclaim:** Loffler et al. 2014 tests sensitivity in standard
  (non-RURO) models; apply the caution by analogy to the JMP's ability channel.
  The 2018 published version (loefflerSensitivityStructuralLabor2018) is also
  in the corpus at T3 and may be cited interchangeably for the same caution.

- **Claim:** Hours-and-wage offers are the structural objects behind the access
  channel; they are not merely computational artifacts.
  **Sources:** Bloemen 2000 [explicit hours-and-wage offer restrictions];
  Bloemen 2008 [explicit hours-offer distributions as search equilibrium object].
  **Do not overclaim:** Bloemen 2000/2008 model offers, not the JMP's three-way
  access/ability/preference decomposition.
```

### Section: "Couples / Singles"
After the existing sole bullet, add:
```
- **Claim:** A collective household model with non-participation provides a
  structural contrast to the JMP's unitary assumption: if within-couple
  bargaining matters, the unitary model absorbs it into a joint preference block.
  **Sources:** Bloemen 2010 [explicit collective-household non-participation
  model — background contrast only].
  **Do not overclaim:** The JMP uses a unitary household design. Bloemen 2010 is
  not a model component and does not identify within-couple welfare. Cite only
  as a one-paragraph contrast in the household-unit discussion; do not import
  any bargaining mechanism.
```

**No other INDEX 06 sections are modified.**

---

## INDEX 07 — Inference and Computation (→ v2)

**Trigger:** Cameron & Miller 2015 summary accepted. This is the only DR03
source touching INDEX 07 that can be acted on immediately (all others remain
gated on verification). Write INDEX 07 v2 as soon as the Cameron-Miller summary
is accepted.

### Section: "Bootstrap"
Replace the existing single bullet with the following expanded version:
```
- **Claim:** Headline uncertainty should use cluster-robust bootstrap, especially
  because bound/pinned parameters invalidate simple asymptotic SEs for headline
  welfare/decomposition claims.
  **Sources:** JMP project state v1 [explicit]; JMP welfare spec v5 [explicit];
  Cameron & Miller 2015 [explicit cluster-robust variance and cluster bootstrap
  for household-clustered data — authoritative practitioner anchor].
  **Do not overclaim:** Cameron & Miller 2015 covers the general econometric
  justification; the JMP's specific bootstrap implementation for a structural
  RURO model with bound parameters remains the JMP's own design choice and is
  not pre-approved by C&M.
```

### Section: "Standard Errors"
In the first bullet, add Cameron & Miller 2015 as a supporting source:
```
  **Sources:** JMP project state v1 [explicit]; JMP welfare spec v5 [explicit];
  Cameron & Miller 2015 [explicit: cluster-robust SE justification when
  idiosyncratic errors are correlated within household clusters]; Beffy et al.
  2019 [derived-by-analogy identification trade-off].
```
(Replace the existing `**Sources:**` line in that bullet; no other text changes
in that bullet.)

### Sections that remain unchanged in v2

The following sections are unchanged pending verification-gate outcomes:

- **"Simulation Error"** — Crede/Grammatikos 2022 and Dagsvik-Strøm-Locatelli
  2021 remain gated. The existing project-notes anchors are acceptable until
  those verifications clear.
- **"Sampled Alternatives"** — no new source authorized.
- **"Simulated Likelihood"** — no new source authorized.
- All other sections — no change.

### One-line Train 2009 addition

In the "Simulated Likelihood" section, append at the end of the section (not
as a new claim bullet, but as a standalone reference note):

```
> *Methods reference:* Train (2009), *Discrete Choice Methods with Simulation*
> (MIT Press, 2nd ed.; freely downloadable from author website), is the standard
> reference for quasi-random integration (Halton sequences, MLHS) and simulated
> maximum likelihood in discrete-choice models. Cite for simulation-method
> language only; not a welfare or decomposition source.
```

**No other INDEX 07 sections are modified.**

---

## Indexes with no authorized changes (remain at v1)

| Index | Reason |
|---|---|
| INDEX 00 (T1A/T1B status) | DR03 tier promotions of Bloemen 2000/2008 require updating this index too — but since INDEX 00 is a derived status register, update it together with INDEX 02/06 v2 as a single pass. |
| INDEX 01 (Master bibliography) | Update only after bib entries for Bloemen 2010 and Cameron-Miller 2015 are added to the base `.bib`; the master bibliography index should mirror the `.bib`, not lead it. |
| INDEX 03 (Welfare and money-metric) | No changes authorized now. Loffler et al. 2014 is handled in INDEX 06 "Wage-Offer Modelling"; do not add an INDEX 03 CV/EV note until a later verified need is recorded. |
| INDEX 04 (Responsibility and EOP) | No changes authorized. DR03 suggestions here (Yitzhaki; Lerman-Yitzhaki; Lundberg-Pollak) are rejected or gated. |
| INDEX 05 (Decomposition) | No changes authorized. Sun-Leung 2019 is gated; Shorrocks + Audoly already anchor the interaction claim. |
| INDEX 08 (Writing bank) | Writing-bank paragraphs may be drafted after index v2 files are finalized. Do not update INDEX 08 before INDEX 02/06/07 v2 are written. |

---

## Summary: which indexes update after which summaries

| Completed summary | Index updates triggered |
|---|---|
| Bloemen 2000 (`T1A/Bloemen_2000_job_offer_restrictions.md`) | INDEX 02 v2 (partial); INDEX 06 v2 (partial); INDEX 00 v2 |
| Bloemen 2008 (`T1A/Bloemen_2008_job_search_hours.md`) | INDEX 02 v2 (completes it); INDEX 06 v2 (partial); INDEX 00 v2 |
| Cameron & Miller 2015 (`T2/Cameron_Miller_2015_cluster_robust.md`) | INDEX 07 v2 (completes it); INDEX 01 v2 (after bib entry added) |
| Bloemen 2010 (`T1B/Bloemen_2010_collective_household.md`) | INDEX 06 v2 (Couples/Singles section; contributes to the combined INDEX 06 v2 update) |
| Loffler et al. 2014 (`T2/Loffler_et_al_2014_wage_exogeneity.md`) | INDEX 06 v2 (Wage-Offer Modelling section; completes INDEX 06 v2 once Bloemen 2000/2008/2010 are also complete) |
| Magnac-Robin 2014 (after verification) | INDEX 06 Wage-Offer Modelling v3 (if verified) |
| Dagsvik-Strom-Locatelli 2021 (after verification) | INDEX 03 v2 (discrete compensated effects note) |
| Sun-Leung 2019 (after verification) | INDEX 05 v2 (low-urgency interaction note) |
| Crede-Grammatikos 2022 (after verification) | INDEX 07 v3 Simulation Error section |

**Sequencing rule:** Write INDEX 06 v2 only when the four INDEX-06-relevant
summaries are complete (Bloemen 2000, Bloemen 2008, Bloemen 2010, Loffler
2014). Cameron-Miller 2015 unlocks INDEX 07 v2 only and is not an INDEX 06
dependency. Writing INDEX 06 twice (one partial update per summary) would create
a messy intermediate state. INDEX 02 and INDEX 07 can each be written sooner as
their individual triggers complete.

---

## What is not authorized

- Edits to INDEX 03 (Welfare), INDEX 04 (Responsibility/EOP), INDEX 05
  (Decomposition) based on DR03 recommendations — all the suggested sources
  for those indexes are rejected or gated.
- Adding Chiappori 1988/1992, Lundberg-Pollak 1996, or Mulligan-Rubinstein 2008
  to any index entry, even as a "do not overclaim" caution. These are background
  at most; they earn at most a one-sentence prose mention in writing, not an
  index slot.
- Adding any verification-gated source (§9 of memo) to any index before the
  verification log clears it.
- Overwriting v1 files. Every edit produces a `_v2` file; v1 files are preserved.
