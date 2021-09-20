
# As an alternative, we can import one specific thing from the module
from random import randint 

print(randint(0,10))
print(type(randint))

#this line will no longer work since we didnt import the entire random module
#  print(type(random))

# We can also import multiple things from a module 
from random import randint, seed
print(type(seed))

#This replaces anything locally called randint:
from random import randint 
seed = "apple"

#this will replace the value of apple with the module item seed. 
from random import seed
print(seed)


