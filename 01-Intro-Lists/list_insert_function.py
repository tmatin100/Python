########## INSERT INTO MIDDLE OF LIST ##########

#Lists are ordered, and this order may matter to you. 

work_days = ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"]
print(work_days)
print(work_days[3])

#OVERTIME!
work_days.insert(2, "Wednesday") #index, "data"
print(work_days)
print(work_days[3])

#What if we want to do the opposite and take a day out?
