##Multiplication quiz

import pyinputplus as pyip
import random
import time

def multiplication_quiz(num_questions,seconds,tries):
    correct = 0     #num of correct answers given by the user
    
    for q in range(num_questions):     #number of questions
        a = random.randint(0,9)
        b = random.randint(0,9)
        correct_answer = a * b
        
        prompt = (f'{q+1}. {a} x {b} = ')
        try:
            pyip.inputInt(prompt, allowRegexes=[f'^{correct_answer}$'],               #right answers
                                blockRegexes=[('.*', 'Nope,that\'s not correct.')],   #wrong answers
                                timeout=seconds, limit=tries)                         #restrictions
                              
            
        except pyip.TimeoutException:               #exceeded time allowed to answer
            print('Sorry, you\'re out of time.')
        except pyip.RetryLimitException:            #exceeded number of tries allowed
            print('Sorry, you\'re out of tries.')
        else: 
            #no exceptions were raised -- correct answer
            print('Correct!')
            correct += 1
        
        time.sleep(1)
    
    print(f'You got {correct} out of {num_questions}.')

seconds = 8
tries = 3
questions = 10

print('Welcome to the multiplication quiz!')
print(f'You will have {questions} multiplication questions to answer.')
print(f'You will have {seconds} seconds to answer and {tries} tries per question.')
ready = pyip.inputYesNo(prompt='Are you ready to start? ')

if ready == 'yes':
    multiplication_quiz(questions, seconds, tries)
else:
    print('The go to study and come back later.')
