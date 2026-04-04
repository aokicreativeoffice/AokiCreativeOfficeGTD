# Flow Selection Engine

## 1. 目的
入力された問いに対して、適切な推論フローを選択する。

---

## 2. フロー一覧

- Case Flow（事例・観察）
- Solution Flow（問題解決・設計）
- Hypothesis Flow（仮説検証）
- Search Flow（探索・理解）
- Research Flow（厳密検証）
- Cross Domain Flow（応用・転用）

---

## 3. 判定アルゴリズム

### Step 1：問いの型判定

| 条件 | フロー |
|------|------|
| 「なぜ」「どうして」＋具体事例 | Case Flow |
| 「どうすれば」「設計」「改善」 | Solution Flow |
| 「〜では？」「仮説」 | Hypothesis Flow |
| 「とは何か」「整理」「一覧」 | Search Flow |
| 「検証」「データ」「分析」 | Research Flow |
| 「別領域」「応用」「転用」 | Cross Domain Flow |

---

### Step 2：優先順位

複数該当する場合：

1. Solution（最優先）
2. Hypothesis
3. Case
4. Search
5. Cross Domain
6. Research（明示的な場合のみ）

---

## 4. 出力形式

```text
Flow Type: ○○
Reason: ○○
Next Step:
  - 呼び出すHub
  - 使用ノート
```
---

## 5. フロー別呼び出し先

### Case Flow

- Case Hub    
- Pattern Extraction    
- Pattern Hub    
- Structure Hub    
- Mechanism Hub    

---

### Solution Flow

- Problem Type    
- Structure Hub    
- Mechanism Hub    
- Method Hub    
- Decision Hub    

---

### Hypothesis Flow

- Hypothesis    
- Structure Hub    
- Mechanism Hub    
- Mismatch Detection    
- Research（必要時）    

---

### Search Flow

- Graph Traversal    
- Concept Links    
- Pattern / Structure / Mechanism Hub    

---

### Cross Domain Flow

- Cross Domain Mapping    
- Bridge Concept    

---

### Research Flow

- Research Loop    
- dataset / test / result    

---

## 6. 注意点

- Flowは1つに固定しない（必要に応じて切り替え）    
- 初期選択が最も重要（誤ると探索コスト増大）    
- 「わからない場合はSearch Flowから開始」    

---

## 7. 典型パターン

- Case → Structure → Mechanism（観察・分析）
- Problem → Structure → Mechanism → Solution（設計）
- Hypothesis → Mechanism → Test（検証）
- Search → Pattern → Structure（理解）