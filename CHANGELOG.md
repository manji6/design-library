# CHANGELOG

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
