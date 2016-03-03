from re import match


def validate_pin(pin):
    return bool(match(r'(\d{4}|\d{6})$', pin))

assert validate_pin('') is False
assert validate_pin('1') is False
assert validate_pin('1234567') is False
assert validate_pin('-1234') is False
assert validate_pin('1111') is True
assert validate_pin('123456') is True
