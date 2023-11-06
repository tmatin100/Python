# init

class PlayerCharacter:  
    def __init__(self, name, age):
        self.name = name # attributes 
        self.age = age 
    
    def method (self): 
        return self



# a class method  allows us to instntiate objects wihout the class constructior using a decorateor- @ 
    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)
    
    @staticmethod
    def stc_method(param1, param1): 
        # code 

      
player3 = PlayerCharacter.adding_things(2,3)

print(player3.age)


