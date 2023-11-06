# Generate a number 1 to 10
# input from user? 
# check that input is a number 1 to 10 
# check if number is the right guess. Otherwise ask again 
# https://pypi.org/


from random import randint

import sys


# generate random number between 1 to 10 by passing in as an arguments to the file
#answer = randint(int(sys.argv[1]), int(sys.argv[2]))

answer = randint(1, 10)

# get the input fro the user and convert it into an int
guess = input('Please guess the the random from 1 to 10: ')
guess = int(guess)



# check that inpute 

while True: 
    try: 
        guess = int(input('Please guess the the random from 1 to 10: '))
        if 1 <= (guess) <= 10 : 
            if (guess) == answer : 
                print('Congratulations! youve guess the corect number!')
                break
        else: 
            print('Sorry thats the wrong number, please try again')
    except ValueError:
        print('Sorry thats the wrong number, please try again')
        continue
       