# Auto Relation Rules

## 0. 目的
ノート作成・更新時に、relationを半自動で付与し
- リンク漏れ防止
- Knowledge Graphの一貫性維持
- 推論可能性の向上
を実現する

---

## 1. 基本原則

1. concept_typeに応じて付与ルールを固定する
2. relationは「方向」を必ず持つ
3. 1ノートにつき最大5本まで（過剰防止）
4. 不明な場合は付与しない（誤リンク回避）

---

## 2. ルール構造

```yaml
rule:
  trigger: 条件
  relation: 関係
  target: 対象ノード
```

##  3. Concept Type別ルール
### Pattern
```yaml
- trigger: Patternに対応するSolutionがある
  relation: maps_to
  target: Solution

- trigger: PatternがCaseから抽出された
  relation: abstracts
  target: Case

- trigger: PatternがMechanismに依存
  relation: based_on
  target: Mechanism
```

### Mechanism
```yaml
- trigger: Mechanismが結果を生む
  relation: causes
  target: Event / Outcome

- trigger: Mechanismが条件として必要
  relation: enables
  target: Solution

- trigger: MechanismがPatternを支える
  relation: explains
  target: Pattern
```

### Solution
```yaml
- trigger: SolutionがPatternを利用
  relation: used_in
  target: Pattern

- trigger: SolutionがDecisionで選ばれる
  relation: selected_by
  target: Decision

- trigger: Solutionが問題に適用
  relation: applied_to
  target: Problem
```

### Desicion
```yaml
- trigger: DecisionがSolutionを選択
  relation: selects
  target: Solution

- trigger: DecisionがExecutionに繋がる
  relation: executed_as
  target: Execution
```

### Execution
```yaml
- trigger: ExecutionがCaseになる
  relation: recorded_as
  target: Case
```

### Case
```yaml
- trigger: CaseがPatternを生成
  relation: transformed_to
  target: Pattern

- trigger: Caseが特定の概念の例
  relation: instance_of
  target: Concept
```

### Event
```yaml
- trigger: EventがEventを引き起こす
  relation: causes
  target: Event

- trigger: EventがMechanismを発動
  relation: triggers
  target: Mechanism
```

### Actor
```yaml
- trigger: Actorが行為を行う
  relation: performs
  target: Action / Event

- trigger: ActorがEventに関与
  relation: participates_in
  target: Event
```

---

## 4. キーワードベース補助ルール

|系|キーワード|type|
|---|---|---|---|
|causes系|「〜を引き起こす」「原因」「結果」| causes|
|enables系|「可能にする」「条件」「前提」| enables|
|used_in系|「利用する」「適用する」| used_in|
|abstracts系|「抽象化」「共通」「パターン」| abstracts|

 ## 5. 自動付与手順（運用）
1. concept_typeを確認
2. 該当ルールを抽出
3. Descriptionから対象ノードを特定
4. relationを最大3つ付与
5. 不自然なら削除

## 6. 出力フォーマット

```YAML
relations:
  - type: causes
    to: 市場失敗

  - type: used_in
    to: 価格戦略
```

## 7. 禁止事項
❌ related_toの乱用
❌ 双方向リンクの乱発
❌ relationなしで放置

## 8. 最小自動ルール

|type|relation|接続先|
|---|---|---|
| Pattern | maps_to | Solution|
|Solution | selected_by | Decision|
| Decision | executed_as | Execution||- Execution | recorded_as | Case|
| Case | transformed_to | Pattern|

## 9. 一行定義
Auto Relation = 「ノート作成時にリンクを強制的に生成するルール」

---

# ■ GitHubでの簡易自動化（任意）

```bash
# relation未記入ノート検出
grep -L "relations:" -r .

# candidate relation検出
grep -r "原因\|引き起こす" .
```