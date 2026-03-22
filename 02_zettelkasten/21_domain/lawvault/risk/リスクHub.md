# フロー
```mermaid
flowchart TD  
  
F[Fact]  
F --> R[Risk Pattern]  
F --> I[Issue]  
F --> A[Alert]
F --> I[Issue（risk triggers内蔵）]
```

# リスクレベル
```yaml
level:  
- 低  
- 中  
- 高  
- 致命的
```