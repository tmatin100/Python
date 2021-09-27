######### REMOVE DUPLICATES FROM LIST / CREATE SET FROM LIST ##########

#You can remove duplicate elements from a list by converting it to a set and back. 

colors = ["red", "red", "green", "green", "blue", "blue", "blue"]

#list id prior to making changes bellow
print(id(colors), colors)

# colors = will replce the entire list in the memory 
#if we need to keep the same area of memory in the list, then we can use  [:]
#we are using the set function inside a list fucntion to convert the items 
# into a set and then back to a list and reassigning the value to the same list
colors[:] = list(set(colors))

#list id after maknig changes above. Notice that the order is not the same, since
#sets are always undorderd. You can use other solutions like using a
#the sorted function to sort the data any way you'd like. 
print(id(colors), colors)


#Earlier on in our life we used some code to count each type of element in a list. 
#notice you are replacing the colors variable in the memory. However, 
#if you have aliases pointing towards this list you might get some wired
#bugs so just be carefull when suing this method. 
colors = ["red", "red", "green", "green", "blue", "blue", "blue"]

#we can do the same using listh comprehension
#we converted the data into set since we dont want to count duplicates
count = [[colors.count(item), item] for item in set(colors)]

print(count)

#This works because is iterates through the set {"red", "green", "blue"} counting each in colors

