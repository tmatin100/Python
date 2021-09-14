
#print(len(["hi","hello","wassap"]))

greetings = ["hi","hello","wassap"]
#print(greetings)
#print(greetings[2])

#print(len(greetings))

#n is the list size
#highest index = n-1

for item in greetings: 
    print(item)

#you can use i and the range function to access length of  the index of the list.
for i in range(len(greetings)):
    print(i, greetings[i])