#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
在所有页面底部加入：顺口餐饮-酸奶资料库
- 位置：在 </body> 之前；若无 </body> 则在 </html> 之前；若都没有则追加到文件末尾
- 防重复：若已存在标记 id="site-footer-note" 则跳过
- 排除：backup_original 目录
"""
import os
import re
from pathlib import Path

ROOT = Path('/Volumes/acasis/yogweb')
NOTE_HTML = '\n<!-- site-footer-note -->\n<div id="site-footer-note">顺口餐饮-酸奶资料库</div>\n'

BODY_CLOSE_RE = re.compile(r"</body>\s*</html>\s*$", re.IGNORECASE)
HAS_NOTE_RE = re.compile(r'id\s*=\s*"site-footer-note"', re.IGNORECASE)


def add_note(path: Path) -> bool:
    try:
        content = path.read_text(encoding='utf-8')
        if HAS_NOTE_RE.search(content):
            return False

        # 优先插入到 </body> 前
        if '</body>' in content.lower():
            # 找到最后一个 </body>（忽略大小写）
            idx = content.lower().rfind('</body>')
            new_content = content[:idx] + NOTE_HTML + content[idx:]
        elif '</html>' in content.lower():
            idx = content.lower().rfind('</html>')
            new_content = content[:idx] + NOTE_HTML + content[idx:]
        else:
            new_content = content.rstrip() + NOTE_HTML

        path.write_text(new_content, encoding='utf-8')
        return True
    except Exception as e:
        print(f"❌ 处理失败 {path}: {e}")
        return False


def main():
    html_files = [p for p in ROOT.rglob('*.html') if 'backup_original' not in str(p)]
    changed = 0
    for i, p in enumerate(sorted(html_files), 1):
        if add_note(p):
            changed += 1
            print(f"[{i}/{len(html_files)}] ✅ 注入: {p.relative_to(ROOT)}")
    print(f"\n📊 完成：注入 {changed}/{len(html_files)} 个 HTML 文件")

if __name__ == '__main__':
    main()
