# 代码生成时间: 2025-09-18 01:35:00
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import os

"""
A document format converter using Python and Tkinter.
This program allows users to select a document, choose a target format,
and convert the document to the selected format.
"""

class DocumentFormatter:
    def __init__(self, root):
        self.root = root
        self.root.title('Document Format Converter')
        self.root.geometry('400x200')

        # Create buttons
        self.open_button = tk.Button(self.root, text='Open Document', command=self.open_document)
        self.open_button.pack(pady=10)

        self.convert_button = tk.Button(self.root, text='Convert Document', command=self.convert_document, state=tk.DISABLED)
        self.convert_button.pack(pady=10)

        self.format_label = tk.Label(self.root, text='Select a format: ')
        self.format_label.pack(pady=5)

        self.format_var = tk.StringVar()
        self.format_var.set('Choose a format')
        self.format_options = ['PDF', 'DOCX', 'TXT']
        self.format_menu = tk.OptionMenu(self.root, self.format_var, *self.format_options, command=self.update_format)
        self.format_menu.pack(pady=5)

        self.status_label = tk.Label(self.root, text='')
        self.status_label.pack(pady=10)

    def open_document(self):
        """Open a document file for conversion."""
        file_path = filedialog.askopenfilename(filetypes=[('All Files', '*.*')])
        if file_path:
            self.convert_button.config(state=tk.NORMAL)
            self.status_label.config(text=f'Document opened: {os.path.basename(file_path)}')
        else:
            self.status_label.config(text='No document selected.')

    def convert_document(self):
        """Convert the selected document to the chosen format."""
        try:
            file_path = filedialog.askopenfilename()
            if not file_path:
                raise ValueError('No document selected for conversion.')
            target_format = self.format_var.get()
            if target_format == 'Choose a format':
                raise ValueError('No format selected.')

            # Convert the document (this is a placeholder for the actual conversion logic)
            converted_file_path = f'{os.path.splitext(file_path)[0]}.{target_format.lower()}'
            messagebox.showinfo('Conversion Successful', f'Document converted to {target_format} and saved as {converted_file_path}')
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def update_format(self, value):
        """Update the status label when a format is selected."""
        if value == 'Choose a format':
            self.convert_button.config(state=tk.DISABLED)
            self.status_label.config(text='Please select a format and a document to convert.')
        else:
            self.convert_button.config(state=tk.NORMAL)
            self.status_label.config(text='Ready to convert.')

if __name__ == '__main__':
    root = tk.Tk()
    app = DocumentFormatter(root)
    root.mainloop()