########## REVERSED ITERATOR ##########


data = ["a", "b", "c", "d", "e", "f", "g", "h"]

for item in data: 
    print(item)

print(data)

#a reverse itereator does not change the data but creased a reverese itterator:

for item in reversed(data): 
    print(item)
print(data)

#this is fine untill you have a ton of data in a list
data_reversed = []
for item in reversed(data): 
    data_reversed.append(item)
print(data_reversed)