# Error Handling

while True: 
    try: 
        age = int(input('what is your age?'))
        10/age
        raise Exception ('Hey cut it out')
       #a raise ValueError('Hey cut it out')
    #except ValueError: 
       # print("please enter a number")
       # continue
    except ZeroDivisionError:
        print('please neter age higher tha 0')
        break
    else: 
        print('thank you')
        break
    finally:                              # Runs rgardless of any code before
        print('ok, I am finally done')
    print('can you hear me?')