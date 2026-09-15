"""Build the V18 rehearsal pack from the compiled V18 deck and its notes.

Same method as build_rehearsal_script_v16.py: "On slide" is the projected page,
"Say" is the frame's note with number macros expanded from deck_numbers_v18.tex.
Writes reports/rehearsal_pack_v18.md and refreshes reports/rehearsal_pack_v1.md
(the stable rehearsal-script path) to the V18 numbering: main slides are
numbered as on the footline (the title slide is unnumbered), backup slides as
B1, B2, ...  Refuses to write if an internal label from the verifier's V18
list appears in the pack.
"""
from pathlib import Path
import re
import sys

import pymupdf
import pypandoc

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import verify_deck_r6 as gates  # noqa: E402

source = (HERE / "JMP_seminar_beamer_v18.tex").read_text(encoding="utf-8")
numbers = (HERE / "deck_numbers_v18.tex").read_text(encoding="utf-8")
macros = {name: value.replace("$-$", "\u2212")
          for name, value in re.findall(r"\\newcommand\{\\(\w+)\}\{(.*)\}", numbers)}


def expand(text: str) -> str:
    for name, value in sorted(macros.items(), key=lambda item: -len(item[0])):
        text = re.sub(r"\\" + re.escape(name) + r"(\{\})?(?![A-Za-z])", lambda _: value, text)
    return text


def spoken(latex: str) -> str:
    paragraphs = [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", latex)]
    return "\n\n".join(pypandoc.convert_text(expand(p), "markdown", format="latex",
                                             extra_args=["--wrap=none"]).strip()
                       for p in paragraphs if p)


main_src = gates.split_appendix(source)[0]
frames = re.findall(r"\\begin\{frame\}.*?\\end\{frame\}", source, re.S)
n_main = len(re.findall(r"\\begin\{frame\}", main_src))
document = pymupdf.open(HERE / "build/JMP_seminar_beamer_v18.pdf")
if len(frames) != len(document):
    raise SystemExit(f"frame/page mismatch: {len(frames)} vs {len(document)}")

out = [
    "# Seminar rehearsal script — V18", "",
    f"{n_main} main slides (the title slide plus {n_main - 1} numbered slides) and "
    f"{len(frames) - n_main} backup slides after the conclusion. Slide numbers match the "
    "footline of JMP_seminar_beamer_v18.pdf; the title slide is unnumbered.", "",
    "EA is presented first, as the prospect perspective; ATT is the attained-outcome "
    "benchmark. That is an order of presentation: neither perspective is designated primary.",
    "",
]
for index, (frame, page) in enumerate(zip(frames, document), 1):
    if index == n_main + 1:
        out += ["# Backup", ""]
    title = re.search(r"\\frametitle\{(.*?)\}", frame)
    title = title.group(1) if title else "Title"
    label = ("Title slide" if index == 1 else f"Slide {index - 1}" if index <= n_main
             else f"Backup B{index - n_main}")
    projected = re.sub(r"\s+", " ", page.get_text()).strip()
    projected = re.sub(r"[\x00-\x1f\x7f-\x9f]", "", projected)
    note = re.search(r"\\note\{(.*?)\}\s*\\end\{frame\}", frame, re.S)
    if not note:
        raise SystemExit("missing note on frame " + str(index))
    out += [f"## {label} — {title}", "", "On slide: " + projected, "",
            "Say:", "", spoken(note[1]), ""]

qa = [
    ("Is the ex-ante measure your preferred welfare measure?",
     r"No. The two measures answer different welfare questions: prospects versus attained "
     r"outcomes. EA is shown first because this talk is about opportunities. Choosing "
     r"between them is a substantive normative decision that the paper does not make."),
    ("Are these causal shares of inequality due to unequal opportunities?",
     r"No. They are restricted structural accounting shares. Household resources, needs "
     r"and composition are held fixed, access is local access rather than total "
     r"opportunity, identification rests on maintained restrictions, and parameter "
     r"uncertainty has not been propagated."),
    ("How does the compensation-responsibility conflict connect to the estimates?",
     r"No measure satisfies full compensation and full responsibility, so any welfare "
     r"comparison takes a position on what to compensate. Taking that position empirically "
     r"requires separating preferences from opportunities, which is what the latent-jobs "
     r"model does. The preference channel is still not equated with responsibility."),
    ("Why does equivalisation matter so much for couples under EA?",
     r"Dividing by the modified-OECD scale moves the ex-ante access-plus-earnings share "
     r"from \VEACoupOppRaw{}\% to \VEACoupOppEq{}\% of baseline inequality and moves the "
     r"preference contribution from \VEACoupPrefRaw{} to \VEACoupPrefEq{} Gini points. "
     r"Both scales are reported and no directional claim about preferences is made."),
    ("Why do single adults reverse and couples not?",
     r"It is not tested. One reading is that a single adult's participation depends on one "
     r"earner's access, while a couple's joint budget and second earner leave earning "
     r"opportunities in front. The reversal is a finding for single-adult households only."),
]
out += ["# Extended Q&A", ""]
for question, answer in qa:
    out += [f"## {question}", "", spoken(answer), ""]
out += ["<!-- Generated by beamer/build_rehearsal_script_v18.py from "
        "beamer/JMP_seminar_beamer_v18.tex and build/JMP_seminar_beamer_v18.pdf. -->", ""]
payload = "\n".join(out)

hits = []
for pattern, case_sensitive in gates.V16_INTERNAL + gates.V18_PROFILE["extra_labels"]:
    for found in re.finditer(pattern, payload, 0 if case_sensitive else re.I):
        context = payload[max(0, found.start() - 400):found.end() + 200]
        if "JMP_seminar_beamer_v18" in context or "rehearsal_script_v18" in context:
            continue                        # the file names in the header and footer
        hits.append(found.group(0))
if hits:
    raise SystemExit("REFUSED: internal labels in rehearsal pack: " + ", ".join(sorted(set(hits))))

for target in (ROOT / "reports/rehearsal_pack_v18.md", ROOT / "reports/rehearsal_pack_v1.md"):
    target.write_text(payload, encoding="utf-8", newline="\n")
print(f"Rehearsal script: {n_main} main + {len(frames) - n_main} backup -> "
      "reports/rehearsal_pack_v18.md and rehearsal_pack_v1.md")
