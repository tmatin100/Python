
# *args **kwargs (keywod auruments)

# *args- this can accept any number of positional aurguments passed in
"""
def super_func(*args): 
    print(args)
    return sum(args)
"""

# **keyword args returns a dcitionary of key value pairs

def super_func(*args, **kwargs):
    total = 0 
    for items in kwargs.values():
        total += items
    return sum(args) + total 


print(super_func(1,2,3,4,5, num1=5, num2=10))
      




