########## __str__ ##########
#By default anytime we print an object it gives a string representation, which gives you a type
#and a memory address.

#for b in Book.favorites: 
   # print(b)

#This is not the pretiest representation, so we can actually ovverdie this 
#and create our own. To do that we can use the str initilaizer (__str__), and pass in self 
class Book():
    favorites = [] #class level attribute/variable

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def is_short(self):
        if self.pages < 100:
            return true

    
    #What happens when you pass object to print?
    #Here we can define a string representaiton of our objects (book1 and book2). All we have to do is return a string 
    #We are createing an object with , str initilaizer (__str__), and passing in the self variable
    def __str__(self):
        #return "5"
        return f"{self.title}, is {self.pages} pages long"

#we are creating objects named book and book1 here using the Book() class
book = Book("The Kite Runner", 168)
book2 = Book("The Alchemist", 72)

# we are refereing to the class here (Book.favorites), not creating objects like above.
Book.favorites.append(book)
Book.favorites.append(book2)

#Favorites is related to books, but not tied to one individual book
print("We use self as a parameter if it's unique to each object :)")
print(Book.favorites)

print("for every single book in this list we are going to print the tittle attribute:")
#for every single book in this list we are now going to print string representaitno of the attributes 
#becasue we have defined that in the __str__ object created earlier. 
#when we pass an jobect to print it is automatically goint to invoke the __str__ methord on the object.
for b in Book.favorites:
    print(b)

