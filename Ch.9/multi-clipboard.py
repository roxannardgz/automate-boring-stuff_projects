#! python3
#Updatable Multi-Clipboard - saves and loads pieces of text to the clipboard

#usage: save <keyword> - saves clipboard to keyword
#       delete <keyword> - deletes the keyword from the shelf
#       <keyword> - loads keyword to clipboard
#       list - loads all keywords to clipboard
#       delete - deletes all keywords

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')  #mcb stands for Multi-ClipBoard

## save clipboard content or delete keyword from shelf
if len(sys.argv) == 3:
    #for saving
   if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    #for deleting
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
## list keywords, load content or delete all keywords
elif len(sys.argv) == 2:
    #for getting the list of keywords
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    #for deleting keywords
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
    #for loading the content of the keyword
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
else:
    print('Incorrect number of keywords. Please check the usage intructions for reference.')

mcbShelf.close()
