"""Build the V9 rehearsal script from the compiled R9 deck."""
from __future__ import annotations

from pathlib import Path
import re

import pymupdf
import pypandoc


ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / "beamer/JMP_seminar_deck_r9.tex").read_text(encoding="utf-8")
numbers = (ROOT / "beamer/deck_numbers_r9.tex").read_text(encoding="utf-8")
macros = dict(re.findall(r"\\newcommand\{\\(\w+)\}\{([^{}]*)\}", numbers + source))
macros.update(Wone="W^1", S=r"\S")


def expand(text: str) -> str:
    for name, value in sorted(macros.items(), key=lambda item: -len(item[0])):
        text = re.sub(r"\\" + re.escape(name) + r"\b", lambda _: value, text)
    return text


def reader_note(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"^Q\\&A note --- .*?\. ", "", text)
    replacements = (
        ("POSFIT v3b", "the corrected predictive diagnostics"),
        ("DECOMP-2", "the preliminary restricted decomposition"),
        ("Mapping-F", "the attained-bundle measure"),
        ("criterion-A", "sampled-alternative"),
        ("S11", "the preferred specification"),
        ("R7 forbids", "the analysis does not permit"),
        ("R9", "the current presentation"),
    )
    for old, new in replacements:
        text = text.replace(old, new)
    text = re.sub(r"(?:MNL )?commit\s+`?[0-9a-f]{7,40}`?[,;]?", "", text)
    text = re.sub(r"\b(?:JMP|MNL)[A-Za-z0-9_./\\-]*\.(?:md|csv|json|py)",
                  "the source analysis", text)
    return text


frames = re.findall(r"\\begin\{frame\}.*?\\end\{frame\}", source, re.S)
main_count = len(re.findall(r"\\begin\{frame\}", source.split(r"\appendix", 1)[0]))
document = pymupdf.open(ROOT / "beamer/build/JMP_seminar_deck_r9.pdf")
section_titles = {re.sub(r"\s+", " ", value).strip()
                  for value in re.findall(r"\\section\{([^}]+)\}", source)}
section_titles = {value.replace(r"$\Wone$", "W 1") for value in section_titles}
pages = [page for page in document
         if re.sub(r"\s+", " ", page.get_text()).strip() not in section_titles]
if len(frames) != len(pages):
    raise SystemExit(f"frame/page mismatch: {len(frames)} vs {len(pages)}")

out = [
    "# Unequal Job Opportunities and Well-Being Inequality: A Latent-Jobs Structural Decomposition",
    "",
    "## Seminar rehearsal script — V9",
    "",
    f"The main presentation contains {main_count} slides. The remaining "
    f"{len(frames)-main_count} slides are backup material.",
    "",
    "## Main presentation",
    "",
]
for index, (frame, page) in enumerate(zip(frames, pages), 1):
    if index == main_count + 1:
        out += ["## Backup / appendix", ""]
    projected = re.sub(r"\s+", " ", page.get_text()).strip()
    projected = re.sub(r"[\x00-\x1f\x7f-\x9f]", "", projected)
    note = re.search(r"\\note\{(.*?)\}\s*\\end\{frame\}", frame, re.S)
    if not note:
        raise SystemExit("missing note on frame " + str(index))
    spoken = pypandoc.convert_text(
        expand(reader_note(note.group(1))),
        "markdown",
        format="latex",
        extra_args=["--wrap=none"],
    ).strip()
    title = (f"### Slide {index}" if index <= main_count
             else f"### Backup slide {index-main_count}")
    out += [title, "", "On slide: " + projected, "", "Say: " + spoken, ""]

out += [r'''## Extended Q&A

### What are the two welfare perspectives?

The attained-bundle measure asks what the realised job is worth against the
universally available non-employment state. The ex-ante measure asks what the
whole job prospect is worth by finding the common consumption across that
prospect that produces indifference. Neither is designated primary.

### Why do they disagree about the dominant channel?

The ex-ante measure values the whole prospect, so reachability matters directly.
The attained-bundle measure sees only the realised job, where wages drive
disposable consumption. Earning opportunities dominate the attained-bundle
accounting. For single-adult households, access is about three times earning
opportunities in the ex-ante accounting. Earnings remain larger for couples.

### What are the ex-ante magnitudes?

Access plus earning opportunities accounts for 14.8% of baseline ex-ante
inequality for single adults on the raw-household basis and 20.3% after
equivalisation. For couples the corresponding figures are 21.3% and 7.9%.
These are restricted accounting shares, not total or causal opportunity shares.

### Why is the couples scale result flagged?

Equivalisation moves the couples ex-ante access-plus-earnings share from 21.3%
to 7.9% and turns the preference contribution negative. The scale convention
is materially consequential, so no directional claim about preferences is
made.

### Are the ex-ante results numerically certified?

Yes. All twelve declared checks pass for both household types, including
reference-integral accuracy, effective sample size, wage-tail control, two-seed
stability, analytical identities, Shapley closure and an independent
implementation. That certifies the calculation, not the model's maintained
economic assumptions or a causal interpretation.

### How should the earlier figures near 90% be understood?

They described all non-preference circumstances, including household resources
and composition, not job opportunities. They are not comparable with the
restricted access-and-earnings figures in the current results.

### What remains preliminary?

The attained-bundle counterfactual is still subject to ongoing numerical
validation, especially because its finite integration sample sparsely covers
short hours. Both decompositions hold resources, needs and composition fixed;
neither propagates parameter uncertainty.
'''.strip(), ""]

payload = "\n".join(out)
target = ROOT / "reports/rehearsal_pack_v9.md"
target.write_text(payload, encoding="utf-8", newline="\n")
print(f"Rehearsal script: {main_count} main + {len(frames)-main_count} backup slides.")
