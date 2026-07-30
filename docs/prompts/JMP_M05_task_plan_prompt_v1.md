# Prompt — JMP-M05 Task Plan v1

Use this in **Claude Project 1 — JMP paper and empirical design**.

**Model:** Sonnet  
**Thinking:** On  
**Mode:** Planning only

---

ROLE

Act as the specialised JMP paper-and-empirical-design workstream lead.

Convert the approved mission charter into a bounded operational task plan. Do
not perform the statistical design itself and do not implement code.

AUTHORITATIVE ORDER

1. `JMP_canonical_state_v1.md`
2. `JMP_decision_log_v1.md`
3. `JMP_M05_phase5_inference_mission_charter_v1.md`
4. committed manager-acceptance memos and exact repository evidence
5. project memory

Project memory must not override the supplied governance files.

READ

- `docs/governance/JMP_program_governance_v1.md`
- `docs/governance/JMP_canonical_state_v1.md`
- `docs/governance/JMP_roadmap_v1.md`
- `docs/governance/JMP_decision_log_v1.md`
- `docs/governance/JMP_mission_template_v1.md`
- `docs/missions/JMP_M05_phase5_inference_mission_charter_v1.md`
- Phase-3 manager acceptance
- Phase-4 manager acceptance
- Phase-4 execution report v2
- Phase-4 diagnostics
- current parameter-map/specification sources
- current JAX likelihood and score-related sources

Exact repository paths must be verified. Mark unknown paths as UNKNOWN rather
than inventing them.

TASK

Produce a task plan for the design-only stage of JMP-M05.

The plan must:

1. identify the exact economic and statistical questions to resolve;
2. identify every authoritative source required;
3. separate source-verification tasks from statistical decisions;
4. organize work around the three manager decisions:
   - finite-sample correction;
   - active-bound treatment;
   - score artifact format;
5. specify the formal derivations required;
6. specify the numerical-gate design required;
7. identify any narrowly targeted literature verification needed;
8. define the exact structure of the final inference-design memo;
9. preserve all mission non-scope restrictions;
10. end with one recommended sequence for producing the design memo.

Do not:

- write code;
- compute scores or covariance matrices;
- run inference;
- alter the mission gates;
- reopen Phase 3 or Phase 4;
- start synthetic recovery;
- start welfare or decomposition;
- produce several equally weighted baselines.

CREATE

`docs/missions/JMP_M05_task_plan_v1.md`

Use exactly these headings:

1. Plan verdict
2. Mission interpretation
3. Authoritative inputs
4. Source-verification tasks
5. Statistical design tasks
6. Finite-sample correction analysis
7. Active-bound inference analysis
8. Fixed-pin reporting analysis
9. Regional-block inference analysis
10. Score-artifact decision analysis
11. Numerical-gate design
12. Package-interface implications
13. Targeted literature verification
14. Required design-memo structure
15. Halt conditions
16. Deliverables
17. Recommended execution order
18. Immediate next action

FINAL VERDICT

Use exactly one:

- READY FOR DESIGN MEMO
- READY WITH SOURCE GAPS
- BLOCKED

Do not create or modify any other file.
Do not commit.
