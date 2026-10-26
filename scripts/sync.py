#!/usr/bin/env python3
"""从 GameAtlas 生产库同步最新游戏，回写本仓追踪文件 index.json / STATUS.json（可选 CHECKLIST.md）。

这是「拉取方向」脚本：远端 GameAtlas 新增/改动了游戏 → 对齐本地 index.json。
与 scripts/push.py（回推方向：本地 .md 写入远端 wiki）互为镜像。

用法:
    python3 scripts/sync.py report             # 只读：打印本地 vs 远端差异，不写任何文件
    python3 scripts/sync.py sync               # 写 index.json + STATUS.json（新增/孤儿关联/内容位）
    python3 scripts/sync.py sync --checklist   # 顺带重算 CHECKLIST.md（同 scripts/qa.py --fix 口径）
    python3 scripts/sync.py sync --drop        # 连同远端已消失条目从 index 一并删除

对账规则
  1. 新增：远端 public_id 本地 index 没有 → 追加；file 按 <series|title>/<title>_WIKI.md；
     has_content 取决于该文件是否已落盘。
  2. 孤儿关联：本地 public_id=null 且远端出现同名（title 相等）游戏 → 原地写回 public_id、
     title_alt、release_date、ga_year，保留原 file，has_content 按落盘重算。用于把「回生产库
     的孤儿」（如 最终幻想：零式）重新挂上。
  3. 内容位：所有带 public_id 且远端仍存在的条目，has_content 按本地文件存在性重算（回推后保持同步）。
  4. 消失（默认只报告、不删）：本地某 public_id 远端查不到。带 --drop 才删——腾掉前先确认不是「改名」。

已存在的孤儿（public_id=null）即使未匹配到远端也原样保留：那些是「人工扩写、不在生产库」的条目
（如命令与征服正传泰伯伦系），属本仓独有内容，不随远端增删。

凭据: 复用 push.py 来源——环境变量 GA_PASSWORD 或 /root/WikiAltas/.secrets/credentials.md（GameAtlas 生产库行）。
"""
import argparse, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from push import GA, ROOT, INDEX  # 复用凭据/登录与路径约定

CHECKLIST = os.path.join(ROOT, "CHECKLIST.md")
STATUS = os.path.join(ROOT, "STATUS.json")
OTHER = {"光环", "刺客信条", "半条命", "双人合作"}  # 另一代理 IP（与 dispatch.py / qa.py 一致）


def fetch_all(ga):
    env = ga.call("GET", "/api/games/all")
    if not env.get("success"):
        raise SystemExit("拉取 /api/games/all 失败：%s" % env.get("error"))
    return env.get("data") or []


def file_exists(rel):
    p = os.path.join(ROOT, rel)
    return os.path.isfile(p) and os.path.getsize(p) > 0


def reconcile(remote, idx):
    """返回 (add, refresh, drop, link_map)。
    add=[(game, entry)]；refresh={new_pid: new_entry}（孤儿关联+内容位）；
    drop=[entry]；link_map={孤儿标题: 新pid}。纯函数。"""
    local_by_pid = {e["public_id"]: dict(e) for e in idx if e.get("public_id")}
    local_orphans = {e["title"]: dict(e) for e in idx if not e.get("public_id")}
    remote_by_pid = {g["public_id"]: g for g in remote}
    link_map = {}
    remote_by_title = {}
    for g in remote:
        for key in (g.get("title"), g.get("title_alt")):
            if key:
                remote_by_title.setdefault(key, g)

    add, refresh, drop = [], {}, []

    # 孤儿先占用远端条目，其 public_id 不得再计入「新增」
    claimed = {remote_by_title[e["title"]]["public_id"]
               for e in local_orphans.values() if remote_by_title.get(e["title"])}

    # 1) 新增
    for g in remote:
        if g["public_id"] in local_by_pid or g["public_id"] in claimed:
            continue
        series = (g.get("series") or {}).get("name")
        dir_ = series or g["title"]  # 无 series 时用作品名作一级目录
        add.append((g, {
            "public_id": g["public_id"],
            "title": g["title"],
            "title_alt": g.get("title_alt"),
            "series": series,
            "ip": dir_,
            "ga_year": g["release_date"][:4] if g.get("release_date") else None,
            "release_date": g.get("release_date"),
            "file": "%s/%s_WIKI.md" % (dir_, g["title"]),
            "has_content": file_exists("%s/%s_WIKI.md" % (dir_, g["title"])),
        }))

    # 2) 孤儿关联（title 精确相等）
    for title in list(local_orphans):
        g = remote_by_title.get(title)
        if not g or g["public_id"] in local_by_pid:
            continue
        ne = dict(local_orphans[title])
        ne["public_id"] = g["public_id"]
        if g.get("title_alt"):
            ne["title_alt"] = g["title_alt"]
        if g.get("release_date"):
            ne["release_date"] = g["release_date"]
            ne["ga_year"] = g["release_date"][:4]
        ne.pop("note", None)
        ne["has_content"] = file_exists(ne["file"])
        refresh[g["public_id"]] = ne
        link_map[title] = g["public_id"]
        del local_orphans[title]

    # 3) 内容位：带 public_id 且远端仍存在、且未被孤儿关联覆盖的条目
    for pid, e in local_by_pid.items():
        if pid not in remote_by_pid or pid in refresh:
            continue
        should = file_exists(e["file"])
        if bool(e.get("has_content")) != should:
            ne = dict(e); ne["has_content"] = should
            refresh[pid] = ne

    # 4) 消失（仅报告，--drop 才删）
    drop = [local_by_pid[pid] for pid in local_by_pid if pid not in remote_by_pid]

    return add, refresh, drop, link_map


def apply(idx, add, refresh, drop, link_map, drop_enabled):
    """纯函数：按 reconcile 结果构建新 index。原顺序保留，孤儿就地升为已关联版，新增追加末尾。

    - 带 public_id 的条目：落入 refresh 则用刷新版（内容位/孤儿关联的新 pid 同标题），否则原样。
    - 孤儿（pid=null）：确切在 link_map 里 → 用 refresh[新pid] 就地升级；其余原样保留（人工扩写）。
    """
    drop_pids = {e["public_id"] for e in drop} if drop_enabled else set()
    new_idx = []
    for e in idx:
        pid = e.get("public_id")
        if pid is None:
            if e.get("title") in link_map:
                new_idx.append(refresh[link_map[e["title"]]])
            else:
                new_idx.append(e)  # 人工扩写，不在生产库，保留
        else:
            if pid in drop_pids:
                continue
            new_idx.append(refresh.get(pid, e))
    new_idx.extend(ne for _g, ne in add)
    return new_idx


def write_status(idx):
    st = {"done": sum(1 for e in idx if e.get("has_content")),
          "pending_mine": 0, "pending_other": 0}
    open(STATUS, "w", encoding="utf-8").write(json.dumps(st, ensure_ascii=False, indent=1) + "\n")
    return st


def refresh_checklist(idx):
    """按 scripts/qa.py --fix 同口径重算 CHECKLIST.md（以 index.json 为唯一事实源）。"""
    from collections import OrderedDict
    done = [r for r in idx if file_exists(r["file"])]
    pend = [r for r in idx if not file_exists(r["file"])]
    by = OrderedDict()
    for r in idx:
        by.setdefault(r["ip"], []).append(r)
    mine = sum(1 for r in pend if r["ip"] not in OTHER)
    other = sum(1 for r in pend if r["ip"] in OTHER)
    L = ["# WikiAtlas 游戏 Wiki 重写清单", "", "## 进度总览",
         "- 全量：**%d 部 · %d 个 IP**" % (len(idx), len(by)),
         "- 已入库：**%d 部**" % len(done),
         "- 待写：%d = 本代理 **%d** + 另一代理 **%d**（光环/刺客信条/半条命/双人合作）" % (len(pend), mine, other),
         "- 回推 GameAtlas 生产库：见 push-log/ 最近小结（`python3 scripts/push.py status`）。", "",
         "## 约定",
         "- 结构 `<游戏IP>/<单作>_WIKI.md`；映射见 `index.json`；规范见 `/root/WikiAltas/skills`。",
         "- 执行说明 `WRITING-BRIEF.md`；派单 `scripts/dispatch.py`；自检 `scripts/qa.py`；远端同步 `scripts/sync.py`。", ""]
    for ip, items in by.items():
        d = sum(1 for r in items if file_exists(r["file"]))
        tag = "（另一代理）" if ip in OTHER else ""
        L.append("## %s（%d/%d）%s" % (ip, d, len(items), tag))
        for r in items:
            mark = "x" if file_exists(r["file"]) else " "
            alt = " — %s" % r["title_alt"] if r.get("title_alt") else ""
            L.append("- [%s] **%s**%s → `%s`" % (mark, r["title"], alt, r["file"]))
        L.append("")
    open(CHECKLIST, "w", encoding="utf-8").write("\n".join(L))


def print_report(add, refresh, drop, old_by_pid, drop_enabled):
    only_content = sum(1 for p, ne in refresh.items()
                       if p in old_by_pid and old_by_pid[p].get("public_id") == p)
    link_n = len(refresh) - only_content
    print("新增 %d ｜ 孤儿关联 %d ｜ 内容位 %d ｜ 远端已消失 %d%s"
          % (len(add), link_n, only_content, len(drop),
             "（--drop：将删除）" if (drop and drop_enabled) else ""))
    for g, ne in add:
        print("  ＋ 新增  %s → %s（%s）" % (g["title"], ne["file"],
              "已有文件" if ne["has_content"] else "待写"))
    for p, ne in refresh.items():
        why = "孤儿关联" if p not in old_by_pid else "内容位→%s" % ne["has_content"]
        print("  ⚭ 刷新  %s（%s, has_content=%s）" % (ne["title"], why, ne["has_content"]))
    for e in drop:
        print("  − 消失  %s（pid %s）%s" % (e["title"], (e.get("public_id") or "")[:8],
              "【将删除】" if drop_enabled else "（默认保留）"))
    if not (add or refresh or drop):
        print("  （本地已与远端一致，无变更）")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sp = sub.add_parser("sync")
    sp.add_argument("--checklist", action="store_true", help="顺带重算 CHECKLIST.md")
    sp.add_argument("--drop", action="store_true", help="连同远端已消失条目从 index 删除")
    sub.add_parser("report")
    args = ap.parse_args()
    drop_enabled = bool(getattr(args, "drop", False))

    ga = GA()
    remote = fetch_all(ga)
    idx = json.load(open(INDEX, encoding="utf-8"))
    add, refresh, drop, link_map = reconcile(remote, idx)
    old_by_pid = {e["public_id"]: e for e in idx if e.get("public_id")}
    print("GameAtlas: %d 部 ｜ 本地 index: %d 条" % (len(remote), len(idx)))
    print_report(add, refresh, drop, old_by_pid, drop_enabled)

    if args.cmd != "sync":
        print("\n（report 模式：未写任何文件；加 sync 落盘）")
        return

    new_idx = apply(idx, add, refresh, drop, link_map, drop_enabled)
    open(INDEX, "w", encoding="utf-8").write(json.dumps(new_idx, ensure_ascii=False, indent=1) + "\n")
    st = write_status(new_idx)
    if args.checklist:
        refresh_checklist(new_idx)
    print("\n✅ index.json 已写（%d 条）｜ STATUS.json done=%d ｜ CHECKLIST.md %s"
          % (len(new_idx), st["done"], "已刷新" if args.checklist else "未动"))
    if drop and not drop_enabled:
        print("⚠ 有 %d 条远端已消失但未删除（用 --drop 才会删）" % len(drop))


if __name__ == "__main__":
    main()
