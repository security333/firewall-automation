import tkinter as tk
from tkinter import filedialog, messagebox
import paramiko
import os

class FileUploadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Upload App")
        self.root.geometry("400x200")

        self.server_ip = "192.168.1.100"  # Change to your server's IP
        self.ssh_port = 22
        self.ssh_key_file = os.path.expanduser("~/.ssh/id_rsa")  # Update with the path to the SSH private key

        self.setup_ui()

    def setup_ui(self):
        self.user_label = tk.Label(self.root, text="Enter Username:")
        self.user_label.pack(pady=5)

        self.user_entry = tk.Entry(self.root)
        self.user_entry.pack(pady=5)

        self.select_file_button = tk.Button(self.root, text="Select CSV File", command=self.select_file)
        self.select_file_button.pack(pady=10)

        self.upload_button = tk.Button(self.root, text="Upload File", command=self.upload_file, state=tk.DISABLED)
        self.upload_button.pack(pady=10)

    def select_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if self.file_path:
            self.upload_button.config(state=tk.NORMAL)
        else:
            self.upload_button.config(state=tk.DISABLED)

    def upload_file(self):
        username = self.user_entry.get().strip()
        if not username:
            messagebox.showerror("Error", "Please enter a username.")
            return

        if not self.file_path.endswith(".csv"):
            messagebox.showerror("Error", "Only CSV files are allowed.")
            return

        try:
            self.upload_to_server(username, self.file_path)
            messagebox.showinfo("Success", "File uploaded successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to upload file: {e}")

    def upload_to_server(self, username, file_path):
        target_directory = f"/tspa/{username}"

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.server_ip, port=self.ssh_port, key_filename=self.ssh_key_file)

        sftp = ssh.open_sftp()
        try:
            sftp.chdir(target_directory)
        except IOError:
            sftp.mkdir(target_directory)
            sftp.chdir(target_directory)

        target_file = os.path.join(target_directory, os.path.basename(file_path))
        sftp.put(file_path, target_file)

        sftp.close()
        ssh.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = FileUploadApp(root)
    root.mainloop()
