# Regular Expressions in python
# https://regex101.com/
# https://docs.python.org/3/library/re.html
# https://regexone.com/


import re 


string = 'search inside of this text please!'

print('search' in string)

print(re.search('this', string))

a = re.search('this', string)

# checs where the string exists as a tupple 
print(a.span())

# check where the text starts and ends
print(a.start())
print(a.end())

# usefull for multiple searches and group 
print(a.group())

# crate a pattern to use 
pattern = re.compile('this')

b = pattern.search(string)
c = pattern.findall(string)
d = pattern.fullmatch(string)
e = pattern.match(string)
print(b)
print(c)
print(d)
print(e)

# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"(/[a-zA-Z]+/g)([a])"

test_str = "Hey how are you? "

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.

