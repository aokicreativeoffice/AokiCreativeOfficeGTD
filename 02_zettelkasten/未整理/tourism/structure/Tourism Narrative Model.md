---
note_type: permanent
layer: structure
status: stable
maturity: canonical
domain: tourism
related:
  - [[Tourism Explanation Structure]]
  - [[Tourism Experience Model]]
  - [[Tourism Attractiveness Model]]
  - [[Japan World Model]]
  - [[00 Japanese Culture Kernel]]
created: 2026-03-10
updated: 2026-03-10
tags:
  - tourism
  - narrative
  - storytelling
---

# Tourism Narrative Model

Tourism Narrative Model は、観光地の説明を  
**単なる情報ではなく物語として構造化するモデル**である。

観光客の記憶に残る体験は、

**事実 → 意味 → 物語**

の構造を持つ。

---

# 核心

観光体験は

**場所ではなく物語として記憶される**

---

# 基本構造

```mermaid
graph TD

Place["観光地"]
Facts["事実"]
Meaning["意味"]
Story["物語"]
Memory["記憶"]

Place --> Facts
Facts --> Meaning
Meaning --> Story
Story --> Memory
```

---

# 観光物語の構成

観光物語は次の要素から構成される。

```mermaid
graph TD

Setting["舞台"]
Character["人物"]
Event["出来事"]
Conflict["対立"]
Resolution["結末"]

Setting --> Story
Character --> Story
Event --> Story
Conflict --> Story
Resolution --> Story
```

---

# 1 舞台  
Setting

物語の場所。

例

- 京都
- 奈良
- 富士山
- 城

舞台は観光地そのもの。

---

# 2 人物  
Character

物語を動かす人物。

例

- 天皇
- 将軍
- 僧侶
- 職人
- 武士

人物が入ると歴史が生きた物語になる。

---

# 3 出来事  
Event

歴史的出来事や文化的行為。

例

- 戦い
- 建築
- 宗教儀礼
- 政治事件

---

# 4 対立  
Conflict

物語の緊張。

例

- 政治争い
- 戦争
- 宗教対立
- 社会変化

対立があると話が面白くなる。

---

# 5 結末  
Resolution

現在の観光地につながる結果。

例

- 城が残った
- 寺が建立された
- 都市が発展した

---

# 観光説明との関係

観光説明は

**WHAT / HOW / WHY**

から物語に発展する。

```mermaid
graph TD

WHAT["WHAT"]
HOW["HOW"]
WHY["WHY"]
Narrative["物語"]

WHAT --> Narrative
HOW --> Narrative
WHY --> Narrative
```

---

# 観光物語の深度

```mermaid
graph TD

L1["レベル1: 情報"]
L2["レベル2: 意味"]
L3["レベル3: 物語"]
L4["レベル4: 文化理解"]

L1 --> L2
L2 --> L3
L3 --> L4
```

---

# 例

## 城

WHAT  
城

HOW  
防御構造

WHY  
武士の政治拠点

Narrative  
戦国時代の権力争いの舞台

---

## 神社

WHAT  
神社

HOW  
神を祀る

WHY  
自然信仰

Narrative  
地域の信仰と歴史の中心

---

## 京都

WHAT  
古都

HOW  
寺社と町並み

WHY  
日本文化の中心

Narrative  
1000年以上続いた都の物語

---

# 観光OSでの位置

```mermaid
graph TD

WorldModel["Japan World Model"]
Kernel["Culture Kernel"]
Site["Tourism Site Structure"]
Experience["Tourism Experience Model"]
Attractiveness["Tourism Attractiveness Model"]
Narrative["Tourism Narrative Model"]
Explanation["Tourism Explanation"]

WorldModel --> Kernel
Kernel --> Site
Site --> Experience
Experience --> Attractiveness
Attractiveness --> Narrative
Narrative --> Explanation
```

---

# ガイドにとっての意味

良いガイドは

- 情報を説明する人ではない

**物語を語る人である**

---

# 一言で言うと

観光地とは

**物語が宿る場所**

である。