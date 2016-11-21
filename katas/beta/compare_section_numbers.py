def to_tuple(s):
    return tuple(int(a) if a else 0 for a in s.rstrip('0.').split('.'))


def compare(s1, s2):
    a = to_tuple(s1)
    b = to_tuple(s2)
    return (a > b) - (a < b)
