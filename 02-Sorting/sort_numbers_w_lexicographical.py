########## SORT NUMBERS WITH LEXICOGRAPHICAL SORTING ##########

#We can sort numbers similar to strings 1, 11, 111, 2, 22, 222
numbers = [1, 54, 76, 12, 111, 4343, 6, 8888, 3, 222, 1, 0, 222, -1, -122, 5, -30]
numbers.sort(key=str)
print(numbers)

#using the storted function
print(sorted(numbers, key=str))

#Basically, when we are working with strings, 
#"111" < "12"  because we compare by character left to right
#So we can cast each to a str using the str constructor 