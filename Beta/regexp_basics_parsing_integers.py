from re import compile, match

BASES = {'b': 2, 'o': 8, None: 10, 'x': 16}
REGEX = compile(r'[+-]?(0(?P<base>[bxo]))?[\d\w]+$')


def to_integer(strng):
    m = match(REGEX, strng)
    if m and strng == strng[slice(*m.span())]:
        try:
            return int(strng, BASES[m.group('base')])
        except (KeyError, ValueError):
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
