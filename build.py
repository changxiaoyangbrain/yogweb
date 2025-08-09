#!/usr/bin/env python3
"""
YogWeb 生产构建脚本
"""

import os
import shutil
import gzip

def build_production():
    print("🚀 开始生产构建...")
    
    # 创建构建目录
    build_dir = 'dist'
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    os.makedirs(build_dir)
    
    # 复制文件
    print("📁 复制文件...")
    
    # 复制HTML文件
    for html_file in ['performance_optimized.html', 'modern_features_demo.html']:
        if os.path.exists(html_file):
            shutil.copy2(html_file, build_dir)
    
    # 复制压缩CSS
    shutil.copytree('css', f'{build_dir}/css')
    shutil.copytree('style', f'{build_dir}/style')
    shutil.copytree('common', f'{build_dir}/common')
    
    # 复制图片和其他资源
    for dir_name in ['images', 'js']:
        if os.path.exists(dir_name):
            shutil.copytree(dir_name, f'{build_dir}/{dir_name}')
    
    # 创建Gzip版本
    print("🗜️ 创建Gzip版本...")
    for root, dirs, files in os.walk(build_dir):
        for file in files:
            if file.endswith(('.css', '.js', '.html')):
                filepath = os.path.join(root, file)
                with open(filepath, 'rb') as f:
                    content = f.read()
                
                with gzip.open(filepath + '.gz', 'wb') as f:
                    f.write(content)
    
    print("✅ 构建完成！输出目录: dist/")

if __name__ == "__main__":
    build_production()
