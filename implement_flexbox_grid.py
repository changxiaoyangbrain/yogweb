#!/usr/bin/env python3
"""
CSS Grid/Flexbox布局实现脚本 - 将float布局转换为现代布局
作者: Claude Code
"""

import os
import re
import sys

def process_css_file(filepath):
    """处理单个CSS文件，转换布局"""
    print(f"处理: {filepath}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 1. 替换float布局为flexbox
        # 查找float: left/right的元素
        float_patterns = [
            # float: left; 转为 flex项目
            (r'(\s*)float\s*:\s*left\s*;', r'\1/* float: left; */ display: flex; flex-direction: row;'),
            (r'(\s*)float\s*:\s*right\s*;', r'\1/* float: right; */ margin-left: auto;'),
            
            # 清除浮动转为flexbox容器
            (r'(\s*)clear\s*:\s*both\s*;', r'\1/* clear: both; */ display: flex; flex-wrap: wrap;'),
        ]
        
        for pattern, replacement in float_patterns:
            content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
        
        # 2. 转换特定的布局模式
        
        # mikakuSec布局 - 左右布局转为flexbox
        if '.mikakuSec' in content:
            # 容器变为flex容器
            content = re.sub(
                r'(\.scienceArea \.mikakuSec\{[^}]*?)zoom:1;',
                r'\1display: flex; gap: 1rem; align-items: flex-start;',
                content
            )
            
            # 移除float，改为flex项目
            content = re.sub(
                r'(\.scienceArea \.mikakuSec \.photoBox\{)float:left;(width:159px;)',
                r'\1flex-shrink: 0; \2',
                content
            )
            
            content = re.sub(
                r'(\.scienceArea \.mikakuSec \.textBox\{)float:right;(width:305px;)',
                r'\1flex: 1; \2',
                content
            )
        
        # 3. 处理列表布局
        # ul li float: left 转为 flex
        content = re.sub(
            r'(ul li\{[^}]*?)float\s*:\s*left\s*;',
            r'\1/* float: left converted to flex item */',
            content
        )
        
        # 为ul添加flex容器样式
        if 'ul li' in content and 'float:left' in content:
            # 在对应的ul后添加flex样式
            content = re.sub(
                r'(\.sciLinkBlock\d+ ul):after\{[^}]+\}',
                r'\1{ display: flex; flex-wrap: wrap; gap: 0.5rem; }\n\1:after{ display: none; }',
                content
            )
        
        # 4. 处理表格布局中的dl元素
        if 'dl dt' in content and 'float' in content:
            # dt/dd布局转为flex
            content = re.sub(
                r'(\.scienceArea \.mikakuSec \.textBox dl dt\{)float:right;(width:142px;)',
                r'\1order: 2; \2',
                content
            )
            
            content = re.sub(
                r'(\.scienceArea \.mikakuSec \.textBox dl dd\{)float:left;(width:153px;)',
                r'\1order: 1; \2',
                content
            )
            
            # dl容器变为flex
            content = re.sub(
                r'(\.scienceArea \.mikakuSec \.textBox dl)[,\s]*\n',
                r'\1{ display: flex; flex-direction: row-reverse; gap: 1rem; }\n\1,\n',
                content
            )
        
        # 5. 添加响应式flexbox支持
        responsive_additions = """
/* 响应式Flexbox增强 */
@media screen and (max-width: 640px) {
    .mikakuSec {
        flex-direction: column !important;
        gap: 1rem !important;
    }
    
    .mikakuSec .photoBox,
    .mikakuSec .textBox {
        width: 100% !important;
        flex: none !important;
    }
    
    .sciLinkBlock01 ul,
    .sciLinkBlock02 ul,
    .sciLinkBlock03 ul {
        flex-direction: column !important;
        align-items: center !important;
    }
}
"""
        
        # 如果文件包含相关类，添加响应式样式
        if any(cls in content for cls in ['.mikakuSec', '.sciLinkBlock']):
            content += responsive_additions
        
        # 6. 优化现有的grid系统
        if 'table.recipe' in content:
            # 食谱表格使用CSS Grid
            grid_enhancement = """
/* Recipe表格Grid增强 */
table.recipe {
    display: grid;
    grid-template-columns: 1fr;
    gap: 0.5rem;
}

table.recipe dl.foods {
    display: grid;
    grid-template-columns: 60% 1fr;
    gap: 0.5rem;
    align-items: start;
}

@media screen and (max-width: 640px) {
    table.recipe dl.foods {
        grid-template-columns: 1fr;
    }
}
"""
            content += grid_enhancement
        
        # 只有内容发生变化才写入文件
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✅ 已更新布局样式")
            return True
        else:
            print(f"  ⚪ 无需更改")
            return False
            
    except Exception as e:
        print(f"  ❌ 错误: {e}")
        return False

def main():
    """主函数"""
    print("🚀 开始实现CSS Grid/Flexbox布局...")
    
    # 需要处理的CSS文件
    css_files = [
        'style/css/science.css',
        'style/css/beauty.css', 
        'style/css/choshoku.css',
        'css/utilities.css'
    ]
    
    updated_files = []
    
    for css_file in css_files:
        if os.path.exists(css_file):
            if process_css_file(css_file):
                updated_files.append(css_file)
        else:
            print(f"⚠️  文件不存在: {css_file}")
    
    print(f"\n✅ 布局现代化完成!")
    print(f"📊 处理了 {len(css_files)} 个文件")
    print(f"📝 更新了 {len(updated_files)} 个文件")
    
    if updated_files:
        print("\n📋 更新的文件:")
        for file in updated_files:
            print(f"  • {file}")
        
        print("\n🎯 实现的功能:")
        print("• Float布局转换为Flexbox")
        print("• 添加响应式Grid支持")
        print("• 优化列表和卡片布局")
        print("• 增强表格Grid系统")
        print("• 移动设备适配")
    
    print("\n🔗 下一步:")
    print("• 测试页面布局效果")
    print("• 验证响应式表现")
    print("• 优化CSS组织结构")

if __name__ == "__main__":
    main()