from itertools import izip


def step_through_with(s):
    for a, b in izip(s, s[1:]):
        if a == b:
            return True
    return False
