#!/usr/bin/env python3
"""对已落盘的游戏 Wiki 跑机械门自检，并刷新 CHECKLIST.md。

用法:
    python3 scripts/qa.py            # 只检查已存在的文件，打印报告
    python3 scripts/qa.py --fix      # 顺带刷新 CHECKLIST.md 勾选
退出码：有问题时为 1。
"""
import argparse, json, os, re, sys
from collections import Counter, OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OTHER = {"光环", "刺客信条", "半条命", "双人合作"}
HARD = ["广受好评", "众所周知", "神作", "封神之作", "不得不说", "好评如潮"]  # 空泛套话，出现即不合格
SOFT = ["据说", "据报道"]  # 需人看上下文：若能指到来源则合规，否则改用「待核实」

def check(path):
    s = open(path, encoding="utf-8").read()
    lines = s.split("\n")
    h1 = [l for l in lines if l.startswith("# ")]
    chaps = re.findall(r"^## (\d+)\.\s*(.+?)\s*$", s, re.M)
    nums = [int(n) for n, _ in chaps]
    names = [t for _, t in chaps]
    probs = []
    if len(h1) != 1 or "Wiki" not in h1[0]:
        probs.append("H1")
    if s.count(":::epigraph") != 1:
        probs.append("epigraph")
    if nums != list(range(1, len(nums) + 1)):
        probs.append(f"nums={nums}")
    if names[-2:] != ["一句话总结", "参考资料"]:
        probs.append(f"tail={names[-2:]}")
    if not any(l.startswith("> 说明") for l in lines):
        probs.append("no-说明")
    zh = len(re.findall(r"[\u4e00-\u9fff]", s))
    if zh < 5000:
        probs.append(f"short({zh})")
    hard = [w for w in HARD if w in s]
    if hard:
        probs.append("套话:" + ",".join(hard))
    soft = [w for w in SOFT if w in s]
    if soft:
        probs.append("⚠:" + ",".join(soft))
    return zh, len(nums), probs

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix", action="store_true")
    args = ap.parse_args()

    rows = json.load(open(os.path.join(ROOT, "index.json"), encoding="utf-8"))
    done = [r for r in rows if os.path.exists(os.path.join(ROOT, r["file"]))]
    bad = warn = 0
    byip = Counter()
    for r in sorted(done, key=lambda x: x["file"]):
        zh, n, probs = check(os.path.join(ROOT, r["file"]))
        byip[r["ip"]] += 1
        hard = [p for p in probs if not p.startswith("⚠")]
        soft = [p for p in probs if p.startswith("⚠")]
        if hard:
            bad += 1
        if soft:
            warn += 1
        if probs:
            print(f"{'✗' if hard else '·'} {r['file']}  {zh}字 ch={n}  {';'.join(probs)}")
    print(f"\n已落盘 {len(done)}/{len(rows)} 篇；结构异常 {bad} 篇；软告警 {warn} 篇。")
    print("按 IP：", dict(byip))

    if args.fix:
        by = OrderedDict()
        for r in rows:
            by.setdefault(r["ip"], []).append(r)
        pend = [r for r in rows if not os.path.exists(os.path.join(ROOT, r["file"]))]
        mine = [r for r in pend if r["ip"] not in OTHER]
        other = [r for r in pend if r["ip"] in OTHER]
        L = ["# WikiAtlas 游戏 Wiki 重写清单", "",
             "## 进度总览", f"- 全量：**{len(rows)} 部 · {len(by)} 个 IP**",
             f"- 已入库：**{len(done)} 部**", 
             f"- 待写：{len(pend)} = 本代理 **{len(mine)}** + 另一代理 **{len(other)}**（光环/刺客信条/半条命/双人合作）", "",
             "## 约定",
             "- 结构 `<游戏IP>/<单作>_WIKI.md`；映射见 `index.json`；规范见 `/root/WikiAltas/skills`。",
             "- 执行说明 `WRITING-BRIEF.md`；派单模板 `DISPATCH.md`；自检 `scripts/qa.py`。", ""]
        for ip, items in by.items():
            d = sum(1 for r in items if os.path.exists(os.path.join(ROOT, r["file"])))
            tag = "（另一代理）" if ip in OTHER else ""
            L.append(f"## {ip}（{d}/{len(items)}）{tag}")
            for r in items:
                mark = "x" if os.path.exists(os.path.join(ROOT, r["file"])) else " "
                alt = f" — {r['title_alt']}" if r["title_alt"] else ""
                L.append(f"- [{mark}] **{r['title']}**{alt} → `{r['file']}`")
            L.append("")
        open(os.path.join(ROOT, "CHECKLIST.md"), "w", encoding="utf-8").write("\n".join(L))
        print("CHECKLIST.md 已刷新")
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()
