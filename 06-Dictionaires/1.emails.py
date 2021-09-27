######### INTRO TO DICTIONARIES #########
#In a dictionary there is going to be an association of two pieces of data
#such as a key-value pair
#dictionary stores key-value pairs
#The equiv of an associative array/hash table
emails = {
    "Caleb":"caleb@email.com", 
    "Gal":"g@example.com" 
}

print(emails)
#in this case, the key is the name, email is the value. 
#Data type doesn't matter at all for the value.
#Key must be a hashable --> What does this mean?
#Classes have a function __hash__ invoked when used as the key
print(hash("hello")) 

#I'm not sure of exact internals on how the hash is used, but imagine it like so:
#You have an area of memory with 8 spots, and you need to store the value at some spot...
print(hash("hello") % 8) 

#Almost always immutable type (should be, anyway)
#a tuple will work, list will not. a number will work

#Why use a hashtable? Extremely fast to add or look up data
#O(1) --> constant time. More elements does not mean slower unlike a sort or something
#https://en.wikipedia.org/wiki/Hash_table
#Hashtables often used for memoization


