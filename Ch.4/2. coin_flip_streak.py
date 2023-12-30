## Coin Flip Streaks

import random

chance_sample = 0
sample_size = 10000
reps= 100

for experiment_num in range(sample_size):
#create list of 100 heads or tails values
    result = []
    for i in range(reps):
        flip = random.randint(0,1) #0 for heads, 1 for tails
        result.append(flip)


    #check streak of six heads or tails in a row
    consecutives = 0
    six_consecutives = 0

    for j in range(reps - 1):
        if result[j] == result[j+1]:
            consecutives += 1
            if consecutives == 5:
                six_consecutives += 1
        else:
            consecutives = 0

    #calculate the probability of getting a streak of 6
    chance = six_consecutives / reps * 100
    print('Chance of steak: ' + str(chance) + '%')
    
    chance_sample += chance

print('The average chance of getting a streak of 6, based on a sample size of ' + str(sample_size) + ', is ' + str(chance_sample / 10000) + '%')
