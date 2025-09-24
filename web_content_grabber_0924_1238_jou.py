# 代码生成时间: 2025-09-24 12:38:25
import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import threading

"""
A simple web content grabber application using Python and TKinter.
This application allows users to input a URL, and then fetches the content of the webpage.
"""

class WebContentGrabber:
    def __init__(self, root):
        """Initialize the application."""
        self.root = root
        self.root.title("Web Content Grabber")
        self.root.geometry("400x200")
# TODO: 优化性能

        self.url_label = tk.Label(root, text="Enter URL: ")
        self.url_label.pack(pady=10)

        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack(pady=5)

        self.fetch_button = tk.Button(root, text="Fetch Content", command=self.fetch_content)
        self.fetch_button.pack(pady=20)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)
# TODO: 优化性能

    def fetch_content(self):
        """Fetch the content of the webpage."""
        url = self.url_entry.get()
        try:
            response = requests.get(url)
# TODO: 优化性能
            response.raise_for_status()  # Raise an exception for HTTP errors
            content = response.text
            self.display_content(content)
# 扩展功能模块
        except requests.exceptions.HTTPError as errh:
            messagebox.showerror("HTTP Error", f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            messagebox.showerror("Error", f"Error Connecting: {errc}")
# 改进用户体验
        except requests.exceptions.Timeout as errt:
            messagebox.showerror("Timeout Error", f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            messagebox.showerror("Error", f"Error: {err}")

    def display_content(self, content):
        """Display the content of the webpage."""
        soup = BeautifulSoup(content, 'html.parser')
        self.result_label.config(text=soup.get_text(separator="
"))

    def start_thread(self, url):
        """Start a new thread for fetching content."""
        thread = threading.Thread(target=self.fetch_content, args=(url,))
        thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = WebContentGrabber(root)
    root.mainloop()