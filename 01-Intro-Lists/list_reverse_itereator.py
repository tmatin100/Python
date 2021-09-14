########## SWAP AND REVERSE ALGORITHMS ##########
#we can swap each element at a time using a for loop

data = ["a", "b", "c", "d", "e", "f", "g", "h","i"]
print(data)

#We are only going to go to the range of the half of the data or else it will 
#will put everything back to current order. However, we also need to make sure
#we are using  floor // devision otherwise well get an error. Also, we 
# dont need to worry about an odd nubmer, becuase if there is one it will 
#just stay in the middle in this case the letter the index of the letter e.
#This is going to run in Big O of N because we are just doing 
# a few operations for each elements in the list. If the list list size
# doubles, we are not doing exponetially more work, were just 
# doing double the work. For space complexity this in an  in place algorhytm. 
#We are not going outside and creating another list. We are just modifying it from
#within. 

for index in range(len(data) // 2):
    data[index], data[-index-1] = data[-index-1], data[index]

print(data) 