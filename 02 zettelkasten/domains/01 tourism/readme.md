# 構成
domain/tourism/
├─00_Hub/
│  ├─Tourism Hub.md
│  ├─00_Readme.md
│  ├─10_Workflow.md
│  └─90_Templates.md
│
├─01_Taxonomy/                # 評価軸（あなたが既に作っている概念群の受け皿）
│  ├─Boundary.md              # 境界性
│  ├─Immersion.md             # 没入性
│  ├─Symbolism.md             # 象徴性
│  ├─MeaningTimeLayers.md     # 意味体験の時間層
│  ├─MemoryDevices.md         # 記憶装置
│  └─...(追加していく)
│
├─02_Stock/                   # 観光地（資産）そのものの台帳
│  ├─Places/
│  │  ├─JP/
│  │  └─Overseas/
│  ├─Routes/                  # 回遊・モデルコース（線）
│  ├─Areas/                   # 歴史地区など（面）
│  └─Events/                  # 祭り・イベント（時間資産）
│
├─03_Cases/                   # 訪問記録・観測ログ（一次情報）
│  ├─Trips/
│  └─SpotChecks/
│
├─04_Analysis/
│  ├─Scorecards/              # 採点表（チェックシート）
│  ├─Comparisons/             # A vs B 比較
│  ├─Segments/                # ターゲット別分析（家族/カップル/オタク等）
│  └─Hypotheses/              # 仮説→検証
│
├─05_Maps_Assets/             # 地図・図・写真（外部リンクでもOK）
│  ├─Maps/
│  ├─Photos/
│  └─Diagrams/
│
└─06_Operations/              # 実務への落とし込み（商品・運用）
   ├─Products/                # ツアー商品設計
   ├─GuidingScripts/          # ガイド台本
   ├─Risk_Compliance/         # 事故・炎上・法務/ルール
   └─KPI/                     # 集客/満足/回遊/単価
# 運用
##  Taxonomy = 「評価軸の辞書」
境界性/没入性/象徴性…など 概念定義・評価基準・観測ポイント
観光地の個別ノートには “結果” を書く。基準は taxonomy 側に置く。
## Stock = 「観光資産の台帳（静的ストック）」
観光地そのもののプロフィール
ここが「資産データベース」扱い
- Places（点る資産）
- Routes（線資産）
- Areas（面資産）
- Events（時間資産）
## Cases = 「訪問ログ（一次情報）」
行った/見た/聞いた/混雑/導線/天気/料金/体験価値の変動など
ストックノートの“根拠”としてリンクする
## Analysis = 「採点・比較・セグメント・仮説検証」
チェックシート、ランキング、改善案、商品化適性
## Operations = 「売り物・運用・リスク」
ここに落とせて初めて “分析が金に変わる”

# 運用フロー
候補をStockに登録（仮でも良い）
現地/資料でCaseを書く（一次情報優先）
Scorecardで採点（taxonomy基準に従う）
セグメント適合（家族/友人5人/インバウンド等）
商品化判定（運用負荷・リスク・単価）
Productsへ落とす（台本・導線・KPI）