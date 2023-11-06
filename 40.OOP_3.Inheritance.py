# Inheritence - allows new objects take the properties of old objects 

# no init method used since we are not passing in any new auguments 
#user gets attributes from the object base class, underneath the hood its accepting a parent class name object 
# by default, like this : class User(object): 
class User: 
    def sign_in(self):
        print('logged in')

# Inherit from parrent class by passing the parent class User as an argumenti 
#subclass or derrived class 1
class Wizard(User): 
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self): 
        print(f'{self.name} attacking with power of {self.power}')


# Inherit from parrent class by passing the parent class User as an argument
# subclass or derrived class 2
class Archer(User): 
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows 
   
    def attack(self): 
        print(f'{self.name} attacking with power of {self.num_arrows}')

# lets instantiate a classs and print, it should print 'logged in'
wizard1 = Wizard('Merlin', 50)

#print(wizard1)
wizard1.sign_in()
wizard1.attack()

archer1= Archer('Robin', 100)

#print(archer1)
archer1.sign_in()
archer1.attack()


# we can check if something is an instance of a class with the isinstance python builtin fucntion
# isinstance(object, class)

print(isinstance(wizard1, Wizard))

# there is a base classs named object above the Parent User class, form which wizard one also inherits it's attributes
print(isinstance(wizard1, object))