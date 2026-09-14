"""Offline browser/render checks for the V8 report and gallery."""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

from playwright.sync_api import sync_playwright


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REPORT = ROOT / "reports/JMP_research_story_report_v8.html"
GALLERY = ROOT / "reports/JMP_results_gallery_v8.html"
OUT = ROOT / "reports/v8_render_gate.json"
SCREEN_REPORT = Path(tempfile.gettempdir()) / "jmp_v8_report_results.png"
SCREEN_GALLERY = Path(tempfile.gettempdir()) / "jmp_v8_gallery_opening.png"


def inspect_page(page, path: Path, wait_for_math: bool) -> dict:
    errors = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    page.goto(path.as_uri(), wait_until="load")
    if wait_for_math:
        page.wait_for_function(
            "window.MathJax && MathJax.startup && MathJax.startup.promise"
        )
        page.evaluate("MathJax.startup.promise")
    info = page.evaluate("""() => ({
      images_ok: Array.from(document.images).every(x => x.complete && x.naturalWidth > 0),
      image_count: document.images.length,
      math_count: document.querySelectorAll('.math').length,
      rendered_math_count: document.querySelectorAll('mjx-container').length,
      math_errors: Array.from(document.querySelectorAll('[data-mjx-error],mjx-merror')).map(x => x.textContent),
      details_count: document.querySelectorAll('details').length,
      closed_details: Array.from(document.querySelectorAll('details')).every(x => !x.open),
      provenance_closed: !document.querySelector('#provenance > details') || !document.querySelector('#provenance > details').open,
      viewport_overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth + 1,
      headings: Array.from(document.querySelectorAll('h1,h2')).map(x => x.textContent.trim()),
      figures: document.querySelectorAll('figure').length,
      captions: document.querySelectorAll('figcaption').length
    })""")
    info["javascript_errors"] = errors
    return info


def main() -> int:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            executable_path=(
                r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            ),
            headless=True,
        )
        context = browser.new_context(
            viewport={"width": 1440, "height": 1050}, offline=True
        )
        report_page = context.new_page()
        report = inspect_page(report_page, REPORT, wait_for_math=True)
        report_page.get_by_role(
            "heading", name="5. What the current results say", exact=True
        ).scroll_into_view_if_needed()
        report_page.screenshot(path=str(SCREEN_REPORT))

        gallery_page = context.new_page()
        gallery = inspect_page(gallery_page, GALLERY, wait_for_math=False)
        gallery_page.screenshot(path=str(SCREEN_GALLERY))
        browser.close()

    checks = {
        "report_images": report["images_ok"] and report["image_count"] > 0,
        "report_math": report["math_count"] > 0
        and report["rendered_math_count"] >= report["math_count"]
        and not report["math_errors"],
        "report_javascript": not report["javascript_errors"],
        "report_provenance_collapsed": report["details_count"] >= 1
        and report["closed_details"],
        "report_viewport": not report["viewport_overflow"],
        "gallery_images": gallery["images_ok"] and gallery["image_count"] > 0,
        "gallery_captions": gallery["captions"] >= gallery["figures"],
        "gallery_provenance_collapsed": gallery["details_count"] >= 1
        and gallery["provenance_closed"],
        "gallery_javascript": not gallery["javascript_errors"],
        "gallery_viewport": not gallery["viewport_overflow"],
    }
    failed = [name for name, ok in checks.items() if not ok]
    result = {
        "gate": "V8 offline render",
        "status": "PASS" if not failed else "FAIL",
        "checks": checks,
        "report": report,
        "gallery": gallery,
        "screenshots": "temporary visual-inspection captures completed",
        "failures": failed,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8",
                   newline="\n")
    for name, ok in checks.items():
        print(f'{"PASS" if ok else "FAIL"}: {name}')
    print("temporary screenshots captured for visual inspection")
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
