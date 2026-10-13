#!/usr/bin/env python3
"""按 index.json 生成待写的游戏 Wiki 派单清单/提示词。

用法:
    python3 scripts/dispatch.py                 # 待写全量（排除已落盘与「另一代理」IP）
    python3 scripts/dispatch.py --ip 合金装备    # 只看某个 IP
    python3 scripts/dispatch.py --limit 12      # 只出前 N 个
    python3 scripts/dispatch.py --prompts       # 额外打印可直接派发的 prompt 文本
    python3 scripts/dispatch.py --include-other # 连「另一代理」负责的 IP 一并列出
"""
import argparse, json, os, sys

# 另一代理负责的 IP（这些留给他们，本脚本默认跳过）
OTHER_AGENT_IPS = {"光环", "刺客信条", "半条命", "双人合作"}

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(ROOT, "index.json")

PROMPT = (
    "读 `/root/Game_Wiki/WRITING-BRIEF.md` 并**严格按其执行**"
    "（它写了该读哪些技能、怎么写、怎么自检与回报）。\n"
    "目标作品：{title}（英文名 {alt}；IP：{ip}）。\n"
    "输出到精确路径：`/root/Game_Wiki/{file}`。"
)


def load():
    with open(INDEX, encoding="utf-8") as f:
        return json.load(f)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ip")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--prompts", action="store_true")
    ap.add_argument("--include-other", action="store_true")
    args = ap.parse_args()

    rows = load()
    pending = []
    for r in rows:
        if os.path.exists(os.path.join(ROOT, r["file"])):
            continue
        if not args.include_other and r["ip"] in OTHER_AGENT_IPS:
            continue
        if args.ip and r["ip"] != args.ip:
            continue
        pending.append(r)

    if args.limit:
        pending = pending[: args.limit]

    print(f"待写 {len(pending)} 篇\n")
    for r in pending:
        print(f"  {r['ip']:>8} | {r['title']} → {r['file']}")
    if args.prompts:
        print("\n" + "=" * 60)
        for r in pending:
            print("\n--- " + r["title"] + " ---")
            print(PROMPT.format(title=r["title"], alt=r.get("title_alt") or "—",
                                ip=r["ip"], file=r["file"]))


if __name__ == "__main__":
    sys.exit(main())
