digits = '0123456789'
characters = 'abcdefghijklmnopqrstuvwxyz'
up = characters.upper()
special = '-_!?&$%'

all = digits+special+characters+up

from random import choice

password = ''.join(choice(all) for i in range(8))
password2 = ''.join(choice(all) for i in range(8))
password3 = ''.join(choice(all) for i in range(8))

password4 = ''.join(choice(all) for i in range(10))
password5 = ''.join(choice(all) for i in range(20))
password6 = ''.join(choice(all) for i in range(30))

print('HERE ARE 3 DIFFERENT PASSWORDS')

print(password)
print(password2)
print(password3)

print('HERE ARE SOME LONGER PASSWORDS')

print(password4)
print(password5)
print(password6)
