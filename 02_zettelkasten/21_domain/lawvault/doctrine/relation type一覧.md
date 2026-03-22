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