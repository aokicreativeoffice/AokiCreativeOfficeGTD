---
note_type: permanent
layer: structure
status: stable
maturity: canonical
domain: tourism
related:
  - [[Tourism Site Structure]]
  - [[Tourism Experience Model]]
  - [[Tourist Capability Model]]
  - [[Tourism Object Taxonomy]]
created: 2026-03-10
updated: 2026-03-10
tags:
  - tourism
  - attractiveness
  - evaluation
---

# Tourism Attractiveness Model

Tourism Attractiveness Model は、観光地の魅力度を説明するモデルである。

観光地の価値は

- 観光資源
- 体験構造
- 探索難易度
- 観光客能力

の相互作用によって決まる。

---

# 核心

観光体験価値

**= 観光地魅力 × 観光客能力 ÷ 探索難易度**

---

# 基本構造

```mermaid
graph TD

Attraction["観光地魅力"]
Capability["観光客能力"]
Difficulty["探索難易度"]
Experience["観光体験価値"]

Attraction --> Experience
Capability --> Experience
Difficulty --> Experience
```

---

# 観光地魅力  
Attraction

観光地そのものの魅力。

## 要素

- 景観
- 歴史
- 文化
- 活動
- 社会交流

リンク

[[Tourism Object Taxonomy]]

---

# 魅力構造

```mermaid
graph TD

Landscape["景観"]
History["歴史"]
Culture["文化"]
Activity["体験"]
Social["社会交流"]

Landscape --> Attraction
History --> Attraction
Culture --> Attraction
Activity --> Attraction
Social --> Attraction
```

---

# 探索難易度  
Difficulty

観光地の理解や探索の難しさ。

## 要素

- 地理的難易度
- 情報不足
- 文化理解の難しさ
- アクセス難易度
- 空間構造

---

# 探索難易度構造

```mermaid
graph TD

Access["アクセス難易度"]
Space["空間複雑性"]
Information["情報不足"]
CultureDiff["文化理解難度"]

Access --> Difficulty
Space --> Difficulty
Information --> Difficulty
CultureDiff --> Difficulty
```

---

# 観光客能力  
Capability

観光客が観光地を体験できる能力。

リンク

[[Tourist Capability Model]]

能力例

- 空間探索能力
- 知識能力
- 文化理解能力
- 社会交流能力
- 身体能力

---

# 滞在時間との関係

観光地魅力は滞在時間に影響する。

```mermaid
graph TD

Experience["体験価値"]
Stay["滞在時間"]
Return["再訪意欲"]

Experience --> Stay
Experience --> Return
```

---

# 観光地タイプ別の特徴

## テーマパーク

特徴

- 高魅力
- 低難易度

初心者でも楽しめる。

---

## 歴史都市

特徴

- 高魅力
- 中難易度

知識があるほど楽しめる。

---

## 秘境

特徴

- 中魅力
- 高難易度

探索能力が必要。

---

# モデル例

京都

```mermaid
graph TD

Attraction["高魅力"]
Difficulty["中難易度"]
Capability["観光客能力"]

Attraction --> Experience
Capability --> Experience
Difficulty --> Experience
```

---

# 観光設計への応用

観光地の価値を上げる方法

## 1 魅力を上げる

- 景観保全
- 文化価値提示
- 体験開発

## 2 難易度を下げる

- 案内整備
- ガイド
- 情報提供

## 3 能力を補助する

- ガイドツアー
- 解説
- 教育

---

# 観光OSでの位置

```mermaid
graph TD

WorldModel["Japan World Model"]
Kernel["Culture Kernel"]
Site["Tourism Site Structure"]
Capability["Tourist Capability Model"]
Experience["Tourism Experience Model"]
Attractiveness["Tourism Attractiveness Model"]
Explanation["Tourism Explanation"]

WorldModel --> Kernel
Kernel --> Site
Site --> Capability
Capability --> Experience
Experience --> Attractiveness
Attractiveness --> Explanation
```

---

# 一言で言うと

観光地の価値は

**魅力・難易度・観光客能力のバランスで決まる。**