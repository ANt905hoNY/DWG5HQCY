# 代码生成时间: 2025-09-22 18:15:29
import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os
import json

"""
A simple Python program using Tkinter to backup and restore data.
This program allows the user to select a folder for backup and a destination for restore.
It uses shutil for copying files and os for file operations.
"""

# Constants for file paths and backup extension
BACKUP_EXTENSION = "_backup"

# Function to backup data
def backup_data(source_path):
    try:
        # Get the backup path by appending the extension to the source path
        backup_path = source_path + BACKUP_EXTENSION
        # Copy the source folder to the backup folder
        shutil.copytree(source_path, backup_path)
        messagebox.showinfo("Backup Successful", f"Data backed up successfully to {backup_path}")
    except Exception as e:
        messagebox.showerror("Backup Failed", f"An error occurred: {e}")

# Function to restore data
def restore_data(backup_path, target_path):
    try:
        # Copy the backup folder to the target folder
        shutil.copytree(backup_path, target_path)
        messagebox.showinfo("Restore Successful", f"Data restored successfully to {target_path}")
    except Exception as e:
        messagebox.showerror("Restore Failed", f"An error occurred: {e}")

# Main application class
class DataBackupRestoreApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Data Backup and Restore")
        self.geometry("400x200")

        # Button to select source folder for backup
        tk.Button(self, text="Backup Data", command=self.backup_data).pack(pady=10)

        # Button to select backup and target folders for restore
        tk.Button(self, text="Restore Data", command=self.restore_data).pack(pady=10)

    # Method to handle backup data
    def backup_data(self):
        source_path = filedialog.askdirectory(title="Select Source Folder")
        if source_path:
            backup_data(source_path)

    # Method to handle restore data
    def restore_data(self):
        backup_path = filedialog.askdirectory(title="Select Backup Folder")
        target_path = filedialog.askdirectory(title="Select Target Folder")
        if backup_path and target_path:
            restore_data(backup_path, target_path)

# Run the application
if __name__ == "__main__":
    app = DataBackupRestoreApp()
    app.mainloop()