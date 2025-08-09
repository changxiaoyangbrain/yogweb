#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
网站本地化清理脚本
移除所有外部依赖，使网站完全本地化运行
"""

import os
import re
from pathlib import Path

def clean_html_file(file_path):
    """清理单个HTML文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 1. 移除明治官网的CSS引用
        content = re.sub(r'<link[^>]*href="https://www\.meiji\.co\.jp/assets/css/structure\.css"[^>]*>\n?', '', content)
        content = re.sub(r'<link[^>]*href="https://www\.meiji\.co\.jp/common/css/import\.css"[^>]*>\n?', '', content)
        
        # 2. 移除明治官网的JS引用
        content = re.sub(r'<script[^>]*src="https://www\.meiji\.co\.jp/common/js/checkDevice\.js"[^>]*></script>\n?', '', content)
        content = re.sub(r'<script[^>]*src="https://www\.meiji\.co\.jp/common/js/swfobject\.js"[^>]*></script>\n?', '', content)
        
        # 3. 移除或注释掉checkDevice()调用
        content = re.sub(r'<script>\s*var sp_redirect_url[^<]*checkDevice\(\);\s*</script>\n?', 
                         '<!-- Device check removed for local deployment -->\n', content)
        
        # 4. 移除手机端重定向链接
        content = re.sub(r'<link[^>]*rel="alternate"[^>]*media="only screen[^>]*href="https://www\.meiji\.co\.jp/smartphone[^>]*>\n?', '', content)
        
        # 5. 移除Google Tag Manager
        content = re.sub(r'<!-- Google Tag Manager -->[\s\S]*?<!-- End Google Tag Manager -->\n?', '', content, flags=re.MULTILINE)
        content = re.sub(r'<!-- Google Tag Manager \(noscript\) -->[\s\S]*?<!-- End Google Tag Manager \(noscript\) -->\n?', '', content, flags=re.MULTILINE)
        content = re.sub(r'<noscript><iframe src="https://www\.googletagmanager\.com[^>]*></iframe></noscript>\n?', '', content)
        
        # 6. 移除Google Analytics
        content = re.sub(r'<!-- Google Analytics Include -->[\s\S]*?<!-- //Google Analytics Include -->\n?', '', content, flags=re.MULTILINE)
        
        # 7. 移除OneTrust Cookie同意
        content = re.sub(r'<!-- meiji\.co\.jp[^>]*OneTrust Cookie[^>]*-->[\s\S]*?<!-- meiji\.co\.jp[^>]*OneTrust Cookie[^>]*-->\n?', '', content, flags=re.MULTILINE)
        content = re.sub(r'<script[^>]*src="https://cdn-au\.onetrust\.com[^>]*></script>\n?', '', content)
        
        # 8. 移除BOOMR性能监控脚本
        content = re.sub(r'<script>\(window\.BOOMR_mq=window\.BOOMR_mq[^<]*</script>\n?', '', content)
        content = re.sub(r'<script>!function\(e\)\{var n="https://s\.go-mpulse\.net/boomerang/"[\s\S]*?</script>', '', content, flags=re.MULTILINE)
        
        # 9. 修复绝对路径为相对路径（针对图片翻转效果）
        # 计算当前文件相对于根目录的深度
        rel_path = os.path.relpath(file_path, '/Volumes/acasis/yogweb')
        depth = len(Path(rel_path).parents) - 1
        
        if depth > 0:
            # 为子目录文件添加相对路径前缀
            prefix = '../' * depth
            # 替换onmouseover中的绝对路径
            content = re.sub(r"onmouseover=\"MM_swapImage\([^,]+,\s*'',\s*'/yogurtlibrary/zh/([^']+)'", 
                           f"onmouseover=\"MM_swapImage(\\g<0>,''','{prefix}\\1'", content)
            content = re.sub(r"'/yogurtlibrary/zh/", f"'{prefix}", content)
        
        # 10. 清理页脚中的明治全球链接和图标
        content = re.sub(r'<a href="https://www\.meiji\.com/global/"[^>]*>Global<img[^>]*></a>', 
                        '<a href="#">Global</a>', content)
        content = re.sub(r'<img src="https://www\.meiji\.co\.jp/assets/img/icons/pagetop\.svg"[^>]*>', 
                        '<span>↑</span>', content)
        content = re.sub(r'<img src="https://www\.meiji\.co\.jp/assets/img/icons/external_gray\.svg"[^>]*>', '', content)
        
        # 11. 清理空白行（多个连续空行合并为一个）
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
    
    print("🧹 开始清理网站，实现完全本地化...")
    print(f"📁 工作目录: {root_dir}")
    
    # 查找所有HTML文件
    html_files = find_html_files(root_dir)
    print(f"📊 找到 {len(html_files)} 个HTML文件")
    
    # 处理每个文件
    cleaned_count = 0
    for i, file_path in enumerate(html_files, 1):
        rel_path = os.path.relpath(file_path, root_dir)
        print(f"[{i}/{len(html_files)}] 处理: {rel_path}", end=' ')
        
        if clean_html_file(file_path):
            print("✅ 已清理")
            cleaned_count += 1
        else:
            print("⏭️  跳过")
    
    print(f"\n✨ 清理完成！")
    print(f"📈 共处理 {cleaned_count}/{len(html_files)} 个文件")
    print("\n🎯 清理内容包括:")
    print("  • 移除所有明治官网CSS/JS依赖")
    print("  • 移除Google Tag Manager和Analytics")
    print("  • 移除Cookie同意和性能监控脚本")
    print("  • 修复绝对路径为相对路径")
    print("  • 清理设备检测和重定向代码")
    print("\n🚀 网站现在可以完全本地化运行，并适合部署到Cloudflare！")

if __name__ == "__main__":
    main()