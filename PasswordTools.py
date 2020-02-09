import string
import random


# getting methods

def get_letter():
    return random.choice(string.ascii_lowercase)


def get_number():
    return random.randint(0, 9).__str__()


def get_position(max_index):
    return random.randint(0, max_index)


# casting methods

def to_bool(answer):
    return answer is 'Y'


# asking methods

def ask_only_numbers():
    return to_bool(str(input('Only Numbers? ')).strip().upper()[0])


def ask_uppercase():
    return to_bool(str(input('With Uppercase? ')).strip().upper()[0])


def ask_lowercase():
    return to_bool(str(input('With Lowercase? ')).strip().upper()[0])


def ask_number():
    return to_bool(str(input('With Numbers? ')).strip().upper()[0])
