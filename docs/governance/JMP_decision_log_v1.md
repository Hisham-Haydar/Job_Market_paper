# JMP Decision Log v1

**Date opened:** 2026-07-30  
**Rule:** Append-only. Do not silently rewrite prior decisions. Superseding entries must cite the earlier decision ID.

## A. Accepted decisions

### D-001 — Two-programme structure

The project has two connected goals:

1. empirical JMP;
2. public `dclaborsupply` package.

The application uses the package, but the package remains generic.

### D-002 — Top-level management

The ChatGPT JMP project is the programme manager and canonical-state gatekeeper. Claude projects are subordinate specialised workstreams.

### D-003 — Active empirical prototype

The active prototype is France 2016 singles P2a region-live.

### D-004 — Formal reference baseline

The pooled 47-parameter specification with negative log-likelihood `238504.6360973987` remains the formal certified reference baseline.

### D-005 — Phase-3 acceptance

The P2a Phase-3 production estimate is accepted at negative log-likelihood `19053.46553160093`.

Accepted bundle SHA-256:

`2cf237648743f59bd742b12feceaea67c5fd377b26faf4fb6fad6f452f86864b`.

### D-006 — Phase-4 acceptance

The P2a Phase-4 curvature and regional-identification result is accepted.

Accepted bundle SHA-256:

`5484886985aecd28e511719e42f45b85ad0e1755d1f951dbd13a79281d9665f3`.

The free Hessian is full rank and positive definite. The ten-dimensional regional design and conditional Schur complement are full rank and positive definite.

### D-007 — Next mission

The next mission is household-clustered inference. Design is authorized; implementation and real execution are not authorized.

### D-008 — Cluster identity

The inferential cluster is the household `idhh`. The required cluster count is 1,555. Row counts or alternative counts are not cluster counts.

### D-009 — Synthetic recovery remains mandatory

Real-data Hessian and inference evidence do not replace synthetic recovery.

### D-010 — Welfare and decomposition status

Welfare and decomposition outputs remain non-reportable until the relevant missions and recovery gates pass.

### D-011 — Headline decomposition

The main paper should first distinguish:

1. opportunity environment;
2. preferences.

A supporting decomposition may split opportunity into access and wage/ability channels.

### D-012 — Normative terminology

Use opportunity-related and preference-related inequality. Preferences are not automatically responsibility.

### D-013 — Theory-paper separation

The Maniquet theory paper remains strictly separate from the JMP.

### D-014 — Repository separation

`MNL` is the France application. `dclaborsupply-monorepo` is the generic package. France-specific logic must not be upstreamed as generic package logic.

### D-015 — End-to-end notebook role

The notebook will be the transparent application narrative and will load accepted artifacts by default. Production scripts and immutable bundles remain certification authorities.

## B. Provisional choices

### P-001 — Main welfare measure

W³ is the preferred first welfare-measure implementation, subject to a dedicated welfare-contract mission.

### P-002 — Welfare robustness

Use one primary alternative money-metric measure before expanding to the full W¹–W⁶ family.

### P-003 — Preference-absorption estimand

The preferred level estimand is:

\[
C_R^{\mathrm{standard}}-C_R^{\mathrm{RURO}}.
\]

The normalized rate remains provisional until comparability is established.

### P-004 — Public package timing

A public package release should follow successful use of the public API by the France application.

## C. Rejected paths

### R-001 — Country ranking as core JMP

Rejected. Country comparisons may be later extensions but are not the paper's central contribution.

### R-002 — Broad optimal-tax expansion now

Rejected unless directly required by the core decomposition.

### R-003 — All welfare measures initially

Rejected. Build and certify one main measure and one robustness measure first.

### R-004 — Couples and singles simultaneously

Rejected for the first empirical prototype. Singles remain the baseline until the pipeline is complete.

### R-005 — Treating preferences as responsibility by definition

Rejected.

### R-006 — Treating experimental welfare outputs as accepted results

Rejected.

## D. Deferred extensions

### X-001 — Couples

Deferred until the singles pipeline is certified.

### X-002 — Pooled years and alternative years

Deferred until the single-year baseline result is credible.

### X-003 — Continuous regional labour-market conditions

Deferred until the magnitude and stability of the current opportunity component are known.

### X-004 — Occupation-specific wage densities

Deferred pending a later specification mission.

### X-005 — Decomposition bootstrap

Deferred until the baseline decomposition is implemented and validated.

### X-006 — Software paper

Deferred until the package has a stable public release.
