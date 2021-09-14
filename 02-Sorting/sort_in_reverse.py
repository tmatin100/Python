########## SORT IN REVERSE ##########


#You can easily get a reverse sorted list.
numbers = [1, 32, 54, 34, 65, 11, 100, -1, 3]
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

#However, sorted has an optional/default parameter
#We can pass a value to it

print(sorted(numbers, reverse=True))
