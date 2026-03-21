---
id:
title:

type: solution
layer: domain

domain: []
concept_type: [solution]

relations:
# - type: addresses
#   to:
# - type: uses
#   to:
# - type: implemented_by
#   to:
# - type: evaluated_by
#   to:
# - type: instantiates
#   to:

tags: [solution]
status: draft
---

# Summary
解決策の要約（1〜2行）

---

# Target Problem（必須）
- 問題定義：
- 適用スコープ：
- 成功条件（KPI）：

---

# Preconditions（前提条件）
- 必須条件：
- 望ましい条件：
- 非適用条件（重要）：

---

# Mechanism（なぜ効くか：必須）

## Phase 1：初期状態
- 

## Phase 2：Trigger
- 何を変えるか

## Phase 3：Transformation（必須）
- 状態変数がどう変わるか

## Phase 4：Amplification
- 効果が広がる理由（フィードバック）

## Phase 5：Outcome
- 期待される結果

---

# Structure（設計）
- コンポーネント：
- 役割分担：
- インターフェース：

---

# Implementation（Method接続：必須）
- 使用する手法：
  - [[Method A]]
  - [[Method B]]

- 実行フロー（概要）：
  1.
  2.
  3.

---

# Expected Outcome（期待結果）

## ■ 定量
- KPI：

## ■ 定性
- 影響：

---

# Trade-offs（副作用）
- コスト増：
- リスク：
- 他領域への影響：

---

# Evaluation（評価）

## ■ 指標
- Impact：
- Cost：
- Risk：
- Feasibility：

## ■ 想定スコア
- High / Medium / Low（または数値）

---

# Variants（代替案）
- Variant A：
- Variant B：

---

# Failure Modes（失敗条件：重要）
- 条件不足：
- 逆効果になるケース：

---

# Relation（Graph用・本文）

- [[Solution]] #addresses [[Problem]]
- [[Solution]] #uses [[Mechanism]]
- [[Solution]] #implemented_by [[Method]]
- [[Solution]] #evaluated_by [[Metric]]
- [[Solution]] #instantiates [[Pattern]]

※最低5個以上

---

# Knowledge Graph Links（必須）

## Mechanism
- [[フィードバックメカニズム]]
- [[ロックインメカニズム]]
- （最低2つ）

## Decision
- [[Decision]]

## Method
- [[Method]]

---

# Pattern接続

- [[Solution]] #instantiates [[Pattern]]
- [[Pattern]] #uses [[Solution]]

---

# Examples（必須）
- [[Case]]
- [[Decision]]

---

# Weak Solution Check（必須）

- [ ] 対象問題が明確
- [ ] Mechanismが5フェーズで説明されている
- [ ] Methodに落とせる
- [ ] 副作用が書かれている
- [ ] 失敗条件がある

※未達 → 再設計

---

# Implications
- 
- 
- 

---

# 一行圧縮

-