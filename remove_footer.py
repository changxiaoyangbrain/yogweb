#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import glob

def remove_footer_from_file(file_path):
    """从HTML文件中删除footer版权信息"""
    print(f"处理文件: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 删除footer区域的多种模式
        patterns = [
            # 完整的footer区域
            r'<!-- Common Footer Include -->\s*<footer[^>]*>.*?</footer>\s*<!-- Common Footer Include -->',
            # 只有footer标签
            r'<footer[^>]*>.*?</footer>',
            # 删除返回顶部和版权信息
            r'<div[^>]*l-pagetop[^>]*>.*?</div>',
            r'<p[^>]*m-footer-copyright[^>]*>.*?</p>',
            # 删除版权相关注释
            r'<!-- Common Footer Include -->'
        ]
        
        original_content = content
        
        for pattern in patterns:
            content = re.sub(pattern, '', content, flags=re.DOTALL | re.IGNORECASE)
        
        # 清理多余的空行
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        content = re.sub(r'</body>\s*\n+', '</body>\n', content)
        
        # 只有内容发生变化时才写入文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ 已处理: {file_path}")
            return True
        else:
            print(f"⏭️  无需处理: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ 处理失败 {file_path}: {e}")
        return False

def main():
    """主函数：批量处理所有HTML文件"""
    
    # 获取所有包含版权信息的HTML文件
    html_files = []
    
    # 搜索所有HTML文件
    for root, dirs, files in os.walk('/Volumes/acasis/yogweb'):
        # 跳过备份目录
        if 'backup_original' in root:
            continue
            
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                
                # 检查文件是否包含版权信息
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if '© 明治酸奶资料库' in content or 'l-footer' in content:
                            html_files.append(file_path)
                except:
                    continue
    
    print(f"找到 {len(html_files)} 个包含版权信息的文件")
    
    processed_count = 0
    for file_path in html_files:
        if remove_footer_from_file(file_path):
            processed_count += 1
    
    print(f"\n📊 处理完成:")
    print(f"   总计文件: {len(html_files)}")
    print(f"   成功处理: {processed_count}")
    print(f"   无需处理: {len(html_files) - processed_count}")

if __name__ == '__main__':
    main()