# 基本構造

```mermaid
flowchart TD  
  
Q[Question]  
  
Q --> D[Domain Detection]  
  
D --> E[Engine Selection]  
  
E --> A[Application Context]  
  
A --> Solution
```

---

# 固有構造
```mermaid
flowchart TD  
  
%% =========================  
%% Domain  
%% =========================  
  
L[law]  
H[history]  
B[business]  
G[geography]  
T[tourism]  
S[story]  
R[reading]  
P[photography]  
M[music]  
F[fashion]  
TP[tourism_philosophy]  
  
%% =========================  
%% Engines  
%% =========================  
  
IP[interpretation]  
  
NM[normative]  
CS[causal]  
DS[decision]  
EL[evaluation]  
MN[meaning]  
  
SP[spatial]  
NW[network]  
TPL[temporal]  
EX[expression]  
  
%% =========================  
%% Routing  
%% =========================  
  
R --> IP  
  
IP --> NM  
IP --> CS  
IP --> MN  
  
L --> NM  
H --> CS  
B --> DS  
  
G --> SP  
G --> NW  
  
T --> EL  
T --> SP  
  
S --> MN  
S --> TPL  
S --> EX  
S --> CS  
S --> EL  
  
P --> EX  
P --> EL  
P --> MN  
  
M --> TPL  
M --> EX  
  
F --> EX  
F --> EL  
  
TP --> MN

%% =========================  
%% InterEngine  
%% =========================  

CS --> DS  
EL --> DS  
MN --> EX  
SP --> EL
NM --> DS
```

# Routing ルール
## Engine Hub
[[Engine Hub]]に則る。

## Question Type Routing

- なぜ？ → causal
- どうすべき？ → decision
- 正しい？ → normative
- どちらが良い？ → evaluation
- どういう意味？ → meaning
- どう構成されている？ → spatial / temporal
- どう表現する？ → expression
- 文章を理解したい → interpretation

## Execution Flow

1. Questionを書く
2. Interpretationを通す（必須）
3. Question Typeを判定
4. Engineを選択
5. 必要なら複数Engineを連結
6. Expressionで出力