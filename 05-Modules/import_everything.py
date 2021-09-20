########## import * ##########

#We now we can bring one specific item from a module using 
from random import randint

#This puts it directly in our symbol table replacing anything called randint
#You will see sometimes importing everything, even though it's not recommended
#100% guarentee 30% of the time to yeet out something important:

seed = "watermelon"
from random import *

print("Today we are going to plant", seed, "seeds! Yay!") #Not what we wanted. 

#We can get a better picture of this by printing the output of dir()
#which shows the identifiers in scope

a, b, c, e, f, g = 0, 0, 0, 0, 0, 0 #find these:
print(dir())

