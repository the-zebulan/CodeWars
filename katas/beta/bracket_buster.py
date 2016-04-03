import re

REGEX = re.compile(r'\[(.*?)\]')


def bracket_buster(strng):
    try:
        return REGEX.findall(strng)
    except TypeError:
        return 'Take a seat on the bench.'
