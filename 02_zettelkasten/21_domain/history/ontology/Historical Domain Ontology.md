---
note_type:
  - ontology
layer:
  - meta
status:
  - stable
maturity:
  - draft
domain: history
created: 2026-03-07
updated: 2026-03-07
---

# 歴史ドメイン・オントロジー定義 (History Domain Ontology)

歴史を「単なる記述」から「動的な構造」として捉えるための、エンティティおよびリレーションの定義集。

## 1. 主要エンティティ (Core Entities)

歴史ノートを作成する際は、以下の4つのいずれかに分類し、属性（Properties）を付与する。

| エンティティ名 | 定義・役割 | 主な属性例 |
| :--- | :--- | :--- |
| **主体 (Actor)** | 変化を駆動する個人、集団、組織。 | `ideology`, `incentive`, `power_base` |
| **事件 (Event)** | 変化が顕在化する特定の時点・出来事。 | `trigger`, `outcome`, `event_type` |
| **構造 (Structure)** | 変化を規定・制約する制度や枠組み。 | `legitimacy_source`, `stability` |
| **潮流 (Epoch)** | 時代を支配する精神、パラダイム。 | `main_paradigm`, `dominant_power` |

---

## 2. 事件の分類 (Event Taxonomy)

`Event` エンティティには、以下の `event_type` をタグ付けし、変化の性質を特定する。

1. **引き金事件 (Trigger Event)**: 潜在的な矛盾を一気に爆発させる急激な触媒。
2. **潮流事件 (Trend-setting Event)**: 新しい価値観やパラダイムを定着させる長期的な起点。
3. **構造的転換点 (Structural Pivot)**: 権力の正当性やシステムが不可逆に入れ替わる瞬間。
4. **収束事件 (Convergence Event)**: 複数の独立した因果チェーンが交差・同期する地点。
5. **盲目的破局 (Blind Catastrophe)**: システムの限界や外部要因による制御不能な崩壊。

---

## 3. 定義済みリレーション (Defined Relations)

[[02_zettelkasten/04_meta/ontology/Relation Types|Relation Types]] に基づき、歴史分析で多用する接続定義。

### 因果・動態リレーション
- **`causes` / `triggers`**: 直接的な因果関係。
- **`catalyzes` (触媒)**: 小さな事象が、背景にある巨大な構造変化を加速させる。
- **`constrained_by` (制約)**: 構造（Structure）が主体（Actor）の選択肢を制限する。
- **`explains` (説明)**: 抽象的な理論や構造が、具体的な事件の理由を裏付ける。

### 構造・系統リレーション
- **`instance_of`**: 具体的な事件を抽象的な「型（Pattern）」に紐付ける。
- **`replaces`**: 古い制度やパラダイムを新しいものが上書きする。
- **`inherited_from`**: 前時代の要素を継承・変奏している。
- **`analogous_to`**: 時代を超えた構造的な類似性を指摘する。

---

## 4. 分析フレームワーク (Analytical Framework)

歴史ノートを記述する際の「問い（Question）」の型：
1. **正当性の所在**: 「この構造において、権力の正当性（Legitimacy）はどこにあるか？」
2. **情報の非対称性**: 「主体の意思決定を歪めた『文脈剥離』や『情報の武器化』はあったか？」
3. **インセンティブの不一致**: 「主体の行動は、国家の利益ではなく『体制の延命』に紐付いていないか？」

---
## 5. ログ
- 2026-03-25: エムス電報事件の分析を経て、歴史ドメインの基本構造を定義。