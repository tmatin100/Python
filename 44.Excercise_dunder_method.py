# create a superlist using the classs SuperLIst(), and add a dunder method __len__ 
# and modify it to return 1000, no mather what 

# inherit the attributes of list in this class 
class SuperList(list):
    def __len__(self): 
        return 1000


super_list1 = SuperList()

print(len(super_list1))

super_list1.append(5)

print(super_list1[0])
print(super_list1)

#is Superlist a subclass of list ? 
print(issubclass(SuperList, list))

#is list a subclass of object? 
print(issubclass(list, object))

