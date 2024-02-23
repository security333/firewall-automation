# without functions

import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.withdraw()  # Hide the main window

browse_files = filedialog.askopenfilename(
    initialdir=os.path.expanduser("~"),  # Use the user's home directory
    title="Select text file containing list of IPs",
    filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
)

if browse_files:
    print("Selected file:", browse_files)
    with open(browse_files, 'r') as file:
        addresses = file.read().splitlines()
    print("IP addresses:", addresses)
else:
    print("No file selected.")


# same code with fucntions

import tkinter as tk
from tkinter import filedialog
import os

def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    browse_files = filedialog.askopenfilename(
        initialdir=os.path.expanduser("~"),  # Use the user's home directory
        title="Select text file containing list of IPs",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )

    return browse_files

def read_addresses(file_path):
    addresses = []
    if file_path:
        with open(file_path, 'r') as file:
            addresses = file.read().splitlines()
    return addresses

def main():
    file_path = select_file()
    if file_path:
        print("Selected file:", file_path)
        addresses = read_addresses(file_path)
        print("IP addresses:", addresses)
    else:
        print("No file selected.")

if __name__ == "__main__":
    main()

