#! python3

# selective_copy.py - searches for files with certain extensions and lists them.

import shutil, os, re
from tkinter import Tk, messagebox
from tkinter.filedialog import askdirectory
from tkinter import simpledialog

# Initialize the Tk root window and hide it
root = Tk()
root.withdraw()

# Ask the user for a file extension
extension = simpledialog.askstring(title="Extension", prompt="Which extension files are you looking for? ")

#print(extension)
if not extension:
    messagebox.showerror(title="Error", message="No extension input")
else:
    # Ask the user to select a folder
    folder = askdirectory(title="Select Folder")

    if not folder:
        messagebox.showerror(title="Error", message="No folder selected.")
        exit()

    # Create regex to match files with the input extension
    extension_pattern = re.compile(rf'\.{extension}$')
    file_list = []

    # Walk through the selected folder and search for the file extension
    for filename in os.listdir(folder):
        found_file = extension_pattern.search(filename)
        
        # Skip files with different extensions
        if found_file == None:
            continue
        
        # Add file to the list of found files with correct extension
        file_list.append(filename)
    
    # Convert the list to a string with each filename on a new line
    file_list_str = '\n'.join(file_list)

    # Show the list in a message box
    if file_list:
        messagebox.showinfo(title="Files Found", message=file_list_str)
    else:
        messagebox.showinfo(title="Files Found", message="No files found with the specified extension.")


# Clean up and close the Tk root window
root.destroy()
