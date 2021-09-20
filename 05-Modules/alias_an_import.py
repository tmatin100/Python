########## Alias an import ##########

# if we normally import math and also, caeate a variable named math it will
# replace the math module to the value of the variiable which is 3. 
import math 
math = 3 
print(math)

#the reverse is also true, the math variable will be replaced by the math module 
math = 3 
import math 
print(math)


#if you need to certain varible name that matches with the module name, 
# we can use an alias like this below
math = 3 
print(math)

import math as m 
print(m)


#another example of alias 
from random import randint as r 
randint = 6564564   #variable that has the same name as a module item
print(randint, r)


#This can be used to preserve data locally:
randint = "SUPER IMPORTANT DATA DON'T DELETE!!!!"
from random import randint as r

print("Printing alias of randint as r:", r(0,10))
print("Printing the value of the variable randint:", randint)

