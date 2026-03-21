---
note_type: permanent
layer: structure
status: stable
maturity: canonical
domain: tourism
related:
  - [[Tourism Object Taxonomy]]
  - [[Tourism Explanation Structure]]
  - [[Japan World Model]]
  - [[Japan Aesthetics]]
created: 2026-03-10
updated: 2026-03-10
tags:
  - tourism
  - structure
  - site_model
---

# Tourism Site Structure

Tourism Site Structure は、  
観光地がどのように

- 観光体験
- 滞在時間
- 満足度

を生み出すかを説明する構造モデルである。

観光地は単なる場所ではなく、

**資源 → 体験 → 感情 → 滞在**

というプロセスで成立する。

---

# 核心

観光地の魅力は

**観光資源 × 体験構造**

によって生まれる。

---

# 基本構造

```mermaid
graph TD

Resource["観光資源"]
Experience["観光体験"]
Emotion["感情反応"]
Stay["滞在行動"]

Resource --> Experience
Experience --> Emotion
Emotion --> Stay
```

---

# 観光資源

観光地に存在する要素。

## 資源タイプ

- 景観
- 歴史
- 文化
- 活動
- 自然
- 社会

リンク

[[Tourism Object Taxonomy]]

---

# 体験構造

観光客が実際に行う行動。

```mermaid
graph TD

See["見る"]
Walk["歩く"]
Learn["知る"]
Do["体験する"]
Interact["交流する"]
```

---

# 感情反応

体験は感情を生む。

主な観光感情

- 美しい
- 面白い
- 神聖
- 歴史を感じる
- 非日常

```mermaid
graph TD

Experience["体験"]
Emotion["感情"]

Experience --> Emotion
```

---

# 滞在行動

感情は観光行動に影響する。

- 滞在時間
- 再訪意欲
- 推薦

```mermaid
graph TD

Emotion["感情"]
Stay["滞在時間"]
Return["再訪"]
Recommend["推薦"]

Emotion --> Stay
Emotion --> Return
Emotion --> Recommend
```

---

# 観光地の構造

観光地は次の層を持つ。

```mermaid
graph TD

Resource["観光資源"]
Space["空間構造"]
Route["移動"]
Experience["体験"]

Resource --> Space
Space --> Route
Route --> Experience
```

---

# 観光地の評価構造

観光地の魅力は

**資源 × 体験密度**

で決まる。

```mermaid
graph TD

Resource["資源量"]
Density["体験密度"]
Attraction["魅力度"]

Resource --> Attraction
Density --> Attraction
```

---

# 探索難易度との関係

観光地の魅力は  
観光客の能力との関係でも変化する。

```mermaid
graph TD

Attraction["本来魅力"]
Difficulty["探索難易度"]
Skill["観光客能力"]

Attraction --> ExperienceValue
Difficulty --> ExperienceValue
Skill --> ExperienceValue
```

---

# 観光地構造の例

京都

```mermaid
graph TD

Temple["寺院"]
Garden["庭園"]
Street["町並み"]
Food["飲食"]

Temple --> Experience
Garden --> Experience
Street --> Experience
Food --> Experience
```

---

# 観光説明との関係

```mermaid
graph TD

Site["観光地"]
Explanation["観光説明"]

Site --> Explanation
Explanation --> Experience
```

---

# 観光OSでの位置

```mermaid
graph TD

WorldModel["World Model"]
Kernel["Culture Kernel"]
SiteStructure["Tourism Site Structure"]
Explanation["Tourism Explanation"]

WorldModel --> Kernel
Kernel --> SiteStructure
SiteStructure --> Explanation
```

---

# 一言で言うと

観光地とは

**資源が体験を生み、体験が感情を生み、感情が滞在を生む場所**

である。