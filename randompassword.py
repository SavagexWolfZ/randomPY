digits = '0123456789'
characters = 'abcdefghijklmnopqrstuvwxyz'
up = characters.upper()
specialCharacters = '-_!?&$%'

all = digits+specialCharacters+characters+up

from random import choice

password = ''.join(choice(all) for i in range(8))
password2 = ''.join(choice(all) for i in range(8))
password3 = ''.join(choice(all) for i in range(8))

password4 = ''.join(choice(all) for i in range(15))
password5 = ''.join(choice(all) for i in range(20))
password6 = ''.join(choice(all) for i in range(30))

password100 = ''.join(choice(all) for i in range(100))
password200 = ''.join(choice(all) for i in range(100))
password300 = ''.join(choice(all) for i in range(100))

print('HERE ARE 3 DIFFERENT PASSWORDS')

print(password)
print(password2)
print(password3)

print('HERE ARE SOME LONGER PASSWORDS')

print(password4)
print(password5)
print(password6)

print('HERE ARE SOME 100 DIGIT PASSWORDS')

print(password100)
print(password200)
print(password300)
