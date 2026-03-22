---
id:
title: Fact Finding Engine（事実認定エンジン）

engine_type: [fact_finding]
applicable_domains: [law, history, investigation]

relations:
# - type: precedes
#   to: Normative Engine

tags: []
status: draft
---

# Summary
証拠・証言・資料から「何が事実か」を確定する推論エンジン

---

# Core Function
「何が起きたか」を確定する

---

# Structrure
  
## Fact Layer（事実）  
- [[主要事実]]  
- [[間接事実]]  
- [[補助事実]]  
  
## Evidence Layer（証拠）  
- [[直接証拠]]  
- [[間接証拠]]  
- [[状況証拠]]  
  
## Inference Layer（推認）  
- [[推認メカニズム]]  
- [[信用性評価]]  
- [[矛盾検出]]  
  
## Flow  

1. [[争点ノード]]を開く
2. Required Factsを見る
3. [[主要事実]]に飛ぶ
4. [[間接事実]]、[[補助に降りる
5. 証拠に到達
6. 推認して戻る
7. [[Normative Engine]]へ

---

# Inputs
- 証拠（文書・データ）
- 証言
- 状況証拠
- 前提事実

---

# Output
- 認定事実
- 不確定領域
- 事実関係の構造

---

# Thinking Protocol

## Step1 事実候補の抽出
- 主張されている事実は何か
- 争点はどこか

## Step2 証拠の整理
- 証拠の種類（直接証拠 / 間接証拠）
- 出所は信頼できるか

## Step3 信用性評価
- 一貫性
- 利害関係
- 他証拠との整合性

## Step4 事実構造化
- 時系列
- 因果関係
- 行為主体

## Step5 推認
- 直接証拠がない部分を推論で補う

## Step6 確定 / 留保
- 確定事実
- 不明点
- 仮説

---

# Key Mechanisms
- 証拠評価
- 信用性判断
- 推認（間接事実→主要事実）
- 矛盾検出

---

# Constraints / Pitfalls
- バイアス（先入観）
- 証拠の過信
- ストーリー補完しすぎ

---

# Examples
- 事故の過失認定
- 労働者性の事実認定

---

# Links
- [[Normative Engine]]
- [[証拠評価基準]]
- [[推認メカニズム]]