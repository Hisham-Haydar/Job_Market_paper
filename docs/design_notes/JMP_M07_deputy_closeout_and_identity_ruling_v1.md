# JMP-M07 Deputy Closeout and Empirical-Identity Ruling v1

**Programme:** Goal 1 — Empirical JMP  
**Decision-maker:** Deputy Programme Director  
**Date:** 2026-08-05  
**Status:** Binding  
**M07 disposition:** Accepted and closed  
**Next primary mission:** JMP-M08  
**Parallel bounded task:** JMP-M07I

## 1. Deputy acceptance of JMP-M07

The Goal 1 Manager's acceptance of JMP-M07 is ratified.

The accepted manuscript inference backbone is:

- `manuscript/sections/FR_P2a_empirical_inference_v2.md`;
- `manuscript/appendices/FR_P2a_inference_appendix_note_v2.md`.

The accepted support packet is:

- `docs/results/FR_P2a_phase5_inference_results_memo_v1.md`;
- `docs/results/FR_P2a_phase5_parameter_reporting_map_v1.csv`;
- `docs/missions/JMP_M07_stageC_independent_economics_review_v1.md`;
- `docs/missions/JMP_M07_goal_manager_acceptance_v1.md`;
- `docs/missions/JMP_M08_welfare_input_handoff_v1.md`;
- `docs/missions/JMP_M07_stageB_author_cover_note_v1.md`.

No further M07 drafting, claim audit, Phase-5 computation, or software-certification work is authorized. The v1 manuscript drafts remain immutable history; the v2 drafts control.

Before successor work writes to `Job_Market_paper`, the Goal 1 Manager shall perform one documentation-only M07 closeout commit after verifying the final file set and hashes. This is routine closure and does not return to the deputy unless the repository state conflicts with the accepted packet.

## 2. Empirical-identity ruling

### 2.1 Binding paper-facing identity

The paper's current and only accepted empirical application is:

> **France 2016 single-adult households, P2a region-live specification, 1,555 households.**

This is the application named in the accepted estimation, inference, and frozen M08 handoff. It is therefore the empirical identity that must control the title page, abstract, extended abstract, introduction, contribution statement, data section, results roadmap, and welfare mission.

### 2.2 Treatment of couples and pooled-year work

Couples and pooled 2015–2017 work are not co-primary empirical baselines for the present manuscript.

They may be described only as:

- historical model-development or certification anchors, where technically necessary;
- later external-validity or scale extensions;
- future work conditional on successful validation of the singles pipeline.

They may not appear in the abstract or introduction as delivered results, promised coequal applications, or the source of current paper-facing estimates. The phrase “singles prototype is obsolete,” and any equivalent instruction, is superseded.

### 2.3 Staged framing

The paper may use one concise staged sentence:

> The empirical analysis first establishes the complete estimation–welfare–decomposition pipeline for France 2016 single-adult households; extension to couples and pooled years is subsequent work.

This sentence is subordinate framing, not the paper's main contribution claim. The contribution remains the consistent structural treatment of access, ability, and preferences across estimation, welfare measurement, and decomposition.

### 2.4 Why this ruling is binding

A manuscript should advertise the application for which it has accepted evidence. Retaining a couples-centred identity would create a direct contradiction between the abstract and the paper's accepted results, obscure the scientific value of the singles proof of concept, and pressure the programme to produce couples results before the singles welfare pipeline is validated.

## 3. Sequencing ruling

Two successor actions are authorized.

### Primary: JMP-M08

`JMP-M08 — France 2016 Singles Welfare Integration and Baseline Decomposition Prototype`

M08 begins immediately and is the programme's central path.

### Parallel bounded task: JMP-M07I

`JMP-M07I — Manuscript Identity Alignment`

M07I updates the stale identity documents to the ruling above. It must not delay M08 and must close before the next abstract or introduction is circulated.

## 4. Welfare-stage sequencing decisions

1. M08 is a **point-estimate prototype and functional-sensitivity mission**, not the final welfare-inference freeze.
2. The accepted W-4/S-10 four-scenario sensitivity is mandatory in M08.
3. The existing welfare-integration blocker for singles must be resolved before any welfare number is promoted:
   - thin effective sample size on the 101-alternative singles grids;
   - blocked redraw cross-check;
   - failed EUROMOD reprice parity on existing nodes.
4. The old pooled/couples requirement to validate the full 2015/2016/2017 × singles/couples grid is superseded for M08. M08 validates the exact France 2016 P2a singles production path only. Other cells are deferred.
5. LOC4 Path B remains binding:
   - M08 uses the certified baseline;
   - LOC4 is the first mandatory robustness after M08;
   - no preferred quantitative decomposition magnitude is frozen before LOC4.
6. Bootstrap uncertainty for final headline welfare and decomposition estimates is sequenced after the preferred specification is resolved through LOC4. M08 does not use asymptotic delta-method standard errors as a substitute.
7. A direct inferential claim on a W-4 coordinate, a material S-10 loading, or an unconditional active-set claim triggers the existing Tier-2 halt.

## 5. Repository authority

- `Job_Market_paper`: governance, design, paper-facing aggregate results, manuscript text.
- `MNL`: France-specific welfare execution, restricted household-level welfare artifacts, application code, manifests, and validation evidence.
- `dclaborsupply-monorepo`: read-only during M08 by default. A generic package-source change requires a separate PKG mission or explicit deputy amendment.

No raw microdata or household-level welfare vector may be committed to the public paper repository. Paper-facing outputs must be aggregate or disclosure-reviewed.

## 6. Next return gate

Return to the deputy only with:

- the completed M08 acceptance packet;
- a material S-10 Tier-2 trigger;
- a structural reprice-parity failure that prevents singles welfare certification;
- a required generic package change;
- a conflict between the frozen welfare design and the accepted P2a application;
- or a proposed change to the LOC4 or empirical-identity rulings.
