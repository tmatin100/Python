# Set 
# A set is a collection which is unordered, unchangeable*, and unindexed. No duplicates 
# https://www.w3schools.com/python/python_sets_methods.asp

my_set = {1,2,3,4,5,5}
print(my_set)

my_set.add(100)

# 2 is not added since it already exists
my_set.add(2)

print(my_set)

# use the set() function to convert a list into a set

my_list = [1,2,3,4,5,5]

my_set = set(my_list)
print(my_list)
print(my_set)

print(1 in my_set)

print(len(my_set))

new_set = my_set.copy()
print(new_set)

my_set.clear()
print(my_set)

#covert a set into a list 
print(list(my_set))

