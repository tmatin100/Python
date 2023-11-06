# Methods vs. Functions
"""
list()
print()
max()
min()
input()
"""

def some_random_stuff(): 
    pass

some_random_stuff()

# methods use a .
name = 'name'.capitalize()
print(name)

# Docstrings are helpfull methods to put comments and notes inside a function 

# method 1 with the help function 
def test(a):
    ''' 
    Info: this funciton tests and prints param a
    '''
    print(a)

help(test)

# method 2 
print(test.__doc__)


