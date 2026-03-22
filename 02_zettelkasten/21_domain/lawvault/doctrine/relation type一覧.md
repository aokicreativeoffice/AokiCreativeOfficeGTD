# 1. 設計原則
- 構造（structure）
- 推論（inference）
- 証拠（evidence）
- 制御（control）

# 2. relation type一覧
## ①構造系（静的関係）
```yaml
- type: is_a
  description: 上位概念（taxonomy）

- type: part_of
  description: 構成要素

- type: has_part
  description: 部分を持つ

- type: instance_of
  description: 抽象 → 具体
```

## ② 推論系（最重要）
```yaml
- type: requires
  description: 争点 → 必要事実

- type: inferred_from
  description: 主要事実 ← 間接事実

- type: leads_to
  description: 原因 → 結果

- type: equivalent_to
  description: 同義

- type: contradicts
  description: 矛盾

- type: strengthens
  description: 推論を強める

- type: weakens
  description: 推論を弱める
```

## ③ 証拠系
```yaml
- type: evidenced_by
  description: 事実 ← 証拠

- type: supports
  description: 補助的支持

- type: refutes
  description: 反証

- type: derived_from
  description: データ由来
```

## ④ 制御系（思考制御）
```yaml
- type: depends_on
  description: 争点依存関係

- type: excludes
  description: 排他関係

- type: parallel_to
  description: 並列関係

- type: precedes
  description: 時系列・手順

- type: used_in
  description: Engineで使用

- type: applies_to
  description: 適用対象
```