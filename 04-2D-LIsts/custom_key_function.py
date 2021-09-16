########## CUSTOM KEY FUNCTION ##########

#Any fuction you could use on a list to manipulate the data should do the trick
#Here's another example:
data = [[5, 5, 5], [3, 4, 5], [3, -3, 0], [1,1,1,79], [1, 10, 1, 20]]

def avg(data):
    avg = sum(data) / len(data)
    print(data, "average is", avg) #for our sake to see
    return avg


print(sorted(data, key=avg))