import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

from openai import OpenAI

VAULT_ROOT = Path(r"G:\マイドライブ\AokiCreativeOfficeGTD")
INDEX_PATH = VAULT_ROOT / "ai-assistant" / "data" / "vault_index.json"

# 必要なら変更
DEFAULT_MODEL = "gpt-5.2-codex"

TOKEN_RE = re.compile(r"[A-Za-z0-9_\-一-龠ぁ-んァ-ン]+")

from dotenv import load_dotenv
load_dotenv()

# まずは手動辞書で query expansion
SYNONYM_MAP = {
    "kernel": ["普遍原理", "原理", "中核原理", "基本原理"],
    "普遍原理": ["kernel", "原理", "中核原理"],
    "structure": ["構造", "思考構造", "分析構造", "手順"],
    "構造": ["structure", "思考構造", "分析構造", "手順"],
    "method": ["方法", "手法", "分析手法"],
    "方法": ["method", "手法", "分析手法"],
    "world model": ["世界モデル", "世界理解", "モデル"],
    "世界モデル": ["world model", "世界理解", "モデル"],
    "hub": ["ハブ", "中核ノート", "親ノート"],
    "ハブ": ["hub", "中核ノート", "親ノート"],
    "observation": ["観察", "観測", "知覚", "スキャン"],
    "観察": ["observation", "観測", "知覚", "スキャン"],
    "problem": ["問題", "課題", "論点"],
    "問題": ["problem", "課題", "論点"],
    "reading": ["読書", "読解", "解釈"],
    "読書": ["reading", "読解", "解釈"],
    "personality": ["人格", "自己", "性格"],
    "人格": ["personality", "自己", "性格"],
    "sales": ["営業", "商談", "提案"],
    "営業": ["sales", "商談", "提案"],
    "diagnostic questions": ["診断質問", "診断問い", "問い"],
    "診断質問": ["diagnostic questions", "診断問い", "問い"],
    "problem type": ["問題類型", "問題タイプ", "類型"],
    "問題類型": ["problem type", "問題タイプ", "類型"],
    "alert": ["アラート", "警告", "異常検知"],
    "アラート": ["alert", "警告", "異常検知"],
    "metric": ["指標", "評価指標", "メトリクス"],
    "指標": ["metric", "評価指標", "メトリクス"],
    "constraint": ["制約", "制限", "ボトルネック"],
    "制約": ["constraint", "制限", "ボトルネック"],
    "incentive": ["インセンティブ", "動機づけ", "誘因"],
    "インセンティブ": ["incentive", "動機づけ", "誘因"],
    "competition": ["競争", "対立", "競合"],
    "競争": ["competition", "対立", "競合"],
    "coordination": ["協調", "調整", "連携"],
    "協調": ["coordination", "調整", "連携"],
    "knowledge system": ["知識体系", "知識システム", "思考OS"],
    "思考os": ["knowledge system", "知識体系", "知識システム"],
    "韓国併合": ["韓国", "併合", "朝鮮", "日韓", "帝国主義", "植民地"],
}


def load_index() -> List[Dict[str, Any]]:
    if not INDEX_PATH.exists():
        raise FileNotFoundError(
            f"Index file not found: {INDEX_PATH}\n"
            "先に make_index.py / build_index.py を実行してください。"
        )
    return json.loads(INDEX_PATH.read_text(encoding="utf-8"))


def tokenize(text: str) -> List[str]:
    return [m.group(0).lower() for m in TOKEN_RE.finditer(text)]


def safe_join(values: List[str]) -> str:
    return " ".join(v for v in values if isinstance(v, str))


def expand_query(query: str) -> Tuple[str, List[str]]:
    expanded_terms: List[str] = [query]
    added_terms: List[str] = []

    q_lower = query.lower()
    query_tokens = tokenize(query)

    for key, synonyms in SYNONYM_MAP.items():
        key_lower = key.lower()

        # フレーズ一致
        if key_lower in q_lower:
            for s in synonyms:
                if s not in expanded_terms:
                    expanded_terms.append(s)
                    added_terms.append(s)
            continue

        # トークン一致
        for token in query_tokens:
            if token == key_lower:
                for s in synonyms:
                    if s not in expanded_terms:
                        expanded_terms.append(s)
                        added_terms.append(s)

    expanded_query = " ".join(dict.fromkeys(expanded_terms))
    return expanded_query, added_terms


def build_search_text(note: Dict[str, Any]) -> str:
    filename = note.get("filename", "")
    stem = note.get("stem", "")
    path = note.get("path", "")

    headings = safe_join(
        [h.get("title", "") for h in note.get("headings", []) if isinstance(h, dict)]
    )
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
    headings = [
        str(h.get("title", "")).lower()
        for h in note.get("headings", [])
        if isinstance(h, dict)
    ]
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

    if matched and len(matched) == len(set(query_terms)):
        score += 10

    if "hub" in filename or "hub" in stem:
        score += 4
    if "readme" in filename:
        score += 4
    if "index" in filename:
        score += 2

    return score, matched


def search_notes(
    notes: List[Dict[str, Any]], query: str, top_n: int = 8
) -> List[Tuple[int, Dict[str, Any], Dict[str, int]]]:
    ranked = []

    for note in notes:
        score, matched = score_note(note, query)
        if score > 0:
            ranked.append((score, note, matched))

    ranked.sort(key=lambda x: x[0], reverse=True)
    return ranked[:top_n]


def format_context(results: List[Tuple[int, Dict[str, Any], Dict[str, int]]]) -> str:
    chunks = []

    for i, (score, note, matched) in enumerate(results, start=1):
        frontmatter = note.get("frontmatter", {})
        layer = frontmatter.get("layer", "") if isinstance(frontmatter, dict) else ""
        note_type = frontmatter.get("note_type", "") if isinstance(frontmatter, dict) else ""

        headings = note.get("headings", [])
        heading_titles = [h.get("title", "") for h in headings[:8] if isinstance(h, dict)]
        body = str(note.get("text", ""))[:4000]

        chunk = f"""
[DOCUMENT {i}]
path: {note.get("path", "")}
filename: {note.get("filename", "")}
stem: {note.get("stem", "")}
score: {score}
layer: {layer}
note_type: {note_type}
matched_terms: {matched}
headings: {heading_titles}

content:
{body}
"""
        chunks.append(chunk.strip())

    return "\n\n".join(chunks)


def build_prompt(user_question: str, expanded_query: str, context: str) -> str:
    return f"""
あなたはユーザー専用のVaultアシスタントです。
与えられたVault文脈を最優先で使って回答してください。

ルール:
1. まずVault文脈に基づいて答える
2. Vaultにないことは「Vault上では未確認」と明示する
3. 一般知識で補う場合は、それが補足だと明示する
4. 可能ならノート同士の関係も説明する
5. 参照した path も示す
6. 日本語で答える
7. 元質問と展開語の両方を踏まえて解釈する

ユーザーの元の質問:
{user_question}

検索用に展開したクエリ:
{expanded_query}

Vault文脈:
{context}
""".strip()


def ask_openai(prompt: str, model: str = DEFAULT_MODEL) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY が設定されていません。")

    print("[4/5] OpenAI API 呼び出し開始...")
    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model=model,
        input=prompt,
    )

    print("[5/5] OpenAI API 呼び出し完了")

    if hasattr(response, "output_text") and response.output_text:
        return response.output_text

    try:
        return response.output[0].content[0].text
    except Exception:
        return str(response)


def main() -> None:
    try:
        print("[1/5] index 読み込み中...")
        notes = load_index()
        print(f"      notes={len(notes)}")

        if len(sys.argv) >= 2:
            user_question = " ".join(sys.argv[1:]).strip()
        else:
            user_question = input("vault> ").strip()

        if not user_question:
            print("質問が空です。")
            return

        expanded_query, added_terms = expand_query(user_question)

        print("[2/5] 関連ノート検索中...")
        print(f"      original_query = {user_question}")
        print(f"      expanded_query = {expanded_query}")
        if added_terms:
            print(f"      added_terms = {added_terms}")

        results = search_notes(notes, expanded_query, top_n=8)
        print(f"      hits={len(results)}")

        if not results:
            print("Vault内に関連ノートが見つかりませんでした。")
            return

        print("[3/5] context 作成中...")
        context = format_context(results)
        prompt = build_prompt(user_question, expanded_query, context)

        answer = ask_openai(prompt)

        print("\n" + "=" * 80)
        print("QUESTION")
        print(user_question)
        print("=" * 80)
        print("EXPANDED QUERY")
        print(expanded_query)
        print("=" * 80)
        print("TOP MATCHES")
        for i, (score, note, matched) in enumerate(results, start=1):
            print(f"[{i}] score={score} path={note.get('path','')} matched={matched}")
        print("=" * 80)
        print("ANSWER")
        print(answer)
        print("=" * 80)

    except Exception as e:
        print("[ERROR]")
        print(type(e).__name__, str(e))


if __name__ == "__main__":
    main()