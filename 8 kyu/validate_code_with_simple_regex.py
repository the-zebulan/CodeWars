def validate_code(code):
    return str(code).startswith(('1', '2', '3'))


assert validate_code(123) is True
assert validate_code(248) is True
assert validate_code(8) is False
assert validate_code(321) is True
assert validate_code(9453) is False
