# JMP Canonical State v1

**As of:** 2026-07-30  
**Status:** Authoritative until superseded  
**MNL HEAD:** `982c52217031158c4a2368709d4a6b211ebcde76`  
**Nested `dclaborsupply` HEAD and MNL gitlink:** `27756a06ea189339aa82915ed2124628afed20eb`

## 1. Two programme goals

### Goal 1 — Empirical JMP

Produce a publishable empirical paper estimating how unequal job opportunities affect money-metric well-being inequality and how omission of heterogeneous opportunities causes opportunity disadvantage to be absorbed into estimated preferences.

### Goal 2 — Public package

Produce a public, country-, year-, dataset-, dimension-, and specification-agnostic `dclaborsupply` package that estimates preferences and opportunity mechanisms in discrete-choice labour-supply models.

## 2. Main paper question

> How much money-metric well-being inequality is attributable to unequal job opportunities, and how much opportunity-related inequality is misclassified as preference heterogeneity when constrained opportunities are omitted?

Supporting questions:

1. How much does a standard common-opportunity model overstate preference heterogeneity?
2. How should money-metric well-being be measured when feasible job sets differ?
3. What share of well-being inequality is opportunity-related under the stated compensation principle?
4. How sensitive is the decomposition to a limited set of defensible money-metric measures?

## 3. Active empirical prototype

- Country: France
- Year: 2016
- Population: singles
- Application: P2a region-live
- Alternatives per household: 101
- Household clusters: 1,555
- Total parameters: 47
- Free parameters: 37
- Fixed pins: 10
- Active-bound free parameters:
  - `beta_l_age2_sm`
  - `beta_l_age2_sf`

## 4. Formal reference baseline

The pooled 47-parameter specification remains the formal certified reference baseline:

- specification: `joint_pooled_v1_bll0_tlmpin`;
- accepted pooled negative log-likelihood: `238504.6360973987`.

It is a reference and regression anchor. It is not automatically the active paper application.

## 5. Accepted Phase-3 state

- Status: **ACCEPTED**
- Accepted negative log-likelihood: `19053.46553160093`
- Accepted Phase-3 bundle SHA-256:  
  `2cf237648743f59bd742b12feceaea67c5fd377b26faf4fb6fad6f452f86864b`
- Optimizer success: yes
- Ten pins: bitwise unchanged
- Post-estimation input recheck: passed
- Current accepted estimate is the canonical P2a parameter vector.

## 6. Accepted Phase-4 state

- Status: **ACCEPTED**
- Accepted Phase-4 bundle SHA-256:  
  `5484886985aecd28e511719e42f45b85ad0e1755d1f951dbd13a79281d9665f3`
- Hessian: exact 37×37 negLL Hessian
- Hessian rank: 37
- Minimum eigenvalue: `0.1037326963880782`
- Condition number: `405353.94719781954`
- Condition classification: clean
- Regional design source: `production_likelihood_loader_arrays`
- Regional design shape: 1,555×10
- Regional design rank: 10
- Raw regional subblock: positive definite
- Raw regional minimum eigenvalue: `3.3787399166319405`
- Schur-complement rank: 10
- Schur-complement minimum eigenvalue: `2.255741652065068`
- Regional loading warning: false
- Post-evaluation input recheck: passed

Interpretation: the 37 free parameters are locally identified at the accepted estimate, and the ten-parameter regional/access block remains locally identified conditional on the other free parameters.

## 7. Current authorization

Authorized:

- Phase-5 design and manager review.

Not authorized:

- Phase-5 implementation;
- Phase-5 real execution;
- synthetic-recovery claims;
- welfare or decomposition reporting;
- notebook inference, post-estimation, or welfare execution;
- promotion of the P2a application over the formal pooled reference baseline.

## 8. Required next mission

`JMP-M05 — Household-clustered inference`

The design must freeze:

1. finite-sample correction;
2. treatment of the two active-bound parameters;
3. treatment of the ten fixed pins;
4. household-score construction;
5. regional-block inference;
6. whether the complete household-score matrix is committed or stored as a hashed binary artifact.

## 9. Later required missions

- `JMP-M06`: synthetic recovery;
- `JMP-M07`: comparison model and preference-absorption estimand;
- `JMP-M08`: welfare-measure contract;
- `JMP-M09`: decomposition contract;
- `JMP-M10`: end-to-end notebook and certified results;
- `JMP-M11`: manuscript production.

## 10. Welfare and decomposition status

Existing welfare or decomposition outputs are experimental unless a manager-acceptance memo explicitly certifies them for this P2a state.

The current main decomposition should initially distinguish:

1. opportunity environment;
2. preferences.

A nested supporting decomposition may later split opportunity into access and wage/ability channels.

Preferences must not automatically be labelled responsibility.

## 11. Package/application separation

`MNL` is the France application. `dclaborsupply-monorepo` is the generic engine.

No France-specific cleaning, EUROMOD logic, country variables, or JMP welfare operators may be hard-coded into the public package.

## 12. Theory-paper boundary

The separate Maniquet theory paper remains outside the JMP. It is neither the empirical baseline nor a required implementation target.

## 13. Stale-context warnings

The following statements in older project memories are not canonical unless revalidated:

- pooled 2015–2017 as the active paper application;
- LOC4 four-density redesign as the immediate next task;
- welfare and `V_i` as production-ready;
- decomposition implementation as currently authorized;
- prior M1-clean governance as applicable to the current P2a state.
