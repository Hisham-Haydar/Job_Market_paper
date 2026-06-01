#!/usr/bin/env python3
"""Rebuild Markdown extractions from PDFs with stronger cleanup."""

from __future__ import annotations

import html
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path


BASE_DIR = Path(r"C:\Users\hisham\Desktop\Job_Market_paper\Literature")
OUT_DIR = BASE_DIR / "md_extractions"
PDFTOTEXT = Path(r"C:\Program Files\MiKTeX\miktex\bin\x64\pdftotext.exe")

TOP_EDGE_FRAC = 0.09
BOTTOM_EDGE_FRAC = 0.07

NOISE_SNIPPETS = (
    "this content downloaded from",
    "all use subject to",
    "about.jstor.org/terms",
    "jstor is a not-for-profit service",
    "range of content in a trusted digital archive",
    "for more information about jstor",
    "linked references are available on jstor",
    "published online by cambridge university press",
    "digitize, preserve and extend access",
    "preserve and extend access",
    "collaborating with jstor",
    "terms & conditions of use",
    "support@jstor.org",
    "garsington road, oxford",
    "main street, maiden, ma",
)

INLINE_NOISE_PATTERNS = (
    re.compile(r"Electronic copy available at:\s*https?://ssrn\.com/abstract=\d+(?:\s+\d+)?\s*", re.I),
    re.compile(r"Available at http://qeconomics\.org\.\s*https?://doi\.org/\S+\s*", re.I),
    re.compile(
        r"(?:\b\d{8},\s*\d{4},\s*\d+,\s*)?Downloaded from https://onlinelibrary\.wiley\.com/doi/\S+.*?"
        r"Creative Commons License\s*",
        re.I,
    ),
    re.compile(r"Journal of Economic Surveys\s*\(2009\)\s*Vol\.\s*23,\s*No\.\s*3,\s*pp\.\s*586\S*", re.I),
    re.compile(r"Econometrica,\s*Vol\.\s*70,\s*No\.\s*6\s*\(November,\s*2002\),\s*2455\S*", re.I),
    re.compile(r"\b2455\s+s\.\s*blomquist\s+and\s+w\.\s*newey\b", re.I),
    re.compile(r"\bnonlinear budget sets\s+s\.\s*blomquist\s+and\s+w\.\s*newey\b", re.I),
    re.compile(
        r"[@?]?\s*The Author\(s\)\.?\s*Journal compilation\s*[@?]?\s*Royal Econ\w*(?:\s+Society)?(?:\s+2007\??)?\s*",
        re.I,
    ),
)

MOJIBAKE_REPLACEMENTS = (
    ("ï»¿", ""),
    ("Â©", "©"),
    ("Â®", "®"),
    ("Â±", "±"),
    ("Â§", "§"),
    ("Â°", "°"),
    ("â€“", "–"),
    ("â€”", "—"),
    ("â€˜", "‘"),
    ("â€™", "’"),
    ("â€œ", "“"),
    ("â€", "”"),
    ("â€¢", "•"),
    ("â€¦", "…"),
    ("â‰¤", "≤"),
    ("â‰¥", "≥"),
    ("â‰ ", "≠"),
    ("âˆˆ", "∈"),
    ("âˆ’", "−"),
    ("âˆ—", "∗"),
    ("âŠ‚", "⊂"),
    ("â‰ˆ", "≈"),
    ("â†’", "→"),
    ("â†", "†"),
    ("â€", '"'),
    ("\x03", "ℓ"),
)

METADATA_PREFIXES = (
    "author(s):",
    "source:",
    "published by:",
    "stable url:",
    "doi:",
    "keywords",
    "jel classification",
)

TITLE_STOPWORDS = {
    "a",
    "an",
    "and",
    "as",
    "at",
    "by",
    "for",
    "from",
    "in",
    "of",
    "on",
    "or",
    "the",
    "to",
    "with",
}


@dataclass
class Line:
    text: str
    x_min: float
    x_max: float
    y_min: float
    y_max: float


@dataclass
class Unit:
    text: str
    kind: str


def fix_text(text: str) -> str:
    text = html.unescape(text)
    for bad, good in MOJIBAKE_REPLACEMENTS:
        text = text.replace(bad, good)
    text = "".join(ch for ch in text if ch >= " " or ch in "\n\t")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\s+\n", "\n", text)
    return text.strip()


def clean_unit_text(text: str) -> str:
    text = fix_text(text)
    if not text:
        return ""
    for pattern in INLINE_NOISE_PATTERNS:
        text = pattern.sub(" ", text)
    text = re.sub(r"\b\d{3,4}\s+\d{3,4}\b(?=\s+[A-Za-z])", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"\s+([,.;:!?])", r"\1", text)
    if re.fullmatch(r"\d{4}\]\s+[A-Z][A-Z0-9 ,:&'()/\-]{5,}\s+\d{1,3}", text):
        return ""
    return text


def join_tokens(words: list[str]) -> str:
    out = ""
    no_space_before = {",", ".", ";", ":", "!", "?", "%", ")", "]", "}", "”", "’"}
    no_space_after = {"(", "[", "{", "“", "‘"}
    for raw in words:
        token = fix_text(raw)
        if not token:
            continue
        if not out:
            out = token
            continue
        if token in no_space_before or token.startswith(("’", "'", "n't")):
            out += token
        elif out[-1] in no_space_after or out.endswith("-"):
            out += token
        else:
            out += " " + token
    return out.strip()


def is_heading_text(text: str) -> bool:
    s = text.strip()
    if not s or len(s) > 140:
        return False
    if re.fullmatch(r"Abstract|Summary|References|REFERENCE|REFERENCES|Introduction|Conclusion|Conclusions", s, re.I):
        return True
    if re.fullmatch(r"Appendix(?:\s+[A-Z0-9]+)?", s, re.I):
        return True
    if re.fullmatch(r"CHAPTER\s+\d+", s, re.I):
        return True
    if re.fullmatch(r"[IVXLC]+\.\s+.+", s):
        return True
    if re.fullmatch(r"\d+(?:\.\d+)+\s+.+", s):
        return True
    if s.isupper() and 1 <= len(s.split()) <= 10:
        return True
    return False


def looks_like_title(text: str) -> bool:
    s = text.strip().strip("*")
    if not s or len(s) > 180:
        return False
    if "@" in s:
        return False
    if re.search(r"\b(university|statistics norway|department|po box|research department)\b", s, re.I):
        return False
    if re.search(r"\b\d{4,6}\b", s):
        return False
    if any(s.lower().startswith(prefix) for prefix in METADATA_PREFIXES):
        return False
    if any(bad in s.lower() for bad in ("jstor", "cambridge university press", "stable url", "doi:")):
        return False
    words = re.findall(r"[A-Za-z][A-Za-z'’\-]*", s)
    if len(words) < 5:
        return False
    good = 0
    for word in words:
        if word.lower() in TITLE_STOPWORDS or word[:1].isupper():
            good += 1
    return good / len(words) >= 0.8


def unit_kind(text: str) -> str:
    lower = text.lower()
    if is_heading_text(text):
        return "heading"
    if lower.startswith(METADATA_PREFIXES):
        return "meta"
    if text.startswith("http://") or text.startswith("https://"):
        return "url"
    return "paragraph"


def looks_like_short_running_head(text: str) -> bool:
    words = re.findall(r"[A-Za-z][A-Za-z'’\-]*", text.strip())
    if not (2 <= len(words) <= 4):
        return False
    return all(word[:1].isupper() for word in words)


def is_edge_noise(text: str, y_mid: float, page_height: float, page_no: int) -> bool:
    stripped = text.strip()
    if not stripped:
        return True

    lower = stripped.lower()
    near_edge = y_mid < page_height * TOP_EDGE_FRAC or y_mid > page_height * (1 - BOTTOM_EDGE_FRAC)
    near_top = y_mid < 100
    near_bottom = y_mid > page_height - 60

    if any(snippet in lower for snippet in NOISE_SNIPPETS):
        return True
    if re.match(r"^\d{1,3}(?:\.\d{1,3}){3}\s+on\s+\w{3},", lower):
        return True
    if stripped.startswith("©") or stripped.startswith("Â©"):
        return True
    if "blackwell publishing" in lower:
        return True
    if "scand. j. of economics" in lower and near_top:
        return True
    if stripped == "This" and page_no > 1:
        return True
    if page_no > 1 and near_top and looks_like_short_running_head(stripped):
        return True
    if page_no > 1 and near_top and looks_like_title(stripped) and len(stripped.split()) <= 5:
        return True
    if near_bottom and re.fullmatch(r"\d{1,4}", stripped):
        return True
    if page_no > 1 and near_top and re.fullmatch(r"\d+(?:\.\d+)+\s+[A-Za-z].{0,80}", stripped):
        return True
    if page_no > 1 and near_top and re.fullmatch(r"\d{1,4}\s+[A-Za-z].{0,100}", stripped):
        return True
    if page_no > 1 and near_top and re.fullmatch(r"[A-Za-z][A-Za-z .,'’():;/\-]{2,110}\s+\d(?:\s*\d)*", stripped):
        return True
    if page_no > 1 and near_top and lower.startswith("doi:"):
        return True
    if not near_edge:
        return False
    if re.fullmatch(r"\d{1,4}", stripped):
        return True
    if re.fullmatch(r"[A-Za-z .,'’():;/\-]{2,110}\s+\d{1,4}", stripped):
        return True
    if re.fullmatch(r"\d{1,4}\s+[A-Za-z][A-Za-z .,'’():;/\-]{2,110}", stripped):
        return True
    if stripped.startswith("https://doi.org/"):
        return True
    if stripped.startswith("http://doi.org/"):
        return True
    return False


def parse_bbox_html(pdf_path: Path) -> list[list[Line]]:
    html_path = OUT_DIR / "__bbox_tmp__.html"
    try:
        subprocess.run(
            [str(PDFTOTEXT), "-q", "-bbox-layout", "-enc", "UTF-8", str(pdf_path), str(html_path)],
            check=True,
        )
        raw = html_path.read_text(encoding="utf-8", errors="ignore")
    finally:
        if html_path.exists():
            html_path.unlink()

    raw = raw.replace('xmlns="http://www.w3.org/1999/xhtml"', "")
    raw = re.sub(r"&(?!#?[A-Za-z0-9]+;)", "&amp;", raw)
    raw = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", raw)
    root = ET.fromstring(raw)

    pages: list[list[Line]] = []
    for page_no, page in enumerate(root.findall(".//page"), start=1):
        page_height = float(page.attrib["height"])
        page_lines: list[Line] = []

        for block in page.findall(".//block"):
            for line in block.findall("./line"):
                words = [word.text or "" for word in line.findall("./word")]
                text = join_tokens(words)
                if not text:
                    continue
                x_min = float(line.attrib.get("xMin", block.attrib.get("xMin", "0")))
                x_max = float(line.attrib.get("xMax", block.attrib.get("xMax", "0")))
                y_min = float(line.attrib.get("yMin", block.attrib.get("yMin", "0")))
                y_max = float(line.attrib.get("yMax", block.attrib.get("yMax", "0")))
                y_mid = (y_min + y_max) / 2
                if is_edge_noise(text, y_mid, page_height, page_no):
                    continue
                page_lines.append(Line(text=text, x_min=x_min, x_max=x_max, y_min=y_min, y_max=y_max))

        pages.append(page_lines)
    return pages


def block_gap(prev: Line, curr: Line) -> float:
    return curr.y_min - prev.y_max


def is_same_block(prev: Line, curr: Line) -> bool:
    if abs(curr.x_min - prev.x_min) > 18:
        return False
    if block_gap(prev, curr) > 16:
        return False
    return True


def render_block(lines: list[Line]) -> list[Unit]:
    texts = [line.text for line in lines if line.text]
    if not texts:
        return []

    if any(text.lower().startswith(METADATA_PREFIXES) for text in texts):
        return [Unit(text=text, kind=unit_kind(text)) for text in texts]

    if len(texts) == 1:
        text = texts[0]
        return [Unit(text=text, kind=unit_kind(text))]

    if 2 <= len(texts) <= 4 and all(len(text) <= 70 for text in texts):
        joined = texts[0]
        for text in texts[1:]:
            if joined.endswith("-") and not joined.endswith(" -"):
                joined = joined[:-1] + text
            else:
                joined = f"{joined} {text}"
        joined = re.sub(r"\s+", " ", joined).strip()
        if looks_like_title(joined):
            return [Unit(text=joined, kind="paragraph")]

    if any(is_heading_text(text) for text in texts):
        out: list[Unit] = []
        for text in texts:
            out.append(Unit(text=text, kind=unit_kind(text)))
        return out

    avg_len = sum(len(text) for text in texts) / len(texts)
    if avg_len < 35:
        return [Unit(text=text, kind=unit_kind(text)) for text in texts]

    paragraph = texts[0]
    for text in texts[1:]:
        if paragraph.endswith("-") and not paragraph.endswith(" -"):
            paragraph = paragraph[:-1] + text
        else:
            paragraph = f"{paragraph} {text}"
    paragraph = re.sub(r"\s+", " ", paragraph).strip()
    return [Unit(text=paragraph, kind=unit_kind(paragraph))]


def lines_to_units(page_lines: list[Line]) -> list[Unit]:
    if not page_lines:
        return []

    blocks: list[list[Line]] = []
    current = [page_lines[0]]
    for line in page_lines[1:]:
        if is_same_block(current[-1], line):
            current.append(line)
        else:
            blocks.append(current)
            current = [line]
    blocks.append(current)

    units: list[Unit] = []
    for block in blocks:
        units.extend(render_block(block))
    return units


def normalize_title(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower().replace("*", "")).strip()


def trim_front_matter(units: list[Unit]) -> list[Unit]:
    if not units:
        return units

    texts = [unit.text for unit in units[:80]]
    abstract_idx = next((i for i, text in enumerate(texts) if text.lower() == "abstract"), None)
    if abstract_idx is not None:
        candidates: dict[str, list[int]] = {}
        for idx, text in enumerate(texts[:abstract_idx]):
            if looks_like_title(text):
                candidates.setdefault(normalize_title(text), []).append(idx)

        for positions in candidates.values():
            if len(positions) >= 2:
                return units[positions[1] :]

        title_positions = [idx for idx, text in enumerate(texts[:abstract_idx]) if looks_like_title(text)]
        if title_positions:
            return units[title_positions[-1] :]

        start_min = max(0, abstract_idx - 10)
        for start in range(abstract_idx - 1, start_min - 1, -1):
            for end in range(start, min(abstract_idx, start + 4)):
                joined = " ".join(texts[start : end + 1])
                joined = re.sub(r"\s+", " ", joined).strip()
                if looks_like_title(joined):
                    rebuilt = units[:start] + [Unit(text=joined, kind="paragraph")] + units[end + 1 :]
                    return rebuilt[start:]

    wrapper_idx = next(
        (
            idx
            for idx, text in enumerate(texts[:25])
            if text.lower().startswith("stable url:") or text.upper() == "REFERENCES"
        ),
        None,
    )
    if wrapper_idx is not None:
        window_stop = min(len(texts), wrapper_idx + 25)
        for start in range(wrapper_idx + 1, window_stop):
            for end in range(start, min(window_stop, start + 4)):
                joined = " ".join(texts[start : end + 1])
                joined = re.sub(r"\s+", " ", joined).strip()
                if looks_like_title(joined):
                    rebuilt = units[:start] + [Unit(text=joined, kind="paragraph")] + units[end + 1 :]
                    return rebuilt[start:]
    return units


def should_merge(prev: Unit, curr: Unit) -> bool:
    if prev.kind != "paragraph" or curr.kind != "paragraph":
        return False
    if is_heading_text(prev.text) or is_heading_text(curr.text):
        return False
    if prev.text.endswith((".", "?", "!", ":", ";", "”", '"')):
        return False
    if curr.text.startswith(("http://", "https://")):
        return False
    if re.match(r"^\d+\s+[A-Z]", curr.text):
        return False
    if any(curr.text.lower().startswith(prefix) for prefix in METADATA_PREFIXES):
        return False
    if curr.text[:1].isupper() and len(curr.text.split()) < 8:
        return False
    return True


def merge_units(units: list[Unit]) -> list[Unit]:
    merged: list[Unit] = []
    for unit in units:
        if not merged:
            merged.append(unit)
            continue
        if should_merge(merged[-1], unit):
            if merged[-1].text.endswith("-") and not merged[-1].text.endswith(" -"):
                merged[-1].text = merged[-1].text[:-1] + unit.text
            else:
                merged[-1].text = f"{merged[-1].text} {unit.text}"
            merged[-1].text = re.sub(r"\s+", " ", merged[-1].text).strip()
        else:
            merged.append(unit)
    return merged


def units_to_markdown(units: list[Unit]) -> str:
    out: list[str] = []
    first_written = False

    for unit in units:
        text = clean_unit_text(unit.text)
        if not text:
            continue

        if not first_written:
            out.append(f"# {text}")
            out.append("")
            first_written = True
            continue

        if unit.kind == "heading":
            out.append(f"## {text}")
            out.append("")
            continue

        out.append(text)
        out.append("")

    while out and out[-1] == "":
        out.pop()
    return "\n".join(out) + "\n"


def pdf_to_markdown(pdf_path: Path) -> str:
    pages = parse_bbox_html(pdf_path)
    units: list[Unit] = []
    for page_lines in pages:
        units.extend(lines_to_units(page_lines))
    units = trim_front_matter(units)
    units = merge_units(units)
    return units_to_markdown(units)


def process_pdf(pdf_path: Path) -> None:
    markdown = pdf_to_markdown(pdf_path)
    out_path = OUT_DIR / f"{pdf_path.stem}.md"
    out_path.write_text(markdown, encoding="utf-8")
    print(f"Cleaned {out_path.name}")


def iter_pdfs(args: list[str]) -> list[Path]:
    if args:
        paths = [Path(arg) for arg in args]
        return [path if path.is_absolute() else BASE_DIR / path for path in paths]
    return sorted(BASE_DIR.glob("*.pdf"))


def main(argv: list[str]) -> int:
    OUT_DIR.mkdir(exist_ok=True)
    pdfs = iter_pdfs(argv[1:])
    for pdf_path in pdfs:
        process_pdf(pdf_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
