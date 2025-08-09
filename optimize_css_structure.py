#!/usr/bin/env python3
"""
CSS组织结构优化脚本 - 整理和优化CSS文件结构
作者: Claude Code
"""

import os
import re
import sys

def create_layout_css():
    """创建统一的布局CSS文件"""
    layout_content = """@charset "utf-8";

/* ==========================================================================
   现代化布局系统 - Layout System
   ========================================================================== */

/* 基础布局容器 */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
}

.container-fluid {
    width: 100%;
    padding: 0 1rem;
}

/* Flexbox布局系统 */
.flex {
    display: flex;
}

.flex-column {
    flex-direction: column;
}

.flex-row {
    flex-direction: row;
}

.flex-wrap {
    flex-wrap: wrap;
}

.flex-center {
    justify-content: center;
    align-items: center;
}

.flex-between {
    justify-content: space-between;
}

.flex-around {
    justify-content: space-around;
}

.flex-1 {
    flex: 1;
}

.gap-1 { gap: 0.5rem; }
.gap-2 { gap: 1rem; }
.gap-3 { gap: 1.5rem; }
.gap-4 { gap: 2rem; }

/* Grid布局系统 */
.grid {
    display: grid;
}

.grid-cols-1 { grid-template-columns: repeat(1, 1fr); }
.grid-cols-2 { grid-template-columns: repeat(2, 1fr); }
.grid-cols-3 { grid-template-columns: repeat(3, 1fr); }
.grid-cols-4 { grid-template-columns: repeat(4, 1fr); }

.grid-gap-1 { grid-gap: 0.5rem; }
.grid-gap-2 { grid-gap: 1rem; }
.grid-gap-3 { grid-gap: 1.5rem; }
.grid-gap-4 { grid-gap: 2rem; }

/* 响应式Grid */
@media screen and (max-width: 768px) {
    .grid-cols-2,
    .grid-cols-3,
    .grid-cols-4 {
        grid-template-columns: 1fr;
    }
}

@media screen and (min-width: 769px) and (max-width: 1024px) {
    .grid-cols-3,
    .grid-cols-4 {
        grid-template-columns: repeat(2, 1fr);
    }
}

/* 卡片布局 */
.card {
    background: var(--bg-primary, #ffffff);
    border-radius: 8px;
    padding: 1.5rem;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    transition: box-shadow 0.3s ease;
}

.card:hover {
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
}

.card-header {
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid var(--border-light, #e0e0e0);
}

.card-body {
    line-height: 1.6;
}

.card-footer {
    margin-top: 1rem;
    padding-top: 0.5rem;
    border-top: 1px solid var(--border-light, #e0e0e0);
}

/* 列表布局 */
.list-reset {
    list-style: none;
    margin: 0;
    padding: 0;
}

.list-horizontal {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
}

.list-vertical {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

/* 响应式显示控制 */
.hidden { display: none !important; }
.block { display: block !important; }
.inline { display: inline !important; }
.inline-block { display: inline-block !important; }

/* 移动端隐藏 */
@media screen and (max-width: 640px) {
    .hidden-mobile { display: none !important; }
}

/* 桌面端隐藏 */
@media screen and (min-width: 641px) {
    .hidden-desktop { display: none !important; }
}

/* 对齐 */
.text-left { text-align: left; }
.text-center { text-align: center; }
.text-right { text-align: right; }

/* 间距系统 */
.m-0 { margin: 0; }
.m-1 { margin: 0.5rem; }
.m-2 { margin: 1rem; }
.m-3 { margin: 1.5rem; }
.m-4 { margin: 2rem; }

.mt-0 { margin-top: 0; }
.mt-1 { margin-top: 0.5rem; }
.mt-2 { margin-top: 1rem; }
.mt-3 { margin-top: 1.5rem; }
.mt-4 { margin-top: 2rem; }

.mb-0 { margin-bottom: 0; }
.mb-1 { margin-bottom: 0.5rem; }
.mb-2 { margin-bottom: 1rem; }
.mb-3 { margin-bottom: 1.5rem; }
.mb-4 { margin-bottom: 2rem; }

.p-0 { padding: 0; }
.p-1 { padding: 0.5rem; }
.p-2 { padding: 1rem; }
.p-3 { padding: 1.5rem; }
.p-4 { padding: 2rem; }

.pt-0 { padding-top: 0; }
.pt-1 { padding-top: 0.5rem; }
.pt-2 { padding-top: 1rem; }
.pt-3 { padding-top: 1.5rem; }
.pt-4 { padding-top: 2rem; }

.pb-0 { padding-bottom: 0; }
.pb-1 { padding-bottom: 0.5rem; }
.pb-2 { padding-bottom: 1rem; }
.pb-3 { padding-bottom: 1.5rem; }
.pb-4 { padding-bottom: 2rem; }

/* 宽度控制 */
.w-full { width: 100%; }
.w-auto { width: auto; }
.w-fit { width: fit-content; }

.max-w-sm { max-width: 640px; }
.max-w-md { max-width: 768px; }
.max-w-lg { max-width: 1024px; }
.max-w-xl { max-width: 1200px; }

/* 高度控制 */
.h-full { height: 100%; }
.h-auto { height: auto; }
.min-h-screen { min-height: 100vh; }

/* 定位 */
.relative { position: relative; }
.absolute { position: absolute; }
.fixed { position: fixed; }
.sticky { position: sticky; }

/* Z-index */
.z-10 { z-index: 10; }
.z-20 { z-index: 20; }
.z-30 { z-index: 30; }
.z-40 { z-index: 40; }
.z-50 { z-index: 50; }
"""
    
    with open('css/layout.css', 'w', encoding='utf-8') as f:
        f.write(layout_content)
    
    print("✅ 创建 css/layout.css")

def create_components_css():
    """创建组件样式文件"""
    components_content = """@charset "utf-8";

/* ==========================================================================
   组件样式系统 - Components System
   ========================================================================== */

/* 按钮组件 */
.btn {
    display: inline-block;
    padding: 0.5rem 1rem;
    margin: 0;
    border: none;
    border-radius: 4px;
    background: var(--bg-primary, #ffffff);
    color: var(--text-primary, #333333);
    font-size: 1rem;
    text-decoration: none;
    cursor: pointer;
    transition: all 0.3s ease;
    text-align: center;
}

.btn:hover {
    opacity: 0.9;
    transform: translateY(-2px);
}

.btn:active {
    transform: translateY(0);
}

.btn-primary {
    background: var(--primary-color, #00053F);
    color: white;
}

.btn-secondary {
    background: var(--secondary-color, #C27D3D);
    color: white;
}

.btn-outline {
    background: transparent;
    border: 2px solid var(--primary-color, #00053F);
    color: var(--primary-color, #00053F);
}

.btn-outline:hover {
    background: var(--primary-color, #00053F);
    color: white;
}

.btn-small {
    padding: 0.25rem 0.5rem;
    font-size: 0.875rem;
}

.btn-large {
    padding: 0.75rem 1.5rem;
    font-size: 1.125rem;
}

/* 输入框组件 */
.input {
    display: block;
    width: 100%;
    padding: 0.5rem;
    border: 1px solid var(--border-color, #cccccc);
    border-radius: 4px;
    font-size: 1rem;
    transition: border-color 0.3s ease;
}

.input:focus {
    outline: none;
    border-color: var(--primary-color, #00053F);
    box-shadow: 0 0 0 3px rgba(0, 5, 63, 0.1);
}

.input-group {
    margin-bottom: 1rem;
}

.input-label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: bold;
    color: var(--text-primary, #333333);
}

/* 导航组件 */
.nav {
    display: flex;
    list-style: none;
    margin: 0;
    padding: 0;
}

.nav-horizontal {
    flex-direction: row;
    gap: 1rem;
}

.nav-vertical {
    flex-direction: column;
    gap: 0.5rem;
}

.nav-item {
    margin: 0;
}

.nav-link {
    display: block;
    padding: 0.5rem 1rem;
    text-decoration: none;
    color: var(--text-primary, #333333);
    transition: all 0.3s ease;
}

.nav-link:hover {
    background: var(--bg-hover, #f5f5f5);
    color: var(--primary-color, #00053F);
}

.nav-link.active {
    background: var(--primary-color, #00053F);
    color: white;
}

/* 徽章组件 */
.badge {
    display: inline-block;
    padding: 0.25rem 0.5rem;
    font-size: 0.75rem;
    font-weight: bold;
    border-radius: 12px;
    background: var(--secondary-color, #C27D3D);
    color: white;
}

.badge-small {
    padding: 0.125rem 0.25rem;
    font-size: 0.625rem;
}

.badge-primary {
    background: var(--primary-color, #00053F);
}

.badge-success {
    background: #28a745;
}

.badge-warning {
    background: #ffc107;
    color: #333;
}

.badge-error {
    background: #dc3545;
}

/* 提示框组件 */
.alert {
    padding: 1rem;
    margin-bottom: 1rem;
    border-radius: 4px;
    border-left: 4px solid;
}

.alert-info {
    background: #e7f3ff;
    border-color: #0066cc;
    color: #004499;
}

.alert-success {
    background: #e8f5e8;
    border-color: #28a745;
    color: #155724;
}

.alert-warning {
    background: #fff8e1;
    border-color: #ffc107;
    color: #856404;
}

.alert-error {
    background: #f8e8e8;
    border-color: #dc3545;
    color: #721c24;
}

/* 分隔线组件 */
.divider {
    height: 1px;
    background: var(--border-color, #e0e0e0);
    margin: 1rem 0;
    border: none;
}

.divider-vertical {
    width: 1px;
    height: 100%;
    background: var(--border-color, #e0e0e0);
    margin: 0 1rem;
}

/* 标签组件 */
.tag {
    display: inline-block;
    padding: 0.25rem 0.5rem;
    font-size: 0.875rem;
    background: var(--bg-light, #f5f5f5);
    color: var(--text-primary, #333333);
    border-radius: 4px;
    margin: 0.125rem;
}

.tag-clickable {
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.tag-clickable:hover {
    background: var(--bg-hover, #e0e0e0);
}

/* 加载组件 */
.loading {
    display: inline-block;
    width: 20px;
    height: 20px;
    border: 2px solid var(--border-color, #e0e0e0);
    border-top: 2px solid var(--primary-color, #00053F);
    border-radius: 50%;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.loading-large {
    width: 40px;
    height: 40px;
    border-width: 4px;
}

/* 响应式组件调整 */
@media screen and (max-width: 640px) {
    .btn {
        width: 100%;
        margin-bottom: 0.5rem;
    }
    
    .nav-horizontal {
        flex-direction: column;
        gap: 0;
    }
    
    .alert {
        margin-left: -1rem;
        margin-right: -1rem;
        border-radius: 0;
    }
}
"""
    
    with open('css/components.css', 'w', encoding='utf-8') as f:
        f.write(components_content)
    
    print("✅ 创建 css/components.css")

def create_responsive_css():
    """创建响应式设计文件"""
    responsive_content = """@charset "utf-8";

/* ==========================================================================
   响应式设计系统 - Responsive System
   ========================================================================== */

/* 媒体查询断点 */
/*
- mobile: 0-640px
- tablet: 641px-1024px  
- desktop: 1025px+
- wide: 1281px+
*/

/* 基础响应式设置 */
* {
    box-sizing: border-box;
}

html {
    font-size: 16px;
    -webkit-text-size-adjust: 100%;
    -ms-text-size-adjust: 100%;
}

body {
    margin: 0;
    padding: 0;
    line-height: 1.6;
    font-family: var(--font-family-zh, 'Microsoft JhengHei', 'PingFang SC', 'SimHei', sans-serif);
}

/* 图片响应式 */
img {
    max-width: 100%;
    height: auto;
    display: block;
}

/* 表格响应式 */
.table-responsive {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
}

.table-responsive table {
    min-width: 600px;
}

/* 移动端优先设计 */
@media screen and (max-width: 640px) {
    /* 移动端基础设置 */
    html {
        font-size: 14px;
    }
    
    body {
        padding: 0;
        margin: 0;
    }
    
    /* 容器调整 */
    .container {
        padding: 0 0.5rem;
    }
    
    /* 字体大小调整 */
    h1 { font-size: 1.5rem; }
    h2 { font-size: 1.25rem; }
    h3 { font-size: 1.125rem; }
    h4 { font-size: 1rem; }
    h5 { font-size: 0.875rem; }
    h6 { font-size: 0.75rem; }
    
    /* 间距调整 */
    .p-4 { padding: 1rem; }
    .p-3 { padding: 0.75rem; }
    .p-2 { padding: 0.5rem; }
    
    .m-4 { margin: 1rem; }
    .m-3 { margin: 0.75rem; }
    .m-2 { margin: 0.5rem; }
    
    /* 表格移动端优化 */
    table {
        font-size: 0.875rem;
    }
    
    .table-stack {
        border: 0;
    }
    
    .table-stack thead {
        display: none;
    }
    
    .table-stack tr {
        display: block;
        border: 1px solid var(--border-color, #e0e0e0);
        margin-bottom: 0.5rem;
        padding: 0.5rem;
    }
    
    .table-stack td {
        display: block;
        text-align: right;
        border: none;
        padding: 0.25rem 0;
    }
    
    .table-stack td::before {
        content: attr(data-label) ': ';
        font-weight: bold;
        float: left;
    }
    
    /* 科学研究区域移动端适配 */
    .scienceArea .mikakuSec {
        flex-direction: column !important;
        gap: 1rem !important;
    }
    
    .scienceArea .mikakuSec .photoBox,
    .scienceArea .mikakuSec .textBox {
        width: 100% !important;
        float: none !important;
    }
    
    .scienceArea .mikakuSec .textBox dl {
        flex-direction: column !important;
    }
    
    .scienceArea .mikakuSec .textBox dl dt,
    .scienceArea .mikakuSec .textBox dl dd {
        width: 100% !important;
        order: unset !important;
    }
    
    /* 链接区块移动端适配 */
    .sciLinkBlock01 ul,
    .sciLinkBlock02 ul,
    .sciLinkBlock03 ul {
        flex-direction: column !important;
        align-items: center !important;
        gap: 0.5rem !important;
    }
    
    .beautyLinkBlock01,
    .sciLinkBlock01,
    .sciLinkBlock02,
    .sciLinkBlock03 {
        background-size: contain !important;
        background-position: center top !important;
        min-height: 200px !important;
        height: auto !important;
    }
}

/* 平板端设计 */
@media screen and (min-width: 641px) and (max-width: 1024px) {
    html {
        font-size: 15px;
    }
    
    .container {
        max-width: 960px;
        padding: 0 1rem;
    }
    
    /* 中等屏幕优化 */
    .grid-cols-4 {
        grid-template-columns: repeat(2, 1fr);
    }
    
    .grid-cols-3 {
        grid-template-columns: repeat(2, 1fr);
    }
    
    /* 科学区域平板适配 */
    .scienceArea .mikakuSec {
        gap: 1.5rem;
    }
    
    .scienceArea .mikakuSec .photoBox {
        width: 200px !important;
    }
    
    .scienceArea .mikakuSec .textBox {
        flex: 1;
        width: auto !important;
    }
}

/* 桌面端设计 */
@media screen and (min-width: 1025px) {
    html {
        font-size: 16px;
    }
    
    .container {
        max-width: 1200px;
    }
    
    /* 大屏幕优化 */
    .grid-cols-xl-5 {
        grid-template-columns: repeat(5, 1fr);
    }
    
    .grid-cols-xl-6 {
        grid-template-columns: repeat(6, 1fr);
    }
}

/* 超宽屏设计 */
@media screen and (min-width: 1281px) {
    .container {
        max-width: 1400px;
    }
    
    html {
        font-size: 18px;
    }
}

/* 打印样式 */
@media print {
    * {
        color: #000 !important;
        background: #fff !important;
        box-shadow: none !important;
    }
    
    .no-print {
        display: none !important;
    }
    
    .print-break {
        page-break-after: always;
    }
    
    a[href]:after {
        content: " (" attr(href) ")";
    }
    
    img {
        max-width: 100% !important;
        page-break-inside: avoid;
    }
}

/* 高对比度模式 */
@media (prefers-contrast: high) {
    :root {
        --primary-color: #000000;
        --text-primary: #000000;
        --bg-primary: #ffffff;
        --border-color: #000000;
    }
    
    .card {
        border: 2px solid #000000;
    }
}

/* 减少动画模式 */
@media (prefers-reduced-motion: reduce) {
    * {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
}

/* 深色模式支持 */
@media (prefers-color-scheme: dark) {
    :root {
        --bg-primary: #1a1a1a;
        --text-primary: #ffffff;
        --border-color: #404040;
        --bg-hover: #2a2a2a;
        --bg-light: #333333;
    }
    
    body {
        background: var(--bg-primary);
        color: var(--text-primary);
    }
    
    .card {
        background: #2a2a2a;
        border: 1px solid #404040;
    }
}
"""
    
    with open('css/responsive.css', 'w', encoding='utf-8') as f:
        f.write(responsive_content)
    
    print("✅ 创建 css/responsive.css")

def create_master_css():
    """创建主CSS文件统一管理"""
    master_content = """@charset "utf-8";

/* ==========================================================================
   YogWeb - 现代化酸奶研究网站样式系统
   ========================================================================== */

/* 基础系统 */
@import url('variables.css');      /* CSS变量定义 */
@import url('responsive.css');     /* 响应式基础设置 */

/* 布局系统 */  
@import url('layout.css');         /* 现代化布局系统 */

/* 组件系统 */
@import url('components.css');     /* 通用组件样式 */
@import url('utilities.css');      /* 实用工具类 */

/* 第三方组件 (保持不变) */
/* 在HTML中单独引入:
   - /common/css/slick.css
   - /common/css/magnific-popup.css
*/

/* 页面特定样式 (保持不变) */
/* 在HTML中按需引入:
   - /style/css/science.css
   - /style/css/beauty.css  
   - /style/css/choshoku.css
*/

/* ==========================================================================
   全局重置和基础设置
   ========================================================================== */

/* 现代化重置 */
*,
*::before,
*::after {
    box-sizing: border-box;
}

html {
    line-height: 1.15;
    -webkit-text-size-adjust: 100%;
    scroll-behavior: smooth;
}

body {
    margin: 0;
    padding: 0;
    font-family: var(--font-family-zh);
    font-size: 1rem;
    line-height: 1.6;
    color: var(--text-primary);
    background-color: var(--bg-primary, #ffffff);
}

/* 链接样式 */
a {
    color: var(--primary-color);
    text-decoration: none;
    transition: color 0.3s ease;
}

a:hover {
    color: var(--secondary-color);
    text-decoration: underline;
}

/* 标题样式 */
h1, h2, h3, h4, h5, h6 {
    margin: 0 0 1rem 0;
    font-weight: bold;
    line-height: 1.3;
    color: var(--primary-color);
}

h1 { font-size: 2rem; }
h2 { font-size: 1.75rem; }
h3 { font-size: 1.5rem; }
h4 { font-size: 1.25rem; }
h5 { font-size: 1.125rem; }
h6 { font-size: 1rem; }

/* 段落和文本 */
p {
    margin: 0 0 1rem 0;
    line-height: 1.6;
}

/* 列表 */
ul, ol {
    margin: 0 0 1rem 0;
    padding-left: 2rem;
}

li {
    margin-bottom: 0.25rem;
}

/* 表格基础样式 */
table {
    border-collapse: collapse;
    width: 100%;
    margin-bottom: 1rem;
}

th, td {
    padding: 0.5rem;
    text-align: left;
    border-bottom: 1px solid var(--border-color, #e0e0e0);
}

th {
    font-weight: bold;
    background-color: var(--bg-light, #f5f5f5);
}

/* 表单元素 */
input, textarea, select {
    font-family: inherit;
    font-size: inherit;
}

/* 图片 */
img {
    max-width: 100%;
    height: auto;
    display: block;
}

/* 代码 */
code {
    background-color: var(--bg-light, #f5f5f5);
    padding: 0.125rem 0.25rem;
    border-radius: 3px;
    font-size: 0.875em;
}

pre {
    background-color: var(--bg-light, #f5f5f5);
    padding: 1rem;
    border-radius: 4px;
    overflow-x: auto;
}

pre code {
    background: none;
    padding: 0;
}

/* 分隔线 */
hr {
    border: none;
    height: 1px;
    background-color: var(--border-color, #e0e0e0);
    margin: 2rem 0;
}

/* ==========================================================================
   可访问性改进
   ========================================================================== */

/* 跳转到主内容链接 */
.skip-to-main {
    position: absolute;
    top: -40px;
    left: 6px;
    background: var(--primary-color);
    color: white;
    padding: 8px;
    text-decoration: none;
    z-index: 1000;
}

.skip-to-main:focus {
    top: 6px;
}

/* 屏幕阅读器专用文本 */
.sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border: 0;
}

/* 焦点指示器 */
:focus {
    outline: 2px solid var(--primary-color);
    outline-offset: 2px;
}

/* ==========================================================================
   打印优化
   ========================================================================== */

@media print {
    .no-print {
        display: none !important;
    }
    
    * {
        color: #000 !important;
        background: transparent !important;
    }
    
    a[href]:after {
        content: " (" attr(href) ")";
    }
}
"""
    
    with open('css/main.css', 'w', encoding='utf-8') as f:
        f.write(master_content)
    
    print("✅ 创建 css/main.css")

def create_usage_guide():
    """创建CSS使用指南"""
    guide_content = """# CSS架构使用指南

## 📁 文件结构

```
css/
├── main.css           # 主文件，统一引入所有样式
├── variables.css      # CSS变量定义 
├── responsive.css     # 响应式基础设置
├── layout.css         # 现代化布局系统
├── components.css     # 通用组件样式
└── utilities.css      # 实用工具类

style/css/             # 页面特定样式 (保持不变)
├── science.css
├── beauty.css
└── choshoku.css

common/css/            # 第三方组件 (保持不变)
├── slick.css
└── magnific-popup.css
```

## 🎯 引入方式

### 方式1: 使用主文件 (推荐)
```html
<link rel="stylesheet" href="/css/main.css">
<!-- 按需引入页面特定样式 -->
<link rel="stylesheet" href="/style/css/science.css">
```

### 方式2: 按需引入
```html
<link rel="stylesheet" href="/css/variables.css">
<link rel="stylesheet" href="/css/responsive.css">  
<link rel="stylesheet" href="/css/layout.css">
<link rel="stylesheet" href="/css/components.css">
<link rel="stylesheet" href="/css/utilities.css">
```

## 🎨 CSS变量系统

```css
:root {
  --primary-color: #00053F;
  --secondary-color: #C27D3D;
  --text-primary: #4b4b4b;
  --bg-primary: #ffffff;
  --border-color: #e0e0e0;
  --font-family-zh: 'Microsoft JhengHei', 'PingFang SC', sans-serif;
}
```

## 🏗 布局系统

### Flexbox布局
```html
<div class="flex flex-center gap-2">
    <div class="flex-1">内容1</div>
    <div>内容2</div>  
</div>
```

### Grid布局
```html
<div class="grid grid-cols-3 grid-gap-2">
    <div>项目1</div>
    <div>项目2</div>
    <div>项目3</div>
</div>
```

### 容器
```html
<div class="container">
    <!-- 最大宽度1200px，居中对齐 -->
</div>

<div class="container-fluid">
    <!-- 100%宽度，左右边距1rem -->
</div>
```

## 🧩 组件系统

### 按钮
```html
<button class="btn btn-primary">主要按钮</button>
<button class="btn btn-secondary">次要按钮</button>
<button class="btn btn-outline">轮廓按钮</button>
```

### 卡片
```html
<div class="card">
    <div class="card-header">
        <h3>卡片标题</h3>
    </div>
    <div class="card-body">
        <p>卡片内容</p>
    </div>
    <div class="card-footer">
        <button class="btn btn-primary">操作</button>
    </div>
</div>
```

### 导航
```html
<ul class="nav nav-horizontal">
    <li class="nav-item">
        <a href="#" class="nav-link active">首页</a>
    </li>
    <li class="nav-item">
        <a href="#" class="nav-link">关于</a>
    </li>
</ul>
```

## 🛠 实用工具类

### 间距
```html
<div class="m-2 p-3">                <!-- margin: 1rem, padding: 1.5rem -->
<div class="mt-4 pb-2">              <!-- margin-top: 2rem, padding-bottom: 1rem -->
```

### 文本对齐
```html
<div class="text-center">居中对齐</div>
<div class="text-right">右对齐</div>
```

### 显示控制
```html
<div class="hidden-mobile">桌面端显示</div>
<div class="hidden-desktop">移动端显示</div>
```

## 📱 响应式设计

### 断点
- mobile: 0-640px
- tablet: 641px-1024px  
- desktop: 1025px+
- wide: 1281px+

### 响应式类
```html
<div class="grid-cols-1 tablet:grid-cols-2 desktop:grid-cols-3">
    <!-- 移动端1列，平板2列，桌面3列 -->
</div>
```

## 🎯 最佳实践

### ✅ 推荐
1. **优先使用工具类** - 快速原型和简单样式
2. **组合使用** - 布局工具类 + 组件类
3. **保持语义化** - 使用有意义的class名
4. **移动端优先** - 先设计小屏幕，再适配大屏幕

### ❌ 避免
1. **内联样式** - 影响维护性
2. **!important滥用** - 破坏级联规则
3. **过度嵌套** - 影响性能和可读性
4. **硬编码尺寸** - 使用相对单位

## 🔧 自定义扩展

### 添加新的工具类
```css
/* 在 utilities.css 中添加 */
.text-gradient {
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
```

### 创建新组件
```css
/* 在 components.css 中添加 */
.timeline {
    position: relative;
    padding-left: 2rem;
}

.timeline::before {
    content: '';
    position: absolute;
    left: 1rem;
    top: 0;
    bottom: 0;
    width: 2px;
    background: var(--border-color);
}
```

## 🚀 性能优化

1. **CSS文件压缩** - 生产环境使用压缩版本
2. **按需加载** - 只加载使用的样式文件
3. **CSS变量** - 减少重复代码
4. **现代布局** - 使用Flexbox/Grid替代float

## 🐛 调试技巧

1. **浏览器开发工具** - 检查样式优先级
2. **CSS变量检查** - 确认变量值是否正确
3. **响应式测试** - 在不同屏幕尺寸下测试
4. **可访问性检查** - 验证颜色对比度和键盘导航
"""
    
    with open('CSS_GUIDE.md', 'w', encoding='utf-8') as f:
        f.write(guide_content)
    
    print("✅ 创建 CSS_GUIDE.md")

def main():
    """主函数"""
    print("🚀 开始优化CSS组织结构...")
    
    # 确保css目录存在
    os.makedirs('css', exist_ok=True)
    
    try:
        # 创建新的CSS架构文件
        create_layout_css()
        create_components_css()  
        create_responsive_css()
        create_master_css()
        create_usage_guide()
        
        print(f"\n✅ CSS组织结构优化完成!")
        
        print(f"\n📋 创建的文件:")
        print(f"  • css/layout.css - 现代化布局系统")
        print(f"  • css/components.css - 通用组件样式")
        print(f"  • css/responsive.css - 响应式设计")
        print(f"  • css/main.css - 主样式文件")
        print(f"  • CSS_GUIDE.md - 使用指南")
        
        print(f"\n🎯 架构特点:")
        print(f"• 模块化CSS组织结构")
        print(f"• 现代化布局系统 (Flexbox/Grid)")
        print(f"• 完整的组件库")
        print(f"• 响应式设计支持")
        print(f"• CSS变量统一管理")
        print(f"• 可访问性优化")
        
        print(f"\n📝 使用方式:")
        print(f"1. 引入主文件: <link rel='stylesheet' href='/css/main.css'>")
        print(f"2. 按需引入页面特定样式")
        print(f"3. 查看 CSS_GUIDE.md 获取详细使用说明")
        
    except Exception as e:
        print(f"❌ 错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()