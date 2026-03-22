# Flow
1. Fact Finding Engine  
2. Normative Engine  
3. Conclusion

# 法律推論パイプライン  
## Step1 争点ノード
[[争点ノード]]
## Step2 事実認定  
[[Fact Finding Engine]]    
## Step3 規範適用  
[[Normative Engine]]    
## Step4 結論  
- 適法
- 違法
- 不明

## フロー
```mermaid
flowchart TD  
  
IP[interpretation]  
PCN[Point of Contention Node]
FF[Fact Finding]  
NM[normative]  
DS[decision]  

IP --> PCN
PCN --> FF  
FF --> NM  
NM --> DS
```
