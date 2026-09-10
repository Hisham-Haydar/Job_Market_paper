# v5 section split verification

Verified on 10 September 2026 against the 1,370-line working source and the existing 34-page PDF captured before this split. The source already contained staged and unstaged author edits; the identity baseline is that current working source, not HEAD. Those edits are preserved in the split source. Unrelated staged and unstaged files are excluded from this commit.

## Layout

The master is 61 lines. Original lines 1-39 remain verbatim: the short preamble is lines 1-31, followed by the document opening and front matter. No separate preamble file is needed. All section and subsection boundaries were checked against the actual commands. The results section's six files are input directly, with the section heading in 05a; no 05_results wrapper is created. The original appendix command and following blank line remain in the master immediately before the appendix inputs. Bibliography commands and the document ending remain in the master.

See [SECTION_MAP.md](SECTION_MAP.md) for every source file, line count, original range, and all 35 labels, and [sections/README.md](sections/README.md) for the editing map. Figure/table files and the bibliography remain where they were.

## Byte identity: PASS

Binary equality comparisons were performed against the captured original, without decoding, newline normalization, or whitespace stripping:

| Comparison | Original bytes | Reassembled bytes | Result | SHA-256 of both |
| --- | ---: | ---: | --- | --- |
| Section files concatenated in master input order | 128250 | 128250 | Exactly equal | `aa6ee29c8c0b331ef9ea299240a28b7736fc87b6205493d4184cab32d17a08a6` |
| Entire master with input lines replaced by section bytes | 131850 | 131850 | Exactly equal | `bc647257f5519a5fec13b7c9194cb623f183663418377fd6f2ed9d2926a2adc2` |

The concatenated section-body baseline is original lines 40-1161 followed by 1164-1367. The appendix switch (1162-1163) is deliberately retained in the master and is included in the full-source comparison. Every original CRLF and blank line is preserved.

Recheck the recorded hashes from the repository root with Python (the optional snapshot comparisons also run when the local verification directory is present):

```python
from pathlib import Path
import hashlib, re
m = Path("manuscript")
master = (m / "JMP_working_paper_for_seminar_v5.tex").read_bytes()
pattern = rb"^\\input\{(sections/[^}]+)\}\r\n"
parts = [(m / (x[1].decode() + ".tex")).read_bytes()
         for x in re.finditer(pattern, master, re.M)]
body = b"".join(parts)
expanded = re.sub(pattern, lambda x: (m / (x[1].decode() + ".tex")).read_bytes(),
                  master, flags=re.M)
assert len(parts) == 17
assert len(body) == 128250
assert hashlib.sha256(body).hexdigest() == "aa6ee29c8c0b331ef9ea299240a28b7736fc87b6205493d4184cab32d17a08a6"
assert len(expanded) == 131850
assert hashlib.sha256(expanded).hexdigest() == "bc647257f5519a5fec13b7c9194cb623f183663418377fd6f2ed9d2926a2adc2"
snapshot = Path(".git/v5-section-split-verification/original.tex")
if snapshot.exists():
    original = snapshot.read_bytes()
    lines = original.splitlines(keepends=True)
    assert expanded == original
    assert body == b"".join(lines[39:1161] + lines[1163:1367])
print("PASS: section body and full expanded source match the original bytes")
```

## Compilation and PDF comparison: PASS

MiKTeX pdfTeX 1.40.28 and latexmk 4.88 were used. Both the original source and the split master completed latexmk with exit status 0, zero TeX errors, and no undefined citations or references. The existing tracked PDF and build products were left intact.

From `manuscript`, the split build command was:

```powershell
$env:PATH = 'C:\Users\hisham\AppData\Local\Programs\MiKTeX\miktex\bin\x64;C:\Program Files\Git\usr\bin;' + $env:PATH
$env:BIBINPUTS = 'C:/Users/hisham/Repo/Job_Market_paper/manuscript;'
latexmk -pdf -interaction=nonstopmode -halt-on-error '-outdir=../.git/v5-section-split-verification/split' JMP_working_paper_for_seminar_v5.tex
```

`BIBINPUTS` points to the unchanged bibliography location because verification output is outside the manuscript directory. The initial baseline attempt without that search path failed to locate the bibliography; after setting it, both complete builds passed. MiKTeX printed its update-check reminder, which is not a compilation error.

| Check | Existing PDF | Unsplit rebuild | Split rebuild |
| --- | ---: | ---: | ---: |
| Pages | 34 | 34 | 34 |
| Label records | 35 | 35 | 35 |
| Section/subsection records | 35 | 35 | 35 |
| Figure records | 13 | 13 | 13 |
| Table records | 21 | 21 | 21 |

All 104 `\newlabel` and `\@writefile{toc/lof/lot}` records match exactly, including numbering, captions/headings, destinations, and page numbers. `pdftotext -layout` output also matches byte for byte across all three PDFs; SHA-256: `9209c9a513c118033c9de136756095f7c0b38a9d1d10cb457dd8fc56814a9111`. PDF binary identity is not asserted because build metadata can change.

Local snapshots, build logs, PDFs, extracted text, numbering records, and per-section hashes are retained in `.git/v5-section-split-verification/` (not committed).
