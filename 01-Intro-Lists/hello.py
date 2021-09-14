print("Hello, World!")

########## APPEND TO LIST #########

healthy = ["pizza", "frozen custard"] #healthy is an example of an object

# we can access this object's members with a .notation aka a method. A method is function attached to an object. In this case we used the .append() method to attach 
#a new item to the list 

healthy.append("apple crisp") 
print(healthy)

#we also have stand alone fuctions such as lengh(), which is not attached to any object.
#Therefore,we need to pass in a data which is called an aurgument, to such fucntions. 
# in this case we are passsing the healthy list object created earlier as an aurgument to the len function and assigning it to a variable named length. 
length = len(healthy)

#we can pss in multiple aurguments for example a string "lenght:"
print("length:", length)



########## CHECKING IF ELEMENT IN LIST #########

healthy = ["pizza", 'frozen custard", "apple crisp",]

print("chicken pot pie" in healthy)
