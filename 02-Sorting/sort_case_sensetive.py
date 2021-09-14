
########## CASE INSENSITIVE SORT ##########

#When working with strings, 'a' and 'A' are different.

strings = ['a', 'A', 'abc', 'ABC', 'aBc', 'aBC', 'Abc']

strings.sort(key=str.lower)  #Capital is considered first

print(strings)



#When working with strings, 'a' and 'A' are different.

letters = ['a', 'A', 'abc', 'ABC', 'aBc', 'aBC', 'Abc']

print(sorted(letters)) #Capital is considered first
print(sorted(letters, key=str.lower))

