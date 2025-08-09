#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CSS现代化分析脚本 - 识别需要现代化的CSS问题
"""

import os
import re
from pathlib import Path

def analyze_css_file(file_path):
    """分析单个CSS文件的现代化需求"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        issues = []
        
        # 1. 检查旧的IE特定属性
        if re.search(r'-ms-filter:', content):
            issues.append("使用了IE特定的-ms-filter属性")
        if re.search(r'filter:\s*alpha\(', content):
            issues.append("使用了IE特定的alpha filter")
        if re.search(r'-moz-opacity:', content):
            issues.append("使用了旧的Mozilla opacity属性")
        
        # 2. 检查过时的浏览器前缀
        outdated_prefixes = [
            r'-webkit-border-radius:', r'-moz-border-radius:',
            r'-webkit-box-shadow:', r'-moz-box-shadow:',
            r'-webkit-transform:', r'-moz-transform:', r'-ms-transform:',
            r'-webkit-transition:', r'-moz-transition:', r'-ms-transition:'
        ]
        for prefix in outdated_prefixes:
            if re.search(prefix, content):
                issues.append(f"使用了可能不需要的浏览器前缀: {prefix.replace(':', '').replace('\\', '')}")
        
        # 3. 检查硬编码的像素值（可以改为相对单位）
        pixel_values = re.findall(r':\s*(\d+)px', content)
        if len(pixel_values) > 10:
            issues.append(f"大量使用像素单位 ({len(pixel_values)} 个)，建议考虑相对单位")
        
        # 4. 检查颜色定义（可以使用CSS变量）
        hex_colors = re.findall(r'#[0-9a-fA-F]{3,6}', content)
        if len(hex_colors) > 5:
            issues.append(f"多个硬编码颜色值 ({len(hex_colors)} 个)，建议使用CSS变量")
        
        # 5. 检查表格布局相关CSS（可以改为现代布局）
        if re.search(r'display:\s*table', content):
            issues.append("使用display: table布局，可考虑flexbox或grid")
        
        # 6. 检查浮动布局
        if re.search(r'float:\s*(left|right)', content):
            issues.append("使用float布局，建议改为flexbox或grid")
        
        # 7. 检查固定宽度设计
        fixed_widths = re.findall(r'width:\s*(\d{3,})px', content)
        if fixed_widths:
            issues.append("使用固定宽度设计，不适合响应式")
        
        # 8. 检查字体定义是否现代
        if re.search(r'font-family:.*"MS\s', content, re.IGNORECASE):
            issues.append("使用旧的Windows字体名称")
        
        return issues
        
    except Exception as e:
        return [f"分析出错: {e}"]

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
    
    print("🔍 CSS现代化需求分析...")
    print(f"📁 工作目录: {root_dir}")
    
    # 查找所有CSS文件
    css_files = find_css_files(root_dir)
    print(f"📊 找到 {len(css_files)} 个CSS文件")
    
    total_issues = {}
    file_issues = {}
    
    for i, file_path in enumerate(css_files, 1):
        rel_path = os.path.relpath(file_path, root_dir)
        
        issues = analyze_css_file(file_path)
        if issues:
            file_issues[rel_path] = issues
            print(f"[{i}/{len(css_files)}] 📝 {rel_path}")
            for issue in issues:
                print(f"  ⚠️ {issue}")
                # 统计问题类型
                issue_type = issue.split('(')[0].split('，')[0]  # 提取主要问题类型
                total_issues[issue_type] = total_issues.get(issue_type, 0) + 1
    
    print(f"\n📈 CSS现代化分析完成！")
    print(f"🔍 发现问题的文件数: {len(file_issues)}")
    
    if total_issues:
        print(f"\n🎯 问题类型统计:")
        for issue_type, count in sorted(total_issues.items(), key=lambda x: x[1], reverse=True):
            print(f"  • {issue_type}: {count} 次")
    
    print(f"\n💡 现代化建议:")
    print(f"  🔧 移除IE兼容代码")
    print(f"  🎨 使用CSS变量管理颜色")
    print(f"  📱 实现响应式设计")
    print(f"  🚀 使用现代布局(Grid/Flexbox)")
    print(f"  ⚡ 优化性能和可维护性")

if __name__ == "__main__":
    main()