from re import compile, search, I

REGEX = compile(r'hello|ciao|salut|hallo|hola|ahoj|czesc', I)


def validate_hello(greeting):
    return bool(search(REGEX, greeting))
