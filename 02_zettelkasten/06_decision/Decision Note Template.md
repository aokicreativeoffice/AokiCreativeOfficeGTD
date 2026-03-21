# Decision: [Problem Name]

## 0. 目的
複数のSolution Instanceを集約し、
定量評価に基づいて最適な意思決定を行う

---

## 1. Problem定義

- Problem:
- 目的:
- 制約:

---

## 2. Solution一覧（自動集約）

### 対象Solution

- [[Solution: A]]
- [[Solution: B]]
- [[Solution: C]]

※各Solutionは必ずDecision Linkを持つこと

---

## 3. 評価軸（Criteria）

- Effectiveness
- Cost
- Feasibility
- Risk
- Speed
- Reversibility

---

## 4. 評価テーブル（中核）

| Solution | Eff | Cost | Fea | Risk | Spd | Rev | Score |
|----------|-----|------|-----|------|-----|-----|-------|
| A |  |  |  |  |  |  |  |
| B |  |  |  |  |  |  |  |
| C |  |  |  |  |  |  |  |

---

## 5. スコア計算
```text
Score = Σ（Wi × Xi）
```


- 重み:
  - Effectiveness:
  - Cost:
  - Feasibility:
  - Risk:
  - Speed:
  - Reversibility:

---

## 6. ランキング

1位:
2位:
3位:

---

## 7. 意思決定

### 採用
- 

### 理由
- 

### 条件付き採用
- 

### 不採用
- 理由:

---

## 8. Decision Link同期（重要）

各SolutionのDecision Linkを更新：

- Status → 評価完了
- スコア反映
- Decision参照リンク追加

---

## 9. 実行計画

- 次アクション:
- 担当:
- 期限:

---

## 10. 事後評価（後日）

- 結果:
- 成否:
- 想定との差分:

---

## 11. Pattern抽出（重要）

- 成功パターン:
- 失敗パターン:
- 使用したmechanism:

→ [[Pattern: XXX]]

---

## 12. 関連リンク

- [[instances → Decisionリンク]]
- [[Scoring Function]]
- [[Decision Cases]]