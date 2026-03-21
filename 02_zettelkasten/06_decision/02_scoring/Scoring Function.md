# Scoring Function

## 0. 目的
複数のSolutionを定量的に比較し、
制約を満たした上で最適な意思決定を導く

---

## 1. 基本構造

Score = Σ (Wi × Xi)

- Wi: 重み（Weight）
- Xi: 評価値（Score 1-5）

---

## 2. 評価軸（Criteria）

### 必須6軸

| 指標 | 内容 |
|------|------|
| Effectiveness | 効果（問題解決力） |
| Cost | コスト（初期＋運用） |
| Feasibility | 実行可能性 |
| Risk | リスク |
| Speed | 実装速度 |
| Reversibility | 可逆性 |

---

## 3. 正規化ルール（重要）

### 3.1 スコア方向統一

すべて「高いほど良い」に変換

- Cost → 低いほど良い → 逆転
- Risk → 低いほど良い → 逆転

---

### 3.2 変換式

```markdown id="norm"
Cost_score = 6 - Cost_raw
Risk_score = 6 - Risk_raw
```

---

## 4. 重み設定（Weight）

### 4.1 デフォルト

```text
Effectiveness: 0.30  
Cost: 0.20  
Feasibility: 0.20  
Risk: 0.10  
Speed: 0.10  
Reversibility: 0.10
```

---

### 4.2 状況別プリセット

#### ■ 攻め（成長重視）

- Effectiveness: 0.4    
- Cost: 0.1    
- Risk: 0.1    
- 他均等    

---

#### ■ 守り（安定重視）

- Risk: 0.3    
- Feasibility: 0.25    
- Cost: 0.2    

---

#### ■ 速度重視

- Speed: 0.3    
- Feasibility: 0.25    

---

## 5. 制約フィルタ（Hard Constraints）

👉 スコア計算前に除外

```text
if Feasibility < 3 → 除外  
if Risk > 4 → 除外  
if Cost > 4 → 要承認
```

---

## 6. スコア計算（標準）

```text
Score =   
(Effectiveness × W1) +  
(Cost_score × W2) +  
(Feasibility × W3) +  
(Risk_score × W4) +  
(Speed × W5) +  
(Reversibility × W6)
```

---

## 7. 拡張モデル

---

### 7.1 ペナルティモデル（実務推奨）

```text
Score = 基本スコア - ペナルティ  
  
ペナルティ =  
(重大リスク × 0.5) +  
(実行難易度 × 0.3)
```

---

### 7.2 ボトルネック制約モデル

```text
Score_final = min(各スコア)  
```
  
※どれか1つでも弱いと全体NG

👉 インフラ・安全系で使用

---

### 7.3 乗算モデル（バランス重視）

```text
Score = Π (Xi^Wi)
```

👉 極端な弱点を許さない

---

### 7.4 オプション価値モデル（高度）

```text
Score = 基本スコア + 柔軟性ボーナス  
  
柔軟性 =  
可逆性 + 拡張性 + スケーラビリティ
```

---

## 8. 出力形式

| Solution | Score | Rank |  
|----------|------|------|  
| A | 3.8 | 1 |  
| B | 3.2 | 2 |  
| C | 2.9 | 3 |

---

## 9. 判断ルール

- 1位を採用    
- ただし差が0.3未満なら併用検討    
- 制約違反は除外    

---

## 10. チェックリスト

-  スコア方向を統一したか    
-  重みが合計1か    
-  制約フィルタを通したか    
-  定性コメントも書いたか    

---

## 11. よくある失敗

### ❌ コストとリスクをそのまま足す

→ 方向が逆

### ❌ 重みが曖昧

→ 意思決定がブレる

### ❌ 制約を無視

→ 実行不能案が上位に来る

---

## 12. 最小版（現場用）

```text
Score =  
効果×0.4  
- コスト×0.2  
- リスク×0.2  
+ 実行性×0.2
```

---

## 13. 接続ノート

- [[Decision Input Template]]    
- [[instances → Decisionリンク]]    
- [[Evaluation Hub]]