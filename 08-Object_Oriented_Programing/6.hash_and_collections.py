########## __hash__ and Collections ##########
########## __hash__ and Collections ##########
# Python hash() function is a built-in function and returns the hash value of an object if it has one. 
#  The hash value is an integer which is used to quickly compare dictionary keys while looking at a dictionary.
# Properties of hash() function:
#  -Objects hashed using hash() are irreversible, leading to loss of information.
#  -hash() returns hashed value only for immutable objects, hence can be used as an indicator to check for mutable/immutable objects.

#The best practice when we override the  equals method ( __eq__ ) it best practice to deal with the hash method (__hash__).
#  We can either create our own custom implementaiton for it, or we can simply state that we are not going to use the hash methord by seting it to None. 
# __hash_ = None is the default when we override __eq__ (Book is not hashable)
# The hash method is typically used for any hashing data structres, such as Sets and Dictionaries. 


class Book():
    favs = [] #class

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def is_short(self):
        if self.pages < 100:
            return True

    def __str__(self):
        return f"{self.title}, {self.pages} pages long"

    def __eq__(self, other):
        if(self.title == other.title and self.pages == other.pages):
            return True
        return False 
        
#This is how we would implement hash, when the data is immuatable only. #This replaces __hash__ = None
    def __hash__(self):
        return hash(self.title) ^ hash(self.pages) #xor with hash of attributes
        #from Mastering Object-Oriented Python

book = Book("Are You My Mother", 72)
book2 = Book("Not the same", 72)

print(book == book2)

#print the hash for book object 
print(hash(book))

#lets change the date attribute inside the book object and check its hash, notice it will change which is a problem. We dont 
#want our hashes to change to maintain data integrity. 
book.title = "Something else"
print(hash(book))

# If two objects are considered equal based on attributes, then they should have the same hash.
#Therefore the value shoudl be True. 

book3 = Book("The Alchemist", 72)
book4 = Book("The Alchemist", 72)
print (book3 == book4)
print (hash(book3) == hash(book4))

# you can now use those data inside a set
books = {"book", "book2"}

#in a dictinary only the key is hashed, not the value. 
#data = {"hello": "hi"}

# List is a type that is not hahsable
# data2 = {[]]: book} 

#It's approriate to give something for __hash__ when you override __eq__
# If you dont want your datastructure to be hashable then you use the None type for hash
# This is basically explicity stating, that this class is not spoosed to be used for hashing
# #This is the recommended way if the data is mutable, for example updating the books title, pages, etc. 
#Typically, the hashes derive from the data its storing, so if you are updating the data, then the hash is also changeing.
# Therefore, its is not recomend to use hashing for mutable data. Or, if you are really carefull you can use hashing for mutable data for hashing, but you should not be changeing it.
#We doo not change objects that are being used inside a dictionary.

__hash__ = None

##################################Sumamary###########################################
#1. Hashes should not change, an object hash should remain the same through the entire execution of the code.
#2. If two objects are considered equeal, then their hashes shoudl be the same. 
#3. If two objects are diffent but, somehow coicentially their hashes are the same, that is okay. Their hashes do not have to be diffent although that is ideal. 