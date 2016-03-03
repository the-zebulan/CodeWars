from re import compile, findall

REGEX = compile(r'[A-Z]+(?=[A-Z][a-z]|$)|[A-Z][^A-Z]*')


def to_underscore(s):
    if not isinstance(s, str):
        return str(s)
    return '_'.join(a.lower() for a in findall(REGEX, s))


assert to_underscore('TestController') == 'test_controller'
assert to_underscore(5) == '5'
