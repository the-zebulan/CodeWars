from re import compile, match

REGEX = compile(r'[a-zA-Z_$][\w$]*$')


def is_valid(idn):
    return bool(match(REGEX, idn))
