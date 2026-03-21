import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

VAULT_ROOT = Path(r"G:\マイドライブ\AokiCreativeOfficeGTD")
INDEX_PATH = VAULT_ROOT / "ai-assistant" / "data" / "vault_index.json"

TOKEN_RE = re.compile(r"[A-Za-z0-9_\-一-龠ぁ-んァ-ン]+")


def load_index() -> List[Dict[str, Any]]:
    if not INDEX_PATH.exists():
        raise FileNotFoundError(
            f"Index file not found: {INDEX_PATH}\n"
            "先に build_index.py を実行してください。"
        )
    return json.loads(INDEX_PATH.read_text(encoding="utf-8"))


def tokenize(text: str) -> List[str]:
    return [m.group(0).lower() for m in TOKEN_RE.finditer(text)]


def safe_join(values: List[str]) -> str:
    return " ".join(v for v in values if isinstance(v, str))


def build_search_text(note: Dict[str, Any]) -> str:
    filename = note.get("filename", "")
    stem = note.get("stem", "")
    path = note.get("path", "")
    headings = safe_join([h.get("title", "") for h in note.get("headings", []) if isinstance(h, dict)])
    wikilinks = safe_join(note.get("wikilinks", []))
    tags = safe_join(note.get("tags", []))

    frontmatter = note.get("frontmatter", {})
    frontmatter_text_parts = []
    if isinstance(frontmatter, dict):
        for k, v in frontmatter.items():
            if isinstance(v, list):
                frontmatter_text_parts.append(k)
                frontmatter_text_parts.extend(str(x) for x in v)
            else:
                frontmatter_text_parts.append(k)
                frontmatter_text_parts.append(str(v))
    frontmatter_text = safe_join(frontmatter_text_parts)

    body = note.get("text", "")

    return " \n ".join(
        [
            filename,
            stem,
            path,
            headings,
            wikilinks,
            tags,
            frontmatter_text,
            body,
        ]
    ).lower()


def score_note(note: Dict[str, Any], query: str) -> Tuple[int, Dict[str, int]]:
    query_terms = tokenize(query)
    if not query_terms:
        return 0, {}

    search_text = build_search_text(note)
    score = 0
    matched: Dict[str, int] = {}

    filename = str(note.get("filename", "")).lower()
    stem = str(note.get("stem", "")).lower()
    path = str(note.get("path", "")).lower()
    headings = [str(h.get("title", "")).lower() for h in note.get("headings", []) if isinstance(h, dict)]
    tags = [str(t).lower() for t in note.get("tags", [])]
    wikilinks = [str(w).lower() for w in note.get("wikilinks", [])]
    frontmatter = note.get("frontmatter", {})
    frontmatter_blob = ""
    if isinstance(frontmatter, dict):
        frontmatter_blob = " ".join(f"{k} {v}" for k, v in frontmatter.items()).lower()

    for term in query_terms:
        term_count = search_text.count(term)
        if term_count == 0:
            continue

        term_score = term_count

        if term in filename:
            term_score += 12
        if term in stem:
            term_score += 10
        if term in path:
            term_score += 8
        if any(term in heading for heading in headings):
            term_score += 8
        if any(term == tag or term in tag for tag in tags):
            term_score += 6
        if any(term in link for link in wikilinks):
            term_score += 5
        if term in frontmatter_blob:
            term_score += 6

        matched[term] = term_score
        score += term_score

    # query の全語が含まれるノートは少し持ち上げる
    if matched and len(matched) == len(set(query_terms)):
        score += 10

    # hub / readme / index 系を少し持ち上げる
    filename_l = filename
    stem_l = stem
    if "hub" in filename_l or "hub" in stem_l:
        score += 4
    if "readme" in filename_l:
        score += 4
    if "index" in filename_l:
        score += 2

    return score, matched


def search_notes(notes: List[Dict[str, Any]], query: str, top_n: int = 10) -> List[Tuple[int, Dict[str, Any], Dict[str, int]]]:
    ranked: List[Tuple[int, Dict[str, Any], Dict[str, int]]] = []

    for note in notes:
        score, matched = score_note(note, query)
        if score > 0:
            ranked.append((score, note, matched))

    ranked.sort(key=lambda x: x[0], reverse=True)
    return ranked[:top_n]


def make_snippet(note: Dict[str, Any], query: str, snippet_len: int = 180) -> str:
    text = str(note.get("text", "")).replace("\n", " ")
    if not text:
        return ""

    query_terms = tokenize(query)
    lower_text = text.lower()

    best_pos = -1
    for term in query_terms:
        pos = lower_text.find(term)
        if pos != -1:
            best_pos = pos
            break

    if best_pos == -1:
        best_pos = 0

    start = max(0, best_pos - snippet_len // 2)
    end = min(len(text), start + snippet_len)
    snippet = text[start:end].strip()

    if start > 0:
        snippet = "..." + snippet
    if end < len(text):
        snippet = snippet + "..."

    return snippet


def print_results(results: List[Tuple[int, Dict[str, Any], Dict[str, int]]], query: str) -> None:
    if not results:
        print("一致するノートは見つかりませんでした。")
        return

    print(f"\nQuery: {query}\n")
    for i, (score, note, matched) in enumerate(results, start=1):
        path = note.get("path", "(unknown path)")
        frontmatter = note.get("frontmatter", {})
        layer = frontmatter.get("layer", "") if isinstance(frontmatter, dict) else ""
        note_type = frontmatter.get("note_type", "") if isinstance(frontmatter, dict) else ""

        print("=" * 80)
        print(f"[{i}] score={score}  path={path}")
        if layer or note_type:
            print(f"    layer={layer}  note_type={note_type}")
        print(f"    matched={matched}")

        headings = note.get("headings", [])
        if headings:
            heading_titles = [h.get("title", "") for h in headings[:5] if isinstance(h, dict)]
            print(f"    headings={heading_titles}")

        snippet = make_snippet(note, query)
        if snippet:
            print(f"    snippet={snippet}")

    print("=" * 80)


def main() -> None:
    notes = load_index()

    if len(sys.argv) >= 2:
        query = " ".join(sys.argv[1:]).strip()
    else:
        query = input("query> ").strip()

    if not query:
        print("クエリが空です。")
        return

    results = search_notes(notes, query, top_n=10)
    print_results(results, query)


if __name__ == "__main__":
    main()