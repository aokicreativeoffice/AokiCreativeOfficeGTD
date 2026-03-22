# フロー
```mermaid
flowchart TD  
  
F[Fact]  
F --> R[Risk Pattern]  
F --> A[Alert]
F --> Irt[Issue（risk triggers内蔵）]
```

# リスクレベル
```yaml
level:  
- 低  
- 中  
- 高  
- 致命的
```