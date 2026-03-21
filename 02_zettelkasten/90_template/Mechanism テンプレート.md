---
id:
title:

type: mechanism
layer: domain

domain: []
concept_type: [mechanism]

relations:
# - type: is_a
#   to:
# - type: causes
#   to:
# - type: depends_on
#   to:
# - type: amplifies
#   to:
# - type: interacts_with
#   to:

tags: [mechanism]
status: draft
---

# Summary
メカニズムの定義（1〜2行で圧縮）

---

# Concept
- 何を説明するメカニズムか
- 適用範囲

---

# Structure
- 主体：
- 状態変数：
- 入力：
- 出力：

---

# Mechanism（強制テンプレ）

## Phase 1：初期状態
- 状況
- 前提条件

## Phase 2：Trigger
- 何が起きたか
- 誰が何をしたか

## Phase 3：Transformation（必須）
- 何が変わったか（状態変数）
- 変換の核

## Phase 4：Amplification
- なぜ影響が広がるか
- フィードバック（正/負）

## Phase 5：Outcome
- 最終結果

---

# Conditions（重要）

## ■ 発動条件
- 

## ■ 非発動条件
- 

---

# Relation（Graph用・本文）

- [[Mechanism]] #is_a [[上位メカニズム]]
- [[Mechanism]] #causes [[Outcome]]
- [[Mechanism]] #depends_on [[Structure]]
- [[Mechanism]] #amplifies [[Effect]]
- [[Mechanism]] #interacts_with [[Mechanism]]

※最低5個以上

---

# Knowledge Graph Links（必須）

## 上位概念
- [[社会メカニズム]]
- [[経済メカニズム]]

## 関連メカニズム
- [[フィードバックメカニズム]]
- [[ロックインメカニズム]]
- [[情報非対称メカニズム]]
- [[協調失敗メカニズム]]

---

# Examples（必須）

- [[Case]]
- [[Event]]

---

# Pattern接続

- [[Mechanism]] #enables [[Pattern]]
- [[Pattern]] #uses [[Mechanism]]

---

# Weak Mechanism Check（必須）

- [ ] Transformationが明確
- [ ] 状態変数が定義されている
- [ ] 単一因果ではない
- [ ] Amplificationが検討されている
- [ ] 条件（発動/非発動）がある

※未達 → 再構成

---

# Pattern

「変換点が不明な説明はメカニズムではない」

---

# 一行圧縮

-