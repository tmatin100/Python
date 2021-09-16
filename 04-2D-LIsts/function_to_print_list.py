######### FUNCTION TO PRINT LIST ##########

grades = [[10, 25, 13, 45], [205], [70, 76, 49, 100]]

#create the function
def print_2d(grades):
    for inner_list in grades:
        for grade in inner_list:
            print(grade, end= " ")
        print()

#invoke the function, the def of the function has to come before this
print_2d(grades)


print_2d(["chickity", "china", "chinese", "chicken", [1, 3, 3], [4]])


