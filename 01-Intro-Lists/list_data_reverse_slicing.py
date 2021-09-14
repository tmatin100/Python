########## REVERSE USING SLICING ##########

#we can use start stop and step while slicing with [:::]
data = ["a", "b", "c", "d", "e", "f", "g", "h"]
print(data)
print(id(data))

#we are goin gto use slicing to assign the whole list and  that
# will reverse the order. However, keep in mind this does not change the list
#it just changes the content inside the list. If you see the id of the date before
#and after it reamins the same. 

data[:] = data [::-1]
print(data)
print(id(data))