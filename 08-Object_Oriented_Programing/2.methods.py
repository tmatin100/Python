########## Methods ##########
#A method is just a function attached to an object.
#we creted a method with the method/fucntion initializer or the constructor, aka __Init__ , to create a method/funciton inside this class. 
#Basically __int__ is what's invoked 
#We can define any functions to be attached to our objects by putting them in our class
#We just have to have the implicit parameter self
#anytime we refer to self, we are just refering to the object, it is implicit so we dont passs any parametrs for it. 
class Book():
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages 
        
    #creating a new method called is_long, anytime we create a method we have to pass in the "self" variable.
    #which refers to the object we are creating in this case book.

    #this a custom method called is_long, which is just a function attached to an object named book.
    #anytime we create a method we just have to create a parameter called self. 
    def is_long(self):
        if self.pages > 100: 
            return True 
        return False

#we can invoke the funciton and pass in the values, how ever we dont need to pass the value for self.
#we are just passing in the values for tittle, and pages. 
book = Book("The Kite runner", 168)
print(book.title)
print(book.is_long())

book2 = Book("The Alchemist", 72)
print(book2.title)
print(book2.is_long())


#A note on __init__
#__init__ is also a method, but it's special in that it is invoked automatically
#When we create an object.
#There are a lot of methods with a similar naming structure we are going to see. 
#__eq__, __hash__, __str__, etc. 
