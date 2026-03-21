import re
import json
from pathlib import Path

print("RUNNING MAKE_INDEX")

VAULT_ROOT = Path(r"G:\マイドライブ\AokiCreativeOfficeGTD")
OUTPUT_PATH = VAULT_ROOT / "ai-assistant" / "data" / "vault_index.json"

WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
TAG_RE = re.compile(r"(?<!\w)#([A-Za-z0-9_\-/]+)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)


def split_frontmatter(text: str):
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[1].strip(), parts[2].strip()
    return "", text


def parse_frontmatter(frontmatter_text: str):
    data = {}
    for line in frontmatter_text.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            data[k.strip()] = v.strip()
    return data


def extract_headings(text: str):
    headings = []
    for m in HEADING_RE.finditer(text):
        headings.append({
            "level": len(m.group(1)),
            "title": m.group(2).strip()
        })
    return headings


def extract_wikilinks(text: str):
    links = []
    for m in WIKILINK_RE.finditer(text):
        raw = m.group(1).strip()
        target = raw.split("|", 1)[0].strip()
        links.append(target)
    return sorted(set(links))


def extract_tags(text: str):
    return sorted(set(TAG_RE.findall(text)))


def read_text_safely(path: Path):
    encodings = ["utf-8", "utf-8-sig", "cp932", "shift_jis", "latin-1"]

    for enc in encodings:
        try:
            return path.read_text(encoding=enc), enc
        except UnicodeDecodeError:
            continue
        except Exception as e:
            print(f"[ERROR] {path} : {e}")
            return None, None

    print(f"[SKIP] decode failed: {path}")
    return None, None


def build_index():
    notes = []
    skipped = []

    for path in VAULT_ROOT.rglob("*.md"):
        if ".obsidian" in path.parts:
            continue
        if "old" in path.parts:
            continue
        if "ai-assistant" in path.parts:
            continue

        text, used_encoding = read_text_safely(path)
        if text is None:
            skipped.append(str(path))
            continue

        frontmatter_text, body = split_frontmatter(text)
        frontmatter = parse_frontmatter(frontmatter_text)

        note = {
            "path": str(path.relative_to(VAULT_ROOT)).replace("\\", "/"),
            "filename": path.name,
            "stem": path.stem,
            "frontmatter": frontmatter,
            "headings": extract_headings(body),
            "wikilinks": extract_wikilinks(body),
            "tags": extract_tags(body),
            "encoding": used_encoding,
            "text": body[:20000],
        }
        notes.append(note)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(
        json.dumps(notes, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    print(f"Indexed {len(notes)} notes")
    print(f"Saved -> {OUTPUT_PATH}")

    if skipped:
        print("\nSkipped files:")
        for s in skipped:
            print(" -", s)


if __name__ == "__main__":
    build_index()