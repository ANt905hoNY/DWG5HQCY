# 代码生成时间: 2025-09-24 00:37:53
import tkinter as tk
from tkinter import messagebox
import requests
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

# HTTP请求处理器类
class HttpRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """
        处理GET请求
        """
        try:
            # 这里可以根据需要添加请求处理逻辑
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write("Hello, this is a GET request.".encode())
        except Exception as e:
            self.send_response(500)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write("Error: An error occurred during the request.".encode())

    def do_POST(self):
        """
        处理POST请求
        """
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            # 这里可以根据需要添加请求处理逻辑
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write("Hello, this is a POST request.".encode())
        except Exception as e:
            self.send_response(500)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write("Error: An error occurred during the request.".encode())

# GUI界面类
class GuiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HTTP Request Handler")
        self.root.geometry("400x200")

        self.label = tk.Label(self.root, text="HTTP Request Handler is running...")
        self.label.pack(pady=20)

        self.start_server()

    def start_server(self):
        """
        启动HTTP服务器
        """
        server_address = ("localhost", 8000)
        self.httpd = HTTPServer(server_address, HttpRequestHandler)
        threading.Thread(target=self.httpd.serve_forever).start()

    def stop_server(self):
        """
        停止HTTP服务器
        """
        self.httpd.shutdown()
        self.httpd.server_close()

# 主程序入口
def main():
    root = tk.Tk()
    app = GuiApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()