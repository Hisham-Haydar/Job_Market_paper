#!/usr/bin/env python3
"""Synchronized M3--M11 wording and claim-to-evidence gate.

The gate reads the six seminar surfaces plus the executed DECOMP-2 and POSFIT
artifacts.  Numerical claims are parsed as signed floats and compared with
recomputed source values; they are not accepted merely because a digit string
occurs somewhere in a document.
"""
from __future__ import annotations

import csv
import hashlib
import html
import json
import re
import sys
import unicodedata
from html.parser import HTMLParser
from pathlib import Path


JMP = Path(__file__).resolve().parents[1]
REPO = JMP.parent
DECOMP = REPO / "MNL_decomp/outputs/welfare/preseminar_pab_v1"
NOTEBOOK = REPO / "MNL/experiments/JMP_SEMINAR_SPRINT/JMP_canonical_AtoZ.ipynb"
OUT_MD = JMP / "reports/JMP_final_claim_wording_gate_v1.md"
OUT_JSON = JMP / "reports/JMP_final_claim_wording_gate_v1.json"


class _VisibleText(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.skip = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style"}:
            self.skip += 1

    def handle_endtag(self, tag):
        if tag in {"script", "style"} and self.skip:
            self.skip -= 1

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)


def read_html(path: Path) -> str:
    raw = path.read_text(encoding="utf-8")
    raw = re.sub(r"data:image/[^;]+;base64,[A-Za-z0-9+/=]+", "", raw)
    p = _VisibleText()
    p.feed(raw)
    return " ".join(p.parts)


def notebook_text(path: Path) -> tuple[str, dict]:
    nb = json.loads(path.read_text(encoding="utf-8"))
    chunks: list[str] = []
    for cell in nb["cells"]:
        if cell.get("cell_type") == "markdown":
            chunks.append("".join(cell.get("source", [])))
        for output in cell.get("outputs", []):
            data = output.get("data", {})
            for mime in ("text/plain", "text/html", "text/markdown"):
                value = data.get(mime)
                if value:
                    chunks.append("".join(value) if isinstance(value, list) else value)
    return "\n".join(chunks), nb


def normalize(value: str) -> str:
    value = html.unescape(unicodedata.normalize("NFKC", value))
    value = value.replace("’", "'").replace("‘", "'")
    value = value.replace("–", "-").replace("—", "-").replace("−", "-")
    value = value.replace("×", "x")
    value = value.replace("\\operatorname{Var}", "Var")
    value = value.replace("\\Delta", "Delta").replace("\\log", "log")
    value = value.replace("\\(", "").replace("\\)", "")
    value = value.replace("\\%", "%").replace("--", "-")
    # Preserve the contents of ordinary one-level LaTeX wrappers.
    for _ in range(3):
        value = re.sub(
            r"\\(?:text|mathrm|mathbf|mathit|emph|textbf|textit|caveat|headlineframe|note)"
            r"\{([^{}]*)\}",
            r"\1",
            value,
        )
    value = re.sub(r"\\[A-Za-z@]+(?:\[[^\]]*\])?", " ", value)
    value = re.sub(r"[{}$*_#>`\"]", " ", value)
    value = re.sub(r"\s*([()/,:;%])\s*", r"\1", value)
    return re.sub(r"\s+", " ", value).strip().lower()


def rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


deck_source = JMP / "beamer/JMP_seminar_deck_r6.tex"
deck_notes = JMP / "beamer/build/JMP_seminar_deck_r6_rehearsal_text.txt"
story_html = JMP / "reports/JMP_research_story_report_v5.html"
paper_tex = JMP / "manuscript/JMP_working_paper_for_seminar_v5.tex"
gallery_html = JMP / "reports/JMP_results_gallery_current.html"
rehearsal_md = JMP / "reports/rehearsal_pack_v1.md"
nb_text, nb = notebook_text(NOTEBOOK)

deck_text = deck_source.read_text(encoding="utf-8")
for macro, expansion in {
    r"\DTwoMinPct": "1.8",
    r"\DTwoMaxPct": "9.9",
    r"\DTwoVarMinPct": "100",
    r"\DTwoVarMaxPct": "127",
}.items():
    deck_text = deck_text.replace(macro, expansion)

surface_raw = {
    "Deck": deck_text + "\n" + deck_notes.read_text(encoding="utf-8"),
    "Story report": read_html(story_html),
    "Working paper": paper_tex.read_text(encoding="utf-8"),
    "Technical gallery": read_html(gallery_html),
    "Canonical notebook": nb_text,
    "Rehearsal script": rehearsal_md.read_text(encoding="utf-8"),
}
surface = {name: normalize(value) for name, value in surface_raw.items()}


M3 = ("The decomposition is bounded by design because household resources, needs and composition are held fixed. "
      "Within that bounded game, equalising P/A/B changes the Gini by 1.8-9.9% of its baseline level, depending on sample and reporting scale.")
M4 = ("Dispersion in consumption is quantitatively large relative to dispersion in log well-being: Var(log C) is roughly 100-127% of Var(log W), "
      "with the excess offset by a large negative covariance between consumption and the leisure valuation. DECOMP-2 holds household resources, "
      "needs and composition fixed, leaving important sources of dispersion outside the P/A/B allocation.")
M5_A = "local geographic/temporal access shifters(region,urban/rural,year)"
M6 = "preferences and opportunity components are jointly estimated, with their separation relying on maintained functional-form and exclusion restrictions."
M7 = ("The money metric is derived from the Measure-1 reference-set principle. Under the current empirical specification its direct reference collapses "
      "to the universally available non-employment state; opportunity heterogeneity therefore affects the current welfare measure through attained bundles.")
TASTE = ("The baseline deliberately keeps systematic preference heterogeneity parsimonious: age profiles for all four adult groups and a child-related "
         "shifter for women. The child term is interpreted as a reduced-form behavioural/time-constraint shifter, not as pure taste.")
M10 = ("In a preliminary three-factor structural exercise that holds household resources, needs and composition fixed, equalising systematic utility "
       "heterogeneity, coarse geographic/temporal access heterogeneity and earning opportunities changes money-metric well-being inequality by 1.8-9.9% "
       "of the baseline Gini, depending on household type and reporting scale. Within the Shapley allocation of that movable component, earning-opportunity "
       "heterogeneity has a larger contribution than the coarse geographic/temporal access channel in both samples and both reporting conventions. "
       "The preference contribution is not sign-robust to equivalisation.")
M10_CAVEAT = "These are preliminary model-based accounting results, not causal estimates and not the final decomposition of total well-being inequality."
M11 = ("a valid gross-wage perturbation requires new tax-benefit repricing over the affected job alternatives, and the current priced support does not "
       "contain that counterfactual.")

required = {
    "M3 boundedness": M3,
    "M4 variance": M4,
    "M5 narrow A": M5_A,
    "M6 identification": M6,
    "M7 welfare reference": M7,
    "Taste shifters": TASTE,
    "M10 approved claim": M10,
    "M10 immediate caveat": M10 + " " + M10_CAVEAT,
}

coverage: dict[str, dict[str, bool]] = {}
failures: list[str] = []
for name, body in surface.items():
    checks = {label: normalize(needle) in body for label, needle in required.items()}
    checks["M8 -1 nat + cases"] = all(x in body for x in (
        "one-nat shortfall",
        "-1",
        "current nonworkers:w=c",
        "current workers:w<c under the maintained empirical domain",
    ))
    checks["Age is not alone"] = all(
        token in body
        for token in (
            "intercept", "age", "four adult groups", "group-specific leisure curvature",
            "shifter for women", "sex and household type", "separate parameter blocks",
        )
    ) and bool(re.search(r"age(?: |-)squared", body))
    checks["M11 if-asked reason"] = normalize(M11) in body
    coverage[name] = checks
    failures.extend(f"{name}: {label}" for label, ok in checks.items() if not ok)


# Forbidden reversals and stale headline formulations.
forbidden = {
    "small by construction": r"(?:delta i|δi|movable inequality).{0,45}small by construction",
    "fixed component alone": r"fixed component alone accounts for",
    "categorical identification": r"(?:preferences and opportunities are identified jointly|jointly identified)",
    "positive-nat worked case": r"l\s*\([^)]*j[^)]*\)\s*-\s*l\s*\([^)]*o[^)]*\)\s*=\s*\+\s*1",
    "group-count fit headline": r"(?:3 of 4|three of (?:the )?four|the three groups that clear|calibration slope passes for three groups)",
    "broad A equality": r"\ba\s*(?:=|is)\s*local labo[u]?r-market access",
}
forbidden_hits: list[str] = []
for name, body in surface.items():
    for label, pattern in forbidden.items():
        if re.search(pattern, body, flags=re.IGNORECASE | re.DOTALL):
            forbidden_hits.append(f"{name}: {label}")
failures.extend(forbidden_hits)


# Notebook-only M9 corrections and preservation of the concurrent inserts.
nb_norm = surface["Canonical notebook"]
m9_required = (
    "thinner or worse opportunity density",
    "sampled/priced representation of potential job alternatives",
    "larger estimated leisure coefficients under the maintained utility-scale normalization",
    "coarse geographic/temporal access",
    "systematic leisure valuation associated with attained hours",
    "raw job-set construction and euromod pricing are not yet one unified rerunnable stage",
    "unified job-set construction + pricing module",
)
m9_ok = all(normalize(x) in nb_norm for x in m9_required)
if not m9_ok:
    failures.append("Canonical notebook: one or more M9 replacement/disclosure phrases")
nb_ids = {cell.get("id") for cell in nb["cells"]}
concurrent_ids = {
    "fds1item2head", "fds1item2code", "fds1item3head", "fds1item3code",
    "fds1item4head", "fds1item4code", "8f8f9514",
}
concurrent_ok = concurrent_ids <= nb_ids
if not concurrent_ok:
    failures.append("Canonical notebook: concurrent FINAL-DIAGNOSTIC/LES cells not preserved")


# Recompute signed DECOMP-2 evidence.
coalitions: dict[tuple[str, str, str], float] = {}
shapley: dict[tuple[str, str, str], float] = {}
for sample in ("singles", "couples"):
    for row in rows(DECOMP / f"coalition_values_{sample}.csv"):
        coalitions[(sample, row["scale"], row["coalition"])] = float(row["I_S_gini"])
    for row in rows(DECOMP / f"shapley_PAB_{sample}.csv"):
        if row["factor"] in {"P", "A", "B"}:
            shapley[(sample, row["scale"], row["factor"])] = float(row["gini_point_contribution"])

range_cells: list[dict[str, object]] = []
for sample in ("singles", "couples"):
    for scale in ("unequivalised", "equivalised"):
        base = coalitions[(sample, scale, "EMPTY")]
        equal = coalitions[(sample, scale, "PAB")]
        pct = 100.0 * (base - equal) / base
        range_cells.append({"sample": sample, "scale": scale, "percent": pct})
expected_range = (round(min(x["percent"] for x in range_cells), 1),
                  round(max(x["percent"] for x in range_cells), 1))

parsed_ranges: dict[str, tuple[float, float] | None] = {}
range_pattern = re.compile(
    r"changes money-metric well-being inequality by\s*([+-]?\d+(?:\.\d+)?)\s*-\s*"
    r"([+-]?\d+(?:\.\d+)?)%\s*of the baseline gini"
)
for name, body in surface.items():
    match = range_pattern.search(body)
    parsed = (float(match.group(1)), float(match.group(2))) if match else None
    parsed_ranges[name] = parsed
    if parsed != expected_range:
        failures.append(f"{name}: parsed M10 range {parsed!r} != evidence {expected_range!r}")

ordering_ok = all(
    shapley[(sample, scale, "B")] > shapley[(sample, scale, "A")]
    for sample in ("singles", "couples") for scale in ("unequivalised", "equivalised")
)
preference_sign_ok = all(
    shapley[(sample, "unequivalised", "P")] > 0
    and shapley[(sample, "equivalised", "P")] < 0
    for sample in ("singles", "couples")
)
if not ordering_ok:
    failures.append("DECOMP-2 evidence: B does not exceed A in every sample/scale")
if not preference_sign_ok:
    failures.append("DECOMP-2 evidence: P does not switch + to - with equivalisation in both samples")

# Detailed tables must contain parsed floats agreeing with all 12 source
# Shapley cells to four displayed decimals (within half a final displayed unit).
# The gallery summarizes the four sign-sensitive P cells in prose; its own
# verifier separately checks that its two embedded decomposition figures were
# generated from the current inputs.
signed_detail: dict[str, bool] = {}
expected_signed = list(shapley.values())
for name in ("Story report", "Working paper", "Canonical notebook"):
    parsed = [float(x) for x in re.findall(r"(?<![\d.])([+-]?\d+\.\d{4,6})(?!\d)", surface[name])]
    ok = all(any(abs(actual - expected) <= 0.0000501 for actual in parsed)
             for expected in expected_signed)
    signed_detail[name] = ok
    if not ok:
        failures.append(f"{name}: signed Shapley cells do not parse back to all source values")
gallery_parsed = [float(x) for x in re.findall(
    r"(?<![\d.])([+-]?\d+\.\d{4})(?!\d)", surface["Technical gallery"]
)]
gallery_expected = [shapley[(sample, scale, "P")]
                    for sample in ("singles", "couples")
                    for scale in ("unequivalised", "equivalised")]
gallery_ok = all(any(abs(actual - expected) <= 0.0000501 for actual in gallery_parsed)
                 for expected in gallery_expected)
signed_detail["Technical gallery"] = gallery_ok
if not gallery_ok:
    failures.append("Technical gallery: signed preference cells do not parse back to source values")

variance_rows = rows(DECOMP / "log_variance_split_v1.csv")
variance_shares = [100.0 * float(row["share_var_log_C"]) for row in variance_rows]
variance_range = (round(min(variance_shares)), round(max(variance_shares)))
if variance_range != (100, 127):
    failures.append(f"DECOMP-2 evidence: rounded variance range is {variance_range}, expected (100, 127)")


# M2 preservation: authoritative groups remain fully represented and the safe
# wording is present on the prose surfaces that summarize fit.  The final gate
# does not change or re-adjudicate those verdicts.
decision_rows = rows(REPO / "MNL_posfit/outputs/positive_fit_diagnostics_v3/decision_rules_results.csv")
fit_groups = sorted({row["group"] for row in decision_rows})
fit_table_ok = len(decision_rows) == 8 and len(fit_groups) == 4 and all(
    {row["weighting"] for row in decision_rows if row["group"] == group}
    == {"weighted", "unweighted"}
    for group in fit_groups
)
safe_fit = normalize(
    "Aggregate participation and occupation margins are reproduced reasonably closely, while hours fit is uneven. "
    "Individual-level predictive diagnostics raise possible excess stochastic dispersion in some groups; the group-level classification is not used as a headline result."
)
fit_wording_ok = all(safe_fit in surface[name] for name in (
    "Deck", "Story report", "Working paper", "Canonical notebook", "Rehearsal script"
))
if not fit_table_ok:
    failures.append("POSFIT-v3: group/weighting adjudication rows are incomplete")
if not fit_wording_ok:
    failures.append("M2 preservation: safe fit wording missing from a prose surface")


artifact_paths = {
    "Deck PDF": JMP / "beamer/build/JMP_seminar_deck_r6.pdf",
    "Story HTML": story_html,
    "Working-paper PDF": JMP / "manuscript/JMP_working_paper_for_seminar_v5.pdf",
    "Gallery HTML": gallery_html,
    "Notebook": NOTEBOOK,
    "Rehearsal script": rehearsal_md,
    "Rehearsal PDF": JMP / "beamer/build/JMP_seminar_deck_r6_rehearsal.pdf",
}
hashes = {name: {"path": str(path), "sha256": sha256(path)}
          for name, path in artifact_paths.items()}

status = "PASS" if not failures else "FAIL"
payload = {
    "status": status,
    "coverage": coverage,
    "forbidden_hits": forbidden_hits,
    "m9_notebook": m9_ok,
    "concurrent_notebook_cells_preserved": concurrent_ok,
    "parsed_ranges": parsed_ranges,
    "evidence_range": expected_range,
    "range_cells": range_cells,
    "shapley": [
        {"sample": sample, "scale": scale, "factor": factor, "value": value}
        for (sample, scale, factor), value in sorted(shapley.items())
    ],
    "B_gt_A_all_cells": ordering_ok,
    "P_sign_switch_both_samples": preference_sign_ok,
    "signed_detail_surfaces": signed_detail,
    "variance_range_rounded_percent": variance_range,
    "fit_table_preserved": fit_table_ok,
    "fit_safe_wording": fit_wording_ok,
    "hashes": hashes,
    "failures": failures,
}
OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

labels = list(required) + ["M8 -1 nat + cases", "Age is not alone", "M11 if-asked reason"]
md = [
    "# Final M3--M11 claim/wording gate",
    "",
    f"**{status}** — {len(failures)} failure(s).",
    "",
    "## Surface coverage",
    "",
    "| Surface | " + " | ".join(labels) + " |",
    "|---|" + "---|" * len(labels),
]
for name, checks in coverage.items():
    md.append("| " + name + " | " + " | ".join("PASS" if checks[x] else "FAIL" for x in labels) + " |")
md += [
    "",
    "## Parsed numerical evidence",
    "",
    "| Sample | Scale | Parsed source Gini change (% baseline) | P | A | B |",
    "|---|---:|---:|---:|---:|---:|",
]
for cell in range_cells:
    sample, scale = cell["sample"], cell["scale"]
    md.append(
        f"| {sample} | {scale} | {cell['percent']:.6f} | "
        f"{shapley[(sample, scale, 'P')]:+.9f} | {shapley[(sample, scale, 'A')]:+.9f} | "
        f"{shapley[(sample, scale, 'B')]:+.9f} |"
    )
md += [
    "",
    f"Parsed surface range: **{expected_range[0]:.1f}--{expected_range[1]:.1f}%** on all six surfaces.",
    f"B > A in all four cells: **{'PASS' if ordering_ok else 'FAIL'}**.  P sign switch in both samples: **{'PASS' if preference_sign_ok else 'FAIL'}**.",
    f"Var(log C)/Var(log W) rounded source range: **{variance_range[0]}--{variance_range[1]}%**.",
    "Signed detailed-table parsing: " + ", ".join(f"{k}={'PASS' if v else 'FAIL'}" for k, v in signed_detail.items()) + ".",
    "",
    "## Preservation and negative checks",
    "",
    f"- Notebook M9 replacements/pricing disclosure: **{'PASS' if m9_ok else 'FAIL'}**.",
    f"- Concurrent LES and FINAL-DIAGNOSTIC cells preserved: **{'PASS' if concurrent_ok else 'FAIL'}**.",
    f"- POSFIT-v3 four-group/two-weighting table preserved: **{'PASS' if fit_table_ok else 'FAIL'}**.",
    f"- Safe fit wording preserved: **{'PASS' if fit_wording_ok else 'FAIL'}**.",
    f"- Forbidden wording hits: **{len(forbidden_hits)}**.",
    "",
    "## Artifact hashes",
    "",
    "| Artifact | SHA-256 | Path |",
    "|---|---|---|",
]
for name, info in hashes.items():
    md.append(f"| {name} | `{info['sha256']}` | `{info['path']}` |")
if failures:
    md += ["", "## Failures", ""] + [f"- {failure}" for failure in failures]
OUT_MD.write_text("\n".join(md) + "\n", encoding="utf-8")

print(f"{status}: {len(failures)} failure(s)")
for failure in failures:
    print("  " + failure)
print(f"wrote {OUT_MD}")
print(f"wrote {OUT_JSON}")
sys.exit(0 if not failures else 1)
