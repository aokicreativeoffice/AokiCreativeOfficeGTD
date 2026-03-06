---
note_type:
  - parmanent
layer:
  - system_model
status:
  - stable
maturity:
  - canonical
domain: knowledge_architecture
related:
problem_type:
created: 2026-03-05
updated: 2026-03-06
---
システムモデルとは、現象の構造や振る舞いを抽象化したモデルである。
# Translation
system model
# Engine
システムモデルの要素
- 要素
- 関係
- フロー
- フィードバック

システムの基本構造

```mermaid
flowchart LR

Elements[Elements]
Relations[Relations]
Flows[Flows]

Elements --> Relations
Relations --> Flows
Flows --> SystemBehavior[System Behavior]
```
# Understanding
システムモデルは、
- [[12 システム]]    
- [[01 因果]]    
- [[05 制約]]    
の理解に役立つ。
システムモデルは、複雑な現象を構造として理解する方法である。
# Background
多くの現象は、線形ではなく相互作用によって動く。
システムモデルは、複雑系の理解のために発展した。
# Example
主なシステムモデル

| モデル                        | 説明          |
| -------------------------- | ----------- |
| [[01 フィードバックループ]]          | 自己強化 / 自己調整 |
| [[02 状態遷移]]                | 状態変化        |
| [[03 フローモデル]]              | 流れ          |
| [[04 ストック・フローモデル]]         | 蓄積          |
| [[05 紐帯モデル]]               | 関係構造        |
| [[06 プリンシパル＝エージェントモデルモデル]] | 代理関係        |
# Use
- 社会分析
- 経済分析
- 組織分析
- 政策分析