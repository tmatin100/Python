backpack = ["sword", "sword", "rubber duck", "slice of pizza", "parachute", "sword"]
print(backpack)


# we are going to create a count variable and generate a set using list
#comprehension. 
#lets use the count function and a for loop to  add the items
# to an empty list name counts. 
#this will count the item however it will count the duplicates as well(sword)
counts = [backpack.count(item) for item in backpack]
print(counts)



#we can use the set fucntion in our loop in order to not count any
#  duplicate items
counts = [backpack.count(item) for item in set(backpack)]
print(counts)

#we can also put the item name in the count inside of the list itself. 
#  This will give you a list of lists with the item and the count.
counts = [[backpack.count(item), item] for item in set(backpack)]
print(counts)

#We can also just print it with out a list and it will just print bunch of print seperate
#statements
[print(backpack.count(item),item) for item in set(backpack)]


