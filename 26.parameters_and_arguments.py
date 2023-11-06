# Parameters - are values we give inside of the brackets when creating a fucntion. These parameters
# gives us the abilty to pass aurguments(actual vlaues) when using the function.

def say_hello(name, emoji):
    print(f'hellooooooo {name} {emoji}')


#aurguments- are actual values we provide to a function, in this case 'Andrei' and ' emoji '

# positional arguments
say_hello('Andrei', ' emoji ')
say_hello('Dan', ':)')


# keyword argument
say_hello( emoji = ':)', name='Emily')

# default parameters , are paramaters used if we done pass any aurguments when calling the functions
def say_hello(name='Darth Vader', emoji='):' ):
    print(f'hellooooooo {name} {emoji}')

say_hello()

