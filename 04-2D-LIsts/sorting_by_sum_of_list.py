########## Sorting by sum of list #########

data = [[10, 2, 3],[10, 20], [4, 5000, 6], [7, 8, 9], [10]]

#We can also sort using a different function to determine which comes first:

print(sorted(data, key=sum))

#You can also reverse the order:
#each list stays same, just order of list is flipped

print(sorted(data, key=sum, reverse=True))
