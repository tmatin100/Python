########## sys path ##########

#When we created the utils module, it came from the same directory.
#This is part of the default search path
#You can see the places modules are searched for by importing a special module
#https://docs.python.org/3/tutorial/modules.html#standard-modules

import sys 

#always available, work directly with interpreter
#unlike some other modules. 
#import winreg ( on windows)
#docs give this example:
sys.ps1 = 'C> ' #(Try it in interactive mode if needed)

print(sys.path)

#path prints locations searched for modules. 

#We could move utils up a directory (or anywhere we want)
#and import it like so:
sys.path.append("/Users/tmaitn/Python")

#There are ways you can do this more dynamically
#https://stackoverflow.com/questions/30218802/get-parent-of-current-directory-from-python-script/39618108
from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)


