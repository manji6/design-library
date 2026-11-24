#!/bin/bash
# design-library の検査一式。各チェックは範囲が増えるたびにここへ足す。
set -u
cd "$(dirname "$0")/.."
fail=0

echo "== tokens consistency =="
for d in designs/*/; do
  if [ -f "$d/DESIGN.md" ]; then
    tmp=$(mktemp)
    python3 scripts/gen-tokens.py "$d/DESIGN.md" "$tmp" || fail=1
    if ! diff -q "$tmp" "$d/tokens.css" >/dev/null 2>&1; then
      echo "MISMATCH: $d/tokens.css is not generated from DESIGN.md"
      fail=1
    fi
    rm -f "$tmp"
  fi
done

echo "== declaration tables =="
for f in designs/*/DESIGN.md; do
  [ -f "$f" ] || continue
  grep -q "要素の宣言表" "$f" || { echo "MISSING declaration table: $f"; fail=1; }
done

echo "== local links =="
python3 - <<'PY' || fail=1
import os, re, sys
bad = []
for root, _, files in os.walk("."):
    if ".git" in root:
        continue
    for name in files:
        if not name.endswith(".md"):
            continue
        p = os.path.join(root, name)
        text = open(p, encoding="utf-8").read()
        for m in re.finditer(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", text):
            url = m.group(1)
            if url.startswith(("http://", "https://", "mailto:")):
                continue
            target = os.path.normpath(os.path.join(root, url))
            if not os.path.exists(target):
                bad.append(f"{p}: {url}")
for b in bad:
    print("BROKEN LINK:", b)
sys.exit(1 if bad else 0)
PY

echo "== pattern headings =="
if [ -f diagrams/_template.md ]; then
  python3 - <<'PY' || fail=1
import glob, re, sys
tpl = open("diagrams/_template.md", encoding="utf-8").read()
heads = re.findall(r"^## (.+)$", tpl, re.M)
bad = []
for p in glob.glob("diagrams/patterns/*/*.md"):
    text = open(p, encoding="utf-8").read()
    have = re.findall(r"^## (.+)$", text, re.M)
    for h in heads:
        if h not in have:
            bad.append(f"{p}: missing heading {h}")
for b in bad:
    print("HEADING:", b)
sys.exit(1 if bad else 0)
PY
fi

if [ "$fail" -ne 0 ]; then
  echo "CHECK FAILED"
  exit 1
fi
echo "ALL CHECKS PASSED"
