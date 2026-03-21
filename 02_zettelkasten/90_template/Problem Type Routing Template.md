# Problem Type Routing Template（強制版）

## ■ 目的
Questionを適切な思考モードに分岐し、
出力の構造と品質を保証する

---

# ■ Step 1：Problem Type判定

- explanation（解説）
- analysis（原因分析）
- decision（意思決定）
- design（設計）

※ [[Routing Engine]] + [[Routing Matrics Table]] を使用

---

# ■ Step 2：Routing（分岐）

---

## ■ explanation（解説）

### ■ 実行フロー（強制）

1. [[Mechanism Template]]
2. [[Knowledge Graph Auto Linking]]
3. [[Weak Explanation Check]]

---

### ■ 出力構造

- Concept
- Structure
- Mechanism（5フェーズ必須）
- Relation（5以上）
- Pattern
- Implication
- 一行圧縮

---

### ■ 禁止

- Solution生成
- Decision実行

---

### ■ 停止条件

Weak Check通過で終了

---

## ■ analysis（原因分析）

### ■ 実行フロー（強制）

1. 原因分解（3層）
2. [[Mechanism Template]]
3. [[Pattern Extraction Engine]]
4. [[Knowledge Graph Auto Linking]]
5. [[Weak Explanation Check]]

---

### ■ 出力構造

- 問題定義
- 表層原因
- 中間原因
- 深層構造
- 転換点
- 反証
- Pattern

---

### ■ 強制条件

- 単一原因禁止
- 因果3層必須
- 転換点必須

---

### ■ 停止条件

Pattern抽出完了

---

## ■ decision（意思決定）

### ■ 実行フロー（フル）

1. [[Pattern Extraction Engine]]（既存検索）
2. Solution生成（最低3案）
3. Instance化
4. Decision（※[[Scoring Function]]必須）
5. Execution
6. [[Execution Log Learning]]
7. [[Case to Pattern Promotion]]
8. [[Knowledge Graph Auto Linking]]
9. [[Weak Explanation Check]]

---

### ■ 出力構造

- Problem Definition
- Options（3以上）
- Criteria
- Scoring
- Decision
- Rationale
- Execution Plan
- Outcome（後更新）
- Learning
- Pattern

---

### ■ 強制条件

- Option3以上
- スコア数値化
- 実行可能性

---

### ■ 停止条件

Execution + Learning完了

---

## ■ design（設計）

### ■ 実行フロー（強制）

1. 要件定義
2. 制約定義
3. Structure設計
4. Component分解
5. Flow設計
6. リスク分析
7. [[Knowledge Graph Auto Linking]]
8. [[Weak Explanation Check]]

---

### ■ 出力構造

- 要件
- 制約
- アーキテクチャ
- コンポーネント
- フロー
- リスク
- 拡張性

---

### ■ 強制条件

- 抽象と具体の両方を含む
- 実装可能である

---

### ■ 停止条件

Structure + Flow確定

---

# ■ 共通強制ルール（最重要）

## ■ 必須通過ノード

すべての分岐で以下を必ず通過：

- [[Mechanism Template]]
- [[Knowledge Graph Auto Linking]]
- [[Weak Explanation Check]]

---

## ■ Relation条件

- Relation 5個以上
- Mechanismリンク 2個以上
- Patternリンク 1個以上

---

## ■ 禁止事項

- 単一因果
- 転換点なし
- Relation不足

---

## ■ 失敗時処理

条件未達の場合：

```text
出力禁止 → Diagnostic Questionsへ戻る