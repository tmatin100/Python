# Filter 


# filter() - The filter functin will return a true or false boolean value 

my_list = [1,2,3,4,5]

def only_odd(item):
   return item % 2 != 0 

# filter accepts a function and an itterable 
print(list(filter(only_odd, my_list)))

#original list remains unchaged 
print(my_list)


