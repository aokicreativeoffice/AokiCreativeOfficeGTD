# Edge Types

## 0. 目的
Knowledge Graph上のリンクに対して、
- 強度
- 信頼性
- 用途
- 更新方法
を定義する

---

## 1. Edge構造

```yaml
edge:
  from: NodeA
  to: NodeB
  relation: causes
  type: strong
  weight: 0.9
  confidence: high
  source: case
  status: validated
```
 #  2. Edge Type分類（4軸）
Edgeは4つの軸で定義する：
- 強度（Strength）
- 信頼性（Confidence）
- 起源（Source）
- 状態（Status）
# 3. Strength（強度）
- strong：強い関係（高頻度・明確）
- medium：条件付き
- weak：弱い
- candidate：未検証
# 4. Confidence（信頼性）
- high：複数caseで確認
- medium：一部確認
- low：仮説
# 5. Source（起源）
- case：実例由来
- theory：理論由来
- inference：推論
- imported：外部知識
# 6. Status（状態）
- active：使用中
- validated：検証済
- tentative：仮
- deprecated：廃止
# 7. Edgeカテゴリ（用途別）
## Core Edge
- is_a
- causes
- enables
## Inference Edge
- amplifies
- reduces
- constrains
## Operational Edge
- used_in
- evaluated_by
- selected_by
- recorded_as
- transformed_to
## Semantic Edge
- similar_to
- contrasts_with
# 8. Edge Weight（数値）
```YAML
weight: 0.0 - 1.0
0.9以上：強い
0.6〜0.8：中
0.3以下：弱い
```
# 9. Edge Priority
YAML

```text
priority:
  - high
  - medium
  - low
```
# 10. Edge更新ルール
Case追加時
```text
Case → Pattern
weight +0.1
confidence 上昇
```
```
失敗時

```text
weight -0.2
status: tentative
```
反証時
```text
status: deprecated
```
# 11. Edge生成ルール
Case → Edge
同構造 + 同結果 → causes生成
- Pattern → Edge
再現性あり → strong化
# 12. Graph利用
- Routing
weight高い順に探索
- Solution生成
strong + validated優先
- Pattern推薦
similar_to利用
# 13. 最小セット

```YAML
type:
  - strong
  - weak

confidence:
  - high
  - low

source:
  - case
  - inference

status:
  - active
  - tentative
```

# 14. Relationとの統合

edge = relation + metadata
# 15. 例
```YAML
from: 情報非対称
to: 市場失敗
relation: causes
type: strong
confidence: high
source: case
status: validated
```
# 16. 一行定義
Edge Type = 「関係の強さと使い方を定義するもの」
