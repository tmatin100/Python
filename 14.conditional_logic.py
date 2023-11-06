is_old = True
is_liscenced = True

"""if is_old: 
    print('you are old enough to drive!')
elif is_liscenced: 
    print('you can drive now!')
else: 
    print('your are no tof age!')

print('ok ok o')"""

if is_old and is_liscenced: 
    print('You can drive now!')
else:
    print('Sorry, You can not drive')
        

# Ternary Operator (conditional expression )
# condititon_if_true if condition else condition_if_false 

is_friend = False
can_message = "message is allowed" if is_friend else "message is not allowed"

is_friend = True 
can_message = "message is allowed" if is_friend else "message is not allowed"
print(can_message)

# Short Circuiting 

is_Freind = True
is_User = True

if is_Freind and is_User: 
    print('best freinds forever')

#this will ignore the second condition , this is called short cirtuiting, which makes the code very effecient
if is_Freind or False: 
    print('best freinds forever')


is_Freind = False
is_User = True

if is_Freind and is_User: 
    print('best freinds forever')



