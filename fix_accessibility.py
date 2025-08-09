#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复可访问性问题
"""

import os
import re
from pathlib import Path

def fix_accessibility_issues(file_path):
    """修复单个HTML文件的可访问性问题"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes = []
        
        # 1. 为鼠标事件添加键盘等效事件
        # 查找带有onmouseover的链接
        onmouseover_pattern = r'<a([^>]*)\s+onmouseover="([^"]*)"([^>]*?)>'
        def add_focus_event(match):
            attrs_before = match.group(1)
            onmouseover_value = match.group(2)
            attrs_after = match.group(3)
            
            # 添加onfocus事件
            onfocus = onmouseover_value
            return f'<a{attrs_before} onmouseover="{onmouseover_value}" onfocus="{onfocus}"{attrs_after}>'
        
        new_content = re.sub(onmouseover_pattern, add_focus_event, content)
        if new_content != content:
            content = new_content
            changes.append("添加键盘焦点事件")
        
        # 2. 为布局表格添加role="presentation"
        # 查找明显用于布局的表格（包含id="wrap"等）
        layout_table_pattern = r'<table([^>]*?)(?:id="wrap"|width="950"|width="721")([^>]*?)>'
        content = re.sub(layout_table_pattern, r'<table\1role="presentation"\2>', content)
        
        # 3. 为数据表格添加基本的可访问性结构
        # 这里我们保守处理，只在明确是数据表格时才添加th
        # 由于这是一个内容网站，大部分表格都是布局用的，所以添加role="presentation"
        content = re.sub(r'<table(?![^>]*role=)', '<table role="presentation"', content)
        if 'role="presentation"' in content:
            changes.append("为布局表格添加presentation角色")
        
        # 4. 确保图片有合适的alt属性（已经有了，不需要修改）
        
        # 5. 为表单元素添加必要的标签（如果有的话）
        
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
    
    print("♿ 修复可访问性问题...")
    print(f"📁 工作目录: {root_dir}")
    
    # 查找所有HTML文件
    html_files = find_html_files(root_dir)
    print(f"📊 找到 {len(html_files)} 个HTML文件")
    
    # 处理每个文件
    fixed_count = 0
    total_changes = []
    
    for i, file_path in enumerate(html_files, 1):
        rel_path = os.path.relpath(file_path, root_dir)
        
        changes = fix_accessibility_issues(file_path)
        if changes:
            print(f"[{i}/{len(html_files)}] 修复可访问性: {rel_path}")
            for change in changes:
                print(f"  • {change}")
            fixed_count += 1
            total_changes.extend(changes)
    
    print(f"\n✨ 可访问性修复完成！")
    print(f"📈 共修复 {fixed_count} 个文件")
    
    if total_changes:
        print("\n♿ 可访问性改进:")
        change_counts = {}
        for change in total_changes:
            change_counts[change] = change_counts.get(change, 0) + 1
        
        for change, count in change_counts.items():
            print(f"  • {change}: {count} 次")

if __name__ == "__main__":
    main()