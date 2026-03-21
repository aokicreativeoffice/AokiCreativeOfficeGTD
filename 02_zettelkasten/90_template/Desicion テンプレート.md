---
id:
title:

type: case
layer: domain

domain: []
concept_type: [event, operational]

relations:
# - type: selected_by
#   to:
# - type: evaluates
#   to:
# - type: depends_on
#   to:
# - type: instantiates
#   to:
# - type: influences
#   to:

tags: []
status: draft
---

# Summary
意思決定の概要（1〜2行で圧縮）

---

# Problem Definition（必須）
- 何を解くのか
- 制約（時間 / コスト / リスク）
- 成功条件（KPI）

---

# Options（必須）
選択肢（最低3案）

- Option A：
- Option B：
- Option C：

---

# Criteria（評価基準）

## ■ 指標
- 効果（Impact）
- コスト（Cost）
- リスク（Risk）
- 実行容易性（Feasibility）
- 再現性（Repeatability）

## ■ 重み（0〜1）
- Impact：
- Cost：
- Risk：
- Feasibility：
- Repeatability：

---

# Scoring Function（必須）

## ■ 数式
Score = Σ (重み × 指標)

## ■ 評価表

| Option | Impact | Cost | Risk | Feasibility | Total |
|--------|--------|------|------|------------|-------|
| A      |        |      |      |            |       |
| B      |        |      |      |            |       |
| C      |        |      |      |            |       |

---

# Evaluation（評価）

- 各Optionの特徴
- トレードオフ

---

# Decision（採用案）

- 採用：
- 代替案：

---

# Rationale（理由）

- なぜこの案が最適か
- 他案が劣る理由

---

# Mechanism（決定の因果）

## Phase 1：初期状態
- 

## Phase 2：Trigger
- 判断が必要になった理由

## Phase 3：Transformation
- 評価により優劣が確定

## Phase 4：Amplification
- 実行により影響が拡大

## Phase 5：Outcome
- 最終結果

---

# Execution Plan（実行）

- Step1：
- Step2：
- Step3：

---

# Outcome（後で更新）

## ■ 実績
- KPI達成度：

## ■ 成功/失敗
- 成功 / 失敗

---

# Learning（学習）

## ■ 成功要因
- 

## ■ 失敗要因
- 

## ■ 改善点
- 

---

# Pattern（抽出）

## ■ パターン名
-

## ■ 構造
A → B → C → D

---

# Relation（Graph用・本文）

- [[Decision]] #evaluates [[Option]]
- [[Decision]] #selected_by [[Actor]]
- [[Decision]] #depends_on [[Mechanism]]
- [[Decision]] #instantiates [[Pattern]]
- [[Decision]] #influences [[Outcome]]

※最低5個以上

---

# Knowledge Graph Links（必須）

## Mechanism
- [[フィードバックメカニズム]]
- [[ロックインメカニズム]]
- （最低2つ）

## Pattern
- [[○○パターン]]

---

# Weak Decision Check（必須）

- [ ] Optionが3つ以上ある
- [ ] Criteriaに重みがある
- [ ] スコアが数値化されている
- [ ] 理由が比較になっている
- [ ] 実行可能である

※未達 → 再設計

---

# 一行圧縮

-