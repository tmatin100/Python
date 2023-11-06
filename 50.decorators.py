# Decorators - supercharge our function and add extra funcionality to it
# Higher Order Function - HOC - a funcion tha accepts or returns another function 

def greet(func):  # a function that accepts another function  
    func()


def greeet2():
    def func():
        return 5
    return func()    #  or returns another funcion


# A decorator supercharges our fucntion- a function that changes and enhances antoher funciton. 
# Decorator Pattern 
def my_decorator(func): 
    def wrap_func(*args, **kwargs):
        print('*********')
        func(*args, **kwargs)
        print('*********')
    return wrap_func

"""@my_decorator 
def hello():
    print('helloooo')
    """

@my_decorator
def hello(greeting, emmoji=':)'):
    print(greeting,emmoji )

hello("HI")

"""@my_decorator
def bye():
    print('see ya later')

bye()
"""

hello2 = my_decorator(hello)
hello2("hi")

