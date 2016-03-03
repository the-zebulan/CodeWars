from re import compile, match

REGEX = compile(r'(-[1-9]\d?|-1[0-1]\d|-12[0-8]|\d|[1-9]\d|1[0-1]\d|12[0-7])$')


def signed_eight_bit_number(number):
    m = match(REGEX, number)
    return bool(m) and m.group(0) == number


assert signed_eight_bit_number("") is False
assert signed_eight_bit_number("0") is True
assert signed_eight_bit_number("00") is False
assert signed_eight_bit_number("-0") is False
assert signed_eight_bit_number("55") is True
assert signed_eight_bit_number("-23") is True
assert signed_eight_bit_number("042") is False
assert signed_eight_bit_number("127") is True
assert signed_eight_bit_number("128") is False
assert signed_eight_bit_number("999") is False
assert signed_eight_bit_number("-128") is True
assert signed_eight_bit_number("-129") is False
assert signed_eight_bit_number("-999") is False
assert signed_eight_bit_number("1\n") is False
assert signed_eight_bit_number("1 ") is False
assert signed_eight_bit_number(" 1") is False
assert signed_eight_bit_number("1\n2") is False
assert signed_eight_bit_number("+1") is False
assert signed_eight_bit_number("--1") is False
assert signed_eight_bit_number("1\n") is False
assert signed_eight_bit_number("1 ") is False
assert signed_eight_bit_number(" 1") is False
assert signed_eight_bit_number("1\n2") is False
assert signed_eight_bit_number("+1") is False
assert signed_eight_bit_number("--1") is False
