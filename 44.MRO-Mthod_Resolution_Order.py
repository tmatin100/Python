class A: 
    num = 10 

class B: 
    pass

class C: 
    num = 1

class D(B, C): 
    pass

print(D.mro())

print(D.num) 

print(D.__mro__)