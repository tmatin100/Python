########## Methods ##########
#A method is just a function attached to an object.
#We can define any functions to be attached to our objects by putting them in our class
#We just have to have the implicit parameter self

#Let's create an object named Book

class Book():
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages 
    #creating a method- anytime we create a method we have to pass the self variable.
    #which refers to the object we are creating in this case Book().

    #this a custom method called is_long, which is just a function 
    # attached to an object named Book().
    def is_long(self):
        if self.pages > 100: 
            return True 
        return False

#we can invoke the Book() funciton and pass in the values
book = Book("The Kite Runner", 72)

print(book.title)
print(book.is_long())

# can check another using the same custom Book() function we've created
book2 = Book("The Alchemist", 168)
print(book2.title)
print(book2.is_long())


#A note on __init__
#__init__ is also a method, but it's special in that it is invoked automatically
#When we create an object.
#There are a lot of methods with a similar naming structure we are going to see. 
#__eq__, __hash__, __str__, etc. 
