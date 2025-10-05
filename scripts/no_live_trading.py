#!/usr/bin/env python3
import sys
from pathlib import Path

BANNED_PATTERNS = [
    "SIMULATION_MODE=LIVE",
    "simulate_only: false",
    "simulate_only:false",
    "LIVE_TRADING=True",
    "LIVE_TRADING = True",
]

def check_file(path: Path) -> list[str]:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return []
    hits = []
    for pat in BANNED_PATTERNS:
        if pat in text:
            hits.append(pat)
    return hits

def main() -> int:
    files = [Path(p) for p in sys.argv[1:] if p.endswith((".py", ".yaml", ".yml", ".env", ".txt", ".md"))]
    failures = {}
    for f in files:
        hits = check_file(f)
        if hits:
            failures[str(f)] = hits
    if failures:
        print("Live-trading patterns are forbidden.\n")
        for fname, pats in failures.items():
            for p in pats:
                print(f" - {fname}: found '{p}'")
        print("\nRefusing commit. Remove/replace the patterns above.")
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
