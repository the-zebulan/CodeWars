def title_to_number(title):
    return sum((ord(a) - 64) * (26 ** i) for i, a in enumerate(title[::-1]))

assert title_to_number('A') == 1
assert title_to_number('Z') == 26
assert title_to_number('AA') == 27
assert title_to_number('AZ') == 52
assert title_to_number('BA') == 53
