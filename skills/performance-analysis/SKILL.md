# Performance Analysis Skill

## 1. Purpose

このSkillは、公開済み記事のPerformance Dataを分析し、

1. 記事がどのような反応を得たかを把握する
2. どの要素が成果に寄与した可能性があるかを分析する
3. 何が問題だった可能性があるかを特定する
4. 次の記事で検証すべき改善案を作る
5. Market Research / Opportunity Analysis / Theme Discovery / Article Planningへフィードバックする

ためのSkillである。

本Skillの目的は「公開済み記事を後から書き換えること」ではない。

目的は、

「今回の記事で得られたデータを、次のコンテンツ制作に利用可能な知見へ変換すること」

である。

---

## 2. Pipeline Position

本Skillは以下のContent Creation Pipelineの最後に位置する。

Market Research
↓
Opportunity Analysis
↓
Theme Discovery
↓
Article Planning
↓
Author Experience Extraction
↓
Article Writing
↓
Publishing
↓
Performance Analysis
↓
Next Content Planning

Performance Analysisは、次回のMarket Research / Opportunity Analysis / Theme Discovery / Article Planningに対するFeedback Sourceとして機能する。

---

## 3. Core Principles

### Principle 1: Data First

Performance Analysisでは、確認できるデータを最優先する。

以下を区別する。

- Observed Data
- Calculated Metric
- Interpretation
- Hypothesis
- Unknown

例えば、

「購入率が低かった」

は、購入数とPVから計算できる場合はObserved / Calculatedとして扱う。

一方、

「タイトルが悪かったから購入率が低かった」

は直接証明できないため、Hypothesisとして扱う。

---

### Principle 2: Unknown Must Remain Unknown

データが存在しない場合、推測によって補完してはいけない。

例えば、

PVしか存在しない場合、

- スキ率
- 購入率
- 売上
- 有料部分到達率

などを推測してはいけない。

必ず、

`Unknown`

として記録する。

---

### Principle 3: Correlation Is Not Causation

Performance Dataから因果関係を勝手に断定してはいけない。

例えば、

「タイトルを変更したらPVが増えた」

という事実があっても、

「タイトル変更によってPVが増えた」

と断定してはいけない。

正しくは、

「タイトル変更後にPVが増加した。タイトル変更が寄与した可能性はあるが、流入元・公開タイミング・SNS投稿など他の要因を切り分けられていない」

とする。

---

### Principle 4: Do Not Rewrite Author Experience

Performance結果を理由に、Author Experience Extractionの内容を書き換えてはいけない。

例えば、

記事が売れなかったからといって、

「実はこの方法が効果的だった」

など、著者が経験していない内容を追加してはいけない。

Performance Dataは、

「記事がどう受け取られたか」

を示すデータであり、

「著者が何を経験したか」

を変更するデータではない。

---

### Principle 5: Separate Content Truth From Performance

以下は別の情報として扱う。

- Author Experienceの真偽
- Article ContentのIntegrity
- Reader Performance
- Monetization Performance

記事が売れなかったからといって、記事内の経験が間違っていたことにはならない。

逆に、記事が売れたからといって、記事内の主張が一般的に正しいことにもならない。

---

### Principle 6: Analyze Before Optimizing

いきなり、

- タイトルを変える
- 価格を下げる
- 有料部分を増やす
- CTAを強くする

などの改善を行ってはいけない。

まず、

1. Data
2. Metrics
3. Observation
4. Interpretation
5. Hypothesis
6. Recommendation

の順番で分析する。

---

### Principle 7: One Article Is Not Enough To Establish a Universal Rule

単一記事の結果から、

「このテーマは売れる」
「このタイトル形式は伸びる」
「この価格が最適」
「恋愛記事は売れない」

などの一般法則を作ってはいけない。

単一記事では、

「今回の記事ではこの傾向が見られた」

というレベルに留める。

複数記事のデータが蓄積された場合のみ、横断的な傾向を分析する。

---

### Principle 8: Optimize for Learning, Not Only Revenue

Performance Analysisの目的は短期的な売上最大化だけではない。

特に初期段階では、

- どのテーマに反応があるか
- どの読者層が反応するか
- どのタイトルがクリックされるか
- 無料から有料へどれくらい移行するか
- どの価格帯が受け入れられるか

などのLearningを蓄積することを重視する。

---

# 4. Required Inputs

最低限、以下の情報を受け取る。

```yaml
article:
  title:
  article_type:
  target_reader:
  primary_theme:
  unique_angle:
  core_thesis:
  monetization_model:
  price:
  publication_date:
  platform:

performance:
  measurement_date:
  pv:
  likes:
  comments:
  purchases:
  revenue:
```

可能であれば以下も取得する。

```yaml
performance:
  paid_views:
  paid_view_rate:
  purchase_rate:
  conversion_rate:
  external_clicks:
  sns_impressions:
  sns_clicks:
  search_impressions:
  search_clicks:
  followers_at_publication:
  followers_after_publication:

experiment:
  title_version:
  thumbnail_version:
  price_version:
  paywall_version:
  cta_version:
```

入力されていない項目はUnknownとする。

---

# 5. Input Validation

分析開始前に以下を確認する。

### Required

- Article WritingまたはPublishing Reportが存在する
- Article Titleが確認できる
- Publication Dateが確認できる、またはUnknownとして明示されている
- Performance Dataの測定日時が確認できる
- PVなど最低1つのPerformance Dataが存在する

### Recommended

- Article Planning
- Author Experience Extraction
- Publishing Report
- 複数記事のPerformance Data

入力が不足している場合は、不足項目を明示する。

不足しているデータを推測してはいけない。

---

# 6. Performance Data Classification

取得したデータを以下の4種類に分類する。

## 6.1 Observed Data

実際に取得した数値。

例:

```yaml
pv: 1240
likes: 42
purchases: 5
revenue: 1500
```

---

## 6.2 Calculated Metrics

Observed Dataから計算できる指標。

例:

```text
Like Rate = Likes / PV
Purchase Rate = Purchases / PV
Revenue per PV = Revenue / PV
Average Revenue per Purchase = Revenue / Purchases
```

---

## 6.3 Interpretation

データから合理的に読み取れる解釈。

例:

「PVに対してスキ数が比較的少ない」

---

## 6.4 Hypothesis

結果の理由についての仮説。

例:

「タイトルはクリックを獲得できた一方、本文の期待値との一致が弱かった可能性がある」

Hypothesisは必ずHypothesisとして明示する。

---

# 7. Measurement Window

Performanceは時間経過によって変化するため、測定日時を必ず記録する。

可能であれば以下のタイミングで取得する。

```text
T+1 day
T+3 days
T+7 days
T+14 days
T+30 days
```

例:

```yaml
measurement:
  publication_date: 2026-08-18

  snapshots:
    - elapsed_days: 1
      pv: 120
      likes: 8
      purchases: 0

    - elapsed_days: 3
      pv: 340
      likes: 19
      purchases: 1

    - elapsed_days: 7
      pv: 620
      likes: 31
      purchases: 3
```

異なる経過時間のデータを同一条件として比較してはいけない。

---

# 8. Basic KPI Analysis

取得可能な指標を以下の順番で分析する。

## 8.1 Reach

主にPVを見る。

```text
PV
External Impressions
Search Impressions
SNS Impressions
```

目的:

「そもそも記事が読者に届いたか」

を確認する。

---

## 8.2 Engagement

```text
Like Rate = Likes / PV
Comment Rate = Comments / PV
```

目的:

「読者が記事を読んだ後に反応したか」

を見る。

---

## 8.3 Monetization

```text
Purchase Rate = Purchases / PV
Revenue per PV = Revenue / PV
Average Revenue per Purchase = Revenue / Purchases
```

PurchasesがUnknownまたは0の場合、計算できない指標はUnknownとする。

---

## 8.4 Conversion

可能であれば、

```text
Paid View → Purchase
```

のConversion Rateを分析する。

PVしかない場合は、

```text
PV → Purchase
```

を暫定的なPurchase Rateとして扱う。

ただし、これは有料部分への到達率を考慮していないため、正式なPaid Conversion Rateとは区別する。

---

# 9. Funnel Analysis

記事を以下のFunnelとして考える。

```text
Impression
    ↓
Click
    ↓
Article View
    ↓
Read
    ↓
Paid Section
    ↓
Purchase
    ↓
Engagement
```

取得できるデータだけでFunnelを構築する。

例えば、

```text
SNS Impression
↓
SNS Click
↓
PV
↓
Paid View
↓
Purchase
```

各段階で大きなDropがある場所を特定する。

データがない段階はUnknownとする。

---

# 10. Content Performance Analysis

Performanceを以下の観点から分析する。

## 10.1 Topic

- テーマ
- 読者ニーズ
- 問題の明確さ
- Unique Angle

---

## 10.2 Title

以下を見る。

- PV
- CTR（取得可能な場合）
- SNSクリック
- Searchクリック
- タイトル変更前後

タイトルについては、

「PVが高い」

だけでは成功と判断しない。

---

## 10.3 Hook

無料部分の、

- 冒頭
- Problem
- Context
- Promise
- Paywall前のHook

を確認する。

特に、

「無料部分を読んだ後に続きを読みたい状態になっているか」

を分析する。

---

## 10.4 Paid Section

以下を分析する。

- 無料部分から有料部分への価値移動
- 有料部分の独自性
- 具体性
- 経験の深さ
- Lesson
- Reflection

ただし、購入率だけを見て、

「有料部分の内容が悪い」

と断定してはいけない。

---

## 10.5 Price

価格変更が行われた場合は、

```text
Price
↓
Purchase
↓
Revenue
```

の変化を見る。

例えば、

```text
300円 → 500円
```

に変更した場合、

購入数だけではなく、

```text
Revenue = Purchases × Price
```

を比較する。

---

## 10.6 CTA

CTAについて、

- CTAクリック
- 購入
- スキ
- コメント

など取得可能なデータを分析する。

CTAの効果を直接測定できない場合、

「CTAが原因」

と断定してはいけない。

---

# 11. Thumbnail Analysis

Thumbnail変更がある場合、

```text
Thumbnail A
↓
Performance
↓
Thumbnail B
↓
Performance
```

を比較する。

可能であればCTRを使用する。

CTRが存在しない場合、

PVの変化のみからThumbnail効果を断定しない。

---

# 12. Title Experiment Analysis

タイトル変更があった場合は、必ずVersion管理する。

```yaml
title_experiment:
  - version: A
    title:
    period:
    pv:
    ctr:
    purchases:

  - version: B
    title:
    period:
    pv:
    ctr:
    purchases:
```

比較する場合、

- 測定期間
- 流入量
- SNS露出
- Search exposure
- Price
- Thumbnail

など、他の変更も確認する。

---

# 13. Monetization Analysis

収益記事の場合、以下を分析する。

```text
Revenue
Purchase Count
Purchase Rate
Average Revenue per Purchase
Revenue per PV
```

重要なのは、

「購入数最大化」

だけではなく、

「Revenue最大化」

を見ることである。

例えば、

```text
¥300 × 10 purchases = ¥3,000

¥500 × 7 purchases = ¥3,500
```

の場合、購入数は減少しているが売上は増加している。

そのため、Price変更では購入数とRevenueを両方評価する。

---

# 14. Free / Paid Boundary Analysis

Free / Paid Articleの場合、以下を分析する。

```text
PV
↓
Paid Section View
↓
Purchase
```

可能であれば、

```text
Paid View Rate
Purchase Rate
Paid Conversion Rate
```

を算出する。

### Interpretation

例えば、

```text
PV高
Paid View高
Purchase低
```

の場合、

- 有料部分への興味はある
- しかし購入に至っていない

という可能性がある。

ただし、

「価格が高い」
「有料部分が弱い」

などの原因はHypothesisとして扱う。

---

# 15. Performance Diagnosis

記事を以下の4タイプに分類する。

## Type A: Reach Strong / Conversion Strong

```text
PV ↑
Engagement ↑
Purchase ↑
```

→ 成功パターン候補。

次回、

- テーマ
- タイトル
- Unique Angle
- Monetization

の再利用を検討する。

---

## Type B: Reach Strong / Conversion Weak

```text
PV ↑
Purchase ↓
```

可能性:

- 無料部分で価値を消費した
- 有料部分への期待値が弱い
- Priceが高い
- Target Readerと購入者が一致していない
- CTAが弱い

ただし原因はHypothesisとして扱う。

---

## Type C: Reach Weak / Conversion Strong

```text
PV ↓
Purchase Rate ↑
```

可能性:

- 内容自体は刺さっている
- Distributionが弱い
- Title / Thumbnailが弱い
- Target Audienceへの到達が不足

次回はDistribution / Title / Topic Discoveryを優先して改善する。

---

## Type D: Reach Weak / Conversion Weak

```text
PV ↓
Purchase Rate ↓
```

可能性:

- Topic Demandが弱い
- Target Readerが曖昧
- Article Promiseが弱い
- Titleが弱い
- Monetization設計が弱い

ただし、単一記事だけでTopicそのものを否定しない。

---

# 16. Hypothesis Ranking

改善仮説を以下の形式で整理する。

```yaml
hypotheses:
  - hypothesis:
    evidence:
    confidence:
    test:
    priority:
```

Confidence:

```text
High
Medium
Low
```

Priority:

```text
P0
P1
P2
```

### P0

次回必ず検証すべき重要仮説。

### P1

有力だが、他の要因も考えられる仮説。

### P2

現時点では弱い仮説。

---

# 17. What Worked / What Did Not Work

最終レポートでは必ず以下を分ける。

## What Worked

データによって支持される良かった点。

## What Did Not Work

データによって弱かった点。

## Unknown

現時点では判断できない点。

## Hypotheses

原因として考えられる仮説。

この4つを混ぜない。

---

# 18. Next Experiment Design

Performance Analysisの最重要Output。

次回記事で試すことを具体化する。

例えば、

```yaml
next_experiments:
  - variable: title
    current:
    next:
    hypothesis:
    metric:

  - variable: price
    current:
    next:
    hypothesis:
    metric:

  - variable: topic
    current:
    next:
    hypothesis:
    metric:
```

一度に大量の変数を変更しない。

可能な限り、

```text
1記事 = 1〜2個の主要仮説
```

として検証する。

---

# 19. Feedback to Previous Pipeline

Performance Analysisの結果を次の工程へ返す。

## Market Research

市場の需要仮説を更新する。

例:

```text
婚活全般
↓
初対面の会話
↓
「会話術」より「相性」に関する体験談
```

など、反応のあった領域を記録する。

ただし単一記事の結果を市場全体の事実に変換しない。

---

## Opportunity Analysis

Opportunity Scoreの仮説を更新する。

評価対象:

- Demand
- Competition
- Monetization
- Personal Fit
- Evidence Strength

---

## Theme Discovery

反応のあったテーマ候補を追加する。

例えば、

```text
「婚活 × 会話術」
「婚活 × 相性」
「婚活 × 行動量」
```

など。

---

## Article Planning

次回の記事について、

- Target Reader
- Article Type
- Unique Angle
- Monetization
- Price
- CTA
- Free / Paid Boundary

などを改善する。

---

# 20. Feedback Must Not Contaminate Author Experience

Performance AnalysisからAuthor Experience Extractionへ逆流させてはいけない。

正しいFeedback:

```text
記事Aは「相性」という切り口で反応が良かった
↓
次の記事でも相性というテーマを検証する
```

誤ったFeedback:

```text
記事Aが売れた
↓
著者は相性について成功体験を持っていたことにする
```

後者は禁止。

---

# 21. Cross-Article Analysis

複数記事のPerformance Dataが存在する場合、記事単位ではなく横断分析を行う。

比較項目:

```text
Theme
Article Type
Title Pattern
Target Reader
Price
Paid Ratio
CTA
Thumbnail
PV
Like Rate
Purchase Rate
Revenue
```

例えば、

| Article | Theme | Price | PV | Purchase | Revenue |
|---|---|---:|---:|---:|---:|
| A | 婚活 | 300 | 1000 | 3 | 900 |
| B | キャリア | 500 | 700 | 8 | 4000 |
| C | 技術 | 300 | 1500 | 10 | 3000 |

などの比較を行う。

ただし、

「Bが一番良いテーマ」

と短絡的に判断せず、

- Audience Size
- Distribution
- Article Quality
- Price
- Publication Timing

なども考慮する。

---

# 22. Statistical Caution

記事数が少ない場合、統計的な結論を強く主張しない。

例えば、

記事1本だけで、

「500円が最適価格」

とは言わない。

複数記事で同様の傾向が観測された場合、

「現時点の小規模データでは500円が有力」

程度に留める。

---

# 23. Performance Baseline

記事数が増えるにつれて、個別記事だけでなくBaselineを構築する。

例:

```yaml
baseline:
  median_pv:
  median_like_rate:
  median_purchase_rate:
  median_revenue:
  median_revenue_per_pv:
```

平均値だけではなく、中央値も使用する。

極端なバズ記事による平均値の歪みを避ける。

---

# 24. Performance Score

必要に応じて総合評価を作成する。

ただし、単一のScoreだけで記事の良し悪しを判断してはいけない。

例:

```yaml
performance_score:
  reach:
  engagement:
  monetization:
  learning_value:
  overall:
```

Learning Valueを独立した評価項目として持つ。

---

# 25. Learning Value

売上が低い記事でも、

「重要な仮説を検証できた記事」

には価値がある。

例えば、

```text
Revenue: Low

しかし、

「500円でも購入されるか」

という仮説を検証できた。

→ Learning Value: High
```

この考え方を採用する。

---

# 26. Publication Context

Performanceを評価するときは、可能な限り以下を記録する。

```yaml
publication_context:
  publication_day:
  publication_time:
  sns_promotion:
  external_traffic:
  search_traffic:
  concurrent_campaign:
  related_articles:
  seasonal_factor:
```

これらが不明な場合はUnknownとする。

---

# 27. No Retroactive Optimization

Performance Analysisの結果だけを理由に、過去の記事を勝手に改変しない。

変更を行う場合は、

```text
Original Version
↓
Experiment
↓
New Version
↓
Performance Comparison
```

としてVersion管理する。

特に、

- Title
- Price
- Thumbnail
- Paywall
- CTA

を変更する場合は、変更日時とVersionを記録する。

---

# 28. Report Structure

最終レポートは以下の構造を使用する。

```text
# Performance Analysis Report

## 1. Input

## 2. Measurement Period

## 3. Raw Performance Data

## 4. Calculated Metrics

## 5. Funnel Analysis

## 6. Content Performance

## 7. Monetization Performance

## 8. What Worked

## 9. What Did Not Work

## 10. Unknown

## 11. Hypotheses

## 12. Diagnosis

## 13. Next Experiments

## 14. Feedback to Market Research

## 15. Feedback to Opportunity Analysis

## 16. Feedback to Theme Discovery

## 17. Feedback to Article Planning

## 18. Cross-Article Insights

## 19. Learning Summary

## 20. Handoff
```

---

# 29. Handoff

Performance Analysisの最後には、次のPipelineへのInputを作る。

```yaml
handoff:
  next_pipeline_stage: Article Planning

  confirmed_learnings:
    - 

  hypotheses:
    - 

  experiments_to_run:
    - 

  themes_to_research:
    - 

  title_patterns_to_test:
    - 

  pricing_to_test:
    - 

  audience_signals:
    - 

  unresolved_questions:
    - 
```

Performance Analysisだけで次の記事を決定してはいけない。

Market Research / Opportunity Analysis / Theme Discoveryの結果と統合して、次回のArticle Planningで最終決定する。

---

# 30. Backward Contamination Check

レポート作成前に以下を確認する。

- [ ] Author Experienceを書き換えていない
- [ ] UnknownをFactに変換していない
- [ ] Performanceから経験を創作していない
- [ ] CorrelationをCausationとして扱っていない
- [ ] 単一記事から一般法則を作っていない
- [ ] 数値を推測していない
- [ ] 未取得のKPIを補完していない
- [ ] 過去の記事を勝手に改変していない

---

# 31. Quality Gate

## Data Integrity

- [ ] Raw Dataの出典を確認した
- [ ] Measurement Dateを確認した
- [ ] Unknownを明示した
- [ ] 推測値をObserved Dataとして扱っていない

## Analytical Integrity

- [ ] Calculated MetricとObserved Dataを区別した
- [ ] InterpretationとHypothesisを区別した
- [ ] CorrelationとCausationを区別した
- [ ] 単一記事から一般化していない

## Content Integrity

- [ ] Author Experienceを変更していない
- [ ] Article Writingを勝手に書き換えていない
- [ ] Article TruthとPerformanceを混同していない

## Monetization Integrity

- [ ] Purchase Countを確認した
- [ ] Revenueを確認した
- [ ] Priceを確認した
- [ ] Price変更がある場合Version管理した
- [ ] RevenueとPurchase Countを分けて評価した

## Experiment Integrity

- [ ] 次回の検証仮説を明示した
- [ ] 仮説にEvidenceを付けた
- [ ] Confidenceを設定した
- [ ] 変更する変数を明確にした
- [ ] 成功判定Metricを設定した

## Pipeline Feedback

- [ ] Market ResearchへのFeedbackを作成した
- [ ] Opportunity AnalysisへのFeedbackを作成した
- [ ] Theme DiscoveryへのFeedbackを作成した
- [ ] Article PlanningへのFeedbackを作成した

---

# 32. Final Output Philosophy

## Weekly Pipeline Integration

観測値は `output/YYYY-MM-DD-<slug>/06-performance/metrics.yml`、分析と次回の仮説は `review.md` に保存する。観測値・計算値・解釈・仮説・Unknownを分離し、次の案件の `00-brief/inputs.md` から参照する。収益目標は過去の確定データが揃うまで予測値として扱わない。

このSkillの最終的な価値は、

「この記事は良かった／悪かった」

という感想を書くことではない。

以下の変換を行うことである。

```text
Performance Data
        ↓
     Metrics
        ↓
   Observations
        ↓
   Hypotheses
        ↓
     Learning
        ↓
 Next Experiments
        ↓
 Next Article Planning
```

最終的に、

「何が起きたか」

「何が分かったか」

「何がまだ分からないか」

「次に何を試すか」

を明確にする。

Performance Analysisは、コンテンツ制作Pipelineの終点ではなく、次のコンテンツ制作を開始するためのFeedback Loopである。

---

# 33. Recommended Performance Data Template

公開後は、可能であれば以下の形式でPerformance Dataを保存する。

```yaml
article_id:
title:
platform:
publication_date:

measurement:
  date:
  elapsed_days:

performance:
  pv:
  likes:
  comments:
  purchases:
  revenue:
  paid_views:
  external_clicks:
  search_clicks:
  sns_impressions:
  sns_clicks:

context:
  title_version:
  thumbnail_version:
  price:
  paywall_version:
  cta_version:

traffic:
  search:
  sns:
  direct:
  recommendation:
  unknown:

experiments:
  active:
  hypothesis:

notes:
```

同じ記事について複数回測定する場合は、各Measurementを別レコードとして保存する。

---

# 34. Recommended File Structure

```text
performance-analysis/
├── SKILL.md
└── reports/
    ├── 2026-08-20-article-001.md
    ├── 2026-08-27-article-002.md
    └── ...
```

複数記事の横断分析を行う場合は、

```text
performance-analysis/
└── cross-analysis/
    ├── 2026-08-monthly.md
    └── 2026-08-cross-article.md
```

のように管理する。

---

# 35. Example Diagnosis

例えば、

```yaml
pv: 2000
likes: 40
purchases: 2
revenue: 600
price: 300
```

だった場合、

Observed Data:

```text
PV = 2000
Likes = 40
Purchases = 2
Revenue = ¥600
```

Calculated:

```text
Like Rate = 2.0%
Purchase Rate = 0.1%
Revenue / PV = ¥0.3
```

Observation:

```text
記事への到達は一定数あった一方、
購入数はPVに対して少なかった。
```

Hypothesis:

```text
有料部分への移行価値が弱かった可能性がある。

ただし、価格・読者層・流入元などの影響を切り分けられていないため、
現時点ではLow〜Medium Confidenceとする。
```

Next Experiment:

```text
次回は価格を変更する前に、
無料部分と有料部分のValue Boundaryを改善した記事を作成し、
同程度の価格帯で比較する。
```

このように、

```text
Data
↓
Calculation
↓
Observation
↓
Hypothesis
↓
Experiment
```

の順番を崩さない。

---

# 36. Final Rule

Performance Analysisでは、

「数字に合わせて物語を作らない」

ことを最重要ルールとする。

数字が示していることだけを事実として扱い、
理由は仮説として扱い、
分からないことはUnknownとして残す。

そして、その不確実性を保ったまま、

「次に何を試せば、より多くのことが分かるか」

まで落とし込む。

これが本Skillの完成条件である。
