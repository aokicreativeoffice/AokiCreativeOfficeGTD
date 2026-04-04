# Knowledge Graph Auto Linking

## ■ 目的
ノート生成時に自動でrelation接続する

---

## ■ 接続ルール

### ① 型接続（必須）
- Case → is_instance_of → Concept
- Concept → is_a → 上位概念

---

### ② Mechanism接続（必須）
以下から最低2つ選択：

- フィードバックメカニズム
- ロックインメカニズム
- 協調失敗メカニズム
- 情報非対称メカニズム
- 正当性メカニズム

---

### ③ Pattern接続（必須）
- Case → instantiates → Pattern
- Pattern → abstracts → Case

---

### ④ 因果接続
- A causes B
- A leads_to B

---

### ⑤ 対比接続（任意）
- contrasts_with

---

## ■ Link Candidates（辞書）

### Mechanism
- [[フィードバックメカニズム]]
- [[ロックインメカニズム]]
- [[協調失敗メカニズム]]
- [[02_zettelkasten/Zettelkasten Engine/02_knowledge/world_model/mechanism/information/情報非対称メカニズム]]
- [[正当性メカニズム]]

### Pattern
- [[正面突破失敗パターン]]
- [[局地成功非展開パターン]]
- [[同期依存パターン]]
- [[外交暴露パターン]]

---

## ■ 最低条件

- Relation 5個以上
- Mechanism 2個以上
- Pattern 1個以上

---

## ■ Pattern

「リンクは後付けではなく生成時に付与する」