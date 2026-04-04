---
note_type: template
layer: structure
status: stable
maturity: canonical
template_type: hub
created: 2026-03-14
updated: 2026-03-14
tags:
  - zettelkasten
  - knowledge_graph
  - hub
  - template
  - navigation
---

# Hub Template

このテンプレートは、Knowledge Graph における Hub ノートを  
**目次ではなく、地図・入口・導線・橋の所在表示** として機能させるための標準形である。

Hub は単なる一覧ではない。  
このテンプレートでは、次の4機能を必ず意識する。

1. Map  
2. Entry Point  
3. Traversal Guide  
4. Bridge Locator  

---

# 使用ルール

- Hub には子ノートの全文を書かない
- 中核ノードを優先して載せる
- ノード同士の関係を書く
- 読む順序を示す
- 関連 Hub と Bridge Node を明示する
- index 的一覧は別ノートに分けてもよい

---

# テンプレート本文

```markdown
---
note_type: hub
layer: structure
status: stable
maturity: canonical
hub_type:
domain:
parent_hub:
related_hubs:
tags:
---

# {{Hub Name}}

## 概要
この Hub は [[{{対象領域}}]] に関する主要ノードを束ねるための Hub である。  
主に [[{{node type 1}}]], [[{{node type 2}}]], [[{{node type 3}}]] を中核に扱い、  
[[{{用途1}}]], [[{{用途2}}]], [[{{用途3}}]] の入口として機能する。

---

## この Hub の役割
この Hub は次の役割を持つ。

- **地図**：この領域の骨格を示す
- **入口**：初学者や LLM がどこから入るかを示す
- **導線**：どの順で辿ると理解しやすいかを示す
- **橋の表示**：他領域へ接続する Bridge Node を示す

---

## 中核ノード
この領域の中心となるノード。

- [[{{Core Node 1}}]]
- [[{{Core Node 2}}]]
- [[{{Core Node 3}}]]
- [[{{Core Node 4}}]]
- [[{{Core Node 5}}]]

### 補助ノード
- [[{{Support Node 1}}]]
- [[{{Support Node 2}}]]
- [[{{Support Node 3}}]]

---

## 関係の見取り図
この領域では、主要ノードはおおむね次のように関係する。

- [[{{Core Node 1}}]] は [[{{Core Node 2}}]] の前提・基盤となる
- [[{{Core Node 2}}]] は [[{{Core Node 3}}]] を説明する
- [[{{Core Node 3}}]] は [[{{Core Node 4}}]] に現れやすい
- [[{{Core Node 4}}]] は [[{{Core Node 5}}]] に接続する
- [[{{Bridge Node 1}}]] は他 Hub への横断経路になる

---

## 全体構造

```mermaid
graph TD
    A[{{Hub Name}}] --> B[{{Core Node 1}}]
    A --> C[{{Core Node 2}}]
    A --> D[{{Core Node 3}}]
    A --> E[{{Core Node 4}}]
    A --> F[{{Core Node 5}}]

    B --> C
    C --> D
    D --> E
    C --> F
```

---

## 読む順序

### 初学者向け
- [[{{Core Node 1}}]] → [[{{Core Node 2}}]] → [[{{Core Node 3}}]]

### 分析向け
- [[{{Core Node 2}}]] → [[{{Core Node 4}}]] → [[{{Core Node 5}}]]

### 実務向け
- [[{{Framework or Method Node 1}}]] → [[{{Tool Node 1}}]] → [[{{Representative Case 1}}]]

---

## 代表的な Traversal

### 1. 定義理解ルート
- [[{{Concept Node}}]] → [[{{Contrast Node}}]] → [[{{Anchor Case}}]]

### 2. 分析ルート
- [[{{Question Node}}]] → [[{{Mechanism Node}}]] → [[{{Structure Node}}]] → [[{{Case Node}}]]

### 3. 抽象化ルート
- [[{{Case Node}}]] → [[{{Pattern Node}}]] → [[{{Mechanism Node}}]] → [[{{Kernel Node}}]]

### 4. 横断ルート
- [[{{Bridge Node 1}}]] → [[{{Other Domain Pattern}}]] → [[{{Other Domain Case}}]]

---

## Bridge Node
この Hub から他領域へ移る際の橋となるノード。

- [[{{Bridge Node 1}}]]  
  - 接続先: [[{{Related Hub 1}}]], [[{{Related Hub 2}}]]

- [[{{Bridge Node 2}}]]  
  - 接続先: [[{{Related Hub 3}}]]

- [[{{Bridge Node 3}}]]  
  - 接続先: [[{{Related Hub 4}}]]

---

## Anchor Case
この Hub の抽象ノードを具体に接地させる代表 case。

- [[{{Anchor Case 1}}]]  
  - 何を示すか: [[{{Concept / Pattern / Mechanism 1}}]]

- [[{{Anchor Case 2}}]]  
  - 何を示すか: [[{{Concept / Pattern / Mechanism 2}}]]

- [[{{Anchor Case 3}}]]  
  - 何を示すか: [[{{Bridge Concept 1}}]]

---

## Representative Pattern / Mechanism
この領域を理解するうえで特に重要な型・作動。

### Pattern
- [[{{Pattern 1}}]]
- [[{{Pattern 2}}]]
- [[{{Pattern 3}}]]

### Mechanism
- [[{{Mechanism 1}}]]
- [[{{Mechanism 2}}]]
- [[{{Mechanism 3}}]]

---

## 主要な問い
この Hub から立てやすい問い。

- [[{{Question 1}}]]
- [[{{Question 2}}]]
- [[{{Question 3}}]]
- [[{{Question 4}}]]

---

## 関連 Method / Tool
この領域を扱うときによく使う方法・道具。

### Method
- [[{{Method 1}}]]
- [[{{Method 2}}]]
- [[{{Method 3}}]]

### Tool
- [[{{Tool 1}}]]
- [[{{Tool 2}}]]
- [[{{Tool 3}}]]

---

## 関連 Hub

### Parent Hub
- [[{{Parent Hub}}]]

### Sibling Hubs
- [[{{Sibling Hub 1}}]]
- [[{{Sibling Hub 2}}]]

### Child Hubs
- [[{{Child Hub 1}}]]
- [[{{Child Hub 2}}]]

### Cross Domain Hubs
- [[{{Cross Domain Hub 1}}]]
- [[{{Cross Domain Hub 2}}]]

---

## ノート追加時の指針
新しいノートをこの Hub にぶら下げるときは、次を確認する。

1. そのノートは中核か補助か  
2. どの既存ノードと relation を持つか  
3. 読む順序に入れるべきか  
4. Bridge Node になりうるか  
5. Anchor Case として使えるか  

---

## この Hub の限界
この Hub では扱いきれない論点。

- [[{{Outside Scope 1}}]]
- [[{{Outside Scope 2}}]]
- [[{{Outside Scope 3}}]]

必要なら以下の Hub へ移る。
- [[{{Other Hub 1}}]]
- [[{{Other Hub 2}}]]

---

## 関連ノート
- [[Knowledge Graph]]
- [[Traversal]]
- [[02_zettelkasten/04_knowledge_graph/Reasoning Path]]
- [[Bridge Concept]]
- [[02_zettelkasten/04_knowledge_graph/Anchor Case]]
```

---

# 最小版テンプレート

Hub をまず軽く作りたい場合は、これだけでもよい。

```markdown
---
note_type: hub
layer: structure
status: draft
hub_type:
---

# {{Hub Name}}

## 概要
この Hub は [[{{領域}}]] の主要ノードを束ねる。

## 中核ノード
- [[{{Core Node 1}}]]
- [[{{Core Node 2}}]]
- [[{{Core Node 3}}]]

## 関係の見取り図
- [[{{Core Node 1}}]] は [[{{Core Node 2}}]] に関わる
- [[{{Core Node 2}}]] は [[{{Core Node 3}}]] を説明する

## 読む順序
- [[{{Core Node 1}}]] → [[{{Core Node 2}}]] → [[{{Core Node 3}}]]

## Bridge Node
- [[{{Bridge Node 1}}]]
- [[{{Bridge Node 2}}]]

## Anchor Case
- [[{{Anchor Case 1}}]]
- [[{{Anchor Case 2}}]]

## 関連 Hub
- [[{{Related Hub 1}}]]
- [[{{Related Hub 2}}]]
```

---

# Domain Hub 用の補正

Domain Hub では、sub hub を見せることが重要になる。

追加推奨セクション:
- sub hub 一覧
- domain 特有の主要問い
- domain で頻出の pattern / mechanism
- 他 domain との bridge

---

# Pattern Hub 用の補正

Pattern Hub では、次を強める。

- pattern 間差分
- representative case
- pattern boundary
- related mechanism

追加推奨セクション:
- 類似 pattern との違い
- pattern 昇格候補
- 代表的な崩れ方 / outcome

---

# Method Hub 用の補正

Method Hub では、次を強める。

- どんな問いに使うか
- 入力に何が必要か
- 出力として何が得られるか
- tool との接続

追加推奨セクション:
- 適用場面
- 非適用場面
- 併用しやすい method

---

# Meta Hub 用の補正

Meta Hub では、次を強める。

- node type / edge type / traversal の関係
- vault 全体の読み方
- hub 間ネットワーク
- reasoning engine との接続

---

# 記入時の注意

## 1. Hub を百科事典にしない
各ノートの中身まで全部書かない。

## 2. index と混同しない
網羅一覧は別ノートでもよい。

## 3. relation を書く
リンクを並べるだけにしない。

## 4. 読み順を書く
Hub は導線を持つべきである。

## 5. bridge と anchor を必ず入れる
Hub を横にも下にも開く。

---

# Hub 記述チェックリスト

- 概要がある  
- 中核ノードがある  
- relation の見取り図がある  
- 読む順序がある  
- bridge node がある  
- anchor case がある  
- 関連 hub がある  
- 子ノートの本文を食っていない  

---

# このテンプレートの使いどころ

- Domain Hub
- Model Hub
- Pattern Hub
- Method Hub
- Meta Hub

---

# 関連ノート
- [[Hub Design Rule]]
- [[Knowledge Graph]]
- [[Traversal]]
- [[Bridge Concept]]
- [[02_zettelkasten/04_knowledge_graph/Anchor Case]]