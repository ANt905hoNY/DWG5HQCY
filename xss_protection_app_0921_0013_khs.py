# 代码生成时间: 2025-09-21 00:13:46
import tkinter as tk
from tkinter import messagebox
import html

"""
XSS Protection Application
-------------------------
This application demonstrates a simple way to protect against XSS (Cross-Site Scripting) attacks.
It uses Python with the Tkinter framework to create a GUI that allows users to input potentially malicious code.
The application sanitizes the input to remove any dangerous characters or tags.
"""

# Function to sanitize user input to prevent XSS attacks
def sanitize_input(user_input):
    # Use html.escape to encode HTML characters
    sanitized_input = html.escape(user_input)
    return sanitized_input

# Function to display sanitized output
def display_output(user_input):
    sanitized_output = sanitize_input(user_input)
    output_label.config(text=sanitized_output)

# Function to handle user input and sanitize it
def handle_input():
    try:
        user_input = input_entry.get()
        display_output(user_input)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("XSS Protection Application")

# Create a label to prompt the user for input
prompt_label = tk.Label(root, text="Enter your text: ")
prompt_label.pack(pady=10)

# Create an entry widget for user input
input_entry = tk.Entry(root, width=50)
input_entry.pack(pady=10)

# Create a button to submit the user input
submit_button = tk.Button(root, text="Sanitize", command=handle_input)
submit_button.pack(pady=10)

# Create a label to display the sanitized output
output_label = tk.Label(root, text="", height=5)
output_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()