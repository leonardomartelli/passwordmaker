import PasswordMethods

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

only_numbers = PasswordMethods.to_bool(str(input('Only Numbers? ')).strip().upper()[0])

if only_numbers:
    content.append(PasswordMethods.CharacterType.NUMBER)
else:
    if PasswordMethods.to_bool(str(input('With Uppercase? ')).strip().upper()[0]):
        content.append(PasswordMethods.CharacterType.UPPERCASE)
    if PasswordMethods.to_bool(str(input('With Lowercase? ')).strip().upper()[0]):
        content.append(PasswordMethods.CharacterType.LOWERCASE)
    if PasswordMethods.to_bool(str(input('With Numbers? ')).strip().upper()[0]):
        content.append(PasswordMethods.CharacterType.NUMBER)
    

print(f'\n{PasswordMethods.create_password(character_number, content)}\n')

print('==x==' * 9)
print(' THANKS FOR USING THE PASSWORD M4KER')
print('==x==' * 9)
