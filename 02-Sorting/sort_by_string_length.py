########## SORT BY STRING LENGTH ##########

random = ["a", "A", "aa", "AAA", "HELLO", "b", "c", "a"]

random.sort(key=len)
print(random)
print(id(random))


#no () on function! len refers to function. len() invokes function
#using the sorted funciton. slicing [:], changes the original list, as you 
# can see the id of the both lists are same. 
random[:] = sorted(random, key=len)
print(random)
print(id(random))


#removing slciing cretes a new list , as you cna see the id is diferent
random = sorted(random, key=len)
print(random)
print(id(random))