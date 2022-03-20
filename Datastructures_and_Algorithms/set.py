#sets are unordered,  can not have duplicates



colors = {"red", "green", "black", "blue", "purple" }

her_fav = { "blue", "orange", "purple", "green"}

#union - taking all the elemnts from two diffent sets

union = colors | her_fav
print (union)

#union method 
union1 = colors.union(her_fav)
print(union1)


#intersection - common items between two sets

#difference - uncommon items in both sets

#symetric difference - everything except the coomon shared items

#for a hastable we hash the items in the set, the data has to be hasable to do so. 

def __has__(self):
    return value 

