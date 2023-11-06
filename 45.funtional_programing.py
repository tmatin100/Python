# Functional Programing - sperates data and fuctions
# Clear+Understandable
# Easy to Extend
# Easy to Maintain 
# Memory Efficient
# DRY - Do Not Repeat Yourself

def multiply_by2(li):
    new_list = []
    for item in li: 
        new_list.append(item*2)
    return new_list

# is this a pure function?  Yes!
# Rule1- given an input it returns the same output ?  Yes!
# Rule2 -Does this produce any side effects? Does it change anyting in the outside world ? 
#  No!

mult1 = multiply_by2([1,2,3,4,5])
print(mult1)

