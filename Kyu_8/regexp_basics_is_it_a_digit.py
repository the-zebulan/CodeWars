from re import compile, match

REGEX = compile(r'\d$')


def is_digit(n):
    m = match(REGEX, n)
    return bool(m) and n[slice(*m.span())] == n


assert is_digit("") is False
assert is_digit("7") is True
assert is_digit(" ") is False
assert is_digit("a") is False
assert is_digit("a5") is False
