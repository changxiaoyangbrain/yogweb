#!/usr/bin/env python3
"""
YogWeb 热重载开发服务器
支持CSS/HTML文件变更自动刷新，实时开发调试
作者: Claude Code
"""

import os
import sys
import time
import json
import threading
import webbrowser
from pathlib import Path
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from socketserver import ThreadingMixIn
from urllib.parse import urlparse, parse_qs
import hashlib
import mimetypes

# 尝试导入文件监听库
try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
    WATCHDOG_AVAILABLE = True
except ImportError:
    WATCHDOG_AVAILABLE = False
    print("⚠️  watchdog未安装，使用轮询模式监听文件变化")
    print("   可通过 pip install watchdog 安装以获得更好的性能")

class FileWatcher:
    """文件监听器"""
    
    def __init__(self, callback):
        self.callback = callback
        self.file_hashes = {}
        self.watch_extensions = {'.css', '.html', '.js', '.json'}
        self.watch_dirs = {'css', 'style', 'common', '.'}
        self.ignore_dirs = {'__pycache__', '.git', 'node_modules', 'dist'}
        
        self.update_file_hashes()
        
    def update_file_hashes(self):
        """更新文件哈希缓存"""
        new_hashes = {}
        
        for watch_dir in self.watch_dirs:
            if not os.path.exists(watch_dir):
                continue
                
            for root, dirs, files in os.walk(watch_dir):
                # 过滤忽略的目录
                dirs[:] = [d for d in dirs if d not in self.ignore_dirs]
                
                for file in files:
                    if any(file.endswith(ext) for ext in self.watch_extensions):
                        filepath = os.path.join(root, file)
                        try:
                            with open(filepath, 'rb') as f:
                                content = f.read()
                                new_hashes[filepath] = hashlib.md5(content).hexdigest()
                        except Exception as e:
                            print(f"⚠️  无法读取文件 {filepath}: {e}")
        
        return new_hashes
    
    def check_changes(self):
        """检查文件变化"""
        new_hashes = self.update_file_hashes()
        changed_files = []
        
        # 检查修改和新增的文件
        for filepath, new_hash in new_hashes.items():
            old_hash = self.file_hashes.get(filepath)
            if old_hash != new_hash:
                changed_files.append(filepath)
        
        # 检查删除的文件
        for filepath in self.file_hashes:
            if filepath not in new_hashes:
                changed_files.append(filepath)
        
        if changed_files:
            print(f"📁 检测到文件变化: {', '.join(changed_files)}")
            self.file_hashes = new_hashes
            self.callback(changed_files)
    
    def start_polling(self):
        """开始轮询监听"""
        def poll():
            while True:
                try:
                    self.check_changes()
                    time.sleep(0.5)  # 500ms轮询间隔
                except KeyboardInterrupt:
                    break
                except Exception as e:
                    print(f"⚠️  文件监听错误: {e}")
                    time.sleep(1)
        
        thread = threading.Thread(target=poll, daemon=True)
        thread.start()
        return thread

if WATCHDOG_AVAILABLE:
    class WatchdogHandler(FileSystemEventHandler):
        """Watchdog文件系统事件处理器"""
        
        def __init__(self, callback):
            self.callback = callback
            self.watch_extensions = {'.css', '.html', '.js', '.json'}
            self.last_event_time = {}
            self.debounce_delay = 0.1  # 100ms防抖
        
        def on_modified(self, event):
            if event.is_directory:
                return
            
            filepath = event.src_path
            if not any(filepath.endswith(ext) for ext in self.watch_extensions):
                return
            
            # 防抖处理
            now = time.time()
            if filepath in self.last_event_time:
                if now - self.last_event_time[filepath] < self.debounce_delay:
                    return
            
            self.last_event_time[filepath] = now
            print(f"📁 文件变化: {filepath}")
            self.callback([filepath])

class DevRequestHandler(SimpleHTTPRequestHandler):
    """开发服务器请求处理器"""
    
    def __init__(self, *args, **kwargs):
        self.dev_server = kwargs.pop('dev_server', None)
        super().__init__(*args, **kwargs)
    
    def end_headers(self):
        """添加CORS和缓存控制头"""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()
    
    def do_GET(self):
        """处理GET请求"""
        parsed_path = urlparse(self.path)
        
        # 热重载API端点
        if parsed_path.path == '/__dev__/reload':
            self.send_reload_response()
            return
        
        if parsed_path.path == '/__dev__/status':
            self.send_status_response()
            return
        
        # 注入热重载脚本到HTML文件
        if self.path.endswith('.html') or self.path == '/':
            self.serve_html_with_reload()
            return
        
        # 普通文件服务
        super().do_GET()
    
    def serve_html_with_reload(self):
        """服务HTML文件并注入热重载脚本"""
        try:
            # 确定实际文件路径
            if self.path == '/':
                filepath = 'index.html'
            else:
                filepath = self.path.lstrip('/')
            
            # 如果文件不存在，尝试一些默认文件
            if not os.path.exists(filepath):
                default_files = ['index.html', 'performance_optimized.html', 'modern_features_demo.html']
                for default in default_files:
                    if os.path.exists(default):
                        filepath = default
                        break
                else:
                    self.send_error(404, f"File not found: {self.path}")
                    return
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 注入热重载脚本
            reload_script = '''
<script>
(function() {
    let lastCheck = Date.now();
    let checkInterval = 1000; // 1秒检查间隔
    
    function checkForReload() {
        fetch('/__dev__/reload?t=' + Date.now())
            .then(response => response.json())
            .then(data => {
                if (data.shouldReload && data.timestamp > lastCheck) {
                    console.log('🔄 检测到文件变化，重新加载页面...');
                    location.reload();
                }
            })
            .catch(() => {
                // 服务器连接失败，可能是服务器重启
                setTimeout(() => location.reload(), 1000);
            });
    }
    
    // 页面加载完成后开始检查
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            setInterval(checkForReload, checkInterval);
        });
    } else {
        setInterval(checkForReload, checkInterval);
    }
    
    // 显示开发模式指示器
    const devIndicator = document.createElement('div');
    devIndicator.innerHTML = '🔧 开发模式';
    devIndicator.style.cssText = `
        position: fixed;
        top: 10px;
        right: 10px;
        background: #28a745;
        color: white;
        padding: 5px 10px;
        border-radius: 20px;
        font-size: 12px;
        z-index: 10000;
        font-family: monospace;
        box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    `;
    document.body.appendChild(devIndicator);
    
    console.log('🚀 YogWeb 开发模式已启用 - 支持热重载');
})();
</script>
</head>'''
            
            if '</head>' in content:
                content = content.replace('</head>', reload_script)
            else:
                # 如果没有</head>标签，在<body>前添加
                if '<body>' in content:
                    content = content.replace('<body>', f'<script>{reload_script}</script><body>')
            
            # 发送响应
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(content.encode('utf-8'))))
            self.end_headers()
            self.wfile.write(content.encode('utf-8'))
            
        except Exception as e:
            self.send_error(500, f"Error serving HTML: {e}")
    
    def send_reload_response(self):
        """发送热重载状态响应"""
        response = {
            'shouldReload': self.dev_server.should_reload if self.dev_server else False,
            'timestamp': int(time.time() * 1000)
        }
        
        if self.dev_server:
            self.dev_server.should_reload = False
        
        content = json.dumps(response).encode('utf-8')
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(content)))
        self.end_headers()
        self.wfile.write(content)
    
    def send_status_response(self):
        """发送服务器状态响应"""
        status = {
            'status': 'running',
            'timestamp': int(time.time() * 1000),
            'watchdog': WATCHDOG_AVAILABLE,
            'server': 'YogWeb Dev Server'
        }
        
        content = json.dumps(status).encode('utf-8')
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(content)))
        self.end_headers()
        self.wfile.write(content)
    
    def log_message(self, format, *args):
        """自定义日志格式"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] {format % args}")

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """多线程HTTP服务器"""
    allow_reuse_address = True
    daemon_threads = True

class DevServer:
    """开发服务器主类"""
    
    def __init__(self, port=8189, host='localhost'):
        self.port = port
        self.host = host
        self.should_reload = False
        self.server = None
        self.file_watcher = None
        
    def on_file_change(self, changed_files):
        """文件变化回调"""
        print(f"🔄 触发热重载: {len(changed_files)} 个文件变化")
        self.should_reload = True
    
    def start_file_watcher(self):
        """启动文件监听"""
        if WATCHDOG_AVAILABLE:
            print("📁 启动 Watchdog 文件监听...")
            self.observer = Observer()
            handler = WatchdogHandler(self.on_file_change)
            
            # 监听多个目录
            watch_dirs = ['css', 'style', 'common', '.']
            for watch_dir in watch_dirs:
                if os.path.exists(watch_dir):
                    self.observer.schedule(handler, watch_dir, recursive=True)
                    print(f"   监听目录: {watch_dir}")
            
            self.observer.start()
        else:
            print("📁 启动轮询文件监听...")
            self.file_watcher = FileWatcher(self.on_file_change)
            self.file_watcher.start_polling()
    
    def create_request_handler(self):
        """创建请求处理器"""
        dev_server = self
        
        class CustomHandler(DevRequestHandler):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, dev_server=dev_server, **kwargs)
        
        return CustomHandler
    
    def start(self):
        """启动开发服务器"""
        try:
            print(f"🚀 启动 YogWeb 开发服务器...")
            print(f"📍 地址: http://{self.host}:{self.port}")
            print(f"📁 目录: {os.getcwd()}")
            
            # 启动文件监听
            self.start_file_watcher()
            
            # 创建HTTP服务器
            handler_class = self.create_request_handler()
            self.server = ThreadedHTTPServer((self.host, self.port), handler_class)
            
            print(f"✅ 服务器已启动")
            print(f"🔧 支持热重载 - CSS/HTML文件变化将自动刷新")
            print(f"🌐 推荐页面:")
            print(f"   • 现代特性演示: http://{self.host}:{self.port}/modern_features_demo.html")
            print(f"   • 性能优化版: http://{self.host}:{self.port}/performance_optimized.html")
            print(f"")
            print(f"按 Ctrl+C 停止服务器")
            
            # 自动打开浏览器
            if webbrowser:
                threading.Timer(1, lambda: webbrowser.open(f'http://{self.host}:{self.port}/modern_features_demo.html')).start()
            
            self.server.serve_forever()
            
        except KeyboardInterrupt:
            self.stop()
        except Exception as e:
            print(f"❌ 服务器错误: {e}")
            sys.exit(1)
    
    def stop(self):
        """停止服务器"""
        print(f"\n🛑 正在停止服务器...")
        
        if hasattr(self, 'observer') and WATCHDOG_AVAILABLE:
            self.observer.stop()
            self.observer.join()
        
        if self.server:
            self.server.shutdown()
            self.server.server_close()
        
        print(f"✅ 服务器已停止")

def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='YogWeb 热重载开发服务器')
    parser.add_argument('--port', '-p', type=int, default=8189, help='服务器端口 (默认: 8189)')
    parser.add_argument('--host', type=str, default='localhost', help='服务器主机 (默认: localhost)')
    parser.add_argument('--open', action='store_true', help='启动后自动打开浏览器')
    
    args = parser.parse_args()
    
    # 检查端口是否被占用
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((args.host, args.port))
    sock.close()
    
    if result == 0:
        print(f"❌ 端口 {args.port} 已被占用")
        # 尝试其他端口
        for port in range(args.port + 1, args.port + 10):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((args.host, port))
            sock.close()
            if result != 0:
                args.port = port
                print(f"✅ 使用替代端口: {port}")
                break
        else:
            print(f"❌ 无法找到可用端口")
            sys.exit(1)
    
    # 启动开发服务器
    dev_server = DevServer(args.port, args.host)
    dev_server.start()

if __name__ == "__main__":
    main()