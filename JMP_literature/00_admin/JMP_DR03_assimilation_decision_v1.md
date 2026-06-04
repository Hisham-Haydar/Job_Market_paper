# JMP DR03 Assimilation Decision — v1

**Intended location:** `JMP_literature/00_admin/JMP_DR03_assimilation_decision_v1.md`
**Status:** decision memo. Authorizes a bounded set of additions. Does not rerun Phase 0 or Phase 1. Does not discard existing indexes.
**Inputs:** `DR03_JMP_targeted_gap_audit_v1.md`; existing `INDEX_01`–`INDEX_07_v1`; `JMP_literature_tiers_expanded_v1.csv`.

---

## 1. Purpose

To decide, source by source, which DR03 recommendations are assimilated into the JMP literature library, at which tier, and with what gating. DR03 is treated as an advisory audit, not an authority. Recommendations are accepted only where they fill a genuine gap in the accepted T1A/T1B corpus and survive a verification check. The memo also fixes the tier of each accepted source, since DR03 over-promotes several candidates to Tier 1A without justification.

---

## 2. DR03 audit verdict

DR03 is **partially reliable and must be filtered, not adopted wholesale.**

Two halves, treated separately:

- **Credible half (DR03 §§3–6, §17–19):** the strengths/weaknesses diagnosis is accurate, and the targeted Tier 1/Tier 2 candidates (Bloemen, Cameron-Miller, Löffler et al., Dagsvik-Strøm-Locatelli, Magnac-Robin) are real, locatable, and on-topic. The index-update and summary-need recommendations are mostly sound.
- **Unreliable half (DR03 §§9–13):** the "missing welfare / decomposition / couples / wage-offer / numerical" lists are heavily padded with references that are fabricated, misattributed, or garbled. These are rejected as a block, with a small number of genuine simulation references salvaged (Train 2009; McFadden-Train 2000).

Net verdict: assimilate the targeted core (Bloemen line + named methods papers), demote the couples-bargaining papers DR03 over-promoted, gate three sources on verification, and reject the padded lists. The corpus's central weakness DR03 correctly identifies — thin coverage of job-offer-restriction models and of explicit cluster-robust inference — is real and worth closing.

---

## 3. What DR03 gets right

- **The job-offer-restriction gap is real.** The accepted corpus models latent jobs via Dagsvik-Jia and Capeau-Decoster but omits the Bloemen line, which defines an offer as a wage-hours package and is the closest search-theoretic antecedent to the JMP's opportunity layer. INDEX 02 ("Random Opportunities," "Constrained Choice Sets") has a visible hole here.
- **The inference gap is real.** INDEX 07 repeatedly asserts a cluster-robust bootstrap plan with no published methodological anchor ("the accepted T1A/T1B literature does not supply the exact JMP bootstrap implementation"). Cameron & Miller (2015) closes that anchor cleanly.
- **The wage-exogeneity gap is real.** No accepted source stress-tests the wage-preference independence assumption. Löffler, Peichl & Siegloch (2014) is the correct citation for that vulnerability, and it bears directly on the ability channel (INDEX 06 "Wage-Offer Modelling").
- **The over-weighting diagnosis is fair.** The corpus does lean heavily on the Dagsvik-Jia and Fleurbaey-Maniquet lines; adding the Bloemen search lineage genuinely broadens the model-class coverage rather than restating it.
- **The theory-paper boundary caution is correct** and consistent with INDEX 03/04: Fleurbaey-Maniquet stays an imported normative primitive, not empirical support.

---

## 4. What DR03 overstates

- **Tier inflation.** DR03 assigns T1A to Bloemen 2010, Mulligan & Rubinstein 2008, and (implicitly) the couples-bargaining cluster. None belongs in the latent-jobs identification spine that defines T1A. Bloemen 2010 is at most T1B; Mulligan-Rubinstein is context, not core.
- **Mulligan & Rubinstein mischaracterized.** DR03 frames it as a "noncooperative household bargaining" and "coupled decision" source. It is primarily a female wage-selection / gender-wage-gap-over-time paper. It is wage-selection context, not a couples joint-choice model, and is not authorized as a couples source.
- **Couples-bargaining relevance overstated.** Chiappori 1988/1992 and Lundberg-Pollak 1996 are collective/bargaining models. The JMP's household unit is unitary by design and intra-household distribution is explicitly out of scope (INDEX 06). These are background contrast at most, not corpus additions that change any claim.
- **Padded "missing" lists.** DR03 §§9–13 list references that are fabricated or misattributed (see §10 below). Treating these as a literature gap would inject phantom citations into the bibliography.
- **"Occupation-conditioned wage" gap oversold.** DR03 implies the literature should supply occupation-as-access support. It cannot — INDEX 02 already records that occupation-as-access is the JMP's own addition with no direct precedent. No DR03 source changes that; it remains a design choice to defend, not a citation to acquire.

---

## 5. Accepted new T1A sources

| Source | Bibkey (provisional) | Why T1A | Cite for | Do NOT cite for |
|---|---|---|---|---|
| Bloemen, H.G. (2000), "A model of labour supply with job offer restrictions," *Labour Economics* 7(3):297–312 | `bloemenModelLabourSupply2000` | Closest published antecedent to the JMP opportunity layer: defines feasible jobs as restricted wage-hours offers; sits on the latent-jobs identification spine | Formal model of restricted wage×hours offers; contrast to fixed-grid; constrained-choice-set motivation | Money-metric welfare, W¹–W⁶, or the access/ability/preference decomposition |
| Bloemen, H.G. (2008), "Job search, hours restrictions, and desired hours of work," *Journal of Labor Economics* 26(1):137–179 | `bloemenJobSearchHours2008` | Rigorous search model with joint wage-and-hours offers; direct precursor to RURO opportunity-density reasoning | Mechanism of hours-and-wage offers; hours-offer distributions; empirical search identification | Welfare decomposition, responsibility cuts, or the proposal correction |

These two are the only authorized T1A promotions. Both already exist in your base `.bib` (`bloemenModelLabourSupply2000`, `bloemenJobSearchHours2008`), so this is a tier promotion, not a new acquisition.

---

## 6. Accepted new T1B sources

| Source | Bibkey (provisional) | Tier decision | Cite for | Do NOT cite for |
|---|---|---|---|---|
| Bloemen, H.G. (2010), "An empirical model of collective household labour supply with non-participation," *Economic Journal* 120(543):183–214 | `bloemenCollectiveHousehold2010` | **T1B, not T1A.** It is a structural couples model with non-participation — more than background — but it is collective/bargaining, off the JMP's unitary-household design and off the latent-jobs identification spine. T1B is the ceiling. | Modeling joint work decisions with non-participation; contrast of collective vs unitary household assumptions | The JMP's latent-job welfare object, opportunity density, or sampling/integration issues |

No other T1B additions are authorized. Chiappori 1988/1992 are explicitly held at background (§8), not T1B, because the JMP does not adopt a collective framework and they would only ever appear as a one-line contrast.

---

## 7. Accepted new T2 sources

| Source | Bibkey (provisional) | Role | Cite for | Gating |
|---|---|---|---|---|
| Cameron, A.C. & Miller, D.L. (2015), "A Practitioner's Guide to Cluster-Robust Inference," *Journal of Human Resources* 50(2):317–372 | `cameronMillerClusterRobust2015` | Inference infrastructure (INDEX 07) | Justification of cluster-robust variance and cluster bootstrap for household-clustered data | None — well-known, verifiable |
| Löffler, M., Peichl, A. & Siegloch, S. (2014), "Structural Labor Supply Models and Wage Exogeneity," IZA DP 8281 / ZEW | `lofflerStructuralLaborSupply2014` | Wage-exogeneity / structural-identification support (INDEX 06 RURO estimation / Wage-Offer Modelling) | Sensitivity of labor-supply and welfare estimates to the wage-preference independence assumption; motivates an ability-channel robustness check | Use WP version; note 2018 published descendant exists. Already in base `.bib`. No INDEX 03 edit is authorized now. |
| Magnac, T. & Robin, J.-M. (2014), wage-offer-distribution estimation | `magnacRobinWageOffer2014` | Wage-offer-distribution support for the ability channel (INDEX 06 "Wage-Offer Modelling") | Modeling/estimating wage-offer distributions as the wage-technology object behind the ability channel | **Conditional accept — see §9.** DR03's metadata is internally inconsistent (two different page ranges, two title variants). Slot reserved; do not enter the bibliography until citation is verified. |

Train (2009), *Discrete Choice Methods with Simulation* is additionally accepted as an **optional T2/T3 methods reference** for simulation-error and quasi-random integration language in INDEX 07 — it is a standard textbook, verifiable, and the one genuinely useful item salvaged from DR03 §13. Not required before the literature skeleton.

---

## 8. Sources to demote or treat as background

| Source | DR03 placement | Decision | Reason |
|---|---|---|---|
| Mulligan & Rubinstein (2008), QJE | T1A | **Background context (T3 / defer)** | Wage-selection and gender-wage-gap-over-time paper, not a couples joint-choice model. Usable only as context for female wage selection; not authorized as a couples or core source. |
| Chiappori (1988), *Econometrica* | T1B | **Background** | Collective household model; JMP is unitary and intra-household distribution is out of scope. One-line contrast only. |
| Chiappori (1992), *JPE* | T1B | **Background** | Same as above. |
| Lundberg & Pollak (1996), *JPE* | T1B (low urgency) | **Defer / background** | Noncooperative bargaining; relevant only if an intra-household bargaining discussion is later added, which is currently out of scope. |

None of these requires a full summary. If any is cited, it is a single contrast sentence in the household-unit paragraph, flagged "background — not a JMP model component."

---

## 9. Sources requiring verification before inclusion

| Source | What to verify | Why gated |
|---|---|---|
| Magnac & Robin (2014), wage-offer distributions | Exact author list, title, journal, volume, pages, DOI. DR03 gives "JPE 122(5):500–536" in one place and "122(5):1007–1044" in another, with two title variants. | Internal inconsistency is a strong signal the citation is garbled or conflated with another paper (e.g. the Postel-Vinay/Robin or Bontemps/Robin/van den Berg wage-offer lineage). Do not enter until confirmed. |
| Dagsvik, Strøm & Locatelli (2021), "Marginal compensated effects in discrete labor supply models," *Journal of Choice Modelling* 41:100326 | DOI and open-access availability; whether content (discrete Slutsky/compensated effects) actually serves the welfare layer. | Plausibly real and on-topic, but unverified. If confirmed, candidate T2 for the welfare-methodology / discrete-compensated-effects note. |
| Crede / Grammatikos (2022), "Sampling effects in simulated maximum likelihood," *Journal of Econometrics* | Whether the paper exists; correct author spelling (DR03 writes both "Crede" and "Creed"); publication status. | Author-name inconsistency plus "forthcoming" status is a red flag. Do not cite the ESS/simulation-error argument to this until confirmed; INDEX 07 currently rests that claim on project notes, which is acceptable in the interim. |
| Sun & Leung (2019), "Accounting for interactions in Shapley decompositions," *J. Economic Inequality* | Existence, exact title, venue. | If real, a useful methodological cite for the symmetric-interaction-allocation claim in INDEX 05. Until verified, that claim stays anchored to Shorrocks 2013 + Audoly et al. 2025, which already support it. |

Verification is a manual lookup (publisher / RePEc / DOI), not a Deep Research rerun.

---

## 10. Sources to reject or defer

Rejected as fabricated, misattributed, or off-topic (DR03 §§9, 10, 12, 13):

- **Aigner, Lovell, Schmidt (1976)** — DR03 describes it as welfare-with-unobserved-heterogeneity; it is the stochastic-frontier production-function paper. Misattributed. Reject.
- **"Daly (2010) VSL," "Arrow & Hancock (1982)," "Sortium & Zollner (2006)," "Campa & Kovacs (2004)," "Ferson & Thrall (1996)," "Qi, Moulin, Xie (2015)," "Magnac (1991) Efficiency Cost of Unemployment Benefits"** — phantom or wrongly described; none is a recognizable, on-topic reference. Reject.
- **Lerman & Yitzhaki (1985), Yitzhaki (1991), Duro & Esteban (already in corpus), Burkhauser et al. (2000)** — additive/source decomposition history. Not needed: the decomposition spine is Shorrocks 1982/2013 + Audoly et al. 2025, already accepted. Defer; not a gap.
- **Chiappori (1985), Blundell-Chiappori-Meghir-Weber (2007), Eckstein-Wolpin (1989), Hyslop (2001)** — collective/dynamic couples models; out of scope per §8. Defer.
- **Hicks (1946), Barsky et al., Kleinjans (2004), Fosgerau-Karlström (2010), Bhat (2001), McFadden-Train (2000)** — McFadden-Train and Bhat are real simulation references but redundant given Train (2009) is accepted as the single methods anchor; the rest are historical or tangential. Defer.

Rejection here means "not assimilated now." Any can be revisited if a specific drafting need arises.

---

## 11. PDF acquisition decisions

- **Already held (no acquisition):** Bloemen 2000, Bloemen 2008, Löffler-Peichl-Siegloch 2014 are in the base `.bib` with file paths. Confirm PDFs resolve.
- **Newly held locally:** Bloemen 2010 (*Economic Journal*) and Cameron & Miller 2015 (*JHR*) are present in `Literature/`; create bib entries and record the local file paths before bibliography/index updates.
- **Acquire after verification only:** Magnac & Robin 2014; Dagsvik-Strøm-Locatelli 2021; Sun & Leung 2019; Crede/Grammatikos 2022. Do not spend acquisition effort until §9 verification passes.
- **Do not acquire:** everything in §10.
- **Optional:** Train 2009 (textbook; library access sufficient, no PDF needed in corpus).

---

## 12. New summary decisions

Required before the literature-review skeleton:

- **Full T1 summary (`summary_T1.md` template):** Bloemen 2000; Bloemen 2008. These are new T1A and must be summarized at full depth, with section 5 (opportunity mechanism) and section 8 (identification) as the load-bearing sections.
- **Trimmed T2 summary (`summary_T2.md` template):** Bloemen 2010 (T1B but a trimmed summary suffices given its contrast role); Cameron & Miller 2015 (inference — sections 0,1,2,8 carry it); Löffler et al. 2014 (wage exogeneity — sections 4,5,8).

Not required before the skeleton (summarize only if cited):
- Magnac & Robin 2014, Dagsvik-Strøm-Locatelli 2021 — only after §9 verification.
- Chiappori, Lundberg-Pollak, Mulligan-Rubinstein — background, no summary; a one-line note in the household-unit paragraph is enough.

No existing summary is rewritten. No re-extraction of the accepted 23.

---

## 13. Index-update decisions

Authorized, surgical edits to existing v1 indexes (create v2 of each touched index; do not overwrite v1):

- **INDEX 02 (Latent Jobs & Opportunities):** add Bloemen 2000 and Bloemen 2008 under "Latent Jobs" (wage-hours offers) and "Random Opportunities" (offer draws), each tagged `[explicit job-offer-restriction precedent]`. Add a "do not overclaim" line: Bloemen models offers but no money-metric welfare or proposal correction.
- **INDEX 06 (Microsimulation & Estimation):** under "RURO Estimation" / "Wage-Offer Modelling," add Löffler et al. 2014 as `[explicit wage-exogeneity caution]`; add Bloemen 2000/2008 as `[explicit hours-and-wage offer precedent]`. Under "Couples/Singles," add Bloemen 2010 as `[background collective-model contrast]` only — with the existing caution that unitary precedent does not identify within-couple welfare.
- **INDEX 07 (Inference & Computation):** under "Bootstrap" and "Standard Errors," add Cameron & Miller 2015 as `[explicit cluster-robust/bootstrap anchor]`, replacing the current reliance on project notes alone. Leave the ESS/simulation-error claims on project notes until Crede/Grammatikos and Dagsvik-Strøm-Locatelli are verified.
- **INDEX 03/04/05:** **no changes authorized now.** DR03's suggested additions here (Yitzhaki, Lerman-Yitzhaki, Lundberg-Pollak, Magnac-Robin pending) are either rejected (§10) or gated (§9). The decomposition and welfare indexes stay as v1.

---

## 14. Writing-bank implications

- The **model-class / motivation** paragraph gains a real search-theoretic antecedent (Bloemen 2000/2008): the JMP can now position the opportunity layer as a structural-welfare descendant of the job-offer-restriction tradition, not only of the Dagsvik-Jia RURO line. This strengthens the "departure from fixed grids" framing without overclaiming.
- The **inference / robustness** section gains a citable standard (Cameron & Miller 2015) for the cluster-robust bootstrap, removing a soft spot where the plan currently cites itself.
- The **identification-risk** discussion gains Löffler et al. 2014 as the named source for the wage-exogeneity vulnerability, which feeds the access-vs-ability bracket argument.
- **No writing-bank claim may yet rest on** Magnac-Robin, Dagsvik-Strøm-Locatelli, Crede/Grammatikos, or Sun-Leung. Until §9 clears, the ability-channel-wage-offer and ESS arguments keep their existing anchors.
- The **theory-paper boundary** is unchanged: Bloemen and the methods papers are empirical/econometric and carry no W¹–W⁶ content. The Haydar-Maniquet theory paper remains the sole home of the axiomatic family.

---

## 15. What is not authorized

- Re-running Phase 0 or Phase 1.
- Discarding or rewriting the existing T1A/T1B indexes (v1).
- Promoting Bloemen 2010 or Mulligan-Rubinstein to T1A.
- Adding any couples/collective model as a corpus component rather than a background contrast.
- Adding any §10 source to the bibliography.
- Entering Magnac-Robin, Dagsvik-Strøm-Locatelli, Crede/Grammatikos, or Sun-Leung into the bibliography or any index before §9 verification.
- Any new occupation-as-access citation — it remains the JMP's own design point with no published precedent.
- A broad literature search. The gap is closed by the targeted additions above; no further Deep Research is warranted.

---

## 16. Immediate next action

1. Promote Bloemen 2000 and Bloemen 2008 to T1A and Capeau et al. 2015 per the expanded-tiers note already flagged; confirm their PDFs resolve in the base `.bib`.
2. Record the two newly held PDFs, Bloemen 2010 and Cameron & Miller 2015, in the bibliography before bibliography/index updates.
3. Produce three new summaries before any literature-skeleton drafting: full T1 for Bloemen 2000 and Bloemen 2008, trimmed T2 for Cameron & Miller 2015. (Bloemen 2010 and Löffler trimmed summaries can follow.)
4. Run the §9 verification lookups (Magnac-Robin, Dagsvik-Strøm-Locatelli, Crede/Grammatikos, Sun-Leung) as a single manual pass; record outcomes in a short `JMP_DR03_verification_log_v1.md`.
5. Apply the INDEX 02 / 06 / 07 edits as v2 files; leave INDEX 03/04/05 at v1.

Save this memo as `JMP_literature/00_admin/JMP_DR03_assimilation_decision_v1.md`.
