#!/usr/bin/env python3
"""Rewrite links to an archived domain for project GitHub Pages."""

from pathlib import Path
import sys


year, domain = sys.argv[1:]
text_suffixes = {".html", ".htm", ".css", ".js", ".xml", ".txt", ".json"}
prefix = f"/{year}/"

for path in Path(".").rglob("*"):
    if not path.is_file() or path.suffix.lower() not in text_suffixes:
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    original = text
    for scheme in ("http", "https"):
        text = text.replace(f"{scheme}://{domain}/", prefix)
        text = text.replace(f"{scheme}://www.{domain}/", prefix)
    if text != original:
        path.write_text(text, encoding="utf-8")

