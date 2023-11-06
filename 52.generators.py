# Genereator is a subset of a itterable 


# iterable 
# __iter__

"""
range(100)  # does not live in memory 

list(range(100))    # list creates a list in memoy 

def make_list(num):          # same as list(range(100))
    result =[]
    for i in range(num):
        result.append(i*2)
    return result 

my_list = make_list(100)
print(list(range(10000)))

"""



# Generator 

def generator_function(num): 
    for i in range(num): 
        yield i*2                # yeld pauses function and comes back to it when next() is called 
                                  # next can be calle as many time s as long as the range does not expire 

g = generator_function(100)
#next(g)
#next(g)
print(next(g))
print(next(g))
print(next(g))


""" 
for item in generator_function(1000):
    print(item)

"""





