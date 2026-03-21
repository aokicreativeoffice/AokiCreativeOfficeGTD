---
id:
title:

type: structure
layer: domain

domain: []
concept_type: [structure]

relations:
# - type: part_of
#   to:
# - type: composed_of
#   to:
# - type: constrains
#   to:
# - type: depends_on
#   to:
# - type: enables
#   to:

tags: [structure]
status: draft
---

# Summary
構造の定義（1〜2行）

---

# Scope & Boundary（重要）
- スケール（個人 / 組織 / 国家 / 市場）
- 境界（どこまで含むか）
- 外部環境：

---

# Components（要素）
- 要素A：
- 要素B：
- 要素C：

---

# State Variables（状態変数：必須）
- 変数1：
- 変数2：
- 変数3：

※何が変わると構造の振る舞いが変わるか

---

# Topology（配置・関係）

## ■ 関係タイプ
- 階層（Hierarchy）：
- ネットワーク（Network）：
- フロー（Flow）：

## ■ 主要接続
- A → B：
- B → C：

---

# Constraints（制約）

## ■ ハード制約
- 法規 / 物理 / 資源

## ■ ソフト制約
- 規範 / 慣習 / インセンティブ

---

# Behavior（構造が生む性質）

- 安定性（Stability）：
- 変化耐性（Resilience）：
- 非線形性（Nonlinearity）：
- ボトルネック：

---

# Mechanism接続（必須）

この構造で働く主なメカニズム：

- [[フィードバックメカニズム]]
- [[ロックインメカニズム]]
- [[協調失敗メカニズム]]

---

# Relation（Graph用・本文）

- [[Structure]] #composed_of [[Component]]
- [[Structure]] #part_of [[上位構造]]
- [[Structure]] #constrains [[Actor]]
- [[Structure]] #enables [[Mechanism]]
- [[Structure]] #depends_on [[Resource/Environment]]

※最低5個以上

---

# Knowledge Graph Links（必須）

## Actor
- [[Actor]]

## Mechanism
- [[Mechanism]]

## Pattern
- [[Pattern]]

---

# Dynamics（時間変化：重要）

- どのように変化するか
- フェーズ変化（臨界点）：

---

# Failure Modes（崩壊条件）

- 崩壊条件：
- 歪みが出る条件：

---

# Examples（必須）

- [[Case]]
- [[Event]]

---

# Pattern接続

- [[Structure]] #instantiates [[Pattern]]
- [[Pattern]] #uses [[Structure]]

---

# Weak Structure Check（必須）

- [ ] 境界が定義されている
- [ ] 状態変数がある
- [ ] 制約が明示されている
- [ ] Mechanismと接続されている
- [ ] 振る舞いが説明されている

※未達 → 再構成

---

# Implications

- 
- 
- 

---

# 一行圧縮

-