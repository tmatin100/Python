# debuggging

#linting
# use ide/editor

# SyntaxError
# TypeError
# NameError
#pdb - python debuding module https://docs.python.org/3/library/pdb.html

# usefull pdb commands t, a, w 
import pdb

def add(num1, num2):
    pdb.set_trace()
    t = 4*5
    return num1 + num2

add(4, 'aaskdfj')

