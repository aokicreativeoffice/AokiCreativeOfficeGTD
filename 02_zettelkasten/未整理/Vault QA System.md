# Vault QA System

Vault QA System は Vault の品質を自動検査する仕組みである。

Vaultは知識グラフであり、文章の集合ではない。
したがって QA は文章校正ではなく

構造  
概念  
リンク  

を検査する。

---

# 1 QAの目的

QA Systemは次を検出する

孤立ノート  
リンク欠落  
抽象レベル誤り  
定義欠落  
Hub欠落  

---

# 2 QAレイヤー

Vault QAは3層で行う

Structure QA  
Concept QA  
Writing QA

---

# 3 Structure QA

Vaultの構造エラーを検出する。

チェック項目

フォルダ位置  
Hub接続  
リンク数  
抽象レベル  

---

## 3.1 孤立ノート検出

条件

リンク数 = 0

対処

Hub接続  
削除  

---

## 3.2 抽象レベル検査

Vaultは次の階層を持つ

Kernel  
Structure  
Mechanism  
Pattern  
Concept  
Method  
Case  

各ノートは必ず
layer:

を持つ。

---

## 3.3 フォルダ整合性

layerとフォルダは一致する必要がある。

例

layer: pattern  
→ patternsフォルダ

---

# 4 Concept QA

概念ノートの品質検査。

必須要素

定義  
構造  
例  

定義がないノートは未完成。

---

## 4.1 定義検出

次の見出しが存在するか
- 定義
- 
なければ警告。

---

## 4.2 再利用性

次を含むか確認
- 例

---

# 5 Writing QA

文章品質の検査。

確認項目

文字数  
長文  
冗長  

---

## 5.1 長文検出

段落

> 5行以上

は警告。

---

## 5.2 ノートサイズ

理想

300〜800文字

---

# 6 Graph QA

知識グラフの整合性を検査。

基本構造
- Case → Pattern
- Pattern → Mechanism  
- Mechanism → Structure  
- Structure → Kernel

リンクがない場合警告。

---

# 7 Hub QA

Hubノートを検査する。

Hub条件

ノート一覧  
分類  

Hubは必須。

---

# 8 Case QA

Caseノートの検査。

必須項目

事例  
主体  
行動  
結果  
Patternリンク  

---

# 9 Pattern QA

Patternノート検査。

必須

定義  
発生条件  
Mechanismリンク  

---

# 10 QAレポート

QA結果は次の形式で出力する。
Vault QA Report

孤立ノート

- note1    
- note2    

定義欠落

- note3    

リンク不足

- note4

---

# 11 QA運用

QAは次のタイミングで行う

Vault更新後  
週次レビュー  
大規模編集後  

---

# 12 QAフロー

QAの流れ

Vault読み込み  
↓  
Structure QA  
↓  
Concept QA  
↓  
Writing QA  
↓  
Report生成  

---

# 13 QA基準

完成ノート条件

Hub接続  
定義あり  
リンクあり  
再利用可能  

この4条件を満たすノートを

完成ノート

とする。