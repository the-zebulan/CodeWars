from re import compile, match

REGEX = compile(r'[+-]?(?:(?=\.?\d)\d*\.\d*|\d+)(?:[eE][+-]?\d+|\d+)?$')


def i_or_f(s):
    return bool(match(REGEX, s))
