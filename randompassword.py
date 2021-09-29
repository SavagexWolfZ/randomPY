from random import choice

digits = '0123456789'
characters = 'abcdefghijklmnopqrstuvwxyz'
up = characters.upper()
specialCharacters = '-_!?&$%'

everything = digits+specialCharacters+characters+up

password = ''.join(choice(everything) for i in range(8))
password2 = ''.join(choice(everything) for i in range(8))
password3 = ''.join(choice(everything) for i in range(8))

password4 = ''.join(choice(everything) for i in range(15))
password5 = ''.join(choice(everything) for i in range(20))
password6 = ''.join(choice(everything) for i in range(30))

password100 = ''.join(choice(everything) for i in range(100))
password200 = ''.join(choice(everything) for i in range(100))
password300 = ''.join(choice(everything) for i in range(100))

print('HERE ARE 3 DIFFERENT PASSWORDS' + '\n' + '==========' + '\n')

print(password+ '\n' + password2 + '\n' + password3 + '\n')

print('HERE ARE SOME LONGER PASSWORDS' + '\n' + '==========' + '\n')

print(password4 + '\n' + password5 + '\n' + password6+ '\n')

print('HERE ARE SOME 100 DIGIT PASSWORDS' + '\n' + '==========' + '\n')

print(password100 + '\n\n' + password200 + '\n\n' + password300 + '\n\n')
