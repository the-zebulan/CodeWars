import string  # forced import by CodeWars kata
from string import ascii_uppercase as up, ascii_lowercase as low, \
    ascii_letters as az, maketrans

ROT13 = maketrans(low[13:] + low[:13] + up[13:] + up[:13], az)


def rot13(message):
    return message.translate(ROT13)
