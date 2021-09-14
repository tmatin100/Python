########## REMOVE ELEMENT FROM LIST USING DEL AND SLICE ##########

work_days = ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"]
work_days.append("Sunday")
print(work_days)
#remove the last element 
del work_days[-1]
print(work_days)

work_days = ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"]
#remove first 2
del work_days[0:2] 
print(work_days)

work_days = ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"]
#remove last 2 (start 2 from right and go to end)
del work_days[-2:] 
print(work_days)

work_days = ["Monday", "Tuesday", "Wednesday", "Wednesday", "Thursday", "Friday", "Saturday"]
work_days.append("Sunday")
del work_days[work_days.index("Wednesday"): work_days.index("Wednesday")+3]
print(work_days)

work_days = ["Monday", "Tuesday", "Wednesday", "Wednesday", "Thursday", "Friday", "Saturday"]
work_days.append("Sunday")
del work_days[work_days.index("Wednesday"): ]
print(work_days)