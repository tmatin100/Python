# Scope - what variables do I have access to? \

#1. Start with local 
#2. Prent local? 
#3. Global
#4. built in python funcitons


#global scope 
a = 1

# Local Parent scope 
def parent(): 
    def confusion(): 
        # builtin python function 
        return sum 

    # local scope 
        #a = 5
       # return a
    return confusion()


print(parent())
print(a)

# global variable
total = 0 

def count():
    # refers to the global variable
    global total
    total +=1
    return total

count()
count()
print(count())


# non local 

def outer(): 
    x = "local"
    def inner(): 
        nonlocal x
        x = 5