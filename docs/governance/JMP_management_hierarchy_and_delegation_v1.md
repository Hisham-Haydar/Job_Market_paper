# JMP Management Hierarchy and Delegation Protocol v1

**Status:** Active after programme-manager acceptance  
**Date:** 2026-07-30  
**Principal investigator:** Hisham Haydar  
**Deputy programme director:** ChatGPT JMP project

## 1. Purpose

This protocol allows the JMP programme to advance without requiring the principal investigator to return to the deputy programme director after every operational task.

The programme remains governed by strategic stage gates. Work between those gates is delegated to persistent goal managers and mission task managers.

## 2. Management hierarchy

### Level 0 — Principal investigator

Hisham retains final authority over:

- paper identity and contribution;
- normative interpretation;
- empirical baseline;
- specification changes;
- public claims;
- repository promotion;
- publication and release decisions.

### Level 1 — Deputy programme director

The ChatGPT JMP project is second in command.

It is responsible for:

- canonical state;
- programme roadmap;
- mission sequencing;
- mission charters;
- cross-goal coordination;
- strategic acceptance;
- escalation decisions;
- final authorization of claims, baseline changes, and production-result promotion.

It should not supervise every operational subtask.

### Level 2A — Goal 1 manager: empirical JMP

A persistent Claude Project 1 manager chat governs the empirical-paper programme between strategic gates.

Recommended title:

`Goal 1 Manager — Empirical JMP`

Responsibilities:

- translate an approved mission charter into tasks;
- appoint task-specific chats and coding agents;
- maintain a mission status ledger;
- review source-verification and design artifacts;
- enforce scope and halt conditions;
- commission independent review;
- manage narrow remediation cycles;
- assemble one final return packet for the deputy programme director.

### Level 2B — Goal 2 manager: dclaborsupply package

A persistent Claude Project 2 manager chat governs the package programme.

Recommended title:

`Goal 2 Manager — dclaborsupply Package`

It may not make paper-level normative or empirical-baseline decisions.

### Level 2C — Welfare/decomposition workstream manager

Claude Project 3 remains subordinate to Goal 1.

Recommended title:

`Goal 1 Workstream Manager — Welfare and Decomposition`

It manages welfare-object and decomposition missions only after they are authorized by a Goal 1 mission charter.

### Level 3 — Mission task manager

Each active mission has one persistent task-manager chat.

Example:

`JMP-M05 Task Manager — Inference Design`

Responsibilities:

- maintain the task checklist;
- issue bounded prompts;
- verify required outputs exist;
- track source gaps;
- enforce halt conditions;
- report to the Goal 1 manager rather than directly to the deputy programme director.

The task manager does not approve its own final mission output.

### Level 4 — Specialist agents

- Claude Code: repository inspection, implementation, tests, executions, and file management.
- Codex: independent code and evidence review.
- Separate Claude/ChatGPT reasoning chat: independent methodological review.
- Deep Research: narrow literature verification.
- GitHub Copilot: autocomplete and small local edits only.

## 3. Strategic gates requiring deputy-programme review

Return to the ChatGPT JMP project only when one of the following occurs:

1. a mission design is complete and independently reviewed;
2. a mission result is complete and requires acceptance;
3. the canonical empirical baseline may change;
4. the main paper estimand or decomposition structure may change;
5. an unresolved source conflict affects accepted evidence;
6. a model specification change is proposed;
7. a real execution requires authorization not already delegated in the mission charter;
8. a public claim, paper result, or package release is proposed;
9. a halt condition cannot be resolved within the delegated mission.

Routine source retrieval, drafting, task decomposition, test fixes, and narrow review remediation do not require deputy-programme review.

## 4. Delegated authority of a goal manager

Within an approved mission charter, the goal manager may:

- approve a task plan;
- order read-only repository audits;
- accept factual source-verification reports;
- request narrow corrections;
- commission a design author;
- commission an independent reviewer;
- manage up to two narrow remediation cycles;
- choose between tools already authorized in the mission charter;
- prepare the final mission return packet.

The goal manager may not:

- change mission scope;
- weaken pre-registered gates;
- alter the main estimand;
- change the active baseline;
- authorize a model redesign;
- authorize welfare or decomposition claims;
- promote experimental results;
- authorize production execution unless the mission charter explicitly delegates that authority;
- alter canonical governance documents.

## 5. Separation of roles

For substantive missions:

- goal manager;
- task manager;
- author/implementer;
- independent reviewer

must be distinct chats or agents.

The same chat may not author and independently approve the same artifact.

## 6. Mission operating cycle

1. Deputy programme director issues a mission charter and delegation packet.
2. Goal manager opens a mission ledger.
3. Task manager closes factual/source prerequisites.
4. Specialist author produces the mission artifact.
5. Independent reviewer evaluates the exact artifact and evidence.
6. Goal manager resolves only narrow review findings.
7. Goal manager creates one final return packet.
8. Deputy programme director accepts, rejects, or changes strategy.

## 7. Escalation classes

### E0 — Routine

Handled by task manager:

- missing path;
- formatting error;
- incomplete inventory;
- test rerun;
- documentation correction.

### E1 — Mission-level

Handled by goal manager:

- source gap;
- bounded methodological ambiguity;
- narrow design correction;
- reviewer-requested clarification;
- one or two remediation cycles.

### E2 — Strategic

Escalate to deputy programme director:

- conflicting accepted sources;
- change in estimand;
- baseline/specification change;
- unresolved inference convention with material interpretive consequences;
- operator infeasibility;
- failed identification or recovery gate;
- expansion beyond mission scope.

### E3 — Principal-investigator decision

Escalate to Hisham:

- final normative choice;
- paper-title or central-contribution change;
- co-author/supervisor-facing commitment;
- public release;
- submission;
- irreversible data or repository action.

## 8. Return cadence

The normal return cadence is one packet per strategic gate, not one message per task.

For JMP-M05 design, the next return occurs only after:

- source verification is complete;
- the inference design memo is complete;
- an independent methodological review is complete;
- narrow corrections are resolved;
- the Goal 1 manager issues a final recommendation.

## 9. Canonical mission ledger

Each goal manager maintains:

`docs/missions/<MISSION_ID>_mission_ledger_v1.md`

The ledger records:

- current stage;
- tasks completed;
- artifacts created;
- reviewer verdicts;
- unresolved issues;
- escalations;
- next authorized action.

It is an operational file, not a substitute for the canonical state or decision log.
