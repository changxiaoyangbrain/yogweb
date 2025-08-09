# CSS架构使用指南

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
