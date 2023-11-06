
# == checks for value

print(True == 1)
print('' == 1)
print([] == 1)
print (10 == 10.0)
print([] == [])
print([] == {})

print(bool([]))
print(bool({}))

print(bool([1]))
print(bool({3}))


# is interperetes the locaiton in memory
print('is interperetes the locaiton in memory') 
print(True is True)
print("1" is "1")

# data structures are created in different locations
print('' is 1)
print([] is 1)
print (10 is 10.0)
print([] is [])
print([1,2,3] is [1,2,3])
print([] is {})
