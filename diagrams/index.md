# index — 図解の選択索引

パターンの一覧ではなく、「読者の問い」から引く表。1行＝1つの問い。同じパターンが複数行に出てよい。
図解の status はこのファイルにだけ持つ: defined＝記述あり／example＝実例まで／name-only＝名前と問いだけ（記述はない）。

**選択の原則: 選んでよいのは defined / example のみ。** name-only の行は需要の記録（台帳）であり、適用できる候補ではない。問いに当たる行が name-only だけのときは、近い defined / example で代用せず、README の手順5（出口）を使い、不足として報告すること。

## 系統への振り分け質問

1. 時間や手順に沿って何かが変わるか → 変化・流れ（flow）
2. 要素どうしの所属、包含、つながりが主題か → 構造・関係（structure）
3. 同じ観点で2つ以上を並べて違いを言いたいか → 比較・対照（compare）
4. 数の大小、割合、推移が主題か → 量・規模（quantity）
5. どこにあるか、どこからどこまでか、境目を何が越えるかが主題か → 位置・境界（position）

## 変化・流れ（flow）

| 伝えたいこと（問い） | 素材の手がかり | 必須の役割 | パターン | 似ているが違うもの | status |
|---|---|---|---|---|---|
| 誰か（何か）がどう変わっていくか | 「〜になる」「〜を経て」「ジャーニー」「段階的に」 | 主体、状態、遷移 | [state-transition](patterns/flow/state-transition.md) | process-steps（主体がない）、funnel（量が主役） | example |
| 条件が違うと、同じ主体の変化はどう違うか | 時代、チャネル、セグメントの対比 | 主体、状態、遷移 | [state-transition / 並置比較](patterns/flow/state-transition.md) | before-after（差だけを言う） | example |
| 何をどの順でやるか | 「まず」「次に」「手順」「プロセス」 |  | process-steps | state-transition | name-only |
| いつ何が起きたか | 日付、時刻、期間 |  | timeline | state-transition（順序だけ） | name-only |
| 回るほど強くなる仕組みは何か | 「好循環」「ループ」「フライホイール」 |  | cycle | state-transition / 循環 | name-only |
| どこで道が分かれるか | 条件分岐、判断、離脱と継続 |  | branching | state-transition / 分岐 | name-only |

## 構造・関係（structure）

| 伝えたいこと（問い） | 素材の手がかり | 必須の役割 | パターン | 似ているが違うもの | status |
|---|---|---|---|---|---|
| 全体はどういう部分からできているか | 階層、分類、配下 |  | tree | containment | name-only |
| 何が何の中に入っているか | 包含、内包、スコープの内外 |  | containment | tree | name-only |
| 層はどう積み重なっているか | 基盤、土台、上位・下位 |  | layers | tree | name-only |
| 要素どうしがどうつながっているか | 連携、依存、相互 |  | network | hub-spoke | name-only |
| 中心にあるものは何とつながっているか | 中核、ハブ、窓口 |  | hub-spoke | network | name-only |

## 比較・対照（compare）

| 伝えたいこと（問い） | 素材の手がかり | 必須の役割 | パターン | 似ているが違うもの | status |
|---|---|---|---|---|---|
| 前と後で何が変わったか | 導入前後、ビフォーアフター |  | before-after | state-transition / 並置比較 | name-only |
| 2つの対象を同じ観点で並べるとどう違うか | 「比べて」「違いは」「使い分け」、方式・製品・体制の対比 | 対象、観点、差分 | [two-way-contrast](patterns/compare/two-way-contrast.md) | contrast-table（3つ以上、表が主役）、state-transition / 並置比較（流れを見せる） | example |
| 選択肢を同じ観点で並べるとどう違うか | 比較表、プラン、候補 |  | contrast-table | matrix-2axis | name-only |
| 2つの軸で位置づけるとどこに来るか | 軸、象限、マッピング |  | matrix-2axis | positioning | name-only |
| 両極の間のどこに位置するか | 連続、グラデーション、程度 |  | spectrum | matrix-2axis | name-only |
| 何を得て何を失うか | トレードオフ、両立しない |  | tradeoff | contrast-table | name-only |

## 量・規模（quantity）

| 伝えたいこと（問い） | 素材の手がかり | 必須の役割 | パターン | 似ているが違うもの | status |
|---|---|---|---|---|---|
| どちらがどれだけ大きいか | 数値の比較、倍率 |  | quantity-compare | contrast-table | name-only |
| 全体はどういう割合でできているか | 構成比、内訳、シェア |  | composition | stacked | name-only |
| 数はどう移り変わってきたか | 推移、増減、時系列の数値 |  | trend | timeline | name-only |
| どこでどれだけ減るか | 離脱、歩留まり、「〜%が」 |  | funnel | state-transition | name-only |
| 積み上げるとどうなるか | 積算、累計、内訳の合計 |  | stacked | composition | name-only |

## 位置・境界（position）

| 伝えたいこと（問い） | 素材の手がかり | 必須の役割 | パターン | 似ているが違うもの | status |
|---|---|---|---|---|---|
| 内と外の境目を何が越えるか | 社内／社外、「〜を越えて」、境界 |  | boundary-crossing | state-transition | name-only |
| 競合の中でどこに立つか | ポジショニング、差別化 |  | positioning | matrix-2axis | name-only |
| 対象の範囲はどこからどこまでか | 対象範囲、スコープ、期間 |  | scope | containment | name-only |
| 中心と周辺はどう分かれるか | コア、周辺、主力と派生 |  | center-periphery | hub-spoke | name-only |
| あるべき姿と現状の差はどこか | ギャップ、乖離、不足 |  | gap | before-after | name-only |
