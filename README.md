# YogWeb - 酸奶研究资料库

中文本地化的酸奶研究静态网站，准备部署到 Cloudflare Pages。

## 项目特点

- 完整的中文本地化内容
- 移除所有外部依赖和第三方服务
- 现代化响应式设计
- 优化的页面性能
- 2x2 网格布局的首页卡片系统
- 无障碍访问支持

## 部署到 Cloudflare Pages

1. Fork 此仓库或直接从 GitHub 导入
2. 在 Cloudflare Pages 中创建新项目
3. 连接到此 GitHub 仓库
4. 构建设置：
   - 构建命令：留空（静态站点）
   - 构建输出目录：`/`（根目录）
5. 部署完成后即可访问

## 文件结构

- `index.html` - 主页
- `css/` - 样式文件
- `js/` - JavaScript 文件
- `images/` - 图片资源
- `laboratory/` - 实验室内容
- `style/` - 样式相关内容
- `_headers` - Cloudflare Pages 缓存配置

## 技术栈

- HTML5 + CSS3
- JavaScript (ES6+)
- 响应式设计
- CSS Grid/Flexbox 布局

---

Generated with [Claude Code](https://claude.ai/code)