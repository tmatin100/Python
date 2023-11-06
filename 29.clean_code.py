# clean code 

# before 

""" 
def is_odd_or_even(num):
    if num % 2 == 0" 
        return True
    elif num %2 !=0: 
        return False
 """
    

# after   
"""
def is_even(num):
    if num % 2 == 0:
        return True
    return False

"""

# even cleaner 

def is_even(num):
    return num % 2 == 0 
        

print(is_even(50))
print(is_even(51))