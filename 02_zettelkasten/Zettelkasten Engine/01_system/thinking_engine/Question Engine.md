---
id: question_engine
title: Question Engine

domain: [system]
concept_type: [engine]

relations:
- type: precedes
  to: Inquiry Hub
- type: routes
  to: Graph Traversal
- type: uses
  to: [Case, Pattern, Mechanism, Kernel, Model, Theory]

tags: [question, reasoning, engine]
status: draft
---

# Summary
問いを入力として、適切な思考経路（Graph Traversal）を選択し、推論と出力を生成する中核エンジン

---

# Core Idea
Question Engineは

「問い → 型分類 → 知識グラフ侵入点 → 探索 → 推論 → 出力」

のパイプラインを制御する

---

# Structure

## 全体フロー

[[Question Engine Map]]

## Question Type（問いの型）

|型|内容|典型質問|
|---|---|---|
|説明型|因果・理由|なぜ起きるか|
|構造型|構成・関係|どういう構造か|
|比較型|差異|何が違うか|
|予測型|将来|何が起きるか|
|設計型|解決|どう作るか|
|事例型|具体|例は何か|

## Entry Node（侵入点）

|Entry|役割|
|---|---|
|Case|具体事例|
|Pattern|一般化|
|Mechanism|因果|
|Kernel|原理|
|Model|抽象モデル|
|Theory理論体系|

## Graph Traversal（探索経路）

|経路|内容|
|---|---|
|Case → Pattern|抽象化|
|Pattern → Mechanism|因果分析|
|Mechanism → Kernel|原理到達|
|Kernel → Mechanism|応用生成|
|Mechanism → Pattern|予測|
|Pattern → Case|具体化|

## Reasoning（推論）

|種類|内容|
|---|---|
|因果推論|原因と結果|
|類推推論|類似から予測|
|比較推論|差異分析|
|構造推論|関係理解|
|仮説生成|新規案|

## Output（出力）

|出力|内容|
|---|---|
|Explanation|説明|
|Prediction|予測|
|Hypothesis|仮説|
|Design|設計|
|Strategy|戦略|

# Dynamics / Mechanism
## ① Question → Question Type
問いの形式で思考モードが決定される
## ② Question Type → Entry Node
問いに応じて「どこから考えるか」が決まる
例：
- 説明型 → Case
- 構造型 → Pattern
- 予測型 → Mechanism
- 設計型 → Kernel
## ③ Entry Node → Graph Traversal
知識グラフ上の移動方向を決定
👉 ここが「思考そのもの」
## ④ Graph → Reasoning
探索経路に応じて推論タイプが決定
## ⑤ Reasoning → Output
推論の種類によって出力形式が変わる

# Examples
## ケース1：炎上はなぜ起きるか
Question Type：説明型
Entry：Case
Traversal：Case → Pattern → Mechanism
Reasoning：因果推論
Output：Explanation
## ケース2：この市場はどうなるか
Question Type：予測型
Entry：Mechanism
Traversal：Mechanism → Pattern
Reasoning：類推推論
Output：Prediction
## ケース3：ビジネスを設計する
Question Type：設計型
Entry：Kernel
Traversal：Kernel → Mechanism → Pattern
Reasoning：仮説生成
Output：Design → Strategy
# Implications
思考は「探索アルゴリズム」である
問いは「探索開始位置と方向」を決める
Reasoningは結果であり、選択されるもの
# Links
[[inquiry Hub]]
[[Routing Matrics]]
[[Inverse Routing Matrics]]
[[AI Query Template]]