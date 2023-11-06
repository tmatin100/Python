# A for loop lets us itterate over anyting that is itterable 
# itterate - to check  each item one by one in a collection
# itterable is an object or collection that can be itterated over such as a list , dictionary tupple or a stiring. 


for item in 'Zeor to Mastery':
    print(item)


for item in (1,2,3,4,5):
    print(item)

for item in (1,2,3,4,5):
     print(item)
     print(item)
     print(item)
print('hi')
print(item)

for item in (1,2,3,4,5): 
    for x in ['a', 'b', 'c']: 
        print(item,x)

user = {
    'name': 'Golem', 
    'age':  5006, 
    'can_swim': False 
}

for item in user: 
    print(item)


# very important methods in your career: items, vlaues, and keys

for item in user.items(): 
    print(item)

for item in user.values():
    print(item)

for item in user.keys(): 
    print(item)


for item in user.items():
    key,value = item ;
    print(key, value)

for k, v in user.items(): 
    print(k, v)