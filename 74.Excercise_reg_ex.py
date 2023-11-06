# https://emailregex.com/index.html

import re 

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

string = 'Tamzidul'

a = pattern.search(string)
print(a)

#Pssword policy 
# At least 8 character long
# contains any sort letters, humbers $%#@

