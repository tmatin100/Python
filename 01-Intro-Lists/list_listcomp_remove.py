########## LIST COMPREHENSION ##########

healthy = ["kale chips", "broccoli"]
backpack = ["pizza", "frozen custard", "apple crisp", "kale chips"] 

#lets remove everything form backpack that is not healthy using list comprehension

#backpack[:] = [item for item in backpack if item in healthy]
#print(backpack)

#healthy_backpack = [item.upper() for item in backpack if item in healthy]
#print(healthy_backpack)

#remove item using loops

healthy_backpack = []

for item in backpack: 
    if item in healthy: 
        healthy_backpack.append(item.upper())


print(healthy_backpack)

#list comprehension example 2 

#squares = [i**2 for i in range(10) if i%2==0]
#print(squares)


#squares = []
#for i in range(10):
    #if i % 2 == 0
     #squares.append(i**2)

     #print(squares)