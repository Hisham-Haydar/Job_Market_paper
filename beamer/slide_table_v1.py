#!/usr/bin/env python
"""Print the per-slide table measured from the verified full PDF."""
import argparse
import csv
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--csv', type=Path)
    ap.add_argument('--words', action='store_true')
    args = ap.parse_args()
    path = HERE / 'build/slide_table_v4.json'
    if not path.exists():
        raise SystemExit('Run python build_deck_v4.py all first.')
    rows = json.loads(path.read_text(encoding='utf-8'))
    print('slide | headline | element | on-slide words')
    for r in rows:
        print('{number} | {headline} | {element} | {on_slide_words}'.format(**r))
    if args.csv:
        with args.csv.open('w',encoding='utf-8',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0]))
            w.writeheader()
            w.writerows(rows)

if __name__ == '__main__': main()
