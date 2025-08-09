#!/usr/bin/env python3
"""
现代CSS特性添加脚本 - 为网站添加现代CSS功能
作者: Claude Code
"""

import os
import sys

def create_animations_css():
    """创建动画和过渡效果文件"""
    animations_content = """@charset "utf-8";

/* ==========================================================================
   动画和过渡效果 - Animations & Transitions
   ========================================================================== */

/* 基础过渡效果 */
.transition {
    transition: all 0.3s ease;
}

.transition-fast {
    transition: all 0.15s ease;
}

.transition-slow {
    transition: all 0.5s ease;
}

.transition-colors {
    transition: color 0.3s ease, background-color 0.3s ease, border-color 0.3s ease;
}

.transition-transform {
    transition: transform 0.3s ease;
}

.transition-opacity {
    transition: opacity 0.3s ease;
}

/* 悬停效果 */
.hover-lift:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.hover-scale:hover {
    transform: scale(1.05);
}

.hover-rotate:hover {
    transform: rotate(5deg);
}

.hover-fade:hover {
    opacity: 0.8;
}

.hover-glow:hover {
    box-shadow: 0 0 20px rgba(0, 5, 63, 0.3);
}

/* 进入动画 */
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes slideInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes slideInDown {
    from {
        opacity: 0;
        transform: translateY(-30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes slideInLeft {
    from {
        opacity: 0;
        transform: translateX(-30px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes slideInRight {
    from {
        opacity: 0;
        transform: translateX(30px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes scaleIn {
    from {
        opacity: 0;
        transform: scale(0.8);
    }
    to {
        opacity: 1;
        transform: scale(1);
    }
}

@keyframes bounceIn {
    0% {
        opacity: 0;
        transform: scale(0.3);
    }
    50% {
        opacity: 1;
        transform: scale(1.05);
    }
    70% {
        transform: scale(0.9);
    }
    100% {
        opacity: 1;
        transform: scale(1);
    }
}

/* 加载动画 */
@keyframes spin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

@keyframes pulse {
    0%, 100% {
        opacity: 1;
    }
    50% {
        opacity: 0.5;
    }
}

@keyframes bounce {
    0%, 20%, 53%, 80%, 100% {
        animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
        transform: translateY(0);
    }
    40%, 43% {
        animation-timing-function: cubic-bezier(0.755, 0.05, 0.855, 0.06);
        transform: translateY(-30px);
    }
    70% {
        animation-timing-function: cubic-bezier(0.755, 0.05, 0.855, 0.06);
        transform: translateY(-15px);
    }
    90% {
        transform: translateY(-4px);
    }
}

/* 无限动画 */
@keyframes float {
    0%, 100% {
        transform: translateY(0px);
    }
    50% {
        transform: translateY(-10px);
    }
}

@keyframes wiggle {
    0%, 7% {
        transform: rotateZ(0);
    }
    15% {
        transform: rotateZ(-15deg);
    }
    20% {
        transform: rotateZ(10deg);
    }
    25% {
        transform: rotateZ(-10deg);
    }
    30% {
        transform: rotateZ(6deg);
    }
    35% {
        transform: rotateZ(-4deg);
    }
    40%, 100% {
        transform: rotateZ(0);
    }
}

/* 动画类 */
.animate-fade-in {
    animation: fadeIn 0.6s ease-out;
}

.animate-slide-in-up {
    animation: slideInUp 0.6s ease-out;
}

.animate-slide-in-down {
    animation: slideInDown 0.6s ease-out;
}

.animate-slide-in-left {
    animation: slideInLeft 0.6s ease-out;
}

.animate-slide-in-right {
    animation: slideInRight 0.6s ease-out;
}

.animate-scale-in {
    animation: scaleIn 0.6s ease-out;
}

.animate-bounce-in {
    animation: bounceIn 0.6s ease-out;
}

.animate-spin {
    animation: spin 1s linear infinite;
}

.animate-pulse {
    animation: pulse 2s ease-in-out infinite;
}

.animate-bounce {
    animation: bounce 1s infinite;
}

.animate-float {
    animation: float 3s ease-in-out infinite;
}

.animate-wiggle {
    animation: wiggle 1s ease-in-out;
}

/* 延迟类 */
.animate-delay-100 { animation-delay: 0.1s; }
.animate-delay-200 { animation-delay: 0.2s; }
.animate-delay-300 { animation-delay: 0.3s; }
.animate-delay-500 { animation-delay: 0.5s; }
.animate-delay-700 { animation-delay: 0.7s; }
.animate-delay-1000 { animation-delay: 1s; }

/* 持续时间类 */
.animate-duration-75 { animation-duration: 75ms; }
.animate-duration-100 { animation-duration: 100ms; }
.animate-duration-150 { animation-duration: 150ms; }
.animate-duration-200 { animation-duration: 200ms; }
.animate-duration-300 { animation-duration: 300ms; }
.animate-duration-500 { animation-duration: 500ms; }
.animate-duration-700 { animation-duration: 700ms; }
.animate-duration-1000 { animation-duration: 1000ms; }

/* 页面切换动画 */
.page-transition {
    opacity: 0;
    transform: translateY(20px);
    animation: slideInUp 0.8s ease-out forwards;
}

/* 渐进式加载动画 */
.progressive-load > * {
    opacity: 0;
    transform: translateY(30px);
    animation: slideInUp 0.6s ease-out forwards;
}

.progressive-load > *:nth-child(1) { animation-delay: 0.1s; }
.progressive-load > *:nth-child(2) { animation-delay: 0.2s; }
.progressive-load > *:nth-child(3) { animation-delay: 0.3s; }
.progressive-load > *:nth-child(4) { animation-delay: 0.4s; }
.progressive-load > *:nth-child(5) { animation-delay: 0.5s; }
.progressive-load > *:nth-child(6) { animation-delay: 0.6s; }
.progressive-load > *:nth-child(7) { animation-delay: 0.7s; }
.progressive-load > *:nth-child(8) { animation-delay: 0.8s; }

/* 交互动画 */
.click-animation:active {
    transform: scale(0.95);
}

.button-ripple {
    position: relative;
    overflow: hidden;
}

.button-ripple:before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 0;
    height: 0;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.3);
    transform: translate(-50%, -50%);
    transition: width 0.3s, height 0.3s;
}

.button-ripple:active:before {
    width: 200px;
    height: 200px;
}

/* 视差滚动效果 */
.parallax {
    background-attachment: fixed;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
}

/* 性能优化 */
.animate-gpu {
    transform: translate3d(0, 0, 0);
    backface-visibility: hidden;
    perspective: 1000px;
}

/* 减少动画偏好支持 */
@media (prefers-reduced-motion: reduce) {
    .animate-fade-in,
    .animate-slide-in-up,
    .animate-slide-in-down,
    .animate-slide-in-left,
    .animate-slide-in-right,
    .animate-scale-in,
    .animate-bounce-in {
        animation: none;
        opacity: 1;
        transform: none;
    }
    
    .hover-lift:hover,
    .hover-scale:hover,
    .hover-rotate:hover {
        transform: none;
    }
    
    .animate-spin,
    .animate-pulse,
    .animate-bounce,
    .animate-float,
    .animate-wiggle {
        animation-duration: 0.01ms;
        animation-iteration-count: 1;
    }
}
"""
    
    with open('css/animations.css', 'w', encoding='utf-8') as f:
        f.write(animations_content)
    
    print("✅ 创建 css/animations.css")

def create_modern_features_css():
    """创建现代CSS特性文件"""
    modern_content = """@charset "utf-8";

/* ==========================================================================
   现代CSS特性 - Modern CSS Features
   ========================================================================== */

/* CSS自定义属性 (CSS Variables) 扩展 */
:root {
    /* 渐变色系统 */
    --gradient-primary: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    --gradient-secondary: linear-gradient(45deg, var(--secondary-color), #FFD700);
    --gradient-neutral: linear-gradient(to right, #f8f9fa, #e9ecef);
    --gradient-dark: linear-gradient(135deg, #2c3e50, #3498db);
    
    /* 阴影系统 */
    --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);
    --shadow-md: 0 3px 6px rgba(0, 0, 0, 0.15), 0 2px 4px rgba(0, 0, 0, 0.12);
    --shadow-lg: 0 10px 20px rgba(0, 0, 0, 0.15), 0 3px 6px rgba(0, 0, 0, 0.10);
    --shadow-xl: 0 20px 40px rgba(0, 0, 0, 0.15), 0 5px 10px rgba(0, 0, 0, 0.12);
    
    /* 边框圆角系统 */
    --radius-sm: 0.25rem;
    --radius-md: 0.375rem;
    --radius-lg: 0.5rem;
    --radius-xl: 0.75rem;
    --radius-2xl: 1rem;
    --radius-3xl: 1.5rem;
    --radius-full: 9999px;
    
    /* 间距系统扩展 */
    --space-px: 1px;
    --space-0: 0;
    --space-1: 0.25rem;
    --space-2: 0.5rem;
    --space-3: 0.75rem;
    --space-4: 1rem;
    --space-5: 1.25rem;
    --space-6: 1.5rem;
    --space-8: 2rem;
    --space-10: 2.5rem;
    --space-12: 3rem;
    --space-16: 4rem;
    --space-20: 5rem;
    
    /* 字体大小系统 */
    --text-xs: 0.75rem;
    --text-sm: 0.875rem;
    --text-base: 1rem;
    --text-lg: 1.125rem;
    --text-xl: 1.25rem;
    --text-2xl: 1.5rem;
    --text-3xl: 1.875rem;
    --text-4xl: 2.25rem;
    --text-5xl: 3rem;
    
    /* 行高系统 */
    --leading-tight: 1.25;
    --leading-snug: 1.375;
    --leading-normal: 1.5;
    --leading-relaxed: 1.625;
    --leading-loose: 2;
    
    /* Z-index系统 */
    --z-0: 0;
    --z-10: 10;
    --z-20: 20;
    --z-30: 30;
    --z-40: 40;
    --z-50: 50;
    --z-auto: auto;
}

/* CSS Grid 高级布局 */
.grid-auto-fit {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: var(--space-4);
}

.grid-auto-fill {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: var(--space-4);
}

/* 复杂Grid模板 */
.grid-layout-1 {
    display: grid;
    grid-template-areas: 
        "header header header"
        "sidebar main main"
        "footer footer footer";
    grid-template-columns: 250px 1fr 1fr;
    grid-template-rows: auto 1fr auto;
    min-height: 100vh;
    gap: var(--space-4);
}

.grid-header { grid-area: header; }
.grid-sidebar { grid-area: sidebar; }
.grid-main { grid-area: main; }
.grid-footer { grid-area: footer; }

/* CSS Container Queries (现代浏览器支持) */
@supports (container-type: inline-size) {
    .container-card {
        container-type: inline-size;
    }
    
    @container (min-width: 400px) {
        .responsive-card {
            display: grid;
            grid-template-columns: 1fr 2fr;
            gap: var(--space-4);
        }
    }
}

/* 现代滤镜效果 */
.filter-blur-sm { filter: blur(4px); }
.filter-blur { filter: blur(8px); }
.filter-blur-lg { filter: blur(12px); }
.filter-brightness-50 { filter: brightness(0.5); }
.filter-brightness-75 { filter: brightness(0.75); }
.filter-brightness-125 { filter: brightness(1.25); }
.filter-contrast-125 { filter: contrast(1.25); }
.filter-grayscale { filter: grayscale(100%); }
.filter-sepia { filter: sepia(100%); }
.filter-hue-rotate-90 { filter: hue-rotate(90deg); }
.filter-invert { filter: invert(100%); }
.filter-saturate-150 { filter: saturate(1.5); }

/* 组合滤镜效果 */
.filter-vintage {
    filter: sepia(50%) contrast(1.2) brightness(0.8);
}

.filter-cool {
    filter: hue-rotate(180deg) saturate(1.2);
}

.filter-warm {
    filter: hue-rotate(-30deg) saturate(1.1) brightness(1.1);
}

/* 背景混合模式 */
.mix-blend-multiply { mix-blend-mode: multiply; }
.mix-blend-screen { mix-blend-mode: screen; }
.mix-blend-overlay { mix-blend-mode: overlay; }
.mix-blend-darken { mix-blend-mode: darken; }
.mix-blend-lighten { mix-blend-mode: lighten; }
.mix-blend-color-dodge { mix-blend-mode: color-dodge; }
.mix-blend-color-burn { mix-blend-mode: color-burn; }

/* CSS渐变背景 */
.bg-gradient-primary {
    background: var(--gradient-primary);
}

.bg-gradient-secondary {
    background: var(--gradient-secondary);
}

.bg-gradient-radial {
    background: radial-gradient(circle, var(--primary-color) 0%, var(--secondary-color) 100%);
}

.bg-gradient-conic {
    background: conic-gradient(from 0deg, var(--primary-color), var(--secondary-color), var(--primary-color));
}

/* 现代阴影系统 */
.shadow-sm { box-shadow: var(--shadow-sm); }
.shadow-md { box-shadow: var(--shadow-md); }
.shadow-lg { box-shadow: var(--shadow-lg); }
.shadow-xl { box-shadow: var(--shadow-xl); }
.shadow-inner { box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1); }
.shadow-outline { box-shadow: 0 0 0 3px rgba(0, 5, 63, 0.1); }
.shadow-none { box-shadow: none; }

/* 彩色阴影 */
.shadow-primary { box-shadow: 0 4px 14px 0 rgba(0, 5, 63, 0.39); }
.shadow-secondary { box-shadow: 0 4px 14px 0 rgba(194, 125, 61, 0.39); }

/* 高级圆角 */
.rounded-none { border-radius: 0; }
.rounded-sm { border-radius: var(--radius-sm); }
.rounded { border-radius: var(--radius-md); }
.rounded-lg { border-radius: var(--radius-lg); }
.rounded-xl { border-radius: var(--radius-xl); }
.rounded-2xl { border-radius: var(--radius-2xl); }
.rounded-3xl { border-radius: var(--radius-3xl); }
.rounded-full { border-radius: var(--radius-full); }

/* 不规则圆角 */
.rounded-tl-lg { border-top-left-radius: var(--radius-lg); }
.rounded-tr-lg { border-top-right-radius: var(--radius-lg); }
.rounded-bl-lg { border-bottom-left-radius: var(--radius-lg); }
.rounded-br-lg { border-bottom-right-radius: var(--radius-lg); }
.rounded-t-lg { border-top-left-radius: var(--radius-lg); border-top-right-radius: var(--radius-lg); }
.rounded-b-lg { border-bottom-left-radius: var(--radius-lg); border-bottom-right-radius: var(--radius-lg); }

/* CSS Clip Path */
.clip-triangle {
    clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
}

.clip-diamond {
    clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);
}

.clip-hexagon {
    clip-path: polygon(30% 0%, 70% 0%, 100% 50%, 70% 100%, 30% 100%, 0% 50%);
}

.clip-arrow {
    clip-path: polygon(0% 20%, 60% 20%, 60% 0%, 100% 50%, 60% 100%, 60% 80%, 0% 80%);
}

/* CSS Variables 深色模式切换 */
.theme-dark {
    --primary-color: #4285f4;
    --secondary-color: #ff9800;
    --text-primary: #ffffff;
    --text-secondary: #b0b0b0;
    --bg-primary: #121212;
    --bg-secondary: #1e1e1e;
    --border-color: #333333;
}

/* 现代表单元素 */
.form-floating {
    position: relative;
}

.form-floating .form-input {
    padding-top: 1.625rem;
    padding-bottom: 0.625rem;
}

.form-floating .form-label {
    position: absolute;
    top: 0;
    left: 0.75rem;
    height: 100%;
    padding: 1rem 0.25rem 0 0;
    pointer-events: none;
    border: 1px solid transparent;
    transform-origin: 0 0;
    transition: opacity 0.1s ease-in-out, transform 0.1s ease-in-out;
}

.form-floating .form-input:focus ~ .form-label,
.form-floating .form-input:not(:placeholder-shown) ~ .form-label {
    opacity: 0.65;
    transform: scale(0.85) translateY(-0.5rem) translateX(0.15rem);
}

/* CSS逻辑属性 */
.margin-inline-4 {
    margin-inline-start: var(--space-4);
    margin-inline-end: var(--space-4);
}

.padding-block-2 {
    padding-block-start: var(--space-2);
    padding-block-end: var(--space-2);
}

/* CSS Scroll Snap */
.scroll-container {
    scroll-snap-type: x mandatory;
    overflow-x: scroll;
    display: flex;
}

.scroll-item {
    scroll-snap-align: center;
    flex-shrink: 0;
}

/* 现代文本效果 */
.text-gradient {
    background: var(--gradient-primary);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.text-stroke {
    -webkit-text-stroke: 2px var(--primary-color);
    -webkit-text-fill-color: transparent;
}

.text-shadow-sm { text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1); }
.text-shadow { text-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24); }
.text-shadow-lg { text-shadow: 0 4px 8px rgba(0, 0, 0, 0.12), 0 2px 4px rgba(0, 0, 0, 0.08); }

/* CSS Backdrop Filter */
.backdrop-blur {
    backdrop-filter: blur(8px);
    background: rgba(255, 255, 255, 0.8);
}

.backdrop-blur-sm {
    backdrop-filter: blur(4px);
    background: rgba(255, 255, 255, 0.9);
}

.backdrop-blur-lg {
    backdrop-filter: blur(16px);
    background: rgba(255, 255, 255, 0.7);
}

/* CSS Sticky定位 */
.sticky-top {
    position: sticky;
    top: 0;
    z-index: var(--z-20);
}

.sticky-bottom {
    position: sticky;
    bottom: 0;
    z-index: var(--z-20);
}

/* CSS aspect-ratio (现代浏览器) */
.aspect-square { aspect-ratio: 1/1; }
.aspect-video { aspect-ratio: 16/9; }
.aspect-photo { aspect-ratio: 4/3; }
.aspect-golden { aspect-ratio: 1.618/1; }

/* Fallback for older browsers */
@supports not (aspect-ratio: 1/1) {
    .aspect-square {
        position: relative;
        padding-bottom: 100%;
        height: 0;
    }
    
    .aspect-square > * {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }
    
    .aspect-video {
        position: relative;
        padding-bottom: 56.25%;
        height: 0;
    }
    
    .aspect-video > * {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }
}

/* CSS Gap替代方案 */
@supports not (gap: 1rem) {
    .flex-gap-4 > * + * {
        margin-left: var(--space-4);
    }
    
    .flex-column.flex-gap-4 > * + * {
        margin-left: 0;
        margin-top: var(--space-4);
    }
}
"""
    
    with open('css/modern-features.css', 'w', encoding='utf-8') as f:
        f.write(modern_content)
    
    print("✅ 创建 css/modern-features.css")

def update_main_css():
    """更新主CSS文件以包含新特性"""
    main_css_additions = """
/* 现代特性文件 */
@import url('animations.css');        /* 动画和过渡效果 */
@import url('modern-features.css');   /* 现代CSS特性 */
"""
    
    # 读取现有的main.css文件
    with open('css/main.css', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 在组件系统部分之后添加现代特性
    updated_content = content.replace(
        '/* 组件系统 */\n@import url(\'components.css\');     /* 通用组件样式 */\n@import url(\'utilities.css\');      /* 实用工具类 */',
        '/* 组件系统 */\n@import url(\'components.css\');     /* 通用组件样式 */\n@import url(\'utilities.css\');      /* 实用工具类 */' + main_css_additions
    )
    
    with open('css/main.css', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("✅ 更新 css/main.css")

def create_demo_html():
    """创建现代特性演示页面"""
    demo_content = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>现代CSS特性演示 - YogWeb</title>
    
    <!-- 引入现代化CSS -->
    <link rel="stylesheet" href="/css/main.css">
    
    <style>
        .demo-section {
            margin-bottom: 3rem;
            padding: 2rem;
            background: white;
            border-radius: var(--radius-lg);
            box-shadow: var(--shadow-md);
        }
        
        .demo-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1rem;
            margin: 1rem 0;
        }
        
        .demo-item {
            padding: 1rem;
            background: var(--gradient-neutral);
            border-radius: var(--radius-md);
            text-align: center;
        }
    </style>
</head>
<body class="bg-gray-50 font-ja">
    <!-- 页面过渡动画 -->
    <div class="page-transition">
        
        <!-- 跳转链接 -->
        <a href="#main-content" class="skip-to-main">跳转到主内容</a>
        
        <!-- 头部 -->
        <header class="sticky-top backdrop-blur p-4 mb-8">
            <div class="container">
                <h1 class="text-gradient text-3xl mb-0">现代CSS特性演示</h1>
                <p class="text-gray-600">YogWeb 现代化样式系统</p>
            </div>
        </header>
        
        <main id="main-content" class="container">
            
            <!-- 动画效果演示 -->
            <section class="demo-section animate-fade-in">
                <h2 class="text-2xl mb-4">动画效果</h2>
                <div class="progressive-load">
                    <div class="demo-item hover-lift transition">悬停上升效果</div>
                    <div class="demo-item hover-scale transition">悬停缩放效果</div>
                    <div class="demo-item hover-glow transition">悬停发光效果</div>
                    <div class="demo-item animate-pulse">脉冲动画</div>
                    <div class="demo-item animate-float">浮动动画</div>
                    <div class="demo-item animate-bounce">弹跳动画</div>
                </div>
            </section>
            
            <!-- 布局系统演示 -->
            <section class="demo-section animate-slide-in-up animate-delay-200">
                <h2 class="text-2xl mb-4">布局系统</h2>
                
                <h3 class="text-lg mb-2">Flexbox布局</h3>
                <div class="flex flex-center gap-2 mb-4 p-4 bg-blue-50 rounded">
                    <div class="card p-2">项目1</div>
                    <div class="card p-2">项目2</div>
                    <div class="card p-2">项目3</div>
                </div>
                
                <h3 class="text-lg mb-2">Grid自适应布局</h3>
                <div class="grid-auto-fit mb-4">
                    <div class="card">自适应卡片1</div>
                    <div class="card">自适应卡片2</div>
                    <div class="card">自适应卡片3</div>
                    <div class="card">自适应卡片4</div>
                </div>
            </section>
            
            <!-- 现代特性演示 -->
            <section class="demo-section animate-slide-in-right animate-delay-300">
                <h2 class="text-2xl mb-4">现代CSS特性</h2>
                
                <!-- 渐变和滤镜 -->
                <div class="demo-grid">
                    <div class="demo-item bg-gradient-primary text-white">主色渐变</div>
                    <div class="demo-item bg-gradient-secondary text-white">辅色渐变</div>
                    <div class="demo-item filter-vintage">复古滤镜</div>
                    <div class="demo-item filter-cool">冷色滤镜</div>
                </div>
                
                <!-- 阴影系统 -->
                <div class="demo-grid mt-4">
                    <div class="demo-item shadow-sm">小阴影</div>
                    <div class="demo-item shadow-md">中阴影</div>
                    <div class="demo-item shadow-lg">大阴影</div>
                    <div class="demo-item shadow-primary">彩色阴影</div>
                </div>
                
                <!-- 形状裁剪 -->
                <div class="demo-grid mt-4">
                    <div class="demo-item clip-triangle bg-gradient-primary" style="height: 100px;">三角形</div>
                    <div class="demo-item clip-diamond bg-gradient-secondary" style="height: 100px;">钻石形</div>
                    <div class="demo-item clip-hexagon bg-gradient-primary" style="height: 100px;">六边形</div>
                    <div class="demo-item clip-arrow bg-gradient-secondary" style="height: 100px;">箭头形</div>
                </div>
            </section>
            
            <!-- 组件演示 -->
            <section class="demo-section animate-scale-in animate-delay-500">
                <h2 class="text-2xl mb-4">组件系统</h2>
                
                <!-- 按钮组 -->
                <div class="flex flex-wrap gap-2 mb-4">
                    <button class="btn btn-primary hover-lift transition click-animation">主要按钮</button>
                    <button class="btn btn-secondary hover-lift transition">次要按钮</button>
                    <button class="btn btn-outline hover-lift transition">轮廓按钮</button>
                    <button class="btn btn-primary btn-small">小按钮</button>
                    <button class="btn btn-primary btn-large">大按钮</button>
                </div>
                
                <!-- 徽章和标签 -->
                <div class="flex flex-wrap gap-2 mb-4">
                    <span class="badge">默认徽章</span>
                    <span class="badge badge-primary">主要徽章</span>
                    <span class="badge badge-success">成功徽章</span>
                    <span class="badge badge-warning">警告徽章</span>
                    <span class="badge badge-error">错误徽章</span>
                </div>
                
                <!-- 提示框 -->
                <div class="alert alert-info mb-2">这是一个信息提示框</div>
                <div class="alert alert-success mb-2">这是一个成功提示框</div>
                <div class="alert alert-warning mb-2">这是一个警告提示框</div>
                <div class="alert alert-error">这是一个错误提示框</div>
            </section>
            
            <!-- 响应式演示 -->
            <section class="demo-section animate-bounce-in animate-delay-700">
                <h2 class="text-2xl mb-4">响应式设计</h2>
                <div class="grid grid-cols-1 tablet:grid-cols-2 desktop:grid-cols-3 gap-4">
                    <div class="card">
                        <h3>响应式卡片1</h3>
                        <p>在移动端显示为单列，平板端2列，桌面端3列</p>
                    </div>
                    <div class="card">
                        <h3>响应式卡片2</h3>
                        <p>使用现代CSS Grid实现</p>
                    </div>
                    <div class="card hidden-mobile">
                        <h3>桌面端专用</h3>
                        <p>这个卡片只在桌面端显示</p>
                    </div>
                </div>
                
                <div class="mt-4 p-4 bg-yellow-50 rounded hidden-desktop">
                    <p class="text-center"><strong>移动端提示</strong><br>这个内容只在移动端显示</p>
                </div>
            </section>
            
            <!-- 现代表单演示 -->
            <section class="demo-section">
                <h2 class="text-2xl mb-4">现代表单</h2>
                <form>
                    <div class="form-floating mb-4">
                        <input type="text" class="form-input input" id="floating-name" placeholder="姓名">
                        <label for="floating-name" class="form-label">请输入您的姓名</label>
                    </div>
                    
                    <div class="input-group mb-4">
                        <label for="email" class="input-label">邮箱地址</label>
                        <input type="email" id="email" class="input" placeholder="example@example.com">
                    </div>
                    
                    <div class="flex gap-2">
                        <button type="submit" class="btn btn-primary button-ripple">提交表单</button>
                        <button type="reset" class="btn btn-outline">重置</button>
                    </div>
                </form>
            </section>
            
            <!-- 滚动捕捉演示 -->
            <section class="demo-section">
                <h2 class="text-2xl mb-4">滚动捕捉</h2>
                <div class="scroll-container gap-4 p-4 bg-gray-100 rounded">
                    <div class="scroll-item card min-w-64">滚动项目1</div>
                    <div class="scroll-item card min-w-64">滚动项目2</div>
                    <div class="scroll-item card min-w-64">滚动项目3</div>
                    <div class="scroll-item card min-w-64">滚动项目4</div>
                    <div class="scroll-item card min-w-64">滚动项目5</div>
                </div>
                <p class="text-sm text-gray-600 mt-2">左右滑动查看滚动捕捉效果</p>
            </section>
            
        </main>
        
        <!-- 底部 -->
        <footer class="bg-gray-800 text-white p-8 mt-12">
            <div class="container text-center">
                <p>YogWeb - 现代化酸奶研究网站 © 2024</p>
                <p class="text-sm text-gray-400 mt-2">使用现代CSS技术构建</p>
            </div>
        </footer>
        
    </div>
    
    <!-- 深色模式切换按钮 -->
    <button class="fixed bottom-4 right-4 btn btn-primary rounded-full p-3 shadow-lg z-50" 
            onclick="toggleDarkMode()" 
            aria-label="切换深色模式">
        🌙
    </button>
    
    <script>
        function toggleDarkMode() {
            document.body.classList.toggle('theme-dark');
            const button = document.querySelector('button[onclick="toggleDarkMode()"]');
            button.textContent = document.body.classList.contains('theme-dark') ? '☀️' : '🌙';
        }
        
        // 页面加载完成后触发渐进式加载动画
        document.addEventListener('DOMContentLoaded', function() {
            const progressiveElements = document.querySelectorAll('.progressive-load');
            progressiveElements.forEach(el => {
                el.classList.add('loaded');
            });
        });
    </script>
</body>
</html>"""
    
    with open('modern_features_demo.html', 'w', encoding='utf-8') as f:
        f.write(demo_content)
    
    print("✅ 创建 modern_features_demo.html")

def main():
    """主函数"""
    print("🚀 开始添加现代CSS特性...")
    
    try:
        # 创建现代CSS特性文件
        create_animations_css()
        create_modern_features_css()
        update_main_css()
        create_demo_html()
        
        print(f"\n✅ 现代CSS特性添加完成!")
        
        print(f"\n📋 新增功能:")
        print(f"  • 完整的动画系统 (淡入、滑动、缩放等)")
        print(f"  • 现代CSS特性 (Grid、Variables、Filters等)")
        print(f"  • 高级布局系统 (Container Queries、Auto-fit)")
        print(f"  • 视觉效果 (渐变、阴影、裁剪路径)")
        print(f"  • 交互动画 (悬停、点击、过渡)")
        print(f"  • 无障碍支持 (减少动画偏好)")
        
        print(f"\n📝 新增文件:")
        print(f"  • css/animations.css - 动画和过渡效果")
        print(f"  • css/modern-features.css - 现代CSS特性")
        print(f"  • modern_features_demo.html - 特性演示页面")
        
        print(f"\n🎯 特性亮点:")
        print(f"• CSS变量系统完整升级")
        print(f"• 支持深色模式切换")
        print(f"• Container Queries现代响应式")
        print(f"• CSS Grid高级布局模式")
        print(f"• 滤镜和混合模式效果")
        print(f"• 滚动捕捉和粘性定位")
        print(f"• 浏览器兼容性回退")
        
        print(f"\n🔗 测试方式:")
        print(f"1. python -m http.server 8189")
        print(f"2. 访问 http://localhost:8189/modern_features_demo.html")
        print(f"3. 测试响应式和动画效果")
        
    except Exception as e:
        print(f"❌ 错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()