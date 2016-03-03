from re import compile, search, I

REGEX = compile(r'hello|ciao|salut|hallo|hola|ahoj|czesc', I)


def validate_hello(greeting):
    return bool(search(REGEX, greeting))


assert validate_hello('hello') is True
assert validate_hello('ciao bella!') is True
assert validate_hello('salut') is True
assert validate_hello('hallo, salut') is True
assert validate_hello('hombre! Hola!') is True
assert validate_hello('Hallo, wie geht\'s dir?') is True
assert validate_hello('AHOJ!') is True
assert validate_hello('czesc') is True
assert validate_hello('meh') is False
assert validate_hello('Ahoj') is True
