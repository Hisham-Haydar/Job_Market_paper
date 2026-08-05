<!-- GOVERNANCE DOCUMENT -->

# JMP Project-State Identity Addendum v2

**Mission:** JMP-M07I — Manuscript Identity Alignment, Stage D (single authorized correction cycle)
**Output file (repository path):** `docs/JMP_project_state_identity_addendum_v2.md`
**Supersedes:** `docs/JMP_project_state_identity_addendum_v1.md` — retained immutable as history
**Corrections applied:** Stage-B review §7, corrections 3, 4 and 5
**Status:** Stage D output; not accepted until the Goal 1 Manager issues `docs/missions/JMP_M07I_identity_alignment_acceptance_v1.md`
**Scope:** bounded. This addendum records a supersession boundary for empirical identity and welfare sequencing. It does **not** rewrite `JMP_project_state_latest.md`.
**Numerical work:** none.

**Authoritative inputs**
- `JMP_M07_deputy_closeout_and_identity_ruling_v1.md`
- `JMP_M07I_manuscript_identity_alignment_charter_v1.md`
- `JMP_M07I_stageB_independent_consistency_review_v1.md`
- `FR_P2a_empirical_inference_v2.md`
- `JMP_project_state_latest.md` (supplied at Stage D; the basis of the section-level map in §4)
- `JMP_core_packet_v1.md`, `JMP_abstract_clean_v1.md`, `JMP_extended_abstract_clean_v1.md`, `JMP_intro_skeleton_v1.md`

**Next authorised action:** Goal 1 Manager acceptance memo. The single authorized correction cycle is now spent; no further Stage-B round is available under the charter.

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
| §8 decomposition | Counterfactuals defined over spouse-specific region × education cells | Counterfactual construction deferred to the M08 welfare mission charter or a subsequently frozen welfare-design artifact; nested access/ability cut added; magnitude placeholder and the pre-LOC4 freeze prohibition added |
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

### 3.5 Stage D amendment (v2 → v3)

The tables above record the v1 → v2 redraft. Stage-B review §7 corrections 1–3 further amended the manuscript set to v3: the deputy staged-extension sentence is now used verbatim with no appended validation condition in the core packet, extended abstract and introduction skeleton; the qualifier "At the resolution and specification studied," is restored to the GSUR concentration statement in the abstract and the introduction's France-design paragraph; and every attribution of the counterfactual constructions to the M08 welfare-input handoff is removed in favour of deferral to the M08 welfare mission charter or a subsequently frozen welfare-design artifact. Each v3 file records the corrections it carries in its own front matter.

## 4. Section-level supersession map for `JMP_project_state_latest.md`

`JMP_project_state_latest.md` (dated 2 June 2026) was supplied at Stage D, so the class-level notice carried by addendum v1 is replaced here by a section-level map covering every section of that document. Scope is unchanged: supersession is asserted **only** for paper-facing empirical identity and for welfare sequencing. Authorities are abbreviated **D** = `JMP_M07_deputy_closeout_and_identity_ruling_v1.md`, **I** = `FR_P2a_empirical_inference_v2.md`, **ID** = the v3 identity set.

| Section | Status | Superseded by |
|---|---|---|
| §1.1 The question | Current | — three-way access/ability/preference cut already correct and carried into ID |
| §1.2 Supporting sub-questions | Current | — |
| §1.3 What the paper is not | Current | — decomposition-not-ranking and theory-paper boundary both carried into ID |
| §1.4 Empirical setting | **Superseded (identity)** | D §2.1 — pooled 2015–2017, three estimation groups and 12,445 households are no longer the paper-facing application; retained as build and certification history |
| §2.1 Money-metric equivalent income | Current | — |
| §2.2 The novel opportunity layer | Current | — |
| §2.3 The ex-ante stance | Current | — |
| §2.4 The welfare unit | **Superseded in part (identity)** | D §2.1–2.2 — the household-unit principle stands, but the couples-as-single-decider provisions describe no household in the current sample and are retained as design provisions for the chartered extension |
| §3.1 RURO factorisation | Current | — |
| §3.2 Preferences (utility block) | Current as certification history | I §5.3–5.4 for the paper-facing count — of the same 47 coordinates, ten are pinned in this sample (eight couples leisure, two survey-year) |
| §3.3 Opportunities (opportunity block) | Current | — the 6-parameter wage/ability and 23-parameter access sub-blocks are the basis of ID's access/ability language |
| §3.4 The occupation channel | Current | — occupation-in-access-only and the `loc4`≠`lindi` discipline both carried into ID |
| §3.5 The certified baseline estimate | Current as certification history | D §2.1 if read as the paper-facing application — the pooled 47-parameter specification is the certification anchor, not the current identity |
| §3.6 Identification and certification | Current | — |
| §3.7 Gender-split investigation | Current | — |
| §3.8 Inference and standard-error structure | **Superseded (paper-facing inference)** | I §5.1–5.4 — cluster-robust bootstrap on `idorighh`, the three-parameters-at-bounds enumeration, and the 21/29 and 9/18 significance counts are pooled-sample facts; the accepted paper-facing inference is the household-clustered sandwich QMLE covariance with 1,555 clusters, the `1555/1520` correction, two active-bound coordinates, a conditional 35-dimensional covariance and the `NA` convention |
| §3.9 Build facts material to the welfare layer | Current as build history | D §4.4 for scope — the 901-alternative couples grid lies outside the current application |
| §4 The household unit, in detail | **Superseded in part (identity)** | D §2.1–2.2 — the single-person sentence is current; the couples exposition is extension-facing, not a description of the present application |
| §5.1 Welfare object and family of measures | Current | — frozen welfare design, unaffected by the identity ruling |
| §5.2 Why a family rather than one measure | Current | — |
| §5.3 Integration scheme and proposal audit | Current | — |
| §5.4 The implementation contract | Current | — including its welfare-versus-decomposition scope boundary |
| §5.5 Stage One: the W³ core | Current as validation history | D §4.4 for scope — the 12,445-household production sample is not the M08 validation scope |
| §5.6 The effective-sample-size finding | **Superseded in part (sequencing)** | D §4.3–4.4 — the singles thin-ESS rows are the live blocker M08 must clear before any welfare number is promoted; the couples rows are deferred |
| §5.7 Redraw cross-check and reprice parity | **Superseded in part (sequencing)** | D §4.3–4.4 — the blocked reprice-parity gate remains binding, but the parity requirement is narrowed to the France 2016 P2a singles production path; the six year×mode obligation is dropped |
| §5.8 Validation-gate summary | **Superseded in part (sequencing)** | D §4.4 — same scope narrowing; gate statuses themselves stand |
| §6.1 The ability/opportunity/preference cut | Current | — the settled allocation (education and experience as ability; region, urbanisation and year as access; occupation via gendered offer parameters; age as preference; gender split across offer and taste) is the basis of ID's nesting. Its second paragraph's couples-compression and singles/couples-separability provisions describe no household in the current sample and are extension-facing |
| §6.2 Status and dependence | Current | — |
| §6.3 Deferred robustness specifications | **Superseded (sequencing)** | D §4.5 — the occupation-interacted wage return is no longer one deferred axis among several; the LOC4 four-density variant is the first mandatory robustness under binding Path B, and no preferred magnitude may be frozen before it |
| §7.1 Current position, in one paragraph | **Superseded (identity and status)** | D §1–§2.1 and I — the paragraph predates accepted Phase-5 inference and states the pooled specification as the project's position |
| §7.2 Immediate next step | **Superseded (sequencing)** | D §3–§4.4 — the authorized next step is M08 under its own charter; the reprice diagnosis is retained as a gating item inside M08, and the full 2015/2016/2017 × singles/couples parity re-run is dropped |
| §7.3 The fork the diagnosis determines | **Superseded in part (identity)** | D §2.2, §2.4 — the "couples-certified with singles carrying a coverage caveat" branch is inadmissible; a structural parity failure is instead a deputy return gate |
| §7.4 The sequence beyond the parity gate | **Superseded (sequencing)** | D §4 — replaced by the accepted order: M08 as point-estimate prototype with mandatory four-scenario sensitivity, LOC4 as first robustness, bootstrap only after the preferred specification, no delta-method substitute |
| §8 Methodological principles on record | Current | — |

**Explicitly not superseded anywhere in this map:** the 47-coordinate parameter vector and its pinning structure; the accepted Phase-3, Phase-4 and Phase-5 results; the frozen welfare-object design and implementation contract; the restricted-custody rules for score and household-level welfare artifacts; the prohibition on committing raw microdata or household-level welfare vectors to the paper repository; and the Tier-2 halt triggers.

## 5. Input status recorded for the Goal 1 Manager

Four documents named as binding inputs by the M07I charter were not supplied at Stage A: `FR_P2a_inference_appendix_note_v2.md`; `JMP_M07_goal_manager_acceptance_v1.md`; `JMP_M08_welfare_input_handoff_v1.md`; and `JMP_project_state_latest.md`. Stage B adjudicated the first two deferrals as holding and the third as not holding; `JMP_project_state_latest.md` was supplied at Stage D. Current status:

- No welfare-design internal is asserted anywhere in the v3 documents beyond what §5.5 of `FR_P2a_empirical_inference_v2.md` establishes. The construction of the opportunity-equalization and preference-neutralization counterfactuals is **not** attributed to the M08 welfare-input handoff, which does not contain it; it is deferred to the M08 welfare mission charter or to a subsequently frozen welfare-design artifact.
- No appendix content is cited.
- §4 above now provides a section-level map against the actual project-state document, closing the charter's exact-supersession requirement. No line-level mapping is asserted beyond section granularity, which is sufficient because the stale content in each affected section is identified by substance in the map's third column.
- **Verification status of the map's source.** `JMP_project_state_latest.md` is not an M07I output and is not carried in the M07I artifact set; the map in §4 was constructed against it as supplied to the correction cycle. The acceptance step should therefore spot-check §4's section list and titles against the live project-state file before the addendum is allowed to control project-state interpretation. If any section has been added, retitled or renumbered in that file since the correction cycle, the map requires a bounded refresh rather than reliance on this version.

## 6. Unresolved decisions

1. **Title divergence.** The identity documents carry *Opportunity Constraints as a Driver of Welfare Inequality: A Latent-Jobs Structural Decomposition Approach*; programme governance headers carry *Unequal Job Opportunities and Well-Being Inequality: A Latent-Jobs Structural Decomposition*. The charter forbids a title decision in this mission, so the provisional identity-document title is retained unchanged and the divergence is escalated to the Goal 1 Manager.
2. **Headline inequality index.** The accepted inference section contemplates a headline index that may differ from the Gini. The v2 documents keep the Gini as the baseline index and note the possibility; resolution belongs to M08.
3. **Project-state supersession.** Closed at Stage D. §4 now carries a section-level map built against the supplied `JMP_project_state_latest.md`; no manager waiver is required.
4. **Positioning memo.** `JMP_literature_positioning_memo_v2.md` describes the France 2016 couples prototype as the empirical anchor in **§§1, 3, 4, 5, 7 and 8** — §4 closes by naming France 2016 couples as the concrete baseline, which the v1 inventory omitted. The memo is not among the authorised M07I outputs and has therefore **not** been revised. It is **not current for empirical identity** and **must not circulate with the v3 identity set unless revised**; until a follow-on bounded task aligns it, it is quarantined as stale project history. The Goal 1 Manager acceptance memo should record this exclusion.
