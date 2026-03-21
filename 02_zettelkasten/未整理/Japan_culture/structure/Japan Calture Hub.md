---
note_type: structure
layer: kernel
status: stable
maturity: canonical
domain: japan_culture
created: 2026-03-10
updated: 2026-03-10
related:
  - Japanese Culture
  - Japan World Model
  - Tourism Explanation Structure
---

# Japanese Culture Kernel

Japanese Culture Kernel は、日本文化を理解するための **普遍原理（Kernel）** の集合である。

個別の文化・歴史・観光地は、この Kernel の組み合わせとして説明できる。

目的

- 日本文化の理解
- 観光地の WHY 説明
- 文化構造の把握

---

# Kernel 一覧

## 自然と世界観

- [[Nature Relation]]
- [[Impermanence]]
- [[Seasonal Sensibility]]

---

## 社会原理

- [[Harmony]]
- [[Hierarchy]]
- [[Community Orientation]]
- [[Authority and Legitimacy]]

---

## 宗教・精神

- [[Purity and Pollution]]
- [[Syncretism]]
- [[Ritualization]]

---

## 美意識

- [[Minimalism]]
- [[Spatial Awareness]]
- [[Symbolism]]
- [[Aestheticization of Life]]

---

## 文化生成

- [[Craftsmanship]]
- [[Embodied Practice]]
- [[Narrative Tradition]]

---

## 文化進化

- [[Adaptation]]
- [[Continuity]]

---

## 行動様式

- [[Controlled Emotion]]

---

# Kernel の役割

Kernel は次の層で機能する。

---

# Kernel間の関係性
```mermaid
graph TD

%% 世界観
Nature["自然共生"]
Impermanence["無常"]
Season["季節感"]

%% 社会
Harmony["和"]
Hierarchy["階層秩序"]
Community["共同体"]
Authority["正統性"]
Emotion["感情制御"]

%% 宗教・儀礼
Purity["清浄"]
Ritual["儀礼化"]
Syncretism["習合"]

%% 美意識
Minimalism["簡素美"]
Space["間"]
Symbol["象徴"]
EmotionSense["情緒"]

%% 文化生成
Craft["職人精神"]
Embodied["身体知"]
Narrative["物語"]
Adaptation["適応"]
Continuity["継続"]
LifeAesthetic["生活美"]

%% 世界観→美意識
Nature --> Season
Nature --> Purity
Impermanence --> Minimalism
Impermanence --> EmotionSense
Season --> EmotionSense

%% 社会構造
Community --> Harmony
Hierarchy --> Harmony
Authority --> Hierarchy
Harmony --> Emotion

%% 宗教文化
Purity --> Ritual
Ritual --> Symbol
Syncretism --> Ritual

%% 美意識
Minimalism --> Space
Space --> LifeAesthetic
EmotionSense --> LifeAesthetic

%% 技術文化
Embodied --> Craft
Craft --> Continuity
Continuity --> Authority

%% 文化進化
Adaptation --> Syncretism
Adaptation --> Continuity

%% 物語
Narrative --> Authority
Narrative --> EmotionSense
```
