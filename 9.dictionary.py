# Dictionary , is an unodered key value pair. Dictionay keys has to be immutable and cannot be changed. Keys has to be unique


dictionary = {'a': [1,2,3], 
              'b': 'hello!',
              'c': True
              }

print(dictionary['a'])

#print the value of a th index of 1 
print(dictionary['a'][1])


#A list of dictionary 
my_list = [ 

{
'a': [1,2,3], 
'b': 'hello!',
'c': True
}, 

{
'a': [4,5,6], 
'b': 'hello!',
'c': True
}
]

print(my_list[1]['a'])
print(my_list[1]['a'][2])


dictionar_2 = {'weapons': [1,2,3], 
              'greetings': 'hello!',
              'is_Magic': True
              }

print(dictionar_2)

