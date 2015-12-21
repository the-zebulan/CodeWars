def get_middle(s):
    q, r = divmod(len(s), 2)
    return s[q - (1 if not r else 0):q + 1]


assert get_middle('test') == 'es'
assert get_middle('testing') == 't'
assert get_middle('middle') == 'dd'
assert get_middle('A') == 'A'
assert get_middle('of') == 'of'
