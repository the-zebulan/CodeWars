from re import compile, finditer

REGEX = compile(r'(?P<chunk>[a-zA-Z]+)(?:_|-|$)')


def to_camel_case(text):
    result = []
    for i, a in enumerate(finditer(REGEX, text)):
        current = a.group('chunk')
        if not i and current[0].islower():
            result.append(current.lower())
        else:
            result.append(current.title())
    return ''.join(result)
