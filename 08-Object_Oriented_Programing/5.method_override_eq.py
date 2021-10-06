 

class Book():
    favorites = [] #class level attribute or variable

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def is_short(self):
        if self.pages < 100:
            return true



 #What happens when you use ==?
    def __eq__(self, other):
        if(self.title == other.title and self.pages == other.pages):
            return True    


book = Book("The Alchemist", 72)
book2 = Book("The Alchemist", 72)

