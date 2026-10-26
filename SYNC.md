# 远端同步：GameAtlas → 本仓追踪文件

GameAtlas 生产库（默认 `http://192.168.1.4:3000`，可用 `GA_BASE` 覆盖）在游戏条目上
**新增 / 改名 / 新增 series** 之后，本仓的 `index.json` / `STATUS.json` / `CHECKLIST.md`
会暂时落后。本文描述如何拉齐（**拉取方向**），与 `scripts/push.py`（回推方向）互为镜像。

> 现状锚点：`index.json` 是唯一事实源；`STATUS.json` 是它的一个投影；`CHECKLIST.md` 可读、
> 亦可随时由 `scripts/qa.py --fix` / `scripts/sync.py sync --checklist` 重建，放心让它重算。

## 一键同步（推荐）

```bash
python3 scripts/sync.py report              # ① 只读：看本地 vs 远端差什么，不写任何文件
python3 scripts/sync.py sync                # ② 落盘 index.json + STATUS.json
python3 scripts/sync.py sync --checklist    # ③ 顺带重算 CHECKLIST.md
python3 scripts/sync.py sync --drop         # 同上，且删除「远端已消失」条目（慎用，见下）
```

依赖 `scripts/push.py` 的同一个登录链路：读 `GA_PASSWORD` 或
`/root/WikiAltas/.secrets/credentials.md`（GameAtlas 生产库行）。复用其 `GA` 类，
所以 **凡能 push 的环境就能 sync**，无额外安装。

### 它对账的四件事（及默认行为）

| # | 情况 | 默认行为 |
|---|---|---|
| 1 | **新增**：远端 public_id 本地没有 | 追加条目；文件路径 `<series 或 标题>/<标题>_WIKI.md`；`has_content` 取本地该文件是否已落盘。 |
| 2 | **孤儿关联**：本地 `public_id=null` 且远端出现同名（title 相等）游戏 | 就地写回 `public_id`/`title_alt`/`release_date`/`ga_year`，**保留原 file**（指向已有文章），重算 `has_content`。 |
| 3 | **内容位**：某条目本地文件实际存在与否和 `has_content` 不一致 | 将 `has_content` 改为「文件存在」的真实值。 |
| 4 | **消失**：本地某 `public_id` 远端查不到 | **只报告，不删**。确认远端是改名/移除且本仓也要跟进时，才加 `--drop`。 |

### 孤儿与人工扩写

`public_id=null` 的条目可能有两类，本脚本分别处理：

- **仍属生产库、只是当时没写 public_id**（例如「最终幻想：零式」首次回库时）→
  规则 2 会在远端对齐 title 后自动补上 public_id。这是最常见的情况。
- **人工扩写、本不在生产库**（例如「命令与征服」正传泰伯伦几部）→
  远端查不到同名游戏，**原样保留**在本仓 `index.json` 里，不会被 sync 误删。
  `scripts/push.py` 也不会推它们（`plan()` 过滤 `public_id=null`）。

### series 没了怎么办

远端条目 `series=null` 时，一级目录名退化为作品标题本身，例如
`龙背上的骑兵 3/龙背上的骑兵 3_WIKI.md`。这是约定，不是 bug；若你认为应该归到某 IP 下，
**先去 GameAtlas 改 series**（或在库管理页给它加个条目），再来 sync 才会落到正确目录。
注意 series 改名的 mismatch：远端改 series 名后，本仓已经写好的目录/文件名不会自动搬迁，
要不要搬迁要人工判断。

## 手动拉取（脚本碰不了或想看懂时）

`/api/games` 与 `/api/games/all` 都可列全线；**需要登录态**（匿名返回 `success:false`）。
最小回声：

```bash
# 登录 → session 落到 cookie jar；getAll 拉回；本地 index 有 262 条；新增游戏 diff 出来
curl -s -c /tmp/ga.cookie -X POST http://192.168.1.4:3000/api/auth/login \
     -H 'Content-Type: application/json' \
     -d '{"password":"<GA_PASSWORD>"}' | python3 -m json.tool | head -3

curl -s -b /tmp/ga.cookie http://192.168.1.4:3000/api/games/all \
     | python3 -c "
import json,sys
remote=json.load(sys.stdin)['data']
local=json.load(open('/root/Game_Wiki/index.json'))
lpids={e['public_id'] for e in local if e.get('public_id')}
new=[g for g in remote if g['public_id'] not in lpids]
print('远端 %d 部；本地 %d 条；新增 %d 部' % (len(remote), len(local), len(new)))
for g in new: print('  ＋', g['title'], '|', g.get('release_date'))
"
```

手动流程建议：

1. `curl` 拉 `all` 找到新增条目 `public_id` / `title` / `series` / `release_date`。
2. 在 `index.json` 末尾追加条目（字段同形），`title_alt` 保留 `null` 也可。
3. 本地若已有对应文章，`has_content=true`；否则 `false`。
4. 重算 `STATUS.json`（`done`= `has_content=true` 的条数）。
5. `python3 scripts/qa.py --fix` 或 `scripts/sync.py sync --checklist` 刷新 CHECKLIST。

**提醒**：如果 sync 加回再来手动改，会把你的改动冲掉。要改就全从 `scripts/sync.py` 的
`reconcile()` 派生（或读完 `sync.py` 改完再跑）。

## 远端改名为何、如何避坑

远端改 public_id 少，但改 `title`/`series` 会发生。表现是本地的 **孤儿关联**（规则 2）
触发不到，因为 title 已经不再相等。此时脚本会报：

- 远端出现一个「新增」（其实是改名后的旧游戏）；
- 本地出现一个「消失」（改名前的 public_id）。

建议：

1. 先 `report` 看清楚；
2. 决定留在哪个标题：若远端已改名，本仓文章标题与文件名也应更新；
3. 手动改 `index.json` 里那条 `title`/`file`，或在 GameAtlas 里回退命名。

单纯「消失」且远端不存在的同名替代时，确认可以 `sync --drop`；否则保留，人来对账。

## 常见命令节奏（和 push 搭配）

```bash
# 每周 / 远端有新游戏时
python3 scripts/sync.py report      # 发现新增
python3 scripts/sync.py sync --checklist   # 落盘
python3 scripts/dispatch.py         # 看新游戏待写 list
python3 scripts/qa.py --fix         # 写完一批后刷新 CHECKLIST 与自检

# 写完 → 回推
python3 scripts/push.py push --only "熊/龙背"   # 只推某 IP/路径片段
python3 scripts/push.py status                 # 看最新一次 push 小结
```

## 日志与可观测

- `scripts/sync.py` **不写磁盘日志**，直接 stdout 即可被 CI / shell 历史捕获。
- 每次 `sync` 都会重写 `index.json`（1 换行）与 `STATUS.json`；如需 diff，直接看 git。
- 依赖 `index.json` 的其它脚本（`dispatch.py`、`qa.py`、`push.py`）会在你写完后自然拿到新数据。

## 2026-10-26 首次使用记录（本次）

- GameAtlas 新增 3 部（使命召唤：现代战争 4 / 真・三国无双２ with 猛将传 Remastered /
  最终幻想：零式）+ 1 部龙背上的骑兵 3（追加发现）。
- 本地漏标 `has_content` 126 条，被 `sync` 更正。
- 「最终幻想：零式」孤儿关联到远端 `920c0e8a-5fcf-4758-beb0-f147a6c295e6`，file 不变。
- 结果：`index.json` 262 条 / `STATUS.json done=260` / 待写 2 部。
