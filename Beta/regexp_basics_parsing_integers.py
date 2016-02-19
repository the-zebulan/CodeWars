from re import compile, match

REGEX = compile(r'[+-]?(0(?P<base>[bxo]))?[\d\w]+\Z')


def to_integer(strng):
    try:
        return int(strng, 0 if match(REGEX, strng).group('base') else 10)
    except (AttributeError, KeyError, ValueError):
        pass


assert to_integer("123") == 123
assert to_integer("0x123") == 0x123
assert to_integer("0o123") == 0o123
assert to_integer("0123") == 123
assert to_integer("123 ") is None
assert to_integer(" 123") is None
assert to_integer("0b1010") == 0b1010
assert to_integer("+123") == 123
assert to_integer("-123") == -123
assert to_integer("0B1010") is None
assert to_integer("0b12") is None
assert to_integer("-0x123") == -0x123
assert to_integer("-0o123") == -0o123
assert to_integer("-0123") == -123
assert to_integer("123\n") is None
assert to_integer("\n123") is None
assert to_integer("-0b1010") == -0b1010
assert to_integer("0xDEADbeef") == 0xDEADBEEF
assert to_integer("0X123") is None
assert to_integer("0O123") is None
assert to_integer("0o18") is None
