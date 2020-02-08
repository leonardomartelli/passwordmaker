import string
import random
from enum import Enum


class CharacterType(Enum):
    UPPERCASE = 0
    LOWERCASE = 1
    NUMBER = 2


def to_bool(answer):
    if answer == 'Y':
        return True
    return False


def get_character():
    return random.choice(string.ascii_lowercase)


def get_number():
    return random.randint(0, 9).__str__()


def switch(argument):
    if argument == CharacterType.UPPERCASE:
        return get_character().upper()
    elif argument == CharacterType.LOWERCASE:
        return get_character()
    else:
        return get_number()


def create_password(character_number, content=[]):
    characters = []

    for c in range(0, character_number):
        index = random.randint(0, len(content) - 1)
        argument = content[index]
        characters.append(switch(argument))

    return ''.join(characters)
