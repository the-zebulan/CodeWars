from re import compile, match

REGEX = compile(r'[+-]?(?:(?=\.?\d)\d*\.\d*|\d+)(?:[eE][+-]?\d+|\d+)?$')


def i_or_f(s):
    return bool(match(REGEX, s))


assert i_or_f('1') is True
assert i_or_f('1.0') is True
assert i_or_f('1e1') is True
assert i_or_f('1E-1') is True
assert i_or_f('1e+1') is True
