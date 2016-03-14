from re import compile, match

REGEX = compile(r'[a-zA-Z]\w*@[\w-]+(\.\w+)+$')


def validate(email):
    return bool(match(REGEX, email))
