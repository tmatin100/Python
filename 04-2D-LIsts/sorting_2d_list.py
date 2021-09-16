########## SORTING 2D LIST ##########
# we can use the sorted function to sort data in a list with
data = [5, 7, 3, 5, 10, 11]
print(sorted(data))

#we can also sort the data by list of lists, it looks at the first element
# the list, if the first is a tie it looks at the seceond and so on. 
data = [[10, 2, 3],[10, 20], [4, 5000, 6], [7, 8, 9], [10]]
print(sorted(data))

# we can do the same with strings
data2 = [["ball", "apple"], ["amazon"], ["amz", "zen"]]
print(sorted(data2))