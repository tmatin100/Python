# One of the most common tools is the reange() funcion. 

print(range(100))
print(range(0, 100))


# we can itterate over a range 
for number in range(0,100): 
    print(number)

for number in range(0,100): 
    print('email list')


for _ in range(0,10): 
    print(_)

# we can go by a step 
for _ in range(0,10,2):
    print(_)

# we can print a range with the -1 step in the end 
for _ in range(10,0,-1):
    print(_)

"""for item in range(10, 0, -2): 
    print(list(range(10)))"""

for item in range(10, 0, -2): 
    print(list(range(10)))

for item in range(2): 
    print(list(range(10)))