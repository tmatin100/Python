#Dictionary Methods
# https://www.w3schools.com/python/python_ref_dictionary.asp
user = {
    'basket' : [1,2,3],
    'greet' : 'hello'
}

print(user.get('age'))

# adds a default value if it doesnt exit
print(user.get('age', 55))

user2 = {
    'basket' : [4,5,6],
    'greet' : 'hello',
    'age' : 20 
}

# does not add a default value if it already exits 
print(user2.get('age', 55))


# create a dictionary using the dict() funciton. 
user3 = dict(name = 'Tam Maitn')
print(user3)


print('age' in user2)

print('age' in user2.keys())
print('hello' in user2.values())

print(user2.items())

user4 = user2.copy()
print(user4)
print(user2)

user4.clear()
print(user4)
print(user2)

print(user.pop('greet'))
print(user)

#removes a random key value pair
print(user2.popitem())
print(user2)

print(user.update({'age' :  55}))
print(user)

