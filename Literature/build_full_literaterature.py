from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DEFAULT_INPUT_DIR = ROOT / "md_extractions"
DEFAULT_OUTPUT_FILE = ROOT / "full_literaterature.md"
DEFAULT_DOCUMENT_TITLE = "Full Literature"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n")


def make_display_title(path: Path) -> str:
    title = path.stem.replace("_", " ")
    title = re.sub(r"\s+", " ", title).strip()
    return title


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", default=str(DEFAULT_INPUT_DIR))
    parser.add_argument("--output-file", default=str(DEFAULT_OUTPUT_FILE))
    parser.add_argument("--document-title", default=DEFAULT_DOCUMENT_TITLE)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_dir = Path(args.input_dir)
    output_file = Path(args.output_file)
    document_title = args.document_title.strip() or DEFAULT_DOCUMENT_TITLE

    files = sorted(input_dir.glob("*.md"), key=lambda p: p.name.lower())
    if not files:
        raise SystemExit(f"No markdown files found in {input_dir}")

    sections: list[str] = []
    index_lines: list[str] = []

    for i, path in enumerate(files, start=1):
        title = make_display_title(path)
        body = read_text(path).strip()
        anchor = f"paper-{i:03d}"
        index_lines.append(f"{i}. [{title}](#{anchor})")

        parts = [
            f'<a id="{anchor}"></a>',
            "",
            f"## {title}",
            "",
            f"**Source file:** `{input_dir.name}/{path.name}`",
        ]
        if body:
            parts.extend(["", body])
        sections.append("\n".join(parts).strip())

    header = "\n".join(
        [
            f"# {document_title}",
            "",
            "Short prefatory note:",
            f"- generated from markdown files in `{input_dir.name}`",
            f"- includes {len(files)} extracted papers in a single file",
            "- sorted alphabetically by extraction filename",
            "- section titles are based on extraction filenames for a cleaner index",
            "- each section preserves the full extracted markdown content underneath",
            "- index links use stable internal anchors",
            "",
            "## Index",
            "",
            *index_lines,
        ]
    ).strip()

    output = header + "\n\n---\n\n" + "\n\n---\n\n".join(sections) + "\n"
    output_file.write_text(output, encoding="utf-8")


if __name__ == "__main__":
    main()
