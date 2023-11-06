# While Loop

i = 0 
while i < 5 : 
    print(i)
    i += 1
else: 
    print('done with all the work')  
    


# this will do the saame as above
i = 0 
while i < 5 : 
    print(i)
    i += 1
print('done with all the work')   


# the else block will not execute since there is a break in the while loop
i = 0 
while i < 5 : 
    print(i)
    i += 1
    break
else: 
    print('done with all the work')   


my_list = [1,2,3]
i = 0 
while i < len(([my_list])): 
    print(my_list[i])
    i+=1


# Break
# Continue
# Pass
while True: 
    response = input('say something: ')
    if (response == 'bye'): 
        break

# goes back to the loop and skips the print staement 
while True: 
    while i < len(my_list): 
        print(my_list[i])
        i += 1
        continue
        print(item)

# is a placeholder for a code, it does absolouty nothing 
while True: 
    response = input('say something: ')
    pass



