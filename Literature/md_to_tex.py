#!/usr/bin/env python3
"""Convert Literature_collection.md to a compilable LaTeX file."""

import re

INPUT  = r"C:\Users\hisham\Desktop\Job_Market_paper\Literature\Literature_collection.md"
OUTPUT = r"C:\Users\hisham\Desktop\Job_Market_paper\Literature\Literature_collection.tex"

# ── character-level escaping ──────────────────────────────────────────────────

_ESC_TABLE = [
    ("\\", "\x01BSLASH\x01"),   # placeholder first so later replacements don't hit it
    ("&",  r"\&"),
    ("%",  r"\%"),
    ("#",  r"\#"),
    ("_",  r"\_"),
    ("{",  r"\{"),
    ("}",  r"\}"),
    ("~",  r"\textasciitilde{}"),
    ("^",  r"\textasciicircum{}"),
    ("\x01BSLASH\x01", r"\textbackslash{}"),
]

def tex_escape(s: str) -> str:
    """Escape LaTeX special characters in plain text (not math, not commands)."""
    for old, new in _ESC_TABLE:
        s = s.replace(old, new)
    return s


# ── inline markup pipeline ────────────────────────────────────────────────────
# Strategy: pull out math spans first (preserve verbatim), then escape the rest,
# then apply bold/italic/code/url substitutions (which emit raw LaTeX).

PLACEHOLDER_RE = re.compile(r'\x02(\d+)\x03')

def process_inline(text: str) -> str:
    """
    Convert one line of Markdown inline markup to LaTeX.
    Processing order:
      1. Extract math ($...$ and $$...$$) into placeholders.
      2. Extract markdown links into placeholders (to avoid escaping their content twice).
      3. tex_escape the remainder.
      4. Restore link and math placeholders.
      5. Apply **bold** and *italic* and `code`.
    """
    store = []

    def stash(s):
        idx = len(store)
        store.append(s)
        return f"\x02{idx}\x03"

    # 1a. $$...$$ display-inline
    def grab_display(m):
        inner = m.group(1).strip()
        return stash(f"${inner}$")   # keep as inline math for now
    text = re.sub(r'\$\$(.+?)\$\$', grab_display, text, flags=re.DOTALL)

    # 1b. $...$ inline math
    def grab_math(m):
        return stash(m.group(0))
    text = re.sub(r'\$[^$\n]+?\$', grab_math, text)

    # 2. Markdown links [label](url)
    def grab_link(m):
        label_raw = m.group(1)
        url       = m.group(2)
        if url.startswith("#"):
            # internal anchor → just the label text (escaped below)
            return stash("\x04" + label_raw + "\x04")   # \x04 = "escape this label"
        else:
            # external URL → \href{url}{label}
            safe_url = url.replace("%", "\\%")
            # label will be escaped when we restore
            return stash("\x05" + safe_url + "\x05" + label_raw + "\x06")
    text = re.sub(r'\[([^\]]*)\]\(([^)]*)\)', grab_link, text)

    # 3. Escape LaTeX special chars in the remaining text
    text = tex_escape(text)

    # 4. Restore placeholders
    def restore(m):
        val = store[int(m.group(1))]
        if val.startswith("\x04"):          # internal link → plain escaped label
            label = val[1:-1]              # strip \x04 markers
            return tex_escape(label)
        elif val.startswith("\x05"):        # external href
            rest = val[1:]
            url_end = rest.index("\x05")
            url   = rest[:url_end]
            label = rest[url_end+1:-1]     # strip trailing \x06
            return r"\href{" + url + r"}{" + tex_escape(label) + r"}"
        else:
            return val                     # math — verbatim
    text = PLACEHOLDER_RE.sub(restore, text)

    # 5. Bold / italic / inline code  (these patterns survive escaping)
    text = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', text)
    text = re.sub(r'\*(.+?)\*',     r'\\textit{\1}', text)
    text = re.sub(r'`([^`]+)`',     lambda m: r'\texttt{' + tex_escape(m.group(1)) + r'}', text)

    return text


# ── preamble ──────────────────────────────────────────────────────────────────

PREAMBLE = r"""\documentclass[11pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage[margin=2.5cm]{geometry}
\usepackage{hyperref}
\hypersetup{
    colorlinks  = true,
    linkcolor   = blue!60!black,
    urlcolor    = blue!60!black,
    citecolor   = blue!60!black,
    pdftitle    = {Literature Collection},
    pdfauthor   = {},
    bookmarksopen    = true,
    bookmarksnumbered = true,
}
\usepackage{amsmath,amssymb}
\usepackage{booktabs}
\usepackage{enumitem}
\usepackage{microtype}
\usepackage{parskip}
\usepackage{titlesec}
\usepackage{xcolor}

% Section heading styles
\titleformat{\section}
  {\large\bfseries\color{blue!70!black}}{}{0em}{}[\titlerule]
\titleformat{\subsection}{\normalsize\bfseries}{}{0em}{}
\titleformat{\subsubsection}{\normalsize\itshape}{}{0em}{}

\setlist[itemize]{noitemsep,topsep=2pt,leftmargin=1.5em}
\setlist[enumerate]{noitemsep,topsep=2pt,leftmargin=1.5em}

\begin{document}

\begin{center}
  {\LARGE\bfseries Literature Collection}\\[6pt]
  {\small Generated from synthesised paper extracts\quad\textbar\quad
         Grouped by paper\quad\textbar\quad
         Sorted alphabetically by first author family name}
\end{center}
\vspace{1em}\hrule\vspace{1em}

"""

POSTAMBLE = "\n\\end{document}\n"


# ── block-level converter ─────────────────────────────────────────────────────

def convert(lines: list[str]) -> str:
    out      = []
    in_list  = False   # itemize
    in_enum  = False   # enumerate

    def close_lists():
        nonlocal in_list, in_enum
        if in_list:
            out.append(r"\end{itemize}")
            in_list = False
        if in_enum:
            out.append(r"\end{enumerate}")
            in_enum = False

    i = 0
    while i < len(lines):
        line = lines[i].rstrip("\n")

        # ── skip the YAML block (already stripped in main) ─────────────────
        # ── display math  $$\n...\n$$ ──────────────────────────────────────
        stripped = line.strip()
        if stripped == "$$":
            close_lists()
            math_inner = []
            i += 1
            while i < len(lines):
                l = lines[i].rstrip("\n").strip()
                if l == "$$":
                    i += 1
                    break
                math_inner.append(l)
                i += 1
            out.append(r"\[")
            out.extend(math_inner)
            out.append(r"\]")
            continue

        # inline $$...$$  (whole line)
        if stripped.startswith("$$") and stripped.endswith("$$") and len(stripped) > 4:
            close_lists()
            inner = stripped[2:-2].strip()
            out.append(r"\[" + inner + r"\]")
            i += 1
            continue

        # ── fenced code block ───────────────────────────────────────────────
        if stripped.startswith("```"):
            close_lists()
            out.append(r"\begin{verbatim}")
            i += 1
            while i < len(lines):
                l = lines[i].rstrip("\n")
                if l.strip().startswith("```"):
                    i += 1
                    break
                out.append(l)
                i += 1
            out.append(r"\end{verbatim}")
            continue

        # ── horizontal rule ─────────────────────────────────────────────────
        if re.match(r'^[-=]{3,}$', stripped):
            close_lists()
            out.append(r"\medskip\hrule\medskip")
            i += 1
            continue

        # ── headings ────────────────────────────────────────────────────────
        m = re.match(r'^(#{1,4})\s+(.*)', line)
        if m:
            close_lists()
            level = len(m.group(1))
            title = process_inline(m.group(2))
            cmd = {1: r"\section*",
                   2: r"\section*",
                   3: r"\subsection*",
                   4: r"\subsubsection*"}.get(level, r"\paragraph")
            # suppress the duplicate top-level "# Literature Collection" heading
            # (already in \begin{document} title block)
            if level == 1 and "Literature Collection" in m.group(2):
                i += 1
                continue
            out.append(f"{cmd}{{{title}}}")
            i += 1
            continue

        # ── bullet list item ─────────────────────────────────────────────────
        m = re.match(r'^(\s*)[-*]\s+(.*)', line)
        if m:
            if in_enum:
                out.append(r"\end{enumerate}")
                in_enum = False
            if not in_list:
                out.append(r"\begin{itemize}")
                in_list = True
            out.append(r"  \item " + process_inline(m.group(2)))
            i += 1
            continue

        # ── numbered list item ───────────────────────────────────────────────
        m = re.match(r'^\s*(\d+)\.\s+(.*)', line)
        if m:
            if in_list:
                out.append(r"\end{itemize}")
                in_list = False
            if not in_enum:
                out.append(r"\begin{enumerate}")
                in_enum = True
            out.append(r"  \item " + process_inline(m.group(2)))
            i += 1
            continue

        # ── blank line ───────────────────────────────────────────────────────
        if stripped == "":
            close_lists()
            out.append("")
            i += 1
            continue

        # ── plain paragraph line ─────────────────────────────────────────────
        close_lists()
        out.append(process_inline(line))
        i += 1

    close_lists()
    return "\n".join(out)


# ── entry point ───────────────────────────────────────────────────────────────

def main():
    with open(INPUT, encoding="utf-8") as f:
        raw = f.read()

    # Strip YAML front matter
    raw = re.sub(r'^---\n.*?\n---\n', '', raw, flags=re.DOTALL)

    lines = raw.splitlines(keepends=True)
    body  = convert(lines)
    tex   = PREAMBLE + body + POSTAMBLE

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(tex)

    print(f"Done. Written {len(tex):,} chars to:\n  {OUTPUT}")


if __name__ == "__main__":
    main()
