backpack = ["sword", "sword", "rubber duck", "slice of pizza", "parachute", "sword"]
print(backpack)

#Sets are created with {}, they are unordered. Duplicate items are not allowed.
# The purpose is to see wheter if something exists or not, since the order doesnt matter. 
backpack2 = {"sword", "sword", "rubber duck", "slice of pizza", "parachute","sword"}
print(backpack2)

#we can check an item in a set like this, which shoud return a boolean value:
print("sword" in backpack2)