#input('jayjay')
#input('secret')

#print('{username}, your password {******} is {passwordlenght} letter long')

username = input('Please enter your username: ')
password = input('Please enter your password: ')

password_length = len(password)

hidden_password = len(password) * '*'

print(f'{username}, your pasword {hidden_password} is {password_length} long')
