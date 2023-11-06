# Exercise: Check for duplicates in list: 

some_list = ['a', 'b','b' , 'c', 'd', 'm ', 'n', 'n']

duplicates = []

for value in some_list: 
    if some_list.count(value) > 1: 
        duplicates.append(value)

print(duplicates)


some_list = ['a', 'b','b' , 'c', 'd', 'm ', 'n', 'n']
duplicates = []

for item in some_list: 
    if some_list.count(item) > 1: 
        if item not in duplicates:
            duplicates.append(item)

print(duplicates)