#!/usr/bin/env python3
"""审计题记写法与可疑措辞：
   1) 每个人的 `:::epigraph` 是「引用式（有署名 ——）」还是「自写（无署名：场景式/自创诗）」。
   2) 列出含「据说 / 据报道」的文件与行。
用法：python3 scripts/epigraph-audit.py
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows = json.load(open(os.path.join(ROOT, "index.json"), encoding="utf-8"))

quoted, written, noepi = [], [], []
soft = []
for r in rows:
    p = os.path.join(ROOT, r["file"])
    if not os.path.exists(p):
        continue
    s = open(p, encoding="utf-8").read()
    m = re.search(r":::epigraph\n(.*?)\n:::", s, re.S)
    if not m:
        noepi.append(r["file"]); continue
    block = m.group(1)
    if any(l.strip().startswith("——") or l.strip().startswith("—") for l in block.split("\n")):
        quoted.append(r["file"])
    else:
        written.append(r["file"])
    for w in ("据说", "据报道"):
        if w in s:
            soft.append((r["file"], w))

print(f"总 {len(quoted)+len(written)+len(noepi)} 篇 | 引用式(有署名) {len(quoted)} | 自写(无署名) {len(written)} | 无题记 {len(noepi)}")
print("\n=== 自写题记（无署名，需复核是否偷懒降级）===")
for f in sorted(written):
    print("  " + f)
print("\n=== 含 据说/据报道 ===")
for f, w in soft:
    print(f"  {f}  [{w}]")
