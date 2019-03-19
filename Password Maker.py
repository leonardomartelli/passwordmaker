#Made by Leonardo Martelli Oliveira (leomartellio)
import string
import random
from random import randint

print('==x==' * 8)
print(' WELCOME TO PASSWORDM4KER')
print('==x==' * 8)

typeof = char = 0
charlist = list()
numchar = int(input('Character Nº: '))

if numchar <= 0:
    print('Please type a valid number!')
    numchar = int(input('Character Nº: '))

letterchoice = str(input('Only Numbers? ')).strip().upper()[0]
if letterchoice not in 'YN':
    print('Please type a valid answer, YES or NO.')
    letterchoice = str(input('Only Numbers? ')).strip().upper()[0]

if letterchoice == 'N':
    upperchar = str(input('With Uppercase? ')).strip().upper()[0]
    if upperchar not in 'YN':
        print('Please type a valid answer, YES or NO.')
        upperchar = str(input('With Uppercase? ')).strip().upper()[0]

    num = str(input('With Numbers? ')).strip().upper()[0]
    if num not in 'YN':
        print('Please type a valid answer, YES or NO.')
        num = str(input('With Numbers? ')).strip().upper()[0]

    if upperchar == 'Y':
        upperchar = True
    else:
        upperchar = False
    if num == 'Y':
        num = True
    else:
        num = False
    if upperchar is True and num is True:
        for c in range(0, numchar):
            typeof = randint(1, 3)

            if typeof == 1:
                char = random.choice(string.ascii_lowercase)
            elif typeof == 2:
                char = random.choice(string.ascii_uppercase)
            else:
                char = randint(0, 9).__str__()

            charlist.append(char)

    elif upperchar is True and num is False:
        for c in range(0, numchar):
            typeof = randint(1, 2)

            if typeof == 1:
                char = random.choice(string.ascii_lowercase)
            elif typeof == 2:
                char = random.choice(string.ascii_uppercase)
            charlist.append(char)

    elif upperchar is False and num is True:
        for c in range(0, numchar):
            typeof = randint(1, 2)

            if typeof == 1:
                char = random.choice(string.ascii_lowercase)
            elif typeof == 2:
                char = randint(0, 9).__str__()

            charlist.append(char)

    elif upperchar is False and num is False:
        for c in range(0, numchar):
            char = random.choice(string.ascii_lowercase)

            charlist.append(char)
else:
    for c in range(0,numchar):
        char = randint(0,9).__str__()
        charlist.append(char)

passw = ''.join(charlist)

print(passw)

print('==x==' * 9)
print(' THANKS FOR USING THE PASSWORDM4KER')
print('==x==' * 9)
