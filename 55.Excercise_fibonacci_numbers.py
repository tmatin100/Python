# Fibbinaci Numbers using a geneorator fucntion
#  https://en.wikipedia.org/wiki/Fibonacci_sequence


def fib(number):  # takes the index number of the fibbonacci numbers
    # a and b are the start of the fibbinacic f1 f2 numbers 
    a = 0 
    b = 1 
    # were going to use the range generator to loop through the function
    for i in range(number):
        yield a     # return the value of a first 
        temp = a  # holds a temporary value of a which is 0 at this point so it doesnt change until we get to first a + b
        a = b      # we will modify a to be equal to b which is 1 
        b = temp + b  # add a to b  which is 0 + 1 


for x in fib(20):
    print(x)



# Use a List. This is slower than a generator 

def fib2(number):
    a = 0 
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        temp1 = a 
        a = b 
        b = temp1 + b 
    return result   

print(fib2(100))
