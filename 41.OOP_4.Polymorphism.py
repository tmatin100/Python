# Polymorphism 
"""In Python, Polymorphism lets us define methods in the child class that have 
the same name as the methods in the parent class."""

class User(object): 
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')

# Inherit from parrent class by passing the parent class User as an argumenti 
#subclass or derrived class 1

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    # lets say we want both user and wizard class to run the attack method 
    def attack(self): 
        User.attack(self)   # we can use both user and wizard's attack method this way , we can accept User as aparameter 
                             # and run User.attack()
        print(f'{self.name} attacking with power of {self.power}')


# Inherit from parrent class by passing the parent class User as an argument
# subclass or derrived class 2
class Archer(User): 
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows 
   
    def attack(self): 
        print(f'{self.name} attacking with power of {self.num_arrows}')

# lets instantiate a classs and print
wizard1 = Wizard('Merlin', 60)
archer1 = Archer('Robin', 30)
# print(wizard1.attack())
# print(archer1.attack())

# create brand new function and pass differnet objects to the same attack function()
# # pollymorphism
def player_attack(char):
    char.attack()

player_attack(wizard1)
player_attack(archer1)