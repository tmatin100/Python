# Error Handleing
"""" 
# TypeError
print(1+'hello)')

# SyntaxError 
# def hooo()
   # psss

# NameError
def hello2():
    1 + name 

hello2()

# IndexError 
li = [1,2,3]
print li[5]

# ZeorDivionError
a = 5/0
print(a)

"""
# try block will try the code inside it
# except block will catch anything that errors out in the try block and print what you wan it to print in that case
while True: 
    try: 
        age = int(input('What is your age? '))
        #print(age)
        10/age 
    except ValueError: 
        print('please enter a number ')
    except ZeroDivisionError: 
        print('please enter an age higheer than zeor ')
    else: 
        print('thank you')
        break


