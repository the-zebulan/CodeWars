import re


def show_me(name):
    return bool(re.match(r'(-[A-Z][a-z]+)+$', '-' + name))
