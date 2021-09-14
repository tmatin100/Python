########## INPUT USING SPLIT ##########

print("List your favorite foods separated by ', '")
print("Example input: ")
print("Kale, bok choy, brussel sprouts")

data = input()
favs = data.split()

for food in favs:
    print("You said: " + food)

#an obvious downfall is that this is very touchy.
#instead, we could ask one food per line