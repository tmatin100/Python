########## Creating a Module ##########

#We can easily create our own module by just creating a python file
#Any variables or functions will be imported
#In this case we have created an utils.py seperately, which contains
#this fucntion:  
"""
def stats_range(data):
    sorted_data = sorted(data)
    return sorted_data[-1] - sorted_data[0]  
"""

import utils
print( utils.stats_range([5, 3, 5, 1, 10]))



