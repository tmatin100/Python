# Set 
# A set is a collection which is unordered, unchangeable*, and unindexed. No duplicates 
# https://www.w3schools.com/python/python_sets_methods.asp



my_set = {1,2,3,4,5,}
your_set = {4,5,6,7,8,9,10,}

# .diffference() - shows the difference between two sets 
print(my_set.difference(your_set))


# .discard() - removes a an element in the set
my_set.discard(5)
print(my_set)

# .difference_update() - removes the difference between two sets
#print(my_set.difference_update(your_set))
#print(my_set)


#.intersection() - shows the intersections between two sets
print(my_set.intersection(your_set))

# .isdisjoint , is this a set wiht nothing in common? 
print(my_set.isdisjoint(your_set))

#.union()- unites two sets with no duplecates 
print(my_set.union(your_set))
#union short hand
print(my_set | your_set)


# issubset - is it part of another set? 

print(my_set.issubset(your_set))

#issuperset - is it hold another set inside it
print(my_set.issuperset(your_set))