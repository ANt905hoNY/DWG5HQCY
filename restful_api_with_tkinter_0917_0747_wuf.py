# 代码生成时间: 2025-09-17 07:47:32
import tkinter as tk
from tkinter import messagebox
from flask import Flask, jsonify, request

# 初始化 Flask 应用
app = Flask(__name__)

# 定义 API 路由和处理函数
@app.route('/api/data', methods=['GET'])
def get_data():
    """获取数据的 API 接口"""
    # 这里只是一个示例，实际的数据获取逻辑需要根据业务需求编写
    data = {"message": "Hello, World!"}
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def post_data():
    """提交数据的 API 接口"""
    try:
        # 获取 JSON 数据
        data = request.get_json()
        if not data:
            raise ValueError("No input data provided")
        # 这里只是一个示例，实际的数据提交逻辑需要根据业务需求编写
        return jsonify({"status": "success", "message": "Data received"}), 200
    except Exception as e:
        # 错误处理
        return jsonify({"status": "error", "message": str(e)}), 400

# 创建 Tkinter GUI 界面
class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RESTful API Interface")
        self.geometry("400x200")
        
        # 添加按钮和标签用于启动和显示 API 状态
        self.start_button = tk.Button(self, text="Start API", command=self.start_api)
        self.start_button.pack(pady=20)
        
        self.status_label = tk.Label(self, text="API is not running")
        self.status_label.pack(pady=20)

    def start_api(self):
        """启动 Flask 应用"""
        try:
            # 使用线程启动 Flask 应用，避免阻塞 Tkinter GUI 线程
            from threading import Thread
            self.thread = Thread(target=lambda: app.run(debug=True, port=5000, use_reloader=False))
            self.thread.start()
            self.status_label.config(text="API is running")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# 运行 Tkinter 应用
if __name__ == '__main__':
    app = MyApp()
    app.mainloop()