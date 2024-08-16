#! python3

# big_files.py - find files that have a size of more than 100MB

import os
from tkinter import Tk, messagebox
from tkinter.filedialog import askdirectory

# Initialize the Tk root window and hide it
root = Tk()
root.withdraw()

# Ask the user to select a folder
folder = askdirectory(title="Select Folder")

if not folder:
    messagebox.showerror(title="Error", message="No folder selected.")
    exit()

# Walk through the selected folder tree
files_cnt = 0
for foldername, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        file_path = os.path.join(foldername, filename)
        if os.path.getsize(file_path) / (1024 * 1024) > 100:
            file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
            print(f'{filename} - {file_size_mb:.2f} MB')
            files_cnt += 1

print(f'There are {files_cnt} files larger than 100MB.')
