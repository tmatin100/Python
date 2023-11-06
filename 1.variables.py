# Constants
PI = 3.14

#augmented assigment operator
some_value = 5
some_value += 2

print(some_value)


#string
print(type("hi hello there 24!"))

username = "supercoder"
passowrd = "supersecret"

long_string = """

WOW
0 0 
---

"""

print(long_string)



first_name = 'Tamizdul'
last_name = 'Matin'

full_name = first_name + " " + last_name

print(full_name)

#string concatenation (only works with strings, sring plus an integer wont work)
print('hello' + 'world')

# type conversion of data types
print(type(int(str(100))))

a = str(100)
b = int(a)
c = type(b)
print(c)

#escape sequence 

# weather = ' It's sunny' 
# /t = tab
# /n = new line 

weather = "\t It\'s\"kind of\" sunny \n hope you have a great day!"

print(weather)

#formatted strings
name = 'Johnny'
age = 55

print('hi ' + name + '. you are ' + str(age)+ ' years old ')


#Formated string using f string funciton in python 3

print(f'hi {name}. You are {age} years old')

#.format
print('hi {}. You are {} years old'.format(name, age))
#print('hi {1}. You are {0} years old'.format(name, age)
      
print('hi {new_name}. You are {new_age} years old'.format(new_name='Sally', new_age=100))

