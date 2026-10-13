# DISPATCH.md —— 子代理派单模板（通用版）

把一款游戏派给**一个 general 子代理**时，用下面这段做 prompt。子代理会自己读 `WRITING-BRIEF.md` 与技能、联网重写、落盘。**一个子代理只写一篇。**

## 1. 通用派单模板

```
读 `/root/Game_Wiki/WRITING-BRIEF.md` 并**严格按其执行**（它写了该读哪些技能、怎么写、怎么自检与回报）。
目标作品：{{TITLE}}（英文名 {{ALT}}；IP：{{IP}}）。{{首发年份/版本限定，如无则删}}
{{⚠️ 消歧或边界提示，如无则删}}
输出到精确路径：`/root/Game_Wiki/{{FILE}}`。
```

字段来源：`index.json` 每一行就是 `{title, title_alt, ip, file, public_id}`。

## 2. 需要人工补的提示（模板里留空、按游戏补）

派单前给子代理补一句边界/消歧说明，常见三类：

- **同名/多版本消歧**：如同一 IP 下两个「现代战争」（2007 / 2019）、重制版 vs 原版（生化危机 2/3/4 重制版）、合集 vs 单作。
- **本地化标题**：GameAtlas 标题可能有错别字（如「重置版」应为「重制版」）或旧译名。
- **未发售/新作**：写「以检索到的官方最新信息为准，未发售则显式说明」。

## 3. 生成待写清单

```bash
python3 scripts/dispatch.py                  # 全部待写（自动排除已落盘、排除另一代理负责的 IP）
python3 scripts/dispatch.py --ip 合金装备     # 只出某个 IP
python3 scripts/dispatch.py --limit 12       # 只出前 N 个
python3 scripts/dispatch.py --include-other  # 连另一代理负责的 IP 也列出
```

## 4. 派单要求（发给子代理前的自检）

- 一篇一代理；目标路径必须与 `index.json` 的 `file` 完全一致（回推靠它定位）。
- 默认同一批并行 **≤ 12 篇**，跑完一批再下一批（避免并发过高导致中途报错）。
- 子代理**只写指定文件**，不碰其它条目、不碰 GameAtlas。
- 落盘后按 `CHECKLIST.md` 勾选、`git commit`（信息含入库篇数与 IP）。
