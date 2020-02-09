import PasswordMaker

print('==x==' * 8)
print(' WELCOME TO PASSWORD M4KER')
print('==x==' * 8)
print('You must always answer with [\'YES\'] OR [\'NO\'] to the binary questions!')
print('==x==' * 8)

content = list()


character_number = int(input('Character Nº: '))
if character_number <= 0:
    print('Please type a valid number!')
    character_number = int(input('Character Nº: '))

only_numbers = PasswordMaker.to_bool(str(input('Only Numbers? ')).strip().upper()[0])

if only_numbers:
    content.append(PasswordMaker.CharacterType.NUMBER)
else:
    if PasswordMaker.to_bool(str(input('With Uppercase? ')).strip().upper()[0]):
        content.append(PasswordMaker.CharacterType.UPPERCASE)
    if PasswordMaker.to_bool(str(input('With Lowercase? ')).strip().upper()[0]):
        content.append(PasswordMaker.CharacterType.LOWERCASE)
    if PasswordMaker.to_bool(str(input('With Numbers? ')).strip().upper()[0]):
        content.append(PasswordMaker.CharacterType.NUMBER)

password_maker = PasswordMaker()

print(f'\n{password_maker.create_password(character_number, content)}\n')

print('==x==' * 9)
print(' THANKS FOR USING THE PASSWORD M4KER')
print('==x==' * 9)
