// 返回页首功能
(function() {
    'use strict';
    
    // 等待DOM加载完成
    document.addEventListener('DOMContentLoaded', function() {
        
        // 查找所有的返回页首链接
        const pageTopLinks = document.querySelectorAll('a[href*="#wrap"], .pageTop01 a, a[alt="返回页首"]');
        
        pageTopLinks.forEach(function(link) {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                
                // 平滑滚动到页面顶部
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            });
        });
        
        // 为了兼容性，也监听包含"返回页首"文本的图片
        const pageTopImages = document.querySelectorAll('img[alt="返回页首"]');
        pageTopImages.forEach(function(img) {
            const parent = img.closest('a');
            if (parent) {
                parent.addEventListener('click', function(e) {
                    e.preventDefault();
                    window.scrollTo({
                        top: 0,
                        behavior: 'smooth'
                    });
                });
            }
        });
    });
})();