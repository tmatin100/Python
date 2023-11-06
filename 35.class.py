#OOP Class

class PlayerCharacter: 

    # Cass Object Attribute - does not change across instances 
    membership = True

    # a class constructor method that is called anytime we instantiate an object 
    def __init__(self, name, age): 
        # only if membeship is true the we are going to assign name and age, in order to access membership attribute we need to use self.mebership
        if (self.membership):
        #self refers to the object creteated at instatntiaiton in this case player1
            self.name = name  # attributes or properties that can be accessed with .methods 
            self.age = age 

    # define a method named run
    def run(self):
        print('run')
        return 'done'
    
    # define a method named shout
    def shout(self, hello):
        print(f'my name is {self.name}')
    

# need to pass in the nmae aurgument or else well get a type error 
player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)

# these objects lives in different places in the memory 
print(player1)
print(player2)

# in this case player1 is self 
print(player1.name)
print(player1.age)

print(player2.name)
print(player2.age)

#access the run function 
print(player1.run())
print(player2.run())

# access the shout function 
print(player1.shout('hello'))
print(player2.shout('Whatsup!'))

#access the Class Object Atttribute that's set to True 
print(player1.membership)

# great way to see the class blueprit of an object is the help() fundtion 
# help(player1)








