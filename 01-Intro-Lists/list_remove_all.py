########## REMOVING ALL OCCURANCES IN LIST ##########

backpack = ["pizza slice", "button", "pizza slice", "fishing pole", 
"pizza slice", "nunchucks", "pizza slice", "sandwich from mcdonalds"]

backpack.remove("pizza slice")
print(backpack) #SO MUCH PIZZA!

#this will go thorugh all the items tons of times, and not effecient when there are 
#huge amount of items, in shuch case this is not very scalalble 
#This may not be the most optimized solution as each removal requires
#an iteration from backpack.count. 
#You should also avoid modifying a list while iterating, so a for-in loop is bad
while backpack.count("pizza slice") > 0:
    backpack.remove("pizza slice")
print(backpack) 


backpack = ["pizza slice", "button", "pizza slice", "fishing pole", 
"pizza slice", "nunchucks", "pizza slice", "sandwich from mcdonalds"]
#slicing
print(backpack[3:5])


backpack = ["pizza slice", "button", "pizza slice", "fishing pole", 
"pizza slice", "nunchucks", "pizza slice", "sandwich from mcdonalds"]
#an effective way to make a copy of a list 
backpack2 = backpack[:]
#these are two diffente items in the memory 
print(id(backpack))
print(backpack)
print(id(backpack2))
print(backpack2)

#keep the list but repace the data with [:], which is same item in the memory
print(id(backpack))
backpack[:] = [1,2,3]
print(backpack)
print(id(backpack))


#replace the entire list withouth [:], which is a brand new object 
print(id(backpack))
backpack = [1,2,3]
print(backpack)
print(id(backpack))



#The original solution is fine for removing data from reasonably sized lists
#Here is a better solution for list with large data:
backpack = ["pizza slice", "button", "pizza slice", "fishing pole", 
"pizza slice", "nunchucks", "pizza slice", "pizza slice", "sandwich from mcdonalds"]

for item in backpack:
    print(item)
    if item == "pizza slice":
        backpack.remove(item)

print(backpack)

#However, we are breaking on of the fundemtal principles of list, which is we
#never remove an item from a list when we are using a for loop in python. When you 
#do this it jynx up the all the indexes and it doesnt work the way you expect. 
#because when we remove it shifts one space to left so we end up getting every 
#other item in the list


# A better way to do it is to copy , where the indexs are going to be based on 
#copy so the indexes dont shift

backpack = ["pizza slice", "button", "pizza slice", "fishing pole", 
"pizza slice", "nunchucks", "pizza slice", "pizza slice", "sandwich from mcdonalds"]

for item in backpack[:]: #uses copy to keep index
    print(item)
    if item == "pizza slice":
        backpack.remove(item)

print(backpack)

#final conclustion: Whenever, we need to remove an it from a list, we need to
# use a copy, ([:]). 

#or we can assaign it to a a new empty list. This

backpack = ["pizza slice", "button", "pizza slice", "fishing pole", 
"pizza slice", "nunchucks", "pizza slice", "pizza slice", "sandwich from mcdonalds"]

new_backpack = []

for item in backpack[:]: #uses copy to keep index
    print(item)
    if item != "pizza slice":
        new_backpack.append(item)

print(new_backpack)


#another way to do this, notice it will create two diffent lists:

backpack = ["pizza slice", "button", "pizza slice", "fishing pole", 
"pizza slice", "nunchucks", "pizza slice", "pizza slice", "sandwich from mcdonalds"]
print(id(backpack))

new_backpack = []

for item in backpack[:]: #uses copy to keep index
    if item != "pizza slice":
        new_backpack.append(item)

backpack = new_backpack

print(backpack)
print(id(backpack))


#Here is a list comprehension version, notice it will create two diffent lists in the memory space


backpack = ["pizza slice", "button", "pizza slice", "fishing pole", 
"pizza slice", "nunchucks", "pizza slice", "pizza slice", "sandwich from mcdonalds"]
print(id(backpack))

backpack = [item for item in backpack if item != "pizza slice"]
print(backpack)

print(id(backpack))


#if we need to keep the same list in the memory, then we need to use slicing [:]


backpack = ["pizza slice", "button", "pizza slice", "fishing pole", 
"pizza slice", "nunchucks", "pizza slice", "pizza slice", "sandwich from mcdonalds"]
print(id(backpack))

backpack[:] = [item for item in backpack if item != "pizza slice"]
print(backpack)

print(id(backpack))
