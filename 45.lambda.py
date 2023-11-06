# lambda expressions are one time anynomous fuctions

from functools import reduce



my_list = [1,2,3]


#lambda param: action(param)

print(list(map(lambda item: item*2, my_list)))


print(list(filter(lambda item: item % 2 != 0, my_list )))


print(reduce(lambda acc, item : acc+item, my_list))

print(my_list)

