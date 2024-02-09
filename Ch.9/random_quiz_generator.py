#quiz generator
#create geography quizzes with questions and answers in random order

import random

# quiz data, where the keys are the States and the values are their capitals
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico':
'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota':
'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':
'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#generate 35 quiz files
for quizNum in range(35):
    #create the quiz file and answer key file
    quizFile = open(f'Quiz Num {quizNum + 1}.txt', 'w')
    answersFile = open(f'Answers Quiz Num {quizNum + 1}.txt', 'w')
    
    # write the header of the quiz
    quizFile.write((' '*20) + f'State Capitals Quiz #{quizNum + 1}')
    quizFile.write('\n\n')
    quizFile.write('Name:' + ('_'*36) + '\n')
    quizFile.write('Date:' + ('_'*16) + (' '*8) + 'Period:' + ('_'*10))
    quizFile.write('\n\n')
    
    # shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)
    
    ##loop through the 50 states and make the questions
    for questionNum in range(50):
        #get right and wrong answers
        correct_answer = capitals[states[questionNum]]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]   #delete the right answer from the list of wrong answers
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options =  wrong_answers + [correct_answer]
        random.shuffle(answer_options)     #to make sure that the correct_answer isn't always D
    
        #write the questions and answer options to the quiz file
        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f'   {  "ABCD"[i]}. {answer_options[i]}\n')
        quizFile.write('\n')
        
        #write the answer key to the answer file
        answersFile.write(f'{questionNum + 1}. {"ABCD"[answer_options.index(correct_answer)]}\n')
        
    quizFile.close()
    answersFile.close()
