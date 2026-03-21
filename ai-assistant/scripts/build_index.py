import json
from pathlib import Path

VAULT_ROOT = Path(r"G:\マイドライブ\AokiCreativeOfficeGTD")
INDEX_PATH = VAULT_ROOT / "ai-assistant" / "data" / "vault_index.json"

def load_index():
    return json.loads(INDEX_PATH.read_text(encoding="utf-8"))

def score_note(note, query):
    q_terms = [t.lower() for t in query.split() if t.strip()]
    text = (
        note["filename"] + " " +
        note["stem"] + " " +
        " ".join(h["title"] for h in note["headings"]) + " " +
        " ".join(note["wikilinks"]) + " " +
        note["text"][:3000]
    ).lower()

    score = 0
    for term in q_terms:
        score += text.count(term)
    return score

def search(query, top_n=10):
    notes = load_index()
    ranked = []
    for note in notes:
        s = score_note(note, query)
        if s > 0:
            ranked.append((s, note))
    ranked.sort(key=lambda x: x[0], reverse=True)
    return ranked[:top_n]

if __name__ == "__main__":
    query = input("query> ").strip()
    results = search(query)
    for score, note in results:
        print(f"[{score}] {note['path']}")