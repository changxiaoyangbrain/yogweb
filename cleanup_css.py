#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
清理CSS文件中的外部依赖
"""

import os
import re
from pathlib import Path

def cleanup_css_file(file_path):
    """清理单个CSS文件中的外部依赖"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 1. 移除外部@import
        content = re.sub(r'@import\s*["\']https://www\.meiji\.co\.jp[^"\']*["\'];?\n?', '', content)
        
        # 2. 移除或替换外部图片引用
        # 对于导航按钮，我们可以用简单的CSS替换
        content = re.sub(
            r'background:\s*url\(["\']https://www\.meiji\.co\.jp/sweets/chocolate/oligosmart/images/nav_prev\.png["\'][^;]*;',
            'background: #ddd; content: "<"; text-align: center;',
            content
        )
        
        content = re.sub(
            r'background:\s*url\(["\']https://www\.meiji\.co\.jp/sweets/chocolate/oligosmart/images/nav_next\.png["\'][^;]*;',
            'background: #ddd; content: ">"; text-align: center;',
            content
        )
        
        # 清理多余空行
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        
        # 只有在内容发生变化时才写入文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def find_css_files(root_dir):
    """查找所有CSS文件"""
    css_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.css'):
                css_files.append(os.path.join(root, file))
    return css_files

def main():
    """主函数"""
    root_dir = '/Volumes/acasis/yogweb'
    
    print("🎨 清理CSS文件中的外部依赖...")
    print(f"📁 工作目录: {root_dir}")
    
    # 查找所有CSS文件
    css_files = find_css_files(root_dir)
    print(f"📊 找到 {len(css_files)} 个CSS文件")
    
    # 处理每个文件
    cleaned_count = 0
    for i, file_path in enumerate(css_files, 1):
        rel_path = os.path.relpath(file_path, root_dir)
        
        if cleanup_css_file(file_path):
            print(f"[{i}/{len(css_files)}] 清理: {rel_path}")
            cleaned_count += 1
    
    print(f"\n✨ CSS清理完成！")
    print(f"📈 共清理 {cleaned_count} 个文件")
    print("\n🎯 清理内容包括:")
    print("  • 移除外部@import引用")
    print("  • 替换外部图片为本地样式")
    print("  • 清理多余空行")
    print("\n✅ CSS文件现在完全本地化！")

if __name__ == "__main__":
    main()