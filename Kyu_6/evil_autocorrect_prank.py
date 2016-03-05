from re import compile, sub

REGEX = compile(r'\b[yY][oO][uU]+\b|\b[uU]\b')


def autocorrect(string):
    return sub(REGEX, 'your sister', string)
