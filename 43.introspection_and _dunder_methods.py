# Introspection 
# The ablity to determine the type of an object at runtime. 
# Python we can do this with some helper fucntions. for example dir()


# Dunder magic methods __

from typing import Any


class Toy(): 
    def __init__(self, color, age): 
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo', 
            'has_pets': False
        }
    
    # theese custom methods only gets modifired within this Toy() class/function
    def __str__(self):
        return f'{self.color}'
    
    def __len__(self):
        return 5
    
    def __call__(self):
        return "Yes??"
    
    def __getitem__(self, i):
        return self.my_dict[i]
    



action_figure = Toy('red', 0)

#introspectin
print(dir(action_figure))

print(action_figure.__str__())

print(str(action_figure))

print(len(action_figure))

print(action_figure())

print(action_figure['name'])