######### UNION AND INTERSECTION #########
#We cna use unoions and intersections to combine sets
#notice blue is in there twice, but doesnt mean it's going to be in the output 
#twice, it will only be there once, since sets don't allow duplicates. 

my_fav = {"red", "green", "blue", "black", "purple"}
her_fav = {"blue", "orange", "purple", "green"}

#union (|) - combines everything between two sets, (theres also a .union() method)
# You may see + (concatenation) to combine lists, in which there are repeats. 
all_favs = my_fav | her_fav
print(all_favs)

#intersections (&) - elements shared between two sets
wedding_colors = my_fav & her_fav
print(wedding_colors)


#there are also methods that we can use such as, .intersection() in order to 
#get the seame results as above
wedding_colors = my_fav.intersection(her_fav)
print(wedding_colors)