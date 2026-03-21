---
id: routing_matrix
title: Routing Matrix

concept_type: [system]

---
# Definition

Routing = Trigger → Transition → Mechanism → Kernel

---
# Purpose
問いを適切なKernel / Structure / Mechanismにルーティングする

---
# Flow
Question
→ Trigger特定
→ Transition特定
→ Mechanism選択
→ Kernel到達
→ Solution
→ Case
→ Pattern生成

---
# Kernel Routing

```mermaid
flowchart TD

Q[問い] --> T[Trigger判定]

%% Trigger分岐
T --> T1[技術ショック]
T --> T2[フィードバック増幅]
T --> T3[非線形臨界]
T --> T4[蓄積型]
T --> T5[内部崩壊]
T --> T6[外圧・競争]
T --> T7[資源制約]
T --> T8[環境変化]
T --> T9[ルール変更]
T --> T10[インセンティブ変更]
T --> T11[権力再編]
T --> T12[期待変化]
T --> T13[ナラティブ変化]
T --> T14[情報更新]

%% Transition Type
T1 --> TR1[置換型]
T2 --> TR2[非連続型]
T3 --> TR3[非連続型]
T4 --> TR4[連続型]
T5 --> TR5[崩壊型]
T6 --> TR6[分岐型]
T7 --> TR7[置換型]
T8 --> TR8[分岐型]
T9 --> TR9[置換型]
T10 --> TR10[連続型]
T11 --> TR11[非連続型]
T12 --> TR12[振動型]
T13 --> TR13[置換型]
T14 --> TR14[振動型]

%% Mechanism層
TR1 --> M1[選択・競争メカニズム]
TR2 --> M2[非線形・フィードバックメカニズム]
TR3 --> M2
TR4 --> M3[蓄積・適応メカニズム]
TR5 --> M4[崩壊メカニズム]
TR6 --> M5[分岐・進化メカニズム]
TR7 --> M6[資源配分メカニズム]
TR8 --> M5
TR9 --> M7[制度変化メカニズム]
TR10 --> M3
TR11 --> M8[権力集中メカニズム]
TR12 --> M9[期待・認知メカニズム]
TR13 --> M10[正当性メカニズム]
TR14 --> M9

%% Kernel層
M1 --> K1[選択原理]
M2 --> K2[非線形性原理]
M3 --> K3[適応原理]
M4 --> K4[崩壊原理]
M5 --> K5[進化原理]
M6 --> K6[資源制約原理]
M7 --> K7[制度原理]
M8 --> K8[権力原理]
M9 --> K9[認知原理]
M10 --> K10[正当性原理]
```

---

# Usage
1. 問いを分類
2. Kernelを特定
3. Structureを特定
4. Mechanismを選択
5. ContextとしてAIに渡す

---

