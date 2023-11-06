# List is an ordered sequence of obect of any type
# Lists are mutable 
# A data structure is a way to organize our data 

li = [1,2,3,4,5]
li1 = ['a', 'b','c', ]
li2 = [1,2,2.5,'a', True]



amazon_cart = ['notebooks', 'sunglasses' ]
print(amazon_cart)
print(amazon_cart[0])
print(amazon_cart[1])

print('-------------------------------------')

# List slicing 
amazon_cart2  = [
    'notebooks', 
    'sunglasses', 
    'toys', 
    'grapes']

print(amazon_cart2)
print(amazon_cart2[0::2])

amazon_cart2[0] = 'laptop'
print(amazon_cart2)

# with list slicing we are creating a new list here
new_cart = amazon_cart2[0:3]
print(new_cart)

#old cart still remains the same. 
print(amazon_cart2)

# what happens if we do this? it points to the amazon_cart2 list in the memory, does not create a new list.
new_cart = amazon_cart2
print(new_cart)
print(amazon_cart2)