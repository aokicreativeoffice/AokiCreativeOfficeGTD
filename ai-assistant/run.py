import os
import json
import re
from datetime import date, datetime
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# ---------- config ----------
REPO_ROOT = Path(__file__).resolve().parents[2]
GTD_ROOT = REPO_ROOT / "gtd"
ZETTEL_ROOT = REPO_ROOT / "zettelkasten" / "permanent"

SCAN = {
    "inbox": GTD_ROOT / "inbox",
    "projects": GTD_ROOT / "projects",
    "next_actions": GTD_ROOT / "next-actions",
    "waiting": GTD_ROOT / "waiting",
    "someday": GTD_ROOT / "someday",
}

MAX_FILES = {
    "inbox": 30,
    "projects": 80,
    "next_actions": 80,
    "waiting": 30,
    "someday": 30,
}

MAX_CHARS_PER_FILE = 4000


# ---------- helpers ----------
def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace")


def list_md_files(folder: Path, limit: int):
    if not folder.exists():
        return []
    files = sorted(folder.rglob("*.md"), key=lambda x: x.stat().st_mtime, reverse=True)
    return files[:limit]


def pack_section(name: str, folder: Path, limit: int) -> str:
    items = []
    for f in list_md_files(folder, limit):
        txt = read_text(f)[:MAX_CHARS_PER_FILE]
        rel = f.relative_to(REPO_ROOT).as_posix()
        items.append(f"---\nFILE: {rel}\n{txt}\n")
    return f"## {name}\n" + "\n".join(items) + "\n"


def pack_zettel(folder: Path, title: str, limit: int) -> str:
    parts = [f"## {title}"]
    files = sorted(folder.rglob("*.md"), key=lambda x: x.stat().st_mtime, reverse=True)
    for f in files[:limit]:
        rel = f.relative_to(REPO_ROOT).as_posix()
        txt = read_text(f)[:2000]
        parts.append(f"---\nFILE: {rel}\n{txt}\n")
    return "\n".join(parts)


def sanitize_filename(s: str) -> str:
    s = re.sub(r"[\\/:*?\"<>|]+", "_", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s[:80]


def make_task_md(task: dict) -> str:
    project = task.get("project") or "_inbox"
    creator = task.get("creator") or "aokicreativeoffice"
    assignee = task.get("assignee") or ""
    status = task.get("status") or "open"
    review_status = task.get("review_status") or "pending"
    effort = task.get("effort") or "スマホで可能"
    done_definition = task.get("done_definition") or "（後で記入）"

    dt = task.get("datetime") or {}
    def g(k): return dt.get(k) or ""

    today = date.today().isoformat()
    title = task.get("title") or "auto_task"

    return f"""---
type: task
status: {status}
review_status: {review_status}
creator: {creator}
assignee: {assignee}
project: {project}
effort: "{effort}"
datetime:
  specified_start: "{g('specified_start')}"
  specified_do: "{g('specified_do')}"
  specified_end: "{g('specified_end')}"
  desired_start: "{g('desired_start')}"
  desired_end: "{g('desired_end')}"
created: {today}
updated: {today}
---

# {title}

## 完了条件
- {done_definition}

## 作業メモ
-

## レビューコメント
-
"""


# ---------- main ----------
def main():
    load_dotenv(REPO_ROOT / ".env")

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY missing")

    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

    system_prompt = read_text(Path(__file__).with_name("prompt.txt"))

    context = []
    for k in SCAN:
        context.append(pack_section(k.upper(), SCAN[k], MAX_FILES[k]))

    zettel = pack_zettel(ZETTEL_ROOT, "PERMANENT_NOTES", 30)

    client = OpenAI(api_key=api_key)

    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": "INBOXを分析し最大3件の次のアクションを出してください。\n\n" + "\n".join(context) + "\n\n" + zettel}
        ],
        temperature=0.3,
    )

    raw = resp.choices[0].message.content.strip()

    data = json.loads(raw)
    tasks = data.get("tasks", [])

    out_dir = GTD_ROOT / "next-actions" / "items"
    out_dir.mkdir(parents=True, exist_ok=True)

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    for i, t in enumerate(tasks, 1):
        md = make_task_md(t)
        fname = f"auto_{stamp}_{i:02d}_{sanitize_filename(t.get('title','task'))}.md"
        (out_dir / fname).write_text(md, encoding="utf-8")

    print(f"[OK] Generated {len(tasks)} task files.")


if __name__ == "__main__":
    main()