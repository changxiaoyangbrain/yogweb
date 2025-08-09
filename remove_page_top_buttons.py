#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量移除全站“返回页首/返回顶部”按钮与容器，并清理残留空白。
目标包含：
- 含有 pagetop/page-top/page_top/pageTop/l-pagetop/m-pagetop 的容器（div/p/li/span/section 等）
- 指向 #wrap/#top/#pagetop 的锚点链接
- 文案为 “返回页首/返回顶部”等的链接
- 包含 alt="返回页首/返回顶部" 的图片及其外层 <a>
- 清除空标签与多余空行
"""
import os
import re
from pathlib import Path

ROOT = Path('/Volumes/acasis/yogweb')

# 需要处理的关键词与类名片段
TEXT_KEYWORDS = [
    '返回页首', '返回顶部', '回到顶部', '頁首', '頁顶', '页首', '页顶'
]
CLASS_TOKENS = [
    'pagetop', 'page-top', 'page_top', 'pageTop', 'l-pagetop', 'm-pagetop'
]
HREF_ANCHORS = [
    '#top', '#wrap', '#pagetop'
]

# 预编译常用模式
CLASS_CONTAINER_RE = re.compile(
    r'<(?:div|p|li|span|section)[^>]*class="[^"]*(?:pagetop|page-top|page_top|pageTop|l-pagetop|m-pagetop)[^"]*"[^>]*>[\s\S]*?</(?:div|p|li|span|section)>',
    re.IGNORECASE
)

# 链接到顶部的 a 标签
A_HREF_TOP_RE = re.compile(
    r'<a[^>]*href="(?:[^"#]*?)?(?:#top|#wrap|#pagetop)"[^>]*>[\s\S]*?</a>',
    re.IGNORECASE
)

# 文字为“返回页首/返回顶部”的 a 标签（忽略空白）
A_TEXT_KEYWORD_RE = re.compile(
    r'<a([^>]*)>(?:(?:\s|&nbsp;|<[^>]+>)*)(?:返回页首|返回顶部|回到顶部|頁首|頁顶|页首|页顶)(?:(?:\s|&nbsp;|<[^>]+>)*)</a>',
    re.IGNORECASE
)

# 包含 alt 为“返回页首/返回顶部”的图片及其外层 a
A_IMG_ALT_RE = re.compile(
    r'<a[^>]*>\s*<img[^>]*alt="(?:返回页首|返回顶部|回到顶部|頁首|頁顶|页首|页顶)"[^>]*>\s*</a>',
    re.IGNORECASE
)

# 单独的 img（无 a 包裹）
IMG_ALT_RE = re.compile(
    r'<img[^>]*alt="(?:返回页首|返回顶部|回到顶部|頁首|頁顶|页首|页顶)"[^>]*>',
    re.IGNORECASE
)

# 可能用到的 id 钩子
ID_PAGETOP_RE = re.compile(r'<a[^>]*id="(?:pagetop|page-top)"[^>]*>[\s\S]*?</a>', re.IGNORECASE)

# 清理空标签与多余空行
EMPTY_TAGS_RE = re.compile(r'<(div|p|li|span|section)([^>]*)>\s*</\1>', re.IGNORECASE)
TRIPLE_BLANKS_RE = re.compile(r'\n\s*\n\s*\n+', re.MULTILINE)


def process_html_file(path: Path) -> bool:
    try:
        content = path.read_text(encoding='utf-8')
        original = content

        # 1) 移除常见容器（类名包含 pagetop 等）
        content = CLASS_CONTAINER_RE.sub('', content)

        # 2) 移除锚点链接到顶部的 a
        content = A_HREF_TOP_RE.sub('', content)

        # 3) 移除文字为返回顶部类关键词的 a
        content = A_TEXT_KEYWORD_RE.sub('', content)

        # 4) 移除包含相应 alt 的图片及其 a 包裹
        content = A_IMG_ALT_RE.sub('', content)
        content = IMG_ALT_RE.sub('', content)

        # 5) 移除 id 钩子的 a
        content = ID_PAGETOP_RE.sub('', content)

        # 6) 清理空标签与多余空行
        prev = None
        # 多次运行直到收敛，避免嵌套空标签遗留
        for _ in range(5):
            prev = content
            content = EMPTY_TAGS_RE.sub('', content)
            content = TRIPLE_BLANKS_RE.sub('\n\n', content)
            if content == prev:
                break

        if content != original:
            path.write_text(content, encoding='utf-8')
            return True
        return False
    except Exception as e:
        print(f"❌ 处理失败 {path}: {e}")
        return False


def main():
    html_files = [p for p in ROOT.rglob('*.html') if 'backup_original' not in str(p)]
    changed = 0
    for i, p in enumerate(sorted(html_files), 1):
        if process_html_file(p):
            changed += 1
            print(f"[{i}/{len(html_files)}] ✅ 移除: {p.relative_to(ROOT)}")
        else:
            # 可打印进度但不冗长
            pass
    print(f"\n📊 完成：修改 {changed}/{len(html_files)} 个 HTML 文件")

if __name__ == '__main__':
    main()
