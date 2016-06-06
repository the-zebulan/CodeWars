import re


def show_me(name):
    return bool(re.match(r'(-[A-Z][a-zA-Z]+)+$', '-' + name))
