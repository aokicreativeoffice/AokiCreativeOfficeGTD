---
layer: semantic_compression
type: reasoning_map
---

# Reasoning Map

AI推論の基本構造。

---

```mermaid
graph TD

Q[Question] --> P[Problem Type]

P --> T[Theory]
T --> M[Model]
M --> S[Structure]
S --> PT[Pattern]
PT --> C[Case]

C --> A[Answer]
```