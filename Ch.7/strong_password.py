## Strong password detection
import re

def isStrong(password):

    is_strong = True
    
    for i in range(1):
        #has at least 8 characters long
        password_rx = re.compile(r'\w{8,}')
        
        validation = password_rx.search(password)
        
        if not validation:
            print('The password must have at least 8 digits.')
            is_strong = False
            break

        #contains both upper and lowercase characters
        password_rx = re.compile(r'[a-z]') #lowecase
        
        validation = password_rx.search(password)
        
        if not validation:
            print('The password must have at least one lowerchase character.')
            is_strong = False
            break
        
        password_rx = re.compile(r'[A-Z]') #uppercase
        
        validation = password_rx.search(password)
        
        if not validation:
            print('The password must have at least one uppercase character.')
            is_strong = False
            break
            
            
        #has at least one digit
        password_rx = re.compile(r'\d')
        
        validation = password_rx.search(password)
        
        if not validation:
            print('The password must have at least one digit.')
            is_strong = False
            break
    
    
    if is_strong == True:
        print('Success! Your password has been updated.')


password = input("Insert the new password: ")
isStrong(password)
