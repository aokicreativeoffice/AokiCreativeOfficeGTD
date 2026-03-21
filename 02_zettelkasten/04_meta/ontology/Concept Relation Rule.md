# Concept Relation Rule

このノートは Vault 内の概念関係（Concept Relation）の使用ルールを定義する。

Vaultは知識グラフであり、ノートは概念ノードである。
関係（relation）はノード間の意味的リンクである。

関係は自由に作るのではなく **layerごとに使用可能な関係を制限する**。

---

# 1 使用可能な関係

Vaultで使用する基本関係は次の通り。

| relation | 意味 |
|---|---|
| is_a | 上位概念 |
| part_of | 構造の一部 |
| derived_from | 派生元 |
| instance_of | 具体例 |
| causes | 因果 |
| caused_by | 原因 |
| explains | 説明 |
| related | 横関係 |

---

# 2 layer構造

Vaultの基本階層は次の通り。

kernel  
↓  
structure  
↓  
mechanism  
↓  
pattern  
↓  
case

  
補助レイヤー  
- model  
- domain  
- method  
- concept

---

# 3 layerごとの関係ルール

## Kernel

世界の基本原理。

使用可能 relation
- explains  
- related

例  
- 社会性原理 ：explains → 同調
- Kernel同士は  related

のみ。

---

## Structure

関係構造。

使用可能 relation
- is_a  
- part_of  
- derived_from  
- related
- 
例  
- 寡占構造  
- is_a → 市場構造


---

## Mechanism

因果メカニズム。

使用可能 relation
- derived_from  
- causes  
- caused_by  
- related

例  
同調  
- derived_from → 社会性原理  
- causes → 集団行動
  
---  
  
## Pattern  
  
繰り返し発生する現象。  
  
使用可能 relation  
- derived_from  
- explains  
- related

  
例：炎上  
- derived_from → 同調
  
---  
  
## Case  
  
具体事例。  
  
使用可能 relation  
- instance_of 
- related

  
例：ランス革命  
- instance_of → 革命パターン

---  
  
## Model  
  
抽象モデル。  
  
使用可能 relation
- explains  
- derived_from  
- related

例  
期待価値モデル  
- explains → 意思決定
  
---  
  
## Domain  
  
学問分野。  
  
使用可能 relation：
- part_of  
- related

  
例  
- 都市計画  
- part_of → 社会科学
  
---  
  
# 4 sibling関係  
  
兄弟関係は、is_a の共有で判断する。  
  
例  
- 同調  
- 社会的証明  
- 権威影響
  
これらは、is_a → 社会心理メカニズムを共有するため siblings である。  
  
---  
  
# 5 構造リンク原則  
  
Vaultでは次のリンクを推奨する。  

- Case → Pattern  
- Pattern → Mechanism  
- Mechanism → Structure  
- Structure → Kernel
  
このリンクがあると知識グラフが安定する。  
  
---  
  
# 6 禁止事項  
  
次の関係は禁止。  
  
- Case → Kernel  
- Pattern → Case  
- Kernel → Case  
  
理由 -  
抽象階層が崩壊するため。  
  
---  
  
# 7 Graph構造  
  
Vaultの知識グラフは次の構造を持つ。  

Kernel  
↓  
Structure  
↓  
Mechanism  
↓  
Pattern  
↓  
Case

  
横方向 
- related

  
---  
  
# 8 Vault QA  
  
QAスクリプトは次を検査する。  
  
- relation誤用  
- layer逆転  
- 孤立ノート  
  
---  
  
# 9 設計原則  
  
Concept relation は、少なく明確にする。  
  
理想 relation 数：5〜8

  
---  
  
# 10 まとめ  
  
Vaultの概念関係は  

- 階層関係  
- 因果関係  
- 横関係
 
の3種類に整理する。    
これにより Vault は **知識グラフとして安定する**。