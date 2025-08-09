#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复剩余的外部链接
"""

import os
import re
from pathlib import Path

def fix_remaining_links(file_path):
    """修复单个HTML文件中的剩余外部链接"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 1. 处理语言切换链接 - 改为相对路径或禁用
        content = re.sub(r'<a href="https://www\.meiji\.co\.jp/yogurtlibrary/">日本語</a>', 
                        '<a href="#" onclick="return false;">日本語</a>', content)
        content = re.sub(r'<a href="https://www\.meiji\.co\.jp/yogurtlibrary/en/">ENG</a>', 
                        '<a href="#" onclick="return false;">ENG</a>', content)
        
        # 2. 处理外部食谱链接
        content = re.sub(r'href="https://www\.meiji\.co\.jp/meiji-shokuiku/[^"]*"', 
                        'href="#" onclick="alert(\'外部链接已移除\'); return false;"', content)
        
        # 3. 处理spacer.gif引用 - 使用本地透明图片或CSS
        content = re.sub(r'src="https://www\.meiji\.co\.jp/yogurtlibrary/images/spacer\.gif"', 
                        'src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"', content)
        
        # 4. 修复错误的面包屑导航链接
        content = re.sub(r'href="https://www\.meiji\.co\.jp/yogurtlibrary/zh/laboratory/report"', 
                        'href="../../index.html"', content)
        
        # 5. 移除剩余的bc/import.js引用
        content = re.sub(r'<script[^>]*src="https://www\.meiji\.co\.jp/common/js/bc/import\.js"[^>]*></script>\n?', '', content)
        
        # 6. 修复双重转义的onmouseover（清理脚本产生的错误）
        content = re.sub(r'onmouseover="MM_swapImage\(onmouseover="MM_swapImage\([^)]*\)[^)]*\)', 
                        'onmouseover="MM_swapImage', content)
        # 修复路径中的多余引号
        content = re.sub(r"MM_swapImage\('([^']+)','',''','([^']+)'", 
                        r"MM_swapImage('\1','','\2'", content)
        
        # 只有在内容发生变化时才写入文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def find_html_files(root_dir):
    """查找所有HTML文件"""
    html_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    return html_files

def main():
    """主函数"""
    root_dir = '/Volumes/acasis/yogweb'
    
    print("🔧 修复剩余的外部链接...")
    print(f"📁 工作目录: {root_dir}")
    
    # 查找所有HTML文件
    html_files = find_html_files(root_dir)
    print(f"📊 找到 {len(html_files)} 个HTML文件")
    
    # 处理每个文件
    fixed_count = 0
    for i, file_path in enumerate(html_files, 1):
        rel_path = os.path.relpath(file_path, root_dir)
        
        if fix_remaining_links(file_path):
            print(f"[{i}/{len(html_files)}] 修复: {rel_path}")
            fixed_count += 1
    
    print(f"\n✨ 修复完成！")
    print(f"📈 共修复 {fixed_count} 个文件")
    print("\n🎯 修复内容包括:")
    print("  • 语言切换链接改为禁用状态")
    print("  • 外部食谱链接改为提示")
    print("  • spacer.gif改为base64透明图片")
    print("  • 修复面包屑导航链接")
    print("  • 清理onmouseover语法错误")

if __name__ == "__main__":
    main()