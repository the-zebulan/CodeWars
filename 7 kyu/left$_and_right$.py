def left(string, i=1):
    return string[:string.index(i) if isinstance(i, str) else i]


def right(string, i=1):
    i = string[::-1].index(i[::-1]) if isinstance(i, str) else i
    return string[-i:] if not i == 0 else ""


text = 'Hello (not so) cruel World!'
assert left(text, 5) == 'Hello'
assert left(text, -22) == 'Hello'
assert left(text, 1) == 'H'
assert left(text) == 'H'
assert left(text, 0) == ''
assert left(text, 99) == 'Hello (not so) cruel World!'
assert right(text, 6) == 'World!'
assert right(text) == '!'
assert left(text, 'o') == 'Hell'
assert right(text, 'o') == 'rld!'
assert left(text, ' ') == 'Hello'
assert right("Don't Repeat Yourself", 'Repeat ') == 'Yourself'
