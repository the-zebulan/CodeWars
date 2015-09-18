from re import match


def validate_PIN(pin):
    """ validate_pin == PEP8, forced mixedCase by CodeWars """
    return bool(match(r'(\d{4}|\d{6})$', pin))

assert validate_PIN('') is False
assert validate_PIN('1') is False
assert validate_PIN('1234567') is False
assert validate_PIN('-1234') is False
assert validate_PIN('1111') is True
assert validate_PIN('123456') is True
