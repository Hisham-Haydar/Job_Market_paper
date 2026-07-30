# JMP Roadmap v1

**Date:** 2026-07-30  
**Status:** Active strategic roadmap

## 1. Programme sequence

The programme follows:

> topic and estimand lock → certified estimation → certified inference → synthetic recovery → comparison-model lock → welfare contract → decomposition contract → end-to-end results → manuscript

Estimation and curvature are complete for the active France 2016 singles P2a prototype. The next mission is inference.

## 2. Goal 1 — Empirical JMP missions

### JMP-M05 — Household-clustered inference

**Purpose:** certify uncertainty quantification for the accepted estimate.

Substages:

1. inference design lock;
2. implementation;
3. independent code review;
4. one real execution;
5. manager acceptance.

Required decisions:

- finite-sample correction;
- active-bound treatment;
- fixed-pin reporting;
- household score artifact;
- regional joint testing.

### JMP-M06 — Synthetic recovery

**Purpose:** show that the decomposition-relevant parameters and opportunity/preference allocation can be recovered under known data-generating values.

Required targets:

- preference parameters;
- access/opportunity parameters;
- wage/ability parameters used later;
- model discrimination between heterogeneous and common opportunities;
- recovery of the opportunity-versus-preference allocation.

Real-data curvature and standard errors do not replace this mission.

### JMP-M07 — Comparison model and absorption-estimand lock

**Purpose:** define and estimate the model that omits heterogeneous opportunities and freeze the preference-absorption estimand.

Primary estimand:

\[
C_R^{\mathrm{standard}}-C_R^{\mathrm{RURO}}.
\]

A normalized absorption rate may be secondary if the welfare objects are comparable.

### JMP-M08 — Welfare-measure contract

**Purpose:** select one main money-metric well-being measure and one primary robustness measure.

Recommended build order:

1. validate W³ for the active empirical model;
2. select one alternative measure;
3. defer the full W¹–W⁶ family.

### JMP-M09 — Decomposition contract

**Purpose:** freeze the empirical operators and inequality decomposition.

Primary headline factors:

1. opportunity environment;
2. preferences.

Supporting opportunity split:

- access-only;
- access plus wage/ability.

The mission must freeze:

- counterfactual operators;
- reference distributions;
- Shapley/Shorrocks protocol;
- inequality index;
- treatment of probabilistic opportunity sets;
- uncertainty propagation.

### JMP-M10 — End-to-end notebook and certified results

**Purpose:** produce a transparent France 2016 singles notebook that loads certified artifacts by default and presents:

cleaning → pricing → latent jobs → estimation → inference → welfare → decomposition → robustness.

The notebook is an exposition and reproducibility layer, not the certification authority.

### JMP-M11 — Manuscript production

**Purpose:** write the JMP around certified results.

Required outputs:

- contribution lock;
- abstract;
- introduction;
- model and identification;
- data and estimation;
- welfare and decomposition;
- results;
- robustness;
- limitations;
- appendices;
- job-market presentation materials.

## 3. Goal 2 — Package missions

### PKG-M01 — Package canonical contract

Freeze public scope, supported configurations, API stability policy, and genericity tests.

### PKG-M02 — Generic inference API

Expose household scores, model covariance, cluster-robust covariance, parameter mapping, and diagnostics without France-specific assumptions.

This mission should follow approval of the JMP Phase-5 design so the generic API supports the accepted statistical contract.

### PKG-M03 — Generic synthetic-recovery framework

Provide reusable simulation and recovery utilities across optional model dimensions.

### PKG-M04 — Public release preparation

Complete:

- API documentation;
- examples;
- installation;
- continuous integration;
- packaging metadata;
- licensing;
- versioning;
- release notes;
- reproducible examples.

### PKG-M05 — Public release

Publish the package after the France application successfully uses the public API.

A software paper is optional and later.

## 4. Central now

1. complete `JMP-M05` design;
2. freeze the three manager decisions;
3. implement and certify inference;
4. move directly to synthetic recovery.

## 5. Useful later

- couples;
- pooled years;
- alternative years;
- continuous regional labour-market indicators;
- occupation-specific wage densities;
- alternative opportunity definitions;
- bootstrap decomposition uncertainty;
- software paper.

## 6. Not worth doing now

- country rankings;
- broad beyond-GDP comparisons;
- optimal-tax expansion unrelated to the core estimand;
- all household types simultaneously;
- all welfare measures before one baseline works;
- another broad literature search;
- engineering hardening with no effect on numerical validity, provenance, or reproducibility.
