# Multiple Inheritence 

class User(): 
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
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows 
   
    def check_arrows(self): 
        print(f'{self.name} has  {self.arrows} arrows remaining')
    
    def run(self):
        print('ran very fast')

# Multiple Inheritence 
class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)     # inherits from the Archer class
        Wizard.__init__(self, name, power)        # inherits from the Wizard class 

hb1 = HybridBorg('borgie', 50, 100)
print(hb1.run())

# check multiple inheritence 
print(hb1.attack())  # power
print(hb1.power)    # power
print(hb1.arrows) # arrows
print(hb1.check_arrows()) 
print(hb1.sign_in())





