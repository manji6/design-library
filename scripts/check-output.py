#!/usr/bin/env python3
"""生成物の適合チェック（試運転の成果物向け）。

使い方: python3 scripts/check-output.py <生成HTML> [デザインdir]

生成 HTML を読み、次を「発明の候補」として列挙する:
- トークン（tokens.css）に無い色（16進値）を、style 属性や <style> で使っている
- デザインの CSS（editorial.css）に無いクラスを使っている
  （ページ固有ブロック <style data-page> で定義したクラスと、JS が付ける
   js / in / active は除く）

見つかれば終了コード 1、無ければ 0。repo 自体の CI ではなく、
試運転で他エージェントが作った成果物を検査するための道具。
"""
import re
import sys
from pathlib import Path

ALLOW_CLASSES = {"js", "in", "active"}


def hexes(text: str) -> set[str]:
    out = set()
    for m in re.finditer(r"#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b", text):
        v = m.group(0).lower()
        if len(v) == 4:  # #abc -> #aabbcc
            v = "#" + "".join(c * 2 for c in v[1:])
        out.add(v)
    return out


def classes_in_css(text: str) -> set[str]:
    return set(re.findall(r"\.([a-zA-Z][\w-]*)", text))


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    target = Path(sys.argv[1])
    design_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("designs/editorial")
    html = target.read_text(encoding="utf-8")

    token_colors = hexes((design_dir / "tokens.css").read_text(encoding="utf-8"))
    css_classes = classes_in_css((design_dir / "editorial.css").read_text(encoding="utf-8"))

    # ページ固有ブロック（<style data-page ...>）は正規の追加先として除外する
    page_styles = re.findall(r"<style[^>]*data-page[^>]*>(.*?)</style>", html, re.S)
    other_styles = [
        s for s in re.findall(r"<style[^>]*>(.*?)</style>", html, re.S)
        if s not in page_styles
    ]
    page_classes = set()
    for s in page_styles:
        page_classes |= classes_in_css(s)

    style_attrs = re.findall(r'style="([^"]*)"', html)
    used_colors = set()
    for s in other_styles + style_attrs:
        used_colors |= hexes(s)
    bad_colors = sorted(used_colors - token_colors)

    used_classes = set()
    for m in re.finditer(r'class="([^"]*)"', html):
        used_classes |= set(m.group(1).split())
    bad_classes = sorted(used_classes - css_classes - page_classes - ALLOW_CLASSES)

    findings = 0
    if bad_colors:
        findings += len(bad_colors)
        print("トークンに無い色（発明の候補）:")
        for c in bad_colors:
            print(f"  {c}")
    if bad_classes:
        findings += len(bad_classes)
        print("デザインの CSS に無いクラス（発明の候補）:")
        for c in bad_classes:
            print(f"  .{c}")
    if findings == 0:
        print("適合: トークン外の色、未定義クラスは見つからなかった")
        return 0
    print(f"候補 {findings} 件。部品の不足か、ページ固有追加の範囲かを確認すること")
    return 1


if __name__ == "__main__":
    sys.exit(main())
