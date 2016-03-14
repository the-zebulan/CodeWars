from re import compile, sub

REGEX = compile(r',+')


def dad_filter(strng):
    return sub(REGEX, ',', strng).rstrip(' ,')
