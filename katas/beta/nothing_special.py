import re

REGEX = re.compile(r'[^a-zA-Z ]')


def nothing_special(s):
    try:
        return REGEX.sub('', s)
    except TypeError:
        return 'Not a string!'
