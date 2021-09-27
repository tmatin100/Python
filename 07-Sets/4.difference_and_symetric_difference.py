######### DIFFERENCE AND SYMMETRIC DIFFERENCE ######### 

my_fav = { "red", "green", "blue", "black", "purple"}
her_fav = {"blue", "orange", "purple", "green"}

#difference(-)
only_me = my_fav - her_fav
print(only_me)

#we can also reverser this 
only_her = her_fav - my_fav
print(only_her)


#symmetric difference is like if you took colors only I liked union 
# with colors only she liked and put em together:
#we can combine the differences with a union, this is an example of a symetric
only_me = my_fav - her_fav
only_her = her_fav - my_fav
union = only_me | only_her
print(union)

#there is actually an operator(^) for symetric which will do the same thing
#as the code above
symetric = my_fav ^ her_fav
print(symetric)


#notice the print fuction results are allways in diffent orders each time
#we print, since sets are always undorderd. 

#like union and intersection, there are method
# versions that return. --> .difference and .symmetric_difference