from itertools import izip


def step_through_with(s):
    for a, b in izip(s, s[1:]):
        if a == b:
            return True
    return False


assert step_through_with("moon") is True
assert step_through_with("test") is False
assert step_through_with("glasses") is True
assert step_through_with("airplane") is False
assert step_through_with("free") is True
assert step_through_with("branch") is False
