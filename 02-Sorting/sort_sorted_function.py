#The sorted funcion can take an iterable as an aurgument ex. sorted(List)
#When we need to make a copy of the data, the sorted fucntion works great.
#however if you are fine modying the original list then the .sort() is recomended

#This returns a NEW list. so original is unaffected!
numbers = [1, 11, 115, 13, 1305, 43]
print(id(numbers))

numbers_sorted = sorted(numbers)

print(numbers)
print(id(numbers))

print(numbers_sorted)
print(id(numbers_sorted))


#This also allows us to assign a sorted listed immediately.
numbers = sorted([1, 11, 115, 13, 1305, 43])
print(numbers)
print(id(numbers))