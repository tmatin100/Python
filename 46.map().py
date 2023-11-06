# map()- The map functin allows us to take an acion on an itterable
"""""
def multiply_by2(li):
    new_list = []
    for item in li: 
        new_list.append(item*2)
    return new_list

print(map(multiply_by2, [1,2,3]))
"""
my_list = [1,2,3,4,5]

# with the map funtion
def multiply_by2(item):
    return item*2

#returns a map object which needs to be converted to a list with the list funtin
print(list(map(multiply_by2, my_list)))

#outside of the function
print(my_list)