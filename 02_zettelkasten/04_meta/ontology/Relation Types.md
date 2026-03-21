# Relation Types

## 0. 目的
ノート間の関係を統一的に表現し、
- 検索可能性
- 推論可能性
- 再利用性
を最大化する

---

## 1. Relation分類（最上位）

Relationは4系統に分ける：

1. 構造（Structure）
2. 因果（Causality）
3. 抽象（Abstraction）
4. 運用（Operational）

### ■ 1. 構造系（Structure Relations）

#### is_a
- 上位概念との関係
- taxonomy

例：
Pattern is_a Knowledge
#### part_of
- 全体の構成要素

例：
Routing Engine part_of Thinking Engine
#### instance_of
- 実例

例：
Decision:求人戦略 instance_of Decision
#### has_component
- 内部構成

例：
Solution has_component Mechanism

---

### ■ 2. 因果系（Causality Relations）

#### causes
- 原因 → 結果

例：
情報非対称 causes 市場失敗
#### enables
- 実現条件

例：
データ蓄積 enables パターン抽出
#### constrains
- 制約

例：
コスト constrains Solution
#### amplifies
- 増幅

例：
SNS amplifies 情報拡散

#### reduces
- 抑制

例：
ルール reduces 不確実性

---

### ■ 4. 抽象系（Abstraction Relations）

#### abstracts
- 抽象化

例：
Pattern abstracts Case
#### generalizes
- 一般化

例：
Mechanism generalizes Pattern
#### specializes
- 特化

例：
Solution specializes Pattern
#### maps_to
- 対応関係

例：
Pattern maps_to Solution
### ■ 4. 運用系（Operational Relations）

#€## used_in
- 使用箇所

例：
Pattern used_in Solution
#### applied_to
- 適用対象

例：
Method applied_to Problem
#### evaluated_by
- 評価方法

例：
Solution evaluated_by Scoring Function
#### selected_by
- 選択

例：
Solution selected_by Decision

#### executed_as
- 実行形態

例：
Decision executed_as Execution
#### recorded_as
- 記録

例：
Execution recorded_as Case

---

## transformed_to
- 変換

例：
Case transformed_to Pattern

### ■ 5. Knowledge Graph系（横断）

#### related_to
- 緩い関係（最終手段）
#### similar_to
- 類似
#### contrasts_with
- 対比

---

# 2. 禁止ルール

❌ related_toの乱用  
❌ 同じ意味のrelationを複数作る  
❌ directionを曖昧にする  

---

# 3. 推奨フォーマット

```yaml
relations:
  - type: causes
    from: 情報非対称
    to: 市場失敗

  - type: used_in
    from: Pattern:供給制限
    to: Solution:受注制限