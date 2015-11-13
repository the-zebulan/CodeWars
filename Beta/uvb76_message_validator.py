from re import compile, match

REGEX = compile(r'MDZHB \d{2} \d{3} [A-Z]+ \d{2} \d{2} \d{2} \d{2}')


def validate(message):
    return bool(match(REGEX, message))


assert validate("Is this a right message?") is False
assert validate("MDZHB 85 596 KLASA 81 00 02 91") is True
assert validate("MDZHB 12 733 EDINENIE 67 79 66 32") is True
assert validate("MDZHV 60 130 VATRUKH 58 89 54 54") is False
