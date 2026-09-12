# JMP household identifier sanitisation — decision note v1

| Field | Value |
|---|---|
| Card | SANITISE-1 — forward ID sanitisation (Deputy ruling, section 3) |
| Date | 2026-09-12 |
| Scope | Live Job_Market_paper working tree (tracked and untracked) and the CLEAN-A cleanup quarantine |
| History | Not rewritten. No commit deleted. No force-push. |

## Decision

1. **Legacy identifiers remain in history.** Three pseudonymous household identifiers, used as worked-example check households in the MEASURE-MAP-1R acceptance record, the measure map, the stochastic ability set bridge memo and its review, appear in historical commits of this repository. Those commits are left as they are.

2. **Current live documents use labels.** Every current version of these documents uses these labels instead:

   | Label | Role in the record |
   |---|---|
   | H-S1 | Single, worker check household |
   | H-C1 | Couple check household |
   | H-S2 | Single, nonworker check household |

   Derived forms of the same identifier are labelled too: the F4A/F4C pooled key appears as `20000_H-S1` or `20000_H-S2`. Only the identifier was replaced. Every surrounding number (ratios, welfare levels, hashes, counts) is unchanged.

3. **The label-to-identifier mapping is outside Git.** It exists only in the restricted store, next to the cleanup quarantine. The same place holds byte-exact pre-sanitisation copies of the untracked and quarantined files. Pre-sanitisation versions of tracked files can be recovered from their historical commits. The mapping must never be committed to either repository.

4. **History was deliberately not rewritten.** Many commits in this repository and in MNL are cited by SHA in rulings, acceptance records and the MNL measure-map gate. Rewriting history would change those SHAs and break the provenance chain that the CLEAN-B hash registry pins. The sanitisation therefore only moves forward.

## Consequences for hash citations

- The SHA-256 of each sanitised tracked document has changed. Citations to the old hash now resolve to the historical version at the cited commit. That commit is still reachable, so every such citation stays verifiable against history.
- The MNL gate `gate/measure_map_accepted.json` was regenerated against the sanitised commit of `JMP_measure_map_v1.md`. The historical commit and hash are kept in the gate file's labelled provenance field.
- Regenerating derived evidence from restricted inputs, such as the bridge fast-lane CSV, will write raw identifiers back. Any regeneration must apply the same labels before the output is committed.
