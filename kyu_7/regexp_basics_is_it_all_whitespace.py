from re import compile, match

REGEX = compile(r'\s*$')


def whitespace(string):
    return bool(match(REGEX, string))
