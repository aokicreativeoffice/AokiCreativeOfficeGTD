# ■ 全体構造（最重要）

Problem  
 ↓  
Structure特定  
 ↓  
Pattern検索  
 ↓  
Pattern適合判定  
 ↓  
Solution候補生成  
 ↓  
Instance化  
 ↓  
Decisionへ

---

# ■ 1. Pattern → Solution Engine（中核ノート）

# Pattern → Solution Engine  
  
## 0. 目的  
Problemに対して、既存Patternを利用し、  
再利用可能なSolution候補を生成する  
  
---  
  
## 1. 入力  
  
- Problem:  
- Structure:  
- 歪み:  
  
---  
  
## 2. Pattern検索  
  
### 方法  
  
- structure一致  
- mechanism一致  
- 歪み一致  
  
---  
  
### 候補Pattern  
  
- [[Pattern: XXX]]  
- [[Pattern: YYY]]  
- [[Pattern: ZZZ]]  
  
---  
  
## 3. 適合判定  
  
各Patternについて：  
  
- 適用可能性:  
- 条件一致:  
- 制約違反:  
  
→ OK / NG  
  
---  
  
## 4. Solution生成  
  
### フォーマット  
  
Patternを元に：  
  
- Concept:  
- Transformation:  
- Mechanism:  
- Instance案:  
  
---  
  
## 5. 出力（最低3案）  
  
### Solution A  
- Pattern:  
- 内容:  
  
---  
  
### Solution B  
- Pattern:  
- 内容:  
  
---  
  
### Solution C  
- Pattern:  
- 内容:  
  
---  
  
## 6. 次工程  
  
→ Instance化    
→ Decisionへ

---

# ■ 2. Pattern検索ルール（辞書）

歪み → Pattern  
  
不足 → 増加 / 集約  
過剰 → 制約 / 削減  
非対称 → 可視化 / シグナル  
断絶 → 接続 / ブリッジ  
過密 → 分散 / 時間分割  
ロックイン → 分離 / 再設計  
低効率 → 標準化 / 自動化  
低品質 → フィルタ / 教育  
不信 → 信頼構築 / 契約

---

# ■ 3. Pattern → Solution変換テンプレ

👉 Patternをそのままsolutionに変換

# Pattern適用 → Solution  
  
## Pattern  
[[Pattern: XXX]]  
  
---  
  
## Solution  
  
### Concept  
- Patternの抽象名  
  
### Transformation  
- Patternに対応する操作  
  
### Mechanism  
- Pattern内mechanism  
  
---  
  
## Instance  
  
- 現場での具体案:

---

# ■ 4. 自動生成プロンプト

👉 これで毎回同じ品質

Problemを入力として：  
  
1. Structureを特定  
2. 歪みを特定  
3. 対応するPatternを3つ以上選択  
4. 各PatternをSolutionに変換  
5. Instance案まで出力せよ

---

# ■ 5. 実例（あなたのケース）

## Problem

求人が来ない

---

## Structure

- 人不足
    
- 労働条件
    
- 情報
    

---

## 歪み

- 不足
    
- 非対称
    
- 過負荷
    

---

## Pattern

- 可視化
    
- 供給制限
    
- インセンティブ設計
    

---

## Solution

### A

可視化 → 条件公開強化

### B

供給制限 → 受注制限

### C

インセンティブ → 賃上げ

---

👉 **ゼロから考えなくていい**

---

# ■ 6. Vault配置

solution/  
└─ generation/  
   └─ Pattern → Solution Engine  
  
pattern/  
└─ library/

---

# ■ 7. 強制ルール（重要）

## ルール1

👉 Solutionを考える前にPatternを引く

## ルール2

👉 Patternを最低3つ使う

## ルール3

👉 PatternなしSolutionは禁止

---

# ■ 8. 状態遷移（完成形）

Problem  
 ↓  
Analysis  
 ↓  
Pattern  
 ↓  
Solution  
 ↓  
Decision  
 ↓  
Execution  
 ↓  
Case  
 ↓  
Pattern（更新）

---

# ■ 9. 本質

この仕組みの正体：

👉 **「経験から直接解決策を引く装置」**

---

# ■ 10. ここまで来た状態

あなたのVaultは：

- 分析できる
    
- 解決できる
    
- 判断できる
    
- 実行できる
    
- 学習できる
    
- 再利用できる ← ★追加
    

👉 **完全な知識OS（実用レベル）**