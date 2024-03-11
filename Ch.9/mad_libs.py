#! python3
# Mad Libs - create a program that reads in text files and lets the user add their own text
# anywhere the words ADJECTIVE, NOUN, VERB or ADVERB appear.


# usage:    enter the name of the file with the template story
#           follow the prompts


import os
import re

# get path and open file
file_name = input('Enter the name of the file: ')
cwd = os.getcwd()
file_path = os.path.join(cwd,f'{file_name}.txt')

with open(file_path) as file:
    text_to_search = file.read()


# find keywords
madlib_rx = re.compile(r'(ADJECTIVE|NOUN|VERB|ADVERB)')
matches = madlib_rx.findall(text_to_search)

final_text = text_to_search

# replace keywords
for match in matches:
    replacement = input(f'Enter a(n) {match.lower()}: ')
    final_text = final_text.replace(match, replacement,1)

# print updated story / text
print(final_text)
