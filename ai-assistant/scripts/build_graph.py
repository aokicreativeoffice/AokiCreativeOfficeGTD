import json
import re
from collections import Counter, defaultdict
from pathlib import Path

VAULT_ROOT = Path(r"G:\マイドライブ\AokiCreativeOfficeGTD")
INDEX_PATH = VAULT_ROOT / "ai-assistant" / "data" / "vault_index.json"
OUTPUT_DIR = VAULT_ROOT / "ai-assistant" / "data" / "graph"

SANITIZE_RE = re.compile(r"[^A-Za-z0-9_]")


def load_index():
    if not INDEX_PATH.exists():
        raise FileNotFoundError(
            f"Index file not found: {INDEX_PATH}\n"
            "先に make_index.py / build_index.py を実行してください。"
        )
    return json.loads(INDEX_PATH.read_text(encoding="utf-8"))


def normalize_name(name: str) -> str:
    return name.strip().lower()


def mermaid_id(text: str) -> str:
    base = SANITIZE_RE.sub("_", text)
    if not base or not base[0].isalpha():
        base = "N_" + base
    return base[:80]


def mermaid_label(text: str) -> str:
    return text.replace('"', "'")


def build_graph(notes):
    stem_to_note = {}
    path_to_note = {}
    normalized_stem_to_stem = {}

    for note in notes:
        stem = note.get("stem", "").strip()
        path = note.get("path", "").strip()
        if stem:
            stem_to_note[stem] = note
            normalized_stem_to_stem[normalize_name(stem)] = stem
        if path:
            path_to_note[path] = note

    outgoing = defaultdict(list)
    incoming = defaultdict(list)
    unresolved_links = []
    link_counter = Counter()

    for note in notes:
        src = note.get("stem", "").strip()
        src_path = note.get("path", "").strip()
        if not src:
            continue

        links = note.get("wikilinks", [])
        seen_targets = set()

        for raw_target in links:
            target = raw_target.strip()
            if not target:
                continue

            resolved = None

            # 1. stem で一致
            normalized_target = normalize_name(Path(target).name)
            if normalized_target in normalized_stem_to_stem:
                resolved = normalized_stem_to_stem[normalized_target]

            # 2. path 的指定を stem に寄せる
            if resolved is None:
                target_name = Path(target).stem.strip()
                if normalize_name(target_name) in normalized_stem_to_stem:
                    resolved = normalized_stem_to_stem[normalize_name(target_name)]

            if resolved is None:
                unresolved_links.append({
                    "source_stem": src,
                    "source_path": src_path,
                    "raw_target": raw_target,
                })
                continue

            if resolved == src:
                continue

            if resolved in seen_targets:
                continue
            seen_targets.add(resolved)

            outgoing[src].append(resolved)
            incoming[resolved].append(src)
            link_counter[resolved] += 1

    all_stems = sorted(stem_to_note.keys())

    isolated = []
    for stem in all_stems:
        out_deg = len(outgoing.get(stem, []))
        in_deg = len(incoming.get(stem, []))
        if out_deg == 0 and in_deg == 0:
            isolated.append(stem)

    hubs = []
    for stem in all_stems:
        hubs.append({
            "stem": stem,
            "path": stem_to_note[stem].get("path", ""),
            "incoming_count": len(incoming.get(stem, [])),
            "outgoing_count": len(outgoing.get(stem, [])),
            "total_degree": len(incoming.get(stem, [])) + len(outgoing.get(stem, [])),
            "layer": stem_to_note[stem].get("frontmatter", {}).get("layer", ""),
            "note_type": stem_to_note[stem].get("frontmatter", {}).get("note_type", ""),
        })

    hubs.sort(key=lambda x: (x["incoming_count"], x["total_degree"]), reverse=True)

    return {
        "nodes": [
            {
                "stem": stem,
                "path": stem_to_note[stem].get("path", ""),
                "layer": stem_to_note[stem].get("frontmatter", {}).get("layer", ""),
                "note_type": stem_to_note[stem].get("frontmatter", {}).get("note_type", ""),
                "incoming_count": len(incoming.get(stem, [])),
                "outgoing_count": len(outgoing.get(stem, [])),
            }
            for stem in all_stems
        ],
        "edges": [
            {"source": src, "target": dst}
            for src in sorted(outgoing.keys())
            for dst in sorted(outgoing[src])
        ],
        "incoming": {k: sorted(v) for k, v in incoming.items()},
        "outgoing": {k: sorted(v) for k, v in outgoing.items()},
        "isolated": isolated,
        "hubs": hubs,
        "unresolved_links": unresolved_links,
    }


def save_json(graph):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUTPUT_DIR / "vault_graph.json"
    out.write_text(json.dumps(graph, ensure_ascii=False, indent=2), encoding="utf-8")
    return out


def save_reports(graph):
    reports = {}

    isolated_path = OUTPUT_DIR / "isolated_notes.txt"
    isolated_path.write_text(
        "\n".join(graph["isolated"]) if graph["isolated"] else "(none)",
        encoding="utf-8",
    )
    reports["isolated"] = isolated_path

    hubs_path = OUTPUT_DIR / "hub_candidates.txt"
    with hubs_path.open("w", encoding="utf-8") as f:
        for i, hub in enumerate(graph["hubs"][:100], start=1):
            f.write(
                f"{i:03d} | in={hub['incoming_count']:3d} | out={hub['outgoing_count']:3d} | "
                f"deg={hub['total_degree']:3d} | layer={hub['layer']} | type={hub['note_type']} | "
                f"{hub['path']}\n"
            )
    reports["hubs"] = hubs_path

    unresolved_path = OUTPUT_DIR / "unresolved_links.txt"
    with unresolved_path.open("w", encoding="utf-8") as f:
        if not graph["unresolved_links"]:
            f.write("(none)\n")
        else:
            for item in graph["unresolved_links"]:
                f.write(
                    f"{item['source_path']} -> {item['raw_target']}\n"
                )
    reports["unresolved"] = unresolved_path

    return reports


def save_mermaid(graph, top_n=40):
    selected = graph["hubs"][:top_n]
    selected_stems = {x["stem"] for x in selected}

    mermaid_lines = ["flowchart TD"]

    for node in selected:
        stem = node["stem"]
        node_id = mermaid_id(stem)
        label = mermaid_label(stem)
        mermaid_lines.append(f'    {node_id}["{label}"]')

    edge_count = 0
    for edge in graph["edges"]:
        src = edge["source"]
        dst = edge["target"]
        if src in selected_stems and dst in selected_stems:
            mermaid_lines.append(
                f"    {mermaid_id(src)} --> {mermaid_id(dst)}"
            )
            edge_count += 1

    if edge_count == 0:
        mermaid_lines.append("    A[No major hub-to-hub edges found]")

    mermaid_text = "\n".join(mermaid_lines)

    mermaid_path = OUTPUT_DIR / "vault_graph_top_hubs.mmd"
    mermaid_path.write_text(mermaid_text, encoding="utf-8")

    md_path = OUTPUT_DIR / "vault_graph_top_hubs.md"
    md_path.write_text(f"```mermaid\n{mermaid_text}\n```", encoding="utf-8")

    return mermaid_path, md_path


def main():
    notes = load_index()
    graph = build_graph(notes)

    graph_json = save_json(graph)
    reports = save_reports(graph)
    mermaid_mmd, mermaid_md = save_mermaid(graph, top_n=40)

    print(f"Nodes: {len(graph['nodes'])}")
    print(f"Edges: {len(graph['edges'])}")
    print(f"Isolated notes: {len(graph['isolated'])}")
    print(f"Unresolved links: {len(graph['unresolved_links'])}")
    print(f"Saved JSON -> {graph_json}")
    print(f"Saved isolated report -> {reports['isolated']}")
    print(f"Saved hub report -> {reports['hubs']}")
    print(f"Saved unresolved report -> {reports['unresolved']}")
    print(f"Saved Mermaid -> {mermaid_mmd}")
    print(f"Saved Mermaid Markdown -> {mermaid_md}")


if __name__ == "__main__":
    main()