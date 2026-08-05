# MISSION JMP-M07 — Phase-5 Inference Results Integration

**Programme:** Goal 1 — Empirical JMP  
**Manager:** Goal 1 Manager — Empirical JMP  
**Mission type:** Economics interpretation, results writing, and welfare-stage handoff  
**Numerical estimation:** Not authorized  
**New model execution:** Not authorized  
**Status:** Authorized

## 1. Mission objective

Convert the accepted France 2016 singles P2a Phase-5 inference artifacts into:

1. a paper-ready empirical inference section;
2. a disciplined interpretation of the regional/access results;
3. a complete reporting treatment for active bounds, pins, and W-4;
4. a frozen handoff specification for the first welfare/decomposition mission.

This mission is about economic interpretation and writing. It must not reopen
Phase 3, Phase 4, Phase 5, or software certification.

## 2. Canonical evidence

Use only the accepted Phase-5 result:

- MNL evidence commit:
  `905348c53b31049db854c16016fa064517c19892`;
- MNL D11/closeout HEAD:
  `520441a653f04196bf1e92e3658a478b4feb3718`;
- Job_Market_paper checkpoint:
  `1e54bcd7fe6eb5d202db97c204a655d385181442`;
- nested dclaborsupply:
  `27756a06ea189339aa82915ed2124628afed20eb`;
- accepted attempt:
  `20260803T133122Z_14772_817e8deb503d408fa73b8b53d598c0db_dryrun_PHASE_5_DRY_RUN_COMPLETE`;
- Phase-5 bundle:
  `d08947ce015f2b2a922c6d5591ebe600c53016922b3a1158d90f125cd2195232`.

No statistic may be recomputed from raw microdata. Mechanical table formatting
from accepted aggregate artifacts is permitted.

## 3. Main empirical message

The results section must distinguish three claims.

### Claim 1 — Confirmatory access-block rejection

Report:

- H0-A, 10 df:
  robust Wald `37.45`, robust p-value `4.7e-05`;
- the regional/urbanisation/GSUR access block is jointly relevant.

Do not describe H0-A as a test of the whole opportunity mechanism.

### Claim 2 — Concentration in GSUR

Report:

- H0-G:
  robust Wald `29.21`, robust p-value `6.5e-08`;
- `beta_E_gsur = -1.105`;
- robust 95% interval `[-1.51, -0.70]`;
- H0-B NUTS-1 dummies:
  robust p-value `0.594`;
- H0-C urbanisation terms:
  robust p-value `0.847`.

The interpretation is:

> At the resolution and specification studied, measured access heterogeneity is
> concentrated in one GSUR dimension rather than diffuse across broad NUTS-1
> geography or the two urbanisation indicators.

Do not translate `gsur` into a substantive label not supported by the data
documentation.

### Claim 3 — Variance-estimator robustness

Model-based and robust inference agree on all four H0-A/B/C/G rejection
decisions.

State this as stability of the test verdicts, not proof of correct
specification.

## 4. Required methods reporting

The methods paragraph must state:

- 1,555 household contributions/clusters;
- conditional 35-dimensional inference;
- two active-bound free parameters excluded from ordinary symmetric inference;
- literal `NA` for active-bound and pinned coordinates;
- accepted Hessian bread;
- household-score sandwich meat;
- correction scalar `1555/1520`;
- model-based and robust covariance both reported;
- regional restrictions selected by parameter name;
- no row-level score persistence.

Keep implementation detail proportionate. The paper should not narrate the
M05B/M05C software-certification history.

## 5. Parameter-table reporting

Produce a 47-row paper table or table-ready source with:

- parameter name;
- economic block;
- estimate;
- model-based standard error;
- robust standard error;
- robust confidence interval;
- status: interior / active bound / pinned;
- inferential fields as literal `NA` where required;
- concise economic label.

Separate panels:

1. preferences;
2. employment/hours access;
3. regional/access;
4. occupation access;
5. wage density.

Do not rank parameters by statistical significance.

## 6. W-4 and S-10 disclosure

Carry the accepted Tier-1 warning for:

- `beta_l0_sm`;
- `beta_w_pexp2`.

Required text:

> Robust symmetric intervals for `beta_l0_sm` and `beta_w_pexp2` approach the
> relevant parameter boundary. They are reported as local diagnostics and
> should not be interpreted as unrestricted evidence beyond the admissible
> parameter region. The welfare analysis therefore includes a pre-registered
> admissible local sensitivity for these coordinates.

Do not reopen estimation and do not trigger Tier 2 during M07.

Use the separate binding specification:

`JMP_M07_S10_tier1_welfare_sensitivity_specification_v1.md`.

## 7. LOC4 ruling

Use:

`JMP_LOC4_pathB_ruling_v1.md`.

The paper-facing baseline remains the certified specification. The LOC4
four-density variant is the first mandatory wage-density robustness axis, but it
does not block the first baseline welfare prototype.

M07 must state this sequencing clearly without presenting unestimated LOC4
results.

## 8. Required outputs

Create in `Job_Market_paper`:

1. `docs/results/FR_P2a_phase5_inference_results_memo_v1.md`
2. `docs/results/FR_P2a_phase5_parameter_reporting_map_v1.csv`
3. `manuscript/sections/FR_P2a_empirical_inference_v1.md`
4. `manuscript/appendices/FR_P2a_inference_appendix_note_v1.md`
5. `docs/design_notes/JMP_M08_welfare_input_handoff_v1.md`
6. `docs/missions/JMP_M07_goal_manager_acceptance_v1.md`

The parameter reporting CSV is a presentation map derived from accepted
artifacts. It is not a new statistical artifact.

## 9. Work stages

### Stage A — Accepted-result extraction

Tool:

- Claude Code;
- Sonnet;
- thinking on;
- medium effort;
- read-only access to MNL and dclaborsupply;
- write access only to the six authorized Job_Market_paper outputs.

Produce an exact source-to-table inventory. No raw-data access and no numerical
re-estimation.

### Stage B — Economics drafting

Tool:

- separate Claude Project chat;
- Opus;
- thinking on;
- high effort.

Inputs:

- accepted-result extraction;
- this charter;
- the Phase-5 strategic assessment;
- canonical JMP question and contribution documents;
- LOC4 and S-10 rulings.

Draft the results section and appendix note.

### Stage C — Independent economics review

Tool:

- separate ChatGPT Thinking chat or separate Claude Opus chat;
- high reasoning;
- no repository writes.

Review only:

- claim-to-evidence alignment;
- interpretation of GSUR concentration;
- distinction between regional access and the whole opportunity mechanism;
- conditional-active-set wording;
- W-4 disclosure;
- absence of causal or responsibility overclaims.

### Stage D — Goal-manager acceptance

The Goal 1 Manager may authorize one narrow writing correction. It then creates
the acceptance memo and the M08 handoff.

## 10. Acceptance criteria

M07 passes only if:

- every reported number maps to an accepted artifact;
- H0-A is described as confirmatory for the named ten-parameter block;
- GSUR concentration is not generalized beyond the measured specification;
- null NUTS-1 and urbanisation results are reported;
- active-bound, pin, and W-4 caveats are visible;
- no new estimation or welfare result is implied;
- LOC4 Path B and the sensitivity handoff are recorded;
- the paper-facing prose is concise enough for a JMP results section.

## 11. Non-scope

Do not:

- rerun inference;
- re-estimate the model;
- run welfare or decomposition;
- implement LOC4;
- add industry `lindi`;
- add external regional covariates;
- modify dclaborsupply;
- reopen software certification;
- interpret preference parameters as responsibility;
- describe statistical rejection as causal identification.

## 12. Return gate

Return to the deputy programme director only with:

- M07 acceptance memo;
- final results memo;
- final manuscript section;
- independent economics-review verdict;
- M08 welfare-input handoff;
- any strategic dispute over the LOC4 or S-10 rulings.

Routine drafting and corrections remain with the Goal 1 Manager.
