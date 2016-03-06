from re import compile, match

REGEX = compile(r'MDZHB \d{2} \d{3} [A-Z]+ \d{2} \d{2} \d{2} \d{2}$')


def validate(message):
    return bool(match(REGEX, message))
