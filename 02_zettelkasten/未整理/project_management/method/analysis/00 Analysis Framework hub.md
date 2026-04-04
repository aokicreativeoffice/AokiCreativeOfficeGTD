---
note_type: structure
layer: structure
status: stable
maturity: canonical
domain: thinking_tools
related:
  - Structure Hub
  - "[[00 Problem Solving Hub]]"
---
# 概要  
Analysis Frameworkは、問題や現象を分析するための思考の型（framework）である。  
現実の複雑な事象を、分解・構造化・因果分析するための思考ツール群。
Frameworkは、World Model を問題分析に適用する橋渡しになる。
# 分析の基本フロー
```mermaid
flowchart TD 
    A[Framework] --> B[Insight]
    B --> C[Decision]

```
# 効果
- 見落としを防ぐ  
- 構造を明確化する  
- 思考を再利用できる
# フレームワーク一覧
## 因果分析  
原因を特定するフレーム  
- [[02_zettelkasten/Zettelkasten Engine/02_process/methods/analysis/根因分析|根因分析]] （根本原因分析）
- [[02_zettelkasten/Zettelkasten Engine/02_process/methods/analysis/なぜなぜ分析|なぜなぜ分析]]（なぜなぜ分析）
- [[02_zettelkasten/Zettelkasten Engine/02_process/methods/analysis/因果連鎖分析|因果連鎖分析]]    （因果連鎖分析）
## 制約分析  
システムの制約を特定する  
- [[02_zettelkasten/Zettelkasten Engine/02_process/methods/analysis/ボトルネック分析|ボトルネック分析]]]（ボトルネック分析）
- [[02_zettelkasten/Zettelkasten Engine/02_process/methods/analysis/制約分析|制約分析]] （制約分析）
## 利害・権力分析  
利害関係者の構造  
- [[02_zettelkasten/Zettelkasten Engine/02_process/methods/analysis/ステークホルダー分析|ステークホルダー分析]] （ステークホルダー分析）
- [[02_zettelkasten/Zettelkasten Engine/02_process/methods/analysis/パワーマッピング|パワーマッピング]]  （パワーマッピング）
- [[02_zettelkasten/Zettelkasten Engine/02_process/methods/analysis/インセンティブ設計|インセンティブ設計]]
## トレードオフ分析  
複数目標のバランス  
- [[02_zettelkasten/Zettelkasten Engine/02_process/methods/analysis/トレードオフ分析|トレードオフ分析]] （トレードオフ分析）
- [[02_zettelkasten/Zettelkasten Engine/02_process/methods/analysis/費用便益分析|費用便益分析]]  （費用便益分析）
## 構造分析  
対象の構造理解  
- [[world model Hub]]
- [[02_zettelkasten/Zettelkasten Engine/02_process/methods/analysis/価値連鎖分析|価値連鎖分析]] 
- [[02_zettelkasten/Zettelkasten Engine/02_process/methods/analysis/システムマッピング|システムマッピング]]（システムマッピング）
- [[02_zettelkasten/Zettelkasten Engine/02_process/methods/analysis/状態遷移モデル|状態遷移モデル]]（状態遷移モデル）
## 情報分析
- [[02_zettelkasten/Zettelkasten Engine/02_process/methods/analysis/代理人問題|代理人問題]]
- [[02_zettelkasten/Zettelkasten Engine/02_process/methods/analysis/信号分析|信号分析]]
## 不確実性分析
- [[02_zettelkasten/Zettelkasten Engine/02_process/methods/analysis/インセンティブ設計]]
- [[02_zettelkasten/Zettelkasten Engine/02_process/methods/analysis/シナリオ分析|シナリオ分析]]
## 意思決定分析
- [[02_zettelkasten/Zettelkasten Engine/02_process/methods/analysis/意思決定フレームワーク|意思決定フレームワーク]]
# 選び方
問題の種類によって使い分ける  
```mermaid
flowchart LR

A[Problem] --> B{What is the main question?}

B --> C[Why did it happen?]
B --> D[Where is the constraint?]
B --> E[Who influences the outcome?]
B --> F[Which option is better?]
B --> G[How is the system structured?]
B --> H[What information signal exists?]
B --> I[What should we choose?]

C --> C1[Root Cause Analysis]
C --> C2[Five Whys]
C --> C3[Causal Chain Analysis]

D --> D1[Bottleneck Analysis]
D --> D2[Constraints Analysis]

E --> E1[Stakeholder Analysis]
E --> E2[Power Mapping]

F --> F1[Trade-off Analysis]
F --> F2[Cost-Benefit Analysis]
F --> F3[Senario Analysis]

G --> G1[Value Chain Analysis]
G --> G2[System Mapping]
G --> G3[State Transition Model]
G --> G4[Principal-Agent Model]

H --> H1[Signal Analysis]

I --> I1[Decision Making]
```

# 使用の基本  
```mermaid
flowchart TD 
    A[問題定義] --> B[フレームワーク選定]
    B --> C[構造整理]
    C --> D[解決策]
```
# 特徴
```mermaid
flowchart TD 
    A[World Model] --> B[Analisys Framework]
    B --> C[Problem Solving]
```