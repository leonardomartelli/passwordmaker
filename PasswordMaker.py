from typing import Type

import PasswordTools
from enum import Enum


class CharacterType(Enum):
    UPPERCASE = 0
    LOWERCASE = 1
    NUMBER = 2


class PasswordMaker:

    def __init__(self):
        self.content = list()
        self.character_number = Type[int]

    # creating password method

    def create_password(self):
        self.set_content()
        self.set_character_number()
        return ''.join(self.get_characters())

    # setting methods

    def set_content(self):
        if PasswordTools.ask_only_numbers():
            self.content.append(CharacterType.NUMBER)
        else:
            if PasswordTools.ask_uppercase():
                self.content.append(CharacterType.UPPERCASE)
            if PasswordTools.ask_lowercase():
                self.content.append(CharacterType.LOWERCASE)
            if PasswordTools.ask_number():
                self.content.append(CharacterType.NUMBER)

    def set_character_number(self):
        self.character_number = int(input('Character Nº: '))

    # getting methods

    def get_character(self):
        return self.switch(self.content[PasswordTools.get_position(len(self.content) - 1)])

    def get_characters(self):
        characters = []

        for c in range(0, self.character_number):
            characters.append(self.get_character())
        return characters

    # static methods

    @staticmethod
    def switch(argument):
        if argument is CharacterType.UPPERCASE:
            return PasswordTools.get_letter().upper()
        elif argument is CharacterType.LOWERCASE:
            return PasswordTools.get_letter()
        else:
            return PasswordTools.get_number()


password_maker = PasswordMaker()


print(password_maker.create_password())
