# Prompt — JMP-M05B Closed-Form Code Review v4

**Tool:** Codex  
**Model:** GPT-5.6 Codex or current strongest Codex review model  
**Reasoning:** Maximum  
**Mode:** Read-only  
**Session:** Fresh  
**Workspace:** exact remediated MNL state with read-only nested package and
redacted restricted-store evidence

## ROLE

Perform the final closed-form independent review of JMP-M05B.

This review decides whether the architectural closure is complete. No further
remediation cycle exists under the mission.

Do not edit files.
Do not compute the full 1,555-household score matrix.
Do not run Phase 5.
Do not commit.
Do not add new objectives beyond the frozen threat model and the seven
authorized closure groups.

## BINDING THREAT MODEL

Protect against unsupported/documented/import-callable application bypasses,
caller-supplied config or custody, stale authorization, mutation, Git leakage,
and transaction inconsistency.

Do not require security against arbitrary malicious code execution, source
rewriting, monkeypatching, or interpreter introspection by an actor already
controlling the Python process.

## READ

- `JMP_M05B_E2_deputy_decision_v2.md`;
- design v4 and binding methods reviews;
- charter and mission ledger;
- reviews v1, v2, and v3;
- remediation reports v1 and v2;
- architectural closure report v1;
- complete current Git diff;
- Phase-5 source/config/tests;
- `phase5_full_score_surface_inventory_v1.json`;
- parameter-map CSV and source inventory;
- accepted Phase-3 and Phase-4 artifacts and verifiers;
- redacted restricted-store provisioning evidence.

## CLOSED-FORM DECISION RULE

The application-level full-score surface count must equal exactly one.

The sole accepted surface is the canonical gated process entry in
`run_p2a_phase5_inference.py`, with parent and T-12 child as internally
authorized roles.

Generic low-level package derivative primitives are not additional application
surfaces unless they independently construct or publish the accepted Phase-5
full-score artifact without the canonical entry.

If a second application-level full-score surface exists, verdict is `REJECT`.

If exactly one exists, verify the remaining six narrow groups and the applicable
original gates. Do not continue searching for stronger in-process adversarial
security outside the frozen threat model.

## REVIEW GATES

### A. Preservation

1. statistical design unchanged;
2. package unchanged;
3. accepted theta, bundles, maps, constants, hypotheses, and custody ruling
   unchanged.

### B. Single surface

4. surface inventory parses and hashes;
5. inventory count is exactly one;
6. static source inspection confirms exactly one application-level full-score
   entry;
7. direct former contract/evaluate route is structurally incapable;
8. no caller-supplied config, authorization record, root, or output path reaches
   full scoring;
9. parent and T-12 child use the same canonical entry;
10. noncanonical-route behavioral tests pass.

### C. Capability and config

11. authorization context is created only after canonical gates;
12. ordinary imports cannot construct it through supported interfaces;
13. canonical YAML bytes/digest are the actual consumed config;
14. store identity is bound to the authenticated provisioning record;
15. child capability is single-use, attempt-bound, and replay-resistant;
16. no claim exceeds the frozen threat model.

### D. STOPPED rename

17. source is revalidated immediately before rename;
18. resulting endpoint is validated after rename;
19. reparse/junction/path escape tests are behavioral and pass.

### E. Post-evaluation reauthentication

20. parent reauthenticates after its final evaluation;
21. T-12 child reauthenticates after its evaluation;
22. sources are reloaded rather than semantically trusted from cache;
23. mutation-window tests stop before publication.

### F. Inventory truthfulness

24. files, directories, junctions, symlinks, unreadable and partial members are
   inventoried;
25. top-level and nested custody facts agree;
26. STOPPED bundle membership/hash reflect actual retained members;
27. partial-write and junction tests pass.

### G. Lifecycle and documentation

28. exact lifecycle profiles exist for uncommitted, committed, and one-attempt
   states;
29. complete no-full-score suite passes in each simulated profile;
30. review/help paths are current;
31. comparator language is exactly mixed absolute/relative.

### H. Original certification gates

32. all applicable original 51-gate checks pass under the revised architecture;
33. accepted artifacts rehash;
34. nested repository is clean;
35. no full score, score artifact, dry-run attempt, or `complete/` was created;
36. `git diff --check` passes;
37. exact state is commit-ready.

## CREATE

`docs/France_case/P2a/FR_P2a_region_live_phase5_code_review_v4.md`

Use exactly these headings:

1. Phase-5 review-v4 verdict
2. Scope and exact state
3. Frozen threat model
4. Statistical-design preservation
5. Package-boundary preservation
6. Closed-form surface inventory
7. Single gated process entry
8. Authorization capability and canonical config
9. Parent and T-12 child roles
10. STOPPED rename safety
11. Post-evaluation reauthentication
12. Retained-member and custody truthfulness
13. Behavioral test coverage
14. Lifecycle-aware test coverage
15. Documentation consistency
16. Accepted-artifact integrity
17. Residual defects
18. Whether exact state may be committed
19. Whether one full dry run may follow after commit
20. Immediate next action

The first section must contain exactly one:

**FINAL VERDICT: APPROVE**

or:

**FINAL VERDICT: REJECT**

No `APPROVE AFTER FIXES` verdict is permitted.

Do not modify or commit anything.
Do not run Phase 5.
