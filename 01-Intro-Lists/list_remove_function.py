########## REMOVE ELEMENT FROM LIST BY VALUE OR INDEX ##########


#We learned how to remove by value:

workdays = ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"]

#VACATION DAY!
workdays.remove("Saturday")
print(workdays)

#However, using slicing and removing by index is also useful:
workdays = ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"]
del workdays[4]
print(workdays)