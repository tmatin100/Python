#Hash Table - an array consisting of a Key value pair, or an association of two diffent values.
# ex.  id: name 

# uses lookuptable, fast insert and retrivals 
# and key:value pairs
# key goes through some processing, and gets a location int he memory - O(1) operation. 
# key % size
# collision- when two items have the same key(explosion), in such case we can use a linked list for the new value (seperate chaining), or just go the next index (linear probing)

data = {}
data[3] = "T.Matin"

print(data[3])

