# A faster and recommended way to count elements is to use the Counter function 
# which cretes a set of dicitionariy without any duplicates

from collections import Counter

backpack = ["sword", "sword", "rubber duck", "slice of pizza", "parachute", 
"sword", "rubber duck", "slice of pizza", "parachute", 
"sword", "rubber duck", "slice of pizza", "parachute",
"sword", "rubber duck", "slice of pizza", "parachute",
"cannon", "laser cannon", "Canon 90D", "can of soup"]

print(Counter(backpack))