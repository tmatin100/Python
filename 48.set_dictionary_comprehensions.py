# set comprihensions


my_list_1 = {num for num in range(0,100)}
my_list_2= {num**2 for num in range(0,100)}

#print(my_list_1)
print(my_list_2)

# dictionary comprehnsion

simple_dict = {'a':1, 'b':2}

my_dict = {key:value**2 for key,value in simple_dict.items()}

my_dict2 = {num:num*2 for num in [1,2,3]}

print(my_dict)
print(my_dict2)