########## Intro to modules ########## 

#A module is just a fancy name for a python file
#By convention, they are often imported at the top of a file
#but you can do it anywhere
import math
#we can use the type() funciton to see what math is, in this case its a class type module
print(type(math))

#We use the module with dot notation to access the functions or variables
#an object of type module
#the math module has diffente methods such as .sqrt() .pi etc. 
print(math.sqrt(25))
print(math.pi)


import pickle
#You will get a path like  
#<module 'pickle' from 'C:\\Users\\Admin .DESKTOP-9R3JN3U\\AppData\\Local\\Programs\\Python\\Python38\\lib\\pickle.py'>
#Check out this: https://docs.python.org/3/py-modindex.html
print(pickle) 


#Here is another example
#Pseudorandom number 0-100 (inclusive)
import random 
print(random.randint(0, 100))

#there are losts of diffente modlues avaialble some of the usefull ones are 
#imported bellow. Rememeber, a module is just a fancy name for a python file
#By convention, they are often imported at the top of a file
#but you can do it anywhere
import math
import pickle
import queue
import heapq  # a data structure
import json   # lets you work with jason data
import random
print(random)