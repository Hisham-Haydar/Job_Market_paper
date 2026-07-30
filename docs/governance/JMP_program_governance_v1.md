# JMP Programme Governance v1

**Status:** Active governance  
**Date:** 2026-07-30  
**Programme owner:** Hisham Haydar  
**Top-level manager:** ChatGPT JMP project

## 1. Purpose

This document governs two connected but distinct programmes:

1. **Goal 1 — Empirical JMP:** produce a publishable economics Job Market Paper on how unequal job opportunities affect money-metric well-being inequality and how opportunity heterogeneity is misattributed to preferences when opportunities are omitted from structural labour-supply estimation.
2. **Goal 2 — Public package:** produce a country-, year-, dataset-, dimension-, and specification-agnostic `dclaborsupply` Python package for estimating preferences and opportunity mechanisms in discrete-choice labour-supply models.

The empirical application uses the package. The package must not become France-specific or JMP-specific.

## 2. Research identity

The main paper studies:

> How much money-metric well-being inequality is attributable to unequal job opportunities, and how much opportunity-related inequality is absorbed into estimated preferences when opportunities are not modeled explicitly?

The empirical sequence is:

1. estimate preferences and opportunities jointly in a RURO / latent-jobs model;
2. estimate a comparison model that does not model heterogeneous opportunities explicitly;
3. compute money-metric well-being consistently with each model;
4. decompose well-being inequality into opportunity-related and preference-related components;
5. quantify the preference-absorption effect;
6. assess sensitivity to a limited number of defensible welfare measures.

The empirical labels are **opportunity-related inequality**, **preference-related inequality**, and **compensation-relevant inequality under the stated normative criterion**. Preferences are not automatically synonymous with responsibility.

## 3. Strict project boundary

The separate theory paper with François Maniquet on jobs and well-being is outside this programme. It may inform terminology or welfare reasoning, but the JMP must remain a distinct empirical or empirically grounded paper. Theory-paper files, proofs, and governance must remain separate.

## 4. Decision hierarchy

The operating hierarchy is:

1. **Hisham:** principal investigator and final substantive decision-maker.
2. **ChatGPT JMP project:** programme director, research strategist, mission author, canonical-state manager, and final gatekeeper.
3. **Claude Project 1:** specialised JMP paper and empirical-design workstream.
4. **Claude Project 2:** specialised `dclaborsupply` package workstream.
5. **Claude Project 3:** specialised welfare and decomposition workstream.
6. **Claude Code:** local implementation, repository inspection, tests, execution, and file management.
7. **Codex:** independent read-only code and evidence review.
8. **GitHub Copilot:** local autocomplete and small coding assistance only.
9. **Deep Research:** targeted literature and methodological verification only.

No subordinate tool may broaden a mission, change a frozen decision, or promote an experimental result without top-level acceptance.

## 5. Source-of-truth hierarchy

When sources conflict, use this order:

1. committed manager-acceptance memo;
2. latest `JMP_canonical_state_vN.md`;
3. latest `JMP_decision_log_vN.md`;
4. current approved mission charter;
5. committed repository source and immutable result artifacts;
6. specialised project memory;
7. chat recollection.

Claude project memory is background context, not governance.

## 6. Repository responsibilities

### `Job_Market_paper`

Authority for:

- research questions and contribution;
- literature positioning;
- governance and design memos;
- welfare and decomposition contracts;
- manuscript, tables, and paper-facing figures;
- decision log and canonical state.

### `MNL`

Authority for:

- France-specific data preparation;
- EUROMOD pricing;
- latent-job pool construction;
- France application specifications;
- certified estimation, inference, welfare, and decomposition executions;
- end-to-end France notebook.

### `dclaborsupply-monorepo`

Authority for:

- generic grouped discrete-choice contracts;
- generic utility and opportunity components;
- specification parsing and parameter mapping;
- likelihood, score, gradient, Hessian, estimation, and inference APIs;
- simulation and recovery tools;
- package documentation and release.

A France-discovered correction may move upstream only when it is generic, tested generically, documented, and does not encode France-specific assumptions.

## 7. Mission system

Every substantial work unit receives a mission ID:

- `JMP-Mxx` for the empirical paper;
- `PKG-Mxx` for the public package.

Each mission has five stages:

1. **Programme decision:** ChatGPT creates the mission charter.
2. **Workstream planning:** the relevant Claude project creates a bounded task plan.
3. **Execution:** the designated tool produces the required artifact or implementation.
4. **Independent review:** Codex or another independent reviewer evaluates the exact state.
5. **Acceptance:** ChatGPT accepts, narrows, rejects, or redesigns the mission and updates canonical records.

The implementer may not approve its own work.

## 8. Required mission controls

Every mission charter must specify:

- programme goal;
- connection to the paper or package;
- canonical starting state;
- exact research question;
- scope and non-scope;
- authoritative files;
- frozen decisions;
- decisions to be made;
- pre-registered gates;
- required artifacts;
- tool allocation;
- halt conditions;
- commit policy;
- return packet;
- next action after acceptance.

Open-ended instructions such as “finish the decomposition” are prohibited.

## 9. Acceptance and evidence policy

A result becomes usable for the JMP only after:

1. the design is approved;
2. implementation matches the approved design;
3. relevant tests and diagnostics pass;
4. an independent review approves the exact state;
5. the result bundle is immutable and provenance-bound;
6. a manager-acceptance memo records permitted and prohibited claims.

A technically successful run is not automatically a publishable result.

## 10. Commit policy

- Design memos are committed after manager acceptance.
- Implementation is committed only after independent review of the exact state.
- Successful result bundles are committed only after manager audit.
- Failed or stopped attempts may be retained as evidence but must never be presented as accepted results.
- No unrelated files may be silently staged to obtain a clean worktree.

## 11. Current programme priority

The active empirical prototype is France 2016 singles P2a region-live.

Accepted:

- Phase 3 production estimation;
- Phase 4 curvature and regional identification.

Next:

- `JMP-M05`: household-clustered inference design and certification.

Still blocked:

- Phase-5 implementation and execution until design decisions are frozen;
- synthetic-recovery claims;
- welfare and decomposition reporting;
- notebook inference, post-estimation, and welfare execution.

## 12. Strategic stopping rule

Engineering hardening is warranted only when it can affect:

- numerical validity;
- identification;
- data or parameter provenance;
- reproducibility;
- transaction integrity;
- scientific interpretation.

Once these are secured, the programme must move toward the central empirical estimands, welfare decomposition, and manuscript production.
