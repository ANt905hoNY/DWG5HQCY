# 代码生成时间: 2025-09-22 05:15:56
import tkinter as tk
from tkinter import messagebox
import threading
import time
import requests

"""
性能测试脚本，使用TKINTER框架创建GUI界面。
用户可以输入URL，并设置并发请求数，程序将模拟请求并显示性能结果。
"""

class PerformanceTester:
    def __init__(self, master):
        self.master = master
        self.master.title("性能测试脚本")

        # 创建输入框和标签
        self.url_label = tk.Label(master, text="URL:")
        self.url_label.pack()
        self.url_entry = tk.Entry(master)
        self.url_entry.pack()

        self.concurrency_label = tk.Label(master, text="并发请求数:")
        self.concurrency_label.pack()
        self.concurrency_entry = tk.Entry(master)
        self.concurrency_entry.pack()

        # 创建开始测试按钮
        self.start_button = tk.Button(master, text="开始测试", command=self.start_test)
        self.start_button.pack()

        # 创建结果显示区域
        self.result_text = tk.Text(master, height=10, width=50)
        self.result_text.pack()

    def start_test(self):
        try:
            # 获取用户输入
            url = self.url_entry.get()
            concurrency = int(self.concurrency_entry.get())

            # 检查输入有效性
            if not url or concurrency <= 0:
                raise ValueError("请输入有效的URL和并发请求数")

            # 启动测试线程
            test_thread = threading.Thread(target=self.run_test, args=(url, concurrency))
            test_thread.start()
        except ValueError as e:
            messagebox.showerror("错误", str(e))

    def run_test(self, url, concurrency):
        try:
            # 模拟并发请求
            start_time = time.time()
            threads = []
            for _ in range(concurrency):
                thread = threading.Thread(target=self.send_request, args=(url,))
                threads.append(thread)
                thread.start()

            # 等待所有线程完成
            for thread in threads:
                thread.join()

            # 计算总耗时
            total_time = time.time() - start_time

            # 显示结果
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"总耗时: {total_time:.2f}秒
")
        except Exception as e:
            messagebox.showerror("错误", str(e))

    def send_request(self, url):
        try:
            # 发送HTTP请求
            response = requests.get(url)
            response.raise_for_status()  # 检查响应状态码
        except requests.RequestException as e:
            # 处理请求异常
            messagebox.showerror("请求错误", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = PerformanceTester(root)
    root.mainloop()