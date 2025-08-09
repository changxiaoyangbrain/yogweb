#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为所有已插入的页脚标注（id="site-footer-note"）添加样式：
- 透明底
- 红色文字
- 居中显示
位置保持不变，仅调整样式；若已有 style，将覆盖为统一样式。
"""
import re
from pathlib import Path

ROOT = Path('/Volumes/acasis/yogweb')
OPEN_TAG_RE = re.compile(r'<div\s+id="site-footer-note"[^>]*>', re.IGNORECASE)
NEW_OPEN_TAG = (
    '<div id="site-footer-note" '
    'style="display:block;text-align:center;color:#d00;background:transparent;padding:8px 0;">'
)


def process_file(p: Path) -> bool:
    try:
        content = p.read_text(encoding='utf-8')
        if 'id="site-footer-note"' not in content:
            return False
        new_content, n = OPEN_TAG_RE.subn(NEW_OPEN_TAG, content)
        if n > 0 and new_content != content:
            p.write_text(new_content, encoding='utf-8')
            return True
        return False
    except Exception as e:
        print(f"❌ 处理失败 {p}: {e}")
        return False


def main():
    html_files = [p for p in ROOT.rglob('*.html') if 'backup_original' not in str(p)]
    changed = 0
    for i, p in enumerate(sorted(html_files), 1):
        if process_file(p):
            changed += 1
            print(f"[{i}/{len(html_files)}] ✅ 更新样式: {p.relative_to(ROOT)}")
    print(f"\n📊 完成：更新 {changed}/{len(html_files)} 个 HTML 文件")

if __name__ == '__main__':
    main()
