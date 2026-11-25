版: v0.2.0

# INDEX — エージェント入口

この repo はデザイン定義の正本である。適用の前にこの INDEX を読み、対象のデザインと図解を選ぶこと。

## 適用条件

- ユーザーがデザイン名を指定したとき、または対象に既存デザインが無いときだけ使う。
- 「おまかせ」の既定は、資料なら **エディトリアル（editorial）**。
- 適用報告は「デザイン slug＋図解 slug＋版」の3点セットで返す（版はこのファイル冒頭の「版:」を写す）。

## 名前解決表（デザイン）

| 表示名 | slug | status | 置き場 |
|---|---|---|---|
| エディトリアル | editorial | ready | designs/editorial/ |
| ダークシネマ | dark-cinema | name-only | （台帳のみ） |
| スイスミニマル | swiss-minimal | name-only | （台帳のみ） |
| MAGIコア | command-core | name-only | （台帳のみ） |
| 朝刊 | morning-edition | name-only | （台帳のみ。実体は newspaper.amanohashi.date） |

status の意味（デザイン）:
- ready: 層0があり、宣言表に「未定」がなく、検査を通過。適用してよい。
- draft: 層0はあるが宣言表に「未定」を含む。ユーザーが名指ししたときだけ適用し、「未定」の要素に触れたら止まって報告する。
- name-only: 台帳のみ。適用せず、その旨を報告する。

旧名の対応: エディトリアル＝旧「案A」、ダークシネマ＝旧「案B」、スイスミニマル＝旧「案C」。

## 図解

図解パターンの選択は diagrams/index.md（読者の問いから引く索引）で行う。図解の status（defined / example / name-only）は diagrams/index.md にだけ持つ。
利用手順は diagrams/README.md にある。

## 最小読み込みセット

| 作業 | 読むもの |
|---|---|
| Web 資料 | 対象デザインの DESIGN.md、tokens.css、sample.html、quality.md |
| スライド・単票 | 対象デザインの DESIGN.md、non-html.md、quality.md |
| 図解 | diagrams/README.md、diagrams/index.md、対象パターンのファイル1本。語彙で迷った時だけ diagrams/vocabulary.md。描画の段でのみ対象デザインの DESIGN.md（図解部品表） |

quality.md は全デザイン共通の生成ルールと検査（AIっぽさを出さないため）。Floor は必須、Reflex を外した場合は報告に理由を書く。

## 読み順

1. この INDEX（stable ブランチ）
2. 対象デザインの DESIGN.md → tokens.css → sample.html
3. 図解が要る場合は diagrams/README.md → diagrams/index.md → パターン
