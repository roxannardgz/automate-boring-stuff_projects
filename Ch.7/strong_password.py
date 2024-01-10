## Strong password detection
import re

#make sure password string is strong
def isStrong(password):
    
    #password status
    is_strong = True   #defaul value
    
    #password checks (strength criteria)
    charater_count_rx = re.compile(r'[\w!@#$%&*()-=+^]{8,}')    #at least 8 characters long
    lower_rx = re.compile(r'[a-z]')                             #includes lowercase char
    upper_rx = re.compile(r'[A-Z]')                             #includes uppercase char
    digit_rx = re.compile(r'\d')                                #includes digit(s)
    
    #dict with checks and error messages
    checks = {1: (charater_count_rx, 'Error: The password must have at least 8 characters.'), 
                2: (lower_rx, 'Error: The password must have at least one lowercase character.'), 
                3: (upper_rx, 'Error: The password must have at least one uppercase character.'), 
                4: (digit_rx, 'Error: The password must have at least one digit.')}

    #check password strength criteria
    for check in checks.values():
        if check[0].search(password) == None:
            print(check[1])               #prints corresponding error message
            is_strong = False             #changes password status
            break                         #exit the loop - doesn't check for remaining validations

    #print message if all the checks are passed
    if is_strong == True:
        print('Success! Your password has been updated.')


password = input("Insert the new password: ")
isStrong(password)
