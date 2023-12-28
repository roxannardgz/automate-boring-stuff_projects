'''The Collatz Sequence'''

import sys

#generate the Collatz sequence
def collatz(number):
    print(number)
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number)
        elif number % 2 == 1:
            number = 3 * number + 1
            print(number)
    number = 0 #exit the while loop


number = 1

while number == 1:
    #detect whether the user types in a noninteger string and handle the error
    try:
        number = int(input('Please enter a whole number greater than 1: '))  
    except ValueError:
        print('This is not even a number. If you don\'t want to play the game that\'s also alright.')
        print('See you later!')
        sys.exit()

    #check for integers greater than 1
    if number <= 1:
        print('The number should be greater than 1. Please try again.')
        number = 1
    else:
        collatz(number)
