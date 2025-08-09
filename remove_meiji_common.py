#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
移除明治共通相关的注释和简化页脚
"""

import os
import re
from pathlib import Path

def clean_meiji_common(file_path):
    """清理明治共通相关内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 1. 移除"明治共通"相关注释
        content = re.sub(r'<!--\s*明治共通[^>]*-->\n?', '', content)
        
        # 2. 简化页脚 - 移除Global链接行
        content = re.sub(r'<li>\s*<a href="#"[^>]*>Global</a>\s*</li>\n?', '', content)
        
        # 3. 移除Cookie设置按钮
        content = re.sub(r'<li>\s*<a class="ot-sdk-show-settings"[^>]*></a>\s*</li>\n?', '', content)
        
        # 4. 如果页脚链接列表为空，移除整个ul
        content = re.sub(r'<ul class="m-footer-links">\s*</ul>\n?', '', content)
        
        # 5. 简化版权信息为中文
        content = re.sub(r'Copyright Meiji Co\., Ltd\. All Rights Reserved\.', 
                        '© 明治酸奶资料库', content)
        
        # 6. 移除Author meta标签中的Meiji Co., Ltd.
        content = re.sub(r'<meta name="Author" content="Meiji Co\., Ltd\.">', 
                        '<meta name="Author" content="明治酸奶资料库">', content)
        
        # 7. 清理多余的空行
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
    
    print("🧹 移除明治共通内容，完全本地化...")
    print(f"📁 工作目录: {root_dir}")
    
    # 查找所有HTML文件
    html_files = find_html_files(root_dir)
    print(f"📊 找到 {len(html_files)} 个HTML文件")
    
    # 处理每个文件
    cleaned_count = 0
    for i, file_path in enumerate(html_files, 1):
        rel_path = os.path.relpath(file_path, root_dir)
        
        if clean_meiji_common(file_path):
            print(f"[{i}/{len(html_files)}] 清理: {rel_path}")
            cleaned_count += 1
    
    print(f"\n✨ 清理完成！")
    print(f"📈 共清理 {cleaned_count} 个文件")
    print("\n🎯 清理内容包括:")
    print("  • 移除明治共通注释")
    print("  • 移除Global链接")
    print("  • 简化版权信息为中文")
    print("  • 清理页脚中的无用元素")
    print("\n✅ 网站现在完全专注于中文酸奶内容！")

if __name__ == "__main__":
    main()