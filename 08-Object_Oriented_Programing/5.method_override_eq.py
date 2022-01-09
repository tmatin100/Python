######################## __eq__ ###############################
#We going to use the __eq__ method to compare two book objects. 

class Book():
    favorites = [] #class level attribute or variable

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def is_short(self):
        if self.pages < 100:
            return true

    def __str__(self):
        #return "5"
        return f"{self.title}, is {self.pages} pages long"

book = Book("The Kite Runner", 168)
book2 = Book("The Alchemist", 72)

#Lets say we are comparing the two book objects, the default behavior of the == is to see if they are using the same area of the 
#memory or if they are the same exact object.

#Therefore, we get a false becasue these objects are in not in the same area of the memory. 
print(book == book2)

#in order for that to happen we have to set book2 = book
book2 = book
#and now we get a value of True since its pointing to the same location in the memroy
print(book == book2)

#However, thats not what we want, and would rather compare it by the tittle and the page number (methods/attributes). 
#Lets compare two books, but lets say they have the exact same data. Printing it now we get a False, however, we want it to be true in this 
#situation since they are the same exact books even though tye are diffent objects. 
book = Book("The Alchemist", 72)
book2 = Book("The Alchemist", 72)

#priting it now, it is the same book, however that is not true, since they are two diffent book objects. 
print(book == book2) 

#We are going to check if the pages and titles of self vs. the other book is the same using the __eq__ constructor
#we are going to create a self attribute for book one and other attribute for book2
#Lets check if self.title is equal to other.tittle, and do the same for it's pages, if this is the case we return True, otherwise False. 
    #What happens when you use ==?
    def __eq__(self, other):
        if(self.title == other.title and self.pages == other.pages):
            return True
     return False
    
#comparison is now true true  since they have the same attributes such as title and pages. 
book = Book("The Alchemist", 72)
book2 = Book("The Alchemist", 72)

print(book == book2)

#just to check it we can use two diffent books, we get a false, since they have diffent attrbutes such as title and pages. 
book = Book("The Alchemist", 72)
book2 = Book("Not the same book", 72)

print(book == book2)

