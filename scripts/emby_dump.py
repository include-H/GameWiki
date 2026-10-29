#!/usr/bin/env python3
"""把 Emby 媒体库的全量条目拉成本地 JSONL + 汇总。

用法:
    python3 scripts/emby_dump.py                 # 全库
    python3 scripts/emby_dump.py --library 第九艺术
    python3 scripts/emby_dump.py --out emby-data

环境变量:
    EMBY_BASE   默认 http://192.168.1.4:8081
    EMBY_KEY    默认读 /root/WikiAltas/.secrets/credentials.md 里的 emby 行
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

DEFAULT_BASE = "http://192.168.1.4:8081"
CREDENTIALS = Path("/root/WikiAltas/.secrets/credentials.md")


def resolve_key(explicit: str | None) -> str:
    """按 EMBY_KEY → credentials.md 的顺序取 API Key（不把密钥写进仓库）。"""
    if explicit:
        return explicit
    if os.environ.get("EMBY_KEY"):
        return os.environ["EMBY_KEY"]
    if CREDENTIALS.exists():
        for line in CREDENTIALS.read_text(encoding="utf-8").splitlines():
            if re.search(r"emby", line, re.I):
                m = re.search(r"([0-9a-f]{32})", line, re.I)
                if m:
                    return m.group(1)
    raise SystemExit("找不到 Emby API Key：请设 EMBY_KEY 或写入 credentials.md")
FIELDS = (
    "Path,ProductionYear,Genres,SeriesName,IndexNumber,ParentIndexNumber,"
    "RunTimeTicks,MediaSources,ProviderIds,OfficialRating,CommunityRating,"
    "DateCreated,Overview,Taglines,Studios,People"
)


def api(base: str, key: str, path: str, **params):
    params["api_key"] = key
    url = f"{base.rstrip('/')}{path}?{urllib.parse.urlencode(params)}"
    with urllib.request.urlopen(url, timeout=60) as resp:
        return json.load(resp)


def libraries(base: str, key: str):
    return api(base, key, "/Library/VirtualFolders")


def iter_items(base: str, key: str, parent_id: str, page: int = 500):
    start = 0
    total = None
    while True:
        data = api(
            base, key, "/Items",
            ParentId=parent_id, Recursive="true", Fields=FIELDS,
            EnableImages="false", EnableUserData="false",
            StartIndex=start, Limit=page,
        )
        items = data.get("Items") or []
        if total is None:
            total = data.get("TotalRecordCount", 0)
        yield from items
        start += len(items)
        if not items or start >= total:
            break


def slim(item: dict) -> dict:
    src = (item.get("MediaSources") or [{}])[0]
    streams = src.get("MediaStreams") or []
    video = next((s for s in streams if s.get("Type") == "Video"), {})
    audio = next((s for s in streams if s.get("Type") == "Audio"), {})
    subs = [s for s in streams if s.get("Type") == "Subtitle"]
    return {
        "id": item.get("Id"),
        "name": item.get("Name"),
        "type": item.get("Type"),
        "parent_id": item.get("ParentId"),
        "series_name": item.get("SeriesName"),
        "season": item.get("ParentIndexNumber"),
        "episode": item.get("IndexNumber"),
        "year": item.get("ProductionYear"),
        "official_rating": item.get("OfficialRating"),
        "community_rating": item.get("CommunityRating"),
        "genres": item.get("Genres") or [],
        "studios": [s.get("Name") for s in item.get("Studios") or []],
        "tags": item.get("Tags") or [],
        "overview": item.get("Overview"),
        "taglines": item.get("Taglines") or [],
        "provider_ids": item.get("ProviderIds") or {},
        "date_created": item.get("DateCreated"),
        "path": item.get("Path") or src.get("Path"),
        "size": src.get("Size"),
        "container": src.get("Container"),
        "runtime_ticks": item.get("RunTimeTicks") or src.get("RunTimeTicks"),
        "video": {
            "codec": video.get("Codec"),
            "width": video.get("Width"),
            "height": video.get("Height"),
            "bitrate": video.get("BitRate"),
            "range": video.get("VideoRange"),
            "fps": video.get("RealFrameRate"),
        } if video else None,
        "audio": {
            "codec": audio.get("Codec"),
            "language": audio.get("Language"),
            "channels": audio.get("Channels"),
            "bitrate": audio.get("BitRate"),
        } if audio else None,
        "subtitle_count": len(subs),
    }


def fmt_size(n: int | None) -> str:
    if not n:
        return "-"
    v = float(n)
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if v < 1024 or unit == "TB":
            return f"{v:.1f}{unit}"
        v /= 1024
    return "-"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default=os.environ.get("EMBY_BASE", DEFAULT_BASE))
    ap.add_argument("--key", default=None)
    ap.add_argument("--library", action="append", help="只拉指定库（可重复）")
    ap.add_argument("--out", default="emby-data")
    args = ap.parse_args()
    key = resolve_key(args.key)

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    libs = libraries(args.base, key)
    wanted = set(args.library or [])
    summary = []
    all_rows = []

    for lib in libs:
        name = lib["Name"]
        if wanted and name not in wanted:
            continue
        item_id = lib.get("ItemId")
        if not item_id or not lib.get("Locations"):
            print(f"跳过 {name}（无 ItemId 或非实体库）", file=sys.stderr)
            continue

        rows = [slim(i) for i in iter_items(args.base, key, str(item_id))]
        all_rows.extend({**r, "library": name} for r in rows)
        lib_file = out / f"{name}.jsonl"
        with lib_file.open("w", encoding="utf-8") as f:
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")

        by_type = Counter(r["type"] for r in rows)
        size = sum(r["size"] or 0 for r in rows)
        summary.append({
            "library": name,
            "collection_type": lib.get("CollectionType"),
            "item_count": len(rows),
            "by_type": dict(by_type),
            "total_size": size,
            "locations": lib.get("Locations"),
        })
        print(f"{name:<10} {len(rows):>6} 条  {fmt_size(size):>9}  {dict(by_type)}")

    with (out / "_all.jsonl").open("w", encoding="utf-8") as f:
        for r in all_rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    with (out / "_summary.json").open("w", encoding="utf-8") as f:
        json.dump({
            "generated_at": __import__("datetime").datetime.now().astimezone().isoformat(timespec="seconds"),
            "server": args.base,
            "libraries": summary,
            "total_items": len(all_rows),
            "total_size": sum(s["total_size"] for s in summary),
        }, f, ensure_ascii=False, indent=2)

    total_size = sum(s["total_size"] for s in summary)
    print(f"\n合计 {len(all_rows)} 条 / {fmt_size(total_size)}；输出目录 {out}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
