import re

REGEX = re.compile(r'''
    ((?P<kebab>[a-z]+(-[a-z]+)+)|
     (?P<snake>[a-z]+(_[a-z]+)+)|
     (?P<camel>[a-z]+([A-Z][a-z]+)+))$''', re.VERBOSE)


def id(s):
    m = REGEX.match(s)
    if not m:
        return 'none'
    return next(k for k, v in m.groupdict().iteritems() if v is not None)

# Shadows built-in name 'id'
