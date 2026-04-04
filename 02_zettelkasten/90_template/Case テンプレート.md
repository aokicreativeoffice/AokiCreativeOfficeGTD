---
id:
title:

type: case
layer: domain

domain: []
concept_type: [event]

relations:
# - type: is_instance_of
#   to:
# - type: causes
#   to:
# - type: depends_on
#   to:
# - type: instantiates
#   to:

tags: []
status: draft
---

# Summary
事例概要（1〜2行で圧縮）

---

# Context
背景（構造・前提条件）

---

# Actors
関与主体（複数可）
- 主体：
- 対象：
- 第三者：

---

# Event（Structure）
何が起きたか（時系列）

1.
2.
3.

---

# Outcome
結果（短期 / 長期）

---

# Mechanism（強制テンプレ）

## Phase 1：初期状態
- 

## Phase 2：Trigger
- 

## Phase 3：Transformation（必須）
- 何が変わったか
- 状態変数の変化

## Phase 4：Amplification
- なぜ影響が拡大したか
- フィードバックの有無

## Phase 5：Outcome
- 最終結果

---

# Relation（Graph用・本文側）

- [[タイトル]] #is_instance_of [[Concept]]
- [[タイトル]] #causes [[Outcome]]
- [[タイトル]] #depends_on [[Mechanism]]
- [[タイトル]] #instantiates [[Pattern]]
- [[タイトル]] #contrasts_with [[Case]]

※最低5個以上

---

# Pattern候補

## ■ パターン名
-

## ■ 構造
A → B → C → D

## ■ 抽象化
具体→一般

---

# Knowledge Graph Links（必須）

## Mechanism
- [[フィードバックメカニズム]]
- [[02_zettelkasten/Zettelkasten Engine/02_knowledge/world_model/mechanism/information/情報非対称メカニズム]]
- （最低2つ）

## Pattern
- [[○○パターン]]

---

# Weak Explanation Check（必須）

- [ ] 単一因果になっていない
- [ ] 転換点がある
- [ ] 「なぜ効いたか」が説明されている
- [ ] 時系列が崩れていない
- [ ] 抽象化されている

※1つでも未チェック → 書き直し

---

# Lessons（Implication）

- 
- 
- 

---

# 一行圧縮

-