# Prompt — JMP-M05C Increment-B Focused Closure Review

**Tool:** Codex  
**Model:** GPT-5.6 Codex or strongest available Codex review model  
**Reasoning:** High  
**Mode:** Read-only  
**Session:** Fresh  
**Scope:** Three frozen probes plus numerical regression only

## ROLE

Verify the finite Increment-B closure defined in
`JMP_M05C_incrementB_proportionality_decision_v1.md`.

This is not a broad software-security or architecture review.

Do not add requirements outside the three frozen probes unless a finding
affects:

- econometric/statistical correctness;
- the actual production path;
- accepted-artifact integrity;
- reproducibility;
- row-level data persistence or disclosure.

Other observations must be listed as nonblocking technical debt.

Do not modify files.
Do not commit.
Do not begin Increment C.
Do not run the full population.

## READ

- certification proportionality rule;
- Increment-B proportionality decision;
- Review B v2;
- three-fix closure report;
- exact current source/test diff;
- the three frozen probe tests;
- existing Increment-A and Increment-B regression tests.

## VERIFY

### Probe provenance

1. the three probes were added before implementation changes or their hashes and
   provenance otherwise establish they were frozen;
2. they reproduce the original defects on the archived/pre-fix source;
3. the implementer did not weaken or replace them.

### B-1

4. the expected T-22 active-name authority is not caller-overridable;
5. it is derived from or exactly bound to the authenticated parameter map;
6. forged expected-name attempts refuse.

### B-2

7. invalid grade and other refusal inputs are validated before filesystem write;
8. nonexistent destinations remain nonexistent;
9. existing sentinel destinations remain byte-identical.

### B-3

10. no unrestricted generic `extra=` mapping remains, or only explicit
    allowlisted scalar fields exist;
11. `5×37` score blocks, arrays, bytes, row-level sequences, nested sensitive
    containers, and protected-field collisions refuse before writing;
12. protected fields cannot be overwritten.

### Regression

13. numerical outputs, constants, schemas, gradient authority, and covariance
    arithmetic are unchanged;
14. Increment-A and Increment-B suites pass;
15. the twelve existing proofs pass;
16. accepted bundles rehash;
17. nested repository is clean;
18. no row-level score artifact exists;
19. no Increment-C code exists;
20. exact state is commit-ready.

## CREATE

`docs/France_case/P2a/FR_P2a_streaming_incrementB_closure_review_v1.md`

Use exactly these headings:

1. Focused review verdict
2. Scope
3. Probe provenance
4. T-22 authority
5. Pre-write serializer refusal
6. No arbitrary score-summary extension
7. Numerical regression
8. Statistical-design preservation
9. Package-boundary preservation
10. Artifact and repository integrity
11. Nonblocking technical debt
12. Whether Increment B may be committed
13. Whether Increment C may begin
14. Immediate next action

The first section must contain exactly one:

**FINAL VERDICT: PASS**

or:

**FINAL VERDICT: FAIL**

Do not introduce `APPROVE AFTER FIXES`.
