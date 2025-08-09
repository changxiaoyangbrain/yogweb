#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CSS现代化脚本 - 系统性现代化CSS代码
"""

import os
import re
from pathlib import Path

# CSS变量定义 - 现代化颜色系统
CSS_VARIABLES = """
:root {
  /* 主色调 */
  --primary-color: #00053F;
  --secondary-color: #C27D3D;
  --accent-color: #D00000;
  --text-primary: #4b4b4b;
  --text-secondary: #666666;
  --text-muted: #39494C;
  
  /* 背景色 */
  --bg-primary: #FFFFFF;
  --bg-secondary: #f8f9fa;
  
  /* 字体 */
  --font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Hiragino Sans", "Hiragino Kaku Gothic ProN", "Hiragino Sans GB", "Microsoft JhengHei", sans-serif;
  --font-family-ja: "Hiragino Sans", "Hiragino Kaku Gothic ProN", "Microsoft JhengHei", sans-serif;
  
  /* 间距 */
  --spacing-xs: 0.25rem;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 1.5rem;
  --spacing-xl: 2rem;
  --spacing-xxl: 3rem;
  
  /* 阴影 */
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.1);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
  
  /* 圆角 */
  --border-radius-sm: 0.25rem;
  --border-radius-md: 0.375rem;
  --border-radius-lg: 0.5rem;
  
  /* 过渡 */
  --transition-fast: 0.15s ease-in-out;
  --transition-base: 0.25s ease-in-out;
  --transition-slow: 0.5s ease-in-out;
}
"""

def modernize_css_file(file_path):
    """现代化单个CSS文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes = []
        
        # 1. 移除IE特定代码
        content = re.sub(r'-ms-filter:[^;]+;?\s*\n?', '', content)
        content = re.sub(r'filter:\s*alpha\([^)]+\);?\s*\n?', '', content)
        content = re.sub(r'-moz-opacity:[^;]+;?\s*\n?', '', content)
        if original_content != content:
            changes.append("移除IE兼容代码")
        
        # 2. 现代化opacity写法
        content = re.sub(r'opacity:\s*0\.(\d+)', r'opacity: 0.\1', content)
        
        # 3. 移除不必要的浏览器前缀（现代浏览器不需要）
        unnecessary_prefixes = [
            r'-webkit-border-radius:[^;]+;?\s*\n?',
            r'-moz-border-radius:[^;]+;?\s*\n?',
            r'-webkit-box-shadow:[^;]+;?\s*\n?', 
            r'-moz-box-shadow:[^;]+;?\s*\n?'
        ]
        for prefix in unnecessary_prefixes:
            old_content = content
            content = re.sub(prefix, '', content)
            if old_content != content:
                changes.append("移除不必要浏览器前缀")
        
        # 4. 现代化字体定义
        old_font_pattern = r'font-family:\s*[^;]*"MS\s[^"]*"[^;]*;'
        if re.search(old_font_pattern, content, re.IGNORECASE):
            content = re.sub(old_font_pattern, 'font-family: var(--font-family-ja);', content, flags=re.IGNORECASE)
            changes.append("现代化字体定义")
        
        # 5. 替换常用颜色为CSS变量
        color_map = {
            '#00053F': 'var(--primary-color)',
            '#C27D3D': 'var(--secondary-color)', 
            '#D00000': 'var(--accent-color)',
            '#4b4b4b': 'var(--text-primary)',
            '#666666': 'var(--text-secondary)',
            '#39494C': 'var(--text-muted)',
            '#FFFFFF': 'var(--bg-primary)'
        }
        
        for old_color, new_var in color_map.items():
            if old_color.lower() in content.lower():
                content = re.sub(re.escape(old_color), new_var, content, flags=re.IGNORECASE)
                changes.append(f"使用CSS变量替代硬编码颜色")
        
        # 6. 现代化过渡效果
        content = re.sub(r'transition:\s*all\s+0\.3s', 'transition: var(--transition-base)', content)
        content = re.sub(r'transition:\s*opacity\s+0\.3s', 'transition: opacity var(--transition-base)', content)
        
        # 7. 添加基础响应式支持（如果文件名包含base或main）
        if 'base.css' in file_path.lower() or 'main.css' in file_path.lower():
            if '@media' not in content:
                responsive_css = """

/* 响应式断点 */
@media (max-width: 768px) {
  .contentInnerFream,
  #contents .laboratoryArea,
  #contents .styleArea {
    width: 100%;
    max-width: none;
  }
  
  .indexContentMenuLi {
    height: auto;
    min-height: 300px;
  }
  
  table[role="presentation"] {
    width: 100%;
  }
  
  .sml, .sml2, .reg, .reg2 {
    font-size: clamp(12px, 2.5vw, 14px);
  }
}

@media (max-width: 480px) {
  .contentInnerFream {
    padding: 0 var(--spacing-md);
  }
  
  table[role="presentation"] td {
    display: block;
    width: 100% !important;
  }
}
"""
                content += responsive_css
                changes.append("添加基础响应式支持")
        
        # 8. 现代化长度单位（保守处理，只处理明显可以改进的）
        # 将一些固定的小数值改为rem
        content = re.sub(r'margin:\s*(\d+)px 0', lambda m: f'margin: {int(m.group(1))/16}rem 0' if int(m.group(1)) <= 32 else m.group(0), content)
        content = re.sub(r'padding:\s*(\d+)px', lambda m: f'padding: {int(m.group(1))/16}rem' if int(m.group(1)) <= 32 else m.group(0), content)
        
        # 只有在内容发生变化时才写入文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return changes
        return []
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return []

def create_modern_css_system():
    """创建现代化CSS系统文件"""
    
    # 创建CSS变量文件
    variables_file = '/Volumes/acasis/yogweb/css/variables.css'
    with open(variables_file, 'w', encoding='utf-8') as f:
        f.write(f"/* CSS变量系统 - 现代化颜色和尺寸管理 */\n{CSS_VARIABLES}")
    
    # 创建现代化工具类
    utilities_css = """
/* 现代化工具类 */
.text-center { text-align: center; }
.text-left { text-align: left; }
.text-right { text-align: right; }

.d-flex { display: flex; }
.d-grid { display: grid; }
.d-block { display: block; }
.d-inline-block { display: inline-block; }
.d-none { display: none; }

.flex-wrap { flex-wrap: wrap; }
.flex-nowrap { flex-wrap: nowrap; }
.justify-center { justify-content: center; }
.justify-between { justify-content: space-between; }
.align-center { align-items: center; }

.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: var(--spacing-md); }
.grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: var(--spacing-md); }

@media (max-width: 768px) {
  .grid-2, .grid-3 { grid-template-columns: 1fr; }
}

.mb-sm { margin-bottom: var(--spacing-sm); }
.mb-md { margin-bottom: var(--spacing-md); }
.mb-lg { margin-bottom: var(--spacing-lg); }
.mt-sm { margin-top: var(--spacing-sm); }
.mt-md { margin-top: var(--spacing-md); }
.mt-lg { margin-top: var(--spacing-lg); }

.p-sm { padding: var(--spacing-sm); }
.p-md { padding: var(--spacing-md); }
.p-lg { padding: var(--spacing-lg); }

.shadow-sm { box-shadow: var(--shadow-sm); }
.shadow-md { box-shadow: var(--shadow-md); }
.shadow-lg { box-shadow: var(--shadow-lg); }

.rounded { border-radius: var(--border-radius-md); }
.rounded-sm { border-radius: var(--border-radius-sm); }
.rounded-lg { border-radius: var(--border-radius-lg); }

.transition { transition: var(--transition-base); }
.transition-fast { transition: var(--transition-fast); }

.hover\\:opacity-70:hover { opacity: 0.7; }
.hover\\:scale-105:hover { transform: scale(1.05); }

/* 现代化卡片样式 */
.card {
  background: var(--bg-primary);
  border-radius: var(--border-radius-md);
  box-shadow: var(--shadow-sm);
  padding: var(--spacing-lg);
  transition: var(--transition-base);
}

.card:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}

/* 现代化按钮样式 */
.btn {
  display: inline-block;
  padding: var(--spacing-sm) var(--spacing-lg);
  background: var(--primary-color);
  color: white;
  text-decoration: none;
  border-radius: var(--border-radius-md);
  transition: var(--transition-base);
  border: none;
  cursor: pointer;
  font-family: inherit;
}

.btn:hover {
  background: color-mix(in srgb, var(--primary-color) 90%, black);
  transform: translateY(-1px);
}

.btn-secondary {
  background: var(--secondary-color);
}

.btn-secondary:hover {
  background: color-mix(in srgb, var(--secondary-color) 90%, black);
}

/* 现代化容器 */
.container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--spacing-md);
}

@media (max-width: 768px) {
  .container {
    padding: 0 var(--spacing-sm);
  }
}
"""
    
    utilities_file = '/Volumes/acasis/yogweb/css/utilities.css'
    with open(utilities_file, 'w', encoding='utf-8') as f:
        f.write(utilities_css)
    
    return ['variables.css', 'utilities.css']

def find_css_files(root_dir):
    """查找所有CSS文件"""
    css_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.css') and not file.startswith('variables') and not file.startswith('utilities'):
                css_files.append(os.path.join(root, file))
    return css_files

def main():
    """主函数"""
    root_dir = '/Volumes/acasis/yogweb'
    
    print("🚀 CSS现代化开始...")
    print(f"📁 工作目录: {root_dir}")
    
    # 1. 创建现代化CSS系统
    print("📦 创建现代化CSS系统...")
    new_files = create_modern_css_system()
    for file in new_files:
        print(f"  ✅ 创建: css/{file}")
    
    # 2. 查找并现代化现有CSS文件
    css_files = find_css_files(root_dir)
    print(f"📊 找到 {len(css_files)} 个CSS文件需要现代化")
    
    modernized_count = 0
    total_changes = []
    
    for i, file_path in enumerate(css_files, 1):
        rel_path = os.path.relpath(file_path, root_dir)
        
        changes = modernize_css_file(file_path)
        if changes:
            print(f"[{i}/{len(css_files)}] 🎨 现代化: {rel_path}")
            for change in changes:
                print(f"  • {change}")
            modernized_count += 1
            total_changes.extend(changes)
    
    print(f"\n✨ CSS现代化完成！")
    print(f"📈 共现代化 {modernized_count} 个文件")
    
    if total_changes:
        print("\n🎯 现代化操作统计:")
        change_counts = {}
        for change in total_changes:
            change_counts[change] = change_counts.get(change, 0) + 1
        
        for change, count in change_counts.items():
            print(f"  • {change}: {count} 次")
    
    print("\n💡 下一步建议:")
    print("  📱 在HTML中引入 css/variables.css 和 css/utilities.css")
    print("  🔧 使用新的工具类替换内联样式")
    print("  📊 测试响应式效果")
    print("  ⚡ 验证现代浏览器兼容性")

if __name__ == "__main__":
    main()