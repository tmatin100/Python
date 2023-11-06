selfish = '1234567'

print(selfish)


#[start:stop:stepover]
print(selfish[0])
print(selfish[0:8])
print(selfish[0:8:2])
print(selfish[1:])
print(selfish[:5])
print(selfish[::1])
print(selfish[-1])
print(selfish[::-1])

#immutibility - strings in python are immutable, meaning they can not be changed 
# we cant do this selfish[0]=8 , instead we would have to assign the whole string
selfish = '8'
print(selfish)

selfish = selfish + '8'
print(selfish)
