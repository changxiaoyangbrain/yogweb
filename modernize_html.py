#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HTML现代化脚本 - 移除已弃用属性，提升代码质量
"""

import os
import re
from pathlib import Path

def modernize_html_file(file_path):
    """现代化单个HTML文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes = []
        
        # 1. 处理body标签的已弃用属性
        content = re.sub(r'<body([^>]*)\s+bgcolor="[^"]*"([^>]*)>', 
                        lambda m: f'<body{m.group(1).strip()}{(" " + m.group(2)) if m.group(2).strip() else ""}>', 
                        content)
        if content != original_content:
            changes.append("移除body bgcolor属性")
            
        content = re.sub(r'<body([^>]*)\s+marginheight="[^"]*"([^>]*)>', 
                        lambda m: f'<body{m.group(1).strip()}{(" " + m.group(2)) if m.group(2).strip() else ""}>', 
                        content)
        content = re.sub(r'<body([^>]*)\s+marginwidth="[^"]*"([^>]*)>', 
                        lambda m: f'<body{m.group(1).strip()}{(" " + m.group(2)) if m.group(2).strip() else ""}>', 
                        content)
        
        # 2. 处理表格的已弃用属性 - 保持结构但移除样式属性
        # 移除table的bgcolor, cellpadding, cellspacing但保留width和border用于布局
        content = re.sub(r'<table([^>]*)\s+bgcolor="[^"]*"([^>]*)>', 
                        lambda m: f'<table{m.group(1).strip()}{(" " + m.group(2)) if m.group(2).strip() else ""}>', 
                        content)
        content = re.sub(r'<table([^>]*)\s+cellpadding="[^"]*"([^>]*)>', 
                        lambda m: f'<table{m.group(1).strip()}{(" " + m.group(2)) if m.group(2).strip() else ""}>', 
                        content)
        content = re.sub(r'<table([^>]*)\s+cellspacing="[^"]*"([^>]*)>', 
                        lambda m: f'<table{m.group(1).strip()}{(" " + m.group(2)) if m.group(2).strip() else ""}>', 
                        content)
        
        # 3. 处理td的已弃用属性 - 保留width用于布局
        content = re.sub(r'<td([^>]*)\s+bgcolor="[^"]*"([^>]*)>', 
                        lambda m: f'<td{m.group(1).strip()}{(" " + m.group(2)) if m.group(2).strip() else ""}>', 
                        content)
        content = re.sub(r'<td([^>]*)\s+valign="[^"]*"([^>]*)>', 
                        lambda m: f'<td{m.group(1).strip()}{(" " + m.group(2)) if m.group(2).strip() else ""}>', 
                        content)
        content = re.sub(r'<td([^>]*)\s+height="[^"]*"([^>]*)>', 
                        lambda m: f'<td{m.group(1).strip()}{(" " + m.group(2)) if m.group(2).strip() else ""}>', 
                        content)
        content = re.sub(r'<td([^>]*)\s+align="[^"]*"([^>]*)>', 
                        lambda m: f'<td{m.group(1).strip()}{(" " + m.group(2)) if m.group(2).strip() else ""}>', 
                        content)
        
        # 4. 处理tr的已弃用属性
        content = re.sub(r'<tr([^>]*)\s+valign="[^"]*"([^>]*)>', 
                        lambda m: f'<tr{m.group(1).strip()}{(" " + m.group(2)) if m.group(2).strip() else ""}>', 
                        content)
        content = re.sub(r'<tr([^>]*)\s+bgcolor="[^"]*"([^>]*)>', 
                        lambda m: f'<tr{m.group(1).strip()}{(" " + m.group(2)) if m.group(2).strip() else ""}>', 
                        content)
        
        # 5. 替换center标签为div with CSS class
        content = re.sub(r'<center>', '<div class="text-center">', content)
        content = re.sub(r'</center>', '</div>', content)
        if '<div class="text-center">' in content:
            changes.append("替换center标签为div")
        
        # 6. 处理img的已弃用属性 - 保留必要的border="0"
        content = re.sub(r'<img([^>]*)\s+name="([^"]*)"([^>]*)>', 
                        lambda m: f'<img{m.group(1).strip()}{(" " + m.group(3)) if m.group(3).strip() else ""} id="{m.group(2)}">', 
                        content)
        
        # 7. 添加基础CSS类到head中（如果不存在）
        if '<div class="text-center">' in content and 'text-center' not in content:
            # 查找是否已有style标签
            if '<style>' in content:
                content = re.sub(r'(<style[^>]*>)', 
                               r'\1\n.text-center { text-align: center; }', content)
            elif '</head>' in content:
                # 添加基础CSS
                css_insert = '''<style>
.text-center { text-align: center; }
table { border-collapse: collapse; }
td { padding: 4px; vertical-align: top; }
</style>'''
                content = content.replace('</head>', css_insert + '\n</head>')
                changes.append("添加基础CSS样式")
        
        # 8. 清理多余的空格和空属性
        content = re.sub(r'\s+>', '>', content)  # 移除标签结尾的多余空格
        content = re.sub(r'<(\w+)\s+>', r'<\1>', content)  # 移除标签中的孤立空格
        
        # 只有在内容发生变化时才写入文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return changes
        return []
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return []

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
    
    print("🔧 HTML现代化处理开始...")
    print(f"📁 工作目录: {root_dir}")
    
    # 查找所有HTML文件
    html_files = find_html_files(root_dir)
    print(f"📊 找到 {len(html_files)} 个HTML文件")
    
    # 处理每个文件
    modernized_count = 0
    total_changes = []
    
    for i, file_path in enumerate(html_files, 1):
        rel_path = os.path.relpath(file_path, root_dir)
        
        changes = modernize_html_file(file_path)
        if changes:
            print(f"[{i}/{len(html_files)}] 现代化: {rel_path}")
            for change in changes:
                print(f"  • {change}")
            modernized_count += 1
            total_changes.extend(changes)
    
    print(f"\n✨ HTML现代化完成！")
    print(f"📈 共处理 {modernized_count} 个文件")
    
    if total_changes:
        print("\n🎯 执行的现代化操作:")
        change_counts = {}
        for change in total_changes:
            change_counts[change] = change_counts.get(change, 0) + 1
        
        for change, count in change_counts.items():
            print(f"  • {change}: {count} 次")
    
    print("\n✅ 代码现代化完成，质量得到提升！")

if __name__ == "__main__":
    main()