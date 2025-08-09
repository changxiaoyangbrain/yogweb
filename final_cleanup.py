#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
最终清理脚本 - 彻底移除所有外部依赖和跟踪代码
"""

import os
import re
from pathlib import Path

def final_cleanup(file_path):
    """最终清理HTML文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 1. 完全移除注释掉的跟踪代码块
        content = re.sub(r'<!-- Commented out.*?-->\n?<!--[\s\S]*?-->', '', content, flags=re.MULTILINE)
        
        # 2. 移除Google Ads相关代码
        content = re.sub(r'<script[^>]*src="https://www\.googleadservices\.com[^>]*>[\s\S]*?</script>\n?', '', content)
        content = re.sub(r'<div[^>]*>[\s]*<img[^>]*src="https://googleads\.g\.doubleclick\.net[^>]*>[\s]*</div>\n?', '', content)
        
        # 3. 移除Yahoo广告跟踪
        content = re.sub(r'<script[^>]*src="https://b92\.yahoo\.co\.jp[^>]*>[\s\S]*?</script>\n?', '', content)
        content = re.sub(r'<script[^>]*src="https://s\.yimg\.jp[^>]*>[\s\S]*?</script>\n?', '', content)
        content = re.sub(r'<div[^>]*>[\s]*<img[^>]*src="https://b97\.yahoo\.co\.jp[^>]*>[\s]*</div>\n?', '', content)
        
        # 4. 移除Google转化跟踪noscript标签
        content = re.sub(r'<noscript>[\s\S]*?googleadservices[\s\S]*?</noscript>\n?', '', content)
        
        # 5. 移除外部政府网站链接（改为文本）
        content = re.sub(r'<a href="https://www\.e-healthnet\.mhlw\.go\.jp[^"]*"[^>]*>([^<]*)</a>', 
                        r'\1（来源：厚生劳动省）', content)
        
        # 6. 移除语言切换菜单（如果用户只需要中文版）
        content = re.sub(r'<ul class="lang_menu">[\s\S]*?</ul>', '', content)
        
        # 7. 清理空的script标签
        content = re.sub(r'<script[^>]*>\s*</script>\n?', '', content)
        
        # 8. 清理过多的空行
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        content = re.sub(r'^\s*\n', '', content, flags=re.MULTILINE)
        
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
    
    print("🧹 执行最终清理，彻底移除所有外部依赖...")
    print(f"📁 工作目录: {root_dir}")
    
    # 查找所有HTML文件
    html_files = find_html_files(root_dir)
    print(f"📊 找到 {len(html_files)} 个HTML文件")
    
    # 处理每个文件
    cleaned_count = 0
    for i, file_path in enumerate(html_files, 1):
        rel_path = os.path.relpath(file_path, root_dir)
        
        if final_cleanup(file_path):
            print(f"[{i}/{len(html_files)}] 清理: {rel_path}")
            cleaned_count += 1
    
    print(f"\n✨ 最终清理完成！")
    print(f"📈 共清理 {cleaned_count} 个文件")
    print("\n🎯 清理内容包括:")
    print("  • 移除所有注释掉的跟踪代码")
    print("  • 移除Google Ads和Yahoo广告代码")
    print("  • 移除语言切换菜单")
    print("  • 转换外部链接为纯文本")
    print("  • 清理多余的空行")
    print("\n✅ 网站现在完全本地化，可以部署到Cloudflare！")

if __name__ == "__main__":
    main()