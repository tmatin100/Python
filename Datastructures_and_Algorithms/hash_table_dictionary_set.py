#create a dictionary- no duplicate keys allowed
data = {"Aakash": "tmatin100@gmail.com", "Anik" : "tanik100@gmail.com", "Ovik":"tovik93@gmail.com"}
print(data)

#this is how we create an empty set
colors = set()
print(type(data))
print(type(colors))

print(hash("Aakash"))


class Test: 
    pass
  #  __hash__= None

data = {"Aakash": "tmatin100@gmail.com", "Anik" : "tanik100@gmail.com", "Ovik":"tovik93@gmail.com"}

print(hash(Test()))

data2 = {"red"}