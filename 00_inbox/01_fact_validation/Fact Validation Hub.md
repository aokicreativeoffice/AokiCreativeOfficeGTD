---
id: fact_validation_hub
title: Fact Validation Hub

domain: [system]
concept_type: [hub]

tags: [validation, fact]
status: active
---

# Summary
事実の真偽・精度を確定するためのハブ。
Thinking OSとは分離される。

---

# Role
- 情報の真偽判定
- 不確実性の明示
- Caseの精度保証

---

# Process

1. 情報収集
2. Source評価
3. クロスチェック
4. 不確実性分類
5. Case確定

---

# Output
→ [[Validated Case]] を生成

---

# Rule（重要）

- Validationが完了するまで思考OSに投入禁止
- 不確実性は必ず明示
---

# Flow
① 情報収集
↓
② Fact Validation Hubで精査
↓
③ Validated Case作成
↓
④ Thinking Inputに貼る（手動）
↓
⑤ Entry Hub起動
↓
⑥ Graph Traversal