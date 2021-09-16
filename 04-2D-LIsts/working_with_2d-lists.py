########## WORKING WITH 2D LISTS ##########

grades = [[6, 3, 5], [60, 43, 4, 23], [205]]

for inner_list in grades : 
    for grade in inner_list:
        print (grade, end=" "  )  #adds space to each index item when priting
    #prints a new line after each inner loop    
    print()

    
# we can also iterate using range function
grades = [[6, 3, 5], [60, 43, 4, 23], [205]]

for i in range(len(grades)):
    for j in range(len(grades[i])):
        print(grades[i] [j], end=" ")
    print()

#another way to do it
for inner in grades:
    if  isinstance(inner, list):
        for grade in inner:
            print(grade, end=" ")
        print()
    else:
        print(inner)

