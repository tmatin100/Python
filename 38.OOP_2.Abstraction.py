
# Abstraction - hiding of information and giving asscess to only what is necessary. 

class PlayerCharacter: i
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')
    
    # We are enpsulating the functionality in the class and useing it our speak method. 
    def speak(self): 
        print(f'myname is {self.name}, and I am {self.age} years old')

player1 = PlayerCharacter('andrei', 100)

# abstraction in action, we dont see the programing behind it 
player1.speak()

# any built in functions such as len(), print() etc.  is an example of an abstration

