##regex version of the trip() method

import re

#delete specific characters or spaces from  beginning and end of string
def strip_regex(input_string, char=''):
    
    if char == '':          #when no character inserted
        pattern_rx = re.compile(r'^[\s]* | [\s]*$')
        return pattern_rx.sub('', input_string)
    else:                   #for character inserted
        pattern = f"[{re.escape(char)}]*"
        regex = re.compile(f"^{pattern}|{pattern}$")
        return regex.sub('', input_string)


# example usage ---> input these strings to try the function
#string1 = "   Hello, World!   "
#string2 = "###Greetings###"

string = input('Enter the string to clean: ')
char_delete = input('Enter the character to delete (or press enter to delete blank spaces): ')

print(strip_regex(string))
print(strip_regex(string, char_delete))
