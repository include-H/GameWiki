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

- `CHECKLIST.md` —— 全量清单（252 部 · 81 个 IP），按 IP 分组，勾选进度。
- `index.json` —— 程序用映射：`public_id` → `file`（回推 GameAtlas 时按它定位）。

## 回推 GameAtlas

`PUT /api/games/{public_id}/wiki`，body `{content, change_summary}`（管理员会话，先 `POST /api/auth/login`）。
覆盖写，**不可轻易撤销**——按 `index.json` 定位文件后批量推送。
