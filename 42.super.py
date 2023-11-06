# Super class method 
class User(object):
    def __init__(self, email):
        self.email = email 

    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power, email):
        # super() is refereing to the supper or parent class which is User. With super we no longer need pass in self.
        #User.__init__(self, email)  # old way
        super().__init__(email)  
        self.name = name 
        self.power = power 

    def attack(self):
        print(f'{self.name} is attacking with power of {self.power}')

wizard1 = Wizard('Merlin',60,'merlin@gmail.com')

print(wizard1.email)
print(wizard1.name)
print(wizard1.power)

wizard1.attack()