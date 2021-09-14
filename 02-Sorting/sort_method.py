 ########## SORT METHOD ##########

#This is using python built in method and not custom built
#You can easily sort a list:
work_days = ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"]
#this actually effects the original list
work_days.sort() 
print(work_days)

#if you need the original list to remain he same then you
# would use the slicing method [:] to copy to a new list 

work_days = ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"]

copy = work_days[:]
copy.sort()
print(copy)
print(id(work_days))
print(id(copy))