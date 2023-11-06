# Working with Files I/O in python

# pyehon has a built in function called open that allows us to read write files

#read ( morde = 'r' by default)
with open('test.txt') as my_file: 
    print(my_file.readlines())


# read + write with mode = 'r+' # reads and it over writes , write just starts form beggining and over writes it 
with open('test.txt', mode='r+') as my_file: 
    text = my_file.write ('hey it\'s me !')
    print(text)

#write mode creates a new file if it doesnt exist
with open('happy.txt', mode = 'w') as my_file:
    text = my_file.write(':)')
    print (text)


# add/append to end of the file:  append with mode = 'a'
with open('test.txt', mode='a') as my_file: 
    text = my_file.write (':)')
    print(text)


# read from a diffent directory 
#with open('/User/tmatin/downloads/happy.txt', mode ='r') as my_file:
   # print(my_file.read())

# pathlib module 
# https://docs.python.org/3/library/pathlib.html


# File IO Errors
try : 
    with open ('sad.txt', mode ='r') as my_file:
        print(my_file.read())
except FileNotFoundError as err: 
    print('file does not exist')
    #raise err 

# I/O error - 

