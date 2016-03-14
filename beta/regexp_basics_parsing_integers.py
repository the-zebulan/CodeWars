from re import compile, match

REGEX = compile(r'[+-]?(0(?P<base>[bxo]))?[\d\w]+\Z')


def to_integer(strng):
    try:
        return int(strng, 0 if match(REGEX, strng).group('base') else 10)
    except (AttributeError, KeyError, ValueError):
        pass
