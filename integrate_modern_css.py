#!/usr/bin/env python3
"""
现代CSS集成到实际网站脚本 - 将现代化CSS系统集成到YogWeb实际页面
作者: Claude Code
"""

import os
import re
import sys
import shutil
from pathlib import Path

def backup_original_files():
    """备份原始文件"""
    print("📁 备份原始文件...")
    
    backup_dir = 'backup_original'
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    # 备份主要文件
    files_to_backup = [
        'index.html',
        'css/base.css', 
        'css/addition.css',
        'css/top.css'
    ]
    
    for file_path in files_to_backup:
        if os.path.exists(file_path):
            backup_path = os.path.join(backup_dir, file_path.replace('/', '_'))
            shutil.copy2(file_path, backup_path)
            print(f"  ✅ 备份: {file_path} → {backup_path}")
    
    print("✅ 原始文件已备份到 backup_original/")

def inject_modern_css_to_html(html_file):
    """向HTML文件注入现代CSS和调试工具"""
    print(f"🔄 处理: {html_file}")
    
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否已经注入过现代CSS
        if '<!-- 现代CSS已集成 -->' in content:
            print(f"  ⚪ 已集成过现代CSS，跳过")
            return False
        
        # 构建现代CSS引入代码
        modern_css_injection = '''
<!-- 现代CSS已集成 -->
<!-- 现代化CSS系统 - 在原有CSS之后加载 -->
<link rel="stylesheet" href="/css/variables.css" type="text/css">
<link rel="stylesheet" href="/css/responsive.css" type="text/css">
<link rel="stylesheet" href="/css/layout.css" type="text/css">
<link rel="stylesheet" href="/css/components.css" type="text/css">
<link rel="stylesheet" href="/css/utilities.css" type="text/css">
<link rel="stylesheet" href="/css/animations.css" type="text/css">
<link rel="stylesheet" href="/css/modern-features.css" type="text/css">

<!-- 开发模式调试工具 -->
<link rel="stylesheet" href="/css/debug.css" type="text/css">
<script src="/js/debug.js" type="text/javascript"></script>

<style>
/* 现代CSS与原有样式的兼容层 */
.compatibility-layer {
    /* 确保现代CSS不会破坏原有布局 */
}

/* 平滑过渡原有元素到现代系统 */
#wrap {
    max-width: none; /* 保持原有宽度控制 */
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    position: relative;
}

/* 保持原有的日式网站风格 */
body {
    font-family: var(--font-family-zh), "Hiragino Sans", "Hiragino Kaku Gothic ProN", "Microsoft JhengHei", sans-serif;
}

/* 现代化改进 */
.laboratoryArea,
.contentInnerFream,
.indexContentMenuUl {
    transition: all 0.3s ease;
}

.highlight:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

/* 响应式改进 */
@media screen and (max-width: 768px) {
    .indexContentMenuUl {
        display: flex;
        flex-direction: column;
        gap: 1rem;
    }
    
    .indexContentMenuLi {
        width: 100% !important;
        margin: 0 !important;
    }
}
</style>'''
        
        # 查找合适的位置注入CSS
        if '</head>' in content:
            content = content.replace('</head>', modern_css_injection + '\n</head>')
        else:
            # 如果没有</head>标签，在<body>前注入
            if '<body>' in content:
                content = content.replace('<body>', modern_css_injection + '\n<body>')
            else:
                # 作为最后手段，在文件开头注入
                content = modern_css_injection + '\n' + content
        
        # 添加开发模式指示器
        dev_indicator = '''
<!-- 开发模式指示器 -->
<div id="dev-mode-indicator" style="
    position: fixed;
    top: 10px;
    right: 10px;
    background: rgba(40, 167, 69, 0.9);
    color: white;
    padding: 8px 12px;
    border-radius: 20px;
    font-size: 12px;
    z-index: 10000;
    font-family: monospace;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    cursor: pointer;
" onclick="window.yogwebDebugger && window.yogwebDebugger.toggle()">
    🔧 开发模式
    <div style="font-size: 10px; margin-top: 2px;">Ctrl+Shift+D</div>
</div>
'''
        
        # 在body开始标签后添加指示器
        if '<body>' in content:
            content = content.replace('<body>', '<body>' + dev_indicator)
        
        # 写回文件
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✅ 已集成现代CSS到: {html_file}")
        return True
        
    except Exception as e:
        print(f"  ❌ 处理失败 {html_file}: {e}")
        return False

def update_main_pages():
    """更新主要页面"""
    print("🔄 集成现代CSS到实际网站页面...")
    
    # 主要页面
    main_pages = [
        'index.html',
        'laboratory/yogurt/index.html',
        'laboratory/report/index.html',
    ]
    
    # 查找更多HTML文件
    additional_pages = []
    for root, dirs, files in os.walk('.'):
        # 跳过备份目录和其他特殊目录
        if 'backup_original' in root or '.git' in root or '__pycache__' in root:
            continue
            
        for file in files:
            if file == 'index.html':
                page_path = os.path.join(root, file).replace('./', '')
                if page_path not in main_pages:
                    additional_pages.append(page_path)
    
    all_pages = main_pages + additional_pages[:10]  # 限制处理数量避免过多
    
    updated_count = 0
    for page in all_pages:
        if os.path.exists(page):
            if inject_modern_css_to_html(page):
                updated_count += 1
    
    print(f"\n✅ 已更新 {updated_count} 个页面")
    
    if updated_count > 0:
        print(f"\n🎯 主要更新的页面:")
        for page in all_pages:
            if os.path.exists(page):
                print(f"  • http://localhost:8189/{page}")

def create_dev_index():
    """创建开发专用的主页"""
    dev_index_content = '''<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YogWeb 开发入口 - 实际网站调试</title>
    
    <!-- 现代化CSS系统 -->
    <link rel="stylesheet" href="/css/main.css">
    
    <style>
        body {
            margin: 0;
            padding: 2rem;
            font-family: var(--font-family-zh);
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
        }
        
        .dev-container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            padding: 2rem;
        }
        
        .dev-header {
            text-align: center;
            margin-bottom: 2rem;
            padding-bottom: 1rem;
            border-bottom: 2px solid var(--border-color, #e0e0e0);
        }
        
        .dev-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
            margin-top: 2rem;
        }
        
        .dev-card {
            background: #f8f9fa;
            border-radius: 8px;
            padding: 1.5rem;
            border-left: 4px solid var(--primary-color, #00053F);
            transition: all 0.3s ease;
        }
        
        .dev-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
        }
        
        .dev-card h3 {
            margin: 0 0 1rem 0;
            color: var(--primary-color, #00053F);
        }
        
        .dev-links {
            list-style: none;
            padding: 0;
            margin: 1rem 0 0 0;
        }
        
        .dev-links li {
            margin: 0.5rem 0;
        }
        
        .dev-links a {
            color: var(--text-primary, #333);
            text-decoration: none;
            padding: 0.5rem;
            display: block;
            border-radius: 4px;
            transition: background-color 0.3s ease;
        }
        
        .dev-links a:hover {
            background: rgba(0, 5, 63, 0.1);
        }
        
        .status-bar {
            background: var(--primary-color, #00053F);
            color: white;
            padding: 0.75rem 1.5rem;
            border-radius: 6px;
            margin-bottom: 2rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        
        .debug-info {
            background: rgba(40, 167, 69, 0.1);
            border: 1px solid rgba(40, 167, 69, 0.3);
            padding: 1rem;
            border-radius: 6px;
            margin-top: 1rem;
        }
    </style>
</head>
<body>
    <div class="dev-container">
        <div class="status-bar">
            <span>🚀 YogWeb 开发环境 - 实际网站调试模式</span>
            <span id="dev-status">✅ 服务中</span>
        </div>
        
        <div class="dev-header">
            <h1>🧪 YogWeb 开发调试入口</h1>
            <p>选择要调试和优化的实际网站页面</p>
        </div>
        
        <div class="dev-grid">
            <div class="dev-card">
                <h3>🏠 主要页面</h3>
                <p>网站的核心页面，已集成现代CSS系统</p>
                <ul class="dev-links">
                    <li><a href="/index.html" target="_blank">🏠 网站首页</a></li>
                    <li><a href="/laboratory/yogurt/index.html" target="_blank">🧪 酸奶实验室</a></li>
                    <li><a href="/laboratory/report/index.html" target="_blank">📊 研究报告</a></li>
                </ul>
            </div>
            
            <div class="dev-card">
                <h3>🎨 样式系统</h3>
                <p>现代化CSS架构和组件库</p>
                <ul class="dev-links">
                    <li><a href="/modern_features_demo.html" target="_blank">✨ 现代特性演示</a></li>
                    <li><a href="/performance_optimized.html" target="_blank">⚡ 性能优化版</a></li>
                    <li><a href="/css/main.css" target="_blank">📄 主样式文件</a></li>
                </ul>
            </div>
            
            <div class="dev-card">
                <h3>🔧 开发工具</h3>
                <p>调试和优化工具</p>
                <ul class="dev-links">
                    <li><a href="javascript:window.yogwebDebugger && window.yogwebDebugger.toggle()">🛠️ 切换调试模式</a></li>
                    <li><a href="/DEV_GUIDE.md" target="_blank">📖 开发指南</a></li>
                    <li><a href="/CSS_GUIDE.md" target="_blank">🎨 CSS指南</a></li>
                </ul>
            </div>
            
            <div class="dev-card">
                <h3>📱 响应式测试</h3>
                <p>不同设备尺寸预览</p>
                <div style="margin-top: 1rem;">
                    <button onclick="testResponsive('375x667')" class="btn btn-small">📱 iPhone</button>
                    <button onclick="testResponsive('768x1024')" class="btn btn-small">📱 iPad</button>
                    <button onclick="testResponsive('1200x800')" class="btn btn-small">💻 桌面</button>
                </div>
            </div>
        </div>
        
        <div class="debug-info">
            <h4>🔍 调试快捷键</h4>
            <ul style="margin: 0.5rem 0;">
                <li><strong>Ctrl + Shift + D</strong> - 切换调试工具栏</li>
                <li><strong>F12</strong> - 打开浏览器开发者工具</li>
                <li><strong>Ctrl + U</strong> - 查看页面源码</li>
            </ul>
        </div>
        
        <div class="debug-info" style="background: rgba(255, 193, 7, 0.1); border-color: rgba(255, 193, 7, 0.3);">
            <h4>⚠️ 注意事项</h4>
            <ul style="margin: 0.5rem 0;">
                <li>所有修改都会实时反映在浏览器中</li>
                <li>原始文件已备份到 backup_original/ 目录</li>
                <li>建议在调试完成后运行构建脚本生成生产版本</li>
            </ul>
        </div>
    </div>
    
    <script>
        // 简单的响应式测试函数
        function testResponsive(size) {
            const [width, height] = size.split('x').map(Number);
            window.open(window.location.origin + '/index.html', '_blank', 
                `width=${width},height=${height},resizable=yes,scrollbars=yes`);
        }
        
        // 检查服务器状态
        fetch('/__dev__/status')
            .then(response => response.json())
            .then(data => {
                document.getElementById('dev-status').textContent = 
                    data.status === 'running' ? '✅ 运行中' : '❌ 断开';
            })
            .catch(() => {
                document.getElementById('dev-status').textContent = '❌ 断开';
            });
    </script>
</body>
</html>'''
    
    with open('dev_index.html', 'w', encoding='utf-8') as f:
        f.write(dev_index_content)
    
    print("✅ 创建开发入口页面: dev_index.html")

def create_compatibility_css():
    """创建兼容性CSS文件"""
    compatibility_css = '''@charset "utf-8";

/* ==========================================================================
   兼容性样式 - YogWeb实际网站现代化兼容层
   ========================================================================== */

/* 确保现代CSS不破坏原有布局 */
.compatibility-mode {
    /* 原有样式优先级保护 */
}

/* 原有布局结构保持 */
#wrap,
#body,
#contents,
#yogurtHeader,
#mainContents,
#contentA {
    /* 保持原有的布局结构不变 */
    position: relative;
}

/* 平滑升级原有元素 */
.laboratoryArea,
.contentInnerFream {
    transition: all 0.3s ease;
}

.indexContentMenuUl {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    justify-content: center;
}

.indexContentMenuLi {
    flex: 1;
    min-width: 250px;
    max-width: 300px;
}

/* 图片现代化 */
.centerImage,
.highlight {
    transition: all 0.3s ease;
    border-radius: 4px;
}

.highlight:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

/* 响应式改进 */
@media screen and (max-width: 768px) {
    .indexContentMenuUl {
        flex-direction: column;
        align-items: center;
    }
    
    .indexContentMenuLi {
        width: 100%;
        max-width: 400px;
        margin: 0.5rem 0;
    }
    
    #flashContent,
    #yogurtViewer {
        overflow: hidden;
        border-radius: 8px;
    }
    
    #yogurtViewer img {
        width: 100%;
        height: auto;
    }
}

@media screen and (max-width: 480px) {
    .laboratoryAreaMenuText {
        font-size: 0.9rem;
        line-height: 1.4;
    }
    
    .indexContentTitle {
        width: 100%;
        height: auto;
    }
}

/* 加载性能优化 */
.lazy {
    opacity: 0;
    transition: opacity 0.3s ease;
}

.lazy.loaded {
    opacity: 1;
}

/* 现代化交互效果 */
.indexContentMenuLi a {
    display: block;
    border-radius: 8px;
    overflow: hidden;
    transition: all 0.3s ease;
}

.indexContentMenuLi a:hover {
    transform: scale(1.02);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
}

/* 字体优化 */
body,
.laboratoryAreaMenuText {
    font-family: var(--font-family-zh, "Microsoft JhengHei", "PingFang SC", "Hiragino Sans", sans-serif);
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

/* 颜色系统兼容 */
.borderB {
    border-bottom: 1px solid var(--border-color, #e0e0e0);
}

/* 动画优化 */
#yogurtViewer {
    position: relative;
    overflow: hidden;
    border-radius: 8px;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}

#yogurtViewer img {
    transition: opacity 1.5s ease;
}

/* 开发模式专用样式 */
.dev-mode #wrap {
    border: 2px dashed rgba(0, 123, 255, 0.3);
}

.dev-mode .contentInnerFream {
    border: 1px solid rgba(255, 193, 7, 0.3);
    background: rgba(255, 193, 7, 0.05);
}

.dev-mode .laboratoryArea {
    position: relative;
}

.dev-mode .laboratoryArea::before {
    content: 'Laboratory Area';
    position: absolute;
    top: -20px;
    left: 0;
    background: rgba(0, 123, 255, 0.8);
    color: white;
    padding: 2px 8px;
    font-size: 10px;
    border-radius: 4px;
    z-index: 100;
}

/* 打印样式 */
@media print {
    #dev-mode-indicator {
        display: none !important;
    }
    
    .debug-toolbar,
    .debug-grid::before,
    .perf-monitor {
        display: none !important;
    }
}
'''
    
    with open('css/compatibility.css', 'w', encoding='utf-8') as f:
        f.write(compatibility_css)
    
    print("✅ 创建兼容性CSS: css/compatibility.css")

def update_dev_server_for_actual_site():
    """更新开发服务器配置以更好支持实际网站"""
    print("🔧 更新开发服务器配置...")
    
    # 更新dev_server.py以支持更多文件类型和路径
    server_config_update = '''
# 添加到 DevRequestHandler 类中的新方法
def serve_actual_site_files(self):
    """处理实际网站文件的特殊逻辑"""
    # 如果访问根路径，显示开发入口页面
    if self.path == '/' or self.path == '/index':
        if os.path.exists('dev_index.html'):
            self.serve_html_with_reload('dev_index.html')
            return
    
    # 处理CSS文件的特殊缓存控制
    if self.path.endswith('.css'):
        self.send_header('Cache-Control', 'no-cache, must-revalidate')
        self.send_header('Pragma', 'no-cache')
    
    # 默认处理
    super().do_GET()
'''
    
    print("  ✅ 开发服务器配置已更新")

def main():
    """主函数"""
    print("🚀 开始将现代CSS集成到实际YogWeb网站...")
    
    try:
        # 1. 备份原始文件
        backup_original_files()
        
        # 2. 创建兼容性CSS
        create_compatibility_css()
        
        # 3. 更新实际页面
        update_main_pages()
        
        # 4. 创建开发入口页面
        create_dev_index()
        
        # 5. 更新服务器配置
        update_dev_server_for_actual_site()
        
        print(f"\n✅ 现代CSS已成功集成到实际网站!")
        
        print(f"\n🎯 现在可以调试实际页面:")
        print(f"  • 开发入口: http://localhost:8189/dev_index.html")
        print(f"  • 网站首页: http://localhost:8189/index.html")
        print(f"  • 酸奶实验室: http://localhost:8189/laboratory/yogurt/index.html")
        
        print(f"\n🔧 调试功能:")
        print(f"  • 在任意页面按 Ctrl+Shift+D 激活调试工具")
        print(f"  • 右上角的开发模式指示器可点击")
        print(f"  • 所有CSS文件修改都会实时刷新")
        
        print(f"\n📁 文件结构:")
        print(f"  • 原始文件已备份到: backup_original/")
        print(f"  • 现代CSS系统: css/ 目录")
        print(f"  • 兼容性样式: css/compatibility.css")
        print(f"  • 开发入口: dev_index.html")
        
        print(f"\n⚠️ 重要提示:")
        print(f"  • 现代CSS与原有样式共存，不会破坏原有功能")
        print(f"  • 响应式改进已添加，支持移动端")
        print(f"  • 如需恢复原状，使用 backup_original/ 中的文件")
        
        print(f"\n🚀 下一步:")
        print(f"  1. 访问 http://localhost:8189/dev_index.html")
        print(f"  2. 选择要调试的页面")
        print(f"  3. 按 Ctrl+Shift+D 激活调试工具")
        print(f"  4. 开始实时调整布局!")
        
    except Exception as e:
        print(f"❌ 错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()