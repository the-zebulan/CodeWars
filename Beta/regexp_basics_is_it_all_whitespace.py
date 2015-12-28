from re import compile, match

REGEX = compile(r'\s*$')


def whitespace(string):
    return bool(match(REGEX, string))


assert whitespace("") is True
assert whitespace(" ") is True
assert whitespace("\n\r\n\r") is True
assert whitespace("a") is False
assert whitespace("w\n") is False
assert whitespace("\t") is True
assert whitespace(" a\n") is False
assert whitespace("\t \n\r\n  ") is True
assert whitespace("\n\r\n\r ") is True
assert whitespace("\n\r\n\r 3") is False
