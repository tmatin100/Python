
# Write a function that will find and print the highest even number from a list 


def highest_even(li):
    evens = [] 
    for item in li : 
        if item % 2 == 0 : 
            evens.append(item)
    # the max function takes an itterable and returns a max value 
    return max(evens)


print(highest_even([10,2,3,4,8,11]))