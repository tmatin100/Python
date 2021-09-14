########## REVERSE LIST ##########
#a list is sequential which means the order maters in a list 
data = [0,1,2,3,4,5]
data.reverse()
print(data)


#if there is a list insie a list, it will order the entire
#  nested list as one item.

data = [0,1,2,3,4, [1,2,3]]
data.reverse()
print(data)

data = [0,1,2,3,4,5]
data_copy = data[:]
print(data, data_copy)


########## SWAP AND REVERSE ALGORITHMS ##########
#In python you can swap two variables on the left of an assignment, and then 
#putting them in the opposite order on the right hand of the assignment

data = ["a", "b", "c", "d", "e", "f", "g", "h"]

me = "Caleb"
you = "Subscriber"
print(me, you)

me, you = you, me 

print(me, you )


temp = me
me = you 
you = temp 

print( me, you)


#REVERSE ALGORITHMS

data = ["a", "b", "c", "d", "e", "f", "g", "h"]

index = 1 

print(data[index])
print(data[-index])
print(data[-index-1])
print(data[index], data[-index-1])


data = ["a", "b", "c", "d", "e", "f", "g", "h"]

index = 0 

print(data[index], data[-index-1])

data[index], data[-index-1] = data[-index-1], data[index]

print(data[index], data[-index-1])
