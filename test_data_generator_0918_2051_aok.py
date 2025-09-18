# 代码生成时间: 2025-09-18 20:51:01
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import random
import string

class TestDataGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title('Test Data Generator')
        self.create_widgets()

    def create_widgets(self):
        # Label for file path entry
        self.label = tk.Label(self.master, text='File Path:')
        self.label.pack()

        # Entry widget for file path
        self.entry = tk.Entry(self.master, width=50)
        self.entry.pack()

        # Button to browse for file
        self.browse_button = tk.Button(self.master, text='Browse', command=self.browse_file)
        self.browse_button.pack()

        # Button to generate test data
        self.generate_button = tk.Button(self.master, text='Generate', command=self.generate_data)
        self.generate_button.pack()

    def browse_file(self):
        # Open file dialog to select a file
        file_path = filedialog.askopenfilename()
        if file_path:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, file_path)

    def generate_data(self):
        # Get the file path from the entry widget
        file_path = self.entry.get()
        if not file_path:
            messagebox.showerror('Error', 'Please select a file')
            return

        try:
            # Read the file content
            with open(file_path, 'r') as file:
                data = file.read()

            # Generate test data based on the file content
            test_data = self.generate_random_data(data)

            # Write the test data to a new file
            self.write_test_data(test_data)

        except Exception as e:
            messagebox.showerror('Error', str(e))

    def generate_random_data(self, data):
        # Generate random test data based on the input data
        # This is a simple implementation and can be expanded
        # based on the specific requirements
        lines = data.splitlines()
        random_data = []
        for line in lines:
            random_data.append(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(len(line))))
        return '
'.join(random_data)

    def write_test_data(self, test_data):
        # Write the test data to a new file
        file_path = self.entry.get().replace('.txt', '_test.txt')
        with open(file_path, 'w') as file:
            file.write(test_data)
        messagebox.showinfo('Success', 'Test data generated successfully')

# Create the main window and pass it to the TestDataGenerator class
root = tk.Tk()
app = TestDataGenerator(root)
root.mainloop()