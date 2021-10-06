########## __str__ ##########

class Book():
    favorites = [] #class level attribute/variable

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def is_short(self):
        if self.pages < 100:
            return true

    #What happens when you pass object to print?
    #here we can define a string representaiton of our objects (book1 and book2)
    def __str__(self):
        return "5"
        return f"{self.title}, {self.pages} pages long"

#we are creating objects named book and book1 here using the Book() class
book = Book("The Kite Runner", 168)
book2 = Book("The Alchemist", 72)

# we are refereing to the class here (Book.favorites), not creating objects like above.
Book.favorites.append(book)
Book.favorites.append(book2)

#Favorites is related to books, but not tied to one individual book
#We use self as a parameter if it's unique to each object :)
print(Book.favorites)

#for every single book in this list we are going to print the tittle attribute
for b in Book.favorites:
    print(b.title)

