/* ==========================================================================
   YogWeb 开发调试工具 - Development Debug Tools
   ========================================================================== */

class YogWebDebugger {
    constructor() {
        this.isEnabled = false;
        this.toolbar = null;
        this.perfMonitor = null;
        this.breakpointIndicator = null;
        
        this.init();
    }
    
    init() {
        // 等待DOM加载完成
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => this.setup());
        } else {
            this.setup();
        }
    }
    
    setup() {
        this.createToolbar();
        this.createPerfMonitor();
        this.createBreakpointIndicator();
        this.bindEvents();
        this.loadDebugCSS();
        
        console.log('🔧 YogWeb 调试工具已加载');
        console.log('   按 Ctrl+Shift+D 切换调试模式');
    }
    
    loadDebugCSS() {
        // 动态加载调试CSS
        const link = document.createElement('link');
        link.rel = 'stylesheet';
        link.href = '/css/debug.css';
        document.head.appendChild(link);
    }
    
    createToolbar() {
        this.toolbar = document.createElement('div');
        this.toolbar.className = 'debug-toolbar';
        this.toolbar.innerHTML = `
            <span>🔧 调试工具</span>
            <button data-action="grid">网格</button>
            <button data-action="containers">容器</button>
            <button data-action="flexbox">Flexbox</button>
            <button data-action="grid-layout">Grid</button>
            <button data-action="info">元素信息</button>
            <button data-action="performance">性能监控</button>
            <button data-action="responsive">响应式</button>
            <button data-action="screenshot">截图</button>
            <button data-action="export">导出CSS</button>
        `;
        document.body.appendChild(this.toolbar);
    }
    
    createPerfMonitor() {
        this.perfMonitor = document.createElement('div');
        this.perfMonitor.className = 'perf-monitor';
        document.body.appendChild(this.perfMonitor);
        
        this.updatePerformance();
    }
    
    createBreakpointIndicator() {
        this.breakpointIndicator = document.createElement('div');
        this.breakpointIndicator.className = 'breakpoint-indicator';
        document.body.appendChild(this.breakpointIndicator);
        
        this.updateBreakpoint();
        window.addEventListener('resize', () => this.updateBreakpoint());
    }
    
    bindEvents() {
        // 键盘快捷键
        document.addEventListener('keydown', (e) => {
            if (e.ctrlKey && e.shiftKey && e.key === 'D') {
                e.preventDefault();
                this.toggle();
            }
        });
        
        // 工具栏按钮事件
        this.toolbar.addEventListener('click', (e) => {
            if (e.target.tagName === 'BUTTON') {
                const action = e.target.dataset.action;
                this.handleAction(action, e.target);
            }
        });
        
        // 元素选择器
        document.addEventListener('mouseover', (e) => {
            if (this.isEnabled && document.body.classList.contains('debug-info')) {
                e.target.style.outline = '2px solid red';
            }
        });
        
        document.addEventListener('mouseout', (e) => {
            if (this.isEnabled && document.body.classList.contains('debug-info')) {
                e.target.style.outline = '';
            }
        });
    }
    
    toggle() {
        this.isEnabled = !this.isEnabled;
        
        if (this.isEnabled) {
            this.toolbar.classList.add('show');
            console.log('🔧 调试模式已开启');
        } else {
            this.toolbar.classList.remove('show');
            this.disableAllDebugModes();
            console.log('🔧 调试模式已关闭');
        }
    }
    
    handleAction(action, button) {
        const isActive = button.classList.contains('active');
        
        switch (action) {
            case 'grid':
                this.toggleDebugMode('debug-grid', button);
                break;
            case 'containers':
                this.toggleDebugMode('debug-containers', button);
                break;
            case 'flexbox':
                this.toggleFlexboxDebug(button);
                break;
            case 'grid-layout':
                this.toggleGridDebug(button);
                break;
            case 'info':
                this.toggleDebugMode('debug-info', button);
                break;
            case 'performance':
                this.togglePerformanceMonitor(button);
                break;
            case 'responsive':
                this.toggleBreakpointIndicator(button);
                break;
            case 'screenshot':
                this.takeScreenshot();
                break;
            case 'export':
                this.exportCSS();
                break;
        }
    }
    
    toggleDebugMode(className, button) {
        const isActive = button.classList.contains('active');
        
        if (isActive) {
            document.body.classList.remove(className);
            button.classList.remove('active');
        } else {
            document.body.classList.add(className);
            button.classList.add('active');
        }
    }
    
    toggleFlexboxDebug(button) {
        const flexElements = document.querySelectorAll('.flex, [style*="display: flex"], [style*="display:flex"]');
        const isActive = button.classList.contains('active');
        
        if (isActive) {
            flexElements.forEach(el => el.classList.remove('debug-flexbox'));
            button.classList.remove('active');
        } else {
            flexElements.forEach(el => el.classList.add('debug-flexbox'));
            button.classList.add('active');
        }
    }
    
    toggleGridDebug(button) {
        const gridElements = document.querySelectorAll('.grid, [style*="display: grid"], [style*="display:grid"]');
        const isActive = button.classList.contains('active');
        
        if (isActive) {
            gridElements.forEach(el => el.classList.remove('debug-grid-layout'));
            button.classList.remove('active');
        } else {
            gridElements.forEach(el => el.classList.add('debug-grid-layout'));
            button.classList.add('active');
        }
    }
    
    togglePerformanceMonitor(button) {
        const isActive = button.classList.contains('active');
        
        if (isActive) {
            this.perfMonitor.classList.remove('show');
            button.classList.remove('active');
        } else {
            this.perfMonitor.classList.add('show');
            button.classList.add('active');
            this.startPerformanceMonitoring();
        }
    }
    
    toggleBreakpointIndicator(button) {
        const isActive = button.classList.contains('active');
        
        if (isActive) {
            this.breakpointIndicator.classList.remove('show');
            button.classList.remove('active');
        } else {
            this.breakpointIndicator.classList.add('show');
            button.classList.add('active');
        }
    }
    
    updatePerformance() {
        if (typeof performance !== 'undefined') {
            const memory = performance.memory ? 
                `内存: ${(performance.memory.usedJSHeapSize / 1024 / 1024).toFixed(1)}MB` : '';
            const timing = performance.timing;
            const loadTime = timing.loadEventEnd - timing.navigationStart;
            
            this.perfMonitor.innerHTML = `
                ⚡ 加载: ${loadTime}ms | ${memory} | ${document.querySelectorAll('*').length} 元素
            `;
        }
    }
    
    updateBreakpoint() {
        const width = window.innerWidth;
        let size = 'mobile';
        
        if (width >= 1281) size = 'wide';
        else if (width >= 1025) size = 'desktop';
        else if (width >= 641) size = 'tablet';
        
        this.breakpointIndicator.innerHTML = `
            📐 ${width}px (${size})
        `;
    }
    
    startPerformanceMonitoring() {
        setInterval(() => {
            this.updatePerformance();
        }, 1000);
    }
    
    disableAllDebugModes() {
        const debugClasses = ['debug-grid', 'debug-containers', 'debug-info'];
        debugClasses.forEach(cls => document.body.classList.remove(cls));
        
        document.querySelectorAll('.debug-flexbox').forEach(el => el.classList.remove('debug-flexbox'));
        document.querySelectorAll('.debug-grid-layout').forEach(el => el.classList.remove('debug-grid-layout'));
        
        this.perfMonitor.classList.remove('show');
        this.breakpointIndicator.classList.remove('show');
        
        // 重置所有工具栏按钮状态
        this.toolbar.querySelectorAll('button').forEach(btn => btn.classList.remove('active'));
    }
    
    takeScreenshot() {
        // 使用html2canvas或类似库截图
        console.log('📸 截图功能 - 请安装html2canvas库');
        
        // 简单的窗口截图替代方案
        if (navigator.mediaDevices && navigator.mediaDevices.getDisplayMedia) {
            navigator.mediaDevices.getDisplayMedia({ video: true })
                .then(stream => {
                    const video = document.createElement('video');
                    video.srcObject = stream;
                    video.play();
                    
                    video.addEventListener('loadedmetadata', () => {
                        const canvas = document.createElement('canvas');
                        canvas.width = video.videoWidth;
                        canvas.height = video.videoHeight;
                        
                        const ctx = canvas.getContext('2d');
                        ctx.drawImage(video, 0, 0);
                        
                        stream.getTracks().forEach(track => track.stop());
                        
                        // 下载截图
                        canvas.toBlob(blob => {
                            const url = URL.createObjectURL(blob);
                            const a = document.createElement('a');
                            a.href = url;
                            a.download = `yogweb-screenshot-${Date.now()}.png`;
                            a.click();
                            URL.revokeObjectURL(url);
                        });
                    });
                });
        }
    }
    
    exportCSS() {
        // 导出当前页面使用的CSS
        const styles = [];
        
        for (let sheet of document.styleSheets) {
            try {
                if (sheet.href && sheet.href.includes('/css/')) {
                    styles.push(`/* ${sheet.href} */`);
                    for (let rule of sheet.cssRules) {
                        styles.push(rule.cssText);
                    }
                }
            } catch (e) {
                console.warn('无法读取CSS规则:', e);
            }
        }
        
        const cssContent = styles.join('\n\n');
        const blob = new Blob([cssContent], { type: 'text/css' });
        const url = URL.createObjectURL(blob);
        
        const a = document.createElement('a');
        a.href = url;
        a.download = `yogweb-exported-styles-${Date.now()}.css`;
        a.click();
        
        URL.revokeObjectURL(url);
        console.log('📁 CSS已导出');
    }
}

// 初始化调试器
window.yogwebDebugger = new YogWebDebugger();

// 全局调试函数
window.debug = {
    highlight: (selector) => {
        document.querySelectorAll(selector).forEach(el => {
            el.classList.add('highlight-element');
            setTimeout(() => el.classList.remove('highlight-element'), 3000);
        });
    },
    
    measure: (selector) => {
        document.querySelectorAll(selector).forEach(el => {
            const rect = el.getBoundingClientRect();
            el.dataset.width = Math.round(rect.width);
            el.dataset.height = Math.round(rect.height);
            el.classList.add('measure-element');
            setTimeout(() => el.classList.remove('measure-element'), 5000);
        });
    },
    
    inspect: (selector) => {
        const el = document.querySelector(selector);
        if (el) {
            const styles = getComputedStyle(el);
            console.group(`🔍 检查元素: ${selector}`);
            console.log('元素:', el);
            console.log('计算样式:', styles);
            console.log('盒模型:', {
                width: styles.width,
                height: styles.height,
                padding: styles.padding,
                margin: styles.margin,
                border: styles.border
            });
            console.log('布局:', {
                display: styles.display,
                position: styles.position,
                flexDirection: styles.flexDirection,
                gridTemplate: styles.gridTemplateColumns
            });
            console.groupEnd();
        }
    }
};

console.log('🔧 YogWeb 调试工具已加载');
console.log('   window.debug.highlight(".selector") - 高亮元素');
console.log('   window.debug.measure(".selector") - 测量尺寸');
console.log('   window.debug.inspect(".selector") - 检查样式');

// ============================================================================
// 页面返回顶部功能已禁用
// ============================================================================
