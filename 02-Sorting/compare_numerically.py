########## COMPARE NUMERICALLY ##########

#Just like we compared using strings in the previous section, we can do it with numbers
#Talse is 0
#True is 1
#expression evaluates to true and maintains that value
#No data is converted to a float in list. Strings are still strings. #bools are bools.

age = 5
stuff = [True, False, 0, -1, "0", "1", "10", age < 30, "20", "2", "5", "9001", "5.5", "6.0", 6]
stuff.sort(key=float)
print(stuff)

#use the sorted fucntion 
print(sorted(stuff, key=float))


