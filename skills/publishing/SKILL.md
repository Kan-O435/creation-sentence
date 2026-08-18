# Publishing Skill

## 0. Purpose

このSkillは、Article Writingで確定した記事を、実際の公開プラットフォームへ安全かつ一貫した形で公開するためのPublishing工程を担当する。

本Skillの目的は、記事そのものを再執筆することではない。

主な責務は以下である。

1. Article Writingの確定版を正本として受け取る
2. 公開に必要なMetadataを整理する
3. Platformを明示的に確定する
4. Platform固有の最新仕様を確認する
5. Category / Tags / Thumbnail / Price / Paywall等を確定する
6. 公開前のIntegrity Checkを実施する
7. 実際の投稿に使用できるPublishing Packageを作成する
8. 公開後のPerformance Analysisへ正確な情報を引き渡す

本Skillでは、Author ExperienceやArticle Writingの内容を勝手に変更してはならない。


---

# 1. Pipeline Position

Publishingは以下のPipelineの中で実行される。

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

PublishingはArticle Writingの後工程である。

Publishingの結果を使ってArticle Writingへ勝手に戻り、本文を書き換えてはならない。

公開後に得られたPV、Like、Purchase、Revenue等のPerformance Dataも、過去のAuthor Experienceを書き換える根拠にはならない。


---

# 2. Core Principles

## Principle 1: Article Writing is the Source of Truth

Article Writingで確定した本文をPublishingの正本とする。

Publishingでは、以下を勝手に変更してはならない。

- 本文
- タイトル
- Article Type
- Target Reader
- Unique Angle
- Core Thesis
- Author Experience
- Author Interpretation
- Result
- CTA
- Free / Paidの意味
- Experience上の不確実性

文章上の明らかなMarkdown整形のみ、Platform仕様に合わせるため必要な場合に限って変更してよい。

ただし、意味・内容・主張が変わる場合は変更してはならない。

---

## Principle 2: No Experience Creation

Publishing工程で著者経験を追加してはならない。

例えば以下を勝手に追加してはいけない。

- デート回数
- マッチング数
- 成功率
- 交際人数
- 成婚
- 収益
- 学習期間
- 婚活期間
- 会話の具体的なエピソード
- 著者が感じた感情
- 他人から聞いた経験
- 推測した結果

Article Writingに存在しない情報は、必要であればUnknownとして扱う。

---

## Principle 3: No Backward Contamination

Publishingで得られた情報によって、過去工程の事実を改変してはならない。

例えば、

記事公開後に売れた
↓
「この方法は効果があった」

と変更してはいけない。

また、

記事が売れなかった
↓
「著者の経験には価値がなかった」

とも判断してはいけない。

PerformanceとExperience Integrityは別の情報として扱う。


---

## Principle 4: Platform Accuracy

Platformを推測だけで確定してはならない。

例えば、

Market Researchでnoteを調査していた
↓
今回もnoteだろう
↓
platform: note

という処理は禁止する。

Platformは以下のいずれかとして扱う。

- 明示的に指定されたPlatform
- Pipeline設定として正式に指定されたPlatform
- Unknown

Platformが明示されていない場合は、

platform: Unknown

とする。

ただし、ユーザーが「今回はnoteで公開する」と明示した場合は、

platform: note

として確定する。

---

## Principle 5: Platform-Specific Information Must Be Verified

Platformが確定したら、そのPlatformの現在の仕様を確認する。

必要に応じてWeb検索を利用する。

確認対象は以下。

- Category
- Tags
- Character limits
- Title limits
- Subtitle
- Paywall
- Pricing
- Thumbnail
- Image requirements
- Formatting
- Publication settings
- Scheduling
- Disclosure requirements
- Affiliate rules
- Advertisement rules

古い記憶や推測だけでPlatform仕様を記述してはならない。

---

## Principle 6: Unknown Must Remain Unknown

確認できない情報を推測で埋めてはならない。

例えば、

category: Unknown

である場合、

「おそらくエッセイ・コラム」

と内部的に候補を持つことは可能だが、

category: エッセイ・コラム

と確定してはならない。

候補と確定値を明確に分離する。

推奨形式：

category: Unknown

category_proposed:
  - エッセイ・コラム


---

## Principle 7: Separate Content Decisions from Publishing Decisions

記事内容と公開設定を分離する。

Content側：

- Topic
- Experience
- Thesis
- Narrative
- Lesson

Publishing側：

- Platform
- Category
- Tags
- Thumbnail
- Price
- Paywall
- Publication Date

Publishing側の都合でContent側を改変してはならない。


---

## Principle 8: Do Not Optimize for Performance Before Publication

Publishing時点で、

「このタイトルの方がPVが増えそう」
「この表現の方が売れそう」

という理由だけでArticle Writingの本文を変更してはならない。

Performance Optimizationは公開後のPerformance Analysisで行う。

Publishingでは、

Content Integrity
+
Platform Compliance
+
Publication Readiness

を優先する。


---

# 3. Required Input

Publishingに必要な最低限のInputは以下。

## Required

### Article Writing

必須。

最低限、以下を含むこと。

- Title
- Article Body
- Article Type
- Target Reader
- Unique Angle
- Core Thesis
- Monetization Model
- CTA

Experience Reportの場合、Author Experience Integrityも確認できる状態であること。

---

## Recommended

### Article Planning

推奨。

以下の確認に利用する。

- Target Reader
- Primary Theme
- Monetization Model
- Price Hypothesis
- CTA
- Article Promise

---

### Author Experience Extraction

Experience Reportでは推奨。

以下のIntegrity Checkに利用する。

- Confirmed Facts
- Author Interpretation
- Unknown
- Contradiction
- Privacy
- Sensitivity


---

# 4. Input Validation

Publishing開始前に以下を確認する。

- Article Writingが存在する
- Article Writingの本文が確定版である
- Titleが存在する
- Article Typeが存在する
- Target Readerが存在する
- Unique Angleが存在する
- Core Thesisが存在する
- Monetization Modelが存在する
- CTAが存在する

Experience Reportの場合：

- Author Experienceが確認されている
- Unknownが明示されている
- 著者確認待ちの重大事項が残っていない

重大なContent Integrity問題が残っている場合、Publishingを開始してはならない。

その場合：

Publication Readiness: C

とする。


---

# 5. Publication Readiness

以下の3段階で判定する。

## A — Ready

公開に必要な情報がすべて確定している。

条件：

- Platform confirmed
- Platform仕様 confirmed
- Metadata confirmed
- Category confirmed
- Tags confirmed
- Price confirmed
- Paywall confirmed
- Thumbnail ready
- Privacy passed
- Experience Integrity passed
- Claim Integrity passed

---

## B — Needs Minor Fix

記事内容は公開可能だが、公開作業上の軽微な項目が残っている。

例：

- Thumbnail未作成
- Category未選択
- Tags微調整
- Publication Date未設定
- Platform仕様の最終確認待ち

---

## C — Needs Author Confirmation

記事内容そのものに関する重大な確認が必要。

例：

- 著者経験が不明
- 結果が不明
- 重要な数字が不明
- 著者が本文を確認していない
- Privacy上の重大な懸念
- Article WritingとAuthor Experienceが矛盾している
- Platformの選択によって記事構造そのものが変わる

Cの場合は公開作業を進めない。


---

# 6. Article Metadata

以下を整理する。

title:
subtitle:
article_type:
target_reader:
primary_theme:
unique_angle:
core_thesis:
monetization_model:
cta:
publication_date:
platform:


## Title Check

以下を確認する。

- 本文と一致している
- Article Promiseと一致している
- 誇張していない
- 本文にない結果を示していない
- Clickbaitになっていない
- Author Experienceにない情報を含めていない

問題がなければArticle WritingのTitleをそのまま採用する。


---

# 7. Platform

Platformを最初に確認する。

platformがUnknownの場合、Platform固有設定を確定してはならない。

例：

platform: Unknown

の場合、

category: Unknown
tags: Proposed
thumbnail_spec: Unknown
paywall_spec: Unknown

として扱う。

Platformが確定したら、Platformの現行仕様を確認する。


---

# 8. Platform Specification Research

Platform確定後、必要に応じてWeb検索を行う。

優先順位：

1. Platform公式ヘルプ
2. Platform公式ガイド
3. Platform公式FAQ
4. 信頼できる一次情報
5. その他の補助情報

検索対象：

- 記事投稿仕様
- 有料記事仕様
- 価格仕様
- Category
- Tags
- Thumbnail
- Image
- Formatting
- Disclosure
- Affiliate
- Publication settings

古い仕様を使用しない。

現在仕様が確認できない場合はUnknownとする。


---

# 9. Category

Platform確定後にCategoryを決める。

手順：

1. Platformの現行Categoryを確認
2. Article Primary Themeを確認
3. Target Readerを確認
4. Article Typeを確認
5. 最も適切なCategoryを選択

判断できない場合：

category: Unknown

とする。

候補がある場合：

category: Unknown

category_proposed:
  - Candidate A
  - Candidate B

のように分離する。

---

# 10. Tags

Tagsは以下の優先順位で選択する。

1. Primary Theme
2. Article Topic
3. Target Reader Intent
4. Content Format
5. Secondary Topic

タグを大量に追加してはいけない。

Platformのタグ仕様・上限が確認できていない場合は、Proposedとして扱う。

例：

tags:
  status: Proposed
  values:
    - 恋愛
    - 婚活
    - コミュニケーション
    - 体験談


---

# 11. Monetization

Article Writing / Article Planningで設定されたMonetization Modelをそのまま引き継ぐ。

例：

monetization_model: Free + Paid Article

Publishing側で勝手に、

Free
↓
Paid

へ変更したり、

Paid
↓
Free

へ変更したりしてはならない。


---

# 12. Price

PriceはArticle Planningで設定された仮説を基本的に引き継ぐ。

例：

price:
  test_price: 300
  recommended_price: 500
  confidence: Low

Publishingでは市場調査を勝手にやり直して価格を変更しない。

ただし、Platform仕様上設定できない場合は著者確認を行う。


---

# 13. Free / Paid Boundary

Article Writingで定義されたFree / Paid境界を確認する。

確認項目：

- Free部分だけでも自然に読める
- Paywall直前で不自然に切れていない
- Paid部分にCore Experienceが含まれている
- Paid部分にArticle Promiseに対応する価値がある
- Free部分ですべての価値を消費していない
- Paid部分が単なる引き延ばしになっていない

Publishing側で境界を勝手に変更してはならない。


---

# 14. CTA

CTAを確認する。

条件：

- Article Contentと一致している
- Target Readerと一致している
- 過度な購入誘導をしない
- 本文にない効果を約束しない
- 不安や焦りを過度に煽らない
- 著者経験を一般法則に変換しない

問題がなければArticle WritingのCTAをそのまま使用する。


---

# 15. Thumbnail

Thumbnailは記事内容と整合する必要がある。

禁止：

- 実際には存在しない成功シーン
- 架空のカップルを著者として見せる
- 架空の収益実績
- 架空のBefore / After
- 本文に存在しない出来事
- 著者本人に見える架空人物
- 実際に存在しない結果を示す画像

推奨：

- 抽象的なビジュアル
- 記事テーマを象徴する物
- テキスト主体
- 内省的な構成
- 実際の経験と矛盾しないイメージ

PlatformのThumbnail仕様を確認してから最終画像を作成する。


---

# 16. Thumbnail Generation

Thumbnailが必要な場合、以下の順序で作成する。

1. Article Theme確認
2. Unique Angle確認
3. Title確認
4. 禁止表現確認
5. Platform仕様確認
6. Thumbnail Concept作成
7. 画像生成
8. Articleとの整合性確認

画像生成では、本文に存在しない出来事を「実際の経験」のように描写しない。

必要であれば画像生成ツールを使用する。


---

# 17. Links

以下を確認する。

- Internal Links
- External Links
- Affiliate Links
- Sponsored Links

存在しないURLを生成してはならない。

関連記事が存在しない場合：

internal_links: none

とする。

Affiliateが存在しない場合：

affiliate_links: none

とする。


---

# 18. Disclosure

以下に該当する場合はDisclosureを確認する。

- Affiliate
- Advertisement
- Sponsored
- PR
- Product Provision
- Paid Review

該当しない場合は、

disclosure: not_required

とする。

Publishing側で存在しない広告関係を追加してはならない。


---

# 19. Privacy Check

以下を確認する。

- 実名
- 住所
- 電話番号
- Email
- SNSアカウント
- 職場
- 学校
- 顔写真
- 第三者を特定可能な情報
- 特定可能なマッチングアプリ情報
- 特定可能なYouTubeチャンネル
- その他個人情報

問題がなければ：

Privacy: Passed

重大な問題があれば：

Privacy: Failed

として公開を停止する。


---

# 20. Experience Integrity

Experience Reportの場合、以下を確認する。

- 著者経験を追加していない
- 著者経験を削除していない
- 数字を追加していない
- 結果を追加していない
- 感情を追加していない
- 因果関係を追加していない
- UnknownをFactに変更していない
- Author InterpretationをFactに変更していない
- 個人的経験を一般法則に変換していない
- 第三者情報を追加していない

すべてPassedの場合：

Experience Integrity: Passed


---

# 21. Claim Integrity

主要Claimについて確認する。

| Claim | Source | Evidence Type |
|---|---|---|
| Claim | Author Experience | Author Fact |
| Claim | Author Experience | Author Interpretation |
| Claim | External Source | External Fact |
| Claim | Analysis | Hypothesis |
| Claim | Unknown | Unknown |

重要なのは、Evidence Typeを混同しないこと。

特に、

Author Interpretation
↓
Author Fact

への変換は禁止する。


---

# 22. External Facts

Article Writingに外部情報が含まれている場合、Sourceを確認する。

外部情報をPublishing側で追加してはならない。

外部情報がArticle Writingに存在しない場合、Publishing側で統計や市場データを追加してはいけない。


---

# 23. Formatting

Platform仕様に合わせてFormattingを確認する。

ただし、

内容を変えるFormatting変更は禁止。

許可される例：

- Markdown headingの変換
- Platformに対応しないMarkdown記法の修正
- 改行調整
- Paywall位置の明示
- Image placeholderの追加

意味を変える文章修正は禁止。


---

# 24. Final Publication Package

最終的に以下を整理する。

Publication Package:

- Title
- Subtitle
- Body
- Platform
- Category
- Tags
- Thumbnail
- Price
- Monetization Model
- Free / Paid Boundary
- CTA
- Links
- Disclosure
- Publication Date
- Publication Settings

PlatformがUnknownの場合、Platform-specific項目は確定版として出力しない。


---

# 25. Publication Checklist

## Content

- [ ] Title confirmed
- [ ] Body confirmed
- [ ] Article Writing version confirmed
- [ ] Article Promise confirmed
- [ ] Unique Angle preserved

## Experience

- [ ] Experience Integrity passed
- [ ] Claim Integrity passed
- [ ] Unknown preserved
- [ ] No invented results
- [ ] No invented numbers

## Monetization

- [ ] Monetization Model confirmed
- [ ] Price confirmed
- [ ] Free / Paid boundary confirmed
- [ ] CTA confirmed
- [ ] Disclosure confirmed

## Platform

- [ ] Platform confirmed
- [ ] Current Platform specifications verified
- [ ] Category confirmed
- [ ] Tags confirmed
- [ ] Formatting confirmed
- [ ] Paywall confirmed

## Thumbnail

- [ ] Thumbnail concept confirmed
- [ ] Thumbnail created
- [ ] Thumbnail does not invent facts
- [ ] Thumbnail matches Platform specification

## Privacy

- [ ] Privacy passed
- [ ] Third-party information checked
- [ ] Personal identification risk checked


---

# 26. Publication Readiness Decision

以下で最終判定する。

A:

すべての公開条件が確定している。

B:

記事は公開可能だが、軽微な公開作業が残っている。

C:

記事内容・Experience Integrity・Privacy等について著者確認が必要。


---

# 27. Needs Confirmation

確認が必要な項目だけを列挙する。

例：

1. Platform
2. Category
3. Price
4. Thumbnail
5. Publication Date

確認不要な項目を無駄に質問しない。


---

# 28. Handoff to Performance Analysis

公開後にPerformance Analysisへ以下を引き渡す。

publication_date:
platform:
title:
article_type:
theme:
target_reader:
monetization_model:
price:
tags:
category:
cta:
thumbnail:
publication_url:

公開前の場合は、

publication_url: Unknown

とする。

Performance Analysisでは、以下を分析対象とする。

- PV
- Likes
- Comments
- Paid Page Views
- Purchases
- Conversion Rate
- Revenue
- Revenue per View
- CTR
- Retention
- Publication Timing
- Traffic Sources

ただし、Performance結果によってAuthor Experienceを改変してはならない。


---

# 29. No Premature Performance Analysis

PublishingではPerformance Analysisを行わない。

公開前：

Publication Readiness

公開後：

Performance Analysis

と明確に分離する。


---

# 30. Final Report Structure

Publishing Reportは以下の構造を基本とする。

# Publishing Report

## 1. Input

- Article Writing
- Article Planning
- Author Experience

## 2. Input Validation

## 3. Publication Status

## 4. Article Metadata

## 5. Platform

## 6. Platform Specification

## 7. Category

## 8. Tags

## 9. Monetization

## 10. Free / Paid Structure

## 11. CTA

## 12. Thumbnail

## 13. Links

## 14. Disclosure

## 15. Privacy Check

## 16. Experience Integrity

## 17. Claim Integrity

## 18. Final Checks

## 19. Needs Confirmation

## 20. Publication Package

## 21. Handoff to Performance Analysis

## 22. Quality Gate


---

# 31. Quality Gate

## Content Integrity

- [ ] Article Writingの本文を変更していない
- [ ] Author Experienceを創作していない
- [ ] Unknownを補完していない
- [ ] 因果関係を追加していない
- [ ] 結果を追加していない

## Editorial Integrity

- [ ] Titleと本文が一致している
- [ ] Unique Angleが維持されている
- [ ] Article Promiseが維持されている
- [ ] CTAが記事内容と一致している

## Monetization

- [ ] Free / Paid境界が明確
- [ ] Priceが確認されている
- [ ] Disclosureが必要な場合は設定されている

## Privacy

- [ ] 第三者情報を確認している
- [ ] 個人特定リスクを確認している
- [ ] Sensitive Contentを確認している

## Platform

- [ ] Platformが確認されている
- [ ] Platformの現行仕様を確認している
- [ ] Categoryが確認されている
- [ ] Tagsが確認されている
- [ ] Platform仕様に対応している
- [ ] Thumbnailが確認されている

## Publication

- [ ] Publication Packageが完成している
- [ ] 公開URLを記録できる
- [ ] Performance AnalysisへのHandoff情報が存在する


---

# 32. Output Rules

Publishingの出力は、原則として以下を分離する。

1. Publication Report
2. Publication Package
3. Needs Confirmation

Article Writing本文を再掲する必要がない場合、本文全文を重複出力しない。

Platform固有情報については、確定値と提案値を必ず明示的に区別する。

使用する表記：

Confirmed
Proposed
Unknown
Needs Confirmation

を明確に使い分ける。


---

# 33. Markdown Safety

Publishing ReportはMarkdownとしてそのまま保存できる形式で出力する。

特にコードブロックを使用する場合、内部に同じ3バッククォートを含めてMarkdown構造を破壊してはならない。

YAMLなどのコードブロックを出力する場合は、

外側：
~~~markdown

内側：
```yaml
...