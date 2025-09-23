# 代码生成时间: 2025-09-23 11:48:59
import tkinter as tk
from tkinter import messagebox
import json
import datetime

# Define a class to handle security audit logging
class SecurityAuditLog:
    def __init__(self, log_file='security_audit.log'):
        """ Initialize the SecurityAuditLog class with a log file. """
        self.log_file = log_file
        self.init_log_file()

    def init_log_file(self):
        """ Check if the log file exists, create if not. """
        try:
            with open(self.log_file, 'w') as file:
                file.write('')
        except Exception as e:
            messagebox.showerror('Error', f'Failed to create log file: {e}')
            raise

    def log_event(self, event_description):
        """ Log an event with a timestamp. """
        try:
            with open(self.log_file, 'a') as file:
                timestamp = datetime.datetime.now().isoformat()
                event = json.dumps({
                    'timestamp': timestamp,
                    'event': event_description
                }, indent=4)
                file.write(event + '
')
        except Exception as e:
            messagebox.showerror('Error', f'Failed to write to log file: {e}')
            raise

    def read_log(self):
        """ Read and return the contents of the log file. """
        try:
            with open(self.log_file, 'r') as file:
                return file.read()
        except Exception as e:
            messagebox.showerror('Error', f'Failed to read log file: {e}')
            raise

# GUI Application
class SecurityAuditApp:
    def __init__(self, master, audit_log):
        """ Initialize the GUI application. """
        self.master = master
        self.audit_log = audit_log
        self.create_widgets()

    def create_widgets(self):
        """ Create the GUI widgets. """
        # Log Event Entry
        self.log_entry = tk.Entry(self.master)
        self.log_entry.pack(pady=10)

        # Log Event Button
        self.log_button = tk.Button(self.master, text='Log Event', command=self.log_event)
        self.log_button.pack(pady=5)

        # Read Log Button
        self.read_log_button = tk.Button(self.master, text='Read Log', command=self.read_log)
        self.read_log_button.pack(pady=5)

    def log_event(self):
        """ Log an event from the user input. """
        event_description = self.log_entry.get()
        if event_description:
            self.audit_log.log_event(event_description)
            messagebox.showinfo('Success', 'Event logged successfully.')
        else:
            messagebox.showwarning('Warning', 'Please enter an event description.')

    def read_log(self):
        """ Display the contents of the log file. """
        log_contents = self.audit_log.read_log()
        messagebox.showinfo('Log Contents', log_contents)

# Main function to run the application
def main():
    # Create the main window
    root = tk.Tk()
    root.title('Security Audit Log')

    # Create a SecurityAuditLog instance
    audit_log = SecurityAuditLog()

    # Create the GUI application
    app = SecurityAuditApp(root, audit_log)

    # Run the main loop
    root.mainloop()

if __name__ == '__main__':
    main()