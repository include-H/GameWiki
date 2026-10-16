#!/usr/bin/env python3
"""Game_Wiki → GameAtlas 生产库 回推脚本。

用法:
  python3 scripts/push.py check                 # 登录 + 对账 roster + 文件体检 + 探测 wiki 端点
  python3 scripts/push.py push --dry-run        # 只读：算出「本机 vs 远端」差异分布，不写
  python3 scripts/push.py push --limit 1        # 只推第 1 条（冒烟）
  python3 scripts/push.py push                  # 全量推送（每条 PUT 后回读校验；差异跳过可用 --force 覆盖）
  python3 scripts/push.py status                # 看最近一次运行的小结

约定（README「回推 GameAtlas」节）:
  PUT /api/games/{public_id}/wiki  body {"content", "change_summary"}
  覆盖写、不可轻易撤销；按 index.json 的 public_id 定位，无 public_id 的条目（人工扩写）不推。
凭据: 环境变量 GA_PASSWORD，或 /root/WikiAltas/.secrets/credentials.md（GameAtlas 生产库行）。
日志: push-log/push-<runid>.jsonl（已 gitignore）。
"""
import argparse, hashlib, http.cookiejar, json, os, re, sys, time, urllib.error, urllib.request
from datetime import datetime

BASE = os.environ.get("GA_BASE", "http://192.168.1.4:3000")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(ROOT, "index.json")
LOGDIR = os.path.join(ROOT, "push-log")
SECRETS = "/root/WikiAltas/.secrets/credentials.md"


def load_password() -> str:
    if os.environ.get("GA_PASSWORD"):
        return os.environ["GA_PASSWORD"]
    txt = open(SECRETS, encoding="utf-8").read()
    m = re.search(r"GameAtlas 生产库[^\n]*?密码:\s*`([^`]+)`", txt)
    if not m:
        raise SystemExit("找不到 GA 凭据（env GA_PASSWORD 或 %s）" % SECRETS)
    return m.group(1)


class GA:
    def __init__(self):
        self.jar = http.cookiejar.CookieJar()
        self.op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.jar))
        env = self.call("POST", "/api/auth/login", {"password": load_password()})
        if not env.get("success"):
            raise SystemExit("登录失败：%s" % env.get("error"))
        if not (env.get("data") or {}).get("is_admin"):
            print("⚠️ 登录成功但 is_admin=False，覆盖写可能被拒")

    def call(self, method, path, body=None):
        data = json.dumps(body, ensure_ascii=False).encode("utf-8") if body is not None else None
        req = urllib.request.Request(BASE + path, data=data, method=method,
                                     headers={"Content-Type": "application/json"})
        try:
            with self.op.open(req, timeout=90) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as e:
            raw = e.read().decode("utf-8", "replace")
            try:
                return json.loads(raw)
            except Exception:
                return {"success": False, "error": "HTTP %s: %s" % (e.code, raw[:300])}
        except Exception as e:
            return {"success": False, "error": "%s: %s" % (type(e).__name__, e)}

    def wiki(self, pid):
        env = self.call("GET", "/api/games/%s/wiki" % pid)
        if not env.get("success"):
            return env, None
        d = env.get("data")
        if isinstance(d, dict):
            return env, d.get("content")
        return env, d if isinstance(d, str) else None


def entries():
    return json.load(open(INDEX, encoding="utf-8"))


def sha(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest() if s is not None else None


def norm(s):
    """GA 入库会去掉末尾换行，比较前统一归一。"""
    return s.rstrip() if s is not None else s


def read_text(file):
    p = os.path.join(ROOT, file)
    t = open(p, "r", encoding="utf-8").read()
    return t


def reconcile(ga):
    idx = entries()
    mine = {e["public_id"]: e for e in idx if e.get("public_id")}
    env = ga.call("GET", "/api/games/all")
    got = {g["public_id"]: g for g in (env.get("data") or [])}
    print("index 带 public_id: %d | 生产库: %d" % (len(mine), len(got)))
    a, b = sorted(set(mine) - set(got)), sorted(set(got) - set(mine))
    print("index 有 / GA 无:", a or "—")
    print("GA 有 / index 无:", b or "—")
    mm = [(e["title"], got[p]["title"]) for p, e in mine.items()
          if p in got and e["title"] != got[p]["title"]]
    print("标题错配:", mm if mm else "—")
    return mine, got


def cmd_check(_):
    ga = GA(); print("✅ 登录成功（admin）")
    mine, _ = reconcile(ga)
    # 文件体检
    bad, small, empty = [], [], []
    for p, e in sorted(mine.items(), key=lambda kv: kv[1]["ip"] + kv[1]["file"]):
        try:
            t = read_text(e["file"])
        except Exception as ex:
            bad.append((e["file"], str(ex))); continue
        n = len(t.encode("utf-8"))
        if not t.strip():
            empty.append(e["file"])
        elif n < 1000:
            empty.append(e["file"])
        elif n < 3000:
            small.append((e["file"], n))
    print("文件读取失败: %s" % (bad or "—"))
    print("空/超小(<1KB): %s" % (empty or "—"))
    print("偏小(1–3KB, 留意): %s" % (small or "—"))
    # 探测 wiki 端点
    for flag in (True, False):
        e = next(x for x in mine.values() if x.get("has_content") is flag)
        env, content = ga.wiki(e["public_id"])
        print("探测 %s（%s, has_content=%s）: success=%s, len=%s"
              % (e["file"], e["public_id"][:8], flag, env.get("success"),
                 len(content) if content is not None else None))
        if content:
            print("   远端头部: %s" % content[:100].replace("\n", "⏎"))


def plan(ga, args):
    """返回 [(pid, entry, local_text, size, remote_text)]"""
    idx = entries()
    sel = [e for e in idx if e.get("public_id")]
    if args.only:
        sel = [e for e in sel if args.only in e.get("ip", "") or args.only in e.get("file", "")]
    sel.sort(key=lambda e: (e.get("ip", ""), e["file"]))
    if args.limit:
        sel = sel[: args.limit]
    out = []
    for e in sel:
        try:
            t = read_text(e["file"])
        except Exception as ex:
            out.append((e["public_id"], e, None, 0, None, "read: %s" % ex))
            continue
        env, remote = ga.wiki(e["public_id"])
        if not env.get("success"):
            out.append((e["public_id"], e, t, len(t.encode()), remote, "get: %s" % env.get("error")))
        else:
            out.append((e["public_id"], e, t, len(t.encode()), remote, None))
        time.sleep(args.sleep)
    return out


def cmd_push(args):
    ga = GA(); print("✅ 登录成功（admin）· 目标 %s" % BASE)
    os.makedirs(LOGDIR, exist_ok=True)
    runid = datetime.now().strftime("%Y%m%d-%H%M%S")
    logf = open(os.path.join(LOGDIR, "push-%s.jsonl" % runid), "a", encoding="utf-8")
    rows = plan(ga, args)
    diff = same = fail = 0
    fails = []
    summary = "全量联网重写稿回推（Game_Wiki 内容仓 · %s）" % datetime.now().strftime("%Y-%m-%d")
    for pid, e, text, size, remote, err in rows:
        rec = {"ts": datetime.now().isoformat(timespec="seconds"), "public_id": pid,
               "file": e["file"], "title": e["title"], "bytes": size}
        if err:
            rec.update(status="error", error=err); fail += 1; fails.append(rec)
        elif text is not None and not text.strip():
            rec.update(status="skip-empty"); same += 1
        elif norm(remote) == norm(text) and not args.force and not args.dry_run:
            rec.update(status="skip-equal")
            same += 1
        elif args.dry_run:
            rec.update(status="would-push", remote_bytes=len(remote.encode()) if remote else 0,
                       remote_sha=sha(remote), local_sha=sha(text))
            diff += 1
        else:
            env = ga.call("PUT", "/api/games/%s/wiki" % pid,
                          {"content": text, "change_summary": summary})
            if not env.get("success"):
                rec.update(status="put-failed", error=env.get("error")); fail += 1; fails.append(rec)
            else:
                venv, vtext = ga.wiki(pid)
                ok = venv.get("success") and norm(vtext) == norm(text)
                rec.update(status="pushed" if ok else "verify-mismatch",
                           local_sha=sha(text), remote_sha=sha(vtext))
                if ok:
                    diff += 1
                else:
                    rec["error"] = "回读不一致"
                    fail += 1; fails.append(rec)
            time.sleep(args.sleep)
        logf.write(json.dumps(rec, ensure_ascii=False) + "\n"); logf.flush()
        print("[%s] %-14s %s（%d B → 远端 %s）"
              % (rec["status"], e["title"], e["file"], size,
                 "一致" if rec["status"] == "skip-equal" else
                 "推送" if rec["status"] == "pushed" else
                 "待推送" if rec["status"] == "would-push" else rec["status"]))
    logf.close()
    s = {"runid": runid, "mode": "dry-run" if args.dry_run else "push", "total": len(rows),
         "written_or_would": diff, "already_equal": same, "failed": fail, "fails": fails}
    json.dump(s, open(os.path.join(LOGDIR, "push-%s.summary.json" % runid), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("\n== 小结 ==  共 %d | 写入/将写入 %d | 已一致跳过 %d | 失败 %d"
          % (len(rows), diff, same, fail))
    if fails:
        for f in fails:
            print("  ✗ %s: %s" % (f["file"], f.get("error")))
    sys.exit(1 if fail else 0)


def cmd_status(_):
    files = sorted(f for f in os.listdir(LOGDIR) if f.endswith(".summary.json")) if os.path.isdir(LOGDIR) else []
    if not files:
        print("push-log/ 还没有运行记录"); return
    s = json.load(open(os.path.join(LOGDIR, files[-1]), encoding="utf-8"))
    print(json.dumps(s, ensure_ascii=False, indent=1)[:2000])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check")
    p = sub.add_parser("push")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--limit", type=int)
    p.add_argument("--only", help="只推 IP/路径包含该串的条目")
    p.add_argument("--force", action="store_true", help="远端已一致也覆盖")
    p.add_argument("--sleep", type=float, default=0.12)
    sub.add_parser("status")
    args = ap.parse_args()
    {"check": cmd_check, "push": cmd_push, "status": cmd_status}[args.cmd](args)


if __name__ == "__main__":
    main()
