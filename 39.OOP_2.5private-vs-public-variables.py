
# Abstraction - hiding of information and giving asscess to only what is necessary. 

# Private Variables - an underscore _ means this should not be modified or private 

class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def run(self):
        print('run')
    
    # We are enpsulating the functionality in the class and useing it wiht our speak method. 
    def speak(self): 
        print(f'myname is {self.name}, and I am {self.age} years old')

player1 = PlayerCharacter('andrei', 100)
player1.name = '!!!'
player1.speak = 'BOOOOOO'

print(player1.speak)
