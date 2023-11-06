# List Methods
# a method is an action owned by a specefic data type
# https://www.w3schools.com/python/python_lists_methods.asp

print('-------------adding--------------------')

basket = [1,2,3,4,5]

print(len(basket))

#adding 
basket.append(100)     # new_list = basket.append(100) will create a value of NONE

print(basket) 

new_list = basket 

print(new_list)

#.insert() allows you to insert something anywhere in the list with an index and an object.
# it modifies the list in place. 

basket.insert(5, 200)


# .extend(), lets you itteerate over a list
basket.extend([101,201])

print(basket)

print('-------------removeing---------------------')
# removing
#.pop() removes the index and returns a vlaue at the index 

basket.pop()
print(basket)
print(new_list)

# .remove() removes the value 
basket.remove(4)
print(basket)


# .clear() removes everyting in the list 
basket.clear()
print(basket)



# .index() , gives you the index of a value entered
basket = ['a', 'b', 'c', 'd', 'e']

print(basket.index('d'))
print(basket.index('d',0,4))  #start, stop, step

print('d' in basket)
print('x' in basket)
print('i' in 'hi myname is Ian')

#.count() counts how many time the item exits
print(basket.count('d'))

#.sort() sorts the list in place 
basket = ['a', 'b', 'c', 'd', 'e', 'd', 'f']
print(basket)
basket.sort()
print(basket)

#sorted function, creates a new array
basket = ['a', 'x','b', 'c', 'd', 'e', 'd', 'f']
print(sorted(basket))

print(basket) # remains unchanged 

# .reverse() reverses the index vlaues in reverse
basket.reverse()
print(basket)

basket.sort()
print(basket)

basket.reverse()
print(basket)


# we can also servese it back with slicing method , this will create a new list and will not modify the original list
print(basket[::-1])
print(basket)

# generate a list with the range() and the list() funciton
print(list(range(100)))   # prints 0 to 99
print(list(range(1,100)))  # prints 1 to 199
print(list(range(101)))  # prints 0 to 100

#.join(), a string method 

sentence = ' '
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'Sky'])
print(new_sentence)

#shorthand way of doing this
new_sentence2 = ' '.join(['hi', 'my', 'name', 'is', 'Tamzidul'])
print(new_sentence2)

# List Unpacking - assigns variables to the values of the list 
list1 = [1,2,3,4,5,6,7,8,9]
a,b,c, *other, d =[1,2,3,4,5,6,7,8,9]
print(list1)
print(a)
print(b)
print(c)
print(other)
print(d)

# None is a special data type that represents the apbsene of value 
a = None
print(a)
