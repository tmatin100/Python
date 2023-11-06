#Tuples are like immutable lists , once created it canot be changed 
# https://www.w3schools.com/python/python_tuples_methods.asp


my_tuple = (1,2,3,4,5,5)
print(my_tuple[1])
print(5 in my_tuple)

# we can use a tuple as a key in a dictionary since it is immutable
user = {
    (1,2) : [1,2,3],
    'greet': 'hello', 
    'age' : 20 
}

print(user[(1,2)])

# sliciing Tuple
my_new_tuple = my_tuple[1:2]
print(my_new_tuple)
print(my_tuple)

# unpacking wiht tupple
#x,y,z *other = (10,20,30,40,50)
#print(x)
#print(y)
#print(z)
#print(other)


#Tuple mthods
print(my_tuple.count(5))

# find the index of something 
print(my_tuple.index(4))

print(len(my_tuple))
