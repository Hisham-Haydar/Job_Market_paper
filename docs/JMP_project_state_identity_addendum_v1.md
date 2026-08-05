<!-- GOVERNANCE DOCUMENT -->

# JMP Project-State Identity Addendum v1

**Mission:** JMP-M07I — Manuscript Identity Alignment, Stage A
**Output file (repository path):** `docs/JMP_project_state_identity_addendum_v1.md`
**Status:** Draft for Stage B review; not accepted until the Goal 1 Manager issues `docs/missions/JMP_M07I_identity_alignment_acceptance_v1.md`
**Scope:** bounded. This addendum records a supersession boundary for empirical identity and welfare sequencing. It does **not** rewrite `JMP_project_state_latest.md`.
**Numerical work:** none.

**Authoritative inputs**
- `JMP_M07_deputy_closeout_and_identity_ruling_v1.md`
- `JMP_M07I_manuscript_identity_alignment_charter_v1.md`
- `FR_P2a_empirical_inference_v2.md`
- `JMP_core_packet_v1.md`, `JMP_abstract_clean_v1.md`, `JMP_extended_abstract_clean_v1.md`, `JMP_intro_skeleton_v1.md`

**Next authorised action:** Stage B independent consistency review (ChatGPT GPT-5.6 Thinking, high reasoning, no repository writes), then Goal 1 Manager acceptance.

---

## 1. The ruling being recorded

The Deputy Programme Director's binding empirical-identity ruling of 2026-08-05 fixes the paper's current and only accepted empirical application as:

> **France 2016 single-adult households, P2a region-live specification, 1,555 households.**

This identity controls the title page, abstract, extended abstract, introduction, contribution statement, data section, results roadmap and welfare mission.

Couples and pooled 2015–2017 work are **not** co-primary empirical baselines. They may appear only as (i) historical model-development or certification anchors where technically necessary, (ii) later external-validity or scale extensions, or (iii) future work conditional on successful validation of the singles pipeline. They may not appear in the abstract or introduction as delivered results, promised coequal applications, or the source of current paper-facing estimates.

The instruction that the "singles prototype is obsolete," and any equivalent instruction wherever it appears in project documentation, is **superseded**.

## 2. Staged-extension framing

One concise staged sentence is authorised, as subordinate framing rather than a contribution claim:

> The empirical analysis first establishes the complete estimation–welfare–decomposition pipeline for France 2016 single-adult households; extension to couples and pooled years is subsequent work.

The contribution claim itself remains the consistent structural treatment of access, ability and preferences across estimation, welfare measurement and decomposition. The headline empirical cut is opportunity environment versus preferences; the access-versus-ability split is the nested supporting decomposition inside the opportunity component.

**One technically necessary historical reference is permitted** and is used once, in `JMP_core_packet_v2.md` §4: eight couples leisure coordinates in the 47-coordinate parameter vector are pinned because the singles objective does not reference them, and two survey-year dummies are pinned because their covariates are identically zero in a 2016-only sample. This is a property of the accepted parameter table, is required to explain the 47/37/35 arithmetic, and carries no inferential content in this application. It is not a couples result and must not be presented as one.

## 3. What changed, document by document

### 3.1 `JMP_core_packet_v1.md` → `docs/JMP_core_packet_v2.md`

| Location | v1 | v2 |
|---|---|---|
| §2 pitch | "household AEI-style money-metric welfare", couples implied | Singles P2a named; welfare stated as money-metric household welfare conditional on the constrained feasible set; nested access/ability added |
| §3 core question | Two-way opportunity vs preference only | Three-way access/ability/preference language, with the headline two-way cut and the nested access/ability cut explicitly ordered |
| §4 safe claims | "with the **couples sample** as the baseline empirical unit" | Singles P2a, 1,555 households; plus accepted inference facts (1,555 clusters, 1555/1520 correction, misspecification-robust reading, 47/10/37/2/35 arithmetic, `NA` convention) and the four regional-access verdicts in bounded wording |
| §4 job representation | "wage-vigintile × 4-hour-interval" couples packages | Packages described by hours, occupation and regional labour market, with an estimated log-wage density — the description carried by the accepted inference section |
| §5 forbidden claims | "should not describe the paper using the obsolete Belgium or singles prototype" | Reversed: singles is the accepted application; couples/pooled must not be presented as delivered results. Added prohibitions on unconditional active-set claims, substantive `gsur` labelling, over-reading non-rejections, responsibility labelling of estimated components, pre-LOC4 magnitude freezing, and delta-method substitutes |
| §6/§7 | Reproduced v1 abstract and extended abstract inline | Replaced by pointers to the controlling v2 files, to prevent identity drift through stale copies |
| §8 baseline | "household/couples sample… should replace all earlier Belgium or singles prototypes" | France 2016 singles P2a as the baseline; access block and wage density described as the two opportunity channels |
| §9 main table | "France 2016 couples prototype decomposition" | Singles P2a table with placeholder cells, a nested access/ability panel, and the four-scenario W-4 sensitivity |
| §10 main figure | Couples-framed stacked bar | Singles-framed stacked bar with the opportunity segment subdivided |
| §11 writing priority | Standardise on "France 2016 couples" | Standardise on France 2016 singles P2a; status stated as estimation and inference accepted, welfare not yet delivered |
| §12 coding priority | "rerun the couples RURO estimation", freeze couples sample | Replaced by an empirical-priority section that restates M08 sequencing from the deputy closeout only, and authorises nothing |

### 3.2 `JMP_abstract_clean_v1.md` → `manuscript/JMP_abstract_clean_v2.md`

| Location | v1 | v2 |
|---|---|---|
| Application sentence | "a France-based RURO model… in which **couples** choose among latent job packages" | France 2016 single-adult households, P2a region-live, 1,555 households |
| Mechanism sentence | "an opportunity mechanism for discrete wage-hours opportunities" | Access mechanism for discrete job opportunities **and** a wage density through which ability-related characteristics operate |
| Decomposition sentence | Opportunity vs preference only | Same headline, with the opportunity component split further into access and ability |
| Evidence | No empirical finding stated | One bounded sentence: regional access block jointly relevant; measured access heterogeneity concentrated in one GSUR dimension rather than diffuse across NUTS-1 geography or urbanisation |
| Magnitudes | None claimed | Explicit placeholder pending M08 acceptance and LOC4 |
| Normative clause | "under a responsibility-sensitive interpretation" | Retained, but marked as an interpretive stance of the paper rather than a property established by the estimates |
| Scope | Absent | Staged sentence added; couples mentioned exactly once |

### 3.3 `JMP_extended_abstract_clean_v1.md` → `manuscript/JMP_extended_abstract_clean_v2.md`

| Location | v1 | v2 |
|---|---|---|
| §2 question | Two-way framing | Three-way access/ability/preference framing with explicit nesting order |
| §4 mechanism | Opportunities govern which packages are feasible | Extended to earning capacity within reachable packages; normative stance flagged as a stated reading, not an estimated property |
| §5 setting | "implemented baseline is a household/couples sample, not a single-person prototype"; couples filter rules; "obsolete Belgium fallback" | Singles P2a, 1,555 households; one-likelihood-term-per-household note; staged-extension sentence; obsolescence language removed |
| §6 strategy | Spouse-level packages, joint household bundles, Box-Cox couples utility with leisure–leisure interaction, "maximum likelihood" | Individual packages over hours, occupation and region; log-wage density with education and potential-experience shifters; Box-Cox singles utility with sex-specific leisure terms; constrained quasi-maximum likelihood |
| §6 (new paragraph) | Absent | Accepted inference summarised: clustering and finite-sample correction, misspecification-robust reading, 47/10/37/2/35 arithmetic, conditional covariance, the four regional-access verdicts in bounded wording, and the accompanying cautions |
| §7 welfare | "AEI-style… relative to a **joint** non-work reference state" | Money-metric household welfare relative to a non-work reference state; adds the W-4 near-boundary disclosure and the pre-registered four-scenario sensitivity |
| §8 decomposition | Counterfactuals defined over spouse-specific region × education cells | Counterfactual construction deferred to the frozen welfare-input design; nested access/ability cut added; magnitude placeholder and the pre-LOC4 freeze prohibition added |
| §9 contribution | Unchanged in substance | Nested access/ability separation added to the inequality-analysis contribution |
| §10 risk | "France RURO estimates still show normalization and convergence problems"; unresolved sample construction; "the exact role of gsur" | Replaced with the accepted-evidence qualifications: conditional active-set inference, non-gating near-boundary diagnostic, LOC4 sequencing. Stale instability claims removed because they contradict the accepted estimation and inference |
| §11 prototype | "feasible France 2016 **couples** exercise"; jobloc/joblind/jobtot; region × education partition; couples utility | Singles P2a exercise on accepted estimates; certified baseline wage specification vs LOC4; access block as the opportunity structure; nested panel and four sensitivity scenarios; success criterion restated as a complete reproducible pipeline rather than a presumed finding |

### 3.4 `JMP_intro_skeleton_v1.md` → `manuscript/JMP_intro_skeleton_v2.md`

| Location | v1 | v2 |
|---|---|---|
| ¶2 | Taste heterogeneity vs unequal access to hours packages | Adds unequal earning capacity within reachable packages; normative stance flagged as adopted, not estimated |
| ¶3 | Two-way question | Three-way question with explicit headline/nested ordering |
| ¶5 | Three-step contribution, two-factor decomposition | Same three steps; Shapley-Shorrocks stated without the "two-factor" label since the nested cut is now part of the design |
| ¶6 | "France 2016… household/couples sample"; spouse-level wage-vigintile × 4-hour packages; "implemented but not yet fully stabilized" | Singles P2a, 1,555 households; package description aligned to the accepted section; bounded regional-access finding with its cautions; conditional-inference and W-4 acknowledgements; staged-extension sentence |
| ¶7 roadmap | Couples sample section; no results section | Singles sample section; a results-and-inference section inserted; nested access/ability added to the decomposition section; LOC4 sequencing added before any headline magnitude |
| Citations | `[cite France status memo]` | `[cite France inference section]` where the claim now rests on `FR_P2a_empirical_inference_v2.md`; other citation placeholders unchanged |

## 4. Supersession boundary for `JMP_project_state_latest.md`

For **empirical identity** and **welfare sequencing** only, the following classes of statement in `JMP_project_state_latest.md` are superseded by the deputy ruling and by the v2 identity documents. Everything else in that document — repository authority, mission history, artifact custody, certification history — is unaffected by this addendum.

**Superseded (empirical identity):**

1. Any statement naming a couples sample, a pooled 2015–2017 sample, or the 47-parameter pooled certified baseline as the paper-facing or current empirical application. These remain valid as certification history and as the origin of the parameter vector; they are no longer the paper's identity.
2. Any statement that the singles prototype is obsolete, a fallback, superseded, or otherwise not the paper's application.
3. Any statement describing the behavioural baseline in couples terms — spouse-specific leisure with a leisure–leisure interaction, joint household job bundles, or a joint non-work welfare reference — as the current specification.
4. Any circumstance-partition statement defining opportunity heterogeneity over spouse-specific region × education cells as the paper's baseline partition.

**Superseded (welfare sequencing):**

5. Any requirement to validate the full 2015/2016/2017 × singles/couples grid before welfare integration. M08 validates the France 2016 P2a singles production path only; other cells are deferred.
6. Any sequencing in which welfare magnitudes may be frozen, or a preferred specification declared, before the LOC4 four-density robustness. LOC4 Path B is binding.
7. Any provision treating asymptotic delta-method standard errors as a substitute for the sequenced bootstrap on headline welfare and decomposition estimates.

**Explicitly not superseded:** the 47-coordinate parameter vector and its pinning structure; the accepted Phase-3, Phase-4 and Phase-5 results; the restricted-custody rules for score and household-level welfare artifacts; the prohibition on committing raw microdata or household-level welfare vectors to the paper repository; and the Tier-2 halt triggers.

## 5. Input gap recorded for the Goal 1 Manager

Four documents named as binding inputs by the M07I charter were **not supplied to Stage A**: `FR_P2a_inference_appendix_note_v2.md`; `JMP_M07_goal_manager_acceptance_v1.md`; `JMP_M08_welfare_input_handoff_v1.md`; and `JMP_project_state_latest.md`.

Consequences, all deliberate:

- No welfare-design internal is asserted anywhere in the v2 documents beyond what §5.5 of `FR_P2a_empirical_inference_v2.md` establishes. The construction of the opportunity-equalization and preference-neutralization counterfactuals is deferred by name to the frozen M08 handoff rather than restated.
- No appendix content is cited.
- §4 above specifies supersession **by claim class and content** rather than by section or line reference. A line-level mapping cannot be produced without `JMP_project_state_latest.md` and is left as an open item for the Goal 1 Manager, who may either supply the file for a bounded v2 of this addendum or confirm that class-level supersession is sufficient.

## 6. Unresolved decisions

1. **Title divergence.** The identity documents carry *Opportunity Constraints as a Driver of Welfare Inequality: A Latent-Jobs Structural Decomposition Approach*; programme governance headers carry *Unequal Job Opportunities and Well-Being Inequality: A Latent-Jobs Structural Decomposition*. The charter forbids a title decision in this mission, so the provisional identity-document title is retained unchanged and the divergence is escalated to the Goal 1 Manager.
2. **Headline inequality index.** The accepted inference section contemplates a headline index that may differ from the Gini. The v2 documents keep the Gini as the baseline index and note the possibility; resolution belongs to M08.
3. **Line-level project-state supersession.** See §5.
4. **Positioning memo.** `JMP_literature_positioning_memo_v2.md` still describes the France 2016 couples prototype as the empirical anchor in §§1, 3, 5, 7 and 8. It is not among the six authorised M07I outputs and has therefore **not** been revised. Circulating it unrevised alongside the v2 identity documents would reintroduce the contradiction this mission removes; a follow-on bounded task is recommended.
