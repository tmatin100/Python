# Generators Performance 

from time import time 
def performance(fn):
    def wrapper(*args, **kawargs):
        t1 = time()
        result = fn(*args, **kawargs)
        t2 = time()
        print(f' It took {t1-t2} ms to run this function.')
        return result
    return wrapper

# Faster since with a genator we dont hold things in memory 
@performance
def long_time():
    print('1')
    for i in range(10000000):  # holds each item on by one in memory and removes before going to the next item 
        i*5 

# Slower since it holds everything in memory first with a list then itterates 
@performance
def long_time2():
    print('2')
    for i in list(range(10000000)):   # creates a list of everythig first then iterates though each item 
        i*5

long_time()

long_time2()

