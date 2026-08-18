# Opportunity Analysis Skill

## 1. Purpose

Market Researchで収集された市場情報を入力として、

「今から参入する価値がある可能性が高い領域はどこか」

を評価・優先順位付けする。

本Skillは市場調査そのものを行うものではない。

Market Research
↓
Opportunity Analysis
↓
Theme Discovery
↓
Article Planning
↓
Article Creation
↓
Publishing
↓
Performance Analysis

というパイプラインにおいて、Market ResearchとTheme Discoveryの間に位置する。

Opportunity Analysisの目的は「最も人気のあるジャンル」を選ぶことではなく、

- 需要が存在する
- Monetizationの可能性がある
- 競合が過度に強くない
- 新規参入可能性がある
- 差別化できる
- 再現性が期待できる
- 情報が十分に新しい
- 今後も需要が期待できる

という複数の条件を組み合わせ、

「参入機会（Opportunity）」

を発見することである。

---

# 2. Core Principle

## Principle 1: Popularity ≠ Opportunity

人気が高いジャンルだからといって、参入価値が高いとは限らない。

以下を区別する。

Popularity
= どれだけ注目されているか

Demand
= 読者側に需要が存在するか

Monetization
= お金に変換できる可能性があるか

Opportunity
= 新規参入者が実際に勝負できる可能性があるか

したがって、

「人気だから参入する」

という判断は禁止する。

---

## Principle 2: Competitionを必ず評価する

需要・収益性だけで判断してはいけない。

Demandが高くても、

- Competitionが非常に高い
- Differentiation Potentialが低い
- Entry Difficultyが高い

場合、そのジャンルは新規参入先として不適切な可能性が高い。

特に、

Demand High
+
Monetization High
+
Competition Very High
+
Differentiation Very Low

という組み合わせは、Negative Opportunityとして扱う。

---

## Principle 3: Opportunity Scoreだけで判断しない

Opportunity Scoreは候補を比較するための補助指標であり、最終判断そのものではない。

以下のようなケースでは、Scoreが高くてもTierを下げる。

- Competitionが極端に高い
- Differentiationが極端に低い
- Evidence ConfidenceがLow
- RiskがHigh
- Entry Difficultyが高い
- Market Researchの根拠が単一事例に依存している
- データの矛盾が大きい

Opportunity Scoreと最終Tierは別概念として扱う。

同程度のOpportunity Scoreでも、Competition、Differentiation、Evidence Confidence、RiskによってTierが異なる場合がある。

---

## Principle 4: Evidence First

Market Researchに存在しない事実を勝手に補完しない。

特に以下は禁止する。

- 売上の推測
- PVの推測
- 購入者数の推測
- 成長率の推測
- 市場規模の推測
- 競合数の推測
- フォロワー数の推測
- 利益率の推測

必要な情報が存在しない場合は、

「不明」
「推定」
「要追加調査」

のいずれかを明記する。

---

## Principle 5: Do Not Overfit

単一の成功事例からジャンル全体の収益性を判断してはいけない。

例えば、

「フォロワー400人未満で月2万円稼いだ事例がある」

ことから、

「恋愛ジャンルなら月2万円稼げる」

とは判断しない。

正しくは、

「少フォロワーから収益化した事例が1件確認されており、参入可能性を示唆する。ただし再現性は未検証」

とする。

自己申告の収益情報は、

- 自己申告
- 単一事例
- 第三者検証なし

などの制約を必ず明記する。

---

# 3. Input

主な入力はMarket Researchのレポート。

例:

- `market/2026-08-17.md`
- `market/2026-08-17-02.md`

複数回のMarket Researchが存在する場合は、可能な限りすべて比較する。

入力データに矛盾がある場合は、一方を勝手に採用せず、

- 情報源
- 発表時期
- 情報の信頼度
- 一次情報か二次情報か
- 内容の一致・不一致

を整理する。

---

# 4. Output

最終成果物は以下の構造を基本とする。

1. Executive Decision
2. Opportunity Ranking
3. Opportunity Gap Analysis
4. Negative Opportunity
5. Tier 1: Immediately Research
6. Tier 2: Watchlist
7. Tier 3: Avoid for Now
8. Additional Research Queue
9. Evidence & Methodology Notes
10. Quality Gate

---

# 5. Evaluation Axes

各候補を以下の8軸で評価する。

## 5.1 Demand

読者側の需要。

評価:

1〜3: 需要が弱い
4〜5: 小規模
6〜7: 中〜高
8〜9: 高い
10: 非常に高い

Market Researchに具体的な需要データがない場合、保守的に評価する。

---

## 5.2 Monetization

有料記事、メンバーシップ、サービス、その他の収益化可能性。

評価:

1〜3: 収益化が難しい
4〜5: 限定的
6〜7: 可能性あり
8〜9: 高い
10: 非常に高い

「人気がある」だけではMonetizationを高くしない。

---

## 5.3 Competition

競合の強さ。

10が「競合が非常に強い」。

評価:

1〜3: 競合が少ない
4〜5: 中程度
6〜7: やや強い
8〜9: 強い
10: 非常に強い

Market Researchに具体的な競合数がない場合、推定であることを明記する。

---

## 5.4 Reproducibility

他の新規参入者にも成功パターンを再現できる可能性。

評価:

1〜3: 再現困難
4〜5: 低〜中
6〜7: 中〜高
8〜9: 高い
10: 非常に高い

個人の特殊な経歴・知名度・資格などに強く依存する場合は低く評価する。

---

## 5.5 Entry Difficulty

参入難易度。

10が「非常に参入しにくい」。

評価:

1〜3: 参入しやすい
4〜5: 比較的容易
6〜7: 中程度
8〜9: 難しい
10: 非常に難しい

---

## 5.6 Freshness

情報・市場の新しさ。

評価:

1〜3: 古い
4〜5: やや古い
6〜7: 比較的新しい
8〜9: 新しい
10: 非常に新しい

古い情報を現在の市場状況として扱わない。

---

## 5.7 Trend Momentum

現在および今後の伸び。

Market Researchで確認された、

- 急成長カテゴリ
- 成長率
- 新規参入増加
- 継続課金の増加
- 市場拡大

などを根拠に評価する。

根拠が弱い場合は保守的に評価する。

---

## 5.8 Differentiation Potential

新規参入者が独自性を作れる可能性。

評価:

1〜3: 差別化困難
4〜5: やや困難
6〜7: 差別化可能
8〜9: 差別化しやすい
10: 非常に差別化しやすい

---

# 6. Opportunity Score

Opportunity Scoreは以下の加重式で計算する。

Demand × 0.15
+
Monetization × 0.25
+
(10 - Competition) × 0.10
+
Reproducibility × 0.15
+
(10 - Entry Difficulty) × 0.10
+
Freshness × 0.05
+
Trend Momentum × 0.10
+
Differentiation Potential × 0.10

合計をOpportunity Scoreとする。

Scoreは1〜10で表示し、小数点以下1桁に丸める。

重要:

CompetitionとEntry Difficultyは、

10 = 悪い

という評価方向なので、Score計算時には10から引く。

---

# 7. Grade

Opportunity Scoreを以下の基準でGrade化する。

| Score | Grade |
|---|---|
| 8.0〜10.0 | S |
| 7.0〜7.9 | A |
| 6.0〜6.9 | B |
| 5.0〜5.9 | C |
| 4.0〜4.9 | D |
| 0〜3.9 | E |

ただしGradeはOpportunity Scoreのみで最終判断しない。

---

# 8. Evidence Confidence

各候補にEvidence Confidenceを付与する。

## High

- 複数の信頼性の高い情報源
- 公式情報
- 複数の独立した事例
- 主張が情報源間で概ね一致

## Medium

- 一部は公式情報
- 具体的事例は存在する
- ただしデータ量が少ない
- 一般化には注意が必要

## Low

- 単一情報源
- 自己申告のみ
- 情報源間で大きな矛盾
- 根拠となる具体的データが少ない

Evidence ConfidenceがLowの場合、Opportunity Scoreが高くてもTierを下げることを検討する。

---

# 9. Risk

以下の観点からRiskを評価する。

- Competition Risk
- Monetization Risk
- Reproducibility Risk
- Platform Risk
- Information Reliability Risk
- Legal / Ethical Risk
- Operational Risk
- Audience Size Risk

最終的に、

Low
Medium
High

で評価する。

---

# 10. Opportunity Gap

最も重要な分析の一つ。

以下のような組み合わせを探す。

## Pattern A

Demand High
+
Monetization High
+
Competition Medium/Low

---

## Pattern B

Demand Medium
+
Monetization High
+
Differentiation High
+
Entry Difficulty Low

---

## Pattern C

Large Genre
+
High Competition

↓

Niche Subgenre

↓

Low Competition
+
Specific Audience
+
Specific Problem

という構造を探す。

---

# 11. GenreからSubgenreへ分解する

Market Researchのジャンルをそのまま評価するだけでは不十分。

例えば、

AI活用

というジャンルがCompetition 9の場合でも、

AI活用
├── 育児 × AI
├── 資格 × AI
├── 占い × AI
├── 営業 × AI
└── デザイン × AI

などに分解することでOpportunity Gapが存在する可能性がある。

ただし、SubgenreのCompetitionやDemandをMarket Researchから直接確認できない場合、

「推定」

として扱う。

---

# 12. Negative Opportunity

人気が高いにもかかわらず、現時点では参入を推奨しない候補を必ず検討する。

典型例:

Demand High
+
Monetization High
+
Competition Very High
+
Differentiation Very Low

このような候補はOpportunity Scoreが高くてもNegative Opportunityに分類できる。

Negative Opportunityでは、

1. なぜ人気なのか
2. なぜ収益化できそうなのか
3. なぜ参入しないのか
4. どの条件なら再検討できるのか

を説明する。

---

# 13. Tier Classification

## Tier 1: Immediately Research

Theme Discoveryにすぐ渡す候補。

条件の目安:

- Opportunity Score 6.0以上
- Competitionが過度に高くない
- Differentiation Potentialが一定以上
- Evidence ConfidenceがMedium以上
- Riskが許容範囲
- 具体的なThemeへ分解できる

Tier 1は通常3〜5候補程度に絞る。

---

## Tier 2: Watchlist

可能性はあるが、追加データが必要な候補。

例:

- 競合状況が不明
- 収益化事例が少ない
- Demandが不明
- 情報源が少ない
- Themeの具体化が不十分

---

## Tier 3: Avoid for Now

現時点では参入を推奨しない候補。

理由を必ず明記する。

ただし、

「永続的に参入禁止」

ではない。

市場状況や差別化条件が変化した場合は再評価する。

---

# 14. TierとScoreの関係

TierはScoreの順位だけで決めない。

例えば、

AI活用
Score 6.6

育児メンバーシップ
Score 6.6

であっても、

AI活用:
Competition 9
Differentiation 3

育児メンバーシップ:
Competition 5
Differentiation 6

であれば、後者を優先する。

つまり、

Opportunity Score
+
Competition
+
Differentiation
+
Evidence Confidence
+
Risk

を総合してTierを決定する。

---

# 15. Additional Research Queue

Opportunity Analysisで判明した「まだ判断できない問題」を次の調査タスクとして整理する。

優先順位を付けて列挙する。

例:

1. 育児×AIの競合記事を追加調査
2. 育児メンバーシップの会員数・価格・更新頻度を調査
3. 恋愛系の少フォロワー収益化事例を複数収集
4. 占い系の収益化事例を追加調査
5. 情報源間で矛盾しているカテゴリを一次情報で確認

Additional Research QueueはTheme Discoveryで必要な情報と、市場調査へ戻すべき情報を区別する。

---

# 16. Theme Discoveryへの引き渡し

Tier 1候補は、単なるジャンル名ではなく、Theme Discoveryで検証できる形にする。

悪い例:

育児

良い例:

育児 × AI活用 × 時短ノウハウ

より具体的な例:

- 育児中の家事をAIで効率化する方法
- 子どもの学習をAIで支援する方法
- 育児記録をAIで整理する方法

ただし、この段階では最終テーマを確定しない。

Opportunity Analysisでは、

「調査する価値のある仮説」

を作る。

実際に需要・競合・価格・読者反応を検証するのはTheme Discoveryの役割。

---

# 17. Do Not Overreach

Opportunity Analysisで以下を断定してはいけない。

- 「必ず稼げる」
- 「このジャンルなら成功する」
- 「競合が少ない」
- 「需要が確実にある」
- 「月○万円稼げる」
- 「初心者でも稼げる」
- 「このテーマなら売れる」

根拠がない場合は、

- 可能性がある
- 示唆される
- 仮説
- 要追加調査
- 現時点では判断不能

などの表現を使用する。

---

# 18. Market Researchとの責務分離

## Market Research

「市場では何が起きているか？」

を調査する。

調査対象:

- 人気ジャンル
- 成長ジャンル
- 有料記事
- メンバーシップ
- 価格
- 収益事例
- 競合
- トレンド
- 公式データ

---

## Opportunity Analysis

「その市場情報から、どこに参入機会がありそうか？」

を判断する。

対象:

- Demand
- Monetization
- Competition
- Reproducibility
- Entry Difficulty
- Freshness
- Trend Momentum
- Differentiation
- Risk
- Evidence Confidence

---

## Theme Discovery

「そのOpportunityを、実際にnoteで勝負できる具体的なテーマまで絞り込めるか？」

を検証する。

したがって、

Market Researchで発見した情報をOpportunity Analysisが再評価し、

Opportunity Analysisで選んだ候補をTheme Discoveryがさらに検証する。

---

# 19. Output Format

最終レポートは以下の形式を基本とする。

# Opportunity Analysis

分析日:

入力:

パイプライン位置づけ:

---

## Executive Decision

全体結論。

S/A/B/C/D/Eの候補数。

Tier 1候補。

Negative Opportunity。

---

## Opportunity Ranking

| Rank | Genre | Subgenre/Theme | Opportunity Score | Grade | Evidence | Risk | Recommendation |
|---|---|---|---:|---|---|---|---|

---

## Opportunity Gap Analysis

発見したOpportunity Gapをパターンごとに説明する。

---

## Negative Opportunity

人気だが現時点では推奨しない候補。

---

## Tier 1: Immediately Research

各候補について、

- Genre / Subgenre
- Opportunity Score
- Evidence Confidence
- Risk
- 各評価軸
- Why This Opportunity
- Main Risks
- What to Research Next

を記載する。

---

## Tier 2: Watchlist

| Genre / Subgenre | Score | 追加で必要なデータ |
|---|---:|---|

---

## Tier 3: Avoid for Now

| Genre / Subgenre | Score | 非推奨理由 |
|---|---:|---|

---

## Additional Research Queue

追加調査を優先順位順に列挙する。

---

## Evidence & Methodology Notes

- 使用したMarket Research
- データの制約
- 推定値
- 自己申告データ
- 情報源間の矛盾
- Score計算方法

を記載する。

---

## Quality Gate

以下を確認する。

- [ ] PopularityとMonetizationを分離した
- [ ] Competitionを評価した
- [ ] Entry Difficultyを評価した
- [ ] Reproducibilityを評価した
- [ ] Information Freshnessを評価した
- [ ] Trend Momentumを評価した
- [ ] Differentiation Potentialを評価した
- [ ] Opportunity Scoreを計算した
- [ ] Evidence Confidenceを付けた
- [ ] Riskを評価した
- [ ] 自己申告データを一般化していない
- [ ] 古いデータを現在の市場状況として扱っていない
- [ ] 不明なデータを勝手に補完していない
- [ ] Negative Opportunityを検討した
- [ ] Opportunity ScoreだけでTierを決定していない
- [ ] Tier 1候補をTheme Discoveryへ渡せる形にした
- [ ] Additional Research Queueを作成した

---

# 20. Final Decision Rule

最終的な意思決定では、

Opportunity Score最大
=
最優先

とはしない。

以下の順番で判断する。

1. Evidenceが十分か
2. Demandが存在するか
3. Monetizationの可能性があるか
4. Competitionが許容範囲か
5. Entry Difficultyが許容範囲か
6. Differentiationできるか
7. Reproducibilityがあるか
8. Trendが維持される可能性があるか
9. Riskが許容範囲か
10. Theme Discoveryで具体的に検証できるか

特に、

「需要があるが競合が強すぎる」

「収益化できるが差別化できない」

「Scoreは高いがEvidenceが弱い」

という候補を無理に推奨しない。

Opportunity Analysisの目的は、

「最も数字が高いジャンルを選ぶこと」

ではなく、

「現時点の証拠から、新規参入者が次に調査する価値のあるOpportunityを発見すること」

である。

そのため、最終的にS/Aランクが存在しなくても問題ない。

十分な根拠がない場合は、

「現時点では明確なS/A Opportunityは発見されなかった」

という結論を許容する。

最終的にはTier 1候補をTheme Discoveryへ引き渡し、具体的なテーマ・読者・課題・競合・価格・販売事例の検証へ進む。

## Weekly Pipeline Integration

Opportunityの結論・反証・不確実性を、案件フォルダの `01-research/research.md` に集約する。市場調査の観測値、評価、仮説を混同せず、次工程が同じ `issue_id` を参照できるようにする。
