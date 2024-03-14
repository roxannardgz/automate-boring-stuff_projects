#! python3

# Regex search: opens all .txt files in a folder
#               searches for any lines that match user-supplied regex
#               the result is printed on the screen

import os
import re

# search for the regex and print to screen
def search_pattern (file_path, pattern):
    with open(file_path) as file:                                   # open current file in files_list
        for line in file:
            if re.search(pattern, line):                            # search for the provided pattern
                print(line)                                         # prints lines found with pattern


# search for .txt files in the provided path
def search_folder(folder_path,pattern):
    files_list = os.listdir(folder_path)                            # list all filenames in the path

    for file_name in files_list:
        if file_name.endswith('.txt'):                              # find the file names with .txt extension
            file_path = os.path.join(folder_path, file_name)        # join complete file path
            search_pattern(file_path, pattern)



# ask for the inputs and call the search function
def main():
    folder_path = input('Enter the path to the folder: ')
    pattern = input('Enter the regular expression to search for: ')
    search_folder(folder_path, pattern)
