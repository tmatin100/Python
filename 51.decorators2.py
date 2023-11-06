#Custtom  Decorator 


from time import time 
def performance(fn):
    def wrapper(*args, **kawargs):
        t1 = time()
        result = fn(*args, **kawargs)
        t2 = time()
        print(f' It took {t1-t2} ms to run this function.')
        return result
    return wrapper


@performance
def long_time():
    for i in range(100000000):
        1*5

long_time()

# web frameworks like Django and Flask use decorators 

