########## __hash__ and Collections ##########

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

    #If should immutable, you could do something like this. 
    #This replaces __hash__ = None
    def __hash__(self):
        return hash(self.title) ^ hash(self.pages) #xor with hash of attributes
        #from Mastering Object-Oriented Python

book = Book("Are You My Mother", 72)
print(book)
equal_book = Book("Are You My Mother", 72)
print("Are they considered equal?", book == equal_book) #yep
print("Are they the same object?", book is equal_book) #nope
book2 = Book("The Digging-est Dog", 72)

print(hash(book), hash(book2))

print("old hash", hash(book))
book.title = "new"
print("new hash", hash(book)) #BAD!!! 
#Hashes shouldn't change