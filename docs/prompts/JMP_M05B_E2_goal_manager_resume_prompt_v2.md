# Prompt — Resume JMP-M05B After Second E2 Decision

Use in the existing persistent:

`Goal 1 Manager — Empirical JMP`

**Model:** Fable; Opus fallback  
**Thinking:** On  
**Effort:** High / long-horizon management

---

Adopt `JMP_M05B_E2_deputy_decision_v2.md` as binding.

The review-v3 REJECT is valid. The statistical design remains closed. One final
architectural closure cycle is authorized; it is not an ordinary third patch
cycle.

Manage autonomously:

1. architectural closure using
   `JMP_M05B_architectural_closure_prompt_v1.md`;
2. no-full-score validation and surface inventory;
3. independent fresh-session Codex review v4 using
   `JMP_M05B_closed_form_code_review_v4_prompt_v1.md`;
4. if and only if review v4 returns APPROVE:
   - separate test-42 housekeeping commit;
   - exact reviewed Phase-5 implementation/review commit;
   - clean preflight;
   - exactly one full dry run;
   - Goal 1 dry-run audit;
5. if review v4 returns REJECT:
   - stop immediately;
   - preserve state;
   - return to the deputy programme director;
   - do not commission another correction.

Update `JMP_M05B_mission_ledger_v1.md`:

- review v3 REJECT and second E2 halt;
- deputy architectural closure authorization;
- ordinary remediation budget exhausted;
- architectural closure is one-time;
- review v4 is binary APPROVE/REJECT;
- no later fix cycle exists.

Every operational reply must contain a complete NEXT ACTION CARD.

The first action card must commission the architectural closure in the preserved
original implementation session:

- Tool: Claude Code
- Model: Opus
- Thinking: On
- Effort: High
- Workspace: MNL with read-only nested package, Job_Market_paper governance, and
  provisioned restricted store
- Prompt: full contents of
  `JMP_M05B_architectural_closure_prompt_v1.md`
- Return destination: this Goal 1 Manager chat

Do not ask Hisham to choose tools, prompts, models, files, or routing.

Return to the deputy programme director only after:

- audited full dry run with the charter packet; or
- review v4 REJECT; or
- an E2 issue such as design/package change, score-identity failure, or custody
  infeasibility.

The production real run remains unauthorized.
