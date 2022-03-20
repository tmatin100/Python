# Stack - Last in first out

data = []           #were using a list as a stack


data.append(5)              #we use the append method to push/add a data 

print(data[len(data)-1])  #looks at the data 


element= data.pop()                 # pop method removes data at the end and returns it
print(element)
print (data)

data.append(5)
data.append(10)
data.append(15)
data.append(20)
print(data)

data.pop()
data.pop()
print(data)


#########################create a custom class##############################
class Stack:
    def __init__(self): 
        self._data = []
    
    def push(self,data1):
        self._data.append(data1)
    
    def pop(self):
        return self._data.pop()

###################crate a custom peek method ######################

    def peek(self):
        return self._data[len(self._data)-1]

stack = Stack()
stack.push(10)
print(stack.peek())
test = stack.pop()
print(test)

