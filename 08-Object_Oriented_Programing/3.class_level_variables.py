########## Class Level Variables ##########

#We're going to talk about class level variables.
#Coming from another language, this would be the closest thing to "static" members
#First, we need to understand self.

#self refers to the object things are being invoked on,
#When we create an object, __init__  assigns stuff to self
#That allows each object to have attributes.

#Any time we create a method, we have self as a parameter.
#This means the method is attached to each object.

#if we leave off self, we are creating it at the class level, which is shared for all objects

#Book() is the class

class Book():
    favorites = []  # class level variable, does not have self like bellow 

    def __init__(self, title, pages): 
        self.title = title
        self.pages = pages
    
    def is_long(self):
        if self.pages > 100: 
            return True
        return False 

#we are creating objects named book and book1 here using the Book() class
book = Book("The Kite Runner", 168)
book2 = Book("The Alchemist", 72)

# we are refereing to the class Book() here (Book.favorites), and not creating objects like above (book = ) . 
Book.favorites.append(book)
Book.favorites.append(book2)

#Favorites is related to books, but not tied to one individual book
#We use self as a parameter if it's unique to each object :)
print(Book.favorites)

#for every single book in this list we are going to print the tittle attribute
for b in Book.favorites:
    print(b.title)




    


