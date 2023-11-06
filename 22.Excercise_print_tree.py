# Print Christmas Treee  

picture = [
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0]
]

# 1. iterate over picture 
# if 0 -> print " "
# if 1 -> print * 

for image in picture:
    for pixel in image: 
        if (pixel == 1): 
            print('*', end='')
        else: 
            print(' ', end='')
    print(' ')



# Developer Fundementals: IV
# clean code
# readability 
# predicetablity 
# DRY ( do not repeat yourself)



