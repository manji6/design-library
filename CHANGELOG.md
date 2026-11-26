# CHANGELOG

## [0.4.1] - 2026-11-26

v0.4.0 の再試運転（Antigravity CLI、EmDash 題材）で得たフィードバックへの対応。再試運転自体は合格だった（2項比較を選定、4点セット報告、check-output 適合）。

- 原則「定義の範囲と自律判断」を INDEX に新設し、スニペットと AGENTS.md に反映: ライブラリが定義するのは共通事項までで、定義されていない部分はデザインの意図を汲んで自律的に判断してよい（「遊び」の幅）。「定義されていない」は表現を諦める理由にならない。定義済みのものの上書き禁止、自律判断の報告、使い回せる構造は不足として報告、という境界も明記
- editorial.css の不整合を修正: .callout が .dg の外で使えなかった問題（単独でも当たるよう基本形を分離。2項比較の差分が対象）、DESIGN.md にある line-break: strict が body に無かった問題、.cols の子要素に min-width: 0 が無かった問題
- 未定義部品（引用、アコーディオン、コード／コピーボタン）は backlog Issue に登録し、需要が出た時点で部品化する

## [0.4.0] - 2026-11-26

Issue #12 の候補 (b) と、外部評価で挙がった「発明の検出を機械化する」への対応。

- 図解パターン「2項比較」（compare/two-way-contrast）を新設し example 化した。12見出しの定義、EmDash 題材の実例分解つき。diagrams/index.md の比較・対照に問い行を追加し、必須役割（対象、観点、差分）を明記
- editorial の DESIGN.md 図解部品表に 2項比較の割り当てを追加（観点を行、対象を列にした .data-table、差分は直下に .callout で1文）。sample.html に実例を追加
- 適合チェック scripts/check-output.py を追加: 生成 HTML から、トークン外の色とデザイン CSS に無いクラスを「発明の候補」として列挙する。旧試運転の成果物では発明クラス17件を検出、正本の sample では0件を確認

## [0.3.2] - 2026-11-26

外部評価（3モデルによるレビュー）で一致した指摘への対応。文面のみの変更。

- name-only の扱いを明記: 選んでよいのはデザイン ready、図解 defined / example のみ。name-only は台帳（需要の記録）であり、近いもので代用せず不足として報告する（INDEX、diagrams/index.md の選択の原則、diagrams/README.md 手順5の出口、snippets/reference.md）
- 適用報告を4点セットに拡張: デザイン slug＋図解 slug＋レイアウト型＋版（v0.3.0 で入れたレイアウト型を報告でも検出できるように）
- status の対照を INDEX に追加（デザインと図解で語彙が違うため）
- ページ固有追加と不足部品の判定基準を AGENTS.md に明記（使い回せる意味的構造はページ固有にせず不足として報告）
- Issue #12 の候補 (a) を本版で適用。(b)（比較系の example 化）は次版で扱う

## [0.3.1] - 2026-11-25

- Pages トップ（index.html）に固定表示していた版番号が v0.1.0 のまま残っていた問題を修正。版番号の固定表示をやめ、Releases と INDEX への参照に変えた（今後ずれない形にした）

## [0.3.0] - 2026-11-25

v0.2.0 での再試運転で見つかった「ページ幅の考え方の欠落」への対応。

- DESIGN.md の Layout に「ページ幅の型」を追加: ワイド型（max-width 1180px、目次サイドバー 210px＋本文のグリッド、長文・調査資料向け）とシングル型（max-width 880px 単一カラム、短文・単票向け）の2型を併記。選び方、帯の幅、図・表が使える幅も明記
- editorial.css にワイド型の部品（page-wide、cols、toc-side、860px 以下での単一カラム化、印刷時の扱い）を追加
- sample.html をワイド型で組み直して実例にした
- Issue #15 として登録し、本版で対応

## [0.2.0] - 2026-11-25

試運転（Antigravity CLI、EmDash 資料ページ）で見つかった仕組みの穴を受けたブラッシュアップ。

- editorial.css に図解部品の完成形を追加: 状態タイトル（本文サイズ・太字）、補足の寸法、並置比較（dg-compare／dg-row／dg-cond）、段の下の注釈（annotation）、キーカラー太枠（keyed）／ink 太枠（heavy）、図の見出し（dg-title）
- editorial.css にデータ表（data-table）を正式部品として追加
- sample.html に並置比較とデータ表の実例を追加
- DESIGN.md の図解部品表に「寸法の目安」の列と注目（太枠）の行、データ表の寸法を追加
- 様式ファイルの扱いを明記（AGENTS.md、snippets/reference.md）: デザインの CSS は改変しない、追加は別ブロック、部品が無い場合は発明せず不足として報告する
- 改善バックログを Issue 化（#10 本対応、#11 本対応、#12 図解選択の偏りは検討として分離）

## [0.1.1] - 2026-11-25

- quality.md を追加: 全デザイン共通の生成ルールと検査（第1層 Floor／Reflex／Finish、第2層 検査）。動きは既定でAIの裁量とし、厳密な定義はデザイン側の層2にだけ書く方針を明記
- INDEX の最小読み込みセットに quality.md を追加し、版を v0.1.1 に更新
- snippets/reference.md に quality.md への準拠を追加
- AGENTS.md に品質の節を追加

## [0.1.0] - 2026-11-24

初回リリース。

- 骨格: README、INDEX（版の記載、名前解決表、最小読み込みセット）、AGENTS.md、snippets/reference.md、scripts（gen-tokens / check）
- デザイン: エディトリアル（editorial）を移行。DESIGN.md（トークン正本＋宣言表）、生成 tokens.css、editorial.css、sample.html、notes.md、non-html.md
- 図解: diagrams/README（考え方と手順）、vocabulary、index（問いの索引）、_template（12見出し）、第1号パターン「状態遷移」（実例の分解を内包）
- GitHub Pages のトップ index.html
