# the numerate() function regurns an enumerate object , must be another object that supports itteration

for char in enumerate('Helllooo'):
    print(char)


for i, char in enumerate('Helllooo'):
    print(i, char)

for i, char in enumerate([1,2,3]):
    print(i,char)

for i , char in enumerate((1,2,3)):
    print(i,char)


# create a script that enumerates from 1 to  100 and prints the index of 50 only. 
for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f'index of 50 is {i}')