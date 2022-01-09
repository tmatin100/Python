########## Create a Class and __init__ ##########
#This section is designed to be a simple introduction to object oriented programming

#What is object oriented programming?
#Well, it allows us to represent anything we want in our code. 
#So far we've represent diffetnet data types using strings, lists, dictionaries etc.
# What if for example we want to use a datatype book? Well, there is no data type for that type. 
#Hence, we can define a custom data type named book. With OOP we can represent any 
# type of data based on our needs. 

#classes- act as a blueprint for an object, however it is not the same as the
#the actual object. ex. a cookie cutter which defines the shape of a cookie object 

#inorder to create a class we use the keyord class and give it a name in this case Book(). 
class Book():
    pass         #we can use the keyord pass to not assign any value



#When we say Book() we are instantiating a new object
#This object is assigned to the book, and book2 variable
#We can use the class Book() to make numerous books:
book =  Book()    #book object
book2 = Book()    #book object 

#Printing it gives us the type and memory location
print(book)
print(book2)

#We can also get the type using the type() funciton:
print(type(book))
print(type(book2))

#We can check type like so:
if isinstance(book, Book):
    print("It is indeed book. Read it")
else:
    print("nope, not a book")

#We can add attributes to any object dynamically like so:
book.title = "The Kite Runner"
print(book.title)


#This is cool and all but every book has a title, so we can make it part of the structure
#This requires a bit more syntax...
#also notice that you can override any class as we go. #the self keyord represents the object

#consider this the constructor, or the function that is invoked when we create a book.
#self refers to the book being created and we don't have to worry about passing that, it's implicit
#Title is passed in as an argument, and assigned to self.title (the title of the book)
class Book():
    def __init__(self, title): 
        # init is an initialzer or a constructor, which is invoked when we create a new book
        self.title = title

book = Book("The Kite Runner")

print(book.title)

#We then pass a title to the Book as we create it:
book = Book("The Kite Runner")
book2 = Book("The Alchemist")
print(book.title)
print(book2.title)

#This will now fail as title is required :)
#book3 = Book()  

#If you want the title to be optional you can give it a default (either a value or None):
class Book():
    def __init__(self, title=None):
        self.title = title

book = Book()
print(book.title) #Still exists just no value.

#This fails as .test doesn't exist.
#print(book.test)
