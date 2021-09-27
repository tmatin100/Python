######### SETS EXPLAINED #########

#Sets are similar to dictionaries in that the data is hashed and it is unordered.
#Sets are similar to lists in that they just contain the data and not a key-value pair
#Sets are different than lists in that you cannot have duplicates

stuff = {"sword", "rubber duck", "sice a pizza"}
print("sword" in stuff)
print(stuff)

#sets can not have duplicate items
stuff.add("sword")
print(stuff)
#Notice only one occurance of sword even though already added

#How is a set different than a dictionary?
#For a set, each element is only one piece of data
#for a dictionary, it is a key-value pair. 

#Behind the scenes, they both use hashing. The hashing is used to determine where to store the data.
#For dictionaries, the KEY is hashed
#for sets, we do not have a key, so the data itself is hashed.
#This means we cannot store something in sets that is not hashable.

#stuff.add(["trying to add a list"])
##stuf.add([1,2,3])

#It's important to understand the purpose of a set...
#Easily check if element in set
#such as to easily check to see if something has been tagged
#To do various set operations (coming soon)

#An example would be to see if a word is ever used in a phrase. Not counted (that wold be a dictionary)

conjunctions = {"but", "or", "so", "and", "yet", "for", "nor"} #fanboys

#create an empty set
seen = set() #THERE'S NOT AN EMPTY SET LITERAL!! #learn something new every day

completely_original_poem = """I still hear your voice when you sleep next to me
I still feel your touch in my dreams
Forgive me my weakness, but I don't know why
Without you it's hard to survive
'Cause every time we touch, I get this feeling
And every time we kiss I swear I could fly
Can't you feel my heart beat fast, I want this to last
Need you by my side"""

#spit the string variable contents into a list of words with the .split() method and store it 
# in a list named words. 
words = completely_original_poem.split()
print(words)

for word in words:
    if str.lower(word) in conjunctions:
        seen.add(str.lower(word))

#print all the conjuction seen in words, however it cant tell us how many times we have
#the data has occurd. For that purpose dictionay is more ideal to use. 
print(seen)

