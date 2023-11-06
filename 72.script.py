import random 
  

def run_guess(guess, answer):
    if 1 <= (guess) <= 10 : 
        if (guess) == answer : 
            print('Congratulations! youve guess the corect number!')
            return True 
        else: 
            print('Sorry thats the wrong number, please try again')

if __name__ == '__main__':
    answer = random.randint(1, 10)
    while True:
        try: 
            guess = int(input('guess a number between 1 to 10:'))
            if (run_guess(guess, answer)):
                break
        except ValueError:
            print('plase enter an number: ')
            continue