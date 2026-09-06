#!/usr/bin/env bash
# Build the JMP seminar deck.  Run from beamer/.
#
#   ./build_deck_v1.sh              all three builds (default)
#   ./build_deck_v1.sh full         45-minute projection deck only
#   ./build_deck_v1.sh short        25-minute running order only
#   ./build_deck_v1.sh rehearsal    presenter build (slide + notes) only
#
# The number macros are regenerated first, so the deck can never drift
# from the frozen seminar-sprint tables.  Then every build is verified by
# verify_deck_v1.py: figure paths, macro definitions, frame and page
# counts, and a log with no error and no overfull box.
#
# Requires pdflatex and latexmk (MiKTeX or TeX Live) on PATH, and perl,
# which latexmk needs.  On Windows, Git Bash supplies perl; add MiKTeX:
#   export PATH="$LOCALAPPDATA/Programs/MiKTeX/miktex/bin/x64:$PATH"
set -euo pipefail
cd "$(dirname "$0")"

OUT=build
JOBS_FULL=JMP_seminar_deck_v1
JOBS_SHORT=JMP_seminar_deck_v1_25min
JOBS_REH=JMP_seminar_deck_v1_rehearsal

python make_deck_macros_v1.py
python make_slide_figures_v1.py
mkdir -p "$OUT"

build_one () {          # $1 = driver .tex basename
  local job="$1"
  echo "=== building $job ==="
  latexmk -pdf -interaction=nonstopmode -outdir="$OUT" "$job.tex" >/dev/null 2>&1 || true
  local err box
  err=$(grep -c '^!' "$OUT/$job.log" || true)
  box=$(grep -c 'Overfull\|Underfull' "$OUT/$job.log" || true)
  printf '    errors=%s  boxes=%s  %s\n' "$err" "$box" \
    "$(grep -o '([0-9]* pages' "$OUT/$job.log" | tail -1)"
  [ "$err" = "0" ] || { echo "    FAILED -- see $OUT/$job.log"; exit 1; }
  [ "$box" = "0" ] || { echo "    FAILED -- overfull/underfull box"; exit 1; }
}

case "${1:-all}" in
  full)      build_one "$JOBS_FULL" ;;
  short)     build_one "$JOBS_SHORT" ;;
  rehearsal) build_one "$JOBS_REH" ;;
  all)
    build_one "$JOBS_FULL"
    build_one "$JOBS_SHORT"
    build_one "$JOBS_REH"
    ;;
  *) echo "usage: $0 [all|full|short|rehearsal]"; exit 2 ;;
esac

echo
echo "=== text exports for review ==="
# A plain-text rendering of each built variant, for reading the deck without
# opening it and for eyeballing the forbidden-label gate by hand.
for f in "$OUT"/*.pdf; do
  [ -e "$f" ] || continue
  b="$(basename "$f" .pdf)"
  pdftotext -layout "$f" "$OUT/${b}_text.txt"
  printf '  %-46s %s lines\n' "${b}_text.txt" "$(wc -l < "$OUT/${b}_text.txt")"
done

echo
echo "=== the per-slide table ==="
python slide_table_v1.py --csv slide_table_v1.csv

echo
echo "=== verification ==="
python verify_deck_v1.py

echo
echo "=== page counts ==="
for f in "$OUT"/*.pdf; do
  [ -e "$f" ] || continue
  printf '  %-46s %s pages\n' "$(basename "$f")" \
    "$(pdfinfo "$f" 2>/dev/null | awk '/^Pages:/{print $2}')"
done
