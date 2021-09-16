########## JOIN ##########

# the .split() method takes a string and seperates the com
data = "this is data"
d = " "
data = data.split(d)
print(data)

# the .join() method does the opposite, it puts them together 
data = d.join(data)
print(data)

data = ["01001100", "01001111", "01001100"]
print(".".join(data))
print("-".join(data))


# we can join strings and integers together with a list comp type loop
#to do that we actually need to convert each element to a string

data = ['this','is','data', 5, 10 ]

#we dont want this becasue we are actually converting the whole list into a string

print(" ".join(str(data)))

#What we need to do is convert each elements in the list to a string and join them together
#the join method take an itterable, so we can use a for loop to do this
#100% original idea stolen from this guy
#https://stackoverflow.com/questions/3590165/join-a-list-of-items-with-different-types-as-string-in-python
#this is also known as a generater expression

print(" ".join(str(i) for i in data))


