#We can make this more dynamic. 
healthy = ["kale chips", "brocolli" ]
backpack = ["pizza", "chicken pot pie", "kale chips"]

#Let's use the .remove() method to remove an item from the backpack list, only if the item does not exists in the healthy list
#in this case pizz is not in the healhty list so it is removed
if "pizza" not in healthy: 
    backpack.remove("pizza")
print(backpack)


#We can also check to see if the item exists in the list 
#in this case kale chips is in the helahty list so it is not removed
if "kale chips" not in healthy: 
    backpack.remove("kale chips")
print(backpack)