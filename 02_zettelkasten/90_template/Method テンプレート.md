---
id:
title:

type: method
layer: domain

domain: []
concept_type: [operational]

relations:
# - type: applied_to
#   to:
# - type: produces
#   to:
# - type: depends_on
#   to:
# - type: uses
#   to:
# - type: evaluated_by
#   to:

tags: [method]
status: draft
---

# Summary
手法の要約（1〜2行）

---

# Purpose
- 何を達成するか（Objective）
- 成功条件（KPI）

---

# Inputs（前提入力）
- データ：
- 仮定：
- リソース：
- 前提条件（Preconditions）：

---

# Outputs（成果物）
- 生成物：
- 期待効果：
- 品質基準（Acceptance Criteria）：

---

# Steps（手順）

## Step 1
- 

## Step 2
- 

## Step 3
- 

※各Stepは「入力→処理→出力」を明示

---

# Control Points（検証点：必須）

- Check 1：
- Check 2：
- Check 3：

※失敗時の分岐（再実行/中断/代替）を明記

---

# Mechanism（なぜ効くか）

## Phase 1：初期状態
- 

## Phase 2：Trigger
- 

## Phase 3：Transformation（必須）
- 何がどう変わるか

## Phase 4：Amplification
- 効果が広がる理由

## Phase 5：Outcome
- 最終的な効果

---

# Constraints（制約）

- 時間：
- コスト：
- リスク：
- 適用範囲：

---

# Relation（Graph用・本文）

- [[Method]] #applied_to [[Case]]
- [[Method]] #produces [[Output]]
- [[Method]] #depends_on [[Mechanism]]
- [[Method]] #uses [[Resource/Tool]]
- [[Method]] #evaluated_by [[Metric]]

※最低5個以上

---

# Knowledge Graph Links（必須）

## Mechanism
- [[フィードバックメカニズム]]
- [[情報非対称メカニズム]]
- （最低2つ）

## Decision
- [[Decision]]

## Actor
- [[Actor]]

---

# Performance（評価）

- 効果（Impact）：
- コスト（Cost）：
- 再現性（Repeatability）：
- スケーラビリティ：

---

# Failure Modes（失敗パターン）

- パターン1：
- パターン2：

---

# Examples（必須）

- [[Case]]
- [[Event]]

---

# Pattern接続

- [[Method]] #instantiates [[Pattern]]
- [[Pattern]] #uses [[Method]]

---

# Weak Method Check（必須）

- [ ] InputsとOutputsが明確
- [ ] Stepsが実行可能
- [ ] 検証点がある
- [ ] Mechanismが説明されている
- [ ] 制約が明示されている

※未達 → 再設計

---

# Implications

- 
- 
- 

---

# 一行圧縮

-