import re


def parser(strng):
    return re.split(r'[!#%&*+:;=>?|]', strng)
