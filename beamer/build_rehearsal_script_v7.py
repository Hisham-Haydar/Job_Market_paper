"""Build the v7 rehearsal pack from the compiled R7 deck and corrected records."""
from pathlib import Path
import re

import pymupdf
import pypandoc


ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / "beamer/JMP_seminar_deck_r7.tex").read_text(encoding="utf-8")
numbers = (ROOT / "beamer/deck_numbers_r7.tex").read_text(encoding="utf-8")
macros = dict(re.findall(r"\\newcommand\{\\(\w+)\}\{([^{}]*)\}", numbers + source))
macros.update(Wone="W^1", S=r"\S")


def expand(text):
    for name, value in sorted(macros.items(), key=lambda item: -len(item[0])):
        text = re.sub(r"\\" + re.escape(name) + r"\b", lambda _: value, text)
    return text


def reader_note(text):
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"^Q\\&A note --- .*?\. ", "", text)
    replacements = (
        ("POSFIT v3b", "the corrected individual-level predictive diagnostics"),
        ("DECOMP-2", "the preliminary restricted decomposition"),
        ("Mapping-F", "the attained-bundle Mapping-F measure"),
        ("criterion-A", "sampled-alternative"),
        ("S11", "the current specification"),
        ("R7 forbids", "the analysis does not permit"),
    )
    for old, new in replacements:
        text = text.replace(old, new)
    text = re.sub(r"(?:MNL )?commit\s+`?[0-9a-f]{7,40}`?[,;]?", "", text)
    text = re.sub(r"\b(?:JMP|MNL)[A-Za-z0-9_./\\-]*\.(?:md|csv|json|py)",
                  "the source analysis", text)
    return text


frames = re.findall(r"\\begin\{frame\}.*?\\end\{frame\}", source, re.S)
main_count = len(re.findall(r"\\begin\{frame\}", source.split(r"\appendix", 1)[0]))
document = pymupdf.open(ROOT / "beamer/build/JMP_seminar_deck_r7.pdf")
section_titles = {re.sub(r"\s+", " ", value).strip()
                  for value in re.findall(r"\\section\{([^}]+)\}", source)}
section_titles = {value.replace(r"$\Wone$", "W 1") for value in section_titles}
pages = [page for page in document
         if re.sub(r"\s+", " ", page.get_text()).strip() not in section_titles]
if len(frames) != len(pages):
    raise SystemExit(f"frame/page mismatch: {len(frames)} vs {len(pages)}")

out = [
    "# Seminar rehearsal script — v7", "",
    f"The main presentation contains {main_count} slides. The remaining "
    f"{len(frames)-main_count} slides are backup material.", "",
    "## Main presentation", "",
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
        expand(reader_note(note[1])), "markdown", format="latex",
        extra_args=["--wrap=none"]).strip()
    title = (f"### Slide {index}" if index <= main_count
             else f"### Backup slide {index-main_count}")
    out += [title, "", "On slide: " + projected, "", "Say: " + spoken, ""]

out += [r'''## Extended Q&A

### What changed in the predictive evaluation?

The current estimates were fully re-evaluated on an explicit current-model
view of the same priced nodes. Hours, occupations, wages, consumption,
proposal columns and node geometry are unchanged; the structural indicator
columns use the current-model band definitions. This is a cross-specification
evaluation correction, not a relabelling exercise and not a re-estimation.

### What are the four corrected adjudications?

Single women and coupled women clear the weighted extensive-accuracy
numerical-adequacy gate. Single men and coupled men are quadrature-limited, so
their extensive accuracy is withheld. The conditioning adjudication is
mechanical stochastic conditioning in all four groups. The excess-dispersion
adjudication is misspecification evidence for coupled men and coupled women,
and inconclusive/quadrature-limited for single men and single women. The
earlier three-group excess-predictability claim is withdrawn.

### What happened to population fit?

The corrected population-moment MAE is 0.0140 for singles and 0.0119 for
couples. Singles MAE rises slightly, so the correction is not presented as an
across-the-board improvement. The remaining common mismatch is
**underprediction of the observed 37-hour mass point**: 5.2 percentage points
for single men, 3.8 for single women, 4.4 for coupled men and 6.5 for coupled
women. That point is outside the structural FT band [37.5, 40.5].

### What is the current welfare measure?

The empirical Mapping-F implementation evaluates the attained bundle against
the universally available non-employment reference. Under the current
specification, estimated opportunity density therefore affects this money
metric through attained outcomes rather than through a direct
opportunity-prospect term.

### Is the ex-ante opportunity-prospect metric a result?

No. W_EA_flat is definition-only and numerically blocked. Under the primary
full-environment domain, non-positive-consumption states contribute zero to the
actual functional through the limiting rule and remain in the flat reference
with common consumption. No one-euro floor, observed-consumption substitution
or silent household deletion is permitted. The 260 couples lacking a priced
NN state remain a blocker. Exact-H pre-validation is the first post-seminar
numerical task, before any pricing design is launched.

### How should the decomposition magnitude be read?

The restricted P/A/B game changes baseline Gini by 1.8–9.9%, depending on
population and reporting scale. This percentage is the change generated by the
declared restricted P/A/B game. It is not an estimate of the total fraction of
inequality caused by unequal job opportunities. Earning opportunities have a
larger Shapley contribution than coarse geographic/temporal access; the
preference sign changes under equivalisation. Closure is exact, the second seed
reproduces the result and anchor exclusion moves the change by at most 0.8%
without a sign flip.

### What is the short-hours limitation?

The preliminary attainment exercise is evaluated on the already-priced
estimation panel. That panel sparsely represents the lower part of the
structural hours support. A separate integration audit shows substantial
structural mass in that region. The direct importance of this limitation for
the current attained-bundle decomposition has not been fully quantified, so
the result remains explicitly preliminary.

### What is the RUM-A/B input limitation?

RUM-A encoded a native-panel hours-density width in one estimation input. The
resulting alternative-invariant log-density shift cancels from the conditional
likelihood, so estimates, standard errors and the criterion comparison are
unchanged. RUM-B does not read those rows. Absolute RUM-A opportunity-mass
metadata remain a disclosed limitation; the corrected benchmark population-fit
MAEs are 0.0273 and 0.0264.
'''.strip(), ""]

provenance = re.search(
    r"% BEGIN READER-VOICE PROVENANCE(.*?)% END READER-VOICE PROVENANCE",
    source, re.S)[1]
provenance = re.sub(r"^% ?", "", provenance, flags=re.M)
out += ["<!-- BEGIN READER-VOICE PROVENANCE", provenance,
        "Script generator: beamer/build_rehearsal_script_v7.py.",
        "END READER-VOICE PROVENANCE -->", ""]
payload = "\n".join(out)
for target in (ROOT / "reports/rehearsal_pack_v7.md",
               ROOT / "reports/rehearsal_pack_v1.md"):
    target.write_text(payload, encoding="utf-8")
print(f"Rehearsal script: {main_count} main + {len(frames)-main_count} backup slides.")
