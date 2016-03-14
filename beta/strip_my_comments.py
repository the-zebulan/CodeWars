from re import compile, sub, DOTALL

REGEX = compile(r'/\*.*?\*/|//[^\n]+', DOTALL)


def strip_it(code):
    return sub(REGEX, '', code)
