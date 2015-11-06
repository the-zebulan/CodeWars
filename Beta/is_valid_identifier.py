from re import compile, match

REGEX = compile(r'[a-zA-Z_$][\w$]*$')


def is_valid(idn):
    return bool(match(REGEX, idn))


assert is_valid("okay_ok1") is True
assert is_valid("$ok") is True
assert is_valid("___") is True
assert is_valid("str_STR") is True
assert is_valid("myIdentf") is True

assert is_valid("1ok0okay") is False
assert is_valid("!Ok") is False
assert is_valid("") is False
assert is_valid("str-str") is False
assert is_valid("no no") is False
