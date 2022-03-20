# Queue- First in First Out

data = []           #were using a list as a queue

#enque 

data.append(5)
data.append(10)
data.append(15)
data.append(20)
print(data)

#deque 

data.pop(0)       # For que we remove the left most element in the bigeneing by removing index 0 
print(data)
element= data.pop(0)
print(element)
print(data)

print(data[0])    #peek


####################use deque for larger data collection types###############################

from collecitons import deque

data = deque()
data.append("T.Matin")
element = data.popleft()

print(element,data)


