# Solution Generation Engine

## 0. 目的
Problemを入力すると、
structure / mechanism / transformationを経由して
複数のsolution候補を半自動生成する

---

## 1. 全体フロー

Problem
 ↓
Structure特定
 ↓
歪み検出
 ↓
Mechanism特定
 ↓
Transformation候補生成
 ↓
Solution生成
 ↓
Decisionへ

---

## 2. 入力フォーマット

Problem:
対象:
制約:
目的:

---

## 3. Step1: Structure分解

### チェック

- 人（人員・スキル）
- 物（設備・資産）
- 金（収益・コスト）
- 情報（可視性・非対称）
- 制度（ルール）
- ネットワーク（接続）

→ 該当箇所を特定

---

## 4. Step2: 歪み検出（必須）

### 該当を選択

- 不足
- 過剰
- 非対称
- 断絶
- 過密
- ロックイン
- フィードバック暴走
- 低効率
- 低品質
- 不信

---

## 5. Step3: Mechanism特定

### 該当を選択

- フィードバック
- ネットワーク
- 非対称
- 競争 / 協力
- ロックイン
- 適応

---

## 6. Step4: Transformation自動生成

## 6.1 ルーティング

歪み → Transformation

- 不足 → 増加 / 強化
- 過剰 → 削減 / 制約
- 非対称 → 可視化 / シグナル
- 断絶 → 接続 / 再配線
- 過密 → 分散 / 時間分割
- ロックイン → 分離 / 置換
- 低効率 → 最適化 / 標準化
- 低品質 → フィルタ / 教育
- 不信 → 可視化 / 契約

---

## 6.2 最低3方向出す（強制）

- 削る方向（Reduce）
- 増やす方向（Increase）
- 構造変更（Rewire）

---

## 7. Step5: Solution生成テンプレ

### Solution A（保守）

Concept:
Transformation:
Mechanism:
内容:

---

### Solution B（中間）

Concept:
Transformation:
Mechanism:
内容:

---

### Solution C（攻め）

Concept:
Transformation:
Mechanism:
内容:

---

## 8. Step6: 制約適用

- 法規制
- コスト
- 人員
- 実行可能性

→ NG案を削除

---

## 9. 出力

- Solution候補一覧
- 各Transformation
- Mechanism

→ Decisionへ渡す

---

## 10. チェックリスト

- [ ] 歪みを定義したか
- [ ] mechanismを特定したか
- [ ] transformationを選んだか
- [ ] 3案以上出したか
- [ ] 制約を考慮したか

---

## 11. 禁止事項

- いきなりsolutionを考える
- 1案しか出さない
- mechanismを書かない

---

## 12. 接続

- [[Transformation Types]]
- [[Solution Routing]]
- [[Mechanism Library]]
- [[Solution Instance Template]]