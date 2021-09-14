# we are going to count a particular element in a list. 

#The len function gives you the length of the list which is the total number
#number of elements in a list, in this case there are 4 items in a list so the result is 4. 

backpack = ["sword","rubber duck", "slice of pizza", "parachute"]


print(len(backpack))

# If we want to count how many times a particular item exists in a list we 
# can use the count function like this:

print(backpack.count("sword"))

#if you would like to cap the number of item in a list you can use a condtion like this: 
#this will add a sowrd to the end of the list
if backpack.count("sword") < 5:
    backpack.append("sword")

print(backpack)

# if you would like to check how many items exists you can use the count function like this: 

if backpack.count ("sword") >= 1

# or you can do this:   

if "sword" in backpack 
