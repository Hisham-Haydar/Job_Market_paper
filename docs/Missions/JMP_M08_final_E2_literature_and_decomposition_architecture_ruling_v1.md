# JMP-M08 Deputy Ruling — Final E2 Closure, Literature Status, and Decomposition Architecture v1

**Programme:** Goal 1 — Empirical JMP  
**Decision-maker:** Deputy Programme Director  
**Date:** 2026-08-07  
**Status:** Binding  
**Scope:** Three decisions only: literature workflow, parity-report E2 closure, and M08 decomposition architecture

---

## 1. Literature workflow ruling

### 1.1 No broad literature reopening

The JMP literature rebuild is treated as complete for the current empirical-design stage.

The accepted record already includes:

- corpus inventory and tiering;
- T1A and T1B paper summaries and audits;
- the targeted DR03 gap audit;
- structured paper summaries consolidated in `Literature_collection.md`;
- literature indexes and a literature-review skeleton;
- a closest-competitor and overclaim-warning architecture.

No new broad paper search, no repeat Zotero-library summarisation, and no new literature mission is authorized during M08 or LOC4.

### 1.2 Permitted later literature work

Only a claim-triggered targeted action is permitted:

- verify one citation or metadata item;
- extract one paper needed for an exact manuscript claim;
- update a working-paper status;
- close one explicitly identified comparator gap.

For the decomposition methods section, the existing corpus entries on Shorrocks (2013), Audoly et al. (2025), Bargain et al. (2013), Dagsvik and Karlström (2005), and Jacquet, Jia and Thoresen (2026) are sufficient for the current design stage.

A Zotero-completeness audit may be performed during final manuscript citation closure, but it is not a current research task.

---

## 2. Final parity-report E2 closure

### 2.1 Valid residual finding

The report-v3 narrow reviewer accepted E2-1, E2-3, and E2-4 and rejected E2-2 because report v3 §0 retained this sentence:

> “The review was explicit that its T4 rejection was ‘an implementation defect that blocks scientific certification; not affirmative evidence of a scientific mismatch’ … and the new run bears that out: the numbers are unchanged, but they are now certified rather than asserted.”

The clause after the quoted reviewer classification makes a pairwise inference between the old and new attempts. It is outside the new attempt's packet and conflicts with the report-wide rule that prior attempts provide lineage only.

### 2.2 Authorized remedy

Create:

`docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v4.md`

Report v3 remains immutable history.

In §0, replace the full sentence above with:

> “The review classified its T4 rejection as an implementation defect that blocked scientific certification rather than affirmative evidence of a finite scientific mismatch.”

No other report text may change except:

- title/version bookkeeping;
- a one-paragraph v4 supersession declaration;
- mechanical cross-reference repair required by the version change.

The v4 declaration must state:

- v4 supersedes v3;
- v3 remains immutable history;
- the only substantive change is removal of the residual E2-2 pairwise inference;
- the attempt of record, code, packet, statistics, tolerance, and PASS verdict are unchanged;
- no execution occurred.

Create a concise change log:

`docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v4_change_log.md`

### 2.3 Final verification

Use one fresh GPT-5.6 Codex read-only review.

Review exactly:

- the pairwise-inference clause is gone;
- no statement elsewhere says prior attempts numerically corroborate the attempt of record;
- prior attempts are lineage/history only;
- no extra substantive or numerical change exists from v3 to v4.

No code review, gate rerun, EUROMOD execution, architecture review, or new requirement is permitted.

On ACCEPT:

- v4 becomes the parity report of record;
- create one acceptance note;
- freeze the parity axis;
- proceed without deputy contact.

On REJECT:

- return to the deputy;
- no further self-authorized correction.

---

## 3. Decomposition architecture ruling

### 3.1 W3 is not a level-inequality decomposition target

`W3` remains:

- the first welfare-engine validation measure;
- the laissez-faire/full-responsibility endpoint in the welfare-family comparison;
- a reference-recovery and inversion diagnostic.

It is not the primary source-decomposition measure.

Reason: under the accepted own-set laissez-faire construction, baseline
\(\Omega_i^3 \simeq 0\) for every household. Hence \(I(\Omega^3)\simeq0\) is correct by construction and contains no observed baseline inequality to allocate.

Do not redefine `W3` and do not create a “common-reference W3.” That would silently replace a characterised welfare measure with a new object.

### 3.2 Primary and secondary decomposition measures

For M08:

- **Primary source decomposition:** `W2`, the non-degenerate Full-Responsibility measure.
- **Secondary decomposition:** `W5`, the access-compensated dual, used to show how attribution changes under a different normative reference.
- **Validation only:** `W3`.
- `W1`, `W4`, and `W6` remain in the six-measure welfare-family results but do not require a Shapley decomposition in M08.

This preserves the intended two-decomposition workload while removing the degenerate object.

All measure references are frozen across coalitions. The decomposition therefore measures changes in attained welfare valued in the baseline measure's units; it does not allow the reference itself to move with the equalised channel.

### 3.3 The three-channel game is conditional, not a complete four-channel causal partition

The M08 Shapley game remains:

\[
N=\{A,B,P\},
\]

where:

- \(A\): access;
- \(B\): ability/wage technology;
- \(P\): preferences.

The following remain fixed across coalitions:

- the disposable-income matrix \(c_{ij}\);
- tax-benefit rules and non-labour-income inputs;
- alternative support;
- proposal correction \(\pi\);
- measure references;
- all other objects not assigned to \(A,B,P\).

Do not invent a fourth `endowment/needs` Shapley operator in M08. Merely naming a fourth channel without an executable counterfactual operator would not constitute a Shapley decomposition. A genuine fourth-channel design would require a separately authorized operator and probably targeted EUROMOD re-evaluation; it is outside M08.

### 3.4 Exact residual accounting

For measure \(k\in\{W2,W5\}\), let \(I^k(S)\) be inequality when channels in \(S\subseteq N\) are equalised.

Compute the standard three-channel Shapley contributions:

\[
\phi_q^k
=
\sum_{S\subseteq N\setminus\{q\}}
\frac{|S|!\,(3-|S|-1)!}{3!}
\left[I^k(S)-I^k(S\cup\{q\})\right],
\qquad q\in\{A,B,P\}.
\]

Define the fixed-background residual:

\[
R_{\mathrm{bg}}^k=I^k(\{A,B,P\}).
\]

The exact identities required are:

\[
\phi_A^k+\phi_B^k+\phi_P^k
=
I^k(\varnothing)-R_{\mathrm{bg}}^k,
\]

and

\[
I^k(\varnothing)
=
\phi_A^k+\phi_B^k+\phi_P^k+R_{\mathrm{bg}}^k.
\]

This is the M08 exhaustiveness rule.

`R_bg` is not a Shapley contribution and is not called an identified endowment, needs, circumstance, unfairness, or causal component. It is the inequality remaining after all three modeled structural channels are equalised while the frozen background is retained.

The residual may contain:

- non-labour-income and demographic variation operating through \(c_{ij}\);
- tax-benefit mapping heterogeneity not assigned to the three channels;
- fixed reference/support heterogeneity;
- any remaining model-fixed heterogeneity;
- numerical integration noise, which must be separately bounded by the integration gates.

The validation memo must enumerate these sources and separate substantive residual inequality from numerical Shapley arithmetic error.

### 3.5 Revised validation gates

Replace the grand-coalition-zero requirement with:

1. **Operator completeness:** all assigned access, ability, and preference arguments are equalised as frozen.
2. **Shapley arithmetic:**  
   \[
   \left|
   \sum_q\phi_q^k-\left[I^k(\varnothing)-R_{\mathrm{bg}}^k\right]
   \right|
   \leq \varepsilon_{\mathrm{Shapley}}.
   \]
3. **Total accounting:**  
   \[
   \left|
   I^k(\varnothing)-\left(\phi_A^k+\phi_B^k+\phi_P^k+R_{\mathrm{bg}}^k\right)
   \right|
   \leq \varepsilon_{\mathrm{Shapley}}.
   \]
4. **Residual reporting:** `R_bg` is reported in levels and as a share of baseline inequality.
5. **No silent renormalisation:** components are not rescaled to force their shares to sum to 100 percent after excluding the residual.

The separate numerical-integration stability tolerance continues to govern the accuracy of each \(I^k(S)\); it is not replaced by the Shapley arithmetic tolerance.

### 3.6 Headline quantities

For the primary `W2` decomposition, report:

\[
C_{\mathrm{access}}=\phi_A^{W2},
\]

\[
C_{\mathrm{opportunity}}=\phi_A^{W2}+\phi_B^{W2},
\]

\[
C_{\mathrm{preference}}=\phi_P^{W2},
\]

\[
R_{\mathrm{bg}}=R_{\mathrm{bg}}^{W2}.
\]

The opportunity share used by S-10 is:

\[
s_{\mathrm{opp}}
=
\frac{\phi_A^{W2}+\phi_B^{W2}}
     {I^{W2}(\varnothing)}.
\]

Also report:

- access-only share \(\phi_A^{W2}/I^{W2}(\varnothing)\);
- preference-related share \(\phi_P^{W2}/I^{W2}(\varnothing)\);
- fixed-background residual share \(R_{\mathrm{bg}}^{W2}/I^{W2}(\varnothing)\).

All contributions are reported signed. Do not suppress a negative contribution and do not reinterpret it causally.

The pre-registered S-10 2-percentage-point trigger applies to \(s_{\mathrm{opp}}\) as defined above.

### 3.7 Interpretation

The paper-facing interpretation becomes:

> The decomposition attributes the part of measured welfare inequality that changes when the model's access, ability, and preference channels are equalised. Inequality remaining after all three equalizations is reported separately as a fixed-background residual, principally reflecting household budget and other frozen heterogeneity outside the three structural labour-market channels.

This preserves the main question while being explicit that the first M08 prototype is not a complete causal decomposition of every determinant of welfare.

A fully specified four-channel decomposition with an endowment/needs operator may be considered only after M08 and LOC4, if the residual is quantitatively material and scientifically worth explaining.

---

## 4. Contract amendments required before freeze

The Goal 1 Manager must amend the execution contract as follows:

1. replace every statement that `W3` is the primary decomposition target with `W2`;
2. replace the former `W2` second-check requirement with `W5` as the secondary decomposition;
3. retain `W3` as validation-only;
4. replace V8/V20 grand-coalition degeneracy with the residual-accounting gates in §3.5;
5. define `R_bg` and the shares in §3.6;
6. remove any requirement that \(I(\{A,B,P\})=0\);
7. remove any claim that the three channels exhaust all household welfare heterogeneity;
8. preserve \(c_{ij}\), \(\pi\), support, and measure references unchanged across coalitions;
9. record that no fourth-channel operator is authorized;
10. keep the access/ability/preference operator definitions otherwise unchanged.

No welfare execution may begin until the amended contract passes the existing Stage-A economics review.

---

## 5. Return rule

The Goal 1 Manager may proceed without deputy contact after:

- report v4 receives final Codex ACCEPT;
- the execution contract incorporates this decomposition ruling;
- the independent Stage-A contract review accepts the amended architecture;
- all other pre-existing freeze items are resolved under manager authority or separately escalated where required.

Return to the deputy only for:

- a valid final E2 REJECT;
- inability to construct non-degenerate `W2`;
- a claim that the residual requires a fourth operator before M08 can answer the paper's question;
- a generic-package change;
- an integration-gate failure without a frozen rule;
- a Tier-2 S-10 trigger;
- or a conflict with LOC4.
