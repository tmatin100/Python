########## Passing by Object Reference ##########
# When passing objects to functions, we have the risk that the functions change the data. 
# If the function replaces the data with a new object, it does not alter the original object.
# As soon as we assign us a new object, that origilan reference is gone. 
# This concept of how this object is passed is known as "Passed by object reference"
# So, when we are pssing a reference to an object, and then we replace the reference, there is no longer a connection there. 


class Book():
    favs = [] #class

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def is_short(self):
        if self.pages < 100:
            return true

    #What happens when you pass object to print?
    def __str__(self):
        return f"{self.title}, {self.pages} pages long"

    #What happens when you use ==?
    def __eq__(self, other):
        if(self.title == other.title and self.pages == other.pages):
            return True
    
    #It's approriate to give something for __hash__ when you override __eq__
    # #This is the recommended way if mutable (like it is here):
    __hash__ = None


#Even though we have the same data they are two diffent books
book1 = Book("The Alchemist", 100)
book2 = Book("The Alchemist", 100)

print(book1)
print(id(book1))

print(book2)
print(id(book2))

#When we do this we bassicaly create two variables pointing to the same item in the memory store
print("When we do this we bassicaly create two variables pointing to the same item in the memory store")
book2 = book1

print(id(book1))
print(id(book2))

#we can also varify if two objects are in the same memory by doing something like this 
print("we can also varify if two objects are in the same memory by doing something like this ")
print(book1 is book2) # its  a short hand of 
print(id(book1) == id(book2))

#if the have the same data but different objects in diffent memories. this is important when we are dealing with functions and pssing objects to them. 

book3 = Book("The Kite Runner", 168)
book4 = Book("The Kite Runner ", 168)

print("if the have the same data but different objects in diffent memories. this is important when we are dealing with functions and pssing objects to them")
#print(book3 == book4)
print(id(book3) == id(book4))
print(book3 is book4)

#lets create a fucntion to change the data (attributes) of an object, withouth changing the id of the data in the memory.  
print("#lets create a fucntion to change the data (attributes) of an object, withouth changing the id of the data in the memory")

book = Book("Are you my mother?", 72)
print(id(book))

def modify_attribute(book):
    print(id(book))   #id remains the same before we changed the data 
    book.title = "Something new"   #this changes 
    print(id(book))  #id remains the same after we changed the data 

modify_attribute(book) 

print(book)



#lets assign a new book in side the fucntion, which will create a new book in memory, hence the id will change.
 
print("#lets assign a new book in side the fucntion, which will create a new book in memory, hence the id will change.")

book = Book("Are you my mother?", 72)
print(id(book))

def modify_object(book):
    print(id(book))   #id before we changed the data 
    book = Book("Something new", 100)  # this does not change
    print(id(book))  #id changed after we changed the data 

modify_object(book) 

# However, anytime we create a variable to modify the object within a function,  the the data will not change the original object
print("#However, anytime we create a variable to modify the object within a function, the the data will not change original object")

# We are still getting the original data from the inital book = Book("Are you my mother?"" , 72) object which is located oustde of the function. 
print('# We are still getting the original data from the inital book = Book("Are you my mother?"" , 72) object which is  located oustde of the function.')
print(book)  

########SUMMARY#########
# Passing objects to functions, we have the risk that the functions change the data. If the function replaces the data with a new object, that does not alter the original object.
# As soona as we assign us a new object, that origilan reference is gone. 
# This concept of how this object is passed is known as "Passed by object reference"
#So, we are pssing a reference to an object, but if we replaceing the reference, then there is no longer a connection there. 