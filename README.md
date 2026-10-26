# Game_Wiki

WikiAtlas 游戏 Wiki 的**内容仓**（暂时回归"Markdown + git 追踪"的老办法，取代 v2 的 PG 存储）。

## 这是什么

- 数据源是 **GameAtlas 生产库**（`http://192.168.1.4:3000`）：库里的一个游戏条目 = 这里的一篇文档。
- 写作规范来自 **`/root/WikiAltas/skills`**（v2 技能体系）：`wiki-write` · `wiki-skeleton` · `media-game` · `epigraph` · `prose-style` · `fact-check` · `index-fields`。
- 内容**联网从头重写**；旧稿只用于定位，不作底稿。

## 目录结构

```
<游戏IP>/<单作>_WIKI.md
```

- 一级目录 = 游戏 IP（取自 GameAtlas 的 series；无 series 的按 IP 归并，见 `index.json`）。
- 文件名 = 作品标题；**仅当标题在本库内重名时**才加原始发行年份消歧（如 `使命召唤：现代战争_2007_WIKI.md` / `_2019_WIKI.md`）。

## 清单与映射

- `CHECKLIST.md` —— 全量清单，按 IP 分组，勾选进度；由 `scripts/qa.py --fix` / `scripts/sync.py sync --checklist` 重建。
- `index.json` —— 程序用映射：`public_id` → `file`（回推 GameAtlas 时按它定位）。

## 远端同步（拉取）

GameAtlas 新增/改动游戏后，把本仓追踪文件拉齐到最新库状态，详见 `SYNC.md`：

```bash
python3 scripts/sync.py report             # 只读：本地 vs 远端差异
python3 scripts/sync.py sync               # 写 index.json + STATUS.json（新增/孤儿关联/内容位）
python3 scripts/sync.py sync --checklist   # 顺带重算 CHECKLIST.md
python3 scripts/sync.py sync --drop        # 连同远端已消失条目删除（慎用）
```

与 `push.py` 方向相反：sync 是 **GameAtlas → 本仓 index**；push 是 **本仓 .md → GameAtlas 库**。
凭据同 push.py（`GA_PASSWORD` 或 `/root/WikiAltas/.secrets/credentials.md`）。
人工扩写条目（`public_id=null`，如命令与征服正传）sync 不动、push 不推。

## 回推 GameAtlas

`PUT /api/games/{public_id}/wiki`，body `{content, change_summary}`（管理员会话，先 `POST /api/auth/login`）。
覆盖写，**不可轻易撤销**——按 `index.json` 定位文件后批量推送。

统一走 `scripts/push.py`（凭据读 `GA_PASSWORD` 或 `/root/WikiAltas/.secrets/credentials.md`）：

```bash
python3 scripts/push.py check          # 登录 + roster 对账 + 文件体检 + 端点探测
python3 scripts/push.py push --dry-run # 只读：本机 vs 远端差异分布
python3 scripts/push.py push --limit 1 # 冒烟一条
python3 scripts/push.py push           # 全量（每条 PUT 后回读校验；中断可重跑，已一致自动跳过）
python3 scripts/push.py status         # 看最近一次运行小结
```

注意：GA 入库会去掉内容末尾换行，脚本比较时已归一；无 `public_id` 的条目（人工扩写，如命令与征服正传）不在生产库，不推。
首次全量回推：**252/252 成功**（2026-10-16，见 `push-log/`）。
