#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复HTML结构问题
"""

import os
import re
from pathlib import Path

def fix_html_structure(file_path):
    """修复单个HTML文件的结构问题"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 1. 修复body标签 - 确保属性之间有空格
        content = re.sub(r'<body([^>]*?)([a-zA-Z]+)="([^"]*)"([^>]*?)>', 
                        lambda m: f'<body{" " if m.group(1) and not m.group(1).endswith(" ") else ""}{m.group(1)}{m.group(2)}="{m.group(3)}"{" " if m.group(4) and not m.group(4).startswith(" ") else ""}{m.group(4)}>', 
                        content)
        
        # 2. 修复table标签的属性间距
        content = re.sub(r'<table([^>]*?)([a-zA-Z]+)="([^"]*)"([^>]*?)>', 
                        lambda m: f'<table{" " if m.group(1) and not m.group(1).endswith(" ") else ""}{m.group(1)}{m.group(2)}="{m.group(3)}"{" " if m.group(4) and not m.group(4).startswith(" ") else ""}{m.group(4)}>', 
                        content)
        
        # 3. 修复td标签的属性间距
        content = re.sub(r'<td([^>]*?)([a-zA-Z]+)="([^"]*)"([^>]*?)>', 
                        lambda m: f'<td{" " if m.group(1) and not m.group(1).endswith(" ") else ""}{m.group(1)}{m.group(2)}="{m.group(3)}"{" " if m.group(4) and not m.group(4).startswith(" ") else ""}{m.group(4)}>', 
                        content)
        
        # 4. 修复img标签的属性间距
        content = re.sub(r'<img([^>]*?)([a-zA-Z]+)="([^"]*)"([^>]*?)>', 
                        lambda m: f'<img{" " if m.group(1) and not m.group(1).endswith(" ") else ""}{m.group(1)}{m.group(2)}="{m.group(3)}"{" " if m.group(4) and not m.group(4).startswith(" ") else ""}{m.group(4)}>', 
                        content)
        
        # 5. 确保所有标签的基本结构正确
        # 修复缺少空格的标签
        content = re.sub(r'<(body|table|td|img|tr)([a-zA-Z])', r'<\1 \2', content)
        
        # 6. 清理多余的空格
        content = re.sub(r'\s{2,}>', '>', content)
        content = re.sub(r'<([a-zA-Z]+)\s+>', r'<\1>', content)
        
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
    
    print("🔧 修复HTML结构问题...")
    print(f"📁 工作目录: {root_dir}")
    
    # 查找所有HTML文件
    html_files = find_html_files(root_dir)
    print(f"📊 找到 {len(html_files)} 个HTML文件")
    
    # 处理每个文件
    fixed_count = 0
    
    for i, file_path in enumerate(html_files, 1):
        rel_path = os.path.relpath(file_path, root_dir)
        
        if fix_html_structure(file_path):
            print(f"[{i}/{len(html_files)}] 修复: {rel_path}")
            fixed_count += 1
    
    print(f"\n✨ HTML结构修复完成！")
    print(f"📈 共修复 {fixed_count} 个文件")

if __name__ == "__main__":
    main()