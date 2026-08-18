# note monetization pipeline

週1本のnote記事を、調査から公開後の振り返りまで一つの案件として管理するSkill集です。目標は月5万円を**予測ではなく検証する**ことです。

## 使い方

```bash
python3 skills/note-weekly-pipeline/scripts/new_issue.py \
  --slug ai-housework-checklist --title '共働き家庭のAI家事チェックリスト'
```

生成された `output/YYYY-MM-DD-<slug>/` を、次の順に埋めます。

1. `01-research/` — 市場・機会・テーマ
2. `02-plan/` — 読者、約束、価格・配布の仮説、KPI
3. `03-source/` — 著者経験と根拠の台帳
4. `04-draft/` — 原稿とClaim Ledger
5. `05-package/` — note公開用メタデータ
6. `06-performance/` — 観測データと次回の仮説

完了前に実行します。

```bash
python3 skills/note-weekly-pipeline/scripts/validate_issue.py output/YYYY-MM-DD-<slug>
```

既存の `research/` は削除せず履歴・入力として使います。新規の運用は `skills/note-weekly-pipeline/SKILL.md` と `output/` を正本にします。

記事の読み応えは、事実を盛るのではなく、チェックリスト、判断基準、比較、明記した架空例、テンプレート、限界と例外で作ります。著者の体験・実績・数字・引用を架空の事実として書かないでください。
