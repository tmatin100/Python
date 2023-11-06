# Encapsulation  https://www.geeksforgeeks.org/encapsulation-in-python/

""" the idea of wrapping data and the methods that work on data within one unit. 
This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.
To prevent accidental change, an object’s variable can only be changed by an object’s method. 
Those types of variables are known as private variables. 
"""


class PlayerCharacter: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')
    
    # We are enpsulating the functionality in the class and useing it our speak method. 
    def speak(self): 
        print(f'myname is {self.name}, and I am {self.age} years old')

player1 = PlayerCharacter('andrei', 100)
player1.speak()

