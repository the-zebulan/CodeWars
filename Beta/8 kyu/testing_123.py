def number(lines):
    return ['{}: {}'.format(i, a) for i, a in enumerate(lines, 1)]

assert number([]) == []
assert number(["a", "b", "c"]) == ["1: a", "2: b", "3: c"]
